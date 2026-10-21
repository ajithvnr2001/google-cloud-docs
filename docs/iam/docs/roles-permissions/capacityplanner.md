---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner/
title: Capacity Planner roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:06.148050+00:00
---

# Capacity Planner roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Capacity Planner roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Capacity Planner. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Capacity Planner roles

Role | Permissions  
---|---  
  
#### Capacityplanner Admin Beta

(`roles/capacityplanner.admin`) Admin role for capacityplanner  |  `capacityplanner.*`

  * `capacityplanner.capacityPlans.create`
  * `capacityplanner.capacityPlans.delete`
  * `capacityplanner.capacityPlans.get`
  * `capacityplanner.capacityPlans.list`
  * `capacityplanner.capacityPlans.update`
  * `capacityplanner.forecasts.list`
  * `capacityplanner.messages.generate`
  * `capacityplanner.operations.get`
  * `capacityplanner.planAlertInsights.list`
  * `capacityplanner.usageAlertInsights.list`
  * `capacityplanner.usageHistories.list`
  * `capacityplanner.usageHistories.summarize`

`cloudquotas.quotas.get` `compute.futureReservations.get` `compute.futureReservations.list` `compute.reservations.get` `compute.reservations.list` `monitoring.timeSeries.list` `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Capacity Planner Viewer Beta

(`roles/capacityplanner.viewer`) Read-only access to Capacity Planner resources  |  `capacityplanner.capacityPlans.get` `capacityplanner.capacityPlans.list` `capacityplanner.forecasts.list` `capacityplanner.messages.generate` `capacityplanner.operations.get` `capacityplanner.planAlertInsights.list` `capacityplanner.usageAlertInsights.list` `capacityplanner.usageHistories.*`

  * `capacityplanner.usageHistories.list`
  * `capacityplanner.usageHistories.summarize`

`cloudquotas.quotas.get` `compute.futureReservations.get` `compute.futureReservations.list` `compute.reservations.get` `compute.reservations.list` `monitoring.timeSeries.list` `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Capacity Planner Beta

(`roles/capacityplanner.planner`) Role that enables capacity planning  |  `capacityplanner.*`

  * `capacityplanner.capacityPlans.create`
  * `capacityplanner.capacityPlans.delete`
  * `capacityplanner.capacityPlans.get`
  * `capacityplanner.capacityPlans.list`
  * `capacityplanner.capacityPlans.update`
  * `capacityplanner.forecasts.list`
  * `capacityplanner.messages.generate`
  * `capacityplanner.operations.get`
  * `capacityplanner.planAlertInsights.list`
  * `capacityplanner.usageAlertInsights.list`
  * `capacityplanner.usageHistories.list`
  * `capacityplanner.usageHistories.summarize`

`cloudquotas.quotas.get` `compute.futureReservations.get` `compute.futureReservations.list` `compute.reservations.get` `compute.reservations.list` `monitoring.timeSeries.list` `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Capacity Planner permissions

Permission | Included in roles  
---|---  
  
#### `capacityplanner.capacityPlans.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)   
  
#### `capacityplanner.capacityPlans.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)   
  
#### `capacityplanner.capacityPlans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.capacityPlans.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.capacityPlans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)   
  
#### `capacityplanner.forecasts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.messages.generate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.planAlertInsights.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.usageAlertInsights.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.usageHistories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `capacityplanner.usageHistories.summarize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
