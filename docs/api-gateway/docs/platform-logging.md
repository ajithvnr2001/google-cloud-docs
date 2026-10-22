---
url: https://docs.cloud.google.com/api-gateway/docs/platform-logging/
title: Platform logs \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:31.995856+00:00
---

# Platform logs  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/platform-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Platform logs

Google Cloud offers two types of API Gateway logs:

  * [**Platform logs**](https://docs.cloud.google.com/api-gateway/docs/platform-logging)
  * [**Audit logs**](https://docs.cloud.google.com/api-gateway/docs/audit-logging)



Google Cloud services automatically generate platform logs for each API Gateway request. These logs provide visibility into request handling, authentication, and interactions with other Google Cloud services. These logs are crucial for debugging gateway errors, analyzing performance, and understanding traffic patterns. For more information about types of platform logs, see the following:

  1. **Request logs**

Each log entry represents a query served by your API Gateway. It contains useful information such as the HTTP status code, latency, response reason, request/response sizes, and more for each request.

**Log query**
         
         resource.type="apigateway.googleapis.com/Gateway"
         resource.labels.gateway_id="GATEWAY_ID"
         resource.labels.location="LOCATION"
         log_name="projects/PROJECT_ID/logs/apigateway.googleapis.com%2Frequests"

     * Where GATEWAY_ID is the name of your API Gateway instance.
     * Where LOCATION is the region where your API Gateway instance is deployed.
     * Where PROJECT_ID is your Google Cloud project ID.
  2. **JWKS queries logs**

When using [JWT Authentication](https://docs.cloud.google.com/api-gateway/docs/authenticating-users-jwt), your API Gateway will make periodic callouts to fetch the required JWKs from the specified JWKs endpoint in your API Config. These logs show useful information about successful and unsuccessful requests to your JWKs endpoint.

**Log query**
         
         resource.type="apigateway.googleapis.com/Gateway"
         resource.labels.gateway_id="GATEWAY_ID"
         resource.labels.location="LOCATION"
         log_name="projects/PROJECT_ID/logs/apigateway.googleapis.com%2Fjwks_queries"

     * Where GATEWAY_ID is the name of your API Gateway instance.
     * Where LOCATION is the region where your API Gateway instance is deployed.
     * Where PROJECT_ID is your Google Cloud project ID.
  3. **Service Control queries logs**

When your API Gateway serves traffic, it makes `check` (for verifying quota and API keys) and `report` (for metrics and logs) calls to [Google Cloud Service Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started). Only if a `check` or a `report` call fails, a `service_control_queries` log with more information is populated.

**Log query**
         
         resource.type="apigateway.googleapis.com/Gateway"
         resource.labels.gateway_id="GATEWAY_ID"
         resource.labels.location="LOCATION"
         log_name="projects/PROJECT_ID/logs/apigateway.googleapis.com%2Fservice_control_queries"

     * Where GATEWAY_ID is the name of your API Gateway instance.
     * Where LOCATION is the region where your API Gateway instance is deployed.
     * Where PROJECT_ID is your Google Cloud project ID.
  4. **Produced API logs**

In addition to logs associated with `apigateway.googleapis.com`, API Gateway also populates Produced API logs. These logs are associated with your managed service and can be used to view logs across all API Gateways implementing a specific managed service.

**Log query**
         
         resource.type="api"
         resource.labels.service="MANAGED_SERVICE"

Where MANAGED_SERVICE is the name of your managed service, which can be found by querying your API Gateway - API resource.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
