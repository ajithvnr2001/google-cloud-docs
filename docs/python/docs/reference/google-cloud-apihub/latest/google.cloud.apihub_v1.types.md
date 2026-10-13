---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types
title: Package types (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:27.179175+00:00
---

# Package types (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 

API documentation for `apihub_v1.types` package.

## Classes 

### [APIMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.APIMetadata)

The API metadata.

### [ActionExecutionDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ActionExecutionDetail)

The details for the action to execute.

### [ActionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ActionType)

Enum for the action type.

### [Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)

An API resource in the API Hub.

### [ApiData](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiData)

The API data to be collected.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ApiHubInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubInstance)

An ApiHubInstance represents the instance resources of the API Hub. Currently, only one ApiHub instance is allowed for each project.

### [ApiHubResource](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubResource)

ApiHubResource is one of the resources such as Api, Operation, Deployment, Definition, Spec and Version resources stored in API-Hub.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ApiMetadataList](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiMetadataList)

The message to hold repeated API metadata.

### [ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)

Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.

### [ApplicationIntegrationEndpointDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApplicationIntegrationEndpointDetails)

The details of the Application Integration endpoint to be triggered for curation.

### [Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)

An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.

### [AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)

The attribute values associated with resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AuthConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig)

AuthConfig represents the authentication information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AuthType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthType)

AuthType represents the authentication type.

### [CollectApiDataRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CollectApiDataRequest)

The CollectApiData method's request.

### [CollectApiDataResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CollectApiDataResponse)

The CollectApiData method's response.

### [CollectionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CollectionType)

The type of the collect request.

### [ConfigValueOption](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ConfigValueOption)

ConfigValueOption represents an option for a config variable of type enum or multi select.

### [ConfigVariable](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ConfigVariable)

ConfigVariable represents a additional configuration variable present in a PluginInstance Config or AuthConfig, based on a ConfigVariableTemplate.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConfigVariableTemplate](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ConfigVariableTemplate)

ConfigVariableTemplate represents a configuration variable template present in a Plugin Config.

### [CreateApiHubInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiHubInstanceRequest)

The CreateApiHubInstance method's request.

### [CreateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiOperationRequest)

The CreateApiOperation method's request.

### [CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiRequest)

The CreateApi method's request.

### [CreateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateAttributeRequest)

The CreateAttribute method's request.

### [CreateCurationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateCurationRequest)

The `CreateCuration][ApiHub.CreateCuration]` method's request.

### [CreateDependencyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateDependencyRequest)

The CreateDependency method's request.

### [CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateDeploymentRequest)

The CreateDeployment method's request.

### [CreateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateExternalApiRequest)

The CreateExternalApi method's request.

### [CreateHostProjectRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateHostProjectRegistrationRequest)

The CreateHostProjectRegistration method's request.

### [CreatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginInstanceRequest)

The CreatePluginInstance method's request.

### [CreatePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginRequest)

The CreatePlugin method's request.

### [CreateRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateRuntimeProjectAttachmentRequest)

The CreateRuntimeProjectAttachment method's request.

### [CreateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateSpecRequest)

The CreateSpec method's request.

### [CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateVersionRequest)

The CreateVersion method's request.

### [Curation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation)

A curation resource in the API Hub.

### [CurationConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CurationConfig)

The curation information for this plugin instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CurationType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CurationType)

Enum for the curation type.

### [Definition](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Definition)

Represents a definition for example schema, request, response definitions contained in an API version. A definition is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, definition will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Also, within OpenAPI spec, only `schema` object is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteApiHubInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiHubInstanceRequest)

The DeleteApiHubInstance method's request.

### [DeleteApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiOperationRequest)

The DeleteApiOperation method's request.

### [DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiRequest)

The DeleteApi method's request.

### [DeleteAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteAttributeRequest)

The DeleteAttribute method's request.

### [DeleteCurationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteCurationRequest)

The `DeleteCuration][ApiHub.DeleteCuration]` method's request.

