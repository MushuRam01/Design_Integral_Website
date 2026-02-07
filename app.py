from flask import Flask, Response, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

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