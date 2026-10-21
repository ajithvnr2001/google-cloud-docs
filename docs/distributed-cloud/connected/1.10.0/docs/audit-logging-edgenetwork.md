---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/audit-logging-edgenetwork/
title: Google Distributed Cloud audit logging \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:34:53.336849+00:00
---

# Google Distributed Cloud audit logging  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/audit-logging-edgenetwork/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)



Send feedback 

#  Google Distributed Cloud audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Google Distributed Cloud. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Google Distributed Cloud audit logs use the service name `edgenetwork.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="edgenetwork.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Distributed Cloud generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseInterconnect`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseNetwork`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseRouter`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnect`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnectAttachment`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetNetwork`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetRouter`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetSubnet`  
`google.cloud.edgenetwork.v1.EdgeNetwork.GetZone`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnectAttachments`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnects`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListNetworks`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListRouters`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListSubnets`  
`google.cloud.edgenetwork.v1.EdgeNetwork.ListZones`  
`ADMIN_WRITE` | `google.cloud.edgenetwork.v1.EdgeNetwork.CreateInterconnectAttachment`  
`google.cloud.edgenetwork.v1.EdgeNetwork.CreateNetwork`  
`google.cloud.edgenetwork.v1.EdgeNetwork.CreateRouter`  
`google.cloud.edgenetwork.v1.EdgeNetwork.CreateSubnet`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DeleteInterconnectAttachment`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DeleteNetwork`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DeleteRouter`  
`google.cloud.edgenetwork.v1.EdgeNetwork.DeleteSubnet`  
`google.cloud.edgenetwork.v1.EdgeNetwork.InitializeZone`  
`google.cloud.edgenetwork.v1.EdgeNetwork.UpdateRouter`  
`google.cloud.edgenetwork.v1.EdgeNetwork.UpdateSubnet`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Distributed Cloud.

### `google.cloud.edgenetwork.v1.EdgeNetwork`

The following audit logs are associated with methods belonging to `google.cloud.edgenetwork.v1.EdgeNetwork`.

#### `CreateInterconnectAttachment`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.CreateInterconnectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.interconnectAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.CreateInterconnectAttachment" `  




#### `CreateNetwork`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.CreateNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.networks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.CreateNetwork" `  




#### `CreateRouter`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.CreateRouter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.routers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.CreateRouter" `  




#### `CreateSubnet`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.CreateSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.subnetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.CreateSubnet" `  




#### `DeleteInterconnectAttachment`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DeleteInterconnectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.interconnectAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DeleteInterconnectAttachment" `  




#### `DeleteNetwork`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DeleteNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.networks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DeleteNetwork" `  




#### `DeleteRouter`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DeleteRouter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.routers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DeleteRouter" `  




#### `DeleteSubnet`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DeleteSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.subnetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DeleteSubnet" `  




#### `DiagnoseInterconnect`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseInterconnect`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.interconnects.getDiagnostics - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseInterconnect" `  




#### `DiagnoseNetwork`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.networks.getStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseNetwork" `  




#### `DiagnoseRouter`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseRouter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.routers.getRouterStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.DiagnoseRouter" `  




#### `GetInterconnect`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnect`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.interconnects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnect" `  




#### `GetInterconnectAttachment`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.interconnectAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetInterconnectAttachment" `  




#### `GetNetwork`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.networks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetNetwork" `  




#### `GetRouter`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetRouter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetRouter" `  




#### `GetSubnet`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetSubnet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.subnetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetSubnet" `  




#### `GetZone`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.GetZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.zones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.GetZone" `  




#### `InitializeZone`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.InitializeZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.zones.initialize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.InitializeZone" `  




#### `ListInterconnectAttachments`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnectAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.interconnectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnectAttachments" `  




#### `ListInterconnects`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.interconnects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListInterconnects" `  




#### `ListNetworks`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListNetworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.networks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListNetworks" `  




#### `ListRouters`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListRouters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.routers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListRouters" `  




#### `ListSubnets`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListSubnets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListSubnets" `  




#### `ListZones`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.ListZones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `edgenetwork.zones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.ListZones" `  




#### `UpdateRouter`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.UpdateRouter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.routers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.UpdateRouter" `  




#### `UpdateSubnet`

  * **Method** : `google.cloud.edgenetwork.v1.EdgeNetwork.UpdateSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `edgenetwork.subnetworks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.edgenetwork.v1.EdgeNetwork.UpdateSubnet" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