### [DeleteDependencyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteDependencyRequest)

The DeleteDependency method's request.

### [DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteDeploymentRequest)

The DeleteDeployment method's request.

### [DeleteExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteExternalApiRequest)

The DeleteExternalApi method's request.

### [DeletePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginInstanceRequest)

The DeletePluginInstance method's request.

### [DeletePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginRequest)

The `DeletePlugin][ApiHub.DeletePlugin]` method's request.

### [DeleteRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteRuntimeProjectAttachmentRequest)

The DeleteRuntimeProjectAttachment method's request.

### [DeleteSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteSpecRequest)

The DeleteSpec method's request.

### [DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteVersionRequest)

The DeleteVersion method's request.

### [Dependency](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Dependency)

A dependency resource defined in the API hub describes a dependency directed from a consumer to a supplier entity. A dependency can be defined between two Operations or between an Operation and [External API][google.cloud.apihub.v1.ExternalApi].

### [DependencyEntityReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DependencyEntityReference)

Reference to an entity participating in a dependency.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DependencyErrorDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DependencyErrorDetail)

Details describing error condition of a dependency.

### [Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)

Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.

### [DeploymentMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeploymentMetadata)

The metadata associated with a deployment.

### [DisablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginInstanceActionRequest)

The DisablePluginInstanceAction method's request.

### [DisablePluginInstanceActionResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginInstanceActionResponse)

The DisablePluginInstanceAction method's response.

### [DisablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginRequest)

The DisablePlugin method's request.

### [DiscoveredApiObservation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiObservation)

Respresents an API Observation observed in one of the sources.

### [DiscoveredApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiOperation)

DiscoveredApiOperation represents an API Operation observed in one of the sources.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Documentation)

Documentation details.

### [EnablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginInstanceActionRequest)

The EnablePluginInstanceAction method's request.

### [EnablePluginInstanceActionResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginInstanceActionResponse)

The EnablePluginInstanceAction method's response.

### [EnablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginRequest)

The EnablePlugin method's request.

### [Endpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Endpoint)

The endpoint to be triggered for curation. The endpoint will be invoked with a request payload containing ApiMetadata. Response should contain curated data in the form of ApiMetadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExecutePluginInstanceActionRequest)

The ExecutePluginInstanceAction method's request.

### [ExecutePluginInstanceActionResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExecutePluginInstanceActionResponse)

The ExecutePluginInstanceAction method's response.

### [ExecutionStatus](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExecutionStatus)

The execution status for the plugin instance.

### [ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)

An external API represents an API being provided by external sources. This can be used to model third-party APIs and can be used to define dependencies.

### [GatewayType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GatewayType)

Enum for the gateway type.

### [GetApiHubInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiHubInstanceRequest)

The GetApiHubInstance method's request.

### [GetApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiOperationRequest)

The GetApiOperation method's request.

### [GetApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiRequest)

The GetApi method's request.

### [GetAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetAttributeRequest)

The GetAttribute method's request.

### [GetCurationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetCurationRequest)

The `GetCuration][ApiHub.GetCuration]` method's request.

### [GetDefinitionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDefinitionRequest)

The GetDefinition method's request.

### [GetDependencyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDependencyRequest)

The `GetDependency][.ApiHubDependencies.GetDependency]` method's request.

### [GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDeploymentRequest)

The GetDeployment method's request.

### [GetDiscoveredApiObservationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDiscoveredApiObservationRequest)

Message for requesting a DiscoveredApiObservation

### [GetDiscoveredApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDiscoveredApiOperationRequest)

Message for requesting a DiscoveredApiOperation

### [GetExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetExternalApiRequest)

The GetExternalApi method's request.

### [GetHostProjectRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetHostProjectRegistrationRequest)

The GetHostProjectRegistration method's request.

### [GetPluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginInstanceRequest)

The GetPluginInstance method's request.

### [GetPluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginRequest)

