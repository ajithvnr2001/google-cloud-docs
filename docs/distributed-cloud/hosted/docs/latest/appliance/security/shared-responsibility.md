---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/security/shared-responsibility/
title: Shared responsibility model \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:29.657553+00:00
---

# Shared responsibility model  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/security/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Shared responsibility model Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance runs its administration clusters directly on the appliance bare metal servers. For maintenance and administrative purposes, you have been provided credentials for accessing these clusters as well as the underlying OS of the bare metal hosts.

Due to the lack of a strong security boundary between your workloads and the OS for the bare metal hosts, it's assumed that this model results in your workloads having access to the host OS. As a result, your workloads could potentially change OS settings, reducing overall device security. Additionally, you have access to any Google-managed applications on the appliance, with the potential to break those applications or their update mechanisms.

This is similar to the [Shared Responsibility Model](https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility) provided by GKE Enterprise products: Google provides secure binaries with secure defaults, and it's up to the customer to securely run and update them.

Component | Google's responsibilities | Customer's responsibilities  
---|---|---  
Hardware | 

  * Provide a tamper resistant device

| 

  * Restrict physical device access

  
Firmware + OS | 

  * Provide a secure OS with frequent OS and firmware updates made available for download
  * Fix security vulnerabilities in a timely manner
  * Device is shipped with initial secure OS settings
  * Access credentials for initial setup provided in a secure manner

| 

  * Review and install security updates when they are made available
  * Restrict and protect access to initial administrator credentials
  * Configure OS firewall rules as advised in initial setup and configuration documentation
  * Maintain secure settings, and/or take responsibility for any setting changes
  * Monitor device for OS security notifications, events, and alerts using GDC console

  
Workloads | 

  * Provide Google application binaries and updates
  * Provide secure Kubernetes distribution and container runtime
  * Google system software updates are made available for download

| 

  * Review and install system software updates when they are made available
  * Avoid and protect against modifying Google-provided applications, such as changing settings or stopping processes. This includes modifying or blocking any system updates
  * Monitor device for software security notifications, events, and alerts using GDC console

  
Storage | 

  * Provide a means for securely transferring data and logs to/from the device

| 

  * Monitor local device storage consumption, notifications, events, and alerts using GDC console
  * Develop and follow a process for maintaining available storage space consistent with the individual customer use case of the device
  * Set appropriate schedules for system log transfer to a customer determined centralized monitoring scheme, as required by individual customer use case
  * Configure, maintain, and restrict access credentials for data transfer tasks on the device

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
