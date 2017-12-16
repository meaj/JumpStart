from django.test import TestCase
from django.test import Client
from importing.models import attendee, csv_file
from workshops.models import Workshop as workshop, session
from django.db import models

# session test cases
'''NEED TO BE IMPLEMENTED BELOW'''
#20 session_title tests
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
#session_date tests
#session_threshold tests


#20 workshop test cases
'''NEED TO BE IMPLEMENTED BELOW'''
#15 title tests
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
#5 owner tests
goodWorkshopTestCase11 = "Admin"
goodWorkshopTestCase12 = "kevin_admin"
badWorkshopTestCase6 = ""
badWorkshopTestCase7 = None
badWorkshopTestCase8 = "#"
#pub_date tests

# 20 email test cases
goodEmailTestCase = "Example@email.com"
goodEmailTestCase2 = ["Example@email.co.uk"]
goodEmailTestCase3 = ["Ex.ample@email.com"]
goodEmailTestCase4 = ['alex-J_.sk@isjdiasjom.com']
goodEmailTestCase5 = ['asidmnoiasdiousandoiasj@isjdiasjom.com']
badEmailTestCase1 = [""]
badEmailTestCase2 = ["."]
badEmailTestCase3 = ["@gmail.com"]
badEmailTestCase4 = ["Broseph@"]
badEmailTestCase5 = None
badEmailTestCase6 = "..."
badEmailTestCase7 = "brosephgmail.com"
badEmailTestCase8 = ".@."
badEmailTestCase9 = "broseph@gmail"
badEmailTestCase10 = "broseph@@gmail.com"
badEmailTestCase11 = "brosephgmail@com"
badEmailTestCase12 = "broseph@gmailcom"
badEmailTestCase13 = "broseph@com"
badEmailTestCase14 = "broseph"
badEmailTestCase15 = "#$!@gmail.com"

# 21 UTSA ID test cases
goodUtsaIdTestCase1 = "abc123"
goodUtsaIdTestCase2 = "abc124"
goodUtsaIdTestCase3 = "xyz900"
goodUtsaIdTestCase4 = "egd748"
goodUtsaIdTestCase5 = "ade092"
badUtsaIdTestCase1 = "123abc"
badUtsaIdTestCase2 = "1abc23"
badUtsaIdTestCase3 = ""
badUtsaIdTestCase4 = "1a2b3c"
badUtsaIdTestCase5 = "123456"
badUtsaIdTestCase6 = "abcdef"
badUtsaIdTestCase7 = "abc1234"
badUtsaIdTestCase8 = "abcd12"
badUtsaIdTestCase9 = "ab1234"
badUtsaIdTestCase10 = "......"
badUtsaIdTestCase11 = "...123"
badUtsaIdTestCase12 = "abc..."
badUtsaIdTestCase13 = "abc12"
badUtsaIdTestCase14 = "ab123"
badUtsaIdTestCase15 = "ab23"
badUtsaIdTestCase16 = None

# 20 csv file test cases
goodCSVTestCase1 = "test.csv"
goodCSVTestCase2 = "test123.csv"
goodCSVTestCase3 = "test.weird.csv"
goodCSVTestCase4 = "another-odd.csv"
goodCSVTestCase5 = "last_good1.csv"
badCSVTestCase1 = "b*d.csv"
badCSVTestCase2 = "test.csb"
badCSVTestCase3 = "test.xlm"
badCSVTestCase4 = "%test.csv%"
badCSVTestCase5 = "te#st.csv"
badCSVTestCase6 = "no\good/name.csv"
badCSVTestCase7 = "test.cv"
badCSVTestCase8 = "test.cvs"
badCSVTestCase9 = "test[].csv"
badCSVTestCase10 = "testcsv"
badCSVTestCase11 = "test"
badCSVTestCase12 = ".csv"
badCSVTestCase13 = "test=csv"
badCSVTestCase14 = "test,csv"
badCSVTestCase15 = None

'''
class workshopTestCase(TestCase):
    print('touched workshop tests')
    '''
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    owner = models.ForeignKey(User, default="Admin")
    '''

    def test_goodWorkshopTest1(self):
'''
            

