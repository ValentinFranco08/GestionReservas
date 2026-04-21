import os
import unittest
from app import create_app, db
from app.models.booking_model import Room

class RoomModelTestCase(unittest.TestCase):
    def setUp(self):
        # Set environment variable to use in-memory db BEFORE create_app
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
        # Create app with test config
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_room_creation_with_equipment(self):
        room = Room(name="Sala de Prueba", capacity=10, equipment="Proyector, TV")
        db.session.add(room)
        db.session.commit()

        saved_room = Room.query.filter_by(name="Sala de Prueba").first()
        self.assertIsNotNone(saved_room)
        self.assertEqual(saved_room.capacity, 10)
        self.assertEqual(saved_room.equipment, "Proyector, TV")

    def test_room_creation_without_equipment(self):
        room = Room(name="Sala Vacía", capacity=5)
        db.session.add(room)
        db.session.commit()

        saved_room = Room.query.filter_by(name="Sala Vacía").first()
        self.assertIsNotNone(saved_room)
        self.assertIsNone(saved_room.equipment)

if __name__ == '__main__':
    unittest.main()
