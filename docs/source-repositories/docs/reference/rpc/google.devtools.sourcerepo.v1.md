---
url: https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1
title: Package google.devtools.sourcerepo.v1 \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:56.737429+00:00
---

# Package google.devtools.sourcerepo.v1  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Reference ](https://docs.cloud.google.com/source-repositories/docs/apis)



Send feedback 

#  Package google.devtools.sourcerepo.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[SourceRepo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.SourceRepo)` (interface)
  * `[CreateRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.CreateRepoRequest)` (message)
  * `[DeleteRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.DeleteRepoRequest)` (message)
  * `[GetProjectConfigRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.GetProjectConfigRequest)` (message)
  * `[GetRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.GetRepoRequest)` (message)
  * `[ListReposRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ListReposRequest)` (message)
  * `[ListReposResponse](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ListReposResponse)` (message)
  * `[MirrorConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.MirrorConfig)` (message)
  * `[ProjectConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ProjectConfig)` (message)
  * `[PubsubConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.PubsubConfig)` (message)
  * `[PubsubConfig.MessageFormat](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.PubsubConfig.MessageFormat)` (enum)
  * `[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)` (message)
  * `[SyncRepoMetadata](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.SyncRepoMetadata)` (message)
  * `[SyncRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.SyncRepoRequest)` (message)
  * `[UpdateProjectConfigRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.UpdateProjectConfigRequest)` (message)
  * `[UpdateRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.UpdateRepoRequest)` (message)



## SourceRepo

The Source Repo API service.

