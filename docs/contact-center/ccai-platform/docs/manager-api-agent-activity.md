---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-agent-activity/
title: Agent activity endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:53:07.203150+00:00
---

# Agent activity endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-agent-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent activity endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Agent activity logs are records created at any time the widget's state has changed. It can be from logging into the widget, getting a deltacast call notification, or accepting a call among other statuses. Each activity creates a new new object. Refer to the following model to verify which fields might contain (PII).:
    
    
    [
      {
        "id": 0,
        "agent_id": 0,
        "whodunnit": {
          "id": 0,
          "name": "string",
          "last_name": "string",
          "first_name": "string",
          "agent_number": "string",
          "avatar_url": "string"
        },
        "status": {
          "id": 0,
          "name": "string",
          "color": "string"
        },
        "started_at": "2018-06-06T21:12:24.766Z",
        "ended_at": "2018-06-06T21:12:24.766Z",
        "duration": 0,
        "activity": "login",
        "call_id": 0,
        "chat_id": 0
      }
    ]
    

The following table contains a summary of every activity that can result in an an activity log being created. 

Activity | Description  
---|---  
chat_picked_up | Event that occurs when an agent picks up an agent  
chat_pick_up_attempt | Event that occurs when an agent attempts to become the responding agent  
chat_notification_offered | Event that occurs once an end user request a chat session and a notification is sent to agents assigned to that queue.   
call_notification_offered | Event that occurs when an end user calls and a multicast or deltacast call notification is offered to the agent.  
call_pick_up_attempt | Event that occurs when an agent attempts to pick up a multicast or deltacast call.   
call_picked_up | Event that occurs when an agent answers a multicast or deltacast call.   
deltacast_call_notification_offered | Event that notes that an end user has called into a queue with multicast where a deltacast call is then broadcasted to an agent in that queue.  
deltacast_call_pick_up_attempt | Event that occurs when an agent tries to answer a deltacsted call  
deltacast_call_picked_up | Event that occurs when an agent successfully answers a deltacasted call.  
deltacast_call_missed | Event that occurs when an agent does not answer their deltacasted call  
multicast_call_notification_offered | Event that notes that an end user has called into a queue with multicast where a multicast call is then broadcasted to the agents in that queue  
multicast_call_pick_up_attempt | Event that occurs when a multicasted call has been attempted to be answered by an agent  
multicast_call_picked_up | Event that occurs when a multicasted call has been answered by an agent  
call_outbound_dialing | Event that occurs when an agent uses the dial pad in the widget to call an end user.  
user_status_changed | Event that occurs when an agent changes the state their widget is in   
login | Event that occurs when an agent logs out of the widget   
logout | Event that occurs when an agent logs into the widget  
  
## Agent activity logs

Parameter | Required | Data Type | Definition  
---|---|---|---  
sort_column | FALSE | String | Sorts response based on any field in the response object.   
sort_direction | FALSE | ASC or DESC | Notes the direction of the sort, whether ascending or descending  
page | FALSE | String | Pairs with per to note what page of records. For example, if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
started_at[from] | FALSE | Time in UTC | creates a lower bound of the started at field. All records returned will be after the inputted value.  
started_at[to] | FALSE | Time in UTC | creates a upper bound of the started at field. All records returned will be before the inputted value.  
ended_at[from] | FALSE | Time in UTC | creates a lower bound of the ended at field. All records returned will be after the inputted value.  
ended_at[to] | FALSE | Time in UTC | creates a upper bound of the ended at field. All records returned will be before the inputted value.  
duration[from] | FALSE | Number | creates a lower bound of the duration field. All records returned will be after the inputted value.  
duration[to] | FALSE | Number | creates a upper bound of the duration field. All records returned will be before the inputted value.  
id[] | FALSE | Array[String] | Array[Strings]. Id of records to search and return  
agent_id[] | FALSE | Array[String] | Filters response by agent id  
activity[] | FALSE | Array[String] | filters records by what task/activity the agent has accomplished. The possible values are: login, logout, call_outbound_dialing, deltacast_call_notification_offered, deltacast_call_pick_up_attempt, deltacast_call_picked_up, deltacast_call_projected, deltacast_call_missed, deltacast_call_bounced, multicast_call_notification_offered, multicast_call_pick_up_attempt, multicast_call_picked_up, user_status_changed, chat_notification_offered, chat_pick_up_attempt, chat_picked_up  
whodunnit_id[] | FALSE | Array[String] | Filters response by agent id. Whodunnit is a subset of the agent object, and uses the same agent_id as its primary key   
call_id[] | FALSE | Array[String] | Filters records by inputted call id's  
chat_id[] | FALSE | Array[String] | Filters records by inputted chat id's  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/agent_activity_logs
    

**_More example Requests/Responses:_**

### Example request: Agent activity logs example

**_Body: None_**

### Example response: Agent activity logs example
    
    
    [
        {
            "id": 190578,
            "agent_id": 118,
            "status": {
                "id": -10,
                "name": "Offline",
                "color": "grey",
            },
            "started_at": "2017-12-22T00:54:18.000Z",
            "ended_at": null,
            "duration": 0,
            "call_id": null,
            "chat_id": null,
            "activity": "logout",
            "whodunnit": null
        },
        {
            "id": 199548,
            "agent_id": 118,
            "status": {
                "id": -10,
                "name": "Offline",
                "color": "grey",
            },
            "started_at": "2018-01-09T22:54:26.000Z",
            "ended_at": null,
            "duration": 0,
            "call_id": null,
            "chat_id": null,
            "activity": "logout",
            "whodunnit": null
        },
        {
            "id": 190577,
            "agent_id": 118,
            "status": {
                "id": -10,
                "name": "Offline",
                "color": "grey",
            },
            "started_at": "2017-12-22T00:54:18.000Z",
            "ended_at": "2018-01-08T22:54:22.000Z",
            "duration": 1548004,
            "call_id": null,
            "chat_id": null,
            "activity": "user_status_changed",
            "whodunnit": null
        },
        {
            "id": 199547,
            "agent_id": 118,
            "status": {
                "id": -10,
                "name": "Offline",
                "color": "grey",
            },
            "started_at": "2018-01-09T22:54:26.000Z",
            "ended_at": null,
            "duration": 0,
            "call_id": null,
            "chat_id": null,
            "activity": "user_status_changed",
            "whodunnit": null
        },
        {
            "id": 190270,
            "agent_id": 118,
            "status": {
                "id": -1,
                "name": "Unavailable",
                "color": "red",
            },
            "started_at": "2017-12-21T21:34:14.000Z",
            "ended_at": "2017-12-22T00:54:18.000Z",
            "duration": 12004,
            "call_id": null,
            "chat_id": null,
            "activity": "user_status_changed",
            "whodunnit": null
        },
        {
            "id": 198036,
            "agent_id": 118,
            "status": {
                "id": -1,
                "name": "Unavailable",
                "color": "red",
            },
            "started_at": "2018-01-08T22:54:22.000Z",
            "ended_at": "2018-01-09T22:54:26.000Z",
            "duration": 86404,
            "call_id": null,
            "chat_id": null,
            "activity": "user_status_changed",
            "whodunnit": null
        },
        {
            "id": 22249,
            "agent_id": 129,
            "status": {
                "id": -10,
                "name": "Offline",
                "color": "grey",
            },
            "started_at": "2017-06-19T18:34:39.000Z",
            "ended_at": null,
            "duration": 0,
            "call_id": null,
            "chat_id": null,
            "activity": "login",
            "whodunnit": null
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
