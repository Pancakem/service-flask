from .. import db

from main.model.bike import Bike


def get_all_bikes():
    return Bike.query.all()


def get_a_bike(plate):
    return Bike.query.filter_by(bike_plate=plate)


def save_new_bike(data):
    bike = Bike.query.filter_by(bike_plate=data["type_id"])

    if not bike:
        new_bike = Bike(
            model=data["name"],
            engine_type=data["description"],
            barcode=data["barcode"],
            retail_price=data["price"],
            bike_plate=data["plate"]
        )
        save_changes(new_bike)

        return {"status": "success",
                "message": "Bike added to inventory"
                }, 200

    else:
        return {
            "status": "failure",
            "message": "There's a plate clash. Plate should be unique"
        }


def inventory_bike_size(barcode=None):
    if barcode is None:
        return len(Bike.query.all())
    else:
        return len(Bike.query.filter_by(barcode=barcode))


def save_changes(data):
    db.session.add(data)
    db.session.commit()
