---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha
title: Package google.cloud.faulttesting.v1alpha \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:48.222131+00:00
---

# Package google.cloud.faulttesting.v1alpha  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Package google.cloud.faulttesting.v1alpha Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[FaultTesting](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting)` (interface)
  * `[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Action)` (message)
  * `[AffectedResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.AffectedResource)` (message)
  * `[CloudSQLFailover](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CloudSQLFailover)` (message)
  * `[CreateExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExclusionWindowRequest)` (message)
  * `[CreateExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExperimentRequest)` (message)
  * `[CreateExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExperimentTemplateRequest)` (message)
  * `[CreateValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateValidationRequest)` (message)
  * `[DeleteExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExclusionWindowRequest)` (message)
  * `[DeleteExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExperimentRequest)` (message)
  * `[DeleteExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExperimentTemplateRequest)` (message)
  * `[DeleteValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteValidationRequest)` (message)
  * `[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)` (message)
  * `[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)` (message)
  * `[Experiment.EndReason](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment.EndReason)` (enum)
  * `[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)` (message)
  * `[GCEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GCEFailCompute)` (message)
  * `[GKEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GKEFailCompute)` (message)
  * `[GetAffectedResourceRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetAffectedResourceRequest)` (message)
  * `[GetExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExclusionWindowRequest)` (message)
  * `[GetExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExperimentRequest)` (message)
  * `[GetExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExperimentTemplateRequest)` (message)
  * `[GetValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetValidationRequest)` (message)
  * `[GetValidationResourceRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetValidationResourceRequest)` (message)
  * `[HTTPAbort](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.HTTPAbort)` (message)
  * `[HTTPDelay](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.HTTPDelay)` (message)
  * `[InstanceList](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.InstanceList)` (message)
  * `[L7LBHTTPFault](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.L7LBHTTPFault)` (message)
  * `[ListAffectedResourcesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListAffectedResourcesRequest)` (message)
  * `[ListAffectedResourcesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListAffectedResourcesResponse)` (message)
  * `[ListExclusionWindowsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExclusionWindowsRequest)` (message)
  * `[ListExclusionWindowsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExclusionWindowsResponse)` (message)
  * `[ListExperimentTemplatesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentTemplatesRequest)` (message)
  * `[ListExperimentTemplatesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentTemplatesResponse)` (message)
  * `[ListExperimentsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentsRequest)` (message)
  * `[ListExperimentsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentsResponse)` (message)
  * `[ListValidationResourcesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationResourcesRequest)` (message)
  * `[ListValidationResourcesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationResourcesResponse)` (message)
  * `[ListValidationsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationsRequest)` (message)
  * `[ListValidationsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationsResponse)` (message)
  * `[MigElement](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.MigElement)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.OperationMetadata)` (message)
  * `[StartExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StartExclusionWindowRequest)` (message)
  * `[StartExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StartExperimentRequest)` (message)
  * `[State](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State)` (enum)
  * `[StopAllExperimentsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopAllExperimentsRequest)` (message)
  * `[StopAllExperimentsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopAllExperimentsResponse)` (message)
  * `[StopExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopExclusionWindowRequest)` (message)
  * `[StopExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopExperimentRequest)` (message)
  * `[UpdateExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.UpdateExclusionWindowRequest)` (message)
  * `[UpdateExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.UpdateExperimentTemplateRequest)` (message)
  * `[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Validation)` (message)
  * `[ValidationResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ValidationResource)` (message)



## FaultTesting

Service for managing experiments in Fault Injection Testing.

