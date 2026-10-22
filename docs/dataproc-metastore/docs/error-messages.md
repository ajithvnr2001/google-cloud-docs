---
url: https://docs.cloud.google.com/dataproc-metastore/docs/error-messages/
title: Error messages \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:41.434704+00:00
---

# Error messages  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains common error messages that you might receive when using Dataproc Metastore. Each section includes more information on what the messages mean and the recommended actions for resolving the errors.

General errors:

  * Invalid client inputs:

    * "ResourceName error Path [RESOURCE_NAME] does not match template [RESOURCE_TEMPLATE]."
    * "Invalid warehouse directory override: [GCS_URI]."
    * "The provided krb5.conf object krb5Config was invalid."
  * Invalid API resource state:

    * "Current state of resource [RESOURCE_NAME] is not a valid state for this operation. Valid state(s) are [RESOURCE_STATE]."
    * You tried to run update, import, export, backup, or restore on a Dataproc Metastore service, but the service was not `ACTIVE`.
    * "Backup [BACKUP_ID] not ready."
  * API access permission:

    * You didn't have enough permission to call the Dataproc Metastore APIs.
  * Insufficient service agent permissions:

    * "The Dataproc Metastore service agent [SERVICE_AGENT] does not have sufficient IAM permissions to access the network [NETWORK]. Please make sure the service agent is granted roles/metastore.serviceAgent in the project [PROJECT_NUMBER]."

    * "Dataproc Metastore Service Agent cannot access Cloud Storage URI [GCS_URI] with permissions [SERVICE_AGENT_PERMISSIONS]; Please check permissions or VPC Service Controls service perimeter."

    * "The provided warehouse directory's Cloud Storage bucket [GCS_URI] is not readable and writable by the Dataproc Metastore service agent."




Errors relating to import and export:

  * Import and export Cloud Storage permissions:

    * ""Dataproc Metastore Service Agent" or "Caller" does not have enough permissions of the Cloud Storage URI for import/export ([SERVICE_AGENT] cannot access Cloud Storage URI [GCS_URI] with permissions [SERVICE_AGENT_PERMISSIONS])."
  * Run Avro import or export on an unsupported Hive version:

    * "Importing from Avro files is not supported for Hive version [HIVE_METASTORE_VERSION], supported versions are [SUPPORT_HIVE_VERSIONS]."
  * Missing import tables:

    * "Avro source files not found for tables [MISSING_TABLE_LIST]."
    * "Hive schema validation failed, missing tables: [MISSING_TABLE_LIST]."



Errors relating to backup and restore:

  * Backup not found for restore:

    * "Backup [BACKUP_ID] not found."
  * Cannot delete a backup:

    * "Cannot delete a backup in a state [RESOURCE_STATE]."



## General errors

This section explains general errors.

### Invalid client inputs

This is a generic error that means something about your request is invalid, independent of the server's state. This error type could be triggered by many different things, such as:

  * When using the REST API, you specified the name of a network in an invalid format.

> ResourceName error Path [RESOURCE_NAME] does not match template [RESOURCE_TEMPLATE].

  * The warehouse directory was not a valid Cloud Storage path. For more information, see [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore).

> Invalid warehouse directory override: [GCS_URI].

  * You specified invalid Kerberos configurations (see [Configure Kerberos for a service](https://docs.cloud.google.com/dataproc-metastore/docs/configure-kerberos)).

> The provided krb5.conf object krb5Config was invalid.




**Recommended action:** Fix your request.

### Invalid API resource state

This is a generic error that means that something about the request is not compatible with the current state of the server resource.

> Current state of resource [RESOURCE_NAME] is not a valid state for this operation. Valid state(s) are [RESOURCE_STATE].

This can happen if the API resource (Dataproc Metastore service, import, export, backup, or restore) is not in the correct state to perform the action, for example:

  * You tried to run update, import, export, backup, or restore on a Dataproc Metastore service, but the service was not `ACTIVE`.
  * You tried to restore a backup, and the Dataproc Metastore service was `ACTIVE`, but the backup was not `ACTIVE`.

> Backup [BACKUP_ID] not ready.




**Recommended action:** Check that your API resource is in the correct state before retrying the request.

### API access permission

You didn't have enough permission to call the Dataproc Metastore APIs.

**Recommended action:** Grant the user the correct [Dataproc Metastore IAM permissions](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles).

### Insufficient service agent permissions

You received a permission error when creating resources in your project. The error is usually caused by a deleted service account, or modified service account permissions, for example:

  * You used a network belonging to a different project, but didn't grant the Dataproc Metastore service agent permission to access it. For more information, see [Cross project deployment](https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment#set-up-permissions).

> The Dataproc Metastore service agent [SERVICE_AGENT] does not have sufficient IAM permissions to access the network [NETWORK]. Please make sure the service agent is granted roles/metastore.serviceAgent in the project [PROJECT_NUMBER].

  * You provided a custom data warehouse Cloud Storage bucket, but you didn't grant the Dataproc Metastore service agent permission to access it. For more information, see [Hive warehouse directory](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#hive-warehouse-dir).

> Dataproc Metastore Service Agent cannot access Cloud Storage URI [GCS_URI] with permissions [SERVICE_AGENT_PERMISSIONS]; Please check permissions or VPC Service Controls service perimeter.




Or Dataproc Metastore couldn't access the warehouse directory Cloud Storage path.

> The provided warehouse directory's Cloud Storage bucket [GCS_URI] is not readable and writable by the Dataproc Metastore service agent.

**Recommended action:** Check your [service account permissions](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control#service-accounts) or [VPC Service Controls service perimeter](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc).

## Errors relating to import and export

This section explains errors relating to import and export.

### Import and export Cloud Storage permissions

Your Dataproc Metastore service agent didn't have enough permissions to perform the import or export.

> "Dataproc Metastore Service Agent" or "Caller" does not have enough permissions of the Cloud Storage URI for import/export ([SERVICE_AGENT] cannot access Cloud Storage URI [GCS_URI] with permissions [SERVICE_AGENT_PERMISSIONS]).

**Recommended action:** Check your [service account permissions](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control#service-accounts) or [VPC Service Controls service perimeter](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc).

### Run Avro import or export on an unsupported Hive version

> Importing from Avro files is not supported for Hive version [HIVE_METASTORE_VERSION], supported versions are [SUPPORT_HIVE_VERSIONS].

**Recommended action:** See [Version policy](https://docs.cloud.google.com/dataproc-metastore/docs/version-policy) for the most up-to-date Hive version support. Update your database files to a supported version.

### Missing import tables

  * For Avro import

> Avro source files not found for tables [MISSING_TABLE_LIST].

  * For SQL import

> Hive schema validation failed, missing tables: [MISSING_TABLE_LIST].




**Recommended action:** Use the [Dataproc Metastore Toolkit](https://github.com/GoogleCloudPlatform/dataproc-metastore-toolkit) as a reference to check the correct Hive metadata schemas of your database files.

## Errors relating to backup and restore

This section explains errors relating to backup and restore.

### Backup not found for restore

When restoring a backup in a service, Dataproc Metastore couldn't find your provided backup resource.

> Backup [BACKUP_ID] not found.

**Recommended action:** Check that your backup exists within your Dataproc Metastore service.

### Cannot delete a backup

You couldn't delete a backup when it was being used to restore a service.

> Cannot delete a backup in a state [RESOURCE_STATE].

**Recommended action:** Wait for the restore job to complete before attempting to delete the backup.

## What's next

  * To find solutions for common issues that you might encounter when using Dataproc Metastore, see [Troubleshooting](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
