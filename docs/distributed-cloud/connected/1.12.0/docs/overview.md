---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview/
title: Overview of connected deployments of Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:58.640706+00:00
---

# Overview of connected deployments of Google Distributed Cloud  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Overview of connected deployments of Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of connected deployments of Google Distributed Cloud, including information about when to use it and its limitations and known issues.

A connected deployment of Distributed Cloud lets you run Google Kubernetes Engine (GKE) clusters on dedicated hardware provided and maintained by either Google or a Google-certified Systems Integrator (SI) that is installed directly on your premises and connects to your local network.

Deploying workloads on a connected Distributed Cloud installation functions in a similar way to deploying workloads on cloud-based GKE clusters. After the hardware has been deployed, your cluster administrator provisions Distributed Cloud connected clusters by using the Google Cloud console or the Google Cloud CLI. In addition, your network administrator configures the Distributed Cloud networking components so that your workloads can communicate with your local network and each other. Your application owners can then deploy workloads to those clusters.

Connected deployments of Distributed Cloud support running workloads in Kubernetes containers and in virtual machines. Select hardware configurations also support GPU-based workloads.

Connected deployments of Distributed Cloud are available as either one or three standalone Distributed Cloud connected server machines that connect directly to your local network through your own network hardware.

Google remotely monitors and maintains your deployments of Distributed Cloud connected, which includes installing software updates and security patches, resolving configuration issues, and diagnosing the Distributed Cloud hardware. To resolve an issue that can't be resolved remotely, you must provide Google's or the Google-certified SI's authorized personnel physical access to the Distributed Cloud hardware.

Your Distributed Cloud connected deployment uses a secure Cloud VPN connection to access Google Cloud services and your applications that run within Google Cloud and your Virtual Private Cloud (VPC) network.

For a technical overview of connected deployments Distributed Cloud, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/how-it-works).

## When to use Distributed Cloud connected

A connected deployment of Distributed Cloud is specifically designed to address the following scenarios in which conventional Google Cloud deployments might not be sufficient:

  * Your applications require a very stable network connection between client and server, and cannot tolerate potential traffic disruptions that commonly occur when transferring data over the internet.
  * Your applications require the lowest attainable network latency and are sensitive to latency spikes or jitter. Distributed Cloud also supports high-performance network technologies for even more advanced scenarios that require the [Network function operator](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/network-function).
  * Your applications generate large amounts of data that would be performance-prohibitive or cost-prohibitive to transfer to and from Google Cloud.
  * Your local laws or regulations dictate that your data must remain on-premises and must not be stored either outside of your business or outside of a specific geographic jurisdiction.



## Limitations of Distributed Cloud connected

A Distributed Cloud connected zone has the following limitations compared to a conventional cloud-based GKE zone:

  * **Processing capacity.** Unlike a conventional cloud-based zone, your connected deployment of Distributed Cloud has limited processing capacity. Be mindful of this limitation when planning and deploying your workloads.
  * **Workload restrictions.** Distributed Cloud connected [places several restrictions on your workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#workload-limitations).



## What's next

  * [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/how-it-works)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
