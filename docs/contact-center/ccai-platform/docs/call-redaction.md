---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-redaction/
title: Call redaction \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:45.646032+00:00
---

# Call redaction  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-redaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call redaction Stay organized with collections  Save and categorize content based on your preferences. 

Call redaction allows agents to stop recording when sensitive customer information is being shared during a call. The time in which the agent has initiated call redaction won't be included in the call recording. This feature is ideal when asking customers to share PII.

**_To enable this feature, contact Support._**

## Feature details

  * Only agents assigned to calls from or to queues that have been specifically enabled will see the option to redact calls

  * Calls initiated from an enabled queue that are transferred to a queue without call redaction enabled won't have the call redaction feature available

  * Agents need to manually initiate and end the redaction

  * Agents will still be able to hear during the redacted section of the call while on the live call




## Enable call redaction for inbound calls

  1. Go to **Settings > Queue**.

  2. Click **Edit / View** for the channels requiring call redaction (IVR / Mobile / Web).

  3. Select the menu option to enable call redaction. The setting is only available for end-nodes, or child-menu options.

  4. Toggle Enable Call Recording Redaction to the **On** position.

  5. Repeat these steps for each queue menu.




## Enable call redaction for outbound calls

  1. From the Admin Portal, go to **Settings > Call**.

  2. Call recording needs to first be enabled for Callback outbound calls or Agent Initiated outbound calls. For more information on these call recording types, see [Recording Calls - Configuration Options](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-config).

  3. Mark the checkbox to enable call redaction for either or both outbound call types.




## Agent experience

  1. From the Agent Adapter, while an active call from an enabled queue, click the **Actions** button, then click **Redact**.

  2. A timer will begin and count the seconds in which call redaction is active.

  3. When ready, click **Stop Redacting**.

  4. Click the **X** in the Actions menu to return to the standard call adapter options.




## CRM logging

When an agent uses the call redaction feature, the timestamps when the call redaction started and ended will be saved on the call record.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
