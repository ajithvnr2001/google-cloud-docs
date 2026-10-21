---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_blogger_v3/
title: Class /GOOG/CL_BLOGGER_V3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:37.750919+00:00
---

# Class /GOOG/CL_BLOGGER_V3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_blogger_v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_BLOGGER_V3 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_blogger_v3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_blogger_v3)



## Class
    
    
    /GOOG/CL_BLOGGER_V3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Blogger API v3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Blog` | PUBLIC  
`TY_002` | `BlogList` | PUBLIC  
`TY_003` | `BlogPerUserInfo` | PUBLIC  
`TY_004` | `BlogUserInfo` | PUBLIC  
`TY_005` | `Comment` | PUBLIC  
`TY_006` | `CommentList` | PUBLIC  
`TY_007` | `Page` | PUBLIC  
`TY_008` | `PageList` | PUBLIC  
`TY_009` | `Pageviews` | PUBLIC  
`TY_010` | `Post` | PUBLIC  
`TY_011` | `PostList` | PUBLIC  
`TY_012` | `PostPerUserInfo` | PUBLIC  
`TY_013` | `PostUserInfo` | PUBLIC  
`TY_014` | `PostUserInfosList` | PUBLIC  
`TY_015` | `User` | PUBLIC  
`TY_044` | `Locale` | PUBLIC  
`TY_045` | `Pages` | PUBLIC  
`TY_057` | `Posts` | PUBLIC  
`TY_063` | `Counts` | PUBLIC  
`TY_067` | `Image` | PUBLIC  
`TY_068` | `Author` | PUBLIC  
`TY_069` | `Blog` | PUBLIC  
`TY_092` | `Image` | PUBLIC  
`TY_093` | `Author` | PUBLIC  
`TY_094` | `Blog` | PUBLIC  
`TY_095` | `Images` | PUBLIC  
`TY_096` | `Location` | PUBLIC  
`TY_097` | `Image` | PUBLIC  
`TY_098` | `Author` | PUBLIC  
`TY_099` | `Blog` | PUBLIC  
`TY_100` | `InReplyTo` | PUBLIC  
`TY_101` | `Post` | PUBLIC  
`TY_102` | `Replies` | PUBLIC  
`TY_103` | `Blogs` | PUBLIC  
`TY_104` | `Locale` | PUBLIC  
`TY_T_001` | `Blog` | PUBLIC  
`TY_T_004` | `BlogUserInfo` | PUBLIC  
`TY_T_005` | `Comment` | PUBLIC  
`TY_T_007` | `Page` | PUBLIC  
`TY_T_010` | `Post` | PUBLIC  
`TY_T_013` | `PostUserInfo` | PUBLIC  
`TY_T_063` | `Counts` | PUBLIC  
`TY_T_095` | `Images` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://blogger.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | blogger:v3 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### APPROVE_COMMENTS

  * Description: blogger.comments.approve 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_COMMENTS

  * Description: blogger.comments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PAGES

  * Description: blogger.pages.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USETRASH` | IMPORTING | `STRING` | useTrash  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_POSTS

  * Description: blogger.posts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USETRASH` | IMPORTING | `STRING` | useTrash  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BLOGS

  * Description: blogger.blogs.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXPOSTS` | IMPORTING | `STRING` | maxPosts  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Blog  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BLOG_USER_INFOS

  * Description: blogger.blogUserInfos.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXPOSTS` | IMPORTING | `STRING` | maxPosts  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | BlogUserInfo  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BY_PATH_POSTS

  * Description: blogger.posts.getByPath 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXCOMMENTS` | IMPORTING | `STRING` | maxComments  
