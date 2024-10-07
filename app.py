from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="Enter QA pair")

@app.route("/", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        
        data = request.form
        print(f'question = {data["question"]}')
        print(f'answer = {data["answer-1"]}')
        print(f'answer_start1 = {data["start-point-answer-1"]}')
        print(f'answer_start2 = {data["start-point-answer-2"]}')
        print(f'answer_start3 = {data["start-point-answer-3"]}')
        
        return render_template("index.html", title="Saved QA pair | Enter another QA pair")
    else:
        return render_template("index.html", title="Enter QA pair")



if __name__ == '__main__':
    app.run(debug=True)