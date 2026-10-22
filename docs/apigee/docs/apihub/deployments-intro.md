---
url: https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro/
title: API deployments overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:28.373777+00:00
---

# API deployments overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API deployments overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

A deployment is an API hub entity that describes where an API is hosted. It represents a specific runtime instance of an API, whether it's a traditional REST API, an agentic API using the Model Context Protocol (MCP), or any other style. For example, a deployment could represent an Apigee API proxy, an API deployed to Google Cloud API Gateway, or APIs deployed to other Google Cloud services or non-Google Cloud services.

You can associate an API version with multiple deployments to model scenarios such as dev, staging, user acceptance testing (UAT), and production deployments corresponding to a given version. You can also associate multiple versions with a single deployment in cases where multiple versions of an API (or potentially different APIs) are deployed together.

A deployment entity includes metadata such as name, display name, description, and associated versions. The following three attributes are required to create a deployment in API hub and specify details about the deployed API:

  * **Deployment type** : Specifies the type of deployment, such as Apigee, Apigee hybrid, Apigee Edge Private Cloud, and others.
  * **Resource URI** : A URI to the deployment resource. For example, if the deployment resource is an Apigee API proxy, then this field must specify the URI to the management user interface of the proxy. **Note:** For **Apigee** deployment types, we recommend that the Resource URI conforms to the following format: `organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)$`

For example, the Resource URI for an Apigee API proxy deployed to the `prod` environment of the `myorg` organization is `organizations/myorg/environments/prod/apis/iloveapis`. 

  * **Endpoints** : The endpoints on which the actual deployment of the API is listening to requests. For example, this field could be a list of IP addresses or hostnames.



## What's next

  * Learn how to [manage deployments](https://docs.cloud.google.com/apigee/docs/apihub/manage-deployments).
  * Learn how to [manage versions](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
