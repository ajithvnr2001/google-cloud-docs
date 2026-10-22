---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-monitor/
title: Monitor consumption of reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:29.386493+00:00
---

# Monitor consumption of reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor consumption of reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to monitor the consumption of [reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) by using Cloud Monitoring.

[Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) collects and stores performance information of Google Cloud services such as Compute Engine. The performance information is called [metrics and time series](https://docs.cloud.google.com/monitoring/docs/monitoring-overview#time-series). You can access the metrics and time series of your Compute Engine reservations to do the following:

  * Display how your reservations are being consumed by using [Monitoring dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

  * Receive timely notifications when the consumption of your reservations is in a specific state by using [Monitoring alerting policies](https://docs.cloud.google.com/monitoring/alerts).




These methods can, for example, help you verify that your reservations are being consumed as you planned or timely act to avoid unnecessary costs from wasted resources or unused reservations.

## Before you begin

  * Review the [ requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) and [ restrictions](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions) for reservations.
  * Enable the Monitoring API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create Monitoring dashboards or alerting policies to monitor the consumption of reservations, ask your administrator to grant you the [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create Monitoring dashboards or alerting policies to monitor the consumption of reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create Monitoring dashboards or alerting policies to monitor the consumption of reservations:

  * To create dashboards: `monitoring.dashboards.create` on the project 
  * To create policy alerts: `monitoring.alertPolicies.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Restrictions

When using Monitoring to access and view the [time series](https://docs.cloud.google.com/monitoring/api/v3/metrics) of a reservation, the following restrictions apply:

  * After you create a reservation, its time series becomes available within 30 minutes.

  * After a time series becomes available, Monitoring starts updating it at least once every 30 minutes.

  * If you delete a reservation, its time series is also deleted and can't be recovered.

  * You can only access and view the time series of a reservation that was created in the current project.




For more information about Monitoring restrictions, see [Cloud Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas).

## Reservations metrics

When creating Monitoring dashboards or alerting policies, you must first select the [Google Cloud metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) to measure how the Google Cloud service is performing. For reservations, you can select the following Compute Engine metrics:

  * **Reserved** : The number of reserved virtual machine (VM) instances in each reservation in the current project.

  * **Used** : The number of consumed VMs in each reservation in the current project.




After you select a metric, you can further filter or group the measurements of reservations' metric. For more information about the available filters for reservations, see Reservations filters in this document.

### Reservations filters

You can use [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters) to group or filter the time series data associated with one or more reservations. Specifically, when creating Monitoring dashboards or alerting policies, you can limit the time series data that they use by specifying one or more of the following labels:

Selector | Label name | Description  
---|---|---  
`metadata.system` | `machine_type` | The machine type specified in the reserved VMs for a reservation.  
`metadata.system` | `name` | The name of a reservation.  
`metadata.system` | `state` | The state of a reservation. You can only monitor reservations in the `ACTIVE` state, which is when a reservation exists.  
`metric` | `reserved_resource_type` | The type of reserved zonal resources by a reservation. You can only monitor the `instance` type, which is a VM instance.  
`metric` | `service_name` |  When you select the **Used** metric in the Google Cloud console, you can view which Google Cloud product consumes the reservation. The value can be one of the following:

  * `COMPUTE_ENGINE`: VMs in Compute Engine
  * `VERTEX_ONLINE_PREDICTION`: VMs in Vertex AI prediction jobs
  * `VERTEX_TRAINING`: VMs in Vertex AI custom training jobs

If you consume reservations both in Compute Engine and Vertex AI, then create a filter for each preceding value.   
`resource` | `location` | The zone where a reservation is located.  
`resource` | `reservation_id` | The identifier (ID) of a reservation.  
`resource` | `resource_container` | The project number of the project where a reservation exists. You can only monitor the reservations that were created in your project.  
  
When creating a filter, you must specify the selector and the label name, followed by a [comparison operator](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#filter-option), and then the value to filter. For example, if you want your query to filter your reservations by zone `us-central1-a`, use the following filter:
    
    
    resource.location = "us-central1-a"
    

To ensure that the value you specify in a filter matches the value of a reservation's field, [view the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations).

**Note:** To view a reservation ID, view the details of the reservation using the Google Cloud CLI or REST.

## Monitor consumption of reservations

To monitor the consumption of your reservations, select one of the following methods specified in this document:

  * Create a dashboard—create Monitoring dashboards and add widgets to the graph areas to display the time series data tied to the consumption of your reservations.

This method is useful when, for example, you want to verify that a VM is correctly consuming a reservation or compare the consumption trend of multiple reservations.

  * Create alerting policies—create alerting policies to send alerts when the time series data tied to the consumption of your reservations reaches a defined threshold.

This method is useful when, for example, you want to be notified when the number of VMs used in the current project is below a specific ratio, or when a reservation remains unused for a specific amount time.




### Create a dashboard

You can create [Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) and view the time series tied to the consumption of your reservations by using the Google Cloud console (recommended) and Monitoring API.

When defining how to display the time series data of a Monitoring filter, you must use one of the following methods:

  * **Basic Query** : this method is useful to quickly configure the time series data for a dashboard widget.

For example, you can use Basic Query to quickly display which one of your reservations in a specific zone isn't fully consumed yet.

  * **PromQL** : this method is useful to retrieve, filter, and manipulate time series data to create more complex configurations for a dashboard widget.

For example, you can use [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql) to display the ratio of consumed VMs to reserved VMs in your reservations.




### Basic Query

The following example describes how to create a Monitoring dashboard with a line chart widget to display your consumed reservations in the `us-central1-a` zone.

### Console

To create a Monitoring dashboard using Basic Query, follow these steps:

  1. In the Google Cloud console, go to **Dashboards**.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click add **Create dashboard**.

The **New dashboard** page opens.

  3. Click add_box **Add widget**.

The **Add widget** pane appears.

  4. Click one of the available widgets. For example, click the **Line** widget.

The **Configure widget** pane appears.

  5. Click **Select a metric**.

  6. In the **Select a metric** window, do the following:

     1. Enter `Reservation`, and then select **Reservation**.

**Important:** If you can't see the **Reservation** metric, see [Metric not listed in menu](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#not-listed).
     2. In the **Active metrics categories** list, select **Reservation** again.

     3. In the **Active metrics** list, select one of the available metrics. For example, select **Used**.

     4. Click **Apply**.

  7. To filter your reservations by a specific zone, do the following:

     1. In the **Add filter** list, select one of the available filters for reservations. For this example, select **location**.

     2. In the **Comparator** list, select one of the available operators. For this example, select **= (equals)** (default).

     3. In the **Value** list, select the zone you want to use to filter your reservations. For this example, select **us-central1-a**.

  8. Click **Apply**.




For more options to customize Monitoring dashboards using the Google Cloud console, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

###  REST 

**Note:** After creating a dashboard using the Monitoring API, you can only [manage it using the Google Cloud console](https://docs.cloud.google.com/monitoring/charts/dashboards).

To create a Monitoring dashboard using Basic Query, make a `POST` request to the [`dashboards.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create).
    
    
    POST https://monitoring.googleapis.com/v1/projects/PROJECT_ID/dashboards
    
    {
      "displayName": "Consumed reservations in zone us-central1-a",
      "mosaicLayout": {
        "columns": 12,
        "tiles": [
          {
            "height": 4,
            "widget": {
              "title": "Reservation - Used for us-central1-a [MEAN]",
              "xyChart": {
                "chartOptions": {
                  "mode": "COLOR"
                },
                "dataSets": [
                  {
                    "minAlignmentPeriod": "60s",
                    "plotType": "LINE",
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "timeSeriesFilter": {
                        "aggregation": {
                          "alignmentPeriod": "60s",
                          "perSeriesAligner": "ALIGN_MEAN"
                        },
                        "filter": "FILTER",
                        "secondaryAggregation": {
                          "alignmentPeriod": "60s",
                          "perSeriesAligner": "ALIGN_NONE"
                        }
                      }
                    }
                  }
                ],
                "timeshiftDuration": "0s",
                "yAxis": {
                  "scale": "LINEAR"
                }
              }
            },
            "width": 6
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the current project.

  * `FILTER`: the Monitoring filter to use for your dashboard. For example, to monitor the consumed reservations in zone `us-central1-a`, specify the following:
        
        resource.type = 'compute.googleapis.com/Reservation' AND metric.type = 'compute.googleapis.com/reservation/used' AND resource.location = 'us-central1-a'




For more options to customize Monitoring dashboards using the Monitoring API, see [Create and manage dashboards by using the API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

### PromQL

The following example describes how to create a Monitoring dashboard with a line chart widget to display the ratio of used VMs to reserved VMs in your reservations.

### Console

To create a Monitoring dashboard and add a widget configured with a query using PromQL, follow these steps:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click add **Create dashboard**.

The **New dashboard** page opens.

  3. Click add_box **Add widget**.

The **Add widget** pane appears.

  4. Click one of the available widgets. For example, click the **Line** widget.

The **Configure widget** pane appears.

  5. If you don't see the code editor, then click code **PromQL** or code **MQL**. For **Language** , select **PromQL**.

  6. In the Query editor, enter a PromQL query. For example, to view the ratio of used VMs to reserved VMs in your reservations, specify the following:
         
         (
           max by (metadata_system_name) ({"compute.googleapis.com/reservation/used"})
           /
           max by (metadata_system_name) ({"compute.googleapis.com/reservation/reserved"})
         )
         

  7. Click **Run query**.

  8. Click **Apply**.




For more options to customize Monitoring dashboards using the Google Cloud console, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

###  REST 

**Note:** After creating a dashboard using the Monitoring API, you can only [manage it using the Google Cloud console](https://docs.cloud.google.com/monitoring/charts/dashboards).

To create a Monitoring dashboard and add a widget configured with a query using PromQL, make a `POST` request to the [`dashboards.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create).
    
    
    POST https://monitoring.googleapis.com/v1/projects/PROJECT_ID/dashboards
    
    {
      "displayName": "Consumed reservations in zone us-central1-a",
      "mosaicLayout": {
        "columns": 12,
        "tiles": [
          {
            "height": 4,
            "widget": {
              "title": "Reservation - Used for us-central1-a [MEAN]",
              "xyChart": {
                "chartOptions": {
                  "mode": "COLOR"
                },
                "dataSets": [
                  {
                    "plotType": "LINE",
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "timeSeriesQueryLanguage": "PROMQL_QUERY"
                    }
                  }
                ],
                "timeshiftDuration": "0s",
                "yAxis": {
                  "scale": "LINEAR"
                }
              }
            },
            "width": 6,
            "xPos": 6
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the current project.

  * `PROMQL_QUERY`: the PromQL query to use for the line chart widget. For example, to view the ratio of used VMs to reserved VMs in your reservations, specify the following:
        
        (
        max by (metadata_system_name) ({"compute.googleapis.com/reservation/used"})
        /
        max by (metadata_system_name) ({"compute.googleapis.com/reservation/reserved"})
        )

**Important:** To specify a PromQL query spanning multiple lines in the `timeSeriesQueryLanguage` field, make sure to include the `\n` character at the end of each line.



For more options to customize Monitoring dashboards using the Monitoring API, see [Create and manage dashboards by using the API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

### Create alerting policies

You can create [Monitoring alerting policies](https://docs.cloud.google.com/monitoring/alerts) to receive notifications about the reservations consumption in the current project by using the Google Cloud console and Monitoring API.

When defining an alert condition for an alerting policy, you must use one of the following methods:

  * **Basic Query** : this method is useful to create simple alert conditions.

For example, you can use Basic Query to create an alert condition that gets triggered whenever a reservation is consumed for the first time.

  * **PromQL** : this method is useful to retrieve, filter, and manipulate time series data to create more complex alert conditions.

For example, you can use [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) to create an alert condition that gets triggered when the ratio of reserved VMs to consumed VMs reaches a specific threshold.




### Basic Query

The following example creates an alerting policy that sends an alert notification when a reservation is consumed for the first time. Specifically, the alert triggers whenever the number of consumed VMs in a reservation is greater than `0`.

### Console

To create a Monitoring alerting policy using Basic Query, follow these steps:

  1. In the Google Cloud console, go to **Alerting**.

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

  2. Click add **Create policy**.

The **Create alerting policy** page opens.

  3. Click bar_chart **Select a metric**.

The **Select a metric** window appears.

  4. In the **Select a metric** window, do the following:

     1. In the **Filter by resource or metric name** field, enter `Reservation`.

     2. If the **Reservation** metric appears in the **Active resources** list, select it. Otherwise, do the following:

        1. Clear **Show only active resources & metrics**.

The **Inactive resources** list appears.

        2. In the **Inactive resources** list, select **Reservation**.

**Important:** If you still can't see the **Reservation** metric, see [Metric not listed in menu](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#not-listed).
     3. In the **Active metrics categories** list, select **Reservation** again.

The **Active metrics** list appears.

     4. In the **Active metrics** list, select one of the available metrics.

For example, select **Used**.

     5. Click **Apply**.

  5. Click add_box **Add filter**.

The **Add filter** section appears.

  6. In the **Add filter** section, do the following:

     1. In the **Label** list, select one of the available filters for reservations specified in this document.

For example, to filter your reservations by name, select **name**.

     2. In the **Comparison** list, select one of the available operators.

For example, select **= (equals)** (default).

     3. In the **Value** list, select the name of the reservation that you want to monitor.

     4. Click **Done**.

  7. Click **Next**.

The **Configure alert trigger** pane appears.

  8. In the **Condition types** section, select one of the following options:

     1. To trigger the condition if a time series falls above or below a specific value, select **Threshold**.

     2. To trigger the condition if a time series doesn't have data for a specific time, select **Metric absence**.

     3. To trigger the condition if a time series is projected to cross the threshold in the near future, select **Forecast**.

For example, select **Threshold** (default).

  9. In the **Alert trigger** list, select the condition that triggers the alert.

For example, select **Any time series violation** (default).

  10. In the **Threshold position** list, select when the condition triggers.

For example, select **Above threshold**.

  11. In the **Threshold value** field, enter a value for the condition.

For example, enter `0`.

  12. In the **Condition name** field, enter a name for your condition.

For example, enter `Reservation RESERVATION_NAME consumed.`

Where RESERVATION_NAME is the name of the reservation that you specified in the previous steps.

  13. Click **Next**.

The **Configure notifications and finalize alert** pane appears.

  14. Click **Use notification channels**.

  15. In the **Notification channels** field, select the channels on which you want to be notified about the incident.

If you have no notification channels available, click **Manage notification channels** , and then follow the steps to create notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  16. In the **Incident autoclose duration** field, select a duration after which an incident is automatically closed.

For example, select **3 days**.

  17. In the **Alert policy name** field, enter a name for the alerting policy.

For example, enter `Alert: you started consuming reservation RESERVATION_NAME!`

Where RESERVATION_NAME is the name of the reservation that you specified in the previous steps.

  18. Click **Next**.

The review page of your alerting condition opens.

  19. Click **Create policy**.

Creating the alerting policy might take a few seconds to complete. This action redirects you to the **Create alerting policy** page.




For more information about the options you have when creating alerting policies using the Google Cloud console and Basic Query, see [Create metric-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

###  REST 

To create a Monitoring alerting policy using Basic Query, make a `POST` request to the [`projects.alertPolicies.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create).
    
    
    POST https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alertPolicies
    
    {
      "displayName": "Alert: you started consuming reservation RESERVATION_NAME!",
      "conditions": [
        {
          "displayName": "Reservation RESERVATION_NAME consumed.",
          "conditionThreshold": {
            "filter": "FILTER",
            "aggregations": [
              {
                "alignmentPeriod": "300s",
                "crossSeriesReducer": "REDUCE_NONE",
                "perSeriesAligner": "ALIGN_MEAN"
              }
            ],
            "comparison": "COMPARISON_GT",
            "duration": "0s",
            "trigger": {
              "count": 1
            },
            "thresholdValue": 0
          }
        }
      ],
      "alertStrategy": {
        "autoClose": "AUTO_CLOSE_TIME"
      },
      "combiner": "OR",
      "enabled": true,
      "notificationChannels": [
        "projects/PROJECT_ID/notificationChannels/NOTIFICATION_CHANNEL"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the current project.

  * `RESERVATION_NAME`: the name of an existing reservation which is located in the current project.

  * `FILTER`: the Monitoring filter to use for your alerting policy. For example, to monitor the `used` metric for the RESERVATION_NAME reservation, specify the following:
        
        resource.type = 'compute.googleapis.com/Reservation' AND metric.type = 'compute.googleapis.com/reservation/used' AND metadata.system.name = 'RESERVATION_NAME'

  * `AUTO_CLOSE_TIME`: the time in seconds before an incident is automatically closed. The value must be between `0s` and `604800s` (7 days). For example, enter `259200s` (3 days).

  * `NOTIFICATION_CHANNEL`: the name of an existing notification channel. To set up a notification channel, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




For more information about the options you have when creating alerting policies using the Monitoring API and Basic Query, see [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api).

### PromQL

The following example creates an alerting policy that sends an alert notification whenever the percentage of used VMs to reserved VMs in your reservations is above 90%.

### Console

To create a Monitoring alerting policy using PromQL, follow these steps:

  1. In the Google Cloud console, go to **Alerting**.

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

  2. Click add **Create policy**.

The **Create alerting policy** page opens.

  3. For **Policy configuration mode** , select **Code editor (MQL or PromQL)**.

The **Query editor** pane appears.

  4. Select **PromQL** as the language, and enter a PromQL query.

For example, to create a query that groups your reservations by name and triggers an alert condition when over 90% of your reservations are consumed, enter the following query:
         
         (
           max by (metadata_system_name) ({"compute.googleapis.com/reservation/used"})
           /
           max by (metadata_system_name) ({"compute.googleapis.com/reservation/reserved"})
         ) > 0.9
         

  5. Click **Next**.

The **Configure alert trigger** pane appears.

  6. If the **Condition name** , enter a name for your condition.

For example, enter `Over 90% of your reservations are consumed.`

  7. Click **Next** again.

The **Configure notifications and finalize alert** pane appears.

  8. Click **Use notification channels**.

  9. In the **Notification channels** field, select the channels on which you want to be notified about the incident.

If you have no notification channels available, click **Manage notification channels** , and then follow the steps to create notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  10. In the **Incident autoclose duration** field, select a duration after which an incident is automatically closed.

For example, select **3 days**.

  11. In the **Alert policy name** field, enter a name for the alerting policy.

For example, enter `Alert: over 90% of your reservations are consumed.`

  12. Click **Next**.

The review page of your alerting condition opens.

  13. Click **Create policy**.

Creating the alerting policy might take a few seconds to complete. This action redirects you to the **Create alerting policy** page.




For more information about creating alerting policies using the Google Cloud console and PromQL, see [Create PromQL-based alerting policies (Console)](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts-console).

###  REST 

To create a Monitoring alerting policy using PromQL, make a `POST` request to the [`projects.alertPolicies.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create).
    
    
    POST https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alertPolicies
    
    {
      "displayName": "Alert: over 90% of your reservations are consumed.",
      "conditions": [
        {
          "displayName": "Over 90% of your reservations are consumed.",
          "conditionMonitoringQueryLanguage": {
            "duration": "0s",
            "trigger": {
              "count": 1
            },
            "query": "PROMQL_QUERY"
          }
        }
      ],
      "alertStrategy": {
        "autoClose": "AUTO_CLOSE_TIME"
      },
      "combiner": "OR",
      "enabled": true,
      "notificationChannels": [
        "projects/PROJECT_ID/notificationChannels/NOTIFICATION_CHANNEL"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the current project.

  * `PROMQL_QUERY`: a PromQL query to use for the alerting policy. For example, to create a query that tracks when the percentage of used VMs to reserved VMs is above 90% in the current project's reservations, specify the following:
        
        (
        max by (metadata_system_name) ({"compute.googleapis.com/reservation/used"})
        /
        max by (metadata_system_name) ({"compute.googleapis.com/reservation/reserved"})
        ) > 0.9

**Important:** To specify a PromQL query spanning multiple lines in the `query` field, make sure to include the `\n` character at the end of each line.
  * `AUTO_CLOSE_TIME`: the time in seconds before an incident is automatically closed. The value must be between `0s` and `604800s` (7 days). For example, enter `259200s` (3 days).

  * `NOTIFICATION_CHANNEL`: the name of an existing notification channel. To set up a notification channel, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




For more information about creating alerting policies using the Monitoring API and PromQL, see [Create PromQL-based alerting policies (API)](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts).

## Troubleshoot

Learn how to [troubleshoot issues with reservation monitoring](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-monitoring).

## What's next

  * Learn how to [consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).

  * Learn how to [attach reservations to commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

  * Learn how to [modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).

  * Learn how to [delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
