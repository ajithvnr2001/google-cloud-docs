---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext/
title: AttributeContext \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:33.377900+00:00
---

# AttributeContext  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  AttributeContext Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Response
    * JSON representation
  * Api
    * JSON representation



This message defines the standard attribute vocabulary for Google APIs.

An attribute is a piece of metadata that describes an activity on a network service. For example, the size of an HTTP request, or the status code of an HTTP response.

Each attribute has a type and a name, which is logically defined as a proto message field in `AttributeContext`. The field type becomes the attribute type, and the field path becomes the attribute name. For example, the attribute `source.ip` maps to field `AttributeContext.source.ip`.

This message definition is guaranteed not to have any wire breaking change. So you can use it directly for passing attributes across different systems.

NOTE: Different system may generate different subset of attributes. Please verify the system specification before relying on an attribute generated a system.

JSON representation  
---  
      
    
    {
      "origin": {
        object ([Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer))
      },
      "source": {
        object ([Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer))
      },
      "destination": {
        object ([Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer))
      },
      "request": {
        object ([Request](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Request))
      },
      "response": {
        object ([Response](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext#Response))
      },
      "resource": {
        object ([Resource](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Resource))
      },
      "api": {
        object ([Api](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext#Api))
      },
      "extensions": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`origin` |  `object (`[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer)`)` The origin of a network activity. In a multi hop network activity, the origin represents the sender of the first hop. For the first hop, the `source` and the `origin` must have the same content.  
`source` |  `object (`[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer)`)` The source of a network activity, such as starting a TCP connection. In a multi hop network activity, the source represents the sender of the last hop.  
`destination` |  `object (`[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Peer)`)` The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop.  
`request` |  `object (`[Request](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Request)`)` Represents a network request, such as an HTTP request.  
`response` |  `object (`[Response](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext#Response)`)` Represents a network response, such as an HTTP response.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Resource)`)` Represents a target resource that is involved with a network activity. If multiple resources are involved with an activity, this must be the primary one.  
`api` |  `object (`[Api](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext#Api)`)` Represents an API operation that is involved to a network activity.  
`extensions[]` |  `object` Supports extensions for advanced use cases, such as logs and metrics.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Response

This message defines attributes for a typical network response. It generally models semantics of an HTTP response.

JSON representation  
---  
      
    
    {
      "code": string,
      "size": string,
      "headers": {
        string: string,
        ...
      },
      "time": string,
      "backendLatency": string
    }  
  
Fields  
---  
`code` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The HTTP response status code, such as `200` and `404`.  
`size` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The HTTP response size in bytes. If unknown, it must be -1.  
`headers` |  `map (key: string, value: string)` The HTTP response headers. If multiple headers share the same key, they must be merged according to HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`time` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the `destination` service sends the last byte of the response.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`backendLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The amount of time it takes the backend service to fully respond to a request. Measured from when the destination service starts to send the request to the backend until when the destination service receives the complete response from the backend.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Api

This message defines attributes associated with API operations, such as a network API request. The terminology is based on the conventions used by Google APIs, Istio, and OpenAPI.

JSON representation  
---  
      
    
    {
      "service": string,
      "operation": string,
      "protocol": string,
      "version": string
    }  
  
Fields  
---  
`service` |  `string` The API service name. It is a logical identifier for a networked API, such as "pubsub.googleapis.com". The naming syntax depends on the API management system being used for handling the request.  
`operation` |  `string` The API operation name. For gRPC requests, it is the fully qualified API method name, such as "google.pubsub.v1.Publisher.Publish". For OpenAPI requests, it is the `operationId`, such as "getPet".  
`protocol` |  `string` The API protocol used for sending the request, such as "http", "https", "grpc", or "internal".  
`version` |  `string` The API version associated with the API operation above, such as "v1" or "v1alpha1".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