CreateRepo  
---  
` rpc CreateRepo(`[CreateRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.CreateRepoRequest)`) returns (`[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`) ` Creates a repo in the given project with the given name.If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteRepo  
---  
` rpc DeleteRepo(`[DeleteRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.DeleteRepoRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes a repo.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetIamPolicy  
---  
` rpc GetIamPolicy(`[GetIamPolicyRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.GetIamPolicyRequest)`) returns (`[Policy](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)`) ` Gets the IAM policy policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetProjectConfig  
---  
` rpc GetProjectConfig(`[GetProjectConfigRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.GetProjectConfigRequest)`) returns (`[ProjectConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ProjectConfig)`) ` Returns the Cloud Source Repositories configuration of the project.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetRepo  
---  
` rpc GetRepo(`[GetRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.GetRepoRequest)`) returns (`[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`) ` Returns information about a repo.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListRepos  
---  
` rpc ListRepos(`[ListReposRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ListReposRequest)`) returns (`[ListReposResponse](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ListReposResponse)`) ` Returns all repos belonging to a project. The sizes of the repos are not set by ListRepos. To get the size of a repo, use GetRepo.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
SetIamPolicy  
---  
` rpc SetIamPolicy(`[SetIamPolicyRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.SetIamPolicyRequest)`) returns (`[Policy](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)`) ` Sets the IAM policy on the specified resource. Replaces any existing policy.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
SyncRepo  
---  
` rpc SyncRepo(`[SyncRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.SyncRepoRequest)`) returns (`[Operation](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Synchronize a connected repo.The response contains SyncRepoMetadata in the metadata field.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
TestIamPermissions  
---  
` rpc TestIamPermissions(`[TestIamPermissionsRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.TestIamPermissionsRequest)`) returns (`[TestIamPermissionsResponse](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.iam.v1#google.iam.v1.TestIamPermissionsResponse)`) ` Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateProjectConfig  
---  
` rpc UpdateProjectConfig(`[UpdateProjectConfigRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.UpdateProjectConfigRequest)`) returns (`[ProjectConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ProjectConfig)`) ` Updates the Cloud Source Repositories configuration of the project.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateRepo  
---  
` rpc UpdateRepo(`[UpdateRepoRequest](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.UpdateRepoRequest)`) returns (`[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`) ` Updates information about a repo.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## CreateRepoRequest

Request for CreateRepo

Fields  
---  
`parent` |  `string` The project in which to create the repo. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `source.repos.create`

  
`repo` |  ``[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`` The repo to create. Only name should be set; setting other fields is an error. The project in the name should match the parent field.  
  
## DeleteRepoRequest

Request for DeleteRepo.

Fields  
---  
`name` |  `string` The name of the repo to delete. Values are of the form `projects/<project>/repos/<repo>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.delete`

  
  
## GetProjectConfigRequest

Request for GetProjectConfig.

Fields  
---  
`name` |  `string` The name of the requested project. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.getProjectConfig`

  
  
## GetRepoRequest

Request for GetRepo.

Fields  
---  
`name` |  `string` The name of the requested repository. Values are of the form `projects/<project>/repos/<repo>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.get`

  
  
## ListReposRequest

Request for ListRepos.

Fields  
---  
`name` |  `string` The project ID whose repos should be listed. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.list`

  
`page_size` |  `int32` Maximum number of repositories to return; between 1 and 500. If not set or zero, defaults to 100 at the server.  
`page_token` |  `string` Resume listing repositories where a prior ListReposResponse left off. This is an opaque token that must be obtained from a recent, prior ListReposResponse's next_page_token field.  
  
## ListReposResponse

Response for ListRepos. The size is not set in the returned repositories.

Fields  
---  
`repos[]` |  ``[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`` The listed repos.  
`next_page_token` |  `string` If non-empty, additional repositories exist within the project. These can be retrieved by including this value in the next ListReposRequest's page_token field.  
  
## MirrorConfig

Configuration to automatically mirror a repository from another hosting service, for example GitHub or Bitbucket.

Fields  
---  
`url` |  `string` URL of the main repository at the other hosting service.  
`webhook_id` |  `string` ID of the webhook listening to updates to trigger mirroring. Removing this webhook from the other hosting service will stop Google Cloud Source Repositories from receiving notifications, and thereby disabling mirroring.  
`deploy_key_id` |  `string` ID of the SSH deploy key at the other hosting service. Removing this key from the other service would deauthorize Google Cloud Source Repositories from mirroring.  
  
## ProjectConfig

Cloud Source Repositories configuration of a project.

Fields  
---  
`name` |  `string` The name of the project. Values are of the form `projects/<project>`.  
`pubsub_configs` |  `map<string, `[PubsubConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.PubsubConfig)`>` How this project publishes a change in the repositories through Cloud Pub/Sub. Keyed by the topic names.  
`enable_private_key_check` |  `bool` Reject a Git push that contains a private key.  
  
## PubsubConfig

Configuration to publish a Cloud Pub/Sub message.

Fields  
---  
`topic` |  `string` A topic of Cloud Pub/Sub. Values are of the form `projects/<project>/topics/<topic>`. The project needs to be the same project as this config is in.  
`message_format` |  ``[MessageFormat](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.PubsubConfig.MessageFormat)`` The format of the Cloud Pub/Sub messages.  
`service_account_email` |  `string` Email address of the service account used for publishing Cloud Pub/Sub messages. This service account needs to be in the same project as the PubsubConfig. When added, the caller needs to have iam.serviceAccounts.actAs permission on this service account. If unspecified, it defaults to the compute engine default service account.  
  
## MessageFormat

The format of the Cloud Pub/Sub messages.

Enums  
---  
`MESSAGE_FORMAT_UNSPECIFIED` | Unspecified.  
`PROTOBUF` | The message payload is a serialized protocol buffer of SourceRepoEvent.  
`JSON` | The message payload is a JSON string of SourceRepoEvent.  
  
## Repo

A repository (or repo) is a Git repository storing versioned source content.

Fields  
---  
`name` |  `string` Resource name of the repository, of the form `projects/<project>/repos/<repo>`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`  
`size` |  `int64` The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.  
`url` |  `string` URL to clone the repository from Google Cloud Source Repositories. Read-only field.  
`mirror_config` |  ``[MirrorConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.MirrorConfig)`` How this repository mirrors a repository managed by another service. Read-only field.  
`pubsub_configs` |  `map<string, `[PubsubConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.PubsubConfig)`>` How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.  
  
## SyncRepoMetadata

Metadata of SyncRepo.

This message is in the metadata field of Operation.

Fields  
---  
`name` |  `string` The name of the repo being synchronized. Values are of the form `projects/<project>/repos/<repo>`.  
`status_message` |  `string` The latest status message on syncing the repository.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time this operation is started.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time this operation's status message is updated.  
  
## SyncRepoRequest

Request for SyncRepo.

Fields  
---  
`name` |  `string` The name of the repo to synchronize. Values are of the form `projects/<project>/repos/<repo>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.update`

  
  
## UpdateProjectConfigRequest

Request for UpdateProjectConfig.

Fields  
---  
`name` |  `string` The name of the requested project. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.updateProjectConfig`

  
`project_config` |  ``[ProjectConfig](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.ProjectConfig)`` The new configuration for the project.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` A FieldMask specifying which fields of the project_config to modify. Only the fields in the mask will be modified. If no mask is provided, this request is no-op.  
  
## UpdateRepoRequest

Request for UpdateRepo.

Fields  
---  
`name` |  `string` The name of the requested repository. Values are of the form `projects/<project>/repos/<repo>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.updateRepoConfig`

  
`repo` |  ``[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rpc/google.devtools.sourcerepo.v1#google.devtools.sourcerepo.v1.Repo)`` The new configuration for the repository.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` A FieldMask specifying which fields of the repo to modify. Only the fields in the mask will be modified. If no mask is provided, this request is no-op.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
