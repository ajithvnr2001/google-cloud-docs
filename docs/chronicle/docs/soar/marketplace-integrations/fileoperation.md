---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fileoperation/
title: FileOperation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:27:48.380055+00:00
---

# FileOperation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fileoperation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FileOperation

This document describes how to integrate FileOperation with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/FileOperation.zip).

## Configure FileOperation integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Tarzip Files Linux

#### Description

Create a zip file on a remote Linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
server_ip | String | N/A | Yes | x.x.x.x  
username | String | N/A | Yes | N/A  
password | String | N/A | Yes | N/A  
source_folder | String | N/A | Yes | The remote server folder with the relevant files. Full path.  
file_filter | String | N/A | Yes | files extension to include in zip file {Example: *.txt}.  
output_folder | String | N/A | Yes | The remote server folder to put the zip file into.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
TarPath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Tarzip Files Windows

#### Description

Compress a tarzip file on windows share.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
source_folder | String | N/A | No | The full path to the folder with the relevant files.  
file_filter | String | *.txt | No | Files extension to include in targzip file {Example: *.txt}.  
output_folder | String | N/A | No | The path to the folder to put the zip file into.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
TarPath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Transfer File Linux to Linux

#### Description

Transfer a file from a remote linux host to another remote linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
source_linux_file_path | String | N/A | Yes | The remote server folder with the relevant files. Full path.  
source_linux_ip | String | N/A | Yes | x.x.x.x  
source_linux_username | String | N/A | Yes | N/A  
source_linux_password | String | N/A | Yes | N/A  
dest_linux_path | String | N/A | Yes | The remote server folder to put the files into.  
dest_linux_ip | String | N/A | Yes | x.x.x.x  
dest_linux_username | String | N/A | Yes | N/A  
dest_linux_password | String | N/A | Yes | N/A  
keep_file | Checkbox | Unchecked | No | Indicates weather to keep the file in source or remove it.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
FilePath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Transfer File Linux to Windows

#### Description

Transfer a file from a windows share to remote Linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
source_linux_file_path | String | N/A | Yes | The remote server folder with the relevant files. Full path.  
source_linux_ip | String | N/A | Yes | x.x.x.x  
source_linux_username | String | N/A | Yes | N/A  
source_linux_password | String | N/A | Yes | N/A  
dest_win_path | String | N/A | Yes | The server folder to put the files into.  
keep_file | Checkbox | Checked | No | Indicates weather to keep the file in source or remove it.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
FilePath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Transfer File Windows to Linux

#### Description

Transfer a file from a windows share to a remote Linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
source_win_file_path | String | N/A | The server folder with the relevant files. Full path.  
dest_linux_path | String | N/A | The remote server folder to put the files into.  
dest_linux_ip | String | N/A | x.x.x.x  
dest_linux_username | String | N/A | N/A  
dest_linux_password | String | N/A | N/A  
keep_file | Checkbox | False | Indicates weather to keep the file in source or remove it.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
FilePath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Transfer File Windows to Windows

#### Description

Transfer a file from windows share to a remote Linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
source_win_file_path | String | N/A | Yes | The folder with the relevant files. Full path.  
dest_win_path | String | N/A | Yes | The folder to put the files into.  
keep_file | String | True | Yes | Indicates weather to keep the file in source or remove it.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
FilePath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Zip Files Linux

#### Description

Create a zip file from source folder files in a remote Linux host.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
server_ip | String | N/A | Yes | x.x.x.x  
username | String | N/A | Yes | N/A  
password | String | N/A | Yes | N/A  
source_folder | String | N/A | Yes | The remote server folder with the relevant files.  
file_filter | String | N/A | Yes | Files extension to include in zip file {ex: *.txt}.  
output_folder | String | N/A | Yes | The remote server folder to put the zip file into.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ZIpPath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Zip Files Windows

#### Description

Create a zip file from a source windows and share the files.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
source_folder | String | N/A | Yes | The folder with the relevant files.  
file_filter | String | N/A | Yes | Files extension to include in zip file {ex: *.txt}.  
output_folder | String | N/A | Yes | The folder to put the zip file into.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ZIpPath | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
