---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview/
title: Viewing your microservices \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:40.546831+00:00
---

# Viewing your microservices  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Viewing your microservices Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring provides a dashboard that summarizes all your services, the **Services Overview** dashboard. The **Services Overview** dashboard is also the entry point for other service-monitoring tasks.

This page describes the summary information on the **Services Overview** dashboard of the Google Cloud console. From this dashboard, you can do the following:

  * See the status of your services, and drill down into any one for additional details.

  * Modify the configuration of services:

    * For services on Cloud Service Mesh, Istio on Google Kubernetes Engine, and App Engine, you can define service-level objectives (SLOs) using standard availability and latency metrics.
    * For custom services, you can do the following: 
      * Create new custom services.
      * Identify metrics to act as service-level indicators (SLIs).
      * Define SLOs based on those SLIs.
    * Set up alerting policies to notify you when performance does not meet the SLOs.

For information on configuration tasks, see the following:

    * [Defining a custom service](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).
    * [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo).
    * [Creating an SLO-based alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert).



You can also use the Monitoring API to manage services programmatically. For more information, see [Using the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures).

## Before you begin

To understand service monitoring, you need to be familiar with concepts like service-level indicators (SLIs), SLOs, error budgets, and SLO-based alerting policies. These concepts are described on other pages, for example:

  * For an introduction to SLIs, SLOs and error budgets, see [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

  * For an introduction to SLO-based alerting policies, see [Alerting on your burn rate](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate).




## Services Overview dashboard

The **Services Overview** dashboard provides a summary view of all the services in your project, including basic information about the health of those services.

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/services-icon.png) **SLOs** page: 

[Go to **SLOs**](https://console.cloud.google.com/monitoring/services)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

If you have not yet created any services, then the **Services Overview** provides a welcome message and an empty list of services:

![The **Services Overview** page provides a welcome message for new
users.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-svc-summary-new.png)

After you have created services, the **Services Overview** page includes the following information:

  * A **Current status** summary that displays an overview of the status of of your services. This region is described in [Summary of services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-summary).

  * An inventory table, **Services** , that displays information about each service. By default, the table shows all services, but you can filter the table so that it shows particular groups of services. The information in this table is described in [Inventory table](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-inventory).

  * A **Supported Services** list that classifies your defined services into categories. You can use this list to limit what is displayed in the the **Services** table. When you select a service type in the list, the table shows only the services of that type.




### Summary of services

The summary card displays the number of services and provides information about their health and configuration:

![The **Services Overview** summary card provides basic health information.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-summary-card.png)

The information displayed on the summary card includes the following:

  * The number of services found.
  * A timestamp indicating when the summary information was collected.
  * The number of services with SLO alerts firing.
  * The number of services out of SLO budget.
  * Services with additional configuration options available.



If there are services with firing SLO alerts or exhausted error budgets, the summary card displays a count and provides a **Show services** option for those services. Clicking **Show services** filters the inventory table so that it shows only the affected services.

If there are services without defined SLOs or alerting policies, the summary card describes them and provides a **Show Services** option. Clicking **Show Services** filters the inventory table so that it shows only those services. The summary card then provides a **Learn more** option that describes SLOs or alerting policies.

If you have GKE entities with no associated custom services, the summary card provides a **Define Service** option. For more information, see [Defining a microservice](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).

### Inventory table

The **Services Overview** inventory table includes a row for each service, as shown in the following screenshot:

![The **Services Overview** inventory table describes each service.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-inventory-table.png)

The inventory table provides the following information for each service listed in the table:

  * **Name** : The display name of the service.

Clicking on the name of a service brings up a dashboard for that service. For more information, see [Using microservice dashboards](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-dashboard).

  * **Type** : One of the following values:

    * `Istio`: an automatically detected Istio on Google Kubernetes Engine or Cloud Service Mesh service.
    * `App Engine`: an automatically detected App Engine service.
    * `Custom`: a GKE service.
  * **SLOs out of error budget** : The ratio of out-of-budget SLOs to the total SLO count. Services with out-of-budget SLOs are also badged to make them stand out in the table.

  * **SLOs with firing alert** : The ratio of alerting policies that are firing to the total count of alerting policies. Services with firing policies are also badged to make them stand out in the table.

  * **Labels** : Information about the service. The types of information displayed varies with the type of service.

  * _more_vert_ **More options** : Lists changes you can make to the service. The choices depend on the service type:

    * **Edit display name** : available for all service types.
    * **Delete service** : available only for custom services.



By default, the inventory table includes all the services in your project, but you can filter the table to reduce the number of entries. You can filter the table from options on the summary card as described in [Summary of services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-summary), or you can filter the table directly.

### Filtering the inventory table

You can filter the inventory table in the following ways:

  * By clicking one of the service-type entries in the **Supported Services** list.

  * By clicking one of the **Show services** options in the summary card, as described in [Summary of services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-summary).

  * By manually adding filters to the inventory table.




To manually add a filter to the inventory table, do the following:

  1. Click _filter_list_ **Filter**. A list of filter options is displayed:

     * **Name** : filter by SLO name.
     * **Type** : filter by SLO type.
     * **Labels** : filter by value of service labels.
     * **SLO count** : filter by number of SLOs configured.
     * **SLO alerts policies count** : filter by number of SLO-based alerting policies configured.
  2. Choose one of the options off the filter list. The chosen option appears in the filter bar.

How you complete the filter varies with the option you select:

     1. If you select **Type** , you then get a list of the available service types. Select a type from the list.

     2. If you select **Name** or **Labels** , then click next to the text in the filter bar and start typing. Values that match are provided on a list. Select a value from the list.

     3. If you select **SLO count** or **SLO alert policies count** , you then get a list of comparison operators to choose from.

        1. Select an operator.
        2. Click next to the operator and enter a comparison value.

The completed filter is replaced by a filter chip. For example, the following chip filters for services that have 2 or fewer SLO-based alerting policies configured:

![A completed filter becomes a chip.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-filterchip.png)




You can add multiple filters by repeating this process. After you add one filter, the filter-options menu also includes an `OR` option for evaluating the filters. By default, services must meet a logical `AND` of all the filters to appear on the table.

To remove a filter, click the _close_ on the filter chip.

## What's next?

For information on service-configuration tasks, see the following:

  * [Defining a custom service](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).
  * [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo).
  * [Creating an SLO-based alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert).



For information on per-service dashboards, see [Using microservice dashboards](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-dashboard).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
