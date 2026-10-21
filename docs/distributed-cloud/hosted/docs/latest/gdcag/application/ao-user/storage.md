---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/storage/
title: Storage overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:20:55.565626+00:00
---

# Storage overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Storage overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the storage options available within Google Distributed Cloud (GDC) air-gapped environments. It describes both block storage and object storage, including their characteristics and use cases. By understanding these distinct storage solutions, you'll be able to effectively plan and manage data storage for your critical applications and services in GDC air-gapped deployments.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who are responsible for selecting and managing storage solutions for their organization's projects in GDC air-gapped environments. For more information about the intended audience, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Block storage

GDC offers secure, reliable, durable, and low-latency network-based block storage that virtual machines (VMs) and containers can access like physical disks. Block storage is located independently from GDC VMs and containers, and can be preserved even after the VMs and containers are deleted. Block storage performance scales automatically with size, and can be resized to meet workload performance and space requirements. GDC block storage provides the following price and performance SKUs:

  * Balanced block storage: Solid-state drive (SSD) block storage that offers balanced performance and cost for general use.



## Object storage

Object storage, also known as object-based storage, is a computer data storage architecture designed to handle large amounts of unstructured data. Unlike other architectures, it designates data as distinct units, bundled with metadata and a unique identifier that can be used to locate and access each data unit. GDC object storage is suitable for use-cases like websites, streaming videos, and mobile apps. Data must be stored for at least 30 days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
