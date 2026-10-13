---
url: https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1
title: Package google.storagetransfer.v1 \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:12.679429+00:00
---

# Package google.storagetransfer.v1  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/storage-transfer/docs/apis)



Send feedback 

#  Package google.storagetransfer.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[StorageTransferService](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.StorageTransferService)` (interface)
  * `[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)` (message)
  * `[AgentPool.BandwidthLimit](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.BandwidthLimit)` (message)
  * `[AgentPool.State](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.State)` (enum)
  * `[AwsAccessKey](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsAccessKey)` (message)
  * `[AwsS3CompatibleData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3CompatibleData)` (message)
  * `[AwsS3Data](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3Data)` (message)
  * `[AzureBlobStorageData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData)` (message)
  * `[AzureBlobStorageData.FederatedIdentityConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData.FederatedIdentityConfig)` (message)
  * `[AzureCredentials](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureCredentials)` (message)
  * `[CreateAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.CreateAgentPoolRequest)` (message)
  * `[CreateTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.CreateTransferJobRequest)` (message)
  * `[DeleteAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.DeleteAgentPoolRequest)` (message)
  * `[DeleteTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.DeleteTransferJobRequest)` (message)
  * `[ErrorLogEntry](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ErrorLogEntry)` (message)
  * `[ErrorSummary](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ErrorSummary)` (message)
  * `[EventStream](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.EventStream)` (message)
  * `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` (message)
  * `[GetAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetAgentPoolRequest)` (message)
  * `[GetGoogleServiceAccountRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetGoogleServiceAccountRequest)` (message)
  * `[GetTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetTransferJobRequest)` (message)
  * `[GoogleServiceAccount](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GoogleServiceAccount)` (message)
  * `[HdfsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.HdfsData)` (message)
  * `[HttpData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.HttpData)` (message)
  * `[ListAgentPoolsRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListAgentPoolsRequest)` (message)
  * `[ListAgentPoolsResponse](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListAgentPoolsResponse)` (message)
  * `[ListTransferJobsRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListTransferJobsRequest)` (message)
  * `[ListTransferJobsResponse](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListTransferJobsResponse)` (message)
  * `[LoggingConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig)` (message)
  * `[LoggingConfig.LoggableAction](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig.LoggableAction)` (enum)
  * `[LoggingConfig.LoggableActionState](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig.LoggableActionState)` (enum)
  * `[MetadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions)` (message)
  * `[MetadataOptions.Acl](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Acl)` (enum)
  * `[MetadataOptions.GID](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.GID)` (enum)
  * `[MetadataOptions.KmsKey](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.KmsKey)` (enum)
  * `[MetadataOptions.Mode](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Mode)` (enum)
  * `[MetadataOptions.StorageClass](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.StorageClass)` (enum)
  * `[MetadataOptions.Symlink](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Symlink)` (enum)
  * `[MetadataOptions.TemporaryHold](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TemporaryHold)` (enum)
  * `[MetadataOptions.TimeCreated](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TimeCreated)` (enum)
  * `[MetadataOptions.UID](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.UID)` (enum)
  * `[NotificationConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig)` (message)
  * `[NotificationConfig.EventType](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.EventType)` (enum)
  * `[NotificationConfig.PayloadFormat](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.PayloadFormat)` (enum)
  * `[ObjectConditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions)` (message)
  * `[PauseTransferOperationRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PauseTransferOperationRequest)` (message)
  * `[PosixFilesystem](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PosixFilesystem)` (message)
  * `[ReplicationSpec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ReplicationSpec)` (message)
  * `[ResumeTransferOperationRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ResumeTransferOperationRequest)` (message)
  * `[RunTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.RunTransferJobRequest)` (message)
  * `[S3CompatibleMetadata](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata)` (message)
  * `[S3CompatibleMetadata.AuthMethod](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.AuthMethod)` (enum)
  * `[S3CompatibleMetadata.ListApi](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.ListApi)` (enum)
  * `[S3CompatibleMetadata.NetworkProtocol](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.NetworkProtocol)` (enum)
  * `[S3CompatibleMetadata.RequestModel](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.RequestModel)` (enum)
  * `[Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule)` (message)
  * `[TransferCounters](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferCounters)` (message)
  * `[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)` (message)
  * `[TransferJob.Status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status)` (enum)
  * `[TransferManifest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferManifest)` (message)
  * `[TransferOperation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation)` (message)
  * `[TransferOperation.Status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.Status)` (enum)
  * `[TransferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions)` (message)
  * `[TransferOptions.OverwriteWhen](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.OverwriteWhen)` (enum)
  * `[TransferSpec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferSpec)` (message)
  * `[UpdateAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.UpdateAgentPoolRequest)` (message)
  * `[UpdateTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.UpdateTransferJobRequest)` (message)



## StorageTransferService

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

