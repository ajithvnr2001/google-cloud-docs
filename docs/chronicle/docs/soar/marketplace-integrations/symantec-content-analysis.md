---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-content-analysis/
title: Symantec Content Analysis \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:29:16.737378+00:00
---

# Symantec Content Analysis  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-content-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Content Analysis

This document provides guidance on how to integrate Symantec Content Analysis with Google SecOps.

## Configure Symantec Content Analysis to work with Google Security Operations

Authentication to the REST API is provided using API keys that administrators can create and manage in the Content Analysis CLI interface. To generate an API key:

  1. Connect to the serial console or SSH to the Content Analysis appliance as a user with administrative privileges.
  2. Enter the boldfaced commands below:
         
         > enable
         
         Password: <enter the password>
         
         # ma-actions api-key create administrator
         
         Use of the MA API is not fully supported in CAS. Are you sure you want to proceed? [yes,no] yes
         
         ***MA API in CAS is an experimental feature and not fully tested; some functions may not behave as expected***
         
         Note that keys are not stored on the system in plain text and cannot be retrieved later.
         
         Created new API Key: <This is the API key> (Key ID 2)
         

  3. Copy the generated API key and save it in a text file, as it cannot be viewed later.


**Note:** For additional information regarding Authentication, see [Supporting Multiple Instances](https://origin-symwisedownload.symantec.com/resources/webguides/contentanalysis/21/Content/Topics/DevGuide/generate_api_key.htm).

## Configure Symantec Content Analysis integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Hash Report

#### Description

Get samples for a hash (MD5 and SHA256).

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Verifies that the user has a connection to Symantec Content Analysis via the user's device.

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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Submit File

#### Description

Upload a file to Symantec Content Analysis for a scan. Symantec provides a REST API for submitting individual files to Content Analysis for evaluation using the current configuration. The API is available to people or programs that want to know how Content Analysis would evaluate a file, but don't want to translate it into ICAP, the web-centric protocol that Content Analysis uses.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
File Path | String | N/A | Submit file from path.  
  
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
file_reputation_score | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