class csv_objectTestCase(TestCase):
    print('touched csv tests')
    '''
    description = models.CharField(max_length=46, blank=True)
    document = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    '''

    def test_goodCSVTest1(self):
        csv_file.objects.create(description="test",
                                document=goodCSVTestCase1
                                )

    def test_goodCSVTest2(self):
        csv_file.objects.create(description="test",
                                document=goodCSVTestCase2
                                )

    def test_goodCSVTest3(self):
        csv_file.objects.create(description="test",
                                document=goodCSVTestCase3
                                )

    def test_goodCSVTest4(self):
        csv_file.objects.create(description="test",
                                document=goodCSVTestCase4
                                )

    def test_goodCSVTest5(self):
        csv_file.objects.create(description="test",
                                document=goodCSVTestCase5
                                )

    def test_badCSVTest1(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase1
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest2(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase2
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest3(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase3
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest4(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase4
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest5(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase5
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest6(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase6
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest7(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase7
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest8(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase8
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest9(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase9
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest10(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase10
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest11(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase11
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest12(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase12
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest13(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase13
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest14(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase14
                                )
        self.assertRaises(TypeError)

    def test_badCSVTest15(self):
        csv_file.objects.create(description="test",
                                document=badCSVTestCase15
                                )
        self.assertRaises(TypeError)


class utsaId_objectTestCase(TestCase):
    print('touched UTSA ID tests')
    '''
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    utsa_id = models.CharField(max_length=6)
    '''

    def test_goodUtsaIdTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=goodUtsaIdTestCase1
                                )

    def test_goodUtsaIdTest2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=goodUtsaIdTestCase2
                                )

    def test_goodUtsaIdTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=goodUtsaIdTestCase3
                                )

    def test_goodUtsaIdTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=goodUtsaIdTestCase4
                                )

    def test_goodUtsaIdTest5(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=goodUtsaIdTestCase5
                                )

    def test_badUtsaIdTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase1
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase2
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase3
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase4
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest5(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase5
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest6(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase6
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest7(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase7
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest8(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase8
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest9(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase9
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest10(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase10
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest11(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase11
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest12(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase12
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest13(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase13
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest14(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase14
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest15(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase15
                                )
        self.assertRaises(TypeError)

    def test_badUtsaIdTest16(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                utsa_id=badUtsaIdTestCase16
                                )
        self.assertRaises(TypeError)


class email_objectTestCase(TestCase):
    print('touched email tests')
    '''
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    attendee_email = models.EmailField
    '''

    def test_goodEmailTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email='example@gmail.com'
                                )

    def test_goodEmailTest2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=goodEmailTestCase2
                                )

    def test_goodEmailTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=goodEmailTestCase3
                                )

    def test_goodEmailTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=goodEmailTestCase4
                                )

    def test_goodEmailTest5(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=goodEmailTestCase5
                                )

    def test_badEmailTest1(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase1
                                )
        self.assertRaises(TypeError)

    def test_badEmailTestCase2(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase2
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest3(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase3
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest4(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase4
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest5(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase5
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest6(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase6
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest7(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase7
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest8(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase8
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest9(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase9
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest10(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase10
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest11(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase11
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest12(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase12
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest13(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase13
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest14(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase14
                                )
        self.assertRaises(TypeError)

    def test_badEmailTest15(self):
        attendee.objects.create(first_name="name", last_name="fast",
                                email=badEmailTestCase15
                                )
        self.assertRaises(TypeError)

#Checks basic url paths that do not rely on incoming dynamic data.
#checks paths for main url paths and app url paths
class urlTestCollect(TestCase):
    def basic_url_test(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        response.status_code
        200
        response = c.get('/customer/details/')
        # response.content
        self.assertEqual(response.status_code, 404)

    def basic_url_test2(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        response.status_code
        200
        response = c.get('/')
        # response.content
        print(response)
        self.assertEqual(response.status_code, 302)

    def basic_url_test3(self):
        c = Client()
        response = c.post('/login/', {'username': 'daniel', 'password': 'danielpassword'})
        response.status_code
        200
        response = c.get('/')
        print(response)
        self.assertRedirects(response, '/accounts/login/?next=/')

    def basic_url_test4(self):
        c = Client()
        response = c.post('/login/', {'username': 'daniel', 'password': 'danielpassword'})
        response.status_code
        200
        response = c.get('http://localhost:8000/workshops/create/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def basic_url_test5(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code
        200
        response = c.get('http://localhost:8000/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def basic_url_test6(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code
        200
        response = c.get('http://localhost:8000/survey')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test7(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code
        200
        response = c.get('http://localhost:8000/workshops/')
        print(response)
        self.assertEqual(response.status_code, 302)

    #should fail as there is no survey setup
    def basic_url_test8(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code
        200
        response = c.get('http://localhost:8000/survey/make/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test9(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code
        200
        response = c.get('http://localhost:8000/survey/make/1')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test10(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/survey/1')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test11(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/survey/0/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test12(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/create')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test13(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/create/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test14(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/temporary/thanks/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def basic_url_test15(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/temporary/thanks')
        print(response)
        self.assertEqual(response.status_code, 200)

    def basic_url_test16(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/thanks')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test17(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/login/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def basic_url_test18(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/logout/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def basic_url_test19(self):
        c = Client()
        response = c.post('/admin/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/admin/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def basic_url_test20(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/splash/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test21(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/create/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test22(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test23(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/index/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def basic_url_test24(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/csv_upload/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def basic_url_test25(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/email_template/')
        print(response)
        self.assertEqual(response.status_code, 302)
