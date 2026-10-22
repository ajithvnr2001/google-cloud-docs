---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-endpoints/
title: Queue endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:17.996518+00:00
---

# Queue endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The queue status endpoints return queue information to determine whether to deflect a call.

## Queue status

Provides real-time data for leaf queues, including estimated wait times, agent availability, callback slot capacity, hours of operation, and holidays. Use this to let voice AI systems dynamically decide whether to escalate a call to a live agent or offer scheduled callback windows to the caller. For more information, see [The queue status endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-status-endpoint).

### Example request

Method: `GET`

URL: `https://{subdomain}.{domain}/apps/api/v1/queues/status`

#### Headers

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
#### Query

Key | Value | Description  
---|---|---  
lang | string | The two-letter language code for the queue, in ISO 639-1 format (for example, `en` or `es`). Required.  
menu_id[] | string | A single queue ID or an array of multiple queue IDs. Required.  
menu_type | string | The menu type. Possible values are `ivr_menu`, `mobile_menu`, and `web_menu`. Required.  
callback_period_hours | integer | The total future window length in hours for which to return callback-slot periods. Must be between 1 and 24. If omitted, a default 4-hour window is used, unless capacity-based scheduling is enabled for your account. Optional.  
callback_start_from | string | The start of the callback-slot search window, in ISO 8601 datetime format in the queue or company timezone. If omitted, defaults to the current time (server time converted to queue or company timezone). Must not be in the past. Optional.  
  
### Example response
    
    
    {
        "queues": [
            {
                "menu_id": 2,
                "menu_type": "ivr_menu",
                "lang": "en",
                "materialized_path": "IVR Support",
                "current_queue_ewt": 18000,
                "scheduled_callback_ewt": 0,
                "logged_in_agents": 0,
                "available_agents": 0,
                "breakthrough_agents": 0,
                "callback_periods": [
                    {
                        "date": "20260225",
                        "start_time": "17:30",
                        "end_time": "17:45",
                        "scheduled_calls": 0,
                        "max_slots": 1,
                        "available_slots": 1
                    },
                    {
                        "date": "20260225",
                        "start_time": "17:45",
                        "end_time": "18:00",
                        "scheduled_calls": 0,
                        "max_slots": 1,
                        "available_slots": 1
                    }
                ],
                "hoops": {
                    "current_status": 0,
                    "time_zone": "America/Los_Angeles",
                    "start_of_hoops": "2026-02-25T09:00:00-08:00",
                    "end_of_hoops": "2026-02-25T18:00:00-08:00",
                    "hoops_early_cutoff_minutes": null
                },
                "holiday": {
                    "current_status": 0,
                    "holiday_name": null,
                    "time_range_all_day": null,
                    "time_range_start_time": null,
                    "time_range_end_time": null,
                    "time_zone": "America/Los_Angeles"
                }
            }
        ]
    }
    

## Queue availability

Get availability status for a queue before you deflect a session to it. This endpoint returns the following boolean properties:

  * `after_hours`: `true` if the queue is unavailable because it's in an after hours state

  * `overcapacity`: `true` if the queue is unavailable because it's in an overcapacity state




### Example request

Method: `GET`

URL: `https://{subdomain}.{domain}/apps/api/v1/queue_operation_statuses`

#### Query

Key | Value | Description  
---|---|---  
menu_id | integer | The ID for the queue that you want availability information for. Required.  
lang | string | The two-letter language code for the queue, in ISO 639-1 format. Required.  
channel_type | string | The channel type. Possible values are `call` and `chat`. Required.  
  
### Example response
    
    
    {
      "menu_id": 1,
      "lang": "en",
      "channel_type": "call",
      "after_hour": false,
      "overcapacity": true
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
