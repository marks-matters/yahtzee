from flask import Flask,render_template,request
import random
import pdb

app = Flask("Hello App")

@app.route("/",methods=["GET","POST"])
def index():
	dice = []

	for keep_die, die_value in request.form.items():
		print keep_die, die_value

	
	for i in range(1,6):
		if str(i) in request.form.keys():
			dice.append(request.form[str(i)])
		else:
			dice.append(random.randint(1,6))
	return render_template("index.html",dice=dice)


def calculate_score(dice, score):
	if score == 'ones':
		final_score = 0
		for d in dice:
			if d ==  1:
				final_score += 1

if __name__ == '__main__':
	app.run(debug = True)