from quart import jsonify, render_template


async def welcome():
    return await render_template("home.html")
__all__ = [
    "welcome"
]