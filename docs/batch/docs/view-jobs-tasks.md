---
url: https://docs.cloud.google.com/batch/docs/view-jobs-tasks/
title: View jobs and tasks \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:26.145376+00:00
---

# View jobs and tasks  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/view-jobs-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  View jobs and tasks Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view Batch jobs and tasks.

**Important:** You cannot view a job and its tasks after the job has been deleted from Batch, which automatically happens 60 days after a job finishes running. For more information, see [Delete jobs](https://docs.cloud.google.com/batch/docs/delete-job).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to view jobs and tasks, ask your administrator to grant you the Batch Job Viewer (`roles/batch.jobsViewer`) or Batch Job Editor (`roles/batch.jobsEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View your jobs

To view your jobs, select one of the following methods:

  * To see all the jobs in your project, view a list of your jobs.

  * To see all the configuration details of a specific job, view the details of a job.




### View a list of your jobs

You can view a list of jobs in the current project using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

###  Console 

  1. To view a list of jobs in the current project using the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

The list of jobs might be multiple pages. If you need to continue to the next page, click navigate_next **Next** at the bottom of the screen.

  2. Optional: If you want to filter the list of jobs, click filter_list **Filter**. Then, type or select a property and a value.

For example, to filter the list to only include jobs in a specific state, enter the following:
         
         Status:JOB_STATE
         

Replace `JOB_STATE` with a [job state](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State)—for example, `FAILED`.

**Note:** Some filtering options—for example, to only list jobs with one or more specific [labels](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels)—aren't supported in the Google Cloud console. For more filtering options, list jobs using the gcloud CLI or Batch API instead.



###  gcloud 

#### View all jobs

To view a list of jobs in the current project using the gcloud CLI, use the [`gcloud batch jobs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/list).
    
    
    gcloud batch jobs list
    

#### View a filtered list of jobs

Optionally, you can add one or more flags to view a filtered list of jobs:

  * To only view jobs in a specific location, include the `--location` flag.

  * To only view jobs based on a filter expression, specify the `--filter` flag.




For example, use the following command:
    
    
    gcloud batch jobs list \
        --location=LOCATION \
        --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where one or more jobs exist.

  * `FILTER_EXPRESSION`: a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) that defines the jobs that you want to list. The filter expression must define one or more property-value pairs that are separated by zero or more [boolean operators (`AND`, `OR` and `NOT`)](https://docs.cloud.google.com/logging/docs/view/building-queries#boolean-operators).

For example, see the following filter expressions:

    * **Filter based on job state:** To only view jobs that are in a specific state, use the following filter expression:
          
          status.state="JOB_STATE"
          

Replace `JOB_STATE` with a [job state](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State)—for example, `FAILED`.

    * **Filter based on[labels](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels):** Suppose that your project has defined the following custom labels:

      * To indicate jobs and their resources that are created by your research team when you view Cloud Billing reports, some of your jobs and their resources have a `team` label that is set to `research`.

      * To indicate time-sensitive workloads, some jobs have a `deadline` label, which is set to various values.

      * To indicate runnables that your development team has successfully tested, some runnables have a `tested` label that is set to `true`.

Then, you might specify the following filter expression:
    
    (allocationPolicy.labels.team=research) AND ((labels.deadline:*) OR (runnables.labels.tested=true))
    

This filter expression only lists jobs that meet all of the following criteria:

      * Jobs that are from the research team, which have a `team` label on the job's allocation policy that is set to `research`.

      * Jobs that meet at least one of the following criteria:

        * Jobs that are time-sensitive, which have a `deadline` label on the job that is set to any value.

        * Jobs that have at least one runnable that has been successfully tested, which are jobs that have at least one runnable with a `tested` label that is set to `true`.




###  API 

#### View all jobs

To view a list of jobs in the current project for a specific location using the Batch API, make a `GET` request to the [`jobs.list` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/list).
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the jobs exist.




#### View a filtered list of jobs

Optionally, you can specify the `filter` query parameter to view a filtered list of jobs based on a filter expression.

For example, make the following `GET` request:
    
    
    GET https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs?filter=FILTER_EXPRESSION
    

Replace `FILTER_EXPRESSION` with a [filter expression](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#body.QUERY_PARAMETERS.filter) that uses [URL-encoding](https://en.wikipedia.org/wiki/URL_encoding). The filter expression must define one or more property-value pairs that are separated by zero or more [boolean operators (`AND`, `OR` and `NOT`)](https://docs.cloud.google.com/logging/docs/view/building-queries#boolean-operators).

For example, see the following filter expressions:

  * **Filter based on job state:** To only view jobs that are in a specific state, use the following filter expression:
        
        status.state="JOB_STATE"
        

Replace `JOB_STATE` with a [job state](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State)—for example, `FAILED`.

  * **Filter based on[labels](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels):** Suppose that your project has defined the following custom labels:

    * To indicate jobs and their resources that are created by your research team when you view Cloud Billing reports, some of your jobs and their resources have a `team` label that is set to `research`.

    * To indicate time-sensitive workloads, some jobs have a `deadline` label, which is set to various values.

    * To indicate runnables that your development team has successfully tested, some runnables have a `tested` label that is set to `true`.

Then, you might specify the following filter expression:
    
    (allocationPolicy.labels.team%3Dresearch)%20AND%20((labels.deadline%3A*)%20OR%20(runnables.labels.tested%3Dtrue))
    

**Note:** The URL-encoded filter expression represents the following decoded filter expression:
    
    (allocationPolicy.labels.team=research) AND ((labels.deadline:*) OR (runnables.labels.tested=true))

This filter expression only lists jobs that meet all of the following criteria:

    * Jobs that are from the research team, which have a `team` label on the job's allocation policy that is set to `research`.

    * Jobs that meet at least one of the following criteria:

      * Jobs that are time-sensitive, which have a `deadline` label on the job that is set to any value.

      * Jobs that have at least one runnable that has been successfully tested, which are jobs that have at least one runnable with a `tested` label that is set to `true`.




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
    	"google.golang.org/api/iterator"
    )
    
    // Lists all jobs in the given project and region
    func listJobs(w io.Writer, projectID, region string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	req := &batchpb.ListJobsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, region),
    	}
    
    	var jobs []*batchpb.Job
    	it := batchClient.ListJobs(ctx, req)
    
    	for {
    		job, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("unable to list jobs: %w", err)
    		}
    		jobs = append(jobs, job)
    	}
    
    	fmt.Fprintf(w, "Jobs: %v\n", jobs)
    
    	return nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import java.io.IOException;
    
    public class ListJobs {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region hosting the jobs.
        String region = "europe-central2";
    
        listJobs(projectId, region);
      }
    
      // Get a list of all jobs defined in given region.
      public static void listJobs(String projectId, String region) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Construct the parent path of the job.
          String parent = String.format("projects/%s/locations/%s", projectId, region);
    
          for ([Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job : batchServiceClient.listJobs(parent).iterateAll()) {
            System.out.println(job.getName());
          }
          System.out.println("Listed all batch jobs.");
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
     * The region that hosts the job.
     */
    // const region = 'us-central-1';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    async function callListJobs() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${region}`,
      };
    
      // Run request
      const iterable = await batchClient.listJobsAsync(request);
      for await (const response of iterable) {
        console.log(response);
      }
    }
    
    await callListJobs();

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import batch_v1
    
    
    def list_jobs(project_id: str, region: str) -> Iterable[batch_v1.Job]:
        """
        Get a list of all jobs defined in given region.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region hosting the jobs.
    
        Returns:
            An iterable collection of Job object.
        """
        client = batch_v1.BatchServiceClient()
    
        return client.list_jobs(parent=f"projects/{project_id}/locations/{region}")
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id) {
        auto const parent = "projects/" + project_id + "/locations/" + location_id;
        // Initialize a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        int i = 0;
        for (auto job : client.ListJobs(parent)) {
          if (!job) throw std::move(job).status();
          std::cout << "Job[" << i++ << "]  " << job->DebugString() << "\n";
        }
      }

