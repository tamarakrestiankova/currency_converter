import json

class JsonCreator:
    """Creates JSON format"""

    @staticmethod
    def finalOutput(input, output, amount):
        """Creates JSON formatted output"""

        finalStructure = {'input': {'amount': amount, 'currency': input}, 'output': output}
        return json.dumps(finalStructure, sort_keys=True)


    @staticmethod
    def jsonErrStructure(errorMessage, errorCode):
        """Creates JSON formattet error message"""

        errorStructure = {'error_code': errorCode, 'error_message': errorMessage}
        return json.dumps(errorStructure, sort_keys=True)

