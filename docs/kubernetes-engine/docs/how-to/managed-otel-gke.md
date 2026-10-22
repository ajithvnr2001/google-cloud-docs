---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke/
title: Deploy Managed OpenTelemetry for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:42.320693+00:00
---

# Deploy Managed OpenTelemetry for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy Managed OpenTelemetry for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to set up Managed OpenTelemetry for GKE to send [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) traces, metrics, and logs to Google Cloud Observability from applications running on GKE.

For more details about how the Managed OpenTelemetry for GKE works, see [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke).

You can use Managed OpenTelemetry for GKE to do the following:

  * Configure workloads running on GKE to send OpenTelemetry Protocol (OTLP) traces, metrics, and logs to the managed collector.
  * Receive OpenTelemetry Protocol (OTLP) traces, metrics, and logs from the applications running on GKE.
  * Export that data to Google Cloud Observability.



If you need collector-level filtering and controls, use the [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel) instead of this managed offering.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. Verify that you have the permissions required to complete this guide. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the GKE, Telemetry (OTLP), Cloud Logging, Cloud Monitoring, Cloud Trace APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com telemetry.googleapis.com logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. Verify that you have the permissions required to complete this guide. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the GKE, Telemetry (OTLP), Cloud Logging, Cloud Monitoring, Cloud Trace APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com telemetry.googleapis.com logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com




### Requirements

To use Managed OpenTelemetry for GKE, you must meet the following requirements:

  * The cluster must have GKE version 1.34.1-gke.2178000 or later.
  * gcloud CLI enabled with version 576.0.0 or later.
  * If you use Terraform to provision your GKE infrastructure, you must use the `terraform-provider-google-beta` provider at version `v7.17.0` or later.



### Required roles

To get the permissions that you need to enable and use GKE managed OpenTelemetry, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Costs

