
def decidePerson():
        age_of_person = int(input("Enter age of Person"))
        if age_of_person < 18:
            print("Person is minor")
        elif age_of_person >= 60 and age_of_person > 18:
            print("Person is adult")
        else:
            print("Person is senior citizen")   
def main():
    decidePerson()

    if __name__ =="__main__":
        main()
        