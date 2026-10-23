---
url: https://docs.cloud.google.com/support/docs/peak-events/create-manage-event-requests/
title: Create and manage event requests \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:08.442424+00:00
---

# Create and manage event requests  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/peak-events/create-manage-event-requests/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Create and manage event requests Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Customer Care lets you create event requests as a part of the [Event Management Service](https://docs.cloud.google.com/support/docs/premium#event_management). This service is offered as a part of [Premium Support](https://docs.cloud.google.com/support/docs/premium).

To learn how to prepare for peak capacity events, we recommend that you go through the [Prepare for a peak capacity event](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) checklist .

This page explains how to create and manage event requests.

## Before you begin

Make sure that you have the following Identity and Access Management (IAM) roles assigned at the organization level to create and manage event requests:

  * [`Advisory Support Editor`](https://docs.cloud.google.com/support/docs/access-control#cloudsupport.advisorySupportEditor): to create and manage event requests.
  * [`Advisory Support Viewer`](https://docs.cloud.google.com/support/docs/access-control#cloudsupport.advisorySupportViewer): for read-only access to existing events.



To learn how to assign roles, see [Granting IAM roles](https://docs.cloud.google.com/support/docs/access-control#granting_roles).

## Create an event request

To notify the Customer Care about your event, you must create an event request. We recommend that you create event requests at least 30 days in advance of the event to allow sufficient time for Customer Care to prepare.

To ensure high-quality support during your most critical windows, focus your monitoring requests on peak activity periods. While events typically last 1–2 weeks, monitoring requests are limited to a maximum of 45 days. If your event requires monitoring for more than 45 days, contact your Google Cloud account team to discuss a customized plan.

To create an event request, do the following:

  1. In the Google Cloud console, go to the **Support** > **Event Management** page.

[Go to Event Management](https://console.cloud.google.com/support/advisorycases)

  2. Click **Create Event**.

  3. Enter a name for your event.

  4. Select an **Event type** :

     * General awareness
     * Peak sales event
     * Migration or cutover
     * Product or feature launch
     * Load or scale testing
     * Upgrade
     * Live event
  5. Enter a description for your event.

  6. Select a timezone.

  7. Select the **Start date** and **Start time** of the event.

  8. Select the **End date** and **End time** of the event.

  9. In the **Critical timeframes** field, mention any specific days or times within the event duration that require special attention. For example, pre-production scaling before a retail sale.

  10. Provide a primary contact who can be used for follow ups and confirmations.

  11. In the **Additional contacts** field, list other people in your organization to be included in event communications.

  12. In the **Impacted projects** field, add a comma-separated list of your Google Cloud project IDs that are impacted by this event.

  13. From the **Impacted products** list, select the products and services that are most important for the event.

  14. Click **Submit**.

  15. To comment on the case, upload file attachments, or modify other case attributes, click **View request**.




After you create the event request, your account team is notified and might reach out for additional information, and guide you through the following:

  * Preparing your systems for key moments and heavy workloads.
  * Running load tests and disaster tests to proactively resolve potential issues.
  * Engaging with Customer Care in the event of any issues that might occur.
  * Reviewing the outcomes of your event and making recommendations for future events.



## View event request details

To view your event requests and their details, do the following:

  1. In the Google Cloud console, go to the **Support** > **Event Management** page.

[Go to Event Management](https://console.cloud.google.com/support/advisorycases)

You can view the list of your event requests and their status.

  2. Click the name of a specific request to view its details.




### Event request status

After an event request is created, you can view its status in the Google Cloud console. The following table provides a description of the different statuses:

Status  | Description   
---|---  
New request  | New request is received. It is reviewed and assigned to a Customer Care specialist.   
In planning  | Customer Care specialists are working on an execution plan and it is shared with you.   
Active event  | Event is in progress.   
Complete  | Event is over.   
Cancelled  | Event is cancelled.   
  
## Update an event request

You can only update an open event request.

To update an event request, do the following:

  1. In the Google Cloud console, go to the **Support** > **Event Management** page.

[Go to Event Management](https://console.cloud.google.com/support/advisorycases)

  2. Click the name of a the event request that you want to update.

  3. Edit the required fields. You can make the following updates only:

     * Add contacts.
     * Add comments.
     * Add attachments.



## Cancel an event request

You can only cancel an event request that is not yet an "Active event".

To cancel an event request, do the following:

  1. In the Google Cloud console, go to the **Support** > **Event Management** page.

[Go to Event Management](https://console.cloud.google.com/support/advisorycases)

  2. Click the name of a the event request that you want to cancel.

  3. Click **Cancel**.




## Contact Customer Care

All users can contact Customer Care with questions about Cloud Billing. You can also request support for technical questions about projects within your organization.

  1. In the Google Cloud console, go to the **Support** > **Overview** page. 

[Go to Overview](https://console.cloud.google.com/support/overview)

  2. Using the resource selector on the console toolbar, select the project for which you'd like support.
  3. In the navigation menu, select your preferred communication channel: 
     * **Billing support** : gives you access to a live chat for billing support
     * **Phone support** : provides a phone number that you can call to receive assistance in supported languages
     * **Community support** : provides links to community discussion groups and mailing lists that can help you find answers or troubleshoot problems



## What's next

  * Learn how to [prepare for a peak capacity event](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) checklist.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
