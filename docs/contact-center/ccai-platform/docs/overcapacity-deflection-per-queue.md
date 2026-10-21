---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/overcapacity-deflection-per-queue/
title: Overcapacity deflection per-queue \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:06.328782+00:00
---

# Overcapacity deflection per-queue  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/overcapacity-deflection-per-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Overcapacity deflection per-queue Stay organized with collections  Save and categorize content based on your preferences. 

Overcapacity deflection is triggered when a session is initiated, but the estimated wait time is larger than the set threshold in **Settings** > **Call** or **Settings** > **Chat**. The global overcapacity selection will be used as the default, but this setting can also be set at the queue level. For more details on the default overcapacity option, refer to [Call Settings: Overcapacity deflection and caller announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#call-settings-overcapacity-deflection).

When there's a need to force a selection for overcapacity for a particular call flow, setting the overcapacity deflection per-queue will direct callers where they need to go. **_This setting allows for only one option, so the caller is not prompted to choose an option like they are when using the default overcapacity option._**

## Overcapacity per-queue setup

![Queue settings](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5488e102.png)

  1. Go to **Settings > Queue.**

  2. Click **Edit / View** to go to the editing section for queue menus within that channel.

  3. Select the menu you want to enable overcapacity deflection for.

  4. Toggle Custom Over Capacity deflection to **Show** to enable and view overcapacity options.

**Message** : Plays the message typed (i.e. "We are experiencing high volume") and then ends the call.

**Queue:** Select from available queue menu options to redirect the call to.

**Phone Number** : Redirects to the number entered.

**Voicemail** : Redirects caller to leave a voicemail.

**Callback** : Keeps the callers place in queue and ends the call. The caller will receive a callback when they are at the top of the queue. Refer to [Call Settings: Overcapacity deflection and caller announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#call-settings-overcapacity-deflection) and also [Custom Callback Number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#custom-callback-number) for more information.

This setting uses the Over Capacity Deflection Callback Option" message will play. This should be configured in **Settings** > **Languages & Messages**. For more information, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages).

  5. Click **Set Overcapacity Deflection** to save.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
