---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-x-changelog/
title: Change log for GCP_APIGEE_X \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:44.284731+00:00
---

# Change log for GCP_APIGEE_X  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-x-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_APIGEE_X

Date | Changes  
---|---  
2026-09-29 |  \- principal.url: Removed mapping of `jsonPayload.proxy.uri` from `principal.url` UDM field in order to introduce a more accurate mapping.  
\- about.url: Mapped `jsonPayload.proxy.uri` raw log field with `about.url` UDM field.  
\- principal.hostname: Removed mapping of `jsonPayload.host` from `principal.hostname` UDM field in order to introduce a more accurate mapping.  
\- principal.asset.hostname: Removed mapping of `jsonPayload.host` from `principal.asset.hostname` UDM field in order to introduce a more accurate mapping.  
\- intermediary.hostname: Mapped `jsonPayload.host` raw log field with `intermediary.hostname` UDM field.  
\- principal.ip: Newly mapped `jsonPayload.client.x-forwarded-for` raw log field with `principal.ip` UDM field.   
2024-10-16 |  Added support for cloud logging policy logs.   
2024-09-30 |  Enhancement:  
\- When `jsonPayload.responseStatusCode` is an integer then converted it to string.  
\- Converted `jsonPayload.headers.x-forwarded-proto` to uppercase and then mapped to `network.application_protocol`.  
\- Mapped `jsonPayload.headers.traceparent` to `additional.fields`.  
\- Mapped `jsonPayload.headers.tracestate` to `additional.fields`.   
2024-08-29 |  Enhancement:  
\- Mapped `jsonPayload.headers.x-apim-gateway-id`, `jsonPayload.headers.x-apigee-tracking-id`, `jsonPayload.headers.x-request-id-client-supplied`, `jsonPayload.env`, `jsonPayload.messageid`, `jsonPayload.org` to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.headers.x-apigee-tls-cipher` to `network.tls.cipher`.  
\- Mapped `jsonPayload.headers.user-agent` to `network.http.user_agent`.  
\- Mapped `jsonPayload.headers.host` to `principal.hostname`.  
\- Mapped `jsonPayload.headers.x-apigee-tls-server-name` to `network.tls.client.server_name`.  
\- Mapped `jsonPayload.headers.x-apigee-tls-protocol` to `network.tls.version_protocol`.  
\- If `jsonPayload.externalClientIp` is valid ip, then mapped to `target.ip` and `target.asset.ip` else mapped to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.responseStatusCode` to `network.http.response_code`.   
2024-07-29 |  Enhancement:  
\- Mapped `jsonPayload.consumerId`, `jsonPayload.targetResponseTime`, `jsonPayload.requestTime`, `jsonPayload.proxyRequest.headers`, `jsonPayload.proxyResponse.headers`, `jsonPayload.apigeeInstance`, `jsonPayload.customerId`, `jsonPayload.productName`, `jsonPayload.appName`, `jsonPayload.proxyBasePath`, `jsonPayload.proxyResourcePath`, `jsonPayload.consumerName`, `jsonPayload.targetRequestTime`, `jsonPayload.msgType`, `jsonPayload.apiName`, `jsonPayload.serviceAudience`, and `jsonPayload.responseTime` to `additional.fields`.  
\- Mapped `jsonPayload.targetServer` to `target.url`.  
\- Mapped `jsonPayload.resourceURL` to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.targetAudience` and `jsonPayload.targetEndpointName` to `target.resource.attribute.labels`.  
\- Mapped `jsonPayload.forwardingVMIp` to `principal.ip` and `principal.asset.ip`  
\- Mapped `jsonPayload.externalClientIp` to `target.ip` and `target.asset.ip`.   
2024-05-22 |  Promoting to default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
