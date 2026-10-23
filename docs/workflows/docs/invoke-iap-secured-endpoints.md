---
url: https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints/
title: Invoke an IAP-secured endpoint \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:54.119144+00:00
---

# Invoke an IAP-secured endpoint  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Invoke an IAP-secured endpoint Stay organized with collections  Save and categorize content based on your preferences. 

You can use Workflows to invoke an endpoint for which Identity-Aware Proxy (IAP) has been enabled. The endpoint can be an on‑premises, Compute Engine, Google Kubernetes Engine (GKE), or other Google Cloud endpoint.

IAP verifies identity and enforces authorization at the application level, so you can use an application-level access control model instead of relying on network-level firewalls. When an application or resource is protected by IAP, it can only be accessed through the proxy by principals who have the correct Identity and Access Management (IAM) role.

For more information, see the [IAP overview](https://docs.cloud.google.com/iap/docs/concepts-overview) and the following guides:

  * [Enable IAP for App Engine](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts)
  * [Enable IAP for Cloud Run](https://docs.cloud.google.com/iap/docs/enabling-cloud-run)
  * [Enable IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto)
  * [Enable IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto)
  * [Enable IAP for on‑premises apps](https://docs.cloud.google.com/iap/docs/enabling-on-prem-howto)



## Make an HTTP request

Calling or invoking an endpoint from Workflows is done through an HTTP request. The most common HTTP request methods have a call shortcut (such as [http.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get) and [http.post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post)), but you can make any type of HTTP request by setting the `call` field to `http.request` and specifying the type of request using the `method` field. For more information, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

## Use a service account with the required permissions

When making requests to other Google Cloud services, your workflow must be associated with a service account that has been granted one or more Identity and Access Management (IAM) roles containing the required permissions to access the requested resources. To learn what service account is associated with an existing workflow, see [Verify a workflow's associated service account](https://docs.cloud.google.com/workflows/docs/authentication#verify-service-account).

When setting up a service account, you associate the requesting identity with the resource you want to give it access to—you make the requesting identity a _principal_ , or user, of the resource—and then assign it the appropriate role. The role defines what permissions the identity has in the context of the resource. When an application or resource is protected by IAP, it can only be accessed through the proxy by principals who have the correct role.

For example, after authentication, IAP applies the relevant allow policy to check if the principal is authorized to access the requested resource. If the principal has the **IAP-secured Web App User** role (`roles/iap.httpsResourceAccessor`) on the Google Cloud console project where the resource exists, they're authorized to access the application.

You can configure access to your IAP-secured resource through the [IAP page](https://console.cloud.google.com/security/iap) by adding the Workflows service account as a principal. For more information, see [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access).

## Add authentication information to your workflow

**Note:** This authentication method is restricted to HTTPS endpoints.

By default, HTTP requests don't contain identity or access tokens for security reasons. You must explicitly add authentication information to your workflow definition. When making requests to an endpoint, use OIDC to authenticate through IAP.

To make an HTTP request using OIDC, add an `auth` section to the `args` section of your workflow's definition, after you specify the URL.

### YAML
    
    
      - step_A:
          call: http.get
          args:
              url: https://www.example.com/endpoint
              body:
                  someValue: "Hello World"
                  anotherValue: 123
              auth:
                  type: OIDC
                  audience: OIDC_AUDIENCE
        

### JSON
    
    
        [
          {
            "step_A": {
              "call": "http.get",
              "args": {
                "url": "https://www.example.com/endpoint",
                "body": {
                  "someValue": "Hello World",
                  "anotherValue": 123
                },
                "auth": {
                  "type": "OIDC",
                  "audience": "OIDC_AUDIENCE"
                }
              }
            }
          }
        ]
          

You can use the `audience` parameter to specify the OIDC audience for the token. When invoking an IAP-enabled endpoint, you must specify the OAuth 2.0 client ID that you have configured for your application. This can be obtained from the [Credentials page](https://console.cloud.google.com/apis/credentials).

## What's next

  * [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication)
  * [Access HTTP response data saved in a variable](https://docs.cloud.google.com/workflows/docs/http-requests#access-data)
  * [Invoke a private endpoint using Service Directory's service registry](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
