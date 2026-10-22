---
url: https://docs.cloud.google.com/batch/docs/samples/batch-list-tasks/
title: List tasks \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:47.658294+00:00
---

# List tasks  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/samples/batch-list-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Samples ](https://docs.cloud.google.com/batch/docs/samples)



#  List tasks Stay organized with collections  Save and categorize content based on your preferences. 

A Batch job consists of one or several tasks. This sample retrieves the name and current state of all tasks in a given job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks)



## Code sample

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id, std::string const& group_id) {
        auto const parent = "projects/" + project_id + "/locations/" + location_id +
                            "/jobs/" + job_id + "/taskGroups/" + group_id;
        // Initialize a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        int i = 0;
        for (auto task : client.ListTasks(parent)) {
          if (!task) throw std::move(task).status();
          std::cout << "Task[" << i++ << "]  " << task->DebugString() << "\n";
        }
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
    	"google.golang.org/api/iterator"
    )
    
    // Lists all tasks in the given project and region
    func listTasks(w io.Writer, projectID, region, jobName, taskGroup string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    	// taskGroup := "group0" // defaults to "group0" on job creation unless overridden
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	req := &batchpb.ListTasksRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s/jobs/%s/taskGroups/%s", projectID, region, jobName, taskGroup),
    	}
    
    	var tasks []*batchpb.Task
    	it := batchClient.ListTasks(ctx, req)
    
    	for {
    		task, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("unable to list tasks: %w", err)
    		}
    		tasks = append(tasks, task)
    	}
    
    	fmt.Fprintf(w, "Tasks: %v\n", tasks)
    
    	return nil
    }
    

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.html);
    import java.io.IOException;
    
    public class ListTasks {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region hosts the job.
        String region = "europe-central2";
        // Name of the job which tasks you want to list.
        String jobName = "JOB_NAME";
        // Name of the group of tasks. Usually it's `group0`.
        String groupName = "group0";
    
        listTasks(projectId, region, jobName, groupName);
      }
    
      // Get a list of all jobs defined in given region.
      public static void listTasks(String projectId, String region, String jobName, String groupName)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          String parent = String.format("projects/%s/locations/%s/jobs/%s/taskGroups/%s", projectId,
              region, jobName, groupName);
          for ([Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.html) task : batchServiceClient.listTasks(parent).iterateAll()) {
            System.out.println(task.getName());
          }
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
     * The name of the job which tasks you want to list.
     */
    // const jobName = 'YOUR_JOB_NAME';
    /**
     * The name of the group of tasks. Usually it's `group0`.
     */
    // const groupName = 'group0';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    async function callListTasks() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${region}/jobs/${jobName}/taskGroups/${groupName}`,
      };
    
      // Run request
      const iterable = await batchClient.listTasksAsync(request);
      for await (const response of iterable) {
        console.log(response);
      }
    }
    
    await callListTasks();

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import batch_v1
    
    
    def list_tasks(
        project_id: str, region: str, job_name: str, group_name: str
    ) -> Iterable[batch_v1.Task]:
        """
        Get a list of all jobs defined in given region.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region hosting the jobs.
            job_name: name of the job which tasks you want to list.
            group_name: name of the group of tasks. Usually it's `group0`.
    
        Returns:
            An iterable collection of Task objects.
        """
        client = batch_v1.BatchServiceClient()
    
        return client.list_tasks(
            parent=f"projects/{project_id}/locations/{region}/jobs/{job_name}/taskGroups/{group_name}"
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=batchforgooglecloud). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
