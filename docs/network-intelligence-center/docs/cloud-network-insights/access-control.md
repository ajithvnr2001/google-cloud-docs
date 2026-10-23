---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-control/
title: Roles and permissions \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:26.554240+00:00
---

# Roles and permissions  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions needed to access Cloud Network Insights. For a detailed description of IAM, see the [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs/overview).

You can grant users or service accounts permissions or predefined roles, or you can create a custom role that uses permissions that you specify.

The roles granted to users in Google Cloud are replicated in AppNeta. If you can edit Cloud Network Insights resources in the Google Cloud console, you can edit them in AppNeta.

## Roles

This section describes how to use predefined and custom roles when granting permissions for Cloud Network Insights.

### Predefined roles for Cloud Network Insights

Cloud Network Insights has the following predefined roles that allow you to enable Cloud Network Insights and modify all Cloud Network Insights resources (Admin), modify all Cloud Network Insights resources (Editor), or view the resources (Viewer):

  * Cloud Network Insights Admin (`roles/networkmanagement.CloudNetworkInsightsAdmin`)
  * Cloud Network Insights Editor (`roles/networkmanagement.CloudNetworkInsightsEditor`)
  * Cloud Network Insights Viewer (`roles/networkmanagement.CloudNetworkInsightsViewer`)



The predefined Network Management roles also include the same permissions as the Cloud Network Insights permissions.

Both the Cloud Network Insights Admin (`roles/networkmanagement.CloudNetworkInsightsAdmin`) and the Cloud Network Insights Editor (`roles/networkmanagement.CloudNetworkInsightsEditor`) roles can modify all Cloud Network Insights resources. However, only the Cloud Network Insights Admin role can accept the Broadcom Terms of Service when enabling Cloud Network Insights for the first time in a project. After Cloud Network Insights has been enabled, users with either role can enable or disable the Cloud Network Insights.

