---
url: https://docs.cloud.google.com/compute/docs/deprecations/container-startup-agent-on-compute/
title: Compute Engine container startup agent deprecation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:54.150460+00:00
---

# Compute Engine container startup agent deprecation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/deprecations/container-startup-agent-on-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine container startup agent deprecation Stay organized with collections  Save and categorize content based on your preferences. 

The _container startup agent_ (konlet) in Compute Engine was deprecated on July 21, 2025. This agent was used to deploy containers on Compute Engine instances when you create VMs or VMs in a managed instance group (MIG). To create and to run containers on VMs and MIGs, use one of the following solutions instead:

  * Run Docker container on VMs using a startup script or `cloud-init`: to run a container on a single VM or on each VM in a MIG, use one of the [Container-optimized VM images](https://docs.cloud.google.com/compute/docs/containers#container_images) and configure container using a [startup script](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#startup-scripts) or [`cloud-init`](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#cloud-init).
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview): to deploy and manage containerized applications at scale.
  * [Cloud Run](https://docs.cloud.google.com/run/docs/deploying): to run stateless container applications and small or medium jobs.
  * [Batch](https://docs.cloud.google.com/batch/docs/create-run-basic-job): to run a batch job that has a definite end state and requires additional computing resources.



For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

## Shutdown schedule

The following table lists the shutdown schedule for Compute Engine container startup agent.

Date | Event  
---|---  
**July 21, 2025** | Compute Engine container startup agent was deprecated.  
**July 31, 2026** | Compute Engine container startup agent shutdown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
