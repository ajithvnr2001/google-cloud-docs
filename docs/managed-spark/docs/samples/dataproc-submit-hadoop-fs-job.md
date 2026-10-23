---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-submit-hadoop-fs-job/
title: Submit hadoop fs job \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:17.054944+00:00
---

# Submit hadoop fs job  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-submit-hadoop-fs-job/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Submit hadoop fs job Stay organized with collections  Save and categorize content based on your preferences. 

Submits a Hadoop FS job to a Dataproc cluster.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dataproc.v1.[HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html);
    import com.google.cloud.dataproc.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html);
    import com.google.cloud.dataproc.v1.[JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html);
    import com.google.cloud.dataproc.v1.[JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html);
    import com.google.cloud.dataproc.v1.[JobMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobMetadata.html);
    import com.google.cloud.dataproc.v1.[JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.concurrent.ExecutionException;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class SubmitHadoopFsJob {
    
      public static ArrayList<String> stringToList(String s) {
        return new ArrayList<>(Arrays.asList(s.split(" ")));
      }
    
      public static void submitHadoopFsJob() throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String region = "your-project-region";
        String clusterName = "your-cluster-name";
        String hadoopFsQuery = "your-hadoop-fs-query";
        submitHadoopFsJob(projectId, region, clusterName, hadoopFsQuery);
      }
    
      public static void submitHadoopFsJob(
          String projectId, String region, String clusterName, String hadoopFsQuery)
          throws IOException, InterruptedException {
        String myEndpoint = String.format("%s-dataproc.googleapis.com:443", region);
    
        // Configure the settings for the job controller client.
        [JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html) jobControllerSettings =
            [JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Create a job controller client with the configured settings. Using a try-with-resources
        // closes the client,
        // but this can also be done manually with the .close() method.
        try ([JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html) jobControllerClient =
            [JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html).create(jobControllerSettings)) {
    
          // Configure cluster placement for the job.
          [JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html) jobPlacement = [JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html).newBuilder().setClusterName(clusterName).build();
    
          // Configure Hadoop job settings. The HadoopFS query is set here.
          [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html) hadoopJob =
              [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html).newBuilder()
                  .setMainClass("org.apache.hadoop.fs.FsShell")
                  .addAllArgs(stringToList(hadoopFsQuery))
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html) job = [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html).newBuilder().setPlacement(jobPlacement).setHadoopJob(hadoopJob).build();
    
          // Submit an asynchronous request to execute the job.
          OperationFuture<Job, JobMetadata> submitJobAsOperationAsyncRequest =
              jobControllerClient.[submitJobAsOperationAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html#com_google_cloud_dataproc_v1_JobControllerClient_submitJobAsOperationAsync_com_google_cloud_dataproc_v1_SubmitJobRequest_)(projectId, region, job);
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html) response = submitJobAsOperationAsyncRequest.get();
    
          // Print output from Google Cloud Storage.
          Matcher matches =
              Pattern.compile("gs://(.*?)/(.*)").matcher(response.[getDriverOutputResourceUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html#com_google_cloud_dataproc_v1_Job_getDriverOutputResourceUri__)());
          matches.matches();
    
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(matches.group(1), String.format("%s.000000000", matches.group(2)));
    
          System.out.println(
              String.format("Job finished successfully: %s", new String(blob.[getContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_getContent_com_google_cloud_storage_Blob_BlobSourceOption____)())));
    
        } catch (ExecutionException e) {
          // If the job does not complete successfully, print the error message.
          System.err.println(String.format("submitHadoopFSJob: %s ", e.getMessage()));
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
