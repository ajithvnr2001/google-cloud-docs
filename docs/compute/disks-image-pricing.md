---
url: https://docs.cloud.google.com/compute/disks-image-pricing/
title: Disk and image pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:10.921097+00:00
---

# Disk and image pricing | Google Cloud

> Source: https://docs.cloud.google.com/compute/disks-image-pricing/

Page Contents




## Disk and image pricing

This page describes the pricing information for Compute Engine disks and [images](https://cloud.google.com/compute/docs/images/os-details). This page does not cover pricing for [VM instances](https://cloud.google.com/compute/vm-instance-pricing), [networking](https://cloud.google.com/vpc/network-pricing), [sole-tenant nodes](https://cloud.google.com/compute/sole-tenant-pricing), or [GPUs](https://cloud.google.com/compute/gpus-pricing).

Compute Engine charges for usage based on the following price sheet. A bill is sent out at the end of each billing cycle, providing a sum of Google Cloud charges. Prices on this page are listed in U.S. dollars (USD).

For Compute Engine, disk size, machine type memory, and network usage are calculated in JEDEC binary gigabytes (GB), or IEC gibibytes (GiB), where 1 GiB is 230 bytes. Similarly, 1 TiB is 240 bytes, or 1024 JEDEC GBs.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

You can also find pricing information with the following options:

  * See the estimated costs of your instances and Compute Engine resources when you create them in the [Google Cloud console](https://console.cloud.google.com/).
  * Estimate your total project costs with the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).
  * View and download prices from the [Pricing Table](https://cloud.google.com/billing/docs/how-to/pricing-table) in the Google Cloud console.
  * View more information about costs and usage in [Cloud Billing reports](https://cloud.google.com/billing/docs/reports).
  * Use the Cloud Billing [Catalog API](https://cloud.google.com/billing/v1/how-tos/catalog-api) for programmatic access to [SKU](https://cloud.google.com/skus) information.



## 

Premium images

Certain images available on Compute Engine are considered premium images and incur charges to use. These images include:

  * Red Hat Enterprise Linux (RHEL and RHEL for SAP)
  * SUSE Linux Enterprise Server (SLES and SLES for SAP)
  * Ubuntu Pro
  * Windows Server
  * SQL Server



**Note:** If you are a Microsoft licensee with a contract that includes Software Assurance, you might be able to move your existing SQL Server licenses to Compute Engine. For more information about License Mobility, see [Using existing Microsoft licenses](https://cloud.google.com/compute/docs/instances/windows/ms-licensing).

The price for a premium image depends on which machine type you use. For example, a standard SLES image costs $0.02 per hour to run on an f1-micro VM, but the same image costs $0.11 per hour to run on an n1-standard-8 VM. The prices for premium images are the same worldwide and don't differ based on zones or regions.

All prices for premium images are in addition to charges for using a machine type. For example, the total price for using an n1-standard-8 VM with an SLES image is the sum of the machine type cost and the image cost:

n1-standard-8 cost + SLES image cost = $0.379998 + $0.11 = $0.49 per hour

[Spot VMs](https://cloud.google.com/compute/docs/instances/spot) (and [preemptible VMs](https://cloud.google.com/compute/docs/instances/preemptible)) don't reduce the costs of premium images and don't change the way that you are billed for the use of those images. If Compute Engine terminates the Spot VMs (or preemptible VMs) that run a premium image, you are billed for that image as if you terminated the VM yourself. The charges for minimum usage still apply, and bills for premium images are still calculated by rounding up to the nearest usage increment.

**Note:** When you use premium images, Google is required to report the appropriate licensing details to the image provider(s). This information might include information about your Google account (such as the person or entity being billed, and the region or country registered to the account), details of the transaction (such as what product or service you have used, the corresponding Google SKU, or the date when you first used the product or service), and usage information (such as total hours of usage).

### 

Red Hat Enterprise Linux (RHEL) and RHEL for SAP images

**Price Model Update starting July 1, 2024.**

[Red Hat announced a price model update](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement) on RHEL and RHEL for SAP to all Cloud providers, including Google Cloud. Starting July 1, 2024, RHEL, RHEL for SAP, and the new RHEL 7 ELS license will be billed on a core-hour model.

**Pricing before July 1, 2024**

RHEL images:

  * **$0.06 USD/hour** for instances with 4 or fewer vCPUs
  * **$0.13 USD/hour** for instances with more than 4 vCPUs



RHEL 6 ELS images:

  * **$0.02 USD/hour** for instances with 4 or fewer vCPUs
  * **$0.05 USD/hour** for instances with more than 4 vCPUs



RHEL for SAP with HA and Update Services images:

  * **$0.10 USD/hour** for instances with 4 or fewer vCPUs
  * **$0.225 USD/hour** for instances with more than 4 vCPUs



**Pricing as of July 1, 2024**

RHEL:

  * **$0.0144 USD per core, per hour** for instances with 8 or fewer vCPUs
  * **$0.0108 USD per core, per hour** for instances with 9 to 127 vCPUs
  * **$0.0096 USD per core, per hour** for instances with 128 vCPUs and more



RHEL for SAP:

  * **$0.0225 USD per core, per hour** for instances with 1 to 8 vCPUs
  * **$0.01625 USD per core, per hour** for instances with 9 to 127 vCPUs
  * **$0.01500 USD per core, per hour** for instances with 128 vCPUs and more



RHEL 7 ELS add-on:

  * **$0.0084 USD per core, per hour** for instances with 1 to 8 vCPUs
  * **$0.0060 USD per core, per hour** for instances with 9 to 127 vCPUs
  * **$0.0050 USD per core, per hour** for instances with 128 vCPUs and more



**Calculating Costs**

With this price update, RHEL and RHEL for SAP subscriptions costs will scale linearly with machine size. Instances with 12 vCPUs or less are expected to see equivalent or reduced costs; instances with more than 12 vCPUs are expected to see increased costs. Please use the tables below to estimate how this change will impact your RHEL and RHEL for SAP costs. Prices in this table are estimates only to the RHEL pricing update impact.

**RHEL**

Instance Size| [Old]Instance Hour Price Model| [Current]Core Hour Pricing Model (effective July 1, 2024)  
---|---|---  
2 vCPUs| $0.06/hour * 730 hours/month= $43.8/month| $0.0144/hour * 730 hours/month * 2 cores= $21.02/month  
4 vCPUs| $0.06/hour * 730 hours/month= $43.8/month| $0.0144/hour * 730 hours/month * 4 cores= $42.05/month  
16 vCPUs| $0.13/hour * 730 hours/month= $94.9/month| $0.0108/hour * 730 hours/month * 16 cores= $126.14/month  
128 vCPUs| $0.13/hour * 730 hours/month= $94.9/month| $0.0096/hour * 730 hours/month * 128 cores= $897.02/month  
  
**RHEL for SAP**

Instance Size| [Old]Instance Hour Price Model| [Current]Core Hour Pricing Model (effective July 1, 2024)  
---|---|---  
2 vCPUs| $0.100/hour * 730 hours/month= $73.00/month| $0.02250/hour * 730 hours/month * 2 cores= $32.85/month  
4 vCPUs| $0.100/hour * 730 hours/month= $73.00/month| $0.02250/hour * 730 hours/month * 4 cores= $65.70/month  
16 vCPUs| $0.225/hour * 730 hours/month= $164.25/month| $0.01625/hour * 730 hours/month * 16 cores= $189.80/month  
128 vCPUs| $0.225/hour * 730 hours/month= $164.25/month| $0.01500/hour * 730 hours/month * 128 cores= $1,401.60/month  
  
**Committed Use Discounts for RHEL**

By purchasing a 1-year commitment for RHEL images you can save up to 20% over the on-demand image price.

HourlyHourly

MonthlyMonthly

Instance vCPU count| On demand price per core| 1-year commitment  
---|---|---  
1-8| $0.0144 / 1 hour| $0.01152 / 1 hour  
9-127| $0.0108 / 1 hour| $0.00864 / 1 hour  
128+| $0.0096 / 1 hour| $0.00768 / 1 hour  
  
All RHEL and RHEL for SAP images are charged a **1 minute** minimum. After 1 minute, RHEL images are charged in **1 second increments**.

**If you have concerns over RHEL and RHEL for SAP software costs, contact your Google Cloud account representative.**

To offset any significant cost increases as a result of this pricing model update, Red Hat and Google have partnered to provide promotional offers to eligible customers, subject to approval from Red Hat. To learn more about the promotional offers for RHEL and RHEL for SAP licenses, contact your Google Cloud account representative.

**Note:** Commitments for RHEL for SAP are unavailable for purchase as Google transitions into the [new RHEL pricing model](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement).

### 

SUSE Linux Enterprise Server (SLES) and SLES for SAP images

SLES images:

  * **$0.02 USD/hour** for f1-micro and g1-small machine types
  * **$0.11 USD/hour** for all other machine types



SLES for SAP images:

  * **$0.17 USD/hour** for instances with 1 - 2 vCPUs
  * **$0.34 USD/hour** for instances with 3 - 4 vCPUs
  * **$0.41 USD/hour** for instances with 5 or more vCPUs



All SLES images are charged a **1 minute** minimum. After 1 minute, SLES images are charged in **1 second increments**.

You can purchase commitments and receive committed use discounts (CUDs) for your SUSE Linux Enterprise Server (SLES) and SLES for SAP licenses. Because you commit to a minimum level of resource usage when you purchase your license commitment, you have to pay the agreed-upon prices for the duration of that commitment, even if your resource usage is lower than that minimum level. As a result, to maximize the benefit of your CUDs, ensure that you use all of your committed licenses and run VMs with those licenses for 100% time of your commitment's term. To learn more about CUDs for licenses and how to purchase a commitment, see [Purchase commitments for licenses](https://web.archive.org/web/20241007153833/https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchaselicensecommitment).

  


#### On-demand and discounted pricing for SLES images

By purchasing a 1- or 3-year commitment for SLES images you can save up to 79% over the on-demand image price.

HourlyHourly

MonthlyMonthly

SKU name| On-demand| 1-year commitment| 3-year commitment  
---|---|---|---  
SLES, 1-2 virtual cores| $0.11 / 1 hour| $0.025 / 1 hour| $0.023 / 1 hour  
SLES, 3-4 virtual cores| $0.11 / 1 hour| $0.05 / 1 hour| $0.045 / 1 hour  
SLES, 5+ virtual cores| $0.11 / 1 hour| $0.06 / 1 hour| $0.054 / 1 hour  
  
#### On-demand and discounted pricing for SLES for SAP images

By purchasing a 1- or 3-year commitment for SLES SAP images you can save up to 63% over the on-demand image price.

HourlyHourly

MonthlyMonthly

SKU name| On-demand| 1-year commitment| 3-year commitment  
---|---|---|---  
SLES for SAP, 1-2 virtual cores| $0.17 / 1 hour| $0.0685 / 1 hour| $0.06126 / 1 hour  
SLES for SAP, 3-4 virtual cores| $0.34 / 1 hour| $0.137 / 1 hour| $0.1225 / 1 hour  
SLES for SAP, 5+ virtual cores| $0.41 / 1 hour| $0.1643 / 1 hour| $0.1476 / 1 hour  
  
SUSE and Google have partnered to provide promotional offers to eligible customers, subject to approval from SUSE. If you would like to discuss any promotional offers on SLES and SLES for SAP licenses, contact your Google Cloud account representative.

### 

Ubuntu Pro

The following sections outline the license cost for using Ubuntu Pro images on Compute Engine. When running VMs that use the premium Ubuntu Pro images, you incur license cost in addition to the regular cost of running the VM. For VM pricing, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).

The license cost for running Ubuntu Pro VMs, per hour, on Compute Engine is calculated as follows:

(license cost for RAM per GB per hour) + (license cost for vCPU per hour)

**Memory**

License cost for memory is charged at one flat rate of **$0.000127** per GB/hour in USD.

**vCPU**

License cost for vCPU varies by the number of vCPUs that the Ubuntu Pro VM has. The following table summarizes the license cost per hour in USD.

HourlyHourly

MonthlyMonthly

Number of vCPUs| License cost (USD)/hour  
---|---  
1| $0.00166 / 1 hour  
2| $0.002971 / 1 hour  
4| $0.005545 / 1 hour  
6 - 8| $0.00997 / 1 hour  
10-16| $0.018063 / 1 hour  
18 - 48| $0.033378 / 1 hour  
50 - 78| $0.060548 / 1 hour  
80 - 96| $0.077871 / 1 hour  
98 - 222| $0.102401 / 1 hour  
>222| $0.122063 / 1 hour  
  
**Example**

For example, if your Ubuntu Pro VM has 64 GB RAM and 16 vCPUs, the license cost is calculated as follows:

Hourly license cost per VM = (0.000127 * 64) + (0.018063) = **$0.026191**

Monthly license cost (31 day month) per VM = 0.026191 * 744 = **$19.486104**

#### Ubuntu pro with attached GPUs license costs

The following sections outline only the license cost for using Ubuntu Pro images with attached GPUs on Compute Engine. When running VMs that use the premium Ubuntu Pro images with attached GPUs, you incur license cost for the premium image and a GPU license in addition to the regular cost of running the VM and the cost of the attached GPU.

  * For VM cost, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * For GPU cost, see [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



The license cost of running Ubuntu VMs with attached GPU, per hour, is calculated as follows:

(license cost for RAM per GB per hour) + (license cost for vCPU per hour) + (license cost for GPU per hour)

The following table summarizes the per GPU license rates per month in USD for Ubuntu Pro VMs. The license fee varies based on the number of GPUs attached to the VM but is the same for all GPU models that are available on Compute Engine.

HourlyHourly

MonthlyMonthly

Number of GPUs| License cost (USD)  
---|---  
1| $0.035 / 1 hour  
2| $0.066 / 1 hour  
4| $0.12 / 1 hour  
8| $0.208 / 1 hour  
>8| $0.30 / 1 hour  
  
**Example**

For example if your Ubuntu Pro VM has 64 GB RAM, 16 vCPUs and 4 GPUs attached, the per hour license cost is calculated as follows:

Hourly license cost per VM = (0.000127 * 64) + (0.018063) + (0.120) = **$0.146191**

Monthly license cost (31 day month) per VM = 0.146191 * 744 = **108.766104**

### 

Windows Server images

If you use a [Compute Engine Windows Server image](https://cloud.google.com/compute/docs/images/os-details#windows_server) or you import a Windows Server image without [bringing your own licenses](https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses), you are billed based on the [machine types](https://cloud.google.com/compute/docs/machine-types) you use as follows:

  * f1-micro and g1-small machine types: **$0.023 USD/hour**.
  * All other machine types: **$0.046 USD/hour per visible vCPU**. For example, n2-highcpu-4, and n2-highmem-4 have 4 vCPUs, so are charged at $0.184 USD/hour (4 x $0.046 USD/hour).



Windows Server images are charged a **1 minute minimum**. After 1 minute, Windows images are charged in **1 second increments**.

For information about licensing for Windows Server images, see [Microsoft licenses](https://cloud.google.com/compute/docs/instances/ms-licensing).

### 

SQL Server images

[SQL Server images](https://cloud.google.com/compute/docs/images/os-details#sql_server) incur costs in addition to the cost for [Windows Server images](https://cloud.google.com/compute/disks-image-pricing#windows_server_pricing) and the cost for the selected machine type.

  * **$0.399 USD per core/hour** for SQL Server Enterprise
  * **$0.1200 USD per core/hour** for SQL Server Standard
  * **$0.011 USD per core/hour** for SQL Server Web
  * No additional charge for SQL Server Express



Microsoft SQL Server licensing requires a core license to be assigned to each virtual CPU on your virtual machine instance, with a four core minimum for each instance. Instances with fewer than 4 vCPUs will be charged for 4 vCPUs to comply with these requirements.

Google recommends that you not use SQL Server images on f1-micro or g1-small [machine types](https://cloud.google.com/compute/docs/machine-types) based on Microsoft's [minimum hardware and software recommendations](https://msdn.microsoft.com/en-us/library/ms143506.aspx).

SQL Server images are charged a **1 minute minimum**. After 1 minute, SQL Server images are charged in **1 second increments**.

For information about licensing for SQL Server OS images, see [Microsoft licenses](https://cloud.google.com/compute/docs/instances/ms-licensing).

## 

Disk pricing

Each VM has at least one disk attached to it. Each disk incurs a cost, described in this section. In addition, if you back up the disk with [standard snapshots](https://cloud.google.com/compute/docs/disks/snapshots) or [instant snapshots](https://cloud.google.com/compute/docs/disks/instant-snapshots) separate charges apply.

All disk-related charges in this section are prorated based on a granularity of seconds. This includes all persistent disk types, snapshot storage, and Local SSD pricing.

For example, based off US pricing, a 200 GB standard Persistent Disk volume would cost $8.00 for the whole month. If you provisioned a 200 GB volume for only half a month, it would cost $4.00. Likewise, a 200 GB SSD Persistent Disk volume would cost $34.00 for the whole month. If you provisioned a 200 GB volume for only half a month, it would cost $17.00.

Provisioned disk space includes all used and unused space. If you provision a 200 GB disk, you are billed for that entire disk space, regardless of how you use it, until you relinquish it.

For disk pricing information and rates, see the following sections on this page:

  * [Persistent Disk and Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistent-disk-and-hyperdisk-pricing)
  * [Disk snapshots](https://docs.cloud.google.com/compute/disks-image-pricing#disk-snapshot-pricing)
  * [Standard snapshot pricing](https://docs.cloud.google.com/compute/disks-image-pricing#standard-snapshot-pricing)
  * [Regional standard snapshots pricing](https://docs.cloud.google.com/compute/disks-image-pricing#regional-standard-snapshot-pricing)
  * [Multi-regional standard snapshots pricing](https://docs.cloud.google.com/compute/disks-image-pricing#multi-regional-standard-snapshots-pricing)
  * [Network charges for standard snapshot creation and restoration](https://docs.cloud.google.com/compute/disks-image-pricing#network-charges-snapshot)
  * [Instant snapshots](https://docs.cloud.google.com/compute/disks-image-pricing#instant-snapshots)
  * [Local SSD pricing](https://docs.cloud.google.com/compute/disks-image-pricing#local-ssd)
  * [Asynchronous Replication](https://docs.cloud.google.com/compute/disks-image-pricing#asynchronous-replication)



### 

Persistent Disk and Hyperdisk pricing

  * Standard, SSD, and balanced Persistent Disks are priced by the amount of provisioned space per disk. For these disk types, I/O operations are included in the price for provisioned space. Since disk performance grows linearly with the size of your disk, consider your I/O needs when choosing the size of your disk.



You are billed for the total provisioned capacity of your Hyperdisk volumes until you delete them. You are charged per GiB per month. Additionally, you are billed for the following:

  * Hyperdisk Balanced and Hyperdisk Balanced High Availability charge a monthly rate for the provisioned IOPS and provisioned throughput (in MBps) in excess of the baseline values of 3,000 IOPS and 140 MBps throughput.
  * Hyperdisk Extreme charges a monthly rate based on the provisioned IOPS.
  * Hyperdisk Throughput charges a monthly rate based on the provisioned throughput (in MBps).



For more information about the different types of persistent disk, see the [Storage options](https://cloud.google.com/compute/docs/disks).

After you successfully delete a persistent disk, you are no longer charged for that disk.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Standard provisioned space| 0 gibibyte month to 30 gibibyte month$0.00 (Free) / 1 gibibyte hour, per 1 month / account30 gibibyte month and above$0.000054795 / 1 gibibyte hour, per 1 month / account  
SSD provisioned space| $0.000232877 / 1 gibibyte hour  
Balanced provisioned space| $0.000136986 / 1 gibibyte hour  
Extreme provisioned space| $0.000171233 / 1 gibibyte hour  
Extreme provisioned IOPS| $0.000089041 / 1 hour  
Regional standard provisioned space| $0.000109589 / 1 gibibyte hour  
Regional SSD provisioned space| $0.000465753 / 1 gibibyte hour  
Regional balanced provisioned space| $0.000273973 / 1 gibibyte hour  
Hyperdisk Extreme provisioned space| $0.000171233 / 1 gibibyte hour  
Hyperdisk Extreme provisioned IOPS| $0.000043836 / 1 hour  
Hyperdisk Throughput provisioned space| $0.000006849 / 1 gibibyte hour  
Hyperdisk Throughput provisioned throughput| $0.000342466 / 1 hour  
Hyperdisk Balanced provisioned space| $0.000109589 / 1 gibibyte hour  
Hyperdisk Balanced provisioned IOPS| $0.000006849 / 1 hour  
Hyperdisk Balanced provisioned throughput| $0.000054795 / 1 hour  
Hyperdisk Balanced High Availability provisioned space| $0.000219178 / 1 gibibyte hour  
Hyperdisk Balanced High Availability provisioned IOPS| $0.000013699 / 1 hour  
Hyperdisk Balanced High Availability provisioned throughput| $0.000109589 / 1 hour  
Hyperdisk Storage Pool Throughput provisioned space standard| $0.000006849 / 1 gibibyte hour  
Hyperdisk Storage Pool Throughput provisioned space advanced| $0.000012329 / 1 gibibyte hour  
Hyperdisk Storage Pool Throughput provisioned throughput standard| $0.000342466 / 1 hour  
Hyperdisk Storage Pool Throughput provisioned throughput advanced| $0.000650685 / 1 hour  
Hyperdisk Storage Pool Balanced provisioned space standard| $0.000109589 / 1 gibibyte hour  
Hyperdisk Storage Pool Balanced provisioned space advanced| $0.000191781 / 1 gibibyte hour  
Hyperdisk Storage Pool Balanced provisioned IOPS standard| $0.000006849 / 1 hour  
Hyperdisk Storage Pool Balanced provisioned IOPS advanced| $0.000012329 / 1 gibibyte hour  
Hyperdisk Storage Pool Balanced provisioned throughput standard| $0.000054795 / 1 hour  
Hyperdisk Storage Pool Balanced provisioned throughput advanced| $0.00010411 / 1 hour  
Hyperdisk ML provisioned space| $0.000109589 / 1 gibibyte hour  
Hyperdisk ML provisioned throughput| $0.000164384 / 1 hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Disk snapshot pricing

You can backup disks with standard, instant, and archive snapshots. Archive and standard snapshots are remote disk backups, while instant snapshots are local disk backups.

Unless otherwise specified, references to standard snapshots include archive snapshots.

### 

Standard snapshot pricing

All standard snapshots in a project incur monthly storage fees. Whenever you create or restore a standard snapshot, you might also incur network fees based on the storage location of the snapshot.

**Note:** Pricing changes were introduced for standard snapshots on **October 1, 2022**. For more information, see [Announcement of upcoming pricing changes for disk snapshots](https://cloud.google.com/compute/pricing-announce).

Standard snapshots incur monthly storage charges as long as they exist in your project. Standard snapshots only incur charges for the total size of the snapshots. For example, if you only used 2 TiB of disk space on a 5 TiB disk, your snapshot size is charged for the resulting compressed storage of the 2 TiB that were used, rather than the full 5 TiB of provisioned disk space. Standard and archive snapshots are [incremental snapshots](https://cloud.google.com/compute/docs/disks/create-snapshots), which contain only the data that has changed since the previous snapshot, providing for a generally lower cost for snapshot storage. When you delete a complete or incremental snapshot, some of its data may move to the next incremental snapshot in the snapshot chain. This additional data increases the storage cost because you are using more space in the storage system.

Standard snapshot storage charges, like disk-related charges, are prorated based on a granularity of seconds.

Starting on April 1, 2023, standard snapshot storage will have a minimum billing period of 1 hour. Archive snapshots are billed for a minimum of 90 days of storage, and also billed for retrieval charges when used to create a disk.

### 

Pricing example

For example, if you create a **100 GB** standard snapshot in the **us-central1** region (where the standard snapshot storage rate and standard snapshot recycle bin storage rate are both $0.05 per GB per month), store for **15 days** , and then delete it. After deletion, it is held in the Recycle Bin for **3 days** (default; configurable) prior to permanent erasure.

  * **Standard Storage (15 days):**
  * Monthly rate for 100 GB: 100 GB * $0.05/GB-month = $5.00/month
  * Hourly rate (based on a 730-hour month): $5.00 / 730 hours ≈ $0.0068493/hour
  * Standard storage cost for 360 hours (15 days): 360 hours * $0.0068493/hour ≈ $2.47
  * **Recycle Bin Storage (3 days):**
  * **During Public Preview:** Recycle Bin storage is **100% discounted** , making the Recycle Bin cost $0.00.
  * **After General Availability (GA):** Storage is billed at the standard monthly regional rates. Charges for 72 hours of retention (3 days): 72 hours * $0.0068493/hour ≈ $0.49.
  * **Total Storage Cost:**
  * **During Public Preview** : ~$2.47 (Standard Storage) + $0.00 (Recycle Bin) = ~$2.47
  * **After GA:** ~$2.47 (Standard Storage) + ~$1.15 (Recycle Bin) = ~$3.62



### 

Additional Information

**Standard Snapshot Storage:**

  * **Compressed and Incremental:** Standard snapshots are incremental. You are billed based on the compressed size of the data that has changed since the previous snapshot.
  * **Minimum Billing Duration:** Both standard snapshot storage and recycle bin storage are billed to a minimum duration of 1 hour.
  * **Recycle Bin Support:** The Recycle Bin feature currently **only covers Standard Snapshots**. _Archive Snapshots_ and _Instant Snapshots_ are explicitly **not supported** by the Recycle Bin and will continue to be permanently deleted immediately upon execution.
  * **No Operational or Retrieval Charges for Recycle Bin:** There are **no charges** for individual lifecycle operations, such as moving a snapshot to the Recycle Bin, permanently deleting a recoverable snapshot, or recovering a snapshot back to an active state.
  * **100% Preview Discount for Recycle Bin:** During the Public Preview phase, Recycle Bin storage is 100% discounted. Standard storage rates will apply automatically upon General Availability (GA).



### 

Regional standard snapshots pricing

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Standard snapshot storage| $0.000068493 / 1 gibibyte hour  
Standard snapshot recycle bin storage| $0.000068493 / 1 gibibyte hour  
Archive snapshot storage| $0.000026027 / 1 gibibyte hour  
Archive snapshot retrieval| $0.019 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Multi-regional standard snapshots pricing

Asia (asia)

  * Asia (asia)
  * Europe (eu)
  * US (us)



HourlyHourly

MonthlyMonthly

Type| **Price (USD)**  
---|---  
Multi-regional standard snapshot storage| $0.000113699 / 1 gibibyte hour  
Multi-regional standard snapshot recycle bin storage| $0.000113699 / 1 gibibyte hour  
Multi-regional archive snapshot storage| $0.000042466 / 1 gibibyte hour  
Multi-regional archive snapshot retrieval| $0.031 / 1 gibibyte  
Multi-regional snapshot download| $0.08 / 1 gibibyte  
Multi-regional snapshot upload| $0.08 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

If you don't require the additional replication and resilience of multi-regional standard snapshots, we recommend using regional standard snapshots by specifying a regional location when snapshots are created.

### 

Network charges for standard snapshot creation and restoration

Network charges are billed under Compute Engine. Standard snapshot storage is compressed.

| North America| Europe| Asia| Indonesia| Oceania| Middle East| **Latin America**  
---|---|---|---|---|---|---|---  
**North America**|  $0.02 / 1 gibibyte| $0.05 / 1 gibibyte| $0.08 / 1 gibibyte| $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.11 / 1 gibibyte| $0.14 / 1 gibibyte  
**Europe**|  $0.05 / 1 gibibyte| $0.02 / 1 gibibyte| $0.08 / 1 gibibyte| $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.11 / 1 gibibyte| $0.14 / 1 gibibyte  
**Asia**|  $0.08 / 1 gibibyte| $0.08 / 1 gibibyte| $0.08 / 1 gibibyte| $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.11 / 1 gibibyte| $0.14 / 1 gibibyte  
**Indonesia**|  $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| N/A| $0.08 / 1 gibibyte| $0.11 / 1 gibibyte| $0.14 / 1 gibibyte  
**Oceania**|  $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.10 / 1 gibibyte| $0.08 / 1 gibibyte| $0.08 / 1 gibibyte| $0.11 / 1 gibibyte| $0.14 / 1 gibibyte  
**Middle East**|  $0.11 / 1 gibibyte| $0.11 / 1 gibibyte| $0.11 / 1 gibibyte| $0.11 / 1 gibibyte| $0.11 / 1 gibibyte| $0.08 / 1 gibibyte| $0.14 / 1 gibibyte  
**Latin America**|  $0.14 / 1 gibibyte| $0.14 / 1 gibibyte| $0.14 / 1 gibibyte| $0.14 / 1 gibibyte| $0.14 / 1 gibibyte| $0.14 / 1 gibibyte| $0.14 / 1 gibibyte  
  
Note that Compute Engine regions and Cloud Storage regions have similar names. Each multi-region contains multiple regions, and each region contains multiple zones. For example, the zone europe-north1-a is part of the europe-north1 region, and europe-north1 is part of the eu multi-region.

If you create or restore a standard snapshot that is stored in a different location than the disk, the data travels over the network between those locations and may incur network fees.

For example, if your disk is located in the us-central1 region, and you make a snapshot to us multi-region, or a different region such as us-west1, you will incur a network charge. A standard snapshot of this disk to the same us-central1 region would not incur a network charge.

Feature| Pricing Launch Date| Examples  
---|---|---  
**Inter-region standard snapshot egress**|  Price changes on [April 1](https://cloud.google.com/compute/pricing-announce#pd_snapshot_egress_skus), 2023| \- Create a standard snapshot in Iowa from a disk in Virginia\- Create a disk in Iowa from a standard snapshot in London\- Create a standard snapshot in US multi-region from a disk in London  
**Multi-region standard snapshot download within the multi-region (create disk)**|  New SKUs as of [April 1](https://cloud.google.com/compute/pricing-announce#multi-regional_snapshot_download), 2023| \- Create a disk in Iowa from a snapshot in US multi-region\- Create a disk in Frankfurt from a snapshot in EU multi-region  
**Multi-region standard snapshot upload within the multi-region (create snapshot)**|  New SKUs as of [April 1](https://cloud.google.com/compute/pricing-announce#multi-regional_snapshot_upload), 2023| \- Create a standard snapshot in US multi-region from a disk in Iowa\- Create a standard snapshot in EU multi-region from a disk in London  
  
### 

Instant Snapshots

[Instant snapshots](https://cloud.google.com/compute/docs/disks/instant-snapshots) provide a near-instantaneous, point-in-time backup of a disk. They are ideal for protecting workloads from application-level data corruption, user error, or bad software upgrades. The point-in-time backups are read-only, frozen views of a disk or volume and serve as short-term, online backups. They are optimized for recovery scenarios where the zone and disk are intact but the data must be quickly restored.

Pricing is based on two components:

  * A per-operation charge to create an instant snapshot.
  * A per-GiB storage charge for differential data that has changed on the disk since the snapshot was taken. The price will be the same as that of the underlying storage.



Instant Snapshot operations in all regions are charged 0.05 USD per operation

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Balanced PD Instant Snapshot data storage| $0.000136986 / 1 gibibyte hour  
Extreme PD Instant Snapshot data storage| $0.000260274 / 1 gibibyte hour  
SSD PD Instant Snapshot data storage| $0.000232877 / 1 gibibyte hour  
Standard PD Instant Snapshot data storage| $0.000054795 / 1 gibibyte hour  
Regional Balanced PD Instant Snapshot data storage| $0.000273973 / 1 gibibyte hour  
Regional SSD PD Instant Snapshot data storage| $0.000465753 / 1 gibibyte hour  
Regional Standard PD Instant Snapshot data storage| $0.000109589 / 1 gibibyte hour  
Hyperdisk Balanced Instant Snapshot data storage| $0.000109589 / 1 gibibyte hour  
Hyperdisk Balanced High Availability Instant Snapshot data storage| $0.000219178 / 1 gibibyte hour  
Hyperdisk Extreme Instant Snapshot data storage| $0.000171233 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Local SSD

Local SSD devices are charged for the amount of provisioned space per device for the lifetime of the VM that it is attached to. There are [two types](https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) of Local SSD disks, Titanium SSD and Local SSD. The prices for these Local SSD disks can differ by region, disk type, and machine series. For example, in the Iowa region, Titanium SSDs attached to the [C4 machine series](https://cloud.google.com/compute/vm-instance-pricing?hl=en&e=48754805#section-1) have a different price than Local SSDs attached to the N2 machines. As mentioned earlier, all Local SSD disk charges are prorated to a granularity of seconds.

Local SSD disks can only be purchased in 375 GiB or 3,000 GiB increments, depending on the machine family type. The cost-per-month for a single device is the monthly rate multiplied by the size of the disk. For example, at a monthly rate of $0.080 per GiB and a single 375 GiB disk, the cost would be $30.00 per device per month. Actual data storage and usage are included in that price and there is no additional charge for local traffic between the virtual machine and the Local SSD device.

For Resource-based CUD pricing for Local SSD disks, a reservation must be created when purchasing the commitment. For Compute Flexible CUD pricing a reservation is not required. For more information on reservations see [Reserving zonal resources](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources).

Spot prices apply to Local SSD disks attached to [Spot VMs](https://cloud.google.com/compute/docs/instances/spot) (or [preemptible VMs](https://cloud.google.com/compute/docs/instances/preemptible)). Spot prices provide smaller discounts for Local SSD disks than for machine types and GPUs. Local SSD disks attached to Spot VMs are not eligible for other discounts.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Type| Default* (USD)_info_

## Consumption model ID:

7754-699E-0EBF| Compute Flexible CUD - 1 Year* (USD)_info_

## Consumption model ID:

D97B-0795-975B| Compute Flexible CUD - 3 Year* (USD)_info_

## Consumption model ID:

70D7-D1AB-12A4| Compute Resource CUDs - 1 Year (USD)| Compute Resource CUDs - 3 Year (USD)  
---|---|---|---|---|---  
Local SSD provisioned space| $0.000109589 / 1 gibibyte hour| $0.000078904 / 1 gibibyte hour| $0.000059178 / 1 gibibyte hour| $0.000069041 / 1 gibibyte hour| $0.000049315 / 1 gibibyte hour  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

*The Default consumption model for Compute Engine is "On Demand"

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Spot prices are dynamic and can change up to once every 30 days, but provide discounts of 60-91% off of the corresponding on-demand price for most machine types and GPUs. Spot prices also provide smaller discounts for local SSDs and A3 machine types. For more information, see the [Spot VMs](https://cloud.google.com/compute/docs/instances/spot#pricing) documentation.

### 

Asynchronous Replication

Asynchronous Replication allows Compute Engine customers to enable disaster recovery protection for mission-critical workloads that require a low Recovery Point Objective and Recovery Time Objective. Async Replication automatically and periodically replicates data from a disk in a primary region to a disk in a secondary (failover) region, so that workloads can be recovered with minimal data loss and minimal downtime if a disaster occurs.

Pricing is based on the amount of provisioned data being protected, and the amount of data replicated over the network. There is no additional price for Compute Engine VMs to use Async Replication, and no additional Google Cloud resources such as dedicated replication VMs are required.

### 

Pricing based on capacity of data being protected

The **Async Replication Protection SKUs** for Asynchronous Replication apply to primary & secondary disks and are based on the provisioned capacity of the underlying disk. Replication Protection is charged while replication is active, i.e. beginning when disks.startAsyncReplication is called and stopping when disks.stopAsyncReplication is called. This SKU is metered based on GiB-month of the primary and secondary disks, with the price dependent on the location. Usage is metered each second.

Note that primary and secondary disks themselves are billed as ordinary disks based on their type, location, and provisioned size.

Additionally, for Hyperdisk, you are billed for the following:

  * Hyperdisk Balanced and Hyperdisk Balanced High Availability charge a monthly rate for the provisioned IOPS and provisioned throughput (in MBps).
  * Hyperdisk Extreme charges a monthly rate based on the provisioned IOPS



  


Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Asynchronous Replication Protection - PD Balanced| $0.000054795 / 1 gibibyte hour  
Asynchronous Replication Protection - PD SSD| $0.000093151 / 1 gibibyte hour  
Asynchronous Replication Protection - Regional PD Balanced| $0.000109589 / 1 gibibyte hour  
Asynchronous Replication Protection - Regional PD SSD| $0.000186301 / 1 gibibyte hour  
Asynchronous Replication Protection - Hyperdisk Balanced| $0.000043836 / 1 gibibyte hour  
Asynchronous Replication Protection - Hyperdisk Balanced provisioned throughput| $0.000021918 / 1 hour  
Asynchronous Replication Protection - Hyperdisk Balanced provisioned IOPS| $0.00000274 / 1 hour  
Asynchronous Replication Protection - Hyperdisk Balanced High Availability| $0.000087671 / 1 gibibyte hour  
Asynchronous Replication Protection - Hyperdisk Balanced High Availability provisioned throughput| $0.000043836 / 1 hour  
Asynchronous Replication Protection - Hyperdisk Balanced High Availability provisioned IOPS| $0.000005479 / 1 hour  
Asynchronous Replication Protection - Hyperdisk Extreme| $0.000068493 / 1 gibibyte hour  
Asynchronous Replication Protection - Hyperdisk Extreme provisioned IOPS| $0.000017534 / 1 hour  
  
### 

Pricing for data replicated over the network

The **Async Replication Inter-region Network SKUs** meter the replicated data sent between regions. Network charges are applied in the project of the secondary (DR) disk. This SKU is metered based on GiB of network usage, with the price dependent on the location. Usage is metered each second.

Regions| Type| Price (USD)  
---|---|---  
Asia| Asynchronous Replication Networking| $0.08 / 1 gibibyte  
Europe| Asynchronous Replication Networking| $0.02 / 1 gibibyte  
North America| Asynchronous Replication Networking| $0.02 / 1 gibibyte  
Oceania| Asynchronous Replication Networking| $0.08 / 1 gibibyte  
South America| Asynchronous Replication Networking| $0.14 / 1 gibibyte  
  
## 

Custom image storage

If you import or create [custom images](https://cloud.google.com/compute/docs/images#custom_images) in Compute Engine, these images incur a storage cost. The cost of these custom images depends on the location where you store the image. There are no network transfer fees for creating images, nor for creating disks from images.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Image storage| $0.000068493 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Machine images

The cost of using a machine image depends on the size of the machine image, and the location where it is stored.

Creating or restoring a VM from a machine image across different locations may incur inter-region or multi-region network transfer fees.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Machine image| $0.000068493 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## What's next

  * Read the [Compute Engine documentation](https://cloud.google.com/compute/docs).
  * Get started with [Compute Engine](https://cloud.google.com/compute/docs/quickstarts).
  * Learn about [Compute Engine solutions and use cases](https://cloud.google.com/architecture?text=Compute%20Engine).
  * Refer to the [Pricing overview](https://cloud.google.com/pricing) documentation.
  * Try the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator/).
  * Learn more about Compute Engine [storage options](https://cloud.google.com/compute/docs/disks/add-persistent-disk).
  * Learn more about Compute Engine [operating systems](https://cloud.google.com/compute/docs/images).
  * Review [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing), [Networking pricing](https://cloud.google.com/vpc/network-pricing), [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing), or [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

Contact sales[](https://cloud.google.com/contact?direct=true)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact)



 _search_ _send_




[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/compute/disks-image-pricing&hl=en-US&prompt=select_account&service=cloudconsole)

Start free[](https://console.cloud.google.com/freetrial)

Start free[](https://console.cloud.google.com/freetrial)

Contact us[](https://cloud.google.com/contact)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)




  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)




  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)




  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)




close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure Modernization
  * Productivity and Collaboration
  * Security
  * Startups and SMB



See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)


  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)


  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)


  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)


  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)


  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)


  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)


  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)


  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)


  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)


  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)


  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)


  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationModernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Application Modernization with AIAI-assisted code refactoring, assessment, and transformation for legacy applications.](https://cloud.google.com/solutions/application-modernization-with-ai)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Mainframe ModernizationAutomated tools and AI-driven guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)


  * [Database ModernizationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Data Lake ModernizationUnify and govern multimodal data on an open, high-performance cloud data lake.](https://cloud.google.com/solutions/data-lakehouse)


  * [Data Warehouse ModernizationMigrate and modernize your enterprise data warehouse for serverless analytics and AI.](https://cloud.google.com/solutions/data-migration)


  * [APIsUnlock legacy applications and build new digital channels using APIs and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [Platform EngManaged services and golden paths to build, manage, and scale internal developer platforms.](https://cloud.google.com/solutions/platform-engineering)


  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)


  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Gemini for enterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)


  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)


  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)


  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)


  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)


  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)


  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)


  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)


  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)


  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)


  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)


  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)


  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)


  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)


  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)


  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)


  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)


  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)


  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)


  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Rapid Migration and Modernization Program (RaMP)End-to-end migration program to simplify and accelerate your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Data Center ExitsMigration solutions for moving VMs, apps, databases, and workloads out of data centers.](https://cloud.google.com/solutions/data-center-migration)


  * [Application Modernization & MigrationDiscovery, assessment, and migration tools for moving and modernizing applications.](https://cloud.google.com/solutions/application-migration)


  * [Database Modernization & MigrationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Cross-Cloud NetworkingSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)


  * [High Performance Computing (HPC)Compute, storage, and networking options to support any high-performance workload.](https://cloud.google.com/solutions/hpc)


  * [VMwareFully managed, native VMware Cloud Foundation software stack on Google Cloud.](https://cloud.google.com/vmware-engine)


  * [SAPCertified infrastructure and AI solutions for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)


  * [WindowsTools, licenses, and partner solutions for running enterprise Windows workloads.](https://cloud.google.com/windows)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)


  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)


  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)


  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)


  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)


  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)


  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)


  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)


  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)


  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)


  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)


  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)



close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3



See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)


  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)


  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)


  * [Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)


  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)


  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)


  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)


  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)


  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)


  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)


  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)



  * Business Intelligence


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)


  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)


  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)


  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)


  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)


  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)


  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)


  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)


  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)


  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)


  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)


  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)


  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)


  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)


  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)


  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)


  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)


  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)


  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)


  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)


  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)


  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)


  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)


  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)


  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)


  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)


  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)



  * Hybrid and Multicloud


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)


  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)


  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)



  * Industry Specific


  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)


  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)


  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)


  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)


  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)


  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)


  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)


  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)


  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)


  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)


  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)


  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)


  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)


  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)


  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)


  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)


  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)


  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)



  * Media Services


  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)


  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)


  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)


  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)


  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)


  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)


  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)


  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)


  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)


  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)


  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)


  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)


  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)


  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)


  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)


  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)


  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)


  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)


  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)


  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)


  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)


  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)


  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)


  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)


  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)


  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)



  * Productivity and Collaboration


  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)


  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)


  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)


  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)


  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)


  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)


  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)


  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)


  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)


  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)


  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)


  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)


  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)


  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)


  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)


  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)


  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)


  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)


  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)


  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)


  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)