The GetPlugin method's request.

### [GetRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetRuntimeProjectAttachmentRequest)

The GetRuntimeProjectAttachment method's request.

### [GetSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecContentsRequest)

The GetSpecContents method's request.

### [GetSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecRequest)

The GetSpec method's request.

### [GetStyleGuideContentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetStyleGuideContentsRequest)

The GetStyleGuideContents method's request.

### [GetStyleGuideRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetStyleGuideRequest)

The GetStyleGuide method's request.

### [GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetVersionRequest)

The GetVersion method's request.

### [GoogleServiceAccountConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GoogleServiceAccountConfig)

Config for Google service account authentication.

### [HostProjectRegistration](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.HostProjectRegistration)

Host project registration refers to the registration of a Google cloud project with Api Hub as a host project. This is the project where Api Hub is provisioned. It acts as the consumer project for the Api Hub instance provisioned. Multiple runtime projects can be attached to the host project and these attachments define the scope of Api Hub.

### [HttpOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.HttpOperation)

The HTTP Operation.

### [HttpOperationDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.HttpOperationDetails)

An HTTP-based API Operation, sometimes called a "REST" Operation.

### [Issue](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Issue)

Issue contains the details of a single issue found by the linter.

### [LintResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LintResponse)

LintResponse contains the response from the linter.

### [LintSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LintSpecRequest)

The LintSpec method's request.

### [LintState](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LintState)

Lint state represents success or failure for linting.

### [Linter](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Linter)

Enumeration of linter types.

### [ListApiOperationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsRequest)

The ListApiOperations method's request.

### [ListApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsResponse)

The ListApiOperations method's response.

### [ListApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisRequest)

The ListApis method's request.

### [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisResponse)

The ListApis method's response.

### [ListAttributesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesRequest)

The ListAttributes method's request.

### [ListAttributesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesResponse)

The ListAttributes method's response.

### [ListCurationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListCurationsRequest)

The `ListCurations][ApiHub.ListCurations]` method's request.

### [ListCurationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListCurationsResponse)

The `ListCurations][ApiHub.ListCurations]` method's response.

### [ListDependenciesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDependenciesRequest)

The ListDependencies method's request.

### [ListDependenciesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDependenciesResponse)

The ListDependencies method's response.

### [ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsRequest)

The ListDeployments method's request.

### [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsResponse)

The ListDeployments method's response.

### [ListDiscoveredApiObservationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDiscoveredApiObservationsRequest)

Message for requesting list of DiscoveredApiObservations

### [ListDiscoveredApiObservationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDiscoveredApiObservationsResponse)

Message for response to listing DiscoveredApiObservations

### [ListDiscoveredApiOperationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDiscoveredApiOperationsRequest)

Message for requesting list of DiscoveredApiOperations

### [ListDiscoveredApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDiscoveredApiOperationsResponse)

Message for response to listing DiscoveredApiOperations

### [ListExternalApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisRequest)

The ListExternalApis method's request.

### [ListExternalApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisResponse)

The ListExternalApis method's response.

### [ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListHostProjectRegistrationsRequest)

The ListHostProjectRegistrations method's request.

### [ListHostProjectRegistrationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListHostProjectRegistrationsResponse)

The ListHostProjectRegistrations method's response.

### [ListPluginInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesRequest)

The ListPluginInstances method's request.

### [ListPluginInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesResponse)

The ListPluginInstances method's response.

### [ListPluginsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsRequest)

The ListPlugins method's request.

### [ListPluginsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsResponse)

The ListPlugins method's response.

### [ListRuntimeProjectAttachmentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListRuntimeProjectAttachmentsRequest)

The ListRuntimeProjectAttachments method's request.

### [ListRuntimeProjectAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListRuntimeProjectAttachmentsResponse)

The ListRuntimeProjectAttachments method's response.

### [ListSpecsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsRequest)

The `ListSpecs][ListSpecs]` method's request.

### [ListSpecsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsResponse)

