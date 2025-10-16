from typing import List
from flask import Flask, request, Response
import json

app = Flask(__name__)

class request_data_model:
    input_expression: str = ""

class response_data_model:
    input_expression: str = ""
    debug_info: List[str] = []
    result: float = 0.0



def calculate(infix_string):
    # log
    print(":in main calculate")

    from src.postfix import infix_to_postfix
    from src.evaluate import evaluate_postfix

    # these are for standalone program main
    # infix_string = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'
    # 
    # read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")
    # 
    # if len(read_line) > 4:
    #     infix_string = read_line
    
    debug_lines = []
    debug_lines.append("postfixing this -> " + str(infix_string))
    postfix_expr = infix_to_postfix(infix_string)
    
    debug_lines.append("evaluating this -> " + str(postfix_expr))
    result = evaluate_postfix(postfix_expr)

    debug_lines.append("Result = " + str(result))
    return result, debug_lines

@app.route('/calculate', methods=['GET'])
def calculate_route():
    request_data = request_data_model()  
    request_data.input_expression = request.json.get('input_expression')
    if request_data.input_expression is None or len(request_data.input_expression) < 1:
        resp = Response("""{"error": "Bad Request - need json with 'input_expression' key"}""", status=400)
        resp.headers["Content-Type"] = "application/json"
        return resp
    response_data = response_data_model()
    response_data.input_expression = request_data.input_expression
    response_data.result, response_data.debug_info = calculate(request_data.input_expression)

    response = Response(json.dumps(response_data.__dict__), status=200)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/', methods=['GET'])
def root_route():
    # newObj = response_data_model()
    # newObj.input_expression = "3 - ( 3 * 3 - ( 8 / 4 ) )"
    # newObj.debug_info = "evaluating this -> 9 - 2"
    # newObj.result = 13.93
    # print(json.dumps(newObj.__dict__))

    return "hello"



if __name__ == '__main__' :
    # log
    # print(":in main main")
    # infix_string = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'
    
    # read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")
    
    # if len(read_line) > 4:
    #     infix_string = read_line
    # print(calculate(infix_string))
    app.run(host='0.0.0.0', port=5000, debug=True)
