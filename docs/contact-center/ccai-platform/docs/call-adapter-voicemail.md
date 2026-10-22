---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-voicemail/
title: Listen to voicemail messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:37.885781+00:00
---

# Listen to voicemail messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-voicemail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Listen to voicemail messages Stay organized with collections  Save and categorize content based on your preferences. 

After the voicemail has finished playing, you have the option to **Forward** , **Dismiss** , or **Call Back**. You can switch tabs while listening to a voicemail but cannot start an outbound call.

  * **Dismiss** : Moves the voicemail to your voicemail history. Dismissed voicemails still generate a ticket in the CRM.
  * **Forward** : Click this option to display a list of available destinations to forward the voicemail. Depending on your configuration you will see **Queue** or **Agent** options, which you can switch between by clicking on the tab. You will see a notification banner when the voicemail has been successfully forwarded.
  * **Call Back** : Select this option to call the end-user back. You must wait for the voicemail to finish playing before you can make an outbound call.



## Voicemail in Zendesk

Private comments will be posted when a voicemail is left, listened to, or if a callback is made through the Agent Adapter.

  * A media player lets you listen to the voicemail and information about the time, date, and the name of the queue called are included in the voicemail name.

  * Different statuses will be seen depending on how the voicemail is managed.

    * **Voicemail Played** : Seen if the agent listened to the voicemail in the agent widget.

    * **Voicemail Dismissed** : Seen if the agent listened to the voicemail in the agent widget and dismissed it without calling the customer back.

    * **Called Back Customer** : Seen if the agent calls the customer back through the agent adapter after listening to the call in the agent adapter




## Voicemail in Salesforce

The voicemail will be associated with an **attachment** to a new **task** in Salesforce, available in the **Activity History** section. To listen to the voicemail:

  1. From the case created in Salesforce, select the subject of the **Task**.

  2. Click the Attachment **file name**.

  3. Click **View File** to listen to the voicemail.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
