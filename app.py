from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello"
@app.route("/calc",method=['GET'])
def calculater():
    operation=request.json["Operation"]
    num1=request.json["Number1"]
    num2=request.json["Number2"]
    if operation=="Add":
        result=num1+num2
        return result
    elif operation=="Multiply":
        result=num1*num2
        return result
    elif operation=="Division":
        result=num1/num2
        return result
    else:
        result=num1-num2
        return result

print("hello")
if __name__=="__main__":
    app.run(debug=True)

