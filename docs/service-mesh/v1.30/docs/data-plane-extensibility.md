---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/data-plane-extensibility/
title: Data plane extensibility with EnvoyFilter \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:26.341764+00:00
---

# Data plane extensibility with EnvoyFilter  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/data-plane-extensibility/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data plane extensibility with EnvoyFilter

You can use the `EnvoyFilter` API to extend data plane capabilities in Cloud Service Mesh that are otherwise not achievable by using other Istio APIs. With the `EnvoyFilter` API, you can customize the Envoy configuration generated from other policies applied to the workloads, like adding filters to the HTTP filter chain.

## Important considerations

  * Note that the API surface is tied to internal implementation details and so special care must be taken when using this feature since incorrect configurations could destabilize the mesh. Only use the `EnvoyFilter` API if other Istio APIs don't suit your needs.
  * The `EnvoyFilter` API is supported with specific restrictions on which fields and extensions may be used for reliability and supportability purposes. For an exhaustive list of supported features in the `EnvoyFilter` API, refer to [Supported features using Istio APIs (managed control plane)](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-managed#envoyfilter).
  * The scope of support Google offers is limited to propagating the user-provided config to the workloads with Envoy sidecars and does not extend to the correctness of the config specified using per-extension APIs.



## Supported API Fields

The `EnvoyFilter` API is supported with the `TRAFFIC_DIRECTOR` control plane implementation only with **limited** support as follows:

  * `targetRefs`: Not supported
  * `configPatches[].applyTo` : only `HTTP_FILTER` is supported
  * `configPatches[].patch.operation`: only `INSERT_FIRST` and `INSERT_BEFORE` when used with the route filter are supported.
  * `configPatches[].patch.value.type_url`: refer to Supported Extensions
  * `configPatches[].patch.filterClass`: Not supported
  * `configPatches[].match.proxy`: Not supported
  * `configPatches[].match.routeConfiguration`: Not supported
  * `configPatches[].match.cluster`: Not supported
  * The following fields are supported for the `INSERT_BEFORE` operation only: 
    * `configPatches[].match.listener`: only `filter` is supported.
    * `configPatches[].match.listener.filter.name`: only `envoy.filters.network.http_connection_manager` is supported.
    * `configPatches[].match.listener.filter.subFilter.name`: only `envoy.filters.http.router` is supported.



## Supported Extensions

Following is the list of supported extensions along with their supported API fields across various [release channels](https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/select-a-release-channel). The API definition and their semantics can be found at the [official Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/http_filters).

### type.googleapis.com/envoy.extensions.filters.http.local_ratelimit.v3.LocalRateLimit

Field | Rapid | Regular | Stable  
---|---|---|---  
`stat_prefix` |  |  |   
`status` |  |  |   
`token_bucket` |  |  |   
`filter_enabled` |  |  |   
`filter_enforced` |  |  |   
`response_headers_to_add` |  |  |   
`request_headers_to_add_when_not_enforced` |  |  |   
`local_rate_limit_per_downstream_connection` |  |  |   
`enable_x_ratelimit_headers` |  |  |   
  
### type.googleapis.com/envoy.extensions.filters.http.grpc_web.v3.GrpcWeb

Field | Rapid | Regular | Stable  
---|---|---|---  
(No fields) |  |  |   
  
### type.googleapis.com/envoy.extensions.filters.http.compressor.v3.Compressor

Field | Rapid | Regular | Stable  
---|---|---|---  
`compressor_library` |  |  |   
`choose_first` |  |  |   
`response_direction_config.common_config.min_content_length` |  |  |   
`response_direction_config.common_config.content_type` |  |  |   
`response_direction_config.common_config.enabled` |  |  |   
`response_direction_config.disable_on_etag_header` |  |  |   
`response_direction_config.remove_accept_encoding_header` |  |  |   
`response_direction_config.uncompressible_response_codes` |  |  |   
`request_direction_config.common_config.min_content_length` |  |  |   
`request_direction_config.common_config.content_type` |  |  |   
`request_direction_config.common_config.enabled` |  |  |   
  
For information on updating your `EnvoyFilter` compressor configuration to be fully supported, see [Modernize EnvoyFilter compressor configurations](https://docs.cloud.google.com/service-mesh/v1.30/docs/migrate/modernize-envoyfilter-compressor).

### type.googleapis.com/envoy.extensions.filters.http.lua.v3.Lua

**Preview — Lua extension**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Field | Rapid | Regular | Stable  
---|---|---|---  
`stat_prefix` |  |  |   
`default_source_code.inline_string`† |  |  |   
  
† **Important Considerations & Restrictions for Inline Lua Scripts:**

  * To ensure security and stability, only a subset of Lua features and Envoy Lua wrappers are permitted. Using unsupported features or exceeding the documented limits in a specific patch results in that patch being dropped and not processed. If all patches within the `EnvoyFilter` use unsupported features or exceed limits, the entire `EnvoyFilter` resource is rejected.
  * Complex Lua scripts can impact performance. Thoroughly test the resource usage of your scripts.



**Unsupported Lua Features:**  
The following Lua features and Envoy-provided Lua wrappers are **not supported** :

  * **Envoy Wrappers** : 
    * `httpCall`
    * `filterContext`
  * **Lua Standard Library** : 
    * **Basic package** : `collectgarbage`, `dofile`, `getmetatable`, `loadfile`, `rawset`, `setfenv`, `setmetatable`
    * **Modules** : `module`
    * **OS package** : `execute`, `remove`, `rename`, `setlocale`
    * **I/O and Debugging libraries** : `io`, `debug`
  * **LuaJIT Extensions** : `ffi`, `jit`



**Script Size and Count Limits:**

  * **Individual Script Size** : A single Lua inline script provided in `default_source_code.inline_string` cannot exceed **50KB**.
  * **Total Script Size** : The total size of all Lua scripts across all EnvoyFilter resources within a single cluster cannot exceed **100KB**.
  * **Patch Count** : The total number of Lua EnvoyFilter `configPatches` across all EnvoyFilter resources within a single cluster is limited to **10**.



## Configuration patch evaluation and partial processing

When you configure an `EnvoyFilter` resource with multiple `configPatches`, Cloud Service Mesh evaluates each patch independently.

  * **Partially valid configurations:** If your `EnvoyFilter` resource contains both valid patches and patches with unsupported fields or errors, the overall resource is accepted. Cloud Service Mesh drops the unsupported or invalid patches and only processes the valid ones. When this occurs, a `Warning` status condition is surfaced on the resource that lists the unsupported fields that caused some patches to be dropped.
  * **Fully invalid configurations:** If none of the `configPatches` in the `EnvoyFilter` are valid, the entire resource is rejected with an error.

**Note:** You must regularly monitor your `EnvoyFilter` resources for warnings. A status of **Accepted** with a **Warning** might indicate that some incorrectly configured patches were dropped from processing, or it could serve as a notice that you are using unsupported fields which you should avoid. 

## Sample Usage

In this tutorial, you'll learn how to use Envoy's built-in local rate limiting to dynamically limit the traffic to a service using the `EnvoyFilter` API.

### Costs

This tutorial uses the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/pricing)



When you finish this tutorial, you can avoid ongoing costs by deleting the resources you created. For more information, see Clean up.

### Before you begin

  * Ensure billing is enabled for your project.
  * [Provision Cloud Service Mesh on a GKE cluster](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane).
  * Clone the repository:
        
        git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples
          cd anthos-service-mesh-samples
        




### Deploy an ingress gateway

  1. Set the current context for `kubectl` to the cluster:

**Note:** Use `--region` instead of `--zone`, if the cluster is a regional cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME  \
             --project=PROJECT_ID \
             --zone=CLUSTER_LOCATION 
         

  2. Create a namespace for your ingress gateway:
         
         kubectl create namespace asm-ingress
         

  3. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.30/docs/check-control-plane-implementation).

