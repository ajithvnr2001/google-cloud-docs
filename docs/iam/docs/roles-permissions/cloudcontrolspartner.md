---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner/
title: Cloud Controls Partner API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:33.663343+00:00
---

# Cloud Controls Partner API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Controls Partner API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Controls Partner API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Controls Partner API roles

Role | Permissions  
---|---  
  
#### Cloud Controls Partner Admin 

(`roles/cloudcontrolspartner.admin`) Full access to Cloud Controls Partner resources.  |  `cloudcontrolspartner.accessapprovalrequests.list` `cloudcontrolspartner.customers.*`

  * `cloudcontrolspartner.customers.create`
  * `cloudcontrolspartner.customers.delete`
  * `cloudcontrolspartner.customers.get`
  * `cloudcontrolspartner.customers.list`

`cloudcontrolspartner.ekmconnections.get` `cloudcontrolspartner.inspectabilityevents.get` `cloudcontrolspartner.partnerpermissions.get` `cloudcontrolspartner.partners.get` `cloudcontrolspartner.platformcontrols.get` `cloudcontrolspartner.violations.list` `cloudcontrolspartner.workloads.list`  
  
#### Cloud Controls Partner Editor 

(`roles/cloudcontrolspartner.editor`) Editor access to Cloud Controls Partner resources.  |  `cloudcontrolspartner.*`

  * `cloudcontrolspartner.accessapprovalrequests.list`
  * `cloudcontrolspartner.customers.create`
  * `cloudcontrolspartner.customers.delete`
  * `cloudcontrolspartner.customers.get`
  * `cloudcontrolspartner.customers.list`
  * `cloudcontrolspartner.ekmconnections.get`
  * `cloudcontrolspartner.inspectabilityevents.get`
  * `cloudcontrolspartner.partnerpermissions.get`
  * `cloudcontrolspartner.partners.get`
  * `cloudcontrolspartner.platformcontrols.get`
  * `cloudcontrolspartner.violations.get`
  * `cloudcontrolspartner.violations.list`
  * `cloudcontrolspartner.workloads.get`
  * `cloudcontrolspartner.workloads.list`

  
  
#### Cloudcontrolspartner Viewer 

(`roles/cloudcontrolspartner.viewer`) Viewer role for cloudcontrolspartner  |  `cloudcontrolspartner.accessapprovalrequests.list` `cloudcontrolspartner.customers.get` `cloudcontrolspartner.customers.list` `cloudcontrolspartner.ekmconnections.get` `cloudcontrolspartner.inspectabilityevents.get` `cloudcontrolspartner.partnerpermissions.get` `cloudcontrolspartner.partners.get` `cloudcontrolspartner.platformcontrols.get` `cloudcontrolspartner.violations.*`

  * `cloudcontrolspartner.violations.get`
  * `cloudcontrolspartner.violations.list`

`cloudcontrolspartner.workloads.*`

  * `cloudcontrolspartner.workloads.get`
  * `cloudcontrolspartner.workloads.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Controls Partner Inspectability Reader 

(`roles/cloudcontrolspartner.inspectabilityReader`) Readonly access to Cloud Controls Partner inspectability resources.  |  `cloudcontrolspartner.customers.get` `cloudcontrolspartner.customers.list` `cloudcontrolspartner.inspectabilityevents.get` `cloudcontrolspartner.platformcontrols.get`  
  
#### Cloud Controls Partner Monitoring Reader 

(`roles/cloudcontrolspartner.monitoringReader`) Read-only access to Cloud Controls Partner monitoring resources.  |  `cloudcontrolspartner.customers.get` `cloudcontrolspartner.customers.list` `cloudcontrolspartner.violations.*`

  * `cloudcontrolspartner.violations.get`
  * `cloudcontrolspartner.violations.list`

`cloudcontrolspartner.workloads.*`

  * `cloudcontrolspartner.workloads.get`
  * `cloudcontrolspartner.workloads.list`

  
  
#### Cloud Controls Partner Reader 

(`roles/cloudcontrolspartner.reader`) Read-only access to Cloud Controls Partner resources.  |  `cloudcontrolspartner.accessapprovalrequests.list` `cloudcontrolspartner.customers.get` `cloudcontrolspartner.customers.list` `cloudcontrolspartner.ekmconnections.get` `cloudcontrolspartner.inspectabilityevents.get` `cloudcontrolspartner.partnerpermissions.get` `cloudcontrolspartner.partners.get` `cloudcontrolspartner.platformcontrols.get` `cloudcontrolspartner.violations.*`

  * `cloudcontrolspartner.violations.get`
  * `cloudcontrolspartner.violations.list`

`cloudcontrolspartner.workloads.*`

  * `cloudcontrolspartner.workloads.get`
  * `cloudcontrolspartner.workloads.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Controls Partner Access Approval Service Agent 

(`roles/cloudcontrolspartner.accessApprovalServiceAgent`) Gives the Partner Console service account access to read Access Approval Requests for workloads associated with a partner.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `accessapproval.requests.get` `accessapproval.requests.list`  
  
#### Cloud Controls Partner EKM Service Agent 

(`roles/cloudcontrolspartner.ekmServiceAgent`) Gives Cloud Controls Partner service agent permission to list EKM connections, get EKM connection status, and provide EKM diagnostic information.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudkms.ekmConnections.get` `cloudkms.ekmConnections.getIamPolicy` `cloudkms.ekmConnections.list` `cloudkms.ekmConnections.verifyConnectivity`  
  
#### Cloud Controls Partner Monitoring Service Agent 

(`roles/cloudcontrolspartner.monitoringServiceAgent`) Gives Cloud Controls Partner monitoring service agent permission to view and list Assured Workload violations. The role is assigned to enable partner monitoring capability.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `assuredworkloads.violations.get` `assuredworkloads.violations.list`  
  
#### Cloud Controls Partner Support Case Service Agent 

(`roles/cloudcontrolspartner.supportCaseServiceAgent`) Gives the Partner Console service account access to support cases for workloads associated with a partner.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudsupport.techCases.get`  
  
## Cloud Controls Partner API permissions

Permission | Included in roles  
---|---  
  
#### `cloudcontrolspartner.accessapprovalrequests.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.customers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)   
  
#### `cloudcontrolspartner.customers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)   
  
#### `cloudcontrolspartner.customers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Inspectability Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.inspectabilityReader) (`roles/cloudcontrolspartner.inspectabilityReader`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.customers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Controls Partner Inspectability Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.inspectabilityReader) (`roles/cloudcontrolspartner.inspectabilityReader`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.ekmconnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.inspectabilityevents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Inspectability Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.inspectabilityReader) (`roles/cloudcontrolspartner.inspectabilityReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.partnerpermissions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.partners.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.platformcontrols.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Inspectability Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.inspectabilityReader) (`roles/cloudcontrolspartner.inspectabilityReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.violations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.violations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.workloads.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudcontrolspartner.workloads.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Controls Partner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.admin) (`roles/cloudcontrolspartner.admin`)  [Cloud Controls Partner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.editor) (`roles/cloudcontrolspartner.editor`)  [Cloudcontrolspartner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.viewer) (`roles/cloudcontrolspartner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Controls Partner Monitoring Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringReader) (`roles/cloudcontrolspartner.monitoringReader`)  [Cloud Controls Partner Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.reader) (`roles/cloudcontrolspartner.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
