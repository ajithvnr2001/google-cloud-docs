---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-user-configuration-data/
title: Get user configuration data \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:09.574687+00:00
---

# Get user configuration data  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-user-configuration-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Get user configuration data Stay organized with collections  Save and categorize content based on your preferences. 

The Apps API is designed to retrieve user configuration data. You can read the current user configuration for all users, or for a single user, regardless of their role or status. Both system and custom roles are included in this output.

This endpoint differs from the endpoints used in the Bulk User Upload process, and provides necessary information to support bulk operations. For more information about how to perform bulk user management processes, see [Bulk User Management API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management-api).

## API capabilities and limitations

When retrieving user data, you can include parameters to tailor the API response to your needs. The following parameters are supported:

  * **Specific User(s)**

    * ID options: Email, System ID, or Custom user ID. Users can specify one or multiple IDs. If multiple user IDs point to the same user, that user should only be represented once in the response.
  * **Pagination**

    * Users can retrieve results in paginated sets to manage large datasets. The API response should indicate whether there are additional pages to retrieve.

    * An API parameter allows users to request a specific page of results.

    * Users can specify the page size. The default page size is 100, and the maximum is 1,000. When a specific page number is provided, user IDs cannot be included in the request.




The API response includes all user profile and configuration fields, except for the 'Status' field. Instead of the 'Status' field, the API will provide a `deactivated_at` field. This field will contain:

  * No value for active users.

  * The date and time when a user was deactivated.




The following table lists the user profile fields that will be included in the API response:

**Table 1. User profile fields table**

**Order** | **Column Type** | **Number of Columns** | **Column(s) Name** | **Valid Values**  
---|---|---|---|---  
1  | Email  | 1  | Email  | Email   
2  | Agent ID  | 1  | Agent ID  | String   
3  | First name  | 1  | First name  | String   
4  | Last name  | 1  | Last name  | String   
5  | Alias  | 1  | Alias  | String   
6  | Deactivated at  | 1  | Deactivated at  | No value, Date/time   
7  | Location  | 1  | Location  | A string that is a location name, Empty (no change), Null (remove current location).   
8  | Chat concurrency  | 1  | Chat concurrency  | 1 to X (where X is configured value), Empty   
9  | Chat concurrency status  | 1  | Chat concurrency status  | 0, 1, Empty   
10  | Non-restricted international calling  | 1  | Non-restricted international calling  | (True/False)   
11  | External User  | 1  | External User  | (Yes/No)   
12  | External SIP URI  | 1  | External SIP URI  | String   
13  | UCaaS Username  | 1  | UCaaS Username  | String   
14  | Agent Extensions  | 1  | Agent Extensions  |   
15  | Roles  | Multiple  | Role: Role Name A Role: Role Name B Role: Role Name C etc.  | 0, 1, Empty   
16  | Team  | Multiple  | Team: Team Name A,  Team: Team Name B,  Team: Team Name C etc.  | 0, 1, Empty   
17  | Phone number  | Multiple  | Direct Inbound Number: 1,  Direct Inbound Number: 2,  Direct Inbound Number: 3  | Phone number in E. 164 format   
18  | Filter  | Single  | Filter  | String   
19  | Filter Timeout  | Single  | Filter Timeout  | Numeric value between 0 - 1,440   
  
## Limitations

  * Only one type of user ID is supported per request.

  * The maximum number of IDs per API request is 1,000.

  * Users cannot provide both user IDs and a page number request in a single API request. The API will return all users based on the request, up to 1,000.




## API error messages

The API will provide the following error messages for specific scenarios:

  * **Page size** : "Exceeded maximum page size request (1,000 is the maximum)"

  * **Page size (number input requirement)** : "Invalid page size request; must be a numeric value"

  * **Combined user ID and pagination request** : "Combination of user ID and pagination request is not supported"

  * **User ID (exceeded)** : "Exceeded maximum number of user IDs (1,000 is the maximum)"




## Example request and response

This example demonstrates retrieving the first page of users with 100 users per page. The response body includes an array of user objects, each containing detailed user configuration data.

**Request:**
    
    
    Method: GET
    Type:
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/users?page=1&per_page=100
    

**Response:**
    
    
    [
      {
        "email": "email",
        "agent_number": "number",
        "first_name": "first",
        "last_name": "last",
        "status": "Active",
        "location": "location",
        "max_chat_limt": 3,
        "max_chat_limit_enabled": true,
        "deleted_at": "2024-07-16T15:57:12.000Z",
        "ucaas_user_name": "username",
        "external_user": true,
        "ucaas_sip_uri": "sip uri",
        "unrestricted_international_calling": false,
        "roles": [
          { "name": "Admin" },
          { "name": "Manager" }
        ],
        "teams": [
          { "name": "name" }
        ],
        "phone_numbers": [
          "123-456-7890",
          "098-765-4321"
        ]
      },
      ...
    ]
    

This example demonstrates retrieving the details of a single user by passing an email parameter. The response body includes a user object containing detailed user configuration data.

**Request:**
    
    
    Method: GET
    Type:
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/users?email[]=email
    

**Response:**
    
    
    [
      {
        "email": "email",
        "agent_number": "number",
        "first_name": "first",
        "last_name": "last",
        "status": "Active",
        "location": "location",
        "max_chat_limt": 3,
        "max_chat_limit_enabled": true,
        "deleted_at": "2024-07-16T15:57:12.000Z",
        "ucaas_user_name": "username",
        "external_user": true,
        "ucaas_sip_uri": "sip uri",
        "unrestricted_international_calling": false,
        "roles": [
          { "name": "Admin" },
          { "name": "Manager" }
        ],
        "teams": [
          { "name": "name" }
        ],
        "phone_numbers": [
          "123-456-7890",
          "098-765-4321"
        ]
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
