---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/remote-agent-utilities/
title: Remote Agent Utilities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:23.533764+00:00
---

# Remote Agent Utilities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/remote-agent-utilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remote Agent Utilities

This document provides guidance on how to integrate Remote Agent Utilities with Google SecOps.

## Configure Remote Agent Utilities integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test Connectivity.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Serialization

#### Description

The action will get the file path (relative path) as the action parameter, will serialize it to a GZIP Base64 string, and will return it in a resultJSON output param.

**Note:** The file limit size: 15 MB. The restriction will be enforced at the TIP level.

#### Parameters

Parameter Display Name | Type | Is Mandatory | Description  
---|---|---|---  
File Path | String | Yes | Full path of the file  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
file_bs64 | N/A | N/A  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _In case of general error:_ "{{Action didn't complete due to error: {error}"}}, result value should be set to false and the action should fail _If action completed successfully:_ "Successfully serialized <file path>" _If action failed to run:_ "Failed to serialized <file path>" | General   
  
### Deserialization

#### Description

The action will get the GZIP Base64 string from the JSON result and will store the data from the original file in a new file in the destination path in the action.

#### Parameters

Parameter Display Name | Type | Is Mandatory | Description  
---|---|---|---  
File Name | String | Yes | File NameThe purpose is to get as a placeholder from prev action (key in json result - u'file_name)  
File base64 | String | Yes | File base64  
  
The purpose is to get as a placeholder from prev action (key in json result - u'base64_file_content)  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
file_new_path | N/A | N/A  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _In case of general error print:_ "{{Action didn't complete due to error: {error}"}}, result value should be set to false and the action should fail _If action failed to run:_ "Failed to deserialized file base64" _If action completed successfully:_ "Successfully deserialized file Base64. New file available here: <file_new_path>" | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
