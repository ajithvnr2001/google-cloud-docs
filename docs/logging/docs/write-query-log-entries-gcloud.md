---
url: https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud/
title: Quickstart: Write and query log entries with the gcloud CLI \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:57.447308+00:00
---

# Quickstart: Write and query log entries with the gcloud CLI  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write and query log entries with the gcloud CLI

This document introduces you to some of the capabilities of Cloud Logging and shows you how to do the following:

  * Write log entries by using the Google Cloud CLI.
  * List log entries by using the gcloud CLI.
  * List log entries by using the Logging API.
  * View and query log entries by using the Logs Explorer.



## Before you begin

You must have a Google Cloud project with billing enabled to complete this quickstart. If you don't have a Google Cloud project, or if you don't have billing enabled for your Google Cloud project, then do the following: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

To get the permissions that you need to create, list, and delete log entries, ask your administrator to grant you the [Logging Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The Logs Writer (`roles/logging.logWriter`) and Logs Viewer (`roles/logging.viewer`) roles contain the permissions to create and list log entries. To delete log entries, grant the Logging Admin (`roles/logging.admin`) role, which contains the permissions to create, list, and delete log entries. Note that the Logging Admin (`roles/logging.admin`) role also grants permissions to perform all actions in Logging.

## Write log entries by using the gcloud CLI

Logging supports log entries with structured and unstructured data. Structured data consists of a JSON data structure; for example, `{"weather": "partly cloudy"}`. Unstructured data is a string of characters; for example, `"A simple entry"`.

In the next steps, you use the gcloud CLI to write a log entry with unstructured data and a log entry with structured data. The [gcloud CLI](https://docs.cloud.google.com/sdk/docs) provide a command-line interface to the Cloud Logging API.

  1. Write a log entry with unstructured data to the log `my-test-log`, run the [`gcloud logging write`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/write) command:
         
         gcloud logging write my-test-log "A simple entry."
         

After the command completes, you see the message: `Created log entry`.

  2. Write a log entry with structured data to the log `my-test-log`:
         
         gcloud logging write --payload-type=json my-test-log '{ "message": "My second entry", "weather": "partly cloudy"}'
         

When you write a log entry with structured data, you must include `--payload-type=json`. If you omit this field, then Logging interprets the payload as unstructured data.




If the log `my-test-log` doesn't exist, then Logging creates the log when the log entry is received.

## List log entries by using the gcloud CLI

You can retrieve log entries from Logging and display them by using the gcloud CLI. For example, to retrieve and display the log entries with a resource type of `global`, run the following command:
    
    
    gcloud logging read "resource.type=global"
    

The command returns a result similar to the following:
    
    
    ---
    insertId: jpj9zjf73t1mn
    jsonPayload:
      message: My second entry
      weather: partly cloudy
    logName: projects/myloggingproject/logs/my-test-log
    receiveTimestamp: '2018-11-01T18:39:31.114507977Z'
    resource:
      labels:
        project_id: myloggingproject
      type: global
    timestamp: '2018-11-01T18:39:31.114507977Z'
    ---
    insertId: vd4m1if7h7u1a
    logName: projects/myloggingproject/logs/my-test-log
    receiveTimestamp: '2018-11-01T18:39:19.718100792Z'
    resource:
      labels:
        project_id: myloggingproject
      type: global
    textPayload: A simple entry
    timestamp: '2018-11-01T18:39:19.718100792Z'
    

For information about reading logs, see the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) reference documentation.

## List log entries by using APIs Explorer

To run Logging API methods without writing any code, see [Using the APIs Explorer](https://docs.cloud.google.com/logging/docs/api). To read a list of log entries from Logging, do the following:

  1. Go to the API reference page for the `entries.list` API method:

[Go to entries.list API page](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list)

  2. Configure and run the API command:

     1. Replace PROJECT_ID in the following text:
            
            "resourceNames": [
            "projects/PROJECT_ID"
            ],
            "filter": "resource.type=global",
            "orderBy": "timestamp desc"
            

     2. Copy the updated text from the previous step, and paste it into the **Request body** field of APIs Explorer.

     3. Click **Execute**.

The method returns a response similar to the following:
    
    {
      "entries": [
        {
          "textPayload": "A simple entry",
          "insertId": "vd4m1if7h7u1a",
          "resource": {
            "type": "global",
            "labels": {
              "project_id": "myloggingproject"
            }
          },
          "timestamp": "2018-11-01T18:39:19.718100792Z",
          "logName": "projects/myloggingproject/logs/my-test-log",
          "receiveTimestamp": "2018-11-01T18:39:19.718100792Z"
        },
        {
          "insertId": "jpj9zjf73t1mn",
          "jsonPayload": {
            "message": "My second entry",
            "weather": "partly cloudy"
          },
          "resource": {
            "type": "global",
            "labels": {
              "project_id": "myloggingproject"
            }
          },
          "timestamp": "2018-11-01T18:39:31.114507977Z",
          "logName": "projects/myloggingproject/logs/my-test-log",
          "receiveTimestamp": "2018-11-01T18:39:31.114507977Z"
        }
      ]
    }
    




## View log entries in the Logs Explorer

To view log entries in the Google Cloud console, you can use the Logs Explorer. Most Google Cloud projects store a large number of logs; you can select certain log entries by writing a query.

To view the log entries that you wrote using the Logs Explorer, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

Ensure your Google Cloud project is selected in the Google Cloud navigation bar. If necessary, use the Google Cloud project drop-down list to select your Google Cloud project.

  2. In the **Resource** menu, select **Global**.

If you don't see the **Global** menu option or if you don't see your log entries, then wait a few minutes and refresh the page. It can take a few minutes for Logging to receive log entries.

  3. To view the details of a log entry, click its _chevron_right_ **Menu**.

The first log entry has its data stored in `textPayload`. The second log entry contains structured data that is stored in `jsonPayload`. The structured payload contains the keys `message` and `weather`.

**Note:** When `message` is a key for a structured log entry, Logging uses it as the summary of the log entry when the entry isn't expanded.



For information about the data format of log entries, see the [`LogEntry` type](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

## Query log entries in the Logs Explorer

You can query log entries by using the query editor and, with structured logs, by the key and value. For example, to display all log entries that contain the text `simple`, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Resource** menu, select **Global**.

  3. In the query editor, enter the string `simple` in quotation marks. The logs display shows only the log entry `A simple entry.`

  4. After you have viewed your log, remove the query string you added and click **Run query**. Both log entries reappear in the display.




To display all log entries with structured data that have a key of `weather` where the `value` field contains `partly`, do the following:

  1. The query editor contains the line `resource.type="global"`. Enter the following command:
         
         jsonPayload.weather:partly
         

  2. Click **Run query**. The result is the single log entry `My second entry`.




Logs Explorer also offers saved, suggested, and recent queries. For more information about queries, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).

For sample queries, see [Sample queries using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library).

## Troubleshooting

  * Typographical errors and unknown field names result in the gcloud CLI commands completing with **invalid argument** messages. For example, if you forget the period in `resource.type`, then it results in the error:
        
        ERROR: (gcloud.logging.read) INVALID_ARGUMENT: Field not found: 'resourcetype'.
        

  * When Cloud Logging hasn't been granted the necessary access permissions, the gcloud CLI commands complete with **permission denied** messages. For example, if a Compute Engine VM instance is configured with the default API settings, then the `list` command completes with a permission denied error:
        
        ERROR: (gcloud.logging.read) PERMISSION_DENIED: Request had insufficient authentication scopes.
        

To fix this condition, modify your Compute Engine VM instance permissions to grant Cloud Logging read permission by doing the following:

    1. Go to the **VM instance details** page for your VM instance. Click **Stop**. This action might take a minute or two to complete.
    2. To modify the configuration, click **Edit**.
    3. Search for the header **Cloud API access scopes** , and click **Details** to display the settings for each API. Change the entry from Cloud Logging API to **Full**. Click **Save**.
    4. To restart your VM instance, click **Start**. After a few moments, your VM is ready to use.


  * When APIs Explorer can't complete your command, or requires additional authorization, it displays a message or error code:

    * **200 response code and no entries** : If the message `nextPageToken` is displayed, then it indicates that APIs Explorer didn't have time to complete the search. Add a `pageToken` to your request, set the value to be the same as that given with the key `nextPageToken`, and then retry the command.
    * **400 response code** : The query value is invalid. For example, if you misspell `global` as `gloobal`, then the message is `Unsupported resource type: gloobal`.
    * **404 response code** : The project ID is invalid. Check the spelling of your project identifier.
    * You might be asked to sign into your Google Cloud project and permit APIs Explorer to access your account.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. (Optional) To delete the log entries you created, run the following `gcloud` command:
         
         gcloud logging logs delete my-test-log
         

If you don't delete your log entries, then they expire and are removed. For retention information, see [Quotas & limits](https://docs.cloud.google.com/logging/quotas).




## What's next

  * For details on the Logging command-line interface, read the reference pages for the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging) command group.
  * For documentation on the Logging API, see [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest).
  * For details on the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).


  * To learn how to collect log entries from your VM instances in Logging, see [Google Cloud Observability agents](https://docs.cloud.google.com/logging/docs/agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
