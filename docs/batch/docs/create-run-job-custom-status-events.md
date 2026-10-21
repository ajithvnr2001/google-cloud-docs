---
url: https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events/
title: Configure custom status events to describe runnables \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:23.228041+00:00
---

# Configure custom status events to describe runnables  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Configure custom status events to describe runnables Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure custom status events, which describe a job's runnables, when you create and run a Batch job. To learn about status events, see [View a job's history through status events](https://docs.cloud.google.com/batch/docs/view-status-events).

Custom status events let you provide additional details in a task's history about the progress of its runnables, which can help make a job easier to analyze and troubleshoot. For example, you can configure custom status events that describe when a runnable starts, a runnable ends, a barrier runnable is reached, or an important event happens during the progression of your code.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Configure custom status events

Configure custom status events by using one or more of following options when you are [creating a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job):

  * Describe a runnable's state by defining its display name. You can do this when you create a job using the gcloud CLI or Batch API.

  * Indicate important runtime events by writing a structured task log with the `batch/custom/event` field for each event. You can do this when using any method to create a job as part of the definitions of script and container runnables.




### Describe a runnable's state

You can configure custom status events that describe a runnable's state by defining a runnable's display name ([`displayName` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.display_name)). The resulting custom status events vary slightly for different types of runnables:

  * If you define a display name for a _container runnable or script runnable_ , then Batch automatically adds two types of custom status events. The first custom status event indicates whenever a task starts this runnable. The second custom status event indicates whenever a tasks finishes this runnable and the corresponding [exit code](https://docs.cloud.google.com/batch/docs/automate-task-retries#retry-some-failures).

  * If you define a display name for a _[barrier runnable](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library#barrier-runnable)_ , then Batch automatically adds a custom status event that indicates whenever a task reaches this barrier.




To create and run a job with custom status events that describes a runnable's state, define the `displayName` field for one or more runnables using the gcloud CLI, Batch API or library.

### gcloud

Use the Google Cloud CLI to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the `displayName` field in one or more `runnables` definitions in the JSON file:
    
    
    ...
    "runnables": [
      {
        "displayName":DISPLAY_NAME,
        ...
      }
    ]
    ...
    

For example, a job with custom status events that describes each runnable's state can have a JSON configuration file similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "displayName":"DISPLAY_NAME1",
                "script": {
                  "text": "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}"
                }
              },
              {
                "displayName":"DISPLAY_NAME2",
                "barrier": {}
              },
              {
                "displayName":"DISPLAY_NAME3",
                "script": {
                  "text": "echo Hello world from script 2 for task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace `DISPLAY_NAME1`, `DISPLAY_NAME2`, and `DISPLAY_NAME3` with the name of the runnable, which must be unique within the job—for example, `script 1`, `barrier 1`, and `script 2`.

### API

Use the REST API to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the `displayName` field in one or more `runnables` definitions in the JSON file:
    
    
    ...
    "runnables": [
      {
        "displayName":DISPLAY_NAME,
        ...
      }
    ]
    ...
    

For example, a job with custom status events that describes each runnable's state can have a JSON configuration file similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "displayName":"DISPLAY_NAME1",
                "script": {
                  "text": "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}"
                }
              },
              {
                "displayName":"DISPLAY_NAME2",
                "barrier": {}
              },
              {
                "displayName":"DISPLAY_NAME3",
                "script": {
                  "text": "echo Hello world from script 2 for task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace `DISPLAY_NAME1`, `DISPLAY_NAME2`, and `DISPLAY_NAME3` with the name of the runnable, which must be unique within the job—for example, `script 1`, `barrier 1`, and `script 2`.

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job with custom events
    func createJobWithCustomEvents(w io.Writer, projectID, jobName string) (*batchpb.Job, error) {
    	region := "us-central1"
    	displayName1 := "script 1"
    	displayName2 := "barrier 1"
    	displayName3 := "script 2"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("batchClient error: %w", err)
    	}
    	defer batchClient.Close()
    
    	runn1 := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Script_{
    			Script: &batchpb.Runnable_Script{
    				Command: &batchpb.Runnable_Script_Text{
    					Text: "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}",
    				},
    			},
    		},
    		DisplayName: displayName1,
    	}
    
    	runn2 := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Barrier_{
    			Barrier: &batchpb.Runnable_Barrier{},
    		},
    		DisplayName: displayName2,
    	}
    
    	runn3 := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Script_{
    			Script: &batchpb.Runnable_Script{
    				Command: &batchpb.Runnable_Script_Text{
    					Text: "echo Hello world from script 2 for task ${BATCH_TASK_INDEX}",
    				},
    			},
    		},
    		DisplayName: displayName3,
    	}
    
    	runn4 := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Script_{
    			Script: &batchpb.Runnable_Script{
    				Command: &batchpb.Runnable_Script_Text{
    					Text: "sleep 30; echo '{\"batch/custom/event\": \"DESCRIPTION\"}'; sleep 30",
    				},
    			},
    		},
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		ComputeResource: &batchpb.ComputeResource{
    			// CpuMilli is milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    			CpuMilli:  2000,
    			MemoryMib: 16,
    		},
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    		Runnables:     []*batchpb.Runnable{runn1, runn2, runn3, runn4},
    	}
    
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	labels := map[string]string{"env": "testing", "type": "container"}
    
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
    
    	job := &batchpb.Job{
    		Name:             jobName,
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           labels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	request := &batchpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, region),
    		JobId:  jobName,
    		Job:    job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, request)
    	if err != nil {
    		return nil, fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    	return created_job, nil
    }
    

