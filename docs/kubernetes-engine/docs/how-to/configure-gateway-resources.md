---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources/
title: Configure Gateway resources using Policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:05.665955+00:00
---

# Configure Gateway resources using Policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure Gateway resources using Policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure the load balancer that Google Kubernetes Engine (GKE) creates when you deploy a Gateway in a GKE cluster.

When you deploy a Gateway, the GatewayClass configuration determines which load balancer GKE creates. This managed load balancer is pre-configured with default settings that you can modify using a _Policy_.

You can customize Gateway resources to fit your infrastructure or application requirements by attaching Policies to Gateways, Services, or ServiceImports. After you apply or modify a Policy, the Gateway controller processes it and automatically reconfigures the underlying load balancer resource. This eliminates the need to delete or recreate your Gateway, Route, or Service resources.

You can also use a BackendTLSPolicy to configure backend authenticated TLS settings to verify the identity of the backends that the Gateway connects to. For more information, see [Configure backend TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-tls).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### GKE Gateway controller requirements

  * Gateway API is supported on [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) clusters only.
  * If you are using the regional or cross-region GatewayClasses, you must enable a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * Your cluster must have the `HttpLoadBalancing` add-on enabled.
  * If you are using Istio, you must upgrade Istio to one of the following versions: 
    * 1.15.2 or later
    * 1.14.5 or later
    * 1.13.9 or later.
  * If you are using Shared VPC, then in the host project, you need to assign the `Compute Network User` role to the GKE Service account for the service project. 



### Restrictions and Limitations

