---
url: https://docs.cloud.google.com/architecture/partners/using-cohesity-with-cloud-storage-for-enterprise-hybrid-data-protection/
title: Data management with Cohesity Helios and Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:47.011451+00:00
---

# Data management with Cohesity Helios and Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/using-cohesity-with-cloud-storage-for-enterprise-hybrid-data-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Data management with Cohesity Helios and Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-03-27 UTC

By Edwin Galang (Cohesity Cloud Solutions Architect) and Vikram Kanodia (Cohesity Cloud Solutions Architect)

This document describes how you can use the [Cohesity Helios data platform](https://www.cohesity.com/products/helios/) with Google Cloud. Using this platform has the following benefits:

  * Long-term data retention with [Cloud Storage](https://docs.cloud.google.com/storage).
  * Backup and recovery of workloads and VMs in [Compute Engine](https://docs.cloud.google.com/compute) and [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine) using [Cohesity DataProtect](https://www.cohesity.com/products/dataprotect/).
  * File services in Google Cloud using [Cohesity SmartFiles](https://www.cohesity.com/products/smartfiles/).



Cohesity Helios is a data management platform that consolidates multiple functions like backup, recovery, analytics, and disaster recovery in a single scalable, secure, AI-driven platform. 

You can deploy Cohesity Helios at your network edge, in a data center, or in Google Cloud.

## Architecture

The following diagram shows how Cohesity integrates with Google Cloud.

![Cohesity and Google Cloud architecture](https://docs.cloud.google.com/architecture/images/partners/cohesity-arch.svg)

As the diagram shows, Cohesity Helios is installed in your data center and in Google Cloud. It connects with Compute Engine and VMware Engine to obtain VM images and stores them in Cloud Storage.

Cohesity Helios connects with Cloud Storage to provide a long-term archive for your data. You can deploy Cohesity Helios in Google Cloud to back up and recover:

  * Compute Engine VMs
  * VMware Engine VMs
  * Application workloads 
    * SAP HANA
    * Oracle database
    * SQL Server



With Cohesity SmartFiles, you can use protocols like network file system (NFS) and server message block (SMB) to provide file services in your Google Cloud environment.

## Cohesity Helios components

Cohesity Helios has the following main components:

  * **Cohesity DataProtect:** A software-defined backup and recovery solution that supports cloud environments. Cohesity DataProtect is designed for hyperscale and offers comprehensive policy-based protection for both on-premises and cloud data sources.
  * **Cohesity SmartFiles:** A multiprotocol file and object solution that supports large enterprises and cloud environments. It's designed to let you scale, protect, and create multiple tiers for data management.



## Long-term data retention with Cloud Storage

Cohesity supports the following [Cloud Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes):

  * Standard
  * Nearline
  * Coldline



That means you can archive your data in the storage class that best meets your long-retention and cost requirements.

Using Cohesity with Cloud Storage provides the following benefits:

  * You don't need cloud gateways to connect Cohesity with Cloud Storage.
  * You can use wildcards in searches to locate and restore archived data from Cloud Storage.
  * You can recover individual VMs, restore files to source VMs, and recover individual application objects.



## Backup and recovery of Compute Engine VMs, VMware Engine VMs, and application workloads

Cohesity DataProtect is designed to provide consistent and comprehensive protection for Compute Engine VMs, VMware Engine VMs, and application workloads.

Using Cohesity DataProtect with Cloud Storage provides the following benefits:

  * A single UI to manage and provision all your backup and recovery services.
  * Policy automation to meet your business service level agreements (SLAs) and assign policies to a single job or to all jobs, globally.
  * Immutable snapshots with Advanced Encryption Standard 256 encryption, multi-factor authentication, and Federal Information Processing Standards certification to help protect against ransomware.
  * The use of strict consistency, erasure coding, and hardware fault tolerance to meet your SLAs and achieve higher data resiliency.
  * Global, variable-length deduplication across workloads and protocols to maximize space.



## File services for Compute Engine VMs and VMware Engine

Cohesity SmartFiles lets you consolidate data silos. It's designed to help securely manage the following unstructured content and application data types, including:

  * Digital libraries
  * Archives
  * Rich media
  * Video surveillance
  * Big data
  * Backup datasets



Cohesity SmartFiles provides the following benefits:

  * Broad compatibility across users and applications, whether on-premises or in the cloud, with support for the NFS and SMB protocols.
  * Resiliency and consistency while eliminating disruptive upgrades, unique and distributed file systems.
  * Ability to grow incrementally using linear performance and capacity that adds additional nodes.
  * Space maximization using [sliding window](https://en.wikipedia.org/wiki/Sliding_window_protocol) variable-length deduplication, Zstandard compression, and small file efficiency.
  * Policies that transparently down-tier and up-tier data storage to optimize spending.
  * An external network-attached storage tiering that coexists with your existing systems.
  * A UI to manage, monitor, and search all your unstructured data. Machine-driven operational insights help predict future needs.



## Configure Cohesity with Cloud Storage

This section describes how to configure Cohesity Helios with Cloud Storage and create a policy to archive data to Cloud Storage for long-term retention.

### Register Cloud Storage with Cohesity Helios

To use Cloud Storage with Cohesity Helios, you must first register it as an external target.

  1. Log in to the [Cohesity Helios](https://helios.cohesity.com/) console using your MyCohesity credentials or your SSO credentials if you are using another identity provider.
  2. In the Cohesity Dashboard, click **Infrastructure > External Targets**.
  3. Click **Register External Target** to access the **Register External Target** page.
  4. Register the Cloud Storage target using the following information:

     * **Purpose:** select **Archival**
     * **New Target:** enter a unique name for the target
     * **Type:** select the Cloud Storage class
     * **Bucket name:** enter the name of the Cloud Storage bucket
     * **Project ID:** enter the name of the project that hosts Cloud Storage
     * **Client Email Address:** enter the service account email address for Cloud Storage
     * **Client Private Key:** enter the private key that is associated with the service account
     * **Encryption:** enable to send and store data in an encrypted format
     * **Compression:** enable to send and store the data in a compressed format
     * **Source Side Deduplication:** enable to deduplicate data before sending it to the target
     * **Bandwidth Throttling:** enable to limit the maximum data transfer rate to the target during a time window

The following screenshot shows sample inputs.

![Sample inputs.](https://docs.cloud.google.com/architecture/images/partners/cohesity-1.png)

  5. To create the new external target, click **Register**.




Next, create a policy to archive data.

### Create a policy to archive data to Cloud Storage

A policy is a reusable set of settings that define how and when data is protected, replicated, and archived.

  1. Log in to the Cohesity Helios console.
  2. In the Cohesity Dashboard, select **Data Protection > Policies.**
  3. Click **Create Policy**.
  4. Enter the following information to configure the policy:

     * **Policy name:** enter a unique name for the policy
     * **DataLock:** enable to create a write-once-read-many (WORM)-compliant backup
     * **Archive to:** select the name of the Cloud Storage bucket
     * **Every:** select how often backups are captured by the protection group
     * **Retain for:** specify the number of days that backups are stored on the Cohesity cluster before the backups are deleted
  5. Click **Add Archive**.

  6. In the **Archive to** list, select the Cloud Storage bucket.

  7. Specify the archive schedule for copies of the snapshots that were created by this job. These copies are stored on the registered target.

The following screenshot shows a sample policy.

![Sample policy.](https://docs.cloud.google.com/architecture/images/partners/cohesity-2-4.png)

  8. Click **Save**.




## Configure Cohesity to back up Compute Engine VMs

The following sections describe how to register a Google Cloud source, create a policy, and create a protection group to back up Compute Engine VMs.

### Register a Google Cloud source

  1. Log in to the Cohesity Helios console.
  2. In the Cohesity Dashboard, select **Data Protection > Sources**.
  3. Select **Register > Virtual Machines**.
  4. Complete the following:

     * **Source Type:** select **Cloud > GCP: IAM User**
     * **Use JSON Key File:** enable to use the service account's JSON key file
     * **Service Account JSON Key File:** select the service account's `JSON` key file or enter the information manually
     * **VPC:** enter the VPC network
     * **Subnet:** enter the VPC subnet

The following screenshot shows a sample registration.

![Sample registration.](https://docs.cloud.google.com/architecture/images/partners/cohesity-3.png)

  5. Click **Register**.




### Create a policy to back up Compute Engine VMs

A policy is a reusable set of settings that define how and when objects are protected, replicated, and archived.

  1. Log in to the Cohesity Helios console.
  2. In the Cohesity Dashboard, select **Data Protection** > **Policies**.
  3. Click **Create Policy**.
  4. Complete the following information: 
     * **Policy name:** enter a unique name for the policy
     * **DataLock:** enable to create a WORM-compliant backup
     * **Archive to:** select the name of the Cloud Storage bucket
     * **Every:** select how often backups are captured by the protection group
     * **Retain for:** specify the number of days that backups are stored on the Cohesity cluster before the backups are deleted
     * **Policy Name:** enter a unique name for the policy
     * **DataLock:** enable to create a WORM-compliant backup
  5. (Optional) To meet long-term retention requirements, archive Google Cloud data to Cloud Storage.

     1. Click **Add Archive** to add Cloud Storage to the policy.

     2. Enter the following information:

        * **Archive to:** select the Cloud Storage bucket.
        * **Every:** select when an archive is created.
        * **Retain for:** select how long the copies are stored in the Cloud Storage bucket before they are deleted.

The following screenshot shows a sample policy.

![Sample policy.](https://docs.cloud.google.com/architecture/images/partners/cohesity-2-4.png)

  6. Click **Save**.




### Create a protection group for Compute Engine VMs

  1. Log in to the Cohesity Helios console.
  2. In the Cohesity Dashboard, select **Data Protection > Protection**.
  3. Click **Protect**.
  4. Click **Add Objects**.
  5. In the **Registered Source** list, select the Google Cloud source.
  6. Select the VMs to protect and click **Continue**.

The following screenshot shows some selected VMs.

![Selected VMs](https://docs.cloud.google.com/architecture/images/partners/cohesity-5.png)

  7. Enter the **Protection Group** name.

The following screenshot shows a selected protection group.

![Selected protection group](https://docs.cloud.google.com/architecture/images/partners/cohesity-6.png)

  8. From the **Policy** list, select the policy.

  9. Click **Protect**.




## Recover Compute Engine VMs

Cohesity can help you recover protected objects (such as VMs) from a snapshot created by a protection group. You can recover data from a Cohesity cluster or a Cloud Storage target. You can recover data to its original location or a new location.

  1. Log in to the Cohesity Helios console.
  2. In the Cohesity Dashboard, select **Data Protection > Recoveries**.
  3. Click **Recover** and select **Virtual Machines > VMs**.
  4. In the **New Recovery** wizard, search for the VMs.
  5. From the search results, select the VMs that you want to recover, the recovery point, and the location to recover the VM from.
  6. Click **Next: Recover Options**.
  7. Complete the following information: 
     * **Recover to:** select the location to recover to
     * **Recovery Options:** select the recovery options
  8. Click **Recover**.



## What's next

Review additional documentation on the Cohesity website:

  * [Next generation data management with Cohesity](https://www.cohesity.com/solutions/cloud/google/).
  * [Cohesity and Google Cloud](https://www.cohesity.com/solutions/cloud/google/).
  * [About Cohesity](https://www.cohesity.com/).
  * [Cohesity Blogs](https://www.cohesity.com/blogs/).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-03-27 UTC."],[],[]] 
