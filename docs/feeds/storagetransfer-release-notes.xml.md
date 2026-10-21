---
url: https://docs.cloud.google.com/feeds/storagetransfer-release-notes.xml
title: Storage Transfer Service - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:50.966321+00:00
---

# Storage Transfer Service - Release notes

> Source: https://docs.cloud.google.com/feeds/storagetransfer-release-notes.xml

tag:google.com,2016:storagetransfer-release-notesStorage Transfer Service - Release notesGoogle Cloud Platform2026-09-28T00:00:00-07:00September 28, 2026tag:google.com,2016:storagetransfer-release-notes#September_28_20262026-09-28T00:00:00-07:00Feature 

Storage Transfer Service now supports transferring data from multiple containers within a Microsoft Azure Storage account in a single transfer job.

For more information, see [Transfer all containers in an Azure Storage account](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/azure-all-containers).

]]> September 21, 2026tag:google.com,2016:storagetransfer-release-notes#September_21_20262026-09-21T00:00:00-07:00Feature 

Storage Transfer Service now supports filtering Amazon S3 source objects by storage class. You can specify a list of storage classes to include when creating or updating transfer jobs using the Google Cloud console, the `gcloud` CLI, or the REST API.

For more information, see [Filter source objects by storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class).

### Feature

Storage Transfer Service now supports filtering source objects using glob patterns with wildcard characters such as `*` and `?`. Glob filtering is supported for transfers from Amazon S3 and Microsoft Azure Blob Storage when configuring transfer jobs using the `gcloud` CLI or the REST API.

For more information, see [Filter source objects using wildcards](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern).

]]> May 08, 2026tag:google.com,2016:storagetransfer-release-notes#May_08_20262026-05-08T00:00:00-07:00Feature 

Storage Transfer Service now supports AWS GovCloud (US) regions, including `us-gov-east-1` and `us-gov-west-1`. You can now transfer data from Amazon S3 buckets located in GovCloud regions using both batch and event-driven transfers.

For more information, see [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) and [Event-driven transfers from AWS S3](https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws).

]]> March 09, 2026tag:google.com,2016:storagetransfer-release-notes#March_09_20262026-03-09T00:00:00-07:00Change 

The size limit for manifest files used in agent-based transfers has been removed.

For more information, see [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).

]]> February 02, 2026tag:google.com,2016:storagetransfer-release-notes#February_02_20262026-02-02T00:00:00-08:00Feature 

Organization Policy Service custom constraints are now available for Storage Transfer Service. You can use custom constraints to control how Storage Transfer Service is used in your organization. For example, you can restrict transfers to only allow Cloud Storage to Cloud Storage transfers, or restrict transfers to a specific list of approved source buckets.

See [Custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints) for details.

]]> January 14, 2026tag:google.com,2016:storagetransfer-release-notes#January_14_20262026-01-14T00:00:00-08:00Feature 

Storage Transfer Service event-driven transfers are now available for Azure Blob Storage and Data Lake Storage Gen2 sources. Event-driven transfers listen to Azure Event Grid notifications via Azure Storage Queues to automatically transfer new or updated objects from your Azure container to Cloud Storage.

For more information, see [Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2](https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure).

]]> December 02, 2025tag:google.com,2016:storagetransfer-release-notes#December_02_20252025-12-02T00:00:00-08:00Feature 

You can now transfer data from AWS S3 or Azure Blob Storage to Cloud Storage over a private network connection, using Cross-Cloud Interconnect or Partner Interconnect. Transferring data over a private connection can optimize costs, provide dedicated bandwidth, and help meet compliance needs by keeping data off the public internet.

See [Transfer from AWS or Azure over a customer-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network) for details.

]]> July 28, 2025tag:google.com,2016:storagetransfer-release-notes#July_28_20252025-07-28T00:00:00-07:00Feature 

Storage Transfer Service agent-based transfers now support [Cloud Storage regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints). When you specify a Cloud Storage regional endpoint for a transfer agent, all data transfer traffic through that agent to or from a Cloud Storage bucket remains within the specified Google Cloud region.

See [Regional endpoints](https://docs.cloud.google.com/storage-transfer/docs/regional-endpoints) for details.

]]> May 22, 2025tag:google.com,2016:storagetransfer-release-notes#May_22_20252025-05-22T00:00:00-07:00Feature 

You can now delegate permissions to a user-managed service account for agentless transfers, instead of using the default Google-managed service agent. This allows for more granular permission control by assigning specific bucket permissions to different user-managed service accounts, and restricting which users can use those service accounts for transfer jobs.

See [Delegate service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions) for details.

]]> May 02, 2025tag:google.com,2016:storagetransfer-release-notes#May_02_20252025-05-02T00:00:00-07:00Feature 

