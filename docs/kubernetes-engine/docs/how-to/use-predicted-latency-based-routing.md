---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-predicted-latency-based-routing/
title: Use predicted latency-based routing with GKE Inference Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:15.361114+00:00
---

# Use predicted latency-based routing with GKE Inference Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-predicted-latency-based-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Use predicted latency-based routing with GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to enable and use predicted latency-based routing provided by llm-d within GKE Inference Gateway. By default, GKE Inference Gateway routes requests using a combination of load signals and prefix-cache affinity heuristics. Predicted latency-based routing replaces the static heuristic weights with an XGBoost model trained continuously on live traffic, making more accurate routing decisions as workload patterns shift.

## When to use predicted latency-based routing

This feature is most effective when the following conditions apply to your workload:

  * **High variance in prompt and completion length** : queue depth alone is a poor proxy for server load when request sizes vary significantly. The latency predictor accounts for actual prefill and decode cost per request.
  * **Per-request latency SLOs** : when your applications specify Time-to-First-Token (TTFT) or Time-per-Output-Token (TPOT) targets on individual requests, the scheduler enforces these targets during routing. It does this by computing the headroom (predicted latency minus SLO target) for each candidate Pod.
  * **Fragile static weight tuning** : if you are frequently re-tuning the balance between cache affinity and load signals as traffic patterns shift, the online-trained model adapts automatically.

**Note:** **Homogeneity requirement** : predicted latency-based scheduling requires a homogeneous `InferencePool`: all Pods must share the same GPU type, model weights, and serving configuration. The XGBoost model is trained on Pod state features without considering Pod shape. Therefore, predictions across heterogeneous hardware or serving configurations would treat different regimes as identical, leading to inaccurate routing decisions. For heterogeneous pool scenarios, continue using the default load and prefix-cache aware routing.

## How predicted latency-based routing works

This section details the architecture and the scheduling pipeline used by predicted latency-based routing.

### Architecture

Predicted latency-based scheduling deploys two additional sidecar containers inside the EPP Pod, alongside the EPP itself:

Component | Description  
---|---  
**Training Server** | Continuously retrains the XGBoost TTFT and TPOT models on completed request samples received from the EPP. Uses stratified bucketing over a sliding window so that rare traffic regimes are not forgotten. Writes updated models to a shared volume.  
**Prediction Servers** | Serve TTFT and TPOT predictions to the EPP on the request hot path. Read the latest trained model from the shared volume. Horizontally scalable — each server instance sustains approximately 300 QPS of prediction work. Multiple instances are load-balanced by a Go coalescing proxy in the EPP that batches concurrent prediction requests within a 1ms window.  
  
### llm-d EPP scheduling pipeline

When predicted latency-based scheduling is enabled, the EPP processes each request through the following sequence of composable plugins:

  1. **`predicted-latency-producer`** : calls the Prediction Server to obtain TTFT and TPOT estimates for every candidate Pod in the `InferencePool`, conditioned on each Pod's current KV-cache utilization, queue depth, prefix cache match score, and the incoming request features. After the response is returned to the client, the producer sends the observed TTFT and inter-token latency back to the Training Server as a new training sample.

     * **Fallback behavior** : if the Prediction Server is unreachable or returns an error, the EPP automatically falls back to a composite score based on KV-cache utilization, queue depth, and prefix cache match.
  2. **`prefix-cache-affinity-filter`** : this filter narrows the candidate set to cache-warm Pods when any Pod's prefix cache match score exceeds the affinity threshold (default of 0.80). This threshold separates two populations observed in production: Pods that already have a conversation history cached from prior turns, and Pods that don't. This filter implements an epsilon-greedy exploit and explore strategy:

     * **Exploit (default path)** : this path routes to cache-warm Pods so that scoring concentrates cache reuse on them.

     * **Explore (small probability)** : this path bypasses the filter entirely on a configurable fraction of requests to seed cache entries on cold Pods to prevent cache fragmentation.

     * **TTFT load gate** : even on the exploit path, if the best cache-warm Pod's predicted TTFT exceeds the best overall Pod's TTFT by more than a configurable threshold (default of 5,000 ms), affinity is broken and the full candidate set is used.

  3. **`slo-headroom-tier-filter` (SLO requests only)**: when the request includes SLO headers, splits candidate Pods into a positive tier (predicted to meet the SLO) and a negative tier (predicted to violate it).

  4. **`latency-scorer`** : scores candidate Pods. Without SLO headers, the Pod with the lowest predicted latency is selected. With SLO headers, the score is based on headroom (SLO minus predicted latency) using the `headroomSelectionStrategy`:

     * `least` (default): Bin-pack. Routes to the Pod with the smallest positive headroom, maximizing utilization and keeping less loaded Pods free for future traffic bursts.
     * `most`: Spread. Routes to the Pod with the most positive headroom, leaving more slack for unexpected load spikes.
  5. **`latency-slo-admitter` (SLO requests only)**: rejects sheddable requests (priority is less than 0) when no candidate Pod is predicted to meet the SLO, instead of consuming capacity on a request predicted to miss its target. This filter has no effect when SLO headers are absent or when a Pod that meets the SLO exists.

  6. **`weighted-random-picker`** : selects the final Pod using weighted random selection over the scores. This spreads load while still favoring better-scoring Pods.




