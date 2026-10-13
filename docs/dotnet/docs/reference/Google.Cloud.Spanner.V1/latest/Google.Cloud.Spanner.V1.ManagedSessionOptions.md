---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions
title: Google Cloud Spanner v1 API - Class ManagedSessionOptions (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:18.168844+00:00
---

# Google Cloud Spanner v1 API - Class ManagedSessionOptions (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class ManagedSessionOptions (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class ManagedSessionOptions

Reference documentation and code samples for the Google Cloud Spanner v1 API class ManagedSessionOptions.

Options to used when creating a managed session.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedSessionOptions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Properties 

### Client
    
    
    public SpannerClient Client { get; }

The Spanner client to use for all operations associated to the session, including session creation. Won't be null.

**Property Value**  
---  
**Type** | **Description**  
`[SpannerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerClient)` |   
  
### DatabaseName
    
    
    public DatabaseName DatabaseName { get; }

The database for which the session will be created. Won't be null.

**Property Value**  
---  
**Type** | **Description**  
`Google.Cloud.Spanner.Common.V1.DatabaseName` |   
  
### DatabaseRole
    
    
    public string DatabaseRole { get; }

The database role with which the session will be created. May be null, in which case the default (public) database role is used if fine grained access control is enabled; otherwise the database role is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Timeout
    
    
    public TimeSpan? Timeout { get; }

The total time allowed for a network call to the Cloud Spanner server, including retries. This setting is applied to calls to create sessions, as well as explicitly beginning transactions. May be null, in which case 1 minute will be used. Otherwise, the value will be positive.

**Property Value**  
---  
**Type** | **Description**  
`[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)` |   
  
## Methods 

### Create(DatabaseName, SpannerClient)
    
    
    public static ManagedSessionOptions Create(DatabaseName databaseName, SpannerClient client)

Creates a [ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions) with the given database name.

**Parameters**  
---  
**Name** | **Description**  
`databaseName` | `Google.Cloud.Spanner.Common.V1.DatabaseName`  
The database name for the associated session. Must not be null.  
`client` | `[SpannerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerClient)`  
The Spanner client that the sessions will use for all command execution, including those executed by associated [ManagedTransaction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedTransaction).  
**Returns**  
---  
**Type** | **Description**  
`[ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions)` |   
  
### WithDatabaseRole(string)
    
    
    public ManagedSessionOptions WithDatabaseRole(string databaseRole)

Creates a [ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions) based on this one but with the given database role.

**Parameter**  
---  
**Name** | **Description**  
`databaseRole` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The database role for the associated session. May be null in which case the default (public) database role is used if fine grained access control is enabled; otherwise the database role is ignored.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions)` |   
  
### WithTimeout(TimeSpan?)
    
    
    public ManagedSessionOptions WithTimeout(TimeSpan? timeout)

Creates a [ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions) based on this one but with the given timeout.

**Parameter**  
---  
**Name** | **Description**  
`timeout` | `[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)`  
The total time allowed for a network call to the Cloud Spanner server, including retries. This setting is applied to calls to create sessions, as well as explicitly beginning transactions. May be null, in which case 1 minute will be used. Otherwise, the value must be positive.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedSessionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ManagedSessionOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
