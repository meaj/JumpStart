from django.test import TestCase
from django.test import Client


#Checks test_basic url paths that do not rely on incoming dynamic data.
#checks paths for main url paths and app url paths
class urlTestCollect(TestCase):
    def test_basic_url_test(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        response.status_code = 200
        response = c.get('/customer/details/')
        # response.content
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test2(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        response.status_code = 200
        response = c.get('/')
        # response.content
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_basic_url_test3(self):
        c = Client()
        response = c.post('/login/', {'username': 'daniel', 'password': 'danielpassword'})
        response.status_code = 200
        response = c.get('/')
        print(response)
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_basic_url_test4(self):
        c = Client()
        response = c.post('/login/', {'username': 'daniel', 'password': 'danielpassword'})
        response.status_code = 200
        response = c.get('http://localhost:8000/workshops/create/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_basic_url_test5(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code = 200
        response = c.get('http://localhost:8000/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_basic_url_test6(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code = 200
        response = c.get('http://localhost:8000/survey')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test7(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code = 200
        response = c.get('http://localhost:8000/workshops/')
        print(response)
        self.assertEqual(response.status_code, 302)

    #should fail as there is no survey setup
    def test_basic_url_test8(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code = 200
        response = c.get('http://localhost:8000/survey/make/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test9(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        response.status_code = 200
        response = c.get('http://localhost:8000/survey/make/1')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test10(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/survey/1')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test11(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/survey/0/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test12(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/create')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test13(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})

        200
        response = c.get('http://localhost:8000/create/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test14(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/temporary/thanks/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_basic_url_test15(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/temporary/thanks')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_basic_url_test16(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/thanks')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test17(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/login/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_basic_url_test18(self):
        c = Client()
        response = c.post('/login/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/logout/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_basic_url_test19(self):
        c = Client()
        response = c.post('/admin/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/admin/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_basic_url_test20(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/splash/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test21(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/create/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test22(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/accounts/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test23(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/index/')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_basic_url_test24(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/csv_upload/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_basic_url_test25(self):
        c = Client()
        response = c.post('/splash/', {'username': 'badaccount', 'password': 'bad'})
        200
        response = c.get('http://localhost:8000/email_template/')
        print(response)
        self.assertEqual(response.status_code, 302)