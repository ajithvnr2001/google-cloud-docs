---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-body-based-routing/
title: Configure Body-Based Routing \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:08.695741+00:00
---

# Configure Body-Based Routing  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-body-based-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure Body-Based Routing Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Learn how to configure Body-Based Routing, a capability of GKE Inference Gateway that lets you route inference requests by extracting the model name directly from the HTTP request body.

This is particularly useful for applications that adhere to specifications like the OpenAI API, where the model identifier is often embedded within the request payload rather than in headers or URL paths.

### How body-based routing works

GKE Inference Gateway implements Body-Based Routing as an `ext_proc` extension of Envoy proxy. The request flow is designed to integrate seamlessly with your existing Gateway API configurations:

  1. **Request reception** : the Layer 7 load balancer receives an incoming inference request.
  2. **Body parameter extraction** : the Layer 7 load balancer forwards the request to the Body to Header extension. This extension extracts the standard `model` parameter from the HTTP request body.
  3. **Header injection** : the extracted model parameter's value is then injected as a new request header (with the key `X-Gateway-Model-Name`).
  4. **Routing decision** : with the model name now available in a request header, the GKE Inference Gateway can use existing Gateway API `HTTPRoute` constructs to make routing decisions. For example, `HTTPRoute` rules can match against the injected header to direct traffic to the appropriate `InferencePool`.
  5. **Endpoint selection** : the Layer 7 load balancer selects the appropriate `InferencePool` (BackendService) and group of endpoints. It then forwards request and endpoint information to the Endpoint Picker extension for fine-grained endpoint selection within the chosen pool.
  6. **Final routing** : the request is routed to the specific model replica selected by the Endpoint Picker extension.



This process helps ensure that even when model information is deep within the request body, your GKE Inference Gateway can intelligently route traffic to the correct backend services.

### Configure body-based routing

The Body-Based Routing (BBR) extension for GKE Inference Gateway runs as a service that you manage within your Kubernetes cluster. From the perspective of the Layer 7 load balancer, the BBR extension is an external gRPC server. When the load balancer needs to inspect a request body to determine the model name, it makes a gRPC call to the BBR service. The BBR service then processes the request and returns information to the load balancer, such as headers to be injected for routing.

To enable body-based routing, deploy the BBR extension as a Pod and integrate it using `GCPRoutingExtension` and `HTTPRoute` resources.

#### Prerequisites

  * Ensure you have a GKE cluster (version 1.32 or later).

  * Follow the main guide to [configure GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway).




#### Deploy the body-based router

The body-based routing extension is deployed as a Kubernetes Deployment and Service, along with a `GCPRoutingExtension` resource within your cluster. You can use Helm for a simplified installation.

To deploy the required resources for the body-based router, run the following command:
    
    
    helm install body-based-router oci://registry.k8s.io/gateway-api-inference-extension/charts/body-based-routing \
        --set provider.name=gke \
        --set inferenceGateway.name=GATEWAY_NAME
    

Replace `GATEWAY_NAME` with the name of your Gateway resource.

This command deploys the following resources:

  * A Service and a Deployment for the Body-Based Routing extension.
  * A `GCPRoutingExtension` resource and a `GCPHealthCheckPolicy` resource to attach the Body-Based Routing extension to your GKE Gateway resource.



#### Configure `HTTPRoute` for model-aware routing

After the extension is deployed and configured, you can define `HTTPRoute` resources that use the injected header (`X-Gateway-Model-Name`) for routing decisions.

The following is an example `HTTPRoute` manifest for model-aware routing:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: routes-to-llms
    spec:
      parentRefs:
      - name: GATEWAY_NAME
      rules:
      - matches:
        - headers:
          - type: Exact
            name: X-Gateway-Model-Name
            value: chatbot # Matches the extracted model name
          path:
            type: PathPrefix
            value: /
        backendRefs:
        - name: gemma # Target InferencePool for 'chatbot' model
          kind: InferencePool
          group: "inference.networking.k8s.io"
      - matches:
        - headers:
          - type: Exact
            name: X-Gateway-Model-Name
            value: sentiment # Matches another extracted model name
          path:
            type: PathPrefix
            value: /
        backendRefs:
        - name: llama # Target InferencePool for 'sentiment' model
          kind: InferencePool
          group: "inference.networking.k8s.io"
    

To apply this manifest to your cluster, save it as `httproute-for-models.yaml` and run the following command:
    
    
    kubectl apply -f httproute-for-models.yaml
    

**Note:** If you need to access your inference pools from different HTTP origins (domains), you can combine body-based routing extensions with `CORS` filters in the same `HTTPRoute`. For more information, see [Configure Cross-Origin Resource Sharing (CORS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors).

### Considerations and limitations

When planning your Body-Based Routing implementation, consider the following:

  * **Fail-closed behavior:** the Body-Based Routing extension is designed to operate in a "fail-closed" mode. If the extension is unavailable or fails to process a request, it results in an error (for example, a 404 or 503 response code if no default backend is configured) rather than routing incorrectly. Ensure your deployments are highly available to maintain service reliability.

  * **Request body size and streaming:** processing large HTTP request bodies, especially with streaming enabled, can introduce complexities. If the Envoy proxy is forced to stream the request body (typically for bodies larger than 250 KB), it might be unable to inject new headers. This can lead to routing failures (for example, a 404 error if the header matching rules cannot be applied).

  * **Long-term maintenance:** the Body-Based Routing extension runs as a component within your GKE clusters. You are responsible for its lifecycle management, including upgrades, security patches, and ensuring its continued operation.




## What's next

  * [Learn how to customize GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations).
  * [Read more about GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway).
  * [Learn more about the Gateway API](https://gateway-api.sigs.k8s.io/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