`IV_Q_PATH` | IMPORTING | `STRING` | path  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BY_URL_BLOGS

  * Description: blogger.blogs.getByUrl 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_URL` | IMPORTING | `STRING` | url  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Blog  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_COMMENTS

  * Description: blogger.comments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PAGES

  * Description: blogger.pages.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PAGE_VIEWS

  * Description: blogger.pageViews.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_RANGE` | IMPORTING | `STRING` | range  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | Pageviews  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_POSTS

  * Description: blogger.posts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODY` | IMPORTING | `STRING` | fetchBody  
`IV_Q_FETCHIMAGES` | IMPORTING | `STRING` | fetchImages  
`IV_Q_MAXCOMMENTS` | IMPORTING | `STRING` | maxComments  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_POST_USER_INFOS

  * Description: blogger.postUserInfos.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXCOMMENTS` | IMPORTING | `STRING` | maxComments  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | PostUserInfo  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_USERS

  * Description: blogger.users.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | User  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_PAGES

  * Description: blogger.pages.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ISDRAFT` | IMPORTING | `STRING` | isDraft  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IS_INPUT` | IMPORTING | `TY_007` | Page  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_POSTS

  * Description: blogger.posts.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODY` | IMPORTING | `STRING` | fetchBody  
`IV_Q_FETCHIMAGES` | IMPORTING | `STRING` | fetchImages  
`IV_Q_ISDRAFT` | IMPORTING | `STRING` | isDraft  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IS_INPUT` | IMPORTING | `TY_010` | Post  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BY_BLOG_COMMENTS

  * Description: blogger.comments.listByBlog 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | CommentList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BY_USER_BLOGS

  * Description: blogger.blogs.listByUser 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHUSERINFO` | IMPORTING | `STRING` | fetchUserInfo  
`IV_Q_ROLE` | IMPORTING | `STRING` | role  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | BlogList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_COMMENTS

  * Description: blogger.comments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | CommentList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PAGES

  * Description: blogger.pages.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | PageList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_POSTS

  * Description: blogger.posts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_FETCHIMAGES` | IMPORTING | `STRING` | fetchImages  
`IV_Q_LABELS` | IMPORTING | `STRING` | labels  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SORTOPTION` | IMPORTING | `STRING` | sortOption  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | PostList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_POST_USER_INFOS

  * Description: blogger.postUserInfos.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_LABELS` | IMPORTING | `STRING` | labels  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | PostUserInfosList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_AS_SPAM_COMMENTS

  * Description: blogger.comments.markAsSpam 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PAGES

  * Description: blogger.pages.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PUBLISH` | IMPORTING | `STRING` | publish  
`IV_Q_REVERT` | IMPORTING | `STRING` | revert  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`IS_INPUT` | IMPORTING | `TY_007` | Page  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_POSTS

  * Description: blogger.posts.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODY` | IMPORTING | `STRING` | fetchBody  
`IV_Q_FETCHIMAGES` | IMPORTING | `STRING` | fetchImages  
`IV_Q_MAXCOMMENTS` | IMPORTING | `STRING` | maxComments  
`IV_Q_PUBLISH` | IMPORTING | `STRING` | publish  
`IV_Q_REVERT` | IMPORTING | `STRING` | revert  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`IS_INPUT` | IMPORTING | `TY_010` | Post  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PUBLISH_PAGES

  * Description: blogger.pages.publish 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PUBLISH_POSTS

  * Description: blogger.posts.publish 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PUBLISHDATE` | IMPORTING | `STRING` | publishDate  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REMOVE_CONTENT_COMMENTS

  * Description: blogger.comments.removeContent 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_PAGES

  * Description: blogger.pages.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_POSTS

  * Description: blogger.posts.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_POSTS

  * Description: blogger.posts.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODIES` | IMPORTING | `STRING` | fetchBodies  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | PostList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_PAGES

  * Description: blogger.pages.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PUBLISH` | IMPORTING | `STRING` | publish  
`IV_Q_REVERT` | IMPORTING | `STRING` | revert  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_PAGE_ID` | IMPORTING | `STRING` | pageId  
`IS_INPUT` | IMPORTING | `TY_007` | Page  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Page  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_POSTS

  * Description: blogger.posts.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FETCHBODY` | IMPORTING | `STRING` | fetchBody  
`IV_Q_FETCHIMAGES` | IMPORTING | `STRING` | fetchImages  
`IV_Q_MAXCOMMENTS` | IMPORTING | `STRING` | maxComments  
`IV_Q_PUBLISH` | IMPORTING | `STRING` | publish  
`IV_Q_REVERT` | IMPORTING | `STRING` | revert  
`IV_P_BLOG_ID` | IMPORTING | `STRING` | blogId  
`IV_P_POST_ID` | IMPORTING | `STRING` | postId  
`IS_INPUT` | IMPORTING | `TY_010` | Post  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Post  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
