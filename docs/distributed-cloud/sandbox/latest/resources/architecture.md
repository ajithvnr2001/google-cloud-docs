---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/architecture/
title: Architecture \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:11.936595+00:00
---

# Architecture  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)
  * [ Resources ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/release-notes)



Send feedback 

#  Architecture Stay organized with collections  Save and categorize content based on your preferences. 

GDC Sandbox simulates the physical and network environment of a Google Distributed Cloud (GDC) air-gapped physical installation, using virtual machines and other Google Cloud services.

The GDC Sandbox platform consists of the following components:

  1. Admin clusters used to deploy the GDC components
  2. Components that provide Block and Object Storage
  3. Kubernetes clusters with worker nodes to run customer workloads
  4. A gateway VM that users connect to using Google Cloud authentication and Cloud IAP



![Architecture of the sandbox](https://docs.cloud.google.com/static/distributed-cloud/sandbox/latest/images/sandbox-arch.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
