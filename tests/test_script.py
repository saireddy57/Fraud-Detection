import unittest

from main import app
import os


class TestToPerform(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        print("self=-----------------------------------appppppppppppppppppppppppp",self.app,app)

    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        print("rres---------------------------------------------ponseeeeeeeeeeeeeeeeeeeeeeeee",response,self.app.get('/'))
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    print("_________________________________________________________name________________________________________________",unittest.main())
    unittest.main()
