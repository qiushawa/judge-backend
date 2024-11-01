import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.config import *
from app.database.model.Base import Base
from app.database.model.User import *
from app.database.model.Question import *
from app.database.model.APIKey import *
from app.util.logger import setup_logger

logger = setup_logger(__name__)

database_path = os.path.abspath(DATABASE_PATH)
engine = create_async_engine(f"sqlite+aiosqlite:///{database_path}", echo=True)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    """建立並管理 AsyncSession 會話的輔助函數。"""
    session = Session()
    try:
        yield session
    finally:
        await session.close()

async def get_user(discord_id: int):
    """根據 Discord ID 獲取用戶資料。"""
    logger.info(f"Fetching user with Discord ID: {discord_id}")
    async for session in get_session():
        result = await session.execute(select(User).filter_by(discord_id=discord_id))
        user = result.scalars().first()
        if user:
            logger.info(f"User found: {user}")
        else:
            logger.warning(f"No user found with Discord ID: {discord_id}")
        return user

async def create_user(discord_id: int, student_id: int, name: str):
    """新增用戶到資料庫。"""
    logger.info(f"Creating user with Discord ID: {discord_id}, Student ID: {student_id}, Name: {name}")
    async for session in get_session():
        new_user = User(discord_id=discord_id, student_id=student_id, name=name)
        session.add(new_user)
        await session.commit()
        logger.info(f"User created: {new_user}")

async def delete_user(discord_id: int):
    """根據 Discord ID 刪除用戶資料。"""
    logger.info(f"Deleting user with Discord ID: {discord_id}")
    async for session in get_session():
        result = await session.execute(select(User).where(User.discord_id == discord_id))
        user = result.scalars().first()
        if user:
            await session.delete(user)
            await session.commit()
            logger.info(f"User deleted: {user}")
            return True
        logger.warning(f"No user found with Discord ID: {discord_id}")
        return False

async def get_question(id: int = None):
    """根據 ID 獲取題目資料。如果沒有提供 ID，則回傳最後一個題目。"""
    if id is not None:
        logger.info(f"Fetching question with ID: {id}")
    else:
        logger.info("Fetching the latest question")
    async for session in get_session():
        if id is not None:
            result = await session.execute(select(Question).filter_by(id=id))
        else:
            result = await session.execute(select(Question).order_by(Question.id.desc()).limit(1))
        question = result.scalars().first()
        if question:
            logger.info(f"Question found: {question}")
        else:
            logger.warning(f"No question found with ID: {id}")
        return question

async def get_all_question_id():
    logger.info("Fetching all question IDs")
    async for session in get_session():
        result = await session.execute(select(Question.id))
        questions = result.scalars().all()
        logger.info(f"Question IDs fetched: {questions}")
        return questions

async def create_question(
    title: str,
    description: str,
    SampleInput: str,
    SampleOutput: str,
    Input: str,
    Output: str,
):
    logger.info(f"Creating question with title: {title}")
    async for session in get_session():
        new_question = Question(
            title=title,
            description=description,
            SampleInput=SampleInput,
            SampleOutput=SampleOutput,
            Input=Input,
            Output=Output
        )
        session.add(new_question)
        await session.commit()
        logger.info(f"Question created: {new_question}")

async def delete_question(id: int):
    logger.info(f"Deleting question with ID: {id}")
    async for session in get_session():
        result = await session.execute(select(Question).where(Question.id == id))
        question = result.scalars().first()
        if question:
            await session.delete(question)
            await session.commit()
            logger.info(f"Question deleted: {question}")
            return True
        logger.warning(f"No question found with ID: {id}")
        return False

async def create_tables():
    """創建資料表。"""
    logger.info("Creating tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Tables created")

__all__ = [
    "get_user",
    "create_user",
    "delete_user",
    "delete_user",
    "get_question",
    "create_question",
    "create_tables",
    "get_all_question_id",
    "delete_question",
]