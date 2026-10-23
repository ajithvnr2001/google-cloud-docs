---
url: https://docs.cloud.google.com/logging/docs/write-query-log-entries-python/
title: Quickstart: Write and query log entries using a Python script \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:04.998990+00:00
---

# Quickstart: Write and query log entries using a Python script  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/write-query-log-entries-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write and query log entries using a Python script

This quickstart introduces you to some of the capabilities of Cloud Logging and shows you how to do the following:

  * Write log entries using a Python script.
  * View log entries using a Python script.
  * Delete log entries using a Python script.
  * Route logs to a Cloud Storage bucket.



Logging can route log entries to the following destinations:

  * Cloud Storage buckets
  * BigQuery datasets
  * Pub/Sub
  * Logging buckets
  * Google Cloud projects



## Before you begin

You must have a Google Cloud project with billing enabled to complete this quickstart. If you don't have a Google Cloud project, or if you don't have billing enabled for your Google Cloud project, do the following: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




This quickstart uses Cloud Logging and Cloud Storage. Use of these resources can incur a cost to you. When you finish this quickstart, you can avoid continued billing by deleting the resources that you created. See Clean up on this page for more details.

### Required roles

To get the permissions that you need to create, list, and delete log entries and Cloud Storage buckets, ask your administrator to grant you the following IAM roles on your project: 

  * Create, list, and delete log entries: [Logging Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) 
  * Create, list, and delete Cloud Storage buckets: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The Logs Writer (`roles/logging.logWriter`) and Logs Viewer (`roles/logging.viewer`) roles contain the permissions to create and list log entries. To delete log entries, grant the Logging Admin (`roles/logging.admin`) role, which contains the permissions to create, list, and delete log entries. Note that the Logging Admin (`roles/logging.admin`) role also grants permissions to perform all actions in Logging.

## Getting started

You can use the Cloud Shell environment or a generic Linux environment to complete this quickstart. Python is preinstalled in the Cloud Shell.

###  Cloud Shell 

  1. Open the Cloud Shell and verify your Google Cloud project configuration:

     1. From the Google Cloud console, click _terminal_ **Activate Cloud Shell**.

The Cloud Shell opens in a window and displays a welcome message.

     2. The welcome message echoes the configured Google Cloud project ID. If this isn't the Google Cloud project that you want to use, run the following command after replacing PROJECT_ID with your project's ID:
            
            gcloud config set project PROJECT_ID
            




### Linux

  1. Ensure that Python is installed and configured. For information about preparing your machine for Python development, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

  2. Install the Cloud Logging client library:
         
         pip install --upgrade google-cloud-logging
         

  3. Set up the Identity and Access Management permissions for your Google Cloud project. In the following steps, you create a service account for your Google Cloud project, and then you generate and download a file to your Linux workstation.

     1. In the Google Cloud console, go to the **Service Accounts** page: 

