---
url: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors/
title: Troubleshooting response errors \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:39.323706+00:00
---

# Troubleshooting response errors  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Troubleshooting response errors Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors "View this page for the Cloud Endpoints gRPC docs")

This page describes how to troubleshoot errors that you receive in a response from a request to your API.

## `BAD_GATEWAY`

If you receive error code `13` and the message `BAD_GATEWAY`, this indicates that the Extensible Service Proxy (ESP) can't reach the service's backend. Check the following:

  * Make sure the backend service is running. How you do that depends on the backend. 
    * For the App Engine flexible environment, the error code for the `BAD_GATEWAY` message might be `502`. See the Errors specific to App Engine flexible environment section for more information. 
    * For Compute Engine see [Troubleshooting Cloud Endpoints on Compute Engine](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gce-deployment) for details. 
    * For GKE, you need to use SSH to access the pod and use `curl`. See [Troubleshooting Endpoints in Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment) for details. 

  * The correct IP address port of the backend service is specified: 
    * For GKE, check the ESP `--backend` flag value (the short option is `-a`) in your deployment manifest file (often called `deployment.yaml`). 
    * For Compute Engine check the ESP `--backend` flag value (the short option is `-a`) in the `docker run` command. 



## `reset reason: connection failure`

If you receive HTTP code `503` or gRPC code `14` and the message `upstream connect error or disconnect/reset before headers. reset reason: connection failure`, this indicates that ESPv2 can't reach the service's backend.

To troubleshoot, double check the items below.

### Backend Address

ESPv2 should be configured with the correct backend address. Common issues include:

  * The scheme of the backend address should match the backend application type. OpenAPI backends should be `http://` and gRPC backends should be `grpc://`.
  * For ESPv2 deployed on Cloud Run, the scheme of the backend address should be either `https://` or `grpcs://`. The `s` tells ESPv2 to set up TLS with the backend.



### DNS Lookup

By default, ESPv2 attempts to resolve domain names to IPv6 addresses. If the IPv6 resolution fails, ESPv2 falls back to IPv4 addresses.

For some networks, the fallback mechanism may not work as intended. Instead, you can force ESPv2 to use IPv4 addresses via the [`--backend_dns_lookup_family` flag](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options).

This error is common if you configure a [Serverless VPC Connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) for ESPv2 deployed on Cloud Run. VPCs do not support IPv6 traffic.

## `API is not enabled for the project`

If you sent an API key in the request, an error message like "API my-api.endpoints.example-project-12345.cloud.goog is not enabled for the project" indicates that the API key was created in a different Google Cloud project than the API. To fix this, you can either [create the API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key) in the same Google Cloud project that the API is associated with, or you can [enable the API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) in the Google Cloud project that the API key was created in.

## `Service control request failed with HTTP response code 403`