Cloud Logging for agent-based transfers now logs skipped files. A skipped file is logged when the file already exists in the sink, and your transfer job is configured to ignore existing files.

See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for details.

]]> March 31, 2025tag:google.com,2016:storagetransfer-release-notes#March_31_20252025-03-31T00:00:00-07:00Change 

Transfers over a [Google-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#egress_options) are now supported from more AWS regions, including regions in Europe and Asia. See the [full list of supported regions](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#managed_private_network_regions).

]]> December 19, 2024tag:google.com,2016:storagetransfer-release-notes#December_19_20242024-12-19T00:00:00-08:00Feature 

When providing a URL list to transfer files, you can now host the list itself in an access-controlled Cloud Storage bucket. See [Transfer from public URLs](https://docs.cloud.google.com/storage-transfer/docs/create-url-list) for full details.

]]> July 23, 2024tag:google.com,2016:storagetransfer-release-notes#July_23_20242024-07-23T00:00:00-07:00Security 

We've released a lighter weight (~50% reduction in image size) and more secure version of the transfer agent container image. If you're running agents that were installed on or before June 17th, 2024, we highly recommend that you delete those agents and [install new agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent) into your agent pool. Any existing transfers using that pool will resume once the new agents are installed.

]]> May 17, 2024tag:google.com,2016:storagetransfer-release-notes#May_17_20242024-05-17T00:00:00-07:00Feature 

Cloud Logging for Storage Transfer Service now supports transfers involving POSIX file systems.

See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for more details.

### Feature

Storage Transfer Service now supports transfers from Amazon S3 over a Google-managed private network. Transfer jobs that select this option pay no AWS egress fees; instead, a flat per-GiB rate is charged by Google Cloud. This allows you to transfer data at a potentially lower overall cost.

Learn more about [egress options for S3 transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#egress_options), including the managed private network.

]]> April 17, 2024tag:google.com,2016:storagetransfer-release-notes#April_17_20242024-04-17T00:00:00-07:00Feature 

Storage Transfer Service has added support for Shared Keys as an authentication method when transferring from Microsoft Azure Storage.

To use an Azure Shared Key, you must store the key value in Secret Manager. See [Save your Microsoft credentials in Secret Manager](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure#secret_manager) for details.

]]> March 13, 2024tag:google.com,2016:storagetransfer-release-notes#March_13_20242024-03-13T00:00:00-07:00Feature 

Support for transfers from cloud and on-premises Hadoop Distributed File System (HDFS) sources is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). 

HDFS support allows for use cases such as migrating from on-premises storage to Cloud Storage, archiving data to free up on-premises storage space, replicating data to Google Cloud for business continuity, or transferring data to Google Cloud for analysis and processing.

See [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/hdfs) for details.

]]> February 22, 2024tag:google.com,2016:storagetransfer-release-notes#February_22_20242024-02-22T00:00:00-08:00Feature 

Storage Transfer Service has added [preview support](https://cloud.google.com/products/#product-launch-stages) for transferring managed folders between Cloud Storage buckets. Permissions on managed folders are copied between buckets when using this option.

See [Transfer Cloud Storage managed folders](https://docs.cloud.google.com/storage-transfer/docs/managed-folders) for details.

]]> November 30, 2023tag:google.com,2016:storagetransfer-release-notes#November_30_20232023-11-30T00:00:00-08:00Feature 

Storage Transfer Service supports transfers from cloud and on-premises Hadoop Distributed File System (HDFS) sources. This feature is in limited release; complete the form linked from the user guide at [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/hdfs) to request access.

This new feature supports use cases such as migrating from on-premises storage to Cloud Storage, archiving data to free up on-premises storage space, replicating data to Google Cloud for business continuity, or transferring data to Google Cloud for analysis and processing.

]]> November 01, 2023tag:google.com,2016:storagetransfer-release-notes#November_01_20232023-11-01T00:00:00-07:00Change 

Storage Transfer Service has updated transfer agent behavior when transferring to Cloud Storage. To align with Cloud Storage [auto-scaling](https://docs.cloud.google.com/storage/docs/request-rate#auto-scaling), agents now gradually ramp up the number of requests being made to Cloud Storage. Customers who transfer many small files may notice initially slower transfer speeds while the requests are ramping up, but increased performance across the duration of the transfer.

]]> October 12, 2023tag:google.com,2016:storagetransfer-release-notes#October_12_20232023-10-12T00:00:00-07:00Feature 

You can now transfer data from Amazon S3 via your CloudFront domain. [Learn more](https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront).

]]> July 25, 2023tag:google.com,2016:storagetransfer-release-notes#July_25_20232023-07-25T00:00:00-07:00Feature 

