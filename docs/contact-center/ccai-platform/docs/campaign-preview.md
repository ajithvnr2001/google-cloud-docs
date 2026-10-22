---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-preview/
title: Preview campaigns \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:58.010552+00:00
---

# Preview campaigns  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Preview campaigns Stay organized with collections  Save and categorize content based on your preferences. 

In a preview dialer campaign, agents dial manually, but the calling list is generated automatically from the campaign list. Agents have an unlimited amount of time to read or preview information about the contact before initiating the outbound call.

When running a preview campaign, the agent sees the contact information for the next end-user in the list and any other relevant information that was uploaded for that end-user. The agent can dial that end-user when they are ready or they can choose to skip that end-user.

Agents are automatically provided a preview of the end-user's CRM record in the background when the call is dialed. The agent can also preview the end-user information provided in the campaign file by clicking the arrow next to the end-user's name in the Contact Center AI Platform (CCAI Platform) agent adapter. The agent adapter also provides a link to view the end-user's account in the CRM if the initial preview is no longer displayed in the background.

If the end-user answers the call, the agent can complete the call, enter their notes, and then close the call. At this point they receive the information for the next end-user in the campaign and repeat the process. If the call is not answered or the line is busy, the agent ends the call and then receives the information for the next end-user in the campaign.

## Call blending

Even with agents reserved for an outbound campaign, you can configure IVR queues so their agents are automatically freed from being assigned outbound campaign calls when the queues meet certain configurable conditions. These conditions include agent availability, queue depth, and SLA. For more information, see [Call blending](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-call-blending).

## Preview campaign calls (agent experience)

A preview campaign selects a end-user record from the call list and proposes it to an available agent. The agent can then review the end-user record (the _Preview_ phase) and decide to call this end-user agent or skip.

When a preview campaign is activated, the caller makes a _reservation call_ for every available agent in the campaign's target queue. For each agent who picks up a reservation call, the campaign presents them with a preview of the profile for the next end-user on its list. This end-user profile is pulled from the CRM, such as Salesforce or Kustomer.

For the agent to be able to handle preview campaign calls, follow these steps:

  1. Sign in to the CCAI Platform portal.

  2. In the CCAI Platform agent call adapter, select **Available** from the status drop-down.

If there is a reservation call, it will be routed to the agent automatically.

  3. Click **Click to Answer**.

**Note:** If the auto answer feature is active, the call dials without having to click the button.
  4. The end-user's name and phone number are displayed. Click the arrow next to the end-user's name to preview their profile from the CSV file.

  5. Click the **View case** link to view the customer's CRM record if it is no longer displayed.

  6. Click **Call** to dial the next end-user on the list or click **Skip** to temporarily pass on the end-user and preview the next contact on the campaign list. Click **Skip & close** to remove the end-user from the campaign list.

**Note:** Clicking **Skip** does not remove the end-user from the list.
  7. The agent clicking **Call** completes the call or transfers the call to another agent. Click **Done**.

  8. On the **Wrap-up: disposition & note** screen, select a disposition code from the drop-down and enter any additional notes regarding the call. Click **Save**.

**Note:** If [Agent Assist call summarization](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#session_summarization) is enabled, the agent can also insert the call summary into the call notes.
  9. Repeat for the next end-user on the campaign list.




## Requirements for campaign files

Campaign files contain a list of end-users (consumers) being called and their phone numbers. These files are uploaded to your campaigns and the information is displayed in the CCAI Platform agent adapter during campaign calls.

**Note:** All lists must be scrubbed against national and company DNC registries prior to upload.

The Campaign files must meet the following requirements:

  * Files must be in CSV file format.

  * Files must contain no more than 10,000 rows.

  * Each file must contain the following two columns:

    * **Name_required** : the name of the end-user

    * **Phone_required** : the phone number of the end-user

Additional columns are permitted. The values in additional columns display in the adapter but are not validated.

  * All phone numbers must be in E.164 format—for example, `+12223334444`.




If any of these requirements are not met, the validation process returns an error message during processing and the file is not uploaded.

## Create a preview campaign for outbound dialer

All lists must be scrubbed against national and company DNC registries prior to upload.

To create a preview campaign, follow these steps:

  1. Go to **Campaigns**.

  2. On the **Campaign manager** screen, click **Add campaign**. The **Add campaign** window opens.

  3. In the **Campaign name** field, enter the campaign name.

  4. To upload a campaign list, click **Choose files**. Your file explorer opens.

  5. Select the file to upload and then click **Open**.

**Note:** When the CSV file or Excel file is uploaded, the list is locked and cannot be modified.
  6. In the **assign queue** field, select the queue you want to assign this campaign to, from the drop-down. You can also start entering the name of the queue to narrow the available options in the drop-down list.

  7. Click **Set**. The new campaign saves and returns to the Campaign Manager screen.




### Configuration considerations

  * **Queue:** One queue must be prebuilt. See [IVR: Adding and Editing Queues Menus](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup).

**Note:** If a queue also is reachable using the IVR menu, the assigned agent is also receiving regular inbound calls. This way, you can have blended campaign calls and regular calls. However, if you make the queue unreachable, then only campaign calls are served.
  * **Agent:** One agent must be in Available status. See [Agent statuses](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
