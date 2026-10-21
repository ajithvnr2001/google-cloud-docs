---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context/
title: Package google.rpc.context \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:35.560902+00:00
---

# Package google.rpc.context  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.rpc.context Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext)` (message)
  * `[AttributeContext.Api](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Api)` (message)
  * `[AttributeContext.Auth](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Auth)` (message)
  * `[AttributeContext.Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Peer)` (message)
  * `[AttributeContext.Request](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Request)` (message)
  * `[AttributeContext.Resource](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Resource)` (message)
  * `[AttributeContext.Response](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Response)` (message)



## AttributeContext

This message defines the standard attribute vocabulary for Google APIs.

An attribute is a piece of metadata that describes an activity on a network service. For example, the size of an HTTP request, or the status code of an HTTP response.

Each attribute has a type and a name, which is logically defined as a proto message field in `AttributeContext`. The field type becomes the attribute type, and the field path becomes the attribute name. For example, the attribute `source.ip` maps to field `AttributeContext.source.ip`.

This message definition is guaranteed not to have any wire breaking change. So you can use it directly for passing attributes across different systems.

NOTE: Different system may generate different subset of attributes. Please verify the system specification before relying on an attribute generated a system.

Fields  
---  
`origin` |  ``[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Peer)`` The origin of a network activity. In a multi hop network activity, the origin represents the sender of the first hop. For the first hop, the `source` and the `origin` must have the same content.  
`source` |  ``[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Peer)`` The source of a network activity, such as starting a TCP connection. In a multi hop network activity, the source represents the sender of the last hop.  
`destination` |  ``[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Peer)`` The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop.  
`request` |  ``[Request](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Request)`` Represents a network request, such as an HTTP request.  
`response` |  ``[Response](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Response)`` Represents a network response, such as an HTTP response.  
`resource` |  ``[Resource](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Resource)`` Represents a target resource that is involved with a network activity. If multiple resources are involved with an activity, this must be the primary one.  
`api` |  ``[Api](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Api)`` Represents an API operation that is involved to a network activity.  
`extensions[]` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Supports extensions for advanced use cases, such as logs and metrics.  
  
## Api

This message defines attributes associated with API operations, such as a network API request. The terminology is based on the conventions used by Google APIs, Istio, and OpenAPI.

Fields  
---  
`service` |  `string` The API service name. It is a logical identifier for a networked API, such as "pubsub.googleapis.com". The naming syntax depends on the API management system being used for handling the request.  
`operation` |  `string` The API operation name. For gRPC requests, it is the fully qualified API method name, such as "google.pubsub.v1.Publisher.Publish". For OpenAPI requests, it is the `operationId`, such as "getPet".  
`protocol` |  `string` The API protocol used for sending the request, such as "http", "https", "grpc", or "internal".  
`version` |  `string` The API version associated with the API operation above, such as "v1" or "v1alpha1".  
  
## Auth

This message defines request authentication attributes. Terminology is based on the JSON Web Token (JWT) standard, but the terms also correlate to concepts in other standards.

Fields  
---  
`principal` |  `string` The authenticated principal. Reflects the issuer (`iss`) and subject (`sub`) claims within a JWT. The issuer and subject should be `/` delimited, with `/` percent-encoded within the subject fragment. For Google accounts, the principal format is: "https://accounts.google.com/{id}"  
`audiences[]` |  `string` The intended audience(s) for this authentication information. Reflects the audience (`aud`) claim within a JWT. The audience value(s) depends on the `issuer`, but typically include one or more of the following pieces of information:

  * The services intended to receive the credential. For example, ["https://pubsub.googleapis.com/", "https://storage.googleapis.com/"].
  * A set of service-based scopes. For example, ["https://www.googleapis.com/auth/cloud-platform"].
  * The client id of an app, such as the Firebase project id for JWTs from Firebase Auth.

