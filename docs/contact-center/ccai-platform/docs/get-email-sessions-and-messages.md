---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-email-sessions-and-messages/
title: Get email sessions and messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:00.946381+00:00
---

# Get email sessions and messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-email-sessions-and-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Get email sessions and messages Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform (CCAI Platform), you can programmatically retrieve email sessions and messages. This can be useful in the following cases:

  * Running an external orchestration or automation workflow that needs to read the content of an inbound email to make content-aware routing or handling decisions.

  * Pulling the sender, subject, body, or attachment details of an email into a downstream system.

  * Enumerating the individual messages in an email conversation and then getting one of them.




Use the following read-only endpoints to get email sessions and messages:

  * **Get an email session** (`GET /apps/api/v1/email/sessions/EMAIL_SUPPORT_ID`). Returns email session summary information and a list of message IDs with metadata. To get the full content of a message, use its `email_thread_id` in a subsequent call to the **Get an email message** endpoint.

  * **Get an email message** (`GET /apps/api/v1/email/messages/EMAIL_THREAD_ID`). Returns the full content of a single message.




These endpoints use [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic-authentication). The endpoints return email information for the instance that the API credentials came from.

## Get an email session

Get email session summary information and a list of message IDs with metadata. Message IDs for draft messages aren't included. To get the full content of a message, use its `email_thread_id` in a subsequent call to the Get an email message endpoint.

To get an email session, follow these steps:

  1. Send a `GET` request to the following endpoint. Authenticate using [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic-authentication).
         
         https://YOUR_CCAAS_HOST/apps/api/v1/email/sessions/EMAIL_SUPPORT_ID
         

Replace the following:

     * `YOUR_CCAAS_HOST`. Your Contact Center AI Platform (CCAI Platform) host.

     * `EMAIL_SUPPORT_ID`. The email session identifier.

The following code sample shows a successful response:
    
    {
      "email_support_id": 12345,
      "status": "active",
      "created_at": "2026-03-25T09:30:00.000+00:00",
      "updated_at": "2026-03-25T10:15:00.000+00:00",
      "email_account_id": 42,
      "total_thread_numbers": 2,
      "email_threads": [
        {
          "email_thread_id": 67890,
          "message_id": "<CAE1234@mail.example.com>",
          "received_at": "2026-03-25T09:30:00.000+00:00",
          "direction": "inbound"
        },
        {
          "email_thread_id": 67891,
          "message_id": "<CAE5678@mail.company.com>",
          "received_at": "2026-03-25T09:45:00.000+00:00",
          "direction": "outbound"
        }
      ]
    }
    

Response fields:

     * `email_support_id`. The session identifier.

     * `status`. The status of the session. Values: `unopened`, `active`, `paused`, `resolved`, `closed`, and `reopened`.

     * `created_at`. The date the session was created.

     * `updated_at`. The date the session was last updated.

     * `email_account_id`. The mailbox identifier.

     * `total_thread_numbers`. The message (thread) count, excluding drafts.

     * `email_threads`. An array of email messages (threads) from the session. Each array element contains the following:

       * `email_thread_id`. The message identifier assigned by CCAI Platform.

       * `message_id`. The message identifier from the RFC 5322 header.

       * `received_at`. The time that the message was received.

       * `direction`. The direction of the message. Values: `inbound` and `outbound`.

  2. Use one of the `email_thread_id` values from the `email_threads` array for `EMAIL_THREAD_ID` in a subsequent call to the `/apps/api/v1/email/messages/EMAIL_THREAD_ID` endpoint. For more information, see Get an email message.




## Get an email message

Get the full content of a single email message.

To get an email message, send a `GET` request to the following endpoint. Authenticate using [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic-authentication).
    
    
    https://YOUR_CCAAS_HOST/apps/api/v1/email/messages/EMAIL_THREAD_ID
    

Replace the following:

  * `YOUR_CCAAS_HOST`. Your Contact Center AI Platform (CCAI Platform) host.

  * `EMAIL_THREAD_ID`. A message identifier returned by your previous call to the `/apps/api/v1/email/sessions/EMAIL_SUPPORT_ID` endpoint. For more information, see Get an email session.




The following code sample shows a successful response:
    
    
    {
      "email_thread_id": 67890,
      "email_support_id": 12345,
      "message_id": "<CAE1234@mail.example.com>",
      "direction": "inbound",
      "received_at": "2026-03-25T09:30:00.000+00:00",
      "from": "consumer@example.com",
      "from_name": "Jane Consumer",
      "to": ["support@company.com"],
      "cc": [],
      "bcc": [],
      "subject": "Order inquiry #98765",
      "body": "I have a question about my recent order...",
      "content_type": "text/plain; charset=utf-8",
      "attachment_count": 1,
      "email_attachments": [
        {
          "file_name": "receipt.pdf",
          "file_type": "application/pdf",
          "size_bytes": 45678,
          "url": null
        }
      ]
    }
    

Response fields:

  * `email_thread_id`. The message identifier assigned by CCAI Platform.

  * `email_support_id`. The session identifier.

  * `message_id`. The message identifier from the RFC 5322 header.

  * `direction`. The direction of the message thread. Values: `inbound` and `outbound`.

  * `received_at`. The time received.

  * `from`. The email address of the sender.

  * `from_name`. The name of the sender.

  * `to`. The email address in the email's **To** field.

  * `cc`. The email address in the email's **CC** field.

  * `bcc`. The email address in the email's **BCC** field.

  * `subject`. The email subject.

  * `body`. The email body.

  * `content_type`. The email content type.

  * `attachment_count`. The number of email attachments.

  * `email_attachments`. An array of email attachments. Each array element contains the following: `file_name`, `file_type`, `size_bytes`, and `url`. The `url` field returns null.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
