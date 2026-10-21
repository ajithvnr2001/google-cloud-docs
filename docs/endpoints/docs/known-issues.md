---
url: https://docs.cloud.google.com/endpoints/docs/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:47.339875+00:00
---

# Known issues  |  Cloud Endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Resources ](https://docs.cloud.google.com/endpoints/docs/release-notes)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

See the following pages for known issues with your Cloud Endpoints API implementation:

  * [Cloud Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/known-issues)
  * [Cloud Endpoints for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/known-issues)



## ESP in GKE with Istio

When the ESP is deployed in GKE with Istio, configure Istio egress gateway to [bypass the network traffic](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-control/#direct-access-to-external-services) to the following hosts:

  * metadata server: 169.254.169.254
  * service control: servicecontrol.googleapis.com
  * service management: servicemanagement.googleapis.com
  * cloudtrace: cloudtrace.googleapis.com
  * hosts specified by the field `x-google-jwk_uri` in the OpenAPI config



This issue doesn't apply to the ESPv2.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
