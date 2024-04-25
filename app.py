from flask import Flask,render_template,request,jsonify

app=Flask(__name__)
list_postman=[]


@app.route('/',methods=["GET","POST"])
def get_method():
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        Marks=request.form.get("Marks")
        Empty={}
        Empty['Name']=Name
        Empty['Age']=Age
        Empty['RollNo']=RollNo
        Empty['Marks']=Marks
        list_postman.append(Empty)
    return render_template("index.html",data=list_postman)

@app.route('/home',methods=["GET","POST"])
def home():
    list_postman.append(request.get_json())
    return list_postman

if __name__=="__main__":
    app.run(debug=True)



