---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-codes-api/
title: Disposition codes API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:23.255872+00:00
---

# Disposition codes API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-codes-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Disposition codes API Stay organized with collections  Save and categorize content based on your preferences. 

The disposition codes API lets your integration do the following:

  * Get disposition code lists for an instance, a queue, or a session.

  * Update the disposition codes or notes (or both) for a previously completed call or chat session.




## Authentication and base URL

All endpoints in this document use standard API token authentication using an API user token (bearer token).

Base URL: `https://SUBDOMAIN.REGION_CODE.ccaiplatform.com`

## Get disposition code list

Get the available disposition codes. You can query at the instance, queue, and session level.

### By instance

Returns the complete disposition code tree for the instance, including all multi-level disposition codes.

**Request example**

The following request gets the full list of disposition codes:
    
    
    GET /api/v1/disposition_codes
    Authorization: Bearer {token}
    Content-Type: application/json
    

**Response example**

The following example response shows the full list of disposition codes:
    
    
    {
      "disposition_codes": [
        {
          "id": 1,
          "name": "Issue Resolved",
          "full_path": "/Support/Issue Resolved",
          "children": []
        },
        {
          "id": 2,
          "name": "Escalated",
          "full_path": "/Support/Escalated",
          "children": [
            {
              "id": 3,
              "name": "Tier 2",
              "full_path": "/Support/Escalated/Tier 2",
              "children": []
            }
          ]
        }
      ]
    }
    

### By queue

Returns the disposition codes assigned to a queue. If no queue-specific list is configured, the global (instance-level) list is returned.

**Request example**

The following request gets disposition codes for a queue:
    
    
    GET /api/v1/disposition_codes?queue_id=QUEUE_ID
    Authorization: Bearer TOKEN
    Content-Type: application/json
    

**Query parameters**

Parameter | Type | Required | Description  
---|---|---|---  
`queue_id` | integer | Yes | The ID of the queue to get disposition codes for.  
  
### By session

Returns the disposition codes available for a given session ID, based on the last queue that the session was routed through.

**Request example**

The following request gets disposition codes for a session:
    
    
    GET /api/v1/disposition_codes?session_id=SESSION_ID
    Authorization: Bearer TOKEN
    Content-Type: application/json
    

**Query parameters**

Parameter | Type | Required | Description  
---|---|---|---  
`session_id` | integer | Yes | The session ID.  
  
## Update disposition code and notes

Submit an updated disposition code or notes (or both) for a previously completed call or chat session. This creates a new disposition record and CRM note. It doesn't edit the original CRM record.

**Request example**

The following request updates the disposition code or notes for a session:
    
    
    POST /api/v1/sessions/SESSION_ID/disposition
    Authorization: Bearer TOKEN
    Content-Type: application/json
    

**Path parameters**

Parameter | Type | Required | Description  
---|---|---|---  
`session_id` | integer | Yes | The session ID of the call or chat to update.  
  
**Request body example**

The following example shows a request body:
    
    
    {
      "disposition_code": {
        "id": 5,
        "full_path": "/Support/Verification/Pending Documents"
      },
      "notes": "Customer must upload documents via portal."
    }
    

**Request body parameters**

Parameter | Type | Required | Description  
---|---|---|---  
`disposition_code` | object | Conditional | The updated disposition code. At least one of `disposition_code` or `notes` must be present.  
`disposition_code.id` | integer | Yes (if `disposition_code` specified) | The disposition code ID.  
`disposition_code.full_path` | string | Yes (if `disposition_code` is specified) | The full hierarchical path of the disposition code, for example, `/Support/Verification/Pending Documents`. Used for validation against the session's disposition tree.  
`notes` | string | No | The updated agent notes. See the **Notes behavior** table.  
  
### Notes behavior

Value | Behavior  
---|---  
**Present with text** , for example, `"notes": "Updated notes"` | Replaces the existing note with the new text.  
**Present as empty string** ("notes": "") | Explicitly clears the existing note. The session metadata file will no longer carry the note. CRM history retains prior records.  
**Omitted** (field absent from request) | Leaves the existing note unchanged.  
  
### Do not call (DNC) disposition

