---
url: https://docs.cloud.google.com/managed-spark/docs/resources/shared-responsibility-model/
title: Managed Service for Apache Spark shared responsibility model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:42.909540+00:00
---

# Managed Service for Apache Spark shared responsibility model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/resources/shared-responsibility-model/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback 

#  Managed Service for Apache Spark shared responsibility model Stay organized with collections  Save and categorize content based on your preferences. 

Running business-critical workloads on Managed Service for Apache Spark requires multiple parties to carry different responsibilities. While not an exhaustive list, this page lists the responsibilities for Google and the customer.

## Managed Service for Apache Spark: Google responsibilities

  * Protecting the underlying infrastructure, including hardware, firmware, kernel, OS, storage, network, and more. This includes:

    * [encrypting data at rest by default](https://docs.cloud.google.com/docs/security/encryption/default-encryption)
    * providing [additional customer-managed disk encryption](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption)
    * [encrypting data in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit)
    * using [custom-designed hardware](https://docs.cloud.google.com/docs/security/titan-hardware-chip)
    * laying [private network cables](https://cloud.google.com/about/locations#network-tab)
    * protecting data centers from physical access
    * protecting the bootloader and kernel against modification using [Shielded Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)
    * providing network protection with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)
    * following secure software development practices
  * Releasing security patches for Managed Service for Apache Spark images . This includes:

    * patches for the base operating systems included in [Managed Service for Apache Spark images](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters) (Ubuntu, Debian, and Rocky Linux)
    * patches and fixes available for the [open source components](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1) included in Managed Service for Apache Spark images Security patches may only be available for operating system versions or open source software that are included in the most recent version of Managed Service for Apache Spark images. Leveraging the latest Managed Service for Apache Spark image version available is a customer responsibility.
  * Providing Google Cloud integrations for Connect, Identity and Access Management, Cloud Audit Logs, Cloud Key Management Service, Security Command Center, and others.

  * Restricting and logging Google administrative access to customer clusters for contractual support purposes with [Access Transparency](https://cloud.google.com/security/products/access-transparency) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)

  * Recommending best practices for configuring Managed Service for Apache Spark and the open source components included in Managed Service for Apache Spark images




## Managed Service for Apache Spark: Customer responsibilities

  * Maintaining your workloads, including your application code, custom images, data, IAM policy, and clusters that you run

  * Running clusters on up-to-date Managed Service for Apache Spark images by leveraging the latest [subminor image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#debian_images), promptly refreshing your custom images, and migrating to the most recent minor image version as soon as it is feasible. Image metadata includes a `previous-subminor` label, which is set to `true` if the cluster is not using the latest subminor image version. For information on how to view image metadata, see [Important notes about versioning](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview#important_notes_about_versioning).

  * Providing Google with environmental details when requested for troubleshooting purposes

  * Following best practices for the configuration of Managed Service for Apache Spark and other Google Cloud services, and for the configuration of open source components included in Managed Service for Apache Spark images




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
