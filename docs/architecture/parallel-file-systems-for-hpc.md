---
url: https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc/
title: Parallel file systems for HPC workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:05.993482+00:00
---

# Parallel file systems for HPC workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Parallel file systems for HPC workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-19 UTC

This document introduces the storage options in Google Cloud for [high performance computing (HPC)](https://docs.cloud.google.com/solutions/hpc) workloads, and explains when to use parallel file systems for HPC workloads. In a parallel file system, several clients use parallel I/O paths to access shared data that's stored across multiple networked storage nodes.

The information in this document is intended for architects and administrators who design, provision, and manage storage for data-intensive HPC workloads. The document assumes that you have a conceptual understanding of [network file systems (NFS)](https://wikipedia.org/wiki/Network_File_System), parallel file systems, [POSIX](https://wikipedia.org/wiki/POSIX), and the storage requirements of HPC applications.

## What is HPC?

HPC systems solve large computational problems fast by aggregating multiple computing resources. HPC drives research and innovation across industries such as healthcare, life sciences, media, entertainment, financial services, and energy. Researchers, scientists, and analysts use HPC systems to perform experiments, run simulations, and evaluate prototypes. HPC workloads such as seismic processing, genomics sequencing, media rendering, and climate modeling generate and access large volumes of data at ever increasing data rates and ever decreasing latencies. High-performance storage and data management are critical building blocks of HPC infrastructure.

## Storage options for HPC workloads in Google Cloud

Setting up and operating HPC infrastructure on-premises is expensive, and the infrastructure requires ongoing maintenance. In addition, on-premises infrastructure typically can't be scaled quickly to match changes in demand. Planning, procuring, deploying, and decommissioning hardware on-premises takes considerable time, resulting in delayed addition of HPC resources or underutilized capacity. In the cloud, you can efficiently provision HPC infrastructure that uses the latest technology, and you can scale your capacity on-demand.

Google Cloud and our technology partners offer cost-efficient, flexible, and scalable storage options for deploying HPC infrastructure in the cloud and for augmenting your on-premises HPC infrastructure. Scientists, researchers, and analysts can quickly access additional HPC capacity for their projects when they need it.

To deploy an HPC workload in Google Cloud, you can choose from the following storage services and products, depending on the requirements of your workload:

Workload type | Recommended storage services and products  
---|---  
Workloads that need low-latency access to data but don't require extreme I/O to shared datasets, and that have limited data sharing between clients. | Use NFS storage. Choose from the following options:  


  * [ Filestore Zonal with a higher capacity band](https://docs.cloud.google.com/filestore)
  * [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)

  
Workloads that generate complex, interdependent, and large-scale I/O, such as tightly coupled HPC applications that use the [Message-Passing Interface (MPI)](https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report/node7.htm#Node7) for reliable inter-process communication. | Use a parallel file system. Choose from the following options:  


  * Google Cloud Managed Lustre
  * DDN Infinia
  * Sycomp Intelligent Data Storage Platform

For more information about the workload requirements that parallel file systems can support, see When to use parallel file systems.  
**Note:** For workloads that don't require low latency or concurrent write access, you can use low-cost [Cloud Storage](https://cloud.google.com/storage), which supports parallel read access and automatically scales to meet your workload's capacity requirement.

## When to use parallel file systems

In a parallel file system, several clients store and access shared data across multiple networked storage nodes by using parallel I/O paths. Parallel file systems are ideal for tightly coupled HPC workloads such as data-intensive artificial intelligence (AI) workloads and analytics workloads that use [SAS](https://www.sas.com/en_us/solutions/analytics.html) applications. Consider using a parallel file system like Managed Lustre for latency-sensitive HPC workloads that have any of the following requirements:

  * **Tightly coupled data processing** : HPC workloads like weather modeling and seismic exploration need to process data repetitively by using many interdependent jobs that run simultaneously on multiple servers. These processes typically use MPI to exchange data at regular intervals, and they use [checkpointing](https://wikipedia.org/wiki/Application_checkpointing) to recover quickly from failures. Parallel file systems enable interdependent clients to store and access large volumes of shared data concurrently over a low-latency network.
  * **Support for POSIX I/O API and for semantics** : Parallel file systems like Managed Lustre are ideal for workloads that need both the POSIX API _and_ semantics. A file system's API and its semantics are independent capabilities. For example, NFS supports the POSIX API, which is how applications read and write data by using functions like `open()`, `read()`, and `write()`. But the way NFS coordinates data access between different clients is not the same as POSIX semantics for coordinating data access between different threads on a machine. For example, NFS doesn't support POSIX read-after-write cache consistency between clients; it relies on weak consistency in NFSv3 and [close-to-open consistency](https://man7.org/linux/man-pages/man5/nfs.5.html#DATA_AND_METADATA_COHERENCE) in NFSv4.
  * **Petabytes of capacity** : Parallel file systems can be scaled to multiple petabytes of capacity in a single file system namespace. NetApp Volumes supports up to 1 PB, and Filestore Regional and Zonal support up to 100 TiB per file system. Cloud Storage offers low-cost and reliable capacity that scales automatically, but might not meet the data-sharing semantics and low-latency requirements of HPC workloads.
  * **Low latency and high bandwidth** : For HPC workloads that need high-speed access to very large files or to millions of small files, parallel file systems can outperform NFS and object storage. The sub-millisecond latency that parallel file systems provide is significantly lower than object storage, which can affect the maximum IOPS. In addition, the maximum bandwidth that's supported by parallel file systems can be orders of magnitude higher than in NFS-based systems, which can saturate a VM's NIC.
  * **Extreme client** **scaling** : NFS storage can support thousands of clients. Parallel file systems can scale to support concurrent access to shared data from over 10,000 clients _and_ can provide high throughput regardless of the number of clients.



## Examples of tightly coupled HPC applications

This section describes examples of tightly coupled HPC applications that need the low-latency and high-throughput storage provided by parallel file systems.

### AI-enabled molecular modeling

Pharmaceutical research is an expensive and data-intensive process. Modern drug research organizations rely on AI to reduce the cost of research and development, to scale operations efficiently, and to accelerate scientific research. For example, researchers use AI-enabled applications to simulate the interactions between the molecules in a drug and to predict the effect of changes to the compounds in the drug. These applications run on powerful, parallelized GPU processors that load, organize, and analyze an extreme amount of data to complete simulations quickly. Parallel file systems provide the storage IOPS and throughput that's necessary to maximize the performance of AI applications.

### Credit risk analysis using SAS applications

Financial services institutions like mortgage lenders and investment banks need to constantly analyze and monitor the credit-worthiness of their clients and of their investment portfolios. For example, large mortgage lenders collect risk-related data about thousands of potential clients every day. Teams of credit analysts use analytics applications to collaboratively review different parts of the data for each client, such as income, credit history, and spending patterns. The insights from this analysis help the credit analysts make accurate and timely lending recommendations.

To accelerate and scale analytics for large datasets, financial services institutions use Grid computing platforms such as [SAS](https://www.sas.com/en_us/solutions/analytics.html) Grid Manager. Parallel file systems like Managed Lustre support the high-throughput and low-latency storage requirements of multi-threaded SAS applications.

### Weather forecasting

To predict weather patterns in a given geographic region, meteorologists divide the region into several _cells_ , and deploy monitoring devices such as ground radars and weather balloons in every cell. These devices observe and measure atmospheric conditions at regular intervals. The devices stream data continuously to a weather-prediction application running in an HPC cluster.

The weather-prediction application processes the streamed data by using mathematical models that are based on known physical relationships between the measured weather parameters. A separate job processes the data from each cell in the region. As the application receives new measurements, every job iterates through the latest data for its assigned cell, and exchanges output with the jobs for the other cells in the region. To predict weather patterns reliably, the application needs to store and share terabytes of data that thousands of jobs running in parallel generate and access.

### CFD for aircraft design

Computational fluid dynamics (CFD) involves the use of mathematical models, physical laws, and computational logic to simulate the behavior of a gas or liquid around a moving object. When aircraft engineers design the body of an airplane, one of the factors that they consider is aerodynamics. CFD enables designers to quickly simulate the effect of design changes on aerodynamics before investing time and money in building expensive prototypes. After analyzing the results of each simulation run, the designers optimize attributes such as the volume and shape of individual components of the airplane's body, and re-simulate the aerodynamics. CFD enables aircraft designers to collaboratively simulate the effect of hundreds of such design changes quickly.

To complete design simulations efficiently, CFD applications need submillisecond access to shared data and the ability to store large volumes of data at speeds of up to 100 GBps.

## Overview of parallel file system options

This section provides a high-level overview of the options that are available in Google Cloud for parallel file systems.

### Google Cloud Managed Lustre

[Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) is a Google-managed service that provides high-throughput and low-latency storage for tightly coupled HPC workloads. It significantly accelerates HPC workloads and AI training and inference by providing high-throughput, low-latency access to massive datasets. For information about using Managed Lustre for AI and ML workloads, see [Overview of storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage). Managed Lustre distributes data across multiple storage nodes, which enables concurrent access by many VMs. This parallel access eliminates bottlenecks that occur with conventional file systems and it enables workloads to rapidly ingest and process the vast amounts of data required.

### DDN Infinia

If you need advanced AI data orchestration, you can use [DDN Infinia](https://console.cloud.google.com/marketplace/product/ddnstorage/infinia), which is available in Google Cloud Marketplace. Infinia provides an AI-focused data intelligence solution that's optimized for inference, training, and real-time analytics. It enables ultra-fast data ingestion, metadata-rich indexing, and seamless integration with AI frameworks like TensorFlow and PyTorch.

The following are the key features of DDN Infinia:

  * **High performance** : Delivers sub-millisecond latency and multiple TB/s throughput.
  * **Scalability** : Supports scaling from terabytes to exabytes and can accommodate up to 100,000+ GPUs and one million simultaneous clients in a single deployment.
  * **Multi-tenancy with predictable quality of service (QoS)** : Offers secure, isolated environments for multiple tenants with predictable QoS for consistent performance across workloads.
  * **Unified data access** : Enables seamless integration with existing applications and workflows through built-in multi-protocol support, including for Amazon S3-compatible, CSI, and Cinder.
  * **Advanced security** : Features built-in encryption, fault-domain-aware erasure coding, and snapshots that help to ensure data protection and compliance.



### Sycomp Intelligent Data Storage Platform

[Sycomp Intelligent Data Storage Platform](https://console.cloud.google.com/marketplace/product/sycomp/sycomp-intelligent-data-storage-platform), which is available in Google Cloud Marketplace, lets you run your high performance computing (HPC), AI and ML, and big data workloads in Google Cloud. With Sycomp Storage you can concurrently access data from thousands of VMs, reduce costs by automatically managing tiers of storage, and run your application on-premises or in Google Cloud. Sycomp Storage can be deployed quickly and it supports access to your data through NFS and the IBM Storage Scale client.

IBM Storage Scale is a parallel file system that helps to securely manage large volumes (PBs) of data. Sycomp Storage Scale is a parallel file system that's well suited for HPC, AI, ML, big data, and other applications that require a POSIX-compliant shared file system. With adaptable storage capacity and performance scaling, Sycomp Storage can support small to large HPC, AI, and ML workloads.

After you deploy a cluster in Google Cloud, you decide how you want to use it. Choose whether you want to use the cluster only in the cloud or in hybrid mode by connecting to existing on-premises IBM Storage Scale clusters, third-party NFS NAS solutions, or other object-based storage solutions.

## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Barak Epstein](https://www.linkedin.com/in/barakepstein1) | Product Manager
  * [Carlos Boneti](https://www.linkedin.com/in/carlosboneti) | Senior Staff Software Engineer
  * [Dean Hildebrand](https://www.linkedin.com/in/dean) | Technical Director, Office of the CTO
  * [Sean Derrington](https://www.linkedin.com/in/seanderrington) | Group Product Manager, Storage
  * [Wyatt Gorman](https://www.linkedin.com/in/wyattgorman) | HPC Outbound Product Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
