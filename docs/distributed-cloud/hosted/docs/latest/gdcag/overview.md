---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview/
title: About Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:05.163009+00:00
---

# About Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  About Google Distributed Cloud air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud brings Google Cloud's infrastructure and services to diverse physical locations, also known as distributed environments, and can run in on-premises data centers.

Distributed Cloud offers two distinct solutions:

  * Google Distributed Cloud (GDC) connected brings Google Cloud infrastructure and services closer to where data is being generated and consumed.

  * Google Distributed Cloud (GDC) air-gapped lets you host, control, and manage infrastructure and services directly on your premises.




Google Distributed Cloud air-gapped does not require connectivity to Google Cloud and helps customers meet compliance and regulatory requirements. Key advantages of using the Distributed Cloud platform include but are not limited to the following:

  * **Open** : Leveraging open source and commercial prebuilt hardware tapping into industry innovation and open ISV ecosystem.
  * **Intelligence** : Based on the Google AI portfolio, enabling real time decisioning and automation in the platform and as a service.
  * **Consistent** : Provides a consistent application experience across Google Cloud, data centers, and Google, operator, and customer edges.
  * **Modern** : Modern Cloud approach based on Google leadership in Kubernetes and GKE Enterprise leading hybrid-cloud solution.
  * **Proven** : Leveraging proven best practices at scale and technologies used for Google services.
  * **Secure** : Security spanning Google Cloud, Google Global Network, Google Edge Infrastructure, and end-user devices.



## Prerequisites

Before deploying Distributed Cloud on your premises, Google runs a site survey to ensure your location can support GDC by validating capabilities such as space, power, cooling, and connectivity.

Based on your requirements, Google generates a solution design and provides a planning document to the cloud hardware provider that ships the required hardware to your data center.

### Hardware

Distributed Cloud hardware comes fully integrated into racks and securely delivered to your premises. We partner with OEM hardware vendors to provide customers with the latest, best-in-class enterprise equipment that is backed by comprehensive services and support. 

Distributed Cloud can run on minimal hardware to provide flexibility, availability, and performance.

### Software

In an isolated environment, you cannot download Distributed Cloud binaries directly to a network. Before deploying Distributed Cloud on an air-gapped system, it is important to have:

  * Internet access to Google Cloud to download the Distributed Cloud distribution.
  * A portable storage device to transfer the distribution to the air-gapped environment, for example, an external hard drive or a thumb drive.
  * On-premise hardware to upload the downloaded files to.
  * SHA256 or MD5 checksum to verify the integrity of the downloaded Distributed Cloud software in the air-gapped environment.
  * Nodes and clusters with enough CPU, RAM, and storage resources to meet the needs of clusters and workloads you are running regardless of your Distributed Cloud configuration.
  * Downloaded Distributed Cloud documentation to use offline.



Distributed Cloud provides a FIPS 140-2 certified Rocky Linux long-term support (LTS) operating system (OS) image that runs on Distributed Cloud bare metal servers and virtual machines. The certified OS image meets all security and compliance requirements.

## Major technical features

Distributed Cloud delivers a multitude of features that let enterprises use the full functionality of a private isolated environment with no internet access.

### Services

The extensive collection of Distributed Cloud services includes data management, artificial intelligence, machine learning, security, observability, and computing services. Distributed Cloud supports both Kubernetes and virtual machine-based workloads.

### Storage

To build a robust infrastructure and store data across an air-gapped cloud environment, Distributed Cloud provides block and object storage services. The underlying storage hardware includes high-performing all-flash solutions for block and more cost-efficient solutions for object storage.

### High availability and data backup

To conform to the data sovereignty requirements, Distributed Cloud delivers an integrated backup solution for data recovery and the ability to control data residency either in a local or remote data center.

Deploying resources across multiple data centers with [multi-zone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview) lets you run disconnected, mission critical workloads on Distributed Cloud by delivering high availability (HA) and disaster recovery (DR) capabilities similar to public hyperscale cloud providers.

Distributed Cloud enables enterprises to perform rolling non-disruptive hardware and software upgrades.

### Networking

Distributed Cloud provides secure networking and high-speed performance to support your mission critical services.

Data plane and management plane networks connect all cloud components hosted in an on-premises environment to ensure data sovereignty. The networks secure data and enable customers to scale and optimize their infrastructure.

The network load balancing service distributes TCP and UDP traffic among clusters and gives absolute control over handling traffic in the Distributed Cloud environment.

## Support

The Cloud Support API might not be available for use with Distributed Cloud. Consult your account manager for details.

## Third-party notices and source code

Third-party notices are provided with each release of GDC. They are provided using a tar file stored in the same Cloud Storage location under a matching tar file that includes `notice` in the name. Alternatively, third-party notices are provided directly in the images included in GDC.

For some of these third-party sources, we also provide copies of the source code. Third-party sources can also be found either in the images or in the following Google-hosted repositories:

  * <https://gdch-oss.googlesource.com>
  * <https://third-party-mirror.googlesource.com>



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