### Streaming mode

The `predicted-latency-producer` plugin supports two training modes, configured using the `streamingMode` parameter:

  * **`streamingMode: false` (default)**: trains on end-to-end (E2E) request latency. Use this mode if your workload mixes streaming and non-streaming responses, or if you only need latency-aware routing without per-request SLO enforcement.
  * **`streamingMode: true`** : trains separate TTFT and TPOT models. TTFT is recorded on the first streamed chunk; TPOT is sampled across subsequent tokens. Use this mode if your workload is fully streaming and you need meaningful `x-slo-ttft-ms` / `x-slo-tpot-ms` enforcement.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Compute Engine API, the Network Services API, and the Model Armor API if needed.

Go to [Enable access to APIs](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com,container.googleapis.com,modelarmor.googleapis.com,networkservices.googleapis.com) and follow the instructions.

  * Ensure you have a working GKE Inference Gateway deployment. See [Deploy GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway).

  * Ensure that your `InferencePool` uses a homogeneous set of Pods—identical GPU type, model weights, and serving configuration.

  * Ensure your GKE cluster is version 1.32.3 or later.

  * Install Helm. See the [Helm installation guide](https://helm.sh/docs/intro/install/).




## Enable predicted latency-based scheduling

The following steps guide you through enabling predicted latency-based scheduling for your GKE Inference Gateway deployment.

### Step 1: Install or upgrade the InferencePool with predicted latency enabled

The `latencyPredictor.enabled=true` flag deploys the Training Server and Prediction Server sidecars inside the EPP Pod and wires up the full scheduling plugin pipeline:
    
    
    helm upgrade --install INFERENCE_POOL_NAME \
      --set inferencePool.modelServers.matchLabels.app=MODEL_SERVER_LABEL \
      --set provider.name=gke \
      --set inferenceExtension.monitoring.gke.enabled=true \
      --set inferenceExtension.latencyPredictor.enabled=true \
      --version LLM_D_VERSION \
      oci://LLM_D_REGISTRY_PATH
    

Replace the following:

  * `INFERENCE_POOL_NAME`: the name of your InferencePool—for example, `vllm-llama3-8b-instruct`.
  * `MODEL_SERVER_LABEL`: the label key used to select your model server Pods.
  * `LLM_D_VERSION`: the llm-d Helm chart version to use.
  * `LLM_D_REGISTRY_PATH`: the llm-d OCI registry path.



### Step 2: Verify the deployment

Confirm the EPP Pod is running with all sidecar containers ready:
    
    
    kubectl get pods -l app=INFERENCE_POOL_NAME-epp
    

The EPP Pod should show all containers in Running or Ready state: the EPP itself, the Training Server, and one or more Prediction Servers.

### Step 3: Send a baseline request

Send a standard inference request to confirm that routing is working before enabling SLO headers:
    
    
    curl -i -X POST GATEWAY_IP:PORT/v1/completions \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
     -H 'x-prediction-based-scheduling: true' \
     -d '{
        "model": "MODEL_NAME",
        "prompt": "PROMPT_TEXT",
        "max_tokens": MAX_TOKENS,
        "temperature": "0"
     }'
    

