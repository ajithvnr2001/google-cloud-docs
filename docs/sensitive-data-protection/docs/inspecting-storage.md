---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage/
title: Inspect Google Cloud storage and databases for sensitive data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:53.011444+00:00
---

# Inspect Google Cloud storage and databases for sensitive data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Inspect Google Cloud storage and databases for sensitive data Stay organized with collections  Save and categorize content based on your preferences. 

Properly managing sensitive data that is stored in a storage repository starts with [storage classification](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction#storage_classification): identifying where your sensitive data is in the repository, what type of sensitive data it is, and how it's being used. This knowledge can help you properly set access control and sharing permissions, and it can be part of an ongoing monitoring plan.

Sensitive Data Protection can detect and classify sensitive data stored in a [Cloud Storage](https://docs.cloud.google.com/storage) location, [Datastore](https://docs.cloud.google.com/datastore) kind, or [BigQuery](https://docs.cloud.google.com/bigquery) table. When scanning files in Cloud Storage locations, Sensitive Data Protection supports scanning of binary, text, image, Microsoft Word, Microsoft Excel, Microsoft Powerpoint, PDF, and Apache Avro files. Files of types that are unrecognized are scanned as binary files. For more information about supported files types, see [Supported file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).

To inspect storage and databases for sensitive data, you specify the location of the data and the type of sensitive data that Sensitive Data Protection should look for. Sensitive Data Protection initiates a job that inspects the data at the given location, and then it makes available details about [infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) found in the content, [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) values, and more.

You can set up inspection of storage and databases using Sensitive Data Protection in the Google Cloud console, via the RESTful DLP API, or programmatically using a [Sensitive Data Protection client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries) in one of several languages.

This topic includes:

  * Best practices for setting up scans of Google Cloud storage repositories and databases.
  * Instructions for setting up an inspection scan using Sensitive Data Protection in the Google Cloud console, and (optionally) for scheduling periodic repeating inspection scans.
  * JSON and code samples for each Google Cloud storage repository type: (Cloud Storage, Firestore in Datastore mode (Datastore), and BigQuery).
  * A detailed overview of the configuration options for scan jobs.
  * Instructions for how to retrieve scan results and how to manage the scan jobs that are created from each successful request.



## Best practices

### Identify and prioritize scanning

It's important to first evaluate your assets and specify which have the highest priority for scanning. When just getting started you may have a large backlog of data that needs classification, and it will be impossible to scan it all immediately. Choose data initially that poses the highest potential risk—for example, data that is frequently accessed, widely accessible, or unknown.

### Ensure that Sensitive Data Protection can access your data

Sensitive Data Protection must be able to access data to be scanned. Be sure that the Sensitive Data Protection [service account](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-permissions#service_account) is permitted to read your resources.

### Limit the scope of your first scans

For best results, limit the scope of your first jobs instead of scanning all of your data. Start with one table, one bucket, or a few files and use [sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#sampling). By limiting the scope of your first scans, you can better determine what detectors to enable and what [exclusion rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#exclusion-rules) might be needed to reduce false positives so that your findings will be more meaningful. Avoid turning on all infoTypes if you don't need them all, as false positives or unusable findings may make it harder to assess your risk. While useful in certain scenarios, infoTypes such as `DATE`, `TIME`, `DOMAIN_NAME`, and `URL` match on a broad range of findings and may not be useful to turn on for large data scans.

When sampling a structured file—such as a CSV, TSV, or Avro file—make sure that the sample size is big enough to cover the file's full header and a row of data. For more information, see [Scanning structured files in structured parsing mode](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#structured-parsing-mode).

### Schedule your scans

Use Sensitive Data Protection [job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers) to automatically run scans and generate findings daily, weekly, or quarterly. These scans can also be configured to only inspect data that has changed since the last scan, which can save time and reduce costs. Running scans on a regular basis can help you identify trends or anomalies in your scan results.

## Job latency

There are no service level objectives (SLO) guaranteed for jobs and job triggers. Latency is affected by several factors, including the amount of data to scan, the storage repository being scanned, the type and number of infoTypes you are scanning for, the region where the job is processed, and the computing resources available in that region. Therefore, the latency of inspection jobs can't be determined in advance.

To help reduce job latency, you can try the following:

  * If [sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#sampling) is available for your job or job trigger, enable it.
  * Avoid enabling infoTypes that you don't need. Although the following are useful in certain scenarios, these infoTypes can make requests run much more slowly than requests that don't include them:

    * `PERSON_NAME`
    * `FEMALE_NAME`
    * `MALE_NAME`
    * `FIRST_NAME`
    * `LAST_NAME`
    * `DATE_OF_BIRTH`
    * `LOCATION`
    * `STREET_ADDRESS`
    * `ORGANIZATION_NAME`
  * Always specify infoTypes explicitly. Do not use an empty infoTypes list.

  * If possible, use a different processing region.




If you're still having latency issues with jobs after trying these techniques, consider using [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect) or [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify) requests instead of jobs. These methods are covered under the Service Level Agreement. For more information, see [Sensitive Data Protection Service Level Agreement](https://cloud.google.com/sensitive-data-protection/sla).

## Before you begin

The instructions provided in this topic assume the following:

  * You have enabled billing.

[Learn how to enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  * You have enabled Sensitive Data Protection.

[Enable Sensitive Data Protection](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)




Storage classification requires the following OAuth scope: `https://www.googleapis.com/auth/cloud-platform`. For more information, see [Authenticating to the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/auth).

## Inspect a Cloud Storage location

You can set up a Sensitive Data Protection inspection of a Cloud Storage location using the Google Cloud console, the DLP API via [REST](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) or [RPC](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc) requests, or programmatically in several languages using a [client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). For information about the parameters included with the following JSON and code samples, see "[Configure storage inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#configuring-storage-inspection)," later in this topic.

Sensitive Data Protection relies on file extensions and media (MIME) types to identify the types of the files to be scanned and the [scanning modes](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#scanning_modes) to apply. For example, Sensitive Data Protection scans a `.txt` file in plain text mode, even if the file is structured as a CSV file, which is normally scanned in structured parsing mode. 

**Note:** Prematurely canceling an operation midway through a job still incurs costs for the portion of the job that was completed. For more information about billing, see [Sensitive Data Protection pricing](https://cloud.google.com/sensitive-data-protection/pricing).

**Note:** Sensitive Data Protection will only scan the version of the file that was present when the job was started. If [Cloud Storage versioning](https://docs.cloud.google.com/storage/docs/object-versioning) is disabled and a file is modified after a job is started but before the job is completed, that file will be skipped. Otherwise, Sensitive Data Protection will scan an older version of the file. To enable versioning for your Cloud Storage objects, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/using-object-versioning). 

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

To set up a scan job of a Cloud Storage bucket using Sensitive Data Protection:

### Console

This section describes how to inspect a Cloud Storage bucket or folder. If you also want Sensitive Data Protection to create a de-identified copy of your data, see [De-identify sensitive data stored in Cloud Storage using the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage-console).

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

**Note:** You can also initiate a Sensitive Data Protection scan directly from the [Cloud Storage browser](https://console.cloud.google.com/storage/browser). In the right-most column for the bucket you want to scan, click the **more actions** menu (displayed as three dots arranged vertically) more_vert, and then click **Scan with Sensitive Data Protection**. The Sensitive Data Protection job creation page opens on a separate tab.
  2. Enter the Sensitive Data Protection job information and click **Continue** to complete each step:

     * For **Choose input data** , name the job by entering a value in the **Name** field. In **Location** , choose Cloud Storage from the **Storage type** menu, and then enter the location of the data to scan. The **Sampling** section is pre-configured to run a sample scan against your data. You can adjust the **Percentage of objects scanned within bucket** field to save resources if you have a large amount of data. For more details, see [Choose input data](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#choose-input-data).

     * (Optional) For **Configure detection** , you can configure what types of data to look for, called "[infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)." You can select from the [list of pre-defined infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), or you can select a template if one exists. For more details, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).

     * For **Add actions** , select one or more actions for Sensitive Data Protection to take after the job completes. For more information, see [Enable inspection or risk analysis actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions). 

After you select actions, click **Continue**. 

     * (Optional) For **Schedule** , to run the scan one time only, leave the menu set to **None**. To schedule scans to run periodically, click **Create a trigger to run the job on a periodic schedule**. For more details, see [Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#schedule-job).

  3. Click **Create**.

  4. After the Sensitive Data Protection job completes, you are redirected to the job details page and notified via email. You can view the results of the inspection on the job details page.

  5. (Optional) If you chose to publish Sensitive Data Protection findings to BigQuery, on the **Job details** page, click **View Findings in BigQuery** to open the table in the BigQuery web UI. You can then query the table and analyze your findings. For more information on querying your results in BigQuery, see [Querying Sensitive Data Protection findings in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings).




### Protocol

Following is sample JSON that can be sent in a POST request to the specified Sensitive Data Protection REST endpoint. This example JSON demonstrates how to use the DLP API to inspect Cloud Storage buckets. For information about the parameters included with the request, see "Configure storage inspection," later in this topic.

**Note:** To specify a Cloud Storage bucket to scan, enter the URL using the following pattern: `gs://[GCS_BUCKET_NAME]/*`. To scan only the specified directory and no deeper, use one asterisk (`*`). To scan the directory recursively, use two asterisks (`**`).

You can quickly try this out in the APIs Explorer on the reference page for `content.inspect`:

[Go to APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect?apix=true)

Keep in mind that a successful request, even in APIs Explorer, will create a new scan job. For information about how to control scan jobs, see "[Retrieve inspection results](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#retrieving-inspection-results)," later in this topic. For general information about using JSON to send requests to the DLP API, see the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json).

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT-ID]/dlpJobs?key={YOUR_API_KEY}
    
    {
      "inspectJob":{
        "storageConfig":{
          "cloudStorageOptions":{
            "fileSet":{
              "url":"gs://[BUCKET-NAME]/*"
            },
            "bytesLimitPerFile":"1073741824"
          },
          "timespanConfig":{
            "startTime":"2017-11-13T12:34:29.965633345Z",
            "endTime":"2018-01-05T04:45:04.240912125Z"
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "excludeInfoTypes":false,
          "includeQuote":true,
          "minLikelihood":"LIKELY"
        },
        "actions":[
          {
            "saveFindings":{
              "outputConfig":{
                "table":{
                  "projectId":"[PROJECT-ID]",
                  "datasetId":"[DATASET-ID]"
                }
              }
            }
          }
        ]
      }
    }
    

**JSON output:**
    
    
    {
      "name":"projects/[PROJECT-ID]/dlpJobs/[JOB-ID]",
      "type":"INSPECT_JOB",
      "state":"PENDING",
      "inspectDetails":{
        "requestedOptions":{
          "snapshotInspectTemplate":{
    
          },
          "jobConfig":{
            "storageConfig":{
              "cloudStorageOptions":{
                "fileSet":{
                  "url":"gs://[BUCKET-NAME]/*"
                },
                "bytesLimitPerFile":"1073741824"
              },
              "timespanConfig":{
                "startTime":"2017-11-13T12:34:29.965633345Z",
                "endTime":"2018-01-05T04:45:04.240912125Z"
              }
            },
            "inspectConfig":{
              "infoTypes":[
                {
                  "name":"PHONE_NUMBER"
                }
              ],
              "minLikelihood":"LIKELY",
              "limits":{
    
              },
              "includeQuote":true
            },
            "actions":[
              {
                "saveFindings":{
                  "outputConfig":{
                    "table":{
                      "projectId":"[PROJECT-ID]",
                      "datasetId":"[DATASET-ID]",
                      "tableId":"[NEW-TABLE-ID]"
                    }
                  }
                }
              }
            ]
          }
        }
      },
      "createTime":"2018-11-07T18:01:14.225Z"
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).[FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectGcsFile {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String gcsUri = "gs://" + "your-bucket-name" + "/path/to/your/file.txt";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectGcsFile(projectId, gcsUri, topicId, subscriptionId);
      }
    
      // Inspects a file in a Google Cloud Storage Bucket.
      public static void inspectGcsFile(
          String projectId, String gcsUri, String topicId, String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the GCS file to be inspected.
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder().[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html).newBuilder().setUrl(gcsUri)).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The name of the bucket where the file resides.
    // const bucketName = 'YOUR-BUCKET';
    
    // The path to the file within the bucket to inspect.
    // Can contain wildcards, e.g. "my-image.*"
    // const fileName = 'my-image.png';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    async function inspectGCSFile() {
      // Get reference to the file to be inspected
      const storageItem = {
        cloudStorageOptions: {
          fileSet: {url: `gs://${bucketName}/${fileName}`},
        },
      };
    
      // Construct request for creating an inspect job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: {
            infoTypes: infoTypes,
            customInfoTypes: customInfoTypes,
            minLikelihood: minLikelihood,
            limits: {
              maxFindingsPerRequest: maxFindings,
            },
          },
          storageConfig: storageItem,
          actions: [
            {
              pubSub: {
                topic: `projects/${projectId}/topics/${topicId}`,
              },
            },
          ],
        },
      };
    
      // Create a GCS File inspection job and wait for it to complete
      const [topicResponse] = await pubsub.topic(topicId).get();
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
      const [jobsResponse] = await dlp.createDlpJob(request);
      // Get the job's ID
      const jobName = jobsResponse.name;
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          reject(err);
        };
    
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', errorHandler);
      });
    
      setTimeout(() => {
        console.log('Waiting for DLP job to fully complete');
      }, 500);
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectGCSFile();

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List, Optional
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_gcs_file(
        project: str,
        bucket: str,
        filename: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str],
        custom_dictionaries: List[str] = None,
        custom_regexes: List[str] = None,
        min_likelihood: Optional[str] = None,
        max_findings: Optional[int] = None,
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze a file on GCS.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bucket: The name of the GCS bucket containing the file, as a string.
            filename: The name of the file in the bucket, including the path, as a
                string; e.g. 'images/myfile.png'.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [
            {
                "info_type": {"name": f"CUSTOM_DICTIONARY_{i}"},
                "dictionary": {"word_list": {"words": custom_dict.split(",")}},
            }
            for i, custom_dict in enumerate(custom_dictionaries)
        ]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [
            {
                "info_type": {"name": f"CUSTOM_REGEX_{i}"},
                "regex": {"pattern": custom_regex},
            }
            for i, custom_regex in enumerate(custom_regexes)
        ]
        custom_info_types = dictionaries + regexes
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "custom_info_types": custom_info_types,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Construct a storage_config containing the file's URL.
        url = f"gs://{bucket}/{filename}"
        storage_config = {"cloud_storage_options": {"file_set": {"url": url}}}
    
        # Convert the project id into full resource ids.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                f"Info type: {finding.info_type.name}; Count: {finding.count}"
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectGCSFile searches for the given info types in the given file.
    func inspectGCSFile(w io.Writer, projectID string, infoTypeNames []string, customDictionaries []string, customRegexes []string, pubSubTopic, pubSubSub, bucketName, fileName string) error {
    	// projectID := "my-project-id"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// customDictionaries := []string{...}
    	// customRegexes := []string{...}
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// bucketName := "my-bucket"
    	// fileName := "my-file.txt"
    
    	ctx := context.Background()
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    	// Convert the custom dictionary word lists and custom regexes to a list of CustomInfoTypes.
    	var customInfoTypes []*dlppb.CustomInfoType
    	for idx, it := range customDictionaries {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_DICTIONARY_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Dictionary_{
    				Dictionary: &dlppb.CustomInfoType_Dictionary{
    					Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    						WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    							Words: strings.Split(it, ","),
    						},
    					},
    				},
    			},
    		})
    	}
    	for idx, it := range customRegexes {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_REGEX_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Regex_{
    				Regex: &dlppb.CustomInfoType_Regex{
    					Pattern: it,
    				},
    			},
    		})
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(pubSubTopic)
    	if exists, err := t.Exists(ctx); err != nil {
    		return fmt.Errorf("t.Exists: %w", err)
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, pubSubTopic); err != nil {
    			return fmt.Errorf("CreateTopic: %w", err)
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(pubSubSub)
    	if exists, err := s.Exists(ctx); err != nil {
    		return fmt.Errorf("s.Exists: %w", err)
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, pubSubSub, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return fmt.Errorf("CreateSubscription: %w", err)
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + pubSubTopic
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: &dlppb.InspectJobConfig{
    				// StorageConfig describes where to find the data.
    				StorageConfig: &dlppb.StorageConfig{
    					Type: &dlppb.StorageConfig_CloudStorageOptions{
    						CloudStorageOptions: &dlppb.CloudStorageOptions{
    							FileSet: &dlppb.CloudStorageOptions_FileSet{
    								Url: "gs://" + bucketName + "/" + fileName,
    							},
    						},
    					},
    				},
    				// InspectConfig describes what fields to look for.
    				InspectConfig: &dlppb.InspectConfig{
    					InfoTypes:       infoTypes,
    					CustomInfoTypes: customInfoTypes,
    					MinLikelihood:   dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    					Limits: &dlppb.InspectConfig_FindingLimits{
    						MaxFindingsPerRequest: 10,
    					},
    					IncludeQuote: true,
    				},
    				// Send a message to PubSub using Actions.
    				Actions: []*dlppb.Action{
    					{
    						Action: &dlppb.Action_PubSub{
    							PubSub: &dlppb.Action_PublishToPubSub{
    								Topic: topic,
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Create the inspect job.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateDlpJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job: %v\n", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    
    		resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    		if err != nil {
    			fmt.Fprintf(w, "Cloud not get job: %v", err)
    			return
    		}
    		r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    		if len(r) == 0 {
    			fmt.Fprintf(w, "No results")
    		}
    		for _, s := range r {
    			fmt.Fprintf(w, "  Found %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    	return nil
    }
    

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect a file stored on Google Cloud Storage , using Pub/Sub for job status notifications.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string $bucketId          The name of the bucket where the file resides
     * @param string $file              The path to the file within the bucket to inspect. Can contain wildcards e.g. "my-image.*"
     * @param int    $maxFindings       (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function inspect_gcs(
        string $callingProjectId,
        string $topicId,
        string $subscriptionId,
        string $bucketId,
        string $file,
        int $maxFindings = 0
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $creditCardNumberInfoType = (new InfoType())
            ->setName('CREDIT_CARD_NUMBER');
        $infoTypes = [$personNameInfoType, $creditCardNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Construct items to be inspected
        $fileSet = (new FileSet())
            ->setUrl('gs://' . $bucketId . '/' . $file);
    
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet($fileSet);
    
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions($cloudStorageOptions);
    
        // Construct the inspect config object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes);
    
        // Construct the action to run when job completes
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Construct inspect job config to run
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (
                    isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()
                ) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while
                }
            }
            print('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    print('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf('  Found %s instance(s) of infoType %s' . PHP_EOL, $infoTypeStat->getCount(), $infoTypeStat->getInfoType()->getName());
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                print('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                print('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectGoogleCloudStorage
    {
        public static DlpJob InspectGCS(
            string projectId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood,
            int maxFindings,
            bool includeQuote,
            IEnumerable<InfoType> infoTypes,
            IEnumerable<CustomInfoType> customInfoTypes,
            string bucketName,
            string topicId,
            string subscriptionId)
        {
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
                {
                    CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                    {
                        FileSet = new CloudStorageOptions.Types.FileSet { Url = $"gs://{bucketName}/*.txt" },
                        BytesLimitPerFile = 1073741824
                    },
                },
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes = { infoTypes },
                    CustomInfoTypes = { customInfoTypes },
                    ExcludeInfoTypes = false,
                    IncludeQuote = includeQuote,
                    Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                    {
                        MaxFindingsPerRequest = maxFindings
                    },
                    MinLikelihood = minLikelihood
                },
                Actions =
                    {
                        new Google.Cloud.Dlp.V2.Action
                        {
                            // Send results to Pub/Sub topic
                            PubSub = new Google.Cloud.Dlp.V2.Action.Types.PublishToPubSub
                            {
                                Topic = topicId,
                            }
                        }
                    }
            };
    
            // Issue Create Dlp Job Request
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
            };
    
            // We need created job name
            var dlpJob = client.CreateDlpJob(request);
    
            // Get a pub/sub subscription and listen for DLP results
            var fireEvent = new ManualResetEventSlim();
    
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(projectId, subscriptionId);
            var subscriber = [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(subscriptionName).Result;
            subscriber.StartAsync(
                (pubSubMessage, cancellationToken) =>
                {
                    // Given a message that we receive on this subscription, we should either acknowledge or decline it
                    if (pubSubMessage.Attributes["DlpJobName"] == dlpJob.Name)
                    {
                        fireEvent.Set();
                        return Task.FromResult(SubscriberClient.Reply.Ack);
                    }
    
                    return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Nack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Nack));
                });
    
            // We block here until receiving a signal from a separate thread that is waiting on a message indicating receiving a result of Dlp job
            if (fireEvent.Wait(TimeSpan.FromMinutes(1)))
            {
                // Stop the thread that is listening to messages as a result of StartAsync call earlier
                subscriber.StopAsync(CancellationToken.None).Wait();
    
                // Now we can inspect full job results
                var job = client.GetDlpJob(new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html) { DlpJobName = new [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html)(projectId, dlpJob.Name) });
    
                // Inspect Job details
                Console.WriteLine($"Processed bytes: {job.InspectDetails.Result.[ProcessedBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails.Types.Result.html#Google_Cloud_Dlp_V2_InspectDataSourceDetails_Types_Result_ProcessedBytes)}");
                Console.WriteLine($"Total estimated bytes: {job.InspectDetails.Result.[TotalEstimatedBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails.Types.Result.html#Google_Cloud_Dlp_V2_InspectDataSourceDetails_Types_Result_TotalEstimatedBytes)}");
                var stats = job.InspectDetails.Result.[InfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeStats.html);
                Console.WriteLine("Found stats:");
                foreach (var stat in stats)
                {
                    Console.WriteLine($"{stat.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name}");
                }
    
                return job;
            }
    
            throw new InvalidOperationException("The wait failed on timeout");
        }
    }

## Inspect a Datastore kind

You can set up an inspection of a Datastore kind using the Google Cloud console, the DLP API via [REST](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) or [RPC](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc) requests, or programmatically in several languages using a [client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries).

**Note:** For information about the parameters included with the following JSON and code samples, see "[Configure storage inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#configuring-storage-inspection)," later in this topic.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

To set up a scan job of a Datastore kind using Sensitive Data Protection:

### Console

To set up a scan job of a Datastore kind using Sensitive Data Protection:

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. Enter the Sensitive Data Protection job information and click **Continue** to complete each step:

     * For **Choose input data** , enter the identifiers for the project, namespace (optional), and kind that you want to scan. For more details, see [Choose input data](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#choose-input-data).

     * (Optional) For **Configure detection** , you can configure what types of data to look for, called "[infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)." You can select from the [list of pre-defined infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), or you can select a template if one exists. For more details, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).

     * For **Add actions** , select one or more actions for Sensitive Data Protection to take after the job completes. For more information, see [Enable inspection or risk analysis actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions). 

After you select actions, click **Continue**. 

     * (Optional) For **Schedule** , configure a time span or schedule by selecting either **Specify time span** or **Create a trigger to run the job on a periodic schedule**. For more information, see [Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#schedule-job).

  3. Click **Create**.

  4. After the Sensitive Data Protection job completes, you are redirected to the job details page and notified via email. You can view the results of the inspection on the job details page.

  5. (Optional) If you chose to publish Sensitive Data Protection findings to BigQuery, on the **Job details** page, click **View Findings in BigQuery** to open the table in the BigQuery web UI. You can then query the table and analyze your findings. For more information on querying your results in BigQuery, see [Querying Sensitive Data Protection findings in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings).




### Protocol

Following is sample JSON that can be sent in a POST request to the specified DLP API REST endpoint. This example JSON demonstrates how to use the DLP API to inspect Datastore kinds. For information about the parameters included with the request, see "[Configure storage inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#configuring-storage-inspection)," later in this topic.

You can quickly try this out in the APIs Explorer on the reference page for `dlpJobs.create`:

[Go to APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create?apix=true)

Keep in mind that a successful request, even in APIs Explorer, will create a new scan job. For information about how to control scan jobs, see [Retrieve inspection results](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#retrieving-inspection-results), later in this topic. For general information about using JSON to send requests to the DLP API, see the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json).

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT-ID]/dlpJobs?key={YOUR_API_KEY}
    
    {
      "inspectJob":{
        "storageConfig":{
          "datastoreOptions":{
            "kind":{
              "name":"Example-Kind"
            },
            "partitionId":{
              "namespaceId":"[NAMESPACE-ID]",
              "projectId":"[PROJECT-ID]"
            }
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "excludeInfoTypes":false,
          "includeQuote":true,
          "minLikelihood":"LIKELY"
        },
        "actions":[
          {
            "saveFindings":{
              "outputConfig":{
                "table":{
                  "projectId":"[PROJECT-ID]",
                  "datasetId":"[BIGQUERY-DATASET-NAME]",
                  "tableId":"[BIGQUERY-TABLE-NAME]"
                }
              }
            }
          }
        ]
      }
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectDatastoreEntity {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String datastoreNamespace = "your-datastore-namespace";
        String datastoreKind = "your-datastore-kind";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        insepctDatastoreEntity(projectId, datastoreNamespace, datastoreKind, topicId, subscriptionId);
      }
    
      // Inspects a Datastore Entity.
      public static void insepctDatastoreEntity(
          String projectId,
          String datastoreNamespce,
          String datastoreKind,
          String topicId,
          String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the Datastore entity to be inspected.
          [PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html) partitionId =
              [PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html).newBuilder()
                  .setProjectId(projectId)
                  .[setNamespaceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.Builder.html#com_google_privacy_dlp_v2_PartitionId_Builder_setNamespaceId_java_lang_String_)(datastoreNamespce)
                  .build();
          [KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html) kindExpression = [KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html).newBuilder().setName(datastoreKind).build();
    
          [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html) datastoreOptions =
              [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html).newBuilder().setKind(kindExpression).setPartitionId(partitionId).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setDatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setDatastoreOptions_com_google_privacy_dlp_v2_DatastoreOptions_)(datastoreOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The project ID the target Datastore is stored under
    // This may or may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // (Optional) The ID namespace of the Datastore document to inspect.
    // To ignore Datastore namespaces, set this to an empty string ('')
    // const namespaceId = '';
    
    // The kind of the Datastore entity to inspect.
    // const kind = 'Person';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    async function inspectDatastore() {
      // Construct items to be inspected
      const storageItems = {
        datastoreOptions: {
          partitionId: {
            projectId: dataProjectId,
            namespaceId: namespaceId,
          },
          kind: {
            name: kind,
          },
        },
      };
    
      // Construct request for creating an inspect job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: {
            infoTypes: infoTypes,
            customInfoTypes: customInfoTypes,
            minLikelihood: minLikelihood,
            limits: {
              maxFindingsPerRequest: maxFindings,
            },
          },
          storageConfig: storageItems,
          actions: [
            {
              pubSub: {
                topic: `projects/${projectId}/topics/${topicId}`,
              },
            },
          ],
        },
      };
      // Run inspect-job creation request
      const [topicResponse] = await pubsub.topic(topicId).get();
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          reject(err);
        };
    
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', errorHandler);
      });
      // Wait for DLP job to fully complete
      setTimeout(() => {
        console.log('Waiting for DLP job to fully complete');
      }, 500);
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectDatastore();

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List, Optional
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_datastore(
        project: str,
        datastore_project: str,
        kind: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str],
        custom_dictionaries: List[str] = None,
        custom_regexes: List[str] = None,
        namespace_id: str = None,
        min_likelihood: Optional[int] = None,
        max_findings: Optional[int] = None,
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze Datastore data.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            datastore_project: The Google Cloud project id of the target Datastore.
            kind: The kind of the Datastore entity to inspect, e.g. 'Person'.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            namespace_id: The namespace of the Datastore document, if applicable.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [
            {
                "info_type": {"name": f"CUSTOM_DICTIONARY_{i}"},
                "dictionary": {"word_list": {"words": custom_dict.split(",")}},
            }
            for i, custom_dict in enumerate(custom_dictionaries)
        ]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [
            {
                "info_type": {"name": f"CUSTOM_REGEX_{i}"},
                "regex": {"pattern": custom_regex},
            }
            for i, custom_regex in enumerate(custom_regexes)
        ]
        custom_info_types = dictionaries + regexes
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "custom_info_types": custom_info_types,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Construct a storage_config containing the target Datastore info.
        storage_config = {
            "datastore_options": {
                "partition_id": {
                    "project_id": datastore_project,
                    "namespace_id": namespace_id,
                },
                "kind": {"name": kind},
            }
        }
    
        # Convert the project id into full resource ids.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                f"Info type: {finding.info_type.name}; Count: {finding.count}"
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        # Register the callback and wait on the event.
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectDatastore searches for the given info types in the given dataset kind.
    func inspectDatastore(w io.Writer, projectID string, infoTypeNames []string, customDictionaries []string, customRegexes []string, pubSubTopic, pubSubSub, dataProject, namespaceID, kind string) error {
    	// projectID := "my-project-id"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// customDictionaries := []string{...}
    	// customRegexes := []string{...}
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// namespaceID := "namespace-id"
    	// kind := "MyKind"
    
    	ctx := context.Background()
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    	// Convert the custom dictionary word lists and custom regexes to a list of CustomInfoTypes.
    	var customInfoTypes []*dlppb.CustomInfoType
    	for idx, it := range customDictionaries {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_DICTIONARY_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Dictionary_{
    				Dictionary: &dlppb.CustomInfoType_Dictionary{
    					Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    						WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    							Words: strings.Split(it, ","),
    						},
    					},
    				},
    			},
    		})
    	}
    	for idx, it := range customRegexes {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_REGEX_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Regex_{
    				Regex: &dlppb.CustomInfoType_Regex{
    					Pattern: it,
    				},
    			},
    		})
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(pubSubTopic)
    	if exists, err := t.Exists(ctx); err != nil {
    		return fmt.Errorf("t.Exists: %w", err)
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, pubSubTopic); err != nil {
    			return fmt.Errorf("CreateTopic: %w", err)
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(pubSubSub)
    	if exists, err := s.Exists(ctx); err != nil {
    		return fmt.Errorf("s.Exists: %w", err)
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, pubSubSub, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return fmt.Errorf("CreateSubscription: %w", err)
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + pubSubTopic
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: &dlppb.InspectJobConfig{
    				// StorageConfig describes where to find the data.
    				StorageConfig: &dlppb.StorageConfig{
    					Type: &dlppb.StorageConfig_DatastoreOptions{
    						DatastoreOptions: &dlppb.DatastoreOptions{
    							PartitionId: &dlppb.PartitionId{
    								ProjectId:   dataProject,
    								NamespaceId: namespaceID,
    							},
    							Kind: &dlppb.KindExpression{
    								Name: kind,
    							},
    						},
    					},
    				},
    				// InspectConfig describes what fields to look for.
    				InspectConfig: &dlppb.InspectConfig{
    					InfoTypes:       infoTypes,
    					CustomInfoTypes: customInfoTypes,
    					MinLikelihood:   dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    					Limits: &dlppb.InspectConfig_FindingLimits{
    						MaxFindingsPerRequest: 10,
    					},
    					IncludeQuote: true,
    				},
    				// Send a message to PubSub using Actions.
    				Actions: []*dlppb.Action{
    					{
    						Action: &dlppb.Action_PubSub{
    							PubSub: &dlppb.Action_PublishToPubSub{
    								Topic: topic,
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Create the inspect job.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateDlpJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job: %v\n", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    
    		resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    		if err != nil {
    			fmt.Fprintf(w, "Error getting completed job: %v\n", err)
    			return
    		}
    		r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    		if len(r) == 0 {
    			fmt.Fprintf(w, "No results")
    			return
    		}
    		for _, s := range r {
    			fmt.Fprintf(w, "  Found %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    	return nil
    }
    

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DatastoreOptions;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\KindExpression;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\PartitionId;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect Datastore, using Pub/Sub for job status notifications.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $dataProjectId     The project ID containing the target Datastore
     * @param string $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string $kind              The datastore kind to inspect
     * @param string $namespaceId       The ID namespace of the Datastore document to inspect
     * @param int    $maxFindings       (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function inspect_datastore(
        string $callingProjectId,
        string $dataProjectId,
        string $topicId,
        string $subscriptionId,
        string $kind,
        string $namespaceId,
        int $maxFindings = 0
    ): void {
        // Instantiate clients
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$personNameInfoType, $phoneNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Construct items to be inspected
        $partitionId = (new PartitionId())
            ->setProjectId($dataProjectId)
            ->setNamespaceId($namespaceId);
    
        $kindExpression = (new KindExpression())
            ->setName($kind);
    
        $datastoreOptions = (new DatastoreOptions())
            ->setPartitionId($partitionId)
            ->setKind($kindExpression);
    
        // Construct the inspect config object
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits);
    
        // Construct the storage config object
        $storageConfig = (new StorageConfig())
            ->setDatastoreOptions($datastoreOptions);
    
        // Construct the action to run when job completes
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Construct inspect job config to run
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (
                    isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()
                ) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while
                }
            }
            print('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    print('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf('  Found %s instance(s) of infoType %s' . PHP_EOL, $infoTypeStat->getCount(), $infoTypeStat->getInfoType()->getName());
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                print('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                print('Unexpected job state.');
        }
    }

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectCloudDataStore
    {
        public static object Inspect(
            string projectId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood,
            int maxFindings,
            bool includeQuote,
            string kindName,
            string namespaceId,
            IEnumerable<InfoType> infoTypes,
            IEnumerable<CustomInfoType> customInfoTypes,
            string datasetId,
            string tableId)
        {
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
                {
                    DatastoreOptions = new [DatastoreOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatastoreOptions.html)
                    {
                        Kind = new [KindExpression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KindExpression.html) { Name = kindName },
                        PartitionId = new [PartitionId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PartitionId.html)
                        {
                            NamespaceId = namespaceId,
                            ProjectId = projectId,
                        }
                    },
                    TimespanConfig = new StorageConfig.Types.TimespanConfig
                    {
                        StartTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow.AddYears(-1)),
                        EndTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow)
                    }
                },
    
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes = { infoTypes },
                    CustomInfoTypes = { customInfoTypes },
                    Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                    {
                        MaxFindingsPerRequest = maxFindings
                    },
                    ExcludeInfoTypes = false,
                    IncludeQuote = includeQuote,
                    MinLikelihood = minLikelihood
                },
                Actions =
                    {
                        new Google.Cloud.Dlp.V2.Action
                        {
                            // Save results in BigQuery Table
                            SaveFindings = new Google.Cloud.Dlp.V2.Action.Types.SaveFindings
                            {
                                OutputConfig = new [OutputStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.html)
                                {
                                    Table = new Google.Cloud.Dlp.V2.BigQueryTable
                                    {
                                        ProjectId = projectId,
                                        DatasetId = datasetId,
                                        TableId = tableId
                                    }
                                }
                            },
                        }
                    }
            };
    
            // Issue Create Dlp Job Request
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
            };
    
            // We need created job name
            var dlpJob = client.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Make sure the job finishes before inspecting the results.
            // Alternatively, we can inspect results opportunistically, but
            // for testing purposes, we want consistent outcome
            var finishedJob = EnsureJobFinishes(projectId, jobName);
            var bigQueryClient = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            var table = bigQueryClient.GetTable(datasetId, tableId);
    
            // Return only first page of 10 rows
            Console.WriteLine("DLP v2 Results:");
            var firstPage = table.ListRows(new [ListRowsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.ListRowsOptions.html) { StartIndex = 0, PageSize = 10 });
            foreach (var item in firstPage)
            {
                Console.WriteLine($"\t {item[""]}");
            }
    
            return finishedJob;
        }
    
        private static DlpJob EnsureJobFinishes(string projectId, string jobName)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = new [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html)(projectId, jobName),
            };
    
            // Simple logic that gives the job 5*30 sec at most to complete - for testing purposes only
            var numOfAttempts = 5;
            do
            {
                var dlpJob = client.GetDlpJob(request);
                numOfAttempts--;
                if (dlpJob.State != [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.html).[JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html).[Running](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html#Google_Cloud_Dlp_V2_DlpJob_Types_JobState_Running))
                {
                    return dlpJob;
                }
    
                Thread.Sleep(TimeSpan.FromSeconds(30));
            } while (numOfAttempts > 0);
    
            throw new InvalidOperationException("Job did not complete in time");
        }
    }

## Inspect a BigQuery table

You can set up an inspection of a BigQuery table using Sensitive Data Protection via REST requests, or programmatically in several languages using a [client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries).

**Note:** For information about the parameters included with the following JSON and code samples, see "[Configure storage inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#configuring-storage-inspection)," later in this topic.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

To set up a scan job of a BigQuery table using Sensitive Data Protection:

### Console

To set up a scan job of a BigQuery table using Sensitive Data Protection:

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. Enter the Sensitive Data Protection job information and click **Continue** to complete each step:

     * For **Choose input data** , name the job by entering a value in the **Name** field. In **Location** , choose BigQuery from the **Storage type** menu, and then enter the information for the table to scan.

The **Sampling** section is pre-configured to run a sample scan against your data. You can adjust the **Limit rows by** and **Maximum number of rows** fields to save resources if you have a large amount of data. For more details, see [Choose input data](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#choose-input-data).

     * (Optional) If you want to be able to link each finding to the row that contains it, set the **Identifying fields** field. 

Enter the names of the columns that uniquely identify each row within the table. If necessary, use dot notation to specify nested fields. You can add as many fields as you want.

You must also turn on the **Save to BigQuery** action to export the findings to BigQuery. When the findings are exported to BigQuery, each finding contains the respective values of the identifying fields. For more information, see [`identifyingFields`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.identifying_fields).

     * (Optional) For **Configure detection** , you can configure what types of data to look for, called "[infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)." You can select from the [list of pre-defined infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), or you can select a template if one exists. For more details, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).

     * For **Add actions** , select one or more actions for Sensitive Data Protection to take after the job completes. For more information, see [Enable inspection or risk analysis actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions). 

After you select actions, click **Continue**. 

     * (Optional) For **Schedule** , to run the scan one time only, leave the menu set to **None**. To schedule scans to run periodically, click **Create a trigger to run the job on a periodic schedule**. For more details, see [Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#schedule-job).

  3. Click **Create**.

  4. After the Sensitive Data Protection job completes, you are redirected to the job details page and notified via email. You can view the results of the inspection on the job details page.

  5. (Optional) If you chose to publish Sensitive Data Protection findings to BigQuery, on the **Job details** page, click **View Findings in BigQuery** to open the table in the BigQuery web UI. You can then query the table and analyze your findings. For more information on querying your results in BigQuery, see [Querying Sensitive Data Protection findings in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings).




### Protocol

Following is sample JSON that can be sent in a POST request to the specified DLP API REST endpoint. This example JSON demonstrates how to use the DLP API to inspect BigQuery tables. For information about the parameters included with the request, see "[Configure storage inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#configuring-storage-inspection)," later in this topic. 

You can quickly try this out in the APIs Explorer on the reference page for `dlpJobs.create`:

[Go to APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create?apix=true)

Keep in mind that a successful request, even in APIs Explorer, will create a new scan job. For information about how to control scan jobs, see "[Retrieve inspection results](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#retrieving-inspection-results)," later in this topic. For general information about using JSON to send requests to the DLP API, see the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json).

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT-ID]/dlpJobs?key={YOUR_API_KEY}
    
    {
      "inspectJob":{
        "storageConfig":{
          "bigQueryOptions":{
            "tableReference":{
              "projectId":"[PROJECT-ID]",
              "datasetId":"[BIGQUERY-DATASET-NAME]",
              "tableId":"[BIGQUERY-TABLE-NAME]"
            },
            "identifyingFields":[
              {
                "name":"id"
              }
            ]
          },
          "timespanConfig":{
            "startTime":"2017-11-13T12:34:29.965633345Z ",
            "endTime":"2018-01-05T04:45:04.240912125Z "
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "excludeInfoTypes":false,
          "includeQuote":true,
          "minLikelihood":"LIKELY"
        },
        "actions":[
          {
            "saveFindings":{
              "outputConfig":{
                "table":{
                  "projectId":"[PROJECT-ID]",
                  "datasetId":"[BIGQUERY-DATASET-NAME]",
                  "tableId":"[BIGQUERY-TABLE-NAME]"
                },
                "outputSchema": "BASIC_COLUMNS"
              }
            }
          }
        ]
      }
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectBigQueryTable {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String bigQueryDatasetId = "your-bigquery-dataset-id";
        String bigQueryTableId = "your-bigquery-table-id";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectBigQueryTable(projectId, bigQueryDatasetId, bigQueryTableId, topicId, subscriptionId);
      }
    
      // Inspects a BigQuery Table
      public static void inspectBigQueryTable(
          String projectId,
          String bigQueryDatasetId,
          String bigQueryTableId,
          String topicId,
          String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the BigQuery table to be inspected.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) tableReference =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setDatasetId(bigQueryDatasetId)
                  .setTableId(bigQueryTableId)
                  .build();
    
          [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html) bigQueryOptions =
              [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html).newBuilder().setTableReference(tableReference).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setBigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setBigQueryOptions_com_google_privacy_dlp_v2_BigQueryOptions_)(bigQueryOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    async function inspectBigquery() {
      // Construct item to be inspected
      const storageItem = {
        bigQueryOptions: {
          tableReference: {
            projectId: dataProjectId,
            datasetId: datasetId,
            tableId: tableId,
          },
        },
      };
    
      // Construct request for creating an inspect job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: {
            infoTypes: infoTypes,
            customInfoTypes: customInfoTypes,
            minLikelihood: minLikelihood,
            limits: {
              maxFindingsPerRequest: maxFindings,
            },
          },
          storageConfig: storageItem,
          actions: [
            {
              pubSub: {
                topic: `projects/${projectId}/topics/${topicId}`,
              },
            },
          ],
        },
      };
    
      // Run inspect-job creation request
      const [topicResponse] = await pubsub.topic(topicId).get();
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          reject(err);
        };
    
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', errorHandler);
      });
      // Wait for DLP job to fully complete
      setTimeout(() => {
        console.log('Waiting for DLP job to fully complete');
      }, 500);
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    
    await inspectBigquery();

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List, Optional
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_bigquery(
        project: str,
        bigquery_project: str,
        dataset_id: str,
        table_id: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str],
        custom_dictionaries: List[str] = None,
        custom_regexes: List[str] = None,
        min_likelihood: Optional[int] = None,
        max_findings: Optional[int] = None,
        timeout: int = 500,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze BigQuery data.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bigquery_project: The Google Cloud project id of the target table.
            dataset_id: The id of the target BigQuery dataset.
            table_id: The id of the target BigQuery table.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [
            {
                "info_type": {"name": f"CUSTOM_DICTIONARY_{i}"},
                "dictionary": {"word_list": {"words": custom_dict.split(",")}},
            }
            for i, custom_dict in enumerate(custom_dictionaries)
        ]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [
            {
                "info_type": {"name": f"CUSTOM_REGEX_{i}"},
                "regex": {"pattern": custom_regex},
            }
            for i, custom_regex in enumerate(custom_regexes)
        ]
        custom_info_types = dictionaries + regexes
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "custom_info_types": custom_info_types,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Construct a storage_config containing the target Bigquery info.
        storage_config = {
            "big_query_options": {
                "table_reference": {
                    "project_id": bigquery_project,
                    "dataset_id": dataset_id,
                    "table_id": table_id,
                }
            }
        }
    
        # Convert the project id into full resource ids.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                "Info type: {}; Count: {}".format(
                                    finding.info_type.name, finding.count
                                )
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        # Register the callback and wait on the event.
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectBigquery searches for the given info types in the given Bigquery dataset table.
    func inspectBigquery(w io.Writer, projectID string, infoTypeNames []string, customDictionaries []string, customRegexes []string, pubSubTopic, pubSubSub, dataProject, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// customDictionaries := []string{...}
    	// customRegexes := []string{...}
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// dataProject := "my-data-project-ID"
    	// datasetID := "my_dataset"
    	// tableID := "mytable"
    
    	ctx := context.Background()
    
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    	// Convert the custom dictionary word lists and custom regexes to a list of CustomInfoTypes.
    	var customInfoTypes []*dlppb.CustomInfoType
    	for idx, it := range customDictionaries {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_DICTIONARY_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Dictionary_{
    				Dictionary: &dlppb.CustomInfoType_Dictionary{
    					Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    						WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    							Words: strings.Split(it, ","),
    						},
    					},
    				},
    			},
    		})
    	}
    	for idx, it := range customRegexes {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_REGEX_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Regex_{
    				Regex: &dlppb.CustomInfoType_Regex{
    					Pattern: it,
    				},
    			},
    		})
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(pubSubTopic)
    	if exists, err := t.Exists(ctx); err != nil {
    		return fmt.Errorf("t.Exists: %w", err)
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, pubSubTopic); err != nil {
    			return fmt.Errorf("CreateTopic: %w", err)
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(pubSubSub)
    	if exists, err := s.Exists(ctx); err != nil {
    		return fmt.Errorf("s.Exits: %w", err)
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, pubSubSub, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return fmt.Errorf("CreateSubscription: %w", err)
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + pubSubTopic
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: &dlppb.InspectJobConfig{
    				// StorageConfig describes where to find the data.
    				StorageConfig: &dlppb.StorageConfig{
    					Type: &dlppb.StorageConfig_BigQueryOptions{
    						BigQueryOptions: &dlppb.BigQueryOptions{
    							TableReference: &dlppb.BigQueryTable{
    								ProjectId: dataProject,
    								DatasetId: datasetID,
    								TableId:   tableID,
    							},
    						},
    					},
    				},
    				// InspectConfig describes what fields to look for.
    				InspectConfig: &dlppb.InspectConfig{
    					InfoTypes:       infoTypes,
    					CustomInfoTypes: customInfoTypes,
    					MinLikelihood:   dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    					Limits: &dlppb.InspectConfig_FindingLimits{
    						MaxFindingsPerRequest: 10,
    					},
    					IncludeQuote: true,
    				},
    				// Send a message to PubSub using Actions.
    				Actions: []*dlppb.Action{
    					{
    						Action: &dlppb.Action_PubSub{
    							PubSub: &dlppb.Action_PublishToPubSub{
    								Topic: topic,
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Create the inspect job.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateDlpJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job: %v\n", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    
    		resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    		if err != nil {
    			fmt.Fprintf(w, "Error getting completed job: %v\n", err)
    			return
    		}
    		r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    		if len(r) == 0 {
    			fmt.Fprintf(w, "No results")
    			return
    		}
    		for _, s := range r {
    			fmt.Fprintf(w, "  Found %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    	return nil
    }
    

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryOptions;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect a BigQuery table , using Pub/Sub for job status notifications.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $dataProjectId     The project ID containing the target Datastore
     * @param string $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string $datasetId         The ID of the dataset to inspect
     * @param string $tableId           The ID of the table to inspect
     * @param int    $maxFindings       (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function inspect_bigquery(
        string $callingProjectId,
        string $dataProjectId,
        string $topicId,
        string $subscriptionId,
        string $datasetId,
        string $tableId,
        int $maxFindings = 0
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $creditCardNumberInfoType = (new InfoType())
            ->setName('CREDIT_CARD_NUMBER');
        $infoTypes = [$personNameInfoType, $creditCardNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Construct items to be inspected
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($dataProjectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
    
        $bigQueryOptions = (new BigQueryOptions())
            ->setTableReference($bigqueryTable);
    
        $storageConfig = (new StorageConfig())
            ->setBigQueryOptions($bigQueryOptions);
    
        // Construct the inspect config object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes);
    
        // Construct the action to run when job completes
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Construct inspect job config to run
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while
                }
            }
            print('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    print('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                print('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                print('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectBigQuery
    {
        public static object Inspect(
            string projectId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood,
            int maxFindings,
            bool includeQuote,
            IEnumerable<FieldId> identifyingFields,
            IEnumerable<InfoType> infoTypes,
            IEnumerable<CustomInfoType> customInfoTypes,
            string datasetId,
            string tableId)
        {
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
                {
                    BigQueryOptions = new [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.html)
                    {
                        TableReference = new Google.Cloud.Dlp.V2.BigQueryTable
                        {
                            ProjectId = projectId,
                            DatasetId = datasetId,
                            TableId = tableId,
                        },
                        IdentifyingFields =
                            {
                                identifyingFields
                            }
                    },
    
                    TimespanConfig = new StorageConfig.Types.TimespanConfig
                    {
                        StartTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow.AddYears(-1)),
                        EndTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow)
                    }
                },
    
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes = { infoTypes },
                    CustomInfoTypes = { customInfoTypes },
                    Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                    {
                        MaxFindingsPerRequest = maxFindings
                    },
                    ExcludeInfoTypes = false,
                    IncludeQuote = includeQuote,
                    MinLikelihood = minLikelihood
                },
                Actions =
                    {
                        new Google.Cloud.Dlp.V2.Action
                        {
                            // Save results in BigQuery Table
                            SaveFindings = new Google.Cloud.Dlp.V2.Action.Types.SaveFindings
                            {
                                OutputConfig = new [OutputStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.html)
                                {
                                    Table = new Google.Cloud.Dlp.V2.BigQueryTable
                                    {
                                        ProjectId = projectId,
                                        DatasetId = datasetId,
                                        TableId = tableId
                                    }
                                }
                            },
                        }
                    }
            };
    
            // Issue Create Dlp Job Request
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
            };
    
            // We need created job name
            var dlpJob = client.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Make sure the job finishes before inspecting the results.
            // Alternatively, we can inspect results opportunistically, but
            // for testing purposes, we want consistent outcome
            var finishedJob = EnsureJobFinishes(projectId, jobName);
            var bigQueryClient = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            var table = bigQueryClient.GetTable(datasetId, tableId);
    
            // Return only first page of 10 rows
            Console.WriteLine("DLP v2 Results:");
            var firstPage = table.ListRows(new [ListRowsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.ListRowsOptions.html) { StartIndex = 0, PageSize = 10 });
            foreach (var item in firstPage)
            {
                Console.WriteLine($"\t {item[""]}");
            }
    
            return finishedJob;
        }
    
        private static DlpJob EnsureJobFinishes(string projectId, string jobName)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = new [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html)(projectId, jobName),
            };
    
            // Simple logic that gives the job 5*30 sec at most to complete - for testing purposes only
            var numOfAttempts = 5;
            do
            {
                var dlpJob = client.GetDlpJob(request);
                numOfAttempts--;
                if (dlpJob.State != [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.html).[JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html).[Running](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html#Google_Cloud_Dlp_V2_DlpJob_Types_JobState_Running))
                {
                    return dlpJob;
                }
    
                Thread.Sleep(TimeSpan.FromSeconds(30));
            } while (numOfAttempts > 0);
    
            throw new InvalidOperationException("Job did not complete in time");
        }
    }
    

## Configure storage inspection

To inspect a Cloud Storage location, Datastore kind, or BigQuery table, you send a request to the [`projects.dlpJobs.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create) method of the DLP API that contains at least the location of the data to scan and what to scan for. Beyond those required parameters, you can also specify where to write the scan results, size and likelihood thresholds, and more. A successful request results in the creation of a [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) object instance, which is discussed in "[Retrieve inspection results](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#retrieving-inspection-results)."

The available configuration options are summarized here:

  * [`InspectJobConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig) object: Contains the configuration information for the inspection job. Note that the `InspectJobConfig` object is also used by the [`JobTriggers`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers) object for scheduling the creation of [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob)s. This object includes:

    * [`StorageConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#StorageConfig) object: Required. Contains details about the storage repository to scan:

      * One of the following must be included in the `StorageConfig` object, depending on the type of storage repository being scanned:

      * [`CloudStorageOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions) object: Contains information about the Cloud Storage bucket to scan.

      * [`DatastoreOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#DatastoreOptions) object: Contains information about the Datastore data set to scan.

      * [`BigQueryOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions) object: Contains information about the BigQuery table (and, optionally, identifying fields) to scan. This object also enables results sampling. For more information, see Enabling results sampling below.

      * [`TimespanConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#TimespanConfig) object: Optional. Specifies the timespan of the items to include in the scan.

    * [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) object: Required. Specifies what to scan for, such as [infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) and [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) values.

      * [`InfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) objects: Required. One or more [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) values to scan for.
      * [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) enumeration: Optional. When set, Sensitive Data Protection will only return findings equal to or above this [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) threshold. If this enum is omitted, the default value is `POSSIBLE`.
      * [`FindingLimits`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FindingLimits) object: Optional. When set, this object enables you to specify a limit for the number of findings returned.
      * `includeQuote` parameter: Optional. Defaults to `false`. When set to `true`, each finding will include a contextual quote from the data that triggered it.
      * `excludeInfoTypes` parameter: Optional. Defaults to `false`. When set to `true`, scan results will exclude type information for the findings.
      * [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) objects: One or more custom, user-created infoTypes. For more information about creating custom infoTypes, see [Creating custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes).
    * `inspectTemplateName` string: Optional. Specifies a template to use to populate default values in the [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) object. If you've already specified `InspectConfig`, template values will be merged in.

    * [`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#Action) objects: Optional. One or more actions to execute at the completion of the job. Each action is executed in the order in which they're listed. This is where you specify where to write results, or whether to publish a notification to a Pub/Sub topic.

  * `jobId`: Optional. An identifier for the job returned by Sensitive Data Protection. If `jobId` is omitted or empty, the system creates an ID for the job. If specified, the job is assigned this ID value. The job ID must be unique, and can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the following regular expression: `[a-zA-Z\\d-]+`.




## Limit the amount of content inspected

If you are scanning BigQuery tables or Cloud Storage buckets, Sensitive Data Protection includes a way to scan a subset of the dataset. This has the effect of providing a sampling of scan results without incurring the potential costs of scanning an entire dataset.

The following sections contain information about limiting the size of both Cloud Storage scans and BigQuery scans.

### Limit Cloud Storage scans

You can enable sampling in Cloud Storage by limiting the amount of data that is scanned. You can instruct the DLP API to scan only files under a certain size, only certain file types, and only a certain percentage of the total number of files in the input file set. To do so, specify the following optional fields within [`CloudStorageOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions):

  * `bytesLimitPerFile`: Sets the maximum number of bytes to scan from a file. If a scanned file's size is larger than this value, the rest of the bytes are omitted. Setting this field has no effect on certain file types. For more information, see [Limits on bytes scanned per file](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file).
  * `fileTypes[]`: Lists the [`FileTypes`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FileType) to include in the scan. This can be set to one or more of the following [enumerated types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).
  * `filesLimitPercent`: Limits the number of files to scan to the specified percentage of the input [`FileSet`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#fileset). Specifying either `0` or `100` here indicates there is no limit.
  * `sampleMethod`: How to sample bytes if not all bytes are scanned. Specifying this value is meaningful only when used in conjunction with `bytesLimitPerFile`. If not specified, scanning starts from the top. This field can be set to one of two values: 
    * `TOP`: Scanning starts from the top.
    * `RANDOM_START`: For each file larger than the size specified in `bytesLimitPerFile`, randomly pick the offset to start scanning. The scanned bytes are contiguous.

**Note:** Because you must scan the entire image when inspecting for sensitive data, sampling is not supported for image file types. Any images scanned will be billed according to the size of the image file.

The following examples demonstrate using the DLP API to scan a 90% subset of a Cloud Storage bucket for person names. The scan starts from a random location in the dataset, and only includes text files under 200 bytes.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class InspectStorageWithSampling
    {
        public static async Task<DlpJob> InspectAsync(
            string projectId,
            string gcsUri,
            string topicId,
            string subId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible),
            IEnumerable<InfoType> infoTypes = null)
        {
    
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct Storage config by specifying the GCS file to be inspected
            // and sample method.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                {
                    FileSet = new CloudStorageOptions.Types.FileSet
                    {
                        Url = gcsUri
                    },
                    BytesLimitPerFile = 200,
                    FileTypes = { new [FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html)[] { [FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html).[Csv](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html#Google_Cloud_Dlp_V2_FileType_Csv) } },
                    FilesLimitPercent = 90,
                    SampleMethod = [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.html).[SampleMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.SampleMethod.html).[RandomStart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.SampleMethod.html#Google_Cloud_Dlp_V2_CloudStorageOptions_Types_SampleMethod_RandomStart)
                }
            };
    
            // Construct the Inspect Config and specify the type of info the inspection
            // will look for.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } }
                },
                IncludeQuote = true,
                MinLikelihood = minLikelihood
            };
    
            // Construct the pubsub action.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PubSub = new Action.Types.PublishToPubSub
                    {
                        Topic = $"projects/{projectId}/topics/{topicId}"
                    }
                }
            };
    
            // Construct the inspect job config using above created objects.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Issue Create Dlp Job Request
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
            };
    
            // We keep the name of the job that we just created.
            var dlpJob = dlp.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Listen to pub/sub for the job
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(projectId, subId);
            var subscriber = await [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(
                subscriptionName);
    
            await subscriber.StartAsync(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancel) =>
            {
                if (message.Attributes["DlpJobName"] == jobName)
                {
                    subscriber.StopAsync(cancel);
                    return Task.FromResult(SubscriberClient.Reply.Ack);
                }
                else
                {
                    return Task.FromResult(SubscriberClient.Reply.Nack);
                }
            });
    
            // Get the latest state of the job from the service
            var resultJob = dlp.GetDlpJob(new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html#Google_Cloud_Dlp_V2_DlpJobName_Parse_System_String_)(jobName)
            });
    
            // Parse the response and process results.
            System.Console.WriteLine($"Job status: {resultJob.State}");
            System.Console.WriteLine($"Job Name: {resultJob.Name}");
    
            var result = resultJob.InspectDetails.Result;
            foreach (var infoType in result.[InfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeStats.html))
            {
                System.Console.WriteLine($"Info Type: {infoType.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name}");
                System.Console.WriteLine($"Count: {infoType.Count}");
            }
            return resultJob;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectGcsFileWithSampling inspects a storage with sampling
    func inspectGcsFileWithSampling(w io.Writer, projectID, gcsUri, topicID, subscriptionId string) error {
    	// projectId := "your-project-id"
    	// gcsUri := "gs://" + "your-bucket-name" + "/path/to/your/file.txt"
    	// topicID := "your-pubsub-topic-id"
    	// subscriptionId := "your-pubsub-subscription-id"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	// Closing the client safely cleans up background resources.
    	defer client.Close()
    
    	// Specify the GCS file to be inspected and sampling configuration
    	var cloudStorageOptions = &dlppb.CloudStorageOptions{
    		FileSet: &dlppb.CloudStorageOptions_FileSet{
    			Url: gcsUri,
    		},
    		BytesLimitPerFile: int64(200),
    		FileTypes: []dlppb.FileType{
    			dlppb.[FileType_TEXT_FILE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_FileType_FILE_TYPE_UNSPECIFIED_FileType_BINARY_FILE_FileType_TEXT_FILE_FileType_IMAGE_FileType_WORD_FileType_PDF_FileType_AVRO_FileType_CSV_FileType_TSV_FileType_POWERPOINT_FileType_EXCEL),
    		},
    		FilesLimitPercent: int32(90),
    		SampleMethod:      dlppb.[CloudStorageOptions_RANDOM_START](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CloudStorageOptions_SAMPLE_METHOD_UNSPECIFIED_CloudStorageOptions_TOP_CloudStorageOptions_RANDOM_START),
    	}
    
    	var storageConfig = &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_CloudStorageOptions{
    			CloudStorageOptions: cloudStorageOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	// Specify how the content should be inspected.
    	var inspectConfig = &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PERSON_NAME"},
    		},
    		ExcludeInfoTypes: true,
    		IncludeQuote:     true,
    		MinLikelihood:    dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(topicID)
    	if exists, err := t.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, topicID); err != nil {
    			return err
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(subscriptionId)
    	if exists, err := s.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, subscriptionId, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return err
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + topicID
    
    	var action = &dlppb.Action{
    		Action: &dlppb.Action_PubSub{
    			PubSub: &dlppb.Action_PublishToPubSub{
    				Topic: topic,
    			},
    		},
    	}
    
    	// Configure the long running job we want the service to perform.
    	var inspectJobConfig = &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Use the client to send the request.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Job Created: %v", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    
    		resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    		if err != nil {
    			fmt.Fprintf(w, "Error getting completed job: %v\n", err)
    			return
    		}
    		r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    		if len(r) == 0 {
    			fmt.Fprintf(w, "No results")
    			return
    		}
    		for _, s := range r {
    			fmt.Fprintf(w, "\nFound %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
    	})
    	if err != nil {
    		return err
    	}
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).[FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).SampleMethod;
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class InspectGcsFileWithSampling {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String gcsUri = "gs://" + "your-bucket-name" + "/path/to/your/file.txt";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectGcsFileWithSampling(projectId, gcsUri, topicId, subscriptionId);
      }
    
      // Inspects a file in a Google Cloud Storage Bucket.
      public static void inspectGcsFileWithSampling(
          String projectId, String gcsUri, String topicId, String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the GCS file to be inspected and sampling configuration
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder()
                  .[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html).newBuilder().setUrl(gcsUri))
                  .[setBytesLimitPerFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setBytesLimitPerFile_long_)(200)
                  .[addFileTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_addFileTypes_com_google_privacy_dlp_v2_FileType_)([FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html).TEXT_FILE)
                  .[setFilesLimitPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFilesLimitPercent_int_)(90)
                  .setSampleMethod(SampleMethod.RANDOM_START)
                  .build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setExcludeInfoTypes(true)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The gcs file path
    // const gcsUri = 'gs://" + "your-bucket-name" + "/path/to/your/file.txt';
    
    // Specify the type of info the inspection will look for.
    // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    // const infoTypes = [{ name: 'PERSON_NAME' }];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    // DLP Job max time (in milliseconds)
    const DLP_JOB_WAIT_TIME = 15 * 1000 * 60;
    
    async function inspectGcsFileSampling() {
      // Specify the GCS file to be inspected and sampling configuration
      const storageItemConfig = {
        cloudStorageOptions: {
          fileSet: {url: gcsUri},
          bytesLimitPerFile: 200,
          filesLimitPercent: 90,
          fileTypes: [DLP.protos.google.privacy.dlp.v2.[FileType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.filetype.html).[TEXT_FILE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.filetype.html)],
          sampleMethod:
            DLP.protos.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cloudstorageoptions-class.html).SampleMethod
              .RANDOM_START,
        },
      };
    
      // Specify how the content should be inspected.
      const inspectConfig = {
        infoTypes: infoTypes,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[POSSIBLE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        includeQuote: true,
        excludeInfoTypes: true,
      };
    
      // Specify the action that is triggered when the job completes.
      const actions = [
        {
          pubSub: {
            topic: `projects/${projectId}/topics/${topicId}`,
          },
        },
      ];
    
      // Create the request for the job configured above.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: inspectConfig,
          storageConfig: storageItemConfig,
          actions: actions,
        },
      };
    
      // Use the client to send the request.
      const [topicResponse] = await pubsub.topic(topicId).get();
    
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
    
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        // Set up the timeout
        const timer = setTimeout(() => {
          reject(new Error('Timeout'));
        }, DLP_JOB_WAIT_TIME);
    
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            clearTimeout(timer);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          clearTimeout(timer);
          reject(err);
        };
    
        subscription.on('message', messageHandler);
        subscription.on('error', errorHandler);
      });
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    
    await inspectGcsFileSampling();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryOptions\SampleMethod;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect storage with sampling.
     * The following examples demonstrate using the Cloud DLP API to scan a 90% subset of a
     * Cloud Storage bucket for person names. The scan starts from a random location in the dataset
     * and only includes text files under 200 bytes.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $gcsUri            Google Cloud Storage file url.
     * @param string $topicId           The ID of the Pub/Sub topic to notify once the job completes.
     * @param string $subscriptionId    The ID of the Pub/Sub subscription to use when listening for job.
     */
    function inspect_gcs_with_sampling(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $gcsUri = 'gs://GOOGLE_STORAGE_BUCKET_NAME/dlp_sample.csv',
        string $topicId = 'dlp-pubsub-topic',
        string $subscriptionId = 'dlp_subcription'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // Construct the items to be inspected.
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet((new FileSet())
                ->setUrl($gcsUri))
            ->setBytesLimitPerFile(200)
            ->setFilesLimitPercent(90)
            ->setSampleMethod(SampleMethod::RANDOM_START);
    
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions($cloudStorageOptions);
    
        // Specify the type of info the inspection will look for.
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $emailAddressInfoType = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $cardNumberInfoType = (new InfoType())
            ->setName('CREDIT_CARD_NUMBER');
        $infoTypes = [$phoneNumberInfoType, $emailAddressInfoType, $cardNumberInfoType];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Construct the action to run when job completes.
        $action = (new Action())
            ->setPubSub((new PublishToPubSub())
                ->setTopic($topic->name()));
    
        // Construct inspect job config to run.
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes.
        // Consider using an asynchronous execution model such as Cloud Functions.
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (
                    isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()
                ) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while.
                }
            }
            printf('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds.
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout.
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_gcs_with_sampling(
        project: str,
        bucket: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str] = None,
        file_types: List[str] = None,
        min_likelihood: str = None,
        max_findings: int = None,
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze files in GCS by
        limiting the amount of data to be scanned.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bucket: The name of the GCS bucket containing the file, as a string.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing infoTypes to look for.
                A full list of info type categories can be fetched from the API.
            file_types: Type of files in gcs bucket where the inspection would happen.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Specify how the content should be inspected. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "exclude_info_types": True,
            "include_quote": True,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Setting default file types as CSV files
        if not file_types:
            file_types = ["CSV"]
    
        # Construct a cloud_storage_options dictionary with the bucket's URL.
        url = f"gs://{bucket}/*"
        storage_config = {
            "cloud_storage_options": {
                "file_set": {"url": url},
                "bytes_limit_per_file": 200,
                "file_types": file_types,
                "files_limit_percent": 90,
                "sample_method": "RANDOM_START",
            }
        }
    
        # Tell the API where to send a notification when the job is complete.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into full resource ids.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message):
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        print("Findings:")
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                f"Info type: {finding.info_type.name}; Count: {finding.count}"
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        # Register the callback and wait on the event.
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

### REST

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT-ID]/dlpJobs?key={YOUR_API_KEY}
    
    {
      "inspectJob":{
        "storageConfig":{
          "cloudStorageOptions":{
            "fileSet":{
              "url":"gs://[BUCKET-NAME]/*"
            },
            "bytesLimitPerFile":"200",
            "fileTypes":[
              "TEXT_FILE"
            ],
            "filesLimitPercent":90,
            "sampleMethod":"RANDOM_START"
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PERSON_NAME"
            }
          ],
          "excludeInfoTypes":true,
          "includeQuote":true,
          "minLikelihood":"POSSIBLE"
        },
        "actions":[
          {
            "saveFindings":{
              "outputConfig":{
                "table":{
                  "projectId":"[PROJECT-ID]",
                  "datasetId":"testingdlp"
                },
                "outputSchema":"BASIC_COLUMNS"
              }
            }
          }
        ]
      }
    }
    

