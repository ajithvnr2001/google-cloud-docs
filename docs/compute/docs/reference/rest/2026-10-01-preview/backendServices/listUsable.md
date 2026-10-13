---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/backendServices/listUsable/
title: Method: backendServices.listUsable \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:04.182787+00:00
---

# Method: backendServices.listUsable  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/backendServices/listUsable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: backendServices.listUsable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * Try it!



API Version : 2026-10-01-preview

Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/backendServices/listUsable?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
  
### Request body

The request body must be empty.

### Response body

Contains a list of usable BackendService resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "selfLink": string,
          "backends": [
            {
              "description": string,
              "group": string,
              "balancingMode": enum,
              "maxUtilization": number,
              "maxRate": integer,
              "maxRatePerInstance": number,
              "maxRatePerEndpoint": number,
              "maxConnections": integer,
              "maxConnectionsPerInstance": integer,
              "maxConnectionsPerEndpoint": integer,
              "maxInFlightRequests": integer,
              "maxInFlightRequestsPerInstance": integer,
              "maxInFlightRequestsPerEndpoint": integer,
              "trafficDuration": enum,
              "capacityScaler": number,
              "failover": boolean,
              "preference": enum,
              "customMetrics": [
                {
                  "name": string,
                  "maxUtilization": number,
                  "dryRun": boolean
                }
              ],
              "orchestrationInfo": {
                "resourceUri": string
              }
            }
          ],
          "healthChecks": [
            string
          ],
          "timeoutSec": integer,
          "port": integer,
          "protocol": enum,
          "fingerprint": string,
          "portName": string,
          "enableCDN": boolean,
          "sessionAffinity": enum,
          "affinityCookieTtlSec": integer,
          "region": string,
          "failoverPolicy": {
            "disableConnectionDrainOnFailover": boolean,
            "dropTrafficIfUnhealthy": boolean,
            "failoverRatio": number
          },
          "loadBalancingScheme": enum,
          "connectionDraining": {
            "drainingTimeoutSec": integer
          },
          "iap": {
            "enabled": boolean,
            "oauth2ClientId": string,
            "oauth2ClientSecret": string,
            "oauth2ClientSecretSha256": string
          },
          "cdnPolicy": {
            "cacheKeyPolicy": {
              "includeProtocol": boolean,
              "includeHost": boolean,
              "includeQueryString": boolean,
              "queryStringWhitelist": [
                string
              ],
              "queryStringBlacklist": [
                string
              ],
              "includeHttpHeaders": [
                string
              ],
              "includeNamedCookies": [
                string
              ]
            },
            "signedUrlKeyNames": [
              string
            ],
            "signedUrlCacheMaxAgeSec": string,
            "requestCoalescing": boolean,
            "cacheMode": enum,
            "defaultTtl": integer,
            "maxTtl": integer,
            "clientTtl": integer,
            "negativeCaching": boolean,
            "negativeCachingPolicy": [
              {
                "code": integer,
                "ttl": integer
              }
            ],
            "bypassCacheOnRequestHeaders": [
              {
                "headerName": string
              }
            ],
            "serveWhileStale": integer
          },
          "customRequestHeaders": [
            string
          ],
          "customResponseHeaders": [
            string
          ],
          "securityPolicy": string,
          "edgeSecurityPolicy": string,
          "logConfig": {
            "enable": boolean,
            "sampleRate": number,
            "optionalMode": enum,
            "optionalFields": [
              string
            ],
            "loggingHttpRequestHeaders": [
              {
                "headerName": string
              }
            ],
            "loggingHttpResponseHeaders": [
              {
                "headerName": string
              }
            ]
          },
          "securitySettings": {
            "clientTlsPolicy": string,
            "subjectAltNames": [
              string
            ],
            "awsV4Authentication": {
              "accessKeyId": string,
              "accessKey": string,
              "accessKeyVersion": string,
              "originRegion": string
            }
          },
          "localityLbPolicy": enum,
          "consistentHash": {
            "httpCookie": {
              "name": string,
              "path": string,
              "ttl": {
                "seconds": string,
                "nanos": integer
              }
            },
            "httpHeaderName": string,
            "minimumRingSize": string
          },
          "circuitBreakers": {
            "maxRequestsPerConnection": integer,
            "maxConnections": integer,
            "maxPendingRequests": integer,
            "maxRequests": integer,
            "maxRetries": integer
          },
          "outlierDetection": {
            "consecutiveErrors": integer,
            "interval": {
              "seconds": string,
              "nanos": integer
            },
            "baseEjectionTime": {
              "seconds": string,
              "nanos": integer
            },
            "maxEjectionPercent": integer,
            "enforcingConsecutiveErrors": integer,
            "enforcingSuccessRate": integer,
            "successRateMinimumHosts": integer,
            "successRateRequestVolume": integer,
            "successRateStdevFactor": integer,
            "consecutiveGatewayFailure": integer,
            "enforcingConsecutiveGatewayFailure": integer
          },
          "network": string,
          "subsetting": {
            "policy": enum
          },
          "connectionTrackingPolicy": {
            "trackingMode": enum,
            "connectionPersistenceOnUnhealthyBackends": enum,
            "idleTimeoutSec": integer,
            "enableStrongAffinity": boolean
          },
          "maxStreamDuration": {
            "seconds": string,
            "nanos": integer
          },
          "compressionMode": enum,
          "serviceLbPolicy": string,
          "serviceBindings": [
            string
          ],
          "localityLbPolicies": [
            {
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "policy": {
                "name": enum
              },
              "customPolicy": {
                "name": string,
                "data": string
              }
              // End of mutually exclusive fields.
            }
          ],
          "externalManagedMigrationState": enum,
          "externalManagedMigrationTestingPercentage": number,
          "ipAddressSelectionPolicy": enum,
          "metadatas": {
            string: string,
            ...
          },
          "haPolicy": {
            "fastIPMove": enum,
            "leader": {
              "backendGroup": string,
              "networkEndpoint": {
                "instance": string
              }
            }
          },
          "usedBy": [
            {
              "reference": string
            }
          ],
          "networkPassThroughLbTrafficPolicy": {
            "zonalAffinity": {
              "spillover": enum,
              "spilloverRatio": number
            }
          },
          "strongSessionAffinityCookie": {
            "name": string,
            "path": string,
            "ttl": {
              "seconds": string,
              "nanos": integer
            }
          },
          "tlsSettings": {
            "sni": string,
            "subjectAltNames": [
              {
                "dnsName": string,
                "uniformResourceIdentifier": string
              }
            ],
            "authenticationConfig": string,
            "identity": string
          },
          "customMetrics": [
            {
              "name": string,
              "dryRun": boolean
            }
          ],
          "params": {
            "resourceManagerTags": {
              string: string,
              ...
            }
          },
          "orchestrationInfo": {
            "resourceUri": string
          }
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#usableBackendServiceList` for lists of usable backend services.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of BackendService resources.  
`items[].kind` |  `string` Output only. Type of resource. Always `compute#backendService` for backend services.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].backends[]` |  `object` The list of backends that serve this BackendService.  
`items[].backends[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].backends[].group` |  `string` The fully-qualified URL of an [instance group](https://cloud.google.com/compute/docs/instance-groups/) or [network endpoint group](https://cloud.google.com/load-balancing/docs/negs/) (NEG) resource. To determine what types of backends a load balancer supports, see the [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service#backends).You must use the **fully-qualified** URL (starting with `<https://www.googleapis.com/>`) to specify the instance group or NEG. Partial URLs are not supported.If haPolicy is specified, backends must refer to NEG resources of type GCE_VM_IP.  
`items[].backends[].balancingMode` |  `enum` Specifies how to determine whether the backend of a load balancer can handle additional traffic or is fully loaded. For usage guidelines, see [ Connection balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode).Backends must use compatible balancing modes. Backends of a backend service may use different balancing modes. For more information, see [ Supported balancing modes and target capacity settings](https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode-combos) and [ Restrictions and guidance for instance groups](https://cloud.google.com/load-balancing/docs/backend-service#restrictions_and_guidance).Note: Currently, if you use the API to configure incompatible balancing modes, the configuration might be accepted even though it has no impact and is ignored. Specifically, Backend.maxUtilization is ignored when Backend.balancingMode is RATE. In the future, this incompatible combination will be rejected.  
`items[].backends[].maxUtilization` |  `number` Optional parameter to define a target capacity for the `UTILIZATION` balancing mode. The valid range is `[0.0, 1.0]`.For usage guidelines, see [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).  
`items[].backends[].maxRate` |  `integer` Defines a maximum number of HTTP requests per second (RPS). For usage guidelines, see [Rate balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).Not available if the backend's `balancingMode` is `CONNECTION`.  
`items[].backends[].maxRatePerInstance` |  `number` Defines a maximum target for requests per second (RPS). For usage guidelines, see [Rate balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).Not available if the backend's `balancingMode` is `CONNECTION`.  
`items[].backends[].maxRatePerEndpoint` |  `number` Defines a maximum target for requests per second (RPS). For usage guidelines, see [Rate balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).Not available if the backend's `balancingMode` is `CONNECTION`.  
`items[].backends[].maxConnections` |  `integer` Defines a target maximum number of simultaneous connections. For usage guidelines, see [Connection balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode). Not available if the backend's `balancingMode` is `RATE`.  
`items[].backends[].maxConnectionsPerInstance` |  `integer` Defines a target maximum number of simultaneous connections. For usage guidelines, see [Connection balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).Not available if the backend's `balancingMode` is `RATE`.  
`items[].backends[].maxConnectionsPerEndpoint` |  `integer` Defines a target maximum number of simultaneous connections. For usage guidelines, see [Connection balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode) and [Utilization balancing mode](https://cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode).Not available if the backend's `balancingMode` is `RATE`.  
`items[].backends[].maxInFlightRequests` |  `integer` Defines a maximum number of in-flight requests for the whole NEG or instance group. Not available if backend's `balancingMode` is `RATE` or `CONNECTION`.  
`items[].backends[].maxInFlightRequestsPerInstance` |  `integer` Defines a maximum number of in-flight requests for a single VM. Not available if backend's `balancingMode` is `RATE` or `CONNECTION`.  
`items[].backends[].maxInFlightRequestsPerEndpoint` |  `integer` Defines a maximum number of in-flight requests for a single endpoint. Not available if backend's `balancingMode` is `RATE` or `CONNECTION`.  
`items[].backends[].trafficDuration` |  `enum`  
`items[].backends[].capacityScaler` |  `number` A multiplier applied to the backend's target capacity of its balancing mode. The default value is `1`, which means the group serves up to 100% of its configured capacity (depending on `balancingMode`). A setting of `0` means the group is completely drained, offering 0% of its available capacity. The valid ranges are `0.0` and [0.1,1.0]. You cannot configure a setting larger than `0` and smaller than `0.1`. You cannot configure a setting of `0` when there is only one backend attached to the backend service.Not available with backends that don't support using a `balancingMode`. This includes backends such as global internet NEGs, regional serverless NEGs, and PSC NEGs.  
`items[].backends[].failover` |  `boolean` This field designates whether this is a failover backend. More than one failover backend can be configured for a given BackendService.This field can only be used for a regional external Passthrough Network Load Balancer or a regional internal Passthrough Network Load Balancer.  
`items[].backends[].preference` |  `enum` This field indicates whether this backend should be fully utilized before sending traffic to backends with default preference. The possible values are: 

  * `PREFERRED`: Backends with this preference level will be filled up to their capacity limits first, based on RTT.
  * `DEFAULT`: If preferred backends don't have enough capacity, backends in this layer would be used and traffic would be assigned based on the load balancing algorithm you use. This is the default

For global external Passthrough Network Load Balancers, the following restrictions apply: 

  * At most one backend can be marked as `PREFERRED`.
  * `PREFERRED` and `DEFAULT` backends cannot reside in the same Cloud region.

  
`items[].backends[].customMetrics[]` |  `object` backendServices.list of custom metrics that are used for `CUSTOM_METRICS` BalancingMode.  
`items[].backends[].customMetrics[].name` |  `string` Name of a custom utilization signal. The name must be 1-64 characters long and match the regular expression `[a-z]([-_.a-z0-9]*[a-z0-9])?` which means that the first character must be a lowercase letter, and all following characters must be a dash, period, underscore, lowercase letter, or digit, except the last character, which cannot be a dash, period, or underscore. For usage guidelines, see Custom Metrics balancing mode. This field can only be used for a global or regional backend service with the loadBalancingScheme set to `EXTERNAL_MANAGED`, `INTERNAL_MANAGED` `INTERNAL_SELF_MANAGED`.  
`items[].backends[].customMetrics[].maxUtilization` |  `number` Optional parameter to define a target utilization for the Custom Metrics balancing mode. The valid range is `[0.0, 1.0]`.  
`items[].backends[].customMetrics[].dryRun` |  `boolean` If true, the metric data is collected and reported to Cloud Monitoring, but is not used for load balancing.  
`items[].backends[].orchestrationInfo` |  `object` Information about the resource or system that manages the backend.  
`items[].backends[].orchestrationInfo.resourceUri` |  `string` The URI of the resource or system that manages the backend.  
`items[].healthChecks[]` |  `string` The list of URLs to the healthChecks, httpHealthChecks (legacy), or httpsHealthChecks (legacy) resource for health checking this backend service. Not all backend services support legacy health checks. See [ Load balancer guide](https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide). Currently, at most one health check can be specified for each backend service. Backend services with instance group or zonal NEG backends must have a health check unless haPolicy is specified. Backend services with internet or serverless NEG backends must not have a health check.healthChecks[] cannot be specified with haPolicy.  
`items[].timeoutSec` |  `integer` The backend service timeout has a different meaning depending on the type of load balancer. For more information see, [ Backend service settings](https://cloud.google.com/load-balancing/docs/backend-service#timeout-setting). The default is 30 seconds. The full range of timeout values allowed goes from 1 through 2,147,483,647 seconds.This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. Instead, use `maxStreamDuration`.  
`items[].port  
**(deprecated)**` |  `integer` Deprecated in favor of `portName`. The TCP port to connect on the backend. The default value is `80`. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit `port`.  
`items[].protocol` |  `enum` The protocol this BackendService uses to communicate with backends.Possible values are HTTP, HTTPS, HTTP2, H2C, TCP, SSL, UDP, GRPC, or UNSPECIFIED, depending on the chosen load balancer or Traffic Director configuration. Refer to [ Load balancing features](https://cloud.google.com/load-balancing/docs/features#protocol-to-backends) for more information.Must be set to GRPC when the backend service is referenced by a URL map that is bound to target gRPC proxy.  
`items[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a BackendService. An up-to-date fingerprint must be provided in order to update the `BackendService`, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a BackendService.A base64-encoded string.  
`items[].portName` |  `string` A named port on a backend instance group representing the port for communication to the backend VMs in that group. The named port must be [defined on each backend instance group](https://cloud.google.com/load-balancing/docs/backend-service#named_ports). This parameter has no meaning if the backends are NEGs. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit `portName`.  
`items[].enableCDN` |  `boolean` If `true`, enables Cloud CDN for the backend service of a global external Application Load Balancer.  
`items[].sessionAffinity` |  `enum` Type of session affinity to use. The default is `NONE`.Only `NONE` and `HEADER_FIELD` are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.For more details, see: [Session Affinity](https://cloud.google.com/load-balancing/docs/backend-service#sessionAffinity).sessionAffinity cannot be specified with haPolicy.  
`items[].affinityCookieTtlSec` |  `integer` Lifetime of cookies in seconds. This setting is applicable to Application Load Balancers and Traffic Director and requires GENERATED_COOKIE or HTTP_COOKIE session affinity.If set to `0`, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value is two weeks (`1,209,600`).Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].region` |  `string` Output only. URL of the region where the regional backend service resides. This field is not applicable to global backend services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`items[].failoverPolicy` |  `object` Requires at least one backend instance group to be defined as a backup (failover) backend. For load balancers that have configurable failover: [Internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview).`failoverPolicy` cannot be specified with `haPolicy`. `failoverPolicy` cannot be used by global external Passthrough Network Load Balancers.  
`items[].failoverPolicy.disableConnectionDrainOnFailover` |  `boolean` This can be set to `true` if the `protocol` is `TCP`, `UDP`, or `UNSPECIFIED`.The default is `false`.  
`items[].failoverPolicy.dropTrafficIfUnhealthy` |  `boolean` If set to `true`, connections to the load balancer are dropped when all primary and all backup backend VMs are unhealthy.If set to `false`, connections are distributed among all primary VMs when all primary and all backup backend VMs are unhealthy. For load balancers that have configurable failover: [Internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview). The default is `false`.  
`items[].failoverPolicy.failoverRatio` |  `number` The value of the field must be in the range `[0, 1]`. If the value is 0, the load balancer performs a failover when the number of healthy primary VMs equals zero. For all other values, the load balancer performs a failover when the total number of healthy primary VMs is less than this ratio. For load balancers that have configurable failover: [Internal TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview).  
`items[].loadBalancingScheme` |  `enum` Specifies the load balancer type. A backend service created for one type of load balancer cannot be used with another. For more information, refer to [ Backend services product and scheme table](https://cloud.google.com/load-balancing/docs/backend-service#supported-backends-scheme).  
`items[].connectionDraining` |  `object` connectionDraining cannot be specified with haPolicy.  
`items[].connectionDraining.drainingTimeoutSec` |  `integer` Configures a duration timeout for existing requests on a removed backend instance. For supported load balancers and protocols, as described in [Enabling connection draining](https://cloud.google.com/load-balancing/docs/enabling-connection-draining).  
`items[].iap` |  `object` The configurations for Identity-Aware Proxy on this resource. Not available for internal passthrough Network Load Balancers and external passthrough Network Load Balancers.  
`items[].iap.enabled` |  `boolean` Whether the serving infrastructure will authenticate and authorize all incoming requests.  
`items[].iap.oauth2ClientId` |  `string` OAuth2 client ID to use for the authentication flow.  
`items[].iap.oauth2ClientSecret` |  `string` OAuth2 client secret to use for the authentication flow. For security reasons, this value cannot be retrieved via the API. Instead, the SHA-256 hash of the value is returned in the oauth2ClientSecretSha256 field.@InputOnly  
`items[].iap.oauth2ClientSecretSha256` |  `string` Output only. SHA256 hash value for the field oauth2ClientSecret above.  
`items[].cdnPolicy` |  `object` Cloud CDN configuration for this BackendService. Only available for [ specified load balancer types](https://cloud.google.com/load-balancing/docs/features#special_features).  
`items[].cdnPolicy.cacheKeyPolicy` |  `object` The CacheKeyPolicy for this CdnPolicy.  
`items[].cdnPolicy.cacheKeyPolicy.includeProtocol` |  `boolean` If true, http and https requests will be cached separately.  
`items[].cdnPolicy.cacheKeyPolicy.includeHost` |  `boolean` If true, requests to different hosts will be cached separately.  
`items[].cdnPolicy.cacheKeyPolicy.includeQueryString` |  `boolean` If true, include query string parameters in the cache key according to queryStringWhitelist and queryStringBlacklist. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.  
`items[].cdnPolicy.cacheKeyPolicy.queryStringWhitelist[]` |  `string` Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify queryStringWhitelist or queryStringBlacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`items[].cdnPolicy.cacheKeyPolicy.queryStringBlacklist[]` |  `string` Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify queryStringWhitelist or queryStringBlacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`items[].cdnPolicy.cacheKeyPolicy.includeHttpHeaders[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`items[].cdnPolicy.cacheKeyPolicy.includeNamedCookies[]` |  `string` Allows HTTP cookies (by name) to be used in the cache key. The name=value pair will be used in the cache key Cloud CDN generates.  
`items[].cdnPolicy.signedUrlKeyNames[]` |  `string` Output only. Names of the keys for signing request URLs.  
`items[].cdnPolicy.signedUrlCacheMaxAgeSec` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. Defaults to 1hr (3600s). When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a `"Cache-Control: public, max-age=[TTL]"` header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.  
`items[].cdnPolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin.  
`items[].cdnPolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this backend. The possible values are:`USE_ORIGIN_HEADERS` Requires the origin to set valid caching headers to cache content. Responses without these headers will not be cached at Google's edge, and will require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server.`FORCE_CACHE_ALL` Cache all content, ignoring any "private", "no-store" or "no-cache" directives in Cache-Control response headers. Warning: this may result in Cloud CDN caching private, per-user (user identifiable) content.`CACHE_ALL_STATIC` Automatically cache static content, including common image formats, media (video and audio), and web assets (JavaScript and CSS). Requests and responses that are marked as uncacheable, as well as dynamic content (including HTML), will not be cached.If no value is provided for `cdnPolicy.cacheMode`, it defaults to `CACHE_ALL_STATIC`.  
`items[].cdnPolicy.defaultTtl` |  `integer` Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of defaultTTL cannot be set to a value greater than that of maxTTL, but can be equal. When the cacheMode is set to `FORCE_CACHE_ALL`, the defaultTTL will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`items[].cdnPolicy.maxTtl` |  `integer` Specifies the maximum allowed TTL for cached content served by this origin. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than maxTTL seconds in the future will be capped at the value of maxTTL, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`items[].cdnPolicy.clientTtl` |  `integer` Specifies a separate client (e.g. browser client) maximum TTL. This is used to clamp the max-age (or Expires) value sent to the client. With FORCE_CACHE_ALL, the lesser of clientTtl and defaultTtl is used for the response max-age directive, along with a "public" directive. For cacheable content in CACHE_ALL_STATIC mode, clientTtl clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the clientTtl and defaultTtl, and also ensures a "public" cache-control directive is present. If a client TTL is not specified, a default value (1 hour) will be used. The maximum allowed value is 31,622,400s (1 year).  
`items[].cdnPolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the cache mode is set to CACHE_ALL_STATIC or USE_ORIGIN_HEADERS, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the cache mode is set to FORCE_CACHE_ALL, negative caching applies to all responses with the specified response code, and override any caching headers. By default, Cloud CDN will apply the following default TTLs to these status codes: HTTP 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m HTTP 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s HTTP 405 (Method Not Found), 501 (Not Implemented): 60s. These defaults can be overridden in negativeCachingPolicy.  
`items[].cdnPolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. negativeCaching must be enabled to configure negativeCachingPolicy. Omitting the policy and leaving negativeCaching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negativeCachingPolicy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`items[].cdnPolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`items[].cdnPolicy.negativeCachingPolicy[].ttl` |  `integer` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`items[].cdnPolicy.bypassCacheOnRequestHeaders[]` |  `object` Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.  
`items[].cdnPolicy.bypassCacheOnRequestHeaders[].headerName` |  `string` The header field name to match on when bypassing cache. Values are case-insensitive.  
`items[].cdnPolicy.serveWhileStale` |  `integer` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`items[].customRequestHeaders[]` |  `string` Headers that the load balancer adds to proxied requests. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers).  
`items[].customResponseHeaders[]` |  `string` Headers that the load balancer adds to proxied responses. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers).  
`items[].securityPolicy` |  `string` Output only. The resource URL for the security policy associated with this backend service.  
`items[].edgeSecurityPolicy` |  `string` Output only. The resource URL for the edge security policy associated with this backend service.  
`items[].logConfig` |  `object` This field denotes the logging options for the load balancer traffic served by this backend service. If logging is enabled, logs will be exported to Stackdriver.  
`items[].logConfig.enable` |  `boolean` Denotes whether to enable logging for the load balancer traffic served by this backend service. The default value is false.  
`items[].logConfig.sampleRate` |  `number` This field can only be specified if logging is enabled for this backend service. The value of the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported. The default value is 1.0.  
`items[].logConfig.optionalMode` |  `enum` This field can only be specified if logging is enabled for this backend service. Configures whether all, none or a subset of optional fields should be added to the reported logs. One of [INCLUDE_ALL_OPTIONAL, EXCLUDE_ALL_OPTIONAL, CUSTOM]. Default is EXCLUDE_ALL_OPTIONAL.  
`items[].logConfig.optionalFields[]` |  `string` This field can only be specified if logging is enabled for this backend service and "logConfig.optionalMode" was set to CUSTOM. Contains a list of optional fields you want to include in the logs. For example: serverInstance, serverGkeDetails.cluster, serverGkeDetails.pod.podNamespace  
`items[].logConfig.loggingHttpRequestHeaders[]` |  `object` The list of request headers that will be logged to Stackdriver.  
`items[].logConfig.loggingHttpRequestHeaders[].headerName` |  `string` The name of the header to be logged.  
`items[].logConfig.loggingHttpResponseHeaders[]` |  `object` The list of response headers that will be logged to Stackdriver.  
`items[].logConfig.loggingHttpResponseHeaders[].headerName` |  `string` The name of the header to be logged.  
`items[].securitySettings` |  `object` This field specifies the security settings that apply to this backend service. This field is applicable to a global backend service with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.  
`items[].securitySettings.clientTlsPolicy` |  `string` Optional. A URL referring to a networksecurity.ClientTlsPolicy resource that describes how clients should authenticate with this service's backends.  `clientTlsPolicy` only applies to a global `BackendService` with the `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  If left blank, communications are not encrypted.  
`items[].securitySettings.subjectAltNames[]` |  `string` Optional. A list of Subject Alternative Names (SANs) that the client verifies during a mutual TLS handshake with an server/endpoint for this `BackendService`. When the server presents its X.509 certificate to the client, the client inspects the certificate's `subjectAltName` field. If the field contains one of the specified values, the communication continues. Otherwise, it fails. This additional check enables the client to verify that the server is authorized to run the requested service.  Note that the contents of the server certificate's `subjectAltName` field are configured by the Public Key Infrastructure which provisions server identities.  Only applies to a global `BackendService` with `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`. Only applies when `BackendService` has an attached `clientTlsPolicy` with `clientCertificate` (mTLS mode).  
`items[].securitySettings.awsV4Authentication` |  `object` The configuration needed to generate a signature for access to private storage buckets that support AWS's Signature Version 4 for authentication. Allowed only for INTERNET_IP_PORT and INTERNET_FQDN_PORT NEG backends.  
`items[].securitySettings.awsV4Authentication.accessKeyId` |  `string` The identifier of an access key used for s3 bucket authentication.  
`items[].securitySettings.awsV4Authentication.accessKey` |  `string` The access key used for s3 bucket authentication. Required for updating or creating a backend that uses AWS v4 signature authentication, but will not be returned as part of the configuration when queried with a REST API GET request.@InputOnly  
`items[].securitySettings.awsV4Authentication.accessKeyVersion` |  `string` The optional version identifier for the access key. You can use this to keep track of different iterations of your access key.  
`items[].securitySettings.awsV4Authentication.originRegion` |  `string` The name of the cloud region of your origin. This is a free-form field with the name of the region your cloud uses to host your origin. For example, "us-east-1" for AWS or "us-ashburn-1" for OCI.  
`items[].localityLbPolicy` |  `enum` The load balancing algorithm used within the scope of the locality. The possible values are: 

  * `ROUND_ROBIN`: This is a simple policy in which each healthy backend is selected in round robin order. This is the default.
  * `LEAST_REQUEST`: An `O(1)` algorithm which selects two random healthy hosts and picks the host which has fewer active requests.
  * `RING_HASH`: The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests.
  * `RANDOM`: The load balancer selects a random healthy host.
  * `ORIGINAL_DESTINATION`: Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer.
  * `MAGLEV`: used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, see [Maglev: A Fast and Reliable Software Network Load Balancer](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/).
  * `WEIGHTED_ROUND_ROBIN`: Per-endpoint Weighted Round Robin Load Balancing using weights computed from Backend reported Custom Metrics. If set, the Backend Service responses are expected to contain non-standard HTTP response header field `Endpoint-Load-Metrics`. The reported metrics to use for computing the weights are specified via the `customMetrics` field.
  * `WEIGHTED_MAGLEV`: Per-endpoint weighted load balancing via health check reported weights. If set, the backend service must configure an HTTP-based Health Check, and health check replies are expected to contain the non-standard HTTP response header field `X-Load-Balancing-Endpoint-Weight` to specify the per-endpoint weights. If set, load balancing is weighted based on the per-endpoint weights reported in the last processed health check replies, as long as every instance either reported a valid weight or had UNAVAILABLE_WEIGHT. Otherwise, load balancing remains equal-weight.

This field is applicable to either: 

  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and loadBalancingScheme set to INTERNAL_MANAGED.
  * A global backend service with the loadBalancingScheme set to INTERNAL_SELF_MANAGED, INTERNAL_MANAGED, or EXTERNAL_MANAGED.

If `sessionAffinity` is not configured—that is, if session affinity remains at the default value of `NONE`—then the default value for `localityLbPolicy` is `ROUND_ROBIN`. If session affinity is set to a value other than `NONE`, then the default value for `localityLbPolicy` is `MAGLEV`.Only `ROUND_ROBIN` and `RING_HASH` are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.localityLbPolicy cannot be specified with haPolicy.  
`items[].consistentHash` |  `object` Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular destination host will be lost when one or more hosts are added/removed from the destination service. This field specifies parameters that control consistent hashing. This field is only applicable when `localityLbPolicy` is set to `MAGLEV` or `RING_HASH`.This field is applicable to either: 

  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and loadBalancingScheme set to INTERNAL_MANAGED.
  * A global backend service with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.

  
`items[].consistentHash.httpCookie` |  `object` Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated. This field is applicable if the `sessionAffinity` is set to `HTTP_COOKIE`.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].consistentHash.httpCookie.name` |  `string` Name of the cookie.  
`items[].consistentHash.httpCookie.path` |  `string` Path to set for the cookie.  
`items[].consistentHash.httpCookie.ttl` |  `object` Lifetime of the cookie.  
`items[].consistentHash.httpCookie.ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].consistentHash.httpCookie.ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].consistentHash.httpHeaderName` |  `string` The hash based on the value of the specified header field. This field is applicable if the `sessionAffinity` is set to `HEADER_FIELD`.  
`items[].consistentHash.minimumRingSize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The minimum number of virtual nodes to use for the hash ring. Defaults to 1024. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.  
`items[].circuitBreakers` |  `object`  
`items[].circuitBreakers.maxRequestsPerConnection` |  `integer` Maximum requests for a single connection to the backend service. This parameter is respected by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there is no limit. Setting this parameter to 1 will effectively disable keep alive.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].circuitBreakers.maxConnections` |  `integer` The maximum number of connections to the backend service. If not specified, there is no limit.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].circuitBreakers.maxPendingRequests` |  `integer` The maximum number of pending requests allowed to the backend service. If not specified, there is no limit.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].circuitBreakers.maxRequests` |  `integer` The maximum number of parallel requests that allowed to the backend service. If not specified, there is no limit.  
`items[].circuitBreakers.maxRetries` |  `integer` The maximum number of parallel retries allowed to the backend cluster. If not specified, the default is 1.Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].outlierDetection` |  `object` Settings controlling the ejection of unhealthy backend endpoints from the load balancing pool of each individual proxy instance that processes the traffic for the given backend service. If not set, this feature is considered disabled.Results of the outlier detection algorithm (ejection of endpoints from the load balancing pool and returning them back to the pool) are executed independently by each proxy instance of the load balancer. In most cases, more than one proxy instance handles the traffic received by a backend service. Thus, it is possible that an unhealthy endpoint is detected and ejected by only some of the proxies, and while this happens, other proxies may continue to send requests to the same unhealthy endpoint until they detect and eject the unhealthy endpoint.Applicable backend endpoints can be: 

  * VM instances in an Instance Group
  * Endpoints in a Zonal NEG (GCE_VM_IP, GCE_VM_IP_PORT)
  * Endpoints in a Hybrid Connectivity NEG (NON_GCP_PRIVATE_IP_PORT)
  * Serverless NEGs, that resolve to Cloud Run, App Engine, or Cloud Functions Services
  * Private Service Connect NEGs, that resolve to Google-managed regional API endpoints or managed services published using Private Service Connect

