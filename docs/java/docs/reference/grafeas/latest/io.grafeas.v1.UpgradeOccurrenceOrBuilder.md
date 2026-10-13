---
url: https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrenceOrBuilder
title: Interface UpgradeOccurrenceOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:01.509394+00:00
---

# Interface UpgradeOccurrenceOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrenceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpgradeOccurrenceOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.5  2.3.1  2.2.3  2.1.3 
    
    
    public interface UpgradeOccurrenceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDistribution()
    
    
    public abstract UpgradeDistribution getDistribution()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution)` | The distribution.  
  
### getDistributionOrBuilder()
    
    
    public abstract UpgradeDistributionOrBuilder getDistributionOrBuilder()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistributionOrBuilder)` |   
  
### getPackage()
    
    
    public abstract String getPackage()

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The package.  
  
### getPackageBytes()
    
    
    public abstract ByteString getPackageBytes()

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for package.  
  
### getParsedVersion()
    
    
    public abstract Version getParsedVersion()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version)` | The parsedVersion.  
  
### getParsedVersionOrBuilder()
    
    
    public abstract VersionOrBuilder getParsedVersionOrBuilder()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[VersionOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.VersionOrBuilder)` |   
  
### getWindowsUpdate()
    
    
    public abstract WindowsUpdate getWindowsUpdate()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsUpdate](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate)` | The windowsUpdate.  
  
### getWindowsUpdateOrBuilder()
    
    
    public abstract WindowsUpdateOrBuilder getWindowsUpdateOrBuilder()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsUpdateOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdateOrBuilder)` |   
  
### hasDistribution()
    
    
    public abstract boolean hasDistribution()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the distribution field is set.  
  
### hasParsedVersion()
    
    
    public abstract boolean hasParsedVersion()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parsedVersion field is set.  
  
### hasWindowsUpdate()
    
    
    public abstract boolean hasWindowsUpdate()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowsUpdate field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
