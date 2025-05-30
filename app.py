"""Simple web app to display stored WEMIX blocks."""
from flask import Flask, render_template
from config import get_settings
from db import get_engine, get_session, Block

app = Flask(__name__)


@app.route("/")
def index():
    settings = get_settings()
    engine = get_engine(settings.db_path)
    session = get_session(engine)
    blocks = session.query(Block).order_by(Block.number.desc()).limit(20).all()
    return render_template("index.html", blocks=blocks)


if __name__ == "__main__":
    app.run(debug=True)
