---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/callback-call-api/
title: Callback call API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:00.048913+00:00
---

# Callback call API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/callback-call-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Callback call API Stay organized with collections  Save and categorize content based on your preferences. 

Callback calls are calls that are requested by an end-user. With the callback call API, you can programmatically schedule callback calls and cancel scheduled calls. With these capabilities, you can create applications that let end-users request callback calls from a queue that you specify. End-users can also cancel calls that they previously scheduled. For information about authentication with the callback call API, see [Basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic_authentication).

## Use the callback call API

You can use the callback call API to schedule callback calls and cancel scheduled calls.

### Schedule a call

If your instance is integrated with Salesforce, check the **Closed record options when initiating an API-scheduled call** setting under **Settings > Operation Management > CRM Record Creation Details**. Scheduling requests are rejected with `422` while **Don't check the record status** is selected. This does not apply to Zendesk or ServiceNow.

To schedule a call, call `POST https://<subdomain>.<domain>/apps/api/v1/calls` and include a request body similar to the following:
    
    
    {
        "call_type": "ScheduledCall",
        "menu_id": 12345,
        "end_user_number": "+18005550100",
        "scheduled_at": "2025-09-02T14:30:00Z"
    }
    

A successful request returns a call object, including the call ID.

### Cancel a scheduled call

To cancel a scheduled call, call `PATCH https://<subdomain>.<domain>/apps/api/v1/calls/scheduled/{id}/cancel`. Specify the ID of the call that you want to cancel.

A successful request returns information about the canceled call.

**Note:** The `user_type` (string, required) - who is canceling: `agent` or `end_user` is a required field. Omitting it returns 400. The value is recorded as the cancellation reason.

### Cancel multiple scheduled calls

To cancel multiple scheduled calls, call `PATCH https://<subdomain>.<domain>/apps/api/v1/calls/scheduled/cancel`. Include a request body that contains a `call_ids` array of the call IDs, as integers, for the calls to be canceled. A value that is not an array, or that contains a non-integer entry, is rejected with `400`.

See the following code sample:
    
    
    {
        "call_ids": [123, 456, 789],
        "user_type": "end_user"
    }
    

Bulk cancel requires `user_type` exactly as the aforementioned single-cancel endpoint does.

The `user_type` (string, required) accepts either `agent` or `end_user`.

**Note:** `call_ids` (array of integers, required) - the scheduled call IDs to cancel (maximum 1,000). A value that is not an array, contains a non-integer entry, or lists more than 1,000 IDs is rejected with 400.

A successful request returns a response with a response header that contains a `Location` URL for checking the status of the cancellation.

## Use callback calls with CRMs

You can use the callback calls API with Salesforce, Zendesk, and ServiceNow CRM integrations.

### General callback behavior

If you're using any supported CRM (such as Salesforce), the following conditions affect scheduled callback behavior:

  * **A record is open and already has an active scheduled call** : If a ticket ID lookup indicates that the record is open and already has an active scheduled call, the call isn't scheduled. The following comment is attached to the CRM record: `A scheduled call was not created because the record already has an active scheduled call`.

  * **The CRM can't be reached** : If a ticket ID lookup indicates that the CRM can't be reached, the call is canceled. The following comment is attached to the CRM record: `A scheduled call was canceled because the CRM was unreachable`.

  * **A record is closed**.




### Callback calls with Salesforce

If you've integrated CCAI Platform with [Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide), you can configure how your instance handles scheduled calls for closed records. Here are the configuration options for Salesforce integrations:

  * Don't check the record status.

  * Check the record status and reopen closed records.

  * Check the record status and cancel scheduled calls for closed records.


**Note:** Ticket ID lookup for checking record status takes place five minutes before the scheduled call countdown begins. The scheduled call countdown is the number of minutes between the time that a call is assigned to an agent and the time that the scheduled call begins. For more information, see [Configure scheduled calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure_scheduled_calls).

#### Don't check the record status

You can configure CCAI Platform so that it doesn't check the record status before making a scheduled call. While this option is selected, requests to schedule a call through the callback call API are rejected with `422`.

To configure CCAI Platform to not check the record status, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Record Creation Details > Closed record options when initiating an API-scheduled call**.

  3. Select **Don't check the record status. Always initiate the API-scheduled call**.

  4. Click **Save General**.




#### Check the record status and reopen closed records

You can configure CCAI Platform to check the record status before making a scheduled call and reopen records that are closed. With this configuration, if the record status is closed, the following actions take place:

  * The call is made as scheduled.

  * The record is reopened.

  * The following comment is attached to the CRM record: `The record was reopened at the time of a scheduled call`.




To configure CCAI Platform to check the record status and reopen closed records, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Record Creation Details > Closed record options when initiating an API-scheduled call**.

  3. Select **Check the record status. If the record is closed > Reopen the record**.

  4. Click **Save General**.




#### Check the record status and cancel scheduled calls for closed records

You can configure CCAI Platform to check the record status before making a scheduled call and cancel scheduled calls for records that are closed. With this configuration, if the record status is closed, the following actions take place:

  * The scheduled call is canceled.

  * The following comment is attached to the CRM record: `A scheduled call was canceled because the record is closed`.




To configure CCAI Platform to check the record status and cancel scheduled calls for closed records, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Record Creation Details > Closed record options when initiating an API-scheduled call**.

  3. Select **Check the record status. If the record is closed > Cancel the scheduled call**.

  4. Click **Save General**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
