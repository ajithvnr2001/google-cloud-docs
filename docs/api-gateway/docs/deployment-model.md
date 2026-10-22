---
url: https://docs.cloud.google.com/api-gateway/docs/deployment-model/
title: API Gateway Deployment Model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:17.381447+00:00
---

# API Gateway Deployment Model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/deployment-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API Gateway Deployment Model

## About API components

An API defined on API Gateway consists of two main components:

  1. **API config** : The API configuration created when you upload an **API definition**. You create the API definition as an OpenAPI spec. If your API manages gRPC services on Cloud Run, you can define your API with a gRPC service definition and configuration.

Each time you upload an API definition, API Gateway creates a new API config. That is, you can create an API config but you cannot later modify it. If you later edit the API definition in the OpenAPI spec or gRPC service definition, and then upload the edited API definition, you create a new API config.

  2. **Gateway** : An [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based, high-performance, scalable proxy that hosts the deployed API config. Deploying an API config to a gateway creates the external facing URL that your API clients use to access the API.




The following image shows these components:

![The API definition on the API Gateway pane shows three API config components and three gateway components.](https://docs.cloud.google.com/static/api-gateway/docs/images/api-def-components.svg)

## About API config deployment to a gateway

You deploy an _API config_ to a _gateway_ to make your API accessible to your API clients:

![In three sample
APIs, an API config is deployed to a gateway, making the APIs accessible to the API clients.](https://docs.cloud.google.com/static/api-gateway/docs/images/concepts-deploy-single-gw.svg)

A gateway:

  * Is deployed to a specific Google Cloud [region](https://cloud.google.com/about/locations/). A region is a specific geographical region on Google Cloud where you can deploy resources.

  * Must host an API config. You cannot create an empty gateway, meaning one without an API config. However, after a gateway is created, you can update the gateway to replace one API config with another.

  * Can only host a single API config. You cannot deploy multiple API configs to the same gateway.




You then manage each deployed gateway separately. For each gateway, you can:

  * Start/stop/delete the gateway
  * View logs and metrics
  * View trace information



## Choose a Google Cloud region

Each gateway is deployed to a specific geographical [region](https://cloud.google.com/about/locations/) on Google Cloud. API Gateway supports the following Google Cloud regions for deployment:

  * `asia-northeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `us-east1`
  * `us-east4`
  * `us-central1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



## Define the endpoint of the deployed API config

When you deploy an API config to a gateway, API Gateway creates a unique URL for the gateway in the `gateway.dev` domain. Your API clients then use a URL in the following form to access the deployed API config:
    
    
    https://GATEWAY_ID-HASH.REGION_CODE.gateway.dev
    

where GATEWAY_ID is the name of the gateway HASH is the unique hash code generated when you deployed the API, and REGION_CODE is the code for the [Cloud location](https://cloud.google.com/about/locations/) where you deployed the gateway.

For example:
    
    
    **my-gateway** -**a12bcd345e67f89g0h**.**uc**.gateway.dev
    

**Note:** Gateways that use model routing can instead get a hostname in a second `gateway.dev` format, for example `https://my-gateway-123456789012.us-central1.gateway.dev`. Gateways created earlier keep their existing hostname, which for model routing is a `run.app` hostname. See [Configure model routing](https://docs.cloud.google.com/api-gateway/docs/model-routing-configure) for details.

## Configure a service account to deploy API configs

An API config deployed on a gateway executes with the permissions associated with the roles granted to the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) used to create the API config. Therefore, you typically define a separate service account for creating API configs. That service account is then assigned only to the roles necessary to access the backend service. In this way, you can limit the permissions associated with the API config.

In addition to the roles necessary to access the backend service, the service account is required to be granted the following permissions:

  * The `iam.serviceAccounts.actAs` permission. This permission is included in the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) role.

  * The permissions necessary to access your backend service. For example, if your backend is implemented as a Cloud Function, then the service account should at the least be assigned to the role of **Cloud Functions Invoker**. For a Cloud Run backend, the role is **Cloud Run Invoker**. By limiting the permissions associated with the API config, you can better secure your backend systems.




See [Configure your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env) for more.

## About scale to zero

API Gateway is a _scale-to-zero_ service. That means when there is no traffic, all gateway instances are deleted. When traffic increases, new instances are created on demand to handle the load. Scale-to-zero is controlled automatically by Google Cloud; you are not required to configure or manage it.

## Use a load balancer

Each gateway deployed in a region contains an integrated load balancer to manage client requests to the API deployed to the gateway. You are not required to create a separate load balancer for each gateway.

You do have to create a load balancer when you deploy the same API on gateways located in different regions. The load balancer then directs API requests to the different regions. See Deploy an API to multiple regions for more.

## Configure SSL access to an API

API Gateway supports HTTPS access to an API deployed to a gateway. Because your APIs are deployed to the `gateway.dev` domain, Google creates and manages the SSL cert on the load balancer integrated with the gateway. You don't have to create or upload your own cert.

## Configure a Domain Name Server

By default, API clients make requests to a `gateway.dev` domain to access a deployed API, as shown above.

Custom domain names are for API Gateway when used in conjunction with HTTP(S) Load Balancing for API GatewayPREVIEW. To customize the domain name, create a load balancer to use your custom domain name and then direct requests to the `gateway.dev` domain of your deployed API. For more information, see [Use a custom domain with API Gateway](https://docs.cloud.google.com/api-gateway/docs/using-custom-domains).

## Deploy multiple API configs in the same API

You can only deploy a single API config to a gateway. However, you can deploy multiple API configs to multiple gateways within the same API.

This section describes two scenarios where you might deploy multiple API configs on multiple gateways within a single API.

### Deploy API configs to multiple gateways in the same region

When building an API, API developers often create development, staging, and production environments, where:

  * The **development** environment is used by developers to create the API.
  * The **staging** environment is used to test the API in preparation for a release to production.
  * The **production** environment is where your external API clients are allowed to access the API.



To support this type of development environment, you define multiple API configs. For example, you might have several API configs in development, one API config being tested on staging, and one API config deployed to production API Gateway lets you create multiple API configs within a single API, and then deploy each API config to different gateway:

![In API 1, three
API configs called API Config Dev, API Config Stage, and API Config Prod are
deployed to three respective gateways.](https://docs.cloud.google.com/static/api-gateway/docs/images/concepts-multiconfig-gw.svg)

In this example, you have three different API configs: **dev** , **stage** , and **prod**. You then deploy each API config to a different gateway, where each gateway defines its own unique endpoint URL.

### Deploy an API config to multiple regions

Often you deploy an API to multiple Google Cloud regions. Deploying in multiple regions offers several advantages, including reduced request latency because requests are directed to an API running in a region geographically close to the client, and improved reliability because a failure in one region does not affect APIs running in other regions.

**Note:** Before you can deploy an API to a region, you must first deploy the backend service to that region. That is, you wouldn't create an API in one region that makes requests to a backend service in a different region. Therefore, if you want to deploy an API to three regions, you first deploy the backend service to those three regions.

To deploy an API to multiple regions, you deploy an API config to a gateway in each region. Each API config is specific to the deployed region because it has to reference the backend service in that region.

In the following image, APIs 1 and 2 are deployed to a single region and API 3 is deployed across multiple regions:

![API 1 and API 2 are
deployed to Region 1, and API 3 is deployed across Region 1, Region 2, and
Region 3 using a load balancer.](https://docs.cloud.google.com/static/api-gateway/docs/images/concepts-multiregion.svg)

In this example, each API config deployed to a gateway for API 3 has a unique URL endpoint, in the form:
    
    
    https://my-gateway1-a12bcd345e67f89g0h.uc.gateway.dev
    https://my-gateway2-b12cde345f67g89h0i.en.gateway.dev
    https://my-gateway3-c12bde345g67h89i0j.uw.gateway.dev
    

You then configure a load balancer using HTTP(S) Load Balancing for API GatewayPREVIEW to handle requests to the API and forward the request to the appropriate region. For more information, see [Create multi-region deployments for API Gateway](https://docs.cloud.google.com/api-gateway/docs/multi-region-deployment).

## Update an API

You can update a deployed API by editing the API definition in the OpenAPI spec, and then uploading the spec. Uploading a new spec creates a new API config.

**Note:** Each time you upload an API definition, API Gateway creates a new API config. After creating the new API config, deploy it to a gateway to make it accessible to your API clients.

API Gateway supports a zero-downtime update model, which means your API continues to handle requests during the deployment of the updated API config. However, there is a period of time while the new API config is being deployed when some requests might still be handled by the previous version of the API config.

If you have deployed the API config across multiple regions and gateways, you have to redeploy the updated API config in each region separately.

## What's next

  * [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
