---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-ui/
title: List conversations using the console \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:49.193167+00:00
---

# List conversations using the console  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  List conversations using the console Stay organized with collections  Save and categorize content based on your preferences. 

You can view the conversations in CX Insights console in the **Conversation Hub** menu.

## Prerequisites

  1. Enable the [Cloud Storage, Speech-to-Text, and Insights APIs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) to set up your project.
  2. Import multiple conversations to CX Insights using [CX Insights console](https://ccai.cloud.google.com/insights/projects) or [the API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api).



## List conversations

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.projects.get`
  * `contactcenterinsights.conversations.list`



The CX Insights console displays the most recent conversations associated with your project. Only 50 results are displayed at a time, starting with the most recent. To see earlier conversations, click **Next page** at the bottom of the table.

The list can also be filtered to select conversations that match specific criteria. You can apply the following filters to the list of conversations, in any combination:

### Filter by upload time

  * **Filter:** For the list of conversations uploaded within the past hour, click **1H**. To filter to those uploaded within the past six hours, one day, one week, and one month, click **6H** , **1D** , **1W** , and **1M** , respectively.

  * **Apply a custom date-time range filter:** Click **Custom** , enter the selected beginning and end date and times, and click **Apply**. The resulting list will include only those uploaded within this range. To remove this filter, click **All**.




### Filter by transcript content

To filter conversations by the phrases they contain, click the conversation filter bar and then select **Transcript** from the autocomplete drop-down. Next, select either **Includes** or **Excludes** , enter the phrase you want to filter for, then click **Apply**. The list of conversations will be updated to include only those that include (or exclude) the given phrase. To remove this filter, click the **X** on the corresponding chip.

### Filter by agent ID

To filter conversations according to the agent that handled them, click the conversation filter bar and then select "Agent ID" from the autocomplete drop-down. Next, type the agent's ID, then click **Apply**. The list of conversations will be updated to include only those that were handled by that agent. To remove this filter, click the **X** on the corresponding chip.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