After sending the JSON input in a POST request to the specified endpoint, a Sensitive Data Protection job is created, and the API sends the following response.

**JSON output:**
    
    
    {
      "name":"projects/[PROJECT-ID]/dlpJobs/[JOB-ID]",
      "type":"INSPECT_JOB",
      "state":"PENDING",
      "inspectDetails":{
        "requestedOptions":{
          "snapshotInspectTemplate":{
    
          },
          "jobConfig":{
            "storageConfig":{
              "cloudStorageOptions":{
                "fileSet":{
                  "url":"gs://[BUCKET_NAME]/*"
                },
                "bytesLimitPerFile":"200",
                "fileTypes":[
                  "TEXT_FILE"
                ],
                "sampleMethod":"TOP",
                "filesLimitPercent":90
              }
            },
            "inspectConfig":{
              "infoTypes":[
                {
                  "name":"PERSON_NAME"
                }
              ],
              "minLikelihood":"POSSIBLE",
              "limits":{
    
              },
              "includeQuote":true,
              "excludeInfoTypes":true
            },
            "actions":[
              {
                "saveFindings":{
                  "outputConfig":{
                    "table":{
                      "projectId":"[PROJECT-ID]",
                      "datasetId":"[DATASET-ID]",
                      "tableId":"[TABLE-ID]"
                    },
                    "outputSchema":"BASIC_COLUMNS"
                  }
                }
              }
            ]
          }
        }
      },
      "createTime":"2018-05-30T22:22:08.279Z"
    }
    

