---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-quickstart/
title: Quickstart \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:35.918639+00:00
---

# Quickstart  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-quickstart/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

End-to-end workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Create a cluster by using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataproc/apiv1?tab=doc). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // This quickstart shows how you can use the Dataproc Client library to create a
    // Dataproc cluster, submit a PySpark job to the cluster, wait for the job to finish
    // and finally delete the cluster.
    //
    // Usage:
    //
    //	go build
    //	./quickstart --project_id <PROJECT_ID> --region <REGION> \
    //	    --cluster_name <CLUSTER_NAME> --job_file_path <GCS_JOB_FILE_PATH>
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"io"
    	"log"
    	"regexp"
    
    	dataproc "cloud.google.com/go/dataproc/apiv1"
    	"cloud.google.com/go/dataproc/apiv1/dataprocpb"
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/option"
    )
    
    func main() {
    	var projectID, clusterName, region, jobFilePath string
    	flag.StringVar(&projectID, "project_id", "", "Cloud Project ID, used for creating resources.")
    	flag.StringVar(&region, "region", "", "Region that resources should be created in.")
    	flag.StringVar(&clusterName, "cluster_name", "", "Name of Cloud Dataproc cluster to create.")
    	flag.StringVar(&jobFilePath, "job_file_path", "", "Path to job file in GCS.")
    	flag.Parse()
    
    	ctx := context.Background()
    
    	// Create the cluster client.
    	endpoint := fmt.Sprintf("%s-dataproc.googleapis.com:443", region)
    	clusterClient, err := dataproc.NewClusterControllerClient(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		log.Fatalf("error creating the cluster client: %s\n", err)
    	}
    
    	// Create the cluster config.
    	createReq := &dataprocpb.CreateClusterRequest{
    		ProjectId: projectID,
    		Region:    region,
    		Cluster: &dataprocpb.Cluster{
    			ProjectId:   projectID,
    			ClusterName: clusterName,
    			Config: &dataprocpb.ClusterConfig{
    				MasterConfig: &dataprocpb.InstanceGroupConfig{
    					NumInstances:   1,
    					MachineTypeUri: "n1-standard-2",
    				},
    				WorkerConfig: &dataprocpb.InstanceGroupConfig{
    					NumInstances:   2,
    					MachineTypeUri: "n1-standard-2",
    				},
    			},
    		},
    	}
    
    	// Create the cluster.
    	createOp, err := clusterClient.CreateCluster(ctx, createReq)
    	if err != nil {
    		log.Fatalf("error submitting the cluster creation request: %v\n", err)
    	}
    
    	createResp, err := createOp.Wait(ctx)
    	if err != nil {
    		log.Fatalf("error creating the cluster: %v\n", err)
    	}
    
    	// Defer cluster deletion.
    	defer func() {
    		dReq := &dataprocpb.DeleteClusterRequest{
    			ProjectId:   projectID,
    			Region:      region,
    			ClusterName: clusterName,
    		}
    		deleteOp, err := clusterClient.DeleteCluster(ctx, dReq)
    		deleteOp.Wait(ctx)
    		if err != nil {
    			fmt.Printf("error deleting cluster %q: %v\n", clusterName, err)
    			return
    		}
    		fmt.Printf("Cluster %q successfully deleted\n", clusterName)
    	}()
    
    	// Output a success message.
    	fmt.Printf("Cluster created successfully: %q\n", createResp.ClusterName)
    
    	// Create the job client.
    	jobClient, err := dataproc.NewJobControllerClient(ctx, option.WithEndpoint(endpoint))
    
    	// Create the job config.
    	submitJobReq := &dataprocpb.SubmitJobRequest{
    		ProjectId: projectID,
    		Region:    region,
    		Job: &dataprocpb.Job{
    			Placement: &dataprocpb.JobPlacement{
    				ClusterName: clusterName,
    			},
    			TypeJob: &dataprocpb.Job_PysparkJob{
    				PysparkJob: &dataprocpb.PySparkJob{
    					MainPythonFileUri: jobFilePath,
    				},
    			},
    		},
    	}
    
    	submitJobOp, err := jobClient.SubmitJobAsOperation(ctx, submitJobReq)
    	if err != nil {
    		fmt.Printf("error with request to submitting job: %v\n", err)
    		return
    	}
    
    	submitJobResp, err := submitJobOp.Wait(ctx)
    	if err != nil {
    		fmt.Printf("error submitting job: %v\n", err)
    		return
    	}
    
    	re := regexp.MustCompile("gs://(.+?)/(.+)")
    	matches := re.FindStringSubmatch(submitJobResp.DriverOutputResourceUri)
    
    	if len(matches) < 3 {
    		fmt.Printf("regex error: %s\n", submitJobResp.DriverOutputResourceUri)
    		return
    	}
    
    	// Dataproc job outget gets saved to a GCS bucket allocated to it.
    	storageClient, err := storage.NewClient(ctx)
    	if err != nil {
    		fmt.Printf("error creating storage client: %v\n", err)
    		return
    	}
    
    	obj := fmt.Sprintf("%s.000000000", matches[2])
    	reader, err := storageClient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(matches[1]).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(obj).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		fmt.Printf("error reading job output: %v\n", err)
    		return
    	}
    
    	defer reader.Close()
    
    	body, err := io.ReadAll(reader)
    	if err != nil {
    		fmt.Printf("could not read output from Dataproc Job: %v\n", err)
    		return
    	}
    
    	fmt.Printf("Job finished successfully: %s", body)
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /* This quickstart sample walks a user through creating a Cloud Dataproc
     * cluster, submitting a PySpark job from Google Cloud Storage to the
     * cluster, reading the output of the job and deleting the cluster, all
     * using the Java client library.
     *
     * Usage:
     *     mvn clean package -DskipTests
     *
     *     mvn exec:java -Dexec.args="<PROJECT_ID> <REGION> <CLUSTER_NAME> <GCS_JOB_FILE_PATH>"
     *
     *     You can also set these arguments in the main function instead of providing them via the CLI.
     */
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dataproc.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html);
    import com.google.cloud.dataproc.v1.[ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html);
    import com.google.cloud.dataproc.v1.[ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html);
    import com.google.cloud.dataproc.v1.[ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html);
    import com.google.cloud.dataproc.v1.[ClusterOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterOperationMetadata.html);
    import com.google.cloud.dataproc.v1.[InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html);
    import com.google.cloud.dataproc.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html);
    import com.google.cloud.dataproc.v1.[JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html);
    import com.google.cloud.dataproc.v1.[JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html);
    import com.google.cloud.dataproc.v1.[JobMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobMetadata.html);
    import com.google.cloud.dataproc.v1.[JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html);
    import com.google.cloud.dataproc.v1.[PySparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.PySparkJob.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class Quickstart {
    
      public static void quickstart(
          String projectId, String region, String clusterName, String jobFilePath)
          throws IOException, InterruptedException {
        String myEndpoint = String.format("%s-dataproc.googleapis.com:443", region);
    
        // Configure the settings for the cluster controller client.
        [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) clusterControllerSettings =
            [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Configure the settings for the job controller client.
        [JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html) jobControllerSettings =
            [JobControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Create both a cluster controller client and job controller client with the
        // configured settings. The client only needs to be created once and can be reused for
        // multiple requests. Using a try-with-resources closes the client, but this can also be done
        // manually with the .close() method.
        try ([ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) clusterControllerClient =
                [ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html).create(clusterControllerSettings);
            [JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html) jobControllerClient =
                [JobControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html).create(jobControllerSettings)) {
          // Configure the settings for our cluster.
          [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) masterConfig =
              [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                  .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                  .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(1)
                  .build();
          [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) workerConfig =
              [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                  .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                  .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(2)
                  .build();
          [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) clusterConfig =
              [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html).newBuilder()
                  .[setMasterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setMasterConfig_com_google_cloud_dataproc_v1_InstanceGroupConfig_)(masterConfig)
                  .setWorkerConfig(workerConfig)
                  .build();
          // Create the cluster object with the desired cluster config.
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) cluster =
              [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html).newBuilder().setClusterName(clusterName).setConfig(clusterConfig).build();
    
          // Create the Cloud Dataproc cluster.
          OperationFuture<Cluster, ClusterOperationMetadata> createClusterAsyncRequest =
              clusterControllerClient.[createClusterAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html#com_google_cloud_dataproc_v1_ClusterControllerClient_createClusterAsync_com_google_cloud_dataproc_v1_CreateClusterRequest_)(projectId, region, cluster);
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) clusterResponse = createClusterAsyncRequest.get();
          System.out.println(
              String.format("Cluster created successfully: %s", clusterResponse.[getClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html#com_google_cloud_dataproc_v1_Cluster_getClusterName__)()));
    
          // Configure the settings for our job.
          [JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html) jobPlacement = [JobPlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobPlacement.html).newBuilder().setClusterName(clusterName).build();
          [PySparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.PySparkJob.html) pySparkJob = [PySparkJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.PySparkJob.html).newBuilder().setMainPythonFileUri(jobFilePath).build();
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html) job = [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html).newBuilder().setPlacement(jobPlacement).setPysparkJob(pySparkJob).build();
    
          // Submit an asynchronous request to execute the job.
          OperationFuture<Job, JobMetadata> submitJobAsOperationAsyncRequest =
              jobControllerClient.[submitJobAsOperationAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html#com_google_cloud_dataproc_v1_JobControllerClient_submitJobAsOperationAsync_com_google_cloud_dataproc_v1_SubmitJobRequest_)(projectId, region, job);
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job.html) jobResponse = submitJobAsOperationAsyncRequest.get();
    
          // Print output from Google Cloud Storage.
          Matcher matches =
              Pattern.compile("gs://(.*?)/(.*)").matcher(jobResponse.[getDriverOutputResourceUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html#com_google_cloud_dataproc_v1_Job_getDriverOutputResourceUri__)());
          matches.matches();
    
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance().getService();
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(matches.group(1), String.format("%s.000000000", matches.group(2)));
    
          System.out.println(
              String.format("Job finished successfully: %s", new String(blob.[getContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_getContent_com_google_cloud_storage_Blob_BlobSourceOption____)())));
    
          // Delete the cluster.
          OperationFuture<Empty, ClusterOperationMetadata> deleteClusterAsyncRequest =
              clusterControllerClient.[deleteClusterAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html#com_google_cloud_dataproc_v1_ClusterControllerClient_deleteClusterAsync_com_google_cloud_dataproc_v1_DeleteClusterRequest_)(projectId, region, clusterName);
          deleteClusterAsyncRequest.get();
          System.out.println(String.format("Cluster \"%s\" successfully deleted.", clusterName));
    
        } catch (ExecutionException e) {
          System.err.println(String.format("quickstart: %s ", e.getMessage()));
        }
      }
    
      public static void main(String... args) throws IOException, InterruptedException {
        if (args.length != 4) {
          System.err.println(
              "Insufficient number of parameters provided. Please make sure a "
                  + "PROJECT_ID, REGION, CLUSTER_NAME and JOB_FILE_PATH are provided, in this order.");
          return;
        }
    
        String projectId = args[0]; // project-id of project to create the cluster in
        String region = args[1]; // region to create the cluster
        String clusterName = args[2]; // name of the cluster
        String jobFilePath = args[3]; // location in GCS of the PySpark job
    
        quickstart(projectId, region, clusterName, jobFilePath);
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // This quickstart sample walks a user through creating a Dataproc
    // cluster, submitting a PySpark job from Google Cloud Storage to the
    // cluster, reading the output of the job and deleting the cluster, all
    // using the Node.js client library.
    
    'use strict';
    
    function main(projectId, region, clusterName, jobFilePath) {
      const dataproc = require('[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)');
      const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
      // Create a cluster client with the endpoint set to the desired cluster region
      const clusterClient = new dataproc.v1.[ClusterControllerClient](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)({
        apiEndpoint: `${region}-dataproc.googleapis.com`,
        projectId: projectId,
      });
    
      // Create a job client with the endpoint set to the desired cluster region
      const jobClient = new dataproc.v1.[JobControllerClient](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)({
        apiEndpoint: `${region}-dataproc.googleapis.com`,
        projectId: projectId,
      });
    
      async function quickstart() {
        // Create the cluster config
        const cluster = {
          projectId: projectId,
          region: region,
          cluster: {
            clusterName: clusterName,
            config: {
              masterConfig: {
                numInstances: 1,
                machineTypeUri: 'n1-standard-2',
              },
              workerConfig: {
                numInstances: 2,
                machineTypeUri: 'n1-standard-2',
              },
            },
          },
        };
    
        // Create the cluster
        const [operation] = await clusterClient.createCluster(cluster);
        const [response] = await operation.promise();
    
        // Output a success message
        console.log(`Cluster created successfully: ${response.clusterName}`);
    
        const job = {
          projectId: projectId,
          region: region,
          job: {
            placement: {
              clusterName: clusterName,
            },
            pysparkJob: {
              mainPythonFileUri: jobFilePath,
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
    
        // Delete the cluster once the job has terminated.
        const deleteClusterReq = {
          projectId: projectId,
          region: region,
          clusterName: clusterName,
        };
    
        const [deleteOperation] =
          await clusterClient.deleteCluster(deleteClusterReq);
        await deleteOperation.promise();
    
        // Output a success message
        console.log(`Cluster ${clusterName} successfully deleted.`);
      }
    
      quickstart();
    }
    
    const args = process.argv.slice(2);
    
    if (args.length !== 4) {
      console.log(
        'Insufficient number of parameters provided. Please make sure a ' +
          'PROJECT_ID, REGION, CLUSTER_NAME and JOB_FILE_PATH are provided, in this order.'
      );
    }
    
    main(...args);

### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """
    Command-line program to create a Dataproc cluster,
    run a PySpark job located in Cloud Storage on the cluster,
    then delete the cluster after the job completes.
    
    Usage:
        python submit_job_to_cluster --project_id <PROJECT_ID> --region <REGION> \
            --cluster_name <CLUSTER_NAME> --job_file_path <GCS_JOB_FILE_PATH>
    """
    
    import argparse
    import os
    import re
    
    from google.cloud import [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest)
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    DEFAULT_FILENAME = "pyspark_sort.py"
    waiting_callback = False
    
    
    def get_pyspark_file(pyspark_file=None):
        if pyspark_file:
            f = open(pyspark_file, "rb")
            return f, os.path.basename(pyspark_file)
        else:
            """Gets the PySpark file from current directory."""
            current_dir = os.path.dirname(os.path.abspath(__file__))
            f = open(os.path.join(current_dir, DEFAULT_FILENAME), "rb")
            return f, DEFAULT_FILENAME
    
    
    def get_region_from_zone(zone):
        try:
            region_as_list = zone.split("-")[:-1]
            return "-".join(region_as_list)
        except (AttributeError, IndexError, ValueError):
            raise ValueError("Invalid zone provided, please check your input.")
    
    
    def upload_pyspark_file(project, bucket_name, filename, spark_file):
        """Uploads the PySpark file in this directory to the configured input
        bucket."""
        print("Uploading pyspark file to Cloud Storage.")
        client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project)
        bucket = client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        blob = bucket.blob(filename)
        blob.[upload_from_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_file)(spark_file)
    
    
    def download_output(project, cluster_id, output_bucket, job_id):
        """Downloads the output file from Cloud Storage and returns it as a
        string."""
        print("Downloading output file.")
        client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project)
        bucket = client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(output_bucket)
        output_blob = (
            "google-cloud-dataproc-metainfo/{}/jobs/{}/driveroutput.000000000".format(
                cluster_id, job_id
            )
        )
        return bucket.blob(output_blob).[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)().decode("utf-8")
    
    
    def quickstart(project_id, region, cluster_name, gcs_bucket, pyspark_file):
        # Create the cluster client.
        cluster_client = [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest).[ClusterControllerClient](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html)(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
        )
    
        # Create the cluster config.
        cluster = {
            "project_id": project_id,
            "cluster_name": cluster_name,
            "config": {
                "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
                "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
            },
        }
    
        # Create the cluster.
        operation = cluster_client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html#google_cloud_dataproc_v1_services_cluster_controller_ClusterControllerClient_create_cluster)(
            request={"project_id": project_id, "region": region, "cluster": cluster}
        )
        result = operation.result()
    
        print(f"Cluster created successfully: {result.cluster_name}")
    
    
        spark_file, spark_filename = get_pyspark_file(pyspark_file)
        upload_pyspark_file(project_id, gcs_bucket, spark_filename, spark_file)
    
        # Create the job client.
        job_client = [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest).[JobControllerClient](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.job_controller.JobControllerClient.html)(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
        )
    
        # Create the job config.
        job = {
            "placement": {"cluster_name": cluster_name},
            "pyspark_job": {"main_python_file_uri": f"gs://{gcs_bucket}/{spark_filename}"},
        }
    
        operation = job_client.[submit_job_as_operation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.job_controller.JobControllerClient.html#google_cloud_dataproc_v1_services_job_controller_JobControllerClient_submit_job_as_operation)(
            request={"project_id": project_id, "region": region, "job": job}
        )
        response = operation.result()
    
        # Dataproc job output is saved to the Cloud Storage bucket
        # allocated to the job. Use regex to obtain the bucket and blob info.
        matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)
    
        output = (
            [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
            .[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(matches.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1))
            .blob(f"{matches.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(2)}.000000000")
            .[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
            .decode("utf-8")
        )
    
        print(f"Job finished successfully: {output}\r\n")
    
        # Delete the cluster once the job has terminated.
        operation = cluster_client.[delete_cluster](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html#google_cloud_dataproc_v1_services_cluster_controller_ClusterControllerClient_delete_cluster)(
            request={
                "project_id": project_id,
                "region": region,
                "cluster_name": cluster_name,
            }
        )
        operation.result()
    
        print(f"Cluster {cluster_name} successfully deleted.")
    
    
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        parser.add_argument(
            "--project_id",
            type=str,
            required=True,
            help="Project to use for creating resources.",
        )
        parser.add_argument(
            "--region",
            type=str,
            required=True,
            help="Region where the resources should live.",
        )
        parser.add_argument(
            "--cluster_name",
            type=str,
            required=True,
            help="Name to use for creating a cluster.",
        )
    
        parser.add_argument(
            "--gcs_bucket", help="Bucket to upload Pyspark file to", required=True
        )
    
        parser.add_argument(
            "--pyspark_file", help="Pyspark filename. Defaults to pyspark_sort.py"
        )
    
        args = parser.parse_args()
        quickstart(
            args.project_id,
            args.region,
            args.cluster_name,
            args.gcs_bucket,
            args.pyspark_file,
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
