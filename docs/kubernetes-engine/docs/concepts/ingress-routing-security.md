---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-routing-security/
title: About GKE Ingress routing and security \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:22.432215+00:00
---

# About GKE Ingress routing and security  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-routing-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About GKE Ingress routing and security Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the core capabilities and networking architecture of GKE Ingress, specifically securing connections from the client to the load balancer and through to application Pods, managing complex routing across multiple backend services, and understanding how load balancer health checks are orchestrated within a cluster.

This page builds upon the foundational concepts described in the [GKE Ingress overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress). For step-by-step instructions and implementation examples using custom resources such as FrontendConfig and BackendConfig, see [Configure Ingress features for GKE applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).

This page is for Networking specialists who design and architect the network for their organization and install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Securing Ingress with HTTPS

GKE Ingress secures traffic between the client and the Application Load Balancer, and from the load balancer to the application Pods.

### Configuring TLS between the client and the load balancer

An HTTP(S) load balancer acts as a proxy between your clients and your application. If you want to accept HTTPS requests from your clients, the load balancer must have a certificate so it can prove its identity to your clients. The load balancer must also have a private key to complete the HTTPS handshake.

When the load balancer accepts an HTTPS request from a client, the traffic between the client and the load balancer is encrypted using TLS. However, the load balancer terminates the TLS encryption, and forwards the request without encryption to the application. For more information, see Configuring encryption between the load balancer and your application.

#### Methods for providing SSL Certificates

**Note:** To use certificates managed by Certificate Manager, we recommend that you use [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). GKE Ingress does not support certificates managed by Certificate Manager.

