---
url: https://docs.cloud.google.com/run/docs/managing/jobs/
title: Manage jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:46.191923+00:00
---

# Manage jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage jobs Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run lets you view jobs, view their details, and delete jobs throughout their lifecycle. To create a job, see [create jobs](https://docs.cloud.google.com/run/docs/create-jobs). To execute a job, see [Execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs).

## Required roles

To get the permissions that you need to manage Cloud Run jobs, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run job. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View jobs in your project

You can view a list of the jobs in your project using the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Optional: Filter the job by one of the criteria in the menu, such as job name, execution time, or region.




###  gcloud 

To list all jobs in your project, run the following command:
    
    
    gcloud run jobs list

To filter jobs by region, run the following command:
    
    
    gcloud run jobs list --region REGION

Replace `REGION` with the name of the region you want to filter—for example `europe-west1`.

For other ways to refine the returned list, including the use of filters, see [jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/jobs/list).

### Client libraries

To view jobs in your project from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_JobsClient_ListJobs)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.JobsClient#com_google_cloud_run_v2_JobsClient_listJobs_com_google_cloud_run_v2_ListJobsRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.jobsclient#_google_cloud_run_v2_JobsClient_listJobs_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.jobs.JobsClient#google_cloud_run_v2_services_jobs_JobsClient_list_jobs)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client#Google__Cloud__Run__V2__Jobs__Client_list_jobs_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.JobsClient#_Google_Cloud_Run_V2_Client_JobsClient__listJobs__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.JobsClient#Google_Cloud_Run_V2_JobsClient_ListJobs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view the list of jobs in your project, send a `GET` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/list).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to view jobs](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.



## View job details

You can view more details about a job using the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Locate the job you are interested in.

  3. Click the job to display the job details page.

  4. Navigate between the **History** , **Logs** , **Metrics** , and **YAML** tabs:

     * **History** shows information about the tasks in the job execution.
     * **Logs** shows the logs information.
     * **Metrics** shows information about the job executions.
     * **YAML** shows the configuration of the job in YAML format.



###  gcloud 

To view details about a job, run the following command:
    
    
    gcloud run jobs describe  JOB

Replace `JOB` with the name of the job.

### Client libraries

To view details about a job from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_JobsClient_GetJob)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.JobsClient#com_google_cloud_run_v2_JobsClient_getJob_com_google_cloud_run_v2_GetJobRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.jobsclient#_google_cloud_run_v2_JobsClient_getJob_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.jobs.JobsClient#google_cloud_run_v2_services_jobs_JobsClient_get_job)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client#Google__Cloud__Run__V2__Jobs__Client_get_job_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.JobsClient#_Google_Cloud_Run_V2_Client_JobsClient__getJob__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.JobsClient#Google_Cloud_Run_V2_JobsClient_GetJob_Google_Cloud_Run_V2_GetJobRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view details about a job, send a `GET` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/get).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to view job details](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



## Delete a job

Deleting a job terminates all the job executions in progress and all running container instances.

Although a deleted job no longer appears in the list of jobs, its logs continue to be available in [Cloud Logging](https://docs.cloud.google.com/run/docs/logging) for the remainder of the log retention period, and monitoring data continues to be available in [Cloud Monitoring](https://docs.cloud.google.com/run/docs/monitoring).

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Select the job.

  3. Click **Delete**.

  4. Click **Confirm**




###  gcloud 

To delete a job, run the following command:
    
    
    gcloud run jobs delete JOB

Replace `JOB` with the name of the job.

If prompted to confirm, respond `y`. Upon completion, a success message will be displayed.

### Client libraries

To delete a job from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_JobsClient_DeleteJob)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.JobsClient#com_google_cloud_run_v2_JobsClient_deleteJobAsync_com_google_cloud_run_v2_DeleteJobRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.jobsclient#_google_cloud_run_v2_JobsClient_deleteJob_member_3_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.jobs.JobsClient#google_cloud_run_v2_services_jobs_JobsClient_delete_job)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client#Google__Cloud__Run__V2__Jobs__Client_delete_job_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.JobsClient#_Google_Cloud_Run_V2_Client_JobsClient__deleteJob__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.JobsClient#Google_Cloud_Run_V2_JobsClient_DeleteJob_Google_Cloud_Run_V2_DeleteJobRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To delete a job, send a `DELETE` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/delete).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X DELETE \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to delete jobs](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
