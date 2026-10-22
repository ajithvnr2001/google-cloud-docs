---
url: https://docs.cloud.google.com/application-design-center/docs/monitor-applications/
title: Monitor application health and performance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:54.854403+00:00
---

# Monitor application health and performance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/monitor-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Monitor application health and performance Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you monitor application health and performance using Application Monitoring telemetry dashboards. 

## Application Monitoring overview

[Application Monitoring in Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring) gives you visibility into the health and performance of your applications. When you register infrastructure resources as services or workloads in an application, using either App Hub or Application Design Center, Application Monitoring automatically provides predefined dashboards that display key log, metric, and trace data in an application-centric context. You can also set up alert policies for your applications.

For more information about the application-centric model and other integrated features, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

### How Application Monitoring works

When you define an application and register its underlying resources, Application Monitoring discovers the application deployment. The application definition acts as a single source of truth that clarifies ownership and dependencies. For [infrastructure supported by Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-services), the registered services and workloads provide the telemetry needed for the predefined dashboards.

These dashboards help you diagnose issues and monitor performance for the application as a whole, rather than as a collection of independent resources.

Telemetry data includes log, metric, and trace data. Because Application Monitoring understands the logical grouping of your application's services and workloads, it automatically enriches all telemetry with [application-specific labels](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-labels). You can then use these labels to filter and query your application's data within the predefined dashboards.

### What you can do with Application Monitoring

The integration with Application Monitoring lets you do the following:

  * **View consolidated dashboards:** Get an immediate overview of your application's health, including golden signals like traffic, error rate, latency, and saturation.
  * **View details for services and workloads:** View dashboards for individual services and workloads to isolate issues.
  * **Correlate telemetry:** Explore log, metric, and trace data in a unified view to understand the full context of an issue.
  * **Create alerts:** Set up alerting policies based on application-specific metrics to be notified of potential problems.



To learn more about Application Monitoring, see the [Application Monitoring overview](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring).

## Get started with Application Monitoring

To view telemetry data for your applications with Application Monitoring, do the following:

  1. Set up an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary). For more information, see the following documentation for Application-centric Google Cloud products:

     * [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).
     * [Set up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup).
  2. Define your application and its components. You can define applications in one of the following ways:

     * [Register resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources).
     * [Design and publish application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  3. [Set up Google Cloud Observability for Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/setup-application-monitoring).

  4. In the Google Cloud console, go to the **Application monitoring** page: 

[Go to **Application monitoring**](https://console.cloud.google.com/monitoring/applications)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  5. In the Google Cloud console, use the project picker to select your [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) or [host project](https://docs.cloud.google.com/app-hub/docs/key-concepts#host-project).

For detailed instructions on how to use the predefined dashboards and explore your telemetry data, see [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).




## Monitor security compliance

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can [validate application designs](https://docs.cloud.google.com/application-design-center/docs/overview#validate-designs) to make sure your infrastructure adheres to organizational policies. This approach simplifies application management by tracing security findings back to their source for efficient root-cause resolution.

To view the runtime security posture of your deployed application components, threats, and compliance status of your applications, do the following:

  * [View application security findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * [Monitor security compliance in Cloud Hub](https://docs.cloud.google.com/hub/docs/security).



## What's next

  * Get started with preconfigured architectures by [building on Google templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Explore how monitoring works in Google Cloud with [application-centric monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
