---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/phishinginitiative/
title: Phishing Initiative \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:12.657747+00:00
---

# Phishing Initiative  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/phishinginitiative/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Phishing Initiative

This document provides guidance on how to integrate Phishing Initiative with Google SecOps.

## Credentials - API Key and Token Authorization

  1. First, to obtain your API Key, sign in to your [PhisingInitiative Account](https://phishing-initiative.eu/contrib/).

![Phishing Initiative login
page](https://docs.cloud.google.com/static/chronicle/images/integrations/phishinginitiative-login-page.jpg)

  2. Click on your username on the upper right side of the screen and choose **API** from the drop down menu.

  3. The page displaying your API Key and Authorization Request will appear. Copy your given API Key to use it as a part of the Authorization process further in configuring Phishing Initiative.

![Get API key
value](https://docs.cloud.google.com/static/chronicle/images/integrations/phishinginitiative-get-api-key.jpg)




## Configure Phishing Initiative integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get URL Status

#### Description

Get the status of a URL.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
url | Returns if it exists in JSON result  
tag | Returns if it exists in JSON result  
tag_label | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_phishing | True/False | is_phishing:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "url": "https: //www.dieutribenhkhop.com",
                "tag": -1,
                "tag_label": "notsubmitted"
            },
            "Entity": "https: //www.dieutribenhkhop.com"
        },{
            "EntityResult": {
                "url": "http: //markossolomon.com/f1q7qx.php",
                "tag": -1,
                "tag_label": "notsubmitted"
            },
            "Entity": "HTTP: //MARKOSSOLOMON.COM/F1Q7QX.PHP"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

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
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
