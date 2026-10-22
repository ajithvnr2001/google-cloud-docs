---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-predictive/
title: Predictive campaigns \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:25.772242+00:00
---

# Predictive campaigns  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-predictive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Predictive campaigns Stay organized with collections  Save and categorize content based on your preferences. 

A predictive campaign predicts the number of contacts that the system must dial to efficiently connect end-users and agents. The campaign simultaneously dials multiple end-users, attempting to connect one of the reserved agents to an end-user. The system determines how many numbers to dial based on the number of available agents and historical call answer rates.

## Call blending

Even with agents reserved for an outbound campaign, you can configure IVR queues so their agents are automatically freed from being assigned outbound campaign calls when the queues meet certain configurable conditions. These conditions include agent availability, queue depth, and SLA. For more information, see [Call blending](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-call-blending).

## Predictive campaign calls (agent experience)

A predictive campaign is an automated dial mode designed to call as many leads as possible by simultaneously dialing multiple phone numbers, then automatically connecting answered calls to the next available agent. The dialing ratio (the number of outbound calls compared to the number of agents managing these calls) is automatically adjusted based on how many calls connect to customers and how many agents are available to take calls. To save the agent time, the system screens out busy signals, disconnected numbers, fax numbers, and voicemails.

When a predictive campaign is activated, the dialer makes a _reservation call_ for every available agent in the campaign's target queue. For every agent who picks up one of the reservation calls, the campaign dials the next batch of customer phone numbers from the campaign list. These calls are made while the reserved agents are waiting on the line.

When the agent picks up a reservation call, the campaign presents them with a preview of the profile for the next customer in the list. This customer profile is pulled from the CRM, such as Salesforce or Kustomer.

For an agent to handle campaign calls, they will need to follow these steps:

  1. Sign in to the CCAI Platform portal or the agent adapter.

  2. In the CCAI Platform agent adapter, select **Available** from the status drop-down.

  3. If there is a reservation call, it will be routed to the agent automatically.

  4. Click **Answer**.

**Note:** If the Auto Answer feature is active, the call will be dialed without having to click the button.
  5. If there is no reserved call, the auto dialer calls the next batch of entries from the campaign list.

  6. When the agent picks up a call, the auto dialer dials the next batch of entries from the campaign list.

  7. Click **Break** to drop the current call and receive the next available call from the campaign list.

  8. If the customer answers the call, the agent is connected and the status bar turns green.

  9. The customer's name and phone number are displayed. Click the down-arrow to the right of the customer's name to preview their profile from the CSV file.

  10. Click the **view case** link to view the customer's CRM record if it is no longer displayed.

  11. Once the agent has completed the call or transferred the call to another agent, click **Done**.

  12. On the **wrap-up: disposition & note** screen, select a disposition code from the drop-down and enter any additional notes regarding the call. Click **Save**.

**Note:** If [Agent Assist call summarization](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#session_summarization) is enabled, the agent can also insert the call summary into the call notes.
  13. The agent is connected to the next call on the campaign list.




## Requirements for campaign files

Campaign files contain a list of end-users (customers) that are called and their phone numbers. These files are uploaded to your campaigns and the information is displayed in the CCAI Platform agent adapter during campaign calls.

**Note:** All lists must be scrubbed against national and company DNC registries prior to upload.

The campaign files must meet the following requirements:

  * Files must be in CSV file format.

  * Files must contain no more than 10,000 rows.

  * Each file must contain the following two columns:

    * **Name_required** : the name of the end-user

    * **Phone_required** : the phone number of the end-user

Additional columns are permitted. The values in additional columns are displayed in the adapter but are not validated.

  * All phone numbers must be in E.164 format—for example, `+12223334444`.




If any of these requirements are not met, the validation process returns an error message during processing and the file is not uploaded.

## Create a predictive campaign

To create a predictive campaign, follow these steps:

  1. In the CCAI Platform portal, click **Campaigns**. If you don't see the **Campaigns** menu, click menu **Menu**. The **Campaign Manager** page appears.

  2. Click **Add Campaign**. The **Add Campaign** dialog appears.

  3. In the **Campaign Name** field, enter a unique campaign name.

  4. In the **Mode** list, select **Predictive**.

  5. Click **Choose Files** , and then select the CSV, XLS, or XLSX campaign file that you want to upload.

  6. In the **Assign Queue** list, select the queue that you want to assign this campaign to.

**Important:** When you assign a campaign to a queue, the campaign isn't limited to the queue's hours of operation.
  7. In the **Assign Time Zone Schema** list, select the time zone schema that you want to assign to this campaign.

  8. For **Abandoned Call Message** , do one of the following:

     1. Select **Text-to-speech** , and then enter your abandoned call message in the text field.

     2. Select **Audio Recording** , and then upload your abandoned call message audio file.

**Note:** You can configure an abandoned call message for all campaigns at **Settings > Campaigns > Abandoned Call Message**.

For more information, see About abandoned calls.

  9. In the **Ringing Timeout** field, enter the number of seconds of ringing after which a call times out and is considered abandoned.

  10. In the **Max Calls Per Agent** list, select the maximum number of calls that the dialer can make per available agent.

  11. In the **Target Agent Occupancy** field, enter the target percentage of agent occupancy. The system adjusts the dialing rate to keep agent usage near this target.

  12. Optional: To enforce a strict abandonment limit, select the **Max Abandonment** checkbox, and then enter a percentage in the field. The maximum abandonment rate is the maximum percentage of calls that the dialer can abandon during the campaign.

**Note:** For campaigns in the United States, the abandonment rate must not exceed three percent over a 30 day period. The allowed abandonment rate varies by country.
  13. Click **Create**.




## About abandoned calls

A call is abandoned in the following scenarios:

  * **Aggressive overdialing** : More end-users pick up than anticipated, causing the queue to run out of available agents.

  * **The end-user waits too long** : The end-user waits more than two seconds after saying "hello" before an agent is connected.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
