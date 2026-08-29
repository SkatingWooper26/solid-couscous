from datetime import datetime


def get_formatted_date(date=None):
    if date == None:
        date = datetime.now()
    return date.strftime("%A, %B %d, %Y")



def main():
    choice = ""
    while choice not in ("yes", "no")
        choice = input("Do you want the date? (YES/NO): ").strip().lower()
        
    if choice == "yes":
        print(f"The date is: {get_formatted_date()}")


if __name__ == "__main__":
    main()