Applicable backend service types can be: 

  * A global backend service with the loadBalancingScheme set to INTERNAL_SELF_MANAGED or EXTERNAL_MANAGED.
  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and loadBalancingScheme set to INTERNAL_MANAGED or EXTERNAL_MANAGED. Not supported for Serverless NEGs.

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.  
`items[].outlierDetection.consecutiveErrors` |  `integer` Number of consecutive errors before a backend endpoint is ejected from the load balancing pool. When the backend endpoint is accessed over HTTP, a 5xx return code qualifies as an error. Defaults to 5.  
`items[].outlierDetection.interval` |  `object` Time interval between ejection analysis sweeps. This can result in both new ejections and backend endpoints being returned to service. The interval is equal to the number of seconds as defined in outlierDetection.interval.seconds plus the number of nanoseconds as defined in outlierDetection.interval.nanos. Defaults to 1 second.  
`items[].outlierDetection.interval.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].outlierDetection.interval.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].outlierDetection.baseEjectionTime` |  `object` The base time that a backend endpoint is ejected for. Defaults to 30000ms or 30s.After a backend endpoint is returned back to the load balancing pool, it can be ejected again in another ejection analysis. Thus, the total ejection time is equal to the base ejection time multiplied by the number of times the backend endpoint has been ejected. Defaults to 30000ms or 30s.  
`items[].outlierDetection.baseEjectionTime.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].outlierDetection.baseEjectionTime.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].outlierDetection.maxEjectionPercent` |  `integer` Maximum percentage of backend endpoints in the load balancing pool for the backend service that can be ejected if the ejection conditions are met. Defaults to 50%.  
`items[].outlierDetection.enforcingConsecutiveErrors` |  `integer` The percentage chance that a backend endpoint will be ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0.  
`items[].outlierDetection.enforcingSuccessRate` |  `integer` The percentage chance that a backend endpoint will be ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.Not supported when the backend service uses Serverless NEG.  
`items[].outlierDetection.successRateMinimumHosts` |  `integer` The number of backend endpoints in the load balancing pool that must have enough request volume to detect success rate outliers. If the number of backend endpoints is fewer than this setting, outlier detection via success rate statistics is not performed for any backend endpoint in the load balancing pool. Defaults to 5.Not supported when the backend service uses Serverless NEG.  
`items[].outlierDetection.successRateRequestVolume` |  `integer` The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this backend endpoint in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that backend endpoint. Defaults to 100.Not supported when the backend service uses Serverless NEG.  
`items[].outlierDetection.successRateStdevFactor` |  `integer` This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev * successRateStdevFactor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900.Not supported when the backend service uses Serverless NEG.  
`items[].outlierDetection.consecutiveGatewayFailure` |  `integer` The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 3.  
`items[].outlierDetection.enforcingConsecutiveGatewayFailure` |  `integer` The percentage chance that a backend endpoint will be ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  
`items[].network` |  `string` The URL of the network to which this backend service belongs.This field must be set for Internal Passthrough Network Load Balancers when the haPolicy is enabled, and for External Passthrough Network Load Balancers when the haPolicy fastIpMove is enabled.This field can only be specified when the load balancing scheme is set to `INTERNAL`, or when the load balancing scheme is set to `EXTERNAL` and haPolicy fastIpMove is enabled.  
`items[].subsetting` |  `object` subsetting cannot be specified with haPolicy.  
`items[].subsetting.policy` |  `enum`  
`items[].connectionTrackingPolicy` |  `object` Connection Tracking configuration for this BackendService. Connection tracking policy settings are only available for external passthrough Network Load Balancers and internal passthrough Network Load Balancers.connectionTrackingPolicy cannot be specified with haPolicy.  
`items[].connectionTrackingPolicy.trackingMode` |  `enum` Specifies the key used for connection tracking. There are two options: 

  * `PER_CONNECTION`: This is the default mode. The Connection Tracking is performed as per the Connection Key (default Hash Method) for the specific protocol.
  * `PER_SESSION`: The Connection Tracking is performed as per the configured Session Affinity. It matches the configured Session Affinity. 

