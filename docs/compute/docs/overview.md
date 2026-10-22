---
url: https://docs.cloud.google.com/compute/docs/overview/
title: Compute Engine overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:45.840436+00:00
---

# Compute Engine overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine overview Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine is an infrastructure as a service (IaaS) product that offers self-managed virtual machine (VM) instances and bare metal instances. Compute Engine offers VMs with a KVM hypervisor, operating systems for both Linux and Windows, and durable storage options. You can configure and control Compute Engine resources using the Google Cloud console, the Google Cloud CLI, or using a REST-based API. You can also use a variety of programming languages available with Google's [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries). 

Here are some of the benefits of using Compute Engine:

  * **Extensibility:** Compute Engine integrates with Google Cloud technologies such as Cloud Storage, Google Kubernetes Engine, and BigQuery, to extend beyond the basic computational capability to create more complex and sophisticated applications.
  * **Scalability:** Scale the number of compute resources as needed without having to manage your own infrastructure. This is useful for businesses that experience sudden increases in traffic, because you can quickly add more instances to handle the increase and remove the instances after they are no longer needed.

  * **Reliability:** The minimum uptime SLO for Compute Engine is 99.5%. The uptime SLO varies depending on the regions and Network Service Tiers that you choose and the deployment configurations. For more information, see [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla). 

  * **Cost-effectiveness:** Compute Engine offers a variety of pricing options to fit your budget. Also, you only pay for the resources that you use, and there are no up-front costs. 




## What Compute Engine provides

Compute Engine provides flexibility so that you can run a wide-range of applications and workloads that support your needs. From batch processing to webserving or high performance computing you can configure Compute Engine to meet your needs.

### Location selection

Google offers worldwide regions for you to deploy Compute Engine resources. You can choose a region that best fits the requirements of your workload:

  * Region-specific restrictions
  * User latency by region
  * Latency requirements of your application
  * Amount of control over latency
  * Balance between low latency and simplicity



For more information about regions and zones, see [About regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

### Compute Engine machine types

Compute Engine provides a comprehensive set of machine families, each containing machine types to choose from when you create a compute instance. Each machine family is comprised of machine series and predefined machine types within each series.

Compute Engine offers general-purpose, compute-optimized, network-optimized, storage-optimized, memory-optimized, and accelerator-optimized machine families. 

If a preconfigured, general-purpose machine type doesn't meet your needs, then you can create a custom machine type with customized CPU and memory resources for some of the machine series. 

For more information, see the [Machine families resource guide](https://docs.cloud.google.com/compute/docs/machine-resource).

### Operating systems

Compute Engine provides many preconfigured public operating system images for both Linux and Windows.

Most public images are provided for no additional cost, but there are some [premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) for which you are billed. You are not billed for importing custom images, but you will incur an [image storage charge](https://docs.cloud.google.com/compute/disks-image-pricing#imagestorage) while you keep the custom image in your project. 

### Storage options

You can choose from several block storage options, including Google Cloud Hyperdisk, Local SSD, and Persistent Disk.

  * **Local SSD:** Physical drives that offer the best performance, but are not durable. If you stop the instance, the data on the Local SSD disks that are attached to the instance is lost. Local SSD disks are attached directly to the same server as the compute instance.

  * **Hyperdisk:** The fastest durable storage for Compute Engine. Data on Hyperdisk volumes is preserved even if you stop the instance. Hyperdisk volumes offer configurable performance and can be resized dynamically. You can also reduce costs and disk management complexity by purchasing capacity and performance in advance with Hyperdisk Storage Pools.

  * **Persistent Disk:** If you need durable storage for a machine series that doesn't support Hyperdisk, then use Persistent Disk. Persistent Disk provides fast durable block storage that is preserved even if you stop the instance.




Each option has unique pricing and performance. For more information about disks in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

For cost comparisons, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk). 

## What's next

  * See the [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms) and [GPUs](https://docs.cloud.google.com/compute/docs/gpus) that are available for your use.
  * Read an [overview of networking capabilities](https://docs.cloud.google.com/compute/docs/networking/network-overview).
  * Learn about the various [deployment strategies](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
