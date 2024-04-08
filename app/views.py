"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, jsonify, send_file , flash
import os
from app.forms import MovieForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from app.models import Movie



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


# @app.route('/api/v1/movies', methods=['POST'])
# def movies():
#     form = MovieForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         title = form.title.data
#         description = form.description.data
#         upload = form.poster.data
#         filename = secure_filename(upload.filename)
#         upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         movie = {'title': title, 'description': description, 
#                  'poster': filename
#                  }
#         flash('Movie Successfully added!', 'success')
#         return jsonify({'message': 'Movie Successfully added', 'movie': movie}), 201
#     errors = form_errors(form)
#     return jsonify({'errors': errors}), 400



















@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm(request.form)

    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        if poster:
            filename = secure_filename(poster.filename)
            poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        movie = {'title': title, 'description': description, 'poster': filename}
        flash('Movie Successfully added!', 'success')
        return jsonify({'message': 'Movie Successfully added', 'movie': movie}), 201

    errors = form.errors
    return jsonify({'errors': errors}), 400














@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    # Query all movies from the database
    movies = Movie.query.all()

    # Convert the movies to a list of dictionaries
    movies_list = [{'id': movie.id, 'title': movie.title, 'description': movie.description, 'poster': movie.poster} for movie in movies]

    # Return the list of movies as JSON with status code 200 (OK)
    return jsonify(movies_list), 200



@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})

# @app.route('/upload', methods=['GET', 'POST'])
# @login_required
# def upload():
#     form = UploadForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         upload = form.upload.data
#         filename = secure_filename(upload.filename)
#         upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash('File uploaded successfully!', 'success')
#         return redirect(url_for('home'))
#     return render_template('upload.html', form=form)



###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404