---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-bulk-user-management/
title: Bulk user management endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:39.179034+00:00
---

# Bulk user management endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-bulk-user-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Bulk user management endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The bulk management API endpoints let you create or update a large number of users through the bulk user management collection.

The API supports the use of JSON files. You can get JSON data using the template API.

Only api_user authentication is supported. You must enter the API user token in the password variable. The legacy authentication using a company secret is not supported.

When a JSON file is uploaded through the upload API, a job is created and validates the json file scheme.

The endpoints supported for bulk user management include the following:

  * Template

  * Bulk add and edit users from file

  * Jobs

  * Proceed

  * Schema Error

  * Update Error




To perform bulk user addition or updates using the bulk user API, do the following:

  1. Call the **Template** method to get the JSON template object that you will use to generate the JSON file.

  2. Call either the **Bulk add users from file** method or the **Bulk update users from file** method, depending on whether you are doing a bulk add or a bulk update. This verifies the schema of JSON file that you provide.

  3. After the JSON file schema is verified, call the **Proceed** method. This starts the job.

  4. To determine the status of the job, call the **Jobs** method.




## JSON file format

You can get the JSON file format by calling the template method.

Field(s) name | Values | Required | Validation  
---|---|---|---  
email | String(Email) | Yes | Must be a valid email. Must be unique within the file within Email column (no duplicates). so only 1 update per email address per file  
new_email | String(Email) | No | Must be a valid email. Must be unique within the file within New Email column (no duplicates). so only 1 update per email address per file  
agent_number | String | No | A string with no validation  
first_name | String | Yes | Non-empty string  
last_name | String | Yes | Non-empty string  
status | Active, Inactive, Empty | No | Must be "Active", "Inactive", or empty  
location | A string that is a location name, Empty, Null | No | Must exactly match one of the **existing** locations (case-insensitive), or Null, or empty  
max_chat_limit | 1 to X (where X is configured value), Empty | No | Must be 1 to X (inclusively), or empty  
max_chat_limit_enabled | 0, 1, Empty | No | Must be 0, 1 or empty  
roles | name: Role name / value: 0, 1, Empty | No | Must be 0, 1 or empty  
teams | name: Team name / value: 0, 1, Empty | No | Must be 0, 1 or empty  
  
Once the JSON file upload API method is successful, the Proceed API method can be called, and user creation or modification work is then processed.

The upload and proceed methods are asynchronously performed by Contact Center AI Platform (CCAI Platform). You can check status by calling the jobs method and specifying `job_id`.

## Status field

The job `status` field can have any of the following values:

Job status | Description  
---|---  
created | A job is created and waiting for validation.  
valid_scheme | Scheme validation is successful and proceed is possible.  
invalid_scheme | Scheme validation failed. Detailed information can be checked through the Scheme error log API.  
in_progress | Performing bulk user update/create.  
finished | Bulk user update/create complete.  
  
## Template

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​subdomain}​.{​domain​}/apps/api/v1/bulk/users/template
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Get template

This example demonstrates how to retrieve the templates.

##### Request

**_Body: None_**

