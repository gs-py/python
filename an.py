import json
import random

def load_jobs(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('jobs', {})
    except (FileNotFoundError, json.JSONDecodeError):
        print("FILE NOT FOUND OR INVALID JSON FORMAT!!!")
        return {}
    
def add(position, date, company, status):
    jobs = load_jobs()
    job_id = str(random.randint(100, 999))
    jobs[job_id] = {
        "company": company,
        "Position": position,
        "date": date,
        "status": status
    }
    write_to_file(jobs)
    print(f"\nSuccessfully Added\n\tCompany: {company}\n\tPosition: {position}\n\tDate: {date}\n\tStatus: {status}\n\tJob ID: {job_id}\n\n")
    

def show_all():
    jobs = load_jobs()
    for job_id, job in jobs.items():
        print(f"\n\tCompany: {job.get('company')}\n\tPosition: {job.get('Position')}\n\tDate: {job.get('date')}\n\tStatus: {job.get('status')}\n\tJob ID: {job_id}")
def write_to_file(jobs, filename='data.json'):
    with open(filename, 'w') as file:
        json.dump({"jobs": jobs}, file, indent=4)
      
company = input(" Enter the company: ")
position = input(" Enter the position: ")
status = input(" Enter the status: ")
date = input(" Enter the date: ")
add(position, date, company, status)
show_all()
mn =load_jobs()
df='1408'
if mn[df] not in mn:
    print("not found")
mn[df]['company']= "amazon"
write_to_file(mn)
show_all()