---
url: https://docs.cloud.google.com/logging/docs/buckets/
title: Configure log buckets \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:41.967183+00:00
---

# Configure log buckets  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure log buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can create, view, and manage Cloud Logging buckets to store and centralize your log data using the Google Cloud console, [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), or the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets). You can also configure retention periods and lock buckets to meet compliance requirements.

To analyze your log data with [Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics), which provides a SQL interface, upgrade your log buckets. This interface lets you query log data and join log and trace data.

To analyze your log data with BigQuery services, create linked BigQuery datasets on your log buckets. These datasets are read-only and are queried similarly to any other BigQuery dataset. Alternatively, you can route log entries directly to BigQuery.

For conceptual information, see [Store log entries](https://docs.cloud.google.com/logging/docs/store-log-entries).

## Before you begin

Configure your project, your IAM roles, and select the interface that you plan to use.

### Configure your project and roles

To get started with buckets, do the following:

  * Configure your Google Cloud project: 
    1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

    2. To get the permissions that you need to create, upgrade, and link a log bucket, ask your administrator to grant you the [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For the full list of permissions and roles, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control). 

  * Understand the [supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) in which you can store your logs. 
  * If you plan to use the Google Cloud CLI or Cloud Logging API to create or manage your log buckets, then understand the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) formatting requirements. 



### Select the interface you plan to use

###  Google Cloud console 

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Create a bucket

These instructions assume that you are using Google-managed encryption. If you prefer to use customer-managed encryption keys (CMEK), then see [Configure CMEK for logs storage](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).

You can create a maximum of 100 buckets per Google Cloud project. You can't create log buckets in folders or organizations.

To create a user-defined log bucket for your Google Cloud project, do the following:

###  Google Cloud console 

To create a log bucket in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click **Create log bucket**.

  3. Enter a **Name** and **Description** for your bucket.

  4. Optional: Upgrade your bucket to use Observability Analytics.

**Note:** After a log bucket has been upgraded to use Observability Analytics, you can't reconfigure the log bucket to change or remove the use of Observability Analytics. 

     1. Select **Upgrade to use Observability Analytics**. 

When you upgrade a bucket to use Observability Analytics, you can query your logs in the **Observability Analytics** page by using SQL queries. You can also continue to view your logs by using the Logs Explorer.

     2. Optional: To view your logs in BigQuery, select **Create a new BigQuery dataset that links to this bucket** and enter a unique dataset name. 

When you select this option, BigQuery can read the data stored in your log bucket. You can now query in the BigQuery interface where you can join your log data, and also access data from other tools like Data Studio and Looker.

  5. To select the storage [region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) for your logs, click the **Select log bucket region** menu and select a region.

**Note:** Log buckets in the `global` region or in multi-regions don't offer added resiliency compared to log buckets created in single regions like `us-west1`.

