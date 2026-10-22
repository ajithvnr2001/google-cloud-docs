---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-team/
title: Team endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:55.429272+00:00
---

# Team endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-team/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Team endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Teams represent a grouping that an agent can be assigned to, which can then be assigned to a queue. Each object represents a single team. 

There are three team endpoints:

  * `/team` \- pulls a list of team.

  * `/team/tree` \- pulls teams in a tree structure.

  * `/team/{:id}` \- pulls a single team resource.




Review the following model to determine which fields might contain PII. 
    
    
    [
      {
        "id": 0,
        "name": "string",
        "parent_id": 0,
        "position": 0,
        "deleted": true,
        "agents_count": 0,
        "assignees": {
          "id": 0,
          "name": "string", // This may be considered PII
          "last_name": "string", // This may be considered PII
          "first_name": "string", // This may be considered PII
          "agent_number": "string", // This may be considered PII
          "avatar_url": "string"
        }
      }
    ]
    

## Team list

Parameter | Required | Data Type | Definition  
---|---|---|---  
sort_column | FALSE | String | Sorts response based on any field in the response object.  
sort_direction | FALSE | ASC or DESC | Notes the direction of the sort, whether ascending or descending  
page | FALSE | String | Pairs with per to note what page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.  
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.  
agents_count[from] | FALSE | Number | creates a lower bound of the agents count field. All records returned will be after the inputted value.  
agents_count[to] | FALSE | Number | creates a upper bound of the agents count field. All records returned will be before the inputted value.  
id[] | FALSE | Array[String] | Array[Strings]. Id of records to search and return  
name[] | FALSE | Array[String] | Returns records based on name of resource.   
parent_id[] | FALSE | Array[String] | Returns records based on the parent id of the given records  
position[] | FALSE | Array[String] | Returns records based on what position a menu is in  
with_deleted | FALSE | Boolean | Returns records that have been deleted (True) or not including records that have been deleted (False)  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/teams
    

**_More example Requests/Responses:_**

### Example request: Team list

**_Body: None_**

### Example Response: Team list
    
    
    [
      {
        "id": 11,
        "name": "Forest Moon of Endor Team",
        "parent_id": null,
        "position": 28,
        "agents_count": 3,
        "deleted": false,
        "assignees": [
          {
            "id": 19,
            "agent_number": "77",
            "name": "Storm Trooper 1",
            "last_name": "Storm",
            "first_name": "Trooper 1"
          },
          {
            "id": 20,
            "agent_number": "78",
            "name": "Storm Trooper 2",
            "last_name": "Storm",
            "first_name": "Trooper 2"
          },
          {
            "id": 21,
            "agent_number": "79",
            "name": "Storm Trooper 3",
            "last_name": "Storm",
            "first_name": "Trooper 3"
          }
        ]
      },
      {
        "id": 12,
        "name": "Death Star Team",
        "parent_id": null,
        "position": 28,
        "agents_count": 3,
        "deleted": false,
        "assignees": [
          {
            "id": 34,
            "agent_number": "80",
            "name": "Storm Trooper 5",
            "last_name": "Storm",
            "first_name": "Trooper 5"
          },
          {
            "id": 35,
            "agent_number": "81",
            "name": "Storm Trooper 6",
            "last_name": "Storm",
            "first_name": "Trooper 6"
          },
          {
            "id": 36,
            "agent_number": "82",
            "name": "Storm Trooper 7",
            "last_name": "Storm",
            "first_name": "Trooper 7"
          }
        ]
      }
    ]
    

**_Status Code:_** 200

## Single team

Parameter | Required | Data Type | Definition  
---|---|---|---  
record_id | FALSE | String | Returns specific record based on id  
with_deleted | FALSE | Boolean | Returns records that have been deleted (True) or not including records that have been deleted (False)  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/teams/{​{team_id}​}
    

**_More example Requests/Responses:_**

### Example request: Single team

**_Body: None_**

### Example response: Single team
    
    
        {
            "id": 11,
            "name": "Forest Moon of Endor Team",
            "parent_id": null,
            "position": 28,
            "agents_count": 3,
            "deleted": false,
            "assignees": [
                {
                    "id": 19,
                    "agent_number": "77",
                    "name": "Storm Trooper 1",
                    "last_name": "Storm",
                    "first_name": "Trooper 1"
                },
                {
                    "id": 20,
                    "agent_number": "78",
                    "name": "Storm Trooper 2",
                    "last_name": "Storm",
                    "first_name": "Trooper 2"
                },
                {
                    "id": 21,
                    "agent_number": "79",
                    "name": "Storm Trooper 3",
                    "last_name": "Storm",
                    "first_name": "Trooper 3"
                }
            ]
        }
    

**_Status Code:_** 200

## Team tree

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/teams/tree
    

**_More example Requests/Responses:_**

### Example request: Team tree

**_Body: None_**

### Example response: Team tree
    
    
    [
      {
        "id": 147,
        "name": "Storm Trooper Reigment",
        "parent_id": null,
        "position": 1,
        "agents_count": 9,
        "deleted": false,
        "children": [
          {
            "id": 34,
            "name": "Storm Trooper 1st Regiment",
            "parent_id": 147,
            "position": 1,
            "agents_count": 2,
            "deleted": false,
            "children": []
          }
        ]
      }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
