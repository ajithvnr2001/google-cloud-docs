---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-campaign-data-sets/
title: Standard Reports: Campaign Datasets \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:59.690436+00:00
---

# Standard Reports: Campaign Datasets  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-campaign-data-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Standard Reports: Campaign Datasets Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform provides standard reports for outbound campaigns.

## Preview Dialer Disposition Report

The **Preview Dialer Disposition Report** provides details on the statuses of the dispositioned calls within the selected campaigns.

### To create a downloadable report:

  1. Go to **Reports > Campaigns**.

  2. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

  3. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

  4. In **Step 3: Select Reports Desired** , choose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

  5. Step 4: Choose Filters, configure the filter the reports by timeframe or timezone.

  6. Click **Download**.




The metrics in this report are as follows:

**Campaign Mode** | Indicates the type of campaign that was selected in the Campaign Manager in the Contact Center AI Platform (CCAI Platform) portal.

  * Predictive
  * Preview

  
---|---  
**Campaign Name** | The name of the campaign as entered in the **Campaign Manager** settings in the CCAI Platform portal.  
**Queue Name** | The name of the queue the call was routed through. In this report it is specifically the queue assigned to the campaign.  
**Handled** | The sum of the calls that were picked up and handled by an agent.  
**Disposition Codes** | Displays the disposition code (as configured in the CCAI Platform portal) that the agent assigned to the interaction after the call was completed. Disposition code are configured in **Settings > Operations Management**. Disposition codes will display within their own column.  
  
## Preview Dialer Detailed Report

The **Preview Dialer Detailed Report** provides a detailed call report of the preview dialer campaign. The reporting metrics provide insights into call status (for example, consumer abandoned, skipped), transfers, and the average handle times of each call.

### To create a downloadable report:

  1. Go to **Reports > Campaigns**.

  2. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

  3. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

  4. In **Step 3: Select Reports Desired, c** hoose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

  5. Step 4: Choose Filters, configure the filter the reports by timeframe or timezone.

  6. Click **Download**.




### Before Call Work

This report contains the metric Before Call Work (BCW).

BCW time calculations correspond to selected campaign (dialer) modes (Preview or Predictive). Also, BCW will only appear in the calculation when a campaign is **active** (in play).

In Preview Dialer mode, BCW is the **agent time before a call started.** For example, the time the agent spends researching the consumer and previewing their information or notes in the CRM.

In Predictive Dialer mode, BCW it is the **agent time after a call started waiting for the consumer to join** the call.

The metrics are as follows:

**Metric Name** | **Definition**  
---|---  
**Campaign Mode** | The type of campaign.

  * Predictive
  * Preview

  
**Campaign Name** | The name of the Campaign as configured in the Campaign Manager within the CCAI Platform portal.  
**Queue Name** | The name of the queue assigned to the Campaign.  
**Started Time** | The timestamp (date and time) when the interaction started.  
**Ended Time** | The timestamp (date and time) when the interaction finished.  
**Interaction ID** | The unique identifier of the interaction.  
**Handled Call** | The interaction was handled by an agent  
**Call Status** | This identifies the outcome of the call. The possible values are:

  * Abandoned by Contact: The interaction was answered by the consumer and then the consumer decides to disconnect from the call.
  * Skipped Call: The interaction was skipped by the agent
  * Skipped & Closed: The interaction was skipped & closed.
  * Carrier Error: There was an error on the carrier side resulting in the call not connecting.
  * Not Picked Up: The interaction was not answered by the consumer.
  * Invalid Number: An invalid number format was presented and did not connect successfully to a consumer.

  
**Agent name** | The identity of the individual that handled the interaction.  
**BCW** | The total time for Before Call Work (BCW) of the interaction. BCW is the time the agent spent acknowledging the contact details in the CRM before the interaction was connected.  
**Talk Time** | The total length of time the agent spent talking to a customer. This metric doesn't include BCW time, Hold Time or Wrap-up time.  
**Hold Time** | The total time for the interaction where the consumer was placed on hold by an agent.  
**Wrap-up Time** | The total time that an agent was in wrap-up status.  
**Handle Time** | The total time for the interaction that elapsed from when the agent started BCW, accepts an interaction to when they end their wrap-up phase._This is calculated as: BCW + Talk Time + Hold time + Wrap-up time._  
**Transferred** | Identifies whether the interaction was transferred.  
  
