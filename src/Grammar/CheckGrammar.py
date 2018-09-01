import language_check
from Models.Grammar import Grammar
class CheckGrammar:

    def checkGrammar(self, message):
        tool = language_check.LanguageTool('es-ES')
        matches = tool.check(message)
        if (len(matches) == 0):
            return  None
        matchesResult = []
        for match in matches:
            grammarObject = Grammar(match.category, match.contextoffset, match.msg, match.replacements, match.errorlength)
            matchesResult.append(grammarObject)
        return matchesResult
