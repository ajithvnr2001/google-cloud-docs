---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-session-events/
title: External session events \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:28.623514+00:00
---

# External session events  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-session-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  External session events Stay organized with collections  Save and categorize content based on your preferences. 

The external session events capability enables real-time data streaming from the CCAI Platform to your external systems using webhooks. This provides immediate visibility into session lifecycles for custom reporting, CRM record updates, or automated post-interaction workflows.

External session events provide a push-based mechanism to notify your server whenever a chat or voice call changes state. By providing an API endpoint, the CCAI Platform will POST JSON-formatted event data to your infrastructure as transitions occur—for example, call connected, agent assigned, session disconnected.

## Configure external session events

To configure external session events, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Session Data Export** pane, click **Manage Data Export Settings**. The **Session Data Export** page appears.

  3. Go to the **External Session Events** pane, and then click the toggle to the on position.

  4. Do one or both of the following:

     * To configure external call session events, do the following:

       1. Select the **Call events - Send call sessions event** checkbox.

       2. In the **API Endpoint** field, enter the full HTTPS URL of your target API.

       3. Enter the username and password. The platform uses these for basic authentication.

     * To configure external chat session events, do the following:

       1. Select the **Chat events - Send chat sessions event** checkbox.

       2. In the **API Endpoint** field, enter the full HTTPS URL of your target API.

       3. Enter the username and password. The platform uses these for basic authentication.

  5. Click **Save**.




## Event lifecycle and state logic

As a session progresses, CCAI Platform sends multiple updates. Each update enriches the `item` object with more metadata as it becomes available.

### State progression table

Event order | State | Participant status | Key data points added  
---|---|---|---  
**1\. Start** | `connected` | External: `connected` | `call_id`, Customer `dn` (phone number).  
**2\. Routing** | `connected` | External: `connected` | `queue_path_names`, `initiator` (Virtual Agent).  
**3\. Assigned** | `connected` | Agent: `accepted` | Live agent name and ID are added.  
**4\. Active** | `connected` | Agent: `connected` | Media stream established (conversation starts).  
**5\. End** | `disconnected` | Both: `disconnected` | `ends_at` timestamp is populated.  
**6\. Final** | `disconnected` | Agent: `dispositionSubmitted` | `dispositions` object containing wrap-up codes.  
  
## Event data schema reference

Events are sent to the webhook in an object. Each webhook event has the same structure, which is shown in the following table:

### Root object

Field | Type | Description  
---|---|---  
`count` | Integer | Number of event objects in the current payload.  
`events` | Array | A collection of event objects containing session details.  
  
### Key session fields

  * **`event_id`** : A UUID for the event notification.
  * **`timestamp`** : Epoch time in milliseconds for when the event was generated.
  * **`connected_at`** and **`ends_at`** : ISO 8601 timestamps for the session duration.
  * **`initiator`** : Identifies the entity that handled the state change—for example, `virtual_agent_15` or `agent_1`.
  * **`dispositions`** : A nested object containing `code`, `custom_code_id`, and any agent `note`.



## Security

All requests are sent with a standard Authorization header: `Authorization: Basic <base64_encoded_credentials>`

## Delivery requirements

  * **Method:** `POST`
  * **Content-Type:** `application/json`
  * **Timeout:** Your server should respond within five seconds.
  * **Acknowledgement:** Your endpoint must return a `200 OK` status code. The platform might use exponential backoff retries if a non-200 code is received.



## Sample payloads

The following are sample payloads received in event messages to the webhook.

### Active conversation (media connected)
    
    
    {
      "count": 1,
      "events": [
        {
          "event_id": "fc066edb-d99f-4db4-ba04-fb5dfea0e86a",
          "timestamp": 1767874769480,
          "type": "CallState",
          "item": {
            "call_id": 1395,
            "state": "connected",
            "queue_path_names": "Test/Talk to Andrew/English",
            "participants": [
              { "state": "connected", "type": "external", "dn": "+15555555555" },
              { "state": "connected", "type": "agent", "name": "Joe Smith", "agent_number": "528431" }
            ]
          }
        }
      ]
    }
    
    

### Final disposition (post-call work)
    
    
    {
      "count": 1,
      "events": [
        {
          "event_id": "479798ff-b1ed-4a5c-a910-17a7edb3f283",
          "timestamp": 1767874769480,
          "type": "CallState",
          "item": {
            "call_id": 1395,
            "state": "disconnected",
            "participants": [
              {
                "type": "agent",
                "state": "dispositionSubmitted",
                "dispositions": {
                  "code": "Call completed",
                  "custom_code_id": "callComplete",
                  "note": "none"
                }
              }
            ]
          }
        }
      ]
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