To submit a "Do Not Call" disposition, use `disposition_code.id: -1`. This is only accepted when the instance has the do not call feature enabled and a DNC disposition is configured. Otherwise, the API returns `422 Unprocessable Entity` with the message: "Do Not Call disposition is not enabled for this tenant."

### Agent attribution

The API doesn't carry an agent identity. The system attributes the disposition to the following, in order of priority:

  1. The agent who originally submitted the disposition for this session.

  2. If no original disposition exists, the most recent agent participant on the call or chat.




If neither exists, the API returns `422 Unprocessable Entity`.

### Validation

The following list describes the validation rules:

  * The session's call or chat must have ended. Attempting to update disposition on an active session returns `422 Unprocessable Entity`.

  * The `disposition_code.id` and `disposition_code.full_path` parameters are validated against the session's disposition tree (based on the queue the session was last routed through).

  * The `allow_disposition_edit` administrator setting is a UI-only control. The public API can always update disposition data regardless of this setting.




**Response example**

The following example shows a response to a successful request:
    
    
    {
      "session_id": 12345,
      "disposition": {
        "id": 5,
        "name": "Verification Pending",
        "full_path": "/Support/Verification/Pending Documents",
        "notes": "Customer must upload documents via portal.",
        "submitted_at": "2026-03-13T10:15:01Z"
      }
    }
    

**Note** : The `name` field is resolved by the server from the disposition tree based on the specified `id` and `full_path` values. It is returned in the response for convenience.

### Session metadata

When a disposition is updated using this API, the following takes place:

  * **External storage** : The session metadata file is regenerated and overwrites the existing metadata file.

  * **CRM** : A new note is created, preserving the audit trail.




## Error handling

This section describes error handling.

### Common status codes

Status | Condition | Example Message  
---|---|---  
`400 Bad Request` | Missing required fields (`disposition_code` and `notes` both absent), or invalid format. | "At least one of disposition_code or notes must be present."  
`401 Unauthorized` | Invalid or missing API token. | "Unauthorized"  
`403 Forbidden` | The API user doesn't have access to the specified session or tenant. | "Forbidden"  
`404 Not Found` | Session not found or doesn't exist. | "Session not found."  
`422 Unprocessable Entity` | Various validation failures. See the **422 Unprocessable entity scenarios** table. | See the **422 Unprocessable entity scenarios** table.  
  
### 422 Unprocessable entity scenarios

Scenario | Error Message  
---|---  
Call or chat session is still active | "Session has not ended. Disposition can only be updated for completed sessions."  
Disposition code ID not found in the session's tree | "Disposition code is invalid for this session's queue."  
DNC disposition submitted but feature is not enabled | "Do Not Call disposition is not enabled for this tenant."  
No agent participant can be resolved for attribution | "Unable to determine agent for disposition attribution."  
  
**Response example**

The following example shows an error response:
    
    
    {
      "error": {
        "code": "session_not_ended",
        "message": "Session has not ended. Disposition can only be updated for completed sessions.",
        "details": {
          "session_id": 12345
        }
      }
    }
    

## Typical integration flow

The following is a typical integration flow:

  1. Get disposition codes for the relevant queue or session:

     * `GET /api/v1/disposition_codes?session_id=SESSION_ID`
  2. Present the disposition tree to the user or automated system for selection.

  3. Submit the updated disposition:

     * `POST /api/v1/sessions/SESSION_ID/disposition`

     * Include the selected disposition_code, with `id` and `full_path`, and any notes.

  4. Handle the response:

     * On 200 OK: The disposition has been updated. CRM records are updated automatically.

     * On error: Display the error message and retry or escalate as appropriate.




## CRM behavior

When a disposition is submitted using this API, the following occurs:

  * A new CRM note is created in the connected CRM, such as Salesforce, ServiceNow, Zendesk, Dynamics, or HubSpot. The original note isn't modified.

  * For external storage, the session metadata file is overwritten with the updated disposition data.




### Limitation

HubSpot call engagements include a scalar `hs_call_disposition` property that is overwritten (not appended) on each disposition update. While the full history is preserved in HubSpot notes, the engagement property only reflects the most recent disposition code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
