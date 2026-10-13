---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/TaskLogonType/
title: TaskLogonType \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:03.034415+00:00
---

# TaskLogonType  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/TaskLogonType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  TaskLogonType Stay organized with collections  Save and categorize content based on your preferences. 

Enum representing the logon type of the task.

Enums  
---  
`TASK_LOGON_TYPE_UNSPECIFIED` | The logon method is not specified. Used for non-NT credentials.  
`PASSWORD` | Use a password for logging on the user. The password must be supplied at registration time.  
`S4U` | Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.  
`INTERACTIVE_TOKEN` | User must already be logged on. The task will be run only in an existing interactive session.  
`GROUP` | Logon with group credentials.  
`SERVICE_ACCOUNT` | Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.  
`INTERACTIVE_TOKEN_OR_PASSWORD` | First use the interactive token. If the user is not logged on (no interactive token is available), the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK_LOGON_PASSWORD.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
