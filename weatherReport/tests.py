import pytest
from .models import User 

class TestModels:
	def test_db_setup(cls, test_app):
		cls.users = User.query.all()
		assert len(cls.users) == 0