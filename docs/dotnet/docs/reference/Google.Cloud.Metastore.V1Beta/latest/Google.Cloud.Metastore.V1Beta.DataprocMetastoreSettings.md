---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings
title: Dataproc Metastore v1beta API - Class DataprocMetastoreSettings (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:35.841991+00:00
---

# Dataproc Metastore v1beta API - Class DataprocMetastoreSettings (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class DataprocMetastoreSettings (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings)


    
    
    public sealed class DataprocMetastoreSettings : ServiceSettingsBase

Reference documentation and code samples for the Dataproc Metastore v1beta API class DataprocMetastoreSettings.

Settings for [DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > DataprocMetastoreSettings

## Inherited Members

[ServiceSettingsBase.VersionHeaderBuilder](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_VersionHeaderBuilder)

[ServiceSettingsBase.CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_CallSettings)

[ServiceSettingsBase.Clock](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Clock)

[ServiceSettingsBase.Scheduler](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Scheduler)

[ServiceSettingsBase.Interceptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Interceptor)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Constructors 

### DataprocMetastoreSettings()
    
    
    public DataprocMetastoreSettings()

Constructs a new [DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings) object with default settings.

## Properties 

### AlterMetadataResourceLocationOperationsSettings
    
    
    public OperationsSettings AlterMetadataResourceLocationOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.AlterMetadataResourceLocation` and `DataprocMetastoreClient.AlterMetadataResourceLocationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### AlterMetadataResourceLocationSettings
    
    
    public CallSettings AlterMetadataResourceLocationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.AlterMetadataResourceLocation` and `DataprocMetastoreClient.AlterMetadataResourceLocationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### CreateBackupOperationsSettings
    
    
    public OperationsSettings CreateBackupOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.CreateBackup` and `DataprocMetastoreClient.CreateBackupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### CreateBackupSettings
    
    
    public CallSettings CreateBackupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.CreateBackup` and `DataprocMetastoreClient.CreateBackupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateMetadataImportOperationsSettings
    
    
    public OperationsSettings CreateMetadataImportOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.CreateMetadataImport` and `DataprocMetastoreClient.CreateMetadataImportAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### CreateMetadataImportSettings
    
    
    public CallSettings CreateMetadataImportSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.CreateMetadataImport` and `DataprocMetastoreClient.CreateMetadataImportAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateServiceOperationsSettings
    
    
    public OperationsSettings CreateServiceOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.CreateService` and `DataprocMetastoreClient.CreateServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### CreateServiceSettings
    
    
    public CallSettings CreateServiceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.CreateService` and `DataprocMetastoreClient.CreateServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteBackupOperationsSettings
    
    
    public OperationsSettings DeleteBackupOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.DeleteBackup` and `DataprocMetastoreClient.DeleteBackupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### DeleteBackupSettings
    
    
    public CallSettings DeleteBackupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.DeleteBackup` and `DataprocMetastoreClient.DeleteBackupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteServiceOperationsSettings
    
    
    public OperationsSettings DeleteServiceOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.DeleteService` and `DataprocMetastoreClient.DeleteServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### DeleteServiceSettings
    
    
    public CallSettings DeleteServiceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.DeleteService` and `DataprocMetastoreClient.DeleteServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### ExportMetadataOperationsSettings
    
    
    public OperationsSettings ExportMetadataOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.ExportMetadata` and `DataprocMetastoreClient.ExportMetadataAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### ExportMetadataSettings
    
    
    public CallSettings ExportMetadataSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.ExportMetadata` and `DataprocMetastoreClient.ExportMetadataAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetBackupSettings
    
    
    public CallSettings GetBackupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.GetBackup` and `DataprocMetastoreClient.GetBackupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetMetadataImportSettings
    
    
    public CallSettings GetMetadataImportSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.GetMetadataImport` and `DataprocMetastoreClient.GetMetadataImportAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetServiceSettings
    
    
    public CallSettings GetServiceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.GetService` and `DataprocMetastoreClient.GetServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### IAMPolicySettings
    
    
    public IAMPolicySettings IAMPolicySettings { get; set; }

The settings to use for the [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicySettings.html)` |   
  
### ListBackupsSettings
    
    
    public CallSettings ListBackupsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.ListBackups` and `DataprocMetastoreClient.ListBackupsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListMetadataImportsSettings
    
    
    public CallSettings ListMetadataImportsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.ListMetadataImports` and `DataprocMetastoreClient.ListMetadataImportsAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListServicesSettings
    
    
    public CallSettings ListServicesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.ListServices` and `DataprocMetastoreClient.ListServicesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### MoveTableToDatabaseOperationsSettings
    
    
    public OperationsSettings MoveTableToDatabaseOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.MoveTableToDatabase` and `DataprocMetastoreClient.MoveTableToDatabaseAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### MoveTableToDatabaseSettings
    
    
    public CallSettings MoveTableToDatabaseSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.MoveTableToDatabase` and `DataprocMetastoreClient.MoveTableToDatabaseAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### QueryMetadataOperationsSettings
    
    
    public OperationsSettings QueryMetadataOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.QueryMetadata` and `DataprocMetastoreClient.QueryMetadataAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### QueryMetadataSettings
    
    
    public CallSettings QueryMetadataSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.QueryMetadata` and `DataprocMetastoreClient.QueryMetadataAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### RemoveIamPolicySettings
    
    
    public CallSettings RemoveIamPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.RemoveIamPolicy` and `DataprocMetastoreClient.RemoveIamPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### RestoreServiceOperationsSettings
    
    
    public OperationsSettings RestoreServiceOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.RestoreService` and `DataprocMetastoreClient.RestoreServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### RestoreServiceSettings
    
    
    public CallSettings RestoreServiceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.RestoreService` and `DataprocMetastoreClient.RestoreServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateMetadataImportOperationsSettings
    
    
    public OperationsSettings UpdateMetadataImportOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.UpdateMetadataImport` and `DataprocMetastoreClient.UpdateMetadataImportAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### UpdateMetadataImportSettings
    
    
    public CallSettings UpdateMetadataImportSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.UpdateMetadataImport` and `DataprocMetastoreClient.UpdateMetadataImportAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateServiceOperationsSettings
    
    
    public OperationsSettings UpdateServiceOperationsSettings { get; set; }

Long Running Operation settings for calls to `DataprocMetastoreClient.UpdateService` and `DataprocMetastoreClient.UpdateServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### UpdateServiceSettings
    
    
    public CallSettings UpdateServiceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataprocMetastoreClient.UpdateService` and `DataprocMetastoreClient.UpdateServiceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public DataprocMetastoreSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings)` | A deep clone of this [DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings) object.  
  
### GetDefault()
    
    
    public static DataprocMetastoreSettings GetDefault()

Get a new instance of the default [DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings).

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings)` | A new instance of the default [DataprocMetastoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
