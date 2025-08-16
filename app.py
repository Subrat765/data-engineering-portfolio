from flask import Flask, render_template, request, jsonify
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects page route"""
    # This will be populated with actual project data
    projects_data = [
        {
            'title': 'Data Pipeline Project',
            'description': 'ETL pipeline using Apache Airflow and Python',
            'technologies': ['Python', 'Apache Airflow', 'PostgreSQL', 'Docker'],
            'link': '#'
        },
        {
            'title': 'Real-time Analytics Dashboard',
            'description': 'Streaming data analytics with Kafka and Spark',
            'technologies': ['Apache Kafka', 'Apache Spark', 'Python', 'React'],
            'link': '#'
        },
        {
            'title': 'Machine Learning Pipeline',
            'description': 'ML model training and deployment pipeline',
            'technologies': ['Python', 'Scikit-learn', 'MLflow', 'AWS'],
            'link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form submission"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # TODO: Implement email sending or database storage
        # For now, just return a success response
        return jsonify({'success': True, 'message': 'Thank you for your message!'})
    
    return jsonify({'success': False, 'message': 'Invalid request'})

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
