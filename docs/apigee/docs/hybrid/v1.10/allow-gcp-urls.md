---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/allow-gcp-urls/
title: Google Cloud URLs to allow for Hybrid \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:26.484875+00:00
---

# Google Cloud URLs to allow for Hybrid  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/allow-gcp-urls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Google Cloud URLs to allow for Hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/allow-gcp-urls.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/allow-gcp-urls.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/allow-gcp-urls.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/allow-gcp-urls.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/allow-gcp-urls.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/allow-gcp-urls.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/allow-gcp-urls.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/allow-gcp-urls.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/allow-gcp-urls.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/allow-gcp-urls.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/allow-gcp-urls.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/allow-gcp-urls.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/allow-gcp-urls.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/allow-gcp-urls.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/allow-gcp-urls.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/allow-gcp-urls.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/allow-gcp-urls.html)



If you have a restricted VPC environment where external domains need to be allowed, here is a list of Google Cloud urls that Apigee hybrid may need to connect with during install and runtime.

## Google Cloud URLs for all Apigee hybrid installations

These URLs are used by all Apigee hybrid installations:

URL | Description  
---|---  
apigee.googleapis.com | The runtime uses these APIs to learn which proxies, shared flows, etc., it should deploy, and to report its current configuration and health.  
apigeeconnect.googleapis.com | This APIs is needed for apigee-mart-server and apigee-connect communication when you have vpc-sc enabled to talk to the control plane.  
binaryauthorization.googleapis.com | Optional. Only for Anthos if [binary authorization](https://docs.cloud.google.com/binary-authorization) is enabled  
gcr.io | Contanier images are hosted in Google Container Registry.  
iamcredentials.googleapis.com | Required for generating access tokens used by other Google Cloud API calls. For example, for runtime to make calls to download runtime contracts from apigee.googleapis.com, the permission is granted by a service account. So the runtime needs to get an access token before making the call to apigee.googleapis.com.  
logging.googleapis.com | This API is needed for the logging agent to send logs to Cloud Logging.  
monitoring.googleapis.com | Cloud Monitoring service endpoint to export metrics.  
oauth2.googleapis.com | Authentication and authorization  
pubsub.googleapis.com | The runtime subscribes to a pubsub topic to learn when to initialize debug sessions.  
serviceusage.googleapis.com | Inspect and manage quota for service consumers on Google Cloud Platform. Required by Anthos Service Mesh  
storage.googleapis.com | The runtime downloads proxies, shared flows, resource files, and keystore aliases from Google Cloud Storage in tenant project.  
sts.googleapis.com | The Security Token Server providers API method for third party developers to exchange third party credentials to Google Cloud Platform tokens.  
www.googleapis.com | Needed for installing Apigee hybrid on Anthos.  
  
##  Google Cloud URLs for Anthos installations 

All Apigee hybrid installations on Anthos (on-prem and multi-cloud) use additional Google Cloud URLs. For more information, see:

  * [Proxy and firewall rules for Anthos on-prem](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/firewall-rules)
  * [Proxy allowlist for Anthos multi-cloud](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/how-to/use-a-proxy#proxy_allowlist_2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
