---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types
title: Package types (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:37.486250+00:00
---

# Package types (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 

API documentation for `config_v1.types` package.

## Classes 

### [ApplyResults](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ApplyResults)

Outputs and artifacts from applying a deployment.

### [AutoMigrationConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.AutoMigrationConfig)

AutoMigrationConfig contains the automigration configuration for a project.

### [CreateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentGroupRequest)

A request to create a deployment group

### [CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentRequest)

### [CreatePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreatePreviewRequest)

A request to create a preview.

### [DeleteDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest)

Request message for Delete DeploymentGroup

### [DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentRequest)

### [DeletePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeletePreviewRequest)

A request to delete a preview.

### [DeleteStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteStatefileRequest)

A request to delete a state file passed to a 'DeleteStatefile' call.

### [Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment)

A Deployment is a group of resources and configs managed and provisioned by Infra Manager.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeploymentGroup](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup)

A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.

### [DeploymentGroupRevision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroupRevision)

A DeploymentGroupRevision represents a snapshot of a DeploymentGroup at a given point in time, created when a DeploymentGroup is provisioned or deprovisioned.

### [DeploymentOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentOperationMetadata)

Ephemeral metadata content describing the state of a deployment operation.

### [DeploymentOperationSummary](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentOperationSummary)

The summary of the deployment operation.

### [DeploymentSource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentSource)

Configuration for a value sourced from a Deployment.

### [DeploymentSpec](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentSpec)

Spec for a deployment to be created.

### [DeploymentUnit](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentUnit)

A DeploymentUnit is a container for a deployment and its dependencies. An existing deployment can be provided directly in the unit, or the unit can act as a placeholder to define the DAG, with the deployment specs supplied in a `provisionDeploymentRequest`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeploymentUnitProgress](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentUnitProgress)

The progress of a deployment unit provisioning or deprovisioning.

### [DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeprovisionDeploymentGroupRequest)

The request message for the DeprovisionDeploymentGroup method.

### [ExportDeploymentStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportDeploymentStatefileRequest)

A request to export a state file passed to a 'ExportDeploymentStatefile' call.

### [ExportLockInfoRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportLockInfoRequest)

A request to get a state file lock info passed to a 'ExportLockInfo' call.

### [ExportPreviewResultRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportPreviewResultRequest)

A request to export preview results.

### [ExportPreviewResultResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportPreviewResultResponse)

A response to `ExportPreviewResult` call. Contains preview results.

### [ExportRevisionStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportRevisionStatefileRequest)

A request to export a state file passed to a 'ExportRevisionStatefile' call.

### [ExternalValueSource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExternalValueSource)

Configuration for a source of an external value.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetAutoMigrationConfigRequest)

The request message for the GetAutoMigrationConfig method.

### [GetDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRequest)

The request message for the GetDeploymentGroup method.

### [GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRevisionRequest)

The request message for the GetDeploymentGroupRevision method.

### [GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentRequest)

### [GetPreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetPreviewRequest)

A request to get details about a preview.

### [GetResourceChangeRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceChangeRequest)

The request message for the GetResourceChange method.

### [GetResourceDriftRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceDriftRequest)

The request message for the GetResourceDrift method.

### [GetResourceRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceRequest)

A request to get a Resource from a 'GetResource' call.

### [GetRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetRevisionRequest)

A request to get a Revision from a 'GetRevision' call.

### [GetTerraformVersionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetTerraformVersionRequest)

The request message for the GetTerraformVersion method.

### [GitSource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GitSource)

A set of files in a Git repository.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ImportStatefileRequest)

A request to import a state file passed to a 'ImportStatefile' call.

### [ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsRequest)

The request message for the ListDeploymentGroupRevisions method.

### [ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsResponse)

The response message for the ListDeploymentGroupRevisions method.

### [ListDeploymentGroupsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsRequest)

The request message for the ListDeploymentGroups method.

### [ListDeploymentGroupsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsResponse)

The response message for the ListDeploymentGroups method.

