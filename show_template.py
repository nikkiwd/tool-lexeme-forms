import mwapi
import sys

# install: pip install prettyprinter
from prettyprinter import cpprint

import templates

def resolve_entity_ids():
    entity_ids = set()

    def add_from_statements(statements):
        for property_id, statement_group in statements.items():
            entity_ids.add(property_id)
            for statement in statement_group:
                entity_ids.add(statement['mainsnak']['datavalue']['value']['id'])

    for name in sys.argv[1:]:
        if name in templates.templates:
            template = templates.templates[name]
        else:
            print("couldn't find a template called " + name + " 🤷")
            continue

        if template.get('test', False):
            continue

        entity_ids.add(template['language_item_id'])
        entity_ids.add(template['lexical_category_item_id'])
        for form in template['forms']:
            entity_ids.update(form['grammatical_features_item_ids'])
            add_from_statements(form.get('statements', {}))
        add_from_statements(template.get('statements', {}))

    entity_ids = list(entity_ids)
    session = mwapi.Session('https://www.wikidata.org', user_agent='lexeme-forms test (https://lexeme-forms.toolforge.org/; mail@lucaswerkmeister.de)')
    labels = {}
    while entity_ids:
        chunk, entity_ids = entity_ids[:50], entity_ids[50:]
        result = session.get(action='wbgetentities',
                             ids=chunk,
                             redirects='no',
                             props='labels',
                             languages='en')
        for entity_id, entity in result['entities'].items():
            labels[entity_id] = entity['labels']['en']['value']

    def get_label(qid):
        if qid in labels:
            return labels[qid] + " (" + qid + ")"
        else:
            return qid

    def edit_statements(statements):
        for property_id, statement_group in statements.items():
            for statement in statement_group:
                statement['mainsnak']['property'] = get_label(statement['mainsnak']['property'])
                statement['mainsnak']['datavalue']['value']['id'] = get_label(statement['mainsnak']['datavalue']['value']['id'])

    for name in sys.argv[1:]:
        if name in templates.templates:
            template = templates.templates[name]
        else:
            continue

        if template.get('test', False):
            continue

        for key in ['language_item_id', 'lexical_category_item_id']:
            template[key] = get_label(template[key])
        for form in template['forms']:
            for i, feature in enumerate(form['grammatical_features_item_ids']):
                form['grammatical_features_item_ids'][i] = get_label(feature)
            edit_statements(form.get('statements', {}))
        edit_statements(template.get('statements', {}))

        cpprint(template)

if len(sys.argv) < 2:
    sys.exit("can't mindread 🙃 run me with the name of the templates you want to see as arguments")

resolve_entity_ids()
