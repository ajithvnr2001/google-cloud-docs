---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/healthChecks/get/
title: Method: healthChecks.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:20.992048+00:00
---

# Method: healthChecks.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/healthChecks/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: healthChecks.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns the specified HealthCheck resource.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/healthChecks/{healthCheck}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`healthCheck` |  `string` Name of the HealthCheck resource to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a health check resource.

Google Compute Engine has two health check resources:

  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)
  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks)



These health check resources can be used for load balancing and for autohealing VMs in a managed instance group (MIG).

**Load balancing**

Health check requirements vary depending on the type of load balancer. For details about the type of health check supported for each load balancer and corresponding backend type, see [Health checks overview: Load balancer guide](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide).

**Autohealing in MIGs**

The health checks that you use for autohealing VMs in a MIG can be either regional or global. For more information, see [ Set up an application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

For more information, see [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "checkIntervalSec": integer,
      "timeoutSec": integer,
      "unhealthyThreshold": integer,
      "healthyThreshold": integer,
      "type": enum,
      "tcpHealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "request": string,
        "response": string,
        "proxyHeader": enum
      },
      "sslHealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "request": string,
        "response": string,
        "proxyHeader": enum
      },
      "httpHealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "host": string,
        "requestPath": string,
        "proxyHeader": enum,
        "response": string
      },
      "httpsHealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "host": string,
        "requestPath": string,
        "proxyHeader": enum,
        "response": string
      },
      "http2HealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "host": string,
        "requestPath": string,
        "proxyHeader": enum,
        "response": string
      },
      "grpcHealthCheck": {
        "port": integer,
        "portName": string,
        "portSpecification": enum,
        "grpcServiceName": string
      },
      "grpcTlsHealthCheck": {
        "port": integer,
        "portSpecification": enum,
        "grpcServiceName": string
      },
      "sourceRegions": [
        string
      ],
      "selfLink": string,
      "region": string,
      "logConfig": {
        "enable": boolean
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`checkIntervalSec` |  `integer` How often (in seconds) to send a health check. The default value is 5 seconds.  
`timeoutSec` |  `integer` How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for `timeoutSec` to have greater value than `checkIntervalSec`.  
`unhealthyThreshold` |  `integer` A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.  
`healthyThreshold` |  `integer` A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.  
`type` |  `enum` Specifies the type of the healthCheck, either `TCP`, `SSL`, `HTTP`, `HTTPS`, `HTTP2`, `GRPC` or `GRPC_WITH_TLS`. Exactly one of the protocol-specific health check fields must be specified, which must match `type` field.  
`tcpHealthCheck` |  `object`  
`tcpHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. The default value is `80`. Valid values are `1` through `65535`.  
`tcpHealthCheck.portName` |  `string` Not supported.  
`tcpHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`tcpHealthCheck.request` |  `string` Instructs the health check prober to send this exact ASCII string, up to 1024 bytes in length, after establishing the TCP connection.  
`tcpHealthCheck.response` |  `string` Creates a content-based TCP health check. In addition to establishing a TCP connection, you can configure the health check to pass only when the backend sends this exact response ASCII string, up to 1024 bytes in length. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp>  
`tcpHealthCheck.proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`sslHealthCheck` |  `object`  
`sslHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. The default value is `443`. Valid values are `1` through `65535`.  
`sslHealthCheck.portName` |  `string` Not supported.  
`sslHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`sslHealthCheck.request` |  `string` Instructs the health check prober to send this exact ASCII string, up to 1024 bytes in length, after establishing the TCP connection and SSL handshake.  
`sslHealthCheck.response` |  `string` Creates a content-based SSL health check. In addition to establishing a TCP connection and the TLS handshake, you can configure the health check to pass only when the backend sends this exact response ASCII string, up to 1024 bytes in length. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp>  
`sslHealthCheck.proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`httpHealthCheck` |  `object`  
`httpHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. The default value is `80`. Valid values are `1` through `65535`.  
`httpHealthCheck.portName` |  `string` Not supported.  
`httpHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Also supported in legacy HTTP health checks for target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for pass-through load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`httpHealthCheck.host` |  `string` The value of the host header in the HTTP health check request. If left empty (default value), the host header is set to the destination IP address to which health check packets are sent. The destination IP address depends on the type of load balancer. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest>  
`httpHealthCheck.requestPath` |  `string` The request path of the HTTP health check request. The default value is `/`. Must comply with [RFC3986](https://www.ietf.org/rfc/rfc3986.txt).  
`httpHealthCheck.proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`httpHealthCheck.response` |  `string` Creates a content-based HTTP health check. In addition to the required HTTP 200 (OK) status code, you can configure the health check to pass only when the backend sends this specific ASCII response string within the first 1024 bytes of the HTTP response body. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http>  
`httpsHealthCheck` |  `object`  
`httpsHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. The default value is `443`. Valid values are `1` through `65535`.  
`httpsHealthCheck.portName` |  `string` Not supported.  
`httpsHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`httpsHealthCheck.host` |  `string` The value of the host header in the HTTPS health check request. If left empty (default value), the host header is set to the destination IP address to which health check packets are sent. The destination IP address depends on the type of load balancer. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest>  
`httpsHealthCheck.requestPath` |  `string` The request path of the HTTPS health check request. The default value is `/`. Must comply with [RFC3986](https://www.ietf.org/rfc/rfc3986.txt).  
`httpsHealthCheck.proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`httpsHealthCheck.response` |  `string` Creates a content-based HTTPS health check. In addition to the required HTTP 200 (OK) status code, you can configure the health check to pass only when the backend sends this specific ASCII response string within the first 1024 bytes of the HTTP response body. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http>  
`http2HealthCheck` |  `object`  
`http2HealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. The default value is `443`. Valid values are `1` through `65535`.  
`http2HealthCheck.portName` |  `string` Not supported.  
`http2HealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`http2HealthCheck.host` |  `string` The value of the host header in the HTTP/2 health check request. If left empty (default value), the host header is set to the destination IP address to which health check packets are sent. The destination IP address depends on the type of load balancer. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest>  
`http2HealthCheck.requestPath` |  `string` The request path of the HTTP/2 health check request. The default value is `/`. Must comply with [RFC3986](https://www.ietf.org/rfc/rfc3986.txt).  
`http2HealthCheck.proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`http2HealthCheck.response` |  `string` Creates a content-based HTTP/2 health check. In addition to the required HTTP 200 (OK) status code, you can configure the health check to pass only when the backend sends this specific ASCII response string within the first 1024 bytes of the HTTP response body. For details, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http>  
`grpcHealthCheck` |  `object`  
`grpcHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. Valid values are `1` through `65535`.  
`grpcHealthCheck.portName` |  `string` Not supported.  
`grpcHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`grpcHealthCheck.grpcServiceName` |  `string` The gRPC service name for the health check. This field is optional. The value of grpcServiceName has the following meanings by convention:   
\- Empty serviceName means the overall status of all services at the backend.   
\- Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service.   
The grpcServiceName can only be ASCII.  
`grpcTlsHealthCheck` |  `object`  
`grpcTlsHealthCheck.port` |  `integer` The TCP port number to which the health check prober sends packets. Valid values are `1` through `65535`.  
`grpcTlsHealthCheck.portSpecification` |  `enum` Specifies how a port is selected for health checking. Can be one of the following values:   
`USE_FIXED_PORT`: Specifies a port number explicitly using the `port` field in the health check. Supported by backend services for passthrough load balancers and backend services for proxy load balancers. Not supported by target pools. The health check supports all backends supported by the backend service provided the backend can be health checked. For example, `GCE_VM_IP` network endpoint groups, `GCE_VM_IP_PORT` network endpoint groups, and instance group backends.   
`USE_NAMED_PORT`: Not supported.   
`USE_SERVING_PORT`: Provides an indirect method of specifying the health check port by referring to the backend service. Only supported by backend services for proxy load balancers. Not supported by target pools. Not supported by backend services for passthrough load balancers. Supports all backends that can be health checked; for example, `GCE_VM_IP_PORT` network endpoint groups and instance group backends.  
For `GCE_VM_IP_PORT` network endpoint group backends, the health check uses the port number specified for each endpoint in the network endpoint group. For instance group backends, the health check uses the port number determined by looking up the backend service's named port in the instance group's list of named ports.  
`grpcTlsHealthCheck.grpcServiceName` |  `string` The gRPC service name for the health check. This field is optional. The value of grpcServiceName has the following meanings by convention:   
\- Empty serviceName means the overall status of all services at the backend.   
\- Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service.   
The grpcServiceName can only be ASCII.  
`sourceRegions[]` |  `string` The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check: 

  * SSL, HTTP2, GRPC, and GRPC_WITH_TLS protocols are not supported.
  * The TCP `request` field is not supported.
  * The `proxyHeader` field for HTTP, HTTPS, and TCP is not supported.
  * The `checkIntervalSec` field must be at least 30.
  * The health check cannot be used with BackendService nor with managed instance group auto-healing.

  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`region` |  `string` Output only. Region where the health check resides. Not applicable to global health checks.  
`logConfig` |  `object` Configure logging on this health check.  
`logConfig.enable` |  `boolean` Indicates whether or not to export logs. This is false by default, which means no health check logging will be done.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.healthChecks.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
