---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-email-security-cloud/
title: Symantec Email Security.cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:31.799960+00:00
---

# Symantec Email Security.cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-email-security-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Email Security.cloud

This document provides guidance on how to integrate Symantec Email Security.cloud with Google SecOps.

## Configure Symantec Email Security.cloud integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IOC API Root | String | https://iocapi.emailsecurity.symantec.com | Yes | IOC API root of the Symantec Email Security.Cloud instance.  
Username | String | N/A | Yes | Username of the Symantec Email Security.Cloud instance.  
Password | Secret | N/A | Yes | Password of the Symantec Email Security.Cloud instance.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Symantec Email Security.Cloud server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

Block entities.

## Actions

### Ping

#### Description

Test connectivity to the Symantec Email Security.Cloud integration with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Symantec Email Security.Cloud server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Symantec Email Security.Cloud server! Error is {0}".format(exception.stacktrace)" | General  
  
### Block Entities

#### Description

Block entities in Symantec Email Security.Cloud. Supported entities: Hostname, IP Address, URL, Filehash, Email Subject, Email Address (user entity that matches email regex).

**Note:** Only the MD5 and SHA256 hashes are supported. All of the entities are treated as "sender IOCs" during blocking.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Remediation Action | DDL | Block and Delete Possible values:

  * Block and Delete
  * Quarantine
  * Redirect
  * Tag Subject
  * Append Header

| No | Specify the remediation action for the entities.  
Description | String | Blocked by PRODUCT_NAME | Yes | Specify a description that should be added to the blocked entities.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * URL
  * Filehash
  * Email Subject
  * Email Address (user entity that matches email regex)



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
            "status": "Failure",
            "reason": "Invalid MD5 value"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully blocked the following entities in Symantec Email Security.Cloud: {entity.identifier}."_If data is not available for one entity (is_success=true):_ "Action wasn't able to block the following entities in Symantec Email Security.Cloud: {entity.identifier}."If data is not available for all entities (is_success=false): "None of the provided entities were blocked."**The action should fail and stop a playbook execution:******If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Block Entities". Reason: {0}''.format(error.Stacktrace)" | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
