---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/remove-end-user-data/
title: Remove end-user data \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:55.538492+00:00
---

# Remove end-user data  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/remove-end-user-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Remove end-user data Stay organized with collections  Save and categorize content based on your preferences. 

You can remove end-user interaction data from your instance for privacy-related reasons. You have the following options, depending on your use case:

  * Remove end-users' interaction data for web SDK and mobile SDKs users

  * Remove subject lines from end-user email interactions




## Remove an end-user's interaction data for the web SDK and the mobile SDK

If you use the web SDK or the mobile SDKs, you can remove an end-user's interaction data from your CCAI Platform instance. To remove all of an end-user's data, however, you must also delete data such as chat transcripts, call recordings, and other session-related files from your CRM or external storage.

To remove an end-user's interaction data for the web SDK and mobile SDKs, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Consumer Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Consumer Privacy** pane, enter the ID that identifies the user in the SDK. You can enter multiple IDs separated by a comma or a space to delete the data for multiple end-users.

  3. Click **Delete**.




## Remove subject lines from end-user email interactions

If you use the email channel, you can remove the subject lines from an end-user's email interactions from your instance. To remove all of the email data for an end user, however, you must also delete their emails from your mail server.

When email subject lines are removed, agents see _Subject removed for privacy_ in the subject line.

To remove subject lines from end-user email interactions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Consumer Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Consumer Privacy** pane, enter either the end-user's CRM contact ID or their CCAI Platform ID. You can enter multiple IDs separated by a comma or a space to delete the data for multiple end-users.

  3. Click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
