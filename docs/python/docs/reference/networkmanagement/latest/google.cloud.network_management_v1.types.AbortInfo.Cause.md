---
url: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.AbortInfo.Cause
title: Class Cause (1.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:28.966110+00:00
---

# Class Cause (1.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.AbortInfo.Cause

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Cause (1.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.38.0 (latest)  1.37.0  1.36.0  1.35.0  1.34.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.1  1.25.3  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.17.3  1.16.0  1.15.1  1.14.0  1.13.3  1.12.0  1.11.0  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.4  1.4.0  1.3.3  1.2.1  1.1.0  1.0.2  0.2.0  0.1.1 
    
    
    Cause(value)

Abort cause types:
    
    
        - The request might contain malformed resource
          URI, project ID, or IP address.
        - The request might contain inconsistent
          information (for example, the request might
          include both the instance and the network, but
          the instance might not have a NIC in that
          network).
    TRACE_TOO_LONG (9):
        Aborted because the number of steps in the
        trace exceeds a certain limit. It might be
        caused by a routing loop.
    INTERNAL_ERROR (10):
        Aborted due to internal server error.
    UNSUPPORTED (15):
        Aborted because the test scenario is not
        supported.
    MISMATCHED_IP_VERSION (16):
        Aborted because the source and destination
        resources have no common IP version.
    GKE_KONNECTIVITY_PROXY_UNSUPPORTED (17):
        Aborted because the connection between the
        control plane and the node of the source cluster
        is initiated by the node and managed by the
        Konnectivity proxy.
    RESOURCE_CONFIG_NOT_FOUND (18):
        Aborted because expected resource
        configuration was missing.
    VM_INSTANCE_CONFIG_NOT_FOUND (24):
        Aborted because expected VM instance
        configuration was missing.
    NETWORK_CONFIG_NOT_FOUND (25):
        Aborted because expected network
        configuration was missing.
    FIREWALL_CONFIG_NOT_FOUND (26):
        Aborted because expected firewall
        configuration was missing.
    ROUTE_CONFIG_NOT_FOUND (27):
        Aborted because expected route configuration
        was missing.
    GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT (19):
        Aborted because PSC endpoint selection for
        the Google-managed service is ambiguous (several
        PSC endpoints satisfy test input).
    GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT (39):
        Aborted because endpoint selection for the
        Google-managed service is ambiguous (several
        endpoints satisfy test input).
    SOURCE_PSC_CLOUD_SQL_UNSUPPORTED (20):
        Aborted because tests with a PSC-based Cloud
        SQL instance as a source are not supported.
    SOURCE_EXTERNAL_CLOUD_SQL_UNSUPPORTED (45):
        Aborted because tests with the external
        database as a source are not supported. In such
        replication scenarios, the connection is
        initiated by the Cloud SQL replica instance.
    SOURCE_REDIS_CLUSTER_UNSUPPORTED (34):
        Aborted because tests with a Redis Cluster as
        a source are not supported.
    SOURCE_REDIS_INSTANCE_UNSUPPORTED (35):
        Aborted because tests with a Redis Instance
        as a source are not supported.
    SOURCE_FORWARDING_RULE_UNSUPPORTED (21):
        Aborted because tests with a forwarding rule
        as a source are not supported.
    NON_ROUTABLE_IP_ADDRESS (22):
        Aborted because one of the endpoints is a
        non-routable IP address (loopback, link-local,
        etc).
    UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT (30):
        Aborted due to an unknown issue in the
        Google-managed project.
    UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG (31):
        Aborted due to an unsupported configuration
        of the Google-managed project.
    NO_SERVERLESS_IP_RANGES (37):
        Aborted because the source endpoint is a
        Cloud Run revision with direct VPC access
        enabled, but there are no reserved serverless IP
        ranges.
    IP_VERSION_PROTOCOL_MISMATCH (40):
        Aborted because the used protocol is not
        supported for the used IP version.
    GKE_POD_UNKNOWN_ENDPOINT_LOCATION (41):
        Aborted because selected GKE Pod endpoint
        location is unknown. This is often the case for
        "Pending" Pods, which don't have assigned IP
        addresses yet.
    

## Enums  
  
---  
**Name** | **Description**  
`CAUSE_UNSPECIFIED` | Cause is unspecified.  
`UNKNOWN_NETWORK` | Aborted due to unknown network. Deprecated, not used in the new tests.  
`UNKNOWN_PROJECT` | Aborted because no project information can be derived from the test input. Deprecated, not used in the new tests.  
`NO_EXTERNAL_IP` | Aborted because traffic is sent from a public IP to an instance without an external IP. Deprecated, not used in the new tests.  
`UNINTENDED_DESTINATION` | Aborted because none of the traces matches destination information specified in the input test request. Deprecated, not used in the new tests.  
`SOURCE_ENDPOINT_NOT_FOUND` | Aborted because the source endpoint could not be found. Deprecated, not used in the new tests.  
`MISMATCHED_SOURCE_NETWORK` | Aborted because the source network does not match the source endpoint. Deprecated, not used in the new tests.  
`DESTINATION_ENDPOINT_NOT_FOUND` | Aborted because the destination endpoint could not be found. Deprecated, not used in the new tests.  
`MISMATCHED_DESTINATION_NETWORK` | Aborted because the destination network does not match the destination endpoint. Deprecated, not used in the new tests.  
`UNKNOWN_IP` | Aborted because no endpoint with the packet's destination IP address is found.  
`GOOGLE_MANAGED_SERVICE_UNKNOWN_IP` | Aborted because no endpoint with the packet's destination IP is found in the Google-managed project.  
`SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK` | Aborted because the source IP address doesn't belong to any of the subnets of the source VPC network.  
`PERMISSION_DENIED` | Aborted because user lacks permission to access all or part of the network configurations required to run the test.  
`PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS` | Aborted because user lacks permission to access Cloud NAT configs required to run the test.  
`PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS` | Aborted because user lacks permission to access Network endpoint group endpoint configs required to run the test.  
`PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS` | Aborted because user lacks permission to access Cloud Router configs required to run the test.  
`NO_SOURCE_LOCATION` | Aborted because no valid source or destination endpoint can be derived from the test request.  
`NO_SOURCE_GCP_NETWORK_LOCATION` | Aborted because the source IP address is not contained within the subnet ranges of the provided VPC network.  
`NO_SOURCE_NON_GCP_NETWORK_LOCATION` | Aborted because the source IP address is not contained within the destination ranges of the routes towards non-GCP networks in the provided VPC network.  
`NO_SOURCE_INTERNET_LOCATION` | Aborted because the source IP address can't be resolved as an Internet IP address.  
`INVALID_ARGUMENT` | Aborted because the source or destination endpoint specified in the request is invalid. Some examples:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