Replace the following:

  * `GATEWAY_IP`: the IP address of your gateway service.
  * `PORT`: the port number of your gateway service.
  * `MODEL_NAME`: the name of the model to use for inference.
  * `PROMPT_TEXT`: the input prompt.
  * `MAX_TOKENS`: the maximum number of tokens to generate.



The `x-prediction-based-scheduling: true` header opts this request into the predicted latency scheduling pipeline. During the predictor warm-up period, the EPP falls back to heuristic routing.

### Step 4: Send SLO-aware requests (optional)

To enable per-request SLO enforcement, add TTFT and TPOT latency objective headers:
    
    
    curl -i -X POST GATEWAY_IP:PORT/v1/completions \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
      -H 'x-prediction-based-scheduling: true' \
      -H 'x-slo-ttft-ms: 500' \
      -H 'x-slo-tpot-ms: 50' \
      -d '{
        "model": "MODEL_NAME",
        "prompt": "PROMPT_TEXT",
        "max_tokens": MAX_TOKENS,
        "temperature": "0",
        "stream": true
      }'
    

Replace the following:

  * `GATEWAY_IP`: the IP address of your gateway service.
  * `PORT`: the port number of your gateway service.
  * `MODEL_NAME`: the name of the model to use for inference.
  * `PROMPT_TEXT`: the input prompt.
  * `MAX_TOKENS`: the maximum number of tokens to generate.



Request headers:

  * `x-prediction-based-scheduling: true`: opts the request into the predicted latency scheduling pipeline.
  * `x-slo-ttft-ms`: maximum acceptable Time-to-First-Token in milliseconds.
  * `x-slo-tpot-ms`: maximum acceptable Time-per-Output-Token in milliseconds.

**Note:** SLO headers are only enforced at the routing level. The EPP uses them to select the Pod most likely to meet the target; the model server does not terminate requests that exceed the SLO after they have been routed. Sheddable requests (priority < 0) are dropped with a 429 error when no Pod is predicted to meet the SLO.

## Monitor predicted latency scheduling

When the latency predictor is enabled, the EPP exposes additional metrics through Cloud Monitoring.

Metric | Description  
---|---  
`inference_objective_request_ttft_seconds` | Actual TTFT distribution (or E2E latency if streamingMode=false).  
`inference_objective_request_predicted_ttft_seconds` | Predicted TTFT distribution (or E2E latency if streamingMode=false).  
`inference_objective_request_tpot_seconds` | Actual TPOT distribution.  
`inference_objective_request_predicted_tpot_seconds` | Predicted TPOT distribution.  
`inference_objective_request_ttft_slo_violation_total` | Counter of TTFT SLO violations.  
  
## Scale the Prediction Server

The EPP makes one prediction call per candidate Pod per incoming request. Each Prediction Server instance sustains approximately 300 QPS of prediction work.

Approximate guidance for Prediction Server instance count:

Cluster QPS (100 Pods) | Prediction servers required  
---|---  
Up to 1,000 QPS | 1 server  
Up to 5,000 QPS | 2 servers  
Up to 10,000 QPS | 4 servers  
  
Add Prediction Server instances by updating the `latencyPredictor.predictionServerCount` Helm value.

## Limitations

  * **Homogeneous`InferencePool` required**: mixed GPU types, model variants, or serving configurations within a single pool are not supported.
  * **Warm-up period** : the XGBoost model requires sufficient live traffic samples before predictions become accurate.
  * **SLO enforcement** : enforcement is at the routing layer only. The model server does not terminate requests that exceed the SLO target after selection.
  * **Status** : this feature is in Preview. It is not recommended for production workloads with strict SLA requirements without thorough testing.



## What's next

  * [Customize GKE Inference Gateway configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations).
  * [Perform rollout operations for GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-inference-gateway-rollout-operations). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
