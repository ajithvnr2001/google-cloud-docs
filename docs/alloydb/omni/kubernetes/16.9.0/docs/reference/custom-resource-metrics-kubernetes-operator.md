---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/custom-resource-metrics-kubernetes-operator/
title: Custom resource metrics for the AlloyDB Omni Kubernetes operator \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:32.762539+00:00
---

# Custom resource metrics for the AlloyDB Omni Kubernetes operator  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/custom-resource-metrics-kubernetes-operator/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Custom resource metrics for the AlloyDB Omni Kubernetes operator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/custom-resource-metrics-kubernetes-operator)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/custom-resource-metrics-kubernetes-operator)

This page describes the custom resource (CR) metrics for the AlloyDB Omni Kubernetes operator. The AlloyDB Omni Kubernetes operator exposes metrics constructed from custom resource manifests in a [Prometheus](https://prometheus.io/) format using [kube-state-metrics](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/). **Note:** These metrics are only available on AlloyDB Omni Kubernetes operator version 1.3.0 and later.

Metric types follow the definition of Prometheus metrics types. A Prometheus Info metric is a special kind of Prometheus Gauge metric, which always has a value of 1 and has multiple labels carrying important information about the corresponding AlloyDB Omni Kubernetes operator Custom Resource.

To learn how to enable custom resource metrics, see [Monitor AlloyDB Omni Kubernetes operator custom resources](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/monitor-kubernetes-operator-custom-resources).

## Custom Resource Definition (CRD) metadata labels

All custom resource metrics have the following labels that mark the group, version, and kind of the CRD. For more information, see [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/). Label definitions and naming are listed in the following table:

**Key** | **Description** | **Example Value**  
---|---|---  
` customresource_group ` | The group of the CRD. | ` alloydbomni.dbadmin.goog `  
` customresource_version ` | The version of the CRD. | ` v1 `  
` customresource_kind ` | The kind of the CRD. | ` DBCluster `  
  
## DBCluster metrics

DBCluster metrics are exposed from `DBCluster` resource manifests. All DBCluster metric names start with `alloydb_omni_dbcluster_`. All DBCluster metrics have the following labels:

**Key** | **Value**  
---|---  
` namespace ` | The namespace that the DBCluster belongs to.  
` dbcluster ` | The name of the DBCluster custom resource.  
  
The labels in the following table will have an empty value —and are considered equivalent to labels that don't exist per [Prometheus metric names and labels](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)— if the relevant field isn't present in the DBCluster manifest.

**Metric Name** | **Description** | **Label** | **Unit** | Type  
---|---|---|---|---  
` alloydb_omni_dbcluster_ha_ready ` | The high availability (HA) readiness of the `DBCluster`: `1` if `ha-ready`, otherwise `0.` | `reason`: The reason why this `DBCluster` is (un)ready for HA. | 1 | Gauge  
` alloydb_omni_dbcluster_primary_ready ` | The readiness of the `DBCluster` primary node: `1` if ready, otherwise `0.` | `reason`: The reason why this `DBCluster`'s primary node is (un)ready. | 1 | Gauge  
` alloydb_omni_dbcluster_status_info ` | The current status of the `DBCluster.` | 

  * `phase`: the phase of the `DBCluster`.


  * `database_version`: the current running version of the AlloyDB Omni image, for example, 15.7.0.


  * `controlplane_agents_version`: the current running version of the control plane agents image, for example, 1.3.0.


  * `read_write_endpoint`: the read-write endpoint of the DBCluster`.`


  * `read_only_endpoint`: the read-only endpoint of the DBCluster.


  * `primary_phase`: the phase of the `DBCluster` primary node.


  * `haready_status`: `HAReady` condition status, `True` or `False.`


  * `haready_reason`: the reason for the `HAReady` condition.

| 1 | Info  
` alloydb_omni_dbcluster_spec_info ` | `DBCluster` configuration under the `spec` field of the DBCluster manifest. | 

  * `num_standbys`:the number of standby nodes configured.


  * database_version: the version of the AlloyDB Omni image configured, for example, 15.7.0.


  * `controlplane_agents_version`: the version of the control plane agents image configured, for example, 1.3.0.


  * `is_deleted`: indicates whether this `DBCluster` is marked for deletion, set to `true` or `false.`


  * `allow_external_incoming_traffic`: indicates whether this `DBCluster` is configured to allow traffic from out of the Kubernetes cluster, `true` or `false`.

| 1 | Info  
` alloydb_omni_dbcluster_spec_num_standbys ` | The number of standbys defined in the `DBCluster` spec. | N/A | 1 | Gauge  
` alloydb_omni_dbcluster_critical_incident_info ` | Critical incident entries under the DBCluster manifest `status.criticalIncidents` section. | 

  * `create_time`: The time when the critical incident occurred.


  * `message`: The error message of the critical incident.


  * `code`: The error code of the critical incident.

| 1 | Info  
` alloydb_omni_dbcluster_critical_incident_create_time ` | The time when the critical incident occurred, expressed in [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time) format. | 

  * `message`: The error message of the critical incident.


  * `code`: The error code of the critical incident.

| sec | Gauge  
  
## Failover metrics

Failover metrics are metrics exposed from the `Failover` resource manifest. All failover metric names start with `alloydb_omni_failover_`. All Failover metrics have the following labels:

**Key** | **Value**  
---|---  
` namespace ` | The namespace that the `Failover` belongs to.  
` failover ` | The name of the `Failover` custom resource.  
` dbcluster ` | The name of the DBCluster custom resource that the Failover targets. This value is the same as the `spec.dbclusterRef` field of the `Failover`.  
  
The labels in the following table will have an empty value —and are considered equivalent to labels that don't exist based on [Prometheus metric names and labels](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)— if the relevant field isn't present in the Failover manifest.

**Metric name** | **Description** | **Label** | **Unit** | Type  
---|---|---|---|---  
` alloydb_omni_failover_start_time ` | The time when this `Failover` started, expressed in [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time) format. | 

  * `state`: the state of the `Failover`.


  * `phase`: the phase of the `Failover`.

| sec | Gauge  
` alloydb_omni_failover_end_time ` | The time when the `Failover` finished, expressed in [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time) format | 

  * `state`: the state of the `Failover`


  * `phase`: the phase of the `Failover`

| sec | Gauge  
` alloydb_omni_failover_status_info ` | The current status of the `Failover`. | 

  * `start_time`: the time when the `Failover` started.


  * `end_time`: the time when the `Failover` finished.


  * `new_primary`: the name of the primary node after the `Failover` finished.


  * `old_primary`: the name of the primary node before the `Failover` started


  * `phase`: the phase of the `Failover`.


  * `state`: the state of the `Failover`.

| 1 | Info  
  
## PgBouncer metrics

PgBouncer metrics are metrics that are exposed from`PgBouncer` resource manifests. All PgBouncer metric names start with `alloydb_omni_pgbouncer_`. All PgBouncer metrics have the following labels:

**Key** | **Value**  
---|---  
` namespace ` | The namespace that the `PgBouncer` belongs to.  
` pgbouncer ` | The name of the `PgBouncer` custom resource.  
` dbcluster ` | The name of the DBCluster custom resource that this `PgBouncer` targets. This value is the same as the `spec.dbclusterRef` field of the `PgBouncer`.  
  
The labels in the following table will have an empty value —and are considered equivalent to labels that don't exist based on [Prometheus metric names and labels](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)— if the relevant field isn't present in the PgBouncer manifest..

**Metric Name** | **Description** | **Label** | Unit | Type  
---|---|---|---|---  
` alloydb_omni_pgbouncer_status_info ` | The current status of the PgBouncer. | 

  * `endpoint`: The endpoint exposed by this PgBouncer. You connect to this endpoint to run queries against the DBCluster that this PgBouncer targets.


  * `phase`: the phase of the PgBouncer

| 1 | Info  
  
## What's next

  * [Monitor AlloyDB Omni Kubernetes operator custom resources](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/monitor-kubernetes-operator-custom-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
