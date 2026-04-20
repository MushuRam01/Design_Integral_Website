import json
import os

from flask import Flask, Response, abort, render_template, request, send_from_directory

app = Flask(__name__)
PROJECTS_PATH = os.path.join(app.root_path, 'data', 'projects.json')


def load_projects():
    try:
        with open(PROJECTS_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def build_categories(projects):
    categories = []
    seen = set()
    for project in projects:
        key = project.get('category_key')
        label = project.get('category_label')
        if key and label and key not in seen:
            categories.append({'key': key, 'label': label})
            seen.add(key)
    return categories

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    projects = load_projects()
    categories = build_categories(projects)
    return render_template('portfolio.html', projects=projects, categories=categories)


@app.route('/portfolio/<slug>')
def project_detail(slug):
    projects = load_projects()
    project = next((item for item in projects if item.get('slug') == slug), None)
    if project is None:
        abort(404)
    return render_template('project_detail.html', project=project)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        ('/', 'weekly', '1.0'),
        ('/services', 'monthly', '0.8'),
        ('/portfolio', 'monthly', '0.8'),
        ('/about_us', 'monthly', '0.7'),
        ('/contact', 'monthly', '0.6'),
    ]

    base_url = request.url_root.rstrip('/')
    urlset = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, changefreq, priority in pages:
        urlset.append('  <url>')
        urlset.append(f'    <loc>{base_url}{path}</loc>')
        urlset.append(f'    <changefreq>{changefreq}</changefreq>')
        urlset.append(f'    <priority>{priority}</priority>')
        urlset.append('  </url>')
    urlset.append('</urlset>')

    xml = '\n'.join(urlset)
    return Response(xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)