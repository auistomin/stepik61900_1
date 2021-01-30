from flask import Flask, render_template, abort
import data
app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departures(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def render_tours(id):
    return render_template('tour.html')


@app.route('/data/')
def render_data():
    res = '<h1>Все туры:</h1>'
    for id, tour in data.tours.items():
        res += '<p>{}: <a href="/data/tours/{}/">{} {} {}* </a></p>'.format(
            tour['country'],
            str(id),
            tour['title'],
            tour['price'],
            tour['stars']
        )
    return res


@app.route('/data/departures/<departure>/')
def render_data_departures(departure):
    res = '<h1>Туры по направлению {}:</h1>'.format(data.departures[departure])
    for id, tour in data.tours.items():
        if tour['departure'] == departure:
            res += '<p>{}: <a href="/data/tours/{}/">{} {} {}* </a></p>'.format(
                tour['country'],
                str(id),
                tour['title'],
                tour['price'],
                tour['stars']
            )
    return res


@app.route('/data/tours/<id>/')
def render_data_tours(id):
    tour = data.tours[int(id)]
    res = '<h1>{}: {} {}:</h1>'.format(
        tour['country'],
        tour['title'],
        tour['price']
    )
    res += '<p>{} ночей</p>'.format(tour['nights'])
    res += '<p>Стоимость: {} Р</p>'.format(tour['price'])
    res += '<p>{}</p>'.format(tour['description'])
    return res


if __name__ == '__main__':
    app.run()