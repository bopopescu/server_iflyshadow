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
        "data": {
            "id": "1574083",
            "username": "snoopdogg",
            "full_name": "Snoop Dogg",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
            "bio": "This is my bio",
            "website": "http://snoopdogg.com",
            "counts": {
                "media": 1320,
                "follows": 420,
                "followed_by": 3410
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