---
url: https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud/
title: Application-centric Google Cloud \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:36.508027+00:00
---

# Application-centric Google Cloud  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Application-centric Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Application-centric Google Cloud, a unified way to design, deploy, and manage your applications and resources across multiple Google Cloud projects.

When Google Cloud resources are spread across projects, tracking application health, performance, security, and cost can be complex. Instead of tracking resources individually, group and manage related resources as registered applications. This lets you:

  * **Deploy consistently** : Use templates to design, deploy, and update applications.
  * **Strengthen governance** : Set ownership and policies at the application level.
  * **Monitor health and cost** : View performance, security posture, and cost in one place.
  * **Troubleshoot efficiently** : Use resource dependencies to find issues and assess impact.
  * **Use AI assistance** : Use Gemini Cloud Assist to design, cost optimize, and troubleshoot.



## Application definition

An application is a logical grouping of [components](https://docs.cloud.google.com/app-hub/docs/key-concepts#component), such as services and workloads, that work together to provide business functionality. For example, the following three-tier web application includes a Cloud Run frontend, a Cloud Run backend, and a Cloud SQL database:

![An example three-tier application](https://docs.cloud.google.com/static/application-design-center/images/three-tier-application.png)

## Core features and integrations

The following diagram illustrates key features and products in Application-centric Google Cloud.

[ ![Relationships between application-centric products and features.](https://docs.cloud.google.com/static/app-hub/images/app-management.svg)](https://docs.cloud.google.com/static/app-hub/images/app-management.svg) **Figure 1.** Relationships between application-centric products and features. 

The numbers in the diagram reference the following descriptions:

  1. **Resources** : Register your Google Cloud resources as logical groupings to manage them collectively.

  2. **Application design and deployment** :

     * Use [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) to design [templates](https://docs.cloud.google.com/app-hub/docs/key-concepts#template) and deploy applications.

     * Use [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) to organize existing resources into applications.

  3. **Observability** : Use Google Cloud Observability to optimize and [monitor applications](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring), agents, and MCP servers:

     * Monitor health and performance with metrics, logs, and traces.
     * Set up alerts based on metrics and logs.
  4. **Cost optimization** : Use App Optimize API to understand spending and resource usage.

     * View cost trends and utilization changes in [Cloud Hub](https://docs.cloud.google.com/hub/docs/optimize) and [Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs).
     * Use [App Optimize API](https://docs.cloud.google.com/app-optimize/overview) directly for trend analysis or to join cost data with other business data.
  5. **Security and compliance** : Manage risk by tracking security posture findings in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

  6. **Insights** :

     * Get a centralized view of alerts, incidents, security findings, costs, maintenance activity, and configuration drift in [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview).
     * Correlate observability, security, and deployment data using an interactive [topology graph](https://docs.cloud.google.com/hub/docs/app-topology).
  7. **AI assistance** : Use [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to get context-aware help with the following:

     * [Design applications](https://docs.cloud.google.com/cloud-assist/design-application) on the design canvas, as downloadable Terraform code, or in your own IDE.
     * [Troubleshoot issues](https://docs.cloud.google.com/cloud-assist/investigations) and [optimize cost](https://docs.cloud.google.com/hub/docs/optimize-gemini) with customized recommendations.



## The application-centric management model

To manage resources, you configure a [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) with a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) that centralizes all application management tasks, metadata, and APIs. For example, you can define the boundary at the folder level by configuring an [app-enabled folder](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-enabled-folder).

### Resource organization example

The following example organizes resources into distinct folder-level management boundaries.

[ ![An example resource model for Application-centric Google Cloud, showing how folders and projects
    can be organized within application management boundaries.](https://docs.cloud.google.com/static/app-hub/images/app-enabled-folder.svg)](https://docs.cloud.google.com/static/app-hub/images/app-enabled-folder.svg) **Figure 2.** An example resource organization model in Application-centric Google Cloud. 

Organizing boundaries by business unit provides these benefits:

  * Each folder is an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) with its own [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project). This lets each business unit register applications using relevant resources.

  * Applications in **Business Unit 1** can include resources in projects within the **Business Sub-Unit 1** folder. This lets business units separate their work while sharing access to resources.




For more information about structuring your resources, see [Best practices for application management](https://docs.cloud.google.com/app-hub/docs/best-practices).

### Automatically enabled APIs

When you set up a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project), [required APIs for application management](https://docs.cloud.google.com/app-hub/docs/enabled-apis) are automatically enabled, including APIs for App Hub, Application Design Center, and Google Cloud Observability.

### Application data stored in the management project

The [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) stores the following data for your [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary):

  * **App Hub data** : The logical model of your applications, [services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service), and [workloads](https://docs.cloud.google.com/app-hub/docs/key-concepts#workload), including metadata such as owners, environment, and business criticality.
  * **Application Design Center data** : [Application templates](https://docs.cloud.google.com/app-hub/docs/key-concepts#template), [catalogs](https://docs.cloud.google.com/app-hub/docs/key-concepts#catalog), and [spaces](https://docs.cloud.google.com/app-hub/docs/key-concepts#space) for designing and deploying applications.



To view aggregated telemetry data for application resources in an app-enabled folder, you [configure the observability scope](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring#def_obs_scope) for the management project.

### Impact of management project deletion

If you delete the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) for a folder boundary, all application model data is permanently lost. Underlying Google Cloud resources in other projects are unaffected, but their logical groupings and metadata in App Hub are deleted.

## What's next

  * [Learn more about App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub)
  * [Learn more about Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview)
  * [Learn more about Cloud Hub](https://docs.cloud.google.com/hub/docs/overview)
  * [Prepare for application management](https://docs.cloud.google.com/app-hub/docs/prepare-for-app-lifecycle-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
