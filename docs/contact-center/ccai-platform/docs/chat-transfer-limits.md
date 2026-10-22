---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transfer-limits/
title: Transfer limits for chats \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:16.884336+00:00
---

# Transfer limits for chats  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transfer-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Transfer limits for chats Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the maximum number times that a chat can be transferred. When the limit is reached for a session, you can configure whether no additional transfers are allowed, or whether one final transfer to a specified queue is allowed.

To configure transfer limits for chats, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Web & Mobile**.

  3. Click the **Use Web & Mobile Chat** toggle to the on position.

  4. In the **Web & Mobile Chat Settings** pane, for **Transfer Limits** , do the following for **Web** or **Mobile** , or both, depending on your requirements:

     1. Select the **Limit the total count of transfers in a single chat session ** checkbox.

     2. In the number field, enter the maximum number of transfers allowed.

     3. For **When the transfer count exceeds the limit** , select one of the following:

        * **Disable all transfer options** : when the limit is reached, this prevents an agent from making additional transfers

        * **Allow one final transfer to the queue** : when the limit is reached, this lets an agent do a final transfer to a queue that you specify. The languages that are enabled in your instance appear. Do the following:

          1. Click the **Search queue** field next to the first language in the list. A list of queues that are available for that language appears.

          2. Click the queue that you want to receive the final transfer. You can type a queue name to narrow your search.

          3. Repeat for every language in the list.

     4. To complete your configuration, do the following:

        * Select the **Include transfer by virtual agent in total transfer count** checkbox if you want transfers by virtual agents to be counted.

        * Select the **Include transfer by human agent in total transfer count** checkbox if you want transfers by human agents to be counted.

        * Select the **Reset transfer counts to "0" when the chat is dismissed** checkbox if you want transfers to reset after the chat.

     5. Click **Save Chat Details**.




## Session metadata

The session metadata file contains the `transfer_limit` field, which provides information about the transfer limit for the session. For more information, see [Session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata).

Here's an example of a `transfer_limit` field:
    
    
    "transfer_limit": {
        "enabled": true,
        "limit_count": 10,
        "limit_reached": "true"
      },
    

## Agent experience

If you select **Disable all transfer options** when configuring the transfer limit, the **Chat Transfer** button in the agent adapter is inactive when the transfer limit is reached for a chat session. If you select **Allow one final transfer to a queue** , the **Chat Transfer** button is active but only the queue that you specified is available for transfer. After transferring the chat, the **Chat Transfer** button is inactive.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
