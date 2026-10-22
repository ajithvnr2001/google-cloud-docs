---
url: https://docs.cloud.google.com/batch/docs/samples/batch-get-task/
title: Describe a task \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:47.386931+00:00
---

# Describe a task  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/samples/batch-get-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Samples ](https://docs.cloud.google.com/batch/docs/samples)



#  Describe a task Stay organized with collections  Save and categorize content based on your preferences. 

A Batch job consists of one or several tasks. This sample retrieves the name and detailed status info for a given task.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks)



## Code sample

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id, std::string const& group_id,
         std::string const& task_number) {
        auto const name = "projects/" + project_id + "/locations/" + location_id +
                          "/jobs/" + job_id + "/taskGroups/" + group_id +
                          "/tasks/" + task_number;
        // Initialize a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.GetTask(name);
        if (!response) throw std::move(response).status();
        std::cout << "GetTask() succeeded with " << response->DebugString() << "\n";
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
    )
    
    // Retrieves the information about the specified job, most importantly its status
    func getTask(w io.Writer, projectID, region, jobName, taskGroup string, taskNumber int32) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    	// taskGroup := "group0" // defaults to "group0" on job creation unless overridden
    	// taskNumber := 0
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	req := &batchpb.GetTaskRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/jobs/%s/taskGroups/%s/tasks/%d",
    			projectID, region, jobName, taskGroup, taskNumber),
    	}
    
    	response, err := batchClient.GetTask(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get task: %w", err)
    	}
    
    	fmt.Fprintf(w, "Task info: %v\n", response)
    
    	return nil
    }
    

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.html);
    import com.google.cloud.batch.v1.[TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskName.html);
    import java.io.IOException;
    
    public class GetTask {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region hosts the job.
        String region = "europe-central2";
        // The name of the job you want to retrieve information about.
        String jobName = "JOB_NAME";
        // The name of the group that owns the task you want to check. Usually it's `group0`.
        String groupName = "group0";
        // Number of the task you want to look up.
        int taskNumber = 0;
    
        getTask(projectId, region, jobName, groupName, taskNumber);
      }
    
      // Retrieve information about a Task.
      public static void getTask(String projectId, String region, String jobName, String groupName,
          int taskNumber) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.html) task = batchServiceClient.getTask([TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskName.html).newBuilder()
              .setProject(projectId)
              .setLocation(region)
              .setJob(jobName)
              .setTaskGroup(groupName)
              .[setTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskName.Builder.html#com_google_cloud_batch_v1_TaskName_Builder_setTask_java_lang_String_)(String.valueOf(taskNumber))
              .build());
          System.out.printf("Retrieved task information: %s", task.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.html#com_google_cloud_batch_v1_Task_getName__)());
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
     * The region that hosts the job.
     */
    // const region = 'us-central-1';
    /**
     * The name of the job you want to retrieve information about.
     */
    // const jobName = 'YOUR_JOB_NAME';
    /**
     * The name of the group that owns the task you want to check.
     * Usually it's `group0`.
     */
    // const groupName = 'group0';
    /**
     * The number of the task you want to look up.
     */
    // const taskNumber = 0;
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    async function callGetJob() {
      // Construct request
      const request = {
        name:
          `projects/${projectId}/locations/${region}/jobs/${jobName}` +
          `/taskGroups/${groupName}/tasks/${taskNumber}`,
      };
    
      // Run request
      const response = await batchClient.getTask(request);
      console.log(response);
    }
    
    await callGetJob();

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def get_task(
        project_id: str, region: str, job_name: str, group_name: str, task_number: int
    ) -> batch_v1.Task:
        """
        Retrieve information about a Task.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region hosts the job.
            job_name: the name of the job you want to retrieve information about.
            group_name: the name of the group that owns the task you want to check. Usually it's `group0`.
            task_number: number of the task you want to look up.
    
        Returns:
            A Task object representing the specified task.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        return client.[get_task](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_get_task)(
            name=f"projects/{project_id}/locations/{region}/jobs/{job_name}"
            f"/taskGroups/{group_name}/tasks/{task_number}"
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=batchforgooglecloud). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
