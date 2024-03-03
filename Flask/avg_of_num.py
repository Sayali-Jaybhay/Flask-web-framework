from flask import Flask , render_template, request, url_for ,redirect

avg=Flask(__name__)


@avg.route('/')
def welcome():
    return render_template('index.html')

@avg.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        
        science=float(request.form['science'])
        c=float(request.form['c'])
        cpp=float(request.form['cpp'])
        dscience=float(request.form['dscience'])
        
  
    avg_score=(science+c+cpp+dscience)/4
    
    res=''

    if (avg_score>=40):
        res='pass1'
    else:
        res='fail'
        
    return redirect(url_for(res, score=avg_score))


@avg.route('/pass1/<int:score>')
def pass1(score):
    return "You are passed and the score is: "+str(score)

@avg.route('/fail/<int:score>')
def fail(score):
    return "You are failed and the score is: "+str(score)



if __name__==('__main__'):
    avg.run(debug=True)