For more details, see [Tracking Mode for Network Load Balancing](https://cloud.google.com/load-balancing/docs/network/networklb-backend-service#tracking-mode) and [Tracking Mode for Internal TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/internal#tracking-mode).  
`items[].connectionTrackingPolicy.connectionPersistenceOnUnhealthyBackends` |  `enum` Specifies connection persistence when backends are unhealthy. The default value is `DEFAULT_FOR_PROTOCOL`.If set to `DEFAULT_FOR_PROTOCOL`, the existing connections persist on unhealthy backends only for connection-oriented protocols (`TCP` and `SCTP`) and only if the Tracking Mode is `PER_CONNECTION` (default tracking mode) or the Session Affinity is configured for 5-tuple. They do not persist for `UDP`.If set to `NEVER_PERSIST`, after a backend becomes unhealthy, the existing connections on the unhealthy backend are never persisted on the unhealthy backend. They are always diverted to newly selected healthy backends (unless all backends are unhealthy).If set to `ALWAYS_PERSIST`, existing connections always persist on unhealthy backends regardless of protocol and session affinity. It is generally not recommended to use this mode overriding the default.For more details, see [Connection Persistence for Network Load Balancing](https://cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-persistence) and [Connection Persistence for Internal TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/internal#connection-persistence).  
`items[].connectionTrackingPolicy.idleTimeoutSec` |  `integer` Specifies how long to keep a Connection Tracking entry while there is no matching traffic (in seconds).For internal passthrough Network Load Balancers: 

  * The minimum (default) is 10 minutes and the maximum is 16 hours.
  * It can be set only if Connection Tracking is less than 5-tuple (i.e. Session Affinity is `CLIENT_IP_NO_DESTINATION`, `CLIENT_IP` or `CLIENT_IP_PROTO`, and Tracking Mode is `PER_SESSION`).

For external passthrough Network Load Balancers the default is 60 seconds. This option is not available publicly.  
`items[].connectionTrackingPolicy.enableStrongAffinity` |  `boolean` Enable Strong Session Affinity for external passthrough Network Load Balancers. This option is not available publicly.  
`items[].maxStreamDuration` |  `object` Specifies the default maximum duration (timeout) for streams to this service. Duration is computed from the beginning of the stream until the response has been completely processed, including all retries. A stream that does not complete in this duration is closed. If not specified, there will be no timeout limit, i.e. the maximum duration is infinite. This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service. This field is only allowed when the `loadBalancingScheme` of the backend service is `INTERNAL_SELF_MANAGED`.  
`items[].maxStreamDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].maxStreamDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].compressionMode` |  `enum` Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header.  
`items[].serviceLbPolicy` |  `string` URL to `networkservices.ServiceLbPolicy` resource.Can only be set if load balancing scheme is EXTERNAL_MANAGED, INTERNAL_MANAGED or INTERNAL_SELF_MANAGED for a global backend service, and EXTERNAL_MANAGED or INTERNAL_MANAGED for a regional backend service. For a global backend service, the service lb policy must be global. For a regional backend service, the service lb policy must be regional and in the same region.  
`items[].serviceBindings[]` |  `string` URLs of `networkservices.ServiceBinding` resources.Can only be set if load balancing scheme is INTERNAL_SELF_MANAGED. If set, lists of backends and health checks must be both empty.  
`items[].localityLbPolicies[]` |  `object` A list of locality load-balancing policies to be used in order of preference. When you use localityLbPolicies, you must set at least one value for either the localityLbPolicies[].policy or the localityLbPolicies[].customPolicy field. localityLbPolicies overrides any value set in the localityLbPolicy field.For an example of how to use this field, see [Define a list of preferred policies](https://cloud.google.com/traffic-director/docs/proxyless-configure-advanced-traffic-management#policy-list).Caution: This field and its children are intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration.  
`items[].localityLbPolicies[].policy` |  `object`  
`items[].localityLbPolicies[].policy.name` |  `enum` The name of a locality load-balancing policy. Valid values include ROUND_ROBIN and, for Java clients, LEAST_REQUEST. For information about these values, see the description of localityLbPolicy.Do not specify the same policy more than once for a backend. If you do, the configuration is rejected.  
`items[].localityLbPolicies[].customPolicy` |  `object`  
`items[].localityLbPolicies[].customPolicy.name` |  `string` Identifies the custom policy.The value should match the name of a custom implementation registered on the gRPC clients. It should follow protocol buffer message naming conventions and include the full path (for example, myorg.CustomLbPolicy). The maximum length is 256 characters.Do not specify the same custom policy more than once for a backend. If you do, the configuration is rejected.For an example of how to use this field, see [Use a custom policy](https://cloud.google.com/traffic-director/docs/proxyless-configure-advanced-traffic-management#custom-lb-config).  
`items[].localityLbPolicies[].customPolicy.data` |  `string` An optional, arbitrary JSON object with configuration data, understood by a locally installed custom policy implementation.  
`items[].externalManagedMigrationState` |  `enum` Specifies the canary migration state. Possible values are PREPARE, TEST_BY_PERCENTAGE, and TEST_ALL_TRAFFIC.To begin the migration from EXTERNAL to EXTERNAL_MANAGED, the state must be changed to PREPARE. The state must be changed to TEST_ALL_TRAFFIC before the loadBalancingScheme can be changed to EXTERNAL_MANAGED. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate traffic by percentage using externalManagedMigrationTestingPercentage.Rolling back a migration requires the states to be set in reverse order. So changing the scheme from EXTERNAL_MANAGED to EXTERNAL requires the state to be set to TEST_ALL_TRAFFIC at the same time. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate some traffic back to EXTERNAL or PREPARE can be used to migrate all traffic back to EXTERNAL.  
`items[].externalManagedMigrationTestingPercentage` |  `number` Determines the fraction of requests that should be processed by the Global external Application Load Balancer.The value of this field must be in the range [0, 100].Session affinity options will slightly affect this routing behavior, for more details, see: [Session Affinity](https://cloud.google.com/load-balancing/docs/backend-service#sessionAffinity).This value can only be set if the loadBalancingScheme in the BackendService is set to EXTERNAL (when using the classic Application Load Balancer) and the migration state is TEST_BY_PERCENTAGE.  
`items[].ipAddressSelectionPolicy` |  `enum` Specifies a preference for traffic sent from the proxy to the backend (or from the client to the backend for proxyless gRPC). The possible values are: 

  * `IPV4_ONLY`: Only send IPv4 traffic to the backends of the backend service (Instance Group, Managed Instance Group, Network Endpoint Group), regardless of traffic from the client to the proxy. Only IPv4 health checks are used to check the health of the backends. This is the default setting.
  * `PREFER_IPV6`: Prioritize the connection to the endpoint's IPv6 address over its IPv4 address (provided there is a healthy IPv6 address).
  * `IPV6_ONLY`: Only send IPv6 traffic to the backends of the backend service (Instance Group, Managed Instance Group, Network Endpoint Group), regardless of traffic from the client to the proxy. Only IPv6 health checks are used to check the health of the backends.

This field is applicable to either: 

  * Advanced global external Application Load Balancer (load balancing scheme EXTERNAL_MANAGED),
  * Regional external Application Load Balancer,
  * Internal proxy Network Load Balancer (load balancing scheme INTERNAL_MANAGED),
  * Regional internal Application Load Balancer (load balancing scheme INTERNAL_MANAGED),
  * Traffic Director with Envoy proxies and proxyless gRPC (load balancing scheme INTERNAL_SELF_MANAGED).

  
`items[].metadatas` |  `map (key: string, value: string)` Deployment metadata associated with the resource to be set by a GKE hub controller and read by the backend RCTH  
`items[].haPolicy` |  `object` Configures self-managed High Availability (HA) for External and Internal Protocol Forwarding.The backends of this regional backend service must only specify zonal network endpoint groups (NEGs) of type GCE_VM_IP.When haPolicy is set for an Internal Passthrough Network Load Balancer, the regional backend service must set the network field. All zonal NEGs must belong to the same network. However, individual NEGs can belong to different subnetworks of that network.When haPolicy is specified, the set of attached network endpoints across all backends comprise an High Availability domain from which one endpoint is selected as the active endpoint (the leader) that receives all traffic.haPolicy can be added only at backend service creation time. Once set up, it cannot be deleted.Note that haPolicy is not for load balancing, and therefore cannot be specified with sessionAffinity, connectionTrackingPolicy, and failoverPolicy.haPolicy requires customers to be responsible for tracking backend endpoint health and electing a leader among the healthy endpoints. Therefore, haPolicy cannot be specified with healthChecks.`haPolicy` can only be specified for External Passthrough Network Load Balancers and Internal Passthrough Network Load Balancers. `haPolicy` cannot be used by global external Passthrough Network Load Balancers.  
`items[].haPolicy.fastIPMove` |  `enum` Specifies whether fast IP move is enabled, and if so, the mechanism to achieve it.Supported values are: 

  * DISABLED: Fast IP Move is disabled. You can only use the haPolicy.leader API to update the leader.
  * >GARP_RA: Provides a method to very quickly define a new network endpoint as the leader. This method is faster than updating the leader using the haPolicy.leader API. Fast IP move works as follows: The VM hosting the network endpoint that should become the new leader sends either a Gratuitous ARP (GARP) packet (IPv4) or an ICMPv6 Router Advertisement(RA) packet (IPv6). Google Cloud immediately but temporarily associates the forwarding rule IP address with that VM, and both new and in-flight packets are quickly delivered to that VM. 

Note the important properties of the Fast IP Move functionality: 

  * The GARP/RA-initiated re-routing stays active for approximately 20 minutes. After triggering fast failover, you must also appropriately set the haPolicy.leader.
  * The new leader instance should continue to send GARP/RA packets periodically every 10 seconds until at least 10 minutes after updating the haPolicy.leader (but stop immediately if it is no longer the leader). 
  * After triggering a fast failover, we recommend that you wait at least 3 seconds before sending another GARP/RA packet from a different VM instance to avoid race conditions.
  * Don't send GARP/RA packets from different VM instances at the same time. If multiple instances continue to send GARP/RA packets, traffic might be routed to different destinations in an alternating order. This condition ceases when a single instance issues a GARP/RA packet.
  * The GARP/RA request always takes priority over the leader API. Using the haPolicy.leader API to change the leader to a different instance will have no effect until the GARP/RA request becomes inactive.
  * The GARP/RA packets should follow the [GARP/RA Packet Specifications.](https://cloud.google.com/load-balancing/docs/garp-ra-packet-spec).
  * When multiple forwarding rules refer to a regional backend service, you need only send a GARP or RA packet for a single forwarding rule virtual IP. The virtual IPs for all forwarding rules targeting the same backend service will also be moved to the sender of the GARP or RA packet. 

The following are the Fast IP Move limitations (that is, when fastIPMove is not DISABLED): 

  * Multiple forwarding rules cannot use the same IP address if one of them refers to a regional backend service with fastIPMove.
  * The regional backend service must set the network field, and all NEGs must belong to that network. However, individual NEGs can belong to different subnetworks of that network. 
  * The maximum number of network endpoints across all backends of a backend service with fastIPMove is 32.
  * The maximum number of backend services with fastIPMove that can have the same network endpoint attached to one of its backends is 64.
  * The maximum number of backend services with fastIPMove in a VPC in a region is 64.
  * The network endpoints that are attached to a backend of a backend service with fastIPMove cannot resolve to Gen3+ machines for IPv6.
  * Traffic directed to the leader by a static route next hop will not be redirected to a new leader by fast failover. Such traffic will only be redirected once an haPolicy.leader update has taken effect. Only traffic to the forwarding rule's virtual IP will be redirected to a new leader by fast failover.

haPolicy.fastIPMove can be set only at backend service creation time. Once set, it cannot be updated.By default, fastIpMove is set to DISABLED.  
`items[].haPolicy.leader` |  `object` Selects one of the network endpoints attached to the backend NEGs of this service as the active endpoint (the leader) that receives all traffic.When the leader changes, there is no connection draining to persist existing connections on the old leader.You are responsible for selecting a suitable endpoint as the leader. For example, preferring a healthy endpoint over unhealthy ones. Note that this service does not track backend endpoint health, and selects the configured leader unconditionally.  
`items[].haPolicy.leader.backendGroup` |  `string` A fully-qualified URL (starting with <https://www.googleapis.com/>) of the zonal Network Endpoint Group (NEG) with `GCE_VM_IP` endpoints that the leader is attached to.The leader's backendGroup must already be specified as a backend of this backend service. Removing a backend that is designated as the leader's backendGroup is not permitted.  
`items[].haPolicy.leader.networkEndpoint` |  `object` The network endpoint within the leader.backendGroup that is designated as the leader.This network endpoint cannot be detached from the NEG specified in the haPolicy.leader.backendGroup until the leader is updated with another network endpoint, or the leader is removed from the haPolicy.  
`items[].haPolicy.leader.networkEndpoint.instance` |  `string` The name of the VM instance of the leader network endpoint. The instance must already be attached to the NEG specified in the haPolicy.leader.backendGroup.The value must be a valid RFC1035 name (1-63 characters) or a valid instance URL. Authorization requires the following IAM permission on the specified resource instance: compute.instances.use  
`items[].usedBy[]` |  `object` Output only. backendServices.list of resources referencing given backend service.  
`items[].usedBy[].reference` |  `string` Output only. Server-defined URL for resources referencing given BackendService like UrlMaps, TargetTcpProxies, TargetSslProxies and ForwardingRule.  
`items[].networkPassThroughLbTrafficPolicy` |  `object` Configures traffic steering properties of internal passthrough Network Load Balancers.networkPassThroughLbTrafficPolicy cannot be specified with haPolicy.  
`items[].networkPassThroughLbTrafficPolicy.zonalAffinity` |  `object` When configured, new connections are load balanced across healthy backend endpoints in the local zone.  
`items[].networkPassThroughLbTrafficPolicy.zonalAffinity.spillover` |  `enum` This field indicates whether zonal affinity is enabled or not. The possible values are: 

  * `ZONAL_AFFINITY_DISABLED`: Default Value. Zonal Affinity is disabled. The load balancer distributes new connections to all healthy backend endpoints across all zones.
  * `ZONAL_AFFINITY_STAY_WITHIN_ZONE`: Zonal Affinity is enabled. The load balancer distributes new connections to all healthy backend endpoints in the local zone only. If there are no healthy backend endpoints in the local zone, the load balancer distributes new connections to all backend endpoints in the local zone.
  * `ZONAL_AFFINITY_SPILL_CROSS_ZONE`: Zonal Affinity is enabled. The load balancer distributes new connections to all healthy backend endpoints in the local zone only. If there aren't enough healthy backend endpoints in the local zone, the load balancer distributes new connections to all healthy backend endpoints across all zones.

  
`items[].networkPassThroughLbTrafficPolicy.zonalAffinity.spilloverRatio` |  `number` The value of the field must be in [0, 1]. When the ratio of the count of healthy backend endpoints in a zone to the count of backend endpoints in that same zone is equal to or above this threshold, the load balancer distributes new connections to all healthy endpoints in the local zone only. When the ratio of the count of healthy backend endpoints in a zone to the count of backend endpoints in that same zone is below this threshold, the load balancer distributes all new connections to all healthy endpoints across all zones.  
`items[].strongSessionAffinityCookie` |  `object` Describes the HTTP cookie used for stateful session affinity. This field is applicable and required if the `sessionAffinity` is set to `STRONG_COOKIE_AFFINITY`.  
`items[].strongSessionAffinityCookie.name` |  `string` Name of the cookie.  
`items[].strongSessionAffinityCookie.path` |  `string` Path to set for the cookie.  
`items[].strongSessionAffinityCookie.ttl` |  `object` Lifetime of the cookie.  
`items[].strongSessionAffinityCookie.ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].strongSessionAffinityCookie.ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].tlsSettings` |  `object` Configuration for Backend Authenticated TLS and mTLS. May only be specified when the backend protocol is SSL, HTTPS or HTTP2.  
`items[].tlsSettings.sni` |  `string` Server Name Indication - see RFC3546 section 3.1. If set, the load balancer sends this string as the SNI hostname in the TLS connection to the backend, and requires that this string match a Subject Alternative Name (SAN) in the backend's server certificate. With a Regional Internet NEG backend, if the SNI is specified here, the load balancer uses it regardless of whether the Regional Internet NEG is specified with FQDN or IP address and port. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[].  
`items[].tlsSettings.subjectAltNames[]` |  `object` A list of Subject Alternative Names (SANs) that the Load Balancer verifies during a TLS handshake with the backend. When the server presents its X.509 certificate to the Load Balancer, the Load Balancer inspects the certificate's SAN field, and requires that at least one SAN match one of the subjectAltNames in the list. This field is limited to 5 entries. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[].  
`items[].tlsSettings.subjectAltNames[].dnsName` |  `string` The SAN specified as a DNS Name.  
`items[].tlsSettings.subjectAltNames[].uniformResourceIdentifier` |  `string` The SAN specified as a URI.  
`items[].tlsSettings.authenticationConfig` |  `string` Reference to the BackendAuthenticationConfig resource from the networksecurity.googleapis.com namespace. Can be used in authenticating TLS connections to the backend, as specified by the authenticationMode field. Can only be specified if authenticationMode is not NONE.  
`items[].tlsSettings.identity` |  `string` Assigns the Managed Identity for the BackendService Workload.  Use this property to configure the load balancer back-end to use certificates and roots of trust provisioned by the Managed Workload Identity system.  The `identity` property is the fully-specified SPIFFE ID to use in the SVID presented by the Load Balancer Workload.  The SPIFFE ID must be a resource starting with the `trustDomain` property value, followed by the path to the Managed Workload Identity.  Supported SPIFFE ID format: 

  * `//<trust_domain>/ns/<namespace>/sa/<subject>`

The Trust Domain within the Managed Identity must refer to a valid Workload Identity Pool. The TrustConfig and CertificateIssuanceConfig will be inherited from the Workload Identity Pool.  Restrictions: 

  * If you set the `identity` property, you cannot manually set the following fields: 
    * `tlsSettings.sni`
    * `tlsSettings.subjectAltNames`
    * `tlsSettings.authenticationConfig`

When defining a `identity` for a RegionBackendServices, the corresponding Workload Identity Pool must have a `ca_pool` configured in the same region.  The system will set up a read-only `tlsSettings.authenticationConfig` for the Managed Identity.  
`items[].customMetrics[]` |  `object` backendServices.list of custom metrics that are used for the `WEIGHTED_ROUND_ROBIN` localityLbPolicy.  
`items[].customMetrics[].name` |  `string` Name of a custom utilization signal. The name must be 1-64 characters long and match the regular expression `[a-z]([-_.a-z0-9]*[a-z0-9])?` which means that the first character must be a lowercase letter, and all following characters must be a dash, period, underscore, lowercase letter, or digit, except the last character, which cannot be a dash, period, or underscore. For usage guidelines, see Custom Metrics balancing mode. This field can only be used for a global or regional backend service with the loadBalancingScheme set to `EXTERNAL_MANAGED`, `INTERNAL_MANAGED` `INTERNAL_SELF_MANAGED`.  
`items[].customMetrics[].dryRun` |  `boolean` If true, the metric data is not used for load balancing.  
`items[].params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid.  
`items[].orchestrationInfo` |  `object` Information about the resource or system that manages the backend service.  
`items[].orchestrationInfo.resourceUri` |  `string` The resource URI of the resource or system that manages the backend service.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
