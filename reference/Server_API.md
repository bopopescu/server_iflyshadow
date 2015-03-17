# Server API
## 1. Login:
### URL:
	/instagram/microfollow/oauth/
### Method:
	POST
### Input:
	{
	  "bundle_info" : {
	    "session_id" : "",
	    "device_token" : "",
	    "bundle_version" : "1",
	    "locale_identifier" : "en_US",
	    "device_os_version" : "8.1",
	    "device_os_name" : "iPhone OS",
	    "bundle_id" : "101",
	    "igm_access_token" : "37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f",
	    "device_model" : "Simulator",
	    "preferred_language" : "en"
	  },
	  "data_info" : {
	    "igm_password" : "013513jv",
	    "igm_code" : "f81a268fa878490d867a12995eebdcb4",
	    "igm_user" : "sharpidea"
	  }
	}

### Output:
	{
	  "data" : {
	    "session_id" : "04c6737e3a6434279dc6476a8c891c0a",
	    "user" : {
	      "username" : "sharpidea",
	      "full_name" : "JIABO",
	      "id" : "37004920",
	      "profile_picture" : "https:\/\/instagramimages-a.akamaihd.net\/profiles\/profile_37004920_75sq_1399257924.jpg",
	      "website" : "http:\/\/test.com.cn",
	      "bio" : "From\nTesr\nHaha"
	    },
	    "mid" : 1,
	    "access_token" : "37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f",
	    "server_time" : 1426098402034
	  },
	  "code" : 200
	}

## 2. User Query:
### URL:
### Method:
	GET
### Input:
### Output:

## 3. Get Follow Users:
### URL:
### Method:
	GET
### Input:
### Output:

## 4. Follow:
### URL:
### Method:
	POST
### Input:
### Output:

## 5. Asset buy:
### URL:
### Method:
	POST
### Input:
### Output:

## 6. Asset query:
### URL:
### Method:
	GET
### Input:
### Output:
