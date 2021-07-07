from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import model


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    prices = "Awaiting entry"
    return render_template("index.html", prices=prices)
    
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        model_input = {"Year Built": request.form["Yearbuilt"],
                       "1stFlrSF" : request.form["1stFlrSF"],
                       "GrLivArea": request.form["GrLivArea"],
                       "LotArea": request.form["LotArea"],
                       "GarageArea": request.form["GarageArea"],
                       "BsmtUnfSF": request.form["BsmtUnfSF"],
                       "TotalBsmtSF": request.form["TotalBsmtSF"],
                       "LotFrontage": request.form["LotFrontage"],
                       "GarageYrBlt": request.form["GarageYrBlt"],
                       "MoSold": request.form["MoSold"]
            
            }
        predicted_price = model.run_model(model_input)
        return render_template("index.html", prices=predicted_price)
    
    return render_template("dummy.html")

    



if __name__ == "__main__":
    app.run()
