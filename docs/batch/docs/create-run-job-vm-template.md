---
url: https://docs.cloud.google.com/batch/docs/create-run-job-vm-template/
title: Define job resources using a VM instance template \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:45.188733+00:00
---

# Define job resources using a VM instance template  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-vm-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Define job resources using a VM instance template Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to define the VM resources for a Batch job by specifying a [Compute Engine VM instance template](https://docs.cloud.google.com/compute/docs/instance-templates) when you create the job.

The types of VM resources that a job runs on are automatically defined by Batch unless you define them by using one of the following methods:

  * **Define a job's VM resources directly by using the[`instances[].policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate.FIELDS.policy).** This method is demonstrated in most Batch documentation.
  * **Define a job's VM resources through a template by using the[`instances[].instanceTemplate` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate.FIELDS.instance_template).** This is the method explained in this document.

Using a template is required to specify VM options that Batch doesn't provide job fields for. Using a template can also be convenient when you want to specify the same VM resources for multiple jobs.


**Important:** This document is intended for users who already understand the requirements for the VM resources for their jobs. Learn how to define the `policy` subfields that correspond to the VM resources that you want to specify before using the `instanceTemplate` field. For more information about the requirements for customizing the resources that a job runs on, see [Job resources](https://docs.cloud.google.com/batch/docs/create-run-job#resources) and [Job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) or [identify an existing instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates). 
  3. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * Create a job from a Compute Engine VM instance template: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) on the VM instance template 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create a job using a Compute Engine VM instance template

This section provides examples for how to create a basic script job from an existing VM instance template. You can create a job from a VM instance template using the gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

### gcloud

To create a job from a VM instance template using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit) and specify the VM instance template in the job's JSON configuration file.

For example, to create a basic script job from a VM instance template:

  1. Create a JSON file in the current directory named `hello-world-instance-template.json` with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                                 }
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": 2000,
                             "memoryMib": 16
                         },
                         "maxRetryCount": 2,
                         "maxRunDuration": "3600s"
                     },
                     "taskCount": 4,
                     "parallelism": 2
                 }
             ],
             "allocationPolicy": {
                 "instances": [
                     {
                         "installGpuDrivers": INSTALL_GPU_DRIVERS,
                         "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
                     }
                 ]
             },
             "labels": {
                 "department": "finance",
                 "env": "testing"
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `INSTALL_GPU_DRIVERS`: Optional. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in your Compute Engine VM instance template, and Batch installs them on your behalf. For more information, see how to [create a job that uses a GPU](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).
     * `INSTANCE_TEMPLATE_NAME`: the name of an existing Compute Engine VM instance template. Learn how to [create](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) and [list instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates).
  2. Run the following command:
         
         gcloud batch jobs submit example-template-job \
           --location us-central1 \
           --config hello-world-instance-template.json
         




### API

To create a basic job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify a VM instance template in the `allocationPolicy` field.

For example, to create a basic script jobs from a VM instance template, use the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs?job_id=example-script-job
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                            }
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": 2000,
                        "memoryMib": 16
                    },
                    "maxRetryCount": 2,
                    "maxRunDuration": "3600s"
                },
                "taskCount": 4,
                "parallelism": 2
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "installGpuDrivers": INSTALL_GPU_DRIVERS,
                    "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
                }
            ]
        },
        "labels": {
            "department": "finance",
            "env": "testing"
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `INSTALL_GPU_DRIVERS`: Optional. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in your Compute Engine VM instance template, and Batch installs them on your behalf. For more information, see how to [create a job that uses a GPU](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).
  * `INSTANCE_TEMPLATE_NAME`: the name of an existing Compute Engine VM instance template. Learn how to [create](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) and [list instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates).



###  Go 

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
    func createScriptJobWithTemplate(w io.Writer, projectID, region, jobName, templateLink string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    	/* A link to an existing Instance Template. Acceptable formats:
    	*  "projects/{project_id}/global/instanceTemplates/{template_name}"
    	*  "{template_name}" - if the template is defined in the same project as used to create the Job.
    	 */
    	// template_link := "my-instance-template"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	// Define what will be done as part of the job.
    	command := &batchpb.Runnable_Script_Text{
    		Text: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
    	}
    
    	// We can specify what resources are requested by each task.
    	resources := &batchpb.ComputeResource{
    		// CpuMilli is milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    		CpuMilli:  2000,
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
    	}
    
    	// Tasks are grouped inside a job using TaskGroups.
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// In this case, we are going to use an Instance Template that defines the VM.
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_InstanceTemplate{
    				InstanceTemplate: templateLink,
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
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithTemplate {
    
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
    
        // A link to an existing Instance Template. Acceptable formats:
        //   * "projects/{projectId}/global/instanceTemplates/{templateName}"
        //   * "{templateName}" - if the template is defined in the same project
        //   as used to create the Job.
        String templateLink = "TEMPLATE_LINK";
    
        createWithTemplate(projectId, region, jobName, templateLink);
      }
    
      // This method shows how to create a sample Batch Job that will run
      // a simple command on Cloud Compute instances created using a provided Template.
      public static void createWithTemplate(String projectId, String region, String jobName,
          String templateLink)
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
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                  + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 2 whole CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use an instance template that defines all the
          // required parameters.
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances(
                      [InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder().[setInstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setInstanceTemplate_java_lang_String_)(templateLink).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
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

###  Node.js 

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
     * a link to an existing Instance Template. Acceptable formats:
     * "projects/{project_id}/global/instanceTemplates/{template_name}"
     * "{template_name}" - if the template is defined in the same project as used to create the Job.
     */
    // const templateLink = 'YOUR_TEMPLATE'
    
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
      'echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.';
    // You can also run a script from a file. Just remember, that needs to be a script that's
    // already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
    // exclusive.
    // runnable.script.path = '/tmp/test.sh'
    task.runnables = [runnable];
    
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
    const instances = new batch.AllocationPolicy.InstancePolicyOrTemplate();
    instances.instanceTemplate = templateLink;
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

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_script_job_with_template(
        project_id: str, region: str, job_name: str, template_link: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances created using a provided Template.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            template_link: a link to an existing Instance Template. Acceptable formats:
                * "projects/{project_id}/global/instanceTemplates/{template_name}"
                * "{template_name}" - if the template is defined in the same project as used to create the Job.
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
        # You can also run a script from a file. Just remember, that needs to be a script that's
        # already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
        # exclusive.
        # runnable.script.path = '/tmp/test.sh'
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
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
        # In this case, we tell the system to use an instance template that defines all the
        # required parameters.
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.instance_template = template_link
        allocation_policy.instances = [instances]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id, std::string const& template_name) {
        // Initialize the request; start with the fields that depend on the sample
        // input.
        google::cloud::batch::v1::CreateJobRequest request;
        request.set_parent("projects/" + project_id + "/locations/" + location_id);
        request.set_job_id(job_id);
        // Most of the job description is fixed in this example; use a string to
        // initialize it, and then override the template name.
        auto constexpr kText = R"pb(
          task_groups {
            task_count: 4
            task_spec {
              compute_resource { cpu_milli: 500 memory_mib: 16 }
              max_retry_count: 2
              max_run_duration { seconds: 3600 }
              runnables {
                script {
                  text: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                }
              }
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
        job->mutable_allocation_policy()->add_instances()->set_instance_template(
            template_name);
        // Create a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.CreateJob(request);
        if (!response) throw std::move(response).status();
        std::cout << "Job : " << response->DebugString() << "\n";
      }

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
