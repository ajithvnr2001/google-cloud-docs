---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries/
title: Quickstart: Create a cluster by using client libraries \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:21.131896+00:00
---

# Quickstart: Create a cluster by using client libraries  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster by using client libraries

The sample code listed, below, shows you how to use the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google_cloud_client_libraries) to create a Managed Service for Apache Spark cluster, run a job on the cluster, then delete the cluster.

You can also perform these tasks using:

  * API REST requests in [Quickstarts Using the API Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template)
  * the Google Cloud console in [Create a cluster by using the Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console)
  * the Google Cloud CLI in [Create a cluster by using the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud)



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc&redirect=https%3A//console.cloud.google.com)




## Run the Code

**Try the walkthrough:** Click **Open in Cloud Shell** to run a Python Cloud Client Libraries walkthrough that creates a cluster, runs a PySpark job, then deletes the cluster.

[ Open in Cloud Shell ](https://ssh.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/googleapis/python-dataproc&cloudshell_working_dir=samples/snippets&tutorial=python-api-walkthrough.md&cloudshell_open_in_editor=submit_job_to_cluster.py)

### Go

  1. [Install the client library](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library) For more information, See [Setting up your development environment](https://docs.cloud.google.com/go/docs/setup).
  2. [Set up authentication](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Clone and run the sample GitHub code. **Selecting a PySpark input file:** The Google Client Library code samples, below, run a PySpark job that you specify as an input parameter. You can pass in the simple "Hello World" PySpark app located in Cloud Storage at `gs://dataproc-examples/pyspark/hello-world/hello-world.py` or your own PySpark app. See [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to learn more about uploading files to Cloud Storage. 
         
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

  1. [Install the client library](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library) For more information, See [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).
  2. [Set up authentication](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Clone and run the sample GitHub code. **Selecting a PySpark input file:** The Google Client Library code samples, below, run a PySpark job that you specify as an input parameter. You can pass in the simple "Hello World" PySpark app located in Cloud Storage at `gs://dataproc-examples/pyspark/hello-world/hello-world.py` or your own PySpark app. See [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to learn more about uploading files to Cloud Storage. 
         
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
         import com.google.cloud.dataproc.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html);
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
               [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html) job = [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html).newBuilder().setPlacement(jobPlacement).setPysparkJob(pySparkJob).build();
         
               // Submit an asynchronous request to execute the job.
               OperationFuture<Job, JobMetadata> submitJobAsOperationAsyncRequest =
                   jobControllerClient.[submitJobAsOperationAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.JobControllerClient.html#com_google_cloud_dataproc_v1_JobControllerClient_submitJobAsOperationAsync_com_google_cloud_dataproc_v1_SubmitJobRequest_)(projectId, region, job);
               [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Job.html) jobResponse = submitJobAsOperationAsyncRequest.get();
         
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

  1. [Install the client library](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library) For more information, See [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).
  2. [Set up authentication](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Clone and run the sample GitHub code. **Selecting a PySpark input file:** The Google Client Library code samples, below, run a PySpark job that you specify as an input parameter. You can pass in the simple "Hello World" PySpark app located in Cloud Storage at `gs://dataproc-examples/pyspark/hello-world/hello-world.py` or your own PySpark app. See [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to learn more about uploading files to Cloud Storage. 
         
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

  1. [Install the client library](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library) For more information, See [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).
  2. [Set up authentication](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Clone and run the sample GitHub code. **Selecting a PySpark input file:** The Google Client Library code samples, below, run a PySpark job that you specify as an input parameter. You can pass in the simple "Hello World" PySpark app located in Cloud Storage at `gs://dataproc-examples/pyspark/hello-world/hello-world.py` or your own PySpark app. See [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to learn more about uploading files to Cloud Storage. 
         
         """
         This quickstart sample walks a user through creating a Cloud Dataproc
         cluster, submitting a PySpark job from Google Cloud Storage to the
         cluster, reading the output of the job and deleting the cluster, all
         using the Python client library.
         
         Usage:
             python quickstart.py --project_id <PROJECT_ID> --region <REGION> \
                 --cluster_name <CLUSTER_NAME> --job_file_path <GCS_JOB_FILE_PATH>
         """
         
         import argparse
         import re
         
         from google.cloud import dataproc_v1 as dataproc
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         
         def quickstart(project_id, region, cluster_name, job_file_path):
             # Create the cluster client.
             cluster_client = dataproc.ClusterControllerClient(
                 client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(region)}
             )
         
             # Create the cluster config.
             cluster = {
                 "project_id": project_id,
                 "cluster_name": cluster_name,
                 "config": {
                     "master_config": {
                         "num_instances": 1,
                         "machine_type_uri": "n1-standard-2",
                         "disk_config": {"boot_disk_size_gb": 100},
                     },
                     "worker_config": {
                         "num_instances": 2,
                         "machine_type_uri": "n1-standard-2",
                         "disk_config": {"boot_disk_size_gb": 100},
                     },
                 },
             }
         
             # Create the cluster.
             operation = cluster_client.create_cluster(
                 request={"project_id": project_id, "region": region, "cluster": cluster}
             )
             result = operation.result()
         
             print("Cluster created successfully: {}".format(result.cluster_name))
         
             # Create the job client.
             job_client = dataproc.JobControllerClient(
                 client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(region)}
             )
         
             # Create the job config.
             job = {
                 "placement": {"cluster_name": cluster_name},
                 "pyspark_job": {"main_python_file_uri": job_file_path},
             }
         
             operation = job_client.submit_job_as_operation(
                 request={"project_id": project_id, "region": region, "job": job}
             )
             response = operation.result()
         
             # Dataproc job output gets saved to the Google Cloud Storage bucket
             # allocated to the job. Use a regex to obtain the bucket and blob info.
             matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)
         
             output = (
                 [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
                 .[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(matches.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1))
                 .blob(f"{matches.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(2)}.000000000")
                 .[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
                 .decode("utf-8")
             )
         
             print(f"Job finished successfully: {output}")
         
             # Delete the cluster once the job has terminated.
             operation = cluster_client.delete_cluster(
                 request={
                     "project_id": project_id,
                     "region": region,
                     "cluster_name": cluster_name,
                 }
             )
             operation.result()
         
             print("Cluster {} successfully deleted.".format(cluster_name))
         
         
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
                 "--job_file_path",
                 type=str,
                 required=True,
                 help="Job in GCS to execute against the cluster.",
             )
         
             args = parser.parse_args()
             quickstart(args.project_id, args.region, args.cluster_name, args.job_file_path)




## View the output

The code outputs the job driver log to the default Managed Service for Apache Spark [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) in Cloud Storage. You can view job driver output from the Google Cloud console in your project's Managed Service for Apache Spark [**Jobs**](https://console.cloud.google.com/project/_/managed-spark/jobs) page in the Google Cloud console. Click the Job ID to view job output on the **Job details** page.

![](https://docs.cloud.google.com/static/managed-spark/images/job-output.png)

## What's next

  * See Managed Service for Apache Spark Cloud Client Library [Additional resources](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#additional_resources). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
