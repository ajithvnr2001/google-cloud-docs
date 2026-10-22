---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling/
title: Configuring horizontal Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:26.933018+00:00
---

# Configuring horizontal Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configuring horizontal Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to scale your deployments in Google Kubernetes Engine (GKE) by automatically adjusting your resources using metrics like resource allocation, load balancer traffic, custom metrics, or multiple metrics simultaneously. This page also provides step-by-step instructions for configuring a [HorizontalPodAutoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) profile, including how to view, delete, clean, and troubleshoot your HPA object. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

This page is for Developers and Operators who manage application scaling in GKE and want to understand how to dynamically optimize performance and maintain cost efficiency through horizontal Pod autoscaling. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### API versions for HorizontalPodAutoscaler objects

When you use the Google Cloud console, HPA objects are created using the `autoscaling/v2` API. The `autoscaling/v1` API is still supported, but is no longer recommended, and does not support certain features such as scaling to and from zero using HPA.

### Create the example Deployment

Before you can create an HPA object you must create the workload it monitors. The examples in this page apply different HPA configurations to the following `nginx` Deployment. Separate examples show an HPA based on resource utilization, based on a [custom or external metric](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics), and based on multiple metrics.

Save the following to a file named `nginx.yaml`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.7.9
            ports:
            - containerPort: 80
            resources:
              # You must specify requests for CPU to autoscale
              # based on CPU utilization
              requests:
                cpu: "250m"
    

This manifest specifies a value for CPU requests. If you want to autoscale based on a resource's utilization as a percentage, you must specify requests for that resource. If you don't specify requests, you can autoscale based only on the absolute value of the resource's utilization, such as milliCPUs for CPU utilization.

To create the Deployment, apply the `nginx.yaml` manifest:
    
    
    kubectl apply -f nginx.yaml
    

The Deployment has `spec.replicas` set to 3, so three Pods are deployed. You can verify this using the `kubectl get deployment nginx` command.

Each of the examples in this page applies a different HPA object to an example nginx Deployment.

## Autoscaling based on resources utilization

This example creates an HPA object to autoscale the `nginx` Deployment when CPU utilization surpasses 50%, and helps ensure that there is always a minimum of 1 replica and a maximum of 10 replicas.

You can create an HPA that targets CPU using the Google Cloud console, the `kubectl apply` command, or for average CPU only, the `kubectl autoscale` command.

**Note:** This example uses `apiVersion: autoscaling/v1`. For more information about the available APIs, see API versions for HPA objects.

### Console

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click the name of the `nginx` Deployment.

  3. Click _list_ **Actions > Edit autoscaling**.

  4. Under the _Horizontal Pod Autoscaling section_ , click **Select and configure**.

  5. Specify the following values:

     * **Minimum number of replicas:** 1
     * **Maximum number of replicas:** 10
     * **Autoscaling metric:** CPU
     * **Target:** 50
     * **Unit:** CPUs
  6. Click **Submit**.




### `kubectl apply`

Save the following YAML manifest as a file named `nginx-hpa.yaml`:
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx
      # Set the minimum and maximum number of replicas the Deployment can scale to.
      minReplicas: 1
      maxReplicas: 10
      metrics:
      - type: Resource
        resource:
          # The target average CPU utilization percentage across all Pods.
          name: cpu
          target:
            type: Utilization
            averageUtilization: 50
    
    

If you create a manifest to match specific details in your own project, then ensure that you don't include sensitive data in the horizontal Pod autoscaler fields.

To create the HPA, apply the manifest using the following command:
    
    
    kubectl apply -f nginx-hpa.yaml
    

### `kubectl autoscale`

To create an HPA object that only targets average CPU utilization, you can use the [`kubectl autoscale`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale) command:
    
    
    kubectl autoscale deployment nginx --cpu-percent=50 --min=1 --max=10
    

**Note:** You can combine the `--dry-run` and `-o yaml` flags to print a YAML manifest for an HPA without actually creating it.

To get a list of HPAs in the cluster, use the following command:
    
    
    kubectl get hpa
    

The output is similar to the following:
    
    
    NAME    REFERENCE          TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
    nginx   Deployment/nginx   0%/50%    1         10        3          61s
    

To get details about HPA, you can use the Google Cloud console or the `kubectl` command.

### Console

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click the name of the `nginx` Deployment.

  3. Click the **Scaling** tab.




### `kubectl get`

To get details about HPA, you can use `kubectl get hpa` with the `-o yaml` flag. The `status` field contains information about the current number of replicas and any recent autoscaling events.
    
    
    kubectl get hpa nginx -o yaml
    

