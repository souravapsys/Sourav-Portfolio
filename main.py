from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [{
    'id':
    1,
    'title':
    "Automation Dept Portal",
    'description':
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries",
    'image':
    "https://a967d5bf-3ab6-47b7-81dc-e194bb9a0108-00-3kfd0appxhijx.pike.replit.dev/static/automdept.jpg"
}, {
    'id':
    2,
    'title':
    "Weather Monitoring System",
    'description':
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries",
    'image':
    "https://a967d5bf-3ab6-47b7-81dc-e194bb9a0108-00-3kfd0appxhijx.pike.replit.dev/static/weathermonitoring.jpg"
}, {
    'id': 3,
    'title': "APTMT",
    'description':
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries",
    'image':
    "https://a967d5bf-3ab6-47b7-81dc-e194bb9a0108-00-3kfd0appxhijx.pike.replit.dev/static/APTMT.jpg",
    'link': "https://apmosys.com/aptmt/"
}]


@app.route('/')
def index():
  return render_template('home.html',
                         projects=PROJECTS,
                         name="Sourabha Mohanty")


@app.route('/api/projects')
def projects():
  return jsonify(PROJECTS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
