from fastapi import APIRouter, Depends
from sqlalchemy import Column, Integer, ForeignKey

router = APIRouter(prefix="/parents", tags=["Parents"])

