---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks/
title: Configure health checks \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:51.100268+00:00
---

# Configure health checks  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure health checks Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides health checking mechanisms that determine whether backend instances respond appropriately to traffic. This document describes how to create and use health checks for load balancers. 

Unless otherwise noted, Google Cloud health checks are implemented by dedicated software tasks that connect to backends according to parameters specified in a health check resource. Each connection attempt is called a probe. Google Cloud records the success or failure of each probe.

The health status of each backend is determined by a configurable number of consecutive successful or failed probes. That is, you configure the number of consecutive probe successes needed to mark a backend healthy and the number of consecutive failures to mark it unhealthy.

This health status dictates whether a backend is eligible to receive new requests or connections. An unhealthy backend, as identified by the health check, won't receive traffic through the load balancer. You define the criteria for a successful probe. For more information, see the section How health checks work.

**Note:** The health check mechanism described here is applicable only to VM workload backends and not applicable to pods. You can configure HTTP(S) health checks for pods using [Kubernetes container probing](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

## Health check protocols

Health checks support the following protocols:

  * TCP
  * HTTP
  * HTTPS



## Select a health check

Health checks must be compatible with the type of load balancer and the backend types. Consider the following factors when selecting a health check:

  * **Protocol:** The protocol that GDC uses to probe the backends. The supported protocols are TCP, HTTP, and HTTPS. The TCP protocol is useful for basic health checks that validate connectivity to a backend, whereas the HTTP and HTTPS protocols provide more granular health checking mechanisms for VMs already running HTTP or HTTPS workloads.
  * **Port specification:** the port that GDC uses with the protocol to probe the health of a backend. You must specify a port for your health check.
  * **Category:** health checks can be global or zonal. Global health checks extend across all zones of a GDC deployment, whereas zonal health checks correspond to one zone. 



## How health checks work

The following sections describe how health checks work.

### Probes

When you establish a health check, you define or accept default settings that govern how often each probe assesses the health of associated endpoints. These settings are crucial because the load balancer stops routing requests to a backend deemed unhealthy using the criteria that you configured. The probe will persist in its evaluations and will resume sending traffic to the backend after it's deemed healthy again.

It's important to note that health check settings apply uniformly to all backends in a backend service or target pool and cannot be configured per backend.

Configuration flag  | Explanation  | Default value   
---|---|---  
check interval  `check-interval` | The time (in seconds) from the start of one probe to the start of the next probe by the same prober.  |  `5s` (5 seconds)   
timeoutSec  `timeoutSec` | The time (in seconds) to wait for a probe before claiming failure.  | `5s` (5 seconds)   
healthyThreshold  `healthyThreshold` | The number of sequential probes that must succeed for the endpoint to be considered healthy.  | 2   
unhealthyThreshold  `unhealthyThreshold` | The number of sequential probes that must fail for the endpoint to be considered unhealthy.  | 2   
  
### Success criteria for HTTP and HTTPS health checks

For HTTP and HTTPS health checks, an HTTP `200 (OK)` status code is required for a successful response before the health check timesout. Other HTTP response codes, including redirects (for example, 301, 302), are considered unhealthy. 

In addition to requiring an HTTP `200 (OK)` response code, you can:

  * Configure each health check prober to send HTTP requests to a specific request path instead of the default request path,`/`.
  * Configure each health check prober to check for the presence of an expected response string in the HTTP response body. The expected response string must consist only of single-byte, printable ASCII characters, located within the first 1,024 bytes of the HTTP response body.



The following table lists valid combinations of **requestPath** and **response** fields that are available for HTTP and HTTPS health checks.

Configuration flags  | Prober behavior  | Success criteria   
---|---|---  
Neither **RequestPath** nor **Response** specified  | The prober uses `/` as the request path.  | HTTP `200 (OK)` response code only.   
Both **RequestPath** and **Response** specified  | The prober uses the configured request path.  | HTTP `200 (OK)` response code _and_ up to the first 1,024 ASCII characters of the HTTP response body must match the expected response string.   
Only **Response** specified  | The prober uses `/` as the request path.  | HTTP `200 (OK)` response code _and_ up to the first 1,024 ASCII characters of the HTTP response body must match the expected response string.   
Only **RequestPath** specified  | The prober uses the configured request path.  | HTTP `200 (OK)` response code only.   
  
### Success criteria for TCP health checks

TCP health checks have the following base success criteria:

  * For TCP health checks, a health check prober must successfully open a TCP connection to the backend before the health check timeout.
  * For TCP health checks, the TCP connection must be closed in one of the following ways: 
    * By the health check prober sending either a FIN or RST (reset) packet.
    * By the backend sending a FIN packet. 
    * If a backend sends a TCP RST packet, the probe might be considered unsuccessful if the health check prober has already sent a FIN packet.



## Before you begin

To configure health check probes, you must have the following:

  * Own the project that you're configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * The necessary identity and access roles:

    * Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.
    * For global ILBs, ask your Organization IAM Admin to grant you the Global Load Balancer Admin (`global-load-balancer-admin`) role. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).

