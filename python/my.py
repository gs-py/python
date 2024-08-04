import json
import random


def show_all():
    jobs=load_jobs()
    for job in jobs:
       print(f"\n\tCompany  :  {job.get('company')}\n\tPosition :  {job.get('Position')}\n\tDate     :  {job.get('date')}\n\tStatus   :  {job.get('status')}\n\tJob id   :  {job.get('job_id')} ")

#____________________________________________________________________________

def load_jobs(filename=r'C:\Users\gladw\Desktop\python\python\job_data.json'):
    try:
        with open(filename, 'r') as files:
            jobs=json.load(files)     
    except (FileNotFoundError,  json.JSONDecodeError):
         jobs = [ ]
         print("FILE NOT FOUND !!!")
    return jobs
         
 #____________________________________________________________________________
   
def add(position,date,company,status):
    jobs =load_jobs()
    rn =str(random.randint(100,999))
    data={
        "company": company,
        "Position": position ,
        "date": date,
        "status":status,
        "job_id": rn
    }
    
    jobs.append(data)
    write_to_file(jobs)
    print(f"\nSucessfully Added\n\tCompany :{company}\n\tPosition :{position}\n\tDate :{date}\n\tStatus :{status}\n\tJob Id :{rn}\n\n")
    
    
#____________________________________________________________________________
     
def write_to_file(jobs):
    with open('job_data.json','w') as files:
        json.dump(jobs,files, indent=4)
    

#____________________________________________________________________________
def delete_entry(position_to_delete):
    jobs =load_jobs()
    length =len(jobs)
    jobs = [job for job in jobs if job.get('Position') != position_to_delete]
    if length > len(jobs):
         write_to_file(jobs)
         print(f"\n\tJob with position '{position_to_delete}' has been deleted.")
    else:
        print(f"\n\tNo job found with position '{position_to_delete}'.")
#____________________________________________________________________________
 
       
def application_stat(c):
    jobs = load_jobs()
    for job in jobs:
        if job.get('company') == c:
            print(f"\n\t Company : {job.get('company')}\n\tStatus  : {job.get('status')}")
    
#____________________________________________________________________________

def edit(pos):
    jobs = load_jobs()
    for job in jobs:
             if job.get('job_id') == pos:  
                 print(f"\n\tCompany  :  {job.get('company')}\n\tPosition :  {job.get('Position')}\n\tDate     :  {job.get('date')}\n\tStatus   :  {job.get('status')}\n\tJob id   :  {job.get('job_id')} ")

    print("\n\tEnter the attribute To Edit\n\t1 : Company Name\n\t2 : Position\n\t3 : Date\n\t4 : Status ")
    gn =input("\n\tEnter the option  : ")
    if gn == "1":
               company = input("\n\tEnter the new company name: ")
               jobs[pos]['company'] = company
               print(f"\n\tprevious company name  : {job.get('company')}")
               job['company'] = company
               print(f"\n\tNew company name  : {job.get('company')}")
               write_to_file(jobs)
    
    elif gn =='2':
        position = input("Enter the new position: ")
        jobs = load_jobs()
        for job in jobs:
            if job.get('job_id') == pos:
                print(f"\n\tprevious Position name  : {job.get('Position')}")
                job['Position'] = position
                print(f"\n\tNew Position name  : {job.get('Position')}")
                write_to_file(jobs)
                
    elif gn == '3':
        date = input("Enter the new date: ")
        jobs = load_jobs()
        for job in jobs:
            if job.get('job_id') == pos:
                print(f"\n\tPrevious date  : {job.get('date')}")
                job['Date'] = date
                print(f"\n\tNew date  : {job.get('date')}")
                write_to_file(jobs)
                
    elif gn =='4':
        status = input("Enter the new status: ")
        jobs = load_jobs()
        for job in jobs:
            if job.get('job_id') == pos:
                print(f"\n\tPrevious status : {job.get('status')}")
                job['status'] = status
                print(f"\n\tNew status : {job.get('status')}")
                write_to_file(jobs)
                
    else:
        print("\n\tInvalid option")
        
#____________________________________________________________________________

def val(pos):
    jobs = load_jobs()
    for job in jobs:
        if job.get('job_id') == pos:
            return True
    else:
        return False
        

#____________________________________________________________________________
        
def menu():
    while True:
        print("\n---------------------------------\n")
        print("1.   Application Status")
        print("2.   Edit")
        print("3.   Add")
        print("4.   Delete")
        print("5.   Applied jobs")
        print("6.   Exit\n")
        print("---------------------------------")
        
        mn = input(" Enter the  option    :  ")
        if mn ==  "1":
            company = input(" Enter the  Company    :  ")
            application_stat(company)
        elif mn == "3":
            company = input(" Enter the  Company    :  ")
            position = input(" Enter the  position    :  ")
            status= input(" Enter the  Status    :  ")
            date = input(" Enter the Date :  ")
            add(position,date,company,status)
        elif mn == "5":
            show_all()
        elif mn == "6":
            print("\n\nExiting the application.\t\t")
            break
        elif mn =='4':
            position_to_delete = input("\n\tEnter the position to delete : ")
            delete_entry(position_to_delete)
        elif mn == "2":
            pos = input(" Enter the  job ID    :  ")
            if val(pos) == True:
                edit(pos)
            else:
                print("\n\tInvalid job ID")
            
        else:
         print("\n\tInvalid option")
            
            
            
            
 
    
    
if  __name__ ==  "__main__"  :
     menu()



