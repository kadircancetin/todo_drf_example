import factory
from factory.faker import faker

FAKE = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"

    username = factory.LazyAttributeSequence(lambda o, n: "user_{}".format(n))
    first_name = factory.LazyAttribute(lambda obj: f"{obj.username}_first_name")
    last_name = factory.LazyAttribute(lambda obj: f"{obj.username}_last_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@{FAKE.free_email_domain()}")
    password = factory.PostGenerationMethodCall("set_password", FAKE.password())
    is_staff = False