### Limit BigQuery scans

To enable sampling in BigQuery by limiting the amount of data that is scanned, specify the following optional fields within [`BigQueryOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions):

  * `rowsLimit`: The maximum number of rows to scan. If the table has more rows than this value, the rest of the rows are omitted. If not set, or if set to 0, all rows will be scanned.
  * `rowsLimitPercent`: The maximum percentage of rows to scan (between 0 and 100). The remaining rows are omitted. Setting this value to either 0 or 100 means no limit. It defaults to 0. Only one of `rowsLimit` and `rowsLimitPercent` can be specified.

**Caution:** A [known issue](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#bq-sampling) is causing the `rowsLimitPercent` field to behave unexpectedly. We recommend using `rowsLimit` instead.
  * `sampleMethod`: How to sample rows if not all rows are scanned. If not specified, scanning starts from the top. This field can be set to one of two values:

    * `TOP`: Scanning starts from the top.
    * `RANDOM_START`: Scanning starts from a randomly selected row.
  * `excludedFields`: Table fields that uniquely identify columns to exclude from being read. This can help reduce the amount of data scanned and bring down the overall cost of an inspection job.

  * `includedFields`: Table fields that uniquely identify specific rows within the table to scan.




Another feature that is useful for limiting the data being scanned, particularly when scanning partitioned tables, is [`TimespanConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#TimespanConfig). `TimespanConfig` allows you to filter out BigQuery table rows by providing start and end time values to define a timespan. Sensitive Data Protection then only scans rows that contain a timestamp within that timespan.

The following examples demonstrate using the DLP API to scan a 1000-row subset of a BigQuery table. The scan starts from a random row.

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectBigQueryTableWithSampling inspect bigQueries for sensitive data with sampling
    func inspectBigQueryTableWithSampling(w io.Writer, projectID, topicID, subscriptionID string) error {
    	// projectId := "your-project-id"
    	// topicID := "your-pubsub-topic-id"
    	// or provide a topicID name to create one
    	// subscriptionID := "your-pubsub-subscription-id"
    	// or provide a subscription name to create one
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.Close()
    
    	// Specify the BigQuery table to be inspected.
    	tableReference := &dlppb.BigQueryTable{
    		ProjectId: "bigquery-public-data",
    		DatasetId: "usa_names",
    		TableId:   "usa_1910_current",
    	}
    
    	bigQueryOptions := &dlppb.BigQueryOptions{
    		TableReference: tableReference,
    		RowsLimit:      int64(10000),
    		SampleMethod:   dlppb.[BigQueryOptions_RANDOM_START](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_BigQueryOptions_SAMPLE_METHOD_UNSPECIFIED_BigQueryOptions_TOP_BigQueryOptions_RANDOM_START),
    		IdentifyingFields: []*dlppb.FieldId{
    			{Name: "name"},
    		},
    	}
    
    	// Provide storage config with BigqueryOptions
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_BigQueryOptions{
    			BigQueryOptions: bigQueryOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PERSON_NAME"},
    	}
    
    	// Specify how the content should be inspected.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:    infoTypes,
    		IncludeQuote: true,
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(topicID)
    	if exists, err := t.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, topicID); err != nil {
    			return err
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(subscriptionID)
    	if exists, err := s.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, subscriptionID, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return err
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := fmt.Sprintf("projects/%s/topics/%s", projectID, topicID)
    
    	action := &dlppb.Action{
    		Action: &dlppb.Action_PubSub{
    			PubSub: &dlppb.Action_PublishToPubSub{
    				Topic: topic,
    			},
    		},
    	}
    
    	// Configure the long running job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Use the client to send the request.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Job Created: %v", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	c, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(c, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    	})
    	if err != nil {
    		return err
    	}
    
    	resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    		Name: j.GetName(),
    	})
    	if err != nil {
    		return err
    	}
    	r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    	if len(r) == 0 {
    		fmt.Fprintf(w, "No results")
    		return err
    	}
    	for _, s := range r {
    		fmt.Fprintf(w, "\nFound %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    	}
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html);
    import com.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html).SampleMethod;
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class InspectBigQueryTableWithSampling {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectBigQueryTableWithSampling(projectId, topicId, subscriptionId);
      }
    
      // Inspects a BigQuery Table
      public static void inspectBigQueryTableWithSampling(
          String projectId, String topicId, String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the BigQuery table to be inspected.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) tableReference =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId("bigquery-public-data")
                  .setDatasetId("usa_names")
                  .setTableId("usa_1910_current")
                  .build();
    
          [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html) bigQueryOptions =
              [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html).newBuilder()
                  .setTableReference(tableReference)
                  .[setRowsLimit](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.Builder.html#com_google_privacy_dlp_v2_BigQueryOptions_Builder_setRowsLimit_long_)(1000)
                  .setSampleMethod(SampleMethod.RANDOM_START)
                  .addIdentifyingFields([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("name"))
                  .build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setBigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setBigQueryOptions_com_google_privacy_dlp_v2_BigQueryOptions_)(bigQueryOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addInfoTypes(infoType).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    // DLP Job max time (in milliseconds)
    const DLP_JOB_WAIT_TIME = 15 * 1000 * 60;
    
    async function inspectBigqueryWithSampling() {
      // Specify the type of info the inspection will look for.
      // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
      const infoTypes = [{name: 'PERSON_NAME'}];
    
      // Specify the BigQuery options required for inspection.
      const storageItem = {
        bigQueryOptions: {
          tableReference: {
            projectId: dataProjectId,
            datasetId: datasetId,
            tableId: tableId,
          },
          rowsLimit: 1000,
          sampleMethod:
            DLP.protos.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigqueryoptions-class.html).SampleMethod
              .RANDOM_START,
          includedFields: [{name: 'name'}],
        },
      };
    
      // Specify the action that is triggered when the job completes.
      const actions = [
        {
          pubSub: {
            topic: `projects/${projectId}/topics/${topicId}`,
          },
        },
      ];
    
      // Construct request for creating an inspect job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: {
            infoTypes: infoTypes,
            includeQuote: true,
          },
          storageConfig: storageItem,
          actions: actions,
        },
      };
      // Use the client to send the request.
      const [topicResponse] = await pubsub.topic(topicId).get();
    
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
    
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
    
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        // Set up the timeout
        const timer = setTimeout(() => {
          reject(new Error('Timeout'));
        }, DLP_JOB_WAIT_TIME);
    
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            clearTimeout(timer);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          clearTimeout(timer);
          reject(err);
        };
    
        subscription.on('message', messageHandler);
        subscription.on('error', errorHandler);
      });
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    
    await inspectBigqueryWithSampling();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryOptions;
    use Google\Cloud\Dlp\V2\BigQueryOptions\SampleMethod;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect BigQuery for sensitive data with sampling.
     * The following examples demonstrate using the Cloud Data Loss Prevention
     * API to scan a 1000-row subset of a BigQuery table. The scan starts from
     * a random row.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $topicId           The Pub/Sub topic ID to notify once the job is completed.
     * @param string $subscriptionId    The Pub/Sub subscription ID to use when listening for job.
     * @param string $projectId         The Google Cloud Project ID.
     * @param string $datasetId         The BigQuery Dataset ID.
     * @param string $tableId           The BigQuery Table ID to be inspected.
     */
    function inspect_bigquery_with_sampling(
        string $callingProjectId,
        string $topicId,
        string $subscriptionId,
        string $projectId,
        string $datasetId,
        string $tableId
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // Specify the BigQuery table to be inspected.
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($projectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
    
        $bigQueryOptions = (new BigQueryOptions())
            ->setTableReference($bigqueryTable)
            ->setRowsLimit(1000)
            ->setSampleMethod(SampleMethod::RANDOM_START)
            ->setIdentifyingFields([
                (new FieldId())
                    ->setName('name')
            ]);
    
        $storageConfig = (new StorageConfig())
            ->setBigQueryOptions($bigQueryOptions);
    
        // Specify the type of info the inspection will look for.
        // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $infoTypes = [$personNameInfoType];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Specify the action that is triggered when the job completes.
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Configure the long running job we want the service to perform.
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (
                    isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()
                ) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while
                }
            }
            printf('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_bigquery_table_with_sampling(
        project: str,
        topic_id: str,
        subscription_id: str,
        min_likelihood: str = None,
        max_findings: str = None,
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze BigQuery data by limiting
        the amount of data to be scanned.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Specify how the content should be inspected. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": [{"name": "PERSON_NAME"}],
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
            "include_quote": True,
        }
    
        # Specify the BigQuery table to be inspected.
        # Here we are using public bigquery table.
        table_reference = {
            "project_id": "bigquery-public-data",
            "dataset_id": "usa_names",
            "table_id": "usa_1910_current",
        }
    
        # Construct a storage_config containing the target BigQuery info.
        storage_config = {
            "big_query_options": {
                "table_reference": table_reference,
                "rows_limit": 1000,
                "sample_method": "RANDOM_START",
                "identifying_fields": [{"name": "name"}],
            }
        }
    
        # Tell the API where to send a notification when the job is complete.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into full resource ids.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
    
                    if job.inspect_details.result.info_type_stats:
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                f"Info type: {finding.info_type.name}; Count: {finding.count}"
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
    
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        # Register the callback and wait on the event.
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectBigQueryWithSampling
    {
        public static async Task<DlpJob> InspectAsync(
            string projectId,
            int maxFindings,
            bool includeQuote,
            string topicId,
            string subId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible),
            IEnumerable<FieldId> identifyingFields = null,
            IEnumerable<InfoType> infoTypes = null)
        {
    
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct Storage config.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                BigQueryOptions = new [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.html)
                {
                    TableReference = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                    {
                        ProjectId = "bigquery-public-data",
                        DatasetId = "usa_names",
                        TableId = "usa_1910_current",
                    },
                    IdentifyingFields =
                    {
                        identifyingFields ?? new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "name" } }
                    },
                    RowsLimit = 100,
                    SampleMethod = [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.Types.html).[SampleMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.Types.SampleMethod.html).[RandomStart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.Types.SampleMethod.html#Google_Cloud_Dlp_V2_BigQueryOptions_Types_SampleMethod_RandomStart)
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } } },
                Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                {
                    MaxFindingsPerRequest = maxFindings,
                },
                IncludeQuote = includeQuote,
                MinLikelihood = minLikelihood
            };
    
            // Construct the pubsub action.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PubSub = new Action.Types.PublishToPubSub
                    {
                        Topic = $"projects/{projectId}/topics/{topicId}"
                    }
                }
            };
    
            // Construct the inspect job config using the actions.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Issue Create Dlp Job Request.
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
            };
    
            // We keep the name of the job that we just created.
            var dlpJob = dlp.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Listen to pub/sub for the job.
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(projectId, subId);
            var subscriber = await [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(
                subscriptionName);
    
            // SimpleSubscriber runs your message handle function on multiple threads to maximize throughput.
            await subscriber.StartAsync(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancel) =>
            {
                if (message.Attributes["DlpJobName"] == jobName)
                {
                    subscriber.StopAsync(cancel);
                    return Task.FromResult(SubscriberClient.Reply.Ack);
                }
                else
                {
                    return Task.FromResult(SubscriberClient.Reply.Nack);
                }
            });
    
            // Get the latest state of the job from the service.
            var resultJob = dlp.GetDlpJob(new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html#Google_Cloud_Dlp_V2_DlpJobName_Parse_System_String_)(jobName)
            });
    
            // Parse the response and process results.
            System.Console.WriteLine($"Job status: {resultJob.State}");
            System.Console.WriteLine($"Job Name: {resultJob.Name}");
            var result = resultJob.InspectDetails.Result;
            foreach (var infoType in result.[InfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeStats.html))
            {
                System.Console.WriteLine($"Info Type: {infoType.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name}");
                System.Console.WriteLine($"Count: {infoType.Count}");
            }
            return resultJob;
        }
    }
    

