---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-off-gcp/
title: Resolving Cloud Service Mesh issues for off-Google Cloud deployments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:50.880713+00:00
---

# Resolving Cloud Service Mesh issues for off-Google Cloud deployments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-off-gcp/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving Cloud Service Mesh issues for off-Google Cloud deployments

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.29/docs/getting-support).

## Failed `CONNECT` requests to HTTP proxy

For Google Distributed Cloud (software only) for VMware and Google Distributed Cloud (software only) for bare metal deployments with a ServiceEntry configured behind a corporate or otherwise private HTTP proxy, you must ensure `CONNECT` requests are configured at TCP level rather than the HTTP level. Otherwise, the `CONNECT` requests sent by the corporate proxy will fail.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
