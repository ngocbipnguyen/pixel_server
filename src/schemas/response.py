from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List
import time

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    """Standard API Response Wrapper"""
    success: bool
    message: str
    data: Optional[T] = None
    error: Optional[str] = None
    timestamp: int | None = None
    
    @classmethod
    def success_response(cls, data: T, message: str = "Operation successful"):
        return cls(
            success=True,
            message=message,
            data=data,
            error=None,
            timestamp=int(time.time() * 1000)
        )
    
    @classmethod
    def error_response(cls, message: str, error: str):
        return cls(
            success=False,
            message=message,
            data=None,
            error=error,
            timestamp=int(time.time() * 1000)
        )

class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated Response Wrapper"""
    success: bool
    message: str
    data: List[T]
    total: int
    page: int | None = None
    page_size: int | None = None
    has_next: bool = False
    has_prev: bool = False
    timestamp: int | None = None
    
    @classmethod
    def create(cls, data: List[T], total: int, message: str = "Data retrieved successfully", 
               page: int | None = None, page_size: int | None = None):
        has_next = False
        has_prev = False
        if page is not None and page_size is not None:
            has_next = (page * page_size) < total
            has_prev = page > 1
        
        return cls(
            success=True,
            message=message,
            data=data,
            total=total,
            page=page,
            page_size=page_size,
            has_next=has_next,
            has_prev=has_prev,
            timestamp=int(time.time() * 1000)
        )

class ListResponse(BaseModel, Generic[T]):
    """List Response Wrapper (no pagination)"""
    success: bool
    message: str
    data: List[T]
    count: int
    timestamp: int | None = None
    
    @classmethod
    def create(cls, data: List[T], message: str = "Data retrieved successfully"):
        # Convert Query object to list if needed
        if hasattr(data, 'all'):
            # It's a SQLAlchemy Query object
            data = list(data.all())
        elif not isinstance(data, list):
            # Convert other iterables to list, or handle None
            if data is None:
                data = []
            else:
                try:
                    data = list(data)
                except (TypeError, ValueError):
                    data = []
        
        return cls(
            success=True,
            message=message,
            data=data,
            count=len(data),
            timestamp=int(time.time() * 1000)
        )

class ErrorResponse(BaseModel):
    """Error Response"""
    success: bool = False
    message: str
    error: str
    error_code: str | None = None
    timestamp: int | None = None
    
    @classmethod
    def create(cls, message: str, error: str, error_code: str | None = None):
        return cls(
            success=False,
            message=message,
            error=error,
            error_code=error_code,
            timestamp=int(time.time() * 1000)
        )

