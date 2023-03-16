from django.test import TestCase, Client
from django.urls import reverse
from factories import AddressFactory, LettingFactory


class LettingsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.address = AddressFactory()
        cls.letting = LettingFactory()

    def test_letting_index(self):
        title_name = "Lettings"
        response = self.client.get(reverse("lettings:index"))
        title = f"<title>{title_name}</title>"
        h1 = f"<h1>{title_name}</h1>"
        response_content = response.content.decode()
        assert response.status_code == 200
        assert title in response_content
        assert h1 in response_content

    def test_letting_page(self):
        response = self.client.get(
            reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        number = self.letting.address.number
        street = self.letting.address.street
        city = self.letting.address.city
        state = self.letting.address.state
        zip_code = self.letting.address.zip_code
        country_iso_code = self.letting.address.country_iso_code
        response_content = response.content.decode()
        title = f"<title>{self.letting}</title>"
        h1 = f"<h1>{self.letting}</h1>"
        address_number_and_street = f"<p>{number} {street}</p>"
        address_city_and_state_and_zipcode = f"<p>{city}, {state} {zip_code}</p>"
        address_country_iso_code = f"<p>{country_iso_code}</p>"
        assert response.status_code == 200
        assert title in response_content
        assert h1 in response_content
        assert address_number_and_street in response_content
        assert address_country_iso_code in response_content
        assert address_city_and_state_and_zipcode in response_content
