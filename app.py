from flask import Flask,render_template,request
from model import image_to_text
import os


app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
	if request.method=='GET':
		return render_template('index.html')
	else:
		file=request.files['file']
		file.save(f'{file.filename}')
		res,res1,temp=image_to_text(file.filename)
		os.remove(f'{file.filename}')
		print(res,res1,temp)
		return render_template('result.html',res=res,res1=res1,temp=temp)



if __name__ == '__main__':
	app.run(debug=True)