### REST

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT-ID]/dlpJobs?key={YOUR_API_KEY}
    
    {
      "inspectJob":{
        "storageConfig":{
          "bigQueryOptions":{
            "tableReference":{
              "projectId":"bigquery-public-data",
              "datasetId":"usa_names",
              "tableId":"usa_1910_current"
            },
            "rowsLimit":"1000",
            "sampleMethod":"RANDOM_START",
            "includedFields":[
              {
                "name":"name"
              }
            ]
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"FIRST_NAME"
            }
          ],
          "includeQuote":true
        },
        "actions":[
          {
            "saveFindings":{
              "outputConfig":{
                "table":{
                  "projectId":"[PROJECT-ID]",
                  "datasetId":"testingdlp",
                  "tableId":"bqsample3"
                },
                "outputSchema":"BASIC_COLUMNS"
              }
            }
          }
        ]
      }
    }
    

After sending the JSON input in a POST request to the specified endpoint, a Sensitive Data Protection job is created, and the API sends the following response.

**JSON output:**
    
    
    {
      "name": "projects/[PROJECT-ID]/dlpJobs/[JOB-ID]",
      "type": "INSPECT_JOB",
      "state": "PENDING",
      "inspectDetails": {
        "requestedOptions": {
          "snapshotInspectTemplate": {},
          "jobConfig": {
            "storageConfig": {
              "bigQueryOptions": {
                "tableReference": {
                  "projectId": "bigquery-public-data",
                  "datasetId": "usa_names",
                  "tableId": "usa_1910_current"
                },
                "rowsLimit": "1000",
                "sampleMethod": "RANDOM_START",
                "includedFields": [
                  {
                    "name": "name"
                  }
                ]
              }
            },
            "inspectConfig": {
              "infoTypes": [
                {
                  "name": "FIRST_NAME"
                }
              ],
              "limits": {},
              "includeQuote": true
            },
            "actions": [
              {
                "saveFindings": {
                  "outputConfig": {
                    "table": {
                      "projectId": "[PROJECT-ID]",
                      "datasetId": "[DATASET-ID]",
                      "tableId": "bqsample"
                    },
                    "outputSchema": "BASIC_COLUMNS"
                  }
                }
              }
            ]
          }
        },
        "result": {}
      },
      "createTime": "2022-11-04T18:53:48.350Z"
    }
    

