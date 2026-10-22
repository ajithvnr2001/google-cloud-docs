---
url: https://docs.cloud.google.com/artifact-registry/docs/secure-deployments/
title: Securing deployments \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:11.627858+00:00
---

# Securing deployments  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/secure-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Securing deployments Stay organized with collections  Save and categorize content based on your preferences. 

Binary Authorization is a Google Cloud service that provides deploy-time enforcement of security policies for [supported Google Cloud environments](https://docs.cloud.google.com/binary-authorization/docs/overview#supported_platforms), including [ Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs), [Cloud Run](https://docs.cloud.google.com/run/docs), and [Google Distributed Cloud](https://docs.cloud.google.com/anthos/gke/docs/on-prem). It supports container images in Artifact Registry and other container image registries.

At deploy time, Binary Authorization can use signatures called attestations to determine that a process was completed earlier. For example, you can use Binary Authorization to:

  * Verify that a container image was built by a specific build system or continuous integration (CI) pipeline.
  * Validate that a container image is compliant with vulnerability signing policy.
  * Verify that a container image passes criteria for promotion to the next deployment environment, such as development to QA.



To learn about using Binary Authorization see the [Binary Authorization documentation](https://docs.cloud.google.com/binary-authorization/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
