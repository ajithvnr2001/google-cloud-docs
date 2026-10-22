---
url: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors/
title: Troubleshooting Response Errors \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:15.739870+00:00
---

# Troubleshooting Response Errors  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Troubleshooting Response Errors Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page describes how to troubleshoot errors that you receive in a response from a request to your API.

## `Upstream backend unavailable`

If you receive error code `14` and the message `upstream backend unavailable`, this indicates that the Extensible Service Proxy (ESP) can't reach the service's backend. Check the following:

  * Make sure the backend service is running. How you do that depends on the backend. 
    * For Compute Engine see [Troubleshooting Cloud Endpoints on Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment) for details. 
    * For GKE, you need to use SSH to access the pod and use `curl`. See [Troubleshooting Endpoints in Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment) for details. 

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

  1. See [Checking required services](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot#checking_required_services) to make sure that all the services that Endpoints and ESP require are enabled on your project.

  2. See [Checking required permissions](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot#checking_required_permissions) to make sure that all the required permissions to the service account associated with the instance running ESP.




## `Method doesn't allow unregistered callers`

ESP responds with the error, `Method doesn't allow unregistered callers`, when you have specified `allow_unregistered_calls: false` in your gRPC API configuration file, but the request to your API doesn't have an API key assigned to a query parameter named `key`.

If you need to generate an API key to make calls to your API, see [Creating an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

## `Method does not exist`

The response, `Method does not exist`, means that the HTTP method (`GET`, `POST`, or other) on the specified URL path wasn't found. To troubleshoot, compare the service configuration that you have deployed to make sure that the method name and URL path that you are sending in the request match:

  1. In the Google Cloud console, go to the **Endpoints Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, select the API that you sent the request to.

  3. Click the **Deployment history** tab.

  4. Select the latest deployment to see the service configuration.




## `Transport is closing`

If you receive an error code `13` and the message `transport is closing`, this indicates that ESP is unreachable.

Check the ESP error logs. How you do that depends on the backend. See the following for more information:

  * [Viewing logs on Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment#viewing_logs_on_the_vm_instance)
  * [Accessing ESP logs on GKE](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment#accessing_logs_from_extensible_service_proxy)



## Unexpected responses

If the HTTP response looks like it is binary, this might indicate that the request is hitting the API by using the `HTTP2` port when you intended to use the `HTTP1` port.

Check your port configuration options for ESP. Because the short-form flags, `-p` (for `HTTP1`) and `-P` (for `HTTP2`), look similar, we recommend that you use the long form flags instead: `--http_port` for `HTTP1` and `--http2_port` for `HTTP2`.

A misconfiguration of the ESP backend might also cause unexpected responses. Make sure the backend flag (`-a` or `--backend`) is set to a gRPC URL such as `--backend=grpc://127.0.0.1:8081`.

For more details on the ESP flags, see [ESP startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options).

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

  * For details on the structure of the logs in the Logs Explorer, see the [Endpoints logs reference](https://docs.cloud.google.com/endpoints/docs/grpc/ref-endpoints-logs)

  * Get started using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs_viewer).

  * Use [Advanced log queries](https://docs.cloud.google.com/logging/docs/view/advanced_filters) for advanced filtering, such as getting all requests with a latency greater than 300 milliseconds.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
