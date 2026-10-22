---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure/
title: Understanding organizations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:15.544167+00:00
---

# Understanding organizations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understanding organizations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

An organization is the top-level container in Apigee. The Apigee organization contains all your API proxies and related resources. While the rest of this topic goes into more depth about organizations, here are a few practical points:

  * An Apigee organization is distinct from and subsidiary to a Google Cloud organization. When you create an organization for Apigee X or Apigee hybrid, it maps to exactly one Google Cloud _project_ , and the Apigee organization and Google Cloud project share a name. Not all Google Cloud projects have an associated Apigee organization.
  * Where the Apigee documentation uses the term "organization," it specifically refers to an Apigee organization. The Apigee documentation uses the phrase "Google Cloud organization" to refer to the alternative.
  * Once created, you cannot rename an Apigee organization.
  * Your Apigee organization name is shown as the project in the URL for the Apigee section of [the Google Cloud console.](https://console.cloud.google.com/apigee/overview) For example: 
        
        https://console.cloud.google.com/apigee/overview?project=ORG_ID

  * When you invoke REST calls to the Apigee API, the organization identifier is a required part of the path. For example, the following `curl` request returns a list of all API proxies in an organization using the [organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations): 
        
        curl https://apigee.googleapis.com/v1/organizations/ORG_ID/apis

  * While you may have created only one organization, you can be authorized in other organizations as a user or administrator with specific permissions. In the cloud console, you can switch to a different organization as described in [Switching between your organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/switch-org). 

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Watch a short video to learn how organizations support a multi-tenancy architecture for API management.

## Organization types

There are two types of organizations:

  * **Paid:** A permanent organization with full scalability. Also known as a _production_ organization. Paid organizations include those created as part of a Subscription or a Pay-as-you-go Apigee pricing model. 

  * **Evaluation:** A temporary, self-service organization for testing Apigee. Sometimes referred to as _eval orgs_ , these organizations are time-limited and lack the scalability and flexibility of production organizations.




See also [Compare eval and paid organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval). 

#### Evaluation organization lifespan

Evaluation organizations have a limited lifespan:

  1. **Day 0:** Create the evaluation organization.
  2. **Day 30:** Google sends you an email notification warning of the upcoming expiration.
  3. **Day 60:** Google deletes the evaluation organization.



## Apigee Organizations within the Google Cloud hierarchy

The following diagram shows the relationship between Apigee organizations and environments, and Google Cloud projects and folders.

![Diagram showing the Apigee organization within a Google Cloud organization hierarchy](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/organizations-and-projects.png)

## Components within an organization

The following image shows the major components of the Apigee organizational model. This model defines how your APIs, API products, apps, and app developers are all related within Apigee.

![Hierarchical diagram showing the organization as the root of an Apigee deployment.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/organization-model.png)

This model does not show all of the features of Apigee, but it is meant to show you that the organization is the root of a deployment.

The following table describes the components of the organizational model in more detail:

Component | Description  
---|---  
Organization |  Every Apigee organization belongs to exactly one Google Cloud project, and a project can contain at most one organization. An organization contains environments, API proxies, API products, API packages, apps, and users. Account holders are not limited to a single organization. Some account holders might define or be a member of multiple organizations that support different app developer communities.  
Environments and environment groups | An _environment_ is an isolated software environment, within an organization, where you [deploy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) API proxies. You can create multiple environments in an organization. An _environment group_ is a group of environments with one or more hostnames. The hostname is part of the URL used to [call API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) deployed to any environment in the environment group.  
API proxy |  An [ _API proxy_](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy) is an interface between incoming requests and backend services. The proxy entity contains the instructions and policies that Apigee executes as it processes requests from clients and responses from the backend.  
API product |  An entity for publishing APIs. API Products get published to the developer portal for consumption by external developers. An API Product presents an interface for accessing one or more published APIs. The interface (which may be described using an OpenAPI specification) may include a combination of one or more of the API requests that are handled by one or more API proxies. The users in an organization create API products. When doing so, they can attach arbitrary metadata to each API Product. One commonly-used type of metadata can define a service plan, which can specify access limits on API calls, stipulate security requirements, allow monitoring and analytics, and provide additional features. Apigee collects data for analytics on API products.  
API provider |  The person or entity that creates and manages API proxies and products. Client app developers access these published APIs.  
App Developer |  An organization contains one or more developers who build the apps that consume the APIs (published as API products) defined by your organization. Developers consume APIs but cannot create APIs or perform any other actions in the organization. Developers can be internal to your company, they can be partners, or they can be external developers who may or may not pay for access to your APIs. You can think of developers as _customers_ who use your APIs. Developers must be registered in your organization before they can register an app and receive an API key or other client credentials that allow access to your APIs. As an API provider, it is up to you to determine how to add, update, or remove developers in your organization. You can manually add them through the UI, create a developer portal to register them through a website, or define and implement your own registration mechanism by using the Apigee API.  
Apigee App (or App) |  Apigee developers create one or more client apps that consume your APIs. Developers creating client applications that call APIs requiring credential checks (such as API keys or OAuth tokens) must first create an App registration with your organization. An App registration provides the developer with the API key, a key/secret pair, or other credentials that must be used when the client application calls your APIs. Because all apps are registered in your organization, you can use Apigee to monitor and collect analytic information on the app and on its use of your APIs.  
  
Additional components of Apigee that are not shown are the API keys and OAuth tokens.

Apigee supports different types of authentication, such as a simple API key, two-legged OAuth, three-legged OAuth, and others.

If the API provider specifies API key verification as the authorization mechanism, the client application must pass an API key with every request to your APIs. If that key is valid, Apigee allows the request. Alternatively, if the API provider specifies OAuth token verification as the authorization mechanism, the client application must first obtain an OAuth token, and then pass that token with every request to your APIs. If that token is valid, Apigee allows the request. Other custom authorization schemes are possible.

As an API provider, you must define a way for developers to register their apps. Each app registration will have one or more keys or credentials associated to it. If you allow developers to register their own applications via a developer portal, the developer can retrieve the key or credential required to access your APIs, via a convenient, self-service experience.

At the time of app registration, developers can choose to access a single API product or multiple API products. A developer's app uses the same key/credential to access all API products associated with the app.

At any time, you can revoke the key so that the developer's app no longer has access to your APIs (even though the registered representation of the developer's app still exists in your organization). Or, you can revoke a developer, in which case all of the credentials for any apps registered for that developer become inoperable. Revocation is reversible. At the time Apigee creates the app credential, you can specify an expiry so that the developer must obtain a new key or credential after a specific time.