close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)




  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)




  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)




  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)




close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)




  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)




  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)




  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)




close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
    * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
    * arrow_forward
  * [Products](https://cloud.google.com/products)
    * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
    * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
    * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)



  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)


  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Application Modernization with AI](https://cloud.google.com/solutions/application-modernization-with-ai)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Mainframe Modernization](https://cloud.google.com/solutions/mainframe-modernization)
  * [Database Modernization](https://cloud.google.com/products/databases)
  * [Data Lake Modernization](https://cloud.google.com/solutions/data-lakehouse)
  * [Data Warehouse Modernization](https://cloud.google.com/solutions/data-migration)
  * [APIs](https://cloud.google.com/solutions/apis-and-applications)
  * [Platform Eng](https://cloud.google.com/solutions/platform-engineering)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini for enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Rapid Migration and Modernization Program (RaMP)](https://cloud.google.com/solutions/cloud-migration-program)
  * [Data Center Exits](https://cloud.google.com/solutions/data-center-migration)
  * [Application Modernization & Migration](https://cloud.google.com/solutions/application-migration)
  * [Database Modernization & Migration](https://cloud.google.com/products/databases)
  * [Cross-Cloud Networking](https://cloud.google.com/solutions/cross-cloud-network)
  * [High Performance Computing (HPC)](https://cloud.google.com/solutions/hpc)
  * [VMware](https://cloud.google.com/vmware-engine)
  * [SAP](https://cloud.google.com/solutions/sap)
  * [Windows](https://cloud.google.com/windows)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)


  * Featured Products
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)


  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)


  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)


