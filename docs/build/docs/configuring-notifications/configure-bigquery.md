---
url: https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery/
title: Configure BigQuery notifications \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:13.258043+00:00
---

# Configure BigQuery notifications  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Configure BigQuery notifications Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build can notify you of build updates by sending you notifications to specific channels, such as Slack or your SMTP server. This page explains how to configure notifications using the [BigQuery notifier](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/bigquery).

The BigQuery notifier lets you specify filters for builds that you want to store in your database. For example, you can group builds by trigger ID, tags, or [substitution values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values). The BigQuery notifier also writes data to BigQuery in a standardized format that includes computed fields not immediately accessible on the Build object, such as image size or execution duration. If you want to learn how to export log entries to BigQuery or another destination, see [Exporting logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Before you begin

  * Enable the Cloud Build, Cloud Run, Pub/Sub, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,pubsub.googleapis.com,bigquery.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/configure-bigquery)



  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk).



## Configure BigQuery notifications

The following section explains how you can manually configure HTTP notifications using the [BigQuery notifier](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/bigquery). If you would like to automate the configuration instead, see [Automating configuration for notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/automate).

To configure BigQuery notifications:

  1. Give your Cloud Run service account permission to create and write BigQuery tables, permission to fetch Artifact Registry data related to your build, and read and write access to Cloud Storage buckets:

     1. Go to the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the **Compute Engine default service account** associated with with your project:

Your **Compute Engine default service account** will look similar to the following:
            
            PROJECT_NUMBER-compute@developer.gserviceaccount.com
            

     3. Click the pencil icon in the row containing your **Compute Engine default service account**. You will see the **Edit access** tab.

     4. Click **Add another role**.

     5. Add the following roles:

        * **Artifact Registry Reader**
        * **BigQuery Data Editor**
        * **Storage Object Viewer**

The **Artifact Registry Reader** role lets you fetch data for your images. The **BigQuery Data Editor** gives you read and write access to your data. The **Storage Object Viewer** gives you read access to Cloud Storage objects.