**Note:** After you create your log bucket, you can't change your bucket's region. If you need a bucket in a different region, you must create a new bucket in that region, [ redirect the appropriate sinks to the new bucket](https://docs.cloud.google.com/logging/docs/export/configure_export_v2), and then  delete the old bucket.

  6. Optional: To set a custom retention period for the logs in the bucket, click **Next**.

In the **Retention period** field, enter the number of days, between 1 day and 3650 days, that you want Cloud Logging to retain your logs. If you don't customize the retention period, the default is `30 days`.

You can also update the retention period for your log bucket after you create it.

  7. Click **Create bucket**.

After the log bucket is created, Logging upgrades the bucket and creates the dataset link, if these options were selected.

It might take a moment for these steps to complete.




###  gcloud 

**Note:** You can't create a linked BigQuery dataset when you create the log bucket unless you use the Google Cloud console. However, if you create and upgrade a log bucket, then you can use the [`gcloud logging links create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/create) command to create a linked BigQuery dataset.

To only create a log bucket, run the [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command. If you want to upgrade the log bucket to use Observability Analytics, then include the `--enable-analytics` and `--async` flags, and make sure that you set the variable LOCATION to a [supported region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions):
    
    
    gcloud logging buckets create BUCKET_ID --location=LOCATION --enable-analytics --async OPTIONAL_FLAGS

The flag `--async` forces the command to be asynchronous. The return of an asynchronous method is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object; it contains information about the progress of the method. When the method completes, the `Operation` object contains information about the success or failure of the request. For more information, see Asynchronous API methods.

If you don't want to upgrade the log bucket to use Observability Analytics, then omit the `--enable-analytics` and `--async` flags.

For example, if you want to create a bucket with the BUCKET_ID `my-bucket` in the `global` region, your command would look like the following:
    
    
    gcloud logging buckets create my-bucket --location global --description "My first bucket"
    

For example, to create a bucket with the BUCKET_ID `my-upgraded-bucket` in the `global` location, and then upgrade the log bucket to use Observability Analytics, your command would look like the following:
    
    
    gcloud logging buckets create my-upgraded-bucket --location global \
          --description "My first upgraded bucket" \
          --enable-analytics --retention-days=45
    

**Note:** After you create your log bucket, you can't change your bucket's region. If you need a bucket in a different region, you must create a new bucket in that region, [ redirect the appropriate sinks to the new bucket](https://docs.cloud.google.com/logging/docs/export/configure_export_v2), and then  delete the old bucket.

###  REST 

**Note:** You can't create a linked BigQuery dataset as part of the create operation unless you use the Google Cloud console. However, if you create and upgrade a log bucket, then you can use the [`projects.locations.buckets.links.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/create) method to create a linked BigQuery dataset.

To create a bucket, use the [`projects.locations.buckets.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create) or the [`projects.locations.buckets.createAsync`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/createAsync) method. Prepare the arguments to the method as follows:

  1. Set the `parent` parameter to be the resource in which to create the bucket: `projects/PROJECT_ID/locations/LOCATION`

The variable LOCATION refers to the [region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) in which you want your logs to be stored.

For example, if you want to create a bucket for project `my-project` in the `global` region, your `parent` parameter would look like this: `projects/my-project/locations/global`

  2. Set the `bucketId` parameter; for example, `my-bucket`.

  3. Do one of the following:

     * To create a log bucket and then upgrade the log bucket to use Observability Analytics:

       1. Set the `LogBucket.analyticsEnabled` boolean to `true`.

**Note:** After a log bucket has been upgraded to use Observability Analytics, you can't reconfigure the log bucket to change or remove the use of Observability Analytics.
       2. Call the asynchronous method [`projects.locations.buckets.createAsync`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/createAsync) to create the bucket.

The response to the asynchronous methods is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains the status. For more information, see Asynchronous API methods.

The `createAsync` method takes several minutes to complete. This method doesn't generate an error message or fail when the `analyticsEnabled` boolean is set to `true`.

     * Otherwise, call the synchronous method [`projects.locations.buckets.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create) to create the bucket. 




After creating a bucket, create a sink to route log entries to your bucket and [configure log views](https://docs.cloud.google.com/logging/docs/logs-views) to control who can access the logs in your new bucket and which logs are accessible to them. You can also update the bucket to configure custom retention and [restricted fields](https://docs.cloud.google.com/logging/docs/field-level-acl).

## List and view details of log buckets

This section describes how to list and view the details of the log buckets in a project, folder, or organization.

### List buckets

To list the log buckets associated with a Google Cloud project, and to see details such as retention settings, do the following:

###  Google Cloud console 

In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

A table named **Log buckets** lists the buckets associated with the current Google Cloud project.

The table lists the following attributes for each log bucket:

  * **Name** : The name of the log bucket.
  * **Description** : The description of the bucket.
  * **Retention period** : The number of days that the bucket's data will be stored by Cloud Logging.
  * **Region** : The geographic location in which the bucket's data is stored.
  * **Status** : Whether the bucket is locked or unlocked.



If a bucket is pending deletion by Cloud Logging, then its table entry is annotated with a _warning_ **warning** symbol.

###  gcloud 

Run the [`gcloud logging buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/list) command:
    
    
    gcloud logging buckets list

You see the following attributes for the log buckets:

  * `LOCATION`: The [region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) in which the bucket's data is stored.
  * `BUCKET_ID`: The name of the log bucket.
  * `RETENTION_DAYS`: The number of days that the bucket's data will be stored by Cloud Logging.
  * `LIFECYCLE_STATE`: Indicates whether the bucket is pending deletion by Cloud Logging.
  * `LOCKED`: Whether the bucket is locked or unlocked.
  * `CREATE_TIME`: A timestamp that indicates when the bucket was created.
  * `UPDATE_TIME`: A timestamp that indicates when the bucket was last modified.



You can also view the attributes for just one bucket. For example, to view the details for the `_Default` log bucket in the `global` region, run the [`gcloud logging buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/describe) command:
    
    
    gcloud logging buckets describe _Default --location=global
    

###  REST 

To list the log buckets associated with a Google Cloud project, use [`projects.locations.buckets.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list) in the Logging API.

### View a bucket's details

The details of a log bucket include the name, description, location, and retention period. You can also view information about when the log bucket was created and last updated, and the name of the linked BigQuery dataset, when one exists.

To view the details of a single log bucket, do the following:

###  Google Cloud console 

In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

On the log bucket, click _more_vert_ **More** and then select **View bucket details**.

The dialog lists the following attributes for the log bucket:

  * **Name** : The name of the log bucket.
  * **Description** : The description of the log bucket.
  * **Retention period** : The number of days that the bucket's data will be stored by Cloud Logging.
  * **Region** : The geographic location in which the bucket's data is stored.


  * **Observability Analytics** : Indicates whether your bucket is upgraded to use Observability Analytics.
  * **BigQuery analysis** : Indicates whether a BigQuery dataset is linked to your bucket.
  * **BigQuery dataset** : Provides a link to your BigQuery dataset, which opens in the **BigQuery Studio** page. The date that BigQuery linking was enabled is also shown.



###  gcloud 

Run the [`gcloud logging buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/describe) command.

For example, the following command reports the details of the `_Default` bucket:
    
    
    gcloud logging buckets describe _Default --location=global
    

You see the following attributes for the log bucket:

  * `createTime`: A timestamp that indicates when the bucket was created.
  * `description`: The description of the log bucket.
  * `lifecycleState`: Indicates whether the bucket is pending deletion by Cloud Logging.
  * `name`: The name of the log bucket.
  * `retentionDays`: The number of days that the bucket's data will be stored by Cloud Logging.
  * `updateTime`: A timestamp that indicates when the bucket was last modified.



###  REST 

To view the details of a single log bucket, use [`projects.locations.buckets.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/get) in the Logging API.

## Manage buckets

This section describes how to manage your log buckets using the Google Cloud CLI or the Google Cloud console.

### Update a bucket

To update the properties of your bucket, such as the description or retention period, do the following:

###  Google Cloud console 

To update your bucket's properties, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. For the bucket you want to update, click _more_vert_ **More**.

  3. Select **Edit bucket**.

  4. Edit your bucket as needed.

  5. Click **Update bucket**.




###  gcloud 

To update your bucket's properties, run the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command:
    
    
    gcloud logging buckets update BUCKET_ID --location=LOCATION UPDATED_ATTRIBUTES

For example:
    
    
    gcloud logging buckets update my-bucket --location=global --description "Updated description"
    

###  REST 

To update your bucket's properties, use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API.

### Configure custom retention

**Note:** Effective April 1, 2023, retention costs apply to logs data retained longer than the [default retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) of the `_Default` bucket and user-defined log buckets. For pricing details, see the Cloud Logging sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. To review the billable storage for your log buckets, go to the **Logs Storage** page of the Google Cloud console. 

When you create a log bucket, you can customize the period that Cloud Logging stores logs in the bucket. You can also configure the retention period for the `_Default` log bucket when that log bucket is in a project.

You can't change the retention period of the `_Required` log bucket. You also can't extend the retention period of a log bucket that is in a folder or organization. However, you can create a log sink to route folder- or organization-level log entries to a log bucket that is in a project, and then configure the retention period of that log bucket.

If you shorten the retention period of a log bucket, then there is a 7-day grace period in which expired logs aren't deleted. You can't query or view the expired logs. However, during this 7-day period, you can restore full access by extending the bucket's retention period. Logs stored during the grace period count toward your retention costs.

Retention enforcement is an eventually-consistent process. If you write log entries to a log bucket when the log entries are older than the bucket's retention period, then you might be able to briefly see these log entries. For example, if you send log entries that are 10 days old to a log bucket with a retention period of 7 days, then those log entries are stored and then eventually purged. These log entries don't contribute to your retention costs. They do contribute to your storage costs. To minimize your storage costs, don't write log entries that are older than your bucket's retention period.

To update the retention period for a custom log bucket or for the `_Default` log bucket that is in a project, do the following:

###  Google Cloud console 

To update a log bucket's retention period, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. For the bucket you want to update, click _more_vert_ **More** , and then select **Edit bucket**.

  3. In the **Retention** field, enter the number of days, between 1 day and 3650 days, that you want Cloud Logging to retain your logs.

  4. Click **Update bucket**. Your new retention period appears in the **Logs bucket** list.




###  gcloud 

To update the retention period for a user-defined log bucket or for the `_Default` log bucket that is in a project, run the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command, after setting a value for RETENTION_DAYS:
    
    
    gcloud logging buckets update BUCKET_ID  --location=LOCATION --retention-days=RETENTION_DAYS

For example, to retain the logs in the `_Default` bucket in the `global` location for a year, your command would look like the following:
    
    
    gcloud logging buckets update _Default --location=global --retention-days=365

If you extend a bucket's retention period, then the retention rules apply going forward and not retroactively. Logs can't be recovered after the applicable retention period ends.

### Lock a bucket

**Warning:** Locking a log bucket is irreversible.

When you lock a bucket against updates, you also lock the bucket's retention policy. After a retention policy is locked, you can't delete the bucket until every log entry in the bucket has fulfilled the bucket's retention period. If you want to prevent the accidental deletion of a project that contains a locked log bucket, then add a lien to the project. To learn more, see [Protecting projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

To prevent anyone from updating or deleting a log bucket, lock the bucket. To lock the bucket, do the following:

###  Google Cloud console 

The Google Cloud console doesn't support locking a log bucket.

###  gcloud 

To lock your bucket, run the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command with the `--locked` flag:
    
    
    gcloud logging buckets update BUCKET_ID --location=LOCATION --locked

For example:
    
    
    gcloud logging buckets update my-bucket --location=global --locked
    

###  REST 

To lock your bucket's attributes, use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. Set the `locked` parameter to `true`.

### Delete a bucket

**Note:** If you delete a log bucket, then make sure that you also delete any log sinks that route log entries to that log bucket.

You can delete log buckets that satisfy one of the following:

  * The log bucket is unlocked.
  * The log bucket is locked and all log entries in the log bucket have fulfilled the bucket's retention period.



You can't delete a log bucket in any of the following situations:

  * The log bucket is locked against updates and it stores log entries that haven't fulfilled the bucket's retention period.


  * There are one or more links on the log bucket. To determine if there are links on your log bucket, you can use the Google Cloud console or run the [`gcloud logging links list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/list) command.

When necessary, delete links by using the [`gcloud logging links delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/delete) command. If you delete a link, then you also delete any associated artifacts, which might include a linked BigQuery dataset.




After you issue the delete command, the log bucket transitions to the [`DELETE_REQUESTED` state](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LifecycleState), and it stays in that state for 7 days. During this time period, Logging continues to route logs to the log bucket. You can stop routing logs to the log bucket by deleting or modifying the log sinks that route log entries to the bucket.

You can't create a new log bucket that uses the same name as a log bucket that is in the `DELETE_REQUESTED` state.

**Note:** Log buckets that are in the `DELETE_REQUESTED` state count toward the [quota](https://docs.cloud.google.com/logging/quotas#log-limits) of buckets per Google Cloud project until they are fully deleted.

To delete a log bucket, do the following:

###  Google Cloud console 

To delete a log bucket, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the bucket that you want to delete, and click _more_vert_**More**.

  3. If the **Linked dataset in BigQuery** column displays a link, then delete the linked BigQuery dataset:

     1. Click **Edit bucket**.
     2. Clear **Create a new BigQuery dataset that links to this bucket** , click **Done** , and then click **Update bucket**. 

After you return to the **Logs Storage** page, click _more_vert_**More** for the bucket you want to delete, then proceed to the next steps.




  1. Select **Delete bucket**.

  2. On the confirmation panel, click **Delete**.

  3. On the **Logs Storage** page, your bucket has an indicator that it's pending deletion. The bucket, including all the logs in it, is deleted after 7 days.




###  gcloud 

To delete a log bucket, run the [`gcloud logging buckets delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/delete) command:
    
    
    gcloud logging buckets delete BUCKET_ID --location=LOCATION

###  REST 

To delete a bucket, use [`projects.locations.buckets.delete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/delete) in the Logging API.

### Restore a deleted bucket

You can restore, or undelete, a log bucket that's in the pending deletion state. To restore a log bucket, do the following:

###  Google Cloud console 

To restore a log bucket that is pending deletion, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. For the bucket you want to restore, click _more_vert_ **More** , and then select **Restore deleted bucket**.

  3. On the confirmation panel, click **Restore**.

  4. On the **Logs Storage** page, the pending-deletion indicator is removed from your log bucket.




###  gcloud 

To restore a log bucket that is pending deletion, run the [`gcloud logging buckets undelete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete) command:
    
    
    gcloud logging buckets undelete BUCKET_ID --location=LOCATION

###  REST 

To restore a bucket that is pending deletion, use [`projects.locations.buckets.undelete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/undelete) in the Logging API.

## Enable Observability Analytics and querying from BigQuery

This section describes how to do the following:

  * Upgrade your log bucket so that you can analyze your log data by using Observability Analytics, which provides a SQL interface.

  * Create links on log buckets. A _link_ provides a connection between a log bucket and a linked BigQuery dataset. You can use BigQuery services to query the linked dataset.




### Upgrade a bucket to use Observability Analytics

After you upgrade a bucket to use Observability Analytics, any new log entries that arrive are available to analyze in the Observability Analytics interface. You can't undo an upgrade operation on a bucket.

To upgrade an existing bucket to use Observability Analytics, the following restrictions apply:

  * The log bucket was created at the Google Cloud project level.
  * The log bucket is [unlocked](https://docs.cloud.google.com/logging/docs/buckets#locking-logs-buckets) unless it is the `_Required` bucket.
  * There aren't pending updates to the bucket.
  * For projects inside a VPC Service Controls perimeter:

    1. The perimeter must not restrict the following services:

       * `logging.googleapis.com`
       * `cloudkms.googleapis.com`: Required for log buckets that use CMEK.
    2. You can't use identity-based ingress or egress rules to grant cross-perimeter access to the Cloud Key Management Service key when your log bucket and your Cloud KMS key are in different VPC Service Controls perimeters.




Upgrading a bucket might take as long as 10 minutes. For troubleshooting information, see [Troubleshoot upgrading a bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/troubleshoot-upgrade-bucket).

###  Google Cloud console 

To upgrade an existing bucket to use Observability Analytics, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the bucket that you want to upgrade.

  3. When the **Observability Analytics available** column displays **Upgrade** , you can upgrade the log bucket to use Observability Analytics. Click **Upgrade**.

A dialog opens. Click **Confirm**.




###  gcloud 

To upgrade your log bucket to use Observability Analytics, run the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command. You must set the `--enable-analytics` flag, and we recommend that you also include the `--async` flag:
    
    
    gcloud logging buckets update BUCKET_ID --location=LOCATION --enable-analytics --async

The flag `--async` forces the command to be asynchronous. The response is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object. Poll the [`projects.locations.operations.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.operations/get) method until the `Operation.done` field is set to `true`. Other fields in the `Operation` structure provide information about the success or failure of the request. For more information, see Asynchronous API methods.

**Note:** Don't update any other property of a log bucket when you upgrade the log bucket to use Observability Analytics. For example, a call to the `update` command that changes the retention period and upgrades the log bucket fails.

###  REST 

To upgrade a log bucket to use Observability Analytics, use the [`projects.locations.buckets.updateAsync`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/updateAsync) method of the Cloud Logging API.

Prepare the arguments to the method as follows:

  1. Set the `LogBucket.analyticsEnabled` boolean to `true`.
  2. For the query parameter of the command, use `updateMask=analyticsEnabled`.



The response to the asynchronous methods is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains information about the success or failure of the request. For more information, see Asynchronous API methods.

The `updateAsync` method might take several minutes to complete.

### Create a linked BigQuery dataset

When you want to use the capabilities of BigQuery to analyze your log data, upgrade a log bucket to use Observability Analytics, and then create a [linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets). With this configuration, Logging stores your log data but BigQuery can read the log data.

**Note:** A log bucket can be linked to at most one BigQuery dataset.

###  Google Cloud console 

To create a link to a BigQuery dataset for an existing log bucket, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the log bucket and verify that the **Observability Analytics available** column displays **Open**.

If this column displays **Upgrade** , then the log bucket hasn't been upgraded to use Observability Analytics. Configure Observability Analytics:

     1. Click **Upgrade**.
     2. Click **Confirm** in the dialog.

After the upgrade completes, proceed to the next step.

  3. On the log bucket, click **More** _more_vert_ , and then click **Edit bucket**.

The **Edit log bucket** dialog opens.

  4. Select **Create a new BigQuery dataset that links to this bucket** and enter the name for the new dataset.

The dataset name must be unique for each Google Cloud project. If you enter the name of an existing dataset, then you receive the following error: `Dataset name must be unique in the selected region.`

  5. Click **Done** and then click **Update bucket**.

After Logging displays the linked dataset name on the **Logs Storage** page, it might take several minutes before BigQuery recognizes the dataset.




###  gcloud 

To create a linked dataset for a log bucket that is upgraded to use Observability Analytics, run the [`gcloud logging links create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/create) command:
    
    
    gcloud logging links create LINK_ID --bucket=BUCKET_ID --location=LOCATION

The LINK_ID that you provide is used as the name of the BigQuery dataset, and the value of this field must be unique for your Google Cloud project.

The `links create` command is asynchronous. The return of an asynchronous method is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object, and it contains information about the progress of the method. When the method completes, the `Operation` object contains the status. For more information, see [Asynchronous API methods](https://docs.cloud.google.com/logging/docs/buckets#async-command).

The `links create` command takes several minutes to complete.

For example, the following command creates a linked dataset named `mylink` for the log bucket named `my-bucket`:
    
    
    gcloud logging links create mylink --bucket=my-bucket --location=global
    

The dataset name must be unique for each Google Cloud project. If you attempt to create a dataset with the same name as an existing dataset, then you receive the following error:

`BigQuery dataset with name "LINK_ID" already exists.`

If you attempt to create a linked dataset for a log bucket that isn't upgraded to use Observability Analytics, then the following error is reported:

`A link can only be created for an analytics-enabled bucket.`

###  REST 

To create a linked a BigQuery dataset for an existing log bucket that is upgraded use Observability Analytics, call the asynchronous [`projects.locations.buckets.links.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/create) method of the Cloud Logging API.

Prepare the arguments to the method as follows:

  1. Construct the request body for the `create` command. The request body is formatted as a [`Link`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links#Link) object.
  2. For the query parameter of the command, use `linkId=LINK_ID`. The LINK_ID that you provide is used as the name of the BigQuery dataset, and the value of this field must be unique for your Google Cloud project..



The response to the asynchronous methods is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains the status. For more information, see [Asynchronous API methods](https://docs.cloud.google.com/logging/docs/buckets#async-command).

The `links.create` method takes several minutes to complete.

The dataset name must be unique for each Google Cloud project. If you attempt to create a dataset with the same name as an existing dataset, then you receive the following error:

`BigQuery dataset with name "LINK_ID" already exists.`

If you attempt to create a linked dataset for a log bucket that isn't upgraded to use Observability Analytics, then the following error is reported:

`A link can only be created for an analytics-enabled bucket.`

### Poll asynchronous API methods

The response of an asynchronous method like [`projects.locations.buckets.createAsync`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/createAsync) is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object.

Applications that call an asynchronous API method should poll the [`operation.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.operations/get) method until the value of the `Operation.done` field is `true`:

  * If `done` is `false`, then the operation is in progress.

To refresh the status information, send a `GET` request to the [`operation.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.operations/get) method.

  * If `done` is `true`, then the operation is complete and either the `error` or `response` field is set:

    * `error`: When set, the asynchronous operation failed. The value of this field is a `Status` object that contains a gRPC error code and an error message.
    * `response`: When set, the asynchronous operation completed successfully, and the value reflects the result.



To poll an asynchronous command by using the Google Cloud CLI, run the following command:
    
    
    gcloud logging operations describe OPERATION_ID --location=LOCATION --project=PROJECT_ID

For more information, see [`gcloud logging operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/operations/describe).

## Read and write log entries

You don't directly write logs to a log bucket. Rather, you write logs to a Google Cloud resource: a Google Cloud project, folder, or organization. The sinks in the parent resource then route the logs to destinations, including log buckets. A sink routes logs to a log bucket destination when the logs match the sink's filter and the sink has permission to route the logs to the log bucket. For more information, see [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview).

Each log bucket has a set of log views. To read logs from a log bucket, you need access to a log view on the log bucket. Log views let you grant a user access to only a subset of the logs stored in a log bucket. To learn more about log views, see [Store log entries](https://docs.cloud.google.com/logging/docs/store-log-entries) and [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

To read logs from a log bucket, do the following:

###  Google Cloud console 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. To customize which logs are displayed in the Logs Explorer, click **Refine scope** , and then select an option. For example, you can view logs stored in a project or by log view.

  3. Click **Apply**. The **Query results** pane reloads with logs that match the option you selected.




For more information, see [Logs Explorer overview: Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

###  gcloud 

To read logs from a log bucket, use the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command and add a [`LOG_FILTER`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#LOG_FILTER) to select data:
    
    
    gcloud logging read LOG_FILTER --bucket=BUCKET_ID --location=LOCATION --view=LOG_VIEW_ID

###  REST 

To read logs from a log bucket, use the [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method. Set `resourceNames` to specify the appropriate bucket and log view, and set `filter` to select data.

For detailed information about the filtering syntax, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

## Monitor volume

This section describes how you can monitor the volume of your log data.

### Track volume of logs stored in log buckets

The **Logs Storage** page in the Google Cloud console tracks the volume of log data stored in log buckets:

In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

The **Logs Storage** page displays a summary of statistics for your Google Cloud project:

![The summary statistics report the amount of log data stored in log buckets
for the selected project.](https://docs.cloud.google.com/static/logging/docs/images/log-storage-summary.png)

The following statistics are reported:

  * **Current month ingestion** : The amount of log data that your Google Cloud project has stored in log buckets since the first day of the current calendar month.

  * **Previous month ingestion** : The amount of log data that your Google Cloud project stored in log buckets in the last calendar month.

  * **Projected ingestion by EOM** : The estimated amount of log data that your Google Cloud project will store in log buckets by the end of the current calendar month, based on current usage.

  * **Current month billable storage** : The amount of log data that has been retained for over 30 days that is billed.




The previous statistics don't include logs in the [`_Required` bucket](https://docs.cloud.google.com/logging/docs/store-log-entries#required-bucket). The logs in that bucket can't be excluded or disabled.

The **Log Router** page in the Google Cloud console gives you tools that you can use to minimize any charges for storing logs in log buckets or for storage that exceeds your monthly allotment. You can do the following:

  * Disable logs from being stored at the bucket level.
  * Exclude certain log entries from being stored in log buckets.



For more information, see [Manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks).

### Alert on monthly log bytes stored in log buckets

To create an alerting policy, go to the **Logs Storage** page in the Google Cloud console, click _add_alert_ **Create usage alert** , and complete the dialog. The **Create alerting policy** page prepopulates the metric type field with `logging.googleapis.com/billing/bytes_ingested`.

To create an alerting policy that triggers when the number of log bytes written to your log buckets exceeds your user-defined limit for [Cloud Logging](https://docs.cloud.google.com/logging/docs), use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Global**.  
In the **Metric categories** menu, select **Logs-based metric**.  
In the **Metrics** menu, select **Monthly log bytes ingested**.   
**Filter** | None.  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `60 m`  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | You determine the acceptable value.  
**Retest window** | Minimum acceptable value is 30 minutes.  
  
For more information about alerting policies, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

## Troubleshoot common issues

If you encounter problems when using log buckets, refer to the following troubleshooting steps and answers to common questions.

### Why can't I delete this bucket?

If you're trying to delete a bucket, do the following:

  * Verify that you have the correct permissions to delete the bucket. For the list of the permissions that you need, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

  * Determine whether the bucket is locked by listing the bucket's attributes. If the bucket is locked, check the bucket's retention period. You can't delete a locked bucket until all of the logs in the bucket have fulfilled the bucket's retention period.



  * Verify that the log bucket doesn't have any links. You can't delete a log buckets that contains links.

The following error is shown in response to a `delete` command on a log bucket that has a linked BigQuery dataset:
        
        FAILED_PRECONDITION: This bucket is used for advanced analytics and has an active link. The link must be deleted first before deleting the bucket
        

To list the links associated with a log bucket, run the [`gcloud logging links list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/list) command or run the [`projects.locations.buckets.links.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/list) API method.

To delete links, use the [`gcloud logging links delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/list) command.




### Which service accounts are routing logs to my bucket?

To determine if any service accounts have IAM permissions to route logs to your bucket, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. From the **Permissions** tab, view by **Roles**. You see a table with all the IAM roles and principals associated with your Google Cloud project.

  3. In the table's **Filter** **text box** _filter_list_ , enter **Logs Bucket Writer**.

You see any principals with the **Logs Bucket Writer** role. If a principal is a service account, its ID contains the string `gserviceaccount.com`.

  4. Optional: If you want to remove a service account from being able to route logs to your Google Cloud project, select the **check box** _check_box_outline_blank_ for the service account and click **Remove**.




### Why do I see logs for a Google Cloud project even though I excluded them from my `_Default` sink?

You might be viewing logs in a log bucket in a [centralized Google Cloud project](https://docs.cloud.google.com/logging/docs/central-log-storage), which aggregates logs from across your organization.

If you're using the Logs Explorer to access these logs and see logs that you excluded from the `_Default` sink, then your view might be set to the Google Cloud project level.

To fix this issue, select **Log view** in the [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope) menu and then select the log view associated with the `_Default` bucket in your Google Cloud project. You shouldn't see the excluded logs anymore.

## What's next

For information on the log bucket API methods, refer to the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) reference documentation.

If you manage an organization or a folder, then you can specify the location of the `_Default` and `_Required` log buckets of child resources. You can also configure whether log buckets use CMEK and the behavior of the `_Default` log sink. For more information, see [Configure default settings for organizations and folders](https://docs.cloud.google.com/logging/docs/default-settings).

For information on addressing common use cases with log buckets, see the following topics:

  * [Aggregate and store your organization's logs](https://docs.cloud.google.com/logging/docs/central-log-storage).


  * [Multi-tenant logging on GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/multi-tenant-logging).


  * [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
