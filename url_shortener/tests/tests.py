from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from ..models import ShortURL
from ..views import generate_shortURL, redirect, home
from datetime import datetime



# try this link to help: https://www.youtube.com/watch?v=qfkFhcxd2XI&t=1903s&ab_channel=ArunRavindranArunRocks
#  or this: https://stackoverflow.com/questions/43501561/how-to-test-views-that-use-post-request-in-django

url = "https://www.linkedin.com/in/ilan-lieberman-9a1043132/"
time = datetime.now()

class TestURLShortener(TestCase):

    def setup(self):
        self.client = Client()
        ShortURL.objects.create(original_url=url, short_url='zqSkSQ', time_date_created=time, count=2)
        # Needed to create an object from my database becuase each test creates their own 'test database'

    # Test for creating a short URL
    def test_creating_short_URL_POST(self):
        """
        Test to create short Urls
        """
        short_url_from_db = []
        print(f'short_url_from_db : {short_url_from_db}')
        response = self.client.post(reverse('generate_shortURL'), data={'original_url': url})

        generated_short_url = response.context["chars"] #To get the shorten url as a result from the view


        self.assertEquals(generated_short_url, 'afasdf')




    # Test for redirecting a short URL to a long URL





    # Test for non-existing short URL

