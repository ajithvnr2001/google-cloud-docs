---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway/
title: Deploy GKE Inference Gateway powered by llm-d \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:07.861241+00:00
---

# Deploy GKE Inference Gateway powered by llm-d  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploy GKE Inference Gateway powered by llm-d Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to deploy GKE Inference Gateway.

This document is intended for Networking specialists responsible for managing GKE infrastructure and platform administrators who manage AI workloads.

Before reading this page, ensure that you're familiar with the following:

  * [About GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).
  * [AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * [Generative AI glossary](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/glossary-genai).
  * [Load balancing in Google Cloud](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), especially how load balancers interact with GKE.
  * GKE Service Extensions. For more information, see the [ GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) documentation.
  * [Customize GKE Gateway traffic using Service Extensions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions).



GKE Inference Gateway enhances Google Kubernetes Engine (GKE) Gateway to optimize the serving of generative AI applications and workloads on GKE. It provides efficient management and scaling of AI workloads, enables workload-specific performance objectives such as latency, and enhances resource utilization, observability, and AI safety.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Compute Engine API, the Kubernetes Engine API, the Network Services API, and the Model Armor API if needed.

Go to [Enable access to APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,modelarmor.googleapis.com,networkservices.googleapis.com) and follow the instructions.

  * Make sure that you have the following roles on the project: `roles/container.admin`, `roles/iam.serviceAccountAdmin`.

  * Ensure your project has sufficient quota for H100 GPUs. To learn more, see [Plan GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).

  * Create a [Hugging Face](https://huggingface.co/) account if you don't already have one. You will need this to access the model resources for this tutorial.

  * Request access to the Llama 3.1 model and generate an access token. Access to this model requires an approved request on Hugging Face, and the deployment will fail if access has not been granted.

    * **Sign the license consent agreement:** You must sign the consent agreement to use the Llama 3.1 model. Go to the model's page on Hugging Face, verify your account, and accept the terms.
    * **Generate an access token:** To access the model, you need a Hugging Face token. In your Hugging Face account, go to **Your Profile > Settings > Access Tokens**, create a new token with at least Read permissions, and copy it to your clipboard.
  * [Configure a proxy-only subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_a_proxy-only_subnet) for your VPC network. The Gateway controller requires an active proxy-only subnet in the region to provision the Application Load Balancer.




### GKE Gateway controller requirements

  * GKE version 1.32.3 or later.
  * Google Cloud CLI version 407.0.0 or later.
  * Gateway API is supported on VPC-native clusters only.
  * Your cluster must have the `HttpLoadBalancing` add-on enabled.
  * If you are using Istio, you must upgrade Istio to one of the following versions: 
    * 1.15.2 or later
    * 1.14.5 or later
    * 1.13.9 or later
  * If you are using Shared VPC, then in the host project, you need to assign the `Compute Network User` role to the GKE Service account for the service project.



### Restrictions and limitations

The following restrictions and limitations apply:

  * GKE Inference Gateway is only supported on the `gke-l7-regional-external-managed` and `gke-l7-rilb` GatewayClass resources.
  * Cross-region internal Application Load Balancers are not supported.
  * An InferencePool can have a maximum of eight `targetPorts`.



## Configure GKE Inference Gateway

To configure GKE Inference Gateway, consider this example. A team runs [`vLLM`](https://docs.vllm.ai/en/latest/) and [`Llama3`](https://www.llama.com/) models and actively experiments with two distinct LoRA fine-tuned adapters: "food-review" and "cad-fabricator".

The high-level workflow for configuring GKE Inference Gateway is as follows:

  1. Prepare your environment: set up the necessary infrastructure and components.
  2. Create an inference pool: define a pool of model servers using the InferencePool Custom Resource.
  3. Specify inference objectives: specify inference objectives using the `InferenceObjective` Custom Resource
  4. Create the Gateway: expose the inference service using Gateway API.
  5. Create the `HTTPRoute`: define how HTTP traffic is routed to the inference service.
  6. Send inference requests: make requests to the deployed model.



### Create the Gateway

The Gateway resource is the entry point for external traffic into your Kubernetes cluster. It defines the listeners that accept incoming connections.

The GKE Inference Gateway works with the following Gateway Classes:

  * `gke-l7-rilb`: for regional internal Application Load Balancers.
  * `gke-l7-regional-external-managed`: for regional external Application Load Balancers.



For more information, see [Gateway Classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_classes) documentation.

To create a Gateway, perform the following steps:

  1. Save the following sample manifest as `gateway.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: GATEWAY_NAME
         spec:
           gatewayClassName: GATEWAY_CLASS
           listeners:
             - protocol: HTTP
               port: 80
               name: http
         

Replace the following:

     * `GATEWAY_NAME`: a unique name for your Gateway resource. For example, `inference-gateway`.
     * `GATEWAY_CLASS`: the Gateway Class you want to use. For example, `gke-l7-regional-external-managed`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f gateway.yaml
         




**Note** : For more information about configuring TLS to secure your Gateway with HTTPS, see the GKE documentation on [TLS configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#https).

### Prepare your environment

  1. Install [Helm](https://helm.sh/docs/intro/install/).

  2. Create a GKE cluster:

     * Create a GKE Autopilot or Standard cluster with version 1.32.3 or later. For a one-click deployment reference setup, see the [`cluster-toolkit gke-a3-highgpu` sample](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#gke-a3-highgpuyaml-).
     * Configure the nodes with your preferred compute family and accelerator.
     * Use [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) for pre-configured and tested deployment manifests, based on your selected accelerator, model, and performance needs.
  3. Install needed Custom Resource Definitions (CRDs) in your GKE cluster:

     * For GKE versions `1.34.0-gke.1626000` or later, the `InferencePool` CRD is included by default. Therefore, install only the alpha `InferenceObjective` CRD:
           
           kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/raw/v1.5.0/config/crd/bases/inference.networking.x-k8s.io_inferenceobjectives.yaml
           

     * For GKE versions earlier than `1.34.0-gke.1626000`, install both the v1 InferencePool and alpha `InferenceObjective` CRDs:
           
           kubectl apply -f  https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v1.5.0/manifests.yaml
           

For more information, see the [compatibility matrix](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway#compatibility).

  4. If you are using GKE version earlier than `v1.32.2-gke.1182001` and you want to use Model Armor with GKE Inference Gateway, you must install the traffic and routing extension CRDs:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/refs/heads/main/config/crd/networking.gke.io_gcptrafficextensions.yaml
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/refs/heads/main/config/crd/networking.gke.io_gcproutingextensions.yaml
         

  5. Set the following environment variables:
         
         export GAIE_VERSION=v1.5.0
         export GUIDE_NAME="optimized-baseline"
         export NAMESPACE=llm-d-optimized-baseline
         export INFRA_PROVIDER=gke   # gke | base
         

  6. Install the Gateway API Inference Extension custom resource definitions (CRDs) required by the llm-d endpoint picker (EPP):
         
         kubectl apply -k \
           "https://github.com/kubernetes-sigs/gateway-api-inference-extension/config/crd?ref=${GAIE_VERSION}"
         

  7. Create the target namespace:
         
         kubectl create namespace ${NAMESPACE}
         




### Create a model server and model deployment

This section shows how to deploy a model server and model. The example uses a `vLLM` model server with a `Llama3` model. The deployment is labeled as `app:vllm-llama3-8b-instruct`. This deployment also uses two LoRA adapters named `food-review` and `cad-fabricator` from Hugging Face.

You can adapt this example with your own model server container and model, serving port, and deployment name. You can also configure LoRA adapters in the deployment, or deploy the base model. The following steps describe how to create the necessary Kubernetes resources.

  1. Create a Kubernetes Secret to store your Hugging Face token. This token is used to access the base model and the LoRA adapters:
         
         kubectl create secret generic hf-token --from-literal=token=HF_TOKEN
         

Replace `HF_TOKEN` with your Hugging Face token.

  2. Deploy the vLLM model server using the GKE-specific Kustomize overlay from the llm-d optimized-baseline guide. Setting `INFRA_PROVIDER=gke` applies GKE-specific configurations including Cloud Monitoring integration:
         
         kubectl apply -n ${NAMESPACE} \
           -k guides/${GUIDE_NAME}/modelserver/gpu/vllm/${INFRA_PROVIDER}/
         




**Note:** GKE provides automatic application monitoring by default. The llm-d monitoring stack is not required for GKE, but is available if you prefer to use it.

If your model server requires multiple ports, ensure the container spec exposes each port. The following example defines a Deployment where the container exposes three ports:

#### Multiport Deployment example
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: multiport-model-server
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: multiport-model-server
      template:
        metadata:
          labels:
            app: multiport-model-server
        spec:
          containers:
          - name: model-server
            image: your-model-server-image
            ports:
            - containerPort: 8080
            - containerPort: 8081
            - containerPort: 9000
    

### Create an inference pool

The InferencePool Kubernetes custom resource defines a group of Pods with a common base large language model (LLM) and compute configuration. The `selector` field specifies which Pods belong to this pool. The labels in this selector must exactly match the labels applied to your model server Pods. The `targetPorts` field defines the ports that the model server uses within the Pods. You can specify up to eight ports. The `extensionRef` field references an extension service that provides additional capability for the inference pool. The InferencePool enables GKE Inference Gateway to route traffic to your model server Pods.

**Note:** Each entry in `targetPorts` field will result in a dedicated Network Endpoint Group (NEG), but all NEGs for the InferencePool are attached to a single Google Cloud Backend Service.

The following InferencePool manifest specifies multiple targetPorts that correspond to the ports exposed by the model server Deployment:

#### Multiport InferencePool example
    
    
    apiVersion: inference.networking.k8s.io/v1
    kind: InferencePool
    metadata:
      name: my-multiport-pool
      namespace: default
    spec:
      selector:
        matchLabels:
          app: multiport-model-server
      targetPorts:
        - number: 8080
        - number: 8081
        - number: 9000
    

Before you create the InferencePool, ensure that the model server Pods that the InferencePool selects are already running.

Clone the recipes and recommendations for the InferencePool from the [llm-d GitHub repository](https://github.com/llm-d/llm-d). This step is required.:
    
    
    git clone https://github.com/llm-d/llm-d -b v0.7.0 && cd llm-d
    

To create an InferencePool and Endpoint Picker using Helm, perform the following steps:
    
    
    helm install ${GUIDE_NAME} \
      -f guides/recipes/scheduler/base.values.yaml \
      -f guides/${GUIDE_NAME}/scheduler/${GUIDE_NAME}.values.yaml \
      --set provider.name=gke \
      --set inferenceExtension.monitoring.gke.enabled=true \
      -n ${NAMESPACE} \
      --version ${GAIE_VERSION} \
      oci://LLM_D_REGISTRY_PATH
    

Replace the following:

  * `GAIE_VERSION`: the version of the Helm chart. For example, `v1.5.0`.
  * `LLM_D_REGISTRY_PATH`: the OCI registry path for the Helm chart. For example, `registry.k8s.io/gateway-api-inference-extension/charts/inferencepool`.



In the `guides/recipes/scheduler/base.values.yaml` file, change the following field to match the label of your model Deployment Pod:

  * `inferencePool.modelServers.matchLabels`: the key and value of the label used to select your model server Pods.

**Note** : The key and value align with the `optimized-baseline` guide example, so we are replacing it to match your Deployment Pod labels.




For monitoring, metrics scraping for Google Cloud Managed Service for Prometheus is enabled by default.

  * To disable this feature, add the `--set inferenceExtension.monitoring.prometheus.enabled=false` flag to the command.
  * If you use the default monitoring on a GKE Autopilot cluster, you must also add the `--set provider.gke.autopilot=true` flag.



The Helm install automatically installs the necessary timeout policy, endpoint-picker and the Pods needed for observability.

This creates an InferencePool object: `vllm-llama3-8b-instruct` referencing the model endpoint services within the Pods. It also creates a deployment of the Endpoint Picker named `app:vllm-llama3-8b-instruct-epp` for this created InferencePool.

#### Deploy Endpoint Picker with high availability

Deploying Endpoint Picker (EPP) with [preferred backends](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy#preferred-backends) enables an active-passive routing topology backed by Cloud Load Balancing.

Using Endpoint Picker with preferred backends helps you achieve the following:

  * **State consistency** : Cloud Load Balancing directs 100% of steady-state `ext_proc` traffic to the primary Endpoint Picker replica (`epp-0`), preserving key-value (KV) cache state and request scheduling context.
  * **Zero-downtime failover** : If the primary Endpoint Picker Pod crashes or undergoes maintenance, Cloud Load Balancing detects the failure using active gRPC health checks and immediately routes traffic to the standby replica (`epp-1`).
  * **Fail-open resilience** : When paired with `failureMode: FailOpen`, transient routing failures bypass Endpoint Picker and allow requests to forward directly to model servers without dropping user requests.



When you enable preferred backends, GKE modifies the architecture and routing in the following ways:

  * **Endpoint Picker StatefulSet architecture** : Endpoint Picker is deployed as a StatefulSet instead of a Deployment. Pod ordinals designate the replica roles: ordinal `epp-0` serves as the primary replica pinned to the `PREFERRED` backend tier, and ordinal `epp-1` serves as the standby replica pinned to the `DEFAULT` tier.
  * **Routing state stays centralized** : Steady-state `ext_proc` traffic routes exclusively to the primary Endpoint Picker replica (`epp-0`) to keep key-value (KV) cache tracking and request scheduling state centralized. If `epp-0` becomes unhealthy, Cloud Load Balancing shifts traffic to the standby replica (`epp-1`).
  * **Dual-Service architecture** : The Helm chart creates a primary Service (`Service/${GUIDE_NAME}-epp`) and a standby backup Service (`Service/${GUIDE_NAME}-epp-backup`). The `InferencePool` resource declaratively targets the standby backup Service. Anchoring declarative Gateway ownership to the standby Service ensures that GKE Gateway controller reconciliation loops don't detach the primary network endpoint groups (NEGs) that you attach to the backend service.



To create an InferencePool and Endpoint Picker with high availability using Helm, perform the following steps:

  1. Deploy the InferencePool and Endpoint Picker with preferred backends by using Helm:
         
         helm install ${GUIDE_NAME} \
           -f guides/recipes/scheduler/base.values.yaml \
           -f guides/${GUIDE_NAME}/scheduler/${GUIDE_NAME}.values.yaml \
           --set provider.name=gke \
           --set inferenceExtension.monitoring.gke.enabled=true \
           --set provider.gke.preferredBackends.enabled=true \
           --set provider.gke.preferredBackends.preferredReplicas=1 \
           --set provider.gke.preferredBackends.defaultReplicas=1 \
           -n ${NAMESPACE} \
           --version ${GAIE_VERSION} \
           oci://LLM_D_REGISTRY_PATH
         

Replace the following:

     * `GAIE_VERSION`: the Gateway API Inference Extension (GAIE) version of the Helm chart. For example, `v1.5.0`. Preferred backends requires Helm chart version `v1.5.0` or later.
     * `LLM_D_REGISTRY_PATH`: the OCI registry path for the Helm chart. For example, `registry.k8s.io/gateway-api-inference-extension/charts/inferencepool`.

For a complete list of parameters, see [`values.yaml`](https://github.com/llm-d/llm-d-router/blob/main/config/charts/llm-d-router-gateway/values.yaml).

  2. Attach the primary NEG to the `BackendService`:
         
         export PROJECT_ID=PROJECT_ID
         export REGION=REGION
         
         export BACKEND_SERVICE=$(gcloud compute backend-services list --project=${PROJECT_ID} --format="value(name)" | grep "${GUIDE_NAME}-epp")
         
         export PRIMARY_NEG=$(kubectl get svc ${GUIDE_NAME}-epp -n ${NAMESPACE} -o jsonpath='{.metadata.annotations.cloud\.google\.com/neg-status}' | jq -r '.network_endpoint_groups["9002"]')
         
         for ZONE in $(kubectl get svc ${GUIDE_NAME}-epp -n ${NAMESPACE} -o jsonpath='{.metadata.annotations.cloud\.google\.com/neg-status}' | jq -r '.zones[]'); do
           gcloud compute backend-services add-backend ${BACKEND_SERVICE} \
             --network-endpoint-group=${PRIMARY_NEG} \
             --network-endpoint-group-zone=${ZONE} \
             --region=${REGION} \
             --project=${PROJECT_ID} \
             --balancing-mode=RATE \
             --max-rate-per-endpoint=100 \
             --preference=PREFERRED
           sleep 15
         done
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region of your cluster and backend service.



After zonal NEGs are attached to the Google Cloud `BackendService`, scaling replica counts (`preferredReplicas` or `defaultReplicas`) or restarting Pods doesn't require running `gcloud` commands again. The GKE NEG controller automatically synchronizes individual Pod IP addresses into the registered zonal NEGs.

If you delete and recreate the parent `Gateway` or `InferencePool` resource, the GKE Gateway controller recreates the underlying Google Cloud `BackendService` with a new cloud identifier. In that event, execute the preceding attachment workflow to attach primary zonal NEGs to the newly created `BackendService`.

### Create the `HTTPRoute`

The `HTTPRoute` resource defines how the GKE Gateway routes incoming HTTP requests to backend services, such as your InferencePool. The `HTTPRoute` resource specifies matching rules (for example, headers or paths) and the backend to which traffic should be forwarded.

  1. To create an `HTTPRoute`, save the following sample manifest as `httproute.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: HTTPROUTE_NAME
         spec:
           parentRefs:
           - name: GATEWAY_NAME
           rules:
           - matches:
             - path:
                 type: PathPrefix
                 value: PATH_PREFIX
             backendRefs:
             - name: INFERENCE_POOL_NAME
               group: "inference.networking.k8s.io"
               kind: InferencePool
         

Replace the following:

     * `HTTPROUTE_NAME`: a unique name for your `HTTPRoute` resource. For example, `my-route`.
     * `GATEWAY_NAME`: the name of the `Gateway` resource that you created. For example, `inference-gateway`.
     * `PATH_PREFIX`: the path prefix that you use to match incoming requests. For example, `/` to match all.
     * `INFERENCE_POOL_NAME`: the name of the InferencePool resource that you want to route traffic to. For example, `vllm-llama3-8b-instruct`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f httproute.yaml
         

**Note:** To configure Cross-Origin Resource Sharing (CORS) for your inference endpoints by using a `CORS` filter in the `HTTPRoute`, see [Configure Cross-Origin Resource Sharing (CORS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors).



### Specify inference objectives

The `InferenceObjective` custom resource lets you specify priority of requests.

The `metadata.name` field of the `InferenceObjective` resource specifies the name of the Inference Objective, the `Priority` field specifies its serving criticality, and the `poolRef` field specifies the InferencePool on which the model is served.
    
    
    apiVersion: inference.networking.x-k8s.io/v1alpha2
    kind: InferenceObjective
    metadata:
      name: NAME
    spec:
      priority: VALUE
      poolRef:
        name: INFERENCE_POOL_NAME
        group: "inference.networking.k8s.io"
    

Replace the following:

  * `NAME`: the name of your Inference Objective. For example, `food-review`.
  * `VALUE`: the priority for the Inference Objective. This is an integer where a higher value indicates a more critical request. For example, 10.
  * `INFERENCE_POOL_NAME`: the name of the InferencePool you created in the previous step. For example, `vllm-llama3-8b-instruct`.



To create an `InferenceObjective`, perform the following steps:

  1. Save the following manifest as `inference-objectives.yaml`. This manifest creates two `InferenceObjective` resources. The first configures the `food-review` Inference Objective on the `vllm-llama3-8b-instruct` InferencePool with a priority of 10. The second configures the `llama3-base-model` Inference Objective to be served with a higher priority of 20.
         
         apiVersion: inference.networking.x-k8s.io/v1alpha2
         kind: InferenceObjective
         metadata:
           name: food-review
         spec:
           priority: 10
           poolRef:
             name: vllm-llama3-8b-instruct
             group: "inference.networking.k8s.io"
         ---
         apiVersion: inference.networking.x-k8s.io/v1alpha2
         kind: InferenceObjective
         metadata:
           name: llama3-base-model
         spec:
           priority: 20 # Higher priority
           poolRef:
             name: vllm-llama3-8b-instruct
         

  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f inference-objectives.yaml
         




### Verify the deployment

To verify that all components are running, run the following commands:
    
    
    kubectl get inferencepool
    kubectl get inferenceobjective
    kubectl get pods -l app=vllm-llama3-8b-instruct-epp
    

### Send inference request

After you have configured GKE Inference Gateway, you can send inference requests to your deployed model. This lets you generate text based on your input prompt and specified parameters.

To send inference requests, perform the following steps:

  1. Set the following environment variables:
         
         export GATEWAY_NAME=GATEWAY_NAME
         export PORT_NUMBER=PORT_NUMBER # Use 80 for HTTP
         

Replace the following:

     * `GATEWAY_NAME`: the name of your Gateway resource.
     * `PORT_NUMBER`: the port number you configured in the Gateway.
  2. To get the Gateway endpoint, run the following command:
         
         echo "Waiting for the Gateway IP address..."
         IP=""
         while [ -z "$IP" ]; do
           IP=$(kubectl get gateway/${GATEWAY_NAME} -o jsonpath='{.status.addresses[0].value}' 2>/dev/null)
           if [ -z "$IP" ]; then
             echo "Gateway IP not found, waiting 5 seconds..."
             sleep 5
           fi
         done
         
         echo "Gateway IP address is: $IP"
         PORT=${PORT_NUMBER}
         

  3. To send a request to the `/v1/completions` endpoint using `curl`, run the following command:
         
         curl -i -X POST ${IP}:${PORT}/v1/completions \
         -H 'Content-Type: application/json' \
         -H 'Authorization: Bearer $(gcloud auth application-default print-access-token)' \
         -d '{
             "model": "MODEL_NAME",
             "prompt": "PROMPT_TEXT",
             "max_tokens": MAX_TOKENS,
             "temperature": "TEMPERATURE"
         }'
         

Replace the following:

     * `MODEL_NAME`: the name of the model or LoRA adapter to use.
     * `PROMPT_TEXT`: the input prompt for the model.
     * `MAX_TOKENS`: the maximum number of tokens to generate in the response.
     * `TEMPERATURE`: controls the randomness of the output. Use the value `0` for deterministic output, or a higher number for more creative output.



The following example shows you how to send a sample request to GKE Inference Gateway:
    
    
    curl -i -X POST ${IP}:${PORT}/v1/completions -H 'Content-Type: application/json' -H 'Authorization: Bearer $(gcloud auth application-default print-access-token)' -d '{
        "model": "food-review-1",
        "prompt": "What is the best pizza in the world?",
        "max_tokens": 2048,
        "temperature": 0
    }'
    

Be aware of the following behaviours:

  * **Request body** : the request body can include additional parameters like `stop` and `top_p`. Refer to the [OpenAI API specification](https://platform.openai.com/docs/api-reference/completions) for a complete list of options.
  * **Error handling** : implement proper error handling in your client code to handle potential errors in the response. For example, check the HTTP status code in the `curl` response. A non-`200` status code generally indicates an error.
  * **Authentication and authorization** : for production deployments, secure your API endpoint with authentication and authorization mechanisms. Include the appropriate headers (for example, `Authorization`) in your requests.



## Compatibility matrix

**Note:** Starting from GKE version `1.34.0-gke.1626000`, Google Kubernetes Engine automatically manages the v1 `InferencePool` CustomResourceDefinition. Attempting to install the v1 `InferencePool` CustomResourceDefinition might cause unexpected issues and results in a warning.

The table outlines the compatibility and support matrix for the Gateway API Inference Extension Custom Resource Definitions (CRDs). It details which CustomResourceDefinition versions are supported by GKE compared to the open-source (OSS) Gateway API Inference Extension project, including specific version requirements and installation notes.

CustomResourceDefinition Name | CustomResourceDefinition API Version | GKE Managed Support | OSS (Gateway API Inference Extension) Support  
---|---|---|---  
V1 InferencePool | inference.networking.k8s.io/v1 | Supported on GKE 1.32.3 or later and CustomResourceDefinition installed by default on GKE 1.34.0-gke.1626000 or later | Supported starting from Gateway API Inference Extension v1.0.0  
Alpha InferencePool _(Recommend users starting with v1 InferencePool as alpha InferencePool version has been deprecated)_ | inference.networking.x-k8s.io/v1alpha2 | Supported on GKE 1.32.3 or later. However, CustomResourceDefinition is _not_ installed by default on GKE. Users need to manually install the CustomResourceDefinition from Gateway API Inference Extension. | Supported starting from Gateway API Inference Extension v0.2.0  
Alpha InferenceObjective | inference.networking.x-k8s.io/v1alpha2 | GKE doesn't manage InferenceObjective | Supported starting from Gateway API Inference Extension v1.0.0  
Alpha InferenceModel _(Recommend users starting with InferenceObjective as InferenceModel has been deprecated)_ | inference.networking.x-k8s.io/v1alpha2 | GKE doesn't manage InferenceModel | Supported starting from Gateway API Inference Extension v0.2.0.  
  
## Secure your inference backend with backend TLS

Backend TLS enables the GKE Gateway load balancer to verify the identity of the inference backends it connects to. Backend TLS adds an explicit verification step during the TLS handshake between the Gateway and the backend Pod. This verification helps ensure that the Gateway communicates only with trusted model servers.

To configure backend TLS for your inference workloads, attach a BackendTLSPolicy to an InferencePool or GCPInferencePoolImport resource.

For more information, see [Configure backend TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-tls).

## What's next

  * [Customize GKE Inference Gateway configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations)
  * [Configure Body-Based Routing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-body-based-routing)
  * [Serve an LLM with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway)
  * [Use predicted latency-based routing with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-predicted-latency-based-routing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