The output is similar to the following:
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"autoscaling/v2","kind":"HorizontalPodAutoscaler","metadata":{"annotations":{},"name":"nginx","namespace":"default"},"spec":{"maxReplicas":10,"metrics":[{"resource":{"name":"cpu","target":{"averageUtilization":50,"type":"Utilization"}},"type":"Resource"}],"minReplicas":1,"scaleTargetRef":{"apiVersion":"apps/v1","kind":"Deployment","name":"nginx"}}}
      creationTimestamp: "2025-10-30T19:42:43Z"
      name: nginx
      namespace: default
      resourceVersion: "220050"
      selfLink: /apis/autoscaling/v2/namespaces/default/horizontalpodautoscalers/nginx
      uid: 70d1067d-fb4d-11e9-8b2a-42010a8e013f
    spec:
      maxReplicas: 10
      minReplicas: 1
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx
      metrics:
      - type: Resource
        resource:
          name: cpu
          target:
            type: Utilization
            averageUtilization: 50
    status:
      conditions:
      - lastTransitionTime: "2025-10-30T19:42:59Z"
        message: recent recommendations were higher than current one, applying the highest recent recommendation
        reason: ScaleDownStabilized
        status: "True"
        type: AbleToScale
      - lastTransitionTime: "2025-10-30T19:42:59Z"
        message: the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
        reason: ValidMetricFound
        status: "True"
        type: ScalingActive
      - lastTransitionTime: "2025-10-30T19:42:59Z"
        message: the desired count is within the acceptable range
        reason: DesiredWithinRange
        status: "False"
        type: ScalingLimited
      currentMetrics:
      - type: Resource
        resource:
          name: cpu
          current:
            averageUtilization: 0
            averageValue: "0"
      currentReplicas: 3
      desiredReplicas: 3
    
    

If you create a manifest to match specific details in your own project, then ensure that you don't include sensitive data in the horizontal Pod autoscaler fields.

Before following the remaining examples in this page, delete the HPA:
    
    
    kubectl delete hpa nginx
    

When you delete an HPA object, the number of replicas of the Deployment remain the same. A Deployment does not automatically revert back to its state before HPA was applied.

You can learn more about deleting an HPA.

## Autoscaling based on a custom or external metric

Any metric that your workload emits, or that you can query from an external source, [can be used for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics). GKE has built-in support for autoscaling based on custom metrics and external metrics in many situations, and Kubernetes supports additional metrics adapters such as KEDA and the Prometheus adapter.

## Autoscaling based on load balancer traffic

Traffic-based autoscaling is a capability of GKE that integrates traffic utilization signals from load balancers to autoscale Pods.

Using traffic as an autoscaling signal might be helpful since it is a leading indicator of load that is complementary to CPU and memory. Built-in integration with GKE helps ensure that the setup is straightforward and that autoscaling reacts to traffic spikes quickly to meet demand.

