---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/audit-logging/
title: Confidential Computing audit logging \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:11.504576+00:00
---

# Confidential Computing audit logging  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Confidential Computing audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Confidential Computing. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Confidential Computing audit logs use the service name `confidentialcomputing.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="confidentialcomputing.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Confidential Computing generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.cloud.confidentialcomputing.v1.ConfidentialComputing.CreateChallenge`  
`google.cloud.confidentialcomputing.v1.ConfidentialComputing.VerifyAttestation`  
`google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.CreateChallenge`  
`google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.VerifyAttestation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Confidential Computing.

### `google.cloud.confidentialcomputing.v1.ConfidentialComputing`

The following audit logs are associated with methods belonging to `google.cloud.confidentialcomputing.v1.ConfidentialComputing`.

#### `CreateChallenge`

  * **Method** : `google.cloud.confidentialcomputing.v1.ConfidentialComputing.CreateChallenge`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `confidentialcomputing.challenges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.confidentialcomputing.v1.ConfidentialComputing.CreateChallenge" `  




#### `VerifyAttestation`

  * **Method** : `google.cloud.confidentialcomputing.v1.ConfidentialComputing.VerifyAttestation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `confidentialcomputing.challenges.verify - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.confidentialcomputing.v1.ConfidentialComputing.VerifyAttestation" `  




### `google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing`

The following audit logs are associated with methods belonging to `google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing`.

#### `CreateChallenge`

  * **Method** : `google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.CreateChallenge`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `confidentialcomputing.challenges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.CreateChallenge" `  




#### `VerifyAttestation`

  * **Method** : `google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.VerifyAttestation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `confidentialcomputing.challenges.verify - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.confidentialcomputing.v1alpha1.ConfidentialComputing.VerifyAttestation" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
