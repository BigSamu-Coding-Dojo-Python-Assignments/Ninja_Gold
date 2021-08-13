from flask import Flask, render_template, request, redirect, session
import random
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = 'akwrhgqu2oyyf8qefblbuywoebuy21e' # set a secret key for security 

@app.route('/')
# Create your views here.
def index():
    if "amountOfGold" not in session:
        session["amountOfGold"] = 0
    if "amountEarnedOrTaken[]" not in session:
        session["amountEarnedOrTaken[]"] = []
    if "earnOrTaken" not in session:
        session["earnOrTaken"] = ""
    if "timeStamp[]" not in session:
        session["timeStamp[]"] = []
    if "stateArray" not in session:
        session["stateArray"] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processMoney():
    if(request.method == "POST"):
        print("Amount of gold before arriving place:", session["amountOfGold"])
        
        #Farm selected
        if request.form["place"] == "farm":
            session["amountEarnedOrTaken[]"].append(int(random.random()*10) + 10)
            indexLastElementInArray = len(session["amountEarnedOrTaken[]"]) - 1
            moneyEarnedorTaken = session["amountEarnedOrTaken[]"][indexLastElementInArray]
            
            session["earnOrTaken"] = "Earn"
        
            session["timeStamp[]"].append(strftime("%b %d, %Y %H:%M %p", gmtime()))
            timeStamp = session["timeStamp[]"][indexLastElementInArray]
            session["stateArray"].append(f" Earned {moneyEarnedorTaken} golds from the farm! ({timeStamp})")
            session["amountOfGold"] += session["amountEarnedOrTaken[]"][indexLastElementInArray]
            
        #Cave selected
        if request.form["place"] == "cave":
            session["amountEarnedOrTaken[]"].append(int(random.random()*5) + 5)
            indexLastElementInArray = len(session["amountEarnedOrTaken[]"]) - 1
            moneyEarnedorTaken = session["amountEarnedOrTaken[]"][indexLastElementInArray]
            
            session["earnOrTaken"] = "Earn"

            session["timeStamp[]"].append(strftime("%b %d, %Y %H:%M %p", gmtime()))
            timeStamp = session["timeStamp[]"][indexLastElementInArray]
            session["stateArray"].append(f" Earned {moneyEarnedorTaken} golds from the cave! ({timeStamp})")
            
            session["amountOfGold"] += session["amountEarnedOrTaken[]"][indexLastElementInArray]
        
        #House selected
        if request.form["place"] == "house":
            session["amountEarnedOrTaken[]"].append(int(random.random()*2) + 3)
            indexLastElementInArray = len(session["amountEarnedOrTaken[]"]) - 1
            moneyEarnedorTaken = session["amountEarnedOrTaken[]"][indexLastElementInArray]

            session["earnOrTaken"] = "Earn"
            
            session["timeStamp[]"].append(strftime("%b %d, %Y %H:%M %p", gmtime()))
            timeStamp = session["timeStamp[]"][indexLastElementInArray]
            session["stateArray"].append(f" Earned {moneyEarnedorTaken} golds from the house! ({timeStamp})")

            session["amountOfGold"] += session["amountEarnedOrTaken[]"][indexLastElementInArray]
        
        #Casino selected
        if request.form["place"] == "casino":
            session["amountEarnedOrTaken[]"].append(int(random.uniform(-1,1)*50))
            indexLastElementInArray = len(session["amountEarnedOrTaken[]"]) - 1
            moneyEarnedorTaken = session["amountEarnedOrTaken[]"][indexLastElementInArray]
            
            session["timeStamp[]"].append(strftime("%b %d, %Y %H:%M %p", gmtime()))
            timeStamp = session["timeStamp[]"][indexLastElementInArray]

            if session["amountEarnedOrTaken[]"][indexLastElementInArray] >= 0:
                session["earnOrTaken"] = "Earn"
                session["stateArray"].append(f" Entered a casino a won {moneyEarnedorTaken} golds!!! Yeahhh!! ({timeStamp})")
            else:
                session["earnOrTaken"] = "Taken"
                session["stateArray"].append(f" Entered a casino a lost {moneyEarnedorTaken} golds... Ouch!! ({timeStamp})")
            
            session["amountOfGold"] += session["amountEarnedOrTaken[]"][indexLastElementInArray]
        
        print("Index:",indexLastElementInArray)
        print("Amount earned or taken:",session["amountEarnedOrTaken[]"])
        print("Earn or Taken:",session["earnOrTaken"])
        print("TimeStamp:",session["timeStamp[]"])
        print("State:",session["stateArray"][indexLastElementInArray])
        print("State Array:",session["stateArray"])
        
        
        print("Amount of gold after leaving place:", session["amountOfGold"])

        return redirect('/')
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)