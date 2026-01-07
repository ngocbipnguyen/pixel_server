# API Response Examples

Base URL: `http://localhost:8000/v1`

## Authentication
Tất cả endpoints (trừ login/register) yêu cầu header:
```
Authorization: Bearer <access_token>
```

---

## 1. User APIs

### POST /v1/user/
**Tạo user mới**

**Request:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "password123"
}
```

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "John Doe",
  "url": null,
  "token": null,
  "timestamps": 1699123456789,
  "is_active": false,
  "follow": false,
  "profile": null,
  "socials": null,
  "collections": null
}
```

**Response 400:**
```json
{
  "detail": "Email already exists"
}
```

---

### POST /v1/user/login
**Đăng nhập**

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response 200:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Response 401:**
```json
{
  "detail": "password was wrong!"
}
```

---

### GET /v1/user/uui?uui=xxx
**Lấy user theo UUI**

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "John Doe",
  "url": "https://example.com/avatar.jpg",
  "token": null,
  "timestamps": 1699123456789,
  "is_active": true,
  "follow": false,
  "profile": {
    "uui": "550e8400-e29b-41d4-a716-446655440000",
    "total_view": 1500,
    "all_time_rank": 25,
    "month_rank": 10
  },
  "socials": [
    {
      "id": "social_123",
      "name": "Instagram",
      "icon_url": "https://example.com/icon.png",
      "link": "https://instagram.com/user",
      "uui": "550e8400-e29b-41d4-a716-446655440000"
    }
  ],
  "collections": []
}
```

**Response 401:**
```json
{
  "detail": "Invalid token"
}
```

---

### GET /v1/user/
**Lấy tất cả users**

**Response 200:**
```json
[
  {
    "uui": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user1@example.com",
    "name": "User One",
    "url": null,
    "token": null,
    "timestamps": 1699123456789,
    "is_active": true,
    "follow": false,
    "profile": null,
    "socials": null,
    "collections": null
  },
  {
    "uui": "660e8400-e29b-41d4-a716-446655440001",
    "email": "user2@example.com",
    "name": "User Two",
    "url": null,
    "token": null,
    "timestamps": 1699123456790,
    "is_active": true,
    "follow": false,
    "profile": null,
    "socials": null,
    "collections": null
  }
]
```

---

### POST /v1/user/update
**Cập nhật user**

**Request:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Updated Name",
  "url": "https://example.com/new-avatar.jpg"
}
```

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "Updated Name",
  "url": "https://example.com/new-avatar.jpg",
  "token": null,
  "timestamps": 1699123456789,
  "is_active": true,
  "follow": false,
  "profile": null,
  "socials": null,
  "collections": null
}
```

---

## 2. Collection APIs

### POST /v1/collect/
**Tạo collection mới**

**Request:**
```json
{
  "title": "My Collection",
  "description": "A beautiful collection",
  "is_private": false,
  "media_count": 0,
  "videos_count": 0,
  "photos_count": 0,
  "uui": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response 200:**
```json
{
  "id": "collection_abc123",
  "title": "My Collection",
  "description": "A beautiful collection",
  "is_private": false,
  "media_count": 0,
  "videos_count": 0,
  "photos_count": 0,
  "timestamp_create": 1699123456789,
  "timestamp_update": 1699123456789,
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "pixels": null
}
```

---

### GET /v1/collect/
**Lấy tất cả collections (sắp xếp theo timestamp_update giảm dần)**

**Response 200:**
```json
[
  {
    "id": "collection_abc123",
    "title": "Collection 1",
    "description": "Description 1",
    "is_private": false,
    "media_count": 10,
    "videos_count": 2,
    "photos_count": 8,
    "timestamp_create": 1699123456789,
    "timestamp_update": 1699123556789,
    "uui": "550e8400-e29b-41d4-a716-446655440000",
    "pixels": []
  },
  {
    "id": "collection_def456",
    "title": "Collection 2",
    "description": "Description 2",
    "is_private": true,
    "media_count": 5,
    "videos_count": 0,
    "photos_count": 5,
    "timestamp_create": 1699123456790,
    "timestamp_update": 1699123456790,
    "uui": "550e8400-e29b-41d4-a716-446655440000",
    "pixels": []
  }
]
```

---

### GET /v1/collect/id?id=collection_abc123
**Lấy collection theo ID**

**Response 200:**
```json
{
  "id": "collection_abc123",
  "title": "My Collection",
  "description": "A beautiful collection",
  "is_private": false,
  "media_count": 10,
  "videos_count": 2,
  "photos_count": 8,
  "timestamp_create": 1699123456789,
  "timestamp_update": 1699123556789,
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "pixels": [
    {
      "id": "pixel_xyz789",
      "type": "photo",
      "width": 1920,
      "height": 1080,
      "avg_color": "#FF5733",
      "timestamps": 1699123456800,
      "is_favorite": false,
      "is_mark": false,
      "collection_id": "collection_abc123",
      "photo": {
        "id": "pixel_xyz789",
        "original": "http://localhost:9000/original/image.jpg",
        "large": "http://localhost:9000/large/image.jpg",
        "medium": "http://localhost:9000/medium/image.jpg",
        "small": "http://localhost:9000/small/image.jpg"
      }
    }
  ]
}
```

---

### GET /v1/collect/uui?uui=xxx
**Lấy collections theo user UUI**

**Response 200:**
```json
[
  {
    "id": "collection_abc123",
    "title": "Collection 1",
    "description": "Description 1",
    "is_private": false,
    "media_count": 10,
    "videos_count": 2,
    "photos_count": 8,
    "timestamp_create": 1699123456789,
    "timestamp_update": 1699123556789,
    "uui": "550e8400-e29b-41d4-a716-446655440000",
    "pixels": []
  }
]
```

---

### POST /v1/collect/update
**Cập nhật collection**

**Request:**
```json
{
  "id": "collection_abc123",
  "title": "Updated Title",
  "description": "Updated description",
  "is_private": true
}
```

**Response 200:**
```json
{
  "id": "collection_abc123",
  "title": "Updated Title",
  "description": "Updated description",
  "is_private": true,
  "media_count": 10,
  "videos_count": 2,
  "photos_count": 8,
  "timestamp_create": 1699123456789,
  "timestamp_update": 1699123656789,
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "pixels": []
}
```

---

## 3. Pixel APIs

### POST /v1/pixel/
**Tạo pixel mới**

**Request:**
```json
{
  "type": "photo",
  "width": 1920,
  "height": 1080,
  "avg_color": "#FF5733",
  "is_favorite": false,
  "is_mark": false,
  "collection_id": "collection_abc123",
  "photo": {
    "original": "http://localhost:9000/original/image.jpg",
    "large": "http://localhost:9000/large/image.jpg",
    "medium": "http://localhost:9000/medium/image.jpg",
    "small": "http://localhost:9000/small/image.jpg"
  }
}
```

**Response 200:**
```json
{
  "id": "pixel_xyz789",
  "type": "photo",
  "width": 1920,
  "height": 1080,
  "avg_color": "#FF5733",
  "timestamps": 1699123456800,
  "is_favorite": false,
  "is_mark": false,
  "collection_id": "collection_abc123",
  "photo": {
    "id": "pixel_xyz789",
    "original": "http://localhost:9000/original/image.jpg",
    "large": "http://localhost:9000/large/image.jpg",
    "medium": "http://localhost:9000/medium/image.jpg",
    "small": "http://localhost:9000/small/image.jpg"
  }
}
```

---

### GET /v1/pixel/id?id=pixel_xyz789
**Lấy pixel theo ID**

**Response 200:**
```json
{
  "id": "pixel_xyz789",
  "type": "photo",
  "width": 1920,
  "height": 1080,
  "avg_color": "#FF5733",
  "timestamps": 1699123456800,
  "is_favorite": false,
  "is_mark": false,
  "collection_id": "collection_abc123",
  "photo": {
    "id": "pixel_xyz789",
    "original": "http://localhost:9000/original/image.jpg",
    "large": "http://localhost:9000/large/image.jpg",
    "medium": "http://localhost:9000/medium/image.jpg",
    "small": "http://localhost:9000/small/image.jpg"
  }
}
```

---

### GET /v1/pixel/id_collect?collection_id=collection_abc123
**Lấy pixels theo collection ID**

**Response 200:**
```json
[
  {
    "id": "pixel_xyz789",
    "type": "photo",
    "width": 1920,
    "height": 1080,
    "avg_color": "#FF5733",
    "timestamps": 1699123456800,
    "is_favorite": false,
    "is_mark": false,
    "collection_id": "collection_abc123",
    "photo": {
      "id": "pixel_xyz789",
      "original": "http://localhost:9000/original/image.jpg",
      "large": "http://localhost:9000/large/image.jpg",
      "medium": "http://localhost:9000/medium/image.jpg",
      "small": "http://localhost:9000/small/image.jpg"
    }
  },
  {
    "id": "pixel_abc456",
    "type": "photo",
    "width": 1280,
    "height": 720,
    "avg_color": "#33FF57",
    "timestamps": 1699123456900,
    "is_favorite": true,
    "is_mark": false,
    "collection_id": "collection_abc123",
    "photo": {
      "id": "pixel_abc456",
      "original": "http://localhost:9000/original/image2.jpg",
      "large": "http://localhost:9000/large/image2.jpg",
      "medium": "http://localhost:9000/medium/image2.jpg",
      "small": "http://localhost:9000/small/image2.jpg"
    }
  }
]
```

---

### GET /v1/pixel/
**Lấy tất cả pixels**

**Response 200:**
```json
[
  {
    "id": "pixel_xyz789",
    "type": "photo",
    "width": 1920,
    "height": 1080,
    "avg_color": "#FF5733",
    "timestamps": 1699123456800,
    "is_favorite": false,
    "is_mark": false,
    "collection_id": "collection_abc123",
    "photo": {
      "id": "pixel_xyz789",
      "original": "http://localhost:9000/original/image.jpg",
      "large": "http://localhost:9000/large/image.jpg",
      "medium": "http://localhost:9000/medium/image.jpg",
      "small": "http://localhost:9000/small/image.jpg"
    }
  }
]
```

---

### POST /v1/pixel/update
**Cập nhật pixel**

**Request:**
```json
{
  "id": "pixel_xyz789",
  "is_favorite": true,
  "is_mark": true
}
```

**Response 200:**
```json
{
  "id": "pixel_xyz789",
  "type": "photo",
  "width": 1920,
  "height": 1080,
  "avg_color": "#FF5733",
  "timestamps": 1699123456800,
  "is_favorite": true,
  "is_mark": true,
  "collection_id": "collection_abc123",
  "photo": {
    "id": "pixel_xyz789",
    "original": "http://localhost:9000/original/image.jpg",
    "large": "http://localhost:9000/large/image.jpg",
    "medium": "http://localhost:9000/medium/image.jpg",
    "small": "http://localhost:9000/small/image.jpg"
  }
}
```

---

## 4. Profile APIs

### POST /v1/profile/
**Tạo profile**

**Request:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "total_view": 1500,
  "all_time_rank": 25,
  "month_rank": 10
}
```

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "total_view": 1500,
  "all_time_rank": 25,
  "month_rank": 10
}
```

