from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import engine, SessionLocal
from models import Base, Calculation
from calculator import calculate_real_size, MICROSCOPE_FACTORS

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
CORS(app)

Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    return render_template("index.html", microscopes=MICROSCOPE_FACTORS.keys())

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.form

    username = data.get("username")
    image_size = float(data.get("image_size"))
    microscope = data.get("microscope")
    unit = data.get("unit")

    result, breakdown = calculate_real_size(image_size, microscope, unit)

    db = SessionLocal()
    record = Calculation(
        username=username,
        image_size=image_size,
        real_size=result,
        unit=unit
    )
    db.add(record)
    db.commit()
    db.close()

    return jsonify({
        "result": result,
        "unit": unit,
        "breakdown": breakdown
    })

@app.route("/records", methods=["GET"])
def get_records():
    db = SessionLocal()
    records = db.query(Calculation).all()
    db.close()

    return jsonify([
        {
            "username": r.username,
            "image_size": r.image_size,
            "real_size": r.real_size,
            "unit": r.unit
        } for r in records
    ])

@app.route("/delete_all", methods=["DELETE"])
def delete_all():
    db = SessionLocal()
    db.query(Calculation).delete()
    db.commit()
    db.close()
    return jsonify({"message": "All records deleted"})

if __name__ == "__main__":
    app.run(debug=True)