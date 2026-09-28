# for loop range(start, end, step)

for i in range(5):
    print("OHID")

for i in range(5):
    print(i)

for i in range(0, 11, 2):
    print(i)

# Real-life example
emails = ["a@gmail.com", "b@gmail.com"]

for email in emails:
    print("Sent to Email", email)

# while loop

i = 3
while i < 6:
    print(i)
    i += 1

# Break
for i in range(10):
    if i == 6:
        break
    print(i)

# continue
for i in range(5):
    if i < 2:
        continue
    print(i)

# else with loops
for i in range(3):
    print(i)
print("Loop is complate.")

# nested loops
for i in range(3):
    for j in range(2):
        print(f"i = {i} , j = {j}")

# loop with string and list

for letter in "ohid":
    print(letter)

fruits_container = ["apple", "mango", "Orange", "pineapple"]

for fruit in fruits_container:
    print(fruit)

# loop with upper string

name = "ohid"

print(name.upper())

for name_letter in name:
    print(name_letter.upper())


# auto rename file
files = ["ohid.jpg", "salam.jpg", "naim.jpg"]

for i,f in enumerate(files):
    print(f"Renaming {f} to OA_{i}.jpg")

for i in range(len(files)):
    f = files[i]
    print(f"Renaming {f} to OA_{i}.jpg")


# Resume skill extractor (NLP Atomation)

skills = ["python", "rag", "ai", "nlp", "ml"]

resume = """
Mohammad Ohidul Alam
Full-Stack and AI/ML Engineer

I am a Full-Stack and AI/ML Engineer focused on building scalable web applications and intelligent systems. I have experience with Python, FastAPI, REST APIs, PostgreSQL, React, Node.js, and modern AI/ML technologies.

Technical Skills:
Python, FastAPI, REST API, PostgreSQL, React, Node.js, MongoDB, MySQL, PyTorch, YOLO, Scikit-learn, RAG, AI Agents, LangGraph, Tool Calling, Docker, MLflow, and GitHub Actions.

AI/ML:
Experience with machine learning, neural networks, NLP, transformer-based models, computer vision, retrieval-augmented generation, and AI agent development.

Software Engineering:
Strong foundation in Data Structures and Algorithms with an emphasis on writing efficient, maintainable, and production-ready code.

Career Interests:
Full-Stack Development, AI Engineering, Machine Learning Engineering, and Intelligent Application Development.
"""

for skill in skills:
    if skill in resume.lower():
        print(f"Matching Skill: {skill}")



# Auto Directory Creator

import os
folders = ["models", "redme", "main", "images/icons", "vector_database", "authentication"]
project_name = input("Enter the Project Name: ")

for folder in folders:
    path = os.path.join(project_name, folder)
    os.makedirs(path, exist_ok = True)
    print("Cereated the Project and Folders: {path}")