##### Response: Template
    
    
    [
        {
            "email": "user1@somedomain.com",
            "new_email": "user1@somedomain.com",
            "agent_number": "A-001",
            "first_name": "James",
            "last_name": "Bond",
            "status": "Active",
            "location": "Mexico",
            "max_chat_limit": "2",
            "max_chat_limit_enabled": "0",
            "roles": [
                {
                    "name": "Admin",
                    "value": 0
                },
                {
                    "name": "Manager",
                    "value": 0
                },
                {
                    "name": "Agent",
                    "value": 0
                },
                {
                    "name": "Developer",
                    "value": 0
                },
                {
                    "name": "Manager Admin",
                    "value": 0
                },
                {
                    "name": "Manager Team",
                    "value": 0
                },
                {
                    "name": "Manager Data",
                    "value": 0
                }
            ],
            "teams": [
                {
                    "name": "test team_1",
                    "value": 0
                },
                {
                    "name": "test Team 2",
                    "value": 0
                },
                {
                    "name": "test team 3",
                    "value": 0
                }
            ]
        },
        {
            "email": "user2@somedomain.com",
            "new_email": "user3@somedomain.com",
            "agent_number": "A-002",
            "first_name": "John",
            "last_name": "Doe",
            "status": "Inactive",
            "location": "",
            "max_chat_limit": "",
            "max_chat_limit_enabled": "1",
            "roles": [
                {
                    "name": "Admin",
                    "value": 0
                },
                {
                    "name": "Manager",
                    "value": 0
                },
                {
                    "name": "Agent",
                    "value": 0
                },
                {
                    "name": "Developer",
                    "value": 0
                },
                {
                    "name": "Manager Admin",
                    "value": 0
                },
                {
                    "name": "Manager Team",
                    "value": 0
                },
                {
                    "name": "Manager Data",
                    "value": 0
                }
            ],
            "teams": [
                {
                    "name": "test team_1",
                    "value": 0
                },
                {
                    "name": "test Team 2",
                    "value": 0
                },
                {
                    "name": "test team 3",
                    "value": 0
                }
            ]
        },
        {
            "email": "user3@somedomain.com",
            "new_email": "user2@somedomain.com",
            "agent_number": "A-003",
            "first_name": "Jane",
            "last_name": "Doe",
            "status": "",
            "location": "null",
            "max_chat_limit": "1",
            "max_chat_limit_enabled": "",
            "roles": [
                {
                    "name": "Admin",
                    "value": 0
                },
                {
                    "name": "Manager",
                    "value": 0
                },
                {
                    "name": "Agent",
                    "value": 0
                },
                {
                    "name": "Developer",
                    "value": 0
                },
                {
                    "name": "Manager Admin",
                    "value": 0
                },
                {
                    "name": "Manager Team",
                    "value": 0
                },
                {
                    "name": "Manager Data",
                    "value": 0
                }
            ],
            "teams": [
                {
                    "name": "test team_1",
                    "value": 0
                },
                {
                    "name": "test Team 2",
                    "value": 0
                },
                {
                    "name": "test team 3",
                    "value": 0
                }
            ]
        }
    ]
    

**_Status Code:_** 200

## Jobs

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/jobs/{job_id}​
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Job detail

This example demonstrates how to retrieve the job detail for a specific job. In this example, the job ID is 1.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job detail
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:06:45.000Z",
        "process_requested_at": null,
        "filename": "100row.csv",
        "total_rows": 100,
        "affected_rows": 0,
        "failed_rows": 0,
        "status": "created",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": null,
        "scheme_errors": [],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job list

This example demonstrates how to get all jobs.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/
    

##### Response: Job list
    
    
    [
        {
            "id": 3,
            "created_at": "2022-01-07T06:21:10.000Z",
            "process_requested_at": "2022-01-07T06:22:25.000Z",
            "filename": "100row_new.csv",
            "total_rows": 100,
            "affected_rows": 0,
            "failed_rows": 0,
            "status": "in_progress",
            "uploaded_user_name": null,
            "proceed_user_name": null,
            "uploaded_api_user_name": "zdco_admin",
            "proceed_api_user_name": "zdco_admin",
            "scheme_errors": [],
            "update_errors": []
        },
        {
            "id": 2,
            "created_at": "2022-01-07T06:17:09.000Z",
            "process_requested_at": null,
            "filename": "100row.csv",
            "total_rows": 100,
            "affected_rows": 0,
            "failed_rows": 0,
            "status": "created",
            "uploaded_user_name": null,
            "proceed_user_name": null,
            "uploaded_api_user_name": "zdco_admin",
            "proceed_api_user_name": null,
            "scheme_errors": [],
            "update_errors": []
        },
        {
            "id": 1,
            "created_at": "2022-01-07T06:06:45.000Z",
            "process_requested_at": null,
            "filename": "100row.csv",
            "total_rows": 100,
            "affected_rows": 0,
            "failed_rows": 0,
            "status": "created",
            "uploaded_user_name": null,
            "proceed_user_name": null,
            "uploaded_api_user_name": "zdco_admin",
            "proceed_api_user_name": null,
            "scheme_errors": [],
            "update_errors": []
        }
    ]
    

**_Status Code:_** 200

#### Job created

This example demonstrates how to retrieve the bulk user request jobs that have been created.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job created
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:39:59.000Z",
        "process_requested_at": null,
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 0,
        "failed_rows": 0,
        "status": "created",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": null,
        "scheme_errors": [],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job validating success

This example demonstrates how to validate that a job is successful.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job validating success
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:40:34.000Z",
        "process_requested_at": null,
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 0,
        "failed_rows": 0,
        "status": "valid_scheme",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": null,
        "scheme_errors": [],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job validating fails

This example demonstrates how to determaine that a job that has failed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job validating fails
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:40:34.000Z",
        "process_requested_at": null,
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 0,
        "failed_rows": 0,
        "status": "invalid_scheme",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": null,
        "scheme_errors": [
            "scheme error detail 1",
            "scheme error detail 2",
            "scheme error detail 3"
        ],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job updating