CreateAgentPool  
---  
` rpc CreateAgentPool(`[CreateAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.CreateAgentPoolRequest)`) returns (`[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)`) ` Creates an agent pool resource.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateTransferJob  
---  
` rpc CreateTransferJob(`[CreateTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.CreateTransferJobRequest)`) returns (`[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)`) ` Creates a transfer job that runs periodically.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteAgentPool  
---  
` rpc DeleteAgentPool(`[DeleteAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.DeleteAgentPoolRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an agent pool.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteTransferJob  
---  
` rpc DeleteTransferJob(`[DeleteTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.DeleteTransferJobRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a transfer job. Deleting a transfer job sets its status to `[DELETED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DELETED)`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetAgentPool  
---  
` rpc GetAgentPool(`[GetAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetAgentPoolRequest)`) returns (`[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)`) ` Gets an agent pool.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetGoogleServiceAccount  
---  
` rpc GetGoogleServiceAccount(`[GetGoogleServiceAccountRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetGoogleServiceAccountRequest)`) returns (`[GoogleServiceAccount](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GoogleServiceAccount)`) ` Returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects. Each Google service account is associated with one Google Cloud project. Users should add this service account to the Google Cloud Storage bucket ACLs to grant access to Storage Transfer Service. This service account is created and owned by Storage Transfer Service and can only be used by Storage Transfer Service.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetTransferJob  
---  
` rpc GetTransferJob(`[GetTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GetTransferJobRequest)`) returns (`[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)`) ` Gets a transfer job.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListAgentPools  
---  
` rpc ListAgentPools(`[ListAgentPoolsRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListAgentPoolsRequest)`) returns (`[ListAgentPoolsResponse](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListAgentPoolsResponse)`) ` Lists agent pools.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTransferJobs  
---  
` rpc ListTransferJobs(`[ListTransferJobsRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListTransferJobsRequest)`) returns (`[ListTransferJobsResponse](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ListTransferJobsResponse)`) ` Lists transfer jobs.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
PauseTransferOperation  
---  
` rpc PauseTransferOperation(`[PauseTransferOperationRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PauseTransferOperationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Pauses a transfer operation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ResumeTransferOperation  
---  
` rpc ResumeTransferOperation(`[ResumeTransferOperationRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ResumeTransferOperationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Resumes a transfer operation that is paused.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
RunTransferJob  
---  
` rpc RunTransferJob(`[RunTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.RunTransferJobRequest)`) returns (`[Operation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Starts a new operation for the specified transfer job. A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateAgentPool  
---  
` rpc UpdateAgentPool(`[UpdateAgentPoolRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.UpdateAgentPoolRequest)`) returns (`[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)`) ` Updates an existing agent pool resource.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateTransferJob  
---  
` rpc UpdateTransferJob(`[UpdateTransferJobRequest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.UpdateTransferJobRequest)`) returns (`[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)`) ` Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already.**Note:** The job's `[status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.TransferJob.Status.google.storagetransfer.v1.TransferJob.status)` field can be modified using this RPC (for example, to set a job's status to `[DELETED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DELETED)`, `[DISABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DISABLED)`, or `[ENABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.ENABLED)`).

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AgentPool

Represents an agent pool.

Fields  
---  
`name` |  `string` Required. Specifies a unique string that identifies the agent pool.Format: `projects/{project_id}/agentPools/{agent_pool_id}`  
`display_name` |  `string` Specifies the client-specified AgentPool description.  
`state` |  `[State](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.State)` Output only. Specifies the state of the AgentPool.  
`bandwidth_limit` |  `[BandwidthLimit](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.BandwidthLimit)` Specifies the bandwidth limit details. If this field is unspecified, the default value is set as 'No Limit'.  
  
## BandwidthLimit

Specifies a bandwidth limit for an agent pool.

Fields  
---  
`limit_mbps` |  `int64` Bandwidth rate in megabytes per second, distributed across all the agents in the pool.  
  
## State

The state of an AgentPool.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | This is an initialization state. During this stage, resources are allocated for the AgentPool.  
`CREATED` | Determines that the AgentPool is created for use. At this state, Agents can join the AgentPool and participate in the transfer jobs in that pool.  
`DELETING` | Determines that the AgentPool deletion has been initiated, and all the resources are scheduled to be cleaned up and freed.  
  
## AwsAccessKey

AWS access key (see [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html)).

For information on our data retention policy for user credentials, see [User credentials](https://docs.cloud.google.com/storage-transfer/docs/data-retention#user-credentials).

Fields  
---  
`access_key_id` |  `string` Required. AWS access key ID.  
`secret_access_key` |  `string` Required. AWS secret access key. This field is not returned in RPC responses.  
  
## AwsS3CompatibleData

An AwsS3CompatibleData resource.

Fields  
---  
`bucket_name` |  `string` Required. Specifies the name of the bucket.  
`path` |  `string` Specifies the root path to transfer objects.Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.  
`endpoint` |  `string` Required. Specifies the endpoint of the storage service.  
`region` |  `string` Specifies the region to sign requests with. This can be left blank if requests should be signed with an empty region.  
Union field `data_provider`. Specifies the metadata of the S3 compatible data provider. Each provider may contain some attributes that do not apply to all S3-compatible data providers. When not specified, S3CompatibleMetadata is used by default. `data_provider` can be only one of the following:  
`s3_metadata` |  `[S3CompatibleMetadata](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata)` A S3 compatible metadata.  
  
## AwsS3Data

An AwsS3Data resource can be a data source, but not a data sink. In an AwsS3Data resource, an object's name is the S3 object's key name.

Fields  
---  
`bucket_name` |  `string` Required. S3 Bucket name (see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/create-bucket-get-location-example.html)).  
`aws_access_key` |  `[AwsAccessKey](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsAccessKey)` Input only. AWS access key used to sign the API requests to the AWS S3 bucket. Permissions on the bucket must be granted to the access ID of the AWS access key.For information on our data retention policy for user credentials, see [User credentials](https://docs.cloud.google.com/storage-transfer/docs/data-retention#user-credentials).  
`path` |  `string` Root path to transfer objects.Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.  
`role_arn` |  `string` The Amazon Resource Name (ARN) of the role to support temporary credentials via `AssumeRoleWithWebIdentity`. For more information about ARNs, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).When a role ARN is provided, Transfer Service fetches temporary credentials for the session using a `AssumeRoleWithWebIdentity` call for the provided role using the `[GoogleServiceAccount](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GoogleServiceAccount)` for this project.  
`cloudfront_domain` |  `string` Optional. The CloudFront distribution domain name pointing to this bucket, to use when fetching.See [Transfer from S3 via CloudFront](https://cloud.google.com/storage-transfer/docs/s3-cloudfront) for more information.Format: `https://{id}.cloudfront.net` or any valid custom domain. Must begin with `https://`.  
`credentials_secret` |  `string` Optional. The Resource name of a secret in Secret Manager.AWS credentials must be stored in Secret Manager in JSON format:{ "access_key_id": "ACCESS_KEY_ID", "secret_access_key": "SECRET_ACCESS_KEY" }`[GoogleServiceAccount](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GoogleServiceAccount)` must be granted `roles/secretmanager.secretAccessor` for the resource.See [Configure access to a source: Amazon S3](https://cloud.google.com/storage-transfer/docs/source-amazon-s3#secret_manager) for more information.If `credentials_secret` is specified, do not specify `[role_arn](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3Data.FIELDS.string.google.storagetransfer.v1.AwsS3Data.role_arn)` or `[aws_access_key](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3Data.FIELDS.google.storagetransfer.v1.AwsAccessKey.google.storagetransfer.v1.AwsS3Data.aws_access_key)`.Format: `projects/{project_number}/secrets/{secret_name}`  
Union field `private_network`.`private_network` can be only one of the following:  
`managed_private_network` |  `bool` Egress bytes over a Google-managed private network. This network is shared between other users of Storage Transfer Service.  
`private_network_service` |  `string` Service Directory Service to be used as the endpoint for transfers from a custom VPC.Format: `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service}`  
  
## AzureBlobStorageData

An AzureBlobStorageData resource can be a data source, but not a data sink. An AzureBlobStorageData resource represents one Azure container. The storage account determines the [Azure endpoint](https://docs.microsoft.com/en-us/azure/storage/common/storage-create-storage-account#storage-account-endpoints). In an AzureBlobStorageData resource, a blobs's name is the [Azure Blob Storage blob's key name](https://docs.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#blob-names).

Fields  
---  
`storage_account` |  `string` Required. The name of the Azure Storage account.  
`azure_credentials` |  `[AzureCredentials](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureCredentials)` Required. Input only. Credentials used to authenticate API requests to Azure.For information on our data retention policy for user credentials, see [User credentials](https://docs.cloud.google.com/storage-transfer/docs/data-retention#user-credentials).  
`container` |  `string` Required. The container to transfer from the Azure Storage account.  
`path` |  `string` Root path to transfer objects.Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.  
`credentials_secret` |  `string` Optional. The Resource name of a secret in Secret Manager.The Azure SAS token must be stored in Secret Manager in JSON format:{ "sas_token" : "SAS_TOKEN" }`[GoogleServiceAccount](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GoogleServiceAccount)` must be granted `roles/secretmanager.secretAccessor` for the resource.See [Configure access to a source: Microsoft Azure Blob Storage](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#secret_manager) for more information.If `credentials_secret` is specified, do not specify `[azure_credentials](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData.FIELDS.google.storagetransfer.v1.AzureCredentials.google.storagetransfer.v1.AzureBlobStorageData.azure_credentials)`.Format: `projects/{project_number}/secrets/{secret_name}`  
`federated_identity_config` |  `[FederatedIdentityConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData.FederatedIdentityConfig)` Optional. Federated identity config of a user registered Azure application.If `federated_identity_config` is specified, do not specify `[azure_credentials](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData.FIELDS.google.storagetransfer.v1.AzureCredentials.google.storagetransfer.v1.AzureBlobStorageData.azure_credentials)` or `[credentials_secret](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData.FIELDS.string.google.storagetransfer.v1.AzureBlobStorageData.credentials_secret)`.  
Union field `private_network`.`private_network` can be only one of the following:  
`private_network_service` |  `string` Service Directory Service to be used as the endpoint for transfers from a customer-managed private network.Format: `projects/{projectId}/locations/{location}/namespaces/{namespace}/services/{service}`See [Transfer from AWS or Azure over a customer-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network) for more information.  
Union field `private_network`.`private_network` can be only one of the following:  
`private_network_service` |  `string` Service Directory Service to be used as the endpoint for transfers from a custom VPC.Format: `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service}`  
  
## FederatedIdentityConfig

The identity of an Azure application through which Storage Transfer Service can authenticate requests using Azure workload identity federation.

Storage Transfer Service can issue requests to Azure Storage through registered Azure applications, eliminating the need to pass credentials to Storage Transfer Service directly.

To configure federated identity, see [Configure access to Microsoft Azure Storage](https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#option_3_authenticate_using_federated_identity).

Fields  
---  
`client_id` |  `string` Required. The client (application) ID of the application with federated credentials.  
`tenant_id` |  `string` Required. The tenant (directory) ID of the application with federated credentials.  
  
## AzureCredentials

Azure credentials

For information on our data retention policy for user credentials, see [User credentials](https://docs.cloud.google.com/storage-transfer/docs/data-retention#user-credentials).

Fields  
---  
`sas_token` |  `string` Required. Azure shared access signature (SAS).For more information about SAS, see [Grant limited access to Azure Storage resources using shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview).  
  
## CreateAgentPoolRequest

Specifies the request passed to CreateAgentPool.

Fields  
---  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the agent pool. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `storagetransfer.agentpools.create`

  
`agent_pool` |  `[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)` Required. The agent pool to create.  
`agent_pool_id` |  `string` Required. The ID of the agent pool to create.The `agent_pool_id` must meet the following requirements:

  * Length of 128 characters or less.
  * Not start with the string `goog`.
  * Start with a lowercase ASCII character, followed by: 
    * Zero or more: lowercase Latin alphabet characters, numerals, hyphens (`-`), periods (`.`), underscores (`_`), or tildes (`~`).
    * One or more numerals or lowercase ASCII characters.

As expressed by the regular expression: `^(?!goog)[a-z]([a-z0-9-._~]*[a-z0-9])?$`.  
  
## CreateTransferJobRequest

Request passed to CreateTransferJob.

Fields  
---  
`transfer_job` |  `[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)` Required. The job to create. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `transferJob`:

  * `storagetransfer.jobs.create`

  
  
## DeleteAgentPoolRequest

Specifies the request passed to DeleteAgentPool.

Fields  
---  
`name` |  `string` Required. The name of the agent pool to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `storagetransfer.agentpools.delete`

  
  
## DeleteTransferJobRequest

Request passed to DeleteTransferJob.

Fields  
---  
`job_name` |  `string` Required. The job to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `jobName`:

  * `storagetransfer.jobs.delete`

  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the job.  
  
## ErrorLogEntry

LINT.IfChange An entry describing an error that has occurred.

Fields  
---  
`url` |  `string` Output only. A URL that refers to the target (a data source, a data sink, or an object) with which the error is associated.  
`error_details[]` |  `string` Optional. A list of messages that carry the error details.  
  
## ErrorSummary

A summary of errors by error code, plus a count and sample error log entries.

Fields  
---  
`error_code` |  `[Code](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code)` Required.  
`error_count` |  `int64` Required. Count of this type of error.  
`error_log_entries[]` |  `[ErrorLogEntry](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ErrorLogEntry)` Error samples.At most 5 error log entries are recorded for a given error code for a single transfer operation.  
  
## EventStream

Specifies the Event-driven transfer options. Event-driven transfers listen to an event stream to transfer updated files.

Fields  
---  
`name` |  `string` Required. Specifies a unique name of the resource such as AWS SQS ARN in the form 'arn:aws:sqs:region:account_id:queue_name', or Pub/Sub subscription resource name in the form 'projects/{project}/subscriptions/{sub}'.  
`event_stream_start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Specifies the date and time that Storage Transfer Service starts listening for events from this stream. If no start time is specified or start time is in the past, Storage Transfer Service starts listening immediately.  
`event_stream_expiration_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Specifies the data and time at which Storage Transfer Service stops listening for events from this stream. After this time, any transfers in progress will complete, but no new transfers are initiated.  
  
## GcsData

In a GcsData resource, an object's name is the Cloud Storage object's name and its "last modification time" refers to the object's `updated` property of Cloud Storage objects, which changes when the content or the metadata of the object is updated.

Fields  
---  
`bucket_name` |  `string` Required. Cloud Storage bucket name. Must meet [Bucket Name Requirements](https://docs.cloud.google.com/storage/docs/naming#requirements).  
`path` |  `string` Root path to transfer objects.Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.The root path value must meet [Object Name Requirements](https://docs.cloud.google.com/storage/docs/naming#objectnames).  
`managed_folder_transfer_enabled` |  `bool` Preview. Enables the transfer of managed folders between Cloud Storage buckets. Set this option on the gcs_data_source.If set to true:

  * Managed folders in the source bucket are transferred to the destination bucket.
  * Managed folders in the destination bucket are overwritten. Other OVERWRITE options are not supported.

See [Transfer Cloud Storage managed folders](https://docs.cloud.google.com/storage-transfer/docs/managed-folders).  
  
## GetAgentPoolRequest

Specifies the request passed to GetAgentPool.

Fields  
---  
`name` |  `string` Required. The name of the agent pool to get. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `storagetransfer.agentpools.get`

  
  
## GetGoogleServiceAccountRequest

Request passed to GetGoogleServiceAccount.

Fields  
---  
`project_id` |  `string` Required. The ID of the Google Cloud project that the Google service account is associated with. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `storagetransfer.projects.getServiceAccount`

  
  
## GetTransferJobRequest

Request passed to GetTransferJob.

Fields  
---  
`job_name` |  `string` Required. The job to get. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `jobName`:

  * `storagetransfer.jobs.get`

  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the job.  
  
## GoogleServiceAccount

Google service account

Fields  
---  
`account_email` |  `string` Email address of the service account.  
`subject_id` |  `string` Unique identifier for the service account.  
  
## HdfsData

An HdfsData resource specifies a path within an HDFS entity (e.g. a cluster). All cluster-specific settings, such as namenodes and ports, are configured on the transfer agents servicing requests, so HdfsData only contains the root path to the data in our transfer.

Fields  
---  
`path` |  `string` Root path to transfer files.  
  
## HttpData

An HttpData resource specifies a list of objects on the web to be transferred over HTTP. The information of the objects to be transferred is contained in a file referenced by a URL. The first line in the file must be `"TsvHttpData-1.0"`, which specifies the format of the file. Subsequent lines specify the information of the list of objects, one object per list entry. Each entry has the following tab-delimited fields:

  * **HTTP URL** — The location of the object.

  * **Length** — The size of the object in bytes.

  * **MD5** — The base64-encoded MD5 hash of the object.




For an example of a valid TSV file, see [Transferring data from URLs](https://cloud.google.com/storage-transfer/docs/create-url-list).

When transferring data based on a URL list, keep the following in mind:

  * When an object located at `http(s)://hostname:port/<URL-path>` is transferred to a data sink, the name of the object at the data sink is `<hostname>/<URL-path>`.

  * If the specified size of an object does not match the actual size of the object fetched, the object is not transferred.

  * If the specified MD5 does not match the MD5 computed from the transferred bytes, the object transfer fails.

  * Ensure that each URL you specify is publicly accessible. For example, in Cloud Storage you can [share an object publicly](https://docs.cloud.google.com/storage/docs/cloud-console#_sharingdata) and get a link to it.

  * Storage Transfer Service obeys `robots.txt` rules and requires the source HTTP server to support `Range` requests and to return a `Content-Length` header in each response.

  * `[ObjectConditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions)` have no effect when filtering objects to transfer.


Fields  
---  
`list_url` |  `string` Required. The URL that points to the file that stores the object list entries. This file must allow public access. The URL is either an HTTP/HTTPS address (e.g. `https://example.com/urllist.tsv`) or a Cloud Storage path (e.g. `gs://my-bucket/urllist.tsv`).  
  
## ListAgentPoolsRequest

The request passed to ListAgentPools.

Fields  
---  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the job. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `storagetransfer.agentpools.list`

  
`filter` |  `string` An optional list of query parameters specified as JSON text in the form of:`{"agentPoolNames":["agentpool1","agentpool2",...]}`Since `agentPoolNames` support multiple values, its values must be specified with array notation. When the filter is either empty or not provided, the list returns all agent pools for the project.  
`page_size` |  `int32` The list page size. The max allowed value is `256`.  
`page_token` |  `string` The list page token.  
  
## ListAgentPoolsResponse

Response from ListAgentPools.

Fields  
---  
`agent_pools[]` |  `[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)` A list of agent pools.  
`next_page_token` |  `string` The list next page token.  
  
## ListTransferJobsRequest

`projectId`, `jobNames`, and `jobStatuses` are query parameters that can be specified when listing transfer jobs.

Fields  
---  
`filter` |  `string` Required. A list of query parameters specified as JSON text in the form of:
    
    
    {
      "projectId":"my_project_id",
      "jobNames":["jobid1","jobid2",...],
      "jobStatuses":["status1","status2",...],
      "dataBackend":"QUERY_REPLICATION_CONFIGS",
      "sourceBucket":"source-bucket-name",
      "sinkBucket":"sink-bucket-name",
    }
    

The JSON formatting in the example is for display only; provide the query parameters without spaces or line breaks.

  * `projectId` is required.
  * Since `jobNames` and `jobStatuses` support multiple values, their values must be specified with array notation. `jobNames` and `jobStatuses` are optional. Valid values are case-insensitive: 
    * `[ENABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.ENABLED)`
    * `[DISABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DISABLED)`
    * `[DELETED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DELETED)`
  * Specify `"dataBackend":"QUERY_REPLICATION_CONFIGS"` to return a list of cross-bucket replication jobs.
  * Limit the results to jobs from a particular bucket with `sourceBucket` and/or to a particular bucket with `sinkBucket`.

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `filter`:

  * `storagetransfer.jobs.list`

  
`page_size` |  `int32` The list page size. The max allowed value is 256.  
`page_token` |  `string` The list page token.  
  
## ListTransferJobsResponse

Response from ListTransferJobs.

Fields  
---  
`transfer_jobs[]` |  `[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)` A list of transfer jobs.  
`next_page_token` |  `string` The list next page token.  
  
## LoggingConfig

Specifies the logging behavior for transfer operations.

Logs can be sent to Cloud Logging for all transfer types. See [Read transfer logs](https://cloud.google.com/storage-transfer/docs/read-transfer-logs) for details.

Fields  
---  
`log_actions[]` |  `[LoggableAction](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig.LoggableAction)` Specifies the actions to be logged. If empty, no logs are generated.  
`log_action_states[]` |  `[LoggableActionState](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig.LoggableActionState)` States in which `log_actions` are logged. If empty, no logs are generated.  
`enable_onprem_gcs_transfer_logs` |  `bool` For PosixFilesystem transfers, enables [file system transfer logs](https://cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format) instead of, or in addition to, Cloud Logging.This option ignores [LoggableAction] and [LoggableActionState]. If these are set, Cloud Logging will also be enabled for this transfer.  
  
## LoggableAction

Loggable actions.

Enums  
---  
`LOGGABLE_ACTION_UNSPECIFIED` | Default value. This value is unused.  
`FIND` | Listing objects in a bucket.  
`DELETE` | Deleting objects at the source or the destination.  
`COPY` | Copying objects to the destination.  
  
## LoggableActionState

Loggable action states.

Enums  
---  
`LOGGABLE_ACTION_STATE_UNSPECIFIED` | Default value. This value is unused.  
`SUCCEEDED` | `LoggableAction` completed successfully. `SUCCEEDED` actions are logged as `INFO`.  
`FAILED` | `LoggableAction` terminated in an error state. `FAILED` actions are logged as `ERROR`.  
`SKIPPED` | The `COPY` action was skipped for this file. Only supported for agent-based transfers. `SKIPPED` actions are logged as `INFO`.  
  
## MetadataOptions

Specifies the metadata options for running a transfer.

Fields  
---  
`symlink` |  `[Symlink](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Symlink)` Specifies how symlinks should be handled by the transfer. By default, symlinks are not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers.  
`mode` |  `[Mode](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Mode)` Specifies how each file's mode attribute should be handled by the transfer. By default, mode is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers.  
`gid` |  `[GID](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.GID)` Specifies how each file's POSIX group ID (GID) attribute should be handled by the transfer. By default, GID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers.  
`uid` |  `[UID](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.UID)` Specifies how each file's POSIX user ID (UID) attribute should be handled by the transfer. By default, UID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers.  
`acl` |  `[Acl](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.Acl)` Specifies how each object's ACLs should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as ACL_DESTINATION_BUCKET_DEFAULT.  
`storage_class` |  `[StorageClass](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.StorageClass)` Specifies the storage class to set on objects being transferred to Google Cloud Storage buckets. If unspecified, the default behavior is the same as `[STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.StorageClass.ENUM_VALUES.google.storagetransfer.v1.MetadataOptions.StorageClass.STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT)`.  
`temporary_hold` |  `[TemporaryHold](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TemporaryHold)` Specifies how each object's temporary hold status should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as `[TEMPORARY_HOLD_PRESERVE](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TemporaryHold.ENUM_VALUES.google.storagetransfer.v1.MetadataOptions.TemporaryHold.TEMPORARY_HOLD_PRESERVE)`.  
`kms_key` |  `[KmsKey](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.KmsKey)` Specifies how each object's Cloud KMS customer-managed encryption key (CMEK) is preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as `[KMS_KEY_DESTINATION_BUCKET_DEFAULT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.KmsKey.ENUM_VALUES.google.storagetransfer.v1.MetadataOptions.KmsKey.KMS_KEY_DESTINATION_BUCKET_DEFAULT)`.  
`time_created` |  `[TimeCreated](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TimeCreated)` Specifies how each object's `timeCreated` metadata is preserved for transfers. If unspecified, the default behavior is the same as `[TIME_CREATED_SKIP](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions.TimeCreated.ENUM_VALUES.google.storagetransfer.v1.MetadataOptions.TimeCreated.TIME_CREATED_SKIP)`. This behavior is supported for transfers to Cloud Storage buckets from Cloud Storage, Amazon S3, S3-compatible storage, and Azure sources.  
  
## Acl

Options for handling Cloud Storage object ACLs.

Enums  
---  
`ACL_UNSPECIFIED` | ACL behavior is unspecified.  
`ACL_DESTINATION_BUCKET_DEFAULT` | Use the destination bucket's default object ACLS, if applicable.  
`ACL_PRESERVE` | Preserve the object's original ACLs. This requires the service account to have `storage.objects.getIamPolicy` permission for the source object. [Uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) must not be enabled on either the source or destination buckets.  
  
## GID

Options for handling file GID attribute.

Enums  
---  
`GID_UNSPECIFIED` | GID behavior is unspecified.  
`GID_SKIP` | Do not preserve GID during a transfer job.  
`GID_NUMBER` | Preserve GID during a transfer job.  
  
## KmsKey

Options for handling the KmsKey setting for Google Cloud Storage objects.

Enums  
---  
`KMS_KEY_UNSPECIFIED` | KmsKey behavior is unspecified.  
`KMS_KEY_DESTINATION_BUCKET_DEFAULT` | Use the destination bucket's default encryption settings.  
`KMS_KEY_PRESERVE` | Preserve the object's original Cloud KMS customer-managed encryption key (CMEK) if present. Objects that do not use a Cloud KMS encryption key will be encrypted using the destination bucket's encryption settings.  
  
## Mode

Options for handling file mode attribute.

Enums  
---  
`MODE_UNSPECIFIED` | Mode behavior is unspecified.  
`MODE_SKIP` | Do not preserve mode during a transfer job.  
`MODE_PRESERVE` | Preserve mode during a transfer job.  
  
## StorageClass

Options for handling Google Cloud Storage object storage class.

Enums  
---  
`STORAGE_CLASS_UNSPECIFIED` | Storage class behavior is unspecified.  
`STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT` | Use the destination bucket's default storage class.  
`STORAGE_CLASS_PRESERVE` | Preserve the object's original storage class. This is only supported for transfers from Google Cloud Storage buckets. REGIONAL and MULTI_REGIONAL storage classes will be mapped to STANDARD to ensure they can be written to the destination bucket.  
`STORAGE_CLASS_STANDARD` | Set the storage class to STANDARD.  
`STORAGE_CLASS_NEARLINE` | Set the storage class to NEARLINE.  
`STORAGE_CLASS_COLDLINE` | Set the storage class to COLDLINE.  
`STORAGE_CLASS_ARCHIVE` | Set the storage class to ARCHIVE.  
  
## Symlink

Whether symlinks should be skipped or preserved during a transfer job.

Enums  
---  
`SYMLINK_UNSPECIFIED` | Symlink behavior is unspecified.  
`SYMLINK_SKIP` | Do not preserve symlinks during a transfer job.  
`SYMLINK_PRESERVE` | Preserve symlinks during a transfer job.  
  
## TemporaryHold

Options for handling temporary holds for Google Cloud Storage objects.

Enums  
---  
`TEMPORARY_HOLD_UNSPECIFIED` | Temporary hold behavior is unspecified.  
`TEMPORARY_HOLD_SKIP` | Do not set a temporary hold on the destination object.  
`TEMPORARY_HOLD_PRESERVE` | Preserve the object's original temporary hold status.  
  
## TimeCreated

Options for handling `timeCreated` metadata for Google Cloud Storage objects.

Enums  
---  
`TIME_CREATED_UNSPECIFIED` | TimeCreated behavior is unspecified.  
`TIME_CREATED_SKIP` | Do not preserve the `timeCreated` metadata from the source object.  
`TIME_CREATED_PRESERVE_AS_CUSTOM_TIME` | Preserves the source object's `timeCreated` or `lastModified` metadata in the `customTime` field in the destination object. Note that any value stored in the source object's `customTime` field will not be propagated to the destination object.  
  
## UID

Options for handling file UID attribute.

Enums  
---  
`UID_UNSPECIFIED` | UID behavior is unspecified.  
`UID_SKIP` | Do not preserve UID during a transfer job.  
`UID_NUMBER` | Preserve UID during a transfer job.  
  
## NotificationConfig

Specification to configure notifications published to Pub/Sub. Notifications are published to the customer-provided topic using the following `PubsubMessage.attributes`:

  * `"eventType"`: one of the `[EventType](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.EventType)` values
  * `"payloadFormat"`: one of the `[PayloadFormat](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.PayloadFormat)` values
  * `"projectId"`: the `[project_id](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.FIELDS.string.google.storagetransfer.v1.TransferOperation.project_id)` of the `TransferOperation`
  * `"transferJobName"`: the `[transfer_job_name](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.FIELDS.string.google.storagetransfer.v1.TransferOperation.transfer_job_name)` of the `TransferOperation`
  * `"transferOperationName"`: the `[name](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.FIELDS.string.google.storagetransfer.v1.TransferOperation.name)` of the `TransferOperation`



The `PubsubMessage.data` contains a `[TransferOperation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation)` resource formatted according to the specified `PayloadFormat`.

Fields  
---  
`pubsub_topic` |  `string` Required. The `Topic.name` of the Pub/Sub topic to which to publish notifications. Must be of the format: `projects/{project}/topics/{topic}`. Not matching this format results in an `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` error.  
`event_types[]` |  `[EventType](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.EventType)` Event types for which a notification is desired. If empty, send notifications for all event types.  
`payload_format` |  `[PayloadFormat](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig.PayloadFormat)` Required. The desired format of the notification message payloads.  
  
## EventType

Enum for specifying event types for which notifications are to be published.

Additional event types may be added in the future. Clients should either safely ignore unrecognized event types or explicitly specify which event types they are prepared to accept.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | Illegal value, to avoid allowing a default.  
`TRANSFER_OPERATION_SUCCESS` | `TransferOperation` completed with status `[SUCCESS](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.Status.ENUM_VALUES.google.storagetransfer.v1.TransferOperation.Status.SUCCESS)`.  
`TRANSFER_OPERATION_FAILED` | `TransferOperation` completed with status `[FAILED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.Status.ENUM_VALUES.google.storagetransfer.v1.TransferOperation.Status.FAILED)`.  
`TRANSFER_OPERATION_ABORTED` | `TransferOperation` completed with status `[ABORTED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.Status.ENUM_VALUES.google.storagetransfer.v1.TransferOperation.Status.ABORTED)`.  
  
## PayloadFormat

Enum for specifying the format of a notification message's payload.

Enums  
---  
`PAYLOAD_FORMAT_UNSPECIFIED` | Illegal value, to avoid allowing a default.  
`NONE` | No payload is included with the notification.  
`JSON` | `TransferOperation` is [formatted as a JSON response](https://developers.google.com/protocol-buffers/docs/proto3#json), in application/json.  
  
## ObjectConditions

Conditions that determine which objects are transferred. Applies only to Cloud Data Sources such as S3, Azure, and Cloud Storage.

The "last modification time" refers to the time of the last change to the object's content or metadata — specifically, this is the `updated` property of Cloud Storage objects, the `LastModified` field of S3 objects, and the `Last-Modified` header of Azure blobs.

For S3 objects, the `LastModified` value is the time the object begins uploading. If the object meets your "last modification time" criteria, but has not finished uploading, the object is not transferred. See [Transfer from Amazon S3 to Cloud Storage](https://cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#transfer_options) for more information.

Transfers with a `[PosixFilesystem](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PosixFilesystem)` source or destination don't support `ObjectConditions`.

Fields  
---  
`min_time_elapsed_since_last_modification` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Ensures that objects are not transferred until a specific minimum time has elapsed after the "last modification time". When a `[TransferOperation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation)` begins, objects with a "last modification time" are transferred only if the elapsed time between the `[start_time](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.FIELDS.google.protobuf.Timestamp.google.storagetransfer.v1.TransferOperation.start_time)` of the `TransferOperation` and the "last modification time" of the object is equal to or greater than the value of min_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.  
`max_time_elapsed_since_last_modification` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Ensures that objects are not transferred if a specific maximum time has elapsed since the "last modification time". When a `[TransferOperation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation)` begins, objects with a "last modification time" are transferred only if the elapsed time between the `[start_time](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.FIELDS.google.protobuf.Timestamp.google.storagetransfer.v1.TransferOperation.start_time)` of the `TransferOperation`and the "last modification time" of the object is less than the value of max_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.  
`include_prefixes[]` |  `string` If you specify `include_prefixes`, Storage Transfer Service uses the items in the `include_prefixes` array to determine which objects to include in a transfer. Objects must start with one of the matching `include_prefixes` for inclusion in the transfer. If `[exclude_prefixes](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions.FIELDS.repeated.string.google.storagetransfer.v1.ObjectConditions.exclude_prefixes)` is specified, objects must not start with any of the `exclude_prefixes` specified for inclusion in the transfer.The following are requirements of `include_prefixes`:

  * Each include-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported.
  * Each include-prefix must omit the leading slash. For example, to include the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the include-prefix as `logs/y=2015/requests.gz`.
  * None of the include-prefix values can be empty, if specified.
  * Each include-prefix must include a distinct portion of the object namespace. No include-prefix may be a prefix of another include-prefix.

The max size of `include_prefixes` is 1000.For more information, see [Filtering objects from transfers](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).  
`exclude_prefixes[]` |  `string` If you specify `exclude_prefixes`, Storage Transfer Service uses the items in the `exclude_prefixes` array to determine which objects to exclude from a transfer. Objects must not start with one of the matching `exclude_prefixes` for inclusion in a transfer.The following are requirements of `exclude_prefixes`:

  * Each exclude-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported.
  * Each exclude-prefix must omit the leading slash. For example, to exclude the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the exclude-prefix as `logs/y=2015/requests.gz`.
  * None of the exclude-prefix values can be empty, if specified.
  * Each exclude-prefix must exclude a distinct portion of the object namespace. No exclude-prefix may be a prefix of another exclude-prefix.
  * If `[include_prefixes](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions.FIELDS.repeated.string.google.storagetransfer.v1.ObjectConditions.include_prefixes)` is specified, then each exclude-prefix must start with the value of a path explicitly included by `include_prefixes`.

The max size of `exclude_prefixes` is 1000.For more information, see [Filtering objects from transfers](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).  
`last_modified_since` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` If specified, only objects with a "last modification time" on or after this timestamp and objects that don't have a "last modification time" are transferred.The `last_modified_since` and `last_modified_before` fields can be used together for chunked data processing. For example, consider a script that processes each day's worth of data at a time. For that you'd set each of the fields as follows:

  * `last_modified_since` to the start of the day
  * `last_modified_before` to the end of the day

  
`last_modified_before` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` If specified, only objects with a "last modification time" before this timestamp and objects that don't have a "last modification time" are transferred.  
`match_glob` |  `string` Optional. If specified, only objects matching this glob are transferred.  
`include_storage_classes[]` |  `string` Optional. If specified, objects in the source matching any of the storage classes in this field will be transferred. Objects in storage classes not included in this field will be skipped.If empty, the default behavior regarding the storage classes is applied. This includes all storage classes except "GLACIER" as per default behavior.Currently, this field only supports S3 data source. For the list of valid Amazon S3 storage classnames, please refer to the AWS documentation: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/sc-howtoset.html>  
  
## PauseTransferOperationRequest

Request passed to PauseTransferOperation.

Fields  
---  
`name` |  `string` Required. The name of the transfer operation. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `storagetransfer.operations.pause`

  
  
## PosixFilesystem

A POSIX filesystem resource.

Fields  
---  
`root_directory` |  `string` Root directory path to the filesystem.  
  
## ReplicationSpec

Specifies the configuration for a cross-bucket replication job. Cross-bucket replication copies new or updated objects from a source Cloud Storage bucket to a destination Cloud Storage bucket. Existing objects in the source bucket are not copied by a new cross-bucket replication job.

Fields  
---  
`object_conditions` |  `[ObjectConditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions)` Object conditions that determine which objects are transferred. For replication jobs, only `include_prefixes` and `exclude_prefixes` are supported.  
`transfer_options` |  `[TransferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions)` Specifies the metadata options to be applied during replication. Delete options are not supported. If a delete option is specified, the request fails with an `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` error.  
Union field `data_source`. The data source to be replicated. `data_source` can be only one of the following:  
`gcs_data_source` |  `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` The Cloud Storage bucket from which to replicate objects.  
Union field `data_sink`. The destination for replicated objects. `data_sink` can be only one of the following:  
`gcs_data_sink` |  `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` The Cloud Storage bucket to which to replicate objects.  
  
## ResumeTransferOperationRequest

Request passed to ResumeTransferOperation.

Fields  
---  
`name` |  `string` Required. The name of the transfer operation. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `storagetransfer.operations.resume`

  
  
## RunTransferJobRequest

Request passed to RunTransferJob.

Fields  
---  
`job_name` |  `string` Required. The name of the transfer job. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `jobName`:

  * `storagetransfer.jobs.run`

  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the transfer job.  
  
## S3CompatibleMetadata

S3CompatibleMetadata contains the metadata fields that apply to the basic types of S3-compatible data providers.

Fields  
---  
`auth_method` |  `[AuthMethod](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.AuthMethod)` Specifies the authentication and authorization method used by the storage service. When not specified, Transfer Service will attempt to determine right auth method to use.  
`request_model` |  `[RequestModel](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.RequestModel)` Specifies the API request model used to call the storage service. When not specified, the default value of RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used.  
`protocol` |  `[NetworkProtocol](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.NetworkProtocol)` Specifies the network protocol of the agent. When not specified, the default value of NetworkProtocol NETWORK_PROTOCOL_HTTPS is used.  
`list_api` |  `[ListApi](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.S3CompatibleMetadata.ListApi)` The Listing API to use for discovering objects. When not specified, Transfer Service will attempt to determine the right API to use.  
  
## AuthMethod

The authentication and authorization method used by the storage service.

Enums  
---  
`AUTH_METHOD_UNSPECIFIED` | AuthMethod is not specified.  
`AUTH_METHOD_AWS_SIGNATURE_V4` | Auth requests with AWS SigV4.  
`AUTH_METHOD_AWS_SIGNATURE_V2` | Auth requests with AWS SigV2.  
  
## ListApi

The Listing API to use for discovering objects.

Enums  
---  
`LIST_API_UNSPECIFIED` | ListApi is not specified.  
`LIST_OBJECTS_V2` | Perform listing using ListObjectsV2 API.  
`LIST_OBJECTS` | Legacy ListObjects API.  
  
## NetworkProtocol

The agent network protocol to access the storage service.

Enums  
---  
`NETWORK_PROTOCOL_UNSPECIFIED` | NetworkProtocol is not specified.  
`NETWORK_PROTOCOL_HTTPS` | Perform requests using HTTPS.  
`NETWORK_PROTOCOL_HTTP` | Not recommended: This sends data in clear-text. This is only appropriate within a closed network or for publicly available data. Perform requests using HTTP.  
  
## RequestModel

The request model of the API.

Enums  
---  
`REQUEST_MODEL_UNSPECIFIED` | RequestModel is not specified.  
`REQUEST_MODEL_VIRTUAL_HOSTED_STYLE` | Perform requests using Virtual Hosted Style. Example: <https://bucket-name.s3.region.amazonaws.com/key-name>  
`REQUEST_MODEL_PATH_STYLE` | Perform requests using Path Style. Example: <https://s3.region.amazonaws.com/bucket-name/key-name>  
  
## Schedule

Transfers can be scheduled to recur or to run just once.

Fields  
---  
`schedule_start_date` |  `[Date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.type#google.type.Date)` Required. The start date of a transfer. Date boundaries are determined relative to UTC time. If `schedule_start_date` and `[start_time_of_day](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.TimeOfDay.google.storagetransfer.v1.Schedule.start_time_of_day)` are in the past relative to the job's creation time, the transfer starts the day after you schedule the transfer request.**Note:** When starting jobs at or near midnight UTC it is possible that a job starts later than expected. For example, if you send an outbound request on June 1 one millisecond prior to midnight UTC and the Storage Transfer Service server receives the request on June 2, then it creates a TransferJob with `schedule_start_date` set to June 2 and a `start_time_of_day` set to midnight UTC. The first scheduled `[TransferOperation](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation)` takes place on June 3 at midnight UTC.  
`schedule_end_date` |  `[Date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.type#google.type.Date)` The last day a transfer runs. Date boundaries are determined relative to UTC time. A job runs once per 24 hours within the following guidelines:

  * If `schedule_end_date` and `[schedule_start_date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.Date.google.storagetransfer.v1.Schedule.schedule_start_date)` are the same and in the future relative to UTC, the transfer is executed only one time.
  * If `schedule_end_date` is later than `schedule_start_date` and `schedule_end_date` is in the future relative to UTC, the job runs each day at `[start_time_of_day](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.TimeOfDay.google.storagetransfer.v1.Schedule.start_time_of_day)` through `schedule_end_date`.

  
`start_time_of_day` |  `[TimeOfDay](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.type#google.type.TimeOfDay)` The time in UTC that a transfer job is scheduled to run. Transfers may start later than this time.If `start_time_of_day` is not specified:

  * One-time transfers run immediately.
  * Recurring transfers run immediately, and each day at midnight UTC, through `[schedule_end_date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.Date.google.storagetransfer.v1.Schedule.schedule_end_date)`.

If `start_time_of_day` is specified:

  * One-time transfers run at the specified time.
  * Recurring transfers run at the specified time each day, through `schedule_end_date`.

  
`end_time_of_day` |  `[TimeOfDay](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.type#google.type.TimeOfDay)` The time in UTC that no further transfer operations are scheduled. Combined with `[schedule_end_date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.Date.google.storagetransfer.v1.Schedule.schedule_end_date)`, `end_time_of_day` specifies the end date and time for starting new transfer operations. This field must be greater than or equal to the timestamp corresponding to the combination of `[schedule_start_date](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.Date.google.storagetransfer.v1.Schedule.schedule_start_date)` and `[start_time_of_day](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule.FIELDS.google.type.TimeOfDay.google.storagetransfer.v1.Schedule.start_time_of_day)`, and is subject to the following:

  * If `end_time_of_day` is not set and `schedule_end_date` is set, then a default value of `23:59:59` is used for `end_time_of_day`.
  * If `end_time_of_day` is set and `schedule_end_date` is not set, then `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` is returned.

  
`repeat_interval` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Interval between the start of each scheduled TransferOperation. If unspecified, the default value is 24 hours. This value may not be less than 1 hour.  
  
## TransferCounters

A collection of counters that report the progress of a transfer operation.

Fields  
---  
`objects_found_from_source` |  `int64` Objects found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.  
`bytes_found_from_source` |  `int64` Bytes found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.  
`objects_found_only_from_sink` |  `int64` Objects found only in the data sink that are scheduled to be deleted.  
`bytes_found_only_from_sink` |  `int64` Bytes found only in the data sink that are scheduled to be deleted.  
`objects_from_source_skipped_by_sync` |  `int64` Objects in the data source that are not transferred because they already exist in the data sink.  
`bytes_from_source_skipped_by_sync` |  `int64` Bytes in the data source that are not transferred because they already exist in the data sink.  
`objects_copied_to_sink` |  `int64` Objects that are copied to the data sink.  
`bytes_copied_to_sink` |  `int64` Bytes that are copied to the data sink.  
`objects_deleted_from_source` |  `int64` Objects that are deleted from the data source.  
`bytes_deleted_from_source` |  `int64` Bytes that are deleted from the data source.  
`objects_deleted_from_sink` |  `int64` Objects that are deleted from the data sink.  
`bytes_deleted_from_sink` |  `int64` Bytes that are deleted from the data sink.  
`objects_from_source_failed` |  `int64` Objects in the data source that failed to be transferred or that failed to be deleted after being transferred.  
`bytes_from_source_failed` |  `int64` Bytes in the data source that failed to be transferred or that failed to be deleted after being transferred.  
`objects_failed_to_delete_from_sink` |  `int64` Objects that failed to be deleted from the data sink.  
`bytes_failed_to_delete_from_sink` |  `int64` Bytes that failed to be deleted from the data sink.  
`directories_found_from_source` |  `int64` For transfers involving PosixFilesystem only.Number of directories found while listing. For example, if the root directory of the transfer is `base/` and there are two other directories, `a/` and `b/` under this directory, the count after listing `base/`, `base/a/` and `base/b/` is 3.  
`directories_failed_to_list_from_source` |  `int64` For transfers involving PosixFilesystem only.Number of listing failures for each directory found at the source. Potential failures when listing a directory include permission failure or block failure. If listing a directory fails, no files in the directory are transferred.  
`directories_successfully_listed_from_source` |  `int64` For transfers involving PosixFilesystem only.Number of successful listings for each directory found at the source.  
`intermediate_objects_cleaned_up` |  `int64` Number of successfully cleaned up intermediate objects.  
`intermediate_objects_failed_cleaned_up` |  `int64` Number of intermediate objects failed cleaned up.  
`unrestored_deep_archive_objects_skipped_count` |  `int64` Number of unrestored deep archive objects skipped.  
`unsupported_s3_glacier_objects_skipped_count` |  `int64` Number of glacier objects skipped, glacier objects are unsupported by default regardless of the restore status. Allowlist the project to copy glacier objects if needed.  
  
## TransferJob

This resource represents the configuration of a transfer job that runs periodically.

Fields  
---  
`name` |  `string` A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service assigns a unique name. Otherwise, the specified name is used as the unique name for this job.If the specified name is in use by a job, the creation request fails with an `[ALREADY_EXISTS](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.ALREADY_EXISTS)` error.This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. For transfers involving PosixFilesystem, this name must start with `transferJobs/OPI` specifically. For all other transfer types, this name must not start with `transferJobs/OPI`.Non-PosixFilesystem example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"`PosixFilesystem example: `"transferJobs/OPI^[A-Za-z0-9-._~]*[A-Za-z0-9]$"`Applications must not rely on the enforcement of naming requirements involving OPI.Invalid job names fail with an `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` error.  
`description` |  `string` A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded.  
`project_id` |  `string` The ID of the Google Cloud project that owns the job.  
`service_account` |  `string` Optional. The user-managed service account to which to delegate service agent permissions. You can grant Cloud Storage bucket permissions to this service account instead of to the Transfer Service service agent.Either the service account email (`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`) or the unique ID (`123456789012345678901`) are accepted.See <https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions> for required permissions.  
`transfer_spec` |  `[TransferSpec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferSpec)` Transfer specification.  
`replication_spec` |  `[ReplicationSpec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ReplicationSpec)` Replication specification.  
`notification_config` |  `[NotificationConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig)` Notification configuration.  
`logging_config` |  `[LoggingConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig)` Logging configuration.  
`schedule` |  `[Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.Schedule)` Specifies schedule for the transfer job. This is an optional field. When the field is not set, the job never executes a transfer, unless you invoke RunTransferJob or update the job to have a non-empty schedule.  
`event_stream` |  `[EventStream](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.EventStream)` Specifies the event stream for the transfer job for event-driven transfers. When EventStream is specified, the Schedule fields are ignored.  
`status` |  `[Status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status)` Status of the job. This value MUST be specified for `CreateTransferJobRequests`.**Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from `[ENABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.ENABLED)` to `[DISABLED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DISABLED)`, and an operation spawned by the transfer is running, the status change would not affect the current operation.  
`creation_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time that the transfer job was created.  
`last_modification_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time that the transfer job was last modified.  
`deletion_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time that the transfer job was deleted.  
`latest_operation_name` |  `string` The name of the most recently started TransferOperation of this JobConfig. Present if a TransferOperation has been created for this JobConfig.  
  
## Status

The status of the transfer job.

Enums  
---  
`STATUS_UNSPECIFIED` | Zero is an illegal value.  
`ENABLED` | New transfers are performed based on the schedule.  
`DISABLED` | New transfers are not scheduled.  
`DELETED` | This is a soft delete state. After a transfer job is set to this state, the job and all the transfer executions are subject to garbage collection. Transfer jobs become eligible for garbage collection 30 days after their status is set to `DELETED`.  
  
## TransferManifest

Specifies where the manifest is located.

Fields  
---  
`location` |  `string` Specifies the path to the manifest in Cloud Storage. The Google-managed service account for the transfer must have `storage.objects.get` permission for this object. An example path is `gs://bucket_name/path/manifest.csv`.  
  
## TransferOperation

A description of the execution of a transfer.

Fields  
---  
`name` |  `string` A globally unique ID assigned by the system.  
`project_id` |  `string` The ID of the Google Cloud project that owns the operation.  
`transfer_spec` |  `[TransferSpec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferSpec)` Transfer specification.  
`notification_config` |  `[NotificationConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.NotificationConfig)` Notification configuration.  
`logging_config` |  `[LoggingConfig](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.LoggingConfig)` Cloud Logging configuration.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Start time of this transfer execution.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` End time of this transfer execution.  
`status` |  `[Status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOperation.Status)` Status of the transfer operation.  
`counters` |  `[TransferCounters](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferCounters)` Information about the progress of the transfer operation.  
`error_breakdowns[]` |  `[ErrorSummary](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ErrorSummary)` Summarizes errors encountered with sample error log entries.  
`transfer_job_name` |  `string` The name of the transfer job that triggers this transfer operation.  
  
## Status

The status of a TransferOperation.

Enums  
---  
`STATUS_UNSPECIFIED` | Zero is an illegal value.  
`IN_PROGRESS` | In progress.  
`PAUSED` | Paused.  
`SUCCESS` | Completed successfully.  
`FAILED` | Terminated due to an unrecoverable failure.  
`ABORTED` | Aborted by the user.  
`QUEUED` | Temporarily delayed by the system. No user action is required.  
`SUSPENDING` | The operation is suspending and draining the ongoing work to completion.  
  
## TransferOptions

TransferOptions define the actions to be performed on objects in a transfer.

Fields  
---  
`overwrite_objects_already_existing_in_sink` |  `bool` When to overwrite objects that already exist in the sink. The default is that only objects that are different from the source are overwritten. If true, all objects in the sink whose name matches an object in the source are overwritten with the source object.  
`delete_objects_unique_in_sink` |  `bool` Whether objects that exist only in the sink should be deleted from the sink.**Note:** This option and `[delete_objects_from_source_after_transfer](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.FIELDS.bool.google.storagetransfer.v1.TransferOptions.delete_objects_from_source_after_transfer)` are mutually exclusive.  
`delete_objects_from_source_after_transfer` |  `bool` Whether objects should be deleted from the source after they are transferred to the sink.**Note:** This option and `[delete_objects_unique_in_sink](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.FIELDS.bool.google.storagetransfer.v1.TransferOptions.delete_objects_unique_in_sink)` are mutually exclusive.  
`overwrite_when` |  `[OverwriteWhen](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.OverwriteWhen)` When to overwrite objects that already exist in the sink. If not set, overwrite behavior is determined by `[overwrite_objects_already_existing_in_sink](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.FIELDS.bool.google.storagetransfer.v1.TransferOptions.overwrite_objects_already_existing_in_sink)`.  
`metadata_options` |  `[MetadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.MetadataOptions)` Represents the selected metadata options for a transfer job.  
  
## OverwriteWhen

Specifies when to overwrite an object in the sink when an object with matching name is found in the source.

Enums  
---  
`OVERWRITE_WHEN_UNSPECIFIED` | Overwrite behavior is unspecified.  
`DIFFERENT` | Overwrites destination objects with the source objects, only if the objects have the same name but different HTTP ETags or checksum values.  
`NEVER` | Never overwrites a destination object if a source object has the same name. In this case, the source object is not transferred.  
`ALWAYS` | Always overwrite the destination object with the source object, even if the HTTP Etags or checksum values are the same.  
  
## TransferSpec

Configuration for running a transfer.

Fields  
---  
`object_conditions` |  `[ObjectConditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.ObjectConditions)` Only objects that satisfy these object conditions are included in the set of data source and data sink objects. Object conditions based on objects' "last modification time" do not exclude objects in a data sink.  
`transfer_options` |  `[TransferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions)` If the option `[delete_objects_unique_in_sink](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferOptions.FIELDS.bool.google.storagetransfer.v1.TransferOptions.delete_objects_unique_in_sink)` is `true` and time-based object conditions such as 'last modification time' are specified, the request fails with an `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` error.  
`transfer_manifest` |  `[TransferManifest](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferManifest)` A manifest file provides a list of objects to be transferred from the data source. This field points to the location of the manifest file. Otherwise, the entire source bucket is used. ObjectConditions still apply.  
`source_agent_pool_name` |  `string` Specifies the agent pool name associated with the posix data source. When unspecified, the default name is used.  
`sink_agent_pool_name` |  `string` Specifies the agent pool name associated with the posix data sink. When unspecified, the default name is used.  
Union field `data_sink`. The write sink for the data. `data_sink` can be only one of the following:  
`gcs_data_sink` |  `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` Optional. A Cloud Storage data sink.  
`posix_data_sink` |  `[PosixFilesystem](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PosixFilesystem)` Optional. A POSIX Filesystem data sink.  
Union field `data_source`. The read source of the data. `data_source` can be only one of the following:  
`gcs_data_source` |  `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` Optional. A Cloud Storage data source.  
`aws_s3_data_source` |  `[AwsS3Data](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3Data)` Optional. An AWS S3 data source.  
`http_data_source` |  `[HttpData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.HttpData)` Optional. An HTTP URL data source.  
`posix_data_source` |  `[PosixFilesystem](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.PosixFilesystem)` Optional. A POSIX Filesystem data source.  
`azure_blob_storage_data_source` |  `[AzureBlobStorageData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AzureBlobStorageData)` Optional. An Azure Blob Storage data source.  
`aws_s3_compatible_data_source` |  `[AwsS3CompatibleData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AwsS3CompatibleData)` Optional. An AWS S3 compatible data source.  
`hdfs_data_source` |  `[HdfsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.HdfsData)` Optional. An HDFS cluster data source.  
Union field `intermediate_data_location`.`intermediate_data_location` can be only one of the following:  
`gcs_intermediate_data_location` |  `[GcsData](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.GcsData)` For transfers between file systems, specifies a Cloud Storage bucket to be used as an intermediate location through which to transfer data.See [Transfer data between file systems](https://cloud.google.com/storage-transfer/docs/file-to-file) for more information.  
  
## UpdateAgentPoolRequest

Specifies the request passed to UpdateAgentPool.

Fields  
---  
`agent_pool` |  `[AgentPool](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool)` Required. The agent pool to update. `agent_pool` is expected to specify following fields:

  * `[name](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.FIELDS.string.google.storagetransfer.v1.AgentPool.name)`
  * `[display_name](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.FIELDS.string.google.storagetransfer.v1.AgentPool.display_name)`
  * `[bandwidth_limit](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.FIELDS.google.storagetransfer.v1.AgentPool.BandwidthLimit.google.storagetransfer.v1.AgentPool.bandwidth_limit)` An `UpdateAgentPoolRequest` with any other fields is rejected with the error `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)`.

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `agentPool`:

  * `storagetransfer.agentpools.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The [field mask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf) of the fields in `agentPool` to update in this request. The following `agentPool` fields can be updated:

  * `[display_name](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.FIELDS.string.google.storagetransfer.v1.AgentPool.display_name)`
  * `[bandwidth_limit](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.AgentPool.FIELDS.google.storagetransfer.v1.AgentPool.BandwidthLimit.google.storagetransfer.v1.AgentPool.bandwidth_limit)`

  
  
## UpdateTransferJobRequest

Request passed to UpdateTransferJob.

Fields  
---  
`job_name` |  `string` Required. The name of job to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `jobName`:

  * `storagetransfer.jobs.update`

  
`project_id` |  `string` Required. The ID of the Google Cloud project that owns the job.  
`transfer_job` |  `[TransferJob](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob)` Required. The job to update. `transferJob` is expected to specify one or more of five fields: `[description](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.string.google.storagetransfer.v1.TransferJob.description)`, `[transfer_spec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.TransferSpec.google.storagetransfer.v1.TransferJob.transfer_spec)`, `[notification_config](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.NotificationConfig.google.storagetransfer.v1.TransferJob.notification_config)`, `[logging_config](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.LoggingConfig.google.storagetransfer.v1.TransferJob.logging_config)`, and `[status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.TransferJob.Status.google.storagetransfer.v1.TransferJob.status)`. An `UpdateTransferJobRequest` that specifies other fields are rejected with the error `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)`. Updating a job status to `[DELETED](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.Status.ENUM_VALUES.google.storagetransfer.v1.TransferJob.Status.DELETED)` requires `storagetransfer.jobs.delete` permission.  
`update_transfer_job_field_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The field mask of the fields in `transferJob` that are to be updated in this request. Fields in `transferJob` that can be updated are: `[description](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.string.google.storagetransfer.v1.TransferJob.description)`, `[transfer_spec](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.TransferSpec.google.storagetransfer.v1.TransferJob.transfer_spec)`, `[notification_config](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.NotificationConfig.google.storagetransfer.v1.TransferJob.notification_config)`, `[logging_config](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.LoggingConfig.google.storagetransfer.v1.TransferJob.logging_config)`, and `[status](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.storagetransfer.v1#google.storagetransfer.v1.TransferJob.FIELDS.google.storagetransfer.v1.TransferJob.Status.google.storagetransfer.v1.TransferJob.status)`. To update the `transfer_spec` of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error `[INVALID_ARGUMENT](https://docs.cloud.google.com/storage-transfer/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
