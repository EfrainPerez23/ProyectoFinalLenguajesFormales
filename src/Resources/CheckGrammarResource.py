from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from Models.Grammar import Grammar
from Grammar.CheckGrammar import CheckGrammar


class CheckGrammarResource(Resource):

    def post(self):
        data = BodyParser.bodyParser([
            {
                'key': 'paragraph',
                '_type': str,
                '_required': True,
                '_help': 'Paragraph cannot be blank!'
            },
        ])

        matches = CheckGrammar().checkGrammar(data['paragraph'])
        if (matches):
            return {'data': [match.json() for match in matches ]}

        return {'data': matches}