Consult the documentation for the credential issuer to determine the information provided.  
`presenter` |  `string` The authorized presenter of the credential. Reflects the optional Authorized Presenter (`azp`) claim within a JWT or the OAuth client id. For example, a Google Cloud Platform client id looks as follows: "123456789012.apps.googleusercontent.com".  
`claims` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` Structured claims presented with the credential. JWTs include `{key: value}` pairs for standard and private claims. The following is a subset of the standard required and optional claims that would typically be presented for a Google-based JWT:{'iss': 'accounts.google.com', 'sub': '113289723416554971153', 'aud': ['123456789012', 'pubsub.googleapis.com'], 'azp': '123456789012.apps.googleusercontent.com', 'email': 'jsmith@example.com', 'iat': 1353601026, 'exp': 1353604926}SAML assertions are similarly specified, but with an identity provider dependent structure.  
`access_levels[]` |  `string` A list of access level resource names that allow resources to be accessed by authenticated requester. It is part of Secure GCP processing for the incoming request. An access level string has the format: "//{api_service_name}/accessPolicies/{policy_id}/accessLevels/{short_name}"Example: "//accesscontextmanager.googleapis.com/accessPolicies/MY_POLICY_ID/accessLevels/MY_LEVEL"  
  
## Peer

This message defines attributes for a node that handles a network request. The node can be either a service or an application that sends, forwards, or receives the request. Service peers should fill in `principal` and `labels` as appropriate.

Fields  
---  
`ip` |  `string` The IP address of the peer.  
`port` |  `int64` The network port of the peer.  
`labels` |  `map<string, string>` The labels associated with the peer.  
`principal` |  `string` The identity of this peer. Similar to `Request.auth.principal`, but relative to the peer instead of the request. For example, the idenity associated with a load balancer that forwared the request.  
`region_code` |  `string` The CLDR country/region code associated with the above IP address. If the IP address is private, the `region_code` should reflect the physical location where this peer is running.  
  
## Request

This message defines attributes for an HTTP request. If the actual request is not an HTTP request, the runtime system should try to map the actual request to an equivalent HTTP request.

Fields  
---  
`id` |  `string` The unique ID for a request, which can be propagated to downstream systems. The ID should have low probability of collision within a single day for a specific service.  
`method` |  `string` The HTTP request method, such as `GET`, `POST`.  
`headers` |  `map<string, string>` The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.  
`path` |  `string` The HTTP URL path.  
`host` |  `string` The HTTP request `Host` header value.  
`scheme` |  `string` The HTTP URL scheme, such as `http` and `https`.  
`query` |  `string` The HTTP URL query in the format of `name1=value1&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed.  
`time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The timestamp when the `destination` service receives the first byte of the request.  
`size` |  `int64` The HTTP request size in bytes. If unknown, it must be -1.  
`protocol` |  `string` The network protocol used with the request, such as "http/1.1", "spdy/3", "h2", "h2c", "webrtc", "tcp", "udp", "quic". See <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids> for details.  
`reason` |  `string` A special parameter for request reason. It is used by security systems to associate auditing information with a request.  
`auth` |  ``[Auth](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Auth)`` The request authentication. May be absent for unauthenticated requests. Derived from the HTTP request `Authorization` header or equivalent.  
  
## Resource

This message defines core attributes for a resource. A resource is an addressable (named) entity provided by the destination service. For example, a file stored on a network storage service.

Fields  
---  
`service` |  `string` The name of the service that this resource belongs to, such as `pubsub.googleapis.com`. The service may be different from the DNS hostname that actually serves the request.  
`name` |  `string` The stable identifier (name) of a resource on the `service`. A resource can be logically identified as "//{resource.service}/{resource.name}". The differences between a resource name and a URI are:

  * Resource name is a logical identifier, independent of network protocol and API version. For example, `//pubsub.googleapis.com/projects/123/topics/news-feed`.
  * URI often includes protocol and version information, so it can be used directly by applications. For example, `https://pubsub.googleapis.com/v1/projects/123/topics/news-feed`.

See <https://cloud.google.com/apis/design/resource_names> for details.  
`type` |  `string` The type of the resource. The syntax is platform-specific because different platforms define their resources differently.For Google APIs, the type format must be "{service}/{kind}".  
`labels` |  `map<string, string>` The labels or tags on the resource, such as AWS resource tags and Kubernetes resource labels.  
`uid` |  `string` The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`annotations` |  `map<string, string>` Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>  
`display_name` |  `string` Mutable. The display name set by clients. Must be <= 63 characters.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The timestamp when the resource was created. This may be either the time creation was initiated or when it was completed.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.  
`delete_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The timestamp when the resource was deleted. If the resource is not deleted, this must be empty.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`location` |  `string` Immutable. The location of the resource. The location encoding is specific to the service provider, and new encoding may be introduced as the service evolves.For Google Cloud products, the encoding is what is used by Google Cloud APIs, such as `us-east1`, `aws-us-east-1`, and `azure-eastus2`. The semantics of `location` is identical to the `cloud.googleapis.com/location` label used by some Google Cloud APIs.  
  
## Response

This message defines attributes for a typical network response. It generally models semantics of an HTTP response.

Fields  
---  
`code` |  `int64` The HTTP response status code, such as `200` and `404`.  
`size` |  `int64` The HTTP response size in bytes. If unknown, it must be -1.  
`headers` |  `map<string, string>` The HTTP response headers. If multiple headers share the same key, they must be merged according to HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.  
`time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The timestamp when the `destination` service generates the first byte of the response.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
