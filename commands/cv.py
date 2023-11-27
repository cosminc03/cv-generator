import click
import json

from utils.data import (
    CV_PERSONAL_INFO,
    CV_EDUCATION,
    CV_EXPERIENCE,
    CV_RECOMMENDATIONS,
)

def register_commands(app):
    @app.cli.command("cv-personal-information", help="Get CV personal information")
    def get_personal():
        click.echo(json.dumps(CV_PERSONAL_INFO, indent=4))

    @app.cli.command("cv-education", help="Get CV education")
    def get_education():
        click.echo(json.dumps(CV_EDUCATION, indent=4))

    @app.cli.command("cv-experience", help="Get CV experience")
    def get_experience():
        click.echo(json.dumps(CV_EXPERIENCE))

    @app.cli.command("cv-recommendations", help="Get CV recommendations")
    def get_recommendations():
        click.echo(json.dumps(CV_RECOMMENDATIONS, indent=4))
