---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/enable-audit-logs/
title: Enable Data Access audit logs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:38:00.760423+00:00
---

# Enable Data Access audit logs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/enable-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Enable Data Access audit logs Stay organized with collections  Save and categorize content based on your preferences. 

To get audit logs about the usage of your model endpoints, you need to enable [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) for Gemini Enterprise Agent Platform. Data Access audit logs include "admin read" operations that read metadata or configuration information. They also include "data read" and "data write" operations that read or write user-provided data.

After you enable Data Access audit logs for Gemini Enterprise Agent Platform, to view the `data_access` log stream in the Google Cloud console, you need to be granted the Private Logs Viewer role (roles/logging.privateLogViewer) .

To learn more about Data Access logs, including how to enable and view the logs, see [Gemini Enterprise Agent Platform audit logging information](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/audit-logging).

## What's next

Overview 

###  [ Introduction to tuning ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/get-started-with-gemini-3)

Learn how to tune a model by providing a training dataset that contains a set of examples of specific downstream tasks. 

Overview 

###  [ Responsible AI ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai)

Learn about some of the limitations to generative AI and recommended practices for using generative AI. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