## Preview Dialer Summary Report

The **Preview Dialer Summary Report** provides a summary of the specific campaign(s) selected.

### To create a downloadable report:

1\. Go to **Reports > Campaigns**.

2\. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

3\. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

4\. In **Step 3: Select Reports Desired, c** hoose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

5\. Step 4: Choose Filters, configure the filter the reports by timeframe or timezone.

6\. Click **Download**.

### Before Call Work

This report contains the metric **Before Call Work** (**BCW**). BCW is a part of the Handle Time calculations (and also appears as aggregated calculations, Average BCW and Total BCW).

BCW is the time the agent can learn more about the client (via the CRM) and read any pertinent notes about the consumer and the call they are going to receive.

This is calculated as _BCW +Talk Time + Hold time + Wrap-up time / All handled interactions_

BCW will only appear in the calculation when a campaign is **active** (in play).

The metrics in this report are as follows:

**Metric Name** | **Definition**  
---|---  
**Campaign Mode** | The type of campaign.

  * Predictive
  * Preview

  
**Campaign Name** | The name of the Campaign as configured in the Campaign Manager within the CCAI Platform portal.  
**Queue Name** | The name of the Queue assigned to the Campaign.  
**Total Volume** | The total volume of calls presented from the Campaign  
**Handled Calls** | The interactions that were handled by an agent  
**Abandoned by Contact** | The interaction was answered by the consumer and then the consumer decides to disconnect from the call.  
**Skipped Calls** | The total number of interactions that were skipped by the agent  
**Skipped & Closed** | The total number of interactions that were skipped and closed.  
**Carrier Error** | The total number of interactions where there was an error on the carrier side resulting in the call not connecting.  
**Not Picked Up** | The total number of interactions where the call was unanswered by the consumer.  
**Invalid Number** | The total number of interactions where an invalid number format was presented and did not connect successfully to the consumer.  
**Not Reached to Contact** | The total number of interactions that did not reach a contact. *_more information about this will be forthcoming._  
**Transfers** | The total number of Interactions that were transferred to other queues.  
**Total BCW Time** | The total time for all Before Call Work. BCW is the time the agent spent acknowledging the contact details in the CRM before the Interaction was connected.  
**Avg. BCW Time** | The average time for all Before Call Work (BCW). BCW is the time the agent spent acknowledging the contact details in the CRM before the Interaction was connected.  
**Total Talk Time** | The total time that the agent spent talking to a customer. This metric doesn't include Before Call work, hold time or wrap-up time.  
**Avg. Talk Time** | The average length of time that the agent spent talking to a customer. This metric doesn't include Before Call work, hold time or wrap-up time.  
**Total Hold Time** | The total time across all interactions where a customer was placed on hold.  
**Avg. Hold Time** | The average time across all interactions where a customer was placed on hold.  
**Total Wrap-up Time** | The total time that an agent was logged in and was in the wrap-up state  
**Avg. Wrap-up Time** | The average amount of time that an agent was logged in and was in the wrap-up state  
**Total Handle Time** | The total time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _BCW +Talk Time + Hold time + Wrap-up time / All handled interactions_  
**Avg. Handle Time** | The average time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _BCW +Talk Time + Hold time + Wrap-up time / All handled interactions_  
  
## Predictive Dialer Disposition Report

The **Predictive Dialer Disposition Report** provides details on the statuses of the dispositioned calls within the selected campaigns.

### To create a downloadable report:

1\. Go to **Reports > Campaigns**.

2\. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

3\. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

4\. In **Step 3: Select Reports Desired** , choose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

5\. In **Step 4: Choose Filters** , configure the filter the reports by **Timeframe** or **Timezone**.

