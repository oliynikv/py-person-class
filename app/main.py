class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            current_person.wife = Person.people[person_dict["wife"]]
            current_person.wife.husband = current_person

    return result