Apply the default injection label to the namespace:
         
         kubectl label namespace asm-ingress \
             istio.io/rev- istio-injection=enabled --overwrite
         

  4. Deploy the example gateway in the `anthos-service-mesh-samples` repository:
         
         kubectl apply -n asm-ingress \
             -f docs/shared/asm-ingress-gateway
         

Expected output:
         
         serviceaccount/asm-ingressgateway configured
         service/asm-ingressgateway configured
         deployment.apps/asm-ingressgateway configured
         gateway.networking.istio.io/asm-ingressgateway configured
         




### Deploy the Online Boutique sample application

  1. If you haven't, set the current context for `kubectl` to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME  \
           --project=PROJECT_ID \
           --zone=CLUSTER_LOCATION 
         

  2. Create the namespace for the sample application:
         
         kubectl create namespace onlineboutique
         

  3. Label the `onlineboutique` namespace to automatically inject Envoy proxies:
         
         kubectl label namespace onlineboutique \
            istio.io/rev- istio-injection=enabled --overwrite
         

  4. Deploy the sample app, the `VirtualService` for the frontend, and service accounts for the workloads. For this tutorial, you will deploy [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo), a microservice demo app. 
         
         kubectl apply \
           -n onlineboutique \
           -f docs/shared/online-boutique/virtual-service.yaml
         
         
         kubectl apply \
           -n onlineboutique \
           -f docs/shared/online-boutique/service-accounts
         




### View your services

  1. View the pods in the `onlineboutique` namespace:
         
         kubectl get pods -n onlineboutique
         

Expected output:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         adservice-85598d856b-m84m6               2/2     Running   0          2m7s
         cartservice-c77f6b866-m67vd              2/2     Running   0          2m8s
         checkoutservice-654c47f4b6-hqtqr         2/2     Running   0          2m10s
         currencyservice-59bc889674-jhk8z         2/2     Running   0          2m8s
         emailservice-5b9fff7cb8-8nqwz            2/2     Running   0          2m10s
         frontend-77b88cc7cb-mr4rp                2/2     Running   0          2m9s
         loadgenerator-6958f5bc8b-55q7w           2/2     Running   0          2m8s
         paymentservice-68dd9755bb-2jmb7          2/2     Running   0          2m9s
         productcatalogservice-84f95c95ff-c5kl6   2/2     Running   0          114s
         recommendationservice-64dc9dfbc8-xfs2t   2/2     Running   0          2m9s
         redis-cart-5b569cd47-cc2qd               2/2     Running   0          2m7s
         shippingservice-5488d5b6cb-lfhtt         2/2     Running   0          2m7s
         

