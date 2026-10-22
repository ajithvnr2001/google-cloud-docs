---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-progressive-amd/
title: Answering machine detection for progressive campaigns \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:56.230307+00:00
---

# Answering machine detection for progressive campaigns  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-progressive-amd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Answering machine detection for progressive campaigns Stay organized with collections  Save and categorize content based on your preferences. 

With answering machine detection (AMD), Contact Center AI Platform (CCAI Platform) can identify whether an outbound call reaches a live person or whether it reaches an answering machine or voicemail during a progressive campaign. If CCAI Platform detects an answering machine or voicemail, the call ends and the dialer proceeds to the next contact.

## Before you begin

You must have a progressive campaign.

## Turn on AMD for progressive campaigns

To turn on AMD for progressive campaigns, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Campaigns**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Dialer Modes > Progressive** section, click the **Enable Answering Machine Detection** toggle to the on position.

  3. Click **Save Dialer Modes**.




## Agent experience

With AMD for progressive campaigns turned on, the agent experience is as follows:

  1. The progressive campaign dialer places an outbound call.

  2. The call is connected to an agent.

  3. CCAI Platform runs voicemail detection to determine whether the call reached a live person or whether it reached voicemail or an answering machine.

  4. One of the following happens:

     * **A live person answers**. The call continues normally.

     * **CCAI Platform detects voicemail or an answering machine**. The following actions take place:

       * The call is terminated.

       * A green banner appears in the call adapter indicating that the system detected an answering machine or voicemail.

       * The dialer calls the next contact on file.




## Reporting

When voicemail or an answering machine is detected in an outbound campaign call, CCAI Platform reports it in campaign metrics, attaching the **Voicemail Detected** label.

## Limitations

AMD performance can be affected by carrier conditions and call audio. Voicemail and answering machine detection are not guaranteed, especially in noisy environments.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
