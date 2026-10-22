---
url: https://docs.cloud.google.com/api-gateway/docs/securing-backend-services/
title: Securing backend services \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:23.132476+00:00
---

# Securing backend services  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/securing-backend-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Securing backend services

In addition to authenticating end user requests to your deployed gateway, it is important to secure access between API Gateway and your backend services. You can prevent public access to your backend managed services (Cloud Run, Cloud Run functions, App Engine, etc.) by:

  * Permitting only authenticated access to your backend service.
  * Granting the necessary permissions to the service account associated with your gateway's API config so that your gateway is authorized to invoke the backend.



This page describes the steps required to secure your backend service and describes the roles and permissions you gateway's service account requires to access those services.

### Cloud Run

All Cloud Run fully managed services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request.

Cloud Run services are secured by IAM. By default, Cloud Run services can be called by any role containing the `run.routes.invoke` permission.

You can [configure IAM on Cloud Run (fully managed) services](https://docs.cloud.google.com/run/docs/securing/managing-access) to grant access to additional users.

For API Gateway, access to Cloud Run services is enabled by granting the gateway's service account the appropriate roles and permissions: the `roles/run.invoker` role or a role containing the `run.routes.invoke` permission.

You can control a gateway's access to an [individual service](https://docs.cloud.google.com/run/docs/securing/managing-access#controlling_access_on_an_individual_service) with service-level IAM or to [all services within a project](https://docs.cloud.google.com/run/docs/securing/managing-access#controlling_access_on_all_services_in_a_project) with project-level IAM.

If a gateway's request to your Cloud Run service is rejected, ensure that the gateway's [service account is granted](https://docs.cloud.google.com/run/docs/securing/managing-access) the `roles/run.invoker` role, and that the gateway's service account has the `run.routes.invoke` permission. Learn more about the invoker roles and permissions in the [Cloud Run IAM reference](https://docs.cloud.google.com/run/docs/reference/iam).

### Cloud Run functions

For Cloud Run functions backend services, [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs) is used to control the ability to view, create, update and delete functions. IAM enforces authentication of callers to Cloud Run functions services, such as API Gateway, by granting **roles**.

Granting roles and permissions with IAM allows for control over two sets of actions:

  * **Developer operations:** creating, updating, and deleting functions, as well as managing access to functions.
  * **Function invocation:** causing a function to be executed.



Granting the ability to invoke a function differs for [HTTP functions](https://docs.cloud.google.com/functions/docs/writing/http) and [background functions](https://docs.cloud.google.com/functions/docs/writing/background).

  * [HTTP functions](https://docs.cloud.google.com/functions/docs/writing/http) require authentication by default. You can [configure IAM on HTTP functions](https://docs.cloud.google.com/functions/docs/securing/managing-access) to specify whether a function allows unauthenticated invocation.
  * [Background functions](https://docs.cloud.google.com/functions/docs/writing/background) can only be invoked by the event source to which they are subscribed.



To enable API Gateway to call your Cloud Run functions backend service, grant the gateway's service account the [`roles/cloudfunctions.invoker`](https://docs.cloud.google.com/functions/docs/reference/iam/roles) role, or any role containing the `cloudfunctions.functions.invoke` permission.

You can control a gateway's access to [an individual function](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#controlling_access_on_a_function) with service-level IAM or to [all functions in a project](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#controlling_access_on_all_functions_in_a_project) with project-level IAM.

If a gateway's requests to your Cloud Run functions service is rejected, ensure that that the gateway's [service account is granted](https://docs.cloud.google.com/functions/docs/securing/managing-access) the `roles/cloudfunctions.invoker` role, and that the gateway's service account has the `cloudfunctions.functions.invoke` permission. Learn more about invoker roles and permissions in the [Cloud Functions IAM reference](https://docs.cloud.google.com/functions/docs/reference/iam).

### App Engine

In order to secure your App Engine app, you must use the [Identity-Aware Proxy (IAP)](https://cloud.google.com/iap/docs) to ensure that requests are authenticated.

Follow the steps to [Enable IAP](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts#enabling_iap) for the project in which your App Engine backend service is deployed. Enabling IAP will ensure that access to your App Engine backend application is secured.

To enable API Gateway to call your App Engine backend service, follow the steps in [Setting up IAP access](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts#iap-access) to grant the service account associated with your gateway the `IAP-secured Web App User` role. In addition, grant the service account a role containing the following permissions:

  * `appengine.applications.update`
  * `clientauthconfig.clients.create`
  * `clientauthconfig.clients.getWithSecret`



### Other Google Cloud APIs

API Gateway does not support proxying to other Google Cloud APIs. This means API configs that reference one or more backends with `*.googleapis.com` (such as `bigquery.googleapis.com`) will result in calls failing with a `401` response code.

API Gateway authenticates to backends with an [ID token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) while other Google Cloud APIs require an [access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens). There are no built-in workarounds at this time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