If you receive error code `14` and the message `Service control request failed with HTTP response code 403`, this indicates that the Service Control API (`servicecontrol.googleapis.com`) isn't enabled on the project.

  1. See [Checking required services](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot#checking_required_services) to make sure that all the services that Endpoints and ESP require are enabled on your project.

  2. See [Checking required permissions](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot#checking_required_permissions) to make sure that all the required permissions to the service account associated with the instance running ESP.




## `Method doesn't allow unregistered callers`

ESP responds with the error, `Method doesn't allow unregistered callers`, when you have specified an API key in the `security` section in your OpenAPI document, but the request to your API doesn't have an API key assigned to a query parameter named `key`.

If you need to generate an API key to make calls to your API, see [Creating an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

## `Method does not exist`

The response, `Method does not exist`, means that the HTTP method (`GET`, `POST`, or other) on the specified URL path wasn't found. To troubleshoot, compare the service configuration that you have deployed to make sure that the method name and URL path that you are sending in the request match:

  1. In the Google Cloud console, go to the **Endpoints Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, select the API that you sent the request to.

  3. Click the **Deployment history** tab.

  4. Select the latest deployment to see the service configuration.




If you don't see the method you are calling specified in the `paths` section of your OpenAPI document, either add the method, or add the `x-google-allow` flag at the top level of the file:
    
    
    x-google-allow: all
    

This flag means that you can avoid listing all methods supported in your backend in your OpenAPI document. When `all` is used, all calls—with or without an API key or user authentication—pass through ESP to your API. See [`x-google-allow`](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-allow) for more information.

## Errors specific to the App Engine flexible environment

This section describes error responses from APIs deployed on the App Engine flexible environment.

### Error code `502` or `503`

App Engine may take a few minutes to respond successfully to requests. If you send a request and get back an `HTTP 502`, `503`, or some other server error, wait a minute and try the request again.

### Error message `BAD_GATEWAY`

An error code `502` with `BAD_GATEWAY` in the message usually indicates that App Engine terminated the application because it ran out of memory. The default App Engine flexible VM only has 1GB of memory, with only 600MB available for the application container.

To troubleshoot error code `502`:

  1. In the Google Cloud console, go to the **Logging** page:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Select the applicable Google Cloud project at the top of the page.

  3. Select **Google App Engine Application** and open **`vm.syslog`**.

  4. Look for a log entry similar to the following:
         
         kernel: [  133.706951] Out of memory: Kill process 4490 (java) score 878 or sacrifice child
         kernel: [  133.714468] Killed process 4306 (java) total-vm:5332376kB, anon-rss:2712108kB, file-rss:0kB
         

If you see an `Out of memory` entry in the log:

     1. Add the following to your `app.yaml` file to increase the size of the default VM:
            
            resources:
              memory_gb: 4
            

     2. Redeploy your API:
            
            gcloud app deploy
            




If you have the `rollout_strategy: managed` option specified in the `endpoints_api_service` section of the `app.yaml` file, use the following command to redeploy your API:
    
    
      gcloud app deploy
    

See [Deploying your API and ESP](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend#deploying_your_api_and_esp) for more information.

## Checking the Cloud Logging logs

To use the Cloud Logging logs to help troubleshoot response errors:

  1. In the Google Cloud console, go to the **Logging** page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select the Google Cloud project.

  3. Using the drop-down menu on the left, select **Produced API** > **[YOUR_SERVICE_NAME]**.

  4. Adjust the time range until you see a row that shows your response error.

  5. Expand the JSON payload and look for `error_cause`.

     * If the `error_cause` is set to `application`, this indicates an issue in your code.

     * If the `error cause` is anything else and you are unable to fix the issue, [export the log](https://docs.cloud.google.com/logging/docs/export/configure_export#configuring_logs_export_in_the_console_name_short) and include it in any communication that you have with Google.




See the following for more information:

  * For details on the structure of the logs in the Logs Explorer, see the [Endpoints logs reference](https://docs.cloud.google.com/endpoints/docs/openapi/ref-endpoints-logs)

  * Get started using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs_viewer).

  * Use [Advanced log queries](https://docs.cloud.google.com/logging/docs/view/advanced_filters) for advanced filtering, such as getting all requests with a latency greater than 300 milliseconds.




## Issues with the example Invoke-WebRequest

In some versions of Windows PowerShell, the example `Invoke-WebRequest` in the [tutorials](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials) fails. We have also received a report that the response contained a list of unsigned bytes that had to be converted to characters. If the example `Invoke-WebRequest` didn't return the expected result, try sending the request using another application. Following are a few suggestions:

  * [Start Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) and follow the Linux steps in the tutorial that you were using to send the request.
  * Install a third-party application, such as the Chrome browser extension Postman (offered by `www.getpostman.com`). When creating the request in Postman:

    * Select `POST` as the HTTP verb.
    * For the header, select the key `content-type` and the value `application/json`.
    * For the body, enter: `{"message":"hello world"}`
    * In the URL, use the actual API key rather than the environment variable. For example:

      * On the App Engine flexible environment: `https://example-project-12345.appspot.com/echo?key=AIza...`
      * On other backends: `http://192.0.2.0:80/echo?key=AIza...`
  * Download and install [`curl`](https://curl.haxx.se/download.html), which you run in the command prompt. Because Windows doesn't handle double quotation marks nested inside single quotation marks, you have to change the `--data` option in the example to:
        
        --data "{\"message\":\"hello world\"}"
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
