---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring/
title: Configure automatic application monitoring for workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:04.011684+00:00
---

# Configure automatic application monitoring for workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure automatic application monitoring for workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can save time and effort configuring and maintaining monitoring applications running on Google Kubernetes Engine (GKE) by enabling automatic application monitoring for supported workloads.

### How automatic application monitoring works

When you enable automatic application monitoring, GKE detects deployed instances of supported workloads and deploys [`PodMonitoring` resources](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) for each detected workload instance. 

Automatic application monitoring also installs out-of-the-box dashboards for monitoring applications. The metrics are collected by [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

### Supported workloads

Automatic application monitoring supports the following workloads:

  * [Apache Airflow](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/airflow)
  * [Istio](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/istio#exporter-podmonitoring)
  * [RabbitMQ](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/rabbitmq)
  * AI model servers: 
    * [JetStream](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetstream)
    * [NVIDIA Triton](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-triton)
    * [SGLang](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/sglang)
    * [TensorFlow Serving](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tf-serving)
    * [Text Generation Inference](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tgi)
    * [TorchServe](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/torchserve)
    * [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm)



The metrics scraping interval for AI model servers is 15s. For non-AI workloads, the scraping interval is 30s.

For more information about other out-of-the-box observability solutions that you can configure manually, see [Introduction to exporter configuration](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction) in the Google Cloud Observability documentation.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the [Cloud Monitoring API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com).



### Requirements for automatic application monitoring

To enable automatic application monitoring, your GKE cluster must meet the following requirements:

  * Your cluster must be running GKE version 1.28 or later.
  * You must have gcloud CLI version 492.0.0 or later.
  * Your cluster must have [Google Cloud Managed Service for Prometheus managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) enabled. Google Cloud Managed Service for Prometheus managed collection is enabled by default for new clusters.



## Enable automatic application monitoring

You can enable automatic application monitoring for new or existing GKE clusters using the Google Cloud console, the Google Cloud CLI or the GKE API.

Metrics scraping takes up to 10 minutes to start for supported workloads after you deploy a new workload or after you enable automatic application monitoring for a cluster.

###  Console 

To enable automatic application monitoring for a new cluster, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click add_box **Create** , and then in the Standard or Autopilot section, click **Configure**.

  3. In the navigation pane, click **Advanced settings** , and then do one of the following:

     * **Autopilot** : In the **Operations** section, select **Enable Automatic Application Monitoring**.
     * **Standard** : In the **Google Cloud Managed Service for Prometheus** row, click _edit_ **Edit configuration** , select **Enable Automatic Application Monitoring** , and then click **Save**.
  4. Click **Create**.




You can also enable automatic application monitoring for an existing cluster by updating the **Enable automatic application monitoring** field in the **Operations** section of the **Cluster Details** tab.

###  gcloud 

To enable automatic application monitoring for a new cluster, use the option `--auto-monitoring-scope=ALL`:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --auto-monitoring-scope=ALL
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



You can also update an existing cluster using the command [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update).

###  API 

To enable automatic application monitoring for a new cluster, make a `POST` request to the method [`clusters.create`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/create):
    
    
    POST https://container.googleapis.com/v1/projects/PROJECT_ID/locations/COMPUTE_LOCATION/clusters
    
    {
      "cluster": {
        "name": "CLUSTER_NAME",
        "initialNodeCount": 1,
        "monitoringConfig": {
          "managedPrometheusConfig": {
            "enabled": true,
            "autoMonitoringConfig": {
              "scope": "ALL"
            }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_NAME`: the name of the new cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



## Determine if automatic application monitoring is enabled

You can determine if automatic application monitoring is enabled or disabled for a cluster using the Google Cloud console, the gcloud CLI, or the GKE API.

###  Console 

Do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster.

  3. In the **Features** section, the **Automatic application monitoring** field indicates if automatic application monitoring is enabled or disabled.




###  gcloud 

Describe the cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --format='value(monitoringConfig.managedPrometheusConfig.autoMonitoringConfig.scope)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



The output is similar to the following:
    
    
    ALL
    

In the output, if the returned value is `ALL`, automatic application monitoring is enabled. Otherwise, automatic application monitoring is disabled.

###  API 

Make a `GET` request to the method [`clusters.get`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/get):
    
    
    GET https://container.googleapis.com/v1/projects/PROJECT_ID/locations/COMPUTE_LOCATION/clusters/CLUSTER_NAME
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



The output is similar to the following:
    
    
    {
      "monitoringConfig": {
        "managedPrometheusConfig": {
          "autoMonitoringConfig": {
            "scope": "ALL"
          }
        }
      }
    }
    

In the JSON output, if the value of the `scope` field inside `autoMonitoringConfig` is `"ALL"`, automatic application monitoring is enabled. Otherwise, automatic application monitoring is disabled.

## View dashboards

When you enable automatic application monitoring, GKE installs out-of-the-box dashboards for monitoring applications for supported workloads that are deployed to your cluster. You won't see dashboards for supported workloads that have never run on a cluster.

### Dashboards with telemetry from automatically monitored workloads

To view the dashboards with telemetry from automatically monitored workloads in the Google Kubernetes Engine page, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster where you want to view dashboards for automatically monitored workloads.

  3. Click the **Observability** tab. The **Integrations** section shows configured dashboards for supported workloads running on the cluster.




To view the dashboards with telemetry from automatically monitored workloads in the Cloud Monitoring page, do the following:

  1. Go to the **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click the **Dashboard List** tab.

  3. Select the **Integrations** category.

  4. Click the name of the dashboard. For example, **RabbitMQ Prometheus Overview**.




### Dashboards for AI/ML observability metrics

To view dashboards for AI/ML observability metrics, do the following:

  1. In the Google Cloud console, go to the **Deployed Models** page:

[Go to Deployed Models](https://console.cloud.google.com/kubernetes/aiml/deployments/models)

  2. To view details about a specific deployment, including its metrics, logs, and dashboards, click the model name in the list.

  3. To view the observability dashboards, click the **Observability** tab. If prompted, click **Enable** to enable metrics collection for the cluster.

     * The **Infrastructure usage** dashboard displays utilization metrics.
     * The **DCGM** dashboard displays NVIDIA Data Center GPU Manager (DCGM) metrics.
     * If the deployment uses vLLM, then the **Model performance** dashboard is available and displays metrics for vLLM model performance.



## Disable automatic application monitoring

If you disable automatic application monitoring on a cluster, the `PodMonitoring` resources that GKE created remain intact and GKE continues to monitor existing supported workloads. GKE stops automatically monitoring new instances of supported workloads that you deploy to the cluster. To stop monitoring existing supported workloads, you must delete the `PodMonitoring` resources that GKE created. If you re-enable automatic application monitoring for a cluster, GKE detects and reconciles the `PodMonitoring` resources that it previously created.

You can disable automatic application monitoring for a cluster using the Google Cloud console, the gcloud CLI, or the GKE API.

###  Console 

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster.

  3. In the **Features** list, find the **Automatic application monitoring** field.

  4. Click _edit_**Edit**.

  5. Deselect **Enable automatic application monitoring**.

  6. Click **Save**.




###  gcloud 

Update the cluster using the option `--auto-monitoring-scope=NONE`:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --auto-monitoring-scope=NONE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



###  API 

Make a `PUT` request to the method [`clusters.update`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update):
    
    
    PUT https://container.googleapis.com/v1/projects/PROJECT_ID/locations/COMPUTE_LOCATION/clusters/CLUSTER_NAME
    
    {
      "update": {
        "desiredMonitoringConfig": {
          "managedPrometheusConfig": {
            "autoMonitoringConfig": {
              "scope": "NONE"
            }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



## Customize automatic monitoring of supported workloads

You can customize the monitoring configuration for individual instances of supported workloads or opt out of monitoring individual instances of supported workloads.

To customize the `PodMonitoring` resource for a deployed instance of a supported workload without impacting the automatic application monitoring of other workloads, you must exclude the instance from automatic application monitoring and then update the configuration or replace the `PodMonitoring` resource associated with the target workload instance.

If you update or delete a `PodMonitoring` resource that GKE created without excluding the associated workload, GKE restores the `PodMonitoring` resource to ensure continuity while monitoring other supported workloads.

**Caution:** If you deploy your own `PodMonitoring` resource for a supported workload while automatic application monitoring is enabled, the `PodMonitoring` resource scrapes and exports metrics in parallel with the `PodMonitoring` resource that GKE creates. This results in duplicative telemetry collection for the workload. To avoid this duplication when using automatic application monitoring, either delete the `PodMonitoring` resources that you created for the supported workloads, or exclude the workloads and manually delete the `PodMonitoring` resources that GKE created.

### Find the `PodMonitoring` resource for a workload

You can identify the `PodMonitoring` resource that GKE created for a workload using the Google Cloud console:

  1. Go to the **Object browser** page.

[Go to Object browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. In the **Cluster** field, enter the name of the cluster.

  3. In the **Namespace** field, enter the name of the namespace.

  4. In the **Object Kinds** filter, select **PodMonitoring**.

  5. Under **monitoring.googleapis.com** , select **PodMonitoring**.

  6. Click an object name to inspect the object. The metadata label `source:gke-auto-monitoring` indicates that GKE created the `PodMonitoring` resource.




### Exclude deployed instances from automatic monitoring

If you don't want to monitor a deployed instance of a supported workload, or if you want to customize the monitoring configuration of a workload, you can exclude the workload from automatic application monitoring.

To exclude a workload, you must add the metadata label `allow-gke-auto-monitoring: false` to the target workload configuration. For example, the following manifest describes a RabbitMQ StatefulSet that is not monitored by automatic application monitoring:
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: rabbitmq
      labels:
        allow-gke-auto-monitoring: "false"
    spec:
      serviceName: rabbitmq
      replicas: 3
    

After you exclude a workload instance, you can delete the `PodMonitoring` resource that GKE created for the workload. GKE does not attempt to restore the `PodMonitoring` resource if you delete or modify it. If you deploy a new workload with the metadata label `allow-gke-auto-monitoring: false`, GKE does not create a `PodMonitoring` resource for the workload.

### Delete the monitoring configuration for a workload

If you want to stop monitoring a workload or if you want to deploy your own customized `PodMonitoring` resource for a workload, you can delete the monitoring configuration.

To delete the automatic application monitoring configuration of an individual workload, do the following:

  1. Exclude the workload from automatic application monitoring.
  2. Identify the `PodMonitoring` resource that GKE created for the workload.
  3. Delete the `PodMonitoring` resource:
         
         kubectl delete podmonitoring POD_MONITORING_NAME -n NAMESPACE
         

Replace the following:

     * `POD_MONITORING_NAME`: the name of the `PodMonitoring` resource.
     * `NAMESPACE`: the namespace of the `PodMonitoring` resource.



To delete the automatic application monitoring configuration of all workloads in a cluster, do the following:

  1. Disable automatic application monitoring.
  2. Delete all `PodMonitoring` resources in the cluster with the metadata label `source:gke-auto-monitoring`:
         
         kubectl delete podmonitorings -l source=gke-auto-monitoring --all-namespaces
         




## Pricing

The automatic application monitoring configuration and installation of out-of-the-box dashboards for supported workloads by automatic application monitoring is available at no additional charge. However, Monitoring charges for the ingestion of metrics by Google Cloud Managed Service for Prometheus according to [Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## What's next

  * Learn how to [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
