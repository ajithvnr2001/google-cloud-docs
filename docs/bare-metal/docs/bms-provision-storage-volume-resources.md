---
url: https://docs.cloud.google.com/bare-metal/docs/bms-provision-storage-volume-resources/
title: Provision storage volume resources \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:45.743295+00:00
---

# Provision storage volume resources  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-provision-storage-volume-resources/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Provision storage volume resources

After ordering storage resources for your Bare Metal Solution environment, you can provision the resources once they are available. You can provision the following self-service options:

  * Create a new Fibre Channel storage volume
  * Create LUNs on a volume
  * Attach a storage volume to a server

**Note:** For guidance on how to design and implement storage volumes and LUNs, see [Storage choices](https://docs.cloud.google.com/bare-metal/docs/bms-planning#storage_choices) and [Storage performance](https://docs.cloud.google.com/bare-metal/docs/bms-planning#storage_performance).

## Create a new storage volume

This feature lets you provision storage that you have previously ordered. To order storage volumes, contact [Google Cloud Sales](https://cloud.google.com/contact/).

**Note:** You can provision multiple storage volumes in a single request only through the Google Cloud console intake form. See [Use the Google Cloud console intake form to enter your selections](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

To create a new storage volume, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) menu.

  2. Click **Create**.

  3. Enter the following information:

Field | Description | Example  
---|---|---  
Region | Google Cloud region located closest to your Bare Metal Solution environment. | `us-central1`  
Name | Create a name for your storage volume. | `volume-1`  
Type | Select the type of storage: 
     * SSD – Solid state drive
     * HDD – Hard drive
| `SSD`  
Performance tier | If you selected the SSD storage type, select the performance tier of the SSD drive: 
     * Standard – Select to create a standard SSD drive.
     * Performance – Select to create a performance SSD drive. **Note:** This option is enabled only if you have selected a region where Performance SSD storage is available. For the list of regions, see [Performance SSD storage](https://docs.cloud.google.com/bare-metal/docs/bms-planning#performance_ssd_storage). 
| `Performance`  
Size | Select the size of the drive in GiB, where 1024 GiB = 1 TiB. The size ranges from a minimum of 100 GiB to a maximum of 16 TiB. If you need more than 16 TiB, create additional volumes as needed.  
  
For Performance SSD drive, the maximum size is 8 TiB per volume.  | `16384`  
Snapshot enabled | Saves a [backup copy of your storage volume](https://cloud.google.com/bare-metal/docs/bms-planning#storage_volume_snapshots) once per day. Required for custom snapshots, but disabled by default. **Note:** When you enable snapshots, Google Cloud reserves 20% of the requested size of the storage volume. For example, if your volume size is 1 TiB (1024 GiB), you can use 819 GiB for data storage, and 205 GiB for the snapshots.  | Checkbox selected to enable snapshots  
Configuration | Select the type of LUN configuration you need: 
     * Default configuration – Create LUNs of equal size (recommended).
     * Custom configuration – Create LUNs with different sizes.
| `Default configuration`  
Target server | Select a server and attach the storage volume. | `server-1`  
  4. Click **Create**.

  5. The console checks if there is enough space available for the requested storage volume. The console implements the change if there is available space, or alerts you if the operation cannot be performed. If your storage volume request succeeds, billing for the additional storage begins automatically.

  6. After you have provisioned the storage volume, you can share it with additional servers.

**Note:** You cannot expand the existing LUNs in a storage volume. Instead, create new LUNs on a new storage volume, migrate the old LUNs to the new storage volume, and decommission the old LUNs.



## Create LUNs on a storage volume

To create LUNs for a storage volume, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) menu.

  2. Click the name of the storage volume on which you want to create a LUN.

  3. Next to the **LUNs** section, click **Create**.

  4. Enter the following information:

Field | Description | Example  
---|---|---  
Number of LUNs | Total number of LUNs you want to create with a particular size. | `4`  
Size | Select the size of the LUN in GiB, where 1024 GiB = 1 TiB. | `1024`  
  5. Click **Add item** if you need to create more than one set of LUNs.

  6. Click **Create** to deploy the new LUNs.

**Note:** When you add a new LUN in an existing storage volume, you need to rescan your LUNs so the new LUN can be placed into service. For more information, see [Storage choices](https://docs.cloud.google.com/bare-metal/docs/bms-planning#storage_choices).



## Attach a storage volume to a server

You can attach multiple storage volumes to a server at once.

To attach a storage volume to a server, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Servers**](https://console.cloud.google.com/compute/bareMetalSolution/servers) page.

  2. Click the name of the server to which you want to attach a storage volume.

  3. In the **LUNs** section, click **Attach Volumes**.

  4. From the **Target volumes** list, select the storage volume you want to attach. You can also select multiple storage volumes.

  5. Click **Attach volumes**.




You can also attach the same storage volume to other servers in parallel. Go to the **Servers** page and repeat this procedure for all the other servers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
