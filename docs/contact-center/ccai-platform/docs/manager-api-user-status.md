---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-user-status/
title: User status endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:40.517418+00:00
---

# User status endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-user-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  User status endpoints Stay organized with collections  Save and categorize content based on your preferences. 

User status represents a state that an agent can be in at any time. Each status (either out-of-the-box or a newly configured status) is represented in a single object, such as the following:
    
    
    [
      {
        "id": 0,
        "name": "string",
        "color": "string"
      }
    ]
    

## User statuses

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/user_statuses
    

**_More example Requests/Responses:_**

### Example request: User statuses

**_Body: None_**

### Example response: User statuses
    
    
    [
        {
            "id": 0,
            "name": "Available",
            "color": "green",
        },
        {
            "id": -1,
            "name": "Unavailable",
            "color": "red",
        },
        {
            "id": -2,
            "name": "Break",
            "color": "yellow",
        },
        {
            "id": -3,
            "name": "Special Task",
            "color": "pink",
        },
        {
            "id": -4,
            "name": "Meal",
            "color": "brown",
        },
        {
            "id": -5,
            "name": "Missed Call",
            "color": "blue_grey",
        },
        {
            "id": -6,
            "name": "Wrap-up",
            "color": "purple",
        },
        {
            "id": -7,
            "name": "In-call",
            "color": "light_blue",
        },
        {
            "id": -8,
            "name": "In-chat",
            "color": "indigo",
        },
        {
            "id": -10,
            "name": "Offline",
            "color": "grey",
        },
        {
            "id": 5,
            "name": "Meal",
            "color": "green",
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
