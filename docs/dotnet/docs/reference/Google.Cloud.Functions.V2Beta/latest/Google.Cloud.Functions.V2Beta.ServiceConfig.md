---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig
title: Cloud Functions v2beta API - Class ServiceConfig (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:27.740532+00:00
---

# Cloud Functions v2beta API - Class ServiceConfig (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class ServiceConfig (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.ServiceConfig)


    
    
    public sealed class ServiceConfig : IMessage<ServiceConfig>, IEquatable<ServiceConfig>, IDeepCloneable<ServiceConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2beta API class ServiceConfig.

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### ServiceConfig()
    
    
    public ServiceConfig()

### ServiceConfig(ServiceConfig)
    
    
    public ServiceConfig(ServiceConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig)`  
  
  
## Properties 

### AllTrafficOnLatestRevision
    
    
    public bool AllTrafficOnLatestRevision { get; set; }

Whether 100% of traffic is routed to the latest revision. On CreateFunction and UpdateFunction, when set to true, the revision being deployed will serve 100% of traffic, ignoring any traffic split settings, if any. On GetFunction, true will be returned if the latest revision is serving 100% of traffic.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AvailableCpu
    
    
    public string AvailableCpu { get; set; }

The number of CPUs used in a single container instance. Default value is calculated from available memory. Supports the same values as Cloud Run, see <https://cloud.google.com/run/docs/reference/rest/v1/Container#resourcerequirements> Example: "1" indicates 1 vCPU

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AvailableMemory
    
    
    public string AvailableMemory { get; set; }

The amount of memory available for a function. Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is supplied the value is interpreted as bytes. See <https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go> a full description.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BinaryAuthorizationPolicy
    
    
    public string BinaryAuthorizationPolicy { get; set; }

Optional. The binary authorization policy to be checked when deploying the Cloud Run service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnvironmentVariables
    
    
    public MapField<string, string> EnvironmentVariables { get; }

Environment variables that shall be available during function execution.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IngressSettings
    
    
    public ServiceConfig.Types.IngressSettings IngressSettings { get; set; }

The ingress settings for the function, controlling what traffic can reach it.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types)[IngressSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types.IngressSettings)` |   
  
### MaxInstanceCount
    
    
    public int MaxInstanceCount { get; set; }

The limit on the maximum number of function instances that may coexist at a given time.

In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate.

See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxInstanceRequestConcurrency
    
    
    public int MaxInstanceRequestConcurrency { get; set; }

Sets the maximum number of concurrent requests that each instance can receive. Defaults to 1.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MinInstanceCount
    
    
    public int MinInstanceCount { get; set; }

The limit on the minimum number of function instances that may coexist at a given time.

Function instances are kept in idle state for a short period after they finished executing the request to reduce cold start time for subsequent requests. Setting a minimum instance count will ensure that the given number of instances are kept running in idle state always. This can help with cold start times when jump in incoming request count occurs after the idle instance would have been stopped in the default case.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Revision
    
    
    public string Revision { get; set; }

Output only. The name of service revision.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecretEnvironmentVariables
    
    
    public RepeatedField<SecretEnvVar> SecretEnvironmentVariables { get; }

Secret environment variables configuration.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SecretEnvVar](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.SecretEnvVar)` |   
  
### SecretVolumes
    
    
    public RepeatedField<SecretVolume> SecretVolumes { get; }

Secret volumes configuration.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SecretVolume](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.SecretVolume)` |   
  
### SecurityLevel
    
    
    public ServiceConfig.Types.SecurityLevel SecurityLevel { get; set; }

Security level configure whether the function only accepts https. This configuration is only applicable to 1st Gen functions with Http trigger. By default https is optional for 1st Gen functions; 2nd Gen functions are https ONLY.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types)[SecurityLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types.SecurityLevel)` |   
  
### Service
    
    
    public string Service { get; set; }

Output only. Name of the service associated with a Function. The format of this field is `projects/{project}/locations/{region}/services/{service}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountEmail
    
    
    public string ServiceAccountEmail { get; set; }

The email of the service's service account. If empty, defaults to `{project_number}-compute@developer.gserviceaccount.com`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAsServiceName
    
    
    public ServiceName ServiceAsServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceName)-typed view over the [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig#Google_Cloud_Functions_V2Beta_ServiceConfig_Service) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceName)` |   
  
### TimeoutSeconds
    
    
    public int TimeoutSeconds { get; set; }

The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Uri
    
    
    public string Uri { get; set; }

Output only. URI of the Service deployed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VpcConnector
    
    
    public string VpcConnector { get; set; }

The Serverless VPC Access connector that this cloud function can connect to. The format of this field is `projects/*/locations/*/connectors/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VpcConnectorAsConnectorName
    
    
    public ConnectorName VpcConnectorAsConnectorName { get; set; }

[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ConnectorName)-typed view over the [VpcConnector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig#Google_Cloud_Functions_V2Beta_ServiceConfig_VpcConnector) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ConnectorName)` |   
  
### VpcConnectorEgressSettings
    
    
    public ServiceConfig.Types.VpcConnectorEgressSettings VpcConnectorEgressSettings { get; set; }

The egress settings for the connector, controlling what traffic is diverted through it.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types)[VpcConnectorEgressSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ServiceConfig.Types.VpcConnectorEgressSettings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
