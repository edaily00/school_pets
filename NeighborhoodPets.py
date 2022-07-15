import json


class DuplicateNameError(Exception):
    pass


class NeighborhoodPets:

    def __init__(self):

        self._all_pets = {}

    def add_pet(self, pet_name, species, owner):
        animal = Pet(pet_name, species, owner)
        if pet_name not in self._all_pets:
            self._all_pets[pet_name] = animal
        else:
            raise DuplicateNameError

    def delete_pet(self, pet_name):
        if pet_name in self._all_pets:
            del self._all_pets[pet_name]

    def get_owner(self, pet_name):
        return self._all_pets[pet_name].get_owner()

    def save_as_json(self, file_name):
        list_pets = []
        with open(file_name, 'w') as outfile:
            for pet in self._all_pets:
                list_pets.append(self._all_pets[pet].__dict__)
            json.dump(list_pets, outfile)

    def read_json(self, file_name):
        with open(file_name, 'r') as infile:
            pets = json.load(infile)

    def get_all_species(self):
        all_species = set()
        for pet in self._all_pets:
            all_species.add(self._all_pets[pet].get_species())
        return all_species



class Pet:

    def __init__(self, pet_name, species, owner):
        super().__init__()
        self._name = pet_name
        self._species = species
        self._owner = owner

    def get_pet_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_owner(self):
        return self._owner

"""
hood = NeighborhoodPets()

hood.add_pet("Ripley", "dog", "Eric")
hood.add_pet("Alice", "cat", "Jess")
hood.add_pet("Alice", "cat", "Jess")

hood.save_as_json("pets.json")

hood1 = NeighborhoodPets()
hood1.add_pet("sam", "shit", "lord")

hood1.read_json("pets.json")

print(hood.get_all_species())

"""