In addition to the GKE Gateway controller [restrictions and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#limitations), the following limitations apply specifically to Policies applied on the Gateway resources:

  * GCPGatewayPolicy resources can only be attached to a `gateway.networking.k8s.io` Gateway.

  * GCPGatewayPolicy resources must exist in the same namespace as the target Gateway.

  * When using a single cluster Gateway, GCPBackendPolicy, and HealthCheckPolicy resources must refer to a Service resource.

  * When using a multi-cluster Gateway, GCPBackendPolicy, and HealthCheckPolicy, resources must refer to a ServiceImport resource.

  * Only one GCPBackendPolicy can be attached to a Service at any given time. When two GCPBackendPolicy policies are created that target the same Service or ServiceImport, the oldest policy takes precedence and the second one fails to be attached.

  * Hierarchical policies are not supported with GKE Gateway.

  * HealthCheckPolicy, and GCPBackendPolicy resources must exist in the same namespace as the target Service or ServiceImport resource.

  * GCPBackendPolicy and HealthCheckPolicy resources are structured in a way that they can reference only one backend service.

  * GCPBackendPolicy does not support `HEADER_FIELD` or `HTTP_COOKIE` options for session affinity. For `HEADER_FIELD` or `HTTP_COOKIE` session affinity, use the GCPTrafficDistributionPolicy resource.

  * Don't use the same backend Service across Gateways of different GatewayClass types (such as Global versus Regional, Internal versus External, or Managed versus Classic) if those Gateways require incompatible configurations. For example, a GCPBackendPolicy configured with features unsupported by a "Classic" GatewayClass cannot be applied to a Service that is also used by a "Classic" Gateway. To ensure correct configuration, create a distinct Service for each Gateway that requires different policy settings.

  * Session affinity configured using a GCPTrafficDistributionPolicy is supported for single-cluster Gateways only.

  * GCPTrafficDistributionPolicy session affinity is not compatible with InferencePool resources because they use dedicated locality load balancing algorithms.

  * GCPTrafficDistributionPolicy does not support configuring session affinity or locality load balancing policies for the classic Application Load Balancer.

  * When using a single-cluster Gateway, GCPBackendPolicy and HealthCheckPolicy resources must refer to a Service or InferencePool resource.

  * When using a multi-cluster Gateway, GCPBackendPolicy and HealthCheckPolicy resources must refer to a ServiceImport or GCPInferencePoolImport resource.

  * Only one GCPBackendPolicy can be attached to a single target resource (Service, ServiceImport, InferencePool, or GCPInferencePoolImport) at any given time. When multiple GCPBackendPolicy resources are created that target the same resource, the oldest policy takes precedence and the newer one fails to be attached.

  * HealthCheckPolicy and GCPBackendPolicy resources must exist in the same namespace as the target Service, ServiceImport, InferencePool, or GCPInferencePoolImport resource.

  * GCPBackendPolicy and HealthCheckPolicy resources can only target a single resource (such as a Service or InferencePool).




**Best practice:** Create a distinct Service for each Gateway using a different GatewayClass to ensure compatibility between the Service's policies and the load balancer type.

## Configure global access for your regional internal Gateway

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

To enable global access with your internal Gateway, attach a policy to the Gateway resource.

The following GCPGatewayPolicy manifest enables regional internal Gateway for global access:
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPGatewayPolicy
    metadata:
      name: my-gateway-policy
      namespace: default
    spec:
      default:
        # Enable global access for the regional internal Application Load Balancer.
        allowGlobalAccess: true
      targetRef:
        group: gateway.networking.k8s.io
        kind: Gateway
        name: my-gateway
    

**Note:** Upgrading an existing internal Gateway by adding global access recreates the forwarding rule of your regional internal load balancer. **This upgrade deletes and then re-creates Google Cloud load balancers which results in up to 15 minutes of unavailability.** We recommend performing this operation during a maintenance window to avoid any application downtime.

## Configure the region for your multi-cluster Gateway

This section describes a functionality that is available on GKE clusters running version 1.30.3-gke.1225000 or later.

If your fleet has clusters across multiple regions, you might need to deploy regional Gateways in different regions for a variety of use cases, for example, cross-region redundancy, low latency and data sovereignty. In your multi-cluster Gateway config cluster, you can specify the region in which you want to deploy the regional Gateways. If you don't specify a region, the default region is the config cluster's region.

To configure a region for your multi-cluster Gateway, use the `region` field in the GCPGatewayPolicy. In the following example, the Gateway is configured in the `us-central1` region:
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPGatewayPolicy
    metadata:
      name: my-gateway-policy
      namespace: default
    spec:
      default:
        region: us-central1
      targetRef:
        group: gateway.networking.k8s.io
        kind: Gateway
        name: my-regional-gateway
    

**Note:** If you update the region in an existing regional multi-cluster Gateway, the underlying load balancer is deleted in the old region and recreated in the new region.

## Configure SSL policies to secure client-to-load-balancer traffic

This section describes functionality available on GKE clusters running version 1.24 or later.

To secure client-to-load-balancer traffic, configure the SSL policy by adding the name of the policy to the GCPGatewayPolicy. By default, the Gateway does not have an SSL policy defined and attached.

Ensure that you [create an SSL policy](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#create_ssl_policies) before referencing the policy in the GCPGatewayPolicy resource.

**Note:** For a regional Gateway, ensure that you create a regional SSL policy. An SSL policy applies to the frontend TLS configuration, which includes both standard TLS and mTLS.

The following GCPGatewayPolicy manifest specifies a security policy named `gke-gateway-ssl-policy`:
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPGatewayPolicy
    metadata:
      name: my-gateway-policy
      namespace: team1
    spec:
      default:
        sslPolicy: gke-gateway-ssl-policy
      targetRef:
        group: gateway.networking.k8s.io
        kind: Gateway
        name: my-gateway
    

## Configure health checks

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

By default, for backend services that use the `HTTP` or `kubernetes.io/h2c` application protocols, the HealthCheck is of the `HTTP` type. For the `HTTPS` protocol, the default HealthCheck is of the `HTTPS` type. For the `HTTP2` protocol, the default HealthCheck is of the `HTTP2` type.

You can use a HealthCheckPolicy to control the load balancer health check settings. Each type of health check (`http`, `https`, `grpc`, `http2`, and `tcp`) has parameters that you can define. Google Cloud creates a unique health check for each backend service for each GKE Service.

For your load balancer to function normally, you might need to configure a custom HealthCheckPolicy for your load balancer if your health check path isn't the standard "/". This configuration is also necessary if you need to adjust the health check parameters. For example, if the default request path is "/" but your service can't be accessed at that request path and instead uses "/health" to report its health, then you must configure `requestPath` in your HealthCheckPolicy accordingly.

When configuring health checks, keep the following limitations in mind:

  * Unlike GKE Ingress, GKE Gateway does not automatically infer health check parameters (such as path, port, or protocol) from your Pod's readiness or liveness probes. If your service does not return a successful response on the default root path (`/`), you must explicitly configure a `HealthCheckPolicy`.
  * Google Cloud health check probes strictly require an HTTP `200` (OK) response code. If your application returns redirects (for example, HTTP `301` or `302`) or client errors (for example, HTTP `401` or `403` on authenticated endpoints) on the probed path, the load balancer will mark the backend unhealthy, resulting in a "No healthy upstream" error.
  * You cannot configure custom HTTP request headers (such as `Authorization` headers) in GKE Gateway `HealthCheckPolicy` probes. If your backend requires authentication headers, you must configure your application to allow unauthenticated access specifically to your dedicated health check path (for example, `/healthz` or `/ping`) for [Google Cloud health check IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

**Note:** To enable the Gateway controller to process health checks and update parameters, the Service that you define in the health check policy must also be referenced in the HTTPRoute manifest.

The following HealthCheckPolicy manifest shows all the fields available when configuring a health check policy:

### Service
    
    
    # Health check configuration for the load balancer. For more information
    # about these fields, see https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks.
    apiVersion: networking.gke.io/v1
    kind: HealthCheckPolicy
    metadata:
      name: lb-healthcheck
      namespace: lb-service-namespace
    spec:
      default:
        checkIntervalSec: INTERVAL  # The default value is 15 seconds.
        timeoutSec: TIMEOUT
        healthyThreshold: HEALTHY_THRESHOLD
        unhealthyThreshold: UNHEALTHY_THRESHOLD
        logConfig:
          enabled: true
        config:
          type: PROTOCOL
          httpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          httpsHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          grpcHealthCheck:
            grpcServiceName: GRPC_SERVICE_NAME
            portSpecification: PORT_SPECIFICATION
            port: PORT
          http2HealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          tcpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            portName: PORT_NAME
            request: REQUEST
            response: RESPONSE
            proxyHeader: PROXY_HEADER
      # Attach to a Service in the cluster.
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: HealthCheckPolicy
    metadata:
      name: lb-healthcheck
      namespace: lb-service-namespace
    spec:
      # The default and config fields control the health check configuration for the
      # load balancer. For more information about these fields, see
      # https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks.
      default:
        checkIntervalSec: INTERVAL
        timeoutSec: TIMEOUT
        healthyThreshold: HEALTHY_THRESHOLD
        unhealthyThreshold: UNHEALTHY_THRESHOLD
        logConfig:
          enabled: ENABLED
        config:
          type: PROTOCOL
          httpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          httpsHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          grpcHealthCheck:
            grpcServiceName: GRPC_SERVICE_NAME
            portSpecification: PORT_SPECIFICATION
            port: PORT
          http2HealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          tcpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            portName: PORT_NAME
            request: REQUEST
            response: RESPONSE
            proxyHeader: PROXY_HEADER
      # Attach to a multi-cluster Service by referencing the ServiceImport.
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

### InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: HealthCheckPolicy
    metadata:
      name: lb-healthcheck
      namespace: lb-service-namespace
    spec:
      default:
        checkIntervalSec: INTERVAL  # The default value is 15 seconds.
        timeoutSec: TIMEOUT
        healthyThreshold: HEALTHY_THRESHOLD
        unhealthyThreshold: UNHEALTHY_THRESHOLD
        logConfig:
          enabled: true
        config:
          type: PROTOCOL
          httpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          httpsHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          grpcHealthCheck:
            grpcServiceName: GRPC_SERVICE_NAME
            portSpecification: PORT_SPECIFICATION
            port: PORT
          http2HealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          tcpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            portName: PORT_NAME
            request: REQUEST
            response: RESPONSE
            proxyHeader: PROXY_HEADER
      # Attach to an InferencePool in the cluster.
      targetRef:
        group: inference.networking.k8s.io
        kind: InferencePool
        name: my-inference-pool
    

### Multi-cluster InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: HealthCheckPolicy
    metadata:
      name: lb-healthcheck
      namespace: lb-service-namespace
    spec:
      default:
        checkIntervalSec: INTERVAL
        timeoutSec: TIMEOUT
        healthyThreshold: HEALTHY_THRESHOLD
        unhealthyThreshold: UNHEALTHY_THRESHOLD
        logConfig:
          enabled: true
        config:
          type: PROTOCOL
          httpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          httpsHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          grpcHealthCheck:
            grpcServiceName: GRPC_SERVICE_NAME
            portSpecification: PORT_SPECIFICATION
            port: PORT
          http2HealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            host: HOST
            requestPath: REQUEST_PATH
            response: RESPONSE
            proxyHeader: PROXY_HEADER
          tcpHealthCheck:
            portSpecification: PORT_SPECIFICATION
            port: PORT
            portName: PORT_NAME
            request: REQUEST
            response: RESPONSE
            proxyHeader: PROXY_HEADER
      # Attach to a multi-cluster InferencePool.
      targetRef:
        group: networking.gke.io
        kind: GCPInferencePoolImport
        name: my-inference-pool-import
    

Replace the following:

  * `INTERVAL`: specifies the [check-interval](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes), in seconds, for each health check prober. This is the time from the start of one prober's check to the start of its next check. If you omit this parameter, the Google Cloud default is 15 seconds if no HealthCheckPolicy is specified, and is 5 seconds when a HealthCheckPolicy is specified with no `checkIntervalSec` value. For more information, see [Multiple probes and frequency](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#multiple-probers).
  * `TIMEOUT`: specifies the amount of time that Google Cloud waits for a response to a probe. The value of `TIMEOUT` must be less than or equal to the `INTERVAL`. Units are seconds. Each probe requires an HTTP 200 (OK) response code to be delivered before the probe timeout.
  * `HEALTHY_THRESHOLD` and `UNHEALTHY_THRESHOLD`: specifies the number of sequential connection attempts that must succeed or fail, for at least one prober, to change the [health state](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state) from healthy to unhealthy or unhealthy to healthy. If you omit one of these parameters, the Google Cloud default is 2.
  * `PROTOCOL`: specifies a [protocol](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol) used by probe systems for health checking. For more information, see [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http), [Success criteria for gRPC](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-grpc) and [Success criteria for TCP](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp). This parameter is required.
  * `ENABLED`: specifies if logging is enabled or disabled.
  * `PORT_SPECIFICATION`: specifies if the health check uses a fixed port (`USE_FIXED_PORT`), named port (`USE_NAMED_PORT`) or serving port (`USE_SERVING_PORT`). If not specified, the health check follows the behavior specified in the `port` field. If `port` is not specified, this field defaults to `USE_SERVING_PORT`.
  * `PORT`: A HealthCheckPolicy only supports specifying [the load balancer health check port by using a port number](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_port_specification). If you omit this parameter, the Google Cloud default is 80. Because the load balancer sends probes to the Pod's IP address directly, you should select a port matching a `containerPort` of a serving Pods, even if the `containerPort` is referenced by a `targetPort` of the Service. You are not limited to `containerPorts` referenced by a Service's `targetPort`.
  * `HOST`: the value of the host header in the health check request. This value uses the [ RFC 1123 ](https://www.rfc-editor.org/rfc/rfc1123#page-13) definition of a hostname except numeric IP addresses are not allowed. If not specified or left empty, this value defaults to the IP address of the health check.
  * `REQUEST`: Specifies the application data to send after the TCP connection is established. If not specified, the value defaults to empty. If both the request and response are empty, the established connection, by itself, indicates health. The request data can only be in ASCII format.
  * `REQUEST_PATH`: specifies the [request-path](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) of the health check request. If not specified or left empty, defaults to `/`.
  * `RESPONSE`: specifies the bytes to match against the beginning of the response data. If not specified or left empty, GKE interprets any response as healthy. The response data can only be ASCII.
  * `PROXY_HEADER`: specifies the proxy header type. You can use `NONE` or `PROXY_V1`. Defaults to `NONE`.
  * `GRPC_SERVICE_NAME`: an optional name of the gRPC Service. Omit this field to specify all Services.



For more information about HealthCheckPolicy fields, see the `healthChecks` [reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks).

## Configure Cloud Armor backend security policy to secure your backend services

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

**Note:** Google Cloud has replaced the LbPolicy policy with the GCPBackendPolicy policy. The LbPolicy is still supported, but with no additional attributes.

Configure the Cloud Armor backend security policy by adding the name of your security policy to the GCPBackendPolicy to secure your backend services. By default, the Gateway does not have any Cloud Armor backend security policy defined and attached.

Make sure that you [create a Cloud Armor backend security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies) prior to referencing the policy in your GCPBackendPolicy. If you are enabling a regional Gateway, then you must create a _regional_ Cloud Armor backend security policy.

The following GCPBackendPolicy manifest specifies a backend security policy named `example-security-policy`:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Apply a Cloud Armor security policy.
        securityPolicy: example-security-policy
      # Attach to a Service in the cluster.
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Apply a Cloud Armor security policy.
        securityPolicy: example-security-policy
      # Attach to a multi-cluster Service by referencing the ServiceImport.
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

### InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        securityPolicy: example-security-policy
      # Attach to an InferencePool in the cluster.
      targetRef:
        group: inference.networking.k8s.io
        kind: InferencePool
        name: my-inference-pool
    

### Multi-cluster InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        securityPolicy: example-security-policy
      # Attach to a multi-cluster InferencePool.
      targetRef:
        group: networking.gke.io
        kind: GCPInferencePoolImport
        name: my-inference-pool-import
    

## Configure IAP

Identity-Aware Proxy (IAP) enforces access control policies on backend services associated with an HTTPRoute. With this enforcement, only authenticated users or applications with the correct Identity and Access Management (IAM) role assigned can access these backend services.

By default, there is no IAP applied to your backend services, you need to explicitly configure IAP in a GCPBackendPolicy.

To configure IAP with Gateway, do the following:

  1. Get the client ID and client secret for your OAuth client. The client secret is available only when you create your OAuth client. For more information, see [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257).
  2. [Enable IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto#enabling_iap).

You don't need to [create a BackendConfig](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto#kubernetes-configure), because BackendConfig is an Ingress configuration resource.

  3. To specify IAP policy referencing a secret:

     1. Save the following GCPBackendPolicy manifest as `backend-policy.yaml`:

### Service
            
            apiVersion: networking.gke.io/v1
            kind: GCPBackendPolicy
            metadata:
              name: backend-policy
            spec:
              default:
                # IAP OAuth2 settings. For more information about these fields,
                # see https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#oauth2.
                iap:
                  enabled: true
                  oauth2ClientSecret:
                    name: CLIENT_SECRET
                  clientID: CLIENT_ID
              # Attach to a Service in the cluster.
              targetRef:
                group: ""
                kind: Service
                name: SERVICE_NAME
            

Replace the following:

        * `CLIENT_SECRET`: the OAuth client secret.
        * `CLIENT_ID`: the OAuth client ID.
        * `SERVICE_NAME`: the name of the Service to target in the GCPBackendPolicy.

### Multi-cluster Service
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: backend-policy
    spec:
      default:
        # IAP OAuth2 settings. For more information about these fields,
        # see https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#oauth2.
        iap:
          enabled: true
          oauth2ClientSecret:
            name: CLIENT_SECRET
          clientID: CLIENT_ID
      # Attach to a multi-cluster Service by referencing the ServiceImport.
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: SERVICEIMPORT_NAME
    

Replace the following:

        * `CLIENT_SECRET`: the OAuth client secret.
        * `CLIENT_ID`: the OAuth client ID.
        * `SERVICEIMPORT_NAME`: the name of the ServiceImport to target in the GCPBackendPolicy.

     2. Apply the `backend-policy.yaml` manifest:
            
            kubectl apply -f backend-policy.yaml
            

  4. Verify your configuration:

     1. Confirm that the policy was applied after creating your GCPBackendPolicy with IAP:
            
            kubectl get gcpbackendpolicy
            

The output is similar to the following:
            
            NAME             AGE
            backend-policy   45m
            

     2. To get more details, use the describe command:
            
            kubectl describe gcpbackendpolicy
            

The output is similar to the following:
            
            Name:         backend-policy
            Namespace:    default
            Labels:       <none>
            Annotations:  <none>
            API Version:  networking.gke.io/v1
            Kind:         GCPBackendPolicy
            Metadata:
              Creation Timestamp:  2023-05-27T06:45:32Z
              Generation:          2
              Resource Version:    19780077
              UID:                 f4f60a3b-4bb2-4e12-8748-d3b310d9c8e5
            Spec:
              Default:
                Iap:
                  Client ID:  441323991697-luotsrnpboij65ebfr13hlcpm5a4heke.apps.googleusercontent.com
                  Enabled:    true
                  oauth2ClientSecret:
                    Name:  my-iap-secret
              Target Ref:
                Group:
                Kind:   Service
                Name:   lb-service
            Status:
              Conditions:
                Last Transition Time:  2023-05-27T06:48:25Z
                Message:
                Reason:                Attached
                Status:                True
                Type:                  Attached
            Events:
              Type     Reason  Age                 From                   Message
              ----     ------  ----                ----                   -------
              Normal   ADD     46m                 sc-gateway-controller  default/backend-policy
              Normal   SYNC    44s (x15 over 43m)  sc-gateway-controller  Application of GCPBackendPolicy "default/backend-policy" was a success
            




## Configure backend service timeout

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

**Note:** Google Cloud has replaced the LbPolicy policy with the GCPBackendPolicy policy. The LbPolicy is still supported, but with no additional attributes.

The following GCPBackendPolicy manifest specifies a [backend service timeout](https://docs.cloud.google.com/load-balancing/docs/backend-service#timeout-setting) period of 40 seconds. The `timeoutSec` field defaults to 30 seconds.

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Backend service timeout, in seconds, for the load balancer. The default
        # value is 30.
        timeoutSec: 40
      # Attach to a Service in the cluster.
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        timeoutSec: 40
      # Attach to a multi-cluster Service by referencing the ServiceImport.
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

### InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        timeoutSec: 40
      # Attach to an InferencePool in the cluster.
      targetRef:
        group: inference.networking.k8s.io
        kind: InferencePool
        name: my-inference-pool
    

### Multi-cluster InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        timeoutSec: 40
      # Attach to a multi-cluster InferencePool.
      targetRef:
        group: networking.gke.io
        kind: GCPInferencePoolImport
        name: my-inference-pool-import
    

## Configure backend selection using GCPBackendPolicy

The `CUSTOM_METRICS` balancing mode within the GCPBackendPolicy lets you configure specific custom metrics that influence how backend services of load balancers distribute traffic. This balancing mode enables load balancing based on custom metrics that you define, and that are reported by the application backends.

**Note:** The `CUSTOM_METRICS` balancing mode is available only on GKE version 1.33 and later.

For more information, see [Traffic management with custom metrics-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#custom-metrics).

The `customMetrics[]` array, in the `backends[]` field, contains the following fields:

  * `name`: specifies the user-defined name of the custom metric.
  * `maxUtilization`: sets the target or maximum utilization for this metric. The valid range is [0, 100].
  * `dryRun`: a boolean field. When true, the metric data reports to Cloud Monitoring but does not influence load balancing decisions.



**Example**

The following example shows a GCPBackendPolicy manifest that configures custom metrics for backend selection and endpoint-level routing.

  1. Save the following manifest as `my-backend-policy.yaml`:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
           namespace: team-awesome
         spec:
           # Attach to the super-service Service.
           targetRef:
             kind: Service
             name: super-service
           default:
             backends:
             # Configuration for all locations.
             - location: "*"
               # Use the rate balancing mode for the load balancer.
               balancingMode: RATE
               # Maximum number of requests per second for each endpoint.
               maxRatePerEndpoint: 9000
             # Configuration for us-central1-a
             - location: us-central1-a
               # maxRatePerEndpoint: 9000 inherited from the * configuration.
               # Use the custom metrics balancing mode for the load balancer.
               balancingMode: CUSTOM_METRICS
               # Configure the custom metrics for the load balancer to use.
               customMetrics:
               - name: gpu-load
                 maxUtilizationPercent: 100 # value ranges from 0 to 100 and maps to the floating point range [0.0, 1.0]
                 dryRun: false
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f my-backend-policy.yaml
         




The load balancer distributes traffic based on the `RATE` balancing mode and the custom `gpu-load` metric.

## Configure endpoint level routing with GCPTrafficDistributionPolicy

The GCPTrafficDistributionPolicy API in Google Kubernetes Engine (GKE) Gateway provides advanced traffic management capabilities that enable precise control over how traffic is distributed to your application pods. This unified, GKE-native resource simplifies managing load balancing algorithms and session affinity settings.

The GCPTrafficDistributionPolicy lets you configure:

  * **Load Balancing Algorithms** : specify how traffic is distributed among endpoints within a backend.

    * **`WEIGHTED_ROUND_ROBIN`** : when you select this algorithm, the load balancer uses custom metrics to compute weights and distribute traffic based on these reported metrics. The `customMetrics[]` array within the GCPTrafficDistributionPolicy configuration includes the following fields:

      * `name`: specifies the user-defined name of the custom metric.
      * `dryRun`: when `true`, the metric data is reported to Cloud Monitoring but doesn't influence load balancing.
**Note:** Custom metrics defined within GCPTrafficDistributionPolicy apply only to the `WEIGHTED_ROUND_ROBIN` `localityLbPolicy` and are not inherited from `backends[].customMetrics[]` in GCPBackendPolicy.
  * **`RING_HASH`** : this algorithm is beneficial for services sensitive to cache performance. It uses consistent hashing to minimize request remapping when backend pods are added or removed, which helps ensure stability during scaling events. Configuring the `minimumHashRingSize` field provides more granular load distribution.

  * **Session affinity** : helps ensure that requests from the same client are consistently routed to the same backend Pod. This is crucial for stateful workloads, such as ecommerce shopping carts or gaming sessions. GKE Gateway uses GCPTrafficDistributionPolicy to support all session affinity types available on Google Cloud Application Load Balancer instances, including `STRONG_COOKIE_AFFINITY`, `HEADER_FIELD`, `HTTP_COOKIE`, `GENERATED_COOKIE`, and `CLIENT_IP`.




For more information, see [Traffic management with custom metrics-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#custom-metrics).

**Example**

The following example shows a GCPTrafficDistributionPolicy manifest that configures endpoint-level routing by using both the `WEIGHTED_ROUND_ROBIN` load balancing algorithm and custom metrics.

  1. Save the following sample manifest as `GCPTrafficDistributionPolicy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPTrafficDistributionPolicy
         metadata:
           name: echoserver-v2
           namespace: team1
         spec:
           targetRefs:
           # Attach to the echoserver-v2 Service in the cluster.
           - kind: Service
             group: ""
             name: echoserver-v2
           default:
             # Use custom metrics to distribute traffic across endpoints.
             localityLbAlgorithm: WEIGHTED_ROUND_ROBIN
             # Configure metrics from an ORCA load report to use for traffic
             # distribution.
             customMetrics:
             - name: orca.named_metrics.bescm11
               dryRun: false
             - name: orca.named_metrics.bescm12
               dryRun: true
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f GCPTrafficDistributionPolicy.yaml
         




The load balancer distributes traffic to endpoints based on the `WEIGHTED_ROUND_ROBIN` algorithm and the provided custom metrics.

### Configure hash ring size

For services where minimizing cache misses is critical, use the `RING_HASH` algorithm. Adjusting the `minimumHashRingSize` field allows for more granular load distribution across backends. While the load balancer automatically manages the ring size, providing a higher minimum value can help ensure a more even distribution of requests for larger backend sets.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: ring-hash-policy
      namespace: default
    spec:
      default:
        localityLbAlgorithm: RING_HASH
        # Defaults to 1024. Larger ring sizes result in more granular
        # load distributions. Supported range is 1 to 2048.
        minimumHashRingSize: 1024
      targetRefs:
      -   group: ""
        kind: Service
        name: my-cache-heavy-service
    

**Note:** The `minimumHashRingSize` field defaults to 1024. While you can increase this up to 2048, the underlying load balancer may use larger ring sizes internally to optimize performance regardless of this setting.

## Configure session affinity

**Warning:** Weighted traffic splitting takes precedence over session affinity. If limited session affinity is incompatible with your workload, don't configure weighted traffic splitting on the same route rule where session stickiness is required.

Configure session affinity to help ensure that requests from the same client are consistently routed to the same backend Pod.

### Configure session affinity using GCPTrafficDistributionPolicy (default)

The session affinity types described in this section require the following minimum GKE versions:

  * **`CLIENT_IP`, `HEADER_FIELD`, `GENERATED_COOKIE`, and `HTTP_COOKIE`:** version 1.35.2-gke.1269001 or later.
  * **`STRONG_COOKIE_AFFINITY`:** version 1.36.3-gke.1767000 or later.



GKE Gateway supports all session affinity types by using the GCPTrafficDistributionPolicy resource. This resource provides more granular control, such as routing based on custom HTTP headers or cookies. Configuring session affinity by using GCPTrafficDistributionPolicy is the default and recommended method.

The following table describes the affinity types that are supported when you use GCPTrafficDistributionPolicy:

Affinity type | Description  
---|---  
`STRONG_COOKIE_AFFINITY` | Stateful cookie-based session persistence. Helps ensure strong session stickiness across scaling events and Pod pool resizes. You must configure the `cookie.name` field, and can optionally configure the `cookie.path` and `cookie.ttl` fields. Works with any `localityLbAlgorithm` setting (the default value is `ROUND_ROBIN`).   
`HTTP_COOKIE` | Affinity based on an HTTP cookie. When responding to the first request, the load balancer generates a cookie and provides it in a `Set-Cookie` response header. On subsequent requests, the client returns the cookie provided by the load balancer, and the load balancer uses it to route requests consistently to the same Pods. You must configure the `cookie.name` field, and can optionally configure the `cookie.path` and `cookie.ttl` fields. Requires the `localityLbAlgorithm` field to be set to `MAGLEV` or `RING_HASH`.   
`GENERATED_COOKIE` | The load balancer generates a cookie to track the session. The name of the cookie is `GCLB` for global external Application Load Balancers, and `GCILB` for regional internal Application Load Balancers and regional external Application Load Balancers. The cookie path is `/`. You can optionally configure the `cookie.ttl` field up to a maximum of two weeks; the `cookie.name` and `cookie.path` fields are not configurable for this type. Requires the `localityLbAlgorithm` field to be set to `MAGLEV` or `RING_HASH`.   
`HEADER_FIELD` | Affinity based on a specific HTTP header. Requires the `localityLbAlgorithm` field to be set to `MAGLEV` or `RING_HASH`.  
`CLIENT_IP` | Affinity based on the client's IP address. Requires the `localityLbAlgorithm` field to be set to `MAGLEV` or `RING_HASH`.  
`NONE` | Disables session affinity.  
  
The following examples demonstrate how to configure GCPTrafficDistributionPolicy grouped by affinity category: cookie-based, header-based, and client IP-based session affinity.

To apply any of the following session affinity configurations to your cluster do the following:

  1. Save the chosen manifest as `policy.yaml`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f policy.yaml
         




#### Cookie-based session affinity

Cookie-based session affinity includes the `STRONG_COOKIE_AFFINITY`, `HTTP_COOKIE`, and `GENERATED_COOKIE` affinity types.

**Stateful cookie affinity (`STRONG_COOKIE_AFFINITY`)**

Stateful cookie affinity (`STRONG_COOKIE_AFFINITY`) provides stateful session persistence that maintains stickiness even during backend scaling events.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: strong-cookie-affinity-policy
      namespace: default
    spec:
      default:
        sessionAffinity:
          type: STRONG_COOKIE_AFFINITY
          cookie:
            name: "GKE_STATEFUL_SESSION"
            path: "/"
            ttl: "24h"
      targetRefs:
      - group: ""
        kind: Service
        name: my-stateful-service
    

**HTTP cookie affinity (`HTTP_COOKIE`)**

The `HTTP_COOKIE` affinity type bases affinity on a specific named cookie returned in a `Set-Cookie` header. To use session affinity types other than `NONE` and `STRONG_COOKIE_AFFINITY`, you must set the `localityLbAlgorithm` field to either `MAGLEV` or `RING_HASH`.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: http-cookie-affinity-policy
      namespace: default
    spec:
      default:
        sessionAffinity:
          type: HTTP_COOKIE
          cookie:
            name: "my-app-session-id"
            path: "/"
            ttl: "3600s"
        # HTTP_COOKIE affinity requires localityLbAlgorithm to be MAGLEV or RING_HASH.
        localityLbAlgorithm: MAGLEV
      targetRefs:
      - group: ""
        kind: Service
        name: my-stateful-service
    

**Generated cookie affinity (`GENERATED_COOKIE`)**

The `GENERATED_COOKIE` affinity type lets the load balancer generate and name the session cookie automatically. You can optionally configure the value of the `cookie.ttl` field up to two weeks (`336h`).
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: generated-cookie-affinity-policy
      namespace: default
    spec:
      default:
        sessionAffinity:
          type: GENERATED_COOKIE
          cookie:
            ttl: "2h30m"
        # GENERATED_COOKIE affinity requires localityLbAlgorithm to be MAGLEV or RING_HASH.
        localityLbAlgorithm: MAGLEV
      targetRefs:
      - group: ""
        kind: Service
        name: my-stateful-service
    

The behavior of zero TTL for cookie-based session affinity includes the following:

  * All cookie-based session affinities (`STRONG_COOKIE_AFFINITY`, `HTTP_COOKIE`, and `GENERATED_COOKIE`) have a `ttl` attribute.

  * A TTL of zero seconds means the load balancer does not assign an `Expires` attribute to the cookie. In this case, the client treats the cookie as a session cookie. The definition of a session varies depending on the client:

    * Some clients, like web browsers, retain the cookie for the entire browsing session. Thi approach means that the cookie persists across multiple requests until the application is closed.
    * Other clients treat a session as a single HTTP request, discarding the cookie immediately after the session ends.



#### Header-based session affinity

The `HEADER_FIELD` affinity type routes traffic based on a specific HTTP header for scenarios such as A/B testing or specialized client routing where a cookie is not suitable. To use session affinity types other than `NONE` and `STRONG_COOKIE_AFFINITY`, you must set the `localityLbAlgorithm` field to either `MAGLEV` or `RING_HASH`. Unlike the default `ROUND_ROBIN`, these algorithms support consistent hashing based on custom fields such as HTTP headers.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: header-affinity-policy
      namespace: default
    spec:
      default:
        sessionAffinity:
          type: HEADER_FIELD
          httpHeaderName: "X-User-Group-ID"
        localityLbAlgorithm: MAGLEV
      targetRefs:
      - group: ""
        kind: Service
        name: SERVICE_NAME
    

#### Client IP-address-based session affinity

The `CLIENT_IP` affinity type routes traffic from a specific client IP address to the same backend Pod on a best-effort basis. To use session affinity types other than `NONE` and `STRONG_COOKIE_AFFINITY`, you must set the `localityLbAlgorithm` field to either `MAGLEV` or `RING_HASH`.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: client-ip-affinity-policy
      namespace: default
    spec:
      default:
        sessionAffinity:
          type: CLIENT_IP
        localityLbAlgorithm: MAGLEV
      targetRefs:
      - group: ""
        kind: Service
        name: SERVICE_NAME
    

#### Verify the policy

To ensure your GCPTrafficDistributionPolicy is correctly configured and active, verify its status after you apply it:

  1. To check the policy's status, run the following command:
         
         kubectl describe gcptrafficdistributionpolicy POLICY_NAME
         

Replace `POLICY_NAME` with the name of your policy.

  2. In the output, check the `Conditions` section. A status of `True` with the reason `Attached` indicates that the configuration is valid and active.




### Configure session affinity using GCPBackendPolicy

This section describes configuring session affinity using GCPBackendPolicy.

**Note:** To configure session affinity, we recommend that you use GCPTrafficDistributionPolicy instead. GCPBackendPolicy and LbPolicy remain supported for existing configurations. Using GCPBackendPolicy for session affinity is supported for existing configurations. If both policies target the same Service, the GCPTrafficDistributionPolicy configuration takes precedence.

You can configure GCPBackendPolicy session affinity based on the following criteria:

  * Client IP address (`CLIENT_IP`)
  * Generated cookie (`GENERATED_COOKIE`)



When you configure session affinity for your Service by using GCPBackendPolicy, the Gateway sets the `localityLbPolicy` setting on the backend service to `MAGLEV`. When you remove session affinity from GCPBackendPolicy, the Gateway reverts the `localityLbPolicy` setting to the default value, `ROUND_ROBIN`.

**Warning:** This locality value is silently set on the GKE-managed backend service and is not reflected in the output of a gcloud CLI command, in the UI, or with Terraform.

The following GCPBackendPolicy manifest specifies session affinity based on the client IP address:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # On a best-effort basis, send requests from a specific client IP address
        # to the same backend. This field also sets the load balancer locality
        # policy to MAGLEV. For more information, see
        # https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy
        sessionAffinity:
          type: CLIENT_IP
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # On a best-effort basis, send requests from a specific client IP address
        # to the same backend. This field also sets the load balancer locality
        # policy to MAGLEV. For more information, see
        # https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy
        sessionAffinity:
          type: CLIENT_IP
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

The following GCPBackendPolicy manifest specifies session affinity based on a generated cookie and configures the cookie TTL to 50 seconds:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Include an HTTP cookie in the Set-Cookie header of the response.
        # This field also sets the load balancer locality policy to MAGLEV. For more
        # information, see
        # https://docs.cloud.google.com/load-balancing/docs/l7-internal#generated_cookie_affinity.
        sessionAffinity:
          type: GENERATED_COOKIE
          cookieTtlSec: 50  # The cookie expires in 50 seconds.
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Include an HTTP cookie in the Set-Cookie header of the response.
        # This field also sets the load balancer locality policy to MAGLEV. For more
        # information, see
        # https://docs.cloud.google.com/load-balancing/docs/l7-internal#generated_cookie_affinity.
        sessionAffinity:
          type: GENERATED_COOKIE
          cookieTtlSec: 50  # The cookie expires in 50 seconds.
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

## Configure connection draining timeout

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

**Note:** Google Cloud has replaced the LbPolicy policy with the GCPBackendPolicy policy. The LbPolicy is still supported, but with no additional attributes.

You can configure [connection draining timeout](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) using GCPBackendPolicy. Connection draining timeout is the time, in seconds, to wait for connections to drain. The timeout duration can be from 0 to 3600 seconds. The default value is 0, which also disables connection draining.

The following GCPBackendPolicy manifest specifies a connection draining timeout of 60 seconds:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        connectionDraining:
          drainingTimeoutSec: 60
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        connectionDraining:
          drainingTimeoutSec: 60
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

### InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        connectionDraining:
          drainingTimeoutSec: 60
      # Attach to an InferencePool in the cluster.
      targetRef:
        group: inference.networking.k8s.io
        kind: InferencePool
        name: my-inference-pool
    

### Multi-cluster InferencePool

`yaml apiVersion: networking.gke.io/v1 kind: GCPBackendPolicy metadata: name: my-backend-policy namespace: lb-service-namespace spec: default: connectionDraining: drainingTimeoutSec: 60 # Attach to a multi-cluster InferencePool. targetRef: group: networking.gke.io kind: GCPInferencePoolImport name: my-inference-pool-import`

For the specified duration of the timeout, GKE waits for existing requests to the removed backend to complete. The load balancer does not send new requests to the removed backend. After the timeout duration is reached, GKE closes all remaining connections to the backend.

## HTTP access logging

This section describes a functionality that is available on GKE clusters running version 1.24 or later.

**Note:** Google Cloud has replaced the LbPolicy policy with the GCPBackendPolicy policy. The LbPolicy is still supported, but with no additional attributes.

By default:

  * The Gateway controller logs all HTTP requests from clients to [Cloud Logging](https://docs.cloud.google.com/logging/docs).
  * The sampling rate is 1,000,000, which means all requests are logged.
  * No optional fields are logged.



You can disable [access logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring) on your Gateway using a GCPBackendPolicy in three ways:

  * You can leave the GCPBackendPolicy with no `logging` section
  * You can set `logging.enabled` to `false`
  * You can set `logging.enabled` to `true` and set `logging.sampleRate` to `0`



You can also configure the access logging sampling rate and a list of optional fields, for example `tls.cipher` or `orcaLoadReport`.

To enable logging of the optional fields:

  * Set `logging.OptionalMode` to `CUSTOM`.
  * Provide the list of optional fields to be logged in `logging.optionalFields`. See [logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#log-fields) for the list of supported fields.



You can disable logging of the optional fields in two ways:

  * You can remove all entries from `logging.optionalFields`.
  * You can set `logging.OptionalMode` to `EXCLUDE_ALL_OPTIONAL`.



The following GCPBackendPolicy manifest modifies access logging's default sample rate and sets it to 50% of the HTTP requests. The manifest also enables logging of two optional fields for a given Service resource:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Access logging configuration for the load balancer.
        logging:
          enabled: true
          # Log 50% of the requests. The value must be an integer between 0 and
          # 1000000. To get the proportion of requests to log, GKE
          # divides this value by 1000000.
          sampleRate: 500000
          # Log specific optional fields.
          optionalMode: CUSTOM
          optionalFields:
          - tls.cipher
          - orcaLoadReport.cpu_utilization
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Access logging configuration for the load balancer.
        logging:
          enabled: true
          # Log 50% of the requests. The value must be an integer between 0 and
          # 1000000. To get the proportion of requests to log, GKE
          # divides this value by 1000000.
          sampleRate: 500000
          # Log specific optional fields.
          optionalMode: CUSTOM
          optionalFields:
          - tls.cipher
          - orcaLoadReport.cpu_utilization
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

### InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Access logging configuration for the load balancer.
        logging:
          enabled: true
          # Log 50% of the requests. The value must be an integer between 0 and
          # 1000000. To get the proportion of requests to log, GKE
          # divides this value by 1000000.
          sampleRate: 500000
          # Log specific optional fields.
          optionalMode: CUSTOM
          optionalFields:
          - tls.cipher
          - orcaLoadReport.cpu_utilization
      # Attach to an InferencePool in the cluster.
      targetRef:
        group: inference.networking.k8s.io
        kind: InferencePool
        name: my-inference-pool
    

### Multi-cluster InferencePool
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        # Access logging configuration for the load balancer.
        logging:
          enabled: true
          # Log 50% of the requests. The value must be an integer between 0 and
          # 1000000. To get the proportion of requests to log, GKE
          # divides this value by 1000000.
          sampleRate: 500000
          # Log specific optional fields.
          optionalMode: CUSTOM
          optionalFields:
          - tls.cipher
          - orcaLoadReport.cpu_utilization
      # Attach to a multi-cluster InferencePool.
      targetRef:
        group: networking.gke.io
        kind: GCPInferencePoolImport
        name: my-inference-pool-import
    

This manifest has the following fields:

  * `enable: true`: explicitly enables access logging. Logs are available in Logging.
  * `sampleRate: 500000`: specifies that 50% of packets are logged. You can use a value between 0 and 1,000,000. GKE converts this value to a floating point value in the range [0, 1] by dividing by 1,000,000. This field is only relevant if `enable` is set to `true`. `sampleRate` is an optional field, but if it's configured then `enable: true` must also be set. If `enable` is set to `true` and `sampleRate` is not provided then GKE sets `enable` to `false`.
  * `optionalMode: CUSTOM`: specifies that a set of `optionalFields` should be included in log entries.
  * `optionalFields: tls.cipher, orcaLoadReport.cpu_utilization`: specifies that log entries should include both the name of the cipher used for the TLS handshake and the service's CPU utilization, whenever these are available.



## Configure traffic-based autoscaling for your single-cluster Gateway

Ensure your GKE cluster is running the version 1.31.1-gke.2008000 or later.

To enable traffic-based autoscaling and capacity-based load balancing in a single-cluster Gateway, you can configure Service capacity. Service capacity is the ability to specify the amount of traffic capacity that a Service can receive before Pods are autoscaled or traffic overflows to other available clusters.

To configure Service capacity, create a Service and an associated GCPBackendPolicy. The GCPBackendPolicy manifest uses the field `maxRatePerEndpoint` which defines a maximum Requests per Second (RPS) value per Pod in a Service. The following GCPBackendPolicy manifest defines a maximum RPS of 10:
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: store
    spec:
      default:
        maxRatePerEndpoint: 10
      targetRef:
        group: ""
        kind: Service
        name: store
    

To learn more about traffic-based autoscaling, see [Autoscaling based on load balancer traffic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#autoscale-traffic).

## Troubleshooting

This section provides guidance for troubleshooting common issues when configuring Gateway resources using Policies.

### GCPTrafficDistributionPolicy not taking effect

**Symptom:** Traffic is not being distributed according to the session affinity or locality settings defined in your policy.

**Reason:** This typically occurs if the policy is not correctly bound to the Service or if the Gateway controller has encountered a validation error while attempting to sync the configuration to the load balancer.

**Workaround:**

  1. Verify policy status: Check if the policy has been attached to your Service:
         
         kubectl describe gcptrafficdistributionpolicy POLICY_NAME
         

Replace `POLICY_NAME` with the name of your policy.

In the output, look for the `Conditions` section. A status of `True` with the reason `Attached` indicates that the configuration is valid and has been applied. If the status is `False`, check the `Reason` and `Message` fields for validation errors (for example, an unsupported algorithm for the chosen affinity type).

  2. Verify Gateway configuration synchronization: Confirm that the Gateway managing the traffic has successfully synchronized these settings with the cloud infrastructure.

In the `Status` section, verify that the `Programmed` condition has a `Status` of `True`. If it is `False`, it indicates the Gateway controller encountered an error, potentially related to your GCPTrafficDistributionPolicy.

Check the `Reason` and `Message` fields next to the `Programmed` condition for immediate details. For more granular error messages or a history of synchronization failures, check the `Events` at the bottom of the output.




### Multiple GCPBackendPolicy attached to the same Service

**Symptom:**

The following status condition might occur when you attach a GCPBackendPolicy to a Service or a ServiceImport:
    
    
    status:
      conditions:
        - lastTransitionTime: "2023-09-26T20:18:03Z"
          message: conflicted with GCPBackendPolicy "[POLICY_NAME]" of higher precedence, hence not applied
          reason: Conflicted
          status: "False"
          type: Attached
    

**Reason:**

This status condition indicates that you are trying to apply a second GCPBackendPolicy to a Service or ServiceImport that already has a GCPBackendPolicy attached.

Multiple GCPBackendPolicy attached to the same Service or ServiceImport is not supported with GKE Gateway. See [Restrictions and Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#restrictions_and_limitations) for more details.

**Workaround:**

Configure a single GCPBackendPolicy that includes all custom configurations and attach it to your target resource (Service, ServiceImport, InferencePool, or GCPInferencePoolImport).

### Session affinity ignored during traffic splitting

**Symptom:**

Requests are not consistently routed to the same backend Pod even though session affinity is configured.

**Reason:**

Weighted traffic splitting takes precedence over session affinity. If an HTTPRoute defines weights for multiple backends, the load balancer first selects a backend based on weights before applying affinity logic.

**Workaround:**

Avoid using weighted traffic splitting on the same HTTPRoute rule where session stickiness is required.

### Cloud Armor security policy not found

**Symptom:**

The following error message might appear when you enable Cloud Armor on your regional Gateway:
    
    
    Invalid value for field 'resource': '{
    "securityPolicy":"projects/123456789/regions/us-central1/securityPolicies/<policy_name>"}'.
    The given security policy does not exist.
    

**Reason:**

The error message indicates that the specified regional Cloud Armor security policy does not exist in your Google Cloud project.

**Workaround:**

Create a regional [Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies) in your project and reference this policy in your GCPBackendPolicy.

## What's next

  * Learn how to [deploy a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Learn more about the [Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn how to [reference a Gateway from a resource](https://gateway-api.sigs.k8s.io/references/policy-attachment/#policy-attachment-for-ingress).
  * View the [Policy Types API reference](https://googlecloudplatform.github.io/gke-gateway-api/).
  * View the [API type definitions](https://github.com/GoogleCloudPlatform/gke-gateway-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
