---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/mhs-overview/
title: Managed Harbor Service overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:05.732054+00:00
---

# Managed Harbor Service overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/mhs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Managed Harbor Service overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance Managed Harbor Service (MHS) is a fully managed service that lets you store and manage container images, even in air-gapped environments completely isolated from the internet or other networks. The GDC air-gapped appliance environment comes with a preconfigured Harbor registry called `tear-harbor` in a GDC project called `tear`. Harbor is an open source registry that secures artifacts with policies and role-based access control, ensuring images are scanned, free from vulnerabilities, and images are signed as trusted.

GDC MHS provides control-plane operations. It enables GDC MHS data-plane operations like pushing and pulling container images. Pushing your container images to a container registry solution like Harbor provides a centralized, secure, scalable, and efficient way to store, manage, and deploy your Docker images.

Harbor is a Cloud Native Computing Foundation (CNCF) graduated open source project that provides a built-in cloud container registry solution for Kubernetes and Docker. With managed service integration, you can store and manage your artifacts on GDC MHS. offers the following features:

  * Harbor instances are automatically provisioned and managed by GDC.
  * Harbor is integrated with GDC's IAM and observability systems.
  * Harbor instances can be upgraded to the newer stable version.
  * Harbor is enhanced to meet GDC's compliance and quality requirements.



## What's next

Before you can push images, begin by configuring your workspace:

  * [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects)
  * [Manage Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