CreateExclusionWindow  
---  
` rpc CreateExclusionWindow(`[CreateExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExclusionWindowRequest)`) returns (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)`) ` Creates a new exclusion window. Once created, an exclusion window must be started with `StartExclusionWindow` to take effect.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateExperiment  
---  
` rpc CreateExperiment(`[CreateExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExperimentRequest)`) returns (`[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)`) ` Creates an `Experiment` and prepares it to run by identifying all cloud resources that will be affected. The `Experiment` starts in the `PREPARING` state and transitions to `PREPARED` once the resources are identified. You can then list these resources using the [`list` method for `AffectedResources`](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/list). To execute the `Experiment`, call [`start`](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/start) on the `Experiment` after it reaches the `PREPARED` state.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experiments.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateExperimentTemplate  
---  
` rpc CreateExperimentTemplate(`[CreateExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateExperimentTemplateRequest)`) returns (`[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)`) ` Creates a new experiment template. You can use this template to create multiple `Experiment` instances.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experimentTemplates.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateValidation  
---  
` rpc CreateValidation(`[CreateValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CreateValidationRequest)`) returns (`[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Validation)`) ` Creates a new `Validation` dry run. This process involves analyzing the provided `Action` to identify all the Google Cloud resources that match the targeting criteria. You can view the results by listing the `ValidationResource` children of the `Validation` dry run. The `Validation` dry run starts in the `PREPARING` state and transitions to `COMPLETED` once the analysis is finished.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.validations.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteExclusionWindow  
---  
` rpc DeleteExclusionWindow(`[DeleteExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExclusionWindowRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an exclusion window.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteExperiment  
---  
` rpc DeleteExperiment(`[DeleteExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExperimentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an `Experiment` record. The `Experiment` must be in a `COMPLETED` state before it can be deleted.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experiments.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteExperimentTemplate  
---  
` rpc DeleteExperimentTemplate(`[DeleteExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteExperimentTemplateRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an experiment template.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experimentTemplates.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteValidation  
---  
` rpc DeleteValidation(`[DeleteValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.DeleteValidationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a record of a dry run.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.validations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAffectedResource  
---  
` rpc GetAffectedResource(`[GetAffectedResourceRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetAffectedResourceRequest)`) returns (`[AffectedResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.AffectedResource)`) ` Gets the details of a specific cloud resource that is being or was affected by a particular `Experiment`. The response includes the resource's state within the `Experiment`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.affectedResources.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetExclusionWindow  
---  
` rpc GetExclusionWindow(`[GetExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExclusionWindowRequest)`) returns (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)`) ` Get the details of an exclusion window.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetExperiment  
---  
` rpc GetExperiment(`[GetExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExperimentRequest)`) returns (`[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)`) ` Returns a single `Experiment` resource, including its current state and configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experiments.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetExperimentTemplate  
---  
` rpc GetExperimentTemplate(`[GetExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetExperimentTemplateRequest)`) returns (`[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)`) ` Retrieves the details of a specific experiment template.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experimentTemplates.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetValidation  
---  
` rpc GetValidation(`[GetValidationRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetValidationRequest)`) returns (`[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Validation)`) ` Retrieves the details of a specific `Validation` dry run.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.validations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetValidationResource  
---  
` rpc GetValidationResource(`[GetValidationResourceRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GetValidationResourceRequest)`) returns (`[ValidationResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ValidationResource)`) ` Gets the details of a specific `ValidationResource`. This field shows a resource that was flagged as potentially affected by the `Action` defined in the parent `Validation`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.validationResources.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAffectedResources  
---  
` rpc ListAffectedResources(`[ListAffectedResourcesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListAffectedResourcesRequest)`) returns (`[ListAffectedResourcesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListAffectedResourcesResponse)`) ` Lists all cloud resources that are being or were affected by a specific `Experiment`. This method is useful for seeing the scope of an `Experiment` and the status of each resource involved.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.affectedResources.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListExclusionWindows  
---  
` rpc ListExclusionWindows(`[ListExclusionWindowsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExclusionWindowsRequest)`) returns (`[ListExclusionWindowsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExclusionWindowsResponse)`) ` Lists all exclusion windows in a project and region, or all exclusion windows in a project in all regions if the location is given as "-".

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListExperimentTemplates  
---  
` rpc ListExperimentTemplates(`[ListExperimentTemplatesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentTemplatesRequest)`) returns (`[ListExperimentTemplatesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentTemplatesResponse)`) ` Lists all experiment templates in a specified project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experimentTemplates.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListExperiments  
---  
` rpc ListExperiments(`[ListExperimentsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentsRequest)`) returns (`[ListExperimentsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListExperimentsResponse)`) ` Lists all experiments in a specified project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experiments.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListValidationResources  
---  
` rpc ListValidationResources(`[ListValidationResourcesRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationResourcesRequest)`) returns (`[ListValidationResourcesResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationResourcesResponse)`) ` Lists all cloud resources identified as potentially affected within a specific `Validation` dry run.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.validationResources.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListValidations  
---  
` rpc ListValidations(`[ListValidationsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationsRequest)`) returns (`[ListValidationsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ListValidationsResponse)`) ` Lists all dry runs in a specified project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.validations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StartExclusionWindow  
---  
` rpc StartExclusionWindow(`[StartExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StartExclusionWindowRequest)`) returns (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)`) ` Starts or restarts an existing exclusion window. This method sets `start_time` to the current time and `end_time` to current time plus the duration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
StartExperiment  
---  
` rpc StartExperiment(`[StartExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StartExperimentRequest)`) returns (`[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)`) ` Starts an existing `Experiment`. The `Experiment` must already be in the `PREPARED` state. This method initiates the fault injection process. The `Experiment` state will transition to `INJECTING` and then to `INJECTED` once the fault is active.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experiments.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StopAllExperiments  
---  
` rpc StopAllExperiments(`[StopAllExperimentsRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopAllExperimentsRequest)`) returns (`[StopAllExperimentsResponse](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopAllExperimentsResponse)`) ` Stops all running experiments in a given location for a given project. This method initiates the process of reverting any changes made by the experiments, returning the affected resources to their normal state. The `Experiment` states will transition to `REVERTING` and then to `COMPLETED`.Returns an RPC error if it can't list experiments at all. Otherwise, it lists and stops all experiments it can, and returns a response including success count and a list of errors. If there are no experiments to stop, it returns successfully with an empty response message.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experiments.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StopExclusionWindow  
---  
` rpc StopExclusionWindow(`[StopExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopExclusionWindowRequest)`) returns (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)`) ` Stops an active exclusion window. This method sets `end_time` to the current time.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
StopExperiment  
---  
` rpc StopExperiment(`[StopExperimentRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.StopExperimentRequest)`) returns (`[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)`) ` Stops a running `Experiment`. This method initiates the process of reverting any changes made by the `Experiment`, returning the affected resources to their normal state. The `Experiment` state will transition to `REVERTING` and then to `COMPLETED`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experiments.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateExclusionWindow  
---  
` rpc UpdateExclusionWindow(`[UpdateExclusionWindowRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.UpdateExclusionWindowRequest)`) returns (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)`) ` Updates an exclusion window.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateExperimentTemplate  
---  
` rpc UpdateExperimentTemplate(`[UpdateExperimentTemplateRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.UpdateExperimentTemplateRequest)`) returns (`[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)`) ` Updates an existing experiment template.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `faulttesting.experimentTemplates.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## Action

The action to be performed by the experiment.

Fields  
---  
Union field `action`. Details about the fault-injection action. `action` can be only one of the following:  
`cloud_sql_failover` |  `[CloudSQLFailover](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.CloudSQLFailover)` Specifies a CloudSQLFailover action.  
`l7_lb_http_fault` |  `[L7LBHTTPFault](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.L7LBHTTPFault)` Specifies an L7LBHTTPFault action.  
`gce_fail_compute` |  `[GCEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GCEFailCompute)` Specifies a GCEFailCompute action.  
`gke_fail_compute` |  `[GKEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.GKEFailCompute)` Specifies a GKEFailCompute action.  
  
## AffectedResource

Represents a specific Google Cloud resource, like a virtual machine or database that is targeted by an experiment.

Fields  
---  
`name` |  `string` Identifier. Unique identifier for this record, linking it to a specific experiment and resource. Format: `projects/{project_id}/locations/{location}/experiments/{experiment_id}/affectedResources/{affected_resource_id}`.  
`display_name` |  `string` Optional. A human-readable name for the affected resource record.  
`affected_resource_uri` |  `string` Required. The full unique address (URI) of the Google Cloud resource affected by this `Experiment`. Example: the full path to a specific Compute Engine instance.  
`cloud_console_path` |  `string` Output only. A direct link to view this specific resource in the Google Cloud Console.  
`state` |  `[State](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State)` The current state of this resource within the experiment. Example: `PREPARING`, `INJECTED`, `COMPLETED`.  
`state_message` |  `string` A plain-language explanation of what is currently happening with this resource in the experiment.  
`error` |  `[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.rpc#google.rpc.Status)` Output only. Details of any error that occurred while setting up, running, or stopping the experiment on this specific resource. Empty if no errors occurred.  
  
## CloudSQLFailover

CloudSQLFailover causes a Cloud SQL primary instance to fail over to another instance.

Fields  
---  
`instance` |  `string` Required. The identifying name of the Cloud SQL instance to fail over. Format: `projects/{project}/instances/{instance}`  
  
## CreateExclusionWindowRequest

Request message for `[FaultTesting.CreateExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExclusionWindow)`.

Fields  
---  
`parent` |  `string` Required. The project and location where the exclusion window will be created. Format: `projects/{project}/locations/{location}`.  
`exclusion_window_id` |  `string` Required. The ID to use for the `exclusion_window`, which will become the final component of the `exclusion_window`'s resource name. Required.This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Must start with a letter and cannot end with a hyphen.  
`exclusion_window` |  `[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)` Required. The exclusion window to create.  
  
## CreateExperimentRequest

Request message for `[FaultTesting.CreateExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperiment)`.

Fields  
---  
`parent` |  `string` Required. The project and location where the experiment will be created. Format: `projects/{projectId}/locations/{location}`.  
`experiment_id` |  `string` Optional. The ID to use for the `Experiment`, which will become the final component of the resource name. If not provided, a UUID will be generated. This value should be 4-63 characters, start with a letter or number, end with a letter or number, and contain only lowercase letters, numbers, and hyphens.  
`experiment` |  `[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)` Required. The experiment to create. The request body contains an instance of `Experiment`.  
  
## CreateExperimentTemplateRequest

Request message for `[FaultTesting.CreateExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperimentTemplate)`.

Fields  
---  
`parent` |  `string` Required. The project and location where this experiment template will be created. Format: `projects/{projectId}/locations/{location}`.  
`experiment_template_id` |  `string` Optional. The ID to use for the experiment template, which will become the final component of the resource name. This value should be 4-63 characters, start with a letter, end with a letter or number, and contain only lowercase letters, numbers, and hyphens.  
`experiment_template` |  `[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)` Required. The experiment template to create. The request body contains an instance of `ExperimentTemplate`.  
  
## CreateValidationRequest

Request message for `[FaultTesting.CreateValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.CreateValidation)`.

Fields  
---  
`parent` |  `string` Required. The project and location where this dry run will be created. Format: `projects/{projectId}/locations/{location}`.  
`validation_id` |  `string` Optional. The ID to use for the dry run, which will become the final component of the resource name. If not provided, a UUID will be generated. This value should be 4-63 characters, start with a letter or number, end with a letter or number, and contain only lowercase letters, numbers, and hyphens.  
`validation` |  `[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Validation)` Required. The dry run to create. The request body contains an instance of `Validation`.  
  
## DeleteExclusionWindowRequest

Request message for `[FaultTesting.DeleteExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExclusionWindow)`.

Fields  
---  
`name` |  `string` Required. The name of the exclusion window to delete. Format: `projects/{project}/locations/{location}/exclusionWindows/{exclusion_window}`.  
  
## DeleteExperimentRequest

Request message for `[FaultTesting.DeleteExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperiment)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment to delete. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
`force` |  `bool` Optional. Should always be set to true. If set to `true`, any affected resources under this experiment will also be deleted. Otherwise, the request will only work if the experiment has no affected resources.  
  
## DeleteExperimentTemplateRequest

Request message for `[FaultTesting.DeleteExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperimentTemplate)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment template to delete. Format: `projects/{projectId}/locations/{location}/experimentTemplates/{experimentTemplateId}`.  
  
## DeleteValidationRequest

Request message for `[FaultTesting.DeleteValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.DeleteValidation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the dry run to delete. Format: `projects/{projectId}/locations/{location}/validations/{validationId}`.  
`force` |  `bool` Optional. Should always be set to true. If set to true, any `ValidationResource`s under this `Validation` will also be deleted. Otherwise, the request will only work if the `Validation` has no `ValidationResource`s.  
  
## ExclusionWindow

A time period during which new fault injection experiments are blocked from starting.

Fields  
---  
`name` |  `string` Identifier. The resource name of the exclusion window. Format: `projects/{project}/locations/{location}/exclusionWindows/{exclusion_window}`  
`description` |  `string` Optional. Description of the exclusion window's purpose (for example, "Black Friday freeze"). Max length is 2000 characters.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. The length of time the exclusion window remains active once started. While active, new experiments are blocked in the region. Specified as a duration (for example, "86400s" for 24 hours).  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the exclusion window was started. This field is empty if the window has not been started.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the exclusion window expires. This field is empty if the window has not been started.  
  
## Experiment

Represents a single fault injection experiment where faults are deliberately introduced to your cloud resources to see how your application responds.

Fields  
---  
`name` |  `string` Identifier. Unique identifier for the experiment. Format: `projects/{project_id}/locations/{location}/experiments/{experiment_id}`.  
`display_name` |  `string` Optional. A human-readable name of the experiment.  
`description` |  `string` Optional. Notes or details to describe the purpose or context of the experiment. Minimum length is 0, maximum length is 2000.  
`experiment_template` |  `string` Required. The unique identifier of the reusable experiment template used to configure the experiment. This field determines the type of fault, target, and duration. Format: `projects/{project_id}/locations/{location}/experimentTemplates/{experimentTemplateId}`.  
`template_display_name` |  `string` Output only. The human-readable name of the experiment template used for the experiment. Minimum length is 0, maximum length is 1000.  
`template_description` |  `string` Output only. The description from the experiment template used for the experiment. Minimum length is 0, maximum length is 2000.  
`template_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The planned duration of the experiment, as defined in the experiment template. Minimum duration is 1 minute, maximum is 10 days.  
`effective_action` |  `[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Action)` Output only. The specific fault that was introduced during the experiment. Examples: Triggering a database failover, adding delays to web requests. This field comes from the experiment template.  
`state` |  `[State](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State)` Output only. The current state of the experiment. Example: `PREPARING`, `INJECTED`, `COMPLETED`.  
`end_reason` |  `[EndReason](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment.EndReason)` Output only. Why the experiment stopped. Example: It finished normally, or was cancelled by a user.  
`end_notes` |  `string` Output only. Optional user-added notes explaining why the experiment was stopped, particularly if it was manually cancelled.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when the experiment record was created.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when the fault injection actually began.  
`state_update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when the experiment's state was last updated.  
`stop_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when the experiment entered the REVERTING state.  
  
## EndReason

The reason why an experiment concluded. String values are used in JSON.

Enums  
---  
`END_REASON_UNSPECIFIED` | The reason for stopping is not specified.  
`CANCELLED` | A user manually stopped the experiment.  
`COMPLETED` | The experiment finished normally after its duration.  
  
## ExperimentTemplate

Template for a failure-injection experiment.

Fields  
---  
`name` |  `string` Identifier. The resource name of this experiment template. Format: `projects/{project}/locations/{location}/experimentTemplates/{experiment_template}`  
`display_name` |  `string` Optional. Human-readable template name. Min length 0, max 1000.  
`description` |  `string` Optional. Optional user-provided description or notes. Min length 0. Max length 2000.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. How long the experiment is intended to run. Min duration is 0, max is 10 days.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the template was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the template was last updated.  
`action` |  `[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Action)` Required. The action to be performed.  
  
## GCEFailCompute

GCEFailCompute specifies which instances to fail.

Fields  
---  
Union field `specifier`. Use one of these elements to specify which GCE instance(s) to fail. `specifier` can be only one of the following:  
`secure_tag_value` |  `string` Specifies a group of non-MIG (Managed Instance Group) instances by secure tag. See <https://cloud.google.com/firewall/docs/tags-firewalls-overview> for more details on tags. Format: `{project}/{tag_key}/{tag_value}`.  
`mig` |  `[MigElement](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.MigElement)` Specifies a managed instance group. Can be zonal or regional.  
`location` |  `string` Specifies that an entire zone or region should be affected.  
`instances` |  `[InstanceList](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.InstanceList)` Specifies a list of instances.  
  
## GKEFailCompute

GKEFailCompute specifies infrastructure or workload to fail.

Fields  
---  
`cluster` |  `string` Required. Options for selecting which GKE resources to fail. The GKE cluster resource name. Format: `projects/{project}/locations/{location}/clusters/{cluster}`  
`location` |  `string` Optional. Specifies a zone or region location.  
`k8s_namespace[]` |  `string` Optional. Specifies one or more Kubernetes namespaces.  
  
## GetAffectedResourceRequest

Request message for `[FaultTesting.GetAffectedResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetAffectedResource)`.

Fields  
---  
`name` |  `string` Required. The resource name of the affected resource. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}/affectedResources/{affectedResourceId}`.  
  
## GetExclusionWindowRequest

Request message for `[FaultTesting.GetExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExclusionWindow)`.

Fields  
---  
`name` |  `string` Required. The name of the exclusion window to retrieve. Format: `projects/{project}/locations/{location}/exclusionWindows/{exclusion_window}`.  
  
## GetExperimentRequest

Request message for `[FaultTesting.GetExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExperiment)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment to retrieve. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
  
## GetExperimentTemplateRequest

Request message for `[FaultTesting.GetExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetExperimentTemplate)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment template to retrieve. Format: `projects/{projectId}/locations/{location}/experimentTemplates/{experimentTemplateId}`.  
  
## GetValidationRequest

Request message for `[FaultTesting.GetValidation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetValidation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the dry run to retrieve. Format: `projects/{projectId}/locations/{location}/validations/{validationId}`.  
  
## GetValidationResourceRequest

Request message for `[FaultTesting.GetValidationResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.GetValidationResource)`.

Fields  
---  
`name` |  `string` Required. The resource name of the validation resource to retrieve. Format: `projects/{projectId}/locations/{location}/validations/{validationId}/validationResources/{validationResourceId}`.  
  
## HTTPAbort

Artificially return a specific HTTP status code for a percentage of requests.

Fields  
---  
`status_code` |  `int32` Required. HTTP status code to return. In the range 500 to 599, inclusive.  
`percentage` |  `int32` Required. Percentage of requests to abort, in the range 0 to 100, inclusive.  
  
## HTTPDelay

Artificially delay HTTP responses for a percentage of requests.

Fields  
---  
`percentage` |  `int32` Required. Percentage of requests to delay, in the range 0 to 100, inclusive.  
`delay` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. Delay duration.  
  
## InstanceList

A GCEFailCompute option for failing multiple instances by name.

Fields  
---  
`instances[]` |  `string` Required. Specifies instances by name. Format: `projects/{project}/zones/{zone}/instances/{instance}`  
  
## L7LBHTTPFault

Injection of HTTP faults into a layer 7 load balancer.

Fields  
---  
`forwarding_rule` |  `string` Required. The identifying name of the forwarding rule resource where the faults will be injected. Format: `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}` or `projects/{project}/global/forwardingRules/{forwarding_rule}`  
`backend_service` |  `string` Optional. Optional identifying name of the backend service to inject faults into. Format: `projects/{project}/regions/{region}/backendServices/{backend_service}` or `projects/{project}/global/backendServices/{backend_service}` If not specified, all backend services connected to the forwarding_rule will be affected.  
Union field `fault`. The fault to be injected. Can inject either an HTTP error code or a delay. `fault` can be only one of the following:  
`abort` |  `[HTTPAbort](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.HTTPAbort)` Returns an HTTP error code for some requests.  
`delay` |  `[HTTPDelay](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.HTTPDelay)` Delays some HTTP responses.  
  
## ListAffectedResourcesRequest

Request message for `[FaultTesting.ListAffectedResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListAffectedResources)`.

Fields  
---  
`parent` |  `string` Required. The experiment from which to list affected resources. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
`page_size` |  `int32` Optional. The maximum number of affected resources to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous list call, used to retrieve the subsequent page.When paginating, all other parameters provided to `ListAffectedResources` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression to restrict the affected resources returned. Follows <https://google.aip.dev/160> and supports all fields.  
  
## ListAffectedResourcesResponse

Response message for `[FaultTesting.ListAffectedResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListAffectedResources)`.

Fields  
---  
`affected_resources[]` |  `[AffectedResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.AffectedResource)` The affected resources from the specified experiment, ordered from newest to oldest based on creation time.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListExclusionWindowsRequest

Request message for `[FaultTesting.ListExclusionWindows](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExclusionWindows)`.

Fields  
---  
`parent` |  `string` Required. The project and location from which to list exclusion windows. Format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. The maximum number of exclusion windows to return from this call. The service may return fewer than this value. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListExclusionWindows` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListExclusionWindows` must match the call that provided the page token.  
  
## ListExclusionWindowsResponse

Response message for `[FaultTesting.ListExclusionWindows](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExclusionWindows)`.

Fields  
---  
`exclusion_windows[]` |  `[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)` The exclusion windows from the specified project.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached, each with the format `projects/{project}/locations/{location}`.  
  
## ListExperimentTemplatesRequest

Request message for `[FaultTesting.ListExperimentTemplates](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates)`.

Fields  
---  
`parent` |  `string` Required. The project and location from which to list experiment templates. Format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. The maximum number of templates to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous list call, used to retrieve the subsequent page.When paginating, all other parameters provided to `ListExperimentTemplates` must match the call that provided the page token.  
  
## ListExperimentTemplatesResponse

Response message for `[FaultTesting.ListExperimentTemplates](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates)`.

Fields  
---  
`experiment_templates[]` |  `[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)` The experiment templates from the specified project.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListExperimentsRequest

Request message for `[FaultTesting.ListExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListExperiments)`.

Fields  
---  
`parent` |  `string` Required. The project and location from which to list experiments. Format: `projects/{projectId}/locations/{location}`.  
`page_size` |  `int32` Optional. The maximum number of experiments to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous list call, used to retrieve the subsequent page.When paginating, all other parameters provided to `ListExperiments` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression to restrict the experiments returned. Example: `state="INJECTED"`. Returns only experiments matching the expression. Follows <https://google.aip.dev/160> and supports all fields.  
  
## ListExperimentsResponse

List experiments for a specified project.

Fields  
---  
`experiments[]` |  `[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Experiment)` The experiments from the specified project, ordered from newest to oldest based on creation time.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListValidationResourcesRequest

Request message for `[FaultTesting.ListValidationResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListValidationResources)`.

Fields  
---  
`parent` |  `string` Required. The `Validation` dry run from which to list validation resources. Format: `projects/{projectId}/locations/{location}/validations/{validationId}`.  
`page_size` |  `int32` Optional. The maximum number of validation resources to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListValidationResources` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListValidationResources` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression to restrict the validation resources returned. Follows <https://google.aip.dev/160> and supports all fields.  
  
## ListValidationResourcesResponse

Response message for `[FaultTesting.ListValidationResources](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListValidationResources)`.

Fields  
---  
`validation_resources[]` |  `[ValidationResource](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ValidationResource)` The validation resources from the specified `Validation`, ordered from newest to oldest based on creation time.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListValidationsRequest

Request message for `[FaultTesting.ListValidations](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.ListValidations)`.

Fields  
---  
`parent` |  `string` Required. The project and location from which to list dry runs. Format: `projects/{projectId}/locations/{location}`.  
`page_size` |  `int32` Optional. The maximum number of dry runs to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous list call, used to retrieve the subsequent page.When paginating, all other parameters provided to `ListValidations` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression to restrict the dry runs returned. Example: `state="COMPLETED"`. Returns only dry runs matching the expression. Follows <https://google.aip.dev/160> and supports all fields.  
  
## ListValidationsResponse

List dry runs for a specified project.

Fields  
---  
`validations[]` |  `[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Validation)` The dry runs from the specified project, ordered from newest to oldest based on creation time.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## MigElement

Details specifying a Managed Instance Group (MIG) and optionally a zone within it.

Fields  
---  
`instance_group_manager` |  `string` Required. Specifies the manager of a managed instance group. Can be zonal or regional. Format: `projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}` or `projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}`  
`location` |  `string` Optional. Optionally specify a zone location to further restrict a regional MIG.  
  
## OperationMetadata

Represents the metadata of the long-running operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[google.longrunning.Operation.error](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` Output only. API version used to start the operation.  
  
## StartExclusionWindowRequest

Request message for `[FaultTesting.StartExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StartExclusionWindow)`.

Fields  
---  
`name` |  `string` Required. The resource name of the exclusion window to start. Format: `projects/{project}/locations/{location}/exclusionWindows/{exclusion_window}`.  
  
## StartExperimentRequest

Request message for `[FaultTesting.StartExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StartExperiment)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment to start. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
  
## State

Represents the current state of an `Experiment` or `Validation` dry run. String values are used in JSON.

Enums  
---  
`STATE_UNSPECIFIED` | The state is not known or not set.  
`PREPARING` | The system is identifying the target Google Cloud resources for the `Experiment` or `Validation` and checking necessary permissions.  
`PREPARED` | The experiment is fully set up and ready to start.  
`INJECTING` | The system is actively applying the fault to the targeted resources. Example: Slowing down responses, triggering errors.  
`INJECTED` | The fault is active on the targeted resources. The `Experiment` is now running for its planned duration.  
`REVERTING` | The `Experiment` is being stopped, and FIT is removing the fault and restoring the resources to their normal operational state.  
`COMPLETED` | The `Experiment` or `Validation` has finished, and the resources are back to their normal state. No further actions will occur.  
  
## StopAllExperimentsRequest

Request message for `[FaultTesting.StopAllExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopAllExperiments)`.

Fields  
---  
`parent` |  `string` Required. The project and location where all experiments will be stopped. Format: `projects/{projectId}/locations/{location}`.  
  
## StopAllExperimentsResponse

Response message for `[FaultTesting.StopAllExperiments](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopAllExperiments)`. Response is a complete success only if `errors` is empty.

Fields  
---  
`stopped_experiments_count` |  `int32` The number of experiments that were stopped. These experiments are in reachable locations with statuses that allows them to be stopped, and did not get an error from `StopExperiment`.  
`errors[]` |  `[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.rpc#google.rpc.Status)` Errors that occurred while listing or stopping experiments. Each experiment that fails the internal `StopExperiment` call will have an entry in this list.  
  
## StopExclusionWindowRequest

Request message for `[FaultTesting.StopExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopExclusionWindow)`.

Fields  
---  
`name` |  `string` Required. The resource name of the exclusion window to stop. Format: `projects/{project}/locations/{location}/exclusionWindows/{exclusion_window}`.  
  
## StopExperimentRequest

Request message for `[FaultTesting.StopExperiment](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.StopExperiment)`.

Fields  
---  
`name` |  `string` Required. The resource name of the experiment to stop. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
  
## UpdateExclusionWindowRequest

Request message for `[FaultTesting.UpdateExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExclusionWindow)`.

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`exclusion_window` |  `[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExclusionWindow)` Required. The exclusion window to update.  
  
## UpdateExperimentTemplateRequest

The request message for `[FaultTesting.UpdateExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExperimentTemplate)`.

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. A comma-separated list of fields to update. If not provided, all editable fields will be considered for updates. Fields like `name` and `createTime` cannot be updated.  
`experiment_template` |  `[ExperimentTemplate](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.ExperimentTemplate)` Required. The experiment template to update. The request body contains an instance of `ExperimentTemplate`.  
  
## Validation

Represents a `Validation` dry run of a fault injection.

Fields  
---  
`name` |  `string` Identifier. Unique identifier for the `Validation` dry run. Format: `projects/{project_id}/locations/{location}/validations/{validationId}`.  
`display_name` |  `string` Optional. A human-readable name of the `Validation` dry run.  
`description` |  `string` Optional. Notes or details about the `Validation` dry run. Minimum length is 0, maximum length is 2000.  
`action` |  `[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.Action)` Required. The fault injection action being checked.  
`state` |  `[State](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State)` Output only. The current state of the `Validation` dry run. Either `PREPARING` or `COMPLETED`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when this `Validation` dry run was started (RFC3339 UTC "Zulu" format).  
`stop_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The date and time when this `Validation` dry run finished (RFC3339 UTC "Zulu" format).  
  
## ValidationResource

Represents a specific Google Cloud resource that a `Validation` dry run identified as _potentially_ being affected.

Fields  
---  
`name` |  `string` Identifier. Unique identifier for this specific record within the `Validation` results. Format: `projects/{project}/locations/{location}/validations/{validation}/validationResources/{validationResourceId}`.  
`display_name` |  `string` Optional. A human-readable name for the `ValidationResource` record.  
`affected_resource_uri` |  `string` Required. The full unique address (URI) of the Google Cloud resource that was identified.  
`cloud_console_path` |  `string` Output only. A direct link to view this specific resource in the Google Cloud Console.  
`state` |  `[State](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State)` The current state of this resource within the dry run. Typically `COMPLETED`.  
`state_message` |  `string` A human-readable description of the validation status for this resource.  
`error` |  `[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.rpc#google.rpc.Status)` Output only. Details of any error encountered while checking the resource during the dry run. Empty if the check was successful.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
