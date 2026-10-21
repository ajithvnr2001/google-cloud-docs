---
url: https://docs.cloud.google.com/telecom-network-automation/docs/overview/
title: Telecom Network Automation overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:30.872795+00:00
---

# Telecom Network Automation overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Telecom Network Automation overview Stay organized with collections  Save and categorize content based on your preferences. 

Telecom Network Automation is a managed cloud implementation of [Nephio](https://docs.cloud.google.com/telecom-network-automation/docs/nephio.org), an open source project from Google and the Linux Foundation. Telecom Network Automation delivers carrier-grade, Kubernetes-based, multi-cloud, multi-vendor and built-in cloud intent automation through common automation templates.

Use Telecom Network Automation to accelerate service delivery, reduce operational processes, optimize network reliability, and enforce compliance and security requirements:

  * **Accelerate service delivery** : Deploy new services efficiently, or add capacity to a network by automating the entire network components and software stacks provision.
  * **Reduce operational processes** : Use a single interface for deploying and managing entire networks from initial configuration to continuous deployment and operations.
  * **Optimize network reliability and availability** : Test systems in the network lifecycle and reduce maintenance time. Telecom Network Automation supports the following tests and configurations: 
    * Cross-version testing.
    * Vendor-specific testing.
    * Pre-submit validations for configurations.
    * Test framework integration for a multi-stage release qualification pipeline.
  * **Adhere to compliance and security requirements** : Maintain control of system updates by reviewing audit logs for admin activity and data access.



Additionally, you can integrate Telecom Network Automation with a Google Cloud product. To learn about product integration, see the following:

  * [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview) (GDC)
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine)



## About Telecom Network Automation

Telecom Network Automation supports a declarative, intent-based mechanism of control-loop automation that addresses the imperative model with the advantages of Kubernetes and Nephio. Telecom Network Automation is a centralized solution to deploy entire telecom networks and manage them in a single place.

![TNA lifecycle shows declaring intent and the control loop](https://docs.cloud.google.com/telecom-network-automation/images/tna-overview.png)

The Telecom Network Automation architecture comprises the Kubernetes Resource Model and the Configuration as Data concept. This model and concept provide declarative capabilities and intent reconciliation, and shows what runs in an environment matches your intent.

Telecom Network Automation uses standard custom resource definitions (CRD) and pluggable Kubernetes operators. Standard CRDs alleviate interoperability issues. The Kubernetes operators are installed on a GKE cluster that behaves as the Telecom Network Automation control plane. These operators process your requests for deploying infrastructure; work through validation, automation, and reconciliation; and sync the requests to the network.

## Survivability mode

If a network disconnection between the Telecom Network Automation managed cluster and the Telecom Network Automation management plane occurs, the workload network functions and clusters created using Telecom Network Automation can continue to run. Telecom Network Automation continues to reconnect, and until it successfully reconnects, further monitoring and actuation is not possible.

Users are responsible for maintaining all the data stored on the clusters, workloads, redundant backups, electrical power supply to the Edge nodes, HVAC, physical security, local network connectivity, firewall rules and security. Telecom Network Automation requires a constant connection to Google Cloud.

![A diagram showing the service level orchestration](https://docs.cloud.google.com/telecom-network-automation/images/tna-service-orchestration.png)

Telecom Network Automation delivers zero-touch provisioning (ZTP) of cloud infrastructure which translates into increased network availability and resilience while reducing maintenance downtime. Specifically, Telecom Network Automation provides the following support and delivery measures:

  * Supports initial configuration, deployment, and continuous deployment and operation, from a single pane of glass user interface (UI).

  * Adopts the GitOps approach that provides continuous reconciliation with simplified configuration management at scale. Telecom Network Automation uses Kubernetes capabilities and supports configuration versioning, tagging, and additional capabilities such as measuring intent drift.

  * Embraces embedded continuous integration and continuous delivery. Specifically, Telecom Network Automation supports cross-version and vendor-specific testing, presubmit validation of configuration, and integrate the test framework into a multi-stage release qualification pipeline that prevent defects from going into the production environment.




Collectively, these Telecom Network Automation capabilities let CSPs in their journey to ZTP, while maintaining their ability to exercise control on system updates. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
