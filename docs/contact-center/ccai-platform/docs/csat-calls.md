---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-calls/
title: CSAT Survey for IVR Calls \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:11.056280+00:00
---

# CSAT Survey for IVR Calls  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CSAT Survey for IVR Calls Stay organized with collections  Save and categorize content based on your preferences. 

This feature invites callers to submit their customer satisfaction rating, or CSAT score, following the conclusion of their IVR call to collect valuable feedback. The CSAT rating used is a fixed 1-5 scale and the results of the survey will be stored in your CRM. Admins can choose if the caller is alerted of the survey before connecting to an agent, or if the CSAT survey isn't announced until the end of the call. Because the survey is automated, enabling this feature requires no additional agent training. If you are using the Web or Mobile SDKs, see: [Mobile and Web Customer Satisfaction Ratings (CSAT)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-mobile-web)

## Details

  * CSAT is offered for inbound calls only.

  * The feature can be enabled and disabled globally or per-queue.

  * Pre-call and Post-call message options offer the ability to configure whether the CSAT survey announcement occurs prior to connecting with an agent or after the support session is complete.

  * Callers will have the opportunity to submit a score 3 times. If they fail to enter a valid option 3 times, the call will end with no CSAT score recorded.




## Configuration

The following sections provide details on how to configure the CSAT feature.

### Enable CSAT surveys globally

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Navigate to the **Customer Satisfaction Ratings** section.

  3. Enable by toggling the switch to **ON**.

  4. Options to enable:

     1. **Enable Customer Satisfaction Rating to post in CRM ticket** (mandatory).

When enabled, the 1-5 rating will be posted as a comment in the CRM record.

When disabled, the rating won't be stored with CCAI Platform or in the CRM - making the setting mandatory.

     2. **Enable Customer Satisfaction qualitative feedback** (does not apply).

  5. Click **Set CSAT** to save.

  6. Go to **Settings** > **Call**.

  7. In the **CallerAnnouncements** section, toggle **Enable CSAT After Calls for All IVR Queues** to **ON**.

  8. Mark the checkbox next to **Enable CSAT Notification Announcement Prior to Connecting to an Agent** to play a message letting the caller know that the CSAT survey will be offered to them after the call. This message is recommended for higher response rates since callers might terminate the call before the survey plays if not alerted before-hand. 

  9. Click **Set Caller Announcements** to save.




### Enable CSAT surveys per-queue

  1. Go to **Settings** > **Queue** > IVR **Edit/View**.

  2. Select a queue - the queue must not contain child queues.

  3. In the queue settings section on the right, toggle **Enable CSAT Survey After Call** to **On**.

  4. The setting is automatically saved.




### Customizing messages

Messages to customize:

**Pre-Call Notification of CSAT Survey** : Occurs prior to connecting with an agent and notifies the caller that there will be a CSAT survey once the call with the agent is finished

**Post-Call Notification for CSAT Rating** : Occurs once the agent ends the call to instruct the caller to enter a 1 through 5 for their overall satisfaction rating

#### Order of messages

If [Estimated Wait Time Announcement](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features/index.md#UUID-2e4f63ce-ef81-4e9c-7210-598f50437994) is enabled, the order of announcements to a caller will be:

  1. Estimated Wait Time

  2. Connecting Message

  3. Recording a Call Message

  4. Pre-Call Notification of CSAT Rating

  5. _Call takes place_

  6. Post-Call Notification of CSAT Rating




#### Uploading custom messages

  1. From the Admin Portal, go to **Settings** > **Languages & Messages**.

  2. Select the language you would like to configure if you are using multiple languages.

  3. Scroll to **Pre-Call Notification of CSAT Rating** and enter the Text-to-speech message, or upload a recording.

     * Proposed message: **Please stay on the line after the call to take a brief survey**.
  4. Scroll to **Post-Call Notification of CSAT Rating** and enter the Text-to-speech message, or upload a recording.

-Proposed message: "Using the dial pad, rate your satisfaction on a scale of 1 to 5 with 5 being the best rating."

  5. Click **Apply** to save.




## Viewing scores in the CRM record

Be sure to **Enable Customer Satisfaction Rating** to post in CRM ticket in Operation Management (as shown in Enable CSAT surveys globally) in order for CSAT scores to save to the CRM record. CCAI Platform does not store your CSAT ratings and ratings collected from IVR calls won't be available in CCAI Platform reports.

In Zendesk: CSAT rating is posted as a private comment formatted as "Customer rating feedback received - [score]" and can be mapped to a custom field.

In Salesforce: CSAT rating is posted as a comment within a task associated with the Case or CCAI Platform Session object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
