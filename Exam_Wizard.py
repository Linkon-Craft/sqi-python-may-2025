questions = [
    {
        "question": "1. Explain the process of 'photosynthesis'. ",
        "ideal_answer1": ["photosynthesis","choroplast"],
        "ideal_answer2": ["light energy", "chemical energy", "chlorophyll", "carbon dioxide", "water", "glucose", "oxygen", "atp"],
    },
    {
        "question": "2. What is 'Money'. ",
        "ideal_answer1": ["money","goods", "exchange"],
        "ideal_answer2": ["medium", "people", "means", "value", "services", "account", "payment", "trade"],
    },
    {
        "question": "3. What is 'Reproduction'. ",
        "ideal_answer1": ["reproduction","biological", "living"],
        "ideal_answer2": ["organisms", "produced", "parent", "fundamental", "species"],
    }
]


def exam_wizard():
    score1 = 0
    score2 = 0
    for q in questions:
        print("\n" + q["question"] )
        user_answer = input("Enter your Answer: ").lower().split()
        for q["ideal_answer1"] in questions:
            if q["ideal_answer1"] in user_answer:
                score1 += 2
            else: 
                score1 = 0
        for q["ideal_answer2"] in questions:
            if q["ideal_answer2"] in user_answer: 
                score2 += 1
            else: 
                score2 = 0

        
    print(f"Examination completed You scored {score1 + score2}")



menu = """
1. Wizard Question
2. Exit

"""
print("Welcome 👋")
while True:
    print(menu)
    choice = input("Choose an option from the menu: ").strip()
    if choice == "2":
        print("Goodbye 👋")
        break

    if choice == "1":
        print(exam_wizard())






# Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. 
# It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of 
# carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.




# What is money?
# Money is a widely accepted medium of exchange that facilitates transactions for goods and services, 
# and for the repayment of debts. It serves as a store of value and a unit of account, enabling people to trade, 
# save, and measure the value of things. 



# Reproduction is a biological process where new living organisms (offspring) are produced from their parent(s). 
# It's a fundamental characteristic of all living things, ensuring the continuation of a species. 