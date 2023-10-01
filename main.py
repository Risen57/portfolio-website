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
        "28-09-2023",
        "I3wm Customisation tips",
        "baseblog"
    ],
    [
        "28-09-2023",
        "arch tips",
        "baseblog"
    ],
    [
        "28-09-2023",
        "I3wm tips",
        "baseblog"
    ],
    [
        "28-09-2023",
        "I3wm Customisation tips",
        "baseblog"
    ],
    [
        "28-09-2023",
        "I3wm Customisation tips",
        "baseblog"
    ],
    [
        "09-09-2023",
        "I3wm Customisation tips",
        "baseblog"
    ]
]


@app.route("/")
def index():
    return render_template('index.html', projects=projects, blogs=blogs)


@app.route("/blog/baseblog")
def blogpage():
    return render_template("blogs/baseblog.html")


if __name__ == "__main__":
    app.run(debug=True)
