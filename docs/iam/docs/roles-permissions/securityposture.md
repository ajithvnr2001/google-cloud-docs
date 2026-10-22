---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture/
title: Security Posture API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:58.604162+00:00
---

# Security Posture API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Security Posture API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Security Posture API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Security Posture API roles

Role | Permissions  
---|---  
  
#### Security Posture Admin 

(`roles/securityposture.admin`) Full access to Security Posture service APIs.  Lowest-level resources where you can grant this role:

  * Organization

|  `orgpolicy.*`

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.organizations.get` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `securityposture.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`
  * `securityposture.operations.delete`
  * `securityposture.operations.get`
  * `securityposture.operations.list`
  * `securityposture.postureDeployments.create`
  * `securityposture.postureDeployments.delete`
  * `securityposture.postureDeployments.get`
  * `securityposture.postureDeployments.list`
  * `securityposture.postureDeployments.update`
  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`
  * `securityposture.postures.create`
  * `securityposture.postures.delete`
  * `securityposture.postures.extract`
  * `securityposture.postures.get`
  * `securityposture.postures.list`
  * `securityposture.postures.update`
  * `securityposture.reports.create`
  * `securityposture.reports.get`
  * `securityposture.reports.list`

  
  
#### Security Posture Viewer 

(`roles/securityposture.viewer`) Read only access to all the SecurityPosture Service resources.  |  `resourcemanager.organizations.get` `securityposture.locations.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`

`securityposture.operations.get` `securityposture.operations.list` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postureTemplates.*`

  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`

`securityposture.postures.get` `securityposture.postures.list` `securityposture.reports.get` `securityposture.reports.list`  
  
#### Security Posture Deployer 

(`roles/securityposture.postureDeployer`) Mutate and read permissions to the Posture Deployment resource.  |  `orgpolicy.*`

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.organizations.get` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `securityposture.operations.get` `securityposture.postureDeployments.*`

  * `securityposture.postureDeployments.create`
  * `securityposture.postureDeployments.delete`
  * `securityposture.postureDeployments.get`
  * `securityposture.postureDeployments.list`
  * `securityposture.postureDeployments.update`

  
  
#### Security Posture Deployments Viewer 

(`roles/securityposture.postureDeploymentsViewer`) Read only access to the Posture Deployment resource.  |  `resourcemanager.organizations.get` `securityposture.operations.get` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list`  
  
#### Security Posture Resource Editor 

(`roles/securityposture.postureEditor`) Mutate and read permissions to the Posture resource.  |  `securityposture.operations.get` `securityposture.postures.*`

  * `securityposture.postures.create`
  * `securityposture.postures.delete`
  * `securityposture.postures.extract`
  * `securityposture.postures.get`
  * `securityposture.postures.list`
  * `securityposture.postures.update`

  
  
#### Security Posture Resource Viewer 

(`roles/securityposture.postureViewer`) Read only access to the Posture resource.  |  `resourcemanager.organizations.get` `securityposture.operations.get` `securityposture.postures.get` `securityposture.postures.list`  
  
#### Security Posture Shift-Left Validator 

(`roles/securityposture.reportCreator`) Create access for Reports, e.g. IaC Validation Report.  |  `securityposture.operations.get` `securityposture.reports.*`

  * `securityposture.reports.create`
  * `securityposture.reports.get`
  * `securityposture.reports.list`

  
  
## Security Posture API permissions

Permission | Included in roles  
---|---  
  
#### `securityposture.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `securityposture.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `securityposture.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)   
  
#### `securityposture.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  [Security Posture Deployments Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeploymentsViewer) (`roles/securityposture.postureDeploymentsViewer`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)  [Security Posture Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureViewer) (`roles/securityposture.postureViewer`)  [Security Posture Shift-Left Validator](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.reportCreator) (`roles/securityposture.reportCreator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `securityposture.postureDeployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postureDeployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postureDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  [Security Posture Deployments Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeploymentsViewer) (`roles/securityposture.postureDeploymentsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postureDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  [Security Posture Deployments Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeploymentsViewer) (`roles/securityposture.postureDeploymentsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postureDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)   
  
#### `securityposture.postureTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `securityposture.postureTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `securityposture.postures.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postures.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)   
  
#### `securityposture.postures.extract`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)   
  
#### `securityposture.postures.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)  [Security Posture Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureViewer) (`roles/securityposture.postureViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securityposture.postures.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)  [Security Posture Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureViewer) (`roles/securityposture.postureViewer`)   
  
#### `securityposture.postures.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureEditor) (`roles/securityposture.postureEditor`)   
  
#### `securityposture.reports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Shift-Left Validator](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.reportCreator) (`roles/securityposture.reportCreator`)   
  
#### `securityposture.reports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Shift-Left Validator](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.reportCreator) (`roles/securityposture.reportCreator`)   
  
#### `securityposture.reports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Posture Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.viewer) (`roles/securityposture.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Posture Shift-Left Validator](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.reportCreator) (`roles/securityposture.reportCreator`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
