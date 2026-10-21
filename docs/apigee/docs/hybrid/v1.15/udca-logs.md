---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/udca-logs/
title: UDCA logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:30:48.499501+00:00
---

# UDCA logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/udca-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  UDCA logs Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/udca-logshtml)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/udca-logshtml)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/udca-logshtml)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/udca-logshtml)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/udca-logshtml)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/udca-logshtml)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/udca-logshtml)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/udca-logshtml)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/udca-logshtml)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/udca-logshtml)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/udca-logshtml)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/udca-logshtml)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/udca-logshtml)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/udca-logshtml)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/udca-logshtml)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/udca-logshtml)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/udca-logshtml)



To troubleshoot the UDCA in Apigee hybrid, look at the log files. UDCA logs are written to `stdout/stderr` and can be viewed using the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) `logs` command.

On the Kubernetes administration machine, execute the following command:
    
    
    kubectl logs pod_name apigee-udca -n namespace

The following table lists common error messages that might appear in the UDCA log files and their meanings. Log messages will include a timestamp and often a stacktrace or other information to help you diagnose and fix the issue.

Entry Type | Log message | Meaning  
---|---|---  
Error | `Failed to create directory for dataset dataset_name` | The directory configured for the given dataset did not exist and the UDCA failed to create it. It could be a permission issue in the setup. This issue prevents UDCA from starting.  
Error | `Shutdown action was interrupted. It is possible that some data will be lost` | As part of a shutdown, UDCA tries to upload all files on disk. This message indicates that the shutdown took longer than expected and some data might not be uploaded and hence lost.  
Error | `Scheduled DatasetHandler for dataset dataset_name encountered an exception.` | An attempt to perform an action on the given dataset encountered an unexpected exception while polling the configured directory or while uploading the files.  
Error | `Upload failed for file filename. Max Retries exceeded! Moving dir to failed folder.` | The UDCA failed to upload the given file and moved the file to the dataset's `/failed` subdirectory.  
Error | `Re-queuing files from failed directory encountered an exception.` | The UDCA requeues files from the `/failed` directory after a successful upload. This ensures that the UDCA retry to upload files after network/upstream issues are resolved. This message indicates that UDCA experienced an error when trying to requeue the file.  
Error | `Shutting down datasetHandler encountered an exception.` | The UDCA experienced an exception when trying to shut down.  
Error | `Failed to move file from directory_name to directory_name.` | The UDCA encountered an exception while moving a file between sub-directories for internal lifecycle management.  
Error | `Failed to delete file filename.` | The UDCA encountered an exception while deleting a file after a successful upload.  
Error | `Failed to rename file from file_name to file_name.` | The UDCA encountered an exception while appending UUID to a file while renaming.  
Warning | `Received 429 - Too many Requests from upstream service. Skipping remaining files in this iteration and will retry again` | The UDCA received an error that it had exceeded its quota from an upstream service. As a result, the UDCA skipped the remaining files in this iteration and will retry in the next interval.  
Warning | `File upload failed for filename. error_message` | The UDCA failed to upload the given file due to the returned error. The UDCA will attempt to upload the file 3 times before moving it to the dataset's `/failed` subdirectory.  
Warning | `Request request_URI timed out. Aborting request` | The specified asynchronous request to upload the file timed out and was cancelled.  
Warning | `Request request_URI failed. Exception exception` | The specified asynchronous request failed with an exception.  
Warning | `Metrics Computation Failed: error_message` | The periodic computation of the UDCA's file system metrics encountered an exception.  
Warning | `Will attempt to upload api file file_name uncompressed` | The UDCA encountered an issue trying to compress the file before uploading. The uncompressed file will be uploaded in this case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
