---
url: https://docs.cloud.google.com/media-cdn/docs/client-connectivity/
title: Client connectivity and IP addresses \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:59.229696+00:00
---

# Client connectivity and IP addresses  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/client-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Client connectivity and IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN supports modern networking protocols from the client to the edge, increasing throughput and reducing overall network latency.

## IP addressing

Each Edge Cache service that you configure has dedicated, anycast IPv4 and IPv6 addresses, which are associated with each Edge Cache service that you create and are not shared with other customers.

  * After configuring an Edge Cache service, the IP addresses are assigned and become available.
  * Assigned addresses don't change for the life of a given Edge Cache service.
  * Creating a new Edge Cache service issues new IP addresses scoped to that service. IP addresses are not shared across your services.



All Media CDN services support IPv6 between clients and each edge node.

**Caution:** Deleting a service releases its IP addresses. These IP addresses might not be re-assigned to other services that you create.

### Retrieve IP addresses

To retrieve the IP addresses assigned to an Edge Cache service:

###  gcloud 

Use the `gcloud edge-cache services` command.
    
    
    gcloud edge-cache services describe SERVICE_NAME
    
    
    
    ...
    ipv4Addresses: ["35.1.1.1"]
    ipv6Addresses: ["2600:1901:0:fa74::"]
    ...
    

Notes:

  * Media CDN issues one IPv4 and one IPv6 address per service.
  * We recommend creating DNS records for both IP addresses (as A and AAAA records).
  * Configure your services to accept traffic for any domain names (hostnames) that you are using. When traffic is received for hosts without a `.routing.hostRules[].hosts` entry, Media CDN rejects the traffic with an HTTP 404 error.



Depending on the geographies that your users are in, you might see more traffic to one protocol than another, based on user devices and ISP support in those geographies.

## Client timeouts

The following timeouts apply to client connections:

Timeout | Maximum duration | Status code | Description  
---|---|---|---  
**Maximum request duration** | 5 minutes | HTTP `408 Request Timeout` | The maximum duration of a single request-response.  
**Header timeout** | 10 seconds | HTTP `408 Request Timeout` | How long the client has to send the full set of request headers.  
  
For origin timeouts and configuration, review the [failover and timeouts](https://docs.cloud.google.com/media-cdn/docs/origins#failover-and-timeouts) section of the origin documentation.

## Client request limits

For details about client request and response limits, see the [quotas and limits](https://docs.cloud.google.com/media-cdn/quotas) documentation.

## Network protocol support

Media CDN supports HTTP/3, HTTP/2, and HTTP/1.1 connections from clients. Media CDN supports both ALPN (Application Layer Protocol Negotiation) as well as the `Alt-Svc` (alternative service) HTTP response header for advertising protocol support.

Protocol | Supported | SSL (TLS) Required  
---|---|---  
HTTP/3 (IETF QUIC) | Yes | Yes  
HTTP/2 | Yes | Yes  
HTTPS (HTTP/1.1 over TLS) | Yes | Yes  
HTTP/1.1 | Yes | No  
  
Notes:

  * HTTP/2 (h2) is supported by default.
  * To enable HTTP/3 (QUIC), please contact your account team directly.
  * HTTPS, HTTP/2, and HTTP/3 require that a valid SSL (TLS) certificate is attached to your service.
  * Clients that do not support HTTP/2 or later automatically connect over HTTP/1.1



For origin protocol support, see [supported origins and protocols](https://docs.cloud.google.com/media-cdn/docs/origins).

## Supported SSL (TLS) versions

For supported SSL (TLS) versions, see the [SSL documentation](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates).

## Troubleshoot client connectivity

  * HTTP/2 (h2) protocol is supported only for clients connecting over TLS. This protocol doesn't support plaintext connections.
  * Clients only negotiate connections they support. New protocols are designed as _opt in_ to provide backward compatibility.
  * If you have clients that have IPv6 addresses but are connecting to your Media CDN services over IPv4, it might be because the network between a Media CDN edge location and your user only supports IPv4.
  * Only HTTP/1.1 and later are supported as client protocols. HTTP/0.9 and HTTP/1.0 requests are rejected with an HTTP 426 (Upgrade Required) error.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