## Apigee users

Apigee users make up the organization's API team, which can include people such as administrators, API proxy and API product creators, or users monitoring analytics and other statistics. End-users are people who use the apps that Apigee developers build. In most cases, this documentation uses the term "user" to refer to an Apigee user.

Administrators can add users to an organization.

Different users can have different roles and access privileges. For example, define some users as Organization Administrators and Operations Administrators with privileges to modify the organization and its components, and define other users with permissions to create API proxies and API products, but without the privileges to modify other users.

Users can be members of multiple organizations. For example, your company might define multiple organizations on Apigee to support different developer communities, even though internally, the same people build all of the API proxies and API products and are therefore members of all of your organizations.

You don't have to create an Apigee organization to be a user. An administrator can add you to an existing organization.

In the Google Cloud console, go to the Apigee page. 

[Go to Apigee](https://console.cloud.google.com//apigee)

## Entitlements and billing

Whether the paid organization uses a **Subscription** or **Pay-as-you-go** pricing model, the items that are metered for billing purposes are: environments, API calls, and proxy deployments.

Subscription plans allow you to pre-pay for entitlements, in exchange for significant discounts. Subscription plans make sense at higher consumption volumes - where there are larger numbers of environments, a high volume of API calls, or a large number of API proxies under management by Apigee. Under the Pay-as-you-go model, you pay only for the resources you use, but you do not enjoy volume discounts.

### Subscription entitlements

Organizations |  You can enable Apigee on any Google Cloud project. Doing so creates an Apigee organization for that project. You can create as many organizations as you like. Just as there is no entitlement or charge required to create a Google Cloud project, there is no entitlement requirement to create an Apigee organization.   
---|---  
Environments |  The entitlement for Environments is expressed in units. There is a two-step process to using an environment unit entitlement: first you create an environment and then you attach that environment to an organization. An environment counts against your environment unit entitlement when the environment has been _attached_ to an organization. See [ Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#environment-and-organization) for the maximum number of environments in a single organization. You can choose to create an Apigee environment in one or more of the available [Google Cloud regions](https://cloud.google.com/docs/geography-and-regions). Each region into which an environment is mapped consumes one environment unit from your entitlement. An environment that is provisioned in a single region consumes one environment unit from your entitlement. An environment that is provisioned in two regions consumes two environment units from your entitlement. Total environment unit usage is the aggregate of the number of environment units used across all organizations. Your total environment unit entitlement is the sum of the entitlement supplied in your Subscription tier plus additional entitlement obtained via Environment Packs. Google enforces the entitlement for environments; you cannot exceed the entitlement limit. If you try to create an environment that exceeds your entitlement limit, you receive an error. You may expand your entitlement by purchasing additional Environment Packs.  
API calls |  Google counts each API call that is processed by Apigee. Your total API call entitlement is the sum of the entitlement supplied in your Subscription tier plus additional entitlement obtained via Call Packs. Under a Subscription plan, Google does not enforce the entitlement limit for API calls. If you exceed your API call entitlement, Apigee will continue to serve API calls. Google bills you for your usage over the existing entitlement. You may expand your API call entitlement at any time by purchasing additional Call Packs.  
Proxy Deployments |  Google counts each API proxy that you deploy. Your total proxy deployment entitlement is the sum of the entitlement supplied in your Subscription tier plus additional entitlement obtained via Proxy Deployment Packs. Under a Subscription plan, Google does not limit proxy deployments to your entitlement. If you deploy more proxies than your entitlement allows, thus exceeding your proxy deployment entitlement, Apigee continues to allow you to deploy new proxies, and Apigee continues to serve API calls. Google bills you for your usage over the existing entitlement. You may expand your Proxy Deployment entitlement by purchasing additional Call Packs.  
  
For more details, see [Subscription entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements). 

### Pay-as-you-go entitlements

Organizations |  You can enable Apigee on any Google Cloud project. Doing so creates an Apigee organization for that project. You can create as many organizations as you like. Just as there is no charge to create a Google Cloud project, under the Pay-as-you-go pricing model, there is no charge to create an Apigee organization.   
---|---  
Environments |  You can attach multiple environments to your Apigee organization. There is a two-step process to using an environment: first you create the environment and then you attach that environment to an organization. Google bills you for environments that are _attached_ to an organization. You may create up to 85 environments in a single organization. For multi-region environments, Google bills you for each region in which the environment is available. You can choose any of the available Google Cloud regions.  
API calls |  Google counts each API call that is processed by Apigee. Google bills you for the number of API calls your Apigee environments process. There is no limit. Apigee auto-scales and continues to serve API calls, even as load rises.   
Proxy Deployments |  Google counts each API proxy that you deploy. Google bills you for the number of deployed API proxies in your Apigee environments.  
  
For more details, see [Pay-as-you-go entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-entitlements). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