**Note:** `HealthCheck` objects are effective only for the load balancers linked to VM endpoints.

## Create and manage health checks

GDC supports global and zonal health checks.

## HealthCheck API

You can configure a `HealthCheck` object as global or zonal. Global `HealthCheck` objects are used for global load balancer configurations, while zonal `HealthCheck` objects are used for zonal load balancer configurations. Both types have the same name and specification. However, they use different apiVersion values and API servers:

  * Zonal apiVersion: [`networking.gdc.goog`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/networking-v1)
  * Global apiVersion: [`networking.global.gdc.goog`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/global-networking-v1)



You can also use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) to create and manage health checks.

### Create a global `HealthCheck`

The following example shows how to create a HealthCheck using the API:
    
    
      kubectl --kubeconfig GLOBAL_ORG_ADMIN_CLUSTER_KUBECONFIG apply -f - <<EOF 
      apiVersion: networking.global.gdc.goog/v1 
      kind: HealthCheck 
      metadata: 
        namespace: PROJECT 
        name: my-hc 
      spec: 
        httpHealthCheck: 
          port: PORT 
          host: HOST 
          requestPath: requestPath 
          response: responseT 
      EOF
    

### Create a zonal `HealthCheck`

The following example shows how to create a HealthCheck using the API:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f - <<EOF 
      apiVersion: networking.gdc.goog/v1
      kind: HealthCheck
      metadata:
        namespace: PROJECT
        name: my-hc
      spec:
        httpHealthCheck:
          port: PORT
          host: HOST
          requestPath: requestPath 
          response: response 
      EOF 
    

To link a health check to a load balancer, refer to the following:

  * [Configure internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service)
  * [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service)



#### Configuration Verification

To ensure that the configuration is correct, verify the `Ready` condition of the `HealthCheck` object. This condition indicates any configuration errors. Additionally, confirm that the fields accurately reflect the required `HealthCheck` settings.

### Additional usage notes

The following sections include additional notes about using health checks on Google Cloud.

#### Certificates and health checks

For protocols like HTTPS, that mandate certificates on your backends,

  * Certificates can be self-signed or from any certificate authority (CA).
  * Expired or future-dated certificates are acceptable.



#### Headers

When configuring health checks for HTTP or HTTPS protocols, you can specify an HTTP `Host` header using the `--host` flag.

It is important to note that the load balancer adds the custom request headers that you configure only to client requests, not to health check probes. Therefore, if your backend requires a specific header for authorization that is absent from the health check packet, the health check might fail.

#### Example health check

If a health check is configured with the following parameters:

  * Interval: 30 seconds
  * Timeout: 5 seconds
  * Protocol: HTTP
  * Unhealthy threshold: 2 (default)
  * Healthy threshold: 2 (default)



The health check will function as follows:

  * Each health check prober will: 
    1. Initiate an HTTP connection from a source IP address to the backend instance every 30 seconds.
    2. Wait up to five seconds for an HTTP `200 (OK)` status code to return (the designated success criteria for HTTP and HTTPS protocols).
  * A backend is deemed unhealthy if at least one health check probe system does the following: 
    1. Does not receive an HTTP `200 (OK)` response for two consecutive probes because of a refused connection, connection timeout, or socket timeout.
    2. Receives two consecutive responses that don't align with the protocol-specific success criteria.
  * A backend is considered healthy when at least one health check probe system receives two consecutive responses that meet the protocol-specific success criteria.



In this example, each prober initiates a connection every 30 seconds. Thirty seconds elapses between a prober's connection attempts regardless of the duration of the timeout (whether or not the connection timed out). In other words, the timeout must always be less than or equal to the interval, and the timeout never increases the interval.

## Limitations

  1. GDC health checks will only service VM endpoints.
  2. Load balancers with health checks cannot be configured with pods and VMs as mixed backends. A load balancer must consist of only pods or only VMs as its endpoints. As of now, a load balancer must consist of only pods or only VMs as its endpoints.
  3. Mutability for the load balancer and the associated health check is not yet supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
