from django.test import TestCase
import datetime
from django.db import models
from django.contrib.auth.models import User
from workshops.models import Workshop as workshop, session

# session test cases
'''NEED TO BE IMPLEMENTED BELOW'''
# 20 session_title tests
goodSessionTestCase1 = "Test Session"
goodSessionTestCase2 = "Test Session A"
goodSessionTestCase3 = "Test Session B"
goodSessionTestCase4 = "Test Session 1"
goodSessionTestCase5 = "Test Session 2"
goodSessionTestCase6 = "Test_Session"
goodSessionTestCase7 = "Test_Session:A"
goodSessionTestCase8 = "Test_Session:B"
goodSessionTestCase9 = "Test_Session#1"
goodSessionTestCase10 = "Test_Session#2"
goodSessionTestCase11 = "Test Session:A"
goodSessionTestCase12 = "Test Session:B"
goodSessionTestCase13 = "Test Session#1"
goodSessionTestCase14 = "Test Session#2"
goodSessionTestCase15 = "TEST SESSION"
badSessionTestCase1 = None
badSessionTestCase2 = ""
badSessionTestCase3 = "#"
badSessionTestCase4 = "5"
badSessionTestCase5 = "."
# session_date tests
# session_threshold tests

# 20 workshop test cases
'''NEED TO BE IMPLEMENTED BELOW'''
# 15 title tests
goodWorkshopTestCase1 = "Test Workshop"
goodWorkshopTestCase2 = "Test Workshop 2017"
goodWorkshopTestCase3 = "test workshop 2017"
goodWorkshopTestCase4 = "TestWorkshop2017"
goodWorkshopTestCase5 = "testWorkshop2017"
goodWorkshopTestCase6 = "Test_Workshop_2017"
goodWorkshopTestCase7 = "test_workshop_2017"
goodWorkshopTestCase8 = "TESTWORKSHOP"
goodWorkshopTestCase9 = "Test Workshop 2017 #1"
goodWorkshopTestCase10 = "Test Workshop #1"
badWorkshopTestCase1 = ""
badWorkshopTestCase2 = None
badWorkshopTestCase3 = "."
badWorkshopTestCase4 = "2017"
badWorkshopTestCase5 = "&"
# 5 owner tests
goodUserTestCase1 = "Admin"
goodUserTestCase2 = "kevin_admin"
badUserTestCase1 = ""
badUserTestCase2 = None
badUserTestCase3 = "#"


# pub_date tests


class sessionTestCase(TestCase):
    print('touched session tests')
    '''
    session_title = models.CharField(max_length=48,default="title")
    session_location = models.CharField(max_length=48,default="CS Main Lab")
    session_date = models.DateTimeField(default="1987-01-01 00:00")
    session_threshold = models.IntegerField(default= 1)
    workshop = models.ForeignKey(Workshop, default=1)
    registered_attendees = models.ManyToManyField(ImportingModels.attendee, default=None)
    '''

    def test_goodSessionTest1(self):
        session.objects.create(session_title=goodSessionTestCase1)

    def test_goodSessionTest2(self):
        session.objects.create(session_title=goodSessionTestCase2)

    def test_goodSessionTest3(self):
        session.objects.create(session_title=goodSessionTestCase3)

    def test_goodSessionTest4(self):
        session.objects.create(session_title=goodSessionTestCase4)

    def test_goodSessionTest5(self):
        session.objects.create(session_title=goodSessionTestCase5)

    def test_goodSessionTest6(self):
        session.objects.create(session_title=goodSessionTestCase6)

    def test_goodSessionTest7(self):
        session.objects.create(session_title=goodSessionTestCase7)

    def test_goodSessionTest8(self):
        session.objects.create(session_title=goodSessionTestCase8)

    def test_goodSessionTest9(self):
        session.objects.create(session_title=goodSessionTestCase9)

    def test_goodSessionTest10(self):
        session.objects.create(session_title=goodSessionTestCase10)

    def test_goodSessionTest11(self):
        session.objects.create(session_title=goodSessionTestCase11)

    def test_goodSessionTest12(self):
        session.objects.create(session_title=goodSessionTestCase12)

    def test_goodSessionTest13(self):
        session.objects.create(session_title=goodSessionTestCase13)

    def test_goodSessionTest14(self):
        session.objects.create(session_title=goodSessionTestCase14)

    def test_goodSessionTest15(self):
        session.objects.create(session_title=goodSessionTestCase15)
        self.assertRaises(TypeError)

    def test_badSessionTest1(self):
        session.objects.create(session_title=badSessionTestCase1)
        self.assertRaises(TypeError)

    def test_badSessionTest2(self):
        session.objects.create(session_title=badSessionTestCase2)
        self.assertRaises(TypeError)

    def test_badSessionTest3(self):
        session.objects.create(session_title=badSessionTestCase3)
        self.assertRaises(TypeError)

    def test_badSessionTest4(self):
        session.objects.create(session_title=badSessionTestCase4)
        self.assertRaises(TypeError)

    def test_badSessionTest5(self):
        session.objects.create(session_title=badSessionTestCase5)
        self.assertRaises(TypeError)


