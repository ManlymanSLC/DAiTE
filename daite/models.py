from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4

Base = declarative_base()

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class User(Base, TimestampMixin):
    __tablename__ = "users"
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    profile: Mapped["Profile"] = relationship("Profile", uselist=False, back_populates="user")
    preferences: Mapped["Preference"] = relationship("Preference", back_populates="user")

class Profile(Base, TimestampMixin):
    __tablename__ = "profiles"
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    user: Mapped[User] = relationship("User", back_populates="profile")

class Preference(Base, TimestampMixin):
    __tablename__ = "preferences"
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    preference_data: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped[User] = relationship("User", back_populates="preferences")

class MatchQueue(Base, TimestampMixin):
    __tablename__ = "match_queue"
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    potential_match_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)

class ChatSession(Base, TimestampMixin):
    __tablename__ = "chat_sessions"
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_a_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user_b_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

