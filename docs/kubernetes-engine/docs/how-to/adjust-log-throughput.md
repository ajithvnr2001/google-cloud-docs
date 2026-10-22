---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput/
title: Adjust log throughput \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:16.018774+00:00
---

# Adjust log throughput  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Adjust log throughput Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes default log throughput and how to increase throughput.

When system logging is enabled, a dedicated Logging agent is automatically deployed and managed. It runs on all GKE nodes in a cluster to collect logs, adds helpful metadata about the container, pod, and cluster, and then sends the logs to Cloud Logging using a fluentbit-based agent.

The dedicated Logging agent provides at least 100 KiB per second log throughput per node for system and workload logs. If a node is underutilized, then depending on the type of log load (for example, text or structured log entries, very few containers on the node or many containers), the dedicated logging agent might provide throughput as much as 500 KiB per second or more. Additionally, in clusters with GKE control plane version 1.23.13-gke.1000 or later, the Logging agent allows for throughput as high as 10 MiB per second on nodes that have at least 2 unused CPU cores. Be aware that at higher throughputs, some logs might be lost. If the logging rate exceeds expected limits, then Fluent Bit's behavior becomes undefined, which might result in problems such as system freezes or Out-of-Memory (OOM) kills.

## Identify nodes with higher log throughput

By default, GKE clusters collect [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics). The system metric `kubernetes.io/node/logs/input_bytes` provides the number of log bytes generated per second on a node. This metric can help you decide which variant of the logging agent makes sense to deploy in your cluster or node pools.

To view the historical logging throughput for each node in your cluster, follow these steps:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Select a metric** field, select `kubernetes.io/node/logs/input_bytes`.

  3. In the **Group by** field, select **project_id** , **location** , **cluster_name** , and **node_name**.

  4. Click **OK**

  5. Optionally, sort the list of metrics in descending order by clicking the column header **Value** above the list of metrics.




To understand how much logging volume is due to system components or due to workloads running on the node, you may also group by the **type** metric label.

## Enable high-throughput logging

If any GKE nodes require more than 100 KiB per second log throughput and your GKE Standard cluster is using control plane version 1.23.13-gke.1000 or later, you can configure GKE to deploy an alternative configuration of the Logging agent designed to maximize logging throughput. This maximum throughput Logging variant allows for throughput as high as 10 MiB per second per node. You can deploy this high-throughput Logging agent to all nodes in a cluster or to all nodes in a node pool.

This high-throughput configuration will consume additional CPU and memory.

**Important:** For high-throughput logging, `pd-balanced`, `pd-ssd` or `pd-extreme` disk types are mandatory because the Fluent Bit agent needs to read and write intensively from and to disks. For more information about disk types and their performance, see [Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance).**Warning:** Changing the logging agent on an existing node pool recreates all nodes. If you change the logging agent for an existing cluster, the existing node pools are unaffected and the change only applies to new node pools added to the cluster.

###  gcloud CLI 

To enable high-throughput logging on all nodes in a new cluster:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=MAX_THROUGHPUT \
        --machine-type=MACHINE_TYPE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the new cluster.
  * `MACHINE_TYPE`: a machine type that has enough CPU for the Logging agent, such as `e2-standard-8`.



All newly created node pools in this cluster, including the default node pool, deploy the high-throughput Logging agent.

To confirm if high-throughput logging is already set for an existing cluster, use the [`gcloud container cluster describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe) command: 
    
    
    gcloud container clusters describe CLUSTER_NAME \
       --location=COMPUTE_LOCATION  \
       --format="value(nodePoolDefaults[].loggingConfig.variantConfig.variant)"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.

**Note:** A `DEFAULT` output indicates the value remains unset, whereas a `MAX_THROUGHPUT` output signifies that it has been configured. 

To configure high-throughput logging for an existing cluster: use the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=MAX_THROUGHPUT
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.



To create a new node pool that uses the high-throughput Logging agent, use the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) command:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=MAX_THROUGHPUT
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the new cluster.



To confirm if high-throughput logging is already set for an existing node pool use the [`gcloud container node-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/describe) command: 
    
    
    gcloud container node-pools describe NODEPOOL_NAME \
       --cluster=CLUSTER_NAME \
       --location=COMPUTE_LOCATION  \
       --format="value(config.loggingConfig.variantConfig.variant)"
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).

**Note:** An `EMPTY` or `DEFAULT` output indicates the value remains unset, whereas a `MAX_THROUGHPUT` output signifies that it has been configured. 

To update an existing node pool, use the [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) command.
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=MAX_THROUGHPUT
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).



###  Terraform 

The following code blocks specify how to declare node pools with or without high-throughput logging.

To manage the node pools explicitly, you must specify your cluster without a default node pool.
    
    
    resource "google_container_cluster" "with_example_logging_variants" {
      provider           = google
      name               = "CLUSTER_NAME"
      location           = "COMPUTE_LOCATION"
      initial_node_count = 0 # Create the cluster without a default node pool.
    }
    

To specify a node pool that uses the high-throughput agent, use the `node_config` field to specify the Logging agent variant as `MAX_THROUGHPUT` and an appropriate machine type:
    
    
    resource "google_container_node_pool" "with_example_logging_variant" {
      provider = google
      name     = "example-node-pool-with-htl"
      cluster  = google_container_cluster.with_example_logging_variants.name
      location = "COMPUTE_LOCATION"
      node_config {
        logging_variant = "MAX_THROUGHPUT"
        # Use a machine type with enough CPU to accommodate the high-throughput agent, such as e2-standard-8.
        machine_type = "e2-standard-8"
      }
      node_count = 1
    }
    

To specify a node pool that uses the default agent, use the `node_config` field to specify the Logging agent variant as `DEFAULT`:
    
    
    resource "google_container_node_pool" "with_default_logging_variant" {
      provider = google
      name     = "example-node-pool-with-default-logging"
      cluster  = google_container_cluster.with_example_logging_variants.name
      location = "COMPUTE_LOCATION"
      node_config {
        logging_variant = "DEFAULT"
      }
      node_count = 1
    }
    

## Disable high-throughput logging

If you no longer want to use the high-throughput Logging agent, deploy the default Logging agent to the cluster or node pool.

**Warning:** Changing the logging agent on an existing node pool recreates all nodes. If you change the logging agent for an existing cluster, the existing node pools are unaffected and the change only applies to new node pools added to the cluster.

###  gcloud CLI 

Pass the flag `--logging-variant=DEFAULT` when you create or update a cluster or node pool.

To use the default logging agent on all nodes in a new cluster:
    
    
      gcloud container clusters create CLUSTER_NAME \
          --location=COMPUTE_LOCATION \
          --logging-variant=DEFAULT \
          --machine-type=MACHINE_TYPE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the new cluster.
  * `MACHINE_TYPE`: a machine type that has enough CPU for the Logging agent, such as `e2-standard-8`.



To use the default logging agent on an existing cluster: use the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=DEFAULT
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.



To use the default logging agent for a new node pool, use the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) command:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=DEFAULT
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the new cluster.



To update an existing node pool, use the [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) command:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --logging-variant=DEFAULT
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).



###  Terraform 

If you no longer want Terraform to create node pools that use the high-throughput Logging agent, set the `logging_variant` field to `DEFAULT`.

## What's next

  * Learn how to [control log ingestion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
