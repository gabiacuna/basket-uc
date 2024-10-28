from django.test import TestCase
from django.urls import reverse
from .models import User, Records

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="test", email="jiji@gmail.com", rut="12345678-9", member_type="student", observation="")
        User.objects.create(name="test2", email="juju@gmail.com", rut="12345678-0", member_type="teacher", observation="")

    def test_user(self):
        user1 = User.objects.get(rut="12345678-9")
        user2 = User.objects.get(rut="12345678-0")
        self.assertEqual(user1.name, "test")
        self.assertEqual(user2.name, "test2")
        print("User test passed")
        # print(f"User1: {user1.name}\tUser1 RUT: {user1.rut}\nUser2: {user2.name}\tUser1 RUT: {user1.rut}")
        print(f'User1: \n\t{user1.name}\n\t{user1.email}\n\t{user1.rut}\n\t{user1.member_type}\n\t{user1.observation}')
        print(f'User2: \n\t{user2.name}\n\t{user2.email}\n\t{user2.rut}\n\t{user2.member_type}\n\t{user2.observation}')

class RecordsTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(name="test", email="jiji@gmail.com", rut="12345678-9", member_type="student", observation="")
        user2 = User.objects.create(name="test2", email="juju@gmail.com", rut="12345678-0", member_type="teacher", observation="")
        Records.objects.create(USER_ID=user1, status=1)
        Records.objects.create(USER_ID=user2, status=0)

    def test_records(self):
        record1 = Records.objects.get(status=1)
        record2 = Records.objects.get(status=0)
        self.assertEqual(record1.USER_ID.name, "test")
        self.assertEqual(record2.USER_ID.name, "test2")

        print("Records test passed")
        print(f'Record1: \n\t{record1.USER_ID.name}\n\t{record1.USER_ID.email}\n\t{record1.USER_ID.rut}\n\t{record1.USER_ID.member_type}\n\t{record1.USER_ID.observation}\n\t{record1.status}')
