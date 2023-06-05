import logging
import connexion
from flask import render_template

logging.basicConfig(level=logging.INFO)
app = connexion.FlaskApp(__name__, specification_dir='specs/')

app.template_folder = 'templates'
app.app.logger.info("Flask logger ready!")

app.add_api(
    'campus-laundry.yaml',
    arguments={'title': 'campus-laundry'}
)


@app.route("/")
def home():
    return render_template('home.html')


application = app.app

if __name__ == "__main__":
    app.run()
