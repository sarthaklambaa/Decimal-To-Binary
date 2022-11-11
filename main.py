from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["POST", "GET"])
def decib():
   # global empty_str
   empty_str =""
   
   if request.method =='POST':
      dec_num = int(request.form.get('dec')) #index.html waala name = aayega idhar
      list=[]
      while dec_num!=0:
         remainder = dec_num%2
         list.append(remainder)
         dec_num=dec_num//2

      for ans in list:
         new_str = str(ans)
         empty_str = new_str + empty_str

   
   return render_template("index.html", empty_str=empty_str)

 
if __name__=='__main__':
   app.run(debug=True)