---
url: https://docs.cloud.google.com/endpoints/docs/openapi/custom-cors-nginx/
title: Creating a Custom nginx.conf to Support CORS \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:28.182527+00:00
---

# Creating a Custom nginx.conf to Support CORS  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/custom-cors-nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Creating a Custom nginx.conf to Support CORS Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx "View this page for the Cloud Endpoints gRPC docs")

As described in [Adding CORS support to ESP](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options#adding_cors_support_to_esp), you can configure the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) to support CORS. If the ESP options don't provide the CORS support that your application requires, you can add the CORS options to ESP's configuration file, `nginx.conf`.

## Adding the CORS options to `nginx.conf`

To add the CORS options:

  1. Start with a `nginx.conf` file that contains the configuration required by Cloud Endpoints. You can start with the [sample `nginx.conf`](https://github.com/GoogleCloudPlatform/endpoints-samples/blob/master/k8s/nginx.conf), or if you have already deployed ESP, you can SSH to the ESP container and copy the `nginx.conf` file from the `/etc/nginx/endpoints/` directory.

  2. Add the CORS options that your application requires to `nginx.conf`. You can use the [CORS on NGINX](https://enable-cors.org/server_nginx.html) example as a starting point.

  3. Start ESP with the `--nginx_config` option with the path to the custom `nginx.conf` file.




## What's next

  * Learn about [ESP's startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options).

  * Learn how to [SSH to ESP's container on GKE](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment#checking_configuration_files).

  * Learn about [using a custom nginx.conf on GKE ](https://docs.cloud.google.com/endpoints/docs/openapi/custom-nginx).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
