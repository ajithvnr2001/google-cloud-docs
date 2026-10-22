---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager/
title: Access Context Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:12.676452+00:00
---

# Access Context Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Access Context Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Access Context Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Access Context Manager roles

Role | Permissions  
---|---  
  
#### Access Context Manager Admin 

(`roles/accesscontextmanager.admin`) Admin role for Access Context Manager  |  `accesscontextmanager.*`

  * `accesscontextmanager.accessLevels.create`
  * `accesscontextmanager.accessLevels.delete`
  * `accesscontextmanager.accessLevels.get`
  * `accesscontextmanager.accessLevels.list`
  * `accesscontextmanager.accessLevels.replaceAll`
  * `accesscontextmanager.accessLevels.update`
  * `accesscontextmanager.authorizedOrgsDescs.create`
  * `accesscontextmanager.authorizedOrgsDescs.delete`
  * `accesscontextmanager.authorizedOrgsDescs.get`
  * `accesscontextmanager.authorizedOrgsDescs.list`
  * `accesscontextmanager.authorizedOrgsDescs.update`
  * `accesscontextmanager.gcpUserAccessBindings.create`
  * `accesscontextmanager.gcpUserAccessBindings.delete`
  * `accesscontextmanager.gcpUserAccessBindings.get`
  * `accesscontextmanager.gcpUserAccessBindings.list`
  * `accesscontextmanager.gcpUserAccessBindings.update`
  * `accesscontextmanager.policies.create`
  * `accesscontextmanager.policies.delete`
  * `accesscontextmanager.policies.get`
  * `accesscontextmanager.policies.getIamPolicy`
  * `accesscontextmanager.policies.list`
  * `accesscontextmanager.policies.setIamPolicy`
  * `accesscontextmanager.policies.update`
  * `accesscontextmanager.servicePerimeters.commit`
  * `accesscontextmanager.servicePerimeters.create`
  * `accesscontextmanager.servicePerimeters.delete`
  * `accesscontextmanager.servicePerimeters.get`
  * `accesscontextmanager.servicePerimeters.list`
  * `accesscontextmanager.servicePerimeters.replaceAll`
  * `accesscontextmanager.servicePerimeters.update`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Context Manager Editor 

(`roles/accesscontextmanager.editor`) Editor role for Access Context Manager  |  `accesscontextmanager.accessLevels.*`

  * `accesscontextmanager.accessLevels.create`
  * `accesscontextmanager.accessLevels.delete`
  * `accesscontextmanager.accessLevels.get`
  * `accesscontextmanager.accessLevels.list`
  * `accesscontextmanager.accessLevels.replaceAll`
  * `accesscontextmanager.accessLevels.update`

`accesscontextmanager.authorizedOrgsDescs.*`

  * `accesscontextmanager.authorizedOrgsDescs.create`
  * `accesscontextmanager.authorizedOrgsDescs.delete`
  * `accesscontextmanager.authorizedOrgsDescs.get`
  * `accesscontextmanager.authorizedOrgsDescs.list`
  * `accesscontextmanager.authorizedOrgsDescs.update`

`accesscontextmanager.gcpUserAccessBindings.*`

  * `accesscontextmanager.gcpUserAccessBindings.create`
  * `accesscontextmanager.gcpUserAccessBindings.delete`
  * `accesscontextmanager.gcpUserAccessBindings.get`
  * `accesscontextmanager.gcpUserAccessBindings.list`
  * `accesscontextmanager.gcpUserAccessBindings.update`

`accesscontextmanager.policies.create` `accesscontextmanager.policies.delete` `accesscontextmanager.policies.get` `accesscontextmanager.policies.getIamPolicy` `accesscontextmanager.policies.list` `accesscontextmanager.policies.update` `accesscontextmanager.servicePerimeters.*`

  * `accesscontextmanager.servicePerimeters.commit`
  * `accesscontextmanager.servicePerimeters.create`
  * `accesscontextmanager.servicePerimeters.delete`
  * `accesscontextmanager.servicePerimeters.get`
  * `accesscontextmanager.servicePerimeters.list`
  * `accesscontextmanager.servicePerimeters.replaceAll`
  * `accesscontextmanager.servicePerimeters.update`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Context Manager Admin 

