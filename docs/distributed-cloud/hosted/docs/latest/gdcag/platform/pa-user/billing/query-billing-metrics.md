---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/query-billing-metrics/
title: Query billing metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:48.944728+00:00
---

# Query billing metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/query-billing-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Query billing metrics Stay organized with collections  Save and categorize content based on your preferences. 

To query and visualize billing metrics, use the [Billing Usage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/track-resource-consumption) and [Projected Cost](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/estimate-projected-costs) dashboards.

These dashboards provide visualizations on the following billing related metrics:

  * `server_org_count`
  * `kube_namespace_resource_usage`
  * `pod:kube_pod_container_resource_requests:sum`
  * `metering_storage_organization_allocated_capacity_bytes`
  * `metering_storage_allocated_capacity_bytes`
  * `metering_gdcbackup_protected_pods_count`
  * `metering_gdcbackup_protected_vms_count`
  * `ai_vision_usage`
  * `ai_speech_audio_length_sum`
  * `ai_translation_usage_codepoints`



Through these dashboards, you can filter the metric values by namespace, Task Order (TO), or Contract Line Item Number (CLIN).

**Note:** Contact your Infrastructure Operator to request the TO or CLIN necessary to filter metric values.

## Before you begin

**Note:** Before accessing the **Billing reports** page you must ask your Organization IAM Admin to:  


  * In case of Organization, grant you the Organization Grafana Viewer (`organization-grafana-viewer`) role.
  * In case of Project, grant you Project Grafana Viewer (`project-grafana-viewer`) role for your project.



## Filter namespace metric values

  * To filter metric values by labels on namespaces, perform the following query in the **Explore** page of the monitoring instance:

`none sum by (label_CONVERTED_LABEL_NAME) (METRIC_NAME{} * on (cluster, namespace) \ group_left(label_CONVERTED_LABEL_NAME) \ kube_namespace_labels{label_CONVERTED_LABEL_NAME=LABEL_VALUE})`

Replace the following variables:

  * CONVERTED_LABEL_NAME: the label key to filter metric values. Replace all non-alphabetic characters in this label with the underscore `_`. For example: `app.kubernetes.io/component` becomes `app_kubernetes_io_component`.
  * METRIC_NAME: the name of the billing-related metrics.
  * LABEL_VALUE: the label value to filter metrics.



## Filter pod metric values

  * To filter metric values by labels on pods, perform the following query in the **Explore** page of the monitoring instance:

`none sum by (label_CONVERTED_LABEL_NAME) (METRIC_NAME{} * on (cluster, namespace, pod) \ group_left(label_CONVERTED_LABEL_NAME) \ kube_pod_labels{label_CONVERTED_LABEL_NAME=LABEL_VALUE})`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
