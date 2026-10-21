---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-email-status-endpoint/
title: Bulk email status endpoint \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:07.546959+00:00
---

# Bulk email status endpoint  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-email-status-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Bulk email status endpoint Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the bulk email status endpoint: `POST /apps/api/v1/email/update_status`. You can use this endpoint to change the status of up to 100 email sessions to a status that you specify. For each email session that you specify, the response reports whether it was updated, required no change, or couldn't be updated, along with the reason. This means that integrations can handle partial success and identify which sessions still need attention.

The bulk email status endpoint supports the following use cases:

  * You manage a high-volume email queue and need to pause, resolve, or close many sessions at once.

  * You run an external workflow that transitions email sessions based on business rules—for example, pausing a batch of sessions during an after-hours window.

  * You want a single operation that reports the outcome of each email session so your integration can retry or reconcile the sessions that didn't transition to a new status.




## Authentication

To authenticate, see [Basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic-authentication).

## How to use the endpoint

To call the bulk email status endpoint, you specify a target status and a list of session IDs for the email sessions whose status you want to update. You can specify only one target status per request. To update sessions to a different status, send a separate request.

Session status can be updated only for email sessions within the instance that owns the API token. A session ID for an email session that isn't in the instance is marked with `"result": "failure"` and `"reason": "not_found"`.

Transitioning a session to `closed` can trigger configured CRM synchronization for those sessions.

For information about getting session IDs for the email sessions you want to update, see [Get email sessions and messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-email-sessions-and-messages).

### Valid status transitions

When you specify the target status, you can transition only from a valid source status to the target status. Any session whose current status isn't a valid source for the target won't change status and will be marked with `"reason": "invalid_transition"`.

The following table shows the target statuses that you can specify and the valid source statuses for each target:

Target status | Valid source statuses  
---|---  
`active` | `unopened`, `reopened`, `paused`  
`paused` | `active`  
`resolved` | `active`  
`closed` | `paused`, `resolved`  
  
## Update email session status

To update email session status, send a `POST` request to the following endpoint:
    
    
    https://YOUR_CCAAS_HOST/apps/api/v1/email/update_status
    

Include a request body with the following structure:
    
    
    {
      "session_ids": [
        "SESSION_ID"
      ],
      "new_email_status": "NEW_EMAIL_STATUS"
    }
    

Replace the following:

  * `YOUR_CCAAS_HOST`: your CCAI Platform host.

  * `SESSION_ID`: a string array of up to 100 email session IDs—for example, `["123", "456", "789"]`. Empty values are rejected.

  * `NEW_EMAIL_STATUS`: the target status applied to every session in the request. Possible values: `active`, `paused`, `resolved`, or `closed`.




Optional: To guard against updating session status for email sessions that changed after you last read them, include the following field in the request body:
    
    
    {
      "existing_email_status": "EXISTING_EMAIL_STATUS"
    }
    

Replace `EXISTING_EMAIL_STATUS` with one of the following statuses: `unopened`, `active`, `paused`, `resolved`, `closed`, or `reopened`. If you include `existing_email_status` and a session isn't in this status, it fails with reason `stale_state`.

The output is similar to the following:
    
    
    {
      "results": [
        { "session_id": "123", "from_status": "active", "to_status": "paused", "result": "success" },
        { "session_id": "456", "result": "failure", "reason": "invalid_transition", "current_status": "closed" },
        { "session_id": "789", "result": "noop", "current_status": "paused" }
      ]
    }
    

### Response fields

The `results` array contains the following fields:

  * `session_id`: the ID of a session that the request targets.

  * `from_status`: the status of the session before the update.

  * `to_status`: the status of the session after the update.

  * `result`: the outcome of the update. Possible values:

    * `success`: the session status was updated. The result includes `from_status` and `to_status`.

    * `failure`: the session status wasn't updated. The result includes `reason` and `current_status`.

    * `noop`: the session was already in the target status, so no update was needed. The result includes `current_status`.

  * `reason`: the reason a status update failed. Possible values:

    * `not_found`: no email session in your instance matches the specified session ID. Retrying won't succeed.

    * `invalid_transition`: the session's current status isn't a valid source status for the specified target status.

    * `stale_state`: you included `existing_email_status` and the session's current status didn't match.

    * `internal_error`: an unexpected error occurred. You can retry the request.

  * `current_status`: the session's status when the request was processed.




### Error messages

The bulk email status endpoint returns the following error messages:

  * `400 Bad Request`: the request body is malformed, `session_ids` is missing or empty, `session_ids` exceeds 100 elements, `new_email_status` is missing or not an accepted status, or `existing_email_status` isn't a valid status.

  * `401 Unauthorized`: authentication failed or the credential isn't an `ApiUser` token.

  * `404 Not Found`: the endpoint isn't available on your instance.




## What's next

  * [Get email sessions and messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-email-sessions-and-messages): locate the sessions that you want to update by querying email interaction records.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
