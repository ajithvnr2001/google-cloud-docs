---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/tls-vars/
title: Accessing TLS connection information in an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:28.632592+00:00
---

# Accessing TLS connection information in an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/tls-vars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Accessing TLS connection information in an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic explains how to access TLS connection information in flow variables for an API proxy running on Apigee or Apigee hybrid. 

## Capturing TLS connection information

During a request to an API proxy, Apigee can capture information about the TLS connection. Your API proxy can then access that information through flow variables to perform additional analysis and validation. 

The type of TLS information captured by Apigee depends on whether the Ingress is configured to support one-way or two-way TLS (only applicable with Apigee hybrid). For example, for one-way TLS, Apigee can capture information about the TLS cipher or TLS protocol used in the TLS connection. 

For two-way TLS, Apigee can capture all of the same information as captured for one-way TLS, and also capture information about the client's cert. For example, Apigee can capture the SHA1 fingerprint of the client cert and the client cert in the PEM format. 

### Capturing information for both one-way and two-way TLS

The following table lists the flow variables that contain TLS connection information captured by Apigee and Apigee hybrid, and available for access in the API proxy. 

**Flow variable** | **Description**  
---|---  
`tls.cipher` | The cipher used by the TLS connection.   
`tls.protocol` | The protocol used by the TLS connection.   
`tls.server.name` | The requested SNI server name.   
`tls.session.id` | The session identifier.   
  
### Capturing additional TLS information during two-way TLS

**Note:** Enabling mTLS only applies to Apigee hybrid.

The following table lists the flow variables that contain client cert details captured by Apigee hybrid in two-way TLS: 

**Flow variable** | **Description**  
---|---  
`tls.client.s.dn` | The subject Distinguished Name (DN) of the client cert.   
`tls.client.i.dn` | The issuer Distinguished Name (DN) of the client cert.   
`tls.client.raw.cert` | The client cert in the PEM format.   
`tls.client.cert.serial` | The serial number of the client cert.   
`tls.client.cert.fingerprint` | The SHA1 fingerprint of the client cert.   
`tls.session.id` | The session identifier.   
  
## Configuring Apigee hybrid to enable two-way TLS

To configure the ingress to request a client certificate, add the following details to the overrides file: 
    
    
    virtualhosts:
      - name: internal
        minTLSProtocolVersion: "1.2" #optional
        maxTLSProtocolVersion: "1.2" #optional
        tlsMode: MUTUAL
        sslSecret: tls-certificates

See also [Configuring TLS and mTLS on the Istio ingress](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ingress-tls). 

## Accessing the flow variables in an API proxy

From within your API proxy, you can access and inspect the TLS flow variables. For example, you can use the [AssignMessage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) or [JavaScript](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) policy to access them. 

You can also reference the flow variables in a `<Condition>` element of a proxy or target flow, or in a `<Step>` or `<RouteRule>`. For example, you could route a request to different targets based on the SN of the client. 

For more, see: 

  * [Overview of flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables)
  * [Controlling how a proxy executes with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
