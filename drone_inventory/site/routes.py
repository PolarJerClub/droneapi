from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from drone_inventory.forms import DroneForm
from drone_inventory.models import Drone, db
from drone_inventory.helpers import random_joke_generator


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('look at this shizzle muy nizzle')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    droneform = DroneForm()

    try:
        if request.method == 'POST' and droneform.validate_on_submit():
            name = droneform.name.data
            description = droneform.description.data
            price = droneform.price.data
            camera_quality = droneform.camera_quality.data
            flight_time = droneform.flight_time.data
            max_speed = droneform.max_speed.data
            dimensions = droneform.dimensions.data
            weight = droneform.weight.data
            cost_of_production = droneform.cost_of_production.data
            series = droneform.series.data
            if droneform.dad_joke.data:
                random_joke = droneform.dad_joke.data
            else:
                random_joke = random_joke_generator()
            user_token = current_user.token

            drone = Drone(name, description, price, camera_quality, flight_time, max_speed, 
                          dimensions, weight, cost_of_production, series, random_joke, user_token)
            
            db.session.add(drone)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Drone not created, please check your form and try again.')

    user_token = current_user.token
    drones = Drone.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=droneform, drones=drones)