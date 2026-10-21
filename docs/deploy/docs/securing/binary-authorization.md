---
url: https://docs.cloud.google.com/deploy/docs/securing/binary-authorization/
title: Secure deployments using Binary Authorization \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:50.662752+00:00
---

# Secure deployments using Binary Authorization  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/securing/binary-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Secure deployments using Binary Authorization Stay organized with collections  Save and categorize content based on your preferences. 

[Binary Authorization](https://docs.cloud.google.com/binary-authorization) is a Google Cloud service that provides software supply-chain security by enforcing a set of rules ([policy](https://docs.cloud.google.com/binary-authorization/docs/overview#policy_model)) on containers deployed on a Google Cloud [supported container-based platform](https://docs.cloud.google.com/binary-authorization/docs/overview#supported_platforms). The service allows or blocks deployment of these containers based on that set of rules.

Also, Binary Authorization provides [continuous validation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#overview) to ensure that each deployed container continues to conform with policy.

There is no direct integration between Cloud Deploy and Binary Authorization, but you can use them together to help secure your software delivery process.

## What Binary Authorization can do for your deployable images

At deploy time, Binary Authorization can use [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) to determine that a process was completed earlier. Here are some examples of what you can use Binary Authorization for:

  * Verify that a container image was built by a specific build system or continuous integration pipeline.

  * Validate that a container image complies with vulnerability signing policy.

  * Verify that a container image passes criteria for promotion to the next target.




## What's next

  * Learn more about how to use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) to help ensure the integrity of your container images.

  * [Try a tutorial](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli), for GKE, to configure and test a Binary Authorization policy that requires attestations.

  * Learn about the [deployment lifecycle](https://docs.cloud.google.com/binary-authorization/docs/overview#lifecycle), in the context of Binary Authorization.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