# Create your tests here.
class workshopTestCase(TestCase):
    print('touched workshop tests')
    '''
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    owner = models.ForeignKey(User, default="Admin")
    '''

    def test_goodWorkshopTest1(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)

    def test_goodWorkshopTest2(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase2)

    def test_goodWorkshopTest3(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase3)

    def test_goodWorkshopTest4(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase4)

    def test_goodWorkshopTest5(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase5)

    def test_goodWorkshopTest6(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase6)

    def test_goodWorkshopTest7(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase7)

    def test_goodWorkshopTest8(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase8)

    def test_goodWorkshopTest9(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase9)

    def test_goodWorkshopTest10(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase10)

    def test_goodWorkshopTest11(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)

    def test_goodWorkshopTest12(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase2)

    def test_goodWorkshopTest13(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase3)

    def test_goodWorkshopTest14(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase4)

    def test_goodWorkshopTest15(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase5)

    def test_goodWorkshopTest16(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase6)

    def test_goodWorkshopTest17(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase7)

    def test_goodWorkshopTest18(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase8)

    def test_goodWorkshopTest19(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase9)

    def test_goodWorkshopTest20(self):
        t_owner = User.objects.create_user(goodUserTestCase2, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase10)

    def test_badWorkshopTest1(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=badWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest2(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=badWorkshopTestCase2)
        self.assertRaises(TypeError)

    def test_badWorkshopTest3(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=badWorkshopTestCase3)
        self.assertRaises(TypeError)

    def test_badWorkshopTest4(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=badWorkshopTestCase4)
        self.assertRaises(TypeError)

    def test_badWorkshopTest5(self):
        t_owner = User.objects.create_user(goodUserTestCase1, "", "password")
        t_date = datetime.date.today()
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=badWorkshopTestCase5)
        self.assertRaises(TypeError)

    def test_badWorkshopTest6(self):
        t_owner = User.objects.create_user(badUserTestCase1, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest7(self):
        t_owner = User.objects.create_user(badUserTestCase1, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest8(self):
        t_owner = User.objects.create_user(badUserTestCase1, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest9(self):
        t_owner = User.objects.create_user(badUserTestCase1, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest10(self):
        t_owner = User.objects.create_user(badUserTestCase1, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest11(self):
        t_owner = User.objects.create_user(badUserTestCase2, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest12(self):
        t_owner = User.objects.create_user(badUserTestCase2, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest13(self):
        t_owner = User.objects.create_user(badUserTestCase2, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest14(self):
        t_owner = User.objects.create_user(badUserTestCase2, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest15(self):
        t_owner = User.objects.create_user(badUserTestCase2, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest16(self):
        t_owner = User.objects.create_user(badUserTestCase3, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest17(self):
        t_owner = User.objects.create_user(badUserTestCase3, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest18(self):
        t_owner = User.objects.create_user(badUserTestCase3, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest19(self):
        t_owner = User.objects.create_user(badUserTestCase3, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

    def test_badWorkshopTest20(self):
        t_owner = User.objects.create_user(badUserTestCase3, "", "password")
        t_date = datetime.date.today()
        self.assertRaises(ValueError)
        workshop.objects.create(owner=t_owner, pub_date=t_date, title=goodWorkshopTestCase1)
        self.assertRaises(TypeError)

from django.test import TestCase

# Create your tests here.
