---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/last-mile-security/
title: Last-mile security \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:47.900214+00:00
---

# Last-mile security  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/last-mile-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Last-mile security Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Last-mile security protects the backend services that are proxied by API Services. The primary goal of last-mile security is to prevent so-called "end-run" attacks, where an app developer discovers the URL for a backend service and bypasses any API proxies to directly hit the backend URL.

Following are the primary options for setting up last-mile security:

  * Client TLS/SSL
  * Outbound authentication



## Client TLS/SSL

The primary mechanism for securing the last-mile is client TLS/SSL, which is also known as 'mutual authentication'.

See [Options for configuring TLS](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls).

## Outbound authentication

Last-mile security can also be enforced by requiring the API proxy to present a credential to the backend service.

For example, you may wish to have an API proxy present an API key to your backend service. You could also have an API proxy obtain and present a OAuth client credentials access token.

### API key

API keys can be applied to outbound requests from API proxies to backend services. This assumes that the backend service is an API that is capable of issuing and validating API keys.

If you do set up an API proxy to present an API key on outbound requests, you must store the API key in a place where it can be retrieved by the API proxy at runtime. One location available for storing API keys is a key/value map. See [Key Value Map Operations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy).

You can use the AssignMessage policy type to add the API key as an HTTP header, query parameter, or payload element to the outbound request. See [Assign Message policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

**Best practice:** To avoid exposing API keys over network, always configure server-side TLS/SSL on your backend services for outbound transactions that use API keys

### OAuth client credentials

OAuth client credentials can be used to add a layer of revocability to API keys. If your backend services support OAuth client credentials, you can configure an API proxy to present a client credentials access token for each request.

The API proxy must be configured to perform a callout to obtain the access token from your token endpoint. The API proxy is also required to cache the access token, to prevent it from obtaining a new access token for each call.

**Warning:** Your backend services must be capable of issuing and validating access tokens using the client credentials grant type for this to work. 

Always configure server-side TLS/SSL on your backend services for transactions that use access tokens.

A number of approaches can be used to implement outbound client credentials.

**Sample:** A working outbound OAuth sample that uses client credentials is implemented in the [Outbound OAuth sample](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/outbound-oauth) on GitHub.

You can modify this sample to call your token endpoint to obtain an access token. This sample uses JavaScript to attach the token to the outbound request as an HTTP Authorization header. You could also use [Assign Message policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) for this purpose.

### SAML

The GenerateSAMLAssertion policy type can be used to attach a SAML assertion to an outbound XML request message, from the API proxy to a backend service. This enables the backend service to perform authentication and authorization on requests received from API proxies.

See [SAML assertion policies overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policies-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