### View the details of a job

You can view the details a job in the current project using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

###  Console 

**Important:** To view _all_ information about a job, use the gcloud CLI, Batch API, or a client library instead.

To view the details of a job in the current project using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. In the **Job name** column, click the name of a job.

The **Job details** page opens.

The **Details** tab is open by default. For more information, click other tabs.




###  gcloud 

To view the details of a job in the current project using the gcloud CLI, use the [`gcloud batch jobs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/describe) with the `--location` flag.
    
    
    gcloud batch jobs describe JOB_NAME \
        --location=LOCATION
    

Replace the following:

  * `JOB_NAME`: the name of an existing job.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.




###  API 

To view the details of a job in the current project using the Batch API, make a `GET` request to the [`jobs.get` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/get).
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `JOB_NAME`: the name of an existing job.




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
    )
    
    // Retrieves the information about the specified job, most importantly its status
    func getJob(w io.Writer, projectID, region, jobName string) (*batchpb.Job, error) {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	req := &batchpb.GetJobRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/jobs/%s", projectID, region, jobName),
    	}
    
    	response, err := batchClient.GetJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("unable to get job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job info: %v\n", response)
    
    	return response, nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobName.html);
    import java.io.IOException;
    
    public class GetJob {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region hosts the job.
        String region = "europe-central2";
    
        // The name of the job you want to retrieve information about.
        String jobName = "JOB_NAME";
    
        getJob(projectId, region, jobName);
      }
    
      // Retrieve information about a Batch Job.
      public static void getJob(String projectId, String region, String jobName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              batchServiceClient.getJob(
                  [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobName.html).newBuilder()
                      .setProject(projectId)
                      .setLocation(region)
                      .setJob(jobName)
                      .build());
    
          System.out.printf("Retrieved the job: %s ", job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
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
     * The region that hosts the job.
     */
    // const region = 'us-central-1';
    /**
     * The name of the job you want to retrieve information about.
     */
    // const jobName = 'YOUR_JOB_NAME';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    async function callGetJob() {
      // Construct request
      const request = {
        name: `projects/${projectId}/locations/${region}/jobs/${jobName}`,
      };
    
      // Run request
      const response = await batchClient.getJob(request);
      console.log(response);
    }
    
    await callGetJob();

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import batch_v1
    
    
    def get_job(project_id: str, region: str, job_name: str) -> batch_v1.Job:
        """
        Retrieve information about a Batch Job.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region hosts the job.
            job_name: the name of the job you want to retrieve information about.
    
        Returns:
            A Job object representing the specified job.
        """
        client = batch_v1.BatchServiceClient()
    
        return client.get_job(
            name=f"projects/{project_id}/locations/{region}/jobs/{job_name}"
        )
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id) {
        auto const name = "projects/" + project_id + "/locations/" + location_id +
                          "/jobs/" + job_id;
        // Initialize a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.GetJob(name);
        if (!response) throw std::move(response).status();
        std::cout << "GetJob() succeeded with " << response->DebugString() << "\n";
      }

## View tasks

To view the tasks for one of your jobs, select one of the following methods:

  * To see all the tasks in a job or a job's task group, view a list of a job's tasks.

  * To see all the configuration details of a specific task, view the details of a task.




### View a list of a job's tasks

You can view a list of the tasks in a job or a job's task group using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

If you want to filter a list of tasks in a job or a job's task group—for example, to only list the tasks that have successfully finished running—you must use the gcloud CLI or Batch API.

###  Console 

To view a summary of a job's tasks using the Google Cloud console, view the details of a job to open the **Job details** page. Then, see the **Task details** section.

###  gcloud 

To view a list of the tasks in a job's tasks group using the gcloud CLI, use the [`gcloud batch tasks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/tasks/list) with the following flags:
    
    
    gcloud batch tasks list \
        --job=JOB_NAME \
        --location=LOCATION
    