6\. Click **Download**.

The metrics available in this report are as follows:

**Campaign Mode** | Indicates the type of campaign that was selected in the Campaign Manager in the CCAI Platform portal.

  * Predictive
  * Preview
  * Progressive

  
---|---  
**Campaign Name** | The name of the campaign as entered in the **Campaign Manager** settings.  
**Queue Name** | The name of the queue the call was routed through. In this report it is specifically the queue assigned to the campaign.  
**Handled** | The sum of the calls that were picked up and handled by an agent.  
**Disposition Codes** | Displays the disposition code (as configured in the CCAI Platform portal) that the agent assigned to the interaction after the call was completed. Disposition code are configured in **Settings > Operations Management**. Disposition codes will display within their own column.  
  
## Predictive Dialer Detailed Report

The **Predictive Dialer Detailed Report** provides a detailed report of interactions in the predictive dialer campaign. The report details call status (for example, consumer abandoned, skipped), transfers, the amount of time spent in wrap-up, and the handle times (including total and average) of each call.

### To create a downloadable report:

1\. Go to **Reports > Campaigns**.

2\. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

3\. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

4\. In **Step 3: Select Reports Desired, c** hoose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

5\. Step 4: Choose Filters, configure the filter the reports by timeframe or timezone.

6\. Click **Download**.

### Before Call Work

This report contains the metric Before Call Work (BCW).

BCW is the time an agent was utilized on a call but no consumer was present.

It is a metric captured exclusively for Dialer Campaigns, and each campaign type may have a slightly different definition of the start and end times for BCW.

For example:

In Preview Dialer mode, BCW is the time the agent spends researching the consumer or previewing information or notes in the CRM.

In Predictive Dialer mode, BCW is the agent time waiting for the consumer to join the call.

The following metrics are available.

**Metric Name** | **Definition**  
---|---  
**Campaign Mode** | The type of campaign.

  * Predictive
  * Preview
  * Progressive

  
**Campaign Name** | The name of the Campaign as configured in the Campaign Manager within the CCAI Platform Portal.  
**Queue Name** | The name of the queue assigned to the Campaign.  
**Started Time** | The timestamp (date and time) when the interaction started.  
**Ended Time** | The timestamp (date and time) when the interaction finished.  
**Interaction ID** | The unique identifier of the interaction.  
**Handled Call** | The interaction was handled by an agent  
**Call Status** | Call Outcome (possible values):

  * Abandoned by Dialer:The interaction was abandoned by the dialer
  * Abandoned by Contact: The interaction was answered by the consumer and then the consumer decides to disconnect from the call.
  * Voicemail Hung Up: The interaction encountered a voicemail and disconnected.
  * Invalid Number: An invalid number format was presented and did not connect successfully to a consumer.
  * Carrier Error: The interaction encountered a carrier error.
  * Not Picked Up: The interaction was not answered by the consumer.

  
**Consumer Greeting Time** | The start timestamp of when the consumer voice greeting was captured.  
**Consumer Greeting End Time** | The end timestamp of when the consumer voice greeting ended.  
**Agent Connection Time** | The timestamp of when the agent was connected to the interaction.  
**Agent Name** | The identity of the individual that handled the interaction  
**Talk Time** | The total length of time the agent spent talking to a customer. This metric doesn't include BCW time, hold time or wrap-up time.  
**Hold Time** | The total time for the interaction where the consumer was placed on hold by an agent.  
**Wrap-up Time** | The total time that an agent was in wrap-up status.  
**Handle Time** | The total time for the interaction that elapsed from when the agent started BCW, accepts an interaction to when they end their wrap-up phase._This is calculated as: BCW + Talk Time + Hold time + Wrap-up time._  
**Transferred** | Identifies whether the interaction was transferred.  
**BCW** | BCW is the agent time waiting for the consumer to join the call.  
**Callback Scheduled** | Identifies whether a callback was scheduled. This displays as a TRUE or FALSE.  
**CSAT Score** | Displays the CSAT score as a decimal.  
**Redial Attempt** | Indicates whether a redial was attempted.  
  
