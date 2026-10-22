---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/sar-overview/
title: Artifact Registry overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:40.036272+00:00
---

# Artifact Registry overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/sar-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Artifact Registry overview Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry (SAR) in Google Distributed Cloud (GDC) air-gapped appliance supports and manages the GDC deployment. The GDC private Artifact Registry stores the system artifacts. There are various formats for system artifacts, such as:

  * Container images for GKE Enterprise, KubeVirt, and GDC managed services
  * Operating system (OS) images
  * Firmware formats
  * Golden virtual machine (VM) templates
  * Helm charts



Artifact Registry participates in various GDC system operations such as installation, upgrades, and the lifecycle of resources, in a secure and scalable way.

## Artifact distribution

Artifact distribution is the process of distributing artifacts between registries. Within the Artifact Registry system, there might be instances of Harbor registries that need to distribute artifacts between themselves. Use artifact distribution to perform the following actions:

  * Distribute artifacts from a Harbor registry on the bootstrapper node to a Harbor registry on the org infrastructure cluster.
  * Distribute service bundles from a Harbor registry on the org infrastructure cluster to a Harbor registry on the fleet admin cluster.
  * Pull artifacts from the source registry to a local storage and push them to the destination registry.
  * Deploy Kubernetes and Harbor using Failover registry. This registry stores the necessary container images for Kubernetes and Harbor and runs as a `systemd` service on org infrastructure nodes.



## Learn about system limits

Discover the capabilities and limits of SAR in GDC. SAR supports release artifacts for a set amount of time and has limits in place for storage capacity. Availability and uptime information about SAR is also available. For more information, see [Learn about system limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/sar-system-limits).

## Modify system artifacts

Modify system artifacts in GDC to manage and refine your deployment. To modify system artifacts, you must upload new Docker container images to the bootstrap machine or to the org infrastructure clusters. You can then use `gdcloud artifacts` commands to perform actions like managing packages, building images, patching, and optimizing your deployment. For more information, see [Modify system artifacts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/modify-system-artifacts).

## Audit changes to artifacts

Audit logs track changes and operations performed on system artifacts within the org infrastructure cluster. Use Grafana to access and view these logs. For more information, see [Audit changes to system artifacts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/audit-system-artifacts).

## Push and pull artifacts

You can manually push and pull system artifacts in GDC. Push new system artifacts when the Platform Administrator (PA) requests to enable optional features like the Database Service, or when you need to fix bugs or outages by patching with new artifacts.

GDC automatically pulls the latest artifact from Harbor. However, you might need to manually pull artifacts in some cases. For more information on these operations, see [Push and pull container images from a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/push-container-image).

## Manage SAR during an upgrade

Expand the storage capacity of the SAR in GDC. This might be necessary during an upgrade if the registry runs out of space. The process involves checking the current storage usage and increasing the storage allocation by patching the persistent volume claim. A restart of the Artifact Registry is required for the changes to take effect. For more information, see [Resize artifact registry](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/resize-artifact-registry-storage).

GDC package validation uses a root certificate authority (CA) to validate release key certificates. You must upgrade this root CA if a release notice requires it, or if you see a warning message during a system upgrade. To upgrade the certificate, see [Upgrade package validation certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/upgrade-package-validation-cert).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
