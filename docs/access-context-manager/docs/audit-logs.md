---
url: https://docs.cloud.google.com/access-context-manager/docs/audit-logs/
title: Audit logging \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:12.420692+00:00
---

# Audit logging  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how audit logging works when securing the Google Cloud console and the Google Cloud APIs with Access Context Manager.

Access Context Manager by default logs all access requests to the Google Cloud console and the Google Cloud APIs that are denied because of security policy violations to Cloud Logging. The audit log records are securely stored in Google infrastructure and available for future analysis. The content of the audit log is available on a per-organization basis in the Google Cloud console. The Access Context Manager audit log is written into the "Audited Resource" logging stream and is available in Cloud Logging.

## Audit log record content

Each audit log record contains information which can be divided into two major categories: the information about the original call, and information about security policy violations. It is filled as follows:

**Audit Log Field** | **Meaning**  
---|---  
**`logName`** | The organization identification and audit log type.   
**`serviceName`** | The name of the service handling the call, `contextawareaccess.googleapis.com`, that resulted in the creation of this audit record.   
**`authenticationInfo.principal_email`** | Email address of the user issuing the original call.   
**`timestamp`** | The time of the targeted operation.   
**`resource`** | The target of the audited operation.   
**`resourceName`** | The organization intended to receive this audit record.   
**`requestMetadata.callerIp`** | The IP address from which the call originated.   
**`requestMetadata.requestAttributes.auth.accessLevels`** | The access levels in the organization that the request satisfied, regardless of whether those access levels are applied in the access binding.   
**`status`** | The overall status of handling an operation described in this record.   
**`metadata`** | An instance of the `google.cloud.audit.ContextAwareAccessAuditMetadata` protobuf type, serialized as a JSON `Struct`. It includes the following fields:

  * `appliedAccessLevels`: The access levels required by the active access policy in the binding.
  * `appliedDryRunAccessLevels`: The access levels required by the dry-run access policy in the binding.
  * `unsatisfiedAccessLevels`: The access levels in the organization that the request failed to satisfy. This list can include access levels that aren't applied in the access binding. To identify which access levels caused an access denial, compare this field with `appliedAccessLevels` or `appliedDryRunAccessLevels`.
  * `evaluationResult`: The evaluation result of the active access policy (`GRANTED` or `DENIED`). If no active access levels are applied in the binding, this field is set to `GRANTED`.
  * `dryRunEvaluationResult`: The evaluation result of the dry-run access policy (`GRANTED` or `DENIED`). If no dry-run access levels are applied in the binding, this field is set to `GRANTED`, even when `evaluationResult` is `DENIED`.
  * `deniedApplications`: The applications for which access was denied.

  
  
## Accessing the audit log

The content of the audit log is available on a per-organization basis in the Google Cloud console. The Access Context Manager audit log is written into the "Audited Resource" logging stream and is available in Cloud Logging.

## What's next

  * Learn more about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * Learn more about [Enabling Cloud Audit Logs](https://docs.cloud.google.com/iap/docs/audit-log-howto) in Identity-Aware Proxy.
  * Learn more about [Audit Logging](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) in VPC Service Controls.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
