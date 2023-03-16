from factory import django, SubFactory, Sequence, Faker
from django.contrib.auth.models import User
from profiles.models import Profile
from lettings.models import Letting, Address


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: f"username_{n}")
    first_name = Sequence(lambda n: f"first{n}")
    last_name = Sequence(lambda n: f"last{n}")
    email = Sequence(lambda n: f"{n}@example.com")


class ProfileFactory(django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = SubFactory(UserFactory)
    favorite_city = "city_test"


class AddressFactory(django.DjangoModelFactory):
    class Meta:
        model = Address

    number = Faker("random_int", min=1, max=9999)
    street = Sequence(lambda n: f"street{n}")
    city = Sequence(lambda n: f"city{n}")
    state = Faker("pystr", min_chars=2, max_chars=2)
    zip_code = Faker("random_int", min=1, max=9999)
    country_iso_code = Faker("pystr", min_chars=3, max_chars=3)


class LettingFactory(django.DjangoModelFactory):
    class Meta:
        model = Letting

    title = Sequence(lambda n: f"title_{n}")
    address = SubFactory(AddressFactory)