See [Billing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#billing) for details about costs connected to the use of Managed OpenTelemetry for GKE.

## Enable Managed OpenTelemetry for GKE in a cluster

To set up Managed OpenTelemetry for GKE, you need to do the following:

  * Enable Managed OpenTelemetry for GKE in a cluster.
  * Configure the application that you are monitoring to send signals to the managed collector's endpoint.



When you enable Managed OpenTelemetry for GKE, the following objects are deployed to the cluster:

  * A GKE Managed OpenTelemetry collector deployment that is deployed within the `gke-managed-otel` namespace. The in-cluster managed OpenTelemetry collector HTTP endpoint for logs, metrics, and traces is the following: `http://opentelemetry-collector.gke-managed-otel.svc.cluster.local:4318`.
  * A custom resource definition, `instrumentations.telemetry.googleapis.com`, that you can use to set up automatic configuration of your workloads.

For more details about custom resources, see [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in the Kubernetes documentation.




### Enable on a new cluster

To enable Managed OpenTelemetry for GKE on a new cluster, follow these steps:

###  gcloud 

For an Autopilot cluster, use the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
      --project=PROJECT_ID \
      --managed-otel-scope=COLLECTION_AND_INSTRUMENTATION_COMPONENTS \
      --location=LOCATION \
      --cluster-version=VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region or zone.
  * `VERSION`: the [version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions), which must be `1.34.1-gke.2178000` or later.



For a Standard cluster, use the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
      --project=PROJECT_ID \
      --managed-otel-scope=COLLECTION_AND_INSTRUMENTATION_COMPONENTS \
      --location=LOCATION \
      --cluster-version=VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region or zone.
  * `VERSION`: the [version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions), which must be `1.34.1-gke.2178000` or later.



###  Console 

  * For an Autopilot cluster, do the following:

    1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

    2. In the navigation pane, click **Advanced settings**.

    3. In the **Operations** section, select **Enable managed OpenTelemetry**.

    4. Click **Create**.

  * For a Standard cluster, do the following:

    1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

    2. In the navigation pane, click **Advanced settings**.
    3. In the **Managed OpenTelemetry** row, click _edit_ **Edit configuration**.
    4. Select **Enable managed OpenTelemetry**.
    5. Click **Save**.
    6. Click **Create**.



###  Terraform 

To enable Managed OpenTelemetry for GKE on a new cluster using Terraform, refer to the following example:
    
    
    terraform {
      required_providers {
        google-beta = {
          source  = "hashicorp/google-beta"
          version = ">= 7.17.0"
        }
      }
    }
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-regional-with-managed-otel"
      provider = google-beta
      location = "us-west1"
    
      initial_node_count = 1
      release_channel {
        channel = "RAPID" # The default rapid version already has the feature available.
      }
    
      managed_opentelemetry_config {
        scope = "COLLECTION_AND_INSTRUMENTATION_COMPONENTS"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Enable on an existing cluster

To enable the Managed OpenTelemetry for GKE on an existing cluster, follow these steps:

###  gcloud 

  1. Ensure the cluster version is `1.34.1-gke.2178000` or later. For details about how to upgrade and existing cluster, see [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) and [Autopilot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot).

  2. Enable Managed OpenTelemetry for GKE by using the following command:
         
         gcloud container clusters update CLUSTER_NAME \
           --project=PROJECT_ID \
           --managed-otel-scope=COLLECTION_AND_INSTRUMENTATION_COMPONENTS \
           --location=LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PROJECT_ID`: the Google Cloud project ID.
     * `LOCATION`: the region or zone.



###  Console 

  1. Ensure the cluster version is `1.34.1-gke.2178000` or later. For details about how to upgrade and existing cluster, see [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) and [Autopilot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot).

  2. In the Google Cloud console, go to the Kubernetes clusters page:

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  3. Click the name of the cluster.

  4. In the **Features** list, locate the **Managed OpenTelemetry** option. If it is listed as disabled, click edit **Edit** , and then select **Enable managed OpenTelemetry**.

  5. Click **Save changes**.




###  Terraform 

To enable Managed OpenTelemetry for GKE on an existing cluster, add the `managed_opentelemetry_config` block to your existing `google_container_cluster` resource, similar to the following example:
    
    
    terraform {
      required_providers {
        google-beta = {
          source  = "hashicorp/google-beta"
          version = ">= 7.17.0"
        }
      }
    }
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-regional-with-managed-otel"
      provider = google-beta
      location = "us-west1"
    
      initial_node_count = 1
      release_channel {
        channel = "RAPID" # The default rapid version already has the feature available.
      }
    
      managed_opentelemetry_config {
        scope = "COLLECTION_AND_INSTRUMENTATION_COMPONENTS"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Configure your application to use the Managed OpenTelemetry collector

Applications need to be configured to be able to send signals to the managed collector's endpoint. When the applications are configured, the Managed OpenTelemetry collector receives signals from the applications running on the cluster where the collector is enabled. Signals from the application include traces, metrics, and logs.

To send OpenTelemetry signals, applications need to be already instrumented to generate OpenTelemetry metrics. For details, see [supported workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#supported-workloads).

You can configure your application manually to send signals to the managed collector [endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#managed-collection), or you can use automatic configuration. We don't recommend using both methods together for the same workload, because the automatic configuration can override manual changes. This combination might make it more difficult to track changes to the configuration.

The following sections describe how to configure applications to send signals to the collector using the automatic configuration.

### Set up automatic configuration

Automatic configuration uses environment variables to configure the workloads to send signals to the managed collector's endpoint.

To enable automatic injection of environment variables into Pods, you use the `Instrumentation` custom resource. The environment variables have the OpenTelemetry configuration, and they can be injected into some Pods with matched labels in a namespace or all Pods in a namespace.

Then, when an application is deployed to the namespace, GKE uses the configuration to automatically inject environment variables to the Pods where the workloads run.

  1. To configure the `Instrumentation` custom resource, do the following:

     1. Save the following `Instrumentation` manifest in a file named `otlp-auto-config-namespace.yaml`:
            
            apiVersion: telemetry.googleapis.com/v1alpha1
            kind: Instrumentation
            metadata:
              namespace: NAMESPACE
              name: NAME
            spec:
              selector:
                matchLabels:
                  KEY: VALUE
              autoInstrumentationConfig:
                configInjection:
                  enabled: true
              otelSDKConfig:
                tracer_provider:
                  sampler:
                    parent_based:
                      root:
                        trace_id_ratio_based:
                          ratio: "TRACE_RATIO"
                meter_provider:
                  readers:
                  - periodic:
                      interval: METRICS_INTERVAL
            

Replace the following:

        * `NAMESPACE`: the namespace that contains the Pods you want to target for auto-instrumentation. Use `default` to target the default namespace.
        * `NAME`: the name of the manifest file. In this example, the name is `otlp-auto-config-namespace.yaml`.
        * (Optional) The label attached to Pods to target. If an empty selector is specified (`{}`), then all Pods in the namespace are targeted. 
          * `KEY`: the label's key.
          * `VALUE`: the label's value.
        * `TRACE_RATIO`: the ratio of trace data to collect. If unspecified, the default is `1.0`. For more details, see Modify the trace sampling rate.
        * `METRICS_INTERVAL`: the interval, in milliseconds, of monitoring data to collect. The default is `30000`. The value must be non-negative, with a minimum of 5,000 ms, maximum of 300,000 ms, and multiple of 5,000 ms. For more details, see Modify the metric export interval.
     2. If you want to modify any of the settings, then see the following section to modify the configuration.

     3. Apply the configuration by running the following command:
            
            kubectl apply -f otlp-auto-config-namespace.yaml
            

  2. To inject the environment variables automatically, you need to deploy the application to the namespace in your cluster that has the configuration applied.

     * To apply the configuration to a workload that is not yet running in the namespace, deploy the workload using the following command:
           
           kubectl apply -f DEPLOYMENT_NAME -n NAMESPACE
           

Replace the following:

       * `DEPLOYMENT_NAME`: the name of the deployment.
       * `NAMESPACE`: the namespace.
     * To apply the configuration to a workload that is already running in the namespace, redeploy the workload using the following command:
           
           kubectl rollout restart deployment DEPLOYMENT_NAME -n NAMESPACE
           

Replace the following:

       * `DEPLOYMENT_NAME`: the name of the deployment.
       * `NAMESPACE`: the namespace.



After you apply the configuration to the cluster, GKE automatically configures all workloads when they are deployed to the cluster. The workloads are instrumented by injecting environment variables to the Pods where the workloads run.

When a workload is configured with these environment variables is running in a cluster where the managed collector is deployed, then as the workload runs it sends OpenTelemetry signals to the managed collector. These signals are available for you to view in Google Cloud Observability.

For more detail about viewing the signals, see [View telemetry](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#view-telemetry). For an example, see [Generate sample telemetry](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#generate-telemetry).

### Modify the configuration

To modify the configuration, you need to do the following:

  1. Modify the `Instrumentation` manifest file.

  2. Apply the modified configuration.

  3. Redeploy or restart the applications in the corresponding namespace of your cluster after applying the modified configuration.




For more details about these steps, follow the instructions in the section [Create and deploy the configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#create_and_deploy_the_configuration).

### Modify the amount or frequency of data collection

You can modify the amount of trace data collected by modifying the trace sampling rate.

You can modify the frequency that monitoring data is sent to Cloud Monitoring by modifying the metric export interval.

You can't modify the amount or frequency of logging data collected. You can, however, disable all logging, metrics, or tracing data from being collected. For details, see Select the signal type to collect.

#### Modify the trace sampling rate

A workload can generate a large amount of trace data. For your own situation, it's important for you to determine the balance between the cost of collecting and storing data, and the level of detail that you need for the data to be useful.

The [default OpenTelemetry SDK behavior](https://github.com/open-telemetry/opentelemetry-configuration/blob/26f29f8119042c05fd3e08317c025030e79476d9/examples/kitchen-sink.yaml#L746) is `always_on`, which is equivalent to a ratio of 1.

The following is an example of the configuration of the trace sample rate. In this example, the ratio is 0.25 and so trace data is collected at a rate of 25 percent. Modify this ratio number to change the sample rate.
    
    
        tracer_provider:
          sampler:
            parent_based:
              root:
                trace_id_ratio_based:
                  ratio: "0.25"
    

#### Modify the metric export interval

The metric export interval determines the granularity of data that you are able to see in the graphs in Cloud Monitoring.

The following is an example of the configuration of the metric export interval. In this example, the export interval is 30,000 ms.

Metric export interval is used to specify the delay interval between the start of two consecutive exports of metrics from the OpenTelemetry SDK.

The value of this interval must be non-negative, with a minimum of 5,000 ms, maximum of 300,000 ms, and multiple of 5,000 ms. The value is expressed in milliseconds.
    
    
    meter_provider:
      readers:
      - periodic:
          interval: 30000
    

### Select the signal types to collect

You can control which signal types are collected from a workload by disabling the signal types that you don't want to collect. Signal types are traces, metrics, and logs.

You disable signal types using the environment variables in the container where the workload runs. You modify environment variables by modifying the `Instrumentation` custom resource and then redeploying the workload to the container.

The following example is an `Instrumentation` manifest file configured for the collection of only trace data. The collection of logs and metrics is disabled because `meter_provider` and `logger_provider` are set to `null`.
    
    
    apiVersion: telemetry.googleapis.com/v1alpha1
    kind: Instrumentation
    metadata:
      namespace: default
      name: otlp-auto-config-disable-metrics-logs
    spec:
      selector:
        matchLabels: # Update the labels to match your workloads
          app: telemetrygen-app
      autoInstrumentationConfig:
        configInjection:
          enabled: true
      otelSDKConfig:
        meter_provider: null
        logger_provider: null
    

### Collect multimodal prompts and responses data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can configure Managed OpenTelemetry for GKE to [collect multimodal prompts and responses data](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).

This functionality is available for [LangGraph ReAct agents](https://docs.langchain.com/oss/python/langchain/agents) and generative AI agents built with the [Agent Development Kit (ADK) framework](https://google.github.io/adk-docs/).

When you collect multimodal prompts and responses data with Managed OpenTelemetry for GKE, the full contents of your end user's prompts and responses are collected. This prompt and response data is stored in a Cloud Storage bucket. For details about how to manage the storage bucket, including controlling access or deleting data, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/introduction).

You can use products like [Model Armor](https://docs.cloud.google.com/model-armor/overview) and [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) to manage sensitive data that might be in the prompts and responses.

To configure Managed OpenTelemetry for GKE to collect multimodal prompts and responses data, do the following:

  1. Configure your Google Cloud project and the SDK you are using by following the instructions in the [Collect multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses#collect) section.

  2. Create or identify a Cloud Storage bucket to use to collect multimodal prompts and responses. For details, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  3. Give the service account that your application uses the `storage.objects.create` permission for the Cloud Storage bucket.

This permission lets your application write objects to the Cloud Storage bucket. These objects store the prompts and responses that the agentic application creates and receives. For more information, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  4. Configure the `promptsResponses.uploadBasePath` field in the `Instrumentation` custom resource, for example:
         
         apiVersion: telemetry.googleapis.com/v1alpha1
         kind: Instrumentation
         metadata:
           namespace: default
           name: prompts-responses
         spec:
           selector: {}
           promptsResponses:
             uploadBasePath: gs://BUCKET_NAME
         

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket.




When the `Instrumentation` custom resource is updated and the workloads are restarted, then environment variables that configure the prompts and responses are injected into the containers of the workloads.

For more details about the types of media that you can collect and how to explore your multimodal prompts and responses, see [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).

### Disable automatic configuration of workloads

To disable automatic instrumentation of workloads with the specified configuration, delete the `Instrumentation` custom resource from your cluster. To do so, use the following command:
    
    
    kubectl delete instrumentations.telemetry.googleapis.com INSTRUMENTATION_NAME -n NAMESPACE
    

Replace the following:

  * `INSTRUMENTATION_NAME`: the name of the `Instrumentation` custom resource.
  * `NAMESPACE`: the namespace that contains the Pods where you want automatic configuration disabled.



To disable automatic environment variable injection temporarily while preserving auto-instrumentation configuration for future use, set `autoInstrumentationConfig.configInjection.enabled` to `false` and apply the updated custom resource.

The following is an example of the custom resource with the automatic environment variable injection temporarily disabled:
    
    
    apiVersion: telemetry.googleapis.com/v1alpha1
    kind: Instrumentation
    metadata:
      namespace: default
      name: otlp-auto-config-example
    spec:
      selector:
        matchLabels: # Update the labels to match your workloads
          app: telemetrygen-app
      autoInstrumentationConfig:
        configInjection:
          enabled: false # disable environment variables config injection
      otelSDKConfig:
      ... # preserve OpenTelemetry configuration for future use
    

After you delete the custom resource or update it to disable automatic config injection, GKE doesn't auto-instrument new workloads that are targeted by the `Instrumentation` custom resource.

To stop exporting OTLP signals to the managed collector from a workload that was previously instrumented by the custom resource, you must restart the workload for the change to take effect. To do so, use the following command:
    
    
    kubectl rollout restart deployment DEPLOYMENT_NAME -n NAMESPACE
    

Replace the following:

  * `DEPLOYMENT_NAME`: the name of the deployment.
  * `NAMESPACE`: the namespace.



## View telemetry

When a configured workload runs on GKE where Managed OpenTelemetry for GKE is enabled, then OpenTelemetry signals are sent to Google Cloud Observability.

For details about viewing data in Google Cloud Observability, see the following:

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).
  * [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * [View and analyze logs](https://docs.cloud.google.com/trace/docs/finding-traces).



## Generate sample telemetry

This section describes deploying a sample application and pointing that application to the OTLP endpoint of the Managed OpenTelemetry collector. You can then view the telemetry in Google Cloud.

The sample application is a small generator that exports traces, logs, and metrics to the in-cluster managed OpenTelemetry collector HTTP endpoint. The OTLP endpoint is hard-coded within the application, pointing to `http://opentelemetry-collector.gke-managed-otel.svc.cluster.local:4318`.

If you already have an application instrumented with an OpenTelemetry SDK, then you can generate telemetry from your application by pointing your application to the collector's endpoint, or configuring automatic instrumentation for the application.

To deploy the sample application, do the following:

  1. Connect to your cluster where you have enabled Managed OpenTelemetry. To do so, see [Set a default cluster for `kubectl` commands](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#default_cluster_kubectl).

  2. Run the following command:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/otlp-k8s-ingest/main/sample/gke-app.yaml
         

After a few minutes, telemetry generated by the application begins flowing through the collector to the Google Cloud backend for each signal.

     1. Verify that the telemetry is ingested by viewing logs, metrics, and traces from the demo application in Google Cloud console:

     2. To view metrics, do the following:

        1. In the Google Cloud console, go to the Metrics Explorer page:

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

        2. Run the following PromQL query in Metrics Explorer:
               
               sum(avg_over_time({"__name__"="gen","namespace"="opentelemetry-demo","job"="telemetrygen"}[1h]))
               

     3. To view traces, do the following:

        1. In the Google Cloud console, go to the **Trace Explorer** page.

[Go to Trace Explorer](https://console.cloud.google.com/traces/list)

        2. Filter trace spans by span name equal to `lets-go`.

     4. To view logs, do the following:

        1. In the Google Cloud console, go to the Logs Explorer page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

        2. Run the following query:
               
               resource.type="k8s_pod"
               resource.labels.namespace_name="opentelemetry-demo"
               




## Disable Managed OpenTelemetry for GKE

You can disable Managed OpenTelemetry for GKE in the cluster. When you disable the collector, the Managed OpenTelemetry collector is removed from the cluster, and no new telemetry data is collected.

To disable the Managed OpenTelemetry for GKE, use the following steps.

###  gcloud 

To disable Managed OpenTelemetry for GKE for a cluster, run the following `gcloud` command:
    
    
      gcloud container clusters update CLUSTER_NAME \
      --project=PROJECT_ID \
      --managed-otel-scope=NONE \
      --location=LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region or zone.



###  Console 

  1. In the console, go to the list of clusters:

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the cluster that you want to disable the Managed OpenTelemetry collector.

  3. In **Cluster details** , next to **Managed OpenTelemetry** , select the edit icon.

  4. Clear the checkbox to disable the feature.




###  Terraform 

To disable Managed OpenTelemetry for GKE, update the `managed_opentelemetry_config` block in your `google_container_cluster` resource to set the scope to `NONE`.

  1. Update your Terraform config file:
         
         resource "google_container_cluster" "default" {
           provider = google-beta
           name     = "CLUSTER_NAME"
           location = "LOCATION"
           project  = "PROJECT_ID"
         
           # ... other configuration ...
         
           managed_opentelemetry_config {
             scope = "NONE"
           }
         }
         

  2. Apply the Terraform configuration:
         
         terraform apply
         




Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the region or zone.
  * `PROJECT_ID`: the Google Cloud project ID.



When you disable the Managed OpenTelemetry for GKE, the `Instrumentation` custom resource definition and the `Instrumentation` custom resources aren't removed from the cluster. If you re-enable managed OpenTelemetry, then it uses the configuration preserved in the `Instrumentation` custom resources.

If you have telemetry data that was already collected by Managed OpenTelemetry for GKE, then disabling the collector does not affect this data. Existing data is still stored in Google Cloud Observability, and no new telemetry data is collected.

## Troubleshooting

### Autopilot partner privileged workloads

If you try to use automatic configuration with an Autopilot partner privileged workload, then you might see that workload Pod was rejected.

OpenTelemetry config injection is not supported for [privileged workloads from GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads). Targeting such workloads using an `Instrumentation` custom resource to enable OpenTelemetry environment variable injection may cause the workload to fail to match the Autopilot privileged workload allowlist, which means the config-injected Pod would be rejected by GKE Autopilot.

### Logs, metrics, or traces are not visible in the Google Cloud console

Data might not be visible for many different reasons. These reasons include missing permissions to view the data, or incorrect configuration that prevent data from being collected.

Steps that you can take to resolve common issues are the following:

  * Ensure you have all required APIs enabled in your project.

  * Ensure that the `Instrumentation` custom resource is correctly configured, with namespace matching the namespace where the workload is running, and the selector matching the label of your workload.

  * Inspect the workload's Pod to see if the [environment variables](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#environment_variables) are injected correctly.

  * Check the container logs of OpenTelemetry collector to see if there are errors in the collector. To do so, run the following command:
        
        kubectl logs -n gke-managed-otel -l app=opentelemetry-collector -c opentelemetry-collector
        




### Disabling a telemetry signal is not working

When you disable a telemetry signal using the `Instrumentation` custom resource, make sure you apply the custom resource and redeploy the workloads.

When applying the custom resource, use [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/) in the `kubectl apply` command when updating the `Instrumentation` custom resource.

For details about disabling a telemetry signal, see Select the signal types to collect.

### OpenTelemetry injected variables are not visible in my workload

The variables are injected into the containers of workload pods , not the workload. Check the Pods, not the owner objects like ReplicaSets or Deployments.

For example, to confirm the variables are injected correctly for the sample workload in default namespace used in the previous section Generate telemetry, do the following:

  1. Run the following command:
         
         kubectl get pods -n default -l app=telemetrygen-app -o yaml
         

  2. Examine the `spec.containers[*].env` of the Pods.

  3. Ensure that there is an `Instrumentation` object in the same namespace and check that it is targeting the Pod and has config injection feature enabled. To do so, run the following command:
         
         kubectl get instrumentations.telemetry.googleapis.com -n default -o yaml
         




The variables are injected into the containers only when Pods are created because the Kubernetes API doesn't allow modifying most fields in the spec of an existing Pod, such as environment variables. For the configuration to take effect on workloads that were created before you created the `Instrumentation` object, restart the workload. For example, for a Deployment named `telemetry-gen-app`, run the following command:
    
    
    kubectl rollout restart deployment -n default telemetry-gen-app
    

### An excessive amount of trace data in Cloud Trace

To reduce the data collected by Cloud Trace, you can configure a parent-based sampler with a trace ID ratio to only sample a percentage of your traces.

For example, add the following to the `Instrumentation` object:
    
    
    spec:
      otelSDKConfig:
        tracer_provider:
          sampler:
            parent_based:
              root:
                trace_id_ratio_based:
                  ratio: "0.01"
    

The [default OpenTelemetry SDK behavior](https://github.com/open-telemetry/opentelemetry-configuration/blob/26f29f8119042c05fd3e08317c025030e79476d9/examples/kitchen-sink.yaml#L746) is "always_on" tracing, which is equivalent to a ratio of 1.

### Environment variables don't match the configuration

If you made an update to the `Instrumentation` object, check that you have restarted your Pods as described in the section Modify the configuration.

If you see the wrong configuration for your Pod, check that the Pod is correctly targeted by the `Instrumentation` object, and that you don't have multiple `Instrumentation` objects targeting that same Pod:
    
    
    kubectl get instrumentations --all-namespaces \
    -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,SELECTOR:.spec.selector
    
    kubectl get pod -n ${NAMESPACE:?} ${POD_NAME:?} --show-labels
    

Note that an empty selector targets all Pods in its namespace.

If multiple instrumentations target the same Pod when it is created, the instrumentation that was last updated takes effect.

### The `kubectl logs` command returns no output

When logs are streamed directly from an application to an OpenTelemetry collector, then the logs bypass the standard logging path for the container runtime. This is the common scenario when using OpenTelemetry for logs. By default, the exporter sends the logs to the `otlp` endpoint instead of to the `stdout` and `stderr` streams.

In this case, because the logs are not written to the `stdout` or `stderr` streams for the container runtime to capture, the `kubectl logs` command won't display any output for that application. Instead, logging output is available in Cloud Logging.

If you want to use the OpenTelemetry SDK and also send logs to the `stdout` stream, you can configure this by using the logs exporter. For more information, see [Logs Exporter - Standard output](https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/stdout/).

## What's next

  * For details about how Managed OpenTelemetry for GKE works, see [Managed OpenTelemertry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke).
  * For a self-deployed alternative to the Managed OpenTelemetry for GKE, see [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
