---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-email/
title: Email endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:32.945763+00:00
---

# Email endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Email endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The email endpoints provide access to the email session objects.

The following is a model of the email support resource. Review the model to determine which fields might contain PII.
    
    
    [
      {
          "id": 1442,
          "lang": "en",
          "email_status": "paused",
          "created_at": "2024-01-30T07:09:48.813Z",
          "assigned_at": "2024-01-30T07:09:49.000Z",
          "finished_at": "2024-02-29T10:00:11.000Z",
          "updated_at": "2024-02-29T10:00:11.948Z",
          "queue_duration": 0,
          "email_duration": 10207,
          "out_ticket_id": null,
          "out_ticket_url": null,
          "total_thread_numbers": 2,
          "selected_menu": {
            "id": 0,
            "name": "string",
            "parent_id": 0,
            "position": 0,
            "deleted": true,
            "hidden": "string",
            "menu_type": "email_menu",
            "output_msg": "string"
          },
          "menu_path": {
            "items_count": 0,
            "name": "string",
            "materialized_path": "string"
          },
          "agent_info": {
            "id": 0,
            "name": "string", //This may be considered PII
            "last_name": "string", //This may be considered PII
            "first_name": "string", //This may be considered PII
            "agent_number": "string", //This may be considered PII
            "avatar_url": "string"
          },
          "end_user": {
            "id": 0, 
            "identifier": "string", //This may be considered PII
            "out_contact_id": "string"
          },
          "email_attachments": [
            {
              "id": 0, 
              "file_type": "email_content",
              "url": "string" //This may be considered PII
            }
          ],
          "email_threads": [
            {
                "id": 0,
                "subject": "string", //This may be considered PII
                "attachment_count": 0,
                "direction": "string",
                "is_read": true,
                "is_draft": false,
                "created_at": "2023-12-27T09:55:05.546Z",
                "updated_at": "2023-12-27T09:55:50.701Z"
            },
          ],
          "transfers": [
            {
              "id": 0,
              "status": "transferring",
              "created_at": "2024-01-12T19:49:52.896Z",
              "updated_at": "2024-01-12T19:55:35.896Z",
              "from_menu": {
                "items_count": 0,
                "name": "string",
                "materialized_path": "string"
              },
              "to_menu": {
                "items_count": 0,
                "name": "string",
                "materialized_path": "string"
              },
              "from_agent": {
                "id": 0,
                "name": "string", //This may be considered PII
                "last_name": "string", //This may be considered PII
                "first_name": "string", //This may be considered PII
                "agent_number": "string", //This may be considered PI
                "avatar_url": "string"
              },
              "to_agent": {
                "id": 0,
                "name": "string", //This may be considered PII
                "last_name": "string", //This may be considered PII
                "first_name": "string", //This may be considered PII
                "agent_number": "string", //This may be considered PI
                "avatar_url": "string"
              }
            }
          ],
          "handle_durations": [
              {
                  "agent_id": 0,
                  "email_duration": 0,
                  "menu_path_id": 0,
                  "menu_path": "string",
                  "lang": "en",
                  "transfer": false,
                  "transfer_id": 1,
                  "assignment_type": "string",
                  "started_at": "2024-01-10T07:27:14.000Z",
                  "ended_at": "2024-01-10T07:27:20.000Z",
              }
          ],
          "queue_durations": [
              {
                  "agent_id": 0,
                  "queue_duration": 0,
                  "menu_path_id": 0,
                  "menu_path": "string",
                  "lang": "en",
                  "started_at": "2024-01-10T07:27:14.000Z",
                  "ended_at": "2024-01-10T07:27:20.000Z",
                  "assignment_type": "string",
              }
          ],
          "consumer_handle_durations": [
              {
                  "id": 100,
                  "email_duration": 314,
                  "attachments_count": 10,
                  "started_at": "2016-02-19T18:50:08.000Z",
                  "ended_at": "2016-02-19T18:55:22.000Z"
              }
          ]
      }
    ]
    

## Email

