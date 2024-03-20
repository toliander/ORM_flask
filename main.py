import random
from flask import Flask, render_template

app = Flask(__name__)


def cap():
    # Списки имен и фамилий для капитанов
    first_names = ["James", "John", "William", "Henry", "Christopher", "Thomas", "Richard", "Charles", "Daniel",
                   "Robert"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    # Генерация списка капитанов
    captains = []
    for _ in range(5):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        captain = f"{first_name} {last_name}"
        captains.append(captain)

    return captains


@app.route('/')
@app.route('/distribution')
def index():
    captains = cap()
    return render_template('index.html', captains=captains)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


