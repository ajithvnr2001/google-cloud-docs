---
url: https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.674734+00:00
---

# Troubleshooting  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page explains various error scenarios and troubleshooting steps to resolve the errors.

## Connectivity and networking error scenarios

If your service experiences connectivity or networking issues, check the scenarios in the following sections to see if one of them is causing the problem.

### Service creation fails due to constraint to restrict VPC peering

Don't set the org-policy constraint to restrict VPC peering. Specifying `constraints/compute.restrictVpcPeering` causes your creation request to fail with an `INVALID_ARGUMENT` error. If you must set the constraint, use the following command to allow `under:folders/270204312590`:
    
    
    gcloud resource-manager org-policies allow compute.restrictVpcPeering under:folders/270204312590 --organization ORGANIZATION_ID
    

For more information, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

### Cross-project deployment fails where service account may not exist

To create a Dataproc Metastore service that is accessible in a network belonging to a different project than the one the service belongs to, you must grant `roles/metastore.serviceAgent` to the service project's Dataproc Metastore service agent (`service-SERVICE_PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`) in the network project's IAM policy.
    
    
    gcloud projects add-iam-policy-binding NETWORK_PROJECT_ID \
        --role "roles/metastore.serviceAgent" \
        --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com"
    

**Caution:** This IAM policy change indirectly allows Dataproc Metastore users with `metastore.services.create` permission in the service project to control the addresses and peerings in the network project.**Note:** If you have never created a Dataproc Metastore service in the service project, then the `gcloud projects add-iam-policy-binding` command may fail with an error message containing `Service account [SERVICE_ACCOUNT_NAME] does not exist.` If this happens, you can resolve the issue by attempting to create a service using a non-existent network in the service project. The service creation will fail, but it will trigger the creation of the service account. Afterwards, the command should succeed.