The ListSpecs method's response.

### [ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsRequest)

The ListVersions method's request.

### [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsResponse)

The ListVersions method's response.

### [LookupApiHubInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LookupApiHubInstanceRequest)

The LookupApiHubInstance method's request.

### [LookupApiHubInstanceResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LookupApiHubInstanceResponse)

The LookupApiHubInstance method's response.`

### [LookupRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LookupRuntimeProjectAttachmentRequest)

The LookupRuntimeProjectAttachment method's request.

### [LookupRuntimeProjectAttachmentResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.LookupRuntimeProjectAttachmentResponse)

The ListRuntimeProjectAttachments method's response.

### [OpenApiSpecDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.OpenApiSpecDetails)

OpenApiSpecDetails contains the details parsed from an OpenAPI spec in addition to the fields mentioned in SpecDetails.

### [OperationDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.OperationDetails)

The operation details parsed from the spec.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [Owner](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Owner)

Owner details.

### [Path](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Path)

The path details derived from the spec.

### [Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)

A plugin resource in the API Hub.

### [PluginActionConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginActionConfig)

PluginActionConfig represents the configuration of an action supported by a plugin.

### [PluginCategory](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginCategory)

Enum for the plugin category.

### [PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)

Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.

### [PluginInstanceAction](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstanceAction)

PluginInstanceAction represents an action which can be executed in the plugin instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Point](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Point)

Point within the file (line and character).

### [Range](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Range)

Object describing where in the file the issue was found.

### [RuntimeProjectAttachment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.RuntimeProjectAttachment)

Runtime project attachment represents an attachment from the runtime project to the host project. Api Hub looks for deployments in the attached runtime projects and creates corresponding resources in Api Hub for the discovered deployments.

### [Schema](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Schema)

The schema details derived from the spec. Currently, this entity is supported for OpenAPI spec only. For OpenAPI spec, this maps to the schema defined in the `definitions` section for OpenAPI 2.0 version and in `components.schemas` section for OpenAPI 3.0 and 3.1 version.

### [SearchResourcesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesRequest)

The SearchResources method's request.

### [SearchResourcesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesResponse)

Response for the SearchResources method.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResult)

Represents the search results.

### [Secret](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Secret)

Secret provides a reference to entries in Secret Manager.

### [Severity](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Severity)

Severity of the issue.

### [SourceMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SourceMetadata)

SourceMetadata represents the metadata for a resource at the source.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)

Represents a spec associated with an API version in the API Hub. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.

### [SpecContents](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SpecContents)

The spec contents.

### [SpecDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SpecDetails)

SpecDetails contains the details parsed from supported spec types.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SpecMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SpecMetadata)

The metadata associated with a spec of the API version.

### [StyleGuide](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.StyleGuide)

Represents a singleton style guide resource to be used for linting Open API specs.

### [StyleGuideContents](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.StyleGuideContents)

The style guide contents.

### [UpdateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiOperationRequest)

The UpdateApiOperation method's request.

### [UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiRequest)

The UpdateApi method's request.

### [UpdateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateAttributeRequest)

The UpdateAttribute method's request.

### [UpdateCurationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateCurationRequest)

The `UpdateCuration][ApiHub.UpdateCuration]` method's request.

### [UpdateDependencyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateDependencyRequest)

The UpdateDependency method's request.

### [UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateDeploymentRequest)

The UpdateDeployment method's request.

### [UpdateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateExternalApiRequest)

The UpdateExternalApi method's request.

### [UpdatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdatePluginInstanceRequest)

The UpdatePluginInstance method's request.

### [UpdateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateSpecRequest)

The UpdateSpec method's request.

### [UpdateStyleGuideRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateStyleGuideRequest)

The UpdateStyleGuide method's request.

### [UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateVersionRequest)

The UpdateVersion method's request.

### [Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)

Represents a version of the API resource in API hub. This is also referred to as the API version.

### [VersionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.VersionMetadata)

The metadata associated with a version of the API resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
