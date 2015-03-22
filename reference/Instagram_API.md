# Instagram API
## Users:
### 1. Get User
---
##### Url:
	https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
##### Method:
	GET
##### Input:
	users/{user-id}/?access_token=ACCESS-TOKEN
##### Output:
    {
      "meta" : {
        "code" : 200
      },
      "data" : {
        "counts" : {
          "media" : 86,
          "follows" : 20,
          "followed_by" : 93
        },
        "website" : "http:\/\/test.com.cn",
        "id" : "37004920",
        "bio" : "From\nTesr\nHaha",
        "profile_picture" : "https:\/\/instagramimages-a.akamaihd.net\/profiles\/profile_37004920_75sq_1399257924.jpg",
        "username" : "sharpidea",
        "full_name" : "JIABO"
      }
    }
### 2. GET follows
---
##### Url:
	https://api.instagram.com/v1/users/{user-id}/follows?access_token=ACCESS-TOKEN
##### Method:
	GET
##### Input:
	users/{user-id}/follows?access_token=ACCESS-TOKEN
##### Output:
	{
	    "data": [{
	        "username": "kevin",
	        "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
	        "full_name": "Kevin Systrom",
	        "id": "3"
	    },
	    {
	        "username": "instagram",
	        "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
	        "full_name": "Instagram",
	        "id": "25025320"
	    }]
	}
### 3. GET followed-by
---
##### Url:
	https://api.instagram.com/v1/users/{user-id}/followed-by?access_token=ACCESS-TOKEN
##### Method:
	GET
##### Input:
	users/{user-id}/followed-by?access_token=ACCESS-TOKEN
##### Output:
	{
	    "data": [{
	        "username": "kevin",
	        "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
	        "full_name": "Kevin Systrom",
	        "id": "3"
	    },
	    {
	        "username": "instagram",
	        "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
	        "full_name": "Instagram",
	        "id": "25025320"
	    }]
	}
### 4. GET relationship
---
##### Url:
	https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN
##### Method:
	GET
##### Input:
	users/{user-id}/relationship?access_token=ACCESS-TOKEN
##### Output:
	{
	    "meta": {
	        "code": 200
	    }, 
	    "data": {
	        "outgoing_status": "none", 
	        "incoming_status": "requested_by"
	    }
	}
	
### 5. POST relationship
---
##### Url:
	https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN
##### Method:
	POST
##### Input:
	users/{user-id}/relationship?access_token=ACCESS-TOKEN
    
    PARAMETERS:
	ACCESS_TOKEN	A valid access token.
	ACTION			One of follow/unfollow/block/unblock/approve/ignore.
##### Output:
	{
	    "meta": {
	        "code": 200
	    }, 
	    "data": {
	        "outgoing_status": "requested"
	    }
	}