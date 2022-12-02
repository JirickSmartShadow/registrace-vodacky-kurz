from flask import Flask, render_template, request, request, url_for, flash, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

prihlasky = list()

# test data
# prihlasky.append({'prezdivka': 'aa', 'kamarad': 'aa', 'plavec': True});
# prihlasky.append({'prezdivka': 'bb', 'kamarad': 'bb', 'plavec': False});
# prihlasky.append({'prezdivka': 'cc', 'kamarad': 'cc', 'plavec': True});

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', prihlasky=prihlasky), 200


@app.route('/registrace', methods=['GET', 'POST'])
def registrace():
    if request.method == 'POST':
        prezdivka = request.form['nick']
        kamarad = request.form['kanoe_kamarad']
        plavec = request.form['je_plavec']

        if not kamarad:
            prihlasky.append({'prezdivka': prezdivka, 'kamarad': '', 'plavec': plavec})
            return redirect(url_for('index'))
        else:
            prihlasky.append({'prezdivka': prezdivka, 'kamarad': kamarad, 'plavec': plavec})
            return redirect(url_for('index'))
    return render_template('registrace.html'), 200


@app.route('/vyrizene_registrace', methods=['GET'])
def vyrizene_registrace():
    return render_template('vyrizene_registrace.html', prihlasky=prihlasky), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
