---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientImpl
title: Google Cloud Tasks v2 API - Class CloudTasksClientImpl (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:55.234483+00:00
---

# Google Cloud Tasks v2 API - Class CloudTasksClientImpl (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientImpl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class CloudTasksClientImpl (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CloudTasksClientImpl : CloudTasksClient

Reference documentation and code samples for the Google Cloud Tasks v2 API class CloudTasksClientImpl.

CloudTasks client wrapper implementation, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient) > CloudTasksClientImpl

## Inherited Members

[CloudTasksClient.DefaultEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DefaultEndpoint)

[CloudTasksClient.DefaultScopes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DefaultScopes)

[CloudTasksClient.ServiceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ServiceMetadata)

[CloudTasksClient.CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateAsync_System_Threading_CancellationToken_)

[CloudTasksClient.Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_Create)

[CloudTasksClient.ShutdownDefaultChannelsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ShutdownDefaultChannelsAsync)

[CloudTasksClient.ListQueues(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueues_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListQueuesAsync(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueuesAsync_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListQueues(LocationName, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueues_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListQueuesAsync(LocationName, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueuesAsync_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetQueueAsync(GetQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_Google_Cloud_Tasks_V2_GetQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.GetQueue(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueue_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetQueueAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetQueueAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.GetQueue(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueue_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetQueueAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetQueueAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.CreateQueueAsync(CreateQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_Google_Cloud_Tasks_V2_CreateQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.CreateQueue(string, Queue, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueue_System_String_Google_Cloud_Tasks_V2_Queue_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateQueueAsync(string, Queue, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_System_String_Google_Cloud_Tasks_V2_Queue_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateQueueAsync(string, Queue, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_System_String_Google_Cloud_Tasks_V2_Queue_System_Threading_CancellationToken_)

[CloudTasksClient.CreateQueue(LocationName, Queue, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueue_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Tasks_V2_Queue_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateQueueAsync(LocationName, Queue, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Tasks_V2_Queue_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateQueueAsync(LocationName, Queue, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Tasks_V2_Queue_System_Threading_CancellationToken_)

[CloudTasksClient.UpdateQueueAsync(UpdateQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueueAsync_Google_Cloud_Tasks_V2_UpdateQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.UpdateQueue(Queue, FieldMask, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueue_Google_Cloud_Tasks_V2_Queue_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.UpdateQueueAsync(Queue, FieldMask, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueueAsync_Google_Cloud_Tasks_V2_Queue_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.UpdateQueueAsync(Queue, FieldMask, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueueAsync_Google_Cloud_Tasks_V2_Queue_Google_Protobuf_WellKnownTypes_FieldMask_System_Threading_CancellationToken_)

[CloudTasksClient.DeleteQueueAsync(DeleteQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_Google_Cloud_Tasks_V2_DeleteQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.DeleteQueue(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueue_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteQueueAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteQueueAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.DeleteQueue(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueue_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteQueueAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteQueueAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.PurgeQueueAsync(PurgeQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_Google_Cloud_Tasks_V2_PurgeQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.PurgeQueue(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueue_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PurgeQueueAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PurgeQueueAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.PurgeQueue(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueue_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PurgeQueueAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PurgeQueueAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.PauseQueueAsync(PauseQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_Google_Cloud_Tasks_V2_PauseQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.PauseQueue(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueue_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PauseQueueAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PauseQueueAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.PauseQueue(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueue_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PauseQueueAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PauseQueueAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.ResumeQueueAsync(ResumeQueueRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_Google_Cloud_Tasks_V2_ResumeQueueRequest_System_Threading_CancellationToken_)

[CloudTasksClient.ResumeQueue(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueue_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ResumeQueueAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ResumeQueueAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.ResumeQueue(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueue_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ResumeQueueAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ResumeQueueAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.GetIamPolicyAsync(GetIamPolicyRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Cloud_Iam_V1_GetIamPolicyRequest_System_Threading_CancellationToken_)

[CloudTasksClient.GetIamPolicy(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicy_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetIamPolicyAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetIamPolicyAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.GetIamPolicy(IResourceName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicy_Google_Api_Gax_IResourceName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetIamPolicyAsync(IResourceName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Api_Gax_IResourceName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetIamPolicyAsync(IResourceName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Api_Gax_IResourceName_System_Threading_CancellationToken_)

[CloudTasksClient.SetIamPolicyAsync(SetIamPolicyRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Cloud_Iam_V1_SetIamPolicyRequest_System_Threading_CancellationToken_)

[CloudTasksClient.SetIamPolicy(string, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicy_System_String_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(string, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_System_String_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(string, Policy, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_System_String_Google_Cloud_Iam_V1_Policy_System_Threading_CancellationToken_)

[CloudTasksClient.SetIamPolicy(IResourceName, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicy_Google_Api_Gax_IResourceName_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(IResourceName, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Api_Gax_IResourceName_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(IResourceName, Policy, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Api_Gax_IResourceName_Google_Cloud_Iam_V1_Policy_System_Threading_CancellationToken_)

[CloudTasksClient.TestIamPermissionsAsync(TestIamPermissionsRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Cloud_Iam_V1_TestIamPermissionsRequest_System_Threading_CancellationToken_)

[CloudTasksClient.TestIamPermissions(string, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissions_System_String_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(string, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_System_String_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(string, IEnumerable<string>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_System_String_System_Collections_Generic_IEnumerable_System_String__System_Threading_CancellationToken_)

[CloudTasksClient.TestIamPermissions(IResourceName, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissions_Google_Api_Gax_IResourceName_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Api_Gax_IResourceName_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Api_Gax_IResourceName_System_Collections_Generic_IEnumerable_System_String__System_Threading_CancellationToken_)

[CloudTasksClient.ListTasks(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasks_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListTasksAsync(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasksAsync_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListTasks(QueueName, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasks_Google_Cloud_Tasks_V2_QueueName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.ListTasksAsync(QueueName, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasksAsync_Google_Cloud_Tasks_V2_QueueName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetTaskAsync(GetTaskRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_Google_Cloud_Tasks_V2_GetTaskRequest_System_Threading_CancellationToken_)

[CloudTasksClient.GetTask(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTask_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetTaskAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetTaskAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.GetTask(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTask_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetTaskAsync(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetTaskAsync(TaskName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_Google_Cloud_Tasks_V2_TaskName_System_Threading_CancellationToken_)

[CloudTasksClient.CreateTaskAsync(CreateTaskRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_Google_Cloud_Tasks_V2_CreateTaskRequest_System_Threading_CancellationToken_)

[CloudTasksClient.CreateTask(string, Task, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTask_System_String_Google_Cloud_Tasks_V2_Task_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateTaskAsync(string, Task, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_System_String_Google_Cloud_Tasks_V2_Task_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateTaskAsync(string, Task, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_System_String_Google_Cloud_Tasks_V2_Task_System_Threading_CancellationToken_)

[CloudTasksClient.CreateTask(QueueName, Task, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTask_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Tasks_V2_Task_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateTaskAsync(QueueName, Task, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Tasks_V2_Task_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.CreateTaskAsync(QueueName, Task, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Tasks_V2_Task_System_Threading_CancellationToken_)

[CloudTasksClient.BatchCreateTasksAsync(BatchCreateTasksRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_Google_Cloud_Tasks_V2_BatchCreateTasksRequest_System_Threading_CancellationToken_)

[CloudTasksClient.PollOnceBatchCreateTasks(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PollOnceBatchCreateTasks_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PollOnceBatchCreateTasksAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PollOnceBatchCreateTasksAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchCreateTasks(string, IEnumerable<CreateTaskRequest>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasks_System_String_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchCreateTasksAsync(string, IEnumerable<CreateTaskRequest>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_System_String_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchCreateTasksAsync(string, IEnumerable<CreateTaskRequest>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_System_String_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__System_Threading_CancellationToken_)

[CloudTasksClient.BatchCreateTasks(QueueName, IEnumerable<CreateTaskRequest>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasks_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchCreateTasksAsync(QueueName, IEnumerable<CreateTaskRequest>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchCreateTasksAsync(QueueName, IEnumerable<CreateTaskRequest>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_CreateTaskRequest__System_Threading_CancellationToken_)

[CloudTasksClient.DeleteTaskAsync(DeleteTaskRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_Google_Cloud_Tasks_V2_DeleteTaskRequest_System_Threading_CancellationToken_)

[CloudTasksClient.DeleteTask(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTask_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteTaskAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteTaskAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.DeleteTask(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTask_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteTaskAsync(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.DeleteTaskAsync(TaskName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_Google_Cloud_Tasks_V2_TaskName_System_Threading_CancellationToken_)

[CloudTasksClient.BatchDeleteTasksAsync(BatchDeleteTasksRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_Google_Cloud_Tasks_V2_BatchDeleteTasksRequest_System_Threading_CancellationToken_)

[CloudTasksClient.PollOnceBatchDeleteTasks(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PollOnceBatchDeleteTasks_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.PollOnceBatchDeleteTasksAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PollOnceBatchDeleteTasksAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchDeleteTasks(string, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasks_System_String_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchDeleteTasksAsync(string, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_System_String_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchDeleteTasksAsync(string, IEnumerable<string>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_System_String_System_Collections_Generic_IEnumerable_System_String__System_Threading_CancellationToken_)

[CloudTasksClient.BatchDeleteTasks(QueueName, IEnumerable<TaskName>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasks_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_TaskName__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchDeleteTasksAsync(QueueName, IEnumerable<TaskName>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_TaskName__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.BatchDeleteTasksAsync(QueueName, IEnumerable<TaskName>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_Google_Cloud_Tasks_V2_TaskName__System_Threading_CancellationToken_)

[CloudTasksClient.RunTaskAsync(RunTaskRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_Google_Cloud_Tasks_V2_RunTaskRequest_System_Threading_CancellationToken_)

[CloudTasksClient.RunTask(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTask_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.RunTaskAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.RunTaskAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.RunTask(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTask_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.RunTaskAsync(TaskName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_Google_Cloud_Tasks_V2_TaskName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.RunTaskAsync(TaskName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_Google_Cloud_Tasks_V2_TaskName_System_Threading_CancellationToken_)

[CloudTasksClient.UpdateCmekConfigAsync(UpdateCmekConfigRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfigAsync_Google_Cloud_Tasks_V2_UpdateCmekConfigRequest_System_Threading_CancellationToken_)

[CloudTasksClient.UpdateCmekConfig(CmekConfig, FieldMask, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfig_Google_Cloud_Tasks_V2_CmekConfig_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.UpdateCmekConfigAsync(CmekConfig, FieldMask, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfigAsync_Google_Cloud_Tasks_V2_CmekConfig_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.UpdateCmekConfigAsync(CmekConfig, FieldMask, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfigAsync_Google_Cloud_Tasks_V2_CmekConfig_Google_Protobuf_WellKnownTypes_FieldMask_System_Threading_CancellationToken_)

[CloudTasksClient.GetCmekConfigAsync(GetCmekConfigRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_Google_Cloud_Tasks_V2_GetCmekConfigRequest_System_Threading_CancellationToken_)

[CloudTasksClient.GetCmekConfig(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfig_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetCmekConfigAsync(string, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetCmekConfigAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_System_String_System_Threading_CancellationToken_)

[CloudTasksClient.GetCmekConfig(CmekConfigName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfig_Google_Cloud_Tasks_V2_CmekConfigName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetCmekConfigAsync(CmekConfigName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_Google_Cloud_Tasks_V2_CmekConfigName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetCmekConfigAsync(CmekConfigName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_Google_Cloud_Tasks_V2_CmekConfigName_System_Threading_CancellationToken_)

[CloudTasksClient.GetIamPolicyAsync(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.GetIamPolicyAsync(QueueName, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Cloud_Tasks_V2_QueueName_System_Threading_CancellationToken_)

[CloudTasksClient.GetIamPolicy(QueueName, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicy_Google_Cloud_Tasks_V2_QueueName_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(QueueName, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.TestIamPermissionsAsync(QueueName, IEnumerable<string>, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_System_String__System_Threading_CancellationToken_)

[CloudTasksClient.TestIamPermissions(QueueName, IEnumerable<string>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissions_Google_Cloud_Tasks_V2_QueueName_System_Collections_Generic_IEnumerable_System_String__Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(QueueName, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[CloudTasksClient.SetIamPolicyAsync(QueueName, Policy, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Iam_V1_Policy_System_Threading_CancellationToken_)

[CloudTasksClient.SetIamPolicy(QueueName, Policy, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicy_Google_Cloud_Tasks_V2_QueueName_Google_Cloud_Iam_V1_Policy_Google_Api_Gax_Grpc_CallSettings_)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Remarks

Cloud Tasks allows developers to manage the execution of background work in their applications.

## Constructors 

### CloudTasksClientImpl(CloudTasksClient, CloudTasksSettings, ILogger)
    
    
    public CloudTasksClientImpl(CloudTasks.CloudTasksClient grpcClient, CloudTasksSettings settings, ILogger logger)

Constructs a client wrapper for the CloudTasks service, with the specified gRPC client and settings.

**Parameters**  
---  
**Name** | **Description**  
`grpcClient` | `[CloudTasks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks)[CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks.CloudTasksClient)`  
The underlying gRPC client.  
`settings` | `[CloudTasksSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksSettings)`  
The base [CloudTasksSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksSettings) used within this client.  
`logger` | `[ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)`  
Optional [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger) to use within this client.  
  
## Properties 

### BatchCreateTasksOperationsClient
    
    
    public override OperationsClient BatchCreateTasksOperationsClient { get; }

The long-running operations client for `BatchCreateTasks`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
**Overrides**

[CloudTasksClient.BatchCreateTasksOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksOperationsClient)

### BatchDeleteTasksOperationsClient
    
    
    public override OperationsClient BatchDeleteTasksOperationsClient { get; }

The long-running operations client for `BatchDeleteTasks`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
**Overrides**

[CloudTasksClient.BatchDeleteTasksOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksOperationsClient)

### GrpcClient
    
    
    public override CloudTasks.CloudTasksClient GrpcClient { get; }

The underlying gRPC CloudTasks client

**Property Value**  
---  
**Type** | **Description**  
`[CloudTasks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks)[CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks.CloudTasksClient)` |   
**Overrides**

[CloudTasksClient.GrpcClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GrpcClient)

### LocationsClient
    
    
    public override LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
**Overrides**

[CloudTasksClient.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_LocationsClient)

## Methods 

### BatchCreateTasks(BatchCreateTasksRequest, CallSettings)
    
    
    public override Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata> BatchCreateTasks(BatchCreateTasksRequest request, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | The RPC response.  
**Overrides**

[CloudTasksClient.BatchCreateTasks(BatchCreateTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasks_Google_Cloud_Tasks_V2_BatchCreateTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### BatchCreateTasksAsync(BatchCreateTasksRequest, CallSettings)
    
    
    public override Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(BatchCreateTasksRequest request, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.BatchCreateTasksAsync(BatchCreateTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchCreateTasksAsync_Google_Cloud_Tasks_V2_BatchCreateTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### BatchDeleteTasks(BatchDeleteTasksRequest, CallSettings)
    
    
    public override Operation<Empty, BatchDeleteTasksMetadata> BatchDeleteTasks(BatchDeleteTasksRequest request, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | The RPC response.  
**Overrides**

[CloudTasksClient.BatchDeleteTasks(BatchDeleteTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasks_Google_Cloud_Tasks_V2_BatchDeleteTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### BatchDeleteTasksAsync(BatchDeleteTasksRequest, CallSettings)
    
    
    public override Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(BatchDeleteTasksRequest request, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.BatchDeleteTasksAsync(BatchDeleteTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_BatchDeleteTasksAsync_Google_Cloud_Tasks_V2_BatchDeleteTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### CreateQueue(CreateQueueRequest, CallSettings)
    
    
    public override Queue CreateQueue(CreateQueueRequest request, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.CreateQueue(CreateQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueue_Google_Cloud_Tasks_V2_CreateQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### CreateQueueAsync(CreateQueueRequest, CallSettings)
    
    
    public override Task<Queue> CreateQueueAsync(CreateQueueRequest request, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.CreateQueueAsync(CreateQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateQueueAsync_Google_Cloud_Tasks_V2_CreateQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### CreateTask(CreateTaskRequest, CallSettings)
    
    
    public override Task CreateTask(CreateTaskRequest request, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Overrides**

[CloudTasksClient.CreateTask(CreateTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTask_Google_Cloud_Tasks_V2_CreateTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### CreateTaskAsync(CreateTaskRequest, CallSettings)
    
    
    public override Task<Task> CreateTaskAsync(CreateTaskRequest request, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.CreateTaskAsync(CreateTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTaskAsync_Google_Cloud_Tasks_V2_CreateTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### DeleteQueue(DeleteQueueRequest, CallSettings)
    
    
    public override void DeleteQueue(DeleteQueueRequest request, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Overrides**

[CloudTasksClient.DeleteQueue(DeleteQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueue_Google_Cloud_Tasks_V2_DeleteQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### DeleteQueueAsync(DeleteQueueRequest, CallSettings)
    
    
    public override Task DeleteQueueAsync(DeleteQueueRequest request, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.DeleteQueueAsync(DeleteQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteQueueAsync_Google_Cloud_Tasks_V2_DeleteQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### DeleteTask(DeleteTaskRequest, CallSettings)
    
    
    public override void DeleteTask(DeleteTaskRequest request, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Overrides**

[CloudTasksClient.DeleteTask(DeleteTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTask_Google_Cloud_Tasks_V2_DeleteTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### DeleteTaskAsync(DeleteTaskRequest, CallSettings)
    
    
    public override Task DeleteTaskAsync(DeleteTaskRequest request, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.DeleteTaskAsync(DeleteTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_DeleteTaskAsync_Google_Cloud_Tasks_V2_DeleteTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetCmekConfig(GetCmekConfigRequest, CallSettings)
    
    
    public override CmekConfig GetCmekConfig(GetCmekConfigRequest request, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Overrides**

[CloudTasksClient.GetCmekConfig(GetCmekConfigRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfig_Google_Cloud_Tasks_V2_GetCmekConfigRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetCmekConfigAsync(GetCmekConfigRequest, CallSettings)
    
    
    public override Task<CmekConfig> GetCmekConfigAsync(GetCmekConfigRequest request, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.GetCmekConfigAsync(GetCmekConfigRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetCmekConfigAsync_Google_Cloud_Tasks_V2_GetCmekConfigRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetIamPolicy(GetIamPolicyRequest, CallSettings)
    
    
    public override Policy GetIamPolicy(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Overrides**

[CloudTasksClient.GetIamPolicy(GetIamPolicyRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicy_Google_Cloud_Iam_V1_GetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)
    
    
    public override Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetIamPolicyAsync_Google_Cloud_Iam_V1_GetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetQueue(GetQueueRequest, CallSettings)
    
    
    public override Queue GetQueue(GetQueueRequest request, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.GetQueue(GetQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueue_Google_Cloud_Tasks_V2_GetQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetQueueAsync(GetQueueRequest, CallSettings)
    
    
    public override Task<Queue> GetQueueAsync(GetQueueRequest request, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.GetQueueAsync(GetQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetQueueAsync_Google_Cloud_Tasks_V2_GetQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetTask(GetTaskRequest, CallSettings)
    
    
    public override Task GetTask(GetTaskRequest request, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Overrides**

[CloudTasksClient.GetTask(GetTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTask_Google_Cloud_Tasks_V2_GetTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetTaskAsync(GetTaskRequest, CallSettings)
    
    
    public override Task<Task> GetTaskAsync(GetTaskRequest request, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.GetTaskAsync(GetTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_GetTaskAsync_Google_Cloud_Tasks_V2_GetTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### ListQueues(ListQueuesRequest, CallSettings)
    
    
    public override PagedEnumerable<ListQueuesResponse, Queue> ListQueues(ListQueuesRequest request, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQueuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Overrides**

[CloudTasksClient.ListQueues(ListQueuesRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueues_Google_Cloud_Tasks_V2_ListQueuesRequest_Google_Api_Gax_Grpc_CallSettings_)

### ListQueuesAsync(ListQueuesRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<ListQueuesResponse, Queue> ListQueuesAsync(ListQueuesRequest request, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQueuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable asynchronous sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Overrides**

[CloudTasksClient.ListQueuesAsync(ListQueuesRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListQueuesAsync_Google_Cloud_Tasks_V2_ListQueuesRequest_Google_Api_Gax_Grpc_CallSettings_)

### ListTasks(ListTasksRequest, CallSettings)
    
    
    public override PagedEnumerable<ListTasksResponse, Task> ListTasks(ListTasksRequest request, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Overrides**

[CloudTasksClient.ListTasks(ListTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasks_Google_Cloud_Tasks_V2_ListTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### ListTasksAsync(ListTasksRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<ListTasksResponse, Task> ListTasksAsync(ListTasksRequest request, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable asynchronous sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Overrides**

[CloudTasksClient.ListTasksAsync(ListTasksRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ListTasksAsync_Google_Cloud_Tasks_V2_ListTasksRequest_Google_Api_Gax_Grpc_CallSettings_)

### PauseQueue(PauseQueueRequest, CallSettings)
    
    
    public override Queue PauseQueue(PauseQueueRequest request, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.PauseQueue(PauseQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueue_Google_Cloud_Tasks_V2_PauseQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### PauseQueueAsync(PauseQueueRequest, CallSettings)
    
    
    public override Task<Queue> PauseQueueAsync(PauseQueueRequest request, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.PauseQueueAsync(PauseQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PauseQueueAsync_Google_Cloud_Tasks_V2_PauseQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### PurgeQueue(PurgeQueueRequest, CallSettings)
    
    
    public override Queue PurgeQueue(PurgeQueueRequest request, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.PurgeQueue(PurgeQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueue_Google_Cloud_Tasks_V2_PurgeQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### PurgeQueueAsync(PurgeQueueRequest, CallSettings)
    
    
    public override Task<Queue> PurgeQueueAsync(PurgeQueueRequest request, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.PurgeQueueAsync(PurgeQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_PurgeQueueAsync_Google_Cloud_Tasks_V2_PurgeQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### ResumeQueue(ResumeQueueRequest, CallSettings)
    
    
    public override Queue ResumeQueue(ResumeQueueRequest request, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.ResumeQueue(ResumeQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueue_Google_Cloud_Tasks_V2_ResumeQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### ResumeQueueAsync(ResumeQueueRequest, CallSettings)
    
    
    public override Task<Queue> ResumeQueueAsync(ResumeQueueRequest request, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.ResumeQueueAsync(ResumeQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_ResumeQueueAsync_Google_Cloud_Tasks_V2_ResumeQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### RunTask(RunTaskRequest, CallSettings)
    
    
    public override Task RunTask(RunTaskRequest request, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Overrides**

[CloudTasksClient.RunTask(RunTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTask_Google_Cloud_Tasks_V2_RunTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### RunTaskAsync(RunTaskRequest, CallSettings)
    
    
    public override Task<Task> RunTaskAsync(RunTaskRequest request, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.RunTaskAsync(RunTaskRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_RunTaskAsync_Google_Cloud_Tasks_V2_RunTaskRequest_Google_Api_Gax_Grpc_CallSettings_)

### SetIamPolicy(SetIamPolicyRequest, CallSettings)
    
    
    public override Policy SetIamPolicy(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Overrides**

[CloudTasksClient.SetIamPolicy(SetIamPolicyRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicy_Google_Cloud_Iam_V1_SetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)

### SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)
    
    
    public override Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_SetIamPolicyAsync_Google_Cloud_Iam_V1_SetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)

### TestIamPermissions(TestIamPermissionsRequest, CallSettings)
    
    
    public override TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Overrides**

[CloudTasksClient.TestIamPermissions(TestIamPermissionsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissions_Google_Cloud_Iam_V1_TestIamPermissionsRequest_Google_Api_Gax_Grpc_CallSettings_)

### TestIamPermissionsAsync(TestIamPermissionsRequest, CallSettings)
    
    
    public override Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.TestIamPermissionsAsync(TestIamPermissionsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_TestIamPermissionsAsync_Google_Cloud_Iam_V1_TestIamPermissionsRequest_Google_Api_Gax_Grpc_CallSettings_)

### UpdateCmekConfig(UpdateCmekConfigRequest, CallSettings)
    
    
    public override CmekConfig UpdateCmekConfig(UpdateCmekConfigRequest request, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Overrides**

[CloudTasksClient.UpdateCmekConfig(UpdateCmekConfigRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfig_Google_Cloud_Tasks_V2_UpdateCmekConfigRequest_Google_Api_Gax_Grpc_CallSettings_)

### UpdateCmekConfigAsync(UpdateCmekConfigRequest, CallSettings)
    
    
    public override Task<CmekConfig> UpdateCmekConfigAsync(UpdateCmekConfigRequest request, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.UpdateCmekConfigAsync(UpdateCmekConfigRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateCmekConfigAsync_Google_Cloud_Tasks_V2_UpdateCmekConfigRequest_Google_Api_Gax_Grpc_CallSettings_)

### UpdateQueue(UpdateQueueRequest, CallSettings)
    
    
    public override Queue UpdateQueue(UpdateQueueRequest request, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Overrides**

[CloudTasksClient.UpdateQueue(UpdateQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueue_Google_Cloud_Tasks_V2_UpdateQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

### UpdateQueueAsync(UpdateQueueRequest, CallSettings)
    
    
    public override Task<Queue> UpdateQueueAsync(UpdateQueueRequest request, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Overrides**

[CloudTasksClient.UpdateQueueAsync(UpdateQueueRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_UpdateQueueAsync_Google_Cloud_Tasks_V2_UpdateQueueRequest_Google_Api_Gax_Grpc_CallSettings_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
