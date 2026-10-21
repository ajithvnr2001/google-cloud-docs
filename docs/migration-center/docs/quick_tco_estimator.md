---
url: https://docs.cloud.google.com/migration-center/docs/quick_tco_estimator/
title: Estimate Google Cloud costs with Quick TCO Estimator \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:34:57.683039+00:00
---

# Estimate Google Cloud costs with Quick TCO Estimator  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/quick_tco_estimator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Estimate Google Cloud costs with Quick TCO Estimator Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Quick TCO Estimator is a Gemini-powered tool in Google Cloud Migration Center that provides automated Total Cost of Ownership (TCO) estimates for migrating virtual machines (VMs) and infrastructure to Compute Engine.

Quick TCO Estimator is available in the following Google Cloud regions:

  * `us-central1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west4`



For databases, Quick TCO Estimator evaluates TCO based on the VM infrastructure you provide. While you can include SQL Server vCPU counts for licensing estimates, the tool does not accept database-specific inputs such as engine type or size.

To generate an estimate, manually enter infrastructure totals or upload RVTools exports to automatically populate your assessment data.

The Quick TCO Estimator simplifies migration cost assessment with the following key features:

  * **Conversational guidance:** interact with the context-aware AI chat interface to explain complex calculations, apply suggested actions, and navigate the assessment process without the need for manual spreadsheet entry.
  * **Streamlined sizing and pricing:** access improved sizing logic and pricing data directly within the console to model Google Compute Engine deployments.



Quick TCO Estimator is designed to reduce the time it takes to do cost estimations and provides a single work area to manage your end-to-end migration cost estimation.

This page explains how to perform the following tasks:

  * Create a new estimate
  * Refine source parameters
  * View and understand an estimate
  * Use Migration Center chat
  * Generate artifacts



## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a project.
  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [Verify whether billing is enabled for a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. Make sure that you have the necessary Identity and Access Management (IAM) permissions to create and manage estimates in Migration Center. Typically, this requires the **Migration Center Admin** (`roles/migrationcenter.admin`) role. For more information, see [Roles and permissions](https://docs.cloud.google.com/migration-center/docs/roles-and-permissions#manage).
  4. To export your data to Google Sheets, use a **Google Workspace** account.



### Optional: Upload RVTools export data

To use RVTools export data for your estimate, you can optionally upload your RVTools export files first. Alternatively, you will have the option to upload these files when you create a new estimate.

Make sure that your exported files meet the following requirements:

  * **File types:** supported formats are `csv` (specifically `vInfo.csv` and `vDisk.csv`) and `XLSX` workbooks.
  * **Maximum file size:** 10GB per source.
  * **Row limits:** individual `XLSX` tabs (`vInfo` or `vDisk`) must not exceed 1,048,576 rows.
  * **Mandatory headers:** CSV and Excel files must contain standard RVTools headers for automatic identification: 
    * Required headers for `vDisk`: `VM UUID`, `VM`, `Capacity MiB`, `Disk path`, `Disk mode`, and `Powerstate`.
    * Required headers for `vInfo`: `VM UUID`, `VM`, `Host`, `OS according to the configuration file`, `OS according to the VMware Tools`, `Powerstate`, `CPUs`, `Memory`, and `Disks`.



To upload your files, follow these steps:

  1. In the Google Cloud console, go to the Migration Center user interface.

[Go to Migration Center](https://console.cloud.google.com/migration-ai?gtm_source=documentation&gtm_source_id=activate_migration_center_migration_center)

  2. Click **Sources**. The **Upload files** dialog appears.

  3. Click or drag files into the window and click **Upload**.

  4. Upload your RVTools export. You can upload a single CSV (such as `vInfo.csv` or `vDisks.csv`) or a full Excel workbook.

Migration Center automatically classifies the files as RVTools source if the headers match valid definitions. For Excel (`XLSX`) files, the system specifically processes the `vInfo` and `vDisks` tabs to extract inventory data. You can use these source files when creating a new estimate.




## Create a new estimate

To create a new estimate, follow these steps:

  1. In the Google Cloud console, go to the Migration Center user interface.

[Go to Migration Center](https://console.cloud.google.com/migration-ai?gtm_source=documentation&gtm_source_id=activate_migration_center_migration_center)

  2. On the **Quick TCO Estimator** card, click **Show details**.

  3. Click **Create new estimate**.

  4. Enter an estimate name and then click **Next**.

  5. For the source workload, do one of the following:

     * To manually add information about your source workload, follow these steps:

       1. For **Provisioned VMs** , enter the total number of source VMs.
       2. For **Provisioned vCPUs** , enter the total number of vCPUs.
       3. For **Provisioned RAM (GB)** , enter the total amount of RAM in GB.
       4. For **Provisioned Storage (TiB)** , enter the total amount of storage in TiB.
       5. Click **Next**.
       6. For **GCE configuration** , follow these steps: 
          1. In the **Region** drop-down list, select the Google Cloud region for your target infrastructure; for example, `us-central1`.
          2. Under **Machine family** , select the category that best suits your workload requirements, such as **General-purpose** , **Compute-optimized** , or **Memory-optimized**.
          3. In the **Machine series** drop-down list, select the specific series for your VMs; for example, **N4**.
          4. Under **Disk family** , select the storage family for your workload, such as **Persistent Disk** , **Hyperdisk** , or **Hyperdisk Storage Pool**.
          5. Under **Disk type** , select the specific performance tier for your disks; for example, **PD Balanced** , **PD Extreme** , **PD SSD** , or **PD Standard**.
       7. To finalize your configuration and view the migration cost assessment, click **Create estimate**.
     * To use source data from your RVTools export, follow these steps:

       1. Click **Calculate from a source file**.
       2. Select the sources to use from the list of sources or to add a new source, click **Add sources**.
       3. Click **Apply**. An estimate is automatically created based on the uploaded data.



An estimate is created. The Summary tab opens, displaying your projected average TCO and total workload scope.

## Refine source parameters

After creating an estimate, refine the results by modifying source parameters in the following categories.

Use the **Add group** option to define groups. After groups are defined, they act as the primary filter for your assessment results and proposals. This data appears in breakdown pages and exported reports in the following ways:

  * **Technical breakdown** and **Pricing breakdown** : when viewing your assessment results, the system provides a detailed breakdown of Compute Engine configuration and pricing breakdown for each group.

  * **Artifacts** : Google Sheets exports include technical details and cost data, which are categorized into groups to help ensure that you have the data for your business case.




### Footprint scope

Parameters that define the inventory of your source environment and your high-level target preferences in Google Cloud.

  * **Provisioned VMs:** the total number of source virtual machines to be migrated.
  * **Provisioned vCPUs:** the total count of virtual CPUs allocated across all source VMs.
  * **Provisioned RAM:** the total amount of memory in GB allocated across all source VMs.
  * **Provisioned storage:** the total amount of storage in TiB allocated across all source VMs.
  * **Region:** select the Google Cloud region where you plan to deploy these workloads. This choice affects cost estimation.
  * **Machine family:** the general category of the Compute Engine machine type.
  * **Machine series:** the specific Compute Engine generation and type for the target (for example, N2).
  * **Disk family:** the general category of block storage for the target VMs.
  * **Disk type:** the specific storage performance tier to use (for example, Balanced Persistent Disk (`pd-balanced`), Standard Persistent Disk (`pd-standard`)).



### Sizing and optimization

Parameters that refine the target cloud resources based on actual usage and CPU performance.

  * **Monthly uptime:** the expected monthly uptime percentage for workloads to accurately model consumption costs.
  * **Idle machines:** the percentage of servers that are powered on but idle.
  * **On-premises vCPU utilization:** the average vCPU utilization of source servers, used for rightsizing recommendations.
  * **CPU performance:** enable this to reduce required vCPUs based on the performance improvements of Google Cloud CPUs over on-premises hardware.
  * **Disable SMT:** enable this to run on one thread per core instead of two, which can reduce certain licensing costs.
  * **On-premises memory utilization:** the average or peak memory usage of active on-premises servers.
  * **On-premises disk utilization:** the portion of disk space that is actually consumed by data on the source servers.
  * **Storage headroom:** a percentage of additional storage to allocate beyond the source configuration for future growth.
  * **Network cost:** estimated network spend expressed as a percentage of total compute and storage costs.



### Premium OS licenses

Parameters that specify the number of vCPUs requiring specific third-party software licenses.

  * **RHEL 7 ELS add-on:** number of Red Hat Enterprise Linux (RHEL) 7 Extended Lifecycle Support (ELS) add-on, which is a specific license for organizations running RHEL 7 workloads that have moved past their standard maintenance period.
  * **RHEL:** number of vCPUs requiring Red Hat Enterprise Linux licenses.
  * **Ubuntu Pro:** number of vCPUs requiring Ubuntu Pro licenses.
  * **SLES:** number of vCPUs requiring SUSE Linux Enterprise Server licenses.
  * **Windows Server:** number of vCPUs requiring Windows Server licenses.
  * **SQL Enterprise / Standard / Web:** number of vCPUs requiring specific Microsoft SQL Server license tiers.



### Pricing

Parameters to configure discounts and additional funding to refine the TCO.

  * **CUDs plan:** select a Committed Use Discounts (CUDs) plan (for example, Standard 3 years) for reduced rates.
  * **EDP or GCE discount:** enter a percentage discount from an Enterprise Discount Program or other Compute Engine incentives.
  * **Partner services funding:** enter any expected funding provided by partners in USD.
  * **Spend milestone credits:** enter credits anticipated from meeting specific spend milestones.



### Migration and support

Parameters for operational and migration-specific costs.

  * **Migration cost per VM:** the estimated one-time cost to migrate a single virtual machine.
  * **Support level:** select the Google Cloud support tier (for example, Standard) for inclusion in the cost estimate.



### On-premises assumptions

Parameters that define financial and technical baselines for the current environment to ensure accurate TCO comparisons.

##### Performance and capacity

  * **CPU burst:** percentage of vCPU capacity reserved to handle usage spikes.
  * **Memory burst:** percentage of additional RAM reserved for source requirements.
  * **vCPU to core ratio:** number of virtual CPUs allocated per physical core.
  * **Storage redundancy policy:** redundancy policy (for example, FTT1/R1) determining the raw disk space required.



##### Financial & OpEx

  * **Hardware Life (Years):** useful lifespan of source hardware for amortization calculations.
  * **Raw Storage Price ($/GiB):** estimated market list price per GiB of raw storage.
  * **Monthly DC Cost ($/Host):** monthly cost per host covering rack space, power, cooling, and maintenance.
  * **IT Ops Annual Salary ($):** average annual cost for one full-time IT operations employee.
  * **Hosts per Server / Network / Security Admin:** ratios used to calculate the number of administrators required based on host count.



## View and understand an estimate

After you create an estimate, the Quick TCO Estimator displays the results across three tabs: **Summary** , **Technical breakdown** , and **Pricing breakdown**.

### Summary page

The **Summary** page provides a high-level executive overview of the projected migration outcomes. To view this page, click the **Summary** tab. The **Summary** tab includes the following elements:

  * **Average GCE TCO:** displays the average yearly and monthly GCE TCO (Total Cost of Ownership) along with the estimated percentage of savings.
  * **Total workload scope:** shows the "right-sizing" comparison between the source environment and the target cloud environment, specifically for vCPU, memory, and storage.
  * **5-year TCO:** displays the total cost of ownership comparison over a 5-year period for Google Cloud and on-premises environments.
  * **Configuration:** lets you adjust the footprint scope (for example, number of VMs) and infrastructure preferences (for example, region and machine family) directly from the dashboard.



### Technical breakdown page

The **Technical breakdown** page offers a detailed comparison of parameters between the cloud configuration and on-premises estimations. To view this page, click the **Technical breakdown** tab. The page contains the following details:

  * **GCE Configuration:** lists specific target settings for the cloud environment, including the machine series (N2), vCPUs, memory, disk type (for example, Balanced Persistent Disk (`pd-balanced`), Standard Persistent Disk (`pd-standard`)), and Provisioned IOPS.
  * **On-premises Estimations:** provides "best fit" hardware recommendations for comparison, such as server models (for example, Xeon Gold) and host counts.
  * **Detailed Metrics:** includes advanced technical parameters like SMT status and CPU performance.



### Pricing breakdown page

The **Pricing breakdown** page shows you a granular view of costs divided into specific components. To view this page, click the **Pricing breakdown** tab. The page contains the following details:

  * **Cost Components:** breaks down expenses into categories such as Compute, Storage, Network, Operation, and OS licenses.
  * **Default VM group:** displays the pricing details for the default group of virtual machines, categorized by cost components.
  * **Annual TCO:** provides the total cost of ownership comparison for one year between Google Cloud and on-premises environments.
  * **5-year TCO:** provides the total cost of ownership comparison over five years between Google Cloud and on-premises environments.



## Use Migration Center chat

Migration Center chat uses a dynamic, interactive interface to guide you through cloud assessment and planning. This interface features a Gemini-powered chat assistant and an **Artifacts** section that stores the outputs of your analysis.

Use Migration Center chat to gather insights and generate quick estimates using natural language:

  * **Get quick estimates:** use the chat to generate a capacity-based TCO estimate with minimal input.
  * **Use suggested prompts:** click predefined prompts to learn how costs are calculated or to explore optimization strategies.
  * **Get contextual assistance:** ask specific questions about your configuration, such as `How does N4 series compare to E2 for this workload?`.



To ask a question or request an action, enter a prompt in the field at the bottom of the chat panel. To start a new conversation, click **Clear chat**.

## Generate artifacts

The **Artifacts** section is a centralized repository for the documents, reports, and spreadsheets that you generate during your assessment.

Key artifacts include the following:

  * **Google Sheets:** provides a migration sizing and TCO analysis of your current-state inventory, technical details, and the detailed BOM and prices.



In the **Artifacts** section, you can perform the following actions:

  * To export your inventory or pricing data for further analysis, click **Create sheet**.

  * To organize your saved documents, click **Sort by**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
