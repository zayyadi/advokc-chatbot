from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import datetime

app = FastAPI(
    title="ADVOKC Chatbot API",
    description="API for ADVOKC civic-tech AI chatbot, promise tracking, and advocacy information.",
    version="0.1.0"
)

# --- Pydantic Models ---

class ChatQuery(BaseModel):
    session_id: Optional[str] = None
    query: str = Field(..., min_length=1, description="User's query to the chatbot")

class ChatResponse(BaseModel):
    session_id: Optional[str] = None
    response: str
    retrieved_context: Optional[List[Dict[str, Any]]] = None # For RAG source documents
    timestamp: datetime.datetime

class PromiseBase(BaseModel):
    politician_name: str = Field(..., description="Name of the politician making the promise") # Simplified for now, will link to politician_id later
    promise_title: str = Field(..., description="Concise title of the promise")
    promise_description: str = Field(..., description="Detailed description of the promise")
    category: Optional[str] = "General"
    date_made: Optional[datetime.date] = None
    source_url: Optional[str] = None
    status: str = Field("Pending", description="Status: Pending, In Progress, Fulfilled, Broken, Partially Fulfilled")

class PromiseCreate(PromiseBase):
    pass

class Promise(PromiseBase):
    promise_id: int
    status_update_date: Optional[datetime.date] = None
    evidence_url: Optional[str] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True # For SQLAlchemy or other ORM compatibility if used later

class AdvokcInfo(BaseModel):
    info_key: str
    info_title: str
    info_content: str
    category: Optional[str] = None
    last_updated: datetime.datetime


# --- In-memory "Database" (for placeholder purposes) ---
# Replace these with actual database interactions later

db_promises: List[Promise] = []
db_advokc_info: List[AdvokcInfo] = [
    AdvokcInfo(
        info_key="mission_statement",
        info_title="Our Mission",
        info_content="ADVOKC is dedicated to democratizing access to civic data, tracking political promises transparently, and empowering citizens with verifiable information based on Nigerian civic legal frameworks.",
        category="About Us",
        last_updated=datetime.datetime.now()
    ),
    AdvokcInfo(
        info_key="contact_details",
        info_title="Contact Us",
        info_content="Email: info@advokc.org | Phone: +234 XXX XXXXXXX",
        category="About Us",
        last_updated=datetime.datetime.now()
    )
]
promise_id_counter = 1

# --- API Endpoints ---

@app.get("/", tags=["General"])
async def root():
    return {"message": "Welcome to the ADVOKC Chatbot API"}

@app.post("/chat", response_model=ChatResponse, tags=["Chatbot"])
async def handle_chat(query: ChatQuery):
    # Placeholder: Echo the query for now.
    # In the future, this will involve:
    # 1. Querying the VectorDB (ChromaDB) for relevant context.
    # 2. Injecting context into a prompt for the LLM.
    # 3. Getting the LLM's completion.
    # 4. Logging the query and response.
    print(f"Received query: {query.query} (Session: {query.session_id})")
    return ChatResponse(
        session_id=query.session_id,
        response=f"Placeholder response to: '{query.query}'",
        timestamp=datetime.datetime.now()
    )

@app.get("/promises", response_model=List[Promise], tags=["Promises"])
async def get_promises(status: Optional[str] = None, politician_name: Optional[str] = None):
    # Placeholder: Return all promises or filter by status/politician
    # In the future, this will query the PostgreSQL database.
    filtered_promises = db_promises
    if status:
        filtered_promises = [p for p in filtered_promises if p.status.lower() == status.lower()]
    if politician_name:
        filtered_promises = [p for p in filtered_promises if p.politician_name.lower() == politician_name.lower()]
    return filtered_promises

@app.post("/promises", response_model=Promise, status_code=201, tags=["Promises"])
async def create_promise(promise_in: PromiseCreate):
    # Placeholder: Add promise to in-memory list.
    # In the future, this will insert into the PostgreSQL database.
    global promise_id_counter
    now = datetime.datetime.now()
    new_promise = Promise(
        promise_id=promise_id_counter,
        **promise_in.dict(),
        status_update_date=now.date(),
        created_at=now,
        updated_at=now
    )
    db_promises.append(new_promise)
    promise_id_counter += 1
    return new_promise

@app.get("/promises/{promise_id}", response_model=Promise, tags=["Promises"])
async def get_promise(promise_id: int):
    # Placeholder: Get a specific promise by ID.
    # In the future, this will query the PostgreSQL database.
    for p in db_promises:
        if p.promise_id == promise_id:
            return p
    raise HTTPException(status_code=404, detail="Promise not found")


@app.get("/advokc_info", response_model=List[AdvokcInfo], tags=["ADVOKC Information"])
async def get_advokc_info(category: Optional[str] = None):
    # Placeholder: Return ADVOKC information, optionally filtered by category.
    # In the future, this could query the PostgreSQL database or a static config.
    if category:
        return [info for info in db_advokc_info if info.category and info.category.lower() == category.lower()]
    return db_advokc_info

@app.get("/advokc_info/{info_key}", response_model=AdvokcInfo, tags=["ADVOKC Information"])
async def get_advokc_info_by_key(info_key: str):
    # Placeholder: Get specific ADVOKC info by key.
    for info in db_advokc_info:
        if info.info_key == info_key:
            return info
    raise HTTPException(status_code=404, detail="Information not found")

# To run this app (save as main.py and run in terminal):
# uvicorn main:app --reload
