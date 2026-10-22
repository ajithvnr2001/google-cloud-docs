---
url: https://docs.cloud.google.com/dns/docs/audit-logging/
title: Cloud DNS audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:20.323060+00:00
---

# Cloud DNS audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Cloud DNS audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud DNS. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud DNS audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="dns.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud DNS generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `dns.changes.get`  
`dns.changes.list`  
`dns.managedZones.get`  
`dns.managedZones.getiampolicy`  
`dns.managedZones.list`  
`dns.managedZones.testiampermissions`  
`dns.policies.get`  
`dns.policies.list`  
`dns.projects.get`  
`dns.resourceRecordSets.get`  
`dns.resourceRecordSets.list`  
`dns.responsePolicies.get`  
`dns.responsePolicies.list`  
`dns.responsePolicyRules.get`  
`dns.responsePolicyRules.list`  
`dns.changes.get`  
`dns.changes.list`  
`dns.managedZones.get`  
`dns.managedZones.getiampolicy`  
`dns.managedZones.list`  
`dns.managedZones.testiampermissions`  
`dns.policies.get`  
`dns.policies.list`  
`dns.projects.get`  
`dns.resourceRecordSets.get`  
`dns.resourceRecordSets.list`  
`dns.responsePolicies.get`  
`dns.responsePolicies.list`  
`dns.responsePolicyRules.get`  
`dns.responsePolicyRules.list`  
`ADMIN_WRITE` | `dns.changes.create`  
`dns.managedZones.create`  
`dns.managedZones.delete`  
`dns.managedZones.patch`  
`dns.managedZones.update`  
`dns.policies.create`  
`dns.policies.delete`  
`dns.policies.patch`  
`dns.policies.update`  
`dns.resourceRecordSets.create`  
`dns.resourceRecordSets.delete`  
`dns.resourceRecordSets.patch`  
`dns.responsePolicies.create`  
`dns.responsePolicies.delete`  
`dns.responsePolicies.patch`  
`dns.responsePolicies.update`  
`dns.responsePolicyRules.create`  
`dns.responsePolicyRules.delete`  
`dns.responsePolicyRules.patch`  
`dns.responsePolicyRules.update`  
`dns.changes.create`  
`dns.managedZones.create`  
`dns.managedZones.delete`  
`dns.managedZones.patch`  
`dns.managedZones.update`  
`dns.policies.create`  
`dns.policies.delete`  
`dns.policies.patch`  
`dns.policies.update`  
`dns.resourceRecordSets.create`  
`dns.resourceRecordSets.delete`  
`dns.resourceRecordSets.patch`  
`dns.responsePolicies.create`  
`dns.responsePolicies.delete`  
`dns.responsePolicies.patch`  
`dns.responsePolicies.update`  
`dns.responsePolicyRules.create`  
`dns.responsePolicyRules.delete`  
`dns.responsePolicyRules.patch`  
`dns.responsePolicyRules.update`  
`DATA_READ` | `dns.dnsKeys.get`  
`dns.dnsKeys.list`  
`dns.managedZoneOperations.get`  
`dns.managedZoneOperations.list`  
`dns.dnsKeys.get`  
`dns.dnsKeys.list`  
`dns.managedZoneOperations.get`  
`dns.managedZoneOperations.list`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud DNS.

### `cloud.dns.api.v1.ChangesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ChangesService`.

#### `create`

  * **Method** : `dns.changes.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.resourceRecordSets.create - ADMIN_WRITE`
    * `dns.resourceRecordSets.delete - ADMIN_WRITE`
    * `dns.resourceRecordSets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.create" `  




#### `get`

  * **Method** : `dns.changes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.changes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.get" `  




#### `list`

  * **Method** : `dns.changes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.changes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.list" `  




### `cloud.dns.api.v1.DnsKeysService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.DnsKeysService`.

#### `get`

  * **Method** : `dns.dnsKeys.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.dnsKeys.get - DATA_READ`
    * `dns.dnsKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.dnsKeys.get" `  




#### `list`

  * **Method** : `dns.dnsKeys.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.dnsKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.dnsKeys.list" `  