---

### GET /v1/profile/uui?uui=xxx
**Lấy profile theo UUI**

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "total_view": 1500,
  "all_time_rank": 25,
  "month_rank": 10
}
```

---

### POST /v1/profile/update
**Cập nhật profile**

**Request:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "total_view": 2000,
  "all_time_rank": 20
}
```

**Response 200:**
```json
{
  "uui": "550e8400-e29b-41d4-a716-446655440000",
  "total_view": 2000,
  "all_time_rank": 20,
  "month_rank": 10
}
```

---

## 5. Social APIs

### POST /v1/social/
**Tạo social link**

**Request:**
```json
{
  "name": "Instagram",
  "icon_url": "https://example.com/icon.png",
  "link": "https://instagram.com/user",
  "uui": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response 200:**
```json
{
  "id": "social_123",
  "name": "Instagram",
  "icon_url": "https://example.com/icon.png",
  "link": "https://instagram.com/user",
  "uui": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

### GET /v1/social/id?id=social_123
**Lấy social theo ID**

**Response 200:**
```json
{
  "id": "social_123",
  "name": "Instagram",
  "icon_url": "https://example.com/icon.png",
  "link": "https://instagram.com/user",
  "uui": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

### GET /v1/social/uui?uui=xxx
**Lấy socials theo user UUI**

**Response 200:**
```json
[
  {
    "id": "social_123",
    "name": "Instagram",
    "icon_url": "https://example.com/icon.png",
    "link": "https://instagram.com/user",
    "uui": "550e8400-e29b-41d4-a716-446655440000"
  },
  {
    "id": "social_456",
    "name": "Twitter",
    "icon_url": "https://example.com/twitter-icon.png",
    "link": "https://twitter.com/user",
    "uui": "550e8400-e29b-41d4-a716-446655440000"
  }
]
```

---

### POST /v1/social/update
**Cập nhật social**

**Request:**
```json
{
  "id": "social_123",
  "link": "https://instagram.com/newusername"
}
```

**Response 200:**
```json
{
  "id": "social_123",
  "name": "Instagram",
  "icon_url": "https://example.com/icon.png",
  "link": "https://instagram.com/newusername",
  "uui": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

## 6. Upload APIs

### POST /v1/upload/
**Upload file đơn giản**

**Request:** `multipart/form-data`
- `file`: (file) image/video file

**Response 200:**
```json
{
  "filename": "image.jpg",
  "content_type": "image/jpeg",
  "url": "http://localhost:9000/media/550e8400-e29b-41d4-a716-446655440000.jpg"
}
```

**Response 400:**
```json
{
  "detail": "File type not allowed"
}
```

---

### POST /v1/upload/upload
**Upload image và tạo pixel**

**Request:** `multipart/form-data`
- `file`: (file) image file
- `collection_id`: (string) collection ID

**Response 200:**
```json
{
  "id": "pixel_xyz789",
  "type": "photo",
  "width": 1920,
  "height": 1080,
  "avg_color": null,
  "timestamps": 1699123456800,
  "is_favorite": false,
  "is_mark": false,
  "collection_id": "collection_abc123",
  "photo": {
    "id": "pixel_xyz789",
    "original": "http://localhost:9000/original/image.jpg",
    "large": "http://localhost:9000/large/image.jpg",
    "medium": "http://localhost:9000/medium/image.jpg",
    "small": "http://localhost:9000/small/image.jpg"
  }
}
```

---

### POST /v1/upload/uploads
**Upload nhiều images**

**Request:** `multipart/form-data`
- `files`: (file[]) multiple image files
- `collection_id`: (string) collection ID

**Response 200:**
```json
{
  "success_count": 2,
  "error_count": 0,
  "results": [
    {
      "filename": "image1.jpg",
      "pixel": {
        "id": "pixel_xyz789",
        "type": "photo",
        "width": 1920,
        "height": 1080,
        "collection_id": "collection_abc123"
      },
      "urls": {
        "original": "http://localhost:9000/original/image1.jpg",
        "large": "http://localhost:9000/large/image1.jpg",
        "medium": "http://localhost:9000/medium/image1.jpg",
        "small": "http://localhost:9000/small/image1.jpg"
      }
    },
    {
      "filename": "image2.jpg",
      "pixel": {
        "id": "pixel_abc456",
        "type": "photo",
        "width": 1280,
        "height": 720,
        "collection_id": "collection_abc123"
      },
      "urls": {
        "original": "http://localhost:9000/original/image2.jpg",
        "large": "http://localhost:9000/large/image2.jpg",
        "medium": "http://localhost:9000/medium/image2.jpg",
        "small": "http://localhost:9000/small/image2.jpg"
      }
    }
  ],
  "errors": []
}
```

**Response với errors:**
```json
{
  "success_count": 1,
  "error_count": 1,
  "results": [
    {
      "filename": "image1.jpg",
      "pixel": {...},
      "urls": {...}
    }
  ],
  "errors": [
    {
      "filename": "invalid.txt",
      "error": "File type not allowed"
    }
  ]
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Validation error message"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid token"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Notes

- Tất cả timestamps là milliseconds (Unix timestamp * 1000)
- Tất cả endpoints (trừ login) yêu cầu JWT token trong header
- File upload endpoints hỗ trợ: `image/jpeg`, `image/png`, `image/webp`, `video/mp4`, `video/mov`
- Collections được sắp xếp theo `timestamp_update` giảm dần (mới nhất trước)
- Pixels được sắp xếp theo `timestamps` giảm dần (mới nhất trước)

