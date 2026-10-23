---
url: https://docs.cloud.google.com/run/docs/managing/job-executions/
title: Manage job executions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:15.132847+00:00
---

# Manage job executions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/job-executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage job executions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view and delete job executions. To execute, cancel, or override a job configuration, see [Execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs).

## Required roles

To get the permissions that you need to manage Cloud Run jobs, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run job. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View job executions in your project

You can view a list of the job executions in your project using the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

To view the list of executions for a job, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to display the executions list.

  3. In the execution details page, select the execution you are interested in from the list. You can optionally filter by criteria.




###  gcloud 

  * To list all of the job executions for all jobs in your project, run the following command:
        
        gcloud run jobs executions list

  * To list only the executions for a specific job, run the following command:
        
        gcloud run jobs executions list --job JOB

Replace `JOB` with the name of the job you are filtering on.

For other ways to refine the returned list, including the use of filters, see [jobs executions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/jobs/executions/list).

  * To get the name of the latest execution for a specific job, use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format):
        
        gcloud run jobs describe JOB --format="value(status.latestCreatedExecution.name)"

Replace `JOB` with the name of the job you are filtering on.




Alternatively, to view the details of your latest job execution, see View job execution details.

### Client libraries

To list all of the job executions from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ExecutionsClient_ListExecutions)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient#com_google_cloud_run_v2_ExecutionsClient_listExecutions_com_google_cloud_run_v2_JobName_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.executionsclient#_google_cloud_run_v2_ExecutionsClient_listExecutions_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.executions.ExecutionsClient#google_cloud_run_v2_services_executions_ExecutionsClient_list_executions)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Executions-Rest-Client#Google__Cloud__Run__V2__Executions__Rest__Client_list_executions_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ExecutionsClient#_Google_Cloud_Run_V2_Client_ExecutionsClient__listExecutions__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ExecutionsClient#Google_Cloud_Run_V2_ExecutionsClient_ListExecutions_Google_Cloud_Run_V2_JobName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)



### REST API

To list job executions, send a `GET` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions/list).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB/executions

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to view job executions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



## View job execution details

You can view job execution details for the most recent 1,000 executions of a job using the [execution details pane](https://docs.cloud.google.com/run/docs/managing/job-executions). Older execution details are removed and are no longer visible in the execution details pane. However, the logs and monitoring data for older executions are still available in [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), subject to the retention policies for those products.

You can view more details about a job execution using the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

To view details for a specific job execution:

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the job details pane.

  3. Click the job execution you want to view. The execution details are shown in the right hand panel. See the **Tasks** , **Containers** , **Volumes** , **Networking** , **Security** , and **YAML** , tabs for more details.




###  gcloud 

To view details about a job execution, run the following commands:

  * To describe a specific job execution:
        
        gcloud run jobs executions describe EXECUTION_NAME

Replace `EXECUTION_NAME` with the name of the execution.

You can use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to format the output and to get additional information. For example as YAML:
        
        gcloud run jobs executions describe EXECUTION_NAME --format yaml

  * To describe the latest execution of a job:
        
        gcloud run jobs executions describe-latest --job=JOB

Replace `JOB` with the name of the job.




### Client libraries

To view job execution details from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ExecutionsClient_GetExecution)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient#com_google_cloud_run_v2_ExecutionsClient_getExecution_com_google_cloud_run_v2_ExecutionName_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.executionsclient#_google_cloud_run_v2_ExecutionsClient_getExecution_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.executions.ExecutionsClient#google_cloud_run_v2_services_executions_ExecutionsClient_get_execution)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Executions-Rest-Client#Google__Cloud__Run__V2__Executions__Rest__Client_get_execution_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ExecutionsClient#_Google_Cloud_Run_V2_Client_ExecutionsClient__getExecution__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ExecutionsClient#Google_Cloud_Run_V2_ExecutionsClient_GetExecution_Google_Cloud_Run_V2_ExecutionName_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view job execution details, send a `GET` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions/get).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB/executions/EXECUTION_NAME

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to view job execution details](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.
  * `EXECUTION_NAME`: the name of the job execution.



## Delete a job execution

You can delete a job execution, even during an execution. If you delete an execution, it stops the execution from continuing.

**Note:** In comparison, if you use the job execution [cancel](https://docs.cloud.google.com/run/docs/execute/jobs#cancel-job-execution) method to stop the current job execution, the job execution remains in the list of job executions.

Although a deleted execution does not appear in the list of executions, its logs continue to be available in [Cloud Logging](https://docs.cloud.google.com/run/docs/logging) for the remainder of the log retention period, and monitoring data continues to be available in [Cloud Monitoring](https://docs.cloud.google.com/run/docs/monitoring).

### Console

To delete a job execution:

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the job details pane.

  3. Select the job execution you want to delete.

  4. Under the **Actions** menu, click the ellipsis icon, then click **Delete**.

  5. If prompted to confirm the deletion, click **Confirm**.




###  gcloud 

To delete a job execution, follow these steps:

  1. Run the following command:
         
         gcloud run jobs executions delete EXECUTION_NAME

Replace `EXECUTION_NAME` with the name of the execution.

  2. If prompted to confirm, respond `y`. Upon success, a success message will be displayed.




### Client libraries

To delete a job execution from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ExecutionsClient_DeleteExecution)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient#com_google_cloud_run_v2_ExecutionsClient_deleteExecutionAsync_com_google_cloud_run_v2_DeleteExecutionRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.executionsclient#_google_cloud_run_v2_ExecutionsClient_deleteExecution_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.executions.ExecutionsClient#google_cloud_run_v2_services_executions_ExecutionsClient_delete_execution)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Executions-Rest-Client#Google__Cloud__Run__V2__Executions__Rest__Client_delete_execution_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ExecutionsClient#_Google_Cloud_Run_V2_Client_ExecutionsClient__deleteExecution__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ExecutionsClient#Google_Cloud_Run_V2_ExecutionsClient_DeleteExecution_Google_Cloud_Run_V2_DeleteExecutionRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To delete a job execution, send a `DELETE` HTTP request to request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions/delete).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X DELETE \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB/executions/EXECUTION_NAME

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to delete job executions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.
  * `EXECUTION_NAME`: the name of the job execution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