###  Java 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Barrier](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Barrier.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateBatchCustomEvent {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
        // Name of the runnable, which must be unique
        // within the job. For example: script 1, barrier 1, and script 2.
        String displayName1 = "script 1";
        String displayName2 = "barrier 1";
        String displayName3 = "script 2";
    
        createBatchCustomEvent(projectId, region, jobName, displayName1, displayName2, displayName3);
      }
    
      // Configure custom status events, which describe a job's runnables,
      // when you create and run a Batch job.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchCustomEvent(String projectId, String region, String jobName,
                                               String displayName1, String displayName2,
                                               String displayName3)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addAllRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addAllRunnables_java_lang_Iterable___extends_com_google_cloud_batch_v1_Runnable__)(buildRunnables(displayName1, displayName2, displayName3))
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(3)
              .[setParallelism](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setParallelism_long_)(3)
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING))
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
    
          return result;
        }
      }
    
      // Create runnables with custom scripts
      private static Iterable<Runnable> buildRunnables(String displayName1, String displayName2,
                                                       String displayName3) {
        List<Runnable> runnables = new ArrayList<>();
    
        // Define what will be done as part of the job.
        runnables.add([Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
            .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setDisplayName_java_lang_String_)(displayName1)
            .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                    .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                        "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}")
                    // You can also run a script from a file. Just remember, that needs to be a
                    // script that's already on the VM that will be running the job.
                    // Using setText() and setPath() is mutually exclusive.
                    // .setPath("/tmp/test.sh")
                    )
            .build());
    
        runnables.add([Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setDisplayName_java_lang_String_)(displayName2)
                .[setBarrier](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setBarrier_com_google_cloud_batch_v1_Runnable_Barrier_)([Barrier](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Barrier.html).newBuilder())
                .build());
    
        runnables.add([Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
            .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setDisplayName_java_lang_String_)(displayName3)
            .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                    .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)("echo Hello world from script 2 for task ${BATCH_TASK_INDEX}"))
            .build());
    
        runnables.add([Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
            .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                    // Replace DESCRIPTION with a description
                    // for the custom status event—for example, halfway done.
                    .se[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)sleep 30; echo '{\"batch/custom/event\": \"DESCRIPTION\"}'; sleep 30"))
            .build());
    
        return runnables;
      }
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-custom-events-job';
    // Name of the runnable, which must be unique
    // within the job. For example: script 1, barrier 1, and script 2.
    const displayName1 = 'script 1';
    const displayName2 = 'barrier 1';
    const displayName3 = 'script 2';
    
    // Create runnables with custom scripts
    const runnable1 = new batch.Runnable({
      displayName: displayName1,
      script: new batch.Runnable.Script({
        commands: [
          '-c',
          'echo Hello world from script 1 for task ${BATCH_TASK_INDEX}.',
        ],
      }),
    });
    
    const runnable2 = new batch.Runnable({
      displayName: displayName2,
      barrier: new batch.Runnable.Barrier(),
    });
    
    const runnable3 = new batch.Runnable({
      displayName: displayName3,
      script: new batch.Runnable.Script({
        // Replace DESCRIPTION with a description
        // for the custom status event—for example, halfway done.
        commands: [
          'sleep 30; echo \'{"batch/custom/event": "DESCRIPTION"}\'; sleep 30',
        ],
      }),
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable1, runnable2, runnable3],
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      labels: {env: 'testing', type: 'script'},
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchCustomEvents() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchCustomEvents();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_job_with_status_events(
        project_id: str, region: str, job_name: str
    ) -> batch_v1.Job:
        """
        This method shows the creation of a Batch job with custom status events which describe runnables
        Within the method, the state of a runnable is described by defining its display name.
        The script text is modified to change the commands that are executed, and barriers are adjusted
        to synchronize tasks at specific points.
    
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            region (str): name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name (str): the name of the job that will be created.
                It needs to be unique for each project and region pair.
    
        Returns:
            A job object representing the job created with additional runnables and custom events.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Executes a simple script that prints a message.
        runn1 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runn1.display_name = "Script 1"
        runn1.script.text = "echo Hello world from Script 1 for task ${BATCH_TASK_INDEX}"
    
        # Acts as a barrier to synchronize the execution of subsequent runnables.
        runn2 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runn2.display_name = "Barrier 1"
        runn2.barrier = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Barrier](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Barrier.html)({"name": "hello-barrier"})
    
        # Executes another script that prints a message, intended to run after the barrier.
        runn3 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runn3.display_name = "Script 2"
        runn3.script.text = "echo Hello world from Script 2 for task ${BATCH_TASK_INDEX}"
    
        # Executes a script that imitates a delay and creates a custom event for monitoring purposes.
        runn4 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runn4.script.text = (
            'sleep 30; echo \'{"batch/custom/event": "EVENT_DESCRIPTION"}\'; sleep 30'
        )
    
        # Jobs can be divided into tasks. In this case, we have only one task.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        # Assigning a list of runnables to the task.
        task.runnables = [runn1, runn2, runn3, runn4]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
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
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

After the example job has finished running, the resulting custom status events for each task are similar to the following:
    
    
    statusEvents:
      ...
      - description: 'script at index #0 with display name [DISPLAY_NAME1] started.'
        eventTime: '...'
        type: RUNNABLE_EVENT
      - description: 'script at index #0 with display name [DISPLAY_NAME1] finished with exit
          code 0.'
        eventTime: '...'
        type: RUNNABLE_EVENT
      - description: 'barrier at index #2 with display name [DISPLAY_NAME2] reached.'
        eventTime: '...'
        type: BARRIER_REACHED_EVENT
      - description: 'script at index #2 with display name [DISPLAY_NAME3] started.'
        eventTime: '...'
        type: RUNNABLE_EVENT
      - description: 'script at index #2 with display name [DISPLAY_NAME3] finished with exit
          code 0.'
        eventTime: '...'
        type: RUNNABLE_EVENT
      ...
    

### Indicate important runtime events

You can configure custom status events that indicate when an important event happens while a runnable is running by configuring that runnable to write a structured task log that defines a string for the Batch custom status event (`batch/custom/event`) field.

If a container runnable or script runnable writes a structured task log that defines the `batch/custom/event` JSON field, it produces a custom status event at that time. Although you might configure the structured task log to include additional fields, the custom status event only includes the string for the `batch/custom/event` field.

To create and run a job with custom status events that indicate when an important event happens, configure one or more runnables to [write a structured log by printing JSON](https://docs.cloud.google.com/batch/docs/write-task-logs#structured-log) and define the `batch/custom/event` field as part of the log.

**Note:** Whenever you want a runnable to write logs, you must [enable logs for its job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs). (This has already been done in the following samples.)
    
    
    ...
    "runnables": [
      {
        ...
        "echo '{\"batch/custom/event\":\"EVENT_DESCRIPTION\"}'"
        ...
      }
    ]
    ...
    "logsPolicy": {
      "destination": "CLOUD_LOGGING"
    }
    ...
    

For example, a job with custom status events that indicate when an important event happens can have a JSON configuration file similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "sleep 30; echo '{\"batch/custom/event\": \"EVENT_DESCRIPTION\"}'; sleep 30"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace `EVENT_DESCRIPTION` with a description for the custom status event—for example, `halfway done`.

After the example job has finished running, the resulting custom status event for each task is similar to the following:
    
    
    statusEvents:
      ...
      - description: EVENT_DESCRIPTION
        eventTime: '...'
        type: RUNNABLE_CUSTOM_EVENT
      ...
    

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn how to [view status events](https://docs.cloud.google.com/batch/docs/view-status-events).
  * Learn how to [write task logs](https://docs.cloud.google.com/batch/docs/write-task-logs).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