[Go to **Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. Select your quickstart Google Cloud project, and then click **Create Service Account** :

        * Enter an account name.
        * Enter an account description.
        * Click **Create and continue**.
     3. Click the **Select a role** field and select **Logging Admin**.

     4. Click **Done** to finish creating the service account.

     5. Create a key file and download it to your workstation:

        * For your service account, click _more_vert_ **More options** , and select **Manage keys**.
        * In the **Keys** pane, click **Add key**.
        * Click **Create new key**.
        * For the **Key type** , select **JSON** and then click **Create**. After a moment, a window displays a message similar to the following:

![Private key saved save to your computer.](https://docs.cloud.google.com/static/logging/docs/images/key-saved-20181124.png)

  4. On your Linux workstation, provide your authentication credentials to your application by setting the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path to your key file. For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/FILE_NAME.json"
         

This environment variable only applies to your current shell session, so if you open a new session, set the variable again.




## Clone source

To configure your Cloud Shell for this quickstart, do the following:

  1. Clone the GitHub project `python-logging`:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples
         

The directory `samples/snippets` contains the two scripts used in this quickstart:

     * `snippets.py` lets you manage entries in a log.
     * `export.py` lets you manage log exports.
  2. Change to the `snippets` directory:
         
         cd logging/samples/snippets
         




## Write log entries

The `snippets.py` script uses the Python client libraries to write log entries to Logging. When the `write` option is specified on the command line, the script writes the following log entries:

  * An entry with unstructured data and no specified severity level.
  * An entry with unstructured data and a severity level of `ERROR`.
  * An entry with JSON structured data and no specified severity level.



To write new log entries to the log `my-log`, run the `snippets.py` script with the `write` option:
    
    
    python snippets.py my-log write
    

## View log entries

To view the log entries in the Cloud Shell, run the `snippets.py` script with the `list` option:
    
    
    python snippets.py my-log list
    

The command completes with the result:
    
    
    Listing entries for logger my-log:
    * 2025-11-13T16:05:35.548471+00:00: Hello, world!
    * 2025-11-13T16:05:35.647190+00:00: Goodbye, world!
    * 2025-11-13T16:05:35.726315+00:00: {u'favorite_color': u'Blue', u'quest': u'Find the Holy Grail', u'name': u'King Arthur'}
    

If the result doesn't show any entries, then retry the command. It takes a few moments for Logging to receive and process log entries.

You can also view the log entries you wrote by using the Logs Explorer. For more details, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Delete log entries

To delete all of the log entries in the log `my-log`, run the `snippets.py` script with the option `delete`:
    
    
    python snippets.py my-log delete
    

The command completes with the result:

`Deleted all logging entries for my-log`.

## Route logs

In this section, you do the following:

  * Create a Cloud Storage bucket as the destination for your data.
  * Create a sink that copies new log entries to the destination.
  * Update the permissions of your Cloud Storage bucket.
  * Write log entries to Logging.
  * Optionally, verify the content of your Cloud Storage bucket.



### Create destination

The export destination for this quickstart is a Cloud Storage bucket. To create a Cloud Storage bucket, do the following:

  1. In the Google Cloud console, go to the **Buckets** page: 

[Go to **Buckets**](https://console.cloud.google.com/storage/browser)

If you use the search bar to find this page, then select the result whose subheading is **Cloud Storage**.

  2. Click **Create bucket**.
  3. Enter a name for your bucket. This quickstart uses the name `myloggingproject-1`.
  4. For **Location type** , select **Region** , which selects a bucket location with the lowest latency.
  5. For **Set a default class** , select **Standard**.
  6. For **Access control** , select **Fine-grained**.
  7. For **Protection tools** , select **None** , and then click **Create**.



### Create sink

A sink is a rule that determines if Logging routes a newly arrived log entry to a destination. A sink has three attributes:

  * Name
  * Destination
  * Filter



For more information about sinks, see [About log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

If a newly arrived log entry meets the query conditions, then that log entry is routed to the destination.

The `export.py` script uses the Python client libraries to create, list, modify and delete sinks. To create the sink `mysink` that exports all log entries with a severity of at least `INFO` to the Cloud Storage bucket `myloggingproject-1`, run the following command:
    
    
    python export.py create mysink myloggingproject-1 "severity>=INFO"
    

The script returns the following:

`Created sink mysink`

To view your sinks, run the `export.py` script with the `list` option:
    
    
    python export.py list
    

The script returns the following:

`mysink: severity>=INFO -> storage.googleapis.com/myloggingproject-1`

### Update destination permissions

The permissions of the destination, in this case, your Cloud Storage bucket, aren't modified when you create a sink by using the `export.py` script. You must change the permission settings of your Cloud Storage bucket to grant permissions to write to your sink. For information about service accounts, access scopes, and Identity and Access Management roles, see [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).

To update the permissions on your Cloud Storage bucket:

  1. Identify your sink's **Writer Identity** :

     1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

You see a summary table of your sinks.

     2. Find your sink in the table, select _more_vert_ **Menu** , and then select **View sink details**.

     3. Copy the writer identity to your clipboard.

  2. In the Google Cloud console, go to the **Buckets** page: 

[Go to **Buckets**](https://console.cloud.google.com/storage/browser)

If you use the search bar to find this page, then select the result whose subheading is **Cloud Storage**.

  3. To open the detailed view, click the name of your bucket.

  4. Select **Permissions** and click **Grant Access**.

  5. Paste the writer identity into the **New principals** box. Remove the `serviceAccount:` prefix from the writer identity address.

  6. Set the **Role** to `Storage Admin`, then click **Save**.




For more information, see [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth).

### Validate sink

To validate that your sink and destination are properly configured, do the following:

  1. Write new log entries to the log `my-log`:
         
         python snippets.py my-log write
         

  2. View your Cloud Storage bucket's contents:

     1. In the Google Cloud console, go to the **Buckets** page: 

[Go to **Buckets**](https://console.cloud.google.com/storage/browser)

If you use the search bar to find this page, then select the result whose subheading is **Cloud Storage**.

     2. To open the detailed view, click the name of your bucket. The detailed view lists the folders that contain data. If there isn't data in your bucket, the following message is displayed:

`There are no live objects in this bucket.`

As described in [Late-arriving log entries](https://docs.cloud.google.com/logging/docs/export/storage#gcs-availability), it might take 2 or 3 hours before the first entries appear at the destination, or before you are notified of a configuration error.

After your bucket has received data, the detailed view shows a result similar to:

![Bucket contents detailed view.](https://docs.cloud.google.com/static/logging/docs/images/py-bucket-dir-20181116.png)

     3. The data in each folder is organized in a series of folders labeled with the top-level folder consisting of a log name, and then successively, the year, month, and day. To view the data that was exported by your sink, click the folder name `my-log`, and then continue clicking through the year, month, and day subfolders until you reach a file that ends with `json`:

![Bucket contents subfolder view.](https://docs.cloud.google.com/static/logging/docs/images/py-bucket-detail-20181116.png)

     4. The JSON file contains the log entries that were exported to your Cloud Storage bucket. Click the name of the JSON file to see its contents. The contents are similar to:
            
            {"insertId":"yf1cshfoivz48",
             "logName":"projects/loggingproject-222616/logs/my-log",
             "receiveTimestamp":"2018-11-15T23:06:14.738729911Z",
             "resource":{"labels":{"project_id":"loggingproject-222616"},"type":"global"},
             "severity":"ERROR",
             "textPayload":"Goodbye, world!",
             "timestamp":"2018-11-15T23:06:14.738729911Z"}
            

Because the severity level of `ERROR` is greater than the severity level of `INFO`, the log entry containing the string '"Goodbye, world!"' is exported to the sink destination. The other log entries that were written weren't exported to the destination because their severity level was set to the default value, and the default severity level is less than `INFO`.




### Troubleshooting

There are several reasons why a Cloud Storage bucket might be empty:

  * The bucket hasn't received data. It might take 2 or 3 hours before the first entries appear at the destination, or before you are notified of a configuration error. For more information, see [Late-arriving log entries](https://docs.cloud.google.com/logging/docs/export/storage#gcs-availability).

  * There is a configuration error. In this case, you will receive an email message similar to the following subject line:
        
        [ACTION REQUIRED] Logging export config error in myloggingproject.

The content of the email body describes the configuration issue. For example, if you don't update your destination permissions, then the email lists the following error code:
        
        bucket_permission_denied

To correct this particular condition, see Update destination permissions on this page.

  * No log entries were written after the sink was created. The sink is applied only to newly arriving log entries. To correct this situation, write new log entries:
        
        python snippets.py my-log write
        




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. (Optional) Delete the log entries you created. If you don't delete your log entries, they will expire and be removed. See [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

To delete all log entries in the log `my-log`, run the following command:
         
         python snippets.py my-log delete
         

  2. Delete your Google Cloud project or delete your quickstart resources.

     * To delete your Google Cloud project, from the Google Cloud console **Project Info** pane, click **Go to project settings** , and then click **Shut down**.

     * To delete your quickstart resources:

       1. Delete your sink by running the following command:
              
              python export.py delete mysink
              

       2. Delete your Cloud Storage bucket. Go to the Google Cloud console and click **Storage > Buckets**. Place a check in the box next to your bucket name and then click **Delete**.




## What's next

  * To learn how to read, write, and configure logs from your applications, see [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest).
  * For information about the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * To learn how to route your logs data to supported destinations, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).
  * To learn how to collect log entries from your VM instances, see [Ops Agent overview](https://docs.cloud.google.com/logging/docs/agent/ops-agent).
  * For information about auditing and compliance, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
