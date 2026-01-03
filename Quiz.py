score = 0

print("🧩 Welcome to the Ultimate Quiz Challenge!")
print("Answer the questions below and see how smart you are!\n")

# ===== Geography =====
print("🌍 Geography Questions")
q1 = input("1️⃣ What is the capital of Rwanda? ")
if q1.lower() == "kigali":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Kigali.")

q2 = input("2️⃣ Which is the largest continent by area? ")
if q2.lower() == "asia":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Asia.")

q3 = input("3️⃣ Which ocean is the deepest in the world? ")
if q3.lower() == "pacific":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's the Pacific Ocean.")

# ===== Science =====
print("\n🔬 Science Questions")
q4 = input("4️⃣ What gas do humans need to breathe? ")
if q4.lower() == "oxygen":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Oxygen.")

q5 = input("5️⃣ What planet is known as the Red Planet? ")
if q5.lower() == "mars":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Mars.")

q6 = input("6️⃣ How many bones are in the human body? ")
if q6 == "206":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's 206.")

q7 = input("7️⃣ What is H2O commonly known as? ")
if q7.lower() in ["water"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Water.")

# ===== Math =====
print("\n➗ Math Questions")
q8 = input("8️⃣ What is 9 x 8? ")
if q8 == "72":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's 72.")

q9 = input("9️⃣ What is the square root of 144? ")
if q9 == "12":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's 12.")

q10 = input("🔟 What is 15 + 28? ")
if q10 == "43":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's 43.")

# ===== Literature =====
print("\n📚 Literature Questions")
q11 = input("11️⃣ Who wrote 'Harry Potter'? ")
if q11.lower() in ["jk rowling", "j.k. rowling"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's J.K. Rowling.")

q12 = input("12️⃣ In 'The Chronicles of Narnia', what is the name of the lion? ")
if q12.lower() == "aslan":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Aslan.")

# ===== Fun Facts =====
print("\n🎉 Fun Fact Questions")
q13 = input("13️⃣ Which animal is known as the 'King of the Jungle'? ")
if q13.lower() == "lion":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Lion.")

q14 = input("14️⃣ What is the fastest land animal? ")
if q14.lower() == "cheetah":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Cheetah.")

q15 = input("15️⃣ Which fruit is known as the 'king of fruits'? ")
if q15.lower() == "durian":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Durian.")

# ===== Final Score =====
print(f"\n🏆 Your final score is {score}/15!")

if score == 15:
    print("🌟 Incredible! Perfect score!")
elif score >= 12:
    print("🎉 Amazing! You’re super smart!")
elif score >= 8:
    print("👍 Great job! Keep learning!")
else:
    print("🙂 Nice try! Study a bit more and you’ll ace it next time!")
