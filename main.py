def kbc_game():
    questions = [
        ["Which planet is known as the 'Red Planet'?", "Mars", "Venus", "Mercury", "Jupiter", 1],
        ["Who wrote the Indian National Anthem 'Jana Gana Mana'?", "Bankim Chandra Chatarjee", "Rabindranath Tagore", "Vasco Da Gama", "Abraham Lincoln", 2],
        ["What is the currency of Japan?", "Yuan", "Dollar", "Yen", "Rupee", 3],
        ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
        ["What is the capital of Australia?", "New South Wales", "Brisbane", "Sydney", "Canberra", 4],
        ["How many players are there in a cricket team (on the field)?", 11, 13, 12, 9, 1],
        ["Who was the first woman Prime Minister of India?", "Sarojini Naidu", "Indira Gandhi", "Kiran Bedi", "Arundhati Roy", 2],
        ["Which is the smallest country in the World?", "Monaco", "Russia", "Vatican City", "Tuvalu", 3],
        ["In which year India got Independence?", 1950, 1951, 1952, 1947, 4],
        ["In which year did India become a republic?", 1947, 1953, 1950, 1952, 3],
        ["Who is the founder of 'Microsoft'?", "Steve Jobs", "Bill Gates", "Jeff Bezos", "Jenseng Huang", 2],
        ["Who is the richest person in the World?", "Elon Musk", "Bill Gates", "Warren Buffet", "Bernard Arnault", 1],
        ["Which is the largest country in the World?", "USA", "Canada", "India", "Russia", 4],
        ["Which Indian city is known as the 'Pink City'?", "Hyderabad", "Lucknow", "Jaipur", "Bangalore", 3],
        ["What is the chemical symbol for gold?", "Ag", "Hg", "Fe", "Au", 4]
    ]
    levels = [2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, "1 crore", "7 crore"]
    money = 0
    for i in range(len(questions)):
        print(f"\nQuestion for Rs. {levels[i]}")
        print(f"{i+1}. {questions[i][0]}")
        print(f"1. {questions[i][1]}            2. {questions[i][2]}")
        print(f"3. {questions[i][3]}            4. {questions[i][4]}")
        try:
            answer = int(input("Enter Answer(1, 2, 3, 4): "))
            if answer == questions[i][-1]:
                print(f"✅ Correct Answer! You have WON Rs. {levels[i]}")
                if i == 4:
                    money = 10000
                elif i == 9:
                    money = 320000
                elif i == 13:
                    money = 10000000
                elif i == 14:
                    money = 70000000
            else:
                print("❌ Wrong Answer!")
                break
        except ValueError:
            print("Please enter a valid number (1-4).")
            break
    if money == 70000000:
        print("\n🎉🎉🎉 7 Karrrooooooddddddddd!!! 🎉🎉🎉")
    print(f"\n💰 Your TakeHome Money is Rs. {money}")
if __name__ == "__main__":
    kbc_game()