(`roles/accesscontextmanager.policyAdmin`) Full access to policies, access levels, access zones and authorized orgs descs.  |  `accesscontextmanager.accessLevels.*`

  * `accesscontextmanager.accessLevels.create`
  * `accesscontextmanager.accessLevels.delete`
  * `accesscontextmanager.accessLevels.get`
  * `accesscontextmanager.accessLevels.list`
  * `accesscontextmanager.accessLevels.replaceAll`
  * `accesscontextmanager.accessLevels.update`

`accesscontextmanager.authorizedOrgsDescs.*`

  * `accesscontextmanager.authorizedOrgsDescs.create`
  * `accesscontextmanager.authorizedOrgsDescs.delete`
  * `accesscontextmanager.authorizedOrgsDescs.get`
  * `accesscontextmanager.authorizedOrgsDescs.list`
  * `accesscontextmanager.authorizedOrgsDescs.update`

`accesscontextmanager.policies.*`

  * `accesscontextmanager.policies.create`
  * `accesscontextmanager.policies.delete`
  * `accesscontextmanager.policies.get`
  * `accesscontextmanager.policies.getIamPolicy`
  * `accesscontextmanager.policies.list`
  * `accesscontextmanager.policies.setIamPolicy`
  * `accesscontextmanager.policies.update`

`accesscontextmanager.servicePerimeters.*`

  * `accesscontextmanager.servicePerimeters.commit`
  * `accesscontextmanager.servicePerimeters.create`
  * `accesscontextmanager.servicePerimeters.delete`
  * `accesscontextmanager.servicePerimeters.get`
  * `accesscontextmanager.servicePerimeters.list`
  * `accesscontextmanager.servicePerimeters.replaceAll`
  * `accesscontextmanager.servicePerimeters.update`

`cloudasset.assets.searchAllResources` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Context Manager Viewer 

(`roles/accesscontextmanager.viewer`) Viewer role for Access Context Manager  |  `accesscontextmanager.accessLevels.get` `accesscontextmanager.accessLevels.list` `accesscontextmanager.authorizedOrgsDescs.get` `accesscontextmanager.authorizedOrgsDescs.list` `accesscontextmanager.gcpUserAccessBindings.get` `accesscontextmanager.gcpUserAccessBindings.list` `accesscontextmanager.policies.get` `accesscontextmanager.policies.getIamPolicy` `accesscontextmanager.policies.list` `accesscontextmanager.servicePerimeters.get` `accesscontextmanager.servicePerimeters.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Access Binding Admin 

(`roles/accesscontextmanager.gcpAccessAdmin`) Create, edit, and change Cloud access bindings.  |  `accesscontextmanager.gcpUserAccessBindings.*`

  * `accesscontextmanager.gcpUserAccessBindings.create`
  * `accesscontextmanager.gcpUserAccessBindings.delete`
  * `accesscontextmanager.gcpUserAccessBindings.get`
  * `accesscontextmanager.gcpUserAccessBindings.list`
  * `accesscontextmanager.gcpUserAccessBindings.update`

  
  
#### Cloud Access Binding Reader 

(`roles/accesscontextmanager.gcpAccessReader`) Read access to Cloud access bindings.  |  `accesscontextmanager.gcpUserAccessBindings.get` `accesscontextmanager.gcpUserAccessBindings.list`  
  
#### Access Context Manager Editor 

(`roles/accesscontextmanager.policyEditor`) Edit access to policies. Create, edit, and change access levels, access zones and authorized orgs descs.  |  `accesscontextmanager.accessLevels.*`

  * `accesscontextmanager.accessLevels.create`
  * `accesscontextmanager.accessLevels.delete`
  * `accesscontextmanager.accessLevels.get`
  * `accesscontextmanager.accessLevels.list`
  * `accesscontextmanager.accessLevels.replaceAll`
  * `accesscontextmanager.accessLevels.update`

`accesscontextmanager.authorizedOrgsDescs.*`

  * `accesscontextmanager.authorizedOrgsDescs.create`
  * `accesscontextmanager.authorizedOrgsDescs.delete`
  * `accesscontextmanager.authorizedOrgsDescs.get`
  * `accesscontextmanager.authorizedOrgsDescs.list`
  * `accesscontextmanager.authorizedOrgsDescs.update`

`accesscontextmanager.policies.create` `accesscontextmanager.policies.delete` `accesscontextmanager.policies.get` `accesscontextmanager.policies.getIamPolicy` `accesscontextmanager.policies.list` `accesscontextmanager.policies.update` `accesscontextmanager.servicePerimeters.*`

  * `accesscontextmanager.servicePerimeters.commit`
  * `accesscontextmanager.servicePerimeters.create`
  * `accesscontextmanager.servicePerimeters.delete`
  * `accesscontextmanager.servicePerimeters.get`
  * `accesscontextmanager.servicePerimeters.list`
  * `accesscontextmanager.servicePerimeters.replaceAll`
  * `accesscontextmanager.servicePerimeters.update`

`cloudasset.assets.searchAllResources` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Context Manager Reader 

(`roles/accesscontextmanager.policyReader`) Read access to policies, access levels, access zones and authorized orgs descs.  |  `accesscontextmanager.accessLevels.get` `accesscontextmanager.accessLevels.list` `accesscontextmanager.authorizedOrgsDescs.get` `accesscontextmanager.authorizedOrgsDescs.list` `accesscontextmanager.policies.get` `accesscontextmanager.policies.getIamPolicy` `accesscontextmanager.policies.list` `accesscontextmanager.servicePerimeters.get` `accesscontextmanager.servicePerimeters.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### VPC Service Controls Troubleshooter Viewer 

