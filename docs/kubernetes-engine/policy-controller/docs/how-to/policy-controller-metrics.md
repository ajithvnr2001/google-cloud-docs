---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics/
title: Use Policy Controller metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:55.246166+00:00
---

# Use Policy Controller metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Policy Controller metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use metrics to monitor Policy Controller.

Policy Controller includes multiple metrics related to policy usage. For example, there are metrics recording the number of constraints and constraint templates, and the number of audit violations detected. To create and record these metrics, Policy Controller uses [OpenTelemetry](https://opentelemetry.io/). You can configure Policy Controller to export these metrics to [Prometheus](https://prometheus.io/) or [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). The default setting for exporting metrics exports the metrics to both Prometheus and Cloud Monitoring.

## Pricing

Policy Controller metrics use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to load metrics into Cloud Monitoring. Cloud Monitoring charges for the ingestion of these metrics are based on the number of samples ingested.

For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## Configure metrics export

You can configure how Policy Controller exports its metrics. You can choose Prometheus, Cloud Monitoring, both, or neither when [installing Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#installing). By default, Policy Controller attempts to export metrics to both Prometheus and Cloud Monitoring.

### Export metrics to Cloud Monitoring

To allow Policy Controller to export metrics to Cloud Monitoring, the service account that Policy Controller uses must have the `roles/monitoring.metricsWriter` IAM role on the project. To grant this role, do one of the following:

  * If Policy Controller is running inside a Google Cloud environment that has a [default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default), grant the `roles/monitoring.metricsWriter` role on the project to that service account:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
            --role=roles/monitoring.metricsWriter
        

Replace the following:

    * `PROJECT_ID`: your Google Cloud project ID.
    * `PROJECT_NUMBER`: your numerical Google Cloud project number.
  * If [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) are enabled, grant the `roles/monitoring.metricsWriter` role on the project to the Kubernetes ServiceAccount that Policy Controller uses:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:PROJECT_ID.svc.id.goog[gatekeeper-system/gatekeeper-admin]" \
            --role=roles/monitoring.metricWriter
        

Replace `PROJECT_ID` with the cluster's Google Cloud project ID.

**Note:** GKE clusters [on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem), [on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal), and [GKE Multi-Cloud clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud) (both on AWS and Azure) are automatically registered to your project fleet with fleet Workload Identity Federation enabled.



You can view these metrics with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) or by [using the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### Export metrics to Prometheus

Policy Controller exports metrics for Prometheus on port 8888 of the `gatekeeper-controller-manager-*` Pod under the `gatekeeper-system` namespace.

If Policy Controller is running on a cluster with [Google Cloud Managed Service for Prometheus](https://cloud.google.com/managed-prometheus) configured, these metrics will automatically be collected and stored in [Cloud Monitoring](https://docs.cloud.google.com/monitoring). This also works for clusters that enable Google Cloud Managed Service for Prometheus after Policy Controller is installed. You might also need to grant additional permissions to the default Compute Engine service account that Google Cloud Managed Service for Prometheus uses, depending on your policies. For details on granting permissions to Google Cloud Managed Service for Prometheus, see [Enable Managed Collection: GKE](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke). For more information on configuring Google Cloud Managed Service for Prometheus, see [Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

For more information on Cloud Monitoring pricing, see [Pricing for Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/managed-prometheus#pricing).

For examples on how to view metrics with the Google Cloud Managed Service for Prometheus solution, see [Query using Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm#gmp-in-monitoring).

## View metrics

Policy Controller metrics are exported to your Cloud Monitoring project in Prometheus format. As a result, you can query metrics by using the Cloud Monitoring API and a dashboard in the Google Cloud console. You can edit this dashboard to meet your business and operational needs.

To query the Cloud Monitoring API, use either [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql) (the de-facto query language for Kubernetes metrics) or [Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql/examples) (Google's proprietary metrics query language).

You can use a template to set up a dashboard by searching for "Policy Controller" in the Cloud Monitoring Dashboards page. For more information about creating and editing dashboard templates, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

## Create alerts

To receive notifications when your metrics meet certain thresholds, [create alerting policies in Cloud Monitoring](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

## Third party integration

By using the Cloud Monitoring API, any third party observability tool can ingest Policy Controller metrics.

For example, if you're using Grafana dashboards, add the Cloud Monitoring API as the data source in Grafana. To learn more, see [Google Cloud Monitoring](https://grafana.com/docs/grafana/latest/datasources/google-cloud-monitoring/) in the Grafana documentation.

## Available metrics

If Policy Controller is enabled on your cluster and is configured to export to Cloud Monitoring, you can query the following metrics (all prefixed with `OpenCensus/`):

Name | Type | Labels | Description  
---|---|---|---  
`OpenCensus/audit_duration_seconds` | Cumulative |  | Audit cycle duration distribution  
`OpenCensus/audit_last_run_time` | Gauge |  | The epoch timestamp since the last audit runtime, given as seconds in floating-point  
`OpenCensus/constraint_template_ingestion_count` | Cumulative | status | Total number of constraint template ingestion actions  
`OpenCensus/constraint_template_ingestion_duration_seconds` | Cumulative | status | Constraint Template ingestion duration distribution  
`OpenCensus/constraint_templates` | Gauge | status | Current number of constraint templates  
`OpenCensus/validation_request_count` | Counter | admission_status | Count of admission requests from the API server  
`OpenCensus/validation_request_duration_seconds` | Cumulative | admission_status | Admission request duration distribution  
`OpenCensus/violations` | Gauge | enforcement_action | Number of audit violations detected in the last audit cycle  
`OpenCensus/watch_manager_intended_watch_gvk` | Gauge |  | How many unique GroupVersionKinds Policy Controller is meant to be watching. This metric is a combination of synced resources and constraints.  
`OpenCensus/watch_manager_watched_gvk` | Gauge |  | How many unique GroupVersionKinds Policy Controller is actually watching. This metric is meant to converge on being equal to `OpenCensus/watch_manager_intended_watch_gvk`.  
  
If Policy Controller is configured to export to Prometheus, you can query the following metrics (all prefixed with `Prometheus/`):

Name | Type | Labels | Description  
---|---|---|---  
`Prometheus/gatekeeper_audit_duration_seconds/histogram` | Cumulative |  | Audit cycle duration distribution  
`Prometheus/gatekeeper_audit_last_run_end_time/gauge` | Gauge |  | The epoch timestamp of the end of the last audit run, given as seconds in floating-point  
`Prometheus/gatekeeper_audit_last_run_time/gauge` | Gauge |  | The epoch timestamp of the start of the last audit run, given as seconds in floating-point  
`Prometheus/gatekeeper_constraint_template_ingestion_count/counter` | Cumulative | status | Total number of constraint template ingestion actions  
`Prometheus/gatekeeper_constraint_template_ingestion_duration_seconds/histogram` | Cumulative | status | Constraint Template ingestion duration distribution  
`Prometheus/gatekeeper_constraint_templates/gauge` | Gauge | status | Current number of constraint templates  
`Prometheus/gatekeeper_validation_request_count/counter` | Cumulative | admission_status, admission_dryrun | Count of admission requests from the API server  
`Prometheus/gatekeeper_validation_request_duration_seconds/histogram` | Cumulative | admission_status | Admission request duration distribution  
`Prometheus/gatekeeper_violations/gauge` | Gauge | enforcement_action | Number of audit violations detected in the last audit cycle  
`Prometheus/gatekeeper_watch_manager_intended_watch_gvk/gauge` | Gauge |  | How many unique GroupVersionKinds Policy Controller is meant to be watching. This metric is a combination of synced resources and constraints.  
`Prometheus/gatekeeper_watch_manager_watched_gvk/gauge` | Gauge |  | How many unique GroupVersionKinds Policy Controller is actually watching. This metric is meant to converge on being equal to `Prometheus/gatekeeper_watch_manager_intended_watch_gvk/gauge`.  
  
## What's next

  * [View Policy Controller status in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
