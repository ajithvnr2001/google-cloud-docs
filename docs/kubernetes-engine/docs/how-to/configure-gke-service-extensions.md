---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions/
title: Customize GKE Gateway traffic using Service Extensions \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:06.062732+00:00
---

# Customize GKE Gateway traffic using Service Extensions  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Customize GKE Gateway traffic using Service Extensions Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how Google Kubernetes Engine (GKE) uses Service Extensions to add custom logic into Cloud Load Balancing.

This page is intended for GKE Identity and account admins and Developers who need to configure custom traffic management logic using Service Extensions.

Before reading this page, ensure that you're familiar with the following:

  * [Basic GKE networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)
  * [GKE Gateway Controllers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller)
  * [GKE GatewayClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities)
  * [Service Extensions overview ](https://docs.cloud.google.com/service-extensions/docs/overview)



## Overview

GKE uses Service Extensions to add custom logic into Cloud Load Balancing. You can use Service Extensions for tasks such as advanced traffic splitting, custom authentication, or request logging.

The GKE Gateway controller supports the following Service Extensions:

  * **GCPRoutingExtension** : this extension adds custom logic into Cloud Load Balancing to control traffic routing.
  * **GCPTrafficExtension** : this extension inserts custom logic to Cloud Load Balancing to modify traffic. This logic is applied to traffic after the service is selected. The load balancer can add or change the headers and payloads of HTTP requests and responses. GCPTrafficExtension does not affect service selection or service security policies.
  * **GCPEdgeExtension** : this extension lets you influence backend service selection and Cloud CDN cache keys by modifying request headers. It is exclusively supported for Global External Managed Load Balancers.
  * **GCPAuthzExtension** : this extension lets you delegate authorization decisions to a custom or third-party authorization engine (such as an external web application firewall) or Identity-Aware Proxy. This extension is used with a GCPAuthzPolicy resource, which enforces access control on traffic entering the Gateway and dictates when the callout to the extension should occur.



An extension attaches to a Gateway. For a single-cluster Gateway, the extension references a Service resource, a GCPWasmPlugin resource, or a GoogleAPIServiceName resource. For a multi-cluster Gateway, the extension references a ServiceImport resource or a GoogleAPIServiceName resource.

  * **Reference a Service resource or a ServiceImport resource** : in this model, you deploy your custom logic as a separate backend application, exposed as a Kubernetes Service. The load balancer makes a callout to this service to process traffic. This approach is versatile and lets you implement custom routing logic or perform traffic manipulation, such as header modification or payload inspection.

  * **Reference a GCPWasmPlugin resource** : for high-performance use cases, you can inject custom, user-written logic directly into the data path of the Google Cloud load balancer by using a WebAssembly (Wasm) module. You define a GCPWasmPlugin resource that points to your Wasm module's image in Artifact Registry. This method is used only with GCPTrafficExtension and GCPEdgeExtension resources and a global external Application Load Balancer

  * **Reference a Google API Service** : you can also reference a Google API service directly by using the `googleAPIServiceName` field within a GCPTrafficExtension or GCPAuthzExtension.




In the following diagram, the GCPRoutingExtension resource is attached to a Gateway and references multiple Services. The extension controls traffic routing to the Services.

![The GCPRoutingExtension resource is attached to a Gateway and
        references a Service. The extension
        controls traffic routing.](https://docs.cloud.google.com/static/kubernetes-engine/images/gcp-routing-extensions.svg)**Figure:** How GCPRoutingExtension works with Gateways

In the following diagram, the GCPTrafficExtension resource is attached to a Gateway and references a Service, a GoogleAPIServiceName, or a GCPWasmPlugin. The extension changes the headers and payloads of requests and responses.

![The GCPTrafficExtension resource is attached to a Gateway and
        references a Service, a GoogleAPIServiceName or a GCPWasmPlugin. The extension
        changes the headers and payloads of requests and responses.](https://docs.cloud.google.com/kubernetes-engine/images/gcp-traffic-extensions.svg)**Figure:** How GCPTrafficExtension works with Gateways

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Compute Engine API, the Network Services API, and the Model Armor API if needed.

Go to [Enable access to APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,modelarmor.googleapis.com,networkservices.googleapis.com) and follow the instructions.

  * For detailed information about the pricing of Google Cloud Service Extensions, see [Pricing](https://cloud.google.com/service-extensions/pricing).

  * Review the required roles and permissions in [ Service Extensions access control](https://docs.cloud.google.com/service-extensions/docs/access-control).

  * Familiarize yourself with the quotas and limits in [ Service Extensions quotas](https://docs.cloud.google.com/service-extensions/docs/quotas).

  * If you intend to use Common Expression Language (CEL) matchers, review the supported attributes and operators in the [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

**Note:** The `request.backend_service_name` and `request.backend_service_project_number` request attributes are not supported.
  * Review restrictions and limitations for Service Extensions.




### GKE Gateway controller requirements

  * Your cluster must use GKE version 1.33 or later.
  * To use the GCPWasmPlugin, your cluster must use GKE version 1.33.3 or later.
  * To use the ServiceImport resource, your cluster must use GKE version 1.34.3 or later.
  * You must have a configured Gateway resource for an [internal multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-internal-multi-cluster-gateway). This resource can be a global external Application Load Balancer, cross-region internal Application Load Balancer, regional external Application Load Balancer, or regional internal Application Load Balancer Gateway.
  * Your cluster must have [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway) enabled.
  * You must have a configured [Gateway resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways). This resource can be a global external Application Load Balancer, regional external Application Load Balancer, or regional internal Application Load Balancer Gateway. If you use a GCPWasmPlugin resource, then you must deploy only a global external Application Load Balancer Gateway.
  * You must have a configured [HTTPRoute resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_http-to-https_redirects).



### Restrictions and limitations

The following table lists the restrictions associated with the configuration of Gateway Service Extensions in GKE:

Category | Restrictions and limitations  
---|---  
**Load Balancer** |  The GCPRoutingExtension is supported for the following load balancers: 

  * Regional external Application Load Balancer (`gke-l7-regional-external-managed` Gateway Class)
  * Regional external Application Load Balancer (`gke-l7-regional-external-managed-mc` Gateway Class)
  * Regional internal Application Load Balancer (`gke-l7-rilb` Gateway Class)
  * Regional internal Application Load Balancer (`gke-l7-rilb-mc` Gateway Class)
  * Cross-region internal Application Load Balancer (`gke-l7-cross-regional-internal-managed-mc` Gateway Class)

The GCPTrafficExtension is supported for the following load balancers: 
  * Regional external Application Load Balancer (`gke-l7-regional-external-managed` Gateway Class)
  * Regional external Application Load Balancer (`gke-l7-regional-external-managed-mc` Gateway Class)
  * Regional internal Application Load Balancer (`gke-l7-rilb` Gateway Class)
  * Regional internal Application Load Balancer (`gke-l7-rilb-mc` Gateway Class)
  * Global external Application Load Balancer (`gke-l7-global-external-managed` Gateway Class)
  * Global external Application Load Balancer (`gke-l7-global-external-managed-mc` Gateway Class)
  * Cross-region internal Application Load Balancer (`gke-l7-cross-regional-internal-managed-mc` Gateway Class)

The GCPEdgeExtension is **exclusively supported** for the Global External Managed Load Balancer (`gke-l7-global-external-managed` Gateway Class).   
**Extension chain and specification** | 

  * For a GCPTrafficExtension, each `ExtensionChain` can have a maximum of 3 `Extensions`.
  * For both GCPRoutingExtension and GCPEdgeExtension, each `ExtensionChain` is limited to 1 `Extension`.
  * All extension types (Traffic, Routing, and Edge) can have a maximum of 5 `ExtensionChains` per resource.

  
**Timeout** | 

  * The timeout for each individual message on the stream within an Extension must be between 10 and 10,000 milliseconds. Default timeout is one second.

  
**MatchCondition** | 

  * Each `MatchCondition` within an `ExtensionChain` is limited to a maximum of 10 `CELExpressions`.
  * The resulting `MatchCondition` string that is sent to the GCE has a character limit of 512.
  * The `CELMatcher` string within a `CELExpression` has a maximum length of 512 characters.
  * For GCPEdgeExtension: 
    * Response attributes (for example, `response.code`) in CELMatcher are not supported.
    * Unsupported request attributes include `backend_service_name` and `backend_service_project_number`.
    * The number of regular expressions is limited to 1.
  * Only `backendRefs` field of kind Service or ServiceImport are supported in `CELExpression`.
  * The `backendRefs` field is not supported with the `gke-l7-global-external-managed` and `gke-l7-global-external-managed-mc Gateway Classes`

  
**Header** | 

  * The `ForwardHeaders` list in an `Extension` can contain a maximum of 50 HTTP header names.

  
**Metadata** | 

  * The `Metadata` map in an `Extension` can have a maximum of 16 properties.
  * Keys within the `Metadata` map must be between 1 and 63 characters long.
  * Values within the `Metadata` map must be between 1 and 1,023 characters long.

  
**Event** | 

  * `SupportedEvents` is required for a GCPTrafficExtension.
  * `SupportedEvents` is optional for a GCPRoutingExtension.
  * For GCPEdgeExtension, the `SupportedEvents` list must contain only `RequestHeaders`.
  * If unspecified, `RequestHeaders` event is assumed as supported.

  
**RequestBodySendMode** | 

  * The `RequestBodySendMode` can be used only with backendRefs of kind Service or ServiceImport.
  * The `RequestBodySendMode` can be set only if the `SupportedEvents` include `RequestBody`.
  * If `SupportedEvents` include `RequestBody`, but `RequestBodySendMode` is unset, the default value `Streamed` is used.
  * If `RequestBodySendMode` set to `FullDuplexStreamed`, `SupportedEvents` must include both `RequestBody` and `RequestTrailers`.
  * For a GCPTrafficExtension, only `FullDuplexStreamed` is supported.

  
**ResponseBodySendMode** | 

  * The `ResponseBodySendMode` field is supported for GCPTrafficExtension only.
  * The `ResponseBodySendMode` can be used only with backendRefs of kind Service or ServiceImport.
  * The field can be set only if the `SupportedEvents` include `ResponseBody`.
  * If `SupportedEvents` include `ResponseBody`, but `ResponseBodySendMode` is unset, the default value `Streamed` is used.
  * When this field is set to `FullDuplexStreamed`, `SupportedEvents` must include both `ResponseBody` and `ResponseTrailers`.

  
**Resource references** | 

  * For GCPEdgeExtension, the **only supported backend kind is GCPWasmPlugin**.
  * The `googleAPIServiceName` field is **not supported** for GCPEdgeExtension.
  * The Gateway, Edge extension, and plugin must all reside in the **same namespace**.

  
**GCPWasmPlugin** | 

  * The GCPWasmPlugin field is supported for GCPTrafficExtension and GCPEdgeExtension only.
  * Extensions with GCPWasmPlugin don't support the following fields: 
    * `authority`
    * `timeout`
    * `metadata`
    * `requestBodySendMode`
    * `responseBodySendMode`
  * Extensions with GCPWasmPlugin support only `RequestHeaders`, `RequestBody`, `ResponseHeaders`, and `ResponseBody` events.

  
**GCPAuthzPolicy and GCPAuthzExtension** | 

  * For a given Gateway, there can be only one authorization policy with a `CUSTOM` action.
  * An authorization policy with a `CUSTOM` action is limited to exactly one custom extension.
  * You are limited to a total of five resource-level authorization policies per Gateway.
  * You are limited to 10 GCPAuthzExtension resources and 10 GCPAuthzPolicy resources per project.
  * A single GCPAuthzPolicy resource can point to up to 100 forwarding rules.
  * The Gateway, the GCPAuthzPolicy, and the GCPAuthzExtension must all reside in the same namespace. Cross-namespace references are not allowed.
  * GCPAuthzExtension cannot influence backend service selection.
  * GCPAuthzExtension receives only the request headers, not the body or any part of the response.
  * IAP is supported only for regional load balancers with GCPAuthzExtension.
  * When you use IAP with GCPAuthzExtension, IAM permissions cannot be set on the forwarding rule. Only project-level or organization-level permissions are allowed. For more information, see [Apply permissions to resources](https://docs.cloud.google.com/iap/docs/auth-policies#apply_permissions_to_resources).

  
**`googleAPIServiceName`** | 

  * The `googleAPIServiceName` field is supported for GCPTrafficExtension and GCPAuthzExtension.
  * The `authority` must not be set, if `googleAPIServiceName` is set.
  * Exactly one of either `backendRef` or `googleAPIServiceName` can be set for an Extension.

  
**`backendRef`** |  When you reference a Service that uses the `backendRef` in an Extension, you must meet the following conditions: 

  * Must use HTTP2 as its `appProtocol`.
  * Must be in the same namespace as the Extension and the Gateway that's referenced by the Extension.
  * Can't use [IAP](https://googlecloudplatform.github.io/gke-gateway-api/#identityawareproxyconfig).
  * Can't use [Google Cloud Armor](https://googlecloudplatform.github.io/gke-gateway-api/#gcpbackendpolicyconfig) security policies.
  * Can't use [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview).
  * Must set exactly one of either `backendRef` or `googleAPIServiceName` for an `Extension`.
  * Must set `authority`, if `backendRef` is set and `kind` is Service.

  
**`observabilityMode`** |  Field `observabilityMode` field can be set on the `Extension` with the following limitations: 

  * Supported for GKE clusters on version 1.35.0-gke.3047000 or later.
  * Supported by GCPTrafficExtension and GCPRoutingExtension resources attached to gateways with regional Gateway Classes.
  * Enabled `observabilityMode` is only supported when both the `requestBodySendMode` and `responseBodySendMode` fields are not set, or set to `Streamed`.

  
  
## Refer to a Service

In Service Extensions, you can refer to a Service that hosts the custom logic that you want the load balancer to execute. Gateways don't have Service Extensions by default.

To configure GKE Service Extensions, follow these steps:

  1. Deploy a backend callout Service: create a Kubernetes Service that represents the backend service for custom logic execution. The load balancer invokes this service.

  2. Configure Service Extensions: use the appropriate extension based on your load balancer type.

     1. GCPRoutingExtension for regional Gateways: use this extension for regional external Application Load Balancer and regional internal Application Load Balancer to implement custom routing logic within the region.

     2. GCPTrafficExtension for global external, regional external, and internal Gateways: use this extension for global external Application Load Balancer, regional external Application Load Balancer, and regional internal Application Load Balancer to perform traffic manipulation, such as header modification or payload inspection, across various load balancer types.




### Deploy a backend callout service

A callout service implements custom logic for Gateway Service Extensions in GKE. The Gateway invokes these backend applications, based on GCPTrafficExtension or GCPRoutingExtension configurations, to modify or route traffic.

You deploy a callout service to add custom logic to your Gateway. This separate service handles custom processing, such as header manipulation, payload transformations, or traffic routing.

To deploy a service that can function as a callout for your Gateway, perform the following steps:

  1. (Optional) [Create a secret for TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret): This command creates a Kubernetes secret of type TLS that contains your TLS certificate and private key.

To create the TLS secret for your callout service, replace the following:

     * `SECRET_NAME`: the secret name for your callout service
     * `path-to-cert`: the file paths to your certificate
     * `path-to-key`: the file paths to your key
  2. To verify that the secret was added, run the following command:
         
         kubectl get secrets SECRET_NAME
         

Replace `SECRET_NAME` with the secret name for your callout service.

The output should be similar to the following:
         
         NAME            TYPE                DATA   AGE
         SECRET_NAME     kubernetes.io/tls   2      12s
         

  3. Define Deployment and Service resources.

You must define the following:

     * **Deployment** : to manage the application pods that contain the custom logic for your Service Extensions.
     * **Service** : to expose the application pods that are managed by the Deployment as a network service.
     1. Create a sample manifest `extension-service-app.yaml` that has Deployment and Service definitions:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: extension-service-app
            spec:
              selector:
                matchLabels:
                  app: store
              replicas: 1
              template:
                metadata:
                  labels:
                    app: store
                spec:
                  containers:
                  - name: serviceextensions
                    image: us-docker.pkg.dev/service-extensions-samples/callouts/python-example-basic:public-image-e42d951
                    ports:
                    - containerPort: 8080
                    - containerPort: 443
                    volumeMounts:
                    - name: certs
                      mountPath: "/etc/certs/"
                      readOnly: true
                    env:
                    - name: POD_NAME
                      valueFrom:
                        fieldRef:
                          fieldPath: metadata.name
                    - name: NAMESPACE
                      valueFrom:
                        fieldRef:
                          fieldPath: metadata.namespace
                    - name: TLS_SERVER_CERT_PATH
                      value: "/etc/certs/path-to-cert"
                    - name: TLS_SERVER_PRIVKEY
                      value: "/etc/certs/path-to-key"
                    resources:
                      requests:
                        cpu: 10m
                  volumes:
                  - name: certs
                    secret:
                      secretName: SECRET_NAME
                      optional: false
            ---
            apiVersion: v1
            kind: Service
            metadata:
              name: extension-service
            spec:
              ports:
              - port: 443
                targetPort: 443
                appProtocol: HTTP2
              selector:
                app: store
            

Replace the following:

        * `POD_NAME`: the name of your Pod.
        * `SECRET_NAME`: the secret name for your callout service.
        * `TLS_SERVER_CERT_PATH`: the path to the TLS server certificate within the Pod.
        * `TLS_SERVER_PRIVKEY`: the path to the TLS server private key within the Pod.
     2. Apply the `extension-service-app.yaml` manifest:
            
            kubectl apply -f extension-service-app.yaml
            

  4. Verify your configuration:

     1. Verify that the application was deployed:
            
            kubectl get pod --selector app=store
            

After the application starts running, the output is similar to the following:
            
            NAME                                     READY   STATUS    RESTARTS   AGE
            extension-service-app-85f466bc9b-b5mf4   1/1     Running   0          7s
            

     2. Verify that the Service was deployed:
            
            kubectl get service extension-service
            

The output is similar to the following, which shows a Service for each store Deployment:
            
            NAME                TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
            extension-service   ClusterIP   34.118.225.9   <none>        443/TCP   2m40s
            




### Configure Service Extensions

You can configure either a GCPRoutingExtension or a GCPTrafficExtension to customize your traffic flow.

#### Configure the GCPRoutingExtension for regional Gateways

You can reroute traffic by using a GCPRoutingExtension. To configure a GCPRoutingExtension, update the HTTPRoute to specify the requests for the `service-extensions.com` host.

  1. Update HTTPRoute. Modify your HTTPRoute to include hostnames or paths that will trigger the routing extension.

     1. Save the following sample manifest as the `store-route.yaml` file:
            
            kind: HTTPRoute
            apiVersion: gateway.networking.k8s.io/v1
            metadata:
              name: store
            spec:
              parentRefs:
              - kind: Gateway
                name:GATEWAY_NAME
              hostnames:
              - "store.example.com"
              - "service-extensions.example.com"
              rules:
              - backendRefs:
                - name: store-v1
                  port: 8080
              - matches:
                - headers:
                  - name: env
                    value: canary
                backendRefs:
                - name: store-v2
                  port: 8080
              - matches:
                - path:
                    value: /de
                backendRefs:
                - name: store-german
                  port: 8080
            

Replace `GATEWAY_NAME` with the name of your Gateway.

     2. Apply the `store-route.yaml` manifest:
            
            kubectl apply -f store-route.yaml
            

  2. Define the GCPRoutingExtension.

     1. Save the GCPRoutingExtension configuration in the sample `gcp-routing-extension.yaml` file:
            
            kind: GCPRoutingExtension
            apiVersion: networking.gke.io/v1
            metadata:
              name: my-gateway-extension
              namespace: default
            spec:
              targetRefs:
              - group: "gateway.networking.k8s.io"
                kind: Gateway
                name: GATEWAY_NAME
              extensionChains:
              - name: chain1
                matchCondition:
                  celExpressions:
                  - celMatcher: request.path.contains("serviceextensions")
                extensions:
                - name: ext1
                  authority: "myext.com"
                  timeout: 1s
                  backendRef:
                    group: ""
                    kind: Service
                    name: extension-service
                    port: 443
            

Replace `GATEWAY_NAME` with the name of your Gateway.

     2. Apply the sample manifest to your cluster:
            
            kubectl apply -f gcp-routing-extension.yaml
            

  3. Verify the configuration of the GCPRoutingExtension and its binding to the Gateway.

     1. Check the GCPRoutingExtension deployment:
            
            kubectl describe gcproutingextension my-gateway-extension
            

The output is similar to the following:
            
            Name:         my-gateway-extension
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPRoutingExtension
            Metadata:
              Creation Timestamp:  2025-03-02T17:12:30Z
              Generation:        1
              Resource Version:  31283253
              UID:               ec8efaa0-d8e7-4e1b-9fd4-0ae0ef3c74d0
            Spec:
              Extension Chains:
                Extensions:
                  Authority:    myext.com
                  Backend Ref:
                    Group:
                    Kind: Service
                    Name: extension-service
                    Port: 443
                  Name:       ext1
                  Timeout:    1s
                Match Condition:
                  Cel Expressions:
                    Cel Matcher: request.path.contains("serviceextensions")
                Name:  chain1
              Target Refs:
                Group: gateway.networking.k8s.io
                Kind: Gateway
                Name: GATEWAY_NAME
            Events:  <none>
            

The output displays the details of the GCPRoutingExtension, which is named `my-gateway-extension`, within the default namespace. The output shows the `Spec` field, which contains the definition of how the extension should behave.

     2. Verify the Gateway binding:

        1. Confirm that the GCPRoutingExtension is bound to the Gateway. This might take a few minutes:
               
               kubectl describe gateway GATEWAY_NAME
               

Replace `GATEWAY_NAME` with the name of your Gateway.

The output is similar to the following:
               
               Name:         GATEWAY_NAME
               Namespace:    default
               Labels:       none
               Annotations:  networking.gke.io/addresses: /projects/1234567890/regions/us-central1/addresses/test-hgbk-default-internal-http-5ypwen3x2gcr
                             networking.gke.io/backend-services:
                               /projects/1234567890/regions/us-central1/backendServices/test-hgbk-default-extension-service-443-rduk21fwhoj0, /projects/1234567890/re...
                             networking.gke.io/firewalls: /projects/1234567890/global/firewalls/test-hgbk-l7-default-us-central1
                             networking.gke.io/forwarding-rules: /projects/1234567890/regions/us-central1/forwardingRules/test-hgbk-default-internal-http-qn7dk9i9zm73
                             networking.gke.io/health-checks:
                               /projects/1234567890/regions/us-central1/healthChecks/test-hgbk-default-extension-service-443-rduk21fwhoj0, /projects/1234567890/regio...
                             networking.gke.io/last-reconcile-time: 2025-03-02T17:15:02Z
                             networking.gke.io/lb-route-extensions:
                               /projects/1234567890/locations/us-central1/lbRouteExtensions/test-hgbk-default-internal-http-lwh0op4qorb0
                             networking.gke.io/lb-traffic-extensions:
                             networking.gke.io/ssl-certificates:
                             networking.gke.io/target-http-proxies:
                               /projects/1234567890/regions/us-central1/targetHttpProxies/test-hgbk-default-internal-http-2jzr7e3xclhj
                             networking.gke.io/target-https-proxies:
                             networking.gke.io/url-maps: /projects/1234567890/regions/us-central1/urlMaps/test-hgbk-default-internal-http-2jzr7e3xclhj
               API Version:  gateway.networking.k8s.io/v1
               Kind:         Gateway
               Metadata:
                 Creation Timestamp:  2025-03-02T16:37:50Z
                 Finalizers:
                 gateway.finalizer.networking.gke.io
                 Generation:        1
                 Resource Version:  31284863
                 UID:               fd512611-bad2-438e-abfd-5619474fbf31
               ...
               

The output shows the annotations, which GKE uses to store the links between the Gateway and the underlying Google Cloud resources. The `networking.gke.io/lb-route-extensions` annotation confirms the binding of the gateway to the GCPRoutingExtension.

        2. Check the extension status by confirming that the GCPRoutingExtension has a `Programmed` status with the `ProgrammingSucceeded` reason. This command might take a few minutes.
               
               kubectl describe gcproutingextension my-gateway-extension
               

The output is similar to the following:
               
               Name:         my-gateway-extension
               Namespace:    default
               Labels:       <none>
               Annotations:  <none>
               API Version:  networking.gke.io/v1
               Kind:         GCPRoutingExtension
               Metadata:
                 Creation Timestamp:  2025-03-02T17:12:30Z
                 Generation:          1
                 Resource Version:    31284378
                 UID:                 ec8efaa0-d8e7-4e1b-9fd4-0ae0ef3c74d0
               Spec:
                 Extension Chains:
                   Extensions:
                     Authority:  myext.com
                     Backend Ref:
                       Group:
                       Kind:   Service
                       Name:   extension-service
                       Port:   443
                     Name:     ext1
                     Timeout:  1s
                   Match Condition:
                     Cel Expressions:
                       Cel Matcher:  request.path.contains("serviceextensions")
                   Name:             chain1
                 Target Refs:
                   Group:  gateway.networking.k8s.io
                   Kind:   Gateway
                   Name:   GATEWAY_NAME
               Status:
                 Ancestors:
                   Ancestor Ref:
                     Group:      gateway.networking.k8s.io
                     Kind:       Gateway
                     Name:       GATEWAY_NAME
                     Namespace:  default
                   Conditions:
                     Last Transition Time:  2025-03-02T17:14:15Z
                     Message:
                     Reason:                Accepted
                     Status:                True
                     Type:                  Accepted
                     Last Transition Time:  2025-03-02T17:14:15Z
                     Message:
                     Reason:                ProgrammingSucceeded
                     Status:                True
                     Type:                  Programmed
                   Controller Name:         networking.gke.io/gateway
               Events:
                 Type    Reason  Age                From                   Message
                 ----    ------  ----               ----                   -------
                 Normal  ADD     2m31s              sc-gateway-controller  default/my-gateway-extension
               Normal  SYNC    51s (x2 over 98s)  sc-gateway-controller  Attachment of GCPRoutingExtension "default/my-gateway-extension" to AncestorRef {Group:       "gateway.networking.k8s.io",
               Kind:        "Gateway",
               Namespace:   "default",
               Name:        GATEWAY_NAME,
               SectionName: nil,
               Port:        nil} was a success
                 Normal  SYNC    23s           sc-gateway-controller  Reconciliation of GCPRoutingExtension "default/my-gateway-extension" to AncestorRef {Group:       "gateway.networking.k8s.io",
               Kind:        "Gateway",
               Namespace:   "default",
               Name:        GATEWAY_NAME,
               SectionName: nil,
               Port:        nil} was a success
               

The `Status.Conditions` field shows a `Programmed` condition with `Status: True` and `Reason: ProgrammingSucceeded`. This information confirms that the extension was successfully applied.

  4. Send traffic to your application.

After your Gateway, Route, and application are deployed in your cluster, you can pass traffic to your application.

     1. To access your application, you need to find the IP address of your Gateway.

In your terminal, use the following command:
            
            kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"
            

Replace `GATEWAY_NAME` with the name of your Gateway.

This command outputs the Gateway's IP address. In the follow-up commands, replace `GATEWAY_IP_ADDRESS` with the IP address from the output.

     2. Test the path update by going to the `serviceextensions` version of the store service at `store.example.com/serviceextensions`:
            
            curl http://store.example.com/serviceextensions --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
            

The output is similar to the following:
            
            {
            "cluster_name": "gke1",
            "host_header": "service-extensions.com",
            "metadata": "store-v1",
            "pod_name": "store-v1-5d9554f847-cvxpd",
            "pod_name_emoji": "💇🏼‍♀️",
            "project_id": "gateway-demo",
            "timestamp": "2025-03-15T12:00:00",
            "zone": "us-central1-c"
            }
            




#### Configure the GCPTrafficExtension

You can use a GCPTrafficExtension to use advanced traffic management capabilities within your Google Cloud environment. You can configure this extension across global external Application Load Balancers, regional external Application Load Balancers, and regional internal Application Load Balancers. You can use GCPTrafficExtension to implement custom HTTP request and response logic, sophisticated routing, transformations, and security policies.

  1. Update HTTPRoute. Modify your HTTPRoute to include hostnames or paths that will trigger the traffic extension.

     1. Save the following sample manifest as the `store-route.yaml` file:
            
            kind: HTTPRoute
            apiVersion: gateway.networking.k8s.io/v1
            metadata:
              name: store
            spec:
              parentRefs:
              - kind: Gateway
                name: GATEWAY_NAME
              hostnames:
              - "store.example.com"
              - "service-extensions.example.com"
              rules:
              - backendRefs:
                - name: store-v1
                  port: 8080
              - matches:
                - headers:
                  - name: env
                    value: canary
                backendRefs:
                - name: store-v2
                  port: 8080
              - matches:
                - path:
                    value: /de
                backendRefs:
                - name: store-german
                  port: 8080
            

Replace `GATEWAY_NAME` with the name of your Gateway, such as `internal-http`, `external-http`, or `global-external-http`.

     2. Apply the `store-route.yaml` manifest to your cluster:
            
            kubectl apply -f store-route.yaml
            

  2. Define the GCPTrafficExtension.

     1. Save the GCPTrafficExtension configuration to the sample `gcp-traffic-extension.yaml` file:
            
            kind: GCPTrafficExtension
            apiVersion: networking.gke.io/v1
            metadata:
            name: my-traffic-extension
            namespace: default
            spec:
            targetRefs:
            - group: "gateway.networking.k8s.io"
              kind: Gateway
              name: GATEWAY_NAME
            extensionChains:
            - name: chain1
              matchCondition:
                celExpressions:
                - celMatcher: request.path.contains("serviceextensions")
              extensions:
              - name: ext1
                authority: "myext.com"
                timeout: 1s
                backendRef:
                  group: ""
                  kind: Service
                  name: extension-service
                  port: 443
                supportedEvents:
                  - RequestHeaders
                  - RequestBody
                  - ResponseHeaders
                  - ResponseBody
            

Replace `GATEWAY_NAME` with the name of your Gateway, as `internal-http`, `external-http`, or `global-external-http`.

     2. Apply the sample manifest to your cluster:
            
            kubectl apply -f gcp-traffic-extension.yaml
            

  3. Verify the configuration of the GCPTrafficExtension and its binding to the Gateway.

     1. Check the GCPTrafficExtension deployment:
            
            kubectl describe gcptrafficextension my-traffic-extension
            

The output is similar to the following:
            
            Name:         my-traffic-extension
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPTrafficExtension
            Metadata:
              Creation Timestamp:  2025-03-02T17:12:30Z
              Generation:        1
              Resource Version:  31283253
              UID:               ec8efaa0-d8e7-4e1b-9fd4-0ae0ef3c74d0
            Spec:
              Extension Chains:
                Extensions:
                  Authority:    myext.com
                  Backend Ref:
                    Group:
                    Kind: Service
                    Name: extension-service
                    Port: 443
                  Name:       ext1
                  Timeout:    1s
                Match Condition:
                  Cel Expressions:
                    Cel Matcher: request.path.contains("serviceextensions")
                Name:  chain1
              Target Refs:
                Group: gateway.networking.k8s.io
                Kind: Gateway
                Name: GATEWAY_NAME
            Events:  <none>
            

The output displays the details of the GCPTrafficExtension named `my-traffic-extension` within the default namespace. It shows the `Spec` field, which contains the definition of how the extension should behave.

     2. Verify the Gateway binding:

Confirm that the GCPTrafficExtension is bound to the Gateway. This command might take a few minutes to complete:
            
            kubectl describe gateway GATEWAY_NAME
            

The output is similar to the following:
            
            Name:         GATEWAY_NAME
            Namespace:    default
            Labels:       <none>
            Annotations:  networking.gke.io/addresses: /projects/1234567890/regions/us-central1/addresses/test-hgbk-default-internal-http-5ypwen3x2gcr
                          networking.gke.io/backend-services:
                            /projects/1234567890/regions/us-central1/backendServices/test-hgbk-default-extension-service-443-rduk21fwhoj0, /projects/1234567890/re...
                          networking.gke.io/firewalls: /projects/1234567890/global/firewalls/test-hgbk-l7-default-us-central1
                          networking.gke.io/forwarding-rules: /projects/1234567890/regions/us-central1/forwardingRules/test-hgbk-default-internal-http-qn7dk9i9zm73
                          networking.gke.io/health-checks:
                            /projects/1234567890/regions/us-central1/healthChecks/test-hgbk-default-extension-service-443-rduk21fwhoj0, /projects/1234567890/regio...
                          networking.gke.io/last-reconcile-time: 2025-03-02T17:15:02Z
                          networking.gke.io/lb-traffic-extensions:
                            /projects/1234567890/locations/us-central1/lbTrafficExtensions/test-hgbk-default-internal-http-lwh0op4qorb0
                          networking.gke.io/ssl-certificates:
                          networking.gke.io/target-http-proxies:
                            /projects/1234567890/regions/us-central1/targetHttpProxies/test-hgbk-default-internal-http-2jzr7e3xclhj
                          networking.gke.io/target-https-proxies:
                          networking.gke.io/url-maps: /projects/1234567890/regions/us-central1/urlMaps/test-hgbk-default-internal-http-2jzr7e3xclhj
            API Version:  gateway.networking.k8s.io/v1
            Kind:         Gateway
            Metadata:
              Creation Timestamp:  2025-03-02T16:37:50Z
              Finalizers:
                gateway.finalizer.networking.gke.io
              Generation:        1
              Resource Version:  31284863
              UID:               fd512611-bad2-438e-abfd-5619474fbf31
            ...
            

The output shows the annotations, which GKE uses to store the links between the Gateway and the underlying Google Cloud resources. The `networking.gke.io/lb-traffic-extensions` annotation confirms the binding.

     3. Check the extension status:

To check the extension status of GCPTrafficExtension, run the following command:
            
            kubectl describe gcptrafficextension my-traffic-extension
            

Confirm that the GCPTrafficExtension has a `Programmed` status with the `ProgrammingSucceeded` reason. The command might take a few minutes to complete.

The GCPTrafficExtension resource output is similar to the following:
            
            Name:         my-traffic-extension
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPTrafficExtension
            Metadata:
              Creation Timestamp:  2025-03-02T17:12:30Z
              Generation:          1
              Resource Version:    31284378
              UID:                 ec8efaa0-d8e7-4e1b-9fd4-0ae0ef3c74d0
            Spec:
              Extension Chains:
                Extensions:
                  Authority:  myext.com
                  Backend Ref:
                    Group:
                    Kind:   Service
                    Name:   extension-service
                    Port:   443
                  Name:     ext1
                  Timeout:  1s
                Match Condition:
                  Cel Expressions:
                    Cel Matcher:  request.path.contains("serviceextensions")
                Name:             chain1
              Target Refs:
                Group:  gateway.networking.k8s.io
                Kind:   Gateway
                Name:   GATEWAY_NAME
            Status:
              Ancestors:
                Ancestor Ref:
                  Group:      gateway.networking.k8s.io
                  Kind:       Gateway
                  Name:       GATEWAY_NAME
                  Namespace:  default
                Conditions:
                  Last Transition Time:  2025-03-02T17:14:15Z
                  Message:
                  Reason:                Accepted
                  Status:                True
                  Type:                  Accepted
                  Last Transition Time:  2025-03-02T17:14:15Z
                  Message:
                  Reason:                ProgrammingSucceeded
                  Status:                True
                  Type:                  Programmed
                Controller Name:         networking.gke.io/gateway
            Events:
              Type    Reason  Age                From                   Message
              ----    ------  ----               ----                   -------
              Normal  ADD     2m31s              sc-gateway-controller  default/my-traffic-extension
              Normal  SYNC    51s (x2 over 98s)  sc-gateway-controller  Attachment of GCPTrafficExtension "default/my-gateway-extension" to AncestorRef {Group:       "gateway.networking.k8s.io",
              Kind:        "Gateway",
              Namespace:   "default",
              Name:        GATEWAY_NAME,
              SectionName: nil,
              Port:        nil} was a success
              Normal  SYNC    23s           sc-gateway-controller  Reconciliation of GCPTrafficExtension "default/my-traffic-extension" to AncestorRef {Group:       "gateway.networking.k8s.io",
              Kind:        "Gateway",
              Namespace:   "default",
              Name:        GATEWAY_NAME,
              SectionName: nil,
              Port:        nil} was a success
            

The `Status.Conditions` field shows a `Programmed` condition with `Status: True` and `Reason: ProgrammingSucceeded`. This information confirms that the extension was successfully applied.

  4. Send traffic to your application.

After your Gateway, Route, and application are deployed in your cluster, you can pass traffic to your application.

     1. To access your application, you need to find the IP address of your Gateway.

In your terminal, use the following command:
            
            kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"
            

Replace `GATEWAY_NAME` with the name of your Gateway.

This command outputs the Gateway's IP address. In the follow-up commands, replace `GATEWAY_IP_ADDRESS` with the IP address from the output.

     2. Test the path update by going to the `serviceextensions` version of the store service at `store.example.com/serviceextensions`:
            
            curl http://store.example.com/serviceextensions --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
            

The output is similar to the following:
            
            {
            *   Request completely sent off
            < HTTP/1.1 200 OK
            < server: Werkzeug/2.3.7 Python/3.11.3
            < date: Sun, 02 Mar 2025 16:58:10 GMT
            < content-type: application/json
            < access-control-allow-origin: *
            < hello: service-extensions
            < via: 1.1 google
            < transfer-encoding: chunked
            }
            




#### Configure the GCPAuthzExtension resource

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use a GCPAuthzExtension with a GCPAuthzPolicy to enforce complex authorization decisions by delegating them to an external service or Identity-Aware Proxy (IAP).

  1. Define the GCPAuthzExtension:

You can configure the GCPAuthzExtension to reference either a custom extension service or IAP as a callout service.

     * **Option 1: Reference a custom extension service**

       1. Save the GCPAuthzExtension configuration to the sample `gcp-authz-extension.yaml` file:
    
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzExtension
    metadata:
      name: my-authz-ext
      namespace: default
    spec:
      backendRef:
        kind: Service
        name: "${authz-service}"
      forwardHeaders:
      - Authorization
      failOpen: false
      timeout: "0.1s"
      wireFormat: EXT_PROC_GRPC
    

In the preceding example, `"${authz-service}"` is an extension service, which must be present in the same namespace as GCPAuthzPolicy.

       1. Apply the manifest:
    
    kubectl apply -f gcp-authz-extension.yaml
    

     * **Option 2: Reference IAP as a custom callout service**

You can also configure IAP as a custom callout service by specifying `iap.googleapis.com` in the `googleAPIServiceName` field:

       1. Save the GCPAuthzExtension configuration to the sample `authz-extension-iap.yaml` file:
    
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzExtension
    metadata:
      name: my-authz-ext-iap
      namespace: default
    spec:
      googleAPIServiceName: iap.googleapis.com
      timeout: 50ms
      failOpen: false
    

       1. Apply the manifest:
    
    kubectl apply -f authz-extension-iap.yaml
    

**Note:** IAP is supported only for regional load balancers with GCPAuthzExtension. When you configure IAP with GCPAuthzExtension, IAM permissions cannot be set on the forwarding rule. Only project-level or organization-level permissions are allowed. For more information, see [Apply permissions to resources](https://docs.cloud.google.com/iap/docs/auth-policies#apply_permissions_to_resources).
  2. Define the GCPAuthzPolicy:

The GCPAuthzPolicy targets the Gateway and specifies the action to take on matching traffic:

     * **Set up a`CUSTOM` authorization policy**:

The `CUSTOM` action delegates the authorization decision to the extension that you created in the previous step.

       1. Save the following manifest to `gcp-authz-policy.yaml`:
              
              apiVersion: networking.gke.io/v1
              kind: GCPAuthzPolicy
              metadata:
                name: my-gateway-authz
                namespace: default
              spec:
                enforcementLevel: L7
                targetRefs:
                - group: gateway.networking.k8s.io
                  kind: Gateway
                  name: "GATEWAY_NAME"
                rules:
                - from:
                    sources:
                    - principals:
                      - principal_selector: CLIENT_CERT_URI_SANS
                        principal:
                          exact: "spiffee://cluster.local/ns1/pod1"
                - to:
                    operations:
                    - paths:
                      - exact: "/api/secure-endpoint"
                action: CUSTOM
                customProvider:
                  authzExtension:
                    extensionRefs:
                    - group: networking.gke.io
                      kind: GCPAuthzExtension
                      name: my-authz-ext
              

Replace `GATEWAY_NAME` with the name of your Gateway.

       2. Apply the manifest:
              
              kubectl apply -f gcp-authz-policy.yaml
              




## Refer to a GCPWasmPlugin resource

You can inject custom logic directly into the load balancer's data path by using a GCPWasmPlugin with a GCPTrafficExtension or GCPEdgeExtension. This method lets you deploy custom traffic management capabilities packaged as a Wasm module.

To configure GKE Service Extensions, follow these steps:

  1. Deploy a GCPWasmPlugin: create and deploy a GCPWasmPlugin CustomResourceDefinition (CRD) that contains the custom code for your [Wasm](https://webassembly.org/) module. You can use GCPWasmPlugin with GCPTrafficExtension or GCPEdgeExtension for the `gke-l7-global-external-managed` GatewayClass.

  2. Configure service extensions: configure one of the following extensions with GCPWasmPlugin:

     * GCPTrafficExtension
     * GCPEdgeExtension



### Deploy a GCPWasmPlugin

The GCPWasmPlugin lets you inject custom, user-written logic directly into the data path of the Google Cloud load balancer. The GCPWasmPlugin resource points to the Wasm module's image in Artifact Registry, which is then executed by the load balancer.

Before you continue with the following steps, ensure that you have uploaded your Wasm module to an Artifact Registry repository. For more information, see [Prepare the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code).

To deploy a GCPWasmPlugin resource, complete the following steps:

  1. Save the following manifest as `wasm-plugin.yaml`:
         
         kind: GCPWasmPlugin
         apiVersion: networking.gke.io/v1
         metadata:
           name: gcp-wasm-plugin
         spec:
           versions:
           - name: wasm-plugin-version
             description: "Test wasm plugin version"
             image: "us-docker.pkg.dev/service-extensions-samples/plugins/local-reply:main"
             weight: 1000000
           logConfig:
             enabled: true
             # Configures the sampling rate of activity logs.
             # The value of the field must be in range [0, 1e6].
             sampleRate: 1000000
             # Specifies the lowest level of logs that are exported to Cloud Logging.
             minLogLevel: INFO
         

Note the following:

     * `spec.versions.name`: the version name must be unique within the GCPWasmPlugin resource. You can list up to 10 versions, and only one version must have a non-zero weight.
     * `spec.versions.image`: references the image containing the plugin code that is stored in Artifact Registry.
     * `spec.versions.weight`: specifies the weight of the plugin version. The weight must be a number between 0 and 1,000,000, inclusive.
     * `spec.logConfig`: specifies whether to enable Cloud Logging for this plugin. If the value isn't specified, Cloud Logging is disabled by default.
     * `spec.logConfig.sampleRate`: configures the sampling rate of activity logs. The rate must be a number between 0 and 1,000,000, inclusive. If unspecified when Cloud Logging is enabled, the default value is `1,000,000` (100% of requests are logged).
     * `spec.logConfig.minLogLevel`: specifies the lowest level of logs that are exported to Cloud Logging. If the value isn't specified when Cloud Logging is enabled, the field is set to `INFO` by default.
  2. Apply the `wasm-plugin.yaml` manifest:
         
         kubectl apply -f wasm-plugin.yaml
         

  3. Verify that the plugin was deployed:
         
         kubectl describe gcpwasmplugins.networking.gke.io gcp-wasm-plugin
         

The output is similar to the following:
         
         Name:         gcp-wasm-plugin
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  networking.gke.io/v1
         Kind:         GCPWasmPlugin
         Metadata:
           Creation Timestamp:  2025-08-08T19:54:18Z
           Generation:          1
           Resource Version:    44578
           UID:                 549a12c7-91d1-43ad-a406-d6157a799b79
         Spec:
           Log Config:
             Enabled: true
             Min Log Level: INFO
             Sample Rate: 1000000
           Versions:
             Description:  Test wasm plugin version
             Image:        us-docker.pkg.dev/service-extensions-samples/plugins/local-reply:main
             Name:         wasm-plugin-version
             Weight:       1000000
           Events:     <none>
         




### Configure GCPTrafficExtension

To add custom logic to your global external Application Load Balancer, you can configure a GCPTrafficExtension to use a GCPWasmPlugin. You can use a GCPTrafficExtension to use advanced traffic management capabilities within your Google Cloud environment. You can configure this extension across global external Application Load Balancers.

To configure a GCPTrafficExtension to use a GCPWasmPlugin, complete the following steps:

  1. Define the GCPTrafficExtension.

     1. Save the GCPTrafficExtension configuration as `gcp-traffic-extension-with-plugin.yaml`:
            
            kind: GCPTrafficExtension
            apiVersion: networking.gke.io/v1
            metadata:
              name: gcp-traffic-extension-with-plugin
              namespace: default
            spec:
              targetRefs:
              - group: "gateway.networking.k8s.io"
                kind: Gateway
                name: GATEWAY_NAME
              extensionChains:
              - name: chain1
                matchCondition:
                  celExpressions:
                  - celMatcher: request.path.contains("serviceextensions")
                extensions:
                - name: ext1
                  supportedEvents:
                  - RequestHeaders
                  - ResponseHeaders
                  backendRef:
                    group: "networking.gke.io"
                    kind: GCPWasmPlugin
                    name: gcp-wasm-plugin
            

Replace `GATEWAY_NAME` with the name of your Gateway, such as `global-external-http`.

     2. Apply the sample manifest to your cluster:
            
            kubectl apply -f gcp-traffic-extension-with-plugin.yaml
            

  2. Verify the configuration of the GCPTrafficExtension and its binding to the Gateway.

     1. Check the GCPTrafficExtension deployment:
            
            kubectl describe gcptrafficextensions.networking.gke.io gcp-traffic-extension-with-plugin
            

The output is similar to the following:
            
            Name:         gcp-traffic-extension-with-plugin
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPTrafficExtension
            Metadata:
              Creation Timestamp:  2025-03-02T17:12:30Z
              Generation:        1
              Resource Version:  31283253
              UID:               ec8efaa0-d8e7-4e1b-9fd4-0ae0ef3c74d0
            Spec:
              Extension Chains:
                Extensions:
                  Backend Ref:
                    Group: networking.gke.io
                    Kind: GCPWasmPlugin
                    Name: gcp-wasm-plugin
                  Name:       ext1
                  Supported Events:
                    RequestHeaders
                    ResponseHeaders
                Match Condition:
                  Cel Expressions:
                    Cel Matcher: request.path.contains("serviceextensions")
                Name:  chain1
              Target Refs:
                Group: gateway.networking.k8s.io
                Kind: Gateway
                Name: GATEWAY_NAME
            Events:  <none>
            

Replace `GATEWAY_NAME` with the name of your Gateway.

The output displays the details of the GCPTrafficExtension named `gcp-traffic-extension-with-plugin` within the default namespace. It shows the `Spec` field, which contains the definition of how the extension should behave.

     2. Verify the Gateway binding:

Confirm that the GCPTrafficExtension is bound to the Gateway. This command might take a few minutes to complete:
            
            kubectl describe gateway GATEWAY_NAME
            

Replace `GATEWAY_NAME` with the name of your Gateway.

The output is similar to the following:
            
            Name:         GATEWAY_NAME
            Namespace:    default
            Labels:       <none>
            Annotations:  networking.gke.io/addresses: /projects/922988411345/global/addresses/test-k18j-default-external-http-2jfqxrkgd0fm
                          networking.gke.io/backend-services:
                            /projects/922988411345/global/backendServices/test-k18j-default-gw-serve404-80-8zjp3d8cqfsu, /projects/922988411345/global/backendServices...
                            networking.gke.io/certmap: store-example-com-map
                            networking.gke.io/firewalls: /projects/922988411345/global/firewalls/test-k18j-l7-default-global
                            networking.gke.io/forwarding-rules: /projects/922988411345/global/forwardingRules/test-k18j-default-external-http-wt1tl0cwi6zr
                            networking.gke.io/health-checks:
                              /projects/922988411345/global/healthChecks/test-k18j-default-gw-serve404-80-8zjp3d8cqfsu, /projects/922988411345/global/healthChecks/test-...
                            networking.gke.io/last-reconcile-time: 2025-08-08T20:27:35Z
                            networking.gke.io/lb-route-extensions:
                            **networking.gke.io/lb-traffic-extensions:
                              projects/922988411345/locations/global/lbTrafficExtensions/test-k18j-default-external-http-0tdum40yts35**
                            networking.gke.io/ssl-certificates:
                            networking.gke.io/target-http-proxies:
                            networking.gke.io/target-https-proxies: /projects/922988411345/global/targetHttpsProxies/test-k18j-default-external-http-jy9mc97xb5yh
                            networking.gke.io/url-maps: /projects/922988411345/global/urlMaps/test-k18j-default-external-http-jy9mc97xb5yh
                            **networking.gke.io/wasm-plugin-versions:
                              projects/922988411345/locations/global/wasmPlugins/test-k18j-default-gcp-wasm-plugin-itle20jj9nyk/versions/test-k18j-wasm-plugin-version-i...
                            networking.gke.io/wasm-plugins: projects/922988411345/locations/global/wasmPlugins/test-k18j-default-gcp-wasm-plugin-itle20jj9nyk**
            API Version:  gateway.networking.k8s.io/v1
            Kind:         Gateway
            Metadata:
              Creation Timestamp:  2025-03-02T16:37:50Z
              Finalizers:
                gateway.finalizer.networking.gke.io
              Generation:        1
              Resource Version:  31284863
              UID:               fd512611-bad2-438e-abfd-5619474fbf31
            Spec:
              Gateway Class Name:  gke-l7-global-external-managed
              Listeners:
                Allowed Routes:
                  Namespaces:
                    From:  Same
                Name:      https
                Port:      443
                Protocol:  HTTPS
            ...
            

The output shows the annotations, which GKE uses to store the links between the Gateway and the underlying Google Cloud resources. The `networking.gke.io/lb-traffic-extensions`, `networking.gke.io/wasm-plugin-versions`, and `networking.gke.io/wasm-plugins` annotations confirm the binding.

     3. Check the extension status:

Confirm that the GCPTrafficExtension has a `Programmed` status with the `ProgrammingSucceeded` reason. The command might take a few minutes to complete.
            
            kubectl describe gcptrafficextensions.networking.gke.io gcp-traffic-extension-with-plugin
            

The output is similar to the following:
            
            Name:         gcp-traffic-extension-with-plugin
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPTrafficExtension
            Metadata:
              Creation Timestamp:  2025-08-08T20:08:09Z
              Generation:          1
              Resource Version:    56528
              UID:                 1389f790-9663-45ca-ac4e-a2c082f43359
            Spec:
              Extension Chains:
                Extensions:
                  Backend Ref:
                    Group:  networking.gke.io
                    Kind:   GCPWasmPlugin
                    Name:   gcp-wasm-plugin
                  Name:     ext1
                  Supported Events:
                    RequestHeaders
                    ResponseHeaders
                Match Condition:
                  Cel Expressions:
                    Cel Matcher:  request.path.contains("serviceextensions")
                Name:             chain1
              Target Refs:
                Group:  gateway.networking.k8s.io
                Kind:   Gateway
                Name:   external-http
            Status:
              Ancestors:
                Ancestor Ref:
                  Group:      gateway.networking.k8s.io
                  Kind:       Gateway
                  Name:       external-http
                  Namespace:  default
                Conditions:
                  Last Transition Time:  2025-08-08T20:16:13Z
                  Message:
                  Observed Generation:   1
                  Reason:                Accepted
                  Status:                True
                  Type:                  Accepted
                  Last Transition Time:  2025-08-08T20:16:13Z
                  Message:
                  Observed Generation:   1
                  Reason:                ResolvedRefs
                  Status:                True
                  Type:                  ResolvedRefs
                  Last Transition Time:  2025-08-08T20:16:13Z
                  Message:
                  Observed Generation:   1
                  Reason:                ProgrammingSucceeded
                  Status:                True
                  Type:                  Programmed
                Controller Name:         networking.gke.io/gateway
            Events:
              Type    Reason  Age                  From                   Message
              ----    ------  ----                 ----                   -------
              Normal  ADD     19m                  sc-gateway-controller  default/gcp-traffic-extension-with-plugin
              Normal  SYNC    3m25s (x4 over 11m)  sc-gateway-controller  Attachment of GCPTrafficExtension "default/gcp-traffic-extension-with-plugin" to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil} was a success
              Normal  SYNC  3m25s (x4 over 11m)  sc-gateway-controller  All the object references were able to be resolved for GCPTrafficExtension "default/gcp-traffic-extension-with-plugin" bound to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil}
              Normal  SYNC  3m25s (x4 over 11m)  sc-gateway-controller  Programming of GCPTrafficExtension "default/gcp-traffic-extension-with-plugin" to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil} was a success
            

     4. Check the plugin status.

Confirm that the GCPWasmPlugin resource has a `Programmed` status with the `ProgrammingSucceeded` reason. The command might take a few minutes to complete.
            
            kubectl describe gcpwasmplugins.networking.gke.io gcp-wasm-plugin
            

The output is similar to the following:
            
            Name:         gcp-wasm-plugin
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPWasmPlugin
            Metadata:
              Creation Timestamp:  2025-08-08T19:54:18Z
              Generation:          1
              Resource Version:    44578
              UID:                 549a12c7-91d1-43ad-a406-d6157a799b79
            Spec:
              Log Config:
                Enabled: true
                Min Log Level: INFO
                Sample Rate: 1000000
              Versions:
                Description:  Test wasm plugin version
                Image:        us-docker.pkg.dev/service-extensions-samples/plugins/local-reply:main
                Name:         wasm-plugin-version
                Weight:       1000000
            Status:
              Ancestors:
                Ancestor Ref:
                  Group:      gateway.networking.k8s.io
                  Kind:       Gateway
                  Name:       external-http
                  Namespace:  default
                Conditions:
                  Last Transition Time:  2025-08-08T19:59:06Z
                  Message:
                  Observed Generation:   1
                  Reason:                Accepted
                  Status:                True
                  Type:                  Accepted
                  Last Transition Time:  2025-08-08T19:59:06Z
                  Message:
                  Observed Generation:   1
                  Reason:                ResolvedRefs
                  Status:                True
                  Type:                  ResolvedRefs
                  Last Transition Time:  2025-08-08T19:59:06Z
                  Message:
                  Observed Generation:   1
                  Reason:                ProgrammingSucceeded
                  Status:                True
                  Type:                  Programmed
                Controller Name:         networking.gke.io/gateway
            Events:
              Type    Reason  Age                 From                   Message
              ----    ------  ----                ----                   -------
              Normal  ADD     31m                 sc-gateway-controller  default/gcp-wasm-plugin
              Normal  SYNC    2m1s (x7 over 26m)  sc-gateway-controller  Attachment of WasmPlugin "default/gcp-wasm-plugin" to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil} was a success
              Normal  SYNC  2m1s (x7 over 26m)  sc-gateway-controller  All the object references were able to be resolved for WasmPlugin "default/gcp-wasm-plugin" bound to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil}
              Normal  SYNC  2m1s (x7 over 26m)  sc-gateway-controller  Programming of WasmPlugin "default/gcp-wasm-plugin" to AncestorRef {Group:       "gateway.networking.k8s.io",
            Kind:        "Gateway",
            Namespace:   "default",
            Name:        "external-http",
            SectionName: nil,
            Port:        nil} was a success
            

  3. Send traffic to your application.

After your Gateway, Route, and application are deployed in your cluster, you can pass traffic to your application.

     1. To access your application, you need to find the IP address of your Gateway.

In your terminal, use the following command:
            
            kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"
            

Replace `GATEWAY_NAME` with the name of your Gateway.

This command outputs the Gateway's IP address. In the follow-up commands, replace `GATEWAY_IP_ADDRESS` with the IP address from the output.

     2. Test the path update by going to the `serviceextensions` version of the store service at `store.example.com/serviceextensions`:
            
            curl https://store.example.com/serviceextensions --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert cacert.pem -v
            

The output returns `Hello World`.




### Configure GCPEdgeExtension with GCPWasmPlugin

To add custom logic to your global external Application Load Balancer by using a WebAssembly (Wasm) module, configure a GCPEdgeExtension that references the GCPWasmPlugin.

  1. Save the following GCPEdgeExtension manifest as `gcp-edge-extension-with-plugin.yaml`:
         
         kind: GCPEdgeExtension
         apiVersion: networking.gke.io/v1
         metadata:
           name: gcp-edge-extension-with-plugin
           namespace: default
         spec:
           targetRefs:
           - group: "gateway.networking.k8s.io"
             kind: Gateway
             name: GATEWAY_NAME
           extensionChains:
           - name: chain1
             matchCondition:
               celExpressions:
               - celMatcher: request.path.startsWith("/serviceextensions")
             extensions:
             - name: ext1
               supportedEvents:
               - RequestHeaders
               backendRef:
                 group: "networking.gke.io"
                 kind: GCPWasmPlugin
                 name: gcp-wasm-plugin
         

Replace `GATEWAY_NAME` with the name of your Gateway.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f gcp-edge-extension-with-plugin.yaml
         

  3. Verify the configuration of the GCPEdgeExtension and its binding to the Gateway:

     1. Check the extension status:

To check the extension status of the GCPEdgeExtension, run the following command:
            
            kubectl describe gcpedgeextensions.networking.gke.io gcp-edge-extension-with-plugin
            

Confirm that the GCPEdgeExtension has a `Programmed` status with the `ProgrammingSucceeded` reason. This command might take a few minutes to complete.

     2. Verify the Gateway binding:

Run the following command:
            
            kubectl describe gateway GATEWAY_NAME
            

Replace `GATEWAY_NAME` with the name of your Gateway.

Confirm that the GCPEdgeExtension is bound to the Gateway. This command might take a few minutes to complete. The output includes the `networking.gke.io/lb-edge-extensions` annotation, which confirms the link between the Gateway and the edge extension.




### Send traffic to the extension

After you deploy your Gateway and GCPEdgeExtension, test the routing logic by sending traffic to your application.

  1. To access your application, get the IP address of your Gateway:
         
         kubectl get gateways.gateway.networking.k8s.io external-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is the IP address of the Gateway. In the following commands, replace `GATEWAY_IP_ADDRESS` with the IP address from the output.

  2. Send a request to the base URL:
         
         curl http://store.example.com --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
         

The Gateway routes the request to the default service, such as `store-v1`.

  3. Send a request to the path specified in your celMatcher, such as `/serviceextensions`:
         
         curl http://store.example.com/serviceextensions --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
         

The extension triggers the Wasm plugin, which routes the request to the secondary service, such as `store-v2`.




## Manage the GCPWasmPlugin resource

You can update the GCPWasmPlugin CRD and monitor the plugin.

### Update the GCPWasmPlugin

To update a GCPWasmPlugin resource, follow these steps:

  1. Make the change in your GCPWasmPlugin manifest and follow the steps described in Deploy a GCPWasmPlugin.

For example, to have two versions of the plugin, where one version is serving traffic and the other is not, update your `wasm-plugin.yaml` file to the following:
         
         kind: GCPWasmPlugin
         apiVersion: networking.gke.io/v1
         metadata:
           name: gcp-wasm-plugin
         spec:
           versions:
           - name: wasm-plugin-version-v1
             description: "Serving Wasm Plugin version"
             image: "us-docker.pkg.dev/service-extensions-samples/plugins/local-reply:main"
             weight: 1000000
           - name: wasm-plugin-version-v2
             description: "Non serving Wasm Plugin version"
             image: "us-docker.pkg.dev/service-extensions-samples/plugins/local-reply:main"
             weight: 0
           logConfig:
             enabled: true
             sampleRate: 1000000
             minLogLevel: INFO
         

In this example, the following applies:

     * `wasm-plugin-version-v1` has a `weight` of `1000000`, meaning it serves all traffic.
     * `wasm-plugin-version-v2` has a `weight` of `0`, meaning it does not serve any traffic.
  2. To ensure that the Gateway is updated, run the following command. This command might take a few minutes to complete:
         
         kubectl describe gateway GATEWAY_NAME
         

Replace `GATEWAY_NAME` with the name of your Gateway.




### Monitor GCPWasmPlugin

To view metrics for GCPWasmPlugin in the Google Cloud console, see [Monitoring from a plugins perspective](https://docs.cloud.google.com/service-extensions/docs/monitor-lb-plugins#monitoring_from_a_plugins_perspective).

When you reach the step in the guide where you must select a value from the **Plugin version filter** list, look for the format `prefix−WASM_PLUGIN_VERSION_NAME_FROM_FILE−suffix`, where `WASM_PLUGIN_VERSION_NAME_FROM_FILE` is the specific version name you defined in your GCPWasmPlugin configuration file.

## Troubleshoot traffic extensions on Gateways

This section provides troubleshooting tips for configuring traffic extensions on Gateways.

### Gateway not found

The following error indicates that the Gateway resource specified in the `targetRefs` field of the GCPTrafficExtension, GCPRoutingExtension, or GCPEdgeExtension resource doesn't exist:
    
    
    error: failed to create resource: GCPTrafficExtension.networking.gke.io "my-traffic-extension" is invalid: spec.gatewayRef: gateway "my-gateway" not found in namespace "default"
    

To resolve this issue, ensure that the Gateway resource specified in the `targetRefs` field of the GCPTrafficExtension or GCPRoutingExtension resource exists in the specified namespace.

### Service or service port not found

The following error indicates that the Service or Service port specified in the `backendRef` field of the GCPTrafficExtension or GCPRoutingExtension resource does not exist:
    
    
    error: failed to create resource: GCPTrafficExtension.networking.gke.io "my-traffic-extension" is invalid: spec.service: service "callout-service" not found in namespace "default"
    

To resolve this issue, ensure that the Service and Service port specified in the `backendRef` field of the GCPTrafficExtension or GCPRoutingExtension resource exist in the specified namespace.

### No network endpoints in the NEG

The following error indicates that there are no network endpoints in the NEG are associated with the Service specified in the `backendRef` field of the GCPTrafficExtension or GCPRoutingExtension resource:
    
    
    error: failed to create resource: GCPTrafficExtension.networking.gke.io "my-traffic-extension" is invalid: spec.service: no network endpoints found for service "callout-service"
    

To resolve this issue, ensure that the Service specified in the `backendRef` field of the GCPTrafficExtension or GCPRoutingExtension resource has network endpoints.

### No reply or reply with an error when sending the request

If you don't receive a reply, or if you receive a reply with an error when you send a request, it might indicate that the callout Service is not working correctly.

To resolve this issue, check the logs of the callout Service for any errors.

#### Error code 404 in the JSON payload

The following error indicates that the callout Service is not found or is not responding to the request:
    
    
    {
      "error": {
        "code": 404,
        "message": "Requested entity was not found.",
        "status": "NOT_FOUND"
      }
    }
    

To resolve this issue, ensure that the callout Service is running, that it is listening on the correct port, and that the service is correctly configured in the GCPTrafficExtension or GCPRoutingExtension resource.

#### Error code 500 in the JSON payload

The following error indicates that the callout Service is experiencing an internal server error:
    
    
    {
      "error": {
        "code": 500,
        "message": "Internal server error.",
        "status": "INTERNAL"
      }
    }
    

To resolve this issue, check the logs of the callout Service to identify the cause of the internal server error.

### GCPWasmPlugin does not exist

The following error indicates that the GCPWasmPlugin resource doesn't exist in your project for your GCPTrafficExtension or GCPEdgeExtension:
    
    
    Status:
      Ancestors:
        Ancestor Ref:
          Group:      gateway.networking.k8s.io
          Kind:       Gateway
          Name:       external-http
          Namespace:  default
        Conditions:
          Last Transition Time:  2025-03-06T16:27:57Z
          Message:
          Reason:                Accepted
          Status:                True
          Type:                  Accepted
          Last Transition Time:  2025-03-06T16:27:57Z
          Message:               error cause: invalid-wasm-plugin: GCPWasmPlugin default/my-wasm-plugin in GCPTrafficExtension default/my-gateway-plugin-extension does not exist
          Reason:                GCPWasmPluginNotFound
          Status:                False
          Type:                  ResolvedRefs
        Controller Name:         networking.gke.io/gateway
    

To resolve this issue, create a corresponding GCPWasmPlugin in the Google Cloud project or point an extension to an existing GCPWasmPlugin.

## What's next

  * Learn about [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).
  * Learn how to [Serve an LLM with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway).
  * Learn how to [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
