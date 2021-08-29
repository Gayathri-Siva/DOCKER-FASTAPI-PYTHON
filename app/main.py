from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

import os
import urllib
from db import database, Job_application_Detail_In, Job_application_Detail, fresher_recruiter_details

app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints and Docker")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/job_application_details/", response_model=List[Job_application_Detail], status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    query = fresher_recruiter_details.select().offset(skip).limit(take)
    return await database.fetch_all(query)


@app.get("/job_application_details/{job_apply_id}/", response_model=Job_application_Detail, status_code = status.HTTP_200_OK)
async def read_notes(job_apply_id: int):
    query = fresher_recruiter_details.select().where(job_application_details.c.id == job_apply_id)
    return await database.fetch_one(query)


@app.post("/job_application_details/", response_model=Job_application_Detail, status_code = status.HTTP_201_CREATED)
async def create_new_job_apllication(job_application: Job_application_Detail_In):
    
    query = fresher_recruiter_details.insert().values(name=job_application.name, course=job_application.course, department = job_application.department,
                                                    college_name = job_application.college_name, cgpa = job_application.cgpa,
                                                      year_of_passing = job_application.year_of_passing,
                                                    apllied_position = job_application.apllied_position,
                                                  status_of_application = job_application.status_of_application)
    last_record_id = await database.execute(query)
    return {**job_application.dict(), "id": last_record_id}

@app.put("/job_application_details/{job_apply_id}/", response_model=Job_application_Detail, status_code = status.HTTP_200_OK)
async def update_note(job_apply_id: int, payload: Job_application_Detail_In):
    query = fresher_recruiter_details.update().where(fresher_recruiter_details.c.id == job_apply_id).values(status_of_application = payload.status_of_application)
    await database.execute(query)
    return {**payload.dict(), "id": job_apply_id}