## Predictive Dialer Summary Report

The **Predictive Dialer Summary Report** provides a summary of the specific campaign (s) selected.

### To create a standard campaign report:

1\. Go to **Reports > Campaigns**.

2\. Under **Step 1: Select Campaign Mode,** choose which type of Campaign you want to generate reports on.

3\. Under **Step 2: Select Campaigns** , choose a specific campaign or all campaigns configured in the Campaign Manager settings.

4\. In **Step 3: Select Reports Desired,** choose the reports you would like to download by checking the box next to the report _(options appear based on campaign type selected in Step 1)._

5\. Step 4: Choose Filters, configure the filter the reports by timeframe or timezone.

6\. Click **Download**.

### Before Call Work

This report contains the metric Before Call Work (BCW).

BCW is the time an agent was utilized on a call but no consumer was present.

It is a metric captured exclusively for Dialer Campaigns, and each campaign type may have a slightly different definition of the start and end times for BCW.

For example:

In Preview Dialer mode, BCW is the time the agent spends researching the consumer or previewing information or notes in the CRM.

In Predictive Dialer mode, BCW is the agent time waiting for the consumer to join the call.

The metrics included in this report are as follows:

**Metric Name** | **Definition**  
---|---  
**Campaign Mode** | The type of campaign.

  * Predictive
  * Preview

  
**Campaign Name** | The name of the Campaign as configured in the Campaign Manager within the CCAI Platform portal.  
**Queue Name** | The name of the queue assigned to the campaign.  
**Redialed** | The total number of redials made.  
**Total Volume** | The total volume of calls presented from the campaign  
**Handled Calls** | The total number of handled interactions.  
**Abandoned by Dialer** | The total number of interactions that were abandoned by the dialer.  
**Abandoned by Contact** | The total number of interactions that are answered by the consumer and then the consumer decides to disconnect from the call.  
**Voicemail Hung Up** | The total number of calls where a voicemail was present and the interaction was disconnected by the agent.  
**Carrier Error** | The total number of interactions where there was an error on the carrier side  
**Not Picked Up** | The total number of interactions where the call was unanswered by the consumer  
**DNC Company** | The total number of skipped calls because a contact was on a company DNC list.  
**Invalid Number** | The total number of calls where the number from CSV (as uploaded in the Campaign Manager settings) is in an unsupported format, isn't the right number of digits, duplicate within a campaign, and/or missing a name.  
**Not Reached To Contact** | The total number of calls that were unable to reach the contact. *more info will be forthcoming.  
**Dialer General Error** | The total number of calls where there was an error on the dialer side. *more info will be forthcoming.  
**Transfers** | The total number of interactions that were transferred to other queues.  
**Total BCW Time** | The total time for all Before Call Work. In this report Total BCW Time is the total time the agent spent waiting for the consumer to connect to the call.  
**Avg. BCW Time** | The average of time for all Before Call Work. In this report Avg. BCW is the average time the agent spent waiting for the consumer to connect to the call.  
**Total Talk Time** | The total time that the agent spent talking to a customer (including BCW). This metric doesn't include Hold Time or Wrap-up Time.  
**Avg. Talk Time** | The average length of time that the agent spent talking to a consumer (including BCW). This metric doesn't include Hold Time or Wrap-up Time.  
**Total Hold Time** | The total time across all interactions where a customer was placed on hold.  
**Avg. Hold Time** | The average time across all interactions where a customer was placed on hold.  
**Total Wrap-up Time** | The total time that an agent was logged in and was in the wrap-up state  
**Avg. Wrap-up Time** | The average amount of time that an agent was logged in and was in the wrap-up state  
**Total Handle Time** | The total time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _Interaction Time {including BCW} + Hold time + Wrap-up time / All handled interactions_  
**Avg. Handle Time** | The average time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _Interaction Time {including BCW} + Hold time + Wrap-up time / All handled interactions_  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