Parameter | Required | Data Type | Definition  
---|---|---|---  
sort_column | FALSE | String | Sorts response based on any field in the response object.  
sort_direction | FALSE | ASC or DESC | Notes the direction of the sort, whether ascending or descending.  
page | FALSE | String | Pairs with per to note what page of records. For example, if per is made to be 200 and page is 2, the response would contain record 201-400.  
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example, if per is made to be 200 and page is 2, the response would contain record 201-400.  
assigned_at[from] | FALSE | Time in UTC | Creates a lower bound of the assigned at field. All records returned will be after the inputted value.  
assigned_at[to] | FALSE | Time in UTC | Creates an upper bound of the assigned at field. All records returned will be before the inputted value.  
finished_at[from] | FALSE | Time in UTC | Creates a lower bound of the finished at field. All records returned will be after the inputted value.  
finished_at[to] | FALSE | Time in UTC | Creates an upper bound of the finished at field. All records returned will be before the inputted value.  
updated_at[from] | FALSE | Time in UTC | Creates a lower bound of the updated at field. All records returned will be after the inputted value.  
updated_at[to] | FALSE | Time in UTC | Creates an upper bound of the updated at field. All records returned will be before the inputted value.  
created_at[from] | FALSE | Time in UTC | Creates a lower bound of the created at field. All records returned will be after the inputted value.  
created_at[to] | FALSE | Time in UTC | Creates an upper bound of the created at field. All records returned will be before the inputted value.  
id[] | FALSE | Array[String] | Array of strings. Id of records to search and return.  
agent_id[] | FALSE | Array[String] | Filters response by agent id.  
end_user_id[] | FALSE | Array[String] | Filters response based on the end user id.  
email_status[] | FALSE | Array[String] | Returns records based on where the email is in the email lifecycle. Possible values: unopened, active, paused, resolved, closed, reopened  
total_thread_numbers[from] | FALSE | Number | Creates a lower bound of the total thread numbers field. All records returned will be after the inputted value.  
total_thread_numbers[to] | FALSE | Number | Creates an upper bound of the total thread numbers field. All records returned will be before the inputted value.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/emails
    

**_More example Requests/Responses:_**

### Example request: Email example

**_Query: None_**

**_Body: None_**

