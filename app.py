from flask import Flask, abort, redirect, render_template, request, url_for

from projects import PROJECTS, SKILL_GROUPS, get_next_project, get_project

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"


@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, skill_groups=SKILL_GROUPS)


@app.route("/project/<slug>")
def project(slug):
    proj = get_project(slug)
    if proj is None:
        abort(404)
    return render_template("project.html", project=proj, next_project=get_next_project(slug))


@app.route("/contact", methods=["POST"])
def contact():
    email = request.form.get("email", "").strip()
    info = request.form.get("info", "").strip()
    message = request.form.get("message", "").strip()

    status = "success" if email and message else "error"
    if status == "success":
        # Wire this up to a real mailer / forms API before going live.
        app.logger.info("Contact form submission — email=%s info=%s message=%s", email, info, message)

    return redirect(url_for("home", sent=status) + "#contact")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
