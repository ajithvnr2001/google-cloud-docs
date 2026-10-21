---
url: https://docs.cloud.google.com/dataflow/docs/guides/worker-vm-hardening/
title: Worker VM security and hardening \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:53.788729+00:00
---

# Worker VM security and hardening  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/worker-vm-hardening/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Worker VM security and hardening Stay organized with collections  Save and categorize content based on your preferences. 

When you run data pipelines, maintaining a secure environment and meeting compliance requirements are critical challenges. Dataflow addresses these issues by automatically hardening and securing the virtual machines (VMs) that run your workers, which helps to protect your data and minimize security risks without manual effort.

## Dataflow worker VM operating system

Dataflow worker VMs run on a Google-maintained, hardened version of [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits). Container-Optimized OS is designed and optimized by Google for running containerized workloads securely and efficiently on Google Cloud.

Dataflow uses Container-Optimized OS as the base for Dataflow worker VMs because of its security advantages:

  * **Minimal attack surface:** Container-Optimized OS includes the minimum set of packages necessary to run containers. This reduces the potential attack surface compared to general-purpose operating systems.
  * **Security-centric design:** Container-Optimized OS is built with security as a core principle. It has a read-only file system (except for essential writeable paths), a locked-down firewall, and other secure-by-default configurations.
  * **Regular security updates:** Google's security teams continuously monitor for vulnerabilities and provide timely patches and updates to the Container-Optimized OS image. Dataflow integrates these updates into its VM images.
  * **Managed environment:** As a fully managed service, Dataflow manages the entire lifecycle of the worker VM OS. This helps to ensure consistency, reliability, and the application of security best practices across all worker VMs.



## Dataflow VM image hardening and security practices

Beyond the inherent security benefits of Container-Optimized OS, Google applies additional hardening and security practices to the Dataflow worker VM images:

  * **Vulnerability scanning:** Google regularly scans Dataflow-owned VM images and container images for known vulnerabilities by using internal vulnerability management systems that are integrated with industry-standard CVE feeds.
  * **Timely patching:** Google triages identified vulnerabilities and applies patches based on severity, adhering to defined Service Level Objectives (SLOs) and compliance programs like FedRAMP.
  * **Compliance:** Dataflow has achieved FedRAMP High certification, demonstrating adherence to stringent security standards and practices required by the US Federal government. This includes controls around vulnerability management and system hardening. For more information, see the [Google Cloud compliance offerings](https://cloud.google.com/compliance).
  * **Security bulletins:** For significant vulnerabilities requiring customer action (for example, updating a long-running streaming pipeline), Dataflow publishes [security bulletins](https://docs.cloud.google.com/dataflow/docs/security-bulletins).



## Why custom OS images aren't supported

As a managed service, Dataflow abstracts the underlying infrastructure complexity. This includes the operating system. This approach helps Google provide a highly optimized, secure, and reliable service. You can't use custom OS images (such as an in-house hardened Debian) on Dataflow workers for these reasons:

  * **Managed service integrity:** Using custom images can decrease the stability and performance of Dataflow services while introducing security risks.
  * **Direct integration:** Dataflow components are directly integrated with the specific Container-Optimized OS environment, including networking, agents, and container runtimes.
  * **Operational complexity:** Managing and supporting a wide variety of custom OS images would introduce significant operational overhead and risk.
  * **Security responsibility:** Using custom images confuses the lines of responsibility for OS-level security and patching.



For more information on the division of security responsibilities, see the [ Dataflow shared responsibility model](https://docs.cloud.google.com/dataflow/docs/resources/shared-responsibility).

## What's next

  * Read about [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).
  * Learn more about [Container-Optimized OS security](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security).
  * View [Dataflow security bulletins](https://docs.cloud.google.com/dataflow/docs/security-bulletins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
