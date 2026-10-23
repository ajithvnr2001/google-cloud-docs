---
url: https://docs.cloud.google.com/workflows/docs/calling-run-functions/
title: Invoke Cloud Run functions or Cloud Run \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:02.835326+00:00
---

# Invoke Cloud Run functions or Cloud Run  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/calling-run-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Invoke Cloud Run functions or Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Calling or invoking a Google Cloud service such as Cloud Run functions or Cloud Run from Workflows is done through an HTTP request. The most common HTTP request methods have a call shortcut (such as [http.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get) and [http.post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post)), but you can make any type of HTTP request by setting the `call` field to `http.request` and specifying the type of request using the `method` field. For more information, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

**Note:** Invoking a Google Cloud service through an HTTP request should not be confused with using Workflows [connectors](https://docs.cloud.google.com/workflows/docs/connectors) to perform API operations with other Google Cloud products.

#### To send authenticated requests:

  * Your workflow must be associated with a service account that has been granted one or more Identity and Access Management (IAM) roles containing the required permissions.

  * You must explicitly add authentication information to your workflow definition. By default, HTTP requests do not contain identity or access tokens for security reasons.




For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

## When to call a service

How do you know when to create steps in YAML or JSON using the Workflows syntax or when to create a service—for example, a Cloud Run service or a Cloud Run function—to do the work instead? 

Create services to do any work that is too complex for Workflows; for example, implementing reusable business logic, complex computations, or transformations that are not supported by Workflows expressions and its standard library. A complicated case is typically easier to implement in code, instead of using YAML or JSON and the Workflows syntax. 

## Invoke services that are restricted to internal ingress

Workflows can invoke Cloud Run functions or Cloud Run services in the same Google Cloud project that have ingress restricted to internal traffic. With this configuration, your services are unreachable from the internet but can be reached from Workflows.

To apply these restrictions, you must adjust the ingress settings of your service or function. Note that the Cloud Run service must be reached on its `run.app` URL and not at a custom domain. For more information, see [Restrict network ingress](https://docs.cloud.google.com/run/docs/securing/ingress) (for Cloud Run) and [Configure network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings) (for Cloud Run functions). No other changes are needed to your workflow.

## Use a service account with the required permissions

When making requests to other Google Cloud services, your workflow must be associated with a service account that has the correct permissions to access the requested resources. To learn what service account is associated with an existing workflow, see [Verify a workflow's associated service account](https://docs.cloud.google.com/workflows/docs/authentication#verify-service-account).

When setting up a service account, you associate the requesting identity with the resource you wish to give it access to—you make the requesting identity a **principal** of the resource—and then assign it the appropriate [role](https://docs.cloud.google.com/iam/docs/understanding-roles). The role defines what permissions the identity has in the context of the resource.

For example, to configure a receiving Cloud Run function to accept requests from a specific calling function or service, you need to add the caller's service account as a principal on the receiving function and grant that principal the Cloud Run functions Invoker (`roles/cloudfunctions.invoker`) role. Similarly, to set up a service account for Cloud Run, you grant that service account the Cloud Run Invoker (`roles/run.invoker`) role. To learn more, see [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) or the [Cloud Run authentication overview](https://docs.cloud.google.com/run/docs/authenticating/overview).

### Invoke Cloud Run functions

In Cloud Run functions, invocation permissions are available by managing the underlying Cloud Run service. If your workflow is invoking a Cloud Run functions service, you don't need to grant the caller's service account the Cloud Functions Invoker (`roles/cloudfunctions.invoker`) role. Instead, you must grant the Cloud Run Invoker (`roles/run.invoker`) role.

For more information, see [Compare Cloud Run functions](https://docs.cloud.google.com/run/docs/functions/comparison).

## Add authentication information to your workflow

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
          

The `audience` parameter can be used to specify the OIDC audience for the token. By default, it's set to the same value as `url`; however, it should be set to your service's root URL. For example: `https://region-project.cloudfunctions.net/hello_world`. 

## Specify the media type for the response data

If the `Content-Type` header for the response specifies an `application/json` media type, the JSON response that is stored in a variable is automatically converted to a map that can be accessed.

If necessary, modify the API that is being called to specify an `application/json` media type for the `Content-Type` response header. Otherwise, you can use the [`json.decode`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode) and [`text.encode`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/encode) functions to convert the response body into a map. For example:
    
    
    json.decode(text.encode(RESPONSE_FROM_API))
    

For more information, see [Access HTTP response data saved in a variable](https://docs.cloud.google.com/workflows/docs/http-requests#access-data).

## Execute Cloud Run jobs

Unlike Cloud Run services, [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs) do not listen for or serve HTTP requests. To execute Cloud Run jobs from a workflow, use the [Cloud Run Admin API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/Overview).

For an end-to-end example of executing a Cloud Run job that processes data passed as environment variables to the job, see [Execute a Cloud Run job using Workflows](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs).

For an end-to-end example of executing a Cloud Run job that processes data stored in a Cloud Storage bucket allowing you to encrypt the data using customer-managed encryption keys (CMEK), see [Execute a Cloud Run job that processes event data in Cloud Storage](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs-stored-events).

## What's next

  * [Invoke with an HTTPS Request](https://docs.cloud.google.com/run/docs/triggering/https-request)
  * [Use Workflows with Cloud Run and Cloud Run functions tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/run/cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
