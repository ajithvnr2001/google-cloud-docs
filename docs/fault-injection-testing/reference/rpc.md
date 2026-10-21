---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/
title: Fault Testing API \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:46.782110+00:00
---

# Fault Testing API  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Fault Testing API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: faulttesting.googleapis.com

The Service name `faulttesting.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.faulttesting.v1alpha.FaultTesting](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting)`

Methods  
---  
``[CreateExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExclusionWindow)`` |  Creates a new exclusion window.  
``[CreateExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperiment)`` |  Creates an `Experiment` and prepares it to run by identifying all cloud resources that will be affected.  
``[CreateExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperimentTemplate)`` |  Creates a new experiment template.  
``[CreateValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateValidation)`` |  Creates a new `Validation` dry run.  
``[DeleteExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExclusionWindow)`` |  Deletes an exclusion window.  
``[DeleteExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperiment)`` |  Deletes an `Experiment` record.  
``[DeleteExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperimentTemplate)`` |  Deletes an experiment template.  
``[DeleteValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteValidation)`` |  Deletes a record of a dry run.  
``[GetAffectedResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetAffectedResource)`` |  Gets the details of a specific cloud resource that is being or was affected by a particular `Experiment`.  
``[GetExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExclusionWindow)`` |  Get the details of an exclusion window.  
``[GetExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExperiment)`` |  Returns a single `Experiment` resource, including its current state and configuration.  
``[GetExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExperimentTemplate)`` |  Retrieves the details of a specific experiment template.  
``[GetValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetValidation)`` |  Retrieves the details of a specific `Validation` dry run.  
``[GetValidationResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetValidationResource)`` |  Gets the details of a specific `ValidationResource`.  
``[ListAffectedResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListAffectedResources)`` |  Lists all cloud resources that are being or were affected by a specific `Experiment`.  
``[ListExclusionWindows](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExclusionWindows)`` |  Lists all exclusion windows in a project and region, or all exclusion windows in a project in all regions if the location is given as "-".  
``[ListExperimentTemplates](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates)`` |  Lists all experiment templates in a specified project and location.  
``[ListExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExperiments)`` |  Lists all experiments in a specified project and location.  
``[ListValidationResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListValidationResources)`` |  Lists all cloud resources identified as potentially affected within a specific `Validation` dry run.  
``[ListValidations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListValidations)`` |  Lists all dry runs in a specified project and location.  
``[StartExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StartExclusionWindow)`` |  Starts or restarts an existing exclusion window.  
``[StartExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StartExperiment)`` |  Starts an existing `Experiment`.  
``[StopAllExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopAllExperiments)`` |  Stops all running experiments in a given location for a given project.  
``[StopExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopExclusionWindow)`` |  Stops an active exclusion window.  
``[StopExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopExperiment)`` |  Stops a running `Experiment`.  
``[UpdateExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExclusionWindow)`` |  Updates an exclusion window.  
``[UpdateExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExperimentTemplate)`` |  Updates an existing experiment template.  
  
## `[google.cloud.location.Locations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
``[GetLocation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation)`` |  Gets information about a location.  
``[ListLocations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations)`` |  Lists information about the supported locations for this service.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[CancelOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)`` |  Starts asynchronous cancellation on a long-running operation.  
``[DeleteOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)`` |  Deletes a long-running operation.  
``[GetOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
