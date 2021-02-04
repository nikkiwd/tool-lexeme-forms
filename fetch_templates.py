import mwapi
import re
import sys

## install: pip install prettyprinter
from prettyprinter import cpprint

# install: pip install mwparserfromhell
import mwparserfromhell

import templates

def make_statement(prop, qid):
	st = [{
		'mainsnak': {
			'snaktype': 'value',
			'property': prop,
			'datatype': 'wikibase-item',
			'datavalue': {
				'type': 'wikibase-entityid',
				'value': {
					'entity-type': 'item',
					'id': qid,
				},
			},
		},
		'type': 'statement',
		'rank': 'normal',
	}]
	return st

def fetch_templates():
	template_names = sys.argv[1:]
	session = mwapi.Session('https://test.wikidata.org', user_agent='lexeme-forms test (https://lexeme-forms.toolforge.org/; mail@lucaswerkmeister.de)')
	while template_names:
		chunk, template_names = template_names[:50], template_names[50:]
		result = session.get(action='query',
							 prop='revisions',
							 rvprop='content',
							 rvslots='main',
							 titles=chunk)

		for template_name, page in result["query"]["pages"].items():
			output = dict()
			wikicode = mwparserfromhell.parse(page["revisions"][0]["slots"]["main"]["*"])
			t = wikicode.filter_templates()

			# TODO: Add users to attribution
			output["@attribution"] = dict(users=list(), title=page["title"])
			output["label"] = t[0].get("label").value.strip()
			output["language_item_id"] = t[0].get("langitem").value.strip()
			output["language_code"] = t[0].get("langcode").value.strip()
			output["lexical_category_item_id"] = t[0].get("lexcat").value.strip()

			output["forms"] = list()
			for template in t:
				if not template.name.strip() == "LF-form":
					continue
				form = dict()
				form["label"] = template.get("label").value.strip()
				form["example"] = template.get("example").value.strip()
				form["grammatical_features_item_ids"] = list()
				features = template.get("features").value.split(",")
				for feat in features:
					feat = re.sub("\{\{Q\|Q?([0-9]+)\}\}", r"Q\1", feat.strip())
					form["grammatical_features_item_ids"].append(feat)
				# TODO: Add form statements

				output["forms"].append(form)

			output["statements"] = dict()
			statements = t[0].get("statements").value.split(",")
			for st in statements:
				m = re.match("\{\{(?:St|Cl)\|\|(P[0-9]+)\|(Q[0-9]+)\}\}", st.strip())
				if m:
					# FIXME: This will presumably overwrite multiple statements for the same property
					output["statements"][m.group(1)] = make_statement(m.group(1), m.group(2))
				else:
					print("Failed to match "+st)

			cpprint(output)
			# TODO: Save template to file

	# TODO: Check that all the templates requested were found

if len(sys.argv) < 2:
	sys.exit("can't mindread 🙃 run me with the name of the templates you want to fetch as arguments")

fetch_templates()
