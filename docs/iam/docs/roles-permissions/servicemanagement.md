---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement/
title: Service Management roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:41:55.451667+00:00
---

# Service Management roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Management. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Management roles

Role | Permissions  
---|---  
  
#### Service Management Administrator 

(`roles/servicemanagement.admin`) Full control of Google Service Management resources.  |  `monitoring.timeSeries.list` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceconsumermanagement.*`

  * `serviceconsumermanagement.consumers.get`
  * `serviceconsumermanagement.quota.get`
  * `serviceconsumermanagement.quota.update`
  * `serviceconsumermanagement.tenancyu.addResource`
  * `serviceconsumermanagement.tenancyu.create`
  * `serviceconsumermanagement.tenancyu.delete`
  * `serviceconsumermanagement.tenancyu.list`
  * `serviceconsumermanagement.tenancyu.removeResource`

`servicemanagement.*`

  * `servicemanagement.services.bind`
  * `servicemanagement.services.check`
  * `servicemanagement.services.create`
  * `servicemanagement.services.delete`
  * `servicemanagement.services.get`
  * `servicemanagement.services.getIamPolicy`
  * `servicemanagement.services.list`
  * `servicemanagement.services.quota`
  * `servicemanagement.services.report`
  * `servicemanagement.services.setIamPolicy`
  * `servicemanagement.services.update`

`serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Service Management Editor 

(`roles/servicemanagement.editor`) Editor role for Service Management.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.bind` `servicemanagement.services.check` `servicemanagement.services.create` `servicemanagement.services.delete` `servicemanagement.services.get` `servicemanagement.services.list` `servicemanagement.services.quota` `servicemanagement.services.report` `servicemanagement.services.update`  
  
#### Service Management Viewer 

(`roles/servicemanagement.viewer`) Viewer role for Service Management.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.get` `servicemanagement.services.list`  
  
#### Service Checker 

(`roles/servicemanagement.checker`) Can check admission of a service during runtime.  |  `servicemanagement.services.check`  
  
#### Service Config Editor 

(`roles/servicemanagement.configEditor`) Access to update the service config and create rollouts.  |  `servicemanagement.services.get` `servicemanagement.services.update`  
  
#### Quota Administrator Beta

(`roles/servicemanagement.quotaAdmin`) Provides access to administer service quotas.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudquotas.*`

  * `cloudquotas.quotas.get`
  * `cloudquotas.quotas.update`

`monitoring.alertPolicies.*`

  * `monitoring.alertPolicies.create`
  * `monitoring.alertPolicies.createTagBinding`
  * `monitoring.alertPolicies.delete`
  * `monitoring.alertPolicies.deleteTagBinding`
  * `monitoring.alertPolicies.get`
  * `monitoring.alertPolicies.list`
  * `monitoring.alertPolicies.listEffectiveTags`
  * `monitoring.alertPolicies.listTagBindings`
  * `monitoring.alertPolicies.update`

`monitoring.timeSeries.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.*`

  * `serviceusage.quotas.get`
  * `serviceusage.quotas.update`

`serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Quota Viewer Beta

(`roles/servicemanagement.quotaViewer`) Provides access to view service quotas.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudquotas.quotas.get` `monitoring.timeSeries.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Service Reporter 

(`roles/servicemanagement.reporter`) Can report usage of a service during runtime.  |  `servicemanagement.services.report`  
  
#### Service Consumer 

(`roles/servicemanagement.serviceConsumer`) Can enable the service.  |  `servicemanagement.services.bind`  
  
#### Service Controller 

(`roles/servicemanagement.serviceController`) Can check preconditions and report usage of a service during runtime.  Lowest-level resources where you can grant this role:

  * Project 

|  `servicemanagement.services.check` `servicemanagement.services.get` `servicemanagement.services.quota` `servicemanagement.services.report`  
  
## Service Management permissions

Permission | Included in roles  
---|---  
  
#### `servicemanagement.services.bind`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.serviceConsumer) (`roles/servicemanagement.serviceConsumer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase SDK Provisioning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkProvisioningServiceAgent) (`roles/firebase.sdkProvisioningServiceAgent`) 

  
  
#### `servicemanagement.services.check`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Checker](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.checker) (`roles/servicemanagement.checker`)  [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.serviceController) (`roles/servicemanagement.serviceController`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.serviceAgent) (`roles/apigateway.serviceAgent`) 
  * [Cloud Endpoints Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints#endpoints.serviceAgent) (`roles/endpoints.serviceAgent`) 

  
  
#### `servicemanagement.services.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent) (`roles/apigateway_management.serviceAgent`) 

  
  
#### `servicemanagement.services.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent) (`roles/apigateway_management.serviceAgent`) 

  
  
#### `servicemanagement.services.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.viewer) (`roles/servicemanagement.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.configEditor) (`roles/servicemanagement.configEditor`)  [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.serviceController) (`roles/servicemanagement.serviceController`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent) (`roles/apigateway_management.serviceAgent`) 
  * [Cloud Endpoints Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints#endpoints.serviceAgent) (`roles/endpoints.serviceAgent`) 
  * [Endpoints Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpointsportal#endpointsportal.serviceAgent) (`roles/endpointsportal.serviceAgent`) 

  
  
#### `servicemanagement.services.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `servicemanagement.services.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.viewer) (`roles/servicemanagement.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent) (`roles/apigateway_management.serviceAgent`) 
  * [Endpoints Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpointsportal#endpointsportal.serviceAgent) (`roles/endpointsportal.serviceAgent`) 

  
  
#### `servicemanagement.services.quota`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.serviceController) (`roles/servicemanagement.serviceController`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.serviceAgent) (`roles/apigateway.serviceAgent`) 
  * [Cloud Endpoints Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints#endpoints.serviceAgent) (`roles/endpoints.serviceAgent`) 

  
  
#### `servicemanagement.services.report`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Reporter](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.reporter) (`roles/servicemanagement.reporter`)  [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.serviceController) (`roles/servicemanagement.serviceController`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Telemetry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.telemetryServiceAgent) (`roles/aiplatform.telemetryServiceAgent`) 
  * [Cloud API Gateway Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.serviceAgent) (`roles/apigateway.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Cloud Endpoints Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints#endpoints.serviceAgent) (`roles/endpoints.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicemanagement.services.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)   
  
#### `servicemanagement.services.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Service Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.editor) (`roles/servicemanagement.editor`)  [Service Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.configEditor) (`roles/servicemanagement.configEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud API Gateway Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent) (`roles/apigateway_management.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
