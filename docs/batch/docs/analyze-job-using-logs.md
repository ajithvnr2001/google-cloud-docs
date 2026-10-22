---
url: https://docs.cloud.google.com/batch/docs/analyze-job-using-logs/
title: Analyze a job using logs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:01.768739+00:00
---

# Analyze a job using logs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/analyze-job-using-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Analyze a job using logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable, generate, and view [logs](https://docs.cloud.google.com/logging/docs/overview) from [Cloud Logging](https://docs.cloud.google.com/logging/docs) for a Batch job.

You can use logs to get information that is useful for analyzing your jobs. For example, logs can help you debug failed jobs.

**Important:** You cannot view Cloud Logging logs after they are deleted, which happens automatically after their retention period. Learn more about [log retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) in the Cloud Logging documentation.

Notably, logs are only generated _after_ a job starts running and only if logging was enabled for the job. If you need to analyze a job without logs, [view status events](https://docs.cloud.google.com/batch/docs/view-status-events) instead.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to analyze a job using logs, ask your administrator to grant you the following IAM roles: 

     * To create a job: 
       * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
       * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To view logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Enable logging for a job

To allow logs to be generated for a job, enable logs from Cloud Logging when you create the job:

  * If you create a job using the Google Cloud console, logs from Cloud Logging are always enabled.
  * If you create a job using the gcloud CLI or the Batch API, logs from Cloud Logging are disabled by default. To enable logs from Cloud Logging, include the following configuration for the `logsPolicy` field while creating the job:
        
        {
            ...
            "logsPolicy": {
                "destination": "CLOUD_LOGGING"
            }
            ...
        }
        




## Write and generate logs for a job

When logs from Cloud Logging are enabled for a job, Cloud Logging automatically generates any of the logs that are written for the job. Specifically, Batch jobs can have the following log types:

  * _agent logs_ (`batch_agent_logs`): logs for activities from the Batch service agent.

Batch automatically writes agent logs for every job that has enabled logging.

  * _task logs_ (`batch_task_logs`): logs for any data that you've configured a job's runnables to write to the [standard output (`stdout`) stream or standard error (`stderr`) stream](https://en.wikipedia.org/wiki/Standard_streams).

You can optionally [write task logs](https://docs.cloud.google.com/batch/docs/write-task-logs) for each job that has enabled logging.




## View logs for a job

You can view a job's logs using the Google Cloud console, the gcloud CLI, Logging API, Go, Java, Python, or C++.

###  Console 

To view a job's logs using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. In the **Job name** column, click the name of a job. The **Job details** page opens.

  3. Click the **Logs** tab. Batch displays all logs associated with the job.

  4. Optional: To filter the logs do any of the following:

     * Enter a filter in the filter_list **Filter** field.

     * In the **Severity** list, select a [severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity).

     * Click open_in_new **View in Logs Explorer** to [build a query](https://docs.cloud.google.com/logging/docs/view/building-queries) in the Logs Explorer using the Batch filter parameters.




###  gcloud 

To view logs using the gcloud CLI, use the [`gcloud logging read` command](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries):
    
    
    gcloud logging read "QUERY"
    

where `QUERY` is a query for Batch logs that contains Batch filter parameters.

###  API 

To view logs using the Logging API, use the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list):
    
    
    POST https://logging.googleapis.com/v2/entries:list
    {
        "resourceNames": [
            "projects/PROJECT_ID"
        ],
        "filter": "QUERY"
        "orderBy": "timestamp desc"
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `QUERY`: a query for Batch logs that contains Batch filter parameters.



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
    	"cloud.google.com/go/logging"
    	"cloud.google.com/go/logging/logadmin"
    	"google.golang.org/api/iterator"
    )
    
    // Retrieve the logs written by the given job to Cloud Logging
    func printJobLogs(w io.Writer, projectID string, job *batchpb.Job) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	batchClient, err := batch.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	adminClient, err := logadmin.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("Failed to create logadmin client: %w", err)
    	}
    	defer adminClient.Close()
    
    	const name = "batch_task_logs"
    
    	iter := adminClient.Entries(ctx,
    		// Only get entries from the "batch_task_logs" log for the job with the given UID
    		logadmin.Filter(fmt.Sprintf(`logName = "projects/%s/logs/%s" AND labels.job_uid=%s`, projectID, name, job.Uid)),
    	)
    
    	var entries []*logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry)
    
    	for {
    		logEntry, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("unable to fetch log entry: %w", err)
    		}
    		entries = append(entries, logEntry)
    		fmt.Fprintf(w, "%s\n", logEntry.Payload)
    	}
    
    	fmt.Fprintf(w, "Successfully fetched %d log entries\n", len(entries))
    
    	return nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.logging.v2.[LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.html);
    import com.google.logging.v2.[ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest.html);
    import com.google.logging.v2.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry.html);
    import java.io.IOException;
    
    public class ReadJobLogs {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project hosting the job.
        String projectId = "YOUR_PROJECT_ID";
    
        // The job which logs you want to print.
        [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job = [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder().build();
    
        readJobLogs(projectId, job);
      }
    
      // Prints the log messages created by given job.
      public static void readJobLogs(String projectId, [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `loggingClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.html) loggingClient = [LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.html).create()) {
    
          [ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest.html) request = [ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest.html).newBuilder()
              .addResourceNames(String.format("projects/%s", projectId))
              .setFilter(String.format("labels.job_uid=%s", job.[getUid](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getUid__)()))
              .build();
    
          for ([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry.html) logEntry : loggingClient.listLogEntries(request).iterateAll()) {
            System.out.println(logEntry.getTextPayload());
          }
        }
      }
    }

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from typing import NoReturn
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    from google.cloud import logging
    
    
    def print_job_logs(project_id: str, job: [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)) -> NoReturn:
        """
        Prints the log messages created by given job.
    
        Args:
            project_id: name of the project hosting the job.
            job: the job which logs you want to print.
        """
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        log_client = logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)(project=project_id)
        logger = log_client.[logger](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_logger)("batch_task_logs")
    
        for log_entry in logger.list_entries(filter_=f"labels.job_uid={job.uid}"):
            print(log_entry.payload)
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    #include "google/cloud/logging/v2/logging_service_v2_client.h"
    #include "google/cloud/location.h"
    #include "google/cloud/project.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id) {
        auto const project = google::cloud::Project(project_id);
        auto const location = google::cloud::Location(project, location_id);
        auto const name = location.FullName() + "/jobs/" + job_id;
        auto batch = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto job = batch.GetJob(name);
        if (!job) throw std::move(job).status();
    
        auto logging = google::cloud::logging_v2::LoggingServiceV2Client(
            google::cloud::logging_v2::MakeLoggingServiceV2Connection());
        auto const log_name = project.FullName() + "/logs/batch_task_logs";
        google::logging::v2::ListLogEntriesRequest request;
        request.mutable_resource_names()->Add(project.FullName());
        request.set_filter("logName=\"" + log_name +
                           "\" labels.job_uid=" + job->uid());
        for (auto l : logging.ListLogEntries(request)) {
          if (!l) throw std::move(l).status();
          std::cout << l->text_payload() << "\n";
        }
      }

### Filter Batch logs

You can filter for Batch logs by writing a query that includes one or more of the following filter parameters and zero or more [boolean operators (`AND`, `OR` and `NOT`)](https://docs.cloud.google.com/logging/docs/view/building-queries#boolean-operators).

  * To filter for logs from a specific job, specify the job's unique ID (UID):
        
        labels.job_uid=JOB_UID
        

where `JOB_UID` is the UID of the job. To get a job's UID, [view the details the job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-describe-jobs).

  * To filter for a specific type of Batch logs, specify the log type:
        
        logName=projects/PROJECT_ID/logs/BATCH_LOG_TYPE
        

Replace the following:

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that you want to view logs for.
    * `BATCH_LOG_TYPE`: the type of Batch logs you want to view, either `batch_task_logs` for task logs or `batch_agent_logs` for agent logs.
  * To filter for logs with [custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events), specify that the log must define the `jsonPayload.batch/custom/event` field:
        
        jsonPayload.batch"/"custom"/"event!=NULL_VALUE
        

  * To filter for logs of one or more specific severities, specify the following [comparison](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comparisons):
        
        severityCOMPARISON_OPERATORSEVERITY_ENUM
        

Replace the following:

    * `COMPARISON_OPERATOR`: a [comparison operator](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comparison_operators)—for example, `>=`.
    * `SEVERITY_ENUM`: a [`LogSeverity` enum](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity), which describes the severity of a log—for example, `ERROR`.



For more filter options, see the [Cloud Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) documentation.

## What's next

  * Learn more about [troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn more about [Cloud Logging](https://docs.cloud.google.com/logging).
  * Learn how to [write task logs](https://docs.cloud.google.com/batch/docs/write-task-logs).
  * Learn how to [export job information](https://docs.cloud.google.com/batch/docs/export-job-info).
  * Learn how to [delete jobs](https://docs.cloud.google.com/batch/docs/delete-job).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