### `cloud.dns.api.v1.ManagedZoneOperationsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ManagedZoneOperationsService`.

#### `get`

  * **Method** : `dns.managedZoneOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZoneOperations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZoneOperations.get" `  




#### `list`

  * **Method** : `dns.managedZoneOperations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZoneOperations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZoneOperations.list" `  




### `cloud.dns.api.v1.ManagedZonesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ManagedZonesService`.

#### `create`

  * **Method** : `dns.managedZones.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.create" `  




#### `delete`

  * **Method** : `dns.managedZones.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.delete" `  




#### `get`

  * **Method** : `dns.managedZones.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.get" `  




#### `getiampolicy`

  * **Method** : `dns.managedZones.getiampolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.getiampolicy" `  




#### `list`

  * **Method** : `dns.managedZones.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.list" `  




#### `patch`

  * **Method** : `dns.managedZones.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.patch" `  




#### `testiampermissions`

  * **Method** : `dns.managedZones.testiampermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.testiampermissions" `  




#### `update`

  * **Method** : `dns.managedZones.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.update" `  




### `cloud.dns.api.v1.PoliciesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.PoliciesService`.

#### `create`

  * **Method** : `dns.policies.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.create" `  




#### `delete`

  * **Method** : `dns.policies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.delete" `  




#### `get`

  * **Method** : `dns.policies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.get" `  




#### `list`

  * **Method** : `dns.policies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.list" `  




#### `patch`

  * **Method** : `dns.policies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.patch" `  




#### `update`

  * **Method** : `dns.policies.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.update" `  




### `cloud.dns.api.v1.ProjectsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ProjectsService`.

#### `get`

  * **Method** : `dns.projects.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.projects.get" `  




### `cloud.dns.api.v1.ResourceRecordSetsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ResourceRecordSetsService`.

#### `create`

  * **Method** : `dns.resourceRecordSets.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.create" `  




#### `delete`

  * **Method** : `dns.resourceRecordSets.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.delete" `  




#### `get`

  * **Method** : `dns.resourceRecordSets.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.resourceRecordSets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.get" `  




#### `list`

  * **Method** : `dns.resourceRecordSets.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.resourceRecordSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.list" `  




#### `patch`

  * **Method** : `dns.resourceRecordSets.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.patch" `  




### `cloud.dns.api.v1.ResponsePoliciesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ResponsePoliciesService`.

#### `create`

  * **Method** : `dns.responsePolicies.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.create" `  




#### `delete`

  * **Method** : `dns.responsePolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.delete" `  




#### `get`

  * **Method** : `dns.responsePolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.get" `  




#### `list`

  * **Method** : `dns.responsePolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.list" `  




#### `patch`

  * **Method** : `dns.responsePolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.patch" `  




#### `update`

  * **Method** : `dns.responsePolicies.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.update" `  




### `cloud.dns.api.v1.ResponsePolicyRulesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1.ResponsePolicyRulesService`.

#### `create`

  * **Method** : `dns.responsePolicyRules.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.create" `  




#### `delete`

  * **Method** : `dns.responsePolicyRules.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.delete" `  




#### `get`

  * **Method** : `dns.responsePolicyRules.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicyRules.get - ADMIN_READ`
    * `dns.responsePolicyRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.get" `  




#### `list`

  * **Method** : `dns.responsePolicyRules.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicyRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.list" `  




#### `patch`

  * **Method** : `dns.responsePolicyRules.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.patch" `  




#### `update`

  * **Method** : `dns.responsePolicyRules.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.update" `  




### `cloud.dns.api.v1beta2.ChangesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ChangesService`.

#### `create`

  * **Method** : `dns.changes.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.resourceRecordSets.create - ADMIN_WRITE`
    * `dns.resourceRecordSets.delete - ADMIN_WRITE`
    * `dns.resourceRecordSets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.create" `  




#### `get`

  * **Method** : `dns.changes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.changes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.get" `  




#### `list`

  * **Method** : `dns.changes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.changes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.changes.list" `  




### `cloud.dns.api.v1beta2.DnsKeysService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.DnsKeysService`.