This example demonstrates how to determine that a job that is updating.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job updating
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:40:34.000Z",
        "process_requested_at": "2022-01-07T06:42:59.000Z",
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 52,
        "failed_rows": 0,
        "status": "in_progress",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": "zdco_admin",
        "scheme_errors": [],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job update finish without errors

In this example we show how to identify a job that is finished without errors.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job update finish without errors
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:40:34.000Z",
        "process_requested_at": "2022-01-07T06:42:59.000Z",
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 100,
        "failed_rows": 0,
        "status": "finished",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": "zdco_admin",
        "scheme_errors": [],
        "update_errors": []
    }
    

**_Status Code:_** 200

#### Job update finish with errors

In this example we show how to identify a job that has finished with errors.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Job update finish with errors
    
    
    {
        "id": 1,
        "created_at": "2022-01-07T06:40:34.000Z",
        "process_requested_at": "2022-01-07T06:42:59.000Z",
        "filename": "100row_new.csv",
        "total_rows": 100,
        "affected_rows": 100,
        "failed_rows": 0,
        "status": "finished",
        "uploaded_user_name": null,
        "proceed_user_name": null,
        "uploaded_api_user_name": "zdco_admin",
        "proceed_api_user_name": "zdco_admin",
        "scheme_errors": [],
        "update_errors": [
            "update error detail 1",
            "update error detail 2",
            "update error detail 3"
        ]
    }
    

**_Status Code:_** 200

#### Error: Invalid job ID

This example shows a failure request where the job ID is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/bulk/users/jobs/1
    

##### Response: Error: Invalid job ID
    
    
    {
        "message": "Not Found"
    }
    

**_Status Code:_** 404

## Bulk add and edit users from file

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Endpoint:_**
    
    
    Method: POST
    Type: FORM DATA
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/upload
    

**_Body:_**

Key | Value | Description  
---|---|---  
file |  |   
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Job created

This example shows how to submit a job.

##### Request

**_Body:_**

Key | Value | Description  
---|---|---  
file |  |   
  
##### Response: Job created
    
    
    {
        "id": 1,
        "status": "created",
        "link": "https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/jobs/1"
    }
    

**_Status Code:_** 200

## Proceed

This API endpoint is used to continue an ipport job that has been started.

**_Endpoint:_**
    
    
    Method: POST
    Type: FORM DATA
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/proceed
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Body:_**

Key | Value | Description  
---|---|---  
id | `[job_id}` |   
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Proceed success

This example shows a job proceed that is successful.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | `[job_id}` |   
  
##### Response: Proceed success
    
    
    {
        "id": 1,
        "status": "valid_scheme",
        "link": "https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/jobs/1"
    }
    

**_Status Code:_** 200

#### Error: Proceed when before validation

This example shows a proceed prior to validation being completed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | `[job_id}` |   
  
##### Response: Error: Proceed when before validation
    
    
    {
        "message": "This job cannot proceed update. status: created"
    }
    

**_Status Code:_** 400

#### Error: Proceed when in progress

This example shows a proceed when the job is already in process.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | `[job_id}` |   
  
##### Response: Error: Proceed when in progress
    
    
    {
        "message": "Update is already in progress."
    }
    

**_Status Code:_** 400

## Scheme errors

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/errors/scheme/​{job_id}​
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Scheme errors

This example shows how to retrieve the schema errors.

##### Request

**_Body: None_**

##### Response: Scheme errors
    
    
    [
        {
            "message": "scheme error message 1",
            "column": null,
            "row": 1
        },
        {
            "message": "scheme error message 2",
            "column": null,
            "row": 2
        }
    ]
    

**_Status Code:_** 200

#### No errors

This example showes how to retrieve the schema errors with no errors.

##### Request

**_Body: None_**

##### Response: No errors
    
    
    []
    

**_Status Code:_** 200

## Update errors

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/bulk/users/errors/update/{job_id}​
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Update errors

This example shows how to retrieve the schema errors with update errors.

##### Request

**_Body: None_**

##### Response: Update errors
    
    
    [
        {
            "message": "update error message 1",
            "column": 1,
            "row": 1,
            "error_type": "error"
        },
        {
            "message": "update error message 2",
            "column": null,
            "row": 2,
            "error_type": "error"
        },
        {
            "message": "update warning message 1",
            "column": 3,
            "row": 3,
            "error_type": "warning"
        },
        {
            "message": "update warning message 2",
            "column": null,
            "row": 4,
            "error_type": "warning"
        }
    ]
    

**_Status Code:_** 200

#### No errors

This example shows how to retrieve the schema errors with no errors.

##### Request

**_Body: None_**

##### Response: No errors
    
    
    []
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