Traffic-based autoscaling is enabled by the [Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) and its [global traffic management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management) capabilities. To learn more, see [Traffic-based autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#traffic-based_autoscaling).

Autoscaling based on load balancer traffic is only available for [Gateway workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).

#### Requirements

Traffic-based autoscaling has the following requirements:

  * Supported on GKE versions 1.31 and later.
  * Gateway API enabled in your project.
  * Supported for traffic that goes through load balancers deployed using the Gateway API and either the `gke-l7-global-external-managed`, `gke-l7-regional-external-managed`, `gke-l7-rilb`, or the `gke-l7-gxlb` GatewayClass.



#### Limitations

Traffic-based autoscaling has the following limitations:

  * Not supported by the multi-cluster GatewayClasses (`gke-l7-global-external-managed-mc`, `gke-l7-regional-external-managed-mc`, `gke-l7-rilb-mc`, and `gke-l7-gxlb-mc`).
  * Not supported for traffic using Services of type `LoadBalancer`.
  * There must be a clear and isolated relationship between the components involved in traffic-based autoscaling. One HPA object must be dedicated to scaling a single Deployment (or any scalable resource) exposed by a single Service.
  * After configuring the capacity of your Service using the `maxRatePerEndpoint` field, allow sufficient time (usually one minute, but potentially up to 15 minutes in large clusters) for the load balancer to be updated with this change, before configuring HPA with traffic-based metrics. This approach helps ensure that your service won't temporarily experience a situation where your cluster tries to autoscale based on metrics emitted by a load balancer still undergoing configuration.
  * If traffic-based autoscaling is used on a Service served by multiple load balancers (for example -- by both an Ingress and a Gateway, or by two Gateways), HPA might consider the highest traffic value from individual load balancers to make scaling decisions, rather than the sum of traffic values from all load balancers.



#### Deploy traffic-based autoscaling

The following exercise uses HPA to autoscale the `store-autoscale` Deployment based on the traffic it receives. A [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) accepts ingress traffic from the internet for the Pods. The autoscaler compares traffic signals from the Gateway with the [per-Pod traffic capacity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#service_capacity) that is configured on the `store-autoscale` Service resource. By generating traffic to the Gateway, you influence the number of Pods deployed.

The following diagram demonstrates how traffic-based autoscaling works:

![HorizontalPodAutoscaler scaling a Deployment based on traffic.](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-autoscale-1.svg)

To deploy traffic-based autoscaling, perform the following steps:

  1. For Standard clusters, confirm that the GatewayClasses are installed in your cluster. For Autopilot clusters, the GatewayClasses are installed by default.
         
         kubectl get gatewayclass
         

The output confirms that the GKE GatewayClass resources are ready to use in your cluster:
         
         NAME                               CONTROLLER                  ACCEPTED   AGE
         gke-l7-global-external-managed     networking.gke.io/gateway   True       16h
         gke-l7-regional-external-managed   networking.gke.io/gateway   True       16h
         gke-l7-gxlb                        networking.gke.io/gateway   True       16h
         gke-l7-rilb                        networking.gke.io/gateway   True       16h
         

If you don't see this output, [enable the Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway) in your GKE cluster.

  2. Deploy the sample application and Gateway load balancer to your cluster:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/master/gateway/docs/store-autoscale.yaml
         

The sample application creates:

     * A Deployment with 2 replicas.
     * A Service with an associated `GCPBackendPolicy` setting `maxRatePerEndpoint` set to `10`. To learn more about Gateway capabilities, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).
     * An external Gateway for accessing the application on the internet. To learn more about how to use Gateway load balancers, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
     * An HTTPRoute that matches all traffic and sends it to the `store-autoscale` Service.

The [Service capacity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#service_capacity) is a critical element when using traffic-based autoscaling because it determines the amount of per-Pod traffic that triggers an autoscaling event. It is configured using a `maxRatePerEndpoint` field on a [GCPBackendPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#policy) associated with the Service, which defines the maximum traffic a Service should receive in requests per second, per Pod. Service capacity is specific to your application.

For more information, see [Determining your Service's capacity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#capacity).

  3. Save the following manifest as `hpa.yaml`:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: store-autoscale
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: store-autoscale
           # Set the minimum and maximum number of replicas the Deployment can scale to.
           minReplicas: 1
           maxReplicas: 10
           # This section defines that scaling should be based on the fullness of load balancer
           # capacity, using the following configuration.
           metrics:
           - type: Object
             object:
               describedObject:
                 kind: Service
                 name: store-autoscale
               metric:
                 # The name of the custom metric which measures how "full" a backend is
                 # relative to its configured capacity.
                 name: "autoscaling.googleapis.com|gclb-capacity-fullness"
               target:
                 # The target average value for the metric. The autoscaler adjusts the number
                 # of replicas to maintain an average capacity fullness of 70% across all Pods.
                 averageValue: 70
                 type: AverageValue
         

**Note:** An earlier version of this product used the metric name `autoscaling.googleapis.com|gclb-capacity-utilization`. We recommend that you switch to the `autoscaling.googleapis.com|gclb-capacity-fullness` metric name instead.

This manifest describes an HPA object with the following properties:

     * `minReplicas` and `maxReplicas`: sets the minimum and maximum number of replicas for this Deployment. In this configuration, the number of Pods can scale from `1` to `10` replicas (or from `0` replicas if you configure scaling to and from zero using HPA).
     * `describedObject.name: store-autoscale`: the reference to the `store-autoscale` Service that defines the traffic capacity.
     * `scaleTargetRef.name: store-autoscale`: the reference to the `store-autoscale` Deployment that defines the resource that is scaled by HPA.
     * `averageValue: 70`: target average value of 70% capacity utilization. This gives HPA a growth margin so that the running Pods can process excess traffic while new Pods are being created.

If you create a manifest to match specific details in your own project, then ensure that you don't include sensitive data in the horizontal Pod autoscaler fields.

**Note:** A Deployment or a Service cannot be referenced by more than one HPA. If this condition is not met, HPA stops autoscaling and errors appear in HPA events.



HPA results in the following traffic behavior:

  * The number of Pods is adjusted between 1 and 10 replicas to achieve 70% of the max rate per endpoint. This results in 7 RPS per Pod when `maxRatePerEndpoint=10`.
  * At more than 7 RPS per pod, Pods are scaled up until they've reached their maximum of 10 replicas or until the average traffic is 7 RPS per Pod.
  * If traffic is reduced, Pods scale down to a reasonable rate using the HPA algorithm.



You can also [deploy a traffic generator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#verify_traffic_using_load_testing) to validate traffic-based autoscaling behavior.

At 30 RPS, the Deployment is scaled to 5 replicas so that each replica ideally receives 6 RPS of traffic, which would be 60% utilization per Pod. This is under the 70% target utilization and so the Pods are scaled appropriately. Depending on traffic fluctuations, the number of autoscaled replicas might also fluctuate. For a more detailed description of how the number of replicas is computed, see [Autoscaling behavior](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#autoscaling-behavior).

## Autoscaling based on multiple metrics

This example creates an HPA object that autoscales based on CPU utilization and a custom metric named `packets_per_second`.

If you followed the previous example and still have an HPA object named `nginx`, delete it before following this example.

This example requires `apiVersion: autoscaling/v2`. For more information about the available APIs, see API versions for HPA objects.

Before you can autoscale based on a custom metric, you must create the custom metric and configure your workload to export the metric to Cloud Monitoring. For this reason, the `packets_per_second` metric in the manifest below is included for illustration, but commented out. For more information, see Monitoring documentation for [creating custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics).

Save this YAML manifest as a file named `nginx-multiple.yaml`:
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx
      minReplicas: 1
      maxReplicas: 10
      metrics: # The metrics to base the autoscaling on.
      - type: Resource
        resource:
          name: cpu # Scale based on CPU utilization.
          target:
            type: Utilization
            averageUtilization: 50
            # The HPA will scale the replicas to try and maintain an average
            # CPU utilization of 50% across all Pods.
      - type: Resource
        resource:
          name: memory # Scale based on memory usage.
          target:
            type: AverageValue
            averageValue: 100Mi
            # The HPA will scale the replicas to try and maintain an average
            # memory usage of 100 Mebibytes (MiB) across all Pods.
      # Uncomment these lines if you create the custom packets_per_second metric and
      # configure your app to export the metric.
      # - type: Pods
      #   pods:
      #     metric:
      #       name: packets_per_second
      #     target:
      #       type: AverageValue
      #       averageValue: 100
    

If you create a manifest to match specific details in your own project, then ensure that you don't include sensitive data in the horizontal Pod autoscaler fields.

Apply the YAML manifest:
    
    
    kubectl apply -f nginx-multiple.yaml
    

When created, HPA monitors the `nginx` Deployment for average CPU utilization, average memory utilization, and (if you uncommented it) the custom `packets_per_second` metric. HPA autoscales the Deployment based on the metric whose value would create the larger autoscale event.

## Scale to and from zero

Starting in GKE version 1.37, you can configure the HPA to scale a Deployment down to zero (`0`) replicas when there is no workload demand, and automatically scale it back up when demand increases. When scaling up from zero, GKE [bypasses standard metric tolerance checks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#scaling-to-and-from-zero) to activate Pods without delay.

To configure scaling to and from zero using HPA, you must do the following:

  1. Ensure your cluster runs GKE version 1.37 or later.
  2. Configure at least one custom or external metric by using the [AutoscalingMetric](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-autoscaling) resource.
  3. Set the `minReplicas: 0` field-value pair in an HPA manifest that uses the `autoscaling/v2` API.



For step-by-step instructions, see [Scale GKE workloads to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa).

## Configure the Performance HPA profile

The Performance HPA profile improves the reaction time of horizontal Pod autoscaling, helping to improve the HPA's ability to handle a large number of objects (up to 1,000 objects in minor versions 1.31-1.32 and 5,000 objects in version 1.33 or later).

This profile is automatically enabled on qualifying Autopilot clusters with a control plane running GKE version 1.32 or later. For Standard clusters, the profile is automatically enabled on qualifying clusters with a control plane running GKE version 1.33 or later.

A Standard cluster is exempt from auto-enablement of the Performance HPA profile if it meets all of the following conditions:

  * The cluster is upgrading from an earlier version to version 1.33 or later.
  * The cluster has at least one node pool with any of the following machine types: `e2-micro`, `e2-custom-micro`, `g1-small`, `f1-micro`.
  * Node auto-provisioning is not enabled.



You can also enable the Performance HPA profile on existing clusters if they meet the requirements.

#### Requirements

To enable the Performance HPA profile, verify that your Autopilot and Standard clusters meet the following requirements:

  * Your control plane is running GKE version 1.31 or later.
  * If your control plane is running GKE version 1.31, enable [system metric collection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics).
  * The [Autoscaling API](https://console.cloud.google.com/marketplace/product/google/autoscaling.googleapis.com) is enabled in your project.
  * All [node Service Accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#minimum_permissions) have the [`roles/autoscaling.metricsWriter`](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.metricsWriter) role assigned.
  * If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), verify that the [Autoscaling API](https://console.cloud.google.com/marketplace/product/google/autoscaling.googleapis.com) is included in your service perimeter.



#### Enable the Performance HPA profile

To enable the Performance HPA profile in your cluster, use the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--hpa-profile =performance**
    

Replace:

  * `CLUSTER_NAME`: The name of the cluster.
  * `LOCATION`: Compute zone or region (e.g. us-central1-a or us-central1) for the cluster.
  * `PROJECT_ID`: Your Google Cloud project ID.

**Note:** The Performance HPA profile enhances monitoring by increasing the `gke-metrics-agent` resource requests, and triggers a simultaneous restart of its Pods. This may cause temporary disruption on resource-constrained nodes due to Pod rescheduling.

#### Disable the Performance HPA profile

To disable Performance HPA profile in a cluster, use the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--hpa-profile =none**
    

Replace:

  * `CLUSTER_NAME`: The name of the cluster.
  * `LOCATION`: Compute zone or region (e.g. us-central1-a or us-central1) for the cluster.
  * `PROJECT_ID`: Your Google Cloud project ID.



## Viewing details about a HorizontalPodAutoscaler

To view an HPA's configuration and statistics, use the following command:
    
    
    kubectl describe hpa HPA_NAME
    

Replace `HPA_NAME` with the name of your HPA object.

Each HPA object's current status is shown in `Conditions` field, and autoscaling events are listed in the `Events` field.

**Note:** If you've enabled the Performance HPA profile, `Events: Reason` is listed as `HpaProfilePerformance`.

The output is similar to the following:
    
    
    Name:                                                  nginx
    Namespace:                                             default
    Labels:                                                <none>
    Annotations:                                           kubectl.kubernetes.io/last-applied-configuration:
                                                             {"apiVersion":"autoscaling/v2","kind":"HorizontalPodAutoscaler","metadata":{"annotations":{},"name":"nginx","namespace":"default"},"s...
    CreationTimestamp:                                     Tue, 05 May 2020 20:07:11 +0000
    Reference:                                             Deployment/nginx
    Metrics:                                               ( current / target )
      resource memory on pods:                             2220032 / 100Mi
      resource cpu on pods  (as a percentage of request):  0% (0) / 50%
    Min replicas:                                          1
    Max replicas:                                          10
    Deployment pods:                                       1 current / 1 desired
    Conditions:
      Type            Status  Reason              Message
      ----            ------  ------              -------
      AbleToScale     True    ReadyForNewScale    recommended size matches current size
      ScalingActive   True    ValidMetricFound    the HPA was able to successfully calculate a replica count from memory resource
      ScalingLimited  False   DesiredWithinRange  the desired count is within the acceptable range
    Events:                                                <none>
    

## Deleting a HorizontalPodAutoscaler

You can delete an HPA object by using the Google Cloud console or the `kubectl delete` command.

### Console

To delete the `nginx` HPA object:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click the name of the `nginx` Deployment.

  3. Click _list_ **Actions > Autoscale**.

  4. Click **Delete**.




### `kubectl delete`

To delete the `nginx` HPA object, use the following command:
    
    
    kubectl delete hpa nginx
    

When you delete an HPA object, the Deployment or (or other deployment object) remains at its existing scale, and does not revert back to the number of replicas in the Deployment's original manifest. To manually scale the Deployment back to three Pods, you can use the `kubectl scale` command:
    
    
    kubectl scale deployment nginx --replicas=3
    

## Cleaning up

  1. Delete the HPA object, if you have not done so:
         
         kubectl delete hpa nginx
         

  2. Delete the `nginx` Deployment:
         
         kubectl delete deployment nginx
         

  3. Optionally, [delete the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).




## Troubleshooting

For advice on troubleshooting, see [Troubleshoot horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling).

## What's next

  * Learn more about [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).
  * Learn how to [rightsize HPA workloads with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa).
  * Learn more about [Vertical Pod Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling).
  * Learn more about [CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