Replace the following:

  * `JOB_NAME`: the name of an existing job.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.




Optionally, you can add the `--filter` flag to view a filtered list of tasks in a job's task group based on a filter expression.

For example, use the following command:
    
    
    gcloud batch tasks list \
        --job=example-job \
        --location=us-central1 \
        --filter="FILTER_EXPRESSION"
    

Replace `FILTER_EXPRESSION` with a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

For example, you can specify the following filter expression to only view the tasks in a job's task group that are running or have successfully finished running:
    
    
    STATE=RUNNING OR STATE=SUCCEEDED
    

###  API 

To view a list of tasks in a job's task group using the Batch API, make a `GET` request to the [`tasks.list` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs.taskGroups.tasks/list):
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME/taskGroups/TASK_GROUP_NAME/tasks
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `JOB_NAME`: the name of an existing job.

  * `TASK_GROUP_NAME`: the name of the task group that you want to view the details of. The value must be set to [`group0`](https://docs.cloud.google.com/batch/docs/get-started#restrictions).




Optionally, you can specify the `filter` query parameter to view a filtered list of tasks in a job's task group based on a filter expression.

For example, make the following `GET` request:
    
    
    GET https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs/example-job/taskGroups/group0/tasks?filter=FILTER_EXPRESSION
    

Replace `FILTER_EXPRESSION` with a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) that uses [URL-encoding](https://en.wikipedia.org/wiki/URL_encoding).

For example, you can specify the following filter expression to only view the tasks in a job's task group that are running or have successfully finished running:
    
    
    STATE=RUNNING%20OR%20STATE=SUCCEEDED
    

Note that the URL-encoded filter expression represents the following decoded filter expression:
    
    
    STATE=RUNNING OR STATE=SUCCEEDED
    

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
    

###  Java 

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

###  Node.js 

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

###  Python 

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
    
    

###  C++ 

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

### View the details of a task

You can view the details of a task using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

###  Console 

**Important:** To view _all_ information about a task, use the gcloud CLI, Batch API, or a client library instead.

To view the details of a task using the Google Cloud console, view the details of a job to open the **Job details** page. Then, see the **Task details** section.

###  gcloud 

To view the details of a task using the gcloud CLI, use the [`gcloud batch tasks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/tasks/describe) with the following flags:
    
    
    gcloud batch tasks describe TASK_INDEX \
      --location=LOCATION \
      --job=JOB_NAME \
      --task_group=TASK_GROUP_NAME
    

Replace the following:

  * `TASK_INDEX`: the index of the task that you want to view the details of. In a task group, the task index starts at 0 for the first task and increases by 1 with each additional task. For example, a task group that contains four tasks has the indexes `0`, `1`, `2`, and `3`.

  * `TASK_GROUP_NAME`: the name of the task group that contains the task that you want to view the details of. The value must be set to [`group0`](https://docs.cloud.google.com/batch/docs/get-started#restrictions).

  * `JOB_NAME`: the name of an existing job.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.




###  API 

To view the details of a task using the Batch API, make a `GET` request to the [`tasks.get` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs.taskGroups.tasks/get):
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME/taskGroups/TASK_GROUP_NAME/tasks/TASK_INDEX
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `JOB_NAME`: the name of an existing job.

  * `TASK_GROUP_NAME`: the name of the task group that contains the task that you want to view the details of. The value must be set to [`group0`](https://docs.cloud.google.com/batch/docs/get-started#restrictions).

  * `TASK_INDEX`: the index of the task that you want to view the details of. In a task group, the task index starts at 0 for the first task and increases by 1 with each additional task. For example, a task group that contains four tasks has the indexes `0`, `1`, `2`, an, `3`.




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
    

###  Java 

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

###  Node.js 

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

###  Python 

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
    
    

###  C++ 

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

## What's next

  * Learn about [troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).

  * Learn how to monitor and analyze jobs:

    * [View a job's history of status events](https://docs.cloud.google.com/batch/docs/view-status-events).

    * [Monitor and optimize job resources by viewing metrics](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

    * If you configured logs for a job, you can [analyze a job by using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).

    * If you've configured status notifications, you can [monitor a job using Pub/Sub notifications and analyze notifications using BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).

  * Learn how to manage jobs:

    * [Organize resources using labels](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels).

    * [Cancel jobs](https://docs.cloud.google.com/batch/docs/cancel-job).

    * [Export job information](https://docs.cloud.google.com/batch/docs/export-job-info).

    * [Delete jobs](https://docs.cloud.google.com/batch/docs/delete-job).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
