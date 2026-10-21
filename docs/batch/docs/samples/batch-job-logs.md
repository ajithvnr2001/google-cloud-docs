---
url: https://docs.cloud.google.com/batch/docs/samples/batch-job-logs/
title: View logs from Cloud Logging for a job \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:47:35.839244+00:00
---

# View logs from Cloud Logging for a job  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/samples/batch-job-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Samples ](https://docs.cloud.google.com/batch/docs/samples)



#  View logs from Cloud Logging for a job Stay organized with collections  Save and categorize content based on your preferences. 

If the job has been set up to write logs to Cloud Logging, this sample retrieves its logs. Logs can provide information that is useful for analyzing your jobs. For example, logs can help you debug a failed job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Analyze a job using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=batchforgooglecloud). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
