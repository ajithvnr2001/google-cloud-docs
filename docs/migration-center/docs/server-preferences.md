---
url: https://docs.cloud.google.com/migration-center/docs/server-preferences/
title: Migration preferences for servers \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:25.672660+00:00
---

# Migration preferences for servers  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/server-preferences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration preferences for servers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the available [migration preferences](https://docs.cloud.google.com/migration-center/docs/migration-preferences) for servers in Migration Center.

## Google Cloud options

Specify the target product to which you would like to migrate your infrastructure. You can specify either **No preference** , or one of the following products:

  * Google Compute Engine
  * Google Cloud VMware Engine



If you select **No preference** , Migration Center provides you with recommendations based on the internal default preference logic, which might be updated periodically.

The target product you select and the preferences you set are used to generate the TCO report. Migration Center also lets you customize the preferences for the other non-selected products, which are used to generate the license report.

## Google Compute Engine preferences

If you select Compute Engine as your target product, first select from one of the following tenancy preference modes:

  * Multi-tenant (default)
  * Sole-tenant (dedicated physical Compute Engine servers)



The following table summarizes the differences between multi-tenant and sole-tenant modes:

Multi-tenant | Sole-tenant  
---|---  
VMs share a physical server with VMs from other projects. | VMs have exclusive access to a dedicated physical server.  
Only supports pay-as-you-go (PAYG) licenses for Windows Server. | Supports both bring-your-own-license (BYOL) and PAYG licenses for Windows Server.  
Set your preference based on virtual machine characteristics such as machine series, priority, and pricing. | Set your preference based on the underlying physical hardware, such as node type and CPU overcommit ratio.  
Uses default Simultaneous Multithreading (SMT) settings. | Provides options to disable or configure SMT to balance performance and licensing costs.  
  
Select sole-tenant nodes if you need to keep your VMs physically separated from VMs in other projects to meet security or compliance requirements, or for Windows bring-your-own-license (BYOL) scenarios that require per-core or per-processor licenses.

### VM tenancy preferences

### Multi-tenant (default)

#### Machine series selection

Define the machine series that Migration Center should consider when you generate your TCO reports. You can specify your selection based on performance, cost, or a custom list of machine types.

  * For **Machine priority** , select one of the following options:
  * **Balance latest technology and low cost:** prioritize the latest compute technologies for stable performance, confidential computing, and greater sustainability. Select this option for production workloads where performance is critical. This is the default selection.
  * **Lowest cost:** prioritize the most economical machine series available. Select this option for development environments or other cost-sensitive workloads.

    * To determine the SKUs to be considered in the **Machine series** list, select one of the following options:

      * **Consider pre-released, latest Gen:** include the newest disk or CPU and RAM SKUs, even if not yet launched.
      * **Consider only launched SKUs:** only include launched SKUs.
    * For **Machine series** , select all the Compute Engine machine series that you want to include as possible targets for migration of your virtual machine (VM) instances. To choose the most suitable machine series for your business needs, review the [machine families comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types).

  * For **Microsoft SQL Server licensing** , select the license type for the SQL Server database deployments that you plan to host on Compute Engine.

  * For **Product pricing track** , select one of the following options:

    * **No preference:** defaults to a 3-year resource-based committed use discount (CUD) for the lowest total cost of ownership on predictable workloads.
    * **On demand:** lets you pay for compute resources at the standard price without signing a long-term contract.
    * **1-year resource-based committed use discount (CUD):** receive a significant discount on specific Compute Engine resources in a particular region in exchange for a one-year commitment, payable monthly in USD.
    * **3-year resource-based committed use discount (CUD):** offers a higher discount than a 1-year plan in exchange for a three-year commitment to a minimum amount of resources in a specific region, payable monthly in USD.
    * **1-year flexible committed use discount (CUD):** receive a discount when you commit to a minimum hourly spend for one year on eligible vCPUs and memory across various machine types and regions, payable monthly in USD.
    * **3-year flexible committed use discount (CUD):** receive a discount on eligible compute resources when you commit to a minimum hourly spend for three years, payable monthly in USD.



