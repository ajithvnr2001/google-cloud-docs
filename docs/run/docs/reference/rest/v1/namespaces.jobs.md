---
url: https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs
title: REST Resource: namespaces.jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:33.606406+00:00
---

# REST Resource: namespaces.jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  REST Resource: namespaces.jobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Job
    * JSON representation
  * JobSpec
    * JSON representation
  * ExecutionTemplateSpec
    * JSON representation
  * JobStatus
    * JSON representation
  * ExecutionReference
    * JSON representation
  * CompletionStatus
  * Methods



## Resource: Job

Job represents the configuration of a single job, which references a container image which is run to completion.

JSON representation  
---  
      
    
    {
      "apiVersion": string,
      "kind": string,
      "metadata": {
        object ([ObjectMeta](https://docs.cloud.google.com/run/docs/reference/rest/v1/ObjectMeta))
      },
      "spec": {
        object ([JobSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#JobSpec))
      },
      "status": {
        object ([JobStatus](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#JobStatus))
      }
    }  
  
Fields  
---  
`apiVersion` |  `string` Optional. APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.  
`kind` |  `string` Optional. Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.  
`metadata` |  `object (`[ObjectMeta](https://docs.cloud.google.com/run/docs/reference/rest/v1/ObjectMeta)`)` Optional. Standard object's metadata.  
`spec` |  `object (`[JobSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#JobSpec)`)` Optional. Specification of the desired behavior of a job.  
`status` |  `object (`[JobStatus](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#JobStatus)`)` Output only. Current status of a job.  
  
## JobSpec

JobSpec describes how the job will look.

JSON representation  
---  
      
    
    {
      "template": {
        object ([ExecutionTemplateSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#ExecutionTemplateSpec))
      },
    
      // Union field create_execution can be only one of the following:
      "startExecutionToken": string,
      "runExecutionToken": string
      // End of list of possible types for union field create_execution.
    }  
  
Fields  
---  
`template` |  `object (`[ExecutionTemplateSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#ExecutionTemplateSpec)`)` Optional. Describes the execution that will be created when running a job.  
Union field `create_execution`.`create_execution` can be only one of the following:  
`startExecutionToken` |  `string` A unique string used as a suffix for creating a new execution. The Job will become ready when the execution is successfully started. The sum of job name and token length must be fewer than 63 characters.  
`runExecutionToken` |  `string` A unique string used as a suffix for creating a new execution. The Job will become ready when the execution is successfully completed. The sum of job name and token length must be fewer than 63 characters.  
  
## ExecutionTemplateSpec

ExecutionTemplateSpec describes the metadata and spec an Execution should have when created from a job.

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([ObjectMeta](https://docs.cloud.google.com/run/docs/reference/rest/v1/ObjectMeta))
      },
      "spec": {
        object ([ExecutionSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/ExecutionSpec))
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[ObjectMeta](https://docs.cloud.google.com/run/docs/reference/rest/v1/ObjectMeta)`)` Optional. Optional metadata for this Execution, including labels and annotations.The following annotation keys set properties of the created execution:

  * `run.googleapis.com/cloudsql-instances` sets Cloud SQL connections. Multiple values should be comma separated.
  * `run.googleapis.com/vpc-access-connector` sets a Serverless VPC Access connector.
  * `run.googleapis.com/vpc-access-egress` sets VPC egress. Supported values are `all-traffic`, `all` (deprecated), and `private-ranges-only`. `all-traffic` and `all` provide the same functionality. `all` is deprecated but will continue to be supported. Prefer `all-traffic`.

  
`spec` |  `object (`[ExecutionSpec](https://docs.cloud.google.com/run/docs/reference/rest/v1/ExecutionSpec)`)` Required. ExecutionSpec holds the desired configuration for executions of this job.  
  
## JobStatus

JobStatus represents the current state of a Job.

JSON representation  
---  
      
    
    {
      "observedGeneration": integer,
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/run/docs/reference/rest/v1/Condition))
        }
      ],
      "executionCount": integer,
      "latestCreatedExecution": {
        object ([ExecutionReference](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#ExecutionReference))
      }
    }  
  
Fields  
---  
`observedGeneration` |  `integer` The 'generation' of the job that was last processed by the controller.  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/run/docs/reference/rest/v1/Condition)`)` Conditions communicate information about ongoing/complete reconciliation processes that bring the "spec" inline with the observed state of the world.Job-specific conditions include:

  * `Ready`: `True` when the job is ready to be executed.

  
`executionCount` |  `integer` Number of executions created for this job.  
`latestCreatedExecution` |  `object (`[ExecutionReference](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#ExecutionReference)`)` A pointer to the most recently created execution for this job. This is set regardless of the eventual state of the execution.  
  
## ExecutionReference

Reference to an Execution. Use /Executions.GetExecution with the given name to get full execution including the latest status.

JSON representation  
---  
      
    
    {
      "name": string,
      "creationTimestamp": string,
      "completionTimestamp": string,
      "deletionTimestamp": string,
      "completionStatus": enum ([CompletionStatus](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#CompletionStatus))
    }  
  
Fields  
---  
`name` |  `string` Optional. Name of the execution.  
`creationTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Creation timestamp of the execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completionTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Completion timestamp of the execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deletionTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The read-only soft deletion timestamp of the execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completionStatus` |  `enum (`[CompletionStatus](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs#CompletionStatus)`)` Optional. Status for the execution completion.  
  
## CompletionStatus

Possible execution completion status.

Enums  
---  
`COMPLETION_STATUS_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`EXECUTION_SUCCEEDED` | Job execution has succeeded.  
`EXECUTION_FAILED` | Job execution has failed.  
`EXECUTION_RUNNING` | Job execution is running normally.  
`EXECUTION_PENDING` | Waiting for backing resources to be provisioned.  
`EXECUTION_CANCELLED` | Job execution has been cancelled by the user.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/create)`

|  Create a job.  
  
### `[delete](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/delete)`

|  Delete a job.  
  
### `[get](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/get)`

|  Get information about a job.  
  
### `[list](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/list)`

|  List jobs.  
  
### `[replaceJob](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/replaceJob)`

|  Replace a job.  
  
### `[run](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/run)`

|  Trigger creation of a new execution of this job.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-24 UTC."],[],[]] 
