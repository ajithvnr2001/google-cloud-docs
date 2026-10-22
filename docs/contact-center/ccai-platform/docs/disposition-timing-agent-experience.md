---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-timing-agent-experience/
title: Disposition timing agent experience \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:34.902781+00:00
---

# Disposition timing agent experience  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-timing-agent-experience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Disposition timing agent experience Stay organized with collections  Save and categorize content based on your preferences. 

If your administrator enables it, when you manually change your status to wrap-up, you can attribute disposition codes and notes to a previously completed call or chat session. Your administrator can also configure the agent adapter so you can edit disposition codes and notes for previously completed sessions.

## Use disposition timing

This capability works only if your administrator enables it.

To use disposition timing, follow these steps:

  1. In the agent adapter, switch your status to **Wrap-Up**. The wrap-up timer starts, and a list of previously completed sessions appears.

  2. Select a session from the list. A wrap-up form for the session appears.

  3. Optional: To view or edit a different completed session, select a different session from the list. Switching between sessions on the list doesn't reset the wrap-up timer.

  4. If your administrator has enabled disposition editing, edit the disposition code and notes as needed. Otherwise, these fields are read-only.

**Note:** You can click the **Back** button to return to the session list before submitting your changes.
  5. Click **Submit**. The following occurs:

     * The disposition code and note are saved.

     * The elapsed wrap-up time is attributed to the session that you edited.

     * The wrap-up timer resets to `00:00`.

  6. Optional: Select another session to wrap up.

  7. To exit wrap-up, change your status in the status selector (for example, to **Available**).




## Session list behavior

The list of previously completed sessions in the agent adapter can exhibit the following behaviors:

  * **No sessions appear**. This can happen if you haven't handled any sessions recently.

  * **Sessions become ineligible for editing**. A completed session might become ineligible for editing before you submit your edits. The agent adapter returns an error.

  * **Disposition notes aren't available**. The system only stores disposition notes for 15 to 30 minutes after they are submitted. If disposition notes aren't available for a previously completed session, you can add new ones.




## CRM record autoload

CRM record autoload is available for agent adapters embedded in a CRM if your administrator enables it. With CRM autoload, when you select a previous session to attribute wrap-up to, the associated CRM record automatically displays.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