### [ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsRequest)

### [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsResponse)

### [ListPreviewsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsRequest)

A request to list all previews for a given project and location.

### [ListPreviewsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsResponse)

A response to a `ListPreviews` call. Contains a list of Previews.

### [ListResourceChangesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesRequest)

The request message for the ListResourceChanges method.

### [ListResourceChangesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesResponse)

A response to a 'ListResourceChanges' call. Contains a list of ResourceChanges.

### [ListResourceDriftsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsRequest)

The request message for the ListResourceDrifts method.

### [ListResourceDriftsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsResponse)

A response to a 'ListResourceDrifts' call. Contains a list of ResourceDrifts.

### [ListResourcesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesRequest)

A request to list Resources passed to a 'ListResources' call.

### [ListResourcesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesResponse)

A response to a 'ListResources' call. Contains a list of Resources.

### [ListRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsRequest)

A request to list Revisions passed to a 'ListRevisions' call.

### [ListRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsResponse)

A response to a 'ListRevisions' call. Contains a list of Revisions.

### [ListTerraformVersionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsRequest)

The request message for the ListTerraformVersions method.

### [ListTerraformVersionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsResponse)

The response message for the `ListTerraformVersions` method.

### [LockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.LockDeploymentRequest)

A request to lock a deployment passed to a 'LockDeployment' call.

### [LockInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.LockInfo)

Details about the lock which locked the deployment.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview)

A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PreviewArtifacts](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewArtifacts)

Artifacts created by preview.

### [PreviewOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewOperationMetadata)

Ephemeral metadata content describing the state of a preview operation.

### [PreviewResult](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewResult)

Contains a signed Cloud Storage URLs.

### [PropertyChange](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PropertyChange)

A property change represents a change to a property in the state file.

### [PropertyDrift](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PropertyDrift)

A property drift represents a drift to a property in the state file.

### [ProviderConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProviderConfig)

ProviderConfig contains the provider configurations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProvisionDeploymentGroupOperationMetadata)

Operation metadata for `ProvisionDeploymentGroup` and `DeprovisionDeploymentGroup` long-running operations.

### [ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProvisionDeploymentGroupRequest)

The request message for the ProvisionDeploymentGroup method.

### [QuotaValidation](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.QuotaValidation)

Enum values to control quota checks for resources in terraform configuration files.

### [Resource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Resource)

Resource represents a Google Cloud Platform resource actuated by IM. Resources are child resources of Revisions.

### [ResourceCAIInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceCAIInfo)

CAI info of a Resource.

### [ResourceChange](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceChange)

A resource change represents a change to a resource in the state file.

### [ResourceChangeTerraformInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceChangeTerraformInfo)

Terraform info of a ResourceChange.

### [ResourceDrift](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceDrift)

A resource drift represents a drift to a resource in the state file.

### [ResourceDriftTerraformInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceDriftTerraformInfo)

Terraform info of a ResourceChange.

### [ResourceTerraformInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceTerraformInfo)

Terraform info of a Resource.

### [Revision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Revision)

A child resource of a Deployment generated by a 'CreateDeployment' or 'UpdateDeployment' call. Each Revision contains metadata pertaining to a snapshot of a particular Deployment.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Statefile)

Contains info about a Terraform state file

### [TerraformBlueprint](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformBlueprint)

TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TerraformError](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformError)

Errors encountered during actuation using Terraform

### [TerraformOutput](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformOutput)

Describes a Terraform output.

### [TerraformVariable](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformVariable)

A Terraform input variable.

### [TerraformVersion](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformVersion)

A TerraformVersion represents the support state the corresponding Terraform version.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UnlockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UnlockDeploymentRequest)

A request to unlock a state file passed to a 'UnlockDeployment' call.

### [UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateAutoMigrationConfigRequest)

The request message for the UpdateAutoMigrationConfig method.

### [UpdateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentGroupRequest)

A request message for updating a deployment group

### [UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentRequest)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
