---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/roles-permissions/
title: Roles and permissions \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:12.918277+00:00
---

# Roles and permissions  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions needed for running Firewall Insights.

You can grant users or service accounts permissions or a predefined role, or you can create a custom role that uses permissions that you specify. The following table describes the IAM predefined roles and their associated permissions.

For more information, see the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

Description | Role | Permissions (methods)  
---|---|---  
View firewalls and their details |  Grant one of the following roles:

  * Firewall Recommender Admin role (`roles/recommender.firewallAdmin`)
  * Firewall Recommender Viewer role (`roles/recommender.firewallViewer`)

| `[compute.firewalls.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/list)`  
Only view insights | Grant one of the following roles:

  * Firewall Recommender Admin role (`roles/recommender.firewallAdmin`)
  * Firewall Recommender Viewer role (`roles/recommender.firewallViewer`)

| [`projects.locations.insightTypes.insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)  
View insights metrics | Grant one of the following roles:

  * Firewall Recommender Admin role (`roles/recommender.firewallAdmin`)
  * Firewall Recommender Viewer role (`roles/recommender.firewallViewer`)

| [`monitoring.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)  
View and modify insights | Grant the Firewall Recommender Admin role (`roles/recommender.firewallAdmin`)  | 

  * [`projects.locations.insightTypes.insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)
  * [`projects.locations.insightTypes.insights.markAccepted`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)

  
  
For more information about project roles and permissions, see the following:

  * [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs)
  * [Compute Engine API documentation](https://docs.cloud.google.com/compute/docs/apis)
  * [Cloud Monitoring API documentation](https://docs.cloud.google.com/monitoring/docs/apis)



## Get required roles and permissions

To get the permissions that you need to enable APIs and features, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Firewall Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallAdmin) (`roles/recommender.firewallAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to enable APIs and features. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable APIs and features:

  * Enable APIs: `serviceusage.services.enable`
  * Enable shadowed rule or overly permissive rule insights: `recommender.computeFirewallInsightTypeConfigs.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Select a project

Before you complete any prerequisites or take any other actions with Firewall Insights, we recommend that you create or select a Google Cloud project. Use the following steps:

  1. In the Google Cloud console, go to the **Project selector** page.

[Go to Project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

  3. Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for your Google Cloud project.




## What's next

  * To complete the setup tasks, see [Enable APIs and features](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
