---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-submit-job/
title: Submit job \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:02.639520+00:00
---

# Submit job  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-submit-job/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Submit job Stay organized with collections  Save and categorize content based on your preferences. 

Submits a Spark job to a Dataproc cluster.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job)
  * [Use the Cloud Client Libraries for Python](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-library-example)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataproc/apiv1?tab=doc). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"regexp"
    
    	dataproc "cloud.google.com/go/dataproc/apiv1"
    	"cloud.google.com/go/dataproc/apiv1/dataprocpb"
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/option"
    )
    
    func submitJob(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, region, clusterName string) error {
    	// projectID := "your-project-id"
    	// region := "us-central1"
    	// clusterName := "your-cluster"
    	ctx := context.Background()
    
    	// Create the job client.
    	endpoint := fmt.Sprintf("%s-dataproc.googleapis.com:443", region)
    	jobClient, err := dataproc.NewJobControllerClient(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		log.Fatalf("error creating the job client: %s\n", err)
    	}
    
    	// Create the job config.
    	submitJobReq := &dataprocpb.SubmitJobRequest{
    		ProjectId: projectID,
    		Region:    region,
    		Job: &dataprocpb.Job{
    			Placement: &dataprocpb.JobPlacement{
    				ClusterName: clusterName,
    			},
    			TypeJob: &dataprocpb.Job_SparkJob{
    				SparkJob: &dataprocpb.SparkJob{
    					Driver: &dataprocpb.SparkJob_MainClass{
    						MainClass: "org.apache.spark.examples.SparkPi",
    					},
    					JarFileUris: []string{"file:///usr/lib/spark/examples/jars/spark-examples.jar"},
    					Args:        []string{"1000"},
    				},
    			},
    		},
    	}
    
    	submitJobOp, err := jobClient.SubmitJobAsOperation(ctx, submitJobReq)
    	if err != nil {
    		return fmt.Errorf("error with request to submitting job: %w", err)
    	}
    
    	submitJobResp, err := submitJobOp.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("error submitting job: %w", err)
    	}
    
    	re := regexp.MustCompile("gs://(.+?)/(.+)")
    	matches := re.FindStringSubmatch(submitJobResp.DriverOutputResourceUri)
    
    	if len(matches) < 3 {
    		return fmt.Errorf("regex error: %s", submitJobResp.DriverOutputResourceUri)
    	}
    
    	// Dataproc job output gets saved to a GCS bucket allocated to it.
    	storageClient, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("error creating storage client: %w", err)
    	}
    
    	obj := fmt.Sprintf("%s.000000000", matches[2])
    	reader, err := storageClient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(matches[1]).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(obj).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return fmt.Errorf("error reading job output: %w", err)
    	}
    
    	defer reader.Close()
    
    	body, err := io.ReadAll(reader)
    	if err != nil {
    		return fmt.Errorf("could not read output from Dataproc Job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job finished successfully: %s", body)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dataproc.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html);
    import com.google.cloud.dataproc.v1.[JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html);
    import com.google.cloud.dataproc.v1.[JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html);
    import com.google.cloud.dataproc.v1.[JobMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobMetadata.html);
    import com.google.cloud.dataproc.v1.[JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html);
    import com.google.cloud.dataproc.v1.[SparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.SparkJob.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class SubmitJob {
    
      public static void submitJob() throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String region = "your-project-region";
        String clusterName = "your-cluster-name";
        submitJob(projectId, region, clusterName);
      }
    
      public static void submitJob(String projectId, String region, String clusterName)
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
    
          // Configure Spark job settings.
          [SparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.SparkJob.html) sparkJob =
              [SparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.SparkJob.html).newBuilder()
                  .setMainClass("org.apache.spark.examples.SparkPi")
                  .addJarFileUris("file:///usr/lib/spark/examples/jars/spark-examples.jar")
                  .addArgs("1000")
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html) job = [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html).newBuilder().setPlacement(jobPlacement).setSparkJob(sparkJob).build();
    
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
          System.err.println(String.format("submitJob: %s ", e.getMessage()));
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const dataproc = require('[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)');
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // TODO(developer): Uncomment and set the following variables
    // projectId = 'YOUR_PROJECT_ID'
    // region = 'YOUR_CLUSTER_REGION'
    // clusterName = 'YOUR_CLUSTER_NAME'
    
    // Create a client with the endpoint set to the desired cluster region
    const jobClient = new dataproc.v1.[JobControllerClient](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)({
      apiEndpoint: `${region}-dataproc.googleapis.com`,
      projectId: projectId,
    });
    
    async function submitJob() {
      const job = {
        projectId: projectId,
        region: region,
        job: {
          placement: {
            clusterName: clusterName,
          },
          sparkJob: {
            mainClass: 'org.apache.spark.examples.SparkPi',
            jarFileUris: [
              'file:///usr/lib/spark/examples/jars/spark-examples.jar',
            ],
            args: ['1000'],
          },
        },
      };
    
      const [jobOperation] = await jobClient.submitJobAsOperation(job);
      const [jobResponse] = await jobOperation.promise();
    
      const matches =
        jobResponse.driverOutputResourceUri.match('gs://(.*?)/(.*)');
    
      const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
      const output = await storage
        .bucket(matches[1])
        .file(`${matches[2]}.000000000`)
        .[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)();
    
      // Output a success message.
      console.log(`Job finished successfully: ${output}`);

### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Create the job client.
    job_client = dataproc_v1.JobControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )
    
    # Create the job config.
    job = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {"main_python_file_uri": f"gs://{gcs_bucket}/{spark_filename}"},
    }
    
    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job}
    )
    response = operation.result()
    
    # Dataproc job output is saved to the Cloud Storage bucket
    # allocated to the job. Use regex to obtain the bucket and blob info.
    matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)
    
    output = (
        storage.Client()
        .get_bucket(matches.group(1))
        .blob(f"{matches.group(2)}.000000000")
        .download_as_bytes()
        .decode("utf-8")
    )
    
    print(f"Job finished successfully: {output}\r\n")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
