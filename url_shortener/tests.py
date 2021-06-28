from django.test import TestCase, Client
from django.urls import reverse
from .models import ShortURL
from .views import generate_shortURL, redirect, home
from datetime import datetime


url = "https://www.linkedin.com/in/ilan-lieberman-9a1043132/"
time = datetime.now()

class TestURLShortener(TestCase):

    def setup(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.obj = ShortURL.objects.create(original_url=url, short_url='zqSkSQ', time_date_created=time, count=2)
        # Needed to create an object from my database becuase each test creates their own 'test database'



    # Test for creating a short URL that exist in the database
    def test_creating_short_URL_POST(self):
        """
        Test for creating a short URL and to see if it already exist in the database
        """
        short_url_from_db = ShortURL.objects.get(original_url=url).short_url # To get short url already from the database
        print(f'short_url_from_db : {short_url_from_db}')

        response = self.client.post(reverse('generate_shortURL'), data={'original_url': url})

        generated_short_url = response.context["chars"] #To get the shorten url as a result from the view
        print(f'generated_short_url: {generated_short_url}')

        self.assertEquals(generated_short_url, short_url_from_db)


    # Test for redirecting a short URL to a long URL
    def test_redirecting_shortURL_to_longURL(self, ):
        """
        Test for redirecting a short URL to a long URL
        """

        short_url_from_db = ShortURL.objects.get(original_url=url).short_url  # To get short url already from the database

        response = self.client.get(reverse("redirect", kwargs={"url": short_url_from_db})).context["obj"] #To get the end result from this view (the redirected url)
        print(f'RESPONSE FROM REDIRECT: {response}')

        self.assertEquals(str(response), url)


    # Test for non-existing short URL
    def test_for_non_existing_shortURL(self):
        """
        Test for non-existing short URL
        """

        random_short_url = 'FGHDSB'
        # A short url that is definitely not in the database

        response = self.client.get(reverse("redirect", kwargs={"url": random_short_url}))

        self.assertTemplateUsed(response, 'redirect.html')
        #This test should fail. It should lead to the 404page not the redirect page because the short url is non-existent


