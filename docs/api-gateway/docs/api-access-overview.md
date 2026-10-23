---
url: https://docs.cloud.google.com/api-gateway/docs/api-access-overview/
title: API Gateway API access overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:29.939956+00:00
---

# API Gateway API access overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/api-access-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API Gateway API access overview 

This page describes the API access control options available to you in API Gateway.

## Overview

API Gateway uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to control access to your API. You can grant access to your API at the project level and at the service consumer level. For example, you can:

  * Grant access to your API users so they can enable your API in their own Google Cloud project.
  * Allow principals to view all API Gateway resources.
  * Allow principals to create, update, or delete API Gateway resources.



## Roles that control access to services and resources

You can view and grant roles using the permissions panel on the **API Gateway** > **APIs** or **Gateways** detail pages in the Google Cloud console. Roles can also be granted using the API, or with the Google Cloud CLI.

IAM role name | Role title | Description  
---|---|---  
`roles/servicemanagement.serviceConsumer` | **Service Consumer** | Permissions for a Google Account, Google group, or service account to view and enable the API in their own project. See the [Service Management API access control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control#roles) topic for information about this role.  
`roles/apigateway.viewer` | **API Gateway Viewer** | Read-only access to an API gateway and its related resources. This role includes permissions to get and list APIs, API configs, gateways, and locations.  
`roles/apigateway.admin` | **API Gateway Admin** | Full access to an API gateway and its related resources. This role includes permissions to get, create, update, and delete APIs, API configs, gateways, and locations.  
**Note:** Although you can grant other roles at the service level, we recommend that you use the roles listed in the previous table to manage your API.

## API Gateway permissions and roles

The following table lists the project-level roles that grant access to API Gateway resources and their associated permissions:

Role | Permissions  
---|---  
**API Gateway Viewer** | apigateway.apiconfigs.get  
apigateway.apiconfigs.getIamPolicy  
apigateway.apiconfigs.list  
apigateway.apis.get  
apigateway.apis.getIamPolicy  
apigateway.apis.list  
apigateway.gateways.get  
apigateway.gateways.getIamPolicy  
apigateway.gateways.list  
apigateway.locations.get  
apigateway.locations.list  
apigateway.operations.get  
apigateway.operations.list  
resourcemanager.projects.get  
resourcemanager.projects.list  
**API Gateway Admin** | All permissions included in the **API Gateway Viewer** role, plus:  
apigateway.apiconfigs.create  
apigateway.apiconfigs.delete  
apigateway.apiconfigs.setIamPolicy  
apigateway.apiconfigs.update  
apigateway.apis.create  
apigateway.apis.delete  
apigateway.apis.setIamPolicy  
apigateway.apis.update  
apigateway.gateways.create  
apigateway.gateways.delete  
apigateway.gateways.setIamPolicy  
apigateway.gateways.update  
apigateway.operations.cancel  
apigateway.operations.delete  
**Note:** To view pages in the Google Cloud console, you must grant users the **API Gateway Viewer** role or a higher role at the project level.

## Custom roles

If basic or predefined roles do not meet your specific needs, API Gateway supports the use of custom roles. You can use IAM to create [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) for API Gateway.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
