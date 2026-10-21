---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-batch-pipelines/
title: Troubleshoot Cloud Data Fusion batch pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:39.368944+00:00
---

# Troubleshoot Cloud Data Fusion batch pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-batch-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot Cloud Data Fusion batch pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Cloud Data Fusion batch pipelines.

## Pipeline error: Text file busy

The following error occurs when you run a batch pipeline, causing it to fail:
    
    
    error=26, Text file busy
    

To resolve this issue, set up a trigger that automatically retries a pipeline when it fails.

  1. [Stop the pipeline](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#stop_a_batch_pipeline).
  2. Create a trigger. In this case, when you select an event to execute, choose **Fails**. For more information, see [Create an inbound trigger on a downstream pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/using-triggers#create_inbound_trigger).
  3. [Start the pipeline](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#start_a_batch_pipeline).



## Concurrent pipeline is stuck

In Cloud Data Fusion, running many concurrent batch pipelines can put a strain on the instance, causing jobs to get stuck in `Starting`, `Provisioning`, or `Running` states. As a result, pipelines can't be stopped through the web interface or API calls. When you run many pipelines concurrently, the web interface can become slow or unresponsive. This issue occurs due to multiple UI requests made to the HTTP handler in the backend.

To resolve this issue, control the number of new requests using [Cloud Data Fusion flow control](https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control).

## SSH connection times out while a running pipeline

The following error occurs when you run a batch pipeline:
    
    
    java.io.IOException: com.jcraft.jsch.JSchException:
    java.net.ConnectException: Connection timed out (Connection timed out)
    

To resolve this issue, do the following:

  * Check for a missing firewall rule (typically port 22). To create a new firewall rule, see [Managed Service for Apache Spark cluster network configuration](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network).
  * Check that the Compute Engine enforcer allows the connection between your Cloud Data Fusion instance and the Managed Service for Apache Spark cluster.



## Response code: 401. Error: unknown error

The following error occurs when you run a batch pipeline:
    
    
    java.io.IOException: Failed to send message for program run program_run:
    Response code: 401. Error: unknown error
    

To resolve this issue, you must [grant the Cloud Data Fusion Runner role (`roles/datafusion.runner`)](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission) to the service account used by Managed Service for Apache Spark.

## Pipeline with BigQuery plugin fails with `Access Denied` error

There is a known issue where a pipeline fails with an `Access Denied` error when running BigQuery jobs. This impacts pipelines that use the following plugins:

  * BigQuery sources
  * BigQuery sinks
  * BigQuery Multi Table sinks
  * Transformation Pushdown



Example error in the logs (might differ depending on the plugin you are using):
    
    
    POST https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/jobs
    {
    "code" : 403,
    "errors" : [ {
    "domain" : "global",
    "message" : "Access Denied: Project xxxx: User does not have bigquery.jobs.create permission in project PROJECT_ID",
    "reason" : "accessDenied"
    } ],
    "message" : "Access Denied: Project PROJECT_ID: User does not have bigquery.jobs.create permission in project PROJECT_ID.",
    "status" : "PERMISSION_DENIED"
    }
    

In this example, PROJECT_ID is the project ID that you specified in the plugin. The service account for the project specified in the plugin doesn't have permission to do at least one of the following:

  * Run a BigQuery job
  * Read a BigQuery dataset
  * Create a temporary bucket
  * Create a BigQuery dataset
  * Create the BigQuery table



To resolve this issue, grant the missing roles to the project (PROJECT_ID) that you specified in the plugin:

  * To run a BigQuery job, grant the BigQuery Job User role ([`roles/bigquery.jobUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery)).

  * To read a BigQuery dataset, grant the BigQuery Data Viewer role ([`roles/bigquery.dataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery)).

  * To create a temporary bucket, grant the Storage Admin role ([`roles/storage.admin`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles)).

  * To create a BigQuery dataset or table, grant the BigQuery Data Editor role ([`roles/bigquery.dataEditor`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery)).




For more information, see the plugin's troubleshooting documentation ([Google BigQuery Multi Table Sink Troubleshooting](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464912385)).

## Pipeline doesn't stop at the error threshold

A pipeline might not stop after multiple errors, even if you set the error threshold to `1`.

The error threshold is intended for any exceptions raised from the directive in the event of a failure that is not otherwise handled. If the directive already uses the emitError API, then the error threshold is not activated.

To design a pipeline that fails when a certain threshold is met, use the [`FAIL` directive](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042192/Fail+on+condition+directive).

Whenever the condition passed to the `FAIL` directive is satisfied, it counts against the error threshold and the pipeline fails after the threshold is reached.

## Delete an ephemeral Managed Service for Apache Spark cluster

When Cloud Data Fusion creates an ephemeral Managed Service for Apache Spark cluster during pipeline run provisioning, the cluster gets deleted after the pipeline run is finished. In rare cases, the cluster deletion fails.

**Strongly recommended** : Upgrade to the most recent Cloud Data Fusion version to ensure proper cluster maintenance.

### Set Max Idle Time

To resolve this issue, configure the [`Max Idle Time`](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc#Max-Idle-Time) option. This lets Managed Service for Apache Spark delete clusters automatically, even if an explicit call on the pipeline finish fails.

`Max Idle Time` is available in Cloud Data Fusion versions 6.4 and later.

**Note:** In Cloud Data Fusion 6.6 and later, `Max Idle Time` is set to 30 minutes by default and no additional configuration is needed.

**Recommended** : For versions prior to 6.6, set `Max Idle Time` manually to 30 minutes or greater.

### Delete clusters manually

If you can't upgrade your version or configure the `Max Idle Time` option, instead delete stale clusters manually:

  1. Get each project ID where the clusters were created:

     1. In the pipeline's runtime arguments, check if the Managed Service for Apache Spark project ID is customized for the run.

![Check if the Dataproc project ID is customized for the run](https://docs.cloud.google.com/static/data-fusion/docs/images/support/check-dataproc-project-id.png)

     2. If a Managed Service for Apache Spark project ID is not specified explicitly, determine which provisioner is used, and then check for a project ID:

        1. In the pipeline runtime arguments, check the `system.profile.name` value.

![Get the provisioner name in the runtime arguments](https://docs.cloud.google.com/static/data-fusion/docs/images/support/get-provisioner-name.png)

        2. Open the provisioner settings and check if the Managed Service for Apache Spark project ID is set. If the setting is not present or the field is empty, the project that the Cloud Data Fusion instance is running in is used.

**Important:** Multiple pipeline runs might use different projects. Be sure to get all of the project IDs.
  2. For each project:

     1. Open the project in the Google Cloud console and go to the Managed Service for Apache Spark **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/dataproc/clusters)

     2. Sort the clusters by the date that they were created, from oldest to newest.

     3. If the info panel is hidden, click **Show info panel** and go to the **Labels** tab.

     4. For every cluster that is not in use—for example, more than a day has elapsed—check if it has a Cloud Data Fusion version label. That is an indication that it was created by Cloud Data Fusion.

     5. Select the checkbox by the cluster name and click **Delete**.




## Pipelines fail when run on Managed Service for Apache Spark clusters with primary or secondary workers

In Cloud Data Fusion versions 6.8 and 6.9, an issue occurs causing pipelines to fail if they run on Managed Service for Apache Spark clusters:
    
    
    ERROR [provisioning-task-2:i.c.c.i.p.t.ProvisioningTask@161] - PROVISION task failed in REQUESTING_CREATE state for program run program_run:default.APP_NAME.UUID.workflow.DataPipelineWorkflow.RUN_ID due to
    Caused by: io.grpc.StatusRuntimeException: CANCELLED: Failed to read message.
    Caused by: com.google.protobuf.GeneratedMessageV3$Builder.parseUnknownField(Lcom/google/protobuf/CodedInputStream;Lcom/google/protobuf/ExtensionRegistryLite;I)Z.
    

To resolve this issue, [upgrade](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision) to the patch revision `6.8.3.1`, `6.9.2.1`, or later.

## Cloud Storage plugin intermittently fails with regular expression on Managed Service for Apache Spark 2.0

Pipelines might intermittently fail in Cloud Data Fusion version 6.10.1 when the Cloud Storage plugin uses a `*` regular expression pattern in the path and the execution environment is Managed Service for Apache Spark 2.0.

To resolve this issue, perform one of the following:

  * Update the Managed Service for Apache Spark image to version 2.1 or later.
  * Revert to an earlier version of the Cloud Storage plugin.
  * Increase the memory allocated for the Managed Service for Apache Spark executor.



## Pipelines fail with NoSuchMethodError on Managed Service for Apache Spark 2.2

In Cloud Data Fusion version 6.10.1.1 and later, pipelines might fail with the following error when running on Managed Service for Apache Spark 2.2:
    
    
    java.lang.NoSuchMethodError: 'org.apache.spark.sql.catalyst.encoders.ExpressionEncoder
    org.apache.spark.sql.catalyst.encoders.RowEncoder.apply(org.apache.spark.sql.types.StructType)'
    

To resolve this issue, perform one of the following:

  * Reconfigure the Managed Service for Apache Spark image to version 2.1. For more information, see [Change the Managed Service for Apache Spark image version in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image).
  * Upgrade your Cloud Data Fusion instance to version 6.11.



## Multiple database tables plugin fails if Reference Name contains spaces

In Cloud Data Fusion version 6.10.1 and later, pipelines using the Multiple database tables batch source might fail when the **Reference Name** field contains space characters.

To resolve this issue, update the Multiple database tables plugin to version 1.4.1 or later from the Hub. The updated version doesn't allow spaces in the **Reference Name** field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
