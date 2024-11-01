import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import select
from ..config import *
from ..database.model.Base import Base
from ..database.model.User import *
from ..database.model.Question import *
from ..database.model.APIKey import *

# -------------------------------------------------------
# 資料庫引擎設置
# -------------------------------------------------------

database_path = os.path.abspath(DATABASE_PATH)
engine = create_async_engine(f"sqlite+aiosqlite:///{database_path}", echo=True)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# -------------------------------------------------------
# 通用方法
# -------------------------------------------------------


async def get_session():
    """建立並管理 AsyncSession 會話的輔助函數。"""
    session = Session() 
    try:
        yield session
    finally:
        await session.close()


# -------------------------------------------------------
# 用戶操作方法
# -------------------------------------------------------


async def get_user(discord_id: int):
    """根據 Discord ID 獲取用戶資料。"""
    async for session in get_session():
        result = await session.execute(select(User).filter_by(discord_id=discord_id))
        return result.scalars().first()


async def create_user(discord_id: int, student_id: int, name: str):
    """新增用戶到資料庫。"""
    async for session in get_session():
        new_user = User(discord_id=discord_id, student_id=student_id, name=name)
        session.add(new_user)
        await session.commit()


async def delete_user(discord_id: int):
    """根據 Discord ID 刪除用戶資料。"""
    async for session in get_session():
        result = await session.execute(
            select(User).where(User.discord_id == discord_id)
        )
        user = result.scalars().first()
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False


# -------------------------------------------------------
# 題庫操作方法
# -------------------------------------------------------


async def get_question(id: int = None):
    """根據 ID 獲取題目資料。如果沒有提供 ID，則回傳最後一個題目。"""
    async for session in get_session():
        if id is not None:
            result = await session.execute(select(Question).filter_by(id=id))
        else:
            # 沒有提供 ID，根據 ID 排序並取最後一個題目
            result = await session.execute(select(Question).order_by(Question.id.desc()).limit(1))
        
        return result.scalars().first()
    
async def get_all_question_id():
    async for session in get_session():
        result = await session.execute(select(Question.id))  # 只選擇 id 欄位
        questions = result.scalars().all()  # 獲取所有的 id
        
        # 回傳 JSON 格式的題目 ID 列表
        return questions


async def create_question(
    title: str,
    description: str,
    SampleInput: str,
    SampleOutput: str,
    Input: str,
    Output: str,
):
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

async def delete_question(id: int):
    async for session in get_session():
        result = await session.execute(
            select(Question).where(Question.id == id)
        )
        question = result.scalars().first()
        if question:
            await session.delete(question)
            await session.commit()
            return True
        return False

# -------------------------------------------------------
# 資料庫設置方法
# -------------------------------------------------------


async def create_tables():
    """創建資料表。"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Tables created successfully.")

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