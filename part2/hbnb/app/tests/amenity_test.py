from app.models.amenity import Amenity

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")

def test_amenity_exception():
    try:
        amenity = Amenity(name="")
    except ValueError:
        print("Amenity name check test passed!")

test_amenity_creation()
test_amenity_exception()
