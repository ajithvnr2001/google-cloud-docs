---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-third-party-plugins/
title: Manage third-party plugins \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:13.032711+00:00
---

# Manage third-party plugins  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-third-party-plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage third-party plugins Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub provides out-of-the-box plugins to connect with third-party API gateways and bring your API metadata to API hub. These plugins are ready to use, and are accessible from the **API hub > Settings > Plugins** page. To use these plugins, you must create plugin instances. For more information, see [Create plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances). 

## Supported third-party plugins

The following table lists the currently supported third-party plugins, and the ingested API data. 

Plugin | API data ingested | Additional information  
---|---|---  
[Apigee Edge Public Cloud](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) | API proxy name, environment, organization, and deployment details. | For additional setup information, see [Apigee Edge API hub connector integration.](https://docs.apigee.com/api-platform/get-started/apigee-edge-uapim).  
[Apigee Edge Private Cloud (OPDK)](https://docs.cloud.google.com/https://docs.apigee.com/private-cloud) | API proxy name, environment, organization, and deployment details. | For additional setup information, see [API hub connector integration for OPDK](https://docs.apigee.com/private-cloud/v4.53.00/privatecloud-uapim-overview).  
[AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) (Preview) | REST v1 and HTTP/WebSocket v2 APIs, including versions, stages, deployments, tags, and OpenAPI specs. | Syncs every 6 hours by default. For optional real-time push sync via AWS Lambda and Amazon EventBridge, see the [apihub-plugins/aws/apigateway](https://github.com/GoogleCloudPlatform/apigee-samples/tree/main/apihub-plugins/aws/apigateway) sample.  
[Azure API Management](https://learn.microsoft.com/azure/api-management/api-management-key-concepts) (Preview) | APIs from an Azure API Management (APIM) service, including versions, operations, specs (OpenAPI, WSDL, GraphQL, gRPC, OData), gateway deployments, products, and tags. | Syncs every 6 hours by default. For optional real-time push sync via Azure Function and Azure Event Grid, see the [apihub-plugins/azure/apim](https://github.com/GoogleCloudPlatform/apigee-samples/tree/main/apihub-plugins/azure/apim) sample.  
  
## What's next

  * [Create plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
