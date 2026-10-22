---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/access-control/
title: Roles and permissions \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:52.915048+00:00
---

# Roles and permissions  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Roles and permissions

This page describes the permissions that you need to carry out tasks in Network Topology.

### Required roles and permissions

To get the permissions that you need to carry out tasks in Network Topology, ask your administrator to grant you the following IAM roles on your project: 

  * [Network Management Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to carry out tasks in Network Topology. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to carry out tasks in Network Topology:

  * Open a project: `resourcemanager.projects.get`
  * View the Network Topology graphs for a project and monitored projects: `networkmanagement.topologygraphs.read`
  * View the metrics on the Network Topology graph: `monitoring.timeSeries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view multiple projects, you need to have the `networkmanagement.topologygraphs.read` permission for the [scoping project](https://docs.cloud.google.com/monitoring/settings). For more information, see [View metrics for multiple Cloud projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects). 

For more information about using Network Topology to visualize resources from multiple projects, see [Multiple projects](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#multi-project).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
