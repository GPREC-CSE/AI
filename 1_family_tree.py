class FamilyTree:
    def __init__(self):
        # Dictionary to hold family relationships
        # Format: {'person': {'parents': set(), 'children': set()}}
        self.family = {}

    def add_person(self, person):
        if person not in self.family:
            self.family[person] = {'parents': set(), 'children': set()}

    def add_relationship(self, parent, child):
        self.add_person(parent)
        self.add_person(child)

        self.family[parent]['children'].add(child)
        self.family[child]['parents'].add(parent)

    def get_parents(self, person):
        if person in self.family:
            return self.family[person]['parents']
        else:
            return None

    def get_children(self, person):
        if person in self.family:
            return self.family[person]['children']
        else:
            return None

    def get_siblings(self, person):
        if person not in self.family:
            return None

        siblings = set()
        parents = self.get_parents(person)
        if not parents:
            return siblings

        for parent in parents:
            siblings.update(self.family[parent]['children'])

        siblings.discard(person)
        return siblings

    def __str__(self):
        return str(self.family)

def main():
    tree = FamilyTree()

    while True:
        print("\nFamily Tree System")
        print("1. Add Relationship")
        print("2. Get Parents")
        print("3. Get Children")
        print("4. Get Siblings")
        print("5. Show Family Tree")
        print("6. Exit")
       
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            parent = input("Enter the parent's name: ")
            child = input("Enter the child's name: ")
            tree.add_relationship(parent, child)
            print(f"Added relationship: {parent} -> {child}")

        elif choice == '2':
            person = input("Enter the person's name to get parents: ")
            parents = tree.get_parents(person)
            if parents is None:
                print(f"{person} not found in the family tree.")
            else:
                print(f"Parents of {person}: {', '.join(parents) if parents else 'None'}")

        elif choice == '3':
            person = input("Enter the person's name to get children: ")
            children = tree.get_children(person)
            if children is None:
                print(f"{person} not found in the family tree.")
            else:
                print(f"Children of {person}: {', '.join(children) if children else 'None'}")

        elif choice == '4':
            person = input("Enter the person's name to get siblings: ")
            siblings = tree.get_siblings(person)
            if siblings is None:
                print(f"{person} not found in the family tree.")
            else:
                print(f"Siblings of {person}: {', '.join(siblings) if siblings else 'None'}")

        elif choice == '5':
            print("Current Family Tree:")
            print(tree)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()