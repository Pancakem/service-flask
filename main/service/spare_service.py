from .. import db

from main.model.spares import Spare


def get_a_spare(barcode):
    return Spare.query.filter_by(barcode=barcode)


def new_spare(data): 
    spare = Spare.query.filter_by(barcode=data["barcode"])

    if not spare:
        new_spare = Spare(
                retail_price = data["price"],
            	part_name = data["name"],
	            part_type = data["type"],
    	        barcode = data["barcode"],
	            number_of = data["number"]
        )
        save_changes(new_spare)
    
        return {"status": "success", "message": "Added to inventory."}, 200

    else:
        try:
            spare.update().values(number_of=spare.number_of + data["number"])
            # add some logic here

            return {"status": "success", "message": "Inventory updated."}, 200
        except Exception as e:

            return {"status": "fail", "message": "Error: " + str(e)}, 409
    
def get_all_spares():
    return Spare.query.all()


def inventory_size(barcode):
    return len(Spare.query.filter_by(barcode=barcode))

def save_changes(data):
    db.session.add(data)
    db.session.commit()