**Note:** If you want to grant permissions at the bucket level instead of the project level, add the **Storage Legacy Object Owner** role to your bucket when you create one. To learn more, see [Project-level roles vs. bucket-level roles](https://docs.cloud.google.com/storage/docs/access-control/iam#project-level_roles_vs_bucket-level_roles).
     6. Click **Save**.

  2. Write a notifier configuration file to configure your BigQuery notifier and filter on build events:

In the following example notifier config file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the variable, `build`, to filter build events with a specified trigger ID:
         
         apiVersion: cloud-build-notifiers/v1
         kind: BigQueryNotifier
         metadata:
           name: example-bigquery-notifier
         spec:
           notification:
             filter: build.build_trigger_id == "123e4567-e89b-12d3-a456-426614174000"
             params:
               buildStatus: $(build.status)
             delivery:
               table: projects/PROJECT_ID/datasets/DATASET_NAME/tables/TABLE_NAME
             template:
               type: golang
               uri: gs://BUCKET_NAME/bq.json
         

Where:

     * `buildStatus` is a user-defined parameter. This parameter takes on the value of ${build.status}, the status of the build.
     * `BUCKET_NAME` is the name of your bucket.
     * `PROJECT_ID` is the ID of your Google Cloud project.
     * `DATASET_NAME` is the name you want to give your dataset.
     * `TABLE_NAME` is the name you want to give your table.
     * The `uri` field references the `bq.json` file. This file refers to a JSON template hosted on Cloud Storage and represents the information to insert into your BigQuery table.

**Experimental — Customizing notifications using templates**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view an example of a template file, see the [`bq.json` file](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/bigquery/bq.json) in the cloud-build-notifiers-repository.

The TABLE_NAME in your notifier config file can refer to:

     * a nonexistent table
     * an empty table without a schema
     * an existing table with a schema that matches the schema specifications in the BigQuery notifier

**Note:** References to an existing table with a schema specification not matching the BigQuery notifier will result in an error.

We recommend you specify the build trigger ID as your filter since specifying the build trigger ID lets you correlate build data for your triggers. You can also specify multiple trigger IDs in a list: `build.build_trigger_id in ["example-id-123", "example-id-456"]`.

To obtain your trigger ID, run the following command, where TRIGGER_NAME is the name of your trigger:

gcloud builds triggers describe TRIGGER_NAME

The command will list fields associated with your trigger, including your trigger ID.

**Note:** Data is only stored for build events with a terminal status such as `SUCCESS` or `FAILURE`.

To view the example, see the [notifier config file](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/bigquery/bigquery.yaml.example) for the BigQuery notifier.

For additional fields you can filter by, see the [Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource. For additional filtering examples, see the [Using CEL to filter build events](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery#using_cel_to_filter_build_events).

  3. Upload your notifier configuration file to a Cloud Storage bucket:

     1. If you do not have a Cloud Storage bucket, run the following command to create a bucket, where BUCKET_NAME is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
            
            gcloud storage buckets create gs://BUCKET_NAME/
            

     2. Upload the notifier config file to your bucket:
            
            gcloud storage cp CONFIG_FILE_NAME gs://BUCKET_NAME/CONFIG_FILE_NAME
            

Where:

        * `BUCKET_NAME` is the name of your bucket.
        * `CONFIG_FILE_NAME` is the name of your notifier config file.
  4. Deploy your notifier to Cloud Run:
         
         gcloud run deploy SERVICE_NAME \
            --image=us-east1-docker.pkg.dev/gcb-release/cloud-build-notifiers/bigquery:latest \
            --no-allow-unauthenticated \
            --update-env-vars=CONFIG_PATH=CONFIG_PATH,PROJECT_ID=PROJECT_ID
         

Where:

     * `SERVICE_NAME` is the name of the Cloud Run service to which you're deploying the image.
     * `CONFIG_PATH` is the path to the notifier config file for your BigQuery notifier, `gs://BUCKET_NAME/CONFIG_FILE_NAME`.
     * `PROJECT_ID` is the ID of your Google Cloud project.

The `gcloud run deploy` command pulls the latest version of the hosted image from the [Cloud Build-owned Artifact Registry](https://console.cloud.google.com/artifacts/docker/gcb-release/us-east1/cloud-build-notifiers?project=gcb-release). Cloud Build supports notifier images for nine months. After nine months, Cloud Build deletes the image version. If you would like to use a prior image version, you will need to specify the full semantic version of the image tag in the `image` attribute of your `gcloud run deploy` command. Previous image versions and tags can be found in [Artifact Registry](https://console.cloud.google.com/artifacts/docker/gcb-release/us-east1/cloud-build-notifiers?project=gcb-release).

**Note:** While running this command, you may be prompted to specify additional arguments such as `--region` or `--platform`. To learn more about parameters you can pass to the `gcloud run deploy` command, see [Deploying to Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy#deploying_to). If you are unable to deploy your notifier using this command, see the Cloud Run troubleshooting guide for solutions on how to resolve [Deployment errors](https://docs.cloud.google.com/run/docs/troubleshooting#deployment).

  5. Create a service account to represent your Pub/Sub subscription identity:
         
         gcloud iam service-accounts create SUB_IDENTITY_SERVICE_ACCOUNT \
           --display-name "SUB_IDENTITY_SERVICE_ACCOUNT_DISPLAY_NAME"
         

Where:

     * `SUB_IDENTITY_SERVICE_ACCOUNT` is a name for the service account.

     * `SUB_IDENTITY_SERVICE_ACCOUNT_DISPLAY_NAME` is a display name for the service account.

**Note:** This service account is different from the Pub/Sub service account, which Google Cloud creates when you first [create a Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription). The Pub/Sub service account has an address of `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`.
  6. Grant your Pub/Sub subscription identity service account the permissions necessary to create authentication tokens in your Google Cloud project.
         
         gcloud iam service-accounts add-iam-policy-binding \
             SUB_IDENTITY_SERVICE_ACCOUNT@PROJECT_ID.iiam.gserviceaccount.com \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator
         

Where:

     * `PROJECT_ID` is the ID of your Google Cloud project.

     * `PROJECT_NUMBER` is your Google Cloud project number.

  7. Grant SUB_IDENTITY_SERVICE_ACCOUNT service account the Cloud Run `Invoker` role:
         
         gcloud run services add-iam-policy-binding SERVICE_NAME \
            --member=serviceAccount:SUB_IDENTITY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com \
            --role=roles/run.invoker
         

Where:

     * `SERVICE_NAME` is the name of the Cloud Run service to which you're deploying the image.

     * `PROJECT_ID` is the ID of your Google Cloud project.

  8. Create the `cloud-builds` topic to receive build update messages for your notifier:
         
         gcloud pubsub topics create cloud-builds
         

You can also define a custom topic name in your build config file so that messages are sent to the custom topic instead. In this case, you would create a topic with the same custom topic name:
         
         gcloud pubsub topics create topic-name
         

For more information, see [Pub/Sub topics for build notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers#pubsub-topic-config).

  9. Create a Pub/Sub push subscriber for your notifier:



    
    
         gcloud pubsub subscriptions create subscriber-id \
           --topic=cloud-builds \
           --push-endpoint=SERVICE_URL \
           --push-auth-service-account=SUB_IDENTITY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
    

Where: \+ `SUBSCRIBER_ID` is the name you want to give your subscription. \+ `SERVICE_URL` is the Cloud Run-generated URL for your new service. \+ `PROJECT_ID` is the ID of your Google Cloud project.
    
    
    Note: By default, [subscriptions expire after 31 days of inactivity](/pubsub/docs/subscription-overview#lifecycle).
    You can adjust or disable the expiration period by including the
    [`--expiration-period` flag](/sdk/gcloud/reference/pubsub/subscriptions/create#--expiration-period)
    when creating the subscription.
    

Notifications for your Cloud Build project are now set up.

The next time you invoke a build, your table will be updated with the latest data that matches the filter you've configured for your BigQuery notifier.

## Viewing build data

To view your build data in BigQuery:

  1. Open the BigQuery console page:

[Open the BigQuery page](https://console.cloud.google.com/bigquery)

  2. Under **Resources** , click the project ID you use to configure your BigQuery notifier.

  3. Click your dataset name.

  4. Click your table name.




You can now see information related to your table including its schema and a preview of your build data as listed in the table.

## Accessing build data

You can query data in your table using the [bq command line tool](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) or the [BigQuery console](https://console.cloud.google.com/bigquery).

###  CLI 

To query data in your table using the `bq` command-line tool, run the following command in your terminal where SQL_QUERY is your query:
    
    
    bq query SQL_QUERY
    

If you plan to use the [query examples](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery#example_queries) on this page, make sure you specify the `--nouse_legacy_sql` flag in your command since. The `bq` command-line tool uses Legacy SQL whereas the example queries don't. Run the following command in your terminal to query data without Legacy SQL:
    
    
    bq query SQL_QUERY --nouse_legacy_sql
    

###  Console 

To query data in your table using the BigQuery console:

  1. Open the BigQuery console page:

[Open the BigQuery page](https://console.cloud.google.com/bigquery)

  2. Under **Resources** , click the table name you would like to query.

  3. Write your SQL query in the **Query editor**.




## Using queries to access build data

The following example queries show how you can access build data for your build event, following configuration of the BigQuery notifier:

**Overall build history**
    
    
    SELECT * FROM `projectID.datasetName.tableName`
    

**Build counts grouped by status**
    
    
    SELECT STATUS, COUNT(*)
    FROM `projectID.datasetName.tableName`
    GROUP BY STATUS
    

**Daily deployment frequency for the current week**
    
    
    SELECT DAY, COUNT(STATUS) AS Deployments
    FROM (SELECT DATETIME_TRUNC(CreateTime, WEEK) AS WEEK,
          DATETIME_TRUNC(CreateTime, DAY) AS DAY,
          STATUS
          FROM `projectID.datasetName.tableName`
          WHERE STATUS="SUCCESS")
    WHERE WEEK = DATETIME_TRUNC(CURRENT_DATETIME(), WEEK)
    GROUP BY DAY
    

To see more example queries, see the [Cloud Build BigQuery Notifier README](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/bigquery/README.md) in the `cloud-build-notifiers` repository on GitHub. To learn more about how to query data using BigQuery, see [Querying and viewing data](https://docs.cloud.google.com/bigquery/docs/interacting-with-bigquery#query_view).

## Using CEL to filter build events

Cloud Build uses CEL with the variable, `build`, on fields listed in the [Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource to access fields associated with your build event such as your trigger ID, image list, or substitution values. You can use the `filter` string to filter build events in your build config file using any field listed in the [Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource. To find the exact syntax associated with your field, see the [`cloudbuild.proto`](https://github.com/googleapis/googleapis/blob/master/google/devtools/cloudbuild/v1/cloudbuild.proto) file.

### Filtering by trigger ID

To filter by trigger ID, specify the value of your trigger ID in the `filter` field using `build.build_trigger_id`, where `trigger-id` is your trigger ID as a string:
    
    
    filter: build.build_trigger_id == trigger-id
    

**Note:** Your trigger ID is **not** the name of your trigger. To obtain your trigger ID, run the following command: `gcloud beta builds triggers describe trigger-name`, where trigger-name is the name of your trigger. The command will list fields associated with your trigger, including your trigger ID.

### Filtering by status

To filter by status, specify the build status you want to filter on in the `filter` field using `build.status`.

The following example shows how to filter build events with a `SUCCESS` status using the `filter` field:
    
    
    filter: build.status == Build.Status.SUCCESS
    

You can also filter builds with varying statuses. The following example shows how to filter build events that have a `SUCCESS`, `FAILURE`, or `TIMEOUT` status using the `filter` field:
    
    
    filter: build.status in [Build.Status.SUCCESS, Build.Status.FAILURE, Build.Status.TIMEOUT]
    

To see additional status values you can filter by, see [Status](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#status) under the Build resource reference.

### Filtering by tag

To filter by tag, specify the value of your tag in the `filter` field using `build.tags`, where `tag-name` is the name of your tag:
    
    
    filter: tag-name in build.tags
    

You can filter based on the number of tags specified in your build event using `size`. In the following example, the `filter` field filters build events that have exactly two tags specified with one tag specified as `v1`:
    
    
    filter: size(build.tags) == 2 && "v1" in build.tags
    

### Filtering by images

To filter by images, specify the value of your image in the `filter` field using `build.images`, where `image-name` is the full name of your image as listed in Artifact Registry such as `us-east1-docker.pkg.dev/my-project/docker-repo/image-one`:
    
    
    filter: image-name in build.images
    

In the following example, the `filter` filters on build events that have either `us-east1-docker.pkg.dev/my-project/docker-repo/image-one` or `us-east1-docker.pkg.dev/my-project/docker-repo/image-two` specified as image names:
    
    
    filter: "us-east1-docker.pkg.dev/my-project/docker-repo/image-one" in build.images || "us-east1-docker.pkg.dev/my-project/docker-repo/image-one" in build.images
    

### Filtering by time

You can filter build events based on a build's create time, start time, or finish time by specifying one of the following options in your `filter` field: `build.create_time`, `build.start_time`, or `build.finish_time`.

In the following example, the `filter` field uses `timestamp` to filter build events with a request time to create the build at July 20, 2020 at 6:00 AM:
    
    
    filter: build.create_time == timestamp("2020-07-20:T06:00:00Z")
    

You can also filter on build events by time comparisons. In the following example, the `filter` field uses `timestamp` to filter build events with a start time between July 20, 2020 at 6:00 AM and July 30, 2020 at 6:00 AM.
    
    
    filter: timestamp("2020-07-20:T06:00:00Z") >= build.start_time && build.start_time <= timestamp("2020-07-30:T06:00:00Z")
    

To learn more about how timezones are expressed in CEL, see the language definition for [timezones](https://github.com/google/cel-spec/blob/master/doc/langdef.md#timezones).

To filter by duration of a build, you can use `duration` to compare timestamps. In the following example, the `filter` field uses `duration` to filter build events with a builds that run for at least five minutes:
    
    
    filter: build.finish_time - build.start_time >= duration("5m")
    

**Note:** Timestamps are in RFC 3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.

### Filtering by substitution

You can filter by substitution by specifying the substitution variable in the `filter` field using `build.substitutions`. In the following example, the `filter` field lists builds that contain the substitution variable substitution-variable and checks if the substitution-variable matches the specified substitution-value:
    
    
    filter: build.substitutions[substitution-variable] == substitution-value
    

Where:

  * `substitution-variable` is the name of your substitution variable.
  * `substitution-value` is the name of your substitution value.



You can also filter by default substitution variable values. In the following example, the `filter` field lists builds that have the branch name `master` and builds that have the repository name `github.com/user/my-example-repo`. The default substitution variables `BRANCH_NAME` and `REPO_NAME` are passed in as keys to the `build.substitutions`:
    
    
    filter: build.substitutions["BRANCH_NAME"] == "master" && build.substitutions["REPO_NAME"] == "github.com/user/my-example-repo"
    

If you want to filter on strings using regular expressions, you can use the built-in `matches` function. In the example below, the `filter` field filters for builds with a status of FAILURE or TIMEOUT and that also have a build substitution variable `TAG_NAME` with a value that matches the regular expression `v{DIGIT}.{DIGIT}.{3 DIGITS})`.
    
    
    filter: build.status in [Build.Status.FAILURE, Build.Status.TIMEOUT] && build.substitutions["TAG_NAME"].matches("^v\\d{1}\\.\\d{1}\\.\\d{3}$")
    

To see a list of default substitution values, see [Using default substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions).

## What's next

  * Learn about [Cloud Build notifiers](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers).
  * Learn how to [subscribe to build notifications](https://docs.cloud.google.com/build/docs/subscribe-build-notifications).
  * Learn how to write a [Cloud Build build configuration file](https://docs.cloud.google.com/build/docs/build-config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
