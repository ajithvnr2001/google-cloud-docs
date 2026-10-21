---
url: https://docs.cloud.google.com/migration-center/docs/release-notes/
title: Google Cloud Migration Center release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:19.930150+00:00
---

# Google Cloud Migration Center release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Resources ](https://docs.cloud.google.com/migration-center/docs/release-notes)



Send feedback 

#  Google Cloud Migration Center release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud Migration Center. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/migrationcenter-release-notes.xml) directly. 

## July 07, 2026

Announcement

The [discovery client 6.3.14](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with a new feature and bug fixes.

Feature

**Preview:** Added support for discovery of the following assets from your AWS account:

  * Amazon Athena workgroups
  * Amazon Elastic MapReduce (EMR)
  * Amazon Data Firehose
  * AWS Glue
  * Amazon Kinesis Data Streams (KDS)
  * Amazon ElastiCache



For more information, see [Discover assets on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets) and [Directly import asset inventory data from AWS](https://docs.cloud.google.com/migration-center/docs/aws-import-data).

Fixed

  * Fixed an issue in the Linux performance collection script where the output file had insufficient permissions, preventing access by the original non-root user when the script was run with root privileges.

  * Fixed an issue that caused an incorrect memory utilization report for Amazon Relational Database Service (Amazon RDS) and Azure virtual machine (VM) instances.

  * Fixed an issue that could cause failures when uploading collected database information to Migration Center.




## June 29, 2026

Feature

**Preview:** Quick TCO Estimator is now available in the following regions: `us-central1`, `europe-west1`, `europe-west2`, and `europe-west4`.

Quick TCO Estimator is a Gemini-powered tool in Migration Center that provides automated Total Cost of Ownership (TCO) estimates for migrating virtual machines (VMs) and infrastructure to Compute Engine.

For more information, see [Estimate cloud costs with Quick TCO Estimator](https://docs.cloud.google.com/migration-center/docs/quick_tco_estimator).

## March 30, 2026

Announcement

The [discovery client 6.3.13](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with a new feature and a bug fix.

Feature

**Preview:** Added support for discovery of the following assets from your AWS account:

  * Amazon API Gateway
  * Amazon EC2 Auto Scaling
  * Amazon Elastic Block Store (EBS)
  * Amazon Elastic Container Registry (ECR)
  * Amazon Simple Notification Service (SNS)
  * AWS Application Load Balancer (ALB)
  * AWS AppSync
  * AWS Batch
  * AWS Internet Gateway
  * Elastic IP address (EIP)
  * Elastic Network Interface (ENI)



For more information, see [Discover assets on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets) and [Directly import asset inventory data from AWS](https://docs.cloud.google.com/migration-center/docs/aws-import-data).

Fixed

Fixed an issue where some supported operating systems from the [vSphere guest OS list](https://knowledge.broadcom.com/external/article/321876/determine-the-guest-os-from-a-vm-configu.html) were missing from the discovered assets. The discovery client now uses the VMware vSphere API to collect all supported OS families.

## February 26, 2026

Feature

**Preview:** When visualizing network dependencies in Migration Center, you can now tag assets and filter the dependency graph based on groups, network, and asset details.

For more information, see [Visualize network dependencies](https://docs.cloud.google.com/migration-center/docs/visualize-network-dependencies).

## February 02, 2026

Feature

Migration Center now lets you configure sizing recommendations for your migrated assets. You can define a target sizing strategy, set default utilization estimates for assets that lack performance data, and specify network data transfer out preferences to better estimate your total cost of ownership (TCO).

For more information, see [Sizing and network preferences](https://docs.cloud.google.com/migration-center/docs/server-preferences#sizing-optimization).

Feature

When configuring migration preferences for Compute Engine, you can now select between **Multi-tenant** (default) or **Sole-tenant** preference modes.

For more information, see [Google Compute Engine preferences](https://docs.cloud.google.com/migration-center/docs/server-preferences#compute-engine).

## January 26, 2026

Announcement

The [discovery client 6.3.12](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with a bug fix.

Fixed

Fixed a bug in the MCDC guest collection script.

The guest collection process no longer runs Java or application binaries (Tomcat and JBoss) on target servers. Version identification for Tomcat and JBoss now relies exclusively on static configuration and the release notes.

## January 07, 2026

Announcement

The [discovery client 6.3.11](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Feature

The Migration Center discovery client CLI (`mcdc` CLI) now uses remote WMI collections by default for Windows guest host collections to improve efficiency. This method replaces the use of local collection scripts.

If script-based collection is required for earlier Windows versions (such as Windows Server 2008), you can deactivate this functionality with the `--script` flag.

For more information, see [Collect data remotely over WMI](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery#collect_data_remotely_over_wmi).

Fixed

Fixed an issue in the Migration Center discovery client CLI where region filtering for S3 assets during AWS inventory discovery failed, resulting in asset collection from all regions instead of only specified regions.

Fixed

Fixed an issue where adding vCenter credentials in the Migration Center discovery client UI redirected users to the dashboard instead of opening the credentials pane.

Fixed

Fixed a bug that caused the discovery client not to use the provided proxy when connecting to Migration Center.

## December 17, 2025

Feature

**Preview:** Migration Center now lets you visualize network dependencies between your discovered server assets. You can view a graph of network connections for specific groups or a subset of servers to better understand your infrastructure and plan your application migration.

For more information, see [Visualize network dependencies](https://docs.cloud.google.com/migration-center/docs/visualize-network-dependencies).

## December 10, 2025

Announcement

The [discovery client 6.3.10](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with a bug fix.

Fixed

Fixed a bug in the MCDC guest collection script.

## November 17, 2025

Feature

**Preview:** Migration Center now provides more granular storage preferences for Compute Engine. You can now specify your preference for using Hyperdisk Storage Pools to reduce costs and improve operational efficiency.

For more information, see [Migration preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).

Issue

If you select sole-tenant nodes as your migration target, Migration Center always recommends Hyperdisk Storage Pools even if they are more expensive than individual Hyperdisk volumes. When migrating to sole-tenant nodes, we recommend that you select **Never** in the **Hyperdisk Storage Pools** section of your preferences.

For more information, see [Migration preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).

## November 10, 2025

Announcement

The [discovery client 6.3.9](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Feature

**Preview:** Added support for discovery of the following assets from your AWS account:

  * Amazon DynamoDB
  * Amazon Route53
  * NAT Gateway



For more information, see [Discover assets on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets).

Fixed

Fixed an issue that caused the collection of data from Linux machines to become unresponsive on systems running JBoss EAP.

Fixed

Fixed an issue that caused the VMware vCenter status to incorrectly display the previous status during a new collection, such as `warning` or `error`. The status is now correctly cleared when a new collection job begins.

Fixed

Fixed an issue that prevented the `mcdc discover ls` command from displaying IP addresses.

## October 29, 2025

Feature

**C/C++ application migration to Arm architecture assessment.** The App Modernization Assessment tool now offers a dedicated assessment for C/C++ applications to facilitate their migration to Arm-based architectures (such as Google Cloud Axion C4A VMs). This new feature helps you do the following:

  * **Assess readiness:** understand the effort and readiness required to transition your C/C++ applications from x86-based architectures to Arm.
  * **Identify key challenges:** pinpoint potential code portability issues, architecture-specific dependencies, and necessary build system modifications.
  * **Plan for success:** gain insights into testing considerations crucial for a smooth and successful migration to Arm, whether on Google Cloud or other cloud providers like AWS Graviton instances.



Feature

**Enhanced productivity with command-line completion.** The `codmod` tool now supports shell command-line completion for Bash, Zsh, Fish, and PowerShell, significantly boosting your productivity. This feature lets you quickly type commands, flags, and arguments by pressing the `TAB` key to see and select the available options.

With this feature, you can discover options and see valid flag values. Additionally, suggestions are context-aware, meaning completions are tailored to the specific command. For example, `codmod config set [TAB]` suggests config keys, and file path completion is exclusively available for file and directory flags. For additional details, see [Command-line completion](https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment#shell_auto_completion).

Feature

**Automatic version check and updates.** The `codmod` tool now includes an automatic version check feature to help you stay up-to-date with the latest improvements and fixes. Every 24 hours, the `codmod` tool checks for the availability of a newer version. If an update is available, a notification message appears in your terminal with the new version number and a download link.

  * You can disable the automatic check at any time using the following command: `codmod config set disable_version_check true`.

  * To re-enable automatic checks, simply set the value back to `false`. You can always view the current state and other configurations by running `codmod config list`.




Feature

**Supporting documents for assessment.** The `codmod` tool can now analyze a directory containing additional supporting documents to the codebase. The `codmod` tool supports documentation in textual, PDF, and image (PNG, JPG, JPEG) formats. Provide the directory by passing the `--supporting-documents <directory>` flag to the `create` command.

## October 16, 2025

Feature

**Preview:** Migration Center lets you view detailed total cost of ownership (TCO) information directly in the Google Cloud Console for each asset and migration preference set, without the need to export the TCO report. You can also see AI-powered insights for each allocated Google Cloud asset.

This experimental feature is available only for Compute Engine VMs. VMware Engine, sole-tenant nodes, and database assets are not supported.

For more information, see [Generate TCO reports](https://docs.cloud.google.com/migration-center/docs/generate-tco-report).

## October 15, 2025

Feature

**Preview:** On the Migration Center **Summary** page, you can now see an aggregated view of the detected software assets.

For more information, see [View the collected assets](https://docs.cloud.google.com/migration-center/docs/view-assets).

You can also group your software assets and see a count of each software instance in the total cost of ownership (TCO) report.

For more information, see [Generate TCO reports](https://docs.cloud.google.com/migration-center/docs/generate-tco-report).

## October 06, 2025

Announcement

The [discovery client 6.3.8](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Feature

**Preview:** Added support for discovery of the following assets from your AWS account:

  * Amazon CloudFront
  * Amazon Elastic Container Service (ECS)
  * Amazon Elastic File System (EFS)
  * Amazon Elastic Kubernetes Service (EKS)
  * Amazon Redshift
  * Amazon Simple Storage Service (S3)
  * Amazon Virtual Private Cloud (VPC)
  * AWS Lambda
  * Elastic Load Balancing (ELB)



For more information, see [Discover assets on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets).

Feature

Migration Center now collects and displays CPU manufacturer information for discovered assets. You can see this information on the **Asset details** page.

For more information, see [View the collected assets](https://docs.cloud.google.com/migration-center/docs/view-assets).

Fixed

To better support large VMware vCenter environments, the maximum time for a single collection job has been increased to 24 hours, therefore reducing timeout issues.

Feature

Migration Center Discovery Client user interface now displays a progress bar and asset count for VMware vCenter collections, helping you track long-running jobs.

For more information, see [Add vCenter for discovery](https://docs.cloud.google.com/migration-center/docs/add-servers#add_vcenter_for_discovery).

## September 18, 2025

Feature

**Generally available:** Migration Center now provides more granular Google Compute Engine preferences. You can now adjust your recommendations to balance latest technology and cost, or to prioritize the lowest price. Additionally, you can include pre-released SKUs in assessments, and select from a wider range of pricing tracks including on-demand and committed use discounts.

For more information, see [Migration preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).

## September 10, 2025

Feature

**Generally available:** Migration Center now includes AI-powered suggestions for software detection.

For more information, see [Detected software](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights#detected-software).

## August 14, 2025

Feature

**New quantitative metrics.** The report summary section now includes a summary of key quantitative metrics, providing a quick, data-driven overview of the report at a glance.

Feature

**Added file regex flags.** Two new optional flags, `--force-include` and `--force-exclude`, have been added to provide user flexibility in file selection.

Feature

**Added feedback and support links to HTML report.** The feedback and support links point to Google Forms that will be used to gather feedback and support requests.

Announcement

The Migration Center [App Modernization Assessment tool](https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment) version 0.9.0 is available in Preview. 

The Migration Center App Modernization Assessment, powered by Google Gemini (via Vertex AI), is a tool designed to accelerate your application modernization journey. It offers automated, AI-powered analysis to understand your entire codebase in hours, not months, uncovering dependencies and complexities. This enables organizations to swiftly transition their existing codebases to the cloud by identifying potential blockers and providing tailored recommendations based on Google Cloud best practices, ultimately de-risking and planning your transformation with confidence.

Feature

**Create custom report from template.** Use a document as a template to create a custom report. The report will attempt to match the outline and style of the template document.

Change

**Removed`2.5-flash-lite-exp` from Suggested Models.** To improve the quality of generated reports, the support for `2.5-flash-lite-exp` model was removed.

Change

**Smaller Default Report and new Full Report.** The default report has been streamlined to 5 sections, reducing generation time and cost. A comprehensive 12-section report can now be generated using the new `create full` command.

Change

**Added a Content Security Policy (CSP)** to improve the security of locally viewed HTML reports.

## August 11, 2025

Feature

**Generally available:** Added support for discovery of Amazon Relational Database Service (Amazon RDS) instances and uploading the collected information to Migration Center.

For more information, see [Discover EC2 instances and databases on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-vms).

Feature

**Generally available:** Added support for discovery of Azure virtual machine (VM) instances and uploading the collected information to Migration Center.

For more information, see [Discover virtual machine instances on Azure](https://docs.cloud.google.com/migration-center/docs/discover-azure-vms).

## August 06, 2025

Announcement

The [discovery client 6.3.7](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Fixed

Fixed an issue that prevented the collection of CPU model names for vSphere ESXi hosts, resulting in missing CPU information for vSphere virtual machines (VMs) in Migration Center.

Issue

When you upgrade to discovery client 6.3.7, data collected by earlier versions of discovery client and that was not already uploaded to Migration Center will be deleted.

Fixed

Fixed an issue in the Linux collection script where the output `tar` file had insufficient permissions, which prevented access by the original non-root user when the script was run with root privileges.

Feature

When you run an inventory discovery on your Amazon Web Services (AWS) account, memory utilization for Amazon EC2 instances is collected by the `mcdc` CLI if the Amazon CloudWatch agent is installed and configured.

Feature

When you run a Linux guest scan, the `mcdc` CLI now discovers the Btrfs filesystem.

Feature

**Generally available:** You can now export collected data from the discovery client to a file for manual import into the Migration Center. 

For more information, see [ Use the discovery client in a disconnected environment](https://docs.cloud.google.com/migration-center/docs/discovery-client-offline-export).

Fixed

Fixed an issue where ZFS partitions not generated by the `zpool` command were incorrectly included in Linux scans.

Change

Added guidance on the Migration Center user interface to help Active Directory (AD) administrators to resolve potential authentication failures by verifying `MCDCUsers` group membership.

Fixed

Fixed an issue that caused floppy disk drives to be incorrectly included in Linux disk scans.

Fixed

Fixed an issue that prevented parsing of `df` output on Linux when a mount point name contained spaces.

Feature

You can now filter the discovered Amazon Relational Database Service (Amazon RDS) assets by tags.

## July 14, 2025

Feature

**Generally available:** On the Migration Center **Data Import** page, you can now see short descriptions for connection errors with the discovery client.

For more information, see [Review the discovery client details](https://docs.cloud.google.com/migration-center/docs/manage-discovery-client#review-discovery-client-details).

Feature

**Generally available:** Migration Center lets you generate a network dependencies report from the data you collect from your infrastructure.

For more information, see [Analyze network dependencies](https://docs.cloud.google.com/migration-center/docs/network-dependencies-report).

## July 03, 2025

Deprecated

The Migration Center discovery client v5 and the Rapid Migration Assessment API were shut down on June 30, 2025, and are no longer available.

For more information, see [Migration Center deprecations](https://docs.cloud.google.com/migration-center/docs/deprecations).

## May 21, 2025

Feature

**Preview** : Added support for discovery of Azure virtual machine (VM) instances and uploading the collected information to Migration Center. 

For more information, see [Discover virtual machine instances on Azure](https://docs.cloud.google.com/migration-center/docs/discover-azure-vms).

## April 24, 2025

Feature

**Generally available:** You can now create asset groups in bulk or update group assignments across many assets simultaneously.

For more information, see [Add or update asset group assignments in bulk](https://docs.cloud.google.com/migration-center/docs/create-groups#assign-update-assets-bulk).

## March 24, 2025

Announcement

The [discovery client 6.3.6](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Feature

Added collection and upload of AWS tags to Migration Center. This enables better visibility and easier grouping of your AWS infrastructure.

Fixed

Fixed an issue where the IP range scan remained in the In Progress state indefinitely after restarting the discovery client service during a scan.

Fixed

Fixed an issue that caused incorrect primary IP addresses of Amazon EC2 instances to be uploaded to Migration Center. This improves the accuracy of network dependencies reports.

Change

Added an indicative message to alert users of unsupported browsers.

Feature

Added upload of disk read and write input/output operations per second (IOPS) to Migration Center. This helps ensure accurate pricing and sizing reports.

Feature

Added the `--extended` flag to the `mcdc discover ls` command to include location and collection parameters columns.

Fixed

Fixed an issue in Linux guest collection that omitted filesystem overhead and reservations from total partition size calculations.

Fixed

Fixed an issue that caused incorrect capacity and storage reporting for Windows RAID partitions.

Fixed

Fixed an issue where disk space reporting excluded virtual disk partitions for some filesystems (specifically fuse) on Linux machines. This improves the accuracy of storage capacity and usage data.

Fixed

Fixed an issue on Linux where partition data couldn't be retrieved when mount points contained spaces.

Fixed

Fixed an issue where system memory swap space was sometimes incorrectly reported as disk storage.

Fixed

Fixed an issue that caused VMware vCenter collection to take significantly more time to initiate a subsequent collection after a details or credential updates.

Fixed

Fixed an issue that caused the Win32_Service Windows Management Instrumentation (WMI) query to fail, resulting in Windows guest collection timeouts. This improves the Windows guest collection success rate and reduces execution time.

Feature

**Preview** : Added support for discovery of Amazon Relational Database Service (Amazon RDS) instances and uploading the collected information to Migration Center.

For more information, see [Discover EC2 instances and databases on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-vms).

Fixed

Fixed an issue that required an IP address when using the test credentials feature with VMware tools.

Fixed

Fixed an issue that prevented users from sorting Windows Servers by scan status.

Fixed

Fixed an issue that incorrectly calculated storage sizes for ZFS file systems.

## January 29, 2025

Feature

You can now unregister the discovery client from Migration Center, so that you can register it in a different project without reinstalling.

Announcement

The [discovery client 6.3.5](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Feature

View information about the connected Google Cloud project on the settings page.

Feature

You can now manually renew the service account key used for authentication with Migration Center.

Fixed

Fixed an issue where the Migration Center discovery client CLI `discover ls` command only displayed IPv6 addresses. It now displays only IPv4 addresses.

Fixed

Fixed the migrate to Google Distributed Cloud (GDC) assessment to issue a warning for VMs with disks larger than 5 TiB, instead of the previous 108 TiB limit, to account for object storage limitations.

Fixed

Fixed an issue that caused disk input/output operations per second (IOPS) on Linux to be reported incorrectly to Migration Center.

Fixed

Fixed an issue that caused expired discovery clients to be incorrectly presented as active on the settings page.

Fixed

Fixed an issue that incorrectly reported `procfs` and `sysfs` mounts to Migration Center.

Fixed

Fixed an issue that caused the architecture fields not to be collected from ARM VMs.

Feature

**Preview** : Added support for discovery of AWS EC2 instances and uploading the collected information to Migration Center. 

For more information, see [Discover VMs on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-vms).

Fixed

Fixed an issue preventing RedHat operating system (OS) name and version collection.

Fixed

Fixed an issue where the Migration Center discovery client CLI only reported a single memory usage sample, potentially causing incorrect rightsizing suggestions.

## January 09, 2025

Feature

The Migration Center Use Case Navigator now includes MongoDB workload identification and guidance. This enhancement allows users to gain valuable insights into the potential transformation journeys for their MongoDB workloads, and to generate comprehensive reports on their MongoDB workload footprint.

## November 11, 2024

Announcement

The [discovery client 6.3.4](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Fixed

Reduced potential performance impact of the guest collection script on target Windows VMs by optimizing the collection script.

Fixed

Reduced potential performance impact of the guest collection script on target Linux VMs by setting scripts to execute with a higher `nice` level.

Fixed

Fixed an issue that caused Linux guest collection to report incorrect disk space in some cases by excluding network mounts and temporary file systems, and incorrectly calculating logical volumes.

Feature

The discovery client disk usage collection in Linux and Windows VMs has been enhanced for improved accuracy in disk reporting. The system now supports disk partition type discovery. For Linux VMs, discovery client reports the total disk capacity without partitioning it; for Windows VMs, the partitioned structure is reported.

Fixed

Fixed an issue that caused UDP connections on Windows to not be uploaded to Migration Center.

Feature

ESX CPU hyperthreading detection is now supported in the collection of inventory level data from vCenter.

Fixed

Fixed an issue that caused VMs with a very large number of running processes, services, installed applications, or open files handlers, to be reported incorrectly to Migration Center.

## October 31, 2024

Feature

**Generally available:** Migration Center now detects and surfaces VM hyperthreading enabled or disabled state based on information uploaded on an RVTools file.

Feature

**Generally available:** Added support for Cloud SQL Enterprise Plus for SQL Server.

Feature

**Generally available:** Migration Center now surfaces VM hyperthreading enabled or disabled state based on the information collected by the Migration Center discovery client.

Feature

**Generally available:** You can now authorize Google Cloud engineers to help with your migration by accepting the terms and conditions in Migration Center.

For more information, see [Get started with Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center).

## September 30, 2024

Deprecated

StratoZone was shut down on September 30, 2024, and is no longer available.

Feature

**Generally available:** Migration Center lets you export the inventory and performance data in CSV and Google Sheets format.

For more information, see [Export inventory and performance data](https://docs.cloud.google.com/migration-center/docs/export-inventory-and-performance-data).

Feature

**Generally available:** Migration Center is now available in the following additional regions:

  * europe-west4
  * us-east4
  * us-east5
  * asia-southeast1



For more information, see [Migration Center locations](https://docs.cloud.google.com/migration-center/docs/locations).

Feature

**Generally available:** Migration Center lets you view the relationship between a server and a hosted database directly in the Console.

## September 16, 2024

Feature

The [discovery client 6.3.3](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Fixed

Fixed an issue that caused Linux guest collections to report the wrong number of CPU cores in some cases.

Fixed

MSI installer privileges changes: Users are no longer required to run the MSI installer as administrators. Now, standard users with the ability to install software can also run the installer.

Feature

Added technical fit assessment for BitLocker encryption as part of "Shift to GCE" and "Shift to GDC" assessment. Added rules IDs: `C1W-STO-1` and `D1W-STO-1`.

For more information, see [Offline assessment rules](https://docs.cloud.google.com/migration-center/docs/assessment-rules).

Fixed

Fixed an issue that caused VMs using Windows NLB of the same cluster to be represented as a single VM in Migration Center.

Feature

Added a notification that appears when a new version of the discovery client is available.

Fixed

Reduced the resource consumption of the Windows collection script on the target VMs.

Fixed

Fixed an issue that caused the discovery client to wrongly classify Java processes as JBoss applications.

## August 11, 2024

Feature

Added support for Linux kernel driver information collection required for enhanced technical assessment.

Feature

You can now add new guest OS credentials from the vCenter discovery page.

Feature

The [discovery client 6.3.2](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Fixed

Fixed an issue that sometimes caused Windows guest collections to report the wrong number of CPU cores.

Feature

Added an error tooltip to the upload status in the Scans page.

Fixed

Fixed an issue that caused the installation to fail if the default PowerShell execution policy is too restrictive.

Feature

You can now reset guest OS credentials in the vCenter discovery page.

Fixed

Improved free disk calculation from vCenter inventory collection.

Feature

The discovery client now validates the existence of guest OS credentials before the creation of an IP range.

Fixed

Fixed an issue that caused a temporary directory created during guest-level collection using VMware Guest Tools to not get cleaned up if the collection times out.

Feature

Added technical fit assessment for VirtIO Drivers as part of "Shift to GCE" and "Shift to GDC" assessment rules ID: `C1L-APP-2` and `D1L-APP-3`.

Fixed

The discovery client now preserves the users in the `MCDCUsers` group during an upgrade.

## July 31, 2024

Feature

**Generally available:** Migration Center provides recommendations for [ve2 nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types) on Google Cloud VMware Engine.

Feature

**Generally available:** Migration Center lets you calculate license costs reductions by disabling simultaneous multithreading for virtual machines running Windows Server and Microsoft SQL Server.

For more information, see [Migration preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).

## July 30, 2024

Deprecated

StratoZone is scheduled for end of sale on July 30, 2024, and will reach end of life (complete shutdown) on October 1, 2024.

Deprecated

The Rapid Migration Assessment API is scheduled for end of sale on July 30, 2024, and will reach end of life (complete shutdown) on June 30, 2025.

Deprecated

The Migration Center discovery client v5 is scheduled for end of sale on July 30, 2024, and will reach end of life (complete shutdown) on June 30, 2025.

## July 24, 2024

Feature

The [discovery client 6.3.1](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) is available with new features and bug fixes.

Fixed

Improved CPU utilization collection accuracy.

Fixed

Fixed an issue that caused some dropdown fields in the **Servers** page to get unexpectedly pre-populated by previously selected values.

Fixed

Fixed an issue that caused false positive indications of VMware guest connection test.

Feature

Added support for automated upgrades from previous versions. Upgrades are available for discovery client version 6.3.0 and later.

Fixed

Fixed an issue that caused Windows collection to sometimes consume high CPU and memory when IIS is installed on the machine.

Feature

Added information on machines CPU count per virtual machine in the discovery client detailed offline reports in HTML format.

Fixed

Fixed an issue that caused guest collection failures from source servers running Windows with .NET Framework lower than 4.5.

Fixed

Fixed an issue that prevented the last collection timestamp from being shown on the **Servers** page of the discovery client.

## June 30, 2024

Feature

**Preview:** Migration Center lets you generate a network dependencies report from the data you collect from your infrastructure.

Feature

**Generally available:** Migration Center automatically maps the relationship between a server and a hosted database when both are scanned.

Feature

**Generally available:** Migration Center lets you generate a report for Microsoft licenses (Windows Server and MS SQL Server).

Feature

**Generally available:** Migration Center databases discovery and assessment for Microsoft SQL Server, MySQL, and PostgreSQL databases is now generally available.

For more information, see [Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases).

## June 24, 2024

Announcement

**Generally available:** A [new version of Migration Center discovery client, 6.3.0](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview), is generally available. The following features were added in this release:

  * Offline reports providing detailed technical fit assessment for migration and modernization of VMs. You can generate reports directly from the local discovery client UI in HTML, CSV, JSON, and Microsoft Excel format. 
  * Data collection of network statistics and open ports required for identifying VMs dependencies using network information. 
  * Custom scheduling of data collection from servers to enable opt-out periods.
  * Technical fit assessment for migrating VMs to Google Distributed Cloud. The assessment is available as part of the discovery client offline reports.



Feature

User control on analytics and Cloud Logging during installation lets you opt out from sending data to Google. Users can always opt in or opt out later through the discovery client settings.

Feature

The discovery client collects network statistics such as open ports and traffic usage per connection to provide the information required to [analyze network dependencies](https://docs.cloud.google.com/migration-center/docs/network-dependencies-report) in the Migration Center.

Feature

View the discovery client logs from the Migration Center Console for easy troubleshooting of any communication issues between remote discovery client applications and Migration Center.

Feature

Added support for local report generation that provides detailed technical fit assessment for migration and modernization. The reports are available in HTML, Microsoft XLS, CSV, and JSON format. You can generate [fit assessment reports](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment) in offline mode to support assessment in air-gapped environments.

Feature

Custom scheduling of periodic data collection lets you [define opt-out schedules](https://docs.cloud.google.com/migration-center/docs/add-servers#configure_the_scan_schedule) from periodic collection per server. The feature helps to avoid any potential performance degradation in servers peak usage hours from additional load of data collection.

Fixed

Fixed an issue that may cause instability when scanning over 2000 servers.

## June 14, 2024

Fixed

Discovery client 5.3.5.11: Fixed an issue that may cause large memory usage during collection.

## June 04, 2024

Feature

**Preview:** Detailed description of CloudSQL shape recommendation calculation is available in the detailed pricing report in CSV format.

Feature

**Generally available:** Migration Center lets you download the detailed pricing report as CSV files that include both servers and databases assets.

For more information, see [Generate TCO reports](https://docs.cloud.google.com/migration-center/docs/generate-tco-report).

## May 20, 2024

Announcement

**Preview:** A new version of Migration Center discovery client, 6.2.0, is available in [Preview](https://cloud.google.com/products#product-launch-stages). The following features are available:

  * New and simplified installation flow using self registration with Migration Center.
  * Virtual machine and physical server discovery by scanning ranges of IPs. You can import IP addresses and IP ranges from a CSV file.
  * Automated collection of guest-level data required for assessment using SSH and WMI.
  * Collection of servers inventory data using direct, secure integration with the VMware VCenter API.
  * Simplified experience for managing the credentials required for data collection.
  * Periodic collection of performance data from servers required for right-sizing calculation in Migration Center.



For more information, see [Migration Center discovery client overview](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview).

Feature

The Migration Center discovery client CLI (`mcdc` CLI) supports the offline assessment of migrating VMs running on VMWare vSphere to VMs running on [Google Distributed Cloud (GDC) air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/overview).

The `mcdc` CLI now assesses the migration fit of VMware VMs to Google Distributed Cloud air-gapped with a journey called "Shift | Google Distributed Cloud". This journey is available in all report formats by default. To generate a report focused on applicable journeys to GDC including existing containerization journeys, run the following command using the `mcdc` CLI for Linux or Windows:
    
    
    ./mcdc report --format FORMAT --target-platform gdc --file REPORT_NAME
    

For more information, see [Offline assessment rules](https://docs.cloud.google.com/migration-center/docs/assessment-rules).

Issue

The following are open known issues with the Migration Center discovery client 6.2.0:

  * The maximum number of scanned servers is limited to a total of 2,000 servers. Exceeding this limit may cause instability.
  * Opting out from analytics and Cloud Logging can only be done from the **Settings** page of the discovery client application.
  * In some cases, the discovery client service might not run after boot, and users would get a "connection refused" error when opening the discovery client application. A workaround is to configure the discovery client service to have a delayed start.



## April 19, 2024

Feature

**Preview:** Migration Center displays additional asset-level insights that indicate the installed software detected on scanned virtual machines. Migration Center supports detection of specific third-party software frameworks.

To learn about the software versions reported, see [Detected software workloads](https://docs.cloud.google.com/migration-center/docs/software-workloads-insights).

## March 31, 2024

Change

When you create a cost estimation for a Google Cloud VMware Engine environment, and you choose **General purpose** as the workload type, Migration Center now recommends FTT2/R6 as the default vSAN policy.

## March 12, 2024

Feature

**Preview:** Migration Center introduces databases discovery and assessment for Microsoft SQL Server, MySQL, and PostgreSQL databases, and lets you assess migration journeys to Cloud SQL, providing technical fit assessment for Cloud SQL target. Groups support servers and databases. Expanded preferences for databases allow you to include databases in the TCO report.

For more information, see [Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases).

## February 08, 2024

Feature

**Preview:** You can use VPC Service Controls to secure your Migration Center resources with a service perimeter and control the movement of data across the perimeter boundary.

For more information, see [Secure your data with a service perimeter](https://docs.cloud.google.com/migration-center/docs/service-perimeter).

Feature

**Preview:** Migration Center provides additional explainability details for the recommendations in the detailed pricing report. You can see details for Google Cloud VMware Engine and Compute Engine sole-tenant targets, and learn about details such as rightsizing and resource allocation performed based on the user preferences.

Feature

**Generally available:** Migration Center provides recommendations for storage-only nodes on Google Cloud VMware Engine.

## January 16, 2024

Change

Discovery client 5.3.5.10: Updated .NET runtime to version 6.0.25.

Fixed

Discovery client 5.3.5.10: General fixes to the application.

## January 08, 2024

Feature

**Generally available:** Migration Center lets you estimate the costs of running your Exadata platform as a fully managed service in BigQuery.

For more information, see [Cost estimation](https://docs.cloud.google.com/migration-center/docs/estimate/overview).

## December 07, 2023

Feature

**Generally available:** Migration Center lets you estimate the costs of running your VMware platform as a fully managed service in Google Cloud.

For more information, see [Cost estimation](https://docs.cloud.google.com/migration-center/docs/estimate/overview).

## November 30, 2023

Feature

Migration Center lets you create and export a performance data report for your assets. This data is useful to better understand why certain recommendations, such as the rightsizing recommendations, were made.

For more information, see [Export inventory and performance data](https://docs.cloud.google.com/migration-center/docs/export-inventory-and-performance-data).

## November 15, 2023

Feature

Migration Center lets you mark assets as out of scope. Out of scope assets are hidden from the groups and never appear in the total cost of ownership (TCO) reports. 

For more information, see [Out of scope assets](https://docs.cloud.google.com/migration-center/docs/view-assets#out-of-scope).

## October 31, 2023

Feature

A new version of the Migration Center discovery client CLI is available: version 2.1.0.

Feature

**Preview** : you can now run the `mcdc` CLI 2.1.0 on Windows. The `mcdc` CLI for Windows maintains the existing functionalities of the `mcdc` CLI for Linux, including inventory discovery, guest discovery, and IP range scan. The `mcdc` CLI for Windows also supports guest collection from Windows target machines using WMI.

Feature

With the `mcdc` CLI 2.1.0, you can now export a debug bundle with the following command:
    
    
    mcdc export debug
    

To help troubleshoot your issues, you can share this bundle with Google Cloud Support.

Change

The `OSType` column was removed from the input to the `mcdc discover ips` command.

Change

The `OSType` column was removed from the output of the `mcdc discover ipscan` command.

## October 13, 2023

Change

Discovery client 5.3.5.9: Updated the PostgreSQL and MySQL collection scripts.

## October 02, 2023

Change

The on-premises cost calculator in the Migration Center cost estimation functionality has been updated to include some UI improvements and bug fixes.

## September 21, 2023

Feature

Discovery client 5.3.5.8: Added ability to use local Service Account Key during authorization.

Feature

Discovery client 5.3.5.8: Added ability to scan MongoDB databases.

Feature

Discovery client 5.3.5.8: Added filtering of project names during authorization with Migration Center.

Change

Discovery client 5.3.5.8: Updated mFit script to 1.15.2.

Change

Discovery client 5.3.5.8: Removed database scan banner.

Fixed

Discovery client 5.3.5.8: Improved collection of process details for Linux collection.

## September 12, 2023

Feature

**Generally available:** Migration Center lets you specify custom rightsizing values for your assessment preferences. In addition to the existing sizing optimization strategies—moderate, aggressive, and no rightsizing—the **custom** rightsizing strategy lets you set specific values for your assessment calculations.

## September 11, 2023

Change

Previous reports with logical and physical core count per VM might contain inaccuracies. This release contains a fix to information presented on logical and physical core counts per VM. If you compare reports that were exported prior to this change, you might see a different count of logical and physical cores.

Change

The network usage sizing appears now in the **Network** section of the **Migration preferences** page. The **Egress traffic estimate** knob lets you tune a percentage value of the measured VM egress traffic to be used to estimate billed network traffic per VM. For previous assessments that used the preset method, Migration Center back-filled the egress traffic estimate by using the following values for each sizing optimization strategy:

  * No preference: 10%
  * No rightsizing: 10%
  * Moderate: 10%
  * Aggressive: 5%



## August 15, 2023

Feature

Migration Center discovery client CLI is now **generally available** in version 2.0.0. The `mcdc` CLI maintains the existing functionalities of the fit assessment tool (mFit), and introduces integration with Migration Center.

Feature

**Preview** : With the `mcdc` CLI 2.0.0, you can export the discovered assets to Migration Center. This lets you generate insights and TCO reports for your inventory.

Export assets to Migration Center with the following command:
    
    
    mcdc export mc --project MY_PROJECT
    

For more information, see [Export data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data).

Feature

**Preview** : With the `mcdc` CLI 2.0.0, you can collect VM performance data via the vCenter API.

Feature

**Preview** : With the `mcdc` CLI 2.0.0, you can scan ranges of IP addresses to detect assets in your infrastructure.
    
    
    mcdc discover ipscan --ranges <RANGE_1>,<RANGE_2>
    

For more information, see [Run an IP range scan](https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan).

Change

The on-premises cost calculator in Migration Center cost estimation functionality now lets you apply committed use discounts (CUDs), Enterprise Agreement (EA), and Cloud Commitment Agreement (CCA) discounts. The enhanced Workloads and licensing tab also lets you choose licensing models for your Windows and Linux workloads.

## June 26, 2023

Announcement

Migration Center is now **generally available**.

Feature

Migration Center lets you create total cost of ownership (TCO) reports with Google Cloud VMware Engine and sole-tenant nodes on Compute Engine as additional target asset environments.

Feature

Migration Center lets you export your assets to a Google Sheets file in your Google Drive.

## May 31, 2023

Feature

Discovery client 5.3.5.7: Discovery Client can collect usage and other anonymized data that helps Google improve the product.

Change

Discovery client 5.3.5.7: updated .NET Framework to .NET Core 6.0.

Change

Discovery client 5.3.5.7: updated how Fit Assessment scripts and data are transferred (using Windows registry) between target Windows assets.

Change

Discovery client 5.3.5.7: updated Windows NCrypt algorithm to AES.

Fixed

Discovery client 5.3.5.7: fixed issues with proxy settings in client.

## May 15, 2023

Feature

The data warehousing cost calculator is now generally available in the Migration Center cost estimation functionality. It lets you generate a rapid cost estimate for running your data analytics and warehousing setup from other cloud platforms on BigQuery serverless data warehouse on Google Cloud.

For more information, see [Cost estimation](https://docs.cloud.google.com/migration-center/docs/estimate/overview).

## April 07, 2023

Change

Discovery client 5.3.5.5: changed the default de-duplication logic to user fingerprints instead of FQDN.

Change

Discovery client 5.3.5.5: added support for additional SSH MAC algorithms.

Feature

Discovery client 5.3.5.5: Discovery client now sends technical logs and error messages to Cloud Logging.

Fixed

Discovery client 5.3.5.5: fixed an issue with installer not applying some updates during upgrade.

Fixed

Discovery client 5.3.5.5: fixed an issue with Google Cloud fit recommendation collection to handle various credential formats.

## March 30, 2023

Announcement

A new version of Migration Center is available in Preview.

Feature

**Preview** : Migration Center lets you specify multiple migration preferences that can help you customize your migration assessments.

Feature

**Preview** : You can now create groups of assets that share common characteristics, such as functional dependencies or location.

Feature

**Preview** : Migration Center lets you upload tables with your infrastructure data that you can manually create using the available templates. Migration Center now supports files up to 100 Mb.

Feature

**Preview** : You can now use automated scripts to collect data from your AWS and Azure infrastructure and generate tables that you can upload to Migration Center.

Feature

**Preview** : The total cost of ownership (TCO) summary report is available in Migration Center for assets that are targeted to migrate to Google Compute Engine. You can generate TCO reports to compare the costs of moving your groups of assets based on different migration scenarios that you specify with your migration preferences. You can view TCO reports directly on Migration Center's user interface in the Cloud Console, or export them to Google Slides.

## March 07, 2023

Feature

The SAP cost calculator is now generally available in the Migration Center cost estimation functionality.

## February 16, 2023

Feature

Discovery client 5.3.5.4: offline discovery mode is available in Preview.

Change

Discovery client 5.3.5.4: Migration Center Collector renamed to Migration Center discovery client.

Change

Discovery client 5.3.5.4: updated Google Cloud fit recommendation scripts to version 1.14.0.

Fixed

Discovery client 5.3.5.4: moved local log files to `%PROGRAMDATA%\Google\DiscoveryClient` folder.

Fixed

Discovery client 5.3.5.4: changed VM age to use `CreateDate` for vSphere collection.

## September 28, 2022

Announcement

Migration Center is available in Preview. Migration Center is a new Google Cloud service to streamline migration journeys with intelligent insights and actionable recommendations, bringing together tools and methodologies from rapid cost estimation to migration execution.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
