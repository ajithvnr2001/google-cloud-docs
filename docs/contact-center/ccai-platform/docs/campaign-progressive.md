---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-progressive/
title: Progressive campaigns \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:22.156252+00:00
---

# Progressive campaigns  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-progressive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Progressive campaigns Stay organized with collections  Save and categorize content based on your preferences. 

In a _progressive campaign_ , agents are reserved for end-users on a campaign list. The call adapter displays the end-user's information while the call is dialing.

## Call blending

Even with agents reserved for an outbound campaign, you can configure IVR queues so their agents are automatically freed from being assigned outbound campaign calls when the queues meet certain configurable conditions. These conditions include agent availability, queue depth, and SLA. For more information, see [Call blending](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-call-blending).

## Progressive campaign calls (agent experience)

In a progressive campaign, an agent is reserved by the campaign and waits on the line to dial a specific end-user. The end-user's information is displayed as the agent is dialing, allowing the agent to study the end-user's profile while waiting for the call to be answered. The end-user's CRM page is also displayed in the background for the agent to review.

If the end-user answers the call, the agent can complete the call, enter their notes, and then close the call. At this point, the agent receives the information for the next end-user in the campaign as the call is dialed and then repeats the process. If the call is not answered, goes to voicemail, or fails, then the agent is automatically presented with the next end-user in the campaign and repeats the process.

For an agent to handle a progressive campaign call follow these steps:

  1. Sign in to the CCAI Platform portal.

  2. In the agent call adapter, select **Available** from the status drop-down.

  3. If there is a reservation call, it will be routed to the agent automatically. Click **Click to answer**.

**Note:** If the **auto answer** feature is active, the call dials without having to click the button.
  4. The information for the next end-user displays while the call is dialing, allowing the agent to preview the information while waiting for the call to be answered.

     1. Click the down-arrow to the right of the end-user's name to preview their profile from the CSV file.

     2. Click the **View case** link to view the customer's CRM record if it is no longer displayed.

     3. The agent can click **break** to end the call before the end-user answers and move on to the next end-user in the campaign.

  5. If the end-user answers the call, the agent is connected and the status bar turns green.

If the end-user does not answer the call, the agent starts the process again with the next name in the campaign.

  6. Once the agent has completed the call or transferred the call to another agent, click **Done**.

  7. On the **wrap-up: Disposition & Note** screen, select a disposition code from the drop-down and enter any additional notes regarding the call. Click **Save**.

**Note:** If [Agent Assist call summarization](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent_Assist#session_summarization) is enabled, the agent can also insert the call summary into the call notes.
  8. The campaign dialer calls the next end-user in the campaign and provides a preview of the end-user's information to the agent as the call is connecting.




## Requirements for campaign files

Campaign files contain a list of consumers (**Name** column) being called and their phone numbers (**Phone** column). These columns are required.

These files are uploaded to your campaigns and the information is displayed in the CCAI Platform agent adapter during campaign calls.

**Note:** All lists must be scrubbed against national and company Do Not Call (DNC) registries prior to upload.

The Campaign files must meet the following requirements:

  * Campaign files must be in CSV file format

  * Maximum 10,000 rows

  * Each file must contain a name column and phone column.

The header names need to be exact: **NAME (REQUIRED)** and **PHONE (REQUIRED)**.

**Note:** Additional columns can be included. These values will be displayed in the Adapter but won't be validated.
  * All phone numbers are entered in E.164 format; for example, `+12223334444`.




If any of the these requirements are not met, the validation process returns an error message during processing and the file won't be uploaded.

## Creating a progressive campaign

All campaign lists must be scrubbed against national and company DNC registries prior to upload.

To create a progressive campaign follow these steps:

  1. In the CCAI Platform portal go to **Campaigns**.

  2. Click **Add campaign**. The **Add campaign** window displays.

  3. In the **Campaign name** field, enter a unique campaign name.

  4. To upload a campaign list, click **Choose files**.

Your file explorer opens. Select the CSV file or Excel file to upload and then click **Open**.


**Note:** After the file is uploaded, the campaign list is locked and cannot be modified.

  1. In the **Assign queue** field, use the list to select the queue that you want to assign this campaign to. You can also enter the name of the queue to narrow the available options in the list. When you assign a campaign to a queue, the campaign is not limited to the queues hours of operation.

  2. Click **Save**. The new campaign is saved and returns to the campaign manager page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
