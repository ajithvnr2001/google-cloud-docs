---
url: https://docs.cloud.google.com/batch/docs/samples/batch-create-script-job-with-bucket/
title: Create and submit a job that uses a Cloud Storage bucket \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:40.568962+00:00
---

# Create and submit a job that uses a Cloud Storage bucket  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/samples/batch-create-script-job-with-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Samples ](https://docs.cloud.google.com/batch/docs/samples)



#  Create and submit a job that uses a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Create and submit a sample Batch job that runs a script that accesses an existing Cloud Storage bucket. The job's definition specifies to mount the bucket to all VMs so that the job's tasks can read input data from it or write results to it. After you submit the job, Batch automatically queues, schedules, and executes the job on Compute Engine VMs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and run a job that uses storage volumes](https://docs.cloud.google.com/batch/docs/create-run-job-storage)



## Code sample

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id, std::string const& bucket_name) {
        // Initialize the request; start with the fields that depend on the sample
        // input.
        google::cloud::batch::v1::CreateJobRequest request;
        request.set_parent("projects/" + project_id + "/locations/" + location_id);
        request.set_job_id(job_id);
        // Most of the job description is fixed in this example; use a string to
        // initialize it, and then override the GCS remote path.
        auto constexpr kText = R"pb(
          task_groups {
            task_count: 4
            task_spec {
              compute_resource { cpu_milli: 500 memory_mib: 16 }
              max_retry_count: 2
              max_run_duration { seconds: 3600 }
              runnables {
                script {
                  text: "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt"
                }
              }
              volumes { mount_path: "/mnt/share" }
            }
          }
          allocation_policy {
            instances {
              policy { machine_type: "e2-standard-4" provisioning_model: STANDARD }
            }
          }
          labels { key: "env" value: "testing" }
          labels { key: "type" value: "script" }
          logs_policy { destination: CLOUD_LOGGING }
        )pb";
        auto* job = request.mutable_job();
        if (!google::protobuf::TextFormat::ParseFromString(kText, job)) {
          throw std::runtime_error("Error parsing Job description");
        }
        job->mutable_task_groups(0)
            ->mutable_task_spec()
            ->mutable_volumes(0)
            ->mutable_gcs()
            ->set_remote_path(bucket_name);
        // Create a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.CreateJob(request);
        if (!response) throw std::move(response).status();
        std::cout << "Job : " << response->DebugString() << "\n";
      }

### Go

For more information, see the [Batch Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job that executes the specified script
    func createScriptJobWithBucket(w io.Writer, projectID, region, jobName, bucketName string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    	// jobName := "some-bucket"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	// Define what will be done as part of the job.
    	command := &batchpb.Runnable_Script_Text{
    		Text: "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt",
    	}
    
    	// Specify the Google Cloud Storage bucket to mount
    	volume := &batchpb.Volume{
    		Source: &batchpb.Volume_Gcs{
    			Gcs: &batchpb.GCS{
    				RemotePath: bucketName,
    			},
    		},
    		MountPath:    "/mnt/share",
    		MountOptions: []string{},
    	}
    
    	// We can specify what resources are requested by each task.
    	resources := &batchpb.ComputeResource{
    		// CpuMilli is milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
    		CpuMilli:  500,
    		MemoryMib: 16,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		Runnables: []*batchpb.Runnable{{
    			Executable: &batchpb.Runnable_Script_{
    				Script: &batchpb.Runnable_Script{Command: command},
    			},
    		}},
    		ComputeResource: resources,
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    		Volumes:       []*batchpb.Volume{volume},
    	}
    
    	// Tasks are grouped inside a job using TaskGroups.
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// In this case, we tell the system to use "e2-standard-4" machine type.
    	// Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					MachineType: "e2-standard-4",
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	jobLabels := map[string]string{"env": "testing", "type": "script"}
    
    	// The job's parent is the region in which the job will run
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    
    	job := batchpb.Job{
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           jobLabels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	req := &batchpb.CreateJobRequest{
    		Parent: parent,
    		JobId:  jobName,
    		Job:    &job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    
    	return nil
    }
    

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[GCS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithMountedBucket {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
    
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
    
        // Name of the bucket to be mounted for your Job.
        String bucketName = "BUCKET_NAME";
    
        createScriptJobWithBucket(projectId, region, jobName, bucketName);
      }
    
      // This method shows how to create a sample Batch Job that will run
      // a simple command on Cloud Compute instances.
      public static void createScriptJobWithBucket(String projectId, String region, String jobName,
          String bucketName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world from task ${BATCH_TASK_INDEX}. >> "
                                  + "/mnt/share/output_task_${BATCH_TASK_INDEX}.txt")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) volume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
              .[setGcs](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setGcs_com_google_cloud_batch_v1_GCS_)([GCS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS.html).newBuilder()
                  .setRemotePath(bucketName)
                  .build())
              .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/share")
              .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(500)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .addVolumes(volume)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder().[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  .putLabels("mount", "bucket")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING).build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
        }
      }
    }

