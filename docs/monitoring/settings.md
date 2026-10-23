---
url: https://docs.cloud.google.com/monitoring/settings/
title: Metrics scopes overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:36.922418+00:00
---

# Metrics scopes overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Metrics scopes overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) determines what time-series data your Google Cloud project can chart and monitor. If you only want to chart and monitor the time-series data collected by your Google Cloud project, then you don't need to perform any configuration. We recommend completing the [Compute Engine quickstart](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine). However, if you want to chart and monitor the time-series data collected by multiple Google Cloud projects, then some configuration is required. This document introduces the data model and best practices. For configuration information, see the documents listed in the What's next section.

## Data model

This section introduces the concepts of a resource container, a metrics scope, and a scoping project.

Resource container
    A _resource container_ is a Google Cloud project. Resource containers store time-series data for the services and quota used by that container. The time-series data stored by a resource container includes a label that identifies the resource container. When viewing data stored in multiple resource containers, you can filter and group by that label.
Metrics scope
    The _metrics scope_ of a Google Cloud project defines the set resource containers whose time-series data the project can chart and monitor. The monitored data includes the [services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc) that you construct and associate with SLOs and alerting policies. By default, the metrics scope of a Google Cloud project only includes that project. Therefore, unless you configure the metrics scope, a Google Cloud project can only chart and monitor the time-series data it stores. You can use the Google Cloud console, the Google Cloud CLI, and the Cloud Monitoring API to modify the list of resource containers that are included in a metrics scope.
Scoping project
    A _scoping project_ hosts a metrics scope. The scoping project stores the alerting policies, uptime checks, dashboards, synthetic monitors, [services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc), and monitoring groups that you configure. Because every Google Cloud project hosts a metrics scope, every project is also a scoping project. When you use the Google Cloud console, the scoping project is the project selected by the Google Cloud console project picker.

## App Hub applications and metrics scopes

You manage the metrics scope for [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host projects and management projects for single-project boundaries. You can manage the metrics scope either by using the [Google Cloud console](https://docs.cloud.google.com/monitoring/settings/multiple-projects) or the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/settings/manage-api).

Google Cloud manages the metrics scope for app-enabled folders, unless adding a project to the metrics scope fails due to exhaustion of the metrics scope quota. In that case, you can request a quota increase and then manually add projects to the metrics scope of the management project for your app-enabled folder. To learn more, see [Metrics scopes for app-enabled folders](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders).

## Example metrics scope configuration

Assume that you have two projects, named `Staging` and `Production`, that contain Compute Engine virtual machine (VM) instances. To view the metrics for all of your VMs in a single view, you create another project, `AllEnvironments`, and then add the `Staging` and `Production` projects to the metrics scope of the project named `AllEnvironments`.

With this configuration, to create a chart that displays time-series data stored in the `Staging` project, your first step is to open the Google Cloud console and select a project with the Google Cloud console project picker:

  * If you select `AllEnvironments`, then your chart can display time-series data stored by the `Staging` project along with time-series data stored by the `Production` and `AllEnvironments` projects. To view time-series data that is stored by the `Staging` project, you can add a filter.

The dashed line in the following diagram shows the projects whose time-series data can be charted and monitored by the `AllEnvironments` project:

![Multi-view metrics scope includes all three projects selected.](https://docs.cloud.google.com/static/monitoring/images/settings-metrics-scope-new-project-figure.png)

  * If you select `Staging`, then your chart displays time-series data stored by the `Staging` project.

![The metrics scope of `Staging` only includes the `Staging` project.](https://docs.cloud.google.com/static/monitoring/images/settings-metrics-scope-single-project-figure.png)




## Best practices

  * When you want to chart or monitor time-series data stored in multiple resource containers, we recommend that you use a new Google Cloud project or one without resources as the scoping project, because these projects don't store any time-series data.

Consider a scenario where your scoping project contains resources such as VMs. To chart or monitor only the time-series data for the VMs in the scoping project, you must specify [filters](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics#filter-option) to exclude the time series from VMs stored in monitored resource containers. The requirement to use filters increases the complexity of configuring a chart and an alerting policy, and it increases the possibility of a configuration error.

  * Consider using multiple scoping projects to control which teams have access to the time-series data stored in your projects. The following table illustrates a possible configuration:

| Scope A | Scope B | Scope C  
---|---|---|---  
**Scoping project** | scoping-project-A | scoping-project-B | scoping-project-C  
**Monitored projects** | Project 1  
Project 2 | Project 3  
Project 4 | Project 1  
Project 2  
Project 3  
Project 4  
Project 5  
**IAM-permissioned group**  
(example) | Dev team A | Dev team B | SRE team  



## Grant access to Cloud Monitoring

To view the time-series data that can be charted or monitored by a project, your Identity and Access Management (IAM) role on the project must include all the permissions in the Monitoring Viewer (`roles/monitoring.viewer`) role. _You don't need any other permissions._ For example, suppose the metrics scope of a scoping project monitors three Google Cloud projects and that you have a role of Monitoring Viewer on the scoping project. When you access the scoping project by using the Google Cloud console, you can view the time-series data stored in that project and the time-series data stored in the other three Google Cloud projects.

To modify a metrics scope, your IAM roles on the scoping project and on each resource container that you want to add must include all permissions in the Monitoring Admin (`roles/monitoring.admin`) role.

For more information, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## What's next

  * [Metrics scopes for app-enabled folders](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders).
  * [Configure a metrics scope for projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).
  * [Configure a metrics scope by using the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/settings/manage-api).
  * [Quotas and limits](https://docs.cloud.google.com/monitoring/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