(`roles/accesscontextmanager.vpcScTroubleshooterViewer`) |  `accesscontextmanager.accessLevels.get` `accesscontextmanager.accessLevels.list` `accesscontextmanager.authorizedOrgsDescs.get` `accesscontextmanager.authorizedOrgsDescs.list` `accesscontextmanager.policies.get` `accesscontextmanager.policies.getIamPolicy` `accesscontextmanager.policies.list` `accesscontextmanager.servicePerimeters.get` `accesscontextmanager.servicePerimeters.list` `iam.roles.get` `logging.exclusions.get` `logging.exclusions.list` `logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Access Context Manager permissions

Permission | Included in roles  
---|---  
  
#### `accesscontextmanager.accessLevels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.accessLevels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.accessLevels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.accessLevels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accesscontextmanager.accessLevels.replaceAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.accessLevels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.authorizedOrgsDescs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.authorizedOrgsDescs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.authorizedOrgsDescs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accesscontextmanager.authorizedOrgsDescs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accesscontextmanager.authorizedOrgsDescs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.gcpUserAccessBindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)   
  
#### `accesscontextmanager.gcpUserAccessBindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)   
  
#### `accesscontextmanager.gcpUserAccessBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)  [Cloud Access Binding Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessReader) (`roles/accesscontextmanager.gcpAccessReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `accesscontextmanager.gcpUserAccessBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)  [Cloud Access Binding Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessReader) (`roles/accesscontextmanager.gcpAccessReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `accesscontextmanager.gcpUserAccessBindings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)   
  
#### `accesscontextmanager.policies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.policies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.policies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accesscontextmanager.policies.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accesscontextmanager.policies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.policies.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `accesscontextmanager.policies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.servicePerimeters.commit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.servicePerimeters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.servicePerimeters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.servicePerimeters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [SLZ BQDW Blueprint Organization Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwOrgRemediator) (`roles/securedlandingzone.bqdwOrgRemediator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `accesscontextmanager.servicePerimeters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.viewer) (`roles/accesscontextmanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)  [VPC Service Controls Troubleshooter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.vpcScTroubleshooterViewer) (`roles/accesscontextmanager.vpcScTroubleshooterViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [SLZ BQDW Blueprint Organization Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwOrgRemediator) (`roles/securedlandingzone.bqdwOrgRemediator`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `accesscontextmanager.servicePerimeters.replaceAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)   
  
#### `accesscontextmanager.servicePerimeters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.admin) (`roles/accesscontextmanager.admin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`)  [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)  [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)  [SLZ BQDW Blueprint Organization Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwOrgRemediator) (`roles/securedlandingzone.bqdwOrgRemediator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