#### `get`

  * **Method** : `dns.dnsKeys.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.dnsKeys.get - DATA_READ`
    * `dns.dnsKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.dnsKeys.get" `  




#### `list`

  * **Method** : `dns.dnsKeys.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.dnsKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.dnsKeys.list" `  




### `cloud.dns.api.v1beta2.ManagedZoneOperationsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ManagedZoneOperationsService`.

#### `get`

  * **Method** : `dns.managedZoneOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZoneOperations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZoneOperations.get" `  




#### `list`

  * **Method** : `dns.managedZoneOperations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZoneOperations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZoneOperations.list" `  




### `cloud.dns.api.v1beta2.ManagedZonesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ManagedZonesService`.

#### `create`

  * **Method** : `dns.managedZones.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.create" `  




#### `delete`

  * **Method** : `dns.managedZones.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.delete" `  




#### `get`

  * **Method** : `dns.managedZones.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.get" `  




#### `getiampolicy`

  * **Method** : `dns.managedZones.getiampolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.getiampolicy" `  




#### `list`

  * **Method** : `dns.managedZones.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.list" `  




#### `patch`

  * **Method** : `dns.managedZones.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.patch" `  




#### `testiampermissions`

  * **Method** : `dns.managedZones.testiampermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.managedZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.testiampermissions" `  




#### `update`

  * **Method** : `dns.managedZones.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.managedZones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.managedZones.update" `  




### `cloud.dns.api.v1beta2.PoliciesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.PoliciesService`.

#### `create`

  * **Method** : `dns.policies.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.create" `  




#### `delete`

  * **Method** : `dns.policies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.delete" `  




#### `get`

  * **Method** : `dns.policies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.get" `  




#### `list`

  * **Method** : `dns.policies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.list" `  




#### `patch`

  * **Method** : `dns.policies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.patch" `  




#### `update`

  * **Method** : `dns.policies.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.policies.update" `  




### `cloud.dns.api.v1beta2.ProjectsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ProjectsService`.

#### `get`

  * **Method** : `dns.projects.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.projects.get" `  




### `cloud.dns.api.v1beta2.ResourceRecordSetsService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ResourceRecordSetsService`.

#### `create`

  * **Method** : `dns.resourceRecordSets.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.create" `  




#### `delete`

  * **Method** : `dns.resourceRecordSets.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.delete" `  




#### `get`

  * **Method** : `dns.resourceRecordSets.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.resourceRecordSets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.get" `  




#### `list`

  * **Method** : `dns.resourceRecordSets.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.resourceRecordSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.list" `  




#### `patch`

  * **Method** : `dns.resourceRecordSets.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.changes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.resourceRecordSets.patch" `  




### `cloud.dns.api.v1beta2.ResponsePoliciesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ResponsePoliciesService`.

#### `create`

  * **Method** : `dns.responsePolicies.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.create" `  




#### `delete`

  * **Method** : `dns.responsePolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.delete" `  




#### `get`

  * **Method** : `dns.responsePolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.get" `  




#### `list`

  * **Method** : `dns.responsePolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.list" `  




#### `patch`

  * **Method** : `dns.responsePolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.patch" `  




#### `update`

  * **Method** : `dns.responsePolicies.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicies.update" `  




### `cloud.dns.api.v1beta2.ResponsePolicyRulesService`

The following audit logs are associated with methods belonging to `cloud.dns.api.v1beta2.ResponsePolicyRulesService`.

#### `create`

  * **Method** : `dns.responsePolicyRules.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.create" `  




#### `delete`

  * **Method** : `dns.responsePolicyRules.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.delete" `  




#### `get`

  * **Method** : `dns.responsePolicyRules.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicyRules.get - ADMIN_READ`
    * `dns.responsePolicyRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.get" `  




#### `list`

  * **Method** : `dns.responsePolicyRules.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dns.responsePolicyRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.list" `  




#### `patch`

  * **Method** : `dns.responsePolicyRules.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.patch" `  




#### `update`

  * **Method** : `dns.responsePolicyRules.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dns.responsePolicyRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="dns.responsePolicyRules.update" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `cloud.dns.api.v1.ManagedZonesService.TestIamPermissions`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
