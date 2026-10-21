---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming/
title: Streaming requests and responses \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:43.499096+00:00
---

# Streaming requests and responses  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Streaming requests and responses Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What you'll learn in this topic

After reading this topic you will know the following:

  * What request and response streaming on Apigee is
  * When to use request and response streaming
  * How to enable request and response streaming

**Sample:** If you'd like to jump directly to a code sample, see Related code samples for details.

## What is request and response streaming?

By default, HTTP streaming is disabled and HTTP request and response payloads are written to a buffer in memory before they are processed by the API proxy pipeline. You can change this behavior by enabling streaming. With streaming enabled, request and response payloads are streamed without modification to the client app (for responses) and the target endpoint (for requests). 

## When should I enable streaming?

If your API proxy handles very large requests and/or responses (for size limits, see What else should I know about streaming), you may want to enable streaming.

**Note:** If your API requests or returns a large amount of data, you may see this HTTP error: 
    
    
    {"fault":"{\"detail\":{\"errorcode\":\"protocol.http.TooBigBody\"},\"faultstring\":\"Body buffer overflow\"}"}

If you see this error, we recommend that you enable streaming. If you continue to see the error after you enable streaming, consider removing any policies that require access to the request or response payload. For more information, see [ Message payload size](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#size).

## What else should I know about streaming?

Message payload size is restricted to 30 MB. In non-streamed requests and responses, exceeding that size results in a `protocol.http.TooBigBody` error.

**Caution:** While streaming can help you work around the 30 MB request/response size limit enforced by the product, Apigee doesn't recommend exceeding that limit when streaming and can't support issues that arise as a result of exceeding that limit, such as performance issues, timeouts, and so on.

For payloads larger than 30 MB, Apigee recommends using a signed URLs pattern within an Apigee JavaCallout, illustrated by the [ Edge Callout: Signed URL Generator](https://github.com/DinoChiesa/ApigeeEdge-Java-GoogleUrlSigner) example on GitHub.

**Note:** With streaming enabled, Apigee strongly recommends you do **not** attach policies that require access to the request or response payload. Those types of policies will either cause errors or trigger buffering in the API proxy, which limits payload size to the numbers listed above and defeats the purpose of enabling streaming to handle large payloads. You can attach policies that do not interact with the request/response body, such as authentication or message logging policies.

### Encoded data

When streaming is enabled, Apigee does _not_ encode or decode request or response payloads before sending them to the client connecting to Apigee or a backend target server. See the rows for `request.streaming.enabled` and `response.streaming.enabled` in the [ TargetEndpoint Transport Property Specification](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#targetendpointtransportpropertyspecification) table for more information.

## How to enable request and response streaming

To enable request streaming you need to add the `request.streaming.enabled` property to the ProxyEndpoint and TargetEndpoint definitions in the proxy bundle and set it to `true`. Similarly, set the `response.streaming.enabled` property to enable response streaming.

You can locate these configuration files in the Apigee UI in the Develop view for your proxy. If you are developing locally, these definition files are in `apiproxy/proxies` and `apiproxy/targets`. 

This sample shows how to enable both request and response streaming in the TargetEndpoint definition.
    
    
    <TargetEndpoint name="default">
      <HTTPTargetConnection>
        <URL>http://mocktarget.apigee.net</URL>
        <Properties>
          <Property name="**response.streaming.enabled" >true**</Property>
          <Property name="**request.streaming.enabled" >true**</Property>
          <Property name="supports.http10">true</Property>
          <Property name="request.retain.headers">User-Agent,Referer,Accept-Language</Property>
          <Property name="retain.queryparams">apikey</Property>
        </Properties>
      </HTTPTargetConnection>
    </TargetEndpoint>

This example shows how to enable response and request streaming in the ProxyEndpoint definition:
    
    
    <ProxyEndpoint name="default">
      <HTTPProxyConnection>
        <BasePath>/v1/weather</BasePath>
        <Properties>
          <Property name="allow.http10">true</Property>
          <Property name="**response.streaming.enabled" >true**</Property>
          <Property name="**request.streaming.enabled" >true**</Property>
        </Properties>
      </HTTPProxyConnection>
    </ProxyEndpoint>

For more information about configuring endpoint definitions, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).

## Related code samples

API proxy samples on GitHub are easy to download and use. 

Sample proxies that feature streaming include:

  * [ streaming](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/streaming) \- Demonstrates an API proxy configured for HTTP streaming. 
  * [ Edge Callout: Signed URL Generator](https://github.com/DinoChiesa/ApigeeEdge-Java-GoogleUrlSigner) \- Illustrates the best practice of generating a signed URL to access large files instead of trying to stream them in a request/response. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
