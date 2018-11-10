from django.test import TestCase

from VOD.apps.users import models

from django.utils.crypto import get_random_string


class UserTest(TestCase):
    def test_user_creation(self):
        username = get_random_string()
        email = get_random_string(length=5) + '@gmail.com'
        first_name = get_random_string()
        last_name = get_random_string()
        password = get_random_string()

        random_user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

        self.assertTrue(isinstance(random_user, models.User))
        self.assertEqual(str(random_user), username)

        self.assertFalse(random_user.is_admin)
        self.assertFalse(random_user.is_active)
        self.assertFalse(random_user.is_superuser)

    def test_super_user_creation(self):
        username = get_random_string()
        email = get_random_string(length=5) + '@gmail.com'
        first_name = get_random_string()
        last_name = get_random_string()
        password = get_random_string()

        random_super_user = models.User.objects.create_superuser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

        self.assertTrue(isinstance(random_super_user, models.User))
        self.assertEqual(str(random_super_user), username)
        self.assertTrue(random_super_user.is_admin)
        self.assertTrue(random_super_user.is_active)
        self.assertTrue(random_super_user.is_superuser)

    def test_get_full_name(self):
        username = get_random_string()
        email = get_random_string(length=5) + '@gmail.com'
        first_name = get_random_string()
        last_name = get_random_string()
        password = get_random_string()

        user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

        user_after = models.User.objects.get(username=username)
        self.assertEqual(user.get_full_name(), user_after.get_full_name())

    def test_get_short_name(self):
        username = get_random_string()
        email = get_random_string(length=5) + '@gmail.com'
        first_name = get_random_string()
        last_name = get_random_string()
        password = get_random_string()

        user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

        user_after = models.User.objects.get(username=username)
        self.assertEquals(user.get_short_name(), user_after.get_short_name())

    def test_is_staff(self):
        username = get_random_string()
        email = get_random_string(length=5) + '@gmail.com'
        first_name = get_random_string()
        last_name = get_random_string()
        password = get_random_string()

        user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

        user_after = models.User.objects.get(username=username)
        self.assertEquals(user.is_staff, user_after.is_staff)