For more information, see [Set up a cross-project deployment](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc#set-up-cross-project-deployment).

### Private IP is required for network connectivity

Dataproc Metastore uses private IP only, so no public IP is exposed. This means that only VMs on the [provided Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/dataproc-metastore/docs/reference/pc/google.cloud.metastore.v1#google.cloud.metastore.v1.Service.FIELDS.string.google.cloud.metastore.v1.Service.network) or on-premises (connected through [Cloud VPN or Cloud Interconnect](https://cloud.google.com/hybrid-connectivity)) can access the Dataproc Metastore service.

For more information, see [Service access](https://docs.cloud.google.com/dataproc-metastore/docs/access-service).

### Required ingress-allow firewall rule for Kerberos

Kerberos requires Dataproc Metastore to initiate connections to hosts in your project network. You must create a firewall rule that allows TCP and UDP ingress on all ports from the `/17` IP block that contains the Dataproc Metastore IP.

For more information, see [Firewall rules on your KDC](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/security#network_configuration) and [Firewall rules for your services](https://docs.cloud.google.com/dataproc-metastore/docs/access-service#firewall-rules-for-your-services).

### Connection error caused by resources provisioned in Shared VPC networks

If your service uses a network belonging to a different project, and Compute Engine is protected by the service perimeter, then the metastore project and network project must be in the same perimeter.

To add existing Dataproc Metastore projects to the perimeter, follow the instructions in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

For more information, see [VPC Service Controls with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc).

### Allocated IP range is exhausted

The provided VPC network may run out of available RFC 1918 addresses required by Dataproc Metastore services. If that happens, Dataproc Metastore will attempt to reserve private IP address ranges outside of the RFC 1918 ranges for service creation. For a list of supported non-RFC 1918 private ranges, see [Valid ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in the VPC network documentation.

Non-RFC 1918 private IP addresses used in Dataproc Metastore may conflict with a range in an on-premises network that is connected to the provided VPC network. To check the list of RFC 1918 and non-RFC 1918 private IP addresses reserved by Dataproc Metastore:
    
    
    gcloud compute addresses list \
        --project NETWORK_PROJECT_ID \
        --filter="purpose:VPC_PEERING AND name ~ cluster|resourcegroup"
    

If a conflict is determined and cannot be mitigated by re-configuring the on-premises network, delete the offending Dataproc Metastore service and re-create it again after 2 hours.

For more information, see [IP address range exhaustion](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modify-ip-range).

## Operation timeout error scenarios

The following error scenarios result in an unresponsive service or operation timeouts.

### Use Audit logs to troubleshoot operation timeouts

To troubleshoot service operation timeouts, use the Logs Explorer in the Google Cloud console to retrieve your audit log entries for your Cloud project.

In the Query builder pane, select **Audited Resource** or `audited_resource` as the Google Cloud resource type, followed by **Dataproc Metastore** or `metastore.googleapis.com` as the service. Selecting a method is optional.

For more information, see [Viewing logs](https://docs.cloud.google.com/dataproc-metastore/docs/audit-logging#viewing_logs).

### Service Unavailability

Dataproc Metastore services can become unavailable for various reasons and cause failures. Common reasons this might occur include high CPU usage or out of memory errors.

The issue can be caused by high load or many tables and partitions being queried. To prevent this issue, we recommend using the `Enterprise` tier, which provides flexible scalability, fault tolerance, and multi-zone high availability while handling heavy workloads.

To troubleshoot out of memory errors, use the Logs Explorer in the Google Cloud console to retrieve your audit log entries for your Cloud project.

  1. In the Logs Explorer, click **Query builder**.
  2. Select the following filters 
     * Resource type: `metastore.googleapis.com/Services`
     * Severity: `ERROR`
     * Keyword: `OutofMemoryError`



For more information, see [Viewing logs](https://docs.cloud.google.com/dataproc-metastore/docs/audit-logging#viewing_logs).

## Import and export error scenarios

This section outlines common Dataproc Metastore import and export issues.

### Import fails because the Hive versions don't match

When you import metadata, the Hive metastore and Dataproc Metastore versions must be compatible. Your import may fail if the two don't match.

For more information on compatibility, see [version policy](https://docs.cloud.google.com/dataproc-metastore/docs/version-policy).

You can check Cloud Logging to see if you encountered this error. The following message is an example of this error.
    
    
    Metastore schema version is not compatible. Hive Version: 3.1.0, Database Schema Version: 2.3.0
    

**Note:** You can use [MySQL upgrade scripts](https://github.com/apache/hive/tree/master/standalone-metastore/metastore-server/src/main/sql/mysql) to import metadata from a lower Hive metastore version to a higher version. To do this, import the dump into a MySQL instance and run the upgrade scripts.

### Import fails because there are missing Hive table files

When preparing the import for Avro, there should be a file for each Hive table, even if the table is empty, otherwise the import will fail.

You can use the [Dataproc Metastore Toolkit](https://github.com/GoogleCloudPlatform/dataproc-metastore-toolkit) as a reference to check the correct Hive metadata schemas.

### Service agent or user doesn't have necessary permissions

The Dataproc Metastore service agent (`service-CUSTOMER_PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`) and the user importing the metadata must have the following read permission to the Cloud Storage bucket used for the import:

  * For MySQL, they must have `storage.objects.get` permission on the Cloud Storage object (SQL dump file) used for the import.

  * For Avro, they must have `storage.objects.get` permission on the Cloud Storage bucket used for the import.




For exports, the Dataproc Metastore service agent (`service-CUSTOMER_PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`) and the user creating the export must have `storage.objects.create` permission on the bucket.

### Job fails because the database file is too big

If your database file is too large, it can take more than the [job timeout limit](https://docs.cloud.google.com/dataproc-metastore/docs/quotas#job-timeout-limit) to complete the import or export process. If the import is not able to complete within the 3 hour [job timeout limit](https://docs.cloud.google.com/dataproc-metastore/docs/quotas#job-timeout-limit), you can split your metadata across multiple Dataproc Metastore instances.

## Backup and restore error scenarios

This section outlines common Dataproc Metastore backup and restore issues.

### Unable to create a new backup for a service

If there are already 7 backups in a service, then you must first manually delete a backup before creating a new one. You can delete existing backups from the **Backup/Restore** tab.

### User doesn't have necessary permissions

To backup metadata, you must request an IAM role containing the `metastore.backups.create` IAM permission.

To restore metadata, you must request an IAM role containing the `metastore.services.restore` and `metastore.backups.use` IAM permissions.

### Job fails because the service metadata file is too big

If your [service metadata file](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata#back-up-metadata-from-a-service) is too large, it can take more than the one hour [job timeout limit](https://docs.cloud.google.com/dataproc-metastore/docs/quotas#job-timeout-limit) to complete the backup or restore process.

## Managed Service for Apache Spark cluster error scenarios

The following sections outline common Managed Service for Apache Spark and self-managed cluster issues.

### Managed Service for Apache Spark cluster attachment fails due to mismatched versions

When you attach a Managed Service for Apache Spark cluster, the Managed Service for Apache Spark image and Dataproc Metastore Hive version must be compatible. Check the following image versioning pages to ensure that the Hive version is compatible:

  * Managed Service for Apache Spark [2.0.x release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.0)
  * Managed Service for Apache Spark [1.5.x release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-1.5)
  * Managed Service for Apache Spark [1.4.x release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-1.4)



For more information, see [Managed Service for Apache Spark Image version list](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions).

### Managed Service for Apache Spark cluster creation fails due to insufficient roles

When creating a Managed Service for Apache Spark cluster, the cluster creation fails with the following error message:
    
    
    gcloud.dataproc.clusters.create) INVALID_ARGUMENT: Default Service Account '**********-compute@developer.gserviceaccount.com' is missing required permissions: [dataproc.agents.create, dataproc.agents.delete, dataproc.agents.get, dataproc.agents.update, dataproc.tasks.lease, dataproc.tasks.listInvalidatedLeases, dataproc.tasks.reportStatus]. Service Accounts must have either 'Dataproc/Dataproc Worker' role or all permissions granted by the role.
    

This can occur when you try to create a Managed Service for Apache Spark cluster and attach it to your Dataproc Metastore.

To fix this issue, grant the `roles/dataproc.worker` to your service account. The following example illustrates how to do this, using some sample values.
    
    
    gcloud projects add-iam-policy-binding my_project \
        --member=219315-compute@developer.gserviceaccount.com \
        --role=roles/dataproc.worker

### Connection to metastore fails due to time zone issues

Your Hive file returns the error `The server time zone value 'CDT' is unrecognized or represents more than one time zone`.

If you can't connect to your metastore from Managed Service for Apache Spark, then you must [delete your current cluster](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/delete) and update your `gcloud dataproc clusters create` command or automation tool to include the following time zone parameter:
    
    
    --metadata "hive-metastore-uri=jdbc:mysql://10.207.26.77:3306/hive_metastore?serverTimezone=CST6CDT"
    

## Troubleshooting Google Cloud CLI issues

If you encounter an issue where a gcloud CLI command is unavailable, or if the command behaves differently from how it is documented, try updating the gcloud CLI:
    
    
    gcloud components update
    

## What's next

  * To resolve errors, see [Error messages](https://docs.cloud.google.com/dataproc-metastore/docs/error-messages).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
