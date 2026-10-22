---
url: https://docs.cloud.google.com/audit-manager/docs/troubleshoot-enrollment-issues/
title: Troubleshoot enrollment issues \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:40.096475+00:00
---

# Troubleshoot enrollment issues  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/troubleshoot-enrollment-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Troubleshoot enrollment issues Stay organized with collections  Save and categorize content based on your preferences. 

You can resolve errors that occur when enrolling resources for auditing by reviewing common REST API error messages.

The following table lists error messages that you might encounter when enrolling resources for auditing.

Error code | Error message | Description  
---|---|---  
401 | You don't have the necessary permissions to enroll this resource for audits. | Ensure that you have been granted an owner role for the project or folder, or ask the owner to run this operation on your behalf.   
401 | You don't have write permission to Cloud Storage buckets. | For all specified buckets, ensure that the caller has write permissions.   
400 | No storage bucket provided to store audit evidence. | Provide at least one storage bucket to store audit data where the caller has write permissions.  
400 | Scope provided is invalid. Unable to locate the folder or the project to be audited. | Provide scope for resource in the appropriate format.  
403 | Audit Manager API is not being used in project `PROJECT_ID` or is disabled. | Enable the Audit Manager API by clicking the link provided in the message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
