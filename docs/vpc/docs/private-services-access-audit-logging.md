---
url: https://docs.cloud.google.com/vpc/docs/private-services-access-audit-logging/
title: Private services access audit logging \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:59.045647+00:00
---

# Private services access audit logging  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-services-access-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private services access audit logging

This document lists the audited methods for Service Networking. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Service Networking audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="servicenetworking.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Service Networking generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.servicenetworking.v1.ServicePeeringManager.GetVpcServiceControls`  
`google.cloud.servicenetworking.v1.ServicePeeringManager.ListConnections`  
`google.cloud.servicenetworking.v1.ServicePeeringManager.ListPeeredDnsDomains`  
`ADMIN_WRITE` | `google.cloud.servicenetworking.v1.ServicePeeringManager.CreateConnection` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.CreatePeeredDnsDomain` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.DeleteConnection` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.DeletePeeredDnsDomain` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.DisableVpcServiceControls` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.EnableVpcServiceControls` (LRO)  
`google.cloud.servicenetworking.v1.ServicePeeringManager.UpdateConnection` (LRO)  
`google.longrunning.Operations.GetOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Service Networking.

### `google.cloud.servicenetworking.v1.ServicePeeringManager`

The following audit logs are associated with methods belonging to `google.cloud.servicenetworking.v1.ServicePeeringManager`.

#### `CreateConnection`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.addPeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.CreateConnection" `  




#### `CreatePeeredDnsDomain`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.CreatePeeredDnsDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.createPeeredDnsDomain - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.CreatePeeredDnsDomain" `  




#### `DeleteConnection`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.deleteConnection - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.DeleteConnection" `  




#### `DeletePeeredDnsDomain`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.DeletePeeredDnsDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.deletePeeredDnsDomain - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.DeletePeeredDnsDomain" `  




#### `DisableVpcServiceControls`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.DisableVpcServiceControls`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.disableVpcServiceControls - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.DisableVpcServiceControls" `  




#### `EnableVpcServiceControls`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.EnableVpcServiceControls`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.enableVpcServiceControls - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.EnableVpcServiceControls" `  




#### `GetVpcServiceControls`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.GetVpcServiceControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicenetworking.services.getVpcServiceControls - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.GetVpcServiceControls" `  




#### `ListConnections`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicenetworking.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.ListConnections" `  




#### `ListPeeredDnsDomains`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.ListPeeredDnsDomains`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicenetworking.services.listPeeredDnsDomains - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.ListPeeredDnsDomains" `  




#### `UpdateConnection`

  * **Method** : `google.cloud.servicenetworking.v1.ServicePeeringManager.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.services.addPeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.servicenetworking.v1.ServicePeeringManager.UpdateConnection" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicenetworking.operations.get - DATA_READ`
    * `servicenetworking.services.addPeering - ADMIN_WRITE`
    * `servicenetworking.services.deleteConnection - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.servicenetworking.v1.ServicePeeringManager.AddDnsRecordSet`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.AddDnsZone`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.AddRoles`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.AddSubnetwork`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.GetConsumerConfig`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.GetDnsRecordSet`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.GetDnsZone`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.ListDnsRecordSets`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.ListDnsZones`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.RemoveDnsRecordSet`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.RemoveDnsZone`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.SearchRange`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.UpdateConsumerConfig`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.UpdateDnsRecordSet`
  * `google.cloud.servicenetworking.v1.ServicePeeringManager.ValidateConsumerConfig`
  * `google.cloud.servicenetworking.v1beta.ServicePeeringManager.AddSubnetwork`
  * `google.cloud.servicenetworking.v1beta.ServicePeeringManager.CreateConnection`
  * `google.cloud.servicenetworking.v1beta.ServicePeeringManager.ListConnections`
  * `google.cloud.servicenetworking.v1beta.ServicePeeringManager.SearchRange`
  * `google.cloud.servicenetworking.v1beta.ServicePeeringManager.UpdateConnection`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
