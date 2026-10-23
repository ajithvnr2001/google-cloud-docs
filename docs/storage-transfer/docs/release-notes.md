---
url: https://docs.cloud.google.com/storage-transfer/docs/release-notes/
title: Storage Transfer Service release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:58.765425+00:00
---

# Storage Transfer Service release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/storage-transfer/docs/resources)



Send feedback 

#  Storage Transfer Service release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Storage Transfer Service. We recommend that Storage Transfer Service developers periodically check this list for any new announcements. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/storagetransfer-release-notes.xml) directly. 

## September 28, 2026

Feature

Storage Transfer Service now supports transferring data from multiple containers within a Microsoft Azure Storage account in a single transfer job.

For more information, see [Transfer all containers in an Azure Storage account](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/azure-all-containers).

## September 21, 2026

Feature

Storage Transfer Service now supports filtering Amazon S3 source objects by storage class. You can specify a list of storage classes to include when creating or updating transfer jobs using the Google Cloud console, the `gcloud` CLI, or the REST API.

For more information, see [Filter source objects by storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class).

Feature

Storage Transfer Service now supports filtering source objects using glob patterns with wildcard characters such as `*` and `?`. Glob filtering is supported for transfers from Amazon S3 and Microsoft Azure Blob Storage when configuring transfer jobs using the `gcloud` CLI or the REST API.

For more information, see [Filter source objects using wildcards](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern).

## May 08, 2026

Feature

Storage Transfer Service now supports AWS GovCloud (US) regions, including `us-gov-east-1` and `us-gov-west-1`. You can now transfer data from Amazon S3 buckets located in GovCloud regions using both batch and event-driven transfers.

For more information, see [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) and [Event-driven transfers from AWS S3](https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws).

## March 09, 2026

Change

The size limit for manifest files used in agent-based transfers has been removed.

For more information, see [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).

## February 02, 2026

Feature

Organization Policy Service custom constraints are now available for Storage Transfer Service. You can use custom constraints to control how Storage Transfer Service is used in your organization. For example, you can restrict transfers to only allow Cloud Storage to Cloud Storage transfers, or restrict transfers to a specific list of approved source buckets.

See [Custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints) for details.

## January 14, 2026

Feature

Storage Transfer Service event-driven transfers are now available for Azure Blob Storage and Data Lake Storage Gen2 sources. Event-driven transfers listen to Azure Event Grid notifications via Azure Storage Queues to automatically transfer new or updated objects from your Azure container to Cloud Storage.

For more information, see [Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2](https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure).

## December 02, 2025

Feature

You can now transfer data from AWS S3 or Azure Blob Storage to Cloud Storage over a private network connection, using Cross-Cloud Interconnect or Partner Interconnect. Transferring data over a private connection can optimize costs, provide dedicated bandwidth, and help meet compliance needs by keeping data off the public internet.

See [Transfer from AWS or Azure over a customer-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network) for details.

## July 28, 2025

Feature

Storage Transfer Service agent-based transfers now support [Cloud Storage regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints). When you specify a Cloud Storage regional endpoint for a transfer agent, all data transfer traffic through that agent to or from a Cloud Storage bucket remains within the specified Google Cloud region.

