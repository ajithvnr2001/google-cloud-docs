---
url: https://docs.cloud.google.com/logging/docs/routing/user-managed-service-accounts/
title: Configure log sinks with user-managed service accounts \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:07.700496+00:00
---

# Configure log sinks with user-managed service accounts  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/routing/user-managed-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure log sinks with user-managed service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to route log entries by creating sinks that are configured with user-managed service accounts. By default, Logging uses a Logging service account for all sinks in a resource. However, if your log sinks are in different projects, then you can create and manage your own user-managed service account, which lets you centrally manage Identity and Access Management permissions from the project that contains your user-managed service account.

You can only create a sink that uses a user-managed service account when the sink destination is a log bucket or a Google Cloud project. The example in this document illustrates how to set up a sink that uses a user-managed service account where the destination is a log bucket.

We recommend that you review your log sink configuration when you make any changes to your log storage. For example, if you delete the destination of a log sink, then delete the corresponding log sink.

## Before you begin

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Ensure that you have a user-managed service account and then set the following variables to appropriate values for your user-managed service account:

     * CUSTOM_SA_PROJECT_ID: The project ID of the project that contains your user-managed service account.

     * CUSTOM_SA: The email address of your user-managed service account.

For information about how to create a service account, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

  3. Ensure that you have a log bucket that can serve as the destination of a log sink, and then set the following variables to values that are appropriate for your log bucket. If necessary, [create a log bucket](https://docs.cloud.google.com/logging/docs/buckets):

     * LOG_BUCKET_PROJECT_ID: The project ID of the project containing your log bucket.

     * LOCATION: The location of your log bucket.

     * BUCKET_NAME: The name of your log bucket.

  4. Identify the name of the Logging service account which exists in the project in which you plan to create the log sink, and then set the following variables to their appropriate values:

     * SINK_PROJECT_ID: The project ID of the project where you plan to create the log sink.

     * LOGGING_SA: The email address of the default Logging service account. To get this address, run the following command:
           
           gcloud logging settings describe --project=SINK_PROJECT_ID
           

In the response, the line beginning with `loggingServiceAccountId` lists the email address of your service account.

  5. In the project containing your user-managed service account, ensure the organization policy boolean constraint `iam.disableCrossProjectServiceAccountUsage` isn't enforced. By default, this constraint is enforced. To disable this constraint so that you can attach a service account to a resource in another project, run the following command:
         
         gcloud resource-manager org-policies disable-enforce \
         iam.disableCrossProjectServiceAccountUsage \
         --project=CUSTOM_SA_PROJECT_ID
         

For more information about enabling service accounts across projects, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).




## Grant IAM roles

This section describes the prerequisites for creating a sink that uses a user-managed service account.

### Let user-managed service account write log entries to the sink destination

Give the user-managed service account the permissions it needs to write log entries to the destination of the sink that you will create in a subsequent step. The destination of the sink will be a log bucket stored in the project named LOG_BUCKET_PROJECT_ID.

To give the required permissions to the user-managed service account, grant it the Logs Bucket Writer role (`roles/logging.bucketWriter`) on the project containing the log bucket:
    
    
    gcloud projects add-iam-policy-binding LOG_BUCKET_PROJECT_ID \
    --member='serviceAccount:CUSTOM_SA' \
    --role='roles/logging.bucketWriter'
    

For more information about the previous command, see [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

### Configure service account impersonation

Configure the default Cloud Logging service account, LOGGING_SA, so that it can impersonate the user-managed service account, CUSTOM_SA. The default Cloud Logging service account exists in the Google Cloud project that you want to create log sinks that use the user-managed service account.

To configure service account impersonation, grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to the Cloud Logging service account on the user-managed service account:
    
    
    gcloud iam service-accounts add-iam-policy-binding CUSTOM_SA \
    --project=CUSTOM_SA_PROJECT_ID \
    --member='serviceAccount:LOGGING_SA' \
    --role='roles/iam.serviceAccountTokenCreator'
    

Service account impersonation involves two principals: the service account that lacks permissions to access a resource, and the privilege-bearing service account that has the permissions to access a resource. In this case, the user-managed service account is the privilege-bearing account because it has the ability to write log entries to the sink destination, which is a log bucket in the project named LOG_BUCKET_PROJECT_ID. The Logging service account has the privileges to route log entries.

For more information about the Service Account Token Creator role, see [Service Account Token Creator Role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role).

For more information about service account impersonation, see [About service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

### Let principal run operations as the user-managed service account

Give the principal who will create the sink the permissions they need to run operations as the user-managed service account.

To give the required permissions, grant the principal the Service Account User role (`roles/iam.serviceAccountUser`) on the Google Cloud project that stores the user-managed service account, CUSTOM_SA_PROJECT_ID.

Before you run the following command, make the following replacements:

  * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).



Execute the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    
    gcloud iam service-accounts add-iam-policy-binding CUSTOM_SA \
    --project=CUSTOM_SA_PROJECT_ID \
    --member='PRINCIPAL' \
    --role='roles/iam.serviceAccountUser'
    

If you use custom roles, then the principal needs the `iam.serviceAccounts.actAs` permission.

For more information about the Service Account User role, see [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role).

## Create a log sink that uses a user-managed service account

To create a sink with a user-managed service account, run the `gcloud logging sinks create` command and include the `--custom-writer-identity` option.

Before you run the following command, make the following replacements:

  * SINK_NAME: The name of the log sink.



Execute the [`gcloud logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command:
    
    
    gcloud logging sinks create SINK_NAME \
    logging.googleapis.com/projects/LOG_BUCKET_PROJECT_ID/locations/LOCATION/buckets/BUCKET_NAME \
    --custom-writer-identity=serviceAccount:CUSTOM_SA \
    --project=SINK_PROJECT_ID
    

## Verify that your sink is routing log entries

In this section, you use the gcloud CLI to write and read a log entry to verify that your sink is routing log entries correctly.

To verify that your sink is routing log entries correctly, do the following:

  1. Run the `gcloud logging write` command:

Before you run the following command, make the following replacements:

     * LOG_NAME: The name of the log. For example, you might set this field to `mylog`.

Execute the [`gcloud logging write`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/write) command:
    
    gcloud logging write LOG_NAME "Test log entry" --project=SINK_PROJECT_ID
    

The previous command returns the following message: `Created log entry.`

  2. To read the log entry you just wrote, run the following command:
         
         gcloud logging read 'textPayload="Test log entry"' \
         --bucket=BUCKET_NAME --location=LOCATION \
         --view=_AllLogs --project=SINK_PROJECT_ID
         




## What's next

  * To learn about routing log entries to supported destinations, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

  * For an overview about how Logging routes and stores your log entries, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

  * If you encounter issues as you use sinks to route log entries, see [Troubleshoot routing logs](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

  * To learn how to view your log entries in their destinations, as well as how the log entries are formatted and organized, see [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
