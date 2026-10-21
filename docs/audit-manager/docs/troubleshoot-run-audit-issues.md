---
url: https://docs.cloud.google.com/audit-manager/docs/troubleshoot-run-audit-issues/
title: Troubleshoot run audit issues \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:15.851990+00:00
---

# Troubleshoot run audit issues  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/troubleshoot-run-audit-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Troubleshoot run audit issues Stay organized with collections  Save and categorize content based on your preferences. 

You can resolve errors that occur when running audits by reviewing common REST API error messages.

The following table lists error messages that you might encounter when running audits and generating an audit assessment.

Error code | Error message | Description  
---|---|---  
400 | Invalid compliance framework. Please provide a framework from the following list : [] | Ensure that you've specified a supported compliance framework and try again.   
400 | Invalid report format is passed. | Ensure that you've specified the expected report format: `odf`.  
  
The following table lists the errors that you might encounter when running an audit:

Error code | Error message | Description  
---|---|---  
401 | User has insufficient permissions to run audit on the provided scope. | Ensure that you have been granted the required permissions to run an audit, or ask your administrator to run this operation on your behalf.   
401 | Storage bucket provided is not enrolled for the provided audit resource. | The specified bucket has not been enrolled for the audit operation. Ensure that the enrolled bucket is specified, or retry the enrollment operation for the appropriate bucket.   
403 | Resource is not enrolled to be audited. | The specified resource has not been enrolled for the audit operation. Ensure that the enrolled resource is specified, or retry the enrollment operation for the appropriate resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
