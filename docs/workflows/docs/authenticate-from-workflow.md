---
url: https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow/
title: Make authenticated requests from a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:13.820511+00:00
---

# Make authenticated requests from a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Make authenticated requests from a workflow Stay organized with collections  Save and categorize content based on your preferences. 

To make authenticated HTTP requests, your workflow must be associated with a service account (identified by its email address) that has the appropriate credentials. For more information about attaching an Identity and Access Management (IAM) service account to a workflow, and granting it the permissions required to access resources, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

## Authentication tokens

By default, HTTP requests don't contain identity or access tokens for security reasons. You must explicitly add authentication information to your workflow definition.

To authenticate between Workflows and an HTTP target that requires such authentication, Workflows uses a token in the authorization header based on the credentials of the service account attached to the workflow, and sends the token using HTTPS to the target service. When connecting with Cloud Run functions or Cloud Run, use an [ID token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) (OIDC). For APIs hosted on `googleapis.com`, use an [access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) (OAuth 2.0).

To make an authenticated request from within a workflow, do one of the following depending on the service you are calling:

  * **External APIs** —Use an `Authorization` request header to authenticate with a third-party API. In this document, see Make authenticated requests to external APIs.

  * **Google Cloud APIs** —If available, use a Workflows [connector](https://docs.cloud.google.com/workflows/docs/connectors), which automatically provides the required authentication using the workflow's service account. If you can't use a connector, use an HTTP request with OAuth 2.0 to connect with other Google Cloud APIs. Any API that ends with a hostname of `.googleapis.com` accepts this authentication method. In this document, see Make authenticated requests to Google Cloud APIs.

  * **Cloud Run functions or Cloud Run** —Use OIDC to connect with Cloud Run or Cloud Run functions. In this document, see Make requests to Cloud Run or Cloud Run functions.

  * **Private on‑premises, Compute Engine, Google Kubernetes Engine (GKE), or other Google Cloud endpoints** —Use Identity-Aware Proxy (IAP) with OIDC to enforce access control policies for your endpoints. For more information, see [Invoke an IAP-secured endpoint](https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints) and [learn how to authenticate to an IAP-secured resource from a user or service account](https://docs.cloud.google.com/iap/docs/authentication-howto).




## Make authenticated requests to external APIs

If you're integrating a third-party API, include an `Authorization` request header with the credentials necessary to carry out the authentication. For example, include an ID token in an `Authorization: Bearer ID_TOKEN` header in the request to the service. For more information, consult the API provider's documentation.

## Make authenticated requests to Google Cloud APIs

**Note:** This authentication method is restricted to HTTPS endpoints with a hostname that ends in `.googleapis.com`.

A workflow's service account can generate OAuth 2.0 tokens that the workflow can use to authenticate to any Google Cloud API. When you use this authentication method, the workflow authenticates as its associated service account. To make an HTTP request using the OAuth 2.0 protocol, add an `auth` section to the `args` section of your workflow's definition, after you specify the URL. In this example, a request is sent to the Compute Engine API to stop a VM:

### YAML
    
    
      - step_A:
          call: http.post
          args:
              url: https://compute.googleapis.com/compute/v1/projects/myproject1234/zones/us-central1-b/instances/myvm001/stop
              auth:
                  type: OAuth2
                  scopes: OAUTH_SCOPE
        

### JSON
    
    
        [
          {
            "step_A": {
              "call": "http.post",
              "args": {
                "url": "https://compute.googleapis.com/compute/v1/projects/myproject1234/zones/us-central1-b/instances/myvm001/stop",
                "auth": {
                  "type": "OAuth2",
                  "scopes": "OAUTH_SCOPE"
                }
              }
            }
          }
        ]
          

The `scopes` key is optional, but can be used to specify OAuth 2.0 scopes for the token. Replace `OAUTH_SCOPE` with a string or list of strings. Space and comma-separated strings are also supported. By default, the value is set to `https://www.googleapis.com/auth/cloud-platform`. 

## Make requests to Cloud Run functions or Cloud Run

**Note:** This authentication method is restricted to HTTPS endpoints.

When making requests to Cloud Run functions or Cloud Run, use OIDC to authenticate.

To make an HTTP request using OIDC, add an `auth` section to the `args` section of your workflow's definition, after you specify the URL. In this example, a request is sent to invoke a Cloud Run function:

### YAML
    
    
      - step_A:
          call: http.get
          args:
              url: https://us-central1-project.cloudfunctions.net/functionA
              query:
                  firstNumber: 4
                  secondNumber: 6
                  operation: sum
              auth:
                  type: OIDC
                  audience: OIDC_AUDIENCE
        

### JSON
    
    
        [
          {
            "step_A": {
              "call": "http.get",
              "args": {
                "url": "https://us-central1-project.cloudfunctions.net/functionA",
                "query": {
                  "firstNumber": 4,
                  "secondNumber": 6,
                  "operation": "sum"
                },
                "auth": {
                  "type": "OIDC",
                  "audience": "OIDC_AUDIENCE"
                }
              }
            }
          }
        ]
          

The `audience` key is optional, but can be used to specify the OIDC audience for the token. By default, `OIDC_AUDIENCE` is set to the same value as `url`. 

Note that it's possible for Workflows to invoke Cloud Run functions or Cloud Run services that have ingress restricted to internal traffic. With this configuration, your services are unreachable from the internet but can be reached from Workflows.

For more information, see [Invoke Cloud Run functions or Cloud Run](https://docs.cloud.google.com/workflows/docs/calling-run-functions).

## What's next

  * [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests)
  * [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
