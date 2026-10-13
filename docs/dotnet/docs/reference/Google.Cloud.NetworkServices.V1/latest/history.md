---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/history/
title: Version history \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:59.955044+00:00
---

# Version history  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Version history Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

## Version 1.7.0, released 2026-07-28

### New features

  * Deprecate client_tls_policy field from Endpoint Policy proto
  * A new field `resource_uris` is added to message `.google.cloud.networkservices.v1.AgentGateway`



### Documentation improvements

  * Fix unclosed backtick in AgentGateway registries comment



## Version 1.6.0, released 2026-06-18

### New features

  * Add AgentGateway resource and associated RPCs
  * Support regional EndpointPolicy, GrpcRoute, HttpRoute, Mesh, TcpRoute, and TlsRoute resources
  * Add EXT_AUTHZ_GRPC wire format and BodySendMode enum in dep.proto
  * Add forward_attributes, request_body_send_mode, and response_body_send_mode to Extension
  * Support generic artifacts for Wasm plugin images and configuration
  * Add all_ports and allow_global_access fields to Gateway
  * Add filter to ListHttpRoutesRequest and request_id to CreateHttpRouteRequest
  * Add target_proxies and labels to TlsRoute



### Documentation improvements

  * Update Gateway port limits for SECURE_WEB_GATEWAY
  * Update RouteView resource patterns to use project numbers
  * Update TlsRoute sni_host limit documentation



## Version 1.5.0, released 2025-11-05

### New features

  * Update dependencies



## Version 1.4.0, released 2025-11-05

### New features

  * Add support for LbEdgeExtension resource in NetworkServices API



## Version 1.3.0, released 2025-07-09

### New features

  * Add isolation support to prevent cross-region overflow by adding a new field "isolation_config" to message "ServiceLbPolicy"



## Version 1.2.0, released 2025-06-25

### New features

  * Add support for WasmPlugin resource in NetworkServices API



### Documentation improvements

  * A comment for enum `LoadBalancingScheme` is changed
  * A comment for field `authority` in message `.google.cloud.networkservices.v1.ExtensionChain` is changed
  * A comment for field `service` in message `.google.cloud.networkservices.v1.ExtensionChain` is changed
  * A comment for field `supported_events` in message `.google.cloud.networkservices.v1.ExtensionChain` is changed
  * A comment for field `timeout` in message `.google.cloud.networkservices.v1.ExtensionChain` is changed
  * A comment for field `extensions` in message `.google.cloud.networkservices.v1.ExtensionChain` is changed
  * A comment for field `forwarding_rules` in message `.google.cloud.networkservices.v1.LbTrafficExtension` is changed
  * A comment for field `load_balancing_scheme` in message `.google.cloud.networkservices.v1.LbTrafficExtension` is changed
  * A comment for field `metadata` in message `.google.cloud.networkservices.v1.LbTrafficExtension` is changed
  * A comment for field `parent` in message `.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest` is changed
  * A comment for field `order_by` in message `.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.CreateLbTrafficExtensionRequest` is changed
  * A comment for field `update_mask` in message `.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.DeleteLbTrafficExtensionRequest` is changed
  * A comment for field `forwarding_rules` in message `.google.cloud.networkservices.v1.LbRouteExtension` is changed
  * A comment for field `load_balancing_scheme` in message `.google.cloud.networkservices.v1.LbRouteExtension` is changed
  * A comment for field `metadata` in message `.google.cloud.networkservices.v1.LbRouteExtension` is changed
  * A comment for field `parent` in message `.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest` is changed
  * A comment for field `order_by` in message `.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.CreateLbRouteExtensionRequest` is changed
  * A comment for field `update_mask` in message `.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest` is changed
  * A comment for field `request_id` in message `.google.cloud.networkservices.v1.DeleteLbRouteExtensionRequest` is changed



## Version 1.1.0, released 2025-06-13

### New features

  * Update NetworkServices protos



### Documentation improvements

  * A comment for field `metadata_label_match_criteria` in message `.google.cloud.networkservices.v1.EndpointMatcher` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.EndpointPolicy` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.Gateway` is changed
  * A comment for field `ports` in message `.google.cloud.networkservices.v1.Gateway` is changed
  * A comment for field `scope` in message `.google.cloud.networkservices.v1.Gateway` is changed
  * A comment for message `GrpcRoute` is changed
  * A comment for field `fault_injection_policy` in message `.google.cloud.networkservices.v1.GrpcRoute` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.GrpcRoute` is changed
  * A comment for message `HttpRoute` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.HttpRoute` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.Mesh` is changed
  * A comment for message `ServiceBinding` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.ServiceBinding` is changed
  * A comment for field `service` in message `.google.cloud.networkservices.v1.ServiceBinding` is changed
  * A comment for field `parent` in message `.google.cloud.networkservices.v1.ListServiceBindingsRequest` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.GetServiceBindingRequest` is changed
  * A comment for field `parent` in message `.google.cloud.networkservices.v1.CreateServiceBindingRequest` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.DeleteServiceBindingRequest` is changed
  * A comment for field `address` in message `.google.cloud.networkservices.v1.TcpRoute` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.TcpRoute` is changed
  * A comment for message `TlsRoute` is changed
  * A comment for field `matches` in message `.google.cloud.networkservices.v1.TlsRoute` is changed
  * A comment for field `sni_host` in message `.google.cloud.networkservices.v1.TlsRoute` is changed
  * A comment for field `weight` in message `.google.cloud.networkservices.v1.TlsRoute` is changed
  * A comment for field `name` in message `.google.cloud.networkservices.v1.TlsRoute` is changed



## Version 1.0.0, released 2024-12-05

No API surface changes; just dependency updates and promotion to GA.

## Version 1.0.0-beta01, released 2024-06-19

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
