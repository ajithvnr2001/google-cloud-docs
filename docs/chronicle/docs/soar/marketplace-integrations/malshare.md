---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/malshare/
title: MalShare \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:22.276799+00:00
---

# MalShare  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/malshare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MalShare

This document provides guidance on how to integrate MalShare with Google SecOps.

## Configure MalShare to work with Google Security Operations

### API Key

Your API key will be emailed to you upon successful registration to the MalShare portal.

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure MalShare Integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Key | String | N/A | Yes | API Key generated in Malshare console.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your MalShare connection requires an SSL verification (unchecked by default).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Enrich Hash

#### Description

Search for hashes within MalShare.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
SHA1 | Returns if it exists in JSON result  
SOURCES | Returns if it exists in JSON result  
F_TYPE | Returns if it exists in JSON result  
SSDEEP | Returns if it exists in JSON result  
SHA256 | Returns if it exists in JSON result  
MD5 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
            "SHA1": "72bc52b0962ce9043d2104c511a0c5f1c3b5faf3",
            "SOURCES": ["http://dubaifridays.com/437gfinw2?NzGQTrl=AJQIIksfc"],
            "F_TYPE": "HTML",
            "SSDEEP": "768:uTqtXcyd1AlOIkRZAI+rVEGvbnP0+Dod58GO5Fyk31Qc2vGn:uTKXcyd1pujd5Fyc4I",
            "SHA256": "32d1b186a7ae51b2aa0485fbfff44323576f7195286c44619b5bd43b446678b8",
            "MD5": "9e0e9014a11cc149174d0b306f2ac698"
          },
        "Entity": "9e0e9014a11cc149174d0b306f2ac698"
    }]
    

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
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
        N/A
    

### Upload File

#### Description

Upload a file to MalShare.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
File Path | String | N/A | Yes | The path of the file to upload.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
SHA1 | Returns if it exists in JSON result  
SOURCES | Returns if it exists in JSON result  
F_TYPE | Returns if it exists in JSON result  
SSDEEP | Returns if it exists in JSON result  
SHA256 | Returns if it exists in JSON result  
MD5 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
        N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
