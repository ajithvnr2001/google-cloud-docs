---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/splash/
title: Splash \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:40.677108+00:00
---

# Splash  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/splash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Splash

This document provides guidance on how to integrate Splash with Google SecOps.

## Use Cases

Perform enrichment of entities.

## Configure Splash integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{ip address}}:8050 | Yes | API root of the Splash instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Splash server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Splash with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the Splash server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Splash server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Splash. Supported entities: URL, IP Address.

**Note:** URLs need to have a schema. For IP addresses, action will add the "HTTPS" schema.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight containing all of the retrieved information about the entity.  
Include PNG Screenshot | Checkbox | Checked | No | If enabled, action will return a PNG screenshot in an insight. Note: "Create Insight" should be enabled for this parameter to work.  
Include History | Checkbox | Unchecked | No | If enabled, action will return history information.  
Include HAR | Checkbox | Unchecked | No | If enabled, action will return HAR information.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
original_url | When available in JSON  
final_url | When available in JSON  
title | When available in JSON  
has_history | When available in JSON  
was_redirected | When available in JSON  
count_har_entries | When available in JSON  
  
##### Insights

![Enrich Entities insight
example](https://docs.cloud.google.com/static/chronicle/images/integrations/splash-enrich-entities-insight.png)

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "url": "https://172.30.203.38/",
        "requestedUrl": "https://172.30.203.38/",
        "geometry": [
            0,
            0,
            1024,
            768
        ],
        "title": "Siemplify",
        "history": [
        ],
        "har": {
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available for one(is_success = true):** "Successfully enriched the following entities using information from Splash: {entity.identifier}".  
******If data is not available for one (is_success=true):** "Action wasn't able to enrich the following entities using information from Splash: {entity.identifier}"**If data is not available for all (is_success=false):** None of the provided entities were enriched.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
| **Title:** {entity.identifier} | Entity  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
