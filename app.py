from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/cal",methods=['GET'])
def calculater():
    operation=request.json["Operation"]
    number1=(request.json["Number1"])
    number2=(request.json["Number2"])
    num1=int(number1)
    num2=int(number2)
    if operation=="Add":
        result=num1+num2
    elif operation=="Multiply":
        result=num1*num2
    elif operation=="Division":
        result=num1/num2
    else:
        result=num1-num2
    return "The operation is {} and result is: {}".format(operation,result)
    
if __name__=="__main__":
    app.run(debug=True)

