---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation
title: Cloud Location Finder v1 API - Class CloudLocation (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:54.491866+00:00
---

# Cloud Location Finder v1 API - Class CloudLocation (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class CloudLocation (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class CloudLocation : IMessage<CloudLocation>, IEquatable<CloudLocation>, IDeepCloneable<CloudLocation>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Location Finder v1 API class CloudLocation.

Represents resource cloud locations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudLocation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Constructors 

### CloudLocation()
    
    
    public CloudLocation()

### CloudLocation(CloudLocation)
    
    
    public CloudLocation(CloudLocation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)`  
  
  
## Properties 

### CarbonFreeEnergyPercentage
    
    
    public float CarbonFreeEnergyPercentage { get; set; }

Optional. The carbon free energy percentage of the cloud location. This represents the average percentage of time customers' application will be running on carbon-free energy. See <https://cloud.google.com/sustainability/region-carbon> for more details. There is a difference between default value 0 and unset value. 0 means the carbon free energy percentage is 0%, while unset value means the carbon footprint data is not available.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### CloudLocationName
    
    
    public CloudLocationName CloudLocationName { get; set; }

[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation#Google_Cloud_LocationFinder_V1_CloudLocation_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` |   
  
### CloudLocationType
    
    
    public CloudLocation.Types.CloudLocationType CloudLocationType { get; set; }

Optional. The type of the cloud location.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation.Types)[CloudLocationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation.Types.CloudLocationType)` |   
  
### CloudProvider
    
    
    public CloudLocation.Types.CloudProvider CloudProvider { get; set; }

Optional. The provider of the cloud location. Values can be Google Cloud or third-party providers, including AWS, Azure, or Oracle Cloud Infrastructure.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation.Types)[CloudProvider](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation.Types.CloudProvider)` |   
  
### ContainingCloudLocation
    
    
    public string ContainingCloudLocation { get; set; }

Output only. The containing cloud location in the strict nesting hierarchy. For example, the containing cloud location of a zone is a region.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ContainingCloudLocationAsCloudLocationName
    
    
    public CloudLocationName ContainingCloudLocationAsCloudLocationName { get; set; }

[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)-typed view over the [ContainingCloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation#Google_Cloud_LocationFinder_V1_CloudLocation_ContainingCloudLocation) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. The human-readable name of the cloud location. Example: us-east-2, us-east1.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCarbonFreeEnergyPercentage
    
    
    public bool HasCarbonFreeEnergyPercentage { get; }

Gets whether the "carbon_free_energy_percentage" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the cloud location. Unique name of the cloud location including project and location using the form: `projects/{project_id}/locations/{location}/cloudLocations/{cloud_location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TerritoryCode
    
    
    public string TerritoryCode { get; set; }

Optional. The two-letter ISO 3166-1 alpha-2 code of the cloud location. Examples: US, JP, KR.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