If you want to grant users the ability to view Cloud Network Insights in projects where it is already enabled or to read telemetry and path data, you can grant users the Cloud Network Insights Viewer (`roles/networkmanagement.CloudNetworkInsightsViewer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Cloud Network Insights roles

The following tables describe the IAM predefined roles and their associated permissions for Cloud Network Insights.

For more information, see the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

Role | Permissions  
---|---  
  
#### Cloud Network Insights Admin

(`roles/networkmanagement.CloudNetworkInsightsAdmin`)  
Full access to Cloud Network Insights resources.  
Accept the Broadcom Terms of Service when enabling Cloud Network Insights for the first time in a project.  
Lowest-level resources where you can grant this role:  


  * Project

| 

  * networkmanagement.locations.get
  * networkmanagement.locations.list
  * networkmanagement.monitoringpoints.downloadConfig
  * networkmanagement.monitoringpoints.get
  * networkmanagement.monitoringpoints.list
  * networkmanagement.networkpaths.get
  * networkmanagement.networkpaths.list
  * networkmanagement.operations.get
  * networkmanagement.operations.list
  * networkmanagement.providers.create
  * networkmanagement.providers.delete
  * networkmanagement.providers.generateProviderAccessToken
  * networkmanagement.providers.get
  * networkmanagement.providers.list
  * networkmanagement.webpaths.get
  * networkmanagement.webpaths.list
  * productrequirementsservice.requirements.check
  * productrequirementsservice.requirements.record
  * resourcemanager.organizations.get
  * resourcemanager.organizations.list
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
#### Cloud Network Insights Editor

(`roles/networkmanagement.CloudNetworkInsightsEditor`)  
Editor access to Cloud Network Insightsresources.  
Lowest-level resources where you can grant this role:  


  * Project

| 

  * networkmanagement.locations.get
  * networkmanagement.locations.list
  * networkmanagement.monitoringpoints.downloadConfig
  * networkmanagement.monitoringpoints.get
  * networkmanagement.monitoringpoints.list
  * networkmanagement.networkpaths.get
  * networkmanagement.networkpaths.list
  * networkmanagement.operations.get
  * networkmanagement.operations.list
  * networkmanagement.providers.create
  * networkmanagement.providers.delete
  * networkmanagement.providers.generateProviderAccessToken
  * networkmanagement.providers.get
  * networkmanagement.providers.list
  * networkmanagement.webpaths.get
  * networkmanagement.webpaths.list
  * productrequirementsservice.requirements.check
  * resourcemanager.organizations.get
  * resourcemanager.organizations.list
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
#### Cloud Network Insights Viewer

(`roles/networkmanagement.CloudNetworkInsightsViewer`)  
Read-only access to Cloud Network Insightsresources for telemetry and path data.  
Lowest-level resources where you can grant this role:  


  * Project

| 

  * networkmanagement.monitoringpoints.get
  * networkmanagement.monitoringpoints.list
  * networkmanagement.networkpaths.get
  * networkmanagement.networkpaths.list
  * networkmanagement.providers.generateProviderAccessToken
  * networkmanagement.providers.get
  * networkmanagement.providers.list
  * networkmanagement.webpaths.get
  * networkmanagement.webpaths.list
  * productrequirementsservice.requirements.check
  * resourcemanager.organizations.get
  * resourcemanager.organizations.list
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
### Alerts and logs roles

The following table describes the IAM predefined roles and their associated permissions to view or manage alerts and logs based on Cloud Network Insights data. Users also need a Cloud Network Insights role.

Role | Permissions  
---|---  
  
#### Logs Viewer

(`roles/logging.viewer`)  
Provides access to view logs.  
Lowest-level resources where you can grant this role:  


  * View

| 

  * logging.buckets.get
  * logging.buckets.list
  * logging.exclusions.get
  * logging.exclusions.list
  * logging.links.get
  * logging.links.list
  * logging.locations.*
  * logging.logEntries.list
  * logging.logMetrics.get
  * logging.logMetrics.list
  * logging.logScopes.get
  * logging.logScopes.list
  * logging.logServiceIndexes.list
  * logging.logServices.list
  * logging.logs.list
  * logging.operations.get
  * logging.operations.list
  * logging.queries.getShared
  * logging.queries.listShared
  * logging.queries.usePrivate
  * logging.sinks.get
  * logging.sinks.list
  * logging.usage.get
  * logging.views.get
  * logging.views.list
  * observability.scopes.get
  * resourcemanager.projects.get

  
  
#### Logs Configuration Writer

(`roles/logging.configWriter`)  
Create alerting policies.  
Lowest-level resources where you can grant this role:  


  * View

| 

  * logging.buckets.create
  * logging.buckets.createTagBinding
  * logging.buckets.delete
  * logging.buckets.deleteTagBinding
  * logging.buckets.get
  * logging.buckets.list
  * logging.buckets.listEffectiveTags
  * logging.buckets.listTagBindings
  * logging.buckets.undelete
  * logging.buckets.update
  * logging.exclusions.*
  * logging.links.*
  * logging.locations.*
  * logging.logMetrics.*
  * logging.logScopes.*
  * logging.logServiceIndexes.list
  * logging.logServices.list
  * logging.logs.list
  * logging.notificationRules.*
  * logging.operations.*
  * logging.settings.*
  * logging.sinks.*
  * logging.sqlAlerts.*
  * logging.views.create
  * logging.views.delete
  * logging.views.get
  * logging.views.getIamPolicy
  * logging.views.list
  * logging.views.update
  * observability.scopes.get
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
#### Monitoring NotificationChannel Editor Beta

(`roles/monitoring.notificationChannelEditor`)  
Create an alerting policy that is tied to a notification.  | 

  * monitoring.notificationChannelDescriptors.*
  * monitoring.notificationChannels.create
  * monitoring.notificationChannels.delete
  * monitoring.notificationChannels.get
  * monitoring.notificationChannels.list
  * monitoring.notificationChannels.sendVerificationCode
  * monitoring.notificationChannels.update
  * monitoring.notificationChannels.verify

  
  
#### Monitoring AlertPolicy Viewer

(`roles/monitoring.alertPolicyViewer`)  
View alerting policies.  | 

  * monitoring.alertPolicies.get
  * monitoring.alertPolicies.list
  * monitoring.alertPolicies.listEffectiveTags
  * monitoring.alertPolicies.listTagBindings

  
  
#### Monitoring AlertPolicy Editor

(`roles/monitoring.alertPolicyEditor`)  
Edit alerting policies.  | 

  * monitoring.alertPolicies.*

  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
