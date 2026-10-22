---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-multi-cluster-ray-inference-gateway/
title: Serve an LLM with multi-cluster Ray Serve and GKE Inference Gateway \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:56.648392+00:00
---

# Serve an LLM with multi-cluster Ray Serve and GKE Inference Gateway  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-multi-cluster-ray-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve an LLM with multi-cluster Ray Serve and GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to manage inference requests across multiple Ray Serve clusters on Google Kubernetes Engine (GKE) by configuring the Kubernetes Gateway API and GKE Inference Gateway. This configuration lets you centralize traffic management for multiple teams, distribute workloads across regions for higher capacity, and implement model-aware routing based on request body content.

## Benefits of using GKE Inference Gateway and Ray Serve

Using GKE Inference Gateway and Ray Serve offers the following benefits:

  * **Path routing** : configure each RayService with a path prefix, then serve them with one Gateway routing to multiple Ray Services. 
    * For more information about setting up path prefix rules, see the [Gateway API documentation](https://gateway-api.sigs.k8s.io/guides/http-routing/).
  * **Model-aware routing** : choose a RayService to route to based on the request body—for example, by extracting the requested model from an OpenAI-API JSON request.
  * **Governance** : require API keys to use your service, or enforce quota for users by using [Apigee for authentication and API management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#config-auth-api-management).
  * **Multi-region** : split traffic across multiple GKE clusters with RayServices to attain higher availability or capacity with [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-gateways).
  * **Separation of concerns** : use separate RayServices, which can be administered by separate teams, follow separate rollouts, and run on different topologies.
  * **Security** : use Gateway to act as the SSL terminator to help secure your user traffic over the internet. For more information, see [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).



To configure routing, you need to deploy a Gateway, HTTPRoute, and RayService. A Kubernetes Service for each target Ray cluster is typically created by KubeRay. Ray Serve spreads request load in-cluster, with no need to create an InferencePool or Endpoint Picker.

## Model-aware routing for Ray Serve on GKE

Model-aware routing is enabled by a body-based routing extension. Body-based routing lets you direct traffic to different RayServices based solely on the model named in the user's request, which lets you have a single endpoint that can serve many models hosted in multiple Ray clusters. Your users have simplified access, and your app developers have control over configuring each Ray endpoint.

To configure model-aware routing, you deploy the following key components:

  * A body-based router extension to extract model names from JSON payloads. This router extension is deployed by using Helm.
  * A GKE Gateway (L7 regional internal Application Load Balancer) to handle the incoming traffic.
  * HTTPRoute rules to direct traffic to the correct Ray Service by using headers populated by the router extension.
  * Multiple Ray Serve clusters to manage the lifecycle and autoscaling of siloed models.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have [Helm](https://helm.sh/docs/intro/install/) installed.
  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure that you have a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).



## Prepare your environment

Set up environment variables:
    
    
    export CLUSTER=$(whoami)-ray-bbr
    export PROJECT_ID=$(gcloud config get-value project)
    export LOCATION=us-central1-b
    export REGION=us-central1
    export HUGGING_FACE_TOKEN=YOUR_HUGGING_FACE_TOKEN
    

Replace `YOUR_HUGGING_FACE_TOKEN` with your Hugging Face access token.

## Prepare your infrastructure

In this section, you set up a Ray-enabled, Gateway-enabled GKE cluster with L4 GPUs.

  1. Create a cluster with the Ray Operator and Gateway API enabled:
         
         gcloud container clusters create ${CLUSTER} \
             --project ${PROJECT_ID} \
             --location ${LOCATION} \
             --cluster-version 1.35 \
             --gateway-api standard \
             --addons HttpLoadBalancing,RayOperator \
             --enable-ray-cluster-logging \
             --enable-ray-cluster-monitoring \
             --machine-type e2-standard-4
         

  2. Create a GPU node pool for your model workloads:
         
         gcloud container node-pools create gpu-pool \
             --cluster=${CLUSTER} \
             --location=${LOCATION} \
             --accelerator="type=nvidia-l4,count=1,gpu-driver-version=latest" \
             --machine-type=g2-standard-8 \
             --num-nodes=4
         

  3. Create a proxy-only subnet for the regional internal Application Load Balancer, which is required by body-based routing:
         
         gcloud compute networks subnets create bbr-proxy-only-subnet \
             --purpose=REGIONAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=${REGION} \
             --network=default \
             --range=192.168.10.0/24
         

  4. Deploy your Hugging Face secret:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=${HUGGING_FACE_TOKEN}
         




## Deploy the body-based router for model-aware routing

The body-based router extension intercepts requests, parses the JSON body, and extracts the model field into an `X-Gateway-Model-Name` header.

  1. Create a file named `helm-values.yaml` with the following content:
         
         bbr:
           plugins:
             - type: "body-field-to-header"
               name: "openai-model-extractor"
               json:
                 field_name: "model"
                 header_name: "X-Gateway-Model-Name"
         

  2. Install the body-based router by using Helm:
         
         helm install body-based-router \
             oci://registry.k8s.io/gateway-api-inference-extension/charts/body-based-routing \
             --version v1.4.0 \
             --set provider.name=gke \
             --set inferenceGateway.name=ray-multi-model-gateway \
             --values helm-values.yaml
         




## Deploy RayServices

To deploy your models, you must apply the `RayService` manifests. Each manifest defines a Ray cluster that runs a specific LLM.

  1. Create a file named `gemma-2b-it.yaml` with the following content:
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: gemma-2b-it
         spec:
           serveConfigV2: |
             applications:
             - name: llm_app
               route_prefix: "/"
               import_path: ray.serve.llm:build_openai_app
               args:
                 llm_configs:
                     - model_loading_config:
                         model_id: gemma-2b-it
                         model_source: google/gemma-2b-it
                       accelerator_type: L4
                       log_engine_metrics: true
                       deployment_config:
                         autoscaling_config:
                             min_replicas: 2
                             max_replicas: 2
                         health_check_period_s: 600
                         health_check_timeout_s: 300
           rayClusterConfig:
             headGroupSpec:
               rayStartParams:
                 dashboard-host: "0.0.0.0"
                 num-cpus: "0"
               template:
                 spec:
                   containers:
                     - name: ray-head
                       image: rayproject/ray-llm:2.54.0-py311-cu128
                       resources:
                         limits:
                           memory: "8Gi"
                           ephemeral-storage: "32Gi"
                         requests:
                           cpu: "2"
                           memory: "8Gi"
                           ephemeral-storage: "32Gi"
                       ports:
                         - containerPort: 6379
                           name: gcs-server
                         - containerPort: 8265
                           name: dashboard
                         - containerPort: 10001
                           name: client
                         - containerPort: 8000
                           name: serve
                       env:
                         - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
                           value: "1"
                         - name: RAY_SERVE_ENABLE_HA_PROXY
                           value: "1"
                         - name: HUGGING_FACE_HUB_TOKEN
                           valueFrom:
                             secretKeyRef:
                               name: hf-secret
                               key: hf_api_token
             rayVersion: 2.54.0
             workerGroupSpecs:
               - replicas: 2
                 minReplicas: 2
                 maxReplicas: 2
                 groupName: gpu-group
                 rayStartParams: {}
                 template:
                   spec:
                     containers:
                       - name: llm
                         image: rayproject/ray-llm:2.54.0-py311-cu128
                         env:
                           - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
                             value: "1"
                           - name: RAY_SERVE_ENABLE_HA_PROXY
                             value: "1"
                           - name: HUGGING_FACE_HUB_TOKEN
                             valueFrom:
                               secretKeyRef:
                                 name: hf-secret
                                 key: hf_api_token
                         resources:
                           limits:
                             nvidia.com/gpu: "1"
                             ephemeral-storage: "24Gi"
                           requests:
                             cpu: "6"
                             memory: "24Gi"
                             nvidia.com/gpu: "1"
                             ephemeral-storage: "24Gi"
                     nodeSelector:
                       cloud.google.com/gke-accelerator: nvidia-l4
         

  2. Create a file named `qwen2.5-3b.yaml` with the following content:
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: qwen-25-3b
         spec:
           serveConfigV2: |
             applications:
             - name: llm_app
               route_prefix: "/"
               import_path: ray.serve.llm:build_openai_app
               args:
                 llm_configs:
                     - model_loading_config:
                         model_id: qwen-2.5-3b
                         model_source: Qwen/Qwen2.5-3B
                       accelerator_type: L4
                       log_engine_metrics: true
                       deployment_config:
                         autoscaling_config:
                             min_replicas: 2
                             max_replicas: 2
                         health_check_period_s: 600
                         health_check_timeout_s: 300
           rayClusterConfig:
             headGroupSpec:
               rayStartParams:
                 dashboard-host: "0.0.0.0"
                 num-cpus: "0"
               template:
                 spec:
                   containers:
                     - name: ray-head
                       image: rayproject/ray-llm:2.54.0-py311-cu128
                       resources:
                         limits:
                           memory: "8Gi"
                           ephemeral-storage: "32Gi"
                         requests:
                           cpu: "2"
                           memory: "8Gi"
                           ephemeral-storage: "32Gi"
                       ports:
                         - containerPort: 6379
                           name: gcs-server
                         - containerPort: 8265
                           name: dashboard
                         - containerPort: 10001
                           name: client
                         - containerPort: 8000
                           name: serve
                       env:
                         - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
                           value: "1"
                         - name: RAY_SERVE_ENABLE_HA_PROXY
                           value: "1"
                         - name: HUGGING_FACE_HUB_TOKEN
                           valueFrom:
                             secretKeyRef:
                               name: hf-secret
                               key: hf_api_token
             rayVersion: 2.54.0
             workerGroupSpecs:
               - replicas: 2
                 minReplicas: 2
                 maxReplicas: 2
                 groupName: gpu-group
                 rayStartParams: {}
                 template:
                   spec:
                     containers:
                       - name: llm
                         image: rayproject/ray-llm:2.54.0-py311-cu128
                         env:
                           - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
                             value: "1"
                           - name: RAY_SERVE_ENABLE_HA_PROXY
                             value: "1"
                           - name: HUGGING_FACE_HUB_TOKEN
                             valueFrom:
                               secretKeyRef:
                                 name: hf-secret
                                 key: hf_api_token
                         resources:
                           limits:
                             nvidia.com/gpu: "1"
                             ephemeral-storage: "24Gi"
                           requests:
                             cpu: "6"
                             memory: "24Gi"
                             nvidia.com/gpu: "1"
                             ephemeral-storage: "24Gi"
                     nodeSelector:
                       cloud.google.com/gke-accelerator: nvidia-l4
         

  3. Deploy the models:
         
         kubectl apply -f gemma-2b-it.yaml
         kubectl apply -f qwen2.5-3b.yaml
         




### Configure health checks

To help ensure the load balancer accurately monitors Ray worker health, you must apply the `HealthCheckPolicy` resource.

  1. Create a file named `healthcheck-policy.yaml` with the following content:
         
         apiVersion: networking.gke.io/v1
         kind: HealthCheckPolicy
         metadata:
           name: gemma-serve-healthcheck
           namespace: default
         spec:
           default:
             checkIntervalSec: 5
             timeoutSec: 5
             healthyThreshold: 2
             unhealthyThreshold: 2
             config:
               type: HTTP
               httpHealthCheck:
                 port: 8000
                 requestPath: /-/healthz
           targetRef:
             group: ""
             kind: Service
             name: gemma-2b-it-serve-svc
         ---
         apiVersion: networking.gke.io/v1
         kind: HealthCheckPolicy
         metadata:
           name: qwen-serve-healthcheck
           namespace: default
         spec:
           default:
             checkIntervalSec: 5
             timeoutSec: 5
             healthyThreshold: 2
             unhealthyThreshold: 2
             config:
               type: HTTP
               httpHealthCheck:
                 port: 8000
                 requestPath: /-/healthz
           targetRef:
             group: ""
             kind: Service
             name: qwen-25-3b-serve-svc
         

  2. Apply the health check policy:
         
         kubectl apply -f healthcheck-policy.yaml
         




## Configure routing

To configure routing, you must apply the `Gateway` and `HTTPRoute` manifests. The `HTTPRoute` contains rules that match the `X-Gateway-Model-Name` header (populated by the body-based router) to route traffic to the appropriate Ray service.

  1. Create a file named `gateway.yaml` with the following content:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: ray-multi-model-gateway
           namespace: default
         spec:
           gatewayClassName: gke-l7-rilb
           listeners:
           - allowedRoutes:
               namespaces:
                 from: Same
             name: http
             port: 80
             protocol: HTTP
         ---
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: ray-multi-model-route
         spec:
           parentRefs:
           - name: ray-multi-model-gateway
           rules:
           - matches:
             - headers:
               - type: Exact
                 name: X-Gateway-Model-Name
                 value: gemma-2b-it  # Must match model named in JSON request!
               path:
                 type: PathPrefix
                 value: /
             backendRefs:
             - name: gemma-2b-it-serve-svc  # Ray service name plus "-serve-svc".
               kind: Service
               port: 8000
         
           - matches:
             - headers:
               - type: Exact
                 name: X-Gateway-Model-Name
                 value: qwen-2.5-3b  # Matches another extracted model name
               path:
                 type: PathPrefix
                 value: /
             backendRefs:
             - name: qwen-25-3b-serve-svc  # Target Ray Service.
               kind: Service
               port: 8000
         

  2. Apply the gateway and route:
         
         kubectl apply -f gateway.yaml
         




## Test the deployment

After the Gateway is provisioned and both Ray clusters are ready, you can test routing by sending requests with different model names in the JSON body.

  1. Get the Gateway IP address:
         
         kubectl get gateways ray-multi-model-gateway
         

  2. Start a shell in a network that can reach the Gateway address. You can use curl on one of the Ray cluster Pods:
         
         POD_NAME=$(kubectl get pods -l ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')
         kubectl exec -it $POD_NAME -- bash
         

  3. Send requests by testing routing to Gemma:
         
         curl http://GATEWAY_IP_ADDRESS/v1/chat/completions \
             --header 'Content-Type: application/json' \
             --data '{
             "model": "gemma-2b-it",
             "messages": [{"role": "user", "content": "Tell me about GKE."}]
             }'
         

Replace `GATEWAY_IP_ADDRESS` with the IP address from the previous step.

The output is similar to the following:
         
         {"id":"chatcmpl-594f7cab-f991-4522-9829-acdbb65d9f67","object":"chat.completion","created":1776379509,"model":"gemma-2b-it","choices":[{"index":0,"message":{"role":"assistant","content":"**Google Kubernetes Engine (GKE)** is a fully managed container orchestration service for Kubernetes [...]
         

  4. Test routing to Qwen:
         
         curl http://GATEWAY_IP_ADDRESS/v1/chat/completions \
             --header 'Content-Type: application/json' \
             --data '{
             "model": "qwen-2.5-3b",
             "messages": [{"role": "user", "content": "How does Ray Serve work?"}]
             }'
         

The output is similar to the following:
         
         {"id":"chatcmpl-dfe3f3b7-45fc-481c-b53e-2fc09c033cdb","object":"chat.completion","created":1776380249,"model":"qwen-2.5-3b","choices":[{"index":0,"message":{"role":"assistant","content":"Ray Serve facilitates the hosting and deployment of scalable microservices. [...]
         




The body-based router automatically extracts the value of the `model` field and ensures each request reaches the correct backend service configured in the `gateway.yaml` file.

## Clean up

Delete the cluster:
    
    
    gcloud container clusters delete ${CLUSTER}
    

## What's next

  * Learn about [performance optimizations for Ray Serve](https://www.anyscale.com/blog/ray-serve-inference-lower-latency-higher-throughput-haproxy).
  * Read more about [Gateway on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
