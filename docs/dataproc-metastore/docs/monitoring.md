---
url: https://docs.cloud.google.com/dataproc-metastore/docs/monitoring/
title: Cloud Monitoring \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:39.760358+00:00
---

# Cloud Monitoring  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) provides visibility into the performance, uptime, and overall health of cloud-powered applications. Google Cloud Observability collects and ingests metrics, events, and metadata from Dataproc Metastore services to generate insights using dashboards and charts.

  * See [Monitoring Pricing](https://cloud.google.com/stackdriver/pricing) to understand your costs.

  * See [Monitoring Quotas and limits](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy) for information on metric data retention.




## Access service metrics in Monitoring

Dataproc Metastore service resource metrics are automatically enabled on Dataproc Metastore services. Use Monitoring to view these metrics.

You can access Monitoring from the [Google Cloud console](https://console.cloud.google.com/monitoring) or by using the [Monitoring API](https://docs.cloud.google.com/monitoring/api/v3).

### Console

  1. In the Google Cloud console, go to the **Cloud Monitoring > Metrics explorer** page:

[Go to the Metrics explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. From the "Find resource type and metric" drop-down list, select the resource `Dataproc Metastore Service`.

  3. Click again in the input box, and then select a metric from the drop-down list. Hovering over the metric name displays information about the metric.




You can select filters, group by metric labels, perform aggregations, and select chart viewing options.

### REST

You can use the Monitoring [timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) API to capture and list metrics defined by a `filter` expression. Use the **Try this API** template on the API page to send an API request and display the response.

## Dataproc Metastore service metrics in Monitoring

Metrics from Dataproc Metastore. Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `metastore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`federation/health` BETA ** _(project)_**   
Federation service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Federation](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Federation)** |  _The health of the Federated Dataproc Metastore Service._   
`version`: The Hive Metastore version of the service.   
`federation/server/request_count` BETA ** _(project)_**   
Federation service request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Federation](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Federation)** |  _The number of requests sent to the Federated Dataproc Metastore Service._   
`method_name`: The request method name.   
`status`: End status of the request, one of [success, client_error, server_error].   
`version`: The Hive Metastore version of the service.   
`service/database_cpu_utilization` BETA ** _(project)_**   
Database CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The database CPU utilization of the Dataproc Metastore Service._   
`database_type`: The type of database, one of [SQL, Spanner].   
`service/grpc/finished_requests_count` BETA ** _(project)_**   
gRPC Requests Finished Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests finished by the GRPC Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service, such as ENTERPRISE.   
`version`: The Hive Metastore version of the service.   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc/received_bytes_count` BETA ** _(project)_**   
gRPC Bytes Received   
`DELTA`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes received by the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`service/grpc/request_latencies` BETA ** _(project)_**   
gRPC Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Distribution of gRPC request latencies for a Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc/sent_bytes_count` BETA ** _(project)_**   
gRPC Bytes Sent   
`DELTA`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes sent by the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`service/grpc/started_requests_count` BETA ** _(project)_**   
gRPC Requests Started Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests received and started by the GRPC Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`method_name`: The request method name.   
`service/grpc_client/finished_requests_count` BETA ** _(project)_**   
gRPC Client Requests Finished Count   
`CUMULATIVE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Total number of RPCs completed on the client, regardless of success or failure._   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc_client/received_bytes_count` BETA ** _(project)_**   
gRPC Client Bytes Received   
`CUMULATIVE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes received by the gRPC client._  
`service/grpc_client/request_latencies` BETA ** _(project)_**   
gRPC Client Request Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Distribution of gRPC request latencies for a Dataproc Metastore Service._   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc_client/sent_bytes_count` BETA ** _(project)_**   
gRPC Client Bytes Sent   
`CUMULATIVE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes sent by the gRPC client._  
`service/grpc_client/started_requests_count` BETA ** _(project)_**   
gRPC Client Requests Started Count   
`CUMULATIVE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests started by the gRPC client._   
`method_name`: The request method name.   
`service/health` GA ** _(project)_**   
Service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The health of the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service, such as ENTERPRISE.   
`version`: The Hive Metastore version of the service.   
`release_tag`: Dataproc Metastore release tag, populated by the service backend and may change over service lifetime.   
`service/metadata/bytes_used` BETA ** _(project)_**   
Size of the metadata stored in the Dataproc Metastore service.   
`GAUGE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The amount of data that is stored in the backend database of the service._   
`version`: The Hive Metastore version of the service.   
`database_type`: The type of database, one of [SQL, Spanner].   
`service/migration/replication_lag` BETA ** _(project)_**   
Replication pipeline processing latency in seconds.   
`GAUGE`, `DOUBLE`, `s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Current maximum duration in seconds taken to replicate data to Dataproc Metastore._   
`migration_id`: The migration ID.   
`service/migration/write_throughput` BETA ** _(project)_**   
Destination database write throughput.   
`GAUGE`, `DOUBLE`, `By/s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Current write throughput at the Dataproc Metastore database where the data is being copied to during the replication phase._   
`migration_id`: The migration ID.   
`service/multi_region/health` GA ** _(project)_**   
Multiregional service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The health of the multiregional Dataproc Metastore Service._   
`version`: The Hive Metastore version of the service.   
`release_tag`: Dataproc Metastore release tag, populated by the service backend and may change over service lifetime.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/multi_region/request_count` GA ** _(project)_**   
Multiregional service request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests sent to the multiregional Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/multi_region/request_latencies` GA ** _(project)_**   
Multiregional service request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The latencies of the requests sent to the multiregional Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/query_metadata/request_count` BETA ** _(project)_**   
Admin Interface request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of Admin Interface requests._   
`database_type`: The type of database, one of [SQL, Spanner].   
`code`: The gRPC status code.   
`service/query_metadata/request_latencies` BETA ** _(project)_**   
Admin Interface request latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The end to end request latency for Admin Interface requests._   
`database_type`: The type of database, one of [SQL, Spanner].   
`code`: The gRPC status code.   
`service/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests sent to the Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service/request_latencies` BETA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The latencies of the requests sent to the Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/backup_count` BETA ** _(project)_**   
Scheduled Backups Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of scheduled backups currently stored for the service._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/last_backup_duration` BETA ** _(project)_**   
Scheduled Backups - Last Backup Duration   
`GAUGE`, `INT64`, `s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The duration of the last successful scheduled backup in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/last_backup_size` BETA ** _(project)_**   
Scheduled Backups Request - Last Backup Size   
`GAUGE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The size of the last successful scheduled backup in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
  
Table generated at 2026-10-14 20:24:33 UTC.

## Build a custom Monitoring dashboard

You can build a custom Monitoring dashboard that displays charts of selected Dataproc Metastore service metrics.

  1. Select **\+ CREATE DASHBOARD** from the Monitoring [Dashboards Overview](https://console.cloud.google.com/monitoring/dashboards) page.

  2. Provide a name for the dashboard.

  3. In the upper-right menu, click **Add Chart** to open the Add Chart window.

  4. For the resource type, select `Dataproc Metastore Service`.

  5. Select one or more metrics and chart properties, and then click **Save** to save the chart.

  6. Add additional charts to your dashboard if you'd like.

  7. To save the dashboard, click **Save**. Its title appears in the Monitoring **Dashboards Overview** page.




You can view, update, and delete dashboard charts from the dashboard display page.

## Use Monitoring alerts

You can create a Monitoring alert that notifies you when a Dataproc Metastore service or job metric crosses a specified threshold.

### Create an alert

  1. In the Google Cloud console, open [Monitoring Alerting](https://console.cloud.google.com/monitoring/alerting).

  2. To open the **Create new alerting policy** form, click **\+ CREATE POLICY**

  3. Define an alert by adding alert conditions, policy triggers, notification channels, and documentation.

  4. Select **ADD CONDITION** to open the alert condition form with the Metric tab selected.

  5. Fill in the fields to define an alert condition, and then click **ADD**.

  6. After adding the alert condition, complete the alert policy by setting notification channels, policy triggers, documentation, and the alert policy name.




### View alerts

When an alert is triggered by a metric threshold condition, Monitoring creates an incident and a corresponding event. You can view incidents from the [Monitoring Alerting](https://console.cloud.google.com/monitoring/alerting) page in the Google Cloud console. If you defined a notification mechanism in the alert policy, such as an email or SMS notification, Monitoring also sends a notification of the incident.

## What's next

  * [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
