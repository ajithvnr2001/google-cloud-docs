---
url: https://docs.cloud.google.com/batch/docs/enable-notifications/
title: Create and run a job that sends Pub/Sub status notifications \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:29.334905+00:00
---

# Create and run a job that sends Pub/Sub status notifications  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/enable-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run a job that sends Pub/Sub status notifications Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Batch job that sends [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) notifications. You can use Pub/Sub to get notifications when a job or task state changes, or when a job or task enters a specific state. For more information, see [Monitor jobs using notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).

**Note:** Pub/Sub is a separate Google Cloud service that has its own pricing. For more information, see [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. [Create or identify a Pub/Sub topic for Batch notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications#enable-notifications).
  3. [Configure a subscription to receive and use the notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications#stream).



### Required roles

  * To get the permissions that you need to create and run a job that sends notifications, ask your administrator to grant you the following IAM roles: 

    * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project.
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/get-started#job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
    * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) on the Pub/Sub topic or project.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Unless you are using the default configuration for [the job's service account](https://docs.cloud.google.com/batch/docs/get-started#job-service-account), ensure that it has the necessary permissions.

To ensure that the job's service account has the necessary permissions to publish Pub/Sub notifications, ask your administrator to grant the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role to the job's service account on your Pub/Sub topic. **Important:** You must grant this role to the job's service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

  * If you want a job to publish notifications to a Pub/Sub topic that is in a different project than the job, then the [Batch service agent](https://docs.cloud.google.com/batch/docs/get-started#batch-service-agent) for the job's project must be granted permission to publish to that topic. 

To ensure that the Batch service agent for the job's project has the necessary permissions to publish Pub/Sub notifications to a Pub/Sub topic in another project, ask your administrator to grant the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role to the Batch service agent for the job's project on the Pub/Sub topic. **Important:** You must grant this role to the Batch service agent for the job's project, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 




## Create and run a job that sends notifications

You can create a Batch job that sends Pub/Sub notifications by doing the following:

### gcloud

Use the Google Cloud CLI to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the `notifications` field and one or more [`jobNotification` objects](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobnotification) in the main body of the JSON file:
    
    
    {
    ...
      "notifications": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            ATTRIBUTES
          }
        }
      ]
    ...
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the Pub/Sub topic.
  * `TOPIC_ID`: the Pub/Sub topic ID of the topic you created when you [enabled Pub/Sub notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications#enable-notifications).
  * `ATTRIBUTES`: specify one or more of the following attributes, which each let you receive notifications about the state of the job or all of its tasks.

    * For notifications about all job state changes, specify the following:
          
          "type": "JOB_STATE_CHANGED"
          

    * For notifications about a specific job state change, specify the following:
          
          "type": "JOB_STATE_CHANGED",
          "newJobState": "JOB_STATE"
          

Replace `JOB_STATE` with one of the following job states:

      * `QUEUED`
      * `SCHEDULED`
      * `RUNNING`
      * `SUCCEEDED`
      * `FAILED`

For more information about job states, see [Job lifecycle](https://docs.cloud.google.com/batch/docs/create-run-job#lifecycle).

    * For notifications about all task state changes, specify the following:
          
          "type": "TASK_STATE_CHANGED"
          

    * For notifications about specific task state changes, specify the following:
          
          "type": "TASK_STATE_CHANGED",
          "newTaskState": "TASK_STATE"
          

Replace `TASK_STATE` with one of the following task states:

      * `PENDING`
      * `ASSIGNED`
      * `RUNNING`
      * `SUCCEEDED`
      * `FAILED`

For more information about task states, see [Job lifecycle](https://docs.cloud.google.com/batch/docs/create-run-job#lifecycle).




For example, suppose you want to receive notifications about all job state changes and any time a task fails. To do so, you can have a JSON configuration file that is similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello World! This is task $BATCH_TASK_INDEX."
                }
              }
            ]
          },
          "taskCount": 3,
        }
      ],
      "logsPolicy": {
          "destination": "CLOUD_LOGGING"
      },
      "notifications": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            "type": "JOB_STATE_CHANGED"
          }
        },
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            "type": "TASK_STATE_CHANGED",
            "newTaskState": "FAILED"
          }
        }
      ]
    }
    

### API

