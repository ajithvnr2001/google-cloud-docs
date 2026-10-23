---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb/
title: Configure utilization-based load balancing for GKE Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:34.472819+00:00
---

# Configure utilization-based load balancing for GKE Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure utilization-based load balancing for GKE Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to configure utilization-based load balancing for GKE Services. This page is intended for infrastructure and application teams, and GKE administrators who are responsible for configuring and managing traffic distribution for their GKE Services.

You can use utilization-based load balancers to optimize application performance and availability by intelligently distributing traffic based on the real-time resource usage of your GKE Pods.

Before reading this page, ensure that you are familiar with [utilization-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb#overview) for GKE Services and [how utilization-based load balancing works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb#how-ubb-works).

## Pricing

Utilization-based load balancing is a GKE Gateway capability that is available for no additional cost. [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb) and [GKE](https://cloud.google.com/kubernetes-engine/pricing) pricing still apply.

## Quotas

Utilization-based load balancing does not introduce any new quotas, although all the quotas from [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/quotas) and other dependent services still apply.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the Gateway controller requirements.
  * Review limitations.



### GKE Gateway controller requirements

Utilization-based load balancing for GKE Services requires the following:

  * Google Cloud CLI version 516.0.0 or later.
  * GKE version 1.33.1-gke.1918000 or later in the RAPID channel.
  * [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) must be enabled in your cluster.
  * Performance HPA profile must be enabled in your cluster.
  * [Autoscaling API](https://console.cloud.google.com/marketplace/product/google/autoscaling.googleapis.com) must be enabled in your Google Cloud Project.
  * [Node service accounts must be able to write](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.metricsWriter) to the Autoscaling API.



Utilization-based load balancing for GKE Services supports the following:

  * Single and multi-cluster GKE Services that serve as backends to a Google Cloud-managed load balancer.
  * All GKE editions (Standard, Autopilot and Enterprise).
  * All Google Cloud Application Load Balancers, excluding the classic Application Load Balancers.



### Limitations

Utilization-based load balancing for GKE Services has the following limitations.

  * The supported resource utilization metrics are the following: 
    * CPU resource utilization metrics.
    * Custom metrics emitted by your GKE application. For details, see [Expose custom metrics for load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics).
  * Passthrough or proxy Network Load Balancers aren't supported.
  * Only Gateway API is supported; Service and Ingress APIs aren't supported.
  * Utilization-based load balancing doesn't work well if your traffic is very spiky. Traffic rebalancing takes up to 30 seconds when Pods reach their maximum utilization. The utilization signal is expected to rise with incoming traffic, but this delay means that utilization-based load balancing needs time to adjust. For optimal performance, utilization-based load balancing works best in environments with smooth, predictable traffic flows.
  * Utilization-based load balancing can take up to 30 seconds to update and adjust traffic distribution after configuration changes, such as modifying or removing the dryRun field in a `GCPBackendPolicy`. This delay is a known system-wide behavior. As a result, this feature is best suited for applications with relatively stable traffic patterns that can tolerate this update latency.



By default, _utilization-based load balancing_ is disabled for your GKE Services. You must explicitly enable it. If you don't set a maximum utilization threshold, the system defaults to 80% utilization per endpoint.

Your goal in configuring utilization-based load balancing is to optimize traffic distribution so that backend Pods can efficiently manage their workload, which improves application performance and resource utilization.

## Enable utilization-based load balancing and Performance HPA profile

Before you configure utilization-based load balancing, ensure that your GKE cluster supports the required features. Utilization-based load balancing uses custom metrics, like CPU, to make smarter routing decisions. These decisions depend on the following:

  * Gateway API, which allows service-level policies through `GCPBackendPolicy`.
  * The Performance HPA profile, which lets workloads scale faster and more aggressively by using CPU signals.



### Enable Gateway API and Performance HPA profile

**Autopilot**

Gateway API and Performance HPA profile are available by default in an Autopilot cluster.

**Standard**

To create a new Standard cluster with the Performance HPA profile and Gateway API enabled, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        --cluster-version=CLUSTER_VERSION \
        --gateway-api=standard \
        --hpa-profile=performance \
        --release-channel=rapid
    

Replace the following:

  * `CLUSTER_NAME` with the name of your new cluster.
  * `LOCATION` with the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
  * `PROJECT_ID` with your project ID.
  * `CLUSTER_VERSION` with the GKE version, which must be 1.33.1-gke.1918000 or later.



To enable the Performance HPA profile and Gateway API in an existing GKE Standard cluster, use the following:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        --gateway-api=standard \
        --hpa-profile=performance \
        --release-channel=rapid
    

Replace the following:

  * `CLUSTER_NAME` with the name of your cluster.
  * `LOCATION` with the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
  * `PROJECT_ID` with your project ID.



For more information about the Performance HPA profile, see [Configure the Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).

## Configure utilization-based load balancing

After your cluster is ready, define a policy that directs how traffic is routed based on backend utilization. You must use the Kubernetes Gateway API through `GCPBackendPolicy` for the configuration.

### Prerequisites

Before you configure utilization-based load balancing by using Gateway API, make sure that your GKE cluster meets the following requirements:

  1. **Deploy an application** : ensure that you deploy a Kubernetes application by using a Deployment resource. For more information, see [Deploy an application to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

**Note:** For utilization-based load balancing to function correctly, you must define resource `requests`, particularly for CPU, in your Deployment's container specifications. This allows the system to accurately determine baseline resource utilization and rebalance traffic effectively. Without `requests` defined, the load balancing mechanism might not behave as expected.

For example, a typical deployment manifest might include a resources section like this:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: store-v1
         spec:
           # ... other deployment configurations ...
           template:
             # ... other template configurations ...
             spec:
               containers:
                 - name: your-container-name
                   image: your-image
                   ports:
                     - containerPort: 8080
                   resources:
                     limits:
                       cpu: 100m
                       memory: 45Mi
                     requests:
                       cpu: 100m
                       memory: 45Mi
         

  2. **Expose the application by using a Service** : you must expose the application by using a Kubernetes Service. For more information about how Services work and how to configure them, see [Understand Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service).

  3. **Use a Gateway API-based Application Load Balancer** : expose the Service by using a GKE-managed Application Load Balancer that's configured through Gateway API. For more information, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).




### Create a `GCPBackendPolicy` for CPU-based load balancing

This configuration allows GKE to distribute traffic dynamically based on the real-time CPU utilization of each backend Pod.

To enable utilization-based load balancing for GKE Services, use the `GCPBackendPolicy` custom resource from the Kubernetes Gateway API.

The `GCPBackendPolicy` custom resource lets you declaratively define load balancing behavior within your Kubernetes cluster. By specifying CPU utilization metrics, you control how traffic is distributed across backends based on their current resource usage. This approach helps maintain application performance, prevent individual Pods from becoming overloaded, and improve the application's reliability and user experience.

  1. Save the following sample manifest as `my-backend-policy.yaml`:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
           namespace: team-awesome
         spec:
           targetRef:
             group: ""
             kind: Service
             name: super-service
           default:
             balancingMode: CUSTOM_METRICS
             customMetrics:
             - name: gke.cpu
               dryRun: false
         

Note the following:

     * `spec.targetRef.kind: Service`: targets a standard Kubernetes Service within the same cluster.
     * `spec.targetRef.kind: ServiceImport`: targets a service from another cluster in a multi-cluster setup. For multi-cluster services, the value of the `group` field must be set to `net.gke.io`.
     * `balancingMode: CUSTOM_METRICS`: enables custom metric-based load balancing.
     * `name: gke.cpu`: specifies CPU utilization as the metric for traffic distribution.

If the `maxUtilizationPercent` field is not specified, the default utilization threshold is 80%. Traffic is rebalanced when a backend exceeds 80% CPU usage.

  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f my-backend-policy.yaml
         




By basing traffic distribution on real-time CPU utilization, you automatically optimize performance. This action helps prevent overload on individual Pods.

#### Important considerations for `dryRun` and `balancingMode`

When you configure `GCPBackendPolicy` with custom metrics, consider the interaction between `balancingMode` and the `dryRun` field in your `customMetrics` definition. This interaction determines how the load balancer uses your custom metrics. For more information on custom metrics and their restrictions, including those related to balancing modes, see [Cloud Load Balancing custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics).

  * **`balancingMode: CUSTOM_METRICS`**

    * To distribute traffic based on a custom metric, at least one custom metric in the `customMetrics` list **must have`dryRun` set to `false`**. This setting tells the load balancer to actively use that metric for rebalancing decisions.
    * You can include other custom metrics with `dryRun: true` alongside non-dry-run metrics. This lets you test or monitor new metrics, such as GPU utilization, without them affecting traffic, while another metric, such as CPU utilization with `dryRun: false`, controls balancing.
    * If `balancingMode` is `CUSTOM_METRICS` and _all_ custom metrics have `dryRun` set to `true`, you get an error. For example: `gceSync: generic::invalid_argument: Update: Invalid value for field 'resource.backends[0]': '...'. CUSTOM_METRICS BalancingMode requires at least one non-dry-run custom metric.` The load balancer needs an active metric to make decisions.
  * **`balancingMode` is `RATE` or other non-custom-metric modes**

    * If load balancing is based on criteria other than custom metrics, such as `RATE` for requests per second, you can set `dryRun: true` for all custom metrics. This lets you monitor custom metrics without affecting the primary balancing mechanism. This is useful for testing new custom metrics before switching your `balancingMode` to `CUSTOM_METRICS`.
  * **Monitoring custom metrics**

    * After you configure your `GCPBackendPolicy` and start sending traffic to your application, it takes some time for the custom metrics, such as `gke.cpu`, to appear in Metrics Explorer.
    * For custom metrics to be visible and active in Metrics Explorer, there must be actual traffic flowing through the backend that the policy monitors. If there is no traffic, the metric might only be visible under "Inactive Resources" in Metrics Explorer.



### Set a custom CPU utilization threshold

By default, GKE distributes traffic away from backends that exceed 80% CPU utilization. However, certain workloads might tolerate higher or lower CPU usage before they require traffic redistribution. You can customize this threshold by using the `maxUtilizationPercent` field in the `GCPBackendPolicy` resource.

  1. To configure a GKE Service so that it allows backends to utilize up to 70% CPU before rebalancing is triggered, save the following sample manifest as `my-backend-policy.yaml`:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
           namespace: team-awesome
         spec:
           targetRef:
             group: ""
             kind: Service
             name: super-service
           default:
             balancingMode: CUSTOM_METRICS
             customMetrics:
             - name: gke.cpu
               maxUtilizationPercent: 70
         

Note the following:

     * The `maxUtilizationPercent` field accepts values from 0 to 100. A value of 100 means that a backend can use its full CPU capacity before traffic is rebalanced.
     * For latency-sensitive workloads that require early offloading, use a lower threshold.
     * For workloads that are designed to run close to full capacity, use a higher threshold.
     * For multi-cluster services, the `spec.targetRef.kind` must be `ServiceImport` and the value of the `group` field must be set to `net.gke.io`.
  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f my-backend-policy.yaml
         




By enabling a custom CPU utilization threshold, you can control traffic distribution based on the backend's CPU utilization.

### (Optional) Enable dry run mode

Dry run mode monitors your Pods resource utilization without changing traffic distribution. When dry run mode is enabled, the metrics are exported to Cloud Monitoring, but Cloud Load Balancing ignores these metrics and uses default load balancing behavior.

  1. To enable dry run mode for your GKE Service, save the following sample manifest as `my-backend-policy.yaml`:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
         spec:
           targetRef:
             group: ""
             kind: Service
             name: store-v1
           default:
             balancingMode: RATE
             maxRatePerEndpoint: 10
             customMetrics:
             - name: gke.cpu
               dryRun: true
         

  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f my-backend-policy.yaml
         




When you enable dry run mode, the following occurs:

  * Cloud Load Balancing ignores CPU utilization metrics and uses default load balancing behavior instead.

  * Metrics continue exporting to Cloud Monitoring under `network.googleapis.com/loadbalancer/backend/lb_custom_metric`.




After you review metrics, remove the `dryRun` field from your `GCPBackendPolicy` and reapply the configuration. If issues occur after you disable the dry run, re-enable it by adding `dryRun: true` back to the policy.

### Verify the policy

To confirm that the `GCPBackendPolicy` is applied to your GKE Service and to verify that the GKE controllers recognize the policy, run the following command:
    
    
    kubectl describe gcpbackendpolicy POLICY_NAME -n NAMESPACE
    

The output is similar to the following:
    
    
    Name:         <your policy name>
    Namespace:    <your namespace>
    Labels:       <none>
    Annotations:  <none>
    API Version:  networking.gke.io/v1
    Kind:         GCPBackendPolicy
    Metadata:
      Creation Timestamp:  ...
      Generation:          1
      Resource Version:    …
      UID:                 …
    Spec:
      Default:
        Balancing Mode:  CUSTOM_METRICS
        Custom Metrics:
          Dry Run:  false
          Name:     gke.cpu
      Target Ref:
        Group:
        Kind:   Service
        Name:   super-service
    Status:
      Conditions:
        Last Transition Time:  …
        Message:
        Reason:                Attached
        Status:                True
        Type:                  Attached
    Events:
    …
    

## Configure utilization-based load balancing by using Compute Engine APIs

We recommend that you use Kubernetes Gateway API to configure utilization-based load balancing for your GKE Services.

However, you might prefer to use Compute Engine APIs or Terraform to manage your load balancers directly. If you choose this approach, you must enable utilization-based load balancing at the BackendService level.

  1. For an existing BackendService, enable utilization-based load balancing and attach a Network Endpoint Group (NEG), my-lb-neg, by running the following command:
         
         gcloud compute backend-services add-backend MY_BACKEND_SERVICE \
           --network-endpoint-group my-lb-neg \
           --network-endpoint-group-zone=asia-southeast1-a \
           --global \
           --balancing-mode=CUSTOM_METRICS \
           --custom-metrics 'name="gke.cpu",maxUtilization=0.8'
         

replace the following:

     * `MY_BACKEND_SERVICE` with the name of your BackendService.
     * `CUSTOM_METRICS` with `CUSTOM_METRICS`.
  2. To update the utilization-based load balancing settings for an existing backend entry on your BackendService where a NEG is already attached, run the following command:
         
         gcloud compute backend-services update-backend MY_BACKEND_SERVICE \
           --network-endpoint-group my-lb-neg \
           --network-endpoint-group-zone=asia-southeast1-a \
           --global \
           --balancing-mode=CUSTOM_METRICS \
           --custom-metrics 'name="gke.cpu",maxUtilization=0.8'
         

replace the following:

     * `MY_BACKEND_SERVICE` with the name of your BackendService.
     * `CUSTOM_METRICS` with `CUSTOM_METRICS`.

**Note:** If you use custom metrics, keep the number of configured dimensions below the service limit. If you exceed the limit, you won't be able to add more dimensions.

## Disable utilization-based load balancing for a GKE Service

To disable utilization-based load balancing on your GKE Services, perform the following steps:

  1. If you want to keep the policy for other settings, remove the `balancingMode` and `customMetrics` fields from your `GCPBackendPolicy`.
  2. If you no longer need `GCPBackendPolicy`, you can delete it.
  3. If you use Compute Engine APIs, change back the `--balancing-mode` and `--custom-metrics` flags from your backend service.



## What's next

  * To use custom metrics for load balancing, see [Expose custom metrics for load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics).
  * [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
