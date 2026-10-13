---
url: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes
title: REST Resource: projects.locations.httpRoutes \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:51.484181+00:00
---

# REST Resource: projects.locations.httpRoutes  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/docs/apis)



Send feedback 

#  REST Resource: projects.locations.httpRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HttpRoute
    * JSON representation
  * RouteRule
    * JSON representation
  * RouteMatch
    * JSON representation
  * HeaderMatch
    * JSON representation
  * IntegerRange
    * JSON representation
  * QueryParameterMatch
    * JSON representation
  * RouteAction
    * JSON representation
  * Destination
    * JSON representation
  * HeaderModifier
    * JSON representation
  * Redirect
    * JSON representation
  * ResponseCode
  * FaultInjectionPolicy
    * JSON representation
  * Delay
    * JSON representation
  * Abort
    * JSON representation
  * URLRewrite
    * JSON representation
  * RetryPolicy
    * JSON representation
  * RequestMirrorPolicy
    * JSON representation
  * CorsPolicy
    * JSON representation
  * StatefulSessionAffinityPolicy
    * JSON representation
  * HttpDirectResponse
    * JSON representation
  * Methods



## Resource: HttpRoute

HttpRoute is the resource defining how HTTP traffic should be routed by a Mesh or Gateway resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "selfLink": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "hostnames": [
        string
      ],
      "meshes": [
        string
      ],
      "gateways": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "rules": [
        {
          object ([RouteRule](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the HttpRoute resource. It matches pattern `projects/*/locations/*/httpRoutes/http_route_name>`.  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`hostnames[]` |  `string` Required. Hostnames define a set of hosts that should match against the HTTP host header to select a HttpRoute to process the request. Hostname is the fully qualified domain name of a network host, as defined by RFC 1123 with the exception that: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (`*.`). The wildcard label must appear by itself as the first label.Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. `foo.example.com`) or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. `*.example.com`).Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed.The routes associated with a Mesh or Gateways must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected.For example, while it is acceptable for routes for the hostnames `*.foo.bar.com` and `*.bar.com` to be associated with the same Mesh (or Gateways under the same scope), it is not possible to associate two routes both with `*.bar.com` or both with `bar.com`.  
`meshes[]` |  `string` Optional. Meshes defines a list of meshes this HttpRoute is attached to, as one of the routing rules to route the requests served by the mesh.Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`The attached Mesh should be of a type SIDECAR  
`gateways[]` |  `string` Optional. Gateways defines a list of gateways this HttpRoute is attached to, as one of the routing rules to route the requests served by the gateway.Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the HttpRoute resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`rules[]` |  `object (`[RouteRule](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteRule)`)` Required. Rules that define how traffic is routed and handled. Rules will be matched sequentially based on the RouteMatch specified for the rule.  
  
## RouteRule

Specifies how to match traffic and how to route traffic when traffic is matched.

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([RouteMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteMatch))
        }
      ],
      "action": {
        object ([RouteAction](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteAction))
      }
    }  
  
Fields  
---  
`matches[]` |  `object (`[RouteMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteMatch)`)` A list of matches define conditions used for matching the rule against incoming HTTP requests. Each match is independent, i.e. this rule will be matched if ANY one of the matches is satisfied.If no matches field is specified, this rule will unconditionally match traffic.If a default rule is desired to be configured, add a rule with no matches specified to the end of the rules list.  
`action` |  `object (`[RouteAction](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RouteAction)`)` The detailed rule defining how to route matched traffic.  
  
## RouteMatch

RouteMatch defines specifications used to match requests. If multiple match types are set, this RouteMatch will match if ALL type of matches are matched.

JSON representation  
---  
      
    
    {
      "ignoreCase": boolean,
      "headers": [
        {
          object ([HeaderMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderMatch))
        }
      ],
      "queryParameters": [
        {
          object ([QueryParameterMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#QueryParameterMatch))
        }
      ],
    
      // Union field PathMatch can be only one of the following:
      "fullPathMatch": string,
      "prefixMatch": string,
      "regexMatch": string
      // End of list of possible types for union field PathMatch.
    }  
  
Fields  
---  
`ignoreCase` |  `boolean` Specifies if prefixMatch and fullPathMatch matches are case sensitive. The default value is false.  
`headers[]` |  `object (`[HeaderMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderMatch)`)` Specifies a list of HTTP request headers to match against. ALL of the supplied headers must be matched.  
`queryParameters[]` |  `object (`[QueryParameterMatch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#QueryParameterMatch)`)` Specifies a list of query parameters to match against. ALL of the query parameters must be matched.  
Union field `PathMatch`.`PathMatch` can be only one of the following:  
`fullPathMatch` |  `string` The HTTP request path value should exactly match this value.Only one of fullPathMatch, prefixMatch, or regexMatch should be used.  
`prefixMatch` |  `string` The HTTP request path value must begin with specified prefixMatch. prefixMatch must begin with a /.Only one of fullPathMatch, prefixMatch, or regexMatch should be used.  
`regexMatch` |  `string` The HTTP request path value must satisfy the regular expression specified by regexMatch after removing any query parameters and anchor supplied with the original URL. For regular expression grammar, please see <https://github.com/google/re2/wiki/Syntax>Only one of fullPathMatch, prefixMatch, or regexMatch should be used.  
  
## HeaderMatch

Specifies how to select a route rule based on HTTP request headers.

JSON representation  
---  
      
    
    {
      "header": string,
      "invertMatch": boolean,
    
      // Union field MatchType can be only one of the following:
      "exactMatch": string,
      "regexMatch": string,
      "prefixMatch": string,
      "presentMatch": boolean,
      "suffixMatch": string,
      "rangeMatch": {
        object ([IntegerRange](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#IntegerRange))
      }
      // End of list of possible types for union field MatchType.
    }  
  
Fields  
---  
`header` |  `string` The name of the HTTP header to match against.  
`invertMatch` |  `boolean` If specified, the match result will be inverted before checking. Default value is set to false.  
Union field `MatchType`.`MatchType` can be only one of the following:  
`exactMatch` |  `string` The value of the header should match exactly the content of exactMatch.  
`regexMatch` |  `string` The value of the header must match the regular expression specified in regexMatch. For regular expression grammar, please see: <https://github.com/google/re2/wiki/Syntax>  
`prefixMatch` |  `string` The value of the header must start with the contents of prefixMatch.  
`presentMatch` |  `boolean` A header with headerName must exist. The match takes place whether or not the header has a value.  
`suffixMatch` |  `string` The value of the header must end with the contents of suffixMatch.  
`rangeMatch` |  `object (`[IntegerRange](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#IntegerRange)`)` If specified, the rule will match if the request header value is within the range.  
  
## IntegerRange

Represents an integer value range.

JSON representation  
---  
      
    
    {
      "start": integer,
      "end": integer
    }  
  
Fields  
---  
`start` |  `integer` Start of the range (inclusive)  
`end` |  `integer` End of the range (exclusive)  
  
## QueryParameterMatch

Specifications to match a query parameter in the request.

JSON representation  
---  
      
    
    {
      "queryParameter": string,
    
      // Union field MatchType can be only one of the following:
      "exactMatch": string,
      "regexMatch": string,
      "presentMatch": boolean
      // End of list of possible types for union field MatchType.
    }  
  
Fields  
---  
`queryParameter` |  `string` The name of the query parameter to match.  
Union field `MatchType`.`MatchType` can be only one of the following:  
`exactMatch` |  `string` The value of the query parameter must exactly match the contents of exactMatch.Only one of exactMatch, regexMatch, or presentMatch must be set.  
`regexMatch` |  `string` The value of the query parameter must match the regular expression specified by regexMatch. For regular expression grammar, please see <https://github.com/google/re2/wiki/Syntax>Only one of exactMatch, regexMatch, or presentMatch must be set.  
`presentMatch` |  `boolean` Specifies that the QueryParameterMatcher matches if request contains query parameter, irrespective of whether the parameter has a value or not.Only one of exactMatch, regexMatch, or presentMatch must be set.  
  
## RouteAction

The specifications for routing traffic and applying associated policies.

JSON representation  
---  
      
    
    {
      "destinations": [
        {
          object ([Destination](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Destination))
        }
      ],
      "redirect": {
        object ([Redirect](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Redirect))
      },
      "faultInjectionPolicy": {
        object ([FaultInjectionPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#FaultInjectionPolicy))
      },
      "requestHeaderModifier": {
        object ([HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier))
      },
      "responseHeaderModifier": {
        object ([HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier))
      },
      "urlRewrite": {
        object ([URLRewrite](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#URLRewrite))
      },
      "timeout": string,
      "retryPolicy": {
        object ([RetryPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RetryPolicy))
      },
      "requestMirrorPolicy": {
        object ([RequestMirrorPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RequestMirrorPolicy))
      },
      "corsPolicy": {
        object ([CorsPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#CorsPolicy))
      },
      "statefulSessionAffinity": {
        object ([StatefulSessionAffinityPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#StatefulSessionAffinityPolicy))
      },
      "directResponse": {
        object ([HttpDirectResponse](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HttpDirectResponse))
      },
      "idleTimeout": string
    }  
  
Fields  
---  
`destinations[]` |  `object (`[Destination](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Destination)`)` The destination to which traffic should be forwarded.  
`redirect` |  `object (`[Redirect](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Redirect)`)` If set, the request is directed as configured by this field.  
`faultInjectionPolicy` |  `object (`[FaultInjectionPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#FaultInjectionPolicy)`)` The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure. As part of fault injection, when clients send requests to a backend service, delays can be introduced on a percentage of requests before sending those requests to the backend service. Similarly requests from clients can be aborted for a percentage of requests.timeout and retryPolicy will be ignored by clients that are configured with a faultInjectionPolicy  
`requestHeaderModifier` |  `object (`[HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier)`)` The specification for modifying the headers of a matching request prior to delivery of the request to the destination. If HeaderModifiers are set on both the Destination and the RouteAction, they will be merged. Conflicts between the two will not be resolved on the configuration.  
`responseHeaderModifier` |  `object (`[HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier)`)` The specification for modifying the headers of a response prior to sending the response back to the client. If HeaderModifiers are set on both the Destination and the RouteAction, they will be merged. Conflicts between the two will not be resolved on the configuration.  
`urlRewrite` |  `object (`[URLRewrite](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#URLRewrite)`)` The specification for rewrite URL before forwarding requests to the destination.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Specifies the timeout for selected route. Timeout is computed from the time the request has been fully processed (i.e. end of stream) up until the response has been completely processed. Timeout includes all retries.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`retryPolicy` |  `object (`[RetryPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RetryPolicy)`)` Specifies the retry policy associated with this route.  
`requestMirrorPolicy` |  `object (`[RequestMirrorPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#RequestMirrorPolicy)`)` Specifies the policy on how requests intended for the routes destination are shadowed to a separate mirrored destination. Proxy will not wait for the shadow destination to respond before returning the response. Prior to sending traffic to the shadow service, the host/authority header is suffixed with -shadow.  
`corsPolicy` |  `object (`[CorsPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#CorsPolicy)`)` The specification for allowing client side cross-origin requests.  
`statefulSessionAffinity` |  `object (`[StatefulSessionAffinityPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#StatefulSessionAffinityPolicy)`)` Optional. Specifies cookie-based stateful session affinity.  
`directResponse` |  `object (`[HttpDirectResponse](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HttpDirectResponse)`)` Optional. Static HTTP Response object to be returned regardless of the request.  
`idleTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Destination

Specifications of a destination to which the request should be routed to.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "weight": integer,
      "requestHeaderModifier": {
        object ([HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier))
      },
      "responseHeaderModifier": {
        object ([HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier))
      }
    }  
  
Fields  
---  
`serviceName` |  `string` The URL of a BackendService to route traffic to.  
`weight` |  `integer` Specifies the proportion of requests forwarded to the backend referenced by the serviceName field. This is computed as: - weight/Sum(weights in this destination list). For non-zero values, there may be some epsilon from the exact proportion defined here depending on the precision an implementation supports.If only one serviceName is specified and it has a weight greater than 0, 100% of the traffic is forwarded to that backend.If weights are specified for any one service name, they need to be specified for all of them.If weights are unspecified for all services, then, traffic is distributed in equal proportions to all of them.  
`requestHeaderModifier` |  `object (`[HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier)`)` Optional. The specification for modifying the headers of a matching request prior to delivery of the request to the destination. If HeaderModifiers are set on both the Destination and the RouteAction, they will be merged. Conflicts between the two will not be resolved on the configuration.  
`responseHeaderModifier` |  `object (`[HeaderModifier](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#HeaderModifier)`)` Optional. The specification for modifying the headers of a response prior to sending the response back to the client. If HeaderModifiers are set on both the Destination and the RouteAction, they will be merged. Conflicts between the two will not be resolved on the configuration.  
  
## HeaderModifier

The specification for modifying HTTP header in HTTP request and HTTP response.

JSON representation  
---  
      
    
    {
      "set": {
        string: string,
        ...
      },
      "add": {
        string: string,
        ...
      },
      "remove": [
        string
      ]
    }  
  
Fields  
---  
`set` |  `map (key: string, value: string)` Completely overwrite/replace the headers with given map where key is the name of the header, value is the value of the header.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`add` |  `map (key: string, value: string)` Add the headers with given map where key is the name of the header, value is the value of the header.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`remove[]` |  `string` Remove headers (matching by header names) specified in the list.  
  
## Redirect

The specification for redirecting traffic.

JSON representation  
---  
      
    
    {
      "hostRedirect": string,
      "pathRedirect": string,
      "prefixRewrite": string,
      "responseCode": enum ([ResponseCode](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#ResponseCode)),
      "httpsRedirect": boolean,
      "stripQuery": boolean,
      "portRedirect": integer
    }  
  
Fields  
---  
`hostRedirect` |  `string` The host that will be used in the redirect response instead of the one that was supplied in the request.  
`pathRedirect` |  `string` The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect can not be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect.  
`prefixRewrite` |  `string` Indicates that during redirection, the matched prefix (or path) should be swapped with this value. This option allows URLs be dynamically created based on the request.  
`responseCode` |  `enum (`[ResponseCode](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#ResponseCode)`)` The HTTP Status code to use for the redirect.  
`httpsRedirect` |  `boolean` If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request.The default is set to false.  
`stripQuery` |  `boolean` if set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained.The default is set to false.  
`portRedirect` |  `integer` The port that will be used in the redirected request instead of the one that was supplied in the request.  
  
## ResponseCode

Supported HTTP response code.

Enums  
---  
`RESPONSE_CODE_UNSPECIFIED` | Default value  
`MOVED_PERMANENTLY_DEFAULT` | Corresponds to 301.  
`FOUND` | Corresponds to 302.  
`SEE_OTHER` | Corresponds to 303.  
`TEMPORARY_REDIRECT` | Corresponds to 307. In this case, the request method will be retained.  
`PERMANENT_REDIRECT` | Corresponds to 308. In this case, the request method will be retained.  
  
## FaultInjectionPolicy

The specification for fault injection introduced into traffic to test the resiliency of clients to destination service failure. As part of fault injection, when clients send requests to a destination, delays can be introduced by client proxy on a percentage of requests before sending those requests to the destination service. Similarly requests can be aborted by client proxy for a percentage of requests.

JSON representation  
---  
      
    
    {
      "delay": {
        object ([Delay](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Delay))
      },
      "abort": {
        object ([Abort](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Abort))
      }
    }  
  
Fields  
---  
`delay` |  `object (`[Delay](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Delay)`)` The specification for injecting delay to client requests.  
`abort` |  `object (`[Abort](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Abort)`)` The specification for aborting to client requests.  
  
## Delay

Specification of how client requests are delayed as part of fault injection before being sent to a destination.

JSON representation  
---  
      
    
    {
      "fixedDelay": string,
      "percentage": integer
    }  
  
Fields  
---  
`fixedDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Specify a fixed delay before forwarding the request.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`percentage` |  `integer` The percentage of traffic on which delay will be injected.The value must be between [0, 100]  
  
## Abort

Specification of how client requests are aborted as part of fault injection before being sent to a destination.

JSON representation  
---  
      
    
    {
      "httpStatus": integer,
      "percentage": integer
    }  
  
Fields  
---  
`httpStatus` |  `integer` The HTTP status code used to abort the request.The value must be between 200 and 599 inclusive.  
`percentage` |  `integer` The percentage of traffic which will be aborted.The value must be between [0, 100]  
  
## URLRewrite

The specification for modifying the URL of the request, prior to forwarding the request to the destination.

JSON representation  
---  
      
    
    {
      "pathPrefixRewrite": string,
      "hostRewrite": string
    }  
  
Fields  
---  
`pathPrefixRewrite` |  `string` Prior to forwarding the request to the selected destination, the matching portion of the requests path is replaced by this value.  
`hostRewrite` |  `string` Prior to forwarding the request to the selected destination, the requests host header is replaced by this value.  
  
## RetryPolicy

The specifications for retries.

JSON representation  
---  
      
    
    {
      "retryConditions": [
        string
      ],
      "numRetries": integer,
      "perTryTimeout": string
    }  
  
Fields  
---  
`retryConditions[]` |  `string` Specifies one or more conditions when this retry policy applies. Valid values are: 5xx: Proxy will attempt a retry if the destination service responds with any 5xx response code, of if the destination service does not respond at all, example: disconnect, reset, read timeout, connection failure and refused streams.gateway-error: Similar to 5xx, but only applies to response codes 502, 503, 504.reset: Proxy will attempt a retry if the destination service does not respond at all (disconnect/reset/read timeout)connect-failure: Proxy will retry on failures connecting to destination for example due to connection timeouts.retriable-4xx: Proxy will retry fro retriable 4xx response codes. Currently the only retriable error supported is 409.refused-stream: Proxy will retry if the destination resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry.  
`numRetries` |  `integer` Specifies the allowed number of retries. This number must be > 0\. If not specified, default to 1.  
`perTryTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Specifies a non-zero timeout per retry attempt.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## RequestMirrorPolicy

Specifies the policy on how requests are shadowed to a separate mirrored destination service. The proxy does not wait for responses from the shadow service. Prior to sending traffic to the shadow service, the host/authority header is suffixed with -shadow. Mirroring is currently not supported for Cloud Run destinations.

JSON representation  
---  
      
    
    {
      "destination": {
        object ([Destination](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Destination))
      },
      "mirrorPercent": number
    }  
  
Fields  
---  
`destination` |  `object (`[Destination](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes#Destination)`)` The destination the requests will be mirrored to. The weight of the destination will be ignored.  
`mirrorPercent` |  `number` Optional. The percentage of requests to get mirrored to the desired destination.  
  
## CorsPolicy

The Specification for allowing client side cross-origin requests.

JSON representation  
---  
      
    
    {
      "allowOrigins": [
        string
      ],
      "allowOriginRegexes": [
        string
      ],
      "allowMethods": [
        string
      ],
      "allowHeaders": [
        string
      ],
      "exposeHeaders": [
        string
      ],
      "maxAge": string,
      "allowCredentials": boolean,
      "disabled": boolean
    }  
  
Fields  
---  
`allowOrigins[]` |  `string` Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either an item in allowOrigins or an item in allowOriginRegexes.  
`allowOriginRegexes[]` |  `string` Specifies the regular expression patterns that match allowed origins. For regular expression grammar, please see <https://github.com/google/re2/wiki/Syntax>.  
`allowMethods[]` |  `string` Specifies the content for Access-Control-Allow-Methods header.  
`allowHeaders[]` |  `string` Specifies the content for Access-Control-Allow-Headers header.  
`exposeHeaders[]` |  `string` Specifies the content for Access-Control-Expose-Headers header.  
`maxAge` |  `string` Specifies how long result of a preflight request can be cached in seconds. This translates to the Access-Control-Max-Age header.  
`allowCredentials` |  `boolean` In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access-Control-Allow-Credentials header.Default value is false.  
`disabled` |  `boolean` If true, the CORS policy is disabled. The default value is false, which indicates that the CORS policy is in effect.  
  
## StatefulSessionAffinityPolicy

The specification for cookie-based stateful session affinity where the date plane supplies a “session cookie” with the name "GSSA" which encodes a specific destination host and each request containing that cookie will be directed to that host as long as the destination host remains up and healthy.

The gRPC proxyless mesh library or sidecar proxy will manage the session cookie but the client application code is responsible for copying the cookie from each RPC in the session to the next.

JSON representation  
---  
      
    
    {
      "cookieTtl": string
    }  
  
Fields  
---  
`cookieTtl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The cookie TTL value for the Set-Cookie header generated by the data plane. The lifetime of the cookie may be set to a value from 0 to 86400 seconds (24 hours) inclusive.Set this to 0s to use a session cookie and disable cookie expiration.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## HttpDirectResponse

Static HTTP response object to be returned.

JSON representation  
---  
      
    
    {
      "status": integer,
    
      // Union field HttpBody can be only one of the following:
      "stringBody": string,
      "bytesBody": string
      // End of list of possible types for union field HttpBody.
    }  
  
Fields  
---  
`status` |  `integer` Required. Status to return as part of HTTP Response. Must be a positive integer.  
Union field `HttpBody`. Body to return as part of HTTP Response. `HttpBody` can be only one of the following:  
`stringBody` |  `string` Optional. Response body as a string. Maximum body length is 1024 characters.  
`bytesBody` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Response body as bytes. Maximum body size is 4096B.A base64-encoded string.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/create)`

|  Creates a new HttpRoute in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/delete)`

|  Deletes a single HttpRoute.  
  
### `[get](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/get)`

|  Gets details of a single HttpRoute.  
  
### `[list](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/list)`

|  Lists HttpRoute in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/patch)`

|  Updates the parameters of a single HttpRoute.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
