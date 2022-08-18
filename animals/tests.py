from django.test import TestCase
from groups.models import Group
from traits.models import Trait

from animals.models import Animal

# Create your tests here.

class AnimalTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.animal_1_data ={
            "name": "Irina",
            "age": 4,
            "weight": 6,
        }

        cls.animal_2_data ={
            "name": "Madalena",
            "age": 3,
            "weight": 4,
            "sex": "Fêmea"
        }

        cls.group_1_data ={"name": "gato", "scientific_name": "felis catus"}

        cls.trait_1_data={"name": "pelo curto"}

        cls.trait_2_data={"name": "castrado"}

        cls.trait_3_data={"name": "peludo"}

        cls.group_1=Group.objects.create(**cls.group_1_data)

        cls.trait_1 = Trait.objects.create(**cls.trait_1_data)

        cls.trait_2 = Trait.objects.create(**cls.trait_2_data)

        cls.trait_3 = Trait.objects.create(**cls.trait_3_data)

        cls.animal_instance_1 = Animal(**cls.animal_1_data, group= cls.group_1)

        cls.animal_instance_1.save()

        cls.animal_instance_1.traits.add(cls.trait_1)

        cls.animal_instance_1.traits.add(cls.trait_2)

        
    def test_create_animal(self):
        self.animal_instance_2 = Animal(**self.animal_2_data, group= self.group_1)

        self.animal_instance_2.save()

        self.animal_instance_2.traits.add(self.trait_2)

        self.animal_instance_2.traits.add(self.trait_3)
        self.assertEqual(self.animal_instance_2.id , 2, "Id should equal 2 as the second animal in the database")
        print("test_create_animal  -  OK")
        
    def test_group_relation(self):

        self.assertEqual(self.animal_instance_1.group , self.group_1, "Verifying relation between instances animal and group failed")
        print("test_group_relation  -  OK")


    def test_trait_relation(self):

        trait_list = self.animal_instance_1.traits.all()

        self.assertEqual(trait_list[0] , self.trait_1, "Verifying relation between instances animal and group failed")
        print("test_trait_relation  -  OK")

    def test_sex_choice(self):

        self.assertEqual(self.animal_instance_1.sex ,"Não informado", "Defaul value should equal 'Não informado'")
        print("test_sex_choice  -  OK")
    ...