### Example response: Email example
    
    
    [
        {
            "id": 1442,
            "lang": "en",
            "email_status": "paused",
            "created_at": "2024-01-30T07:09:48.813Z",
            "assigned_at": "2024-01-30T07:09:49.000Z",
            "finished_at": "2024-02-29T10:00:11.000Z",
            "updated_at": "2024-02-29T10:00:11.948Z",
            "queue_duration": 0,
            "email_duration": 10207,
            "out_ticket_id": null,
            "out_ticket_url": null,
            "total_thread_numbers": 2,
            "selected_menu": {
                "id": 16,
                "name": "Test Queue",
                "parent_id": null,
                "position": 3,
                "deleted": false,
                "menu_type": "email_menu",
                "output_msg": null,
                "hidden": false
            },
            "menu_path": {
                "items_count": 1,
                "name": "Test Queue",
                "materialized_path": "16"
            },
            "agent_info": {
                "id": 4,
                "agent_number": "Bill",
                "name": "Test Agent",
                "last_name": "Agent",
                "first_name": "Test",
                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20230919-78154-airlnu.png"
            },
            "end_user": {
                "id": 1499,
                "identifier": null,
                "out_contact_id": null
            },
            "email_attachments": [],
            "email_threads": [
                {
                    "id": 2287,
                    "subject": "3001-002",
                    "attachment_count": 0,
                    "direction": "Outbound",
                    "is_read": true,
                    "is_draft": false,
                    "created_at": "2024-01-30T07:09:48.886Z",
                    "updated_at": "2024-01-30T07:09:48.886Z"
                },
                {
                    "id": 2291,
                    "subject": "Re: 3001-002",
                    "attachment_count": 0,
                    "direction": "Inbound",
                    "is_read": true,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:29:11.019Z",
                    "updated_at": "2024-01-30T09:30:52.853Z"
                },
                {
                    "id": 2292,
                    "subject": "Re: 3001-002",
                    "attachment_count": 0,
                    "direction": "Outbound",
                    "is_read": true,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:31:21.567Z",
                    "updated_at": "2024-01-30T09:31:21.567Z"
                },
                {
                    "id": 2293,
                    "subject": "Re: 3001-002",
                    "attachment_count": 2,
                    "direction": "Inbound",
                    "is_read": false,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:32:57.966Z",
                    "updated_at": "2024-01-30T09:32:57.966Z"
                },
                {
                    "id": 2295,
                    "subject": "Re: 3001-002",
                    "attachment_count": 3,
                    "direction": "Inbound",
                    "is_read": false,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:57:13.536Z",
                    "updated_at": "2024-01-30T09:57:13.536Z"
                },
                {
                    "id": 2296,
                    "subject": "Re: 3001-002",
                    "attachment_count": 3,
                    "direction": "Inbound",
                    "is_read": false,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:59:58.514Z",
                    "updated_at": "2024-01-30T09:59:58.514Z"
                }
            ],
            "transfers": [],
            "handle_durations": [
                {
                    "id": 63,
                    "agent_id": 4,
                    "email_duration": 0,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T07:09:48.813Z",
                    "ended_at": "2024-01-30T07:09:48.886Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 65,
                    "agent_id": 4,
                    "email_duration": 130,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T09:29:11.019Z",
                    "ended_at": "2024-01-30T09:31:21.567Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 67,
                    "agent_id": 4,
                    "email_duration": 1455,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T09:32:57.966Z",
                    "ended_at": "2024-01-30T09:57:13.536Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 68,
                    "agent_id": 4,
                    "email_duration": 164,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T09:57:13.536Z",
                    "ended_at": "2024-01-30T09:59:58.514Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 70,
                    "agent_id": 4,
                    "email_duration": 96,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T09:31:21.567Z",
                    "ended_at": "2024-01-30T09:32:57.966Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 71,
                    "agent_id": 4,
                    "email_duration": 8362,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T07:09:48.886Z",
                    "ended_at": "2024-01-30T09:29:11.019Z",
                    "assignment_type": "auto",
                    "status": 1
                }
            ],
            "queue_durations": [
                {
                    "id": 15,
                    "agent_id": 4,
                    "ended_at": "2024-01-30T07:09:49.308Z",
                    "lang": "en",
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "queue_duration": 0,
                    "started_at": "2024-01-30T07:09:49.139Z",
                    "assignment_type": "auto",
                    "status": 1
                }
            ],
            "consumer_handle_durations": [
                {
                    "id": 1,
                    "email_duration": 8362,
                    "started_at": "2024-01-30T07:09:48.886Z",
                    "ended_at": "2024-01-30T09:29:11.019Z",
                    "attachments_count": 0
                },
                {
                    "id": 2,
                    "email_duration": 96,
                    "started_at": "2024-01-30T09:31:21.567Z",
                    "ended_at": "2024-01-30T09:32:57.966Z",
                    "attachments_count": 2
                },
                {
                    "id": 4,
                    "email_duration": 1455,
                    "started_at": "2024-01-30T09:32:57.966Z",
                    "ended_at": "2024-01-30T09:57:13.536Z",
                    "attachments_count": 0
                },
                {
                    "id": 5,
                    "email_duration": 164,
                    "started_at": "2024-01-30T09:57:13.536Z",
                    "ended_at": "2024-01-30T09:59:58.514Z",
                    "attachments_count": 3
                }
            ]
        },
        {
            "id": 1443,
            "lang": "en",
            "email_status": "paused",
            "created_at": "2024-01-30T07:25:34.736Z",
            "assigned_at": "2024-01-30T07:25:35.000Z",
            "finished_at": "2024-02-29T09:40:05.000Z",
            "updated_at": "2024-02-29T09:40:05.784Z",
            "queue_duration": 0,
            "email_duration": 1396,
            "out_ticket_id": null,
            "out_ticket_url": null,
            "total_thread_numbers": 1,
            "selected_menu": {
                "id": 16,
                "name": "Test Queue",
                "parent_id": null,
                "position": 3,
                "deleted": false,
                "menu_type": "email_menu",
                "output_msg": null,
                "hidden": false
            },
            "menu_path": {
                "items_count": 1,
                "name": "Test Queue",
                "materialized_path": "16"
            },
            "agent_info": {
                "id": 4,
                "agent_number": "Bill",
                "name": "Test Agent",
                "last_name": "Agent",
                "first_name": "Test",
                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20230919-78154-airlnu.png"
            },
            "end_user": {
                "id": 1500,
                "identifier": null,
                "out_contact_id": null
            },
            "email_attachments": [],
            "email_threads": [
                {
                    "id": 2288,
                    "subject": "3001-003",
                    "attachment_count": 0,
                    "direction": "Outbound",
                    "is_read": true,
                    "is_draft": false,
                    "created_at": "2024-01-30T07:25:34.833Z",
                    "updated_at": "2024-01-30T07:25:34.833Z"
                },
                {
                    "id": 2289,
                    "subject": "Re: 3001-003",
                    "attachment_count": 0,
                    "direction": "Inbound",
                    "is_read": false,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:15:43.549Z",
                    "updated_at": "2024-01-30T09:15:43.549Z"
                },
                {
                    "id": 2294,
                    "subject": "Re: 3001-003",
                    "attachment_count": 0,
                    "direction": "Inbound",
                    "is_read": false,
                    "is_draft": false,
                    "created_at": "2024-01-30T09:39:00.127Z",
                    "updated_at": "2024-01-30T09:39:00.127Z"
                }
            ],
            "transfers": [],
            "handle_durations": [
                {
                    "id": 64,
                    "agent_id": 4,
                    "email_duration": 0,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T07:25:34.736Z",
                    "ended_at": "2024-01-30T07:25:34.833Z",
                    "assignment_type": "auto",
                    "status": 1
                },
                {
                    "id": 66,
                    "agent_id": 4,
                    "email_duration": 1396,
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "lang": "en",
                    "transfer": false,
                    "transfer_id": null,
                    "started_at": "2024-01-30T09:15:43.549Z",
                    "ended_at": "2024-01-30T09:39:00.127Z",
                    "assignment_type": "auto",
                    "status": 1
                }
            ],
            "queue_durations": [
                {
                    "id": 16,
                    "agent_id": 4,
                    "ended_at": "2024-01-30T07:25:35.503Z",
                    "lang": "en",
                    "menu_path_id": 5,
                    "menu_path": "Test Queue",
                    "queue_duration": 0,
                    "started_at": "2024-01-30T07:25:35.280Z",
                    "assignment_type": "auto",
                    "status": 1
                }
            ],
            "consumer_handle_durations": [
                {
                    "id": 3,
                    "email_duration": 1396,
                    "started_at": "2024-01-30T09:15:43.549Z",
                    "ended_at": "2024-01-30T09:39:00.127Z",
                    "attachments_count": 0
                }
            ]
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