See [Regional endpoints](https://docs.cloud.google.com/storage-transfer/docs/regional-endpoints) for details.

## May 22, 2025

Feature

You can now delegate permissions to a user-managed service account for agentless transfers, instead of using the default Google-managed service agent. This allows for more granular permission control by assigning specific bucket permissions to different user-managed service accounts, and restricting which users can use those service accounts for transfer jobs.

See [Delegate service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions) for details.

## May 02, 2025

Feature

Cloud Logging for agent-based transfers now logs skipped files. A skipped file is logged when the file already exists in the sink, and your transfer job is configured to ignore existing files.

See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for details.

## March 31, 2025

Change

Transfers over a [Google-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#egress_options) are now supported from more AWS regions, including regions in Europe and Asia. See the [full list of supported regions](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#managed_private_network_regions).

## December 19, 2024

Feature

When providing a URL list to transfer files, you can now host the list itself in an access-controlled Cloud Storage bucket. See [Transfer from public URLs](https://docs.cloud.google.com/storage-transfer/docs/create-url-list) for full details.

## July 23, 2024

Security

We've released a lighter weight (~50% reduction in image size) and more secure version of the transfer agent container image. If you're running agents that were installed on or before June 17th, 2024, we highly recommend that you delete those agents and [install new agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent) into your agent pool. Any existing transfers using that pool will resume once the new agents are installed.

## May 17, 2024

Feature

Cloud Logging for Storage Transfer Service now supports transfers involving POSIX file systems.

See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for more details.

Feature

Storage Transfer Service now supports transfers from Amazon S3 over a Google-managed private network. Transfer jobs that select this option pay no AWS egress fees; instead, a flat per-GiB rate is charged by Google Cloud. This allows you to transfer data at a potentially lower overall cost.

Learn more about [egress options for S3 transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#egress_options), including the managed private network.

## April 17, 2024

Feature

Storage Transfer Service has added support for Shared Keys as an authentication method when transferring from Microsoft Azure Storage.

To use an Azure Shared Key, you must store the key value in Secret Manager. See [Save your Microsoft credentials in Secret Manager](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure#secret_manager) for details.

## March 13, 2024

Feature

Support for transfers from cloud and on-premises Hadoop Distributed File System (HDFS) sources is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). 

HDFS support allows for use cases such as migrating from on-premises storage to Cloud Storage, archiving data to free up on-premises storage space, replicating data to Google Cloud for business continuity, or transferring data to Google Cloud for analysis and processing.

See [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/hdfs) for details.

## February 22, 2024

Feature

Storage Transfer Service has added [preview support](https://cloud.google.com/products/#product-launch-stages) for transferring managed folders between Cloud Storage buckets. Permissions on managed folders are copied between buckets when using this option.

See [Transfer Cloud Storage managed folders](https://docs.cloud.google.com/storage-transfer/docs/managed-folders) for details.

## November 30, 2023

Feature

Storage Transfer Service supports transfers from cloud and on-premises Hadoop Distributed File System (HDFS) sources. This feature is in limited release; complete the form linked from the user guide at [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/hdfs) to request access.

This new feature supports use cases such as migrating from on-premises storage to Cloud Storage, archiving data to free up on-premises storage space, replicating data to Google Cloud for business continuity, or transferring data to Google Cloud for analysis and processing.

## November 01, 2023

Change

Storage Transfer Service has updated transfer agent behavior when transferring to Cloud Storage. To align with Cloud Storage [auto-scaling](https://docs.cloud.google.com/storage/docs/request-rate#auto-scaling), agents now gradually ramp up the number of requests being made to Cloud Storage. Customers who transfer many small files may notice initially slower transfer speeds while the requests are ramping up, but increased performance across the duration of the transfer.

## October 12, 2023

Feature

You can now transfer data from Amazon S3 via your CloudFront domain. [Learn more](https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront).

## July 25, 2023

Feature

Event-driven transfers are now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

Event-driven transfers provide serverless, real-time replication from AWS S3 to Cloud Storage, and between Cloud Storage buckets. With this new capability, you can accelerate your event-driven analytics pipeline, enable automatic replication across Cloud Storage buckets, create a backup copy of data in a different region or project, or perform live migration.

Learn more about [Event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers).

## June 27, 2023

Change

Transfers from Amazon S3 no longer require `s3:GetBucketLocation` permission on the source bucket.

For a full list of required permissions, see [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions).

## June 12, 2023

Feature

Cloud Monitoring for Storage Transfer Service is now Generally Available ([GA](https://cloud.google.com/products/#product-launch-stages)). This integration allows you to monitor the number of objects and data being transferred and to compute transfer speeds. This GA launch also adds monitoring of errors and error codes.

See [Monitor transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs) for details.

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for providing a [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret when creating transfer jobs from AWS S3 or Azure storage.

Secret Manager provides strong encryption, role-based access control, and audit logging to protect your secrets.

For details, see the **Secret Manager** section of the following documents:

  * [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions)
  * [Configure access to a source: Microsoft Azure Storage ](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#ip_restrictions)



## June 06, 2023

Security

We discovered a security vulnerability in the Storage Transfer Service agent container. We've fixed this issue with a container update that is more secure.

If you're running agents that were installed on or before February 17, 2023, you should follow the instructions in the **Action required** email sent to your account email address to update the container image.

Agents installed after February 17, 2023 do not need to be updated.

## April 25, 2023

Feature

Storage Transfer Service now publishes the IP ranges from which it makes requests to your AWS or Azure storage resources when performing a transfer. This allows you to restrict your resources by IP, and still allow Storage Transfer Service access.

For details, see the **IP restrictions** section of the following documents:

  * [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions)
  * [Configure access to a source: Microsoft Azure Storage ](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#ip_restrictions)



## April 14, 2023

Feature

Storage Transfer Service can now optionally preserve UID, GID, and mode metadata for folders, and recreate empty folders, when transferring between file systems.

See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

## April 11, 2023

Feature

Transfers from [S3-compatible storage to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible) are now generally available [(GA)](https://cloud.google.com/products/#product-launch-stages). This feature builds on support for [Multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) and [List Object V2](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list), which makes Cloud Storage suitable for running applications written for the S3 API.

With this new feature, customers can seamlessly copy data from self-managed object storage to Google Cloud Storage. For customers moving data from AWS S3 to Cloud Storage, this feature provides an option to control network routes to Google Cloud, resulting in considerably lower egress charges.

See [Transfer from S3-compatible sources](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible) for details.

## April 06, 2023

Feature

Support for [Manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) in Storage Transfer Service is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). You can use Manifest to transfer a specific list of objects, object versions, and files from cloud and on-premises sources. Programmatic users can use the output of an upstream operation generating a list of files and objects as an input for Storage Transfer Service to act upon.

## January 17, 2023

Announcement

Temporary pricing for Storage Transfer Service has expired; refer to [Pricing](https://cloud.google.com/storage-transfer/pricing) for current charges.

Customers under contract can reach out to Google Cloud representatives for details.

## December 19, 2022

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for tracking progress of a Transfer Job using Cloud Monitoring, allowing you to monitor the number of objects and amount of data copied by Storage Transfer Service in near real-time.

See [Monitor transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs) for details.

## December 15, 2022

Feature

Storage Transfer Service now offers [GA Support](https://cloud.google.com/products/#product-launch-stages) for [transferring data between file systems](https://docs.cloud.google.com/storage-transfer/docs/file-to-file), including on-premises file systems and Filestore instances. This allows you to use the Transfer Service API, gcloud command line tool, or the Cloud console to migrate data from a self-managed file system to Filestore; accelerate data transfer from an on-premise file system to a cloud file system; or move data between on-premises systems. 

You can also [transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) for file system to file system transfers.

## December 09, 2022

Feature

Storage Transfer Service offers [Preview support](https://cloud.google.com/products/#product-launch-stages) for event-driven transfers - serverless, real-time replication from AWS S3 to Cloud Storage, and between Cloud Storage buckets. With this new capability, you can accelerate your event-driven analytics pipeline, enable automatic replication across Cloud Storage buckets, create a backup copy of data in a different region or project, or perform live migration.

Learn more about [Event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers).

## October 07, 2022

Feature

[Multipart upload](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#enable_multipart_uploads) for transfers originating from a file system is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)) and enabled by default.

Multipart uploads can speed up transfers that include large files. You must grant additional permissions on the destination or intermediate bucket; see [Permissions for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#multipart_uploads) for details.

## October 03, 2022

Feature

Support for exporting data from Cloud Storage to a file system is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

You can use this bidirectional data movement capability to move data in and out of Cloud Storage, on-premises clusters, and edge locations including Google Distributed Cloud. To get started, see [Requirements for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up).

Feature

The Storage Transfer Service REST API now provides a [transferJobs.delete](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/delete) method. Deleting a transfer job stops all current and future operations associated with the job, and removes the job from all transfer job listings. Learn more on the [Manage transfers](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#delete-transfer-job) page.

## September 07, 2022

Feature

Storage Transfer Service now offers Preview support for moving data from [S3-compatible storage to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible). This feature builds on recent Cloud Storage launches, namely support for [Multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) and [List Object V2](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list), which makes Cloud Storage suitable for running applications written for the S3 API. With this new feature, customers can seamlessly copy data from self-managed object storage to Google Cloud Storage. For customers moving data from AWS S3 to Cloud Storage, this feature provides an option to control network routes to Google Cloud, resulting in considerably lower egress charges.

See [Transfer from S3-compatible sources](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible) for details.

## August 30, 2022

Feature

Storage Transfer Service now offers [preview](https://cloud.google.com/products/#product-launch-stages) support for [multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#enable_multipart_uploads) for transfers originating from a file system, if the destination or intermediate bucket uses the Standard storage class.

Multipart uploads can speed up transfers that include large files. You must grant additional permissions on the destination or intermediate bucket; see [Permissions for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#multipart_uploads) for details.

## July 18, 2022

Feature

Detailed logging for objects copied between AWS S3, Azure Blob Storage, ADLS Gen 2, and Cloud Storage with Storage Transfer Service is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

With detailed logs of individual objects available in Cloud Logging, you can verify what was transferred and perform additional data integrity checks. This launch simplifies monitoring, reporting, and troubleshooting. Read [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for details.

## June 29, 2022

Feature

Metadata preservation options are now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). This includes the option of preserving POSIX attributes and symlinks when transferring to, from, and between POSIX filesystems; as well as object ACLs, CMEK, temporary holds, and object creation time when transferring between Cloud Storage buckets.

See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

Feature

Expanded overwrite options are new generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). The [overwriteWhen](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#overwritewhen) field can be used to specify whether data that already exists in the destination should be overwritten always, never, or only when ETags and checksum values indicate that the file has changed.

## June 06, 2022

Change

Storage Transfer Service now offers a merged, unified console experience for cloud and file system transfers. All transfer jobs irrespective of source can be tracked though a single interface. This launch simplifies job creation, monitoring, and troubleshooting.

## April 19, 2022

Feature

Storage Transfer Service now provides more options for when to overwrite files that already exist in the destination. The new [`overwriteWhen`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#overwritewhen) field provides three options, that apply to all transfers, including those to or from file systems.

  * `NEVER` provides defense in depth for archival cases, where data is not intended to be overwritten. Users no longer need to rely on a retention policy to protect their data.
  * `DIFFERENT` uses ETags and checksum values to only overwrite a file if the contents have changed.
  * `ALWAYS` overwrites any existing files with the same name. Avoids `LIST` operations on the destination when transferring into Cloud Storage.



## April 12, 2022

Feature

Storage Transfer Service now offers a predefined role to simplify permission assignment to transfer agents. The `roles/storagetransfer.transferAgent` role grants a minimum set of permissions required for the service to communicate with agents and eliminates the need to assign each permission individually.

The role should be granted to the user account or service account being used to authenticate the agents. See the [On-premises agent account](https://docs.cloud.google.com/storage-transfer/docs/iam-permissions-for-on-prem#on-premises_agent_account) documentation for more details.

## March 30, 2022

Feature

Creating and managing data transfers with the gcloud command-line tool is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

You can use `gcloud` commands to perform agent installation, manage agent pool lifecycles, and orchestrate transfer jobs. This launch simplifies writing scripts to automate transfer workflow.

The GA launch adds support for [transfers between file systems](https://docs.cloud.google.com/storage-transfer/docs/file-to-file), [metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation), and [manifests](https://docs.cloud.google.com/storage-transfer/docs/manifest). It also introduces the [`gcloud transfer authorize`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/authorize) command to inspect and grant required permissions for transfers.

## March 23, 2022

Feature

Storage Transfer Service now enforces the Resource Location Restriction, which is part of the [Org Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-supported-by-multiple-google-cloud-services). This allows an organization to define the allowed regions in which location-based Google Cloud resources, such as transfer jobs, can be created.

To learn how Storage Transfer Service chooses the region in which to run a transfer job, refer to [Location of Storage Transfer Service jobs](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#locations).

## March 14, 2022

Announcement

Between April 2, 2022 and December 31, 2022, transfers using Storage Transfer Service will not result in Cloud Storage charges for certain transfer scenarios.

For more details, refer to the [Storage Transfer Service pricing](https://cloud.google.com/storage-transfer/pricing) page.

## March 08, 2022

Feature

Storage Transfer Service now offers more control over preserving metadata when transferring between Cloud Storage buckets. Choose to retain or discard metadata including object ACLs, customer-managed encryption keys (CMEK), temporary holds, and object creation time. In addition, storage class can be set to any supported value, allowing you to change storage class at scale.

For details, refer to [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#between-cloud-buckets).

## March 03, 2022

Feature

Storage Transfer Service now supports [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), which are the recommended option for accessing Cloud APIs programmatically. This launch significantly reduces the amount of code you need to write; see [Getting started](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries) and [Migrating to the Cloud Client Library](https://docs.cloud.google.com/storage-transfer/docs/reference/migration-guide) for more details.

## February 08, 2022

Feature

Support for [agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)) .

You can use agent pools to create isolated groups of agents as a source or sink entity in a transfer job. This enables you to transfer data from multiple data centers and filesystems concurrently, without creating multiple projects for a large transfer spanning multiple filesystems and data centers.

## January 27, 2022

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for moving data between two filesystems and keeping them in sync on a periodic schedule. Transfers can be orchestrated by creating a transfer job through the API or gcloud command-line tool. See [Transfer data between POSIX file systems](https://docs.cloud.google.com/storage-transfer/docs/file-to-file) for details.

This launch offers a managed way to migrate from a self-managed filesystem to [Filestore](https://docs.cloud.google.com/filestore). If you have on-premises systems generating massive amounts of data that needs to be processed in Google Cloud, you can now use Storage Transfer Service to accelerate data transfer from an on-prem filesystem to a cloud filesystem.

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for preserving POSIX attributes and symlinks when transferring to, from, and between POSIX filesystems. Attributes include the user ID of the owner, the group ID of the owning group, the mode or permissions, the modification time, and the size of the file. See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#posix) for details.

## December 13, 2021

Feature

Creating and managing data transfers with the [`gcloud` command-line tool](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-gcloud) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages). You can use `gcloud` commands to perform agent installation, manage agent pool lifecycles, and orchestrate transfer jobs. This launch simplifies writing scripts to automate transfer workflow.

Feature

Integration with AWS Security Token Service is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)) for Storage Transfer Service.

Security conscious customers can use Storage Transfer Service to perform transfers from AWS S3 without passing long-term AWS S3 credentials, which have to be rotated or explicitly revoked when they are no longer needed. Refer to the **Amazon S3 > Federated Identity** tab when [setting up access to your data source](https://docs.cloud.google.com/storage-transfer/docs/configure-access#source).

## December 06, 2021

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for detailed logging for objects copied between AWS S3, Azure Blob, ADLS Gen 2, and Cloud Storage. With detailed logs of individual objects available in Cloud Logging, you can verify what was transferred and perform additional data integrity checks. This launch simplifies monitoring, reporting, and troubleshooting. Read [Configure transfer logs](https://docs.cloud.google.com/storage-transfer/docs/configure-transfer-logs) for details.

## December 03, 2021

Feature

Support for transferring data from [Azure ADLS Gen 2 to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-program#azure-to-cloud) with Storage Transfer Service is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## December 02, 2021

Feature

The Storage Transfer Service API for managing on-premises transfers is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Customers can use RESTful APIs to automate their on-prem to Cloud transfer workflow.

For more information, see [Managing Transfer for on-premises jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs).

Feature

Storage Transfer Service now offers preview support for [Manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest). You can use Manifest to transfer a specific list of objects, object versions, and files from cloud and on-premises sources. Programmatic users can use the output of an upstream operation generating a list of files and objects as an input for Storage Transfer Service to act upon.

## November 04, 2021

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for [agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools). You can use agent pools to create isolated groups of agents as a source or sink entity in a transfer job. This enables you to transfer data from multiple data centers and filesystems concurrently, without creating multiple projects for a large transfer spanning multiple filesystems and data centers.

## November 01, 2021

Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for exporting data from Cloud Storage to a POSIX file system. You can use this bidirectional data movement capability to move data in and out of Cloud Storage, on-premises clusters, and edge locations including Google Distributed Cloud. For more information, see [Download data from Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/download-from-cloud-storage).

## July 26, 2021

Feature

Storage Transfer Service now offers [Public Preview support](https://cloud.google.com/products#product-launch-stages) for managing on-premises transfer via API. Customers can use RESTful APIs to automate their on-prem to Cloud transfer workflow.

For more information, see [Managing Transfer for on-premises jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#rest-api).

## July 01, 2021

Feature

Transfer service for on-premises data support for delete from source is now [Generally Available](https://cloud.google.com/products/#product-launch-stages). For more information, see [Data consistency details](https://docs.cloud.google.com/storage-transfer/docs/on-prem-job-details#consistency-details).

Feature

Storage Transfer Service offers [Preview](https://cloud.google.com/products/#product-launch-stages) for Integration with AWS Security Token Service. Security conscious customers can now use Storage Transfer Service to perform transfers from AWS S3 without passing any security credentials. This release will alleviate the security burden associated with passing long-term AWS S3 credentials, which have to be rotated or explicitly revoked when they are no longer needed. Refer Amazon Web Services (AWS) S3 Federated Identity credentials when [setting up access to your data source](https://docs.cloud.google.com/storage-transfer/docs/configure-access#source).

## June 18, 2021

Feature

Storage Transfer Service offers [Preview support](https://cloud.google.com/products/#product-launch-stages) for transferring data from Azure ADLS Gen 2 to Cloud Storage.

## June 01, 2021

Change

As of June 1 2021 all Transfer service for on-premises projects added a per-project service account. Actions are required before September 1, 2021 to ensure minimal disruptions to your transfers. Please check your email for detailed instructions.

## April 09, 2021

Feature

Obtaining the status of the [latest transfer operation](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-program#checking-status) is in now generally available.

## March 31, 2021

Feature

Storage Transfer Service support for specifying source and destination paths when creating a transfer is now generally available. For more information, see [Specifying source and destination paths](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-program#source-destination-paths).

Feature

Storage Transfer Service now supports event-driven transfer workflows, a new capability that lets customers start Transfer jobs at once based on an event trigger. Customers can create Transfer jobs without specifying a schedule and start a [`TransferOperation`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations) using [`transferJobs.run`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/run) from an existing [`TransferJob` configuration](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs).

Feature

Storage Transfer Service support for hourly schedules and modifying a job's schedule is now generally available. For more information, see [Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#schedule).

## January 20, 2021

Feature

Storage Transfer Service offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for specifying source and destination paths when creating a transfer. For more information, see [Specifying source and destination paths](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-program#source-destination-paths).

## January 19, 2021

Change

Transfer service for on-premises data has updated the cost to $0.0125 per GB transferred to the destination successfully. For more information, see [Transfer for on-premises pricing details](https://cloud.google.com/storage-transfer/pricing).

## November 09, 2020

Feature

Storage Transfer Service offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for hourly schedules and modifying a job's schedule. For more information, see [Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#schedule).

## October 13, 2020

Feature

Obtaining the [status of the latest transfer operation](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-program#checking-status) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## September 01, 2020

Feature

Storage Transfer Service integration for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) is now generally available.

## July 31, 2020

Feature

Transfers from Microsoft Azure Blob Storage are now generally available.

## March 31, 2020

Feature

Transfer service on-premises: [Beta stage](https://cloud.google.com/products/#product-launch-stages) integration with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) integration with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)

## March 23, 2020

Feature

Transfer Service for on-premises data is now generally available. For more information, see [Transfer Service for on-premises data Overview](https://docs.cloud.google.com/storage-transfer/docs/on-prem-overview).

Feature

Storage Transfer Service now offers Beta support for transfers from Microsoft Azure Blob Storage.

## March 20, 2020

Feature

Storage Transfer Service supports [Pub/Sub notifications for transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer) for external cloud provider to Cloud Storage transfers.

## March 16, 2020

Feature

Storage Transfer Service now allows you to specify files to transfer based on their [last modification times](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions.FIELDS.last_modified_since).

## March 09, 2020

Feature

Storage Transfer Service supports [custom job IDs](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#TransferJob.FIELDS.name).

## December 04, 2019

Feature

Storage Transfer Service for on-premises is now in beta.

## September 05, 2019

Feature

API documentation update to clarify transferJobs API descriptions, specifically: scheduleStartDate, scheduleEndDate, and startTimeOfDay.

## August 05, 2019

Feature

Updates to API documentation.

## March 20, 2019

Feature

Adding new IAM roles for Storage Transfer Service.

## August 06, 2018

Feature

Updated documentation for configuring access to the data sink.

## December 07, 2017

Feature

Documentation updates for IAM permissions.

## September 18, 2017

Feature

Documentation update for access control.

## September 07, 2017

Feature

Updates to API documentation.

## August 31, 2016

Feature

Documentation update that provides clearer instructions for configuring a Cloud Storage data source.

## August 25, 2016

Feature

Documentation update to add information for configuring access to a data sink and supported AWS regions.

## June 15, 2016

Feature

API documentation update.

## April 25, 2016

Feature

Documentation updates and content reorganization.

## April 04, 2016

Feature

Updates to API documentation for scheduling jobs.

## February 23, 2016

Feature

Documentation update to support scheduling recurring transfers with Cloud Console.

## December 12, 2015

Feature

Updated Getting Started document for changes to the Create Transfer workflow.

## September 23, 2015

Feature

Several updates to API documentation.

## August 06, 2015

Feature

Documentation includes instructions for enabling API for non-UI users.

## August 05, 2015

Feature

API documentation now includes "Try It" sections.

## July 28, 2015

Feature

Documentation update for using prefixes in Storage Transfer Service user interface.

## July 22, 2015

Feature

Storage Transfer Service, a cloud-to-cloud transfer tool, launched.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
