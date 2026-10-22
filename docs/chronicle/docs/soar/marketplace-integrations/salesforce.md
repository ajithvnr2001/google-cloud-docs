---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/salesforce/
title: Salesforce \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:29.586160+00:00
---

# Salesforce  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Salesforce

This document provides guidance on how to integrate Salesforce with Google SecOps.

## Configure Salesforce to work with Google Security Operations

### Obtain a Security Token

Upon creating your Salesforce account, Salesforce Support will send you an email that contains a security token confirmation to the email address associated with the account. This email is the only place where you can find the Security Token Value. Please note that every time you change the account password, the security token is also regenerated and a similar email is sent.

**Note:** For more information on security tokens, see [Supporting Multiple Instances](https://www.salesforcetutorial.com/security-tokens-in-salesforce-com/).

## Configure Salesforce integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | N/A | Required. | The base URL for your Salesforce instance's API. For example: `https://yourcompany.my.salesforce.com/services/data/vXX.X/` (where `vXX.X` is the API version, for example, `v58.0`).  
Username | String | N/A | Required. | The username for the Salesforce account that connects to the API.  
Password | Password | N/A | Required. | The password for the Salesforce account that connects to the API. If your Salesforce account uses a security token, you must append it to the end of the password.  
Token | Password | Unchecked. | Required. | TThe Salesforce security token used for authentication. Use this parameter with the **Username** and **Password** fields if your Salesforce account requires a security token for authentication.  
Verify SSL | Boolean | Unchecked. | Optional. | If enabled, the integration validates the SSL certificate when connecting to Salesforce.  
  
## Actions

### Add Comment

#### Description

Add a comment to a case.

#### Parameters

**Parameter** | Type | Default Value | Description  
---|---|---|---  
Case Number | String | N/A | The number of the case.  
Title | String | N/A | The comment title.  
Body | String | N/A | The comment's body.  
  
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
    

### Close Case

#### Description

Delete a domain from the OpenDNS block list.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Case Number | String | null | N/A  
  
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
    

### Create Case

#### Description

Create a case.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Subject | String | N/A | The case's subject.  
Status | String | N/A | The case's status. Valid values: New, On Hold, Closed, Escalated.  
Description | String | N/A | The description of the subject.  
Origin | String | N/A | The origin of the case. Valid values: Email, Phone, Web.  
Priority | String | N/A | The case's priority. Valid values: Low, Medium, High.  
Type | String | N/A | The case type. Valid values: Question, Problem, Feature Request.  
  
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
case_number | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Case

#### Description

Get details on a case.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Case Number | String | N/A | The number of the case.  
  
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
    
    
    {
    "Field2": "Value2",
    "attributes":
    {
    "url": "/services/data/v20.0/sobjects/Case/123456789",
    "type": "Case"
    },
    "Field1": "Value1",
    "Field3": "Value3"
    }
    

### List Cases

#### Description

The case list component displays a list of the user's cases. Only authenticated users can see a list of the cases that they've created.

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
    
    
    [
        {
            "Field2": "Value2",
            "attributes": {
                "url": "/services/data/v20.0/sobjects/Case/123456789",
                "type": "Case"
            },
            "Field1": "Value1",
            "Field3": "Value3"
        },
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
    

### Search Records

#### Description

Search all records that contain values with a given pattern.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | N/A  
  
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
    
    
    {
        "Tasks": [{
            "WhoId": "0033600001bbxuPAAQ",
            "ActivityDate": "2018-07-24",
            "Id": "00T3600003T0io5EAB",
            "Subject": "Email Sent: Re: domain - SOAR RFI / RFP template with domain answers"
        },{
            "WhoId": "0033600001cYpvnAAC",
            "ActivityDate": "2018-07-24",
            "Id": "00T3600003T0ixHEAR",
            "Subject": "Email Sent: domain - SOAR RFI / RFP template with domain answers"
        }],
        "Users": [{
            "Phone": null,
            "Name": "lname fname, CISSP",
            "Title": "Senior Sales Engineer",
            "Email": "john_doe@example.com",
            "Id": "0051Q00000FoH8OQAV"
        },{
            "Phone": null,
            "Name": ". Marketo",
            "Title": null,
            "Email": "john_doe@example.com",
            "Id": "0051Q00000FoNDUQA3"
        }],
        "Contacts": [{
            "Name": "John",
            "Title": null,
            "MobilePhone": null,
            "Email": "john_doe@example.com",
            "Phone": null,
            "OwnerId": "00536000006kd4wAAA",
            "Id": "0031Q00001uwg4mQAA",
            "AccountId": "0013600001o7XYtAAM"
        },{
            "Name": "Bill",
            "Title": "test",
            "Email": "john_doe@example.com",
            "Phone": "7327108052",
            "OwnerId": "005360000075cJpAAI",
            "Id": "0031Q00001uwxgWQAQ",
            "AccountId": "0013600001o7XYtAAM"
        }]
    }
    

### Update Case

#### Description

Update a case.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Case Number | String | N/A | The number of the case.  
Subject | String | N/A | The case's subject.  
Status | String | N/A | The case's status. Valid values: New, On Hold, Closed, Escalated.  
Description | String | N/A | The description of the subject.  
Origin | String | N/A | The origin of the case. Valid values: Email, Phone, Web.  
Priority | String | N/A | The case's priority. Valid values: Low, Medium, High.  
Type | String | N/A | The case type. Valid values: Question, Problem, Feature Request.  
  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
