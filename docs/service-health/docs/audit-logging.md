---
url: https://docs.cloud.google.com/service-health/docs/audit-logging/
title: Personalized Service Health audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:05.615422+00:00
---

# Personalized Service Health audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Personalized Service Health audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Personalized Service Health. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Personalized Service Health audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="servicehealth.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Personalized Service Health generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.servicehealth.v1.ServiceHealth.GetEvent`  
`google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationEvent`  
`google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationImpact`  
`google.cloud.servicehealth.v1.ServiceHealth.ListEvents`  
`google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationEvents`  
`google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationImpacts`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetArtifact`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetEvent`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationEvent`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationImpact`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetStatus`  
`google.cloud.servicehealth.v1beta.ServiceHealth.GetStatusForOrganization`  
`google.cloud.servicehealth.v1beta.ServiceHealth.ListArtifacts`  
`google.cloud.servicehealth.v1beta.ServiceHealth.ListEvents`  
`google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationEvents`  
`google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationImpacts`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Personalized Service Health.

### `google.cloud.servicehealth.v1.ServiceHealth`

The following audit logs are associated with methods belonging to `google.cloud.servicehealth.v1.ServiceHealth`.

#### `GetEvent`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.GetEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.events.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.GetEvent" `  




#### `GetOrganizationEvent`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationEvents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationEvent" `  




#### `GetOrganizationImpact`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationImpact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationImpacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.GetOrganizationImpact" `  




#### `ListEvents`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.ListEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.events.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.ListEvents" `  




#### `ListOrganizationEvents`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationEvents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationEvents" `  




#### `ListOrganizationImpacts`

  * **Method** : `google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationImpacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationImpacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1.ServiceHealth.ListOrganizationImpacts" `  




### `google.cloud.servicehealth.v1beta.ServiceHealth`

The following audit logs are associated with methods belonging to `google.cloud.servicehealth.v1beta.ServiceHealth`.

#### `GetArtifact`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.artifacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetArtifact" `  




#### `GetEvent`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.events.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetEvent" `  




#### `GetOrganizationEvent`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationEvents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationEvent" `  




#### `GetOrganizationImpact`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationImpact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationImpacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetOrganizationImpact" `  




#### `GetStatus`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.statuses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetStatus" `  




#### `GetStatusForOrganization`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.GetStatusForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.statuses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.GetStatusForOrganization" `  




#### `ListArtifacts`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.ListArtifacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.artifacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.ListArtifacts" `  




#### `ListEvents`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.ListEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.events.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.ListEvents" `  




#### `ListOrganizationEvents`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationEvents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationEvents" `  




#### `ListOrganizationImpacts`

  * **Method** : `google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationImpacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicehealth.organizationImpacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicehealth.v1beta.ServiceHealth.ListOrganizationImpacts" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
