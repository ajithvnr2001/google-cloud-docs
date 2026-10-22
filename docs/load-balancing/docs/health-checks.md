---
url: https://docs.cloud.google.com/load-balancing/docs/health-checks/
title: Use health checks \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:15.050016+00:00
---

# Use health checks  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/health-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use health checks Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides health checking mechanisms that determine whether backend instances respond properly to traffic. This document describes how to create and use health checks for [load balancers](https://docs.cloud.google.com/load-balancing/docs) and Cloud Service Mesh.

This page assumes that you are familiar with the following concepts:

  * [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts)
  * [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service)
  * [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls)

**Note:** The term _health check_ does not refer to legacy health checks. In this document, legacy health checks are explicitly called _legacy health checks_.

## Create health checks

Google Cloud lets you create or select a health check when you complete the load balancer's backend configuration in the Google Cloud console.

You can also create a health check independently of load balancer configuration in the Google Cloud console. This is useful if you need to create your health check first, or if you need to use a health check for multiple load balancers. You can create a health check using the Google Cloud console, the Google Cloud CLI, or the REST APIs.

**Note:** You must use legacy HTTP health checks for target pool based-regional external passthrough Network Load Balancers. For details, see legacy health checks. [Backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service) use the non-legacy health checks described in this section.

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click **Create a health check**.
  3. On the _Create a health check_ page, supply the following information: 
     * **Name** : Provide a name for the health check.
     * **Description** : Optionally, provide a description.
     * **Scope** : Select a scope, either **Global** or **Regional** , [depending on the type of load balancer](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide). 
       * If you selected **Regional** , pick a **Region** from the drop-down.
     * **Protocol** : Choose [a health check protocol](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#selecting_hc).
     * **Port** : Provide a port number. When you create a health check in the Google Cloud console, you must specify the port using a port number.
     * **Proxy protocol** : Optionally, you can append a proxy header to the requests made by the health check probe systems.
     * **Request path and Response** : For HTTP, HTTPS, and HTTP2 protocols, you can optionally provide a URL path for the health check probe systems to contact. For more information, see Additional flags for HTTP, HTTPS, and HTTP/2 health checks.
     * **Request** and **Response** : For TCP and SSL protocols, you can specify an ASCII text string to send and expected text response string. For more information, see Additional flags for SSL and TCP health checks.
     * **Check interval** : Define the amount of time from the start of one probe to the start of the next one.
     * **Timeout** : Define the amount of time that Google Cloud waits for a response to a probe. Its value must be less than or equal to the check interval.
     * **Healthy threshold** : Define the number of sequential probes that must succeed for the VM instance to be considered healthy.
     * **Unhealthy threshold** : Define the number of sequential probes that must fail for the VM instance to be considered unhealthy.
  4. Click **Create**.



###  gcloud 

  * To create a global health check, use the [appropriate `compute health-checks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create) command:
        
        gcloud compute health-checks create PROTOCOL NAME \
            --global \
            --description=DESCRIPTION \
            --check-interval=CHECK_INTERVAL \
            --timeout=TIMEOUT \
            --healthy-threshold=HEALTHY_THRESHOLD \
            --unhealthy-threshold=UNHEALTHY_THRESHOLD \
            PORT_SPECIFICATION \
            ADDITIONAL_FLAGS
        

  * To create a regional health check, use the [appropriate `compute health-checks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create) command:
        
        gcloud compute health-checks create PROTOCOL NAME \
            --region=REGION \
            --description=DESCRIPTION \
            --check-interval=CHECK_INTERVAL \
            --timeout=TIMEOUT \
            --healthy-threshold=HEALTHY_THRESHOLD \
            --unhealthy-threshold=UNHEALTHY_THRESHOLD \
            PORT_SPECIFICATION \
            ADDITIONAL_FLAGS
        




Replace the following:

  * `PROTOCOL` defines the protocol used for the health check. Valid options are `grpc`, `grpc-with-tls`, `http`, `https`, `http2`, `ssl`, and `tcp`.
  * `NAME` is the name of the health check. Within a given project: Each global health check must have a unique name, and regional health checks must have unique names within a given region.
  * `REGION`: The region of the health check. For regional load balancers, the health check region must match the region of the backend service.
  * `DESCRIPTION` is an optional description.
  * `CHECK_INTERVAL` is the amount of time from the start of one health check probe system's connection to the start of the next one. Units are seconds. If omitted, Google Cloud uses a value of `5s` (5 seconds).
  * `TIMEOUT` is the amount of time that Google Cloud waits for a response to a probe. The value of `TIMEOUT` must be less than or equal to the `CHECK_INTERVAL`. Units are seconds. If omitted, Google Cloud uses a value of `5s` (5 seconds).
  * `HEALTHY_THRESHOLD` and `UNHEALTHY_THRESHOLD` specify the number of sequential probes that must succeed or fail for the VM instance to be considered healthy or unhealthy. If either is omitted, Google Cloud uses a default threshold of `2`.
  * `PORT_SPECIFICATION`: Defines the port specification using one of the Port specification flags.
  * `ADDITIONAL_FLAGS` are other flags for specifying ports and options specific to the `PROTOCOL`. See Additional flags for HTTP, HTTPS, and HTTP/2 health checks, Additional flags for SSL and TCP health checks, or Additional flag for gRPC health checks.



###  Terraform 

To create a global health check, use the [`google_compute_health_check`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_health_check) resource. 
    
    
    resource "google_compute_health_check" "health_check_tcp_with_logging" {
      provider = google-beta
    
      name = "health-check-tcp"
    
      timeout_sec        = 1
      check_interval_sec = 1
    
      tcp_health_check {
        port = "22"
      }
    
      log_config {
        enable = true
      }
    }

To create a regional health check, use the [google_compute_region_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_health_check) resource. 
    
    
    resource "google_compute_region_health_check" "default" {
      name               = "tcp-health-check-region-west"
      timeout_sec        = 5
      check_interval_sec = 5
      tcp_health_check {
        port = "80"
      }
      region = "us-west1"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

  * To create a global health check, use [healthChecks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/insert)

  * To create a regional health check, use [regionHealthChecks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert)




## Modify health checks

You cannot convert a health check to a legacy health check (or the reverse) by modifying the health check. You also cannot change a health check's name or scope (for example, global to regional).

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click a health check to view its details.
  3. If you need to modify the health check, click **Edit** , then: 
     * Make changes to the parameters as necessary.
     * Click **Save**.



###  gcloud 

  1. Identify the name and scope of the health check. For instructions, see List health checks.

  2. Except for a health check's name, protocol, and scope, you can modify any of the common flags, the port specification flags, and other additional flags. To modify an existing health check, use the [appropriate `compute health-checks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/update). For flags that you omit, preconfigured settings are preserved.

     * Example modification of a global health check: The following command modifies a global HTTP health check named `hc-http-port-80` by changing its check interval, timeout, and request path:
           
           gcloud compute health-checks update http hc-http-port-80 \
               --global \
               --check-interval=20s \
               --timeout=15s \
               --request-path="/health"
           

     * Example modification of a regional health check: The following command modifies a regional TCP health check in `us-west1` named `hc-west1-tcp-ldap` by changing its port specification:
           
           gcloud compute health-checks update tcp hc-west1-tcp-ldap \
               --region=us-west1 \
               --port=631
           




###  API 

  1. Identify the name and scope of the health check. See Listing health checks for instructions.

  2. Except for a health check's name, protocol, and scope, you can modify any of the common flags, the port specification flags, and other additional flags with these API calls. Use `patch` API calls to preserve any preconfigured settings that are not explicitly set in the request.

     * To modify a global health check, use either [healthChecks.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/update) or [healthChecks.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/patch).

     * To modify a regional health check, use either [regionHealthChecks.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/update) or [regionHealthChecks.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/patch).




## List health checks

###  Console 

**Note:** The Google Cloud console lists **both** health checks and legacy health checks on its health checks page.

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click a health check to view its details.



###  gcloud 

To list health checks, use the [`compute health-checks list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/list) command:

  * To list global health checks:
        
        gcloud compute health-checks list \
            --global
        

  * To list regional health checks: Replace `REGION_LIST` with a comma-delimited list of Google Cloud regions to query.
        
        gcloud compute health-checks list \
            --regions=REGION_LIST
        




After you know the name and scope of a health check, use the [`compute health-checks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/describe) command to view its current configuration.

  * To describe a global health check, replace `NAME` with its name.
        
        gcloud compute health-checks describe NAME \
            --global
        

  * To describe a regional health check, replace `NAME` with its name and `REGION` with its region.
        
        gcloud compute health-checks describe NAME \
            --region=REGION
        




###  API 

To list health checks, use these API calls:

  * To list global health checks: [healthChecks.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/list)

  * To list regional health checks: [regionHealthChecks.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/list)




To describe a health check's current configuration, use:

  * To describe a global health check: [healthChecks.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/get)

  * To describe a regional health check: [regionHealthChecks.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/get)




## Additional flags

This section describes additional flags you can use when creating or modifying a health check. Some flags, such as port specification, must be set by using `gcloud` or the API.

### Port specification flags

If you create a health check by using the Google Cloud CLI or the API, you have two options to specify the health check's port. The following table shows port specification options for valid load balancer and backend combinations. The term _instance group_ refers to unmanaged instance groups, zonal managed instance groups, or regional managed instance groups.

Each health check can only use one type of port specification.

Product | Backend type | Port specification options  
---|---|---  
[Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network) | Instance groups and [supported NEGs](https://docs.cloud.google.com/load-balancing/docs/negs) | `--port`: Specify a TCP port by number, from `1` to `65535` The `--use-serving-port` flag is ignored for a health check associated with an internal passthrough Network Load Balancer because backend services for this load balancer don't subscribe to any [named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports). This is because they are passthrough load balancers that deliver packets directly to backends instead of creating new connections from the load balancer to the backend.  
Target pools | Legacy health checks which support the port number (`--port`) specification.  
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | Instance groups and [supported NEGs](https://docs.cloud.google.com/load-balancing/docs/negs) | `--port`: Specify a TCP port by number, from `1` to `65535` The `--use-serving-port` flag is ignored for a health check associated with an internal passthrough Network Load Balancer because backend services for this load balancer don't subscribe to any [named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports). This is because they are passthrough load balancers that deliver packets directly to backends instead of creating new connections from the load balancer to the backend.  
[Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
  
[Classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
  
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
  
[Global external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)  
  
[Classic proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)  
  
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)  
  
[Cross-region internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)  
  
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)  
  
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) | [Supported NEGs](https://docs.cloud.google.com/load-balancing/docs/negs) | 

  * `--port`: Specify a TCP port by number, from `1` to `65535`
  * `--use-serving-port`: Use the port of each endpoint in the network endpoint group.

  
Instance groups | 

  * `--port`: Specify a TCP port by number, from `1` to `65535`
  * `--use-serving-port`: Use the same instance group named port to which the backend service subscribes.

  
  
If you omit the port specification while creating the health check, Google Cloud uses the following defaults:

  * If the health check's protocol is `tcp` or `http`, it uses `--port=80`.
  * If the health check's protocol is `ssl`, `https`, or `http2`, it uses `--port=443`.
  * If the health check's protocol is `grpc` or `grpc_with_tls`, there is no implied default; you must include the port specification.



### Additional flags for HTTP, HTTPS, and HTTP/2 health checks

In addition to the common flags and port specification, you can use the following optional flags for HTTP, HTTPS, and HTTP/2 health checks. This example creates an HTTP health check named `hc-http-port-80` using port 80 with default interval, timeout, and health threshold criteria.
    
    
    gcloud compute health-checks create HTTP_PROTOCOL hc-http-port-80 \
        COMMON_FLAGS \
        PORT_SPECIFICATION \
        --host=HOST \
        --proxy-header=PROXY_HEADER \
        --request-path=REQUEST_PATH \
        --response=RESPONSE
    

  * `HTTP_PROTOCOL`: Can be `http` (HTTP/1.1 without TLS), `https` (HTTP/1.1 with TLS), or `http2` (HTTP/2 with TLS).
  * `COMMON_FLAGS`: Defines the common flags. See Creation procedure.
  * `PORT_SPECIFICATION`: Defines the port specification using one of the Port specification flags.
  * `HOST` lets you provide a `Host` HTTP header. If omitted, the IP address of the load balancer's forwarding rule is used.
  * `PROXY_HEADER` must be one of `NONE` or `PROXY_V1`. If omitted, Google Cloud uses `NONE`. The value of `PROXY_V1` adds the header `PROXY UNKNOWN\r\n`.
  * `REQUEST_PATH` specifies the URL path that Google Cloud uses when sending health check requests. If omitted, the health check request is sent to `/`.
  * `RESPONSE` defines an optional expected response. Response strings must follow these rules: 
    * The response string must consist of ASCII letters, numbers, and spaces.
    * The response string can be up to 1,024 characters long.
    * Wildcard matching is **not** supported.
    * Content-based checking does not support inversion; for example, operators such as `!` in HAProxy are not supported.



If Google Cloud finds the expected response string _anywhere_ in the first 1,024 bytes of the received response body, and if the HTTP status is 200 (OK), the probe is considered successful.

The `--request-path` and `--response` flags modify [the success criteria for the health check probe](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http).

### Additional flags for SSL and TCP health checks

In addition to the common flags and port specification, you can use the following optional flags for SSL and TCP health checks. This example creates a TCP health check named `hc-tcp-3268` using port 3268 with default interval, timeout, and health threshold criteria.
    
    
    gcloud compute health-checks create tcp hc-tcp-3268 \
        COMMON_FLAGS \
        PORT_SPECIFICATION \
        --proxy-header=PROXY_HEADER \
        --request=REQUEST_STRING \
        --response=RESPONSE_STRING
    

  * The protocol can be `tcp` (in this example) or `ssl`.
  * `COMMON_FLAGS`: Defines the common flags. See Creation procedure.
  * `PORT_SPECIFICATION`: Defines the port specification using one of the Port specification flags.
  * `PROXY_HEADER` must be one of `NONE` or `PROXY_V1`. If omitted, Google Cloud uses `NONE`. The value of `PROXY_V1` adds the header `PROXY UNKNOWN\r\n`.
  * `REQUEST_STRING`: You can provide a string, up to 1,024 ASCII characters long, to send once the TCP or SSL session has been established.
  * `RESPONSE_STRING`: You can provide a string, up to 1,024 ASCII characters long, for the expected response.



The `--request` and `--response` flags modify [the success criteria for the health check probe](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp). If you use the `--response` flag, either by itself or in conjunction with the `--request` flag, the response returned must exactly match the expected response string.

### Additional flag for gRPC health checks

Your backend gRPC server must implement the gRPC health service as described in [the gRPC health checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). Google Cloud sends a `HealthCheckRequest` message to your backends by calling the `Check` method of the health service on your backend. The service parameter in the request is set to an empty string unless a gRPC service name is specified.

A gRPC health check can check the status of a gRPC service. You can include a string, up to 1,024 ASCII characters long, that is the name of a particular gRPC service running on a backend VM or NEG. To do this, use the following optional flag for gRPC health checks:
    
    
    --grpc-service-name=GRPC_SERVICE_NAME
    

For example, you might have the following services and status that the backend server registers with your backend's gRPC Health service.

  * `MyPackage.ServiceA` with the serving status `SERVING`
  * `MyPackage.ServiceB` with the serving status `NOT_SERVING`
  * Empty service name with the serving status `NOT_SERVING`



If you create a health check against `MyPackage.ServiceA`, as follows, the health check probe returns `HEALTHY`, because the service's status is `SERVING`.
    
    
    gcloud compute health-checks create grpc MyGrpcHealthCheckServiceA \
        --grpc-service-name=MyPackage.ServiceA
    

If you create a health check against `MyPackage.ServiceB`, the health check probe returns `UNHEALTHY` because the service's status is `NOT_SERVING`.

If you create a health check against `MyPackage.ServiceC`, which is not registered with the gRPC Health service, the health check probe returns the gRPC status `NOT_FOUND`, which is the equivalent of `UNHEALTHY`.

If you create a health check against the empty service name, the health check probe returns the status `UNHEALTHY`, because the empty service name is registered with the status `NOT_SERVING`.

## Legacy health checks

This section describes how to create, modify, and list legacy HTTP and HTTPS health checks. You cannot convert a legacy health check to a health check, and you cannot convert a health check to a legacy health check.

To learn which types of load balancers support legacy health checks, see the [Load balancer guide](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide).

### Create legacy health checks

###  Console 

Although the Google Cloud console's health checks page lists and lets you edit both health checks and legacy health checks, you cannot _create_ a new legacy health check from the Google Cloud console's health checks page.

You can create a legacy health check in the Google Cloud console _only while_ [creating a target pool-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network). To create the legacy health check by itself, use this section's `gcloud` or API instructions.

###  gcloud 

To create a legacy health check, use the [`compute http-health-checks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/create) command:
    
    
    gcloud compute LEGACY_CHECK_TYPE create NAME \
        --description=DESCRIPTION \
        --check-interval=CHECK_INTERVAL \
        --timeout=TIMEOUT \
        --healthy-threshold=HEALTHY_THRESHOLD \
        --unhealthy-threshold=UNHEALTHY_THRESHOLD \
        --host=HOST \
        --port=PORT \
        --request-path=REQUEST_PATH
    

Replace the following:

  * `LEGACY_CHECK_TYPE` is `http-health-checks` for a legacy HTTP health check or `https-health-checks` for a legacy HTTPS health check. If you are creating the legacy health check for a target pool-based regional external passthrough Network Load Balancer, you must use `http-health-checks`.
  * `NAME` is the name of the legacy health check. Within a given project, each legacy health check must have a unique name.
  * `DESCRIPTION` is an optional description.
  * `CHECK_INTERVAL` is the amount of time from the start of one probe to the start of the next one. Units are seconds. If omitted, Google Cloud uses a value of `5s` (5 seconds).
  * `TIMEOUT` is the amount of time that Google Cloud will wait for a response to a probe. The value of `TIMEOUT` must be less than or equal to the `CHECK_INTERVAL`. Units are seconds. If omitted, Google Cloud uses a value of `5s` (5 seconds).
  * `HEALTHY_THRESHOLD` and `UNHEALTHY_THRESHOLD` specify the number of sequential probes that must succeed or fail for a VM instance to be considered healthy or unhealthy. If either is omitted, Google Cloud uses a default threshold of `2`.
  * `HOST` lets you provide a host HTTP header. If omitted, the IP address of the load balancer's forwarding rule is used.
  * `PORT` lets you provide a port number. If omitted, Google Cloud uses `80`.
  * `REQUEST_PATH` specifies the URL path that Google Cloud uses when sending health check requests. If omitted, the health check request is sent to `/`.



###  API 

  * To create a legacy HTTP health check, use the [httpHealthChecks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/insert) API call.

  * To create a legacy HTTPS health check, use the [httpsHealthChecks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks/insert)




###  Terraform 

  * To create a legacy HTTP health check resource, use the [`google_compute_http_health_check`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_http_health_check) resource.

  * To create a legacy HTTPS health check resource, use the [`google_compute_https_health_check`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_https_health_check) resource.




### Modify legacy health checks

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click a health check to view its details.
  3. Click **Edit** edit , make changes, and then click **Save**.



###  gcloud 

  * To modify a legacy HTTP health check, use the [`compute http-health-checks update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/update) command, replacing `NAME` with its name. When modifying a legacy health check with `gcloud`, preconfigured settings for flags you omit are preserved. The `OTHER_OPTIONS` are the options described in creating a legacy health check.
        
        gcloud compute http-health-checks update NAME \
          OTHER_OPTIONS
        

  * To modify a legacy HTTPS health check, use the [`compute https-health-checks update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/update) command, replacing `NAME` with its name. When modifying a legacy health check with `gcloud`, preconfigured settings for flags you omit are preserved. The `OTHER_OPTIONS` are the options described in creating a legacy health check.
        
        gcloud compute https-health-checks update NAME \
          OTHER_OPTIONS
        




###  API 

Except for a legacy health check's name and type, you can modify any of the flags used for its creation. The `patch` API calls preserve any preconfigured settings that are not explicitly set in the patch request.

  * To modify a legacy HTTP health check, use either [httpHealthChecks.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/update) or [httpHealthChecks.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/patch).

  * To modify a legacy HTTPS health check, use either [httpsHealthChecks.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks/update) or [httpsHealthChecks.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks/patch).




### List legacy health checks

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click a legacy health check to view its details.



###  gcloud 

  1. To list legacy HTTP health checks, use the [`compute http-health-checks list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/list) command:
         
         gcloud compute http-health-checks list
         

To list legacy HTTPS health checks, use the [`compute https-health-checks list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/list) command:
         
         gcloud compute https-health-checks list
         

  2. To describe a legacy HTTP health check, use the [`compute http-health-checks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/describe) command, replacing `NAME` with its name.
         
         gcloud compute http-health-checks describe NAME
         

To describe a legacy HTTPS health check, use the [`compute https-health-checks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/describe) command, replacing `NAME` with its name.
         
         gcloud compute https-health-checks describe NAME
         




###  API 

  1. To list legacy health checks:

     * Use [httpHealthChecks.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/list) to list legacy HTTP health checks.

     * Use [httpsHealthChecks.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks/list) to list legacy HTTPS health checks.

  2. To describe a legacy health check:

     * Use [httpHealthChecks.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/get) to describe legacy HTTP health check.

     * Use [httpsHealthChecks.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks/get) to describe legacy HTTPS health check.




## Create required firewall rules

You need to create ingress firewall rules applicable to all VMs being load balanced to allow traffic from [health check prober IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). The following example creates a firewall rule that is applicable to VM instances identified by a specific target tag.

This example allows all TCP traffic from Google Cloud health check systems to your VM instances. (TCP traffic includes SSL, HTTP, HTTPS, and HTTP/2 traffic.) If you prefer, you can specify ports along with the TCP protocol; however, if you specify ports, your firewall rules might become specific to a particular health check. If you use `tcp:80` for the protocol and port, this allows TCP traffic on port 80, so Google Cloud could contact your VMs using HTTP on port 80, but it couldn't contact them using HTTPS on port 443.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.   
[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule**.
  3. On the _Create a firewall rule_ page, supply the following information: 
     * **Name** : Provide a name for the rule. For this example, use `fw-allow-health-checks`.
     * **Network** : Choose a VPC network.
     * **Priority** : Enter a number for the priority. Lower numbers have higher priorities. Be sure that the firewall rule has a higher priority than other rules that might deny ingress traffic.
     * **Direction of traffic** : Choose **ingress**.
     * **Action on match** : Choose **allow**.
     * **Targets** : Choose **Specified target tags** , and then enter tags in the **Target tags** field. For this example, use `allow-health-checks`.
     * **Source filter** : Choose **IP ranges**.
     * **Source IP ranges** : Enter the source IP range depending on your load balancer type, traffic type, and health check type. See [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).
     * **Allowed protocols and ports** : Use `tcp` and the port configured in your health check. TCP is the underlying protocol for all health check protocols.
     * Click **Create**.
  4. On each of your instances being load balanced, [add the network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#adding_new_tags_to_vm_instances) so that this new ingress firewall rule applies to them. This example uses `allow-health-checks` for the network tag.



###  gcloud 

  1. Use the following `gcloud` command to create a firewall rule named `fw-allow-health-checks` that lets incoming TCP connections, from Google Cloud health check systems, to instances in your VPC network with the `allow-health-checks` tag. Based on the load balancer type, a different set of [probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) is supported for IPv6 traffic to the backends.

Replace `NETWORK_NAME` with the name of your VPC network and replace `PORT` with the ports used by your load balancer.
         
         gcloud compute firewall-rules create fw-allow-health-checks \
             --network=NETWORK_NAME \
             --action=ALLOW \
             --direction=INGRESS \
             --source-ranges=SOURCE_IP_RANGE \
             --target-tags=allow-health-checks \
             --rules=tcp:PORT

The value for SOURCE_IP_RANGE depends on your load balancer type, traffic type, and health check type. See [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

  2. On each of your instances being load balanced, [add the network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#adding_new_tags_to_vm_instances) so that this new ingress firewall rule applies to them. This example uses `allow-health-checks` for the network tag.




Refer to the [`gcloud` firewall rules documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules) and the [API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls) for more details.

Related documentation:

  * For more information about specifying targets for firewall rules, see the [explanation of targets](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) in the _Firewall Rules overview_ and [Configuring network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).
  * For more information about all the firewall rules required by load balancers, see [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).



## Associate health checks with load balancers

If you haven't already done so, review the [Health checks overview: Select a health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#selecting_hc).

To associate a health check with a _new_ load balancer, refer to the setup guide for the respective load balancer. This section describes how to associate a health check with an existing load balancer's backend service.

This section assumes that you have already:

  * Created a load balancer.
  * Created a health check.
  * Created the required firewall rule.




###  Console 

To associate a health check with an existing load balancer:

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/net-services/loadbalancing)
  2. Click a load balancer to view its details.
  3. Click **Edit** edit , and then click **Backend configuration**.
  4. Choose a health check from the **Health check** menu.
  5. Click **Update**.



###  gcloud 

To associate a health check with an existing backend service, follow these steps.

  1. Identify the name and scope of the backend service. The passthrough Network Load Balancers andproxy Network Load Balancers have only one backend service per load balancer. The Application Load Balancers have one or more backend services associated with a single URL map.

     * To list backend services for internal passthrough Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --region=REGION \
               --filter="loadBalancingScheme=INTERNAL"
           

     * To list backend services for regional external passthrough Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --region=REGION \
               --filter="loadBalancingScheme=EXTERNAL"
           

     * To list backend services for global external proxy Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --global \
               --filter="loadBalancingScheme=EXTERNAL_MANAGED" \
               --filter="protocol=(SSL,TCP)"
           

     * To list backend services for classic proxy Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --global \
               --filter="loadBalancingScheme=EXTERNAL" \
               --filter="protocol=(SSL,TCP)"
           

     * To list backend services for cross-region internal proxy Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --global \
               --filter="loadBalancingScheme=INTERNAL_MANAGED" \
               --filter="protocol=(SSL,TCP)"
           

     * To list backend services for regional external proxy Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --region=REGION \
               --filter="loadBalancingScheme=EXTERNAL_MANAGED" \
               --filter="protocol=(SSL,TCP)"
           

     * To list backend services for regional internal proxy Network Load Balancers, run the following command.
           
           gcloud compute backend-services list \
               --region=REGION \
               --filter="loadBalancingScheme=INTERNAL_MANAGED" \
               --filter="protocol=(SSL,TCP)"
           

     * To identify backend services for global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, first identify a URL map, and then describe the map. URL maps and backend services for these load balancers are always global, regardless of the Network Service Tier. Replace `URL_MAP_NAME` with the name of the URL map. The backend services used by the load balancer are listed in the response.
           
           gcloud compute url-maps list \
               --global
           
           
           gcloud compute url-maps describe URL_MAP_NAME \
               --global
           

     * To identify backend services for either a regional external Application Load Balancer or a regional internal Application Load Balancer, first identify a URL map, and then describe the map. Both URL maps and backend services for these load balancers are regional. Replace `REGION_LIST` with a comma-delimited list of Google Cloud regions to query. Replace `URL_MAP_NAME` with the name of the URL map and `REGION` with its region. The backend services used by the load balancer are listed in the response.
           
           gcloud compute url-maps list \
               --regions=REGION_LIST
           
           
           gcloud compute url-maps describe URL_MAP_NAME \
               --region=REGION
           

  2. Identify a health check. See Listing health checks.

  3. Associate a health check with the backend service by using the [`compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command. Each backend service must reference a single health check. In the following commands, replace `BACKEND_SERVICE_NAME` with the name of the backend service, `HEALTH_CHECK_NAME` with the name of the health check, and, if necessary `REGION` with the Google Cloud region of the backend service, the health check, or both.

     * To change the health check for an internal passthrough Network Load Balancer: An internal passthrough Network Load Balancer's backend service is regional. It can reference a global or regional health check. The following example shows a regional health check reference. If you're using a global health check with your internal passthrough Network Load Balancer, use `--global-health-checks` instead of `--health-checks-region`.
           
           gcloud compute backend-services update BACKEND_SERVICE_NAME \
               --region=REGION \
               --health-checks=HEALTH_CHECK_NAME \
               --health-checks-region=REGION
           

     * To change the health check for a backend service-based regional external passthrough Network Load Balancer: A regional external passthrough Network Load Balancer's backend service is regional. It can reference a regional health check.
           
           gcloud compute backend-services update BACKEND_SERVICE_NAME \
               --region=REGION \
               --health-checks=HEALTH_CHECK_NAME \
               --health-checks-region=REGION
           

     * To change the health check for a global external proxy Network Load Balancer, classic proxy Network Load Balancer, global external Application Load Balancer, classic Application Load Balancer, or a cross-region internal Application Load Balancer: Both the backend service and health check are global for these load balancers. Application Load Balancers can reference more than one health check if it references more than one backend service.
           
           gcloud compute backend-services update BACKEND_SERVICE_NAME \
               --global \
               --health-checks HEALTH_CHECK_NAME \
               --global-health-checks
           

     * To change the health check for either a regional external Application Load Balancer, a regional external proxy Network Load Balancer, a regional internal Application Load Balancer, or a regional internal proxy Network Load Balancer: Both the backend service and health check are regional. Some load balancers might reference more than one health check if they can reference more than one backend service.
           
           gcloud compute backend-services update BACKEND_SERVICE_NAME \
               --region=REGION \
               --health-checks=HEALTH_CHECK_NAME \
               --health-checks-region=REGION
           




###  API 

  1. You can list backend services with the [backendServices.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/list) API call.

  2. View health checks.

  3. To associate a health check with a backend service, use one of these API calls:

     * [backendServices.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update)
     * [backendServices.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch)



## Associate legacy health checks with target pool-based regional external passthrough Network Load Balancers

To associate a legacy health check with a new regional external passthrough Network Load Balancer, refer to [Set up a regional external passthrough Network Load Balancer with a target pool](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network). This section describes how to associate a legacy health check with a target pool-based regional external passthrough Network Load Balancer.

This section assumes that you have already:

  * Created a target pool-based regional external passthrough Network Load Balancer.
  * Created a legacy health check.
  * Created the required firewall rule.




###  Console 

To associate a health check with an existing target pool-based regional external passthrough Network Load Balancer:

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/net-services/loadbalancing)
  2. Click a load balancer to view its details.
  3. Click **Edit** edit , and then click **Backend configuration**.
  4. Choose a legacy health check from the **Health check** menu. (Only eligible legacy health checks are shown.)
  5. Click **Update**.



###  gcloud 

To associate a health check with an existing target pool-based regional external passthrough Network Load Balancer:

  1. Identify the target pool(s). A regional external passthrough Network Load Balancer has at least one target pool, and might have a secondary backup pool.
         
         gcloud compute target-pools list
         

  2. Identify a legacy health check using the `HTTP` protocol. View legacy health checks if necessary.

  3. Associate the legacy health check with the target pool(s). In the following commands, replace `TARGET_POOL_NAME` with the name of the target pool, `REGION` with its region, and `LEGACY_CHECK_NAME` with the name of the legacy health check. The legacy health check must use the HTTP protocol.

     * To remove a legacy HTTP health check from a target pool:
           
           gcloud compute target-pools remove-health-checks TARGET_POOL_NAME \
               --region=REGION \
               --http-health-check LEGACY_CHECK_NAME
           

     * To add a legacy HTTP health check to a target pool:
           
           gcloud compute target-pools add-health-checks TARGET_POOL_NAME \
               --region=REGION \
               --http-health-check LEGACY_CHECK_NAME
           




###  API 

  1. You can list target pools with the [targetPools.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools/list) API call.

  2. View legacy health checks and identify a legacy HTTP health check.

  3. To associate a legacy HTTP health check with a target pool use the API call [targetPools.addHealthCheck](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools/addHealthCheck).




## Check health check status

After you associate a health check with a backend service or a target pool, you can get the instantaneous health check state for the load balancer's backends.

###  Console 

  1. Go to the load balancing summary page.  
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click the name of a load balancer.
  3. Under **Backend** , inspect the **Healthy** column. Health status is reported for each backend instance group or network endpoint group.



###  gcloud 

  * For all load balancers except target pool-based regional external passthrough Network Load Balancers, identify the name and scope (global or regional) of the backend service. For a complete list of load balancers and scopes, see [Backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service).

Use the [`compute backend-services get-health`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) command, replacing `NAME` with the name of the backend service, and `REGION` with its region, if required.

    * To get the instantaneous health state of a global backend service:
          
          gcloud compute backend-services get-health GLOBAL_BACKEND_SERVICE_NAME \
              --global
          

    * To get the instantaneous health state of a regional backend service:
          
          gcloud compute backend-services get-health REGIONAL_BACKEND_SERVICE_NAME \
              --region=REGION
          

  * For target pool-based regional external passthrough Network Load Balancers, identify the name and region of the load balancer's target pool, and then use the [`compute target-pools get-health`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/get-health) command, replacing `NAME` with the name of the target pool, and `REGION` with its region.
        
        gcloud compute target-pools get-health TARGET_POOL_NAME \
            --region=REGION
        




###  API 

  * For all load balancers except target pool-based regional external passthrough Network Load Balancers, identify the name and scope (global or regional) of the backend service. For a complete list of load balancers and scopes, see [Backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service).

    * To get the instantaneous health state of a global backend service, use [backendServices.getHealth](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/getHealth)

    * To get the instantaneous health state of a regional backend service, use [regionBackendServices.getHealth](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/getHealth)

  * For target pool-based regional external passthrough Network Load Balancers, use [targetPools.getHealth](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools/getHealth)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
