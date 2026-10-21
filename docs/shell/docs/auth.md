---
url: https://docs.cloud.google.com/shell/docs/auth/
title: Authorize with Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:33.574043+00:00
---

# Authorize with Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Authorize with Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how authorization works in Cloud Shell.

## Authorize tools in Cloud Shell

When you make a Google Cloud API call or use a command-line tool that requires credentials (such as the gcloud CLI or `bq`) with Cloud Shell for the first time, Cloud Shell prompts you with the **Authorize Cloud Shell** dialog.

To allow the tool to use your credentials to make calls, click **Authorize**.

### Duration of authorization

This authorization lasts the lifetime of your Cloud Shell session. Since each Cloud Shell session is tied to an ephemeral, pre-configured virtual machine, if you restart your VM or close your browser, you will need to reauthorize these tools if you use them in your next new session. To learn more about how Cloud Shell works, refer to the [Concepts page](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) that outlines key features and how they work.

### Revoke access

To revoke access for a session, restart your VM to start a new session by clicking more_vert **More** > **Restart**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
