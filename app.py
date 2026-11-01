import json
print("Job Tracker Application")
print("Successfully")
try:
    with open("jobs.json", "r")as file:
        jobs = json.load(file)
except FileNotFoundError:
    jobs = []
while True:
    company = input("Enter company name: ")
    role = input("Enter job role: ")
    status = input("Enter application status: ")
    job = {
    "company" : company,
    "role" : role,
    "status" : status
}
    print(job)
    jobs.append(job)
    again = input("Add another job? (Y/n): ")
    if again.lower() == "n":
        break
with open("jobs.json", "w")as file:
        json.dump(jobs, file, indent=4)
print(jobs)


