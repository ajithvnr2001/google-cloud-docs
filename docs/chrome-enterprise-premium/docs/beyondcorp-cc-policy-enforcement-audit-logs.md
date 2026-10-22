---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/beyondcorp-cc-policy-enforcement-audit-logs/
title: Client Connector - policy enforcement audit logging \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:48.946086+00:00
---

# Client Connector - policy enforcement audit logging  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/beyondcorp-cc-policy-enforcement-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  Client Connector - policy enforcement audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how audit logging works for secured private applications using Chrome Enterprise Premium client connector. Enabling Cloud Audit Logs lets you view a user access request to a private application and see all the access levels a user has and has not met.

## Enable audit logs

These logs are considered [Data Access logs](https://docs.cloud.google.com/chrome-enterprise-premium/docs/beyondcorp-service-audit-logging#available-logs). Therefore, they must be explicitly enabled for audit logging under the `beyondcorp.googleapis.com` service name since they are disabled by default.

For information about enabling some or all of your Data Access audit logs, see [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Audit log record content

Each audit log record contains information about users who attempted to access the private application, what [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) were enforced, and whether they were denied or granted access.

The following are some important values:

Field | Value  
---|---  
`authenticationInfo` | The email of the user who tried to access the resource as `principalEmail`.  
`requestMetadata.callerIp` | The IP address the request originated from.  
`requestMetadata.requestAttributes` | Contains access level names used for policy enforcement on the user access.  
`authorizationInfo.resource` | The client connector service resource being accessed.  
`authorizationInfo.granted` | A boolean representing whether the user was permitted the requested access.  
`method.Name` | The called policy enforcement method. Should always be `AuthorizeUser`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
