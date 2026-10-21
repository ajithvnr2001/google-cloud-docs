---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview/
title: Network Analyzer overview \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:32:37.517611+00:00
---

# Network Analyzer overview  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Network Analyzer overview Stay organized with collections  Save and categorize content based on your preferences. 

Network Analyzer automatically monitors your Virtual Private Cloud (VPC) network configurations and detects misconfigurations and suboptimal configurations. It provides insights about network topology, firewall rules, routes, configuration dependencies, and connectivity to services and applications. It identifies network failures, provides root cause information, and suggests possible resolutions.

Network Analyzer runs continuously and triggers relevant analyses based on near real-time configuration updates in your network. If a network failure is detected, it tries to correlate the failure with recent configuration changes to identify root causes. Wherever possible, it provides recommendations to suggest details about how to fix the issues.

## Network insight groups and types

The results from Network Analyzer analyses are known as _insights_. Insights are grouped into the following categories:

  * VPC network
  * Network services
  * Kubernetes engine
  * Hybrid connectivity
  * Managed services



For more information about these groups and their related insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## Analysis schedule

Network Analyzer generates insights whenever relevant configuration changes are made, as well as periodically. Analyses are triggered approximately ten minutes after a related configuration change is made. Periodic analyses are performed at least once daily.

Analyses are batched to handle frequent configuration updates.

## Insight attributes

Each insight has key attributes that help you to understand and take corrective actions.

### Priority

Specifies the criticality of the insight depending on the severity of the issue.

  * **Critical:** Include service-impacting issues with large scope impact (such as all the VMs, global, or multi-regions).
  * **High:** Include service impacting issues, but may not be of a large scope.
  * **Medium:** Include issues that have service impact or prevent proper service usage.
  * **Low:** Include warnings of predictive failure in the future (such as utilization) or for optimization (such as recommendations to reduce cost and improve redundancy).



### Resource name

Provides information about the resource where the issue is found.

### Resource type

The type of the resource according to Google Cloud API [resource definitions](https://docs.cloud.google.com/resource-manager/reference/rest).

### Project

The ID of the project to which the resource belongs.

### Insight type

  * **Info:** Provides information about the resources.
  * **Warning:** Indicates a warning condition, which could be service degradation or lack of redundancy.
  * **Error:** Indicates an error condition where service usability or performance is already impacted.



### Network insight

Provides a single-line description of the issue type being reported.

### First report time

Specifies the time when an issue is detected for the first time. If the issue persists, any later analysis (triggered by the system automatically) reports the same issue again with this latest analysis time as the last run time.

### Status

Indicates whether the insight is active, fixed (no longer being reported), or a user has dismissed the insight.

  * **Active:** The insight exists at the time of the query.
  * **Fixed:** The insight was reported before but was resolved at the time of the query.
  * **Dismissed:** The insight has been dismissed by a user.



### Insight details

Provides more detailed information of the finding, and includes related configuration changes where applicable.

## Shared VPC insights

For Shared VPC cases, there are two scenarios:

  * **Host project:** Network Analyzer provides relevant information for VPC networks in the host project, such as IP address utilization insights that display the IP address allocation percentage of subnets. For such insights, the information from service projects is automatically aggregated to derive the insight information. In the IP address utilization insights, the VMs and load balancers in the service projects are included in the calculation of IP address allocation.
  * **Service project:** Services and applications running in service projects have their analyses done in service projects. Example insights include: load balancer insights, GKE insights, and Cloud SQL insights. If these services use the host project VPC network, the analysis automatically includes the host VPC network information such as firewall rules and routes.



## Multiple projects

To view multiple projects in Network Analyzer, configure a metrics scope and add monitored projects to it.

When you add projects to a metrics scope, then this metrics scope lets you monitor the data for the scoping project and the monitored projects. From this metrics scope, you can access the combined metrics of the scoping project and the monitored projects. For more information, see [Viewing metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

To make use of an existing metrics scope and monitor multiple Google Cloud projects in a single view, select the scoping project using the Google Cloud console project picker or the **Change Scope** button. You can also select a single monitoring project using these options.

## Opt out

If you do not want to have projects in your organization analyzed by Network Analyzer, you can go to the Transparency and Control Center to opt out of the Network Analyzer data processing group. To change opt-out settings, you must have the Data Processing Controls Resource Admin role (`roles/dataprocessing.admin`). For more information about opting out, see [Opting out of data processing](https://docs.cloud.google.com/recommender/docs/opting-out).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
