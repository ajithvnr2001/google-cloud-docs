---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsResponseOrBuilder
title: Interface FetchUsableBackupVaultsResponseOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:24.354541+00:00
---

# Interface FetchUsableBackupVaultsResponseOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FetchUsableBackupVaultsResponseOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface FetchUsableBackupVaultsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupVaults(int index)
    
    
    public abstract BackupVault getBackupVaults(int index)

The list of BackupVault instances in the project for the specified location.

If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.

`repeated .google.cloud.backupdr.v1.BackupVault backup_vaults = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)` |   
  
### getBackupVaultsCount()
    
    
    public abstract int getBackupVaultsCount()

The list of BackupVault instances in the project for the specified location.

If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.

`repeated .google.cloud.backupdr.v1.BackupVault backup_vaults = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBackupVaultsList()
    
    
    public abstract List<BackupVault> getBackupVaultsList()

The list of BackupVault instances in the project for the specified location.

If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.

`repeated .google.cloud.backupdr.v1.BackupVault backup_vaults = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)>` |   
  
### getBackupVaultsOrBuilder(int index)
    
    
    public abstract BackupVaultOrBuilder getBackupVaultsOrBuilder(int index)

The list of BackupVault instances in the project for the specified location.

If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.

`repeated .google.cloud.backupdr.v1.BackupVault backup_vaults = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupVaultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVaultOrBuilder)` |   
  
### getBackupVaultsOrBuilderList()
    
    
    public abstract List<? extends BackupVaultOrBuilder> getBackupVaultsOrBuilderList()

The list of BackupVault instances in the project for the specified location.

If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.

`repeated .google.cloud.backupdr.v1.BackupVault backup_vaults = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.backupdr.v1.BackupVaultOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getUnreachable(int index)
    
    
    public abstract String getUnreachable(int index)

Locations that could not be reached.

`repeated string unreachable = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unreachable at the given index.  
  
### getUnreachableBytes(int index)
    
    
    public abstract ByteString getUnreachableBytes(int index)

Locations that could not be reached.

`repeated string unreachable = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the unreachable at the given index.  
  
### getUnreachableCount()
    
    
    public abstract int getUnreachableCount()

Locations that could not be reached.

`repeated string unreachable = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of unreachable.  
  
### getUnreachableList()
    
    
    public abstract List<String> getUnreachableList()

Locations that could not be reached.

`repeated string unreachable = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the unreachable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
