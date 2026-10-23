---
url: https://docs.cloud.google.com/service-mesh/docs/managed/upgrade-clusters/
title: Best practices for upgrading clusters \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:47.117403+00:00
---

# Best practices for upgrading clusters  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/managed/upgrade-clusters/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for upgrading clusters

This page provides guidelines for keeping your managed Cloud Service Mesh cluster seamlessly up-to-date, and recommendations for creating an upgrade strategy that fits your needs and increases availability and reliability of your environments. You can use this information to keep your clusters updated for stability and security with minimal disruptions to your workloads.

## Set up multiple environments

As part of your workflow for delivering software updates, we recommend that you use multiple environments. Multiple environments help you minimize risk and unwanted downtime by testing software and infrastructure updates separately from your production environment. At minimum, you should have a production environment and a pre-production or test environment.

Consider the following recommended environments:

Environment | Description  
---|---  
Production | Used to serve live traffic to end users for mission critical business applications.  
Staging | Used to ensure that all new changes deployed from previous environments are working as intended before the changes are deployed to production.  
Testing | Used to performance benchmark, test and QA workloads against the Cloud Service Mesh release you will use in production. In this environment, you can test the upgrade of the control plane and nodes before doing so in production.  
Development | Used for active development that relies on the same version running in production. In this environment, you create fixes and incremental changes to be deployed in production.  
Canary | Used as a secondary development environment for testing newer Kubernetes releases, Cloud Service Mesh features and APIs to gain better time to market once these releases are promoted into a production ready state.  
  
## Enroll in release channels

Cloud Service Mesh often releases updates, to deliver security updates, fix known issues, and introduce new features. Managed Cloud Service Mesh [release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) offer you the ability to balance between stability and feature set. When you enroll a new cluster in a release channel, Google automatically manages the version and upgrade cadence for the cluster. Control planes and data planes are upgraded on a regular basis.

Similarly for GKE clusters on Google Cloud, we recommend enrolling the [GKE clusters in a release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more information, see [GKE release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Additionally, if you have clusters enrolled in the static channel, ensure you check the [supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms) to confirm compatibility.

To keep clusters up-to-date with the latest Cloud Service Mesh and Kubernetes updates, here are some recommended environments and the respective release channels the clusters should be enrolled in:

Environment | Release channel | Description  
---|---|---  
Production | Stable or regular | For stability and version maturity, use the stable or regular channel for production workloads.  
Staging | Same as production | To ensure your tests are indicative of the version your production will be upgraded to, use the same release channel as production.  
Testing  
Development  
Canary | Rapid | To test the latest managed Cloud Service Mesh releases against your specific configuration and feature set, and to get ahead of the curve by testing new features or APIs, use the rapid channel.  
  
## Create a continuous upgrade strategy

After enrolling your cluster in a release channel, that cluster is regularly upgraded to the version that meets the quality and stability bar for the channel. These updates include security and bug fixes, applied with increasing scrutiny at each channel:

  * Patches are pushed out to control plane and data plane in all channels gradually, accumulating soak time in rapid and regular channels before landing in the stable channel.
  * The control plane is upgraded first, followed by data plane.
  * Cloud Service Mesh will automatically roll out patches to channels based on their criticality and importance.



### Receive updates about new Cloud Service Mesh versions

Information about new versions is published to the main [Cloud Service Mesh release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes) page, as well as to an RSS feed.

## What's next

  * Learn more about [Cloud Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel).
  * Learn about [Cloud Service Mesh versioning](https://docs.cloud.google.com/service-mesh/versions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
