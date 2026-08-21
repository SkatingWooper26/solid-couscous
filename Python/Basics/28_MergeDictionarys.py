

def combine_users(*users):
    return {
        f"user_{user_num}": user
        for user_num, user in enumerate(users, start=1)
    }

def ask_info(questions):
    answers = {}
    for question, data_type in questions.items():
        while True:
            try:
                answers[question] = data_type(
                    input(f"Enter your {question}: "))
                break
            except ValueError:
                print(f"Please enter a valid {question}")
    return answers
                
def main():
    question_list = {"name": str,
                     "age": int,
                     "city": str}
    user_1 = ask_info(question_list)
    print("Now for the next person")
    user_2 = ask_info(question_list)
    combined_dict = combine_users(user_1, user_2)
    print("The combined data is:")
    print(combined_dict)
    print("The separate data is:")
    for user in combined_dict.values():
        print(user)
    

if __name__ == "__main__":
    main()