Use the REST API to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the `notifications` field and one or more [`jobNotification` objects](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#jobnotification) in the main body of the JSON file:
    
    
    {
    ...
      "notifications": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            ATTRIBUTES
          }
        }
      ]
    ...
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the Pub/Sub topic.
  * `TOPIC_ID`: the Pub/Sub topic ID of the topic you created when you [enabled Pub/Sub notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications#enable-notifications).
  * `ATTRIBUTES`: specify one or more of the following attributes, which each let you receive notifications about the state of the job or all of its tasks.

    * For notifications about all job state changes, specify the following:
          
          "type": "JOB_STATE_CHANGED"
          

    * For notifications about a specific job state change, specify the following:
          
          "type": "JOB_STATE_CHANGED",
          "newJobState": "JOB_STATE"
          

Replace `JOB_STATE` with one of the following job states:

      * `QUEUED`
      * `SCHEDULED`
      * `RUNNING`
      * `SUCCEEDED`
      * `FAILED`

For more information about job states, see [Job lifecycle](https://docs.cloud.google.com/batch/docs/create-run-job#lifecycle).

    * For notifications about all task state changes, specify the following:
          
          "type": "TASK_STATE_CHANGED"
          

    * For notifications about specific task state changes, specify the following:
          
          "type": "TASK_STATE_CHANGED",
          "newTaskState": "TASK_STATE"
          

Replace `TASK_STATE` with one of the following task states:

      * `PENDING`
      * `ASSIGNED`
      * `RUNNING`
      * `SUCCEEDED`
      * `FAILED`

For more information about task states, see [Job lifecycle](https://docs.cloud.google.com/batch/docs/create-run-job#lifecycle).




For example, suppose you want to receive notifications about all job state changes and any time a task fails. To do so, you can have a JSON configuration file that is similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello World! This is task $BATCH_TASK_INDEX."
                }
              }
            ]
          },
          "taskCount": 3,
        }
      ],
      "logsPolicy": {
          "destination": "CLOUD_LOGGING"
      },
      "notifications": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            "type": "JOB_STATE_CHANGED"
          }
        },
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "message": {
            "type": "TASK_STATE_CHANGED",
            "newTaskState": "FAILED"
          }
        }
      ]
    }
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job with configured notifications
    func createJobWithNotifications(w io.Writer, projectID, region, jobName, topicName string) (*batchpb.Job, error) {
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("batchClient error: %w", err)
    	}
    	defer batchClient.Close()
    
    	script := &batchpb.Runnable_Script_{
    		Script: &batchpb.Runnable_Script{
    			Command: &batchpb.Runnable_Script_Text{
    				Text: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
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
    		Runnables: []*batchpb.Runnable{{
    			Executable: script,
    		}},
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
    
    	notifications := []*batchpb.JobNotification{
    		{
    			PubsubTopic: fmt.Sprintf("projects/%s/topics/%s", projectID, topicName),
    			Message: &batchpb.JobNotification_Message{
    				Type: batchpb.[JobNotification_JOB_STATE_CHANGED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_JobNotification_TYPE_UNSPECIFIED_JobNotification_JOB_STATE_CHANGED_JobNotification_TASK_STATE_CHANGED),
    			},
    		},
    		{
    			PubsubTopic: fmt.Sprintf("projects/%s/topics/%s", projectID, topicName),
    			Message: &batchpb.JobNotification_Message{
    				Type:         batchpb.[JobNotification_TASK_STATE_CHANGED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_JobNotification_TYPE_UNSPECIFIED_JobNotification_JOB_STATE_CHANGED_JobNotification_TASK_STATE_CHANGED),
    				NewTaskState: batchpb.[TaskStatus_FAILED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_TaskStatus_STATE_UNSPECIFIED_TaskStatus_PENDING_TaskStatus_ASSIGNED_TaskStatus_RUNNING_TaskStatus_FAILED_TaskStatus_SUCCEEDED_TaskStatus_UNEXECUTED),
    			},
    		},
    	}
    
    	job := &batchpb.Job{
    		Name:             jobName,
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           labels,
    		Notifications:    notifications,
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
    import com.google.cloud.batch.v1.[JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html);
    import com.google.cloud.batch.v1.[JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html).[Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html);
    import com.google.cloud.batch.v1.[JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[TaskStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskStatus.html).State;
    import com.google.common.collect.Lists;
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateBatchNotification {
    
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
        // The Pub/Sub topic ID to send the notifications to.
        String topicId = "TOPIC_ID";
    
        createBatchNotification(projectId, region, jobName, topicId);
      }
    
      // Create a Batch job that sends notifications to Pub/Sub
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchNotification(String projectId, String region, String jobName,
                                                String topicId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                      + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(3)
              .[setParallelism](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setParallelism_long_)(1)
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[addAllNotifications](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addAllNotifications_java_lang_Iterable___extends_com_google_cloud_batch_v1_JobNotification__)(buildNotifications(projectId, topicId))
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
    
      // Creates notification configurations to send messages to Pub/Sub when the state is changed
      private static Iterable<JobNotification> buildNotifications(String projectId, String topicId) {
        String pubsubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
    
        [JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html) jobStateChanged = [JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html).newBuilder()
                .[setPubsubTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Builder.html#com_google_cloud_batch_v1_JobNotification_Builder_setPubsubTopic_java_lang_String_)(pubsubTopic)
                .setMessage([Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html).newBuilder().setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).JOB_STATE_CHANGED))
                .build();
    
        [JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html) taskStateChanged = [JobNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.html).newBuilder()
                .[setPubsubTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Builder.html#com_google_cloud_batch_v1_JobNotification_Builder_setPubsubTopic_java_lang_String_)(pubsubTopic)
                .setMessage([Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html).newBuilder()
                        .setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).TASK_STATE_CHANGED)
                        .[setNewTaskState](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Message.Builder.html#com_google_cloud_batch_v1_JobNotification_Message_Builder_setNewTaskState_com_google_cloud_batch_v1_TaskStatus_State_)(State.FAILED))
                .build();
    
        return Lists.newArrayList(jobStateChanged, taskStateChanged);
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
    const PROJECT_ID = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const REGION = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const JOB_NAME = 'job-name-batch-notifications';
    // The Pub/Sub topic ID to send the notifications to.
    const TOPIC_ID = 'topic-id';
    
    // Define what will be done as part of the job.
    const task = new batch.TaskSpec();
    const runnable = new batch.Runnable();
    runnable.script = new batch.Runnable.Script();
    runnable.script.commands = [
      '-c',
      'echo Hello world! This is task ${BATCH_TASK_INDEX}.',
    ];
    task.runnables = [runnable];
    task.maxRetryCount = 2;
    task.maxRunDuration = {seconds: 3600};
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup();
    group.taskCount = 3;
    group.taskSpec = task;
    
    // Create batch notification when job state changed
    const notification1 = new batch.JobNotification();
    notification1.pubsubTopic = `projects/${PROJECT_ID}/topics/${TOPIC_ID}`;
    notification1.message = {
      type: 'JOB_STATE_CHANGED',
    };
    
    // Create batch notification when task state changed
    const notification2 = new batch.JobNotification();
    notification2.pubsubTopic = `projects/${PROJECT_ID}/topics/${TOPIC_ID}`;
    notification2.message = {
      type: 'TASK_STATE_CHANGED',
      newTaskState: 'FAILED',
    };
    
    const job = new batch.Job();
    job.name = JOB_NAME;
    job.taskGroups = [group];
    job.notifications = [notification1, notification2];
    job.labels = {env: 'testing', type: 'script'};
    // We use Cloud Logging as it's an option available out of the box
    job.logsPolicy = new batch.LogsPolicy();
    job.logsPolicy.destination = batch.LogsPolicy.Destination.CLOUD_LOGGING;
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${PROJECT_ID}/locations/${REGION}`;
    
    async function callCreateBatchNotifications() {
      // Construct request
      const request = {
        parent,
        jobId: JOB_NAME,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchNotifications();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_with_pubsub_notification_job(
        project_id: str, region: str, job_name: str, topic_name: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command inside a container on Cloud Compute instances.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            topic_name: the name of the Pub/Sub topic to which the notification will be sent.
                The topic should be created in GCP Pub/Sub before running this method.
                The procedure for creating a topic is listed here: https://cloud.google.com/pubsub/docs/create-topic
    
        Returns:
            A job object representing the job created.
        """
    
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.container = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Container](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Container.html)()
        runnable.container.image_uri = "gcr.io/google-containers/busybox"
        runnable.container.entrypoint = "/bin/sh"
        runnable.container.commands = [
            "-c",
            "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
        ]
    
        # Jobs can be divided into tasks. In this case, we have only one task.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
    
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
    
        # Configuring the first notification
        notification1 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html)()
        notification1.pubsub_topic = f"projects/{project_id}/topics/{topic_name}"
        # Define the message that will be sent to the topic
        first_massage = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html).[Message](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Message.html)()
        # Specify the new job state that will trigger the notification
        # In this case, the notification is triggered when the job state changes to SUCCEEDED
        first_massage.type_ = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html).[Type](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Type.html).JOB_STATE_CHANGED
        first_massage.new_job_state = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.html).State.SUCCEEDED
        # Assign the message to the notification
        notification1.message = first_massage
    
        # Configuring the second notification
        notification2 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html)()
        notification2.pubsub_topic = f"projects/{project_id}/topics/{topic_name}"
        second_message = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html).[Message](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Message.html)()
        second_message.type_ = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.html).[Type](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Type.html).TASK_STATE_CHANGED
        second_message.new_task_state = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskStatus.html).State.FAILED
        notification2.message = second_message
    
        # Assign a list of notifications to the job.
        job.notifications = [notification1, notification2]
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

After the job starts running, you can use its notifications. For example, if the Pub/Sub topic for your job has a subscription that streams notifications to BigQuery, you can [analyze the Pub/Sub notifications in BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications#analyze-bigquery).

## What's next

  * Learn more about how to [monitor job status using Pub/Sub notifications and BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).
  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
