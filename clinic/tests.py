import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Owner, PetType, Pet, Specialty, Vet, Visit


class OwnerModelTest(TestCase):
    def test_owner_str(self):
        owner = Owner(first_name='John', last_name='Doe')
        self.assertEqual(str(owner), 'John Doe')

    def test_owner_creation(self):
        Owner.objects.create(
            first_name='Jane', last_name='Smith',
            address='123 Main St', city='Springfield', telephone='5551234567'
        )
        self.assertEqual(Owner.objects.count(), 1)


class PetTypeModelTest(TestCase):
    def test_pet_type_str(self):
        pt = PetType(name='Dog')
        self.assertEqual(str(pt), 'Dog')


class PetModelTest(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(
            first_name='Alice', last_name='Brown',
            address='5 Oak Ave', city='Shelbyville', telephone='5559876543'
        )
        self.pet_type = PetType.objects.create(name='Cat')

    def test_pet_str(self):
        pet = Pet.objects.create(
            name='Whiskers', birth_date=datetime.date(2020, 1, 1),
            pet_type=self.pet_type, owner=self.owner
        )
        self.assertEqual(str(pet), 'Whiskers (Alice Brown)')

    def test_pet_belongs_to_owner(self):
        pet = Pet.objects.create(
            name='Whiskers', birth_date=datetime.date(2020, 1, 1),
            pet_type=self.pet_type, owner=self.owner
        )
        self.assertEqual(pet.owner, self.owner)


class VetModelTest(TestCase):
    def test_vet_str(self):
        vet = Vet(first_name='Sarah', last_name='Connor')
        self.assertEqual(str(vet), 'Dr. Sarah Connor')

    def test_vet_with_specialty(self):
        specialty = Specialty.objects.create(name='Radiology')
        vet = Vet.objects.create(first_name='James', last_name='Wilson')
        vet.specialties.add(specialty)
        self.assertIn(specialty, vet.specialties.all())


class VisitModelTest(TestCase):
    def setUp(self):
        owner = Owner.objects.create(
            first_name='Bob', last_name='Jones',
            address='10 Elm St', city='Ogdenville', telephone='5550001111'
        )
        pet_type = PetType.objects.create(name='Dog')
        self.pet = Pet.objects.create(
            name='Rex', birth_date=datetime.date(2019, 6, 15),
            pet_type=pet_type, owner=owner
        )

    def test_visit_creation(self):
        visit = Visit.objects.create(
            visit_date=datetime.date.today(),
            description='Annual checkup',
            pet=self.pet
        )
        self.assertEqual(visit.pet, self.pet)
        self.assertEqual(Visit.objects.count(), 1)


class OwnerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_login(self.user)
        self.owner = Owner.objects.create(
            first_name='Bob', last_name='Jones',
            address='10 Elm St', city='Ogdenville', telephone='5550001111'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_owner_list_view(self):
        response = self.client.get(reverse('owner_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jones')

    def test_owner_search(self):
        response = self.client.get(reverse('owner_list'), {'q': 'Bob'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bob')

    def test_owner_search_no_result(self):
        response = self.client.get(reverse('owner_list'), {'q': 'ZZZZZZ'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Jones')

    def test_owner_detail_view(self):
        response = self.client.get(reverse('owner_detail', args=[self.owner.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bob')

    def test_owner_create_get(self):
        response = self.client.get(reverse('owner_create'))
        self.assertEqual(response.status_code, 200)

    def test_owner_create_post(self):
        response = self.client.post(reverse('owner_create'), {
            'first_name': 'New', 'last_name': 'Owner',
            'address': '1 Test St', 'city': 'Testville', 'telephone': '5550000000'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Owner.objects.count(), 2)

    def test_owner_edit(self):
        response = self.client.post(reverse('owner_edit', args=[self.owner.pk]), {
            'first_name': 'Updated', 'last_name': 'Jones',
            'address': '10 Elm St', 'city': 'Ogdenville', 'telephone': '5550001111'
        })
        self.assertEqual(response.status_code, 302)
        self.owner.refresh_from_db()
        self.assertEqual(self.owner.first_name, 'Updated')


class VetViewTest(TestCase):
    def test_vet_list_view(self):
        response = self.client.get(reverse('vet_list'))
        self.assertEqual(response.status_code, 200)
