import collections

templates = collections.OrderedDict([
    ('german-noun-masculine', {
        'label': 'Deutsches Substantiv (Maskulinum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist der [Hund].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum des [Hundes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört dem [Hund].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag den [Hund].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Hunde].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Hunde].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Hunden].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ plural',
                'example': 'Ich mag die [Hunde].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q499327',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('german-noun-feminine', {
        'label': 'Deutsches Substantiv (Femininum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist die [Katze].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum der [Katze].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört der [Katze].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag die [Katze].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Katzen].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Katzen].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Katzen].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ plural',
                'example': 'Ich mag die [Katzen].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775415',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('german-noun-neuter', {
        'label': 'Deutsches Substantiv (Neutrum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist das [Kind].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum des [Kindes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört dem [Kind].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag das [Kind].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Kinder].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Kinder].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Kindern].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ plural',
                'example': 'Ich mag die [Kinder].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775461',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('latin-noun-masculine', {
        'label': 'nomen Latinum (masculinum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puer].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [pueri].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [puero] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puella ad [puerum] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puella cum [puero] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [pueri].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puerorum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [pueris] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puella ad [pueros] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puella cum [pueris] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q499327',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('latin-noun-feminine', {
        'label': 'nomen Latinum (femininum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puella].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [puellae].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Mater [puellae] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [puellam] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [puella] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [puellae].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puellarum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Mater [puellis] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [puellas] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [puellis] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775415',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('latin-noun-neuter', {
        'label': 'nomen Latinum (neutrum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [forum].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [fori].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [foro] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [forum] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [foro] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [fora].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [fororum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [foris] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [fora] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [foris] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775461',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    ('german-noun-neuter-test', {
        'test': True,
        'label': 'Deutsches Substantiv (Neutrum), test.wikidata.org',
        'language_item_id': 'Q348',
        'language_code': 'de',
        'lexical_category_item_id': 'Q92595',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist das [Kind].',
                'grammatical_features_item_ids': ['Q163012', 'Q163014'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum des [Kindes].',
                'grammatical_features_item_ids': ['Q163013', 'Q163014'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört dem [Kind].',
                'grammatical_features_item_ids': ['Q163016', 'Q163014'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag das [Kind].',
                'grammatical_features_item_ids': ['Q163017', 'Q163014'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Kinder].',
                'grammatical_features_item_ids': ['Q163012', 'Q160570'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Kinder].',
                'grammatical_features_item_ids': ['Q163013', 'Q160570'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Kindern].',
                'grammatical_features_item_ids': ['Q163016', 'Q160570'],
            },
            {
                'label': 'Akkusativ plural',
                'example': 'Ich mag die [Kinder].',
                'grammatical_features_item_ids': ['Q163017', 'Q160570'],
            },
        ],
        'claims': {
            'P73601': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P73601',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q163008',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
])