### Node.js

For more information, see the [Batch Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    /**
     * The region you want to the job to run in. The regions that support Batch are listed here:
     * https://cloud.google.com/batch/docs/get-started#locations
     */
    // const region = 'us-central-1';
    /**
     * The name of the job that will be created.
     * It needs to be unique for each project and region pair.
     */
    // const jobName = 'YOUR_JOB_NAME';
    /**
     * The name of the bucket to be mounted.
     */
    // const bucketName = 'YOUR_BUCKET_NAME';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    // Define what will be done as part of the job.
    const task = new batch.TaskSpec();
    const runnable = new batch.Runnable();
    runnable.script = new batch.Runnable.Script();
    runnable.script.text =
      'echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt';
    // You can also run a script from a file. Just remember, that needs to be a script that's
    // already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
    // exclusive.
    // runnable.script.path = '/tmp/test.sh'
    task.runnables = [runnable];
    
    const gcsBucket = new batch.GCS();
    gcsBucket.remotePath = bucketName;
    const gcsVolume = new batch.Volume();
    gcsVolume.gcs = gcsBucket;
    gcsVolume.mountPath = '/mnt/share';
    task.volumes = [gcsVolume];
    
    // We can specify what resources are requested by each task.
    const resources = new batch.ComputeResource();
    resources.cpuMilli = 2000; // in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    resources.memoryMib = 16;
    task.computeResource = resources;
    
    task.maxRetryCount = 2;
    task.maxRunDuration = {seconds: 3600};
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup();
    group.taskCount = 4;
    group.taskSpec = task;
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const allocationPolicy = new batch.AllocationPolicy();
    const policy = new batch.AllocationPolicy.InstancePolicy();
    policy.machineType = 'e2-standard-4';
    const instances = new batch.AllocationPolicy.InstancePolicyOrTemplate();
    instances.policy = policy;
    allocationPolicy.instances = [instances];
    
    const job = new batch.Job();
    job.name = jobName;
    job.taskGroups = [group];
    job.allocationPolicy = allocationPolicy;
    job.labels = {env: 'testing', type: 'script'};
    // We use Cloud Logging as it's an option available out of the box
    job.logsPolicy = new batch.LogsPolicy();
    job.logsPolicy.destination = batch.LogsPolicy.Destination.CLOUD_LOGGING;
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const response = await batchClient.createJob(request);
      console.log(response);
    }
    
    await callCreateJob();

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_script_job_with_bucket(
        project_id: str, region: str, job_name: str, bucket_name: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            bucket_name: name of the bucket to be mounted for your Job.
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt"
        task.runnables = [runnable]
    
        gcs_bucket = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[GCS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.GCS.html)()
        gcs_bucket.remote_path = bucket_name
        gcs_volume = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
        gcs_volume.gcs = gcs_bucket
        gcs_volume.mount_path = "/mnt/share"
        task.volumes = [gcs_volume]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 500  # in milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
        resources.memory_mib = 16
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy.instances = [instances]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script", "mount": "bucket"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=batchforgooglecloud). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
