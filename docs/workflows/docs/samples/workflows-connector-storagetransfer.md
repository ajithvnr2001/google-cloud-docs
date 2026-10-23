---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-storagetransfer/
title: Connector for Storage Transfer Service \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:11.648827+00:00
---

# Connector for Storage Transfer Service  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-storagetransfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Storage Transfer Service Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Storage Transfer Service within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Storage Transfer API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storagetransfer/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Storage Transfer Service connector:
    # Create source and sink Cloud Storage buckets and then create a transfer job
    # that transfers data from the source bucket to the sink bucket
    # Run the transfer job and then set the status of the job to "DELETED"
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - transfer_job_name: "transferJobs/example-transfer-job"
          - src_bucket_name: "SOURCE_BUCKET_NAME"  # replace SOURCE_BUCKET_NAME placeholder
          - sink_bucket_name: "SINK_BUCKET_NAME"  # replace SINK_BUCKET_NAME placeholder
    - create_source_bucket:
        call: googleapis.storage.v1.buckets.insert
        args:
          project: ${project_id}
          body:
            name: ${src_bucket_name}
    - create_sink_bucket:
        call: googleapis.storage.v1.buckets.insert
        args:
          project: ${project_id}
          body:
            name: ${sink_bucket_name}
    - create_transfer_job:
        call: googleapis.storagetransfer.v1.transferJobs.create
        args:
          body:
            name: ${transfer_job_name}
            description: "A job that transfers data from source bucket to sink bucket"
            projectId: ${project_id}
            transferSpec:
              gcsDataSink:
                bucketName: ${sink_bucket_name}
                path: ""
              gcsDataSource:
                bucketName: ${src_bucket_name}
                path: ""
            status: "DISABLED"
    - enable_transfer_job:
        call: googleapis.storagetransfer.v1.transferJobs.patch
        args:
          jobName: ${transfer_job_name}
          body:
            projectId: ${project_id}
            transferJob:
              status: "ENABLED"
    - run_transfer_job:
        call: googleapis.storagetransfer.v1.transferJobs.run
        args:
          jobName: ${transfer_job_name}
          body:
            projectId: ${project_id}
        result: r
    - delete_transfer_job:
        # Transfer jobs become eligible for garbage collection 30 days
        # after their status is set to DELETED
        call: googleapis.storagetransfer.v1.transferJobs.patch
        args:
          jobName: ${transfer_job_name}
          body:
            projectId: ${project_id}
            transferJob:
              status: "DELETED"
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