When the inspect job finishes running and its results have been processed by BigQuery, the results of the scan are available in the specified BigQuery output table. For more information about retrieving inspection results, see [the next section](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#retrieving-inspection-results).

## Retrieve inspection results

**Note:** This section describes how to view inspection results using the DLP API. To view results using Sensitive Data Protection in the Google Cloud console, click the **Jobs & job triggers** tab, click the **All jobs** tab, and then click the job you want to view results for.

You can retrieve a summary of a [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) using the [`projects.dlpJobs.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get) method. The returned `DlpJob` includes its [`InspectDataSourceDetails`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#inspectdatasourcedetails) object, which contains both a summary of the job's configuration ([`RequestedOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#requestedoptions)) and a summary of the outcome of the job ([`Result`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#result)). The outcome summary includes:

  * `processedBytes`: The total size in bytes that have been processed.
  * `totalEstimatedBytes`: Estimate of the number of bytes remaining to process.
  * [`InfoTypeStatistics`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.InfoTypeStats) object: Statistics of how many instances of each infoType were found during the inspection job.



For complete inspection job results, you have several options. Depending on the [`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#Action) you've chosen, inspection jobs are:

  * Saved to BigQuery (the [`SaveFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#SaveFindings) object) in the table specified. Before viewing or analyzing the results, first ensure that the job has completed by using the [`projects.dlpJobs.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get) method, which is described below. Note that you can specify a schema for storing findings using the [`OutputSchema`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#OutputSchema) object.
  * Published to a [Pub/Sub](https://docs.cloud.google.com/pubsub) topic (the [`PublishToPubSub`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PublishToPubSub) object). The topic must have given publishing access rights to Sensitive Data Protection service account that runs the [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) sending the notifications.
  * Published to [Security Command Center](https://docs.cloud.google.com/security-command-center).
  * Published to [Cloud Monitoring](https://docs.cloud.google.com/stackdriver).



To help sift through large amounts of data generated by Sensitive Data Protection, you can use built-in BigQuery tools to run rich SQL analytics or tools such as Data Studio to generate reports. For more information, see [Analyzing and reporting on Sensitive Data Protection findings](https://docs.cloud.google.com/sensitive-data-protection/docs/analyzing-and-reporting). For some sample queries, see [Querying findings in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings).

Sending a storage repository inspection request to Sensitive Data Protection creates and runs a [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) object instance in response. These jobs can take seconds, minutes, or hours to run depending on the size of your data and the configuration that you have specified. Choosing to publish to a Pub/Sub topic (by specifying [`PublishToPubSub`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PublishToPubSub) in [`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#Action)) automatically sends notifications to the topic with the specified name when the job's status changes. The name of the Pub/Sub topic is specified in the form `projects/[PROJECT-ID]/topics/[PUBSUB-TOPIC-NAME]`.

**Note:** For more information about how to create a Pub/Sub function, see [Pub/Sub tutorial](https://docs.cloud.google.com/functions/docs/tutorials/pubsub).

You have full control over the jobs you create, including the following management methods:

  * [`projects.dlpJobs.cancel`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/cancel) method: Stops a job that is currently in progress. The server makes a best effort to cancel the job, but success is not guaranteed. The job and its configuration will remain until you delete it (with .
  * [`projects.dlpJobs.delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/delete) method: Deletes a job and its configuration.
  * [`projects.dlpJobs.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get) method: Retrieves a single job and returns its status, its configuration, and, if the job is done, summary results.
  * [`projects.dlpJobs.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list) method: Retrieves a list of all jobs, and includes the ability to filter results.



## Next steps

  * Learn more about creating storage inspection jobs, see [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).
  * Learn more about [creating a de-identified copy of data in storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage).
  * Learn more about supported file types when inspecting Cloud Storage buckets, see [Supported file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
