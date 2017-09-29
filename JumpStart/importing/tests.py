from django.test  import TestCase
from importing.models import attendee
from django.db import models
# Create your tests here.
goodEmailTestCase = "Example@email.com"
goodEmailTestCase2 = ["Example@email.co.uk"]
goodEmailTestCase3 = ["Ex.ample@email.com"]
badEmailTestCase1 = [""]
badEmailTestCase2 = ["."]
badEmailTestCase3 = ["@gmail.com"]
badEmailTestCase4 = ["Broseph@"]

class email_objectTestCase(TestCase):
    print('touched')
    '''
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    attendee_email = models.EmailField
    '''

    def test_goodEmailTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email = 'example@gmail.com'
                                )
    def test_goodEmailTest2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email = goodEmailTestCase2
                                )
    def test_goodEmailTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email = goodEmailTestCase3
                                )
    def test_goodEmailTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email = 'asidmnoiasdiousandoiasj@isjdiasjom.com'
                                )
    def test_goodEmailTest5(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email = 'alex-J_.sk@isjdiasjom.com'
                                )

    def test_badEmailTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase1
                                )
        self.assertRaises(TypeError)

    def badEmailTestCase2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase1
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase1
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase1
                                )
        self.assertRaises(TypeError)

        def test_badEmailTest4(self):
            attendee.objects.create(first_name="name", last_name="fast",
                                    email=None
                                    )
            self.assertRaises(TypeError)


