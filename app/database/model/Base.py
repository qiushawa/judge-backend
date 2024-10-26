from sqlalchemy.orm import declarative_base, decl_api

Base:decl_api.DeclarativeMeta = declarative_base()

__all__ = ["Base"]