### Sole-tenant

#### Sole tenant configuration

If you select sole-tenant as your tenancy preference mode, configure the following options:

  * **Node type:** select a sole-tenant node type from the list.
  * **Overcommit ratio:** to enable CPU overcommit, select a value between 1.0 and 2.0 by using the slider. The maximum ratio is 2.0.

Overcommit enables VMs on a sole-tenant node to share CPU resources, allowing them to exceed their allocated capacity. This option is useful for workloads that are often underutilized but might have bursts of activity.

  * **Host maintenance policy:** Specify the host maintenance policy that you want to apply in your target sole-tenant nodes. This impacts the required size of the sole-tenant node cluster that you see in the TCO report.

For more information, see [host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy).

  * For **Product pricing track** , select one of the following options:

    * **No preference:** defaults to a 3-year resource-based committed use discount (CUD) for the lowest total cost of ownership on predictable workloads.
    * **On demand:** lets you pay for compute resources at the standard price without signing a long-term contract.
    * **1-year resource-based committed use discount (CUD):** receive a significant discount on specific Compute Engine resources in a particular region in exchange for a one-year commitment, payable monthly in USD.
    * **3-year resource-based committed use discount (CUD):** offers a higher discount than a 1-year plan in exchange for a three-year commitment to a minimum amount of resources in a specific region, payable monthly in USD.
    * **1-year flexible committed use discount (CUD):** receive a discount when you commit to a minimum hourly spend for one year on eligible vCPUs and memory across various machine types and regions, payable monthly in USD.
    * **3-year flexible committed use discount (CUD):** receive a discount on eligible compute resources when you commit to a minimum hourly spend for three years, payable monthly in USD.



For more information, see [About VM tenancy](https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy).

After you select your tenancy preference, specify your preferences for machine series, disk types, and licensing options. These selections are used to generate your TCO reports.

### Storage configuration

You can customize your VM configuration by configuring the following options:

  * For **Storage pool preference** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), select your preference for using [Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools) to provision storage capacity in a single pool for multiple Compute Engine VMs. This preference can help reduce cost and improve operational efficiencies for large-scale storage. Select one of the following options: 
    * **Automatic, cost balanced:** let Migration Center automatically determine whether to include Hyperdisk Storage Pools or individual Hyperdisks to achieve a lower total cost of ownership (TCO) for your workloads. Migration Center recommends Hyperdisk Storage Pools only if the cost is not more than 25% higher than individual Hyperdisk volumes; otherwise, recommends individual Hyperdisk volumes. This is the default selection. 

If you selected sole-tenant nodes as the target, the **Automatic, cost balanced** option recommends Hyperdisk Storage Pools even if they are more expensive than individual Hyperdisk volumes. If you are migrating to sole-tenant nodes, we recommend that you select **Never**. 

    * **Always:** always recommend Hyperdisk Storage Pools for all compatible VMs.
    * **Never:** don't recommend Hyperdisk Storage Pools.

To account for storage savings achieved through compression and deduplication, adjust the **Storage pool compression factor** slider. Using a higher value for this setting helps lower your TCO when using Hyperdisk Storage Pools.

  * For **Disk type** , select your preferred disk type.



Depending on the machine series and disk type that you select, Migration Center might not recommend all of the machine and disk combinations that you selected. For example, Google Cloud Hyperdisk volumes are only available in certain machine series. If you select only Hyperdisk volumes as your migration preferences, Migration Center only recommends machine series that support Hyperdisk volumes.

If you select a machine series that is not available in your preferred region, Migration Center doesn't recommend it. If you don't see a machine or disk combination that you expected, review the [pricing page](https://docs.cloud.google.com/compute/all-pricing) to verify if the combination is available in your preferred region.

### OS license type and pricing track

Select your preferences for licensing and pricing track for Windows Server or specific Linux distributions.

#### Windows Server

For **Windows Server** , if you selected sole-tenant node for Compute Engine, you can bring your own licenses (BYOL), or select pay-as-you-go (PAYG) licenses from Google Cloud. If you selected multi-tenant node for Compute Engine, you can only use PAYG licenses. PAYG licenses are charged on-demand. If you select BYOL, you are not charged for licenses in Migration Center.

By default, Compute Engine runs two vCPUs on each physical core using Simultaneous Multithreading (SMT). This means that for each physical core in your target environment running a Windows workload, you pay for two Windows licenses, which are applied per vCPU.

To reduce the costs of your target servers, you can choose to disable SMT. Migration Center lets you specify one of the following options for SMT to balance license costs and performance:

  * **Auto:** Let Migration Center choose the cheapest among the available options. This is the default.
  * **Enable:** Leave SMT enabled as per default, and calculate the costs of two licenses per physical core.
  * **Disable:** Disable SMT on the physical CPUs to save on the license costs. This might impact the performance of your servers.
  * **Disable with compensation:** Disable SMT on the physical CPUs, but compensate for the missing vCPUs, for example by increasing the target number of CPUs, or by switching to a machine family with higher performance.
  * **No preference:** Use Migration Center default preference algorithm.



When you apply this preference, consider the following:

  * Your SMT preference is applied on top of rightsizing. Therefore, if you select **Disabled** , **Disabled with compensation** or **Auto** , this might increase the target utilization above the target utilization that you set for rightsizing.
  * If there is no target VM series that is compatible with the selected SMT preferences, then the SMT preference is ignored.



For more information about SMT in Compute Engine, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

#### Linux distributions

For Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), and SUSE Linux Enterprise Server (SLES) for SAP, you can bring your own license (BYOL), or use pay-as-you-go (PAYG) licenses from Google Cloud. If you select BYOL, you are not charged for licenses.

If you use PAYG licenses, select one of the following pricing tracks:

  * **On demand:** the standard pricing model where you pay for licenses that you consume without any long-term contract or commitment.
  * **1-year committed use discount (CUD):** a 1-year commitment, payable monthly in USD.
  * **3-year committed use discount (CUD):** a 3-year commitment, payable monthly in USD, with a higher discount than 1-year CUDs.



## Google VMware Engine preferences

If you select VMware Engine as your target product, specify the requirements for the group of virtual machines allocated across VMware Engine nodes.

**Note:** The minimum cluster size recommended by Migration Center is three nodes.

### Machine series families

Select the machine series families that you want to use. If a machine series family is not available in the region you selected, a warning appears.

### Spare nodes

Select the number of spare nodes in this cluster. The default is `0`.

### Storage only nodes

If you have storage-bound workloads, selecting **Use when available** adds additional vSAN storage to storage only nodes, instead of HCI nodes. This might help reduce costs in the TCO report, and should be selected in the majority of cases. If you have specific requirements, however, you can exclude storage only nodes from your target environment by selecting **Don't use**.

If storage only nodes are not available for the machine series you selected, this preference is ignored, and only HCI nodes are considered.

### Product pricing track

Select a product pricing track to choose how you want to pay for Google Cloud services. Select from one of the following options:

  * **No preference:** a 3-year committed use discount, payable upfront in USD.
  * **On demand:** the standard pricing model where you pay for the resources that you consume without any long-term contract or commitment.
  * **1-year committed use discount (CUD):** a 1-year commitment, payable monthly in USD.
  * **3-year committed use discount (CUD):** a 3-year commitment, payable monthly in USD. A 3-year commitment offers a higher discount rate than a 1-year commitment.
  * **1-year committed use discount (CUD):** a 1-year commitment, payable upfront in USD.
  * **3-year committed use discount (CUD):** a 3-year commitment, payable upfront in USD. A 3-year commitment offers price stability and a lower total cost of ownership (TCO).
  * **Convertible 3-year VMware Engine (GCVE) commitment:** a 3-year commitment, payable monthly in USD.

**Note:** On-demand pricing is a baseline charge for vCPUs and memory. Committed use discounts (CUDs) reduce the charges for vCPUs and memory.

For more information about Committed use discounts for VMware Engine, see [Committed use discounts](https://docs.cloud.google.com/vmware-engine/docs/cud).

### VMware Engine service type

Choose how you plan to manage the license by selecting one of the available options:

  * **Fully licensed:** The fully integrated VMware Engine service, which includes all of the hardware, software, support, lifecycle management (such as patching and break fixes), as well as physical hosting environment (power and cooling, rack/stack) for the full VMware private cloud environment. This doesn't entitle the customer to a perpetual ownership of the VMware Cloud Foundation software, but rather, it is sold as a service, similar to other Google Cloud products.

  * **Portable License:** Broadcom and Google Cloud support license portability of VMware Cloud Foundation to VMware Engine. In this model, customers can purchase subscriptions of the new VMware Cloud Foundation software from Broadcom and Broadcom partners, and flexibly use those subscriptions on VMware Engine, as well as on their own on-premises data centers. The remainder of the service (hardware, hosting environment, support, lifecycle management) is purchased directly from Google Cloud or Google Cloud partners.




### VMware Engine Protected

Select if you want to use [VMware Engine Protected](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-engine-protected) to enable backup and disaster recovery on your VMware Engine nodes.

VMware Engine Protected increases the costs in your TCO report and might not be available in all regions. For more information, see [Backup and DR Service pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

### vSAN FTT RAID policy

Select a vSAN storage policy. This policy defines the failures to tolerate (FTT) and the failure tolerance method. Select from one of the following options:

  * **No preference:** a vSAN storage policy is not set.
  * **No Fault Tolerance:** no replicas. Node failure might cause data loss.
  * **FTT=1, RAID=1:** 1 replica. Can tolerate a single node failure. Minimum 3 nodes per cluster.
  * **FTT=1, RAID=5:** 1 replica. Can tolerate a single node failure with lower disk overhead. Minimum 4 nodes per cluster.
  * **FTT=2, RAID=1:** 2 replicas. Can tolerate failures in 2 nodes. Minimum 5 nodes per cluster.
  * **FTT=2, RAID=6:** 2 replicas. Can tolerate failures in 2 nodes with lower disk overhead. Minimum 6 nodes per cluster.
  * **FTT=3, RAID=1:** 3 replicas. Highest safety with high disk overhead. Minimum 7 nodes per cluster.



For more information, see [vSAN storage policies](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsan_storage_policies).

### Advanced settings

To further customize your VMware Engine migration preferences, you can configure settings such as CPU, memory, and storage optimization.

To configure compute settings, modify one or more of the following options:

  * **CPU core overcommit ratio:** specify an overcommit ratio between `1.0` and `8.0`, with `0.1` increment. The default value is `4`. Overcommitment lets you allocate more memory and CPU cores on your VMs than what is available in the physical nodes.

  * **Memory overcommit ratio:** specify the following values: `1.0`, `1.25`, `1.5`, `1.75` and `2.0`. The default value is `1`.

  * **Hyperthreading weight:** specify the CPU performance boost applied to this cluster nodes. The default is `25%`.

  * **HCX mesh:** Increases the amount of management resources, CPU, memory, and storage required by the VMware HCX (Hybrid Cloud Extension) cluster. By default, HCX mesh is enabled.

  * **NSX-T Edge size:** configure the CPU, memory, and storage resources allocated in a VMware NSX-T environment.

Large is recommended for most production deployments. Extra large is for the most demanding throughput and latency requirements.

  * **Storage optimization:** configure the storage optimization performance.

We recommend that you select **Compression** because it balances savings and operational resiliency for most use cases. **Deduplication and compression** might yield cost savings, but you must consider performance implications before you select this option.

If you select deduplication and compression, the **Storage savings ratio** setting lets you specify the amount of storage that you expect to save when you migrate to Google Cloud, based on your current on-premises values. The default value is `1.7`.




## Sizing and network preferences

Configure sizing recommendations and network preferences for your migrated assets.

### Target sizing strategy

For **Sizing method** , configure how Migration Center recommends VM sizes for your migrated assets. You can set the sizing method, utilization targets, and defaults for assets that lack performance data.

  * **No rightsizing:** choose a target VM size that closely match the size of your current machines. The algorithm doesn't apply rightsizing, which means that it doesn't consider the current performance data of your machines.
  * **Moderate (default):** calculate your target VM size based on the current performance of your machines, and apply moderate rightsizing to your VMs. This approach balances between performance and cost.
  * **Aggressive:** calculate your target VM size based on the current performance of your machines, and apply aggressive rightsizing to your VMs. For example, if you underutilize your machine CPU, your TCO report will suggest a VM with fewer CPUs. This approach maximizes the use of the VM's resources and reduces costs, but might also impact performance in the event of an unexpected load.
  * **Custom:** manually configure the parameters that you want the algorithm to use for the calculations. When you choose the custom sizing optimization, you can change the following parameters: 
    * Metrics baseline: the baseline for calculating memory, CPU, and disk IOPS.
    * Storage multiplier: the amount of storage that you want to provision in your infrastructure, as a proportion of the current storage utilization.
    * CPU usage: the CPU utilization that you want to have in your infrastructure, as a percentage of the current utilization.
    * Memory usage: the memory utilization that you want to have in your infrastructure, as a percentage of the current utilization.



The following table shows the calculation parameters for the **Moderate** and **Aggressive** optimization strategies.

Metric | Moderate | Aggressive  
---|---|---  
Metrics baseline | 95th percentile | 95th percentile  
CPU usage | 70% | 90%  
Memory usage | 85% | 100%  
Storage multiplier | 1.25x | 1.10x  
Uptime | 730 hours per month | 730 hours per month  
  
### Source utilization estimated defaults

Migration Center prioritizes actual performance data when generating sizing recommendations. For assets where granular performance data is unavailable, you can set utilization estimates that guide the target sizing strategy. If you selected **No rightsizing** as your target sizing strategy, you cannot set the utilization estimates.

  * **Base sizing strategy on utilization estimates** : this option bases sizing recommendations on utilization estimates for assets for which granular performance data is unavailable. Migration Center applies these estimates to the provisioned capacity to determine the appropriate Google Cloud resource size and cost. You can configure the default utilization percentages (between 1 and 100 percent) for the following resources:

    * **CPU utilization default:** default value is 70%.
    * **Memory utilization default:** default value is 75%.
    * **Disk utilization default:** default value is 75%.
  * **Base sizing strategy on 100% provisioned shape** : this option bases sizing on the asset's 100% provisioned shape (CPU, memory, and disk).




### Network data transfer out estimate

Specify the estimated percentage of network traffic that leaves the Google Cloud network (data transfer out). Migration Center uses this percentage to estimate network costs in the TCO report. You are charged only for data transfer out, and not for data transfers within Google Cloud.

  * For **Data transfer out estimate** , set a value between 1 and 100 percent. The default value is 5%.



## Product pricing track

Specify your preferred pricing track for the VMs that you migrate to Google Cloud.

Choose between on demand pricing, resource-based committed use of one or three years, or flexible committed use of one or three years. Committed use discounts (CUDs) apply when you choose a committed use, and appear in your TCO report.

## What's next

  * Learn more about [committed use discounts for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).
  * Learn more about [sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).
  * Learn more about [VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing).
  * Learn about the [available preferences for Microsoft SQL Server databases](https://docs.cloud.google.com/migration-center/docs/ms-sql-server-preferences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
