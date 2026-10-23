---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-elastic-cross-region-high-availability/
title: Configure elastic cross-region high availability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:05.637467+00:00
---

# Configure elastic cross-region high availability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-elastic-cross-region-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure elastic cross-region high availability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to configure elastic cross-region high availability for AI inference workloads by using Google Kubernetes Engine (GKE) Multi-Cluster Inference Gateway and the GKE Autoscaling feature. This setup lets you intelligently load balance workloads across multiple GKE clusters in different regions.

For more information about GKE Multi-Cluster Inference Gateway, see [About GKE Multi-Cluster Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway).

## Before you begin

  1. Enable the Google Kubernetes Engine API.

[Enable Google Kubernetes Engine API](https://console.cloud.google.com/apis/library/container.googleapis.com?q=kubernetes%20engine)

  2. Install and initialize the Google Cloud CLI if you plan to use it for this task.

**Note:** If you have an existing gcloud CLI installation, ensure a default region or zone is configured using `gcloud config set compute/region` or `gcloud config set compute/zone` to avoid location-related errors. You might still need to specify the location in commands if it differs from the default. For more information, see [gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties).
  3. Ensure your project has sufficient quota for H100 GPUs. For more information, see [GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [resource allocation](https://docs.cloud.google.com/compute/resource-usage).

  4. Use GKE version 1.34.1-gke.1127000 or later.

  5. Use gcloud CLI version 480.0.0 or later.

  6. Make sure that the service account used by your nodes has the `roles/monitoring.metricWriter` and `roles/stackdriver.resourceMetadata.writer` permissions.

  7. Make sure that you have the `roles/container.admin` and `roles/iam.serviceAccountAdmin` Identity and Access Management (IAM) roles on the project.

  8. Complete the following Hugging Face prerequisites:

     1. Create a [Hugging Face](https://huggingface.co/) account.
     2. Request and get approval for access to the Llama 3.1 model on Hugging Face.
     3. Sign the license consent agreement on the model's page on Hugging Face.
     4. Generate a Hugging Face access token with at least Read permissions.



## Create clusters and node pools

To create two GKE clusters in different regions and configure their node pools, follow these steps:

  1. Create the first cluster:
         
         gcloud container clusters create gke-west --zone \
             CLUSTER_1_ZONE \
             --project=PROJECT_ID \
             --gateway-api=standard \
             --cluster-version=GKE_VERSION \
             --machine-type="MACHINE_TYPE" \
             --disk-type="DISK_TYPE" \
             --enable-managed-prometheus --monitoring=SYSTEM,DCGM \
             --hpa-profile=performance \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --async
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_ZONE`: the zone for the first cluster, for example `europe-west3-c`
     * `GKE_VERSION`: the GKE version to use, for example `1.34.1-gke.1127000`
     * `MACHINE_TYPE`: the machine type for the cluster nodes, for example `c2-standard-16`
     * `DISK_TYPE`: the disk type for the cluster nodes, for example `pd-standard`
**Note:** The `--async` flag lets the command return immediately, which creates the cluster in the background. The `get-credentials` command will wait for the cluster to be fully provisioned.**Note:** This example uses zonal clusters, but you can also use regional clusters.
  2. Create an H100 node pool in the first cluster:
         
         gcloud container node-pools create h100 \
             --accelerator "type=nvidia-h100-80gb,count=2,gpu-driver-version=latest" \
             --project=PROJECT_ID \
             --location=CLUSTER_1_ZONE \
             --node-locations=CLUSTER_1_ZONE \
             --cluster=CLUSTER_1_NAME \
             --machine-type=NODE_POOL_MACHINE_TYPE \
             --num-nodes=NUM_NODES \
             --spot \
             --min-nodes=MIN_NUM_NODES \
             --max-nodes=MAX_NUM_NODES \
             --enable-autoscaling \
             --async
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_ZONE`: the zone for the first cluster, for example `europe-west3-c`
     * `CLUSTER_1_NAME`: the name of the first cluster, for example `gke-west`
     * `NODE_POOL_MACHINE_TYPE`: the machine type for the node pool, for example `a3-highgpu-2g`
     * `NUM_NODES`: the number of nodes in the node pool, for example `3`
     * `MIN_NUM_NODES`: the minimum number of nodes for autoscaling in the node pool, for example `1`
     * `MAX_NUM_NODES`: the maximum number of nodes for autoscaling in the node pool, for example `10`
**Note:** The `--spot` flag configures the node pool to use Spot VMs. Spot VMs are cost-effective but can be preempted, which is often acceptable for AI/ML inference workloads.
  3. Get credentials and create a Hugging Face token secret in the first cluster:
         
         gcloud container clusters get-credentials CLUSTER_1_NAME \
             --location CLUSTER_1_ZONE \
             --project=PROJECT_ID
         
         kubectl create secret generic hf-token \
             --from-literal=token=HF_TOKEN
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_NAME`: the name of the first cluster, for example `gke-west`
     * `CLUSTER_1_ZONE`: the zone for the first cluster, for example `europe-west3-c`
     * `HF_TOKEN`: your Hugging Face access token
  4. Create the second cluster in a different region from the first cluster:
         
         gcloud container clusters create gke-east --zone CLUSTER_2_ZONE \
             --project=PROJECT_ID \
             --gateway-api=standard \
             --cluster-version=GKE_VERSION \
             --machine-type="MACHINE_TYPE" \
             --disk-type="DISK_TYPE" \
             --enable-managed-prometheus \
             --monitoring=SYSTEM,DCGM \
             --hpa-profile=performance \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --async
         

Replace `CLUSTER_2_ZONE` with the zone for the second cluster, for example `us-east4-a`.

  5. Create an H100 node pool for the second cluster:
         
         gcloud container node-pools create h100 \
             --accelerator "type=nvidia-h100-80gb,count=2,gpu-driver-version=latest" \
             --project=PROJECT_ID \
             --location=CLUSTER_2_ZONE \
             --node-locations=CLUSTER_2_ZONE \
             --cluster=CLUSTER_2_NAME \
             --machine-type=NODE_POOL_MACHINE_TYPE \
             --num-nodes=NUM_NODES \
             --spot \
             --min-nodes=MIN_NUM_NODES \
             --max-nodes=MAX_NUM_NODES \
             --enable-autoscaling \
             --async
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_2_ZONE`: the zone for the second cluster, for example `us-east4-a`
     * `CLUSTER_2_NAME`: the name of the second cluster, for example `gke-east`
     * `NODE_POOL_MACHINE_TYPE`: the machine type for the node pool, for example `a3-highgpu-2g`
     * `NUM_NODES`: the number of nodes in the node pool, for example `3`
     * `MIN_NUM_NODES`: the minimum number of nodes for autoscaling in the node pool, for example `1`
     * `MAX_NUM_NODES`: the maximum number of nodes for autoscaling in the node pool, for example `10`
  6. Get credentials and create a secret for the Hugging Face token on the second cluster:
         
         gcloud container clusters get-credentials CLUSTER_2_NAME \
             --location CLUSTER_2_ZONE \
             --project=PROJECT_ID
         kubectl create secret generic hf-token --from-literal=token=HF_TOKEN
         

Replace the following. For definitions of other variables, refer to previous steps:

     * `HF_TOKEN`: your Hugging Face access token



## Register clusters to a fleet

  1. Register your clusters to your project's fleet:
         
         gcloud container fleet memberships register CLUSTER_1_NAME \
             --gke-cluster CLUSTER_1_ZONE/CLUSTER_1_NAME \
             --location=global \
             --project=PROJECT_ID
         
         gcloud container fleet memberships register CLUSTER_2_NAME \
             --gke-cluster CLUSTER_2_ZONE/CLUSTER_2_NAME \
             --location=global \
             --project=PROJECT_ID
         

Replace the following, and refer to previous steps for definitions of other variables:

     * `CLUSTER_1_NAME`: the name of the first cluster, for example `gke-west`
     * `CLUSTER_2_NAME`: the name of the second cluster, for example `gke-east`
  2. Enable the Multi=Cluster Ingress feature and designate a configuration cluster:
         
         gcloud container fleet ingress enable \
             --config-membership=projects/PROJECT_ID/locations/global/memberships/CLUSTER_1_NAME
         

Replace the following. For definitions of other variables, refer to previous steps:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_NAME`: the name of the first cluster, for example `gke-west`



## Create proxy-only subnets

**Warning:** Google Cloud lets each VPC network have only one proxy-only subnet per region. If the target region already contains a proxy-only subnet with `purpose=REGIONAL_MANAGED_PROXY` setting, creating the `GLOBAL_MANAGED_PROXY` subnet fails. You must delete the existing regional proxy-only subnet first. Deleting a regional proxy-only subnet affects any regional Envoy-based load balancers in that region that use it, so plan the change accordingly.

  1. Create a subnet in the first cluster's region:
         
         gcloud compute networks subnets create CLUSTER_1_REGION-subnet \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=CLUSTER_1_REGION \
             --network=default \
             --range=SUBNET_RANGE_1 \
             --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_REGION`: the region for the first cluster, for example `europe-west3`
     * `SUBNET_RANGE_1`: the subnet IP range for the proxy-only subnet in the first cluster's region, for example `10.0.0.0/23`
  2. Create a subnet in the second cluster's region:
         
         gcloud compute networks subnets create CLUSTER_2_REGION-subnet \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=CLUSTER_2_REGION \
             --network=default \
             --range=SUBNET_RANGE_2 \
             --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_2_REGION`: the region for the second cluster, for example `us-east4`
     * `SUBNET_RANGE_2`: the subnet IP range for the proxy-only subnet in the second cluster's region, for example `10.5.0.0/23`



## Install the required custom resources

  1. Define context variables for your clusters:
         
         CLUSTER1_CONTEXT="gke_PROJECT_ID_CLUSTER_1_ZONE_CLUSTER_1_NAME"
         CLUSTER2_CONTEXT="gke_PROJECT_ID_CLUSTER_2_ZONE_CLUSTER_2_NAME"
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_1_ZONE`: the zone for the first cluster, for example `europe-west3-c`
     * `CLUSTER_1_NAME`: the name of the first cluster, for example `gke-west`
     * `CLUSTER_2_ZONE`: the zone for the second cluster, for example `us-east4-a`
     * `CLUSTER_2_NAME`: the name of the second cluster, for example `gke-east`
  2. Install the InferencePool and InferenceObjective custom resource on both clusters:
         
         kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v1.0.1/manifests.yaml --context=$CLUSTER1_CONTEXT
         
         kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v1.0.1/manifests.yaml --context=$CLUSTER2_CONTEXT
         




## Deploy resources to the target clusters

  1. Deploy the model servers to both clusters:
         
         kubectl apply -f \
         https://raw.githubusercontent.com/kubernetes-sigs/gateway-api-inference-extension/release-1.0/config/manifests/vllm/gpu-deployment.yaml \
         --context=$CLUSTER1_CONTEXT
         
         kubectl apply -f \
         https://raw.githubusercontent.com/kubernetes-sigs/gateway-api-inference-extension/release-1.0/config/manifests/vllm/gpu-deployment.yaml \
         --context=$CLUSTER2_CONTEXT
         

  2. Save the following manifest to a file named `inference-objective.yaml`:
         
         apiVersion: inference.networking.x-k8s.io/v1alpha2
         kind: InferenceObjective
         metadata:
           name: food-review
         spec:
           priority: 10
           poolRef:
             name: llama3-8b-instruct
             group: "inference.networking.k8s.io"
         

  3. Apply the manifest to both clusters:
         
         kubectl apply -f inference-objective.yaml --context=$CLUSTER1_CONTEXT
         kubectl apply -f inference-objective.yaml --context=$CLUSTER2_CONTEXT
         

  4. Deploy the InferencePool resources to both clusters using Helm:
         
         helm install vllm-llama3-8b-instruct \
           --kube-context $CLUSTER1_CONTEXT \
           --set inferencePool.modelServers.matchLabels.app=vllm-llama3-8b-instruct \
           --set provider.name=gke \
           --set inferenceExtension.monitoring.gke.enabled=true \
           --version v1.0.1 \
           oci://registry.k8s.io/gateway-api-inference-extension/charts/inferencepool
         
         helm install vllm-llama3-8b-instruct \
           --kube-context $CLUSTER2_CONTEXT \
           --set inferencePool.modelServers.matchLabels.app=vllm-llama3-8b-instruct \
           --set provider.name=gke \
           --set inferenceExtension.monitoring.gke.enabled=true \
           --version v1.0.1 \
           oci://registry.k8s.io/gateway-api-inference-extension/charts/inferencepool
         

  5. In both clusters, mark the `InferencePool` resources as exported in both clusters:
         
         kubectl annotate inferencepool vllm-llama3-8b-instruct networking.gke.io/export="True" \
             --context=$CLUSTER1_CONTEXT
         
         kubectl annotate inferencepool vllm-llama3-8b-instruct networking.gke.io/export="True" \
             --context=$CLUSTER2_CONTEXT
         




## Deploy the cross-region Inference Gateway

  1. Save the following manifest as `mygateway.yaml`:
         
         ---
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: cross-region-gateway
           namespace: default
         spec:
           gatewayClassName: gke-l7-cross-regional-internal-managed-mc
           addresses:
           -   type: networking.gke.io/ephemeral-ipv4-address/europe-west3
             value: "europe-west3"
           -   type: networking.gke.io/ephemeral-ipv4-address/us-east4
             value: "us-east4"
           listeners:
           -   name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               kinds:
               -   kind: HTTPRoute
               namespaces:
                 from: All
         ---
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: HTTPRoute
         metadata:
           name: vllm-llama3-8b-instruct-default
         spec:
           parentRefs:
           -   name: cross-region-gateway
             kind: Gateway
           rules:
           -   backendRefs:
             -   group: networking.gke.io
               kind: GCPInferencePoolImport
               name: vllm-llama3-8b-instruct
         ---
         kind: HealthCheckPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: health-check-policy
           namespace: default
         spec:
           targetRef:
             group: "networking.gke.io"
             kind: GCPInferencePoolImport
             name: vllm-llama3-8b-instruct
           default:
             config:
               type: HTTP
               httpHealthCheck:
                   requestPath: /health
                   port: 8000
         

  2. Apply the manifest to the config cluster:
         
         kubectl apply -f mygateway.yaml --context=CLUSTER1_CONTEXT
         

Replace the following:

     * `CLUSTER1_CONTEXT`: the context for the first cluster, for example `gke_my-project_europe-west3-c_gke-west`



## Enable custom metrics reporting

  1. Create a file named `metrics.yaml` with the following content:
         
         apiVersion: autoscaling.gke.io/v1beta1
         kind: AutoscalingMetric
         metadata:
           name: gpu-cache
           namespace: default
         spec:
           selector:
             matchLabels:
               app: vllm-llama3-8b-instruct
           endpoints:
           -   port: 8000
             path: /metrics
             metrics:
             -   name: vllm:kv_cache_usage_perc
               exportName: kv-cache
             -   name: vllm:gpu_cache_usage_perc
               exportName: kv-cache-old
         

  2. For each cluster, apply the metrics configuration:
         
         kubectl apply -f metrics.yaml --context=CLUSTER1_CONTEXT
         kubectl apply -f metrics.yaml --context=CLUSTER2_CONTEXT
         

For definitions of `CLUSTER1_CONTEXT` and `CLUSTER2_CONTEXT`, see Install the required custom resources.




## Configure the load balancing policy

This section describes how to configure the load balancing policy. This policy defines how traffic is distributed across your inference pools based on custom metrics and regional preferences. The following configuration sets `us-east4` as the preferred region. Traffic spills over to other regions only when the `gke.named_metrics.kv-cache` custom Metric in the `us-east4` region reaches 80% utilization.

**Note:** When using the `CUSTOM_METRICS` balancing mode, note the following:

  * For vLLM versions v0.10.2 and newer, use the `gke.named_metrics.kv-cache` metric.
  * For earlier versions, use the `gke.named_metrics.kv-cache-old` metric.


  1. Create a file named `backend-policy.yaml` with the following content:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
         spec:
           targetRef:
             group: "networking.gke.io"
             kind: GCPInferencePoolImport
             name: vllm-llama3-8b-instruct
           default:
             timeoutSec: 600
             balancingMode: CUSTOM_METRICS
             trafficDuration: LONG
             customMetrics:
             -   name: gke.named_metrics.kv-cache
               maxUtilizationPercent: 80
               dryRun: false
             scopes:
             -   selector:
                 gke.io/region: "us-east4"
               backendPreference: PREFERRED
         

  2. Apply the new policy:
         
         kubectl apply -f backend-policy.yaml --context=CLUSTER1_CONTEXT
         

Replace `CLUSTER1_CONTEXT` with the context for the first cluster, for example `gke_my-project_europe-west3-c_gke-west`




## Configure autoscaling

To help ensure that each cluster can handle an increasing load before traffic spills over to other regions, you need to configure the Horizontal-Pod-Autoscaler (HPA) for your model server deployments.

### Key configuration principles

  * **Use the same custom metrics** : the HPA should be configured to scale based on the same custom metrics that you use in the `GCPBackendPolicy` for the Multi-Cluster Inference Gateway (for example, `vllm:kv_cache_usage_perc`). This approach helps to ensures that both load balancing and scaling decisions are driven by the same signal from your inference servers. The metrics you choose must have a value between 0 and 1 to represent utilization. If the metric value is greater than 1, it is interpreted as 100% utilization by the load balancer, which can cause unexpected routing behaviors.

  * **Set a lower HPA target** : the target value for the metric in the HPA configuration must be set lower than the `maxUtilizationPercent` setting that's defined in the `GCPBackendPolicy`. By setting the HPA's target utilization lower (for example, the HPA scales at 50% average utilization), you allow the cluster to add more replicas before the load balancer's threshold (for example, 80% utilization) is reached. This approach helps to maximize the capacity within the preferred Region. A lower utilization target also helps to prevent premature traffic spillover by reserving elastic cross-region high availability for when the current region genuinely approaches its limits.


**Note:** To optimize performance for your workload, you will likely need to tune the HPA target and the load balancer utilization threshold. If you use `kv-cache-utilization` as the metric, you might also need to tune the maximum batch size for better utilization of the KV cache.

  1. Grant your user the ability to create the required authorization roles:
         
         kubectl create clusterrolebinding cluster-admin-binding \
             --clusterrole cluster-admin --user "$(gcloud config get-value account)" --context=CLUSTER1_CONTEXT
         
         kubectl create clusterrolebinding cluster-admin-binding \
             --clusterrole cluster-admin --user "$(gcloud config get-value account)" --context=CLUSTER2_CONTEXT
         

The `CLUSTER1_CONTEXT` and `CLUSTER2_CONTEXT` variables are defined in the Install the required custom resources section.

  2. For each cluster, apply the manifest:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml --context=CLUSTER1_CONTEXT
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml --context=CLUSTER2_CONTEXT
         

  3. Allow the `custom-metrics-stackdriver-adapter` service account to read Cloud Monitoring metrics:
         
         PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         
         gcloud projects add-iam-policy-binding projects/PROJECT_ID \
           --role roles/monitoring.viewer \
           --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/custom-metrics/sa/custom-metrics-stackdriver-adapter
         

Replace `PROJECT_ID` with your project ID

  4. Save the following manifest to a file named `pod-monitoring.yaml`:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: inference-server-podmon
         spec:
           selector:
             matchLabels:
               app: vllm-llama3-8b-instruct
           endpoints:
           -   port: 8000
             path: /metrics
             interval: 5s
         

  5. Apply the manifest to both clusters:
         
         kubectl apply -f pod-monitoring.yaml --context=CLUSTER1_CONTEXT
         kubectl apply -f pod-monitoring.yaml --context=CLUSTER2_CONTEXT
         

  6. Save the following manifest to a file named `hpa.yaml`:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: inference-server-hpa
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: vllm-llama3-8b-instruct
           minReplicas: 1
           maxReplicas: 10
           metrics:
           -   type: Pods
             pods:
               metric:
                 name: prometheus.googleapis.com|vllm:gpu_cache_usage_perc|gauge
               target:
                 type: AverageValue
                 averageValue: "0.5"
         

  7. Apply the manifest to both clusters:
         
         kubectl apply -f hpa.yaml --context=CLUSTER1_CONTEXT
         kubectl apply -f hpa.yaml --context=CLUSTER2_CONTEXT
         




## Verify the deployment

  1. Get the Gateway IP address:
         
         export GW_IP=$(kubectl get gateway/cross-region-gateway -n default --context=CLUSTER1_CONTEXT -o jsonpath='{.status.addresses[0].value}')
         
         echo ${GW_IP}
         

The `CLUSTER1_CONTEXT` variable is defined in the Install the required custom resources section.

  2. Start an interactive `sh` session in a temporary Pod:
         
         kubectl run -it --rm --image=curlimages/curl curly --context=CLUSTER1_CONTEXT -- /bin/sh
         

The `CLUSTER1_CONTEXT` variable is defined in the Install the required custom resources section.

  3. From inside the `curly` Pod, send a test request:
         
         curl -i -X POST <var>GW_IP</var>:80/v1/completions \
         -H 'Content-Type: application/json' \
         -d '{
           "model": "food-review-1",
           "prompt": "What is the best pizza in the world?",
           "max_tokens": 100,
           "temperature": 0
         }'
         

Replace `GW_IP` with the gateway IP address from the previous step.




## Load test the gateway

  1. Apply a sustained load to the Gateway IP address using a load generator within the same VPC network.

  2. Start with a moderate load that you expect the preferred region (`us-east4`) to handle.

  3. Gradually increase the request rate or concurrency of your load test.

  4. While the load test runs, monitor the system in the Google Cloud console or using `kubectl`:

     * **Pod scaling (HPA)** : check the number of Pods in the `vllm-llama3-8b-instruct` Deployment in both clusters.
     * **Node scaling (cluster autoscaler)** : monitor the number of nodes in the `h100` node pools in both clusters.
     * **Custom metrics** : watch the `vllm:kv_cache_usage_perc` metric (for vllm version v0.10.2 and higher) or the `vllm:gpu_cache_usage_perc` metric (for vllm version lower than v.0.10.2) in Monitoring for model server deployments in both clusters.
     * **Load Balancer metrics** : examine the metrics for the Load Balancer associated with the `cross-region-gateway` in Monitoring.



As you increase the load, utilization in `us-east4` increases. When the HPA in the `gke-east` cluster scales out and the average utilization approaches the `maxUtilization` value (80%) that is defined in the `GCPBackendPolicy`, the load balancer begins to route requests to the `gke-west` cluster in `europe-west3`.

## What's next

  * Learn more about the [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn more about the [GKE Multi-Cluster Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway).
  * Learn more about [Multi-Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
