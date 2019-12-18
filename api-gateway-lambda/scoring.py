class Calculator(object):

    def calculate(self,input):
        score = input.x * input.y
        print("Output from Scoring : " + str(score))
        return score

class DataInput(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate(self,input):
    return input.x * input.y

def lambda_handler(event, context):
    #message = 'Hel lo {} 0! '. format(event['first_name 'J,
    # event["last_name{])
    calculator = Calculator()
    data = DataInput(event['x'],event['y'])

    return {
        'Outcome' : calculator.calculate(data)

    }
#curl -X POST -d "{\"x\":6,\"y\":25}" https://q1pb7gq543.execute-api.us-east-1.amazonaws.com/prod/test-scoring-model