You can provide SSL certificates to an HTTP(S) load balancer using the following methods:

  * **Google-managed certificates** : These are Domain Validation (DV) certificates that Google provisions, renews, and manages for your domain names. These certificates don't demonstrate your individual or organizational identity. Google-managed certificates support up to 100 non-wildcard domains. For more information, see [Use Google-managed certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management#google-managed-certificates).

  * **Self-managed certificates shared with Google Cloud** : You can provision your own SSL certificate and create a certificate resource in your Google Cloud project. You then list the certificate resource in an annotation on an Ingress to create an HTTP(S) load balancer that uses the certificate. For more information, see [Use pre-shared certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management#pre-shared-certificates).

  * **Self-managed certificates that use Kubernetes[Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)**: You can provision your own SSL certificate and create a Secret to hold it. You can then refer to the Secret in the `tls` field of an Ingress manifest to create an HTTP(S) load balancer. For more information, see [Use Kubernetes Secrets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management#secrets).




#### Serve HTTPS traffic with multiple certificates

You can configure the Application Load Balancer to present up to 15 TLS certificates to a client. Using [multiple certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#multiplessl) is essential when you need to serve content from multiple hostnames, each requiring a different certificate (for example, separate certificates for your-store.example and your-experimental-store.example). You specify these multiple certificates within your Ingress manifest.

#### Certificate selection and priority

To determine which certificate to present to the client, the load balancer uses Server Name Indication (SNI).

  * If the client uses SNI, or uses a domain name that matches the Common Name (CN) in one of the available certificates, the load balancer uses the certificate whose CN is the closest match to the hostname requested by the client.

  * If the client does not support SNI, or the requested domain name does not match the CN of any available certificate, the load balancer uses the first certificate listed in the Ingress manifest as the default. The load balancer chooses this certificate according to these rules:

    * For Secrets listed in the `tls` block: the primary certificate is the first Secret in the `tls` block.
    * For pre-shared certificates in the `pre-shared-cert` annotation: the primary certificate is the first certificate listed in the annotation.
    * For Google-managed certificates in the `managed-certificates` annotation: all managed certificates are sorted alphabetically by name. The primary certificate is the one that comes first in this alphabetical list. To set a specific certificate as the primary, you must name your `ManagedCertificate` objects accordingly to control the sort order. For example, to make `my-default-cert` the primary over `another-cert`, you might name them `0-my-default-cert` and `1-another-cert`.



When the load balancer presents multiple certificates through different GKE methods, pre-shared certificates take priority over Secrets listed in the Ingress `tls` block.

The following diagram shows the load balancer sending traffic to different backends, depending on the domain name used in the request:

![multiple SSL certificates with Ingress system diagram](https://docs.cloud.google.com/static/kubernetes-engine/images/ingress-multi-ssl.svg)

#### Certificate rotation best practices

If you want to rotate the contents of your Secret or pre-shared certificate, here are some best practices:

  * Create a new Secret or pre-shared certificate with a different name that contains the new certificate data. Update your Ingress to use the new certificate resource.
  * If you don't mind disrupting traffic, you can remove the old resource from the Ingress, provision a new resource with the same name but different contents, and then reattach it to the Ingress.



To avoid managing certificate rotation yourself, use [Google-managed SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management#google-managed-certificates).

#### Enforcing HTTPS-only traffic

If you want all traffic between the client and the HTTP(S) load balancer to use HTTPS, you can disable HTTP by including the `kubernetes.io/ingress.allow-http` annotation in your Ingress manifest and setting the value to `"false"`. For more information, see [Disabling HTTP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management#disable-http).

**Caution:** Disabling HTTP is not supported for Multi Cluster Ingress.

### Configuring encryption between the load balancer and your application

This section explains how to secure the connection from the load balancer to the application Pods.

#### Enabling HTTPS or HTTP/2 Backend Protocol

The external Application Load Balancer acts as a proxy between your clients and your GKE application. Although clients can connect to the load balancer by using HTTPS (for encryption) and various protocols (HTTP/1.1 or HTTP/2), the connection from the load balancer to your backend Pods defaults to unencrypted HTTP/1.1.

If your application is capable of handling more advanced configurations, you can manually update the external Application Load Balancer to use:

  * **HTTP/2** : to optimize performance if your Pods support it.
  * **HTTPS (TLS)** : to enforce end-to-end encryption for traffic between the load balancer proxy and your Pods.



You control both the protocol (HTTP or HTTPS) and the HTTP version (HTTP/1.1 or HTTP/2) used for the backend connection by using the `cloud.google.com/app-protocols` annotation in your Kubernetes Service manifest. This Service manifest must include `type: NodePort` unless you're using [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native-load-balancing). If you use container-native load balancing, use the `type: ClusterIP`.

## Static IP addresses for HTTPS load balancers

When you create an Ingress object for an external Application Load Balancer, you get a stable external IP address that clients can use to access your Services and in turn, your running containers. The IP address is stable in the sense that it lasts for the lifetime of the Ingress object. If you delete your Ingress and create a new Ingress from the same manifest file, you are not guaranteed to get the same external IP address.

If you want a permanent IP address that stays the same across deleting your Ingress and creating a new one, you must reserve a global [static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Then in your Ingress manifest, include an annotation that gives the name of your reserved static IP address. If you modify an existing Ingress to use a static IP address instead of an ephemeral IP address, GKE might change the IP address of the load balancer when GKE re-creates the forwarding rule of the load balancer.

## Routing Traffic

GKE Ingress uses URL maps to define how incoming requests are routed to specific backend services. You can configure routing rules based on hostnames, URL paths, or a combination of both to manage traffic for multiple applications through a single load balancer.

### Multiple backend services

Each external Application Load Balancer or internal Application Load Balancer uses a single URL map, which references one or more backend services. One backend service corresponds to each Service referenced by the Ingress.

For example, you can configure the load balancer to route requests to different backend services depending on the URL path. Requests sent to your-store.example could be routed to a backend service that displays full-price items, and requests sent to your-store.example/discounted could be routed to a backend service that displays discounted items.

You can also configure the load balancer to route requests according to the hostname. Requests sent to your-store.example could go to one backend service, and requests sent to your-experimental-store.example could go to another backend service.

In a GKE cluster, you create and configure an HTTP(S) load balancer by creating a Kubernetes Ingress object. An Ingress object must be associated with one or more Service objects, each of which is associated with a set of Pods.

If you want to configure GKE Ingress with multiple backends for the same host, you must have a single rule with a single host and multiple paths. Otherwise, the GKE ingress controller provisions only one backend service

Here is a manifest for an Ingress called `my-ingress`:
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-ingress
    spec:
     rules:
      - host: your-store.example
        http:
          paths:
          - path: /products
            pathType: ImplementationSpecific
            backend:
              service:
                name: my-products
                port:
                  number: 60000
          - path: /discounted
            pathType: ImplementationSpecific
            backend:
              service:
                name: my-discounted-products
                port:
                  number: 80

**Note:** To use Ingress, you must have the external Application Load Balancer add-on enabled. GKE clusters have external Application Load Balancers enabled by default; you must not disable it.

When you create the Ingress, the GKE ingress controller creates and configures an external Application Load Balancer or an internal Application Load Balancer according to the information in the Ingress and the associated Services. Also, the load balancer is given a stable IP address that you can associate with a domain name.

In the preceding example, assume you have associated the load balancer's IP address with the domain name your-store.example. When a client sends a request to `your-store.example/products`, the request is routed to a Kubernetes Service named `my-products` on port 60000. And when a client sends a request to `your-store.example/discounted`, the request is routed to a Kubernetes Service named `my-discounted-products` on port 80.

The only supported wildcard character for the `path` field of an Ingress is the `*` character. The `*` character must follow a forward slash (`/`) and must be the last character in the pattern. For example, `/*`, `/foo/*`, and `/foo/bar/*` are valid patterns, but `*`, `/foo/bar*`, and `/foo/*/bar` are not.

A more specific pattern takes precedence over a less specific pattern. If you have both `/foo/*` and `/foo/bar/*`, then `/foo/bar/bat` is taken to match `/foo/bar/*`.

For more information about path limitations and pattern matching, see the [URL Maps documentation](https://docs.cloud.google.com/load-balancing/docs/url-map).

The manifest for the `my-products` Service might look like this:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-products
    spec:
      type: NodePort
      selector:
        app: products
        department: sales
      ports:
      - protocol: TCP
        port: 60000
        targetPort: 50000

Note the following in the preceding manifest:

  * The `spec.type` field depends on the load balancing method that you use:

    * If you use [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native-load-balancing), use `type: ClusterIP`.
    * If you use [instance groups](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#instance-groups), use `type: NodePort`.
  * The `selector` field says any Pod that has both the `app: products` label and the `department: sales` label is a member of this Service.

  * When a request comes to the Service on port 60000, it is routed to one of the member Pods on TCP port 50000.

  * Each member Pod must have a container listening on TCP port 50000.




The manifest for the `my-discounted-products` Service might look like this:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-discounted-products
    spec:
      type: NodePort
      selector:
        app: discounted-products
        department: sales
      ports:
      - protocol: TCP
        port: 80
        targetPort: 8080

Note the following in the preceding manifest:

  * The `selector` field says any Pod that has both the `app: discounted-products` label and the `department: sales` label is a member of this Service.

  * When a request comes to the Service on port 80, it is routed to one of the member Pods on TCP port 8080.

  * Each member Pod must have a container listening on TCP port 8080.




### Default backend

You can specify a default backend for your Ingress by providing a `spec.defaultBackend` field in your Ingress manifest. This will handle any requests that don't match the paths defined in the `rules` field. For example, in the following Ingress, any requests that don't match `/discounted` are sent to a service named `my-products` on port 60001.
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-ingress
    spec:
      defaultBackend:
        service:
          name: my-products
          port:
            number: 60001
      rules:
      - http:
          paths:
          - path: /discounted
            pathType: ImplementationSpecific
            backend:
              service:
                name: my-discounted-products
                port:
                  number: 80
    

If you don't specify a default backend, GKE provides a default backend that returns 404. This is created as a `default-http-backend` NodePort service on the cluster in the `kube-system` namespace.

The 404 HTTP response is similar to the following:
    
    
    response 404 (backend NotFound), service rules for the path non-existent
    

To set up GKE Ingress with a custom default backend, see the [GKE Ingress with custom default backend](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-custom-default-backend).

## Health checks

When you expose one or more Services through an Ingress using the default Ingress controller, GKE creates a [classic Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb) or an [internal Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb). Both of these load balancers support multiple [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) on a single [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts). Each of the backend services corresponds to a Kubernetes Service, and each backend service must reference a [Google Cloud health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts). This health check is _different_ from a Kubernetes liveness or readiness probe because the health check is implemented outside of the cluster.

Load balancer health checks are specified _per backend service_. While it's possible to use the same health check for all backend services of the load balancer, the health check reference isn't specified for the whole load balancer (at the Ingress object itself).

GKE creates health checks based on one of the following methods:

  * **`BackendConfig` CRD**: A custom resource definition (CRD) that gives you precise control over how your Services interact with the load balancer. `BackendConfig` CRDs allow you to specify custom settings for the health check associated with the corresponding backend service. These custom settings provide greater flexibility and control over health checks for both the classic Application Load Balancer and internal Application Load Balancer created by an Ingress.
  * **Readiness probe** : A diagnostic check that determines if a container within a Pod is ready to serve traffic. The GKE Ingress controller creates the health check for the Service's backend service based on the readiness probe used by that Service's serving Pods. You can derive the health check parameters such as path, port, and protocol from the readiness probe definition.
  * **Default values** : The parameters used when you don't configure a `BackendConfig` CRD or define attributes for the readiness probe.

**Best practice** : 

Use a `BackendConfig` CRD to have the most control over the load balancer health check settings.

GKE uses the following procedure to create a health check for each backend service corresponding to a Kubernetes Service:

  * If the Service references [a `BackendConfig` CRD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#direct_hc) with `healthCheck` information, GKE uses that to create the health check. Both the GKE Enterprise Ingress controller and the GKE Ingress controller support creating health checks this way.

  * If the Service does _not_ reference a `BackendConfig` CRD:

    * GKE can infer some or all of the parameters for a health check if the Serving Pods use a Pod template with a container whose readiness probe has attributes that can be interpreted as health check parameters. See [Parameters from a readiness probe](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#interpreted_hc) for implementation details and [Default and inferred parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#def_inf_hc) for a list of attributes that can be used to create health check parameters. Only the GKE Ingress controller supports inferring parameters from a readiness probe.

    * If the Pod template for the Service's serving Pods does **not** have a container with a readiness probe whose attributes can be interpreted as health check parameters, [the default values](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#def_inf_hc) are used to create the health check. Both the GKE Enterprise Ingress controller and the GKE Ingress controller can create a health check using only the default values.


**Note:** `containerPort` field must be defined under pod spec and `targetPort` field must be defined under service spec for health check to infer parameters defined under readiness probe. If they are not defined, the health check for the backend service defaults to "/" path even if parameters are defined under readiness probe.

### Default and inferred parameters

The following parameters are used when you do **not** specify health check parameters for the corresponding Service using a `BackendConfig` CRD.

Health check parameter | Default value | Inferable value  
---|---|---  
[Protocol](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol) | HTTP | if present in the Service annotation `cloud.google.com/app-protocols`  
[ Request path](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) | `/` | if present in the serving Pod's `spec`:  
`containers[].readinessProbe.httpGet.path`  
[ Request Host header](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) | `Host: backend-ip-address` | if present in the serving Pod's `spec`:  
`containers[].readinessProbe.httpGet.httpHeaders`  
[ Expected response](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) | HTTP 200 (OK) | HTTP 200 (OK)  
cannot be changed  
[Check interval](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes) | 

  * for Container-native load balancing: 15 seconds
  * for instance groups: 60 seconds

|  if present in the serving Pod's `spec`: 

  * for Container-native load balancing:  
`containers[].readinessProbe.periodSeconds`
  * for instance groups:  
`containers[].readinessProbe.periodSeconds + 60 seconds`

  
[Check timeout](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes) | 5 seconds | if present in the serving Pod's `spec`:  
`containers[].readinessProbe.timeoutSeconds`  
[Healthy threshold](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state) | 1 | 1  
cannot be changed  
[Unhealthy threshold](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state) | 

  * for Container-native load balancing: 2
  * for instance groups: 10

|  same as default: 

  * for Container-native load balancing: 2
  * for instance groups: 10

  
[Port specification](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_port_specification) | 

  * for Container-native load balancing: the Service's `port`
  * for instance groups: the Service's `nodePort`

| The health check probes are sent to the port number specified by the `spec.containers[].readinessProbe.httpGet.port`, as long as all of the following are also true: 

  * The readiness probe's port number must match the serving Pod's `containers[].spec.ports.containerPort`
  * The serving Pod's `containerPort` matches the Service's `targetPort`
  * The Ingress _service backend port specification_ references a valid port from `spec.ports[]` of the Service. This can be done in one of two ways: 
    * `spec.rules[].http.paths[].backend.service.port.name` in the Ingress matches `spec.ports[].name` defined in the corresponding Service
    * `spec.rules[].http.paths[].backend.service.port.number` in the Ingress matches `spec.ports[].port` defined in the corresponding Service

  
[ Destination IP address](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest) | 

  * for Container-native load balancing: the Pod's IP address
  * for instance groups: the node's IP address

|  same as default: 

  * for Container-native load balancing: the Pod's IP address
  * for instance groups: the node's IP address

  
**Note:** A valid Kubernetes readiness probe supports setting multiple HTTP headers in [`readinessProbe.httpGet`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#httpgetaction-v1-core). If `readinessProbe.httpGet.httpHeaders` specifies more than just the `Host` header, the load balancer's health check parameters are set to default values instead of values inferred from the readiness probe. This limitation exists because [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#headers) only support setting the `Host` header.

### Parameters from a readiness probe

When GKE creates the health check for the Service's backend service, GKE can copy certain parameters from _one container's_ readiness probe used by that Service's serving Pods. This option is _only_ supported by the GKE Ingress controller.

Supported readiness probe attributes that can be interpreted as health check parameters are listed along with the default values in Default and inferred parameters. Default values are used for any attributes not specified in the readiness probe or if you don't specify a readiness probe at all.

If serving Pods for your Service contain _multiple_ containers, or if you're using the GKE Enterprise Ingress controller, you should use a `BackendConfig` CRD to define health check parameters. For more information, see When to use a `BackendConfig` CRD instead.

**Warning:** When a backend service's health check parameters are inferred from a serving Pod's readiness probe, GKE does **not** keep the readiness probe and health check synchronized:

  * If you change the readiness probe for the serving Pods of a Service referenced by an Ingress after GKE has created the external Application Load Balancer or the internal Application Load Balancer for that Ingress, the changes you make to the readiness probe will **not** be copied to the health check for the corresponding backend service on the load balancer.
  * Conversely, if you make changes to the health check used by a backend service of a load balancer created on behalf of an Ingress, GKE will **not** update any readiness probe, nor will it revert any changes you make to the health check.



#### When to use `BackendConfig` CRDs instead

Instead of relying on parameters from Pod readiness probes, you should explicitly define health check parameters for a backend service by creating a `BackendConfig` CRD for the Service in these situations:

  * **If you're using GKE Enterprise:** The GKE Enterprise Ingress controller does **not** support obtaining health check parameters from the readiness probes of serving Pods. It can only create health checks using implicit parameters or as defined in a `BackendConfig` CRD.

  * **If you have more than one container in the serving Pods:** GKE does not have a way to select the readiness probe of a _specific container_ from which to infer health check parameters. Because each container can have its own readiness probe, and because a readiness probe isn't a required parameter for a container, you should define the health check for the corresponding backend service by referencing a `BackendConfig` CRD on the corresponding Service.

  * **If you need control over the port used for the load balancer's health checks:** GKE only uses the readiness probe's `containers[].readinessProbe.httpGet.port` for the backend service's health check when that port matches the service port for the Service referenced in the Ingress `spec.rules[].http.paths[].backend.servicePort`.




### Parameters from a `BackendConfig` CRD

You can specify the backend service's health check parameters [using the `healthCheck` parameter of a `BackendConfig` CRD](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#direct_health) referenced by the corresponding Service. This gives you more flexibility and control over health checks for a classic Application Load Balancer or an internal Application Load Balancer created by an Ingress. See [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration) for GKE version compatibility.

This example `BackendConfig` CRD defines the health check protocol (type), a request path, a port, and a check interval in its `spec.healthCheck` attribute:
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: http-hc-config
    spec:
      healthCheck:
        checkIntervalSec: 15
        port: 15020
        type: HTTPS
        requestPath: /healthz
    

To configure all the fields available when configuring a `BackendConfig` health check, use the [custom health check configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#direct_health) example.

To set up GKE Ingress with a custom HTTP health check, see [GKE Ingress with custom HTTP health check](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-custom-http-health-check).

### Pod readiness

After the load balancer's health checks are configured using one of the preceding methods, the GKE Ingress controller uses the health status of the backend endpoints to determine Pod readiness, which is critical for managing rolling updates and overall traffic stability.

For relevant Pods, the corresponding Ingress controller manages a [readiness gate](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate) of type `cloud.google.com/load-balancer-neg-ready`. The Ingress controller polls the load balancer's [health check status](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts), which includes the health of all endpoints in the NEG. When the load balancer's health check status indicates that the endpoint corresponding to a particular Pod is healthy, the Ingress controller sets the Pod's readiness gate value to `True`. The kubelet running on each node then computes the Pod's effective readiness, considering both the value of this readiness gate and, if defined, the Pod's [readiness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/#define-readiness-probes).

Pod readiness gates are automatically enabled when using container-native load balancing through Ingress.

Readiness gates control the rate of a rolling update. When you initiate a rolling update, as GKE creates new Pods, and an endpoint for each new Pod is added to a NEG. When the endpoint is healthy from the perspective of the load balancer, the Ingress controller sets the readiness gate to `True`. A newly created Pod must at least pass its readiness gate _before_ GKE removes an old Pod. This helps ensure that the corresponding endpoint for the Pod has already passed the load balancer's health check and that the backend capacity is maintained.

If a Pod's readiness gate never indicates that the Pod is ready, due to a bad container image or a misconfigured load balancer health check, the load balancer won't direct traffic to the new Pod. If such a failure occurs while rolling out an updated Deployment, the rollout stalls after attempting to create one new Pod because that Pod's readiness gate is never True. See the [troubleshooting section](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress#stalled_rollout) for information on how to detect and fix this situation.

Without container-native load balancing and readiness gates, GKE can't detect if a load balancer's endpoints are healthy before marking Pods as ready. In previous Kubernetes versions, you control the rate that Pods are removed and replaced by specifying a delay period (`minReadySeconds` in the Deployment specification).

GKE sets the value of `cloud.google.com/load-balancer-neg-ready` for a Pod to `True` if any of the following conditions are met:

  * None of the Pod's IP addresses are endpoints in a [`GCE_VM_IP_PORT` NEG](https://docs.cloud.google.com/load-balancing/docs/negs) managed by the GKE control plane.
  * One or more of the Pod's IP addresses are endpoints in a `GCE_VM_IP_PORT` NEG managed by the GKE control plane. The NEG is attached to a [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service). The backend service has a successful load balancer health check.
  * One or more of the Pod's IP addresses are endpoints in a `GCE_VM_IP_PORT` NEG managed by the GKE control plane. The NEG is attached to a backend service. The load balancer health check for the backend service [times out](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method).
  * One or more of the Pod's IP addresses are endpoints in one or more `GCE_VM_IP_PORT` NEGs. None of the NEGs are attached to a backend service. No load balancer health check data is available.



## Support for WebSocket

With external Application Load Balancers, the WebSocket protocol works without any configuration.

If you intend to use the WebSocket protocol, you might want to use a timeout value larger than the default 30 seconds. For WebSocket traffic sent through a Google Cloud external Application Load Balancer, the backend service timeout is interpreted as the maximum amount of time that a WebSocket connection can remain open, whether idle or not.

To set the timeout value for a backend service, see [Backend response timeout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#timeout).

## Advanced networking scenarios

GKE Ingress supports advanced networking configurations such as sharing network resources across projects and using custom Ingress controllers.

### Shared VPC

Ingress and `MultiClusterIngress` resources are supported in [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), but they require additional preparation.

The Ingress controller runs on the GKE control plane and makes API calls to Google Cloud using the GKE service account of the cluster's project. By default, when a cluster that is located in a Shared VPC service project uses a Shared VPC network, the Ingress controller cannot use the service project's GKE service account to create and update ingress allow firewall rules in the host project.

You can grant the service project's GKE service account permissions to create and [manage VPC firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#manage_firewall_resources) in the host project. By granting these permissions, GKE creates ingress allow firewall rules for the following:

  * Google Front End (GFE) proxies and health check systems used by external Application Load Balancers for external Ingress. For more information, see the [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules).

  * Health check systems for internal Application Load Balancers used by internal Ingress.

**Note:** Whether or not you're using Shared VPC, if your cluster uses an internal Ingress, you must manually [create ingress allow firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws) to permit traffic from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in the cluster's VPC network and region. Manual creation of these rules is needed because the GKE Ingress controller cannot create ingress allow firewall rules to permit traffic for an internal Application Load Balancer's proxy-only subnet. For more information, see [Required networking environment in Ingress for internal Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#required-networking-environment).

#### Manually provision firewall rules from the host project




If your security policies only allow firewall management from the host project, then you can provision these firewall rules manually. When you deploy Ingress in a Shared VPC, the Ingress resource event provides the specific firewall rule that is necessary to provide access.

To manually provision a rule:

  1. View the Ingress resource event:
         
         kubectl describe ingress INGRESS_NAME
         

Replace INGRESS_NAME with the name of your Ingress.

You should see output similar to the following example:
         
         Events:
         Type    Reason  Age                    From                     Message
         ----    ------  ----                   ----                     -------
         Normal  Sync    9m34s (x237 over 38h)  loadbalancer-controller  Firewall change required by security admin: `gcloud compute firewall-rules update k8s-fw-l7--6048d433d4280f11 --description "GCE L7 firewall rule" --allow tcp:30000-32767,tcp:8080 --source-ranges 130.211.0.0/22,35.191.0.0/16 --target-tags gke-l7-ilb-test-b3a7e0e5-node --project <project>`
         

The suggested required firewall rule appears in the `Message` column.

  2. Copy and apply the suggested firewall rules from the host project. Applying the rule provides access to your Pods from the load balancer and Google Cloud health checkers.

**Note:** Different types of Ingress require different rules. GKE might show a firewall rule warning even if you have your own custom ingress firewall rules to allow the traffic. You can ignore the warning in that case.

**Note:** For Multi Cluster Ingress, this manual provision step is the only supported way to install firewall rules in a host project. Changing the service account permissions for automatic provisioning is not supported.

#### Providing the Ingress controller permission to manage host project firewall rules

If you want a GKE cluster in a service project to create and manage the firewall resources in your host project, the service project's GKE service account must be granted the appropriate IAM permissions using one of the following strategies:

  * Grant the service project's GKE service account the [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) to the host project. The following example demonstrates this strategy.

  * For a finer grained approach, [create a custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role) that includes only the following permissions: `compute.networks.updatePolicy`, `compute.firewalls.list`, `compute.firewalls.get`, `compute.firewalls.create`, `compute.firewalls.update`, `compute.firewalls.delete`, and `compute.subnetworks.list`. Grant the service project's GKE service account that custom role to the host project.




If you have clusters in more than one service project, you must choose one of the strategies and repeat it for each service project's GKE service account.
    
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
      --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
      --role=roles/compute.securityAdmin
    

Replace the following:

  * `HOST_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the [Shared VPC host project](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_host_project_and_service_project_associations).
  * `SERVICE_PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the [service project](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_host_project_and_service_project_associations) that contains your cluster.



### Use a custom Ingress controller

You can run a custom Ingress controller by disabling the `HttpLoadBalancing` add-on. This prevents the GKE Ingress controller from processing Ingress resources.

If you want to run a custom Ingress controller with the `HttpLoadBalancing` add-on enabled, for example to use features such as [subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#subsetting) and [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net), you can use one of the following approaches:

  * In the Ingress manifest, set the [`kubernetes.io/ingress.class`](https://kubernetes.io/docs/concepts/services-networking/ingress/#deprecated-annotation) annotation. This configuration is supported for clusters running all GKE versions.
  * Configure the `ingressClassName` field.
  * Configure a default Ingress class.



You must ensure that `spec.ingressClassName` is not accidentally overwritten by any process. An update operation that changes `spec.IngressClassName` from a valid value to an empty string (`""`) causes the GKE Ingress controller to process the Ingress.

**Caution:** Google does not provide support for debugging issues with custom Ingress controllers.

#### Configure the `ingressClassName` field

You can use a custom Ingress controller by setting the `ingressClassName` field in the Ingress manifest. The following manifest describes an Ingress that specifies the [`cilium` Ingress controller](https://docs.cilium.io/en/stable/network/servicemesh/ingress/):
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
     name: cafe-ingress
    spec:
     ingressClassName: cilium
     tls:
     - hosts:
       - cafe.example.com
       secretName: cafe-secret
     rules:
     - host: cafe.example.com
    

**Note:** If an Ingress has an empty `spec.ingressClassName` or `spec.ingressClassName` is not present, and the Ingress does not have the annotation `kubernetes.io/ingress.class`, the GKE Ingress controller processes the Ingress.

#### Configure a default Ingress class

You can configure a default Ingress class for all Ingress resources in a cluster by creating an [`IngressClass`](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class) resource with the annotation `ingressclass.kubernetes.io/is-default-class` set to `true`:
    
    
    apiVersion: networking.k8s.io/v1
    kind: IngressClass
    metadata:
      name: gce
      annotations:
        ingressclass.kubernetes.io/is-default-class: "true"
    spec:
      controller: k8s.io/ingress-gce
    

**Note:** The [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) populates the `spec.ingressClassName` field for new Ingress resources in the cluster, but does not modify existing Ingress resources.

#### Summary of GKE Ingress controller behavior

For clusters running GKE versions 1.18 and later, whether or not the GKE Ingress controller processes an Ingress depends on the value of the `kubernetes.io/ingress.class` annotation and the `ingressClassName` field in the Ingress manifest. For more information, see [GKE Ingress controller behavior](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#controller_summary).

## Templates for the Ingress configuration

  * In [GKE Networking Recipes](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main), you can find templates provided by GKE on many common Ingress usage under the [Ingress](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster) section.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
