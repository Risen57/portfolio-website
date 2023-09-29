from flask import Flask, render_template

app = Flask(__name__)

projects = [
    "yownloader",
    "theholygita",
    "Coverch",
    "Games",
    "Todo-app",
    "Notepad",
    "Wikipedia-searcher"
]

blogs = [
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ],
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ],
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ],
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ],
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ],
    [
        "28-09-2023 Friday",
        "I3wm Customisation tips",
        "blogs/baseblog.html"
    ]
]


@app.route("/")
def index():
    return render_template('index.html', projects=projects, blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
