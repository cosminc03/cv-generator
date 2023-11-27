import json

from flask import (
    jsonify,
    request,
    Response
)
from utils.data import (
    CV_PERSONAL_INFO,
    CV_RECOMMENDATIONS,
    CV_EXPERIENCE,
    CV_EDUCATION,
)
from utils.filters import (
    EXPERIENCE_AVAILABLE_FILTERS,
    is_valid_experience,
)

def register_endpoints(app):
    @app.route("/personal", methods=["GET"])
    def personal():
        return jsonify(CV_PERSONAL_INFO)

    @app.route("/education", methods=["GET"])
    def education():
        return jsonify(CV_EDUCATION)

    @app.route("/experience", methods=["GET"])
    def experience():
        args = request.args
        filters = args.to_dict()

        if not set(filters.keys()).issubset(set(EXPERIENCE_AVAILABLE_FILTERS)):
            return Response(
                json.dumps({
                    "errors": [
                        "Invalid filter",
                    ],
                    "availableFilters": EXPERIENCE_AVAILABLE_FILTERS
                }),
                status=400,
                mimetype="application/json"
            )
        experiences = []

        try:
            for experience in CV_EXPERIENCE:
                if is_valid_experience(experience, filters):
                    experiences.append(experience)
        except ValueError as e:
            return Response(
                json.dumps({
                    "errors": [str(e)],
                }),
                status=400,
                mimetype="application/json"
            )

        return jsonify(experiences)

    @app.route("/recommendations", methods=["GET"])
    def recommendations():
        return jsonify(CV_RECOMMENDATIONS)