Event-driven transfers are now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

Event-driven transfers provide serverless, real-time replication from AWS S3 to Cloud Storage, and between Cloud Storage buckets. With this new capability, you can accelerate your event-driven analytics pipeline, enable automatic replication across Cloud Storage buckets, create a backup copy of data in a different region or project, or perform live migration.

Learn more about [Event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers).

]]> June 27, 2023tag:google.com,2016:storagetransfer-release-notes#June_27_20232023-06-27T00:00:00-07:00Change 

Transfers from Amazon S3 no longer require `s3:GetBucketLocation` permission on the source bucket.

For a full list of required permissions, see [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions).

]]> June 12, 2023tag:google.com,2016:storagetransfer-release-notes#June_12_20232023-06-12T00:00:00-07:00Feature 

Cloud Monitoring for Storage Transfer Service is now Generally Available ([GA](https://cloud.google.com/products/#product-launch-stages)). This integration allows you to monitor the number of objects and data being transferred and to compute transfer speeds. This GA launch also adds monitoring of errors and error codes.

See [Monitor transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs) for details.

### Feature

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for providing a [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret when creating transfer jobs from AWS S3 or Azure storage.

Secret Manager provides strong encryption, role-based access control, and audit logging to protect your secrets.

For details, see the **Secret Manager** section of the following documents:

  * [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions)
  * [Configure access to a source: Microsoft Azure Storage ](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#ip_restrictions)

]]> June 06, 2023tag:google.com,2016:storagetransfer-release-notes#June_06_20232023-06-06T00:00:00-07:00Security 

We discovered a security vulnerability in the Storage Transfer Service agent container. We've fixed this issue with a container update that is more secure.

If you're running agents that were installed on or before February 17, 2023, you should follow the instructions in the **Action required** email sent to your account email address to update the container image.

Agents installed after February 17, 2023 do not need to be updated.

]]> April 25, 2023tag:google.com,2016:storagetransfer-release-notes#April_25_20232023-04-25T00:00:00-07:00Feature 

Storage Transfer Service now publishes the IP ranges from which it makes requests to your AWS or Azure storage resources when performing a transfer. This allows you to restrict your resources by IP, and still allow Storage Transfer Service access.

For details, see the **IP restrictions** section of the following documents:

  * [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#ip_restrictions)
  * [Configure access to a source: Microsoft Azure Storage ](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#ip_restrictions)

]]> April 14, 2023tag:google.com,2016:storagetransfer-release-notes#April_14_20232023-04-14T00:00:00-07:00Feature 

Storage Transfer Service can now optionally preserve UID, GID, and mode metadata for folders, and recreate empty folders, when transferring between file systems.

See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

]]> April 11, 2023tag:google.com,2016:storagetransfer-release-notes#April_11_20232023-04-11T00:00:00-07:00Feature 

Transfers from [S3-compatible storage to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible) are now generally available [(GA)](https://cloud.google.com/products/#product-launch-stages). This feature builds on support for [Multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) and [List Object V2](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list), which makes Cloud Storage suitable for running applications written for the S3 API.

With this new feature, customers can seamlessly copy data from self-managed object storage to Google Cloud Storage. For customers moving data from AWS S3 to Cloud Storage, this feature provides an option to control network routes to Google Cloud, resulting in considerably lower egress charges.

See [Transfer from S3-compatible sources](https://docs.cloud.google.com/storage-transfer/docs/s3-compatible) for details.

]]> April 06, 2023tag:google.com,2016:storagetransfer-release-notes#April_06_20232023-04-06T00:00:00-07:00Feature 

Support for [Manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) in Storage Transfer Service is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). You can use Manifest to transfer a specific list of objects, object versions, and files from cloud and on-premises sources. Programmatic users can use the output of an upstream operation generating a list of files and objects as an input for Storage Transfer Service to act upon.

]]> January 17, 2023tag:google.com,2016:storagetransfer-release-notes#January_17_20232023-01-17T00:00:00-08:00Announcement 

Temporary pricing for Storage Transfer Service has expired; refer to [Pricing](https://cloud.google.com/storage-transfer/pricing) for current charges.

Customers under contract can reach out to Google Cloud representatives for details.

]]> December 19, 2022tag:google.com,2016:storagetransfer-release-notes#December_19_20222022-12-19T00:00:00-08:00Feature 

Storage Transfer Service now offers [Preview](https://cloud.google.com/products/#product-launch-stages) support for tracking progress of a Transfer Job using Cloud Monitoring, allowing you to monitor the number of objects and amount of data copied by Storage Transfer Service in near real-time.

See [Monitor transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs) for details.

]]>
