
"""
import redis
from flask import Flask
from flask.ext.socketio import SocketIO
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from config import REDIS_SERVER, REDIS_PORT, REDIS_DB
from utils import make_celery


app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

redis_db = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

socketio = SocketIO(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'sign_in'
login_manager.init_app(app)

celery = make_celery(app)

from . import views, websockets
from . import wizard_views
"""

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome UrbanSim Users!</h1>"

@app.route('/model/<int:forecast_year>/<int:seed>/<string:hh_controls>/<string:emp_controls>/<string:scenario_zoning>/<string:dev_projects>/<string:subarea_controls>/<string:skims>', methods=['GET'])
def simulate(forecast_year, seed, hh_controls, emp_controls, scenario_zoning, dev_projects, subarea_controls, skims):
    """
    Model endpoint for launching simulation.
    GET /model/:year/:seed/:hh_controls/:emp_controls/:scenario_zoning/:dev_projects/:subarea_controls

    Parameters
    ----------
    forecast_year : int
        Year to simulate to.
    seed : int
        Random seed.
    hh_controls : str
        Name of household control totals table.
    emp_controls : str
        Name of employment control totals table.
    scenario_zoning : str
        Name of zoning scenario.
    dev_projects : str
        Name of development projects scenario.
    subarea_controls : str
        Name of subarea controls (i.e. refinement settings).
    skims : str
        Name of skims table.
    Returns
    -------
    simulation_result : dict
        Status, and URL to zipfile of simulation results on S3.
    """
    result = 'FAKE'
    #result = run_simulation(forecast_year, hh_controls=hh_controls, emp_controls=emp_controls,
     #                       scenario_zoning=scenario_zoning, dev_projects=dev_projects,
      #                      subarea_controls=subarea_controls, skims=skims)
    return jsonify({'status':'Simulation complete', 'url':result})


#if __name__ == "__main__":
 #   app.run(host='0.0.0.0')
