---
url: https://docs.cloud.google.com/run/docs/instances/instance-lifecycle/
title: Cloud Run instance lifecycle \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:46.690665+00:00
---

# Cloud Run instance lifecycle  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/instances/instance-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Cloud Run instance lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A Cloud Run instance is a single, individually manageable compute resource that runs continuously. Unlike a Cloud Run service that scales horizontally based on incoming traffic, or a job that executes defined tasks and exits, a Cloud Run instance acts as a lightweight serverless virtual machine (VM), giving you direct control over individual lifecycle states, stable ingress URLs, and continuous compute budgets.

For more details on Cloud Run instances, see the [product overview](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#cloud-run-instances) and [Cloud Run resource comparison](https://docs.cloud.google.com/run/docs/resource-model#comparison-resources).

## Cloud Run instance lifecycle

Like a VM, a Cloud Run instance moves through distinct lifecycle states and is managed through explicit, individual operations. Unlike a VM, you let Cloud Run handle the underlying compute infrastructure, host operating system, and network provisioning, retaining full Serverless ease-of-use.

The following diagram illustrates these lifecycle transitions:

![Cloud Run instances lifecycle.](https://docs.cloud.google.com/static/run/docs/images/cloud-run-instance-lifecycle.svg)**Figure 1.** The different states of Cloud Run instances.

## Lifecycle policies and restart conditions

You can define restart rules for each instance to handle process crashes and exit statements using the `restartPolicy` attribute:

  * `on-failure` (default): Restarts the container if its primary processes exit with a non-zero code, or if the container encounters system-level infrastructure failures.
  * `always`: Automatically restarts the container regardless of its exit status, including a clean exit code of `0`.
  * `never`: Does not restart the container, immediately transitioning the instance to a `STOPPED` or `FAILED` state upon process termination.



If the restart policy is enabled, Cloud Run attempts to restart a failing instance up to 3 times sequentially. If the instance continues to fail, it transitions to the `FAILED` status.

## What's next

  * [Create and manage Cloud Run instances](https://docs.cloud.google.com/run/docs/instances/create-and-manage-instances)
  * [Compare Cloud Run resources](https://docs.cloud.google.com/run/docs/resource-model#comparison-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
