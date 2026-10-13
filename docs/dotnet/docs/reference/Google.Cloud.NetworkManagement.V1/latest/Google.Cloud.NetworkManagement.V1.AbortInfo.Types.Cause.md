---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.AbortInfo.Types.Cause
title: Network Management v1 API - Enum AbortInfo.Types.Cause (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:45.193527+00:00
---

# Network Management v1 API - Enum AbortInfo.Types.Cause (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.AbortInfo.Types.Cause

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Management v1 API - Enum AbortInfo.Types.Cause (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public enum AbortInfo.Types.Cause

Reference documentation and code samples for the Network Management v1 API enum AbortInfo.Types.Cause.

Abort cause types:

## Namespace

[Google.Cloud.NetworkManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1)

## Assembly

Google.Cloud.NetworkManagement.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`DestinationEndpointNotFound` | Aborted because the destination endpoint could not be found. Deprecated, not used in the new tests.  
`FirewallConfigNotFound` | Aborted because expected firewall configuration was missing.  
`GkeKonnectivityProxyUnsupported` | Aborted because the connection between the control plane and the node of the source cluster is initiated by the node and managed by the Konnectivity proxy.  
`GkePodUnknownEndpointLocation` | Aborted because selected GKE Pod endpoint location is unknown. This is often the case for "Pending" Pods, which don't have assigned IP addresses yet.  
`GoogleManagedServiceAmbiguousEndpoint` | Aborted because endpoint selection for the Google-managed service is ambiguous (several endpoints satisfy test input).  
`GoogleManagedServiceAmbiguousPscEndpoint` | Aborted because PSC endpoint selection for the Google-managed service is ambiguous (several PSC endpoints satisfy test input).  
`GoogleManagedServiceUnknownIp` | Aborted because no endpoint with the packet's destination IP is found in the Google-managed project.  
`InternalError` | Aborted due to internal server error.  
`InvalidArgument` | Aborted because the source or destination endpoint specified in the request is invalid. Some examples:

  * The request might contain malformed resource URI, project ID, or IP address.
  * The request might contain inconsistent information (for example, the request might include both the instance and the network, but the instance might not have a NIC in that network).

  
`IpVersionProtocolMismatch` | Aborted because the used protocol is not supported for the used IP version.  
`MismatchedDestinationNetwork` | Aborted because the destination network does not match the destination endpoint. Deprecated, not used in the new tests.  
`MismatchedIpVersion` | Aborted because the source and destination resources have no common IP version.  
`MismatchedSourceNetwork` | Aborted because the source network does not match the source endpoint. Deprecated, not used in the new tests.  
`NetworkConfigNotFound` | Aborted because expected network configuration was missing.  
`NoExternalIp` | Aborted because traffic is sent from a public IP to an instance without an external IP. Deprecated, not used in the new tests.  
`NoServerlessIpRanges` | Aborted because the source endpoint is a Cloud Run revision with direct VPC access enabled, but there are no reserved serverless IP ranges.  
`NoSourceGcpNetworkLocation` | Aborted because the source IP address is not contained within the subnet ranges of the provided VPC network.  
`NoSourceInternetLocation` | Aborted because the source IP address can't be resolved as an Internet IP address.  
`NoSourceLocation` | Aborted because no valid source or destination endpoint can be derived from the test request.  
`NoSourceNonGcpNetworkLocation` | Aborted because the source IP address is not contained within the destination ranges of the routes towards non-GCP networks in the provided VPC network.  
`NonRoutableIpAddress` | Aborted because one of the endpoints is a non-routable IP address (loopback, link-local, etc).  
`PermissionDenied` | Aborted because user lacks permission to access all or part of the network configurations required to run the test.  
`PermissionDeniedNoCloudNatConfigs` | Aborted because user lacks permission to access Cloud NAT configs required to run the test.  
`PermissionDeniedNoCloudRouterConfigs` | Aborted because user lacks permission to access Cloud Router configs required to run the test.  
`PermissionDeniedNoNegEndpointConfigs` | Aborted because user lacks permission to access Network endpoint group endpoint configs required to run the test.  
`ResourceConfigNotFound` | Aborted because expected resource configuration was missing.  
`RouteConfigNotFound` | Aborted because expected route configuration was missing.  
`SourceEndpointNotFound` | Aborted because the source endpoint could not be found. Deprecated, not used in the new tests.  
`SourceExternalCloudSqlUnsupported` | Aborted because tests with the external database as a source are not supported. In such replication scenarios, the connection is initiated by the Cloud SQL replica instance.  
`SourceForwardingRuleUnsupported` | Aborted because tests with a forwarding rule as a source are not supported.  
`SourceIpAddressNotInSourceNetwork` | Aborted because the source IP address doesn't belong to any of the subnets of the source VPC network.  
`SourcePscCloudSqlUnsupported` | Aborted because tests with a PSC-based Cloud SQL instance as a source are not supported.  
`SourceRedisClusterUnsupported` | Aborted because tests with a Redis Cluster as a source are not supported.  
`SourceRedisInstanceUnsupported` | Aborted because tests with a Redis Instance as a source are not supported.  
`TraceTooLong` | Aborted because the number of steps in the trace exceeds a certain limit. It might be caused by a routing loop.  
`UnintendedDestination` | Aborted because none of the traces matches destination information specified in the input test request. Deprecated, not used in the new tests.  
`UnknownIp` | Aborted because no endpoint with the packet's destination IP address is found.  
`UnknownIssueInGoogleManagedProject` | Aborted due to an unknown issue in the Google-managed project.  
`UnknownNetwork` | Aborted due to unknown network. Deprecated, not used in the new tests.  
`UnknownProject` | Aborted because no project information can be derived from the test input. Deprecated, not used in the new tests.  
`Unspecified` | Cause is unspecified.  
`Unsupported` | Aborted because the test scenario is not supported.  
`UnsupportedGoogleManagedProjectConfig` | Aborted due to an unsupported configuration of the Google-managed project.  
`VmInstanceConfigNotFound` | Aborted because expected VM instance configuration was missing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
