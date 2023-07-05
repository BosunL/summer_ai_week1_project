class SocialNetwork:
    def __init__(self):
        self.list_of_people = []

    def save_social_media(self):
        import json
        data = [person.__dict__ for person in self.list_of_people]
        with open('social_media.json', 'w') as file:
            json.dump(data, file)

    def reload_social_media(self):
        import json
        with open('social_media.json', 'r') as file:
            data = json.load(file)
            self.list_of_people = [Person(person['id'], person['year']) for person in data]

    def create_account(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        person = Person(name, age)
        self.list_of_people.append(person)
        print(f"Account created for {name}")

    def get_person(self, person_id):
        for person in self.list_of_people:
            if person.id == person_id:
                return person
        return None


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.blocked_friends = []
        self.messages = []

    def add_friend(self, person_id):
        friend = SocialNetwork.get_person(person_id)
        if friend and friend not in self.friendlist:
            self.friendlist.append(friend)
            print(f"{person_id} added as a friend.")
        else:
            print("Failed to add friend.")

    def view_friends(self):
        print("Friends:")
        for friend in self.friendlist:
            print(friend.id)

    def block_friend(self, person_id):
        friend = SocialNetwork.get_person(person_id)
        if friend and friend in self.friendlist:
            self.friendlist.remove(friend)
            self.blocked_friends.append(friend)
            print(f"{person_id} has been blocked.")
        else:
            print("Failed to block friend.")

    def send_message(self, person_id, message):
        friend = SocialNetwork.get_person(person_id)
        if friend and friend in self.friendlist:
            friend.messages.append((self.id, message))
            print(f"Message sent to {person_id}.")
        else:
            print("Failed to send message.")

    def view_messages(self):
        print("Messages:")
        for sender, message in self.messages:
            print(f"From: {sender}\nMessage: {message}")