All of the pods for your application should be up and running, with a `2/2` in the `READY` column. This indicates that the pods have an Envoy sidecar proxy injected successfully. If it does not show `2/2` after a couple of minutes, visit the [Troubleshooting guide](https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-resources).

  2. Get the external IP, and set it to a variable:
         
         kubectl get services -n asm-ingress
         export FRONTEND_IP=$(kubectl --namespace asm-ingress \
         get service --output jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}' \
         )
         

You see output similar to the following:
         
         NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                      AGE
         asm-ingressgateway   LoadBalancer   10.19.247.233   35.239.7.64   80:31380/TCP,443:31390/TCP,31400:31400/TCP   27m
         
         

  3. Visit the `EXTERNAL-IP` address in your web browser. You should expect to see the Online Boutique shop in your browser.

![online boutique frontend](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/online-boutique.jpeg)




### Apply Rate Limit Config

This section applies an `EnvoyFilter` resource to limit all traffic to the `frontend` service to 5 req/min.

  1. Apply the CR to the `frontend` service:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.istio.io/v1alpha3
         kind: EnvoyFilter
         metadata:
           name: frontend-local-ratelimit
           namespace: onlineboutique
         spec:
           workloadSelector:
             labels:
               app: frontend
           configPatches:
             - applyTo: HTTP_FILTER
               match:
                 context: SIDECAR_INBOUND
                 listener:
                   filterChain:
                     filter:
                       name: "envoy.filters.network.http_connection_manager"
                       subFilter:
                         name: "envoy.filters.http.router"
               patch:
                 operation: INSERT_BEFORE
                 value:
                   name: envoy.filters.http.local_ratelimit
                   typed_config:
                     "@type": type.googleapis.com/udpa.type.v1.TypedStruct
                     type_url: type.googleapis.com/envoy.extensions.filters.http.local_ratelimit.v3.LocalRateLimit
                     value:
                       stat_prefix: http_local_rate_limiter
                       token_bucket:
                         max_tokens: 5
                         tokens_per_fill: 5
                         fill_interval: 60s
                       filter_enabled:
                         runtime_key: local_rate_limit_enabled
                         default_value:
                           numerator: 100
                           denominator: HUNDRED
                       filter_enforced:
                         runtime_key: local_rate_limit_enforced
                         default_value:
                           numerator: 100
                           denominator: HUNDRED
         EOF
         

Expected output:
         
         envoyfilter.networking.istio.io/frontend-local-ratelimit created
         

  2. Verify that the CR status doesn't report any errors:
         
         kubectl get envoyfilter -n onlineboutique frontend-local-ratelimit -o yaml
         

Expected output:
         
         ...
         status:
           conditions:
           - lastTransitionTime: "2025-06-30T14:29:25.467017594Z"
             message: This resource has been accepted. This does not mean it has been propagated
               to all proxies yet
             reason: Accepted
             status: "True"
             type: Accepted
         

  3. Remove the `loadgenerator` deployment as it calls the service multiple times which consumes tokens:
         
         kubectl delete -n onlineboutique deployment loadgenerator
         

Expected output:
         
         deployment.apps/loadgenerator deleted
         

  4. Using `curl`, verify that no more than 5 requests are allowed in 60 sec. The `429` code indicates that the rate limiting is being enforced.
         
         for i in {1..10}; do curl -s http://${FRONTEND_IP} -o /dev/null -w "%{http_code}\n"; sleep 1; done
         

Expected output:
         
         200
         200
         200
         200
         200
         429
         429
         429
         429
         429
         




### Clean up

To avoid incurring continuing charges to your Google Cloud account for the resources used in this tutorial, you can either delete the project or delete the individual resources.

#### Delete the project

**Caution:** Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an appspot.com URL, delete selected resources inside the project instead of deleting the whole project.



In Cloud Shell, delete the project:
    
    
      gcloud projects delete PROJECT_ID
    

#### Delete the resources

  * If you want to keep your cluster and remove the Online Boutique sample:

    1. Delete the application namespaces:
           
           kubectl delete namespace onlineboutique
           

Expected output:
           
           namespace "onlineboutique" deleted
           

    2. Delete the Ingress Gateway namespace:
           
           kubectl delete namespace asm-ingress
           

Expected output:
           
           namespace "asm-ingress" deleted
           

  * If you want to prevent additional charges, delete the cluster:
        
        gcloud container clusters delete CLUSTER_NAME  \
          --project=PROJECT_ID \
          --zone=CLUSTER_LOCATION 
        




## Troubleshooting

See [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-data-plane-extensibility). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
