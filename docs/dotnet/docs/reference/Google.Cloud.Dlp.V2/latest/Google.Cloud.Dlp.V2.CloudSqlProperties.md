---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties
title: Google Cloud Data Loss Prevention v2 API - Class CloudSqlProperties (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:07.344636+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class CloudSqlProperties (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class CloudSqlProperties (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class CloudSqlProperties : IMessage<CloudSqlProperties>, IEquatable<CloudSqlProperties>, IDeepCloneable<CloudSqlProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class CloudSqlProperties.

Cloud SQL connection properties.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudSqlProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### CloudSqlProperties()
    
    
    public CloudSqlProperties()

### CloudSqlProperties(CloudSqlProperties)
    
    
    public CloudSqlProperties(CloudSqlProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties)`  
  
  
## Properties 

### CloudSqlIam
    
    
    public CloudSqlIamCredential CloudSqlIam { get; set; }

Built-in IAM authentication (must be configured in Cloud SQL).

**Property Value**  
---  
**Type** | **Description**  
`[CloudSqlIamCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlIamCredential)` |   
  
### ConnectionName
    
    
    public string ConnectionName { get; set; }

Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.

It is an error to use a connection_name from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connection_name `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CredentialCase
    
    
    public CloudSqlProperties.CredentialOneofCase CredentialCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties)[CredentialOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.CredentialOneofCase)` |   
  
### DatabaseEngine
    
    
    public CloudSqlProperties.Types.DatabaseEngine DatabaseEngine { get; set; }

Required. The database engine used by the Cloud SQL instance that this connection configures.

**Property Value**  
---  
**Type** | **Description**  
`[CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.Types)[DatabaseEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.Types.DatabaseEngine)` |   
  
### MaxConnections
    
    
    public int MaxConnections { get; set; }

Required. The DLP API will limit its connections to max_connections. Must be 2 or greater.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### UsernamePassword
    
    
    public SecretManagerCredential UsernamePassword { get; set; }

A username and password stored in Secret Manager.

**Property Value**  
---  
**Type** | **Description**  
`[SecretManagerCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SecretManagerCredential)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
