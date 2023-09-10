from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        hundert_km = 100
        avg_consumption = float(request.form['avg_consumption'])
        people_traveling = int(request.form['people_traveling'])
        km_to_go = float(request.form['km_to_go'])
        price_liter = float(request.form['price_liter'])

        if people_traveling > 1:
            consumption_calc = avg_consumption * km_to_go / hundert_km * price_liter / people_traveling
        else:
            consumption_calc = avg_consumption * km_to_go / hundert_km * price_liter

        return render_template('index.html', avg_consumption=avg_consumption, people_traveling=people_traveling,
                               km_to_go=km_to_go, price_liter=price_liter, consumption_calc=consumption_calc)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
