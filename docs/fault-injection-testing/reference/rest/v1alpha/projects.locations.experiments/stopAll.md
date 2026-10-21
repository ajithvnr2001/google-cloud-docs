---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stopAll/
title: Method: projects.locations.experiments.stopAll \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:44.436954+00:00
---

# Method: projects.locations.experiments.stopAll  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stopAll/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Method: projects.locations.experiments.stopAll Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Stops all running experiments in a given location for a given project. This method initiates the process of reverting any changes made by the experiments, returning the affected resources to their normal state. The `Experiment` states will transition to `REVERTING` and then to `COMPLETED`.

Returns an RPC error if it can't list experiments at all. Otherwise, it lists and stops all experiments it can, and returns a response including success count and a list of errors. If there are no experiments to stop, it returns successfully with an empty response message.

### HTTP request

`POST https://faulttesting.googleapis.com/v1alpha/{parent=projects/*/locations/*}/experiments:stopAll`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location where all experiments will be stopped. Format: `projects/{projectId}/locations/{location}`.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[FaultTesting.StopAllExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stopAll#google.cloud.faulttesting.v1alpha.FaultTesting.StopAllExperiments)`. Response is a complete success only if `errors` is empty.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "stoppedExperimentsCount": integer,
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Status))
        }
      ]
    }  
  
Fields  
---  
`stoppedExperimentsCount` |  `integer` The number of experiments that were stopped. These experiments are in reachable locations with statuses that allows them to be stopped, and did not get an error from `experiments.stop`.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Status)`)` Errors that occurred while listing or stopping experiments. Each experiment that fails the internal `experiments.stop` call will have an entry in this list.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experiments.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
