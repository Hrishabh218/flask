from flask import Flask

FAI=Flask(__name__)

@FAI.route('/abc') 
def abc():

    return 'response taken successfully'

@FAI.route('/pqr') 
def pqr():

    return 'again response taken successfully'

if __name__=='__main__':
    FAI.run(debug=True)