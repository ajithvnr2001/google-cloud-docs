---
url: https://docs.cloud.google.com/oracle/compute/overview/
title: Oracle on Google Cloud Compute overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:52.233242+00:00
---

# Oracle on Google Cloud Compute overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Oracle on Google Cloud Compute overview Stay organized with collections  Save and categorize content based on your preferences. 

Oracle on Google Cloud Compute provides a way for you to migrate and run your Oracle workloads on Google Cloud, at scale. You can utilize Google Cloud's secure and reliable infrastructure and virtual machines to deploy your Oracle environment. This lets you customize, configure, and manage your database environment as per your requirements, and seamlessly integrate with Google Cloud ecosystem, which includes services such as monitoring and logging.

Oracle on Google Cloud Compute supports [Rehost: lift and shift](https://cloud.google.com/architecture/migration-to-gcp-getting-started#rehost_lift_and_shift) type of migration, letting you move your existing on-premises Oracle databases and applications to Google Cloud with minimal disruption.

Oracle on Google Cloud Compute lets you migrate and deploy your Oracle workloads on the following Google Cloud services:

  * Compute Engine
  * Google Kubernetes Engine (GKE)
  * Google Cloud VMware Engine



![Oracle workloads supported by Oracle on Google Cloud Compute.](https://docs.cloud.google.com/static/oracle/compute/images/oracle-workloads-google-cloud-compute.png)

## Advantages of Oracle on Google Cloud Compute

  * Quick setup. You can create a VM running [Oracle Linux](https://docs.cloud.google.com/compute/docs/images#oracle_linux) in any region today and get started. Google Cloud VMs are quick to provision.
  * Direct deployment of Oracle Databases on Google Cloud VMs. Use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment) or [Oracle Toolkit for Google Cloud](https://google.github.io/oracle-toolkit/user-guide.html) to quickly deploy and manage Oracle databases on Google Cloud VMs.
  * Support for all Linux operating systems that are supported by Oracle, including Oracle Linux.
  * Support for Oracle technologies that you're already familiar with, such as GoldenGate and Data Guard. You can also change things up and expand to use our regional storage or managed instance groups to have multi-region disaster recovery without needing Oracle licenses on either end. It's up to you.
  * Cloud-native features, such as live migration and regional storage, to enhance your deployments.
  * A flexible and extensive array of machine families and scalable block storage options to choose from so that you can run a wide-range of workloads and applications that support your needs.
  * Own and control your Oracle software. You get to choose the Oracle software that you want to run. If you've got an old application that still needs Oracle Database 11g, you can still run those on our latest generation of machines.



## Oracle workloads on Compute Engine

[Compute Engine](https://cloud.google.com/products/compute) provides the following facilities for deploying your Oracle workloads:

  * Customizable infrastructure 
    * Choose machine types (vCPUs, RAM) based on workload needs.
    * Select persistent disk storage optimized for performance.
    * Run any Linux operating system that is supported by Oracle, including [Oracle Linux](https://docs.cloud.google.com/compute/docs/images#oracle_linux).
  * Quick deployment of Oracle Database workloads on Google Cloud

    * Use the [Guided Deployment Automation tool in Workload Manager](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment) to quickly customize and deploy your workloads on Google Cloud, without having to configure the infrastructure. Built-in recommendations and safeguarding helps you ensure that you follow the deployment best practices and avoid errors during the configuration and deployment process.

    * Use [Oracle Toolkit for Google Cloud](https://google.github.io/oracle-toolkit/user-guide.html) to deploy and manage Oracle databases if you're looking for more flexibility and customization options than those offered by Workload Manager.

  * High availability and disaster recovery

    * Use Google Cloud's regional or zonal replication for redundancy.
    * Implement Oracle Data Guard for failover solutions.
    * Backup and recovery automate backups using Cloud Storage or Oracle RMAN.
  * Performance optimization

    * Use Local SSDs for high IOPS (faster transactions).
    * Configure persistent disks (Standard/SSD) based on workload.
    * Take advantage of Google Cloud's networking for fast data transfers.
  * Licensing and cost control

    * Bring Your Own License (BYOL) model.
    * Optimize costs by choosing preemptible instances or committed use discounts.
  * Security and compliance

    * Use Google Cloud Identity and Access Management (IAM) roles and permissions for secure access.
    * Enable VPC Service Controls for network isolation.
    * Configure Oracle TDE (Transparent Data Encryption) for data security.



### Get started with Oracle workloads on Compute Engine

To get started with creating and running Oracle workloads on Compute Engine using Workload Manager, see [Deploy Oracle Database workloads](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview).

To deploy Oracle Database workloads using Oracle Toolkit, see [Quickstart: Use Oracle Toolkit with Compute Engine](https://docs.cloud.google.com/oracle/compute/quickstart-oracle-toolkit).

### Reference architectures

Following are some reference architectures for deploying Oracle workloads on Compute Engine:

  * [Enterprise application with Oracle Database on Compute Engine](https://cloud.google.com/architecture/enterprise-app-oracle-database-compute-engine)
  * [Enterprise application on Compute Engine VMs with Oracle Exadata in Google Cloud](https://cloud.google.com/architecture/enterprise-app-oracle-exadata-database-compute-engine)
  * [Oracle E-Business Suite with Oracle Database on Compute Engine VMs](https://cloud.google.com/architecture/oracle-ebs-on-compute-engine-vm)
  * [Oracle E-Business Suite with Oracle Exadata in Google Cloud](https://cloud.google.com/architecture/oracle-ebs-with-oci-exadata)
  * [Oracle PeopleSoft on Compute Engine with Oracle Exadata](https://cloud.google.com/architecture/oracle-peoplesoft-with-oci-exadata)



## Oracle on Google Kubernetes Engine

You can run an Oracle database on Google Cloud by deploying it on Google Kubernetes Engine (GKE), which lets you use Kubernetes for orchestration and management.

This approach involves containerizing your Oracle database and managing it as a stateful application within a GKE cluster. To ensure data persistence and stability, you can use a StatefulSet to manage the Oracle pods, which are backed by `PersistentVolumes` using Google Cloud Persistent Disk for durable storage. A Kubernetes Service then provides a stable network endpoint for applications to connect to the database, enabling you to take advantage of GKE's capabilities for high availability, scaling, and automated operations.

To simplify this process, you can use [El Carro](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator), an open source operator that automates the entire lifecycle of Oracle databases on Kubernetes. El Carro streamlines complex tasks such as initial provisioning, patching, high-availability configuration, and backup and recovery, using standard Kubernetes APIs. The Google Cloud blog post [El Carro drives change for Regnology — helps drop resource requirements by almost 40 percent](https://cloud.google.com/blog/products/databases/el-carro-automates-oracle-database-management-for-regnology/?e=0) describes how El Carro can help an organization run business-critical Oracle databases on GKE reducing manual effort and improving operational reliability.

For a detailed walkthrough on deploying an Oracle database on GKE using an operator, refer to the tutorial [Oracle Database Operator for Google Kubernetes Engine](https://medium.com/oracledevs/oracle-database-operator-for-kubernetes-on-google-cloud-b1f4e7eeb667) from the Oracle Developers community .

## Oracle on Google Cloud VMware Engine

For information about running Oracle workloads on [VMware Engine](https://cloud.google.com/vmware-engine), see [Support for Oracle workloads in Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-third-party-solutions).

## Licensing

Oracle on Google Cloud Compute uses a bring your own license (BYOL) model. You are responsible for the licensing of all of your software. For more information, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
