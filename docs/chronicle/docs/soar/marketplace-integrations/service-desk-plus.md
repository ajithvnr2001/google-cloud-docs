---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus/
title: ServiceDesk Plus \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:24:06.559113+00:00
---

# ServiceDesk Plus  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ServiceDesk Plus

This document provides guidance on how to integrate ServiceDesk Plus with Google SecOps.

## ‌Configure ServiceDesk Plus to work with Google Security Operations

  1. To generate the API key, under **User block** navigate to **Admin** > **Technicians.**
  2. To generate the API key to the existing technician, click the **Edit icon** beside the technician. On the other side, in case you want to generate the API key to a new technician, click the **Add New Technician** link, and enter the technician details and provide login permission.
  3. Click **Generate link** under the **API key details block**. You can select a time frame for the key to expire using the calendar icon or simply retain the same key perpetually.
  4. If a key is already generated for the technician, a **Re-generate link** appears.



## Configure ServiceDesk Plus integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter | Type | Default Value | Description  
---|---|---|---  
API Root | String | http://{IP OR FQDN}:8080/api/v3/ | API Root of ServiceDesk Plus.  
  
## Actions

### Add Note

#### Description

When you would like to add additional information including technical information to a particular request based on your observations, you can use add notes. You can also use notes to update the status of the request.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The requests' ID.  
Note | String | N/A | The note's content.  
Is Public | Checkbox | Unchecked | Whether to make the note public or not.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Add Note and Wait for Reply

#### Description

Add a note and wait for the new notes to be added to the given request.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The requests' ID.  
Note | String | N/A | The note's content.  
Is Public | Checkbox | N/A | Whether to make the note public or not.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
new_notes | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Close Request

#### Description

When a requester is completely satisfied that their request has been attended to and the reported problem has been solved, then the request can be closed

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The request's ID.  
Comment | String | N/A | Closing comment.  
Resolution Acknowledged | Checkbox | N/A | Whether the resolution of the request is acknowledged or not.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Create Alert Request

#### Description

Create a request related to a Google SecOps alert.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Subject | String | N/A | The subject of the request.  
Requester | String | N/A | The requester of the request. If not specified, set to the user of the API key.  
Status | String | N/A | The status of the request.  
Technician | String | N/A | The name of the technician assigned to the request.  
Priority | String | N/A | The priority of the request.  
Urgency | String | N/A | The urgency of the request.  
Category | String | N/A | The category of the request.  
Request Template | String | N/A | The template of the request.  
Request Type | String | N/A | The type of the request. Example: Incident, Service Request  
Due By Time (ms) | String | N/A | The due date of the request in milliseconds.  
Mode | String | N/A | The mode of the request.  
Level | String | N/A | The level of the request.  
Site | String | N/A | The site of the request.  
Group | String | N/A | The group of the request.  
Impact | String | N/A | The impact of the request.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Create Request

#### Description

If you have a failure or problem in your system, then raise an issue, i.e., send a request to the IT Helpdesk team. There are different modes of placing a request; using web-based form, sending an e-mail notification and making a phone call. ServiceDesk Plus provides options to log details of a request originating in any of the above mentioned forms.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Subject | String | N/A | The subject of the request.  
Requester | String | N/A | The requester of the request. If not specified, set to the user of the API key.  
Description | String | N/A | The description of the request.  
Status | String | N/A | The status of the request.  
Technician | String | N/A | The name of the technician assigned to the request.  
Priority | String | N/A | The priority of the request.  
Urgency | String | N/A | The urgency of the request.  
Category | String | N/A | The category of the request.  
Request Template | String | N/A | The template of the request.  
Request Type | String | N/A | The type of the request. Example: Incident, Service Request  
Due By Time (ms) | String | N/A | The due date of the request in milliseconds.  
Mode | String | N/A | The mode of the request.  
Level | String | N/A | The level of the request.  
Site | String | N/A | The site of the request.  
Group | String | N/A | The group of the request.  
Impact | String | N/A | The impact of the request.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
request_id | N/A | N/A  
  
##### JSON Result
    
    
    {
        "isvipuser": "No",
        "subcategory": null,
        "resolvedtime": "0",
        "site": "Chicago",
        "timespentonreq": "0hrs 0min",
        "technician": "Shawn Adams",
        "responseduebytime": "1556101814544",
        "shortdescription": "Testing the API adding request",
        "fr_duetime": "1556101814544",
        "subject": "Testing API 2",
        "impact": "Affects Business",
        "city": "London",
        "group": null,
        "approval_status": null,
        "area": null,
        "requesttype": "Convert the Incident to Change",
        "yettoreplycount": null,
        "priority": "High",
        "respondedtime": "0",
        "asset": null,
        "createdby": "Demo",
        "duebytime": "1556164814544",
        "department": null,
        "status": "Work Inprogress",
        "category": "General",
        "fcr": "false",
        "description": "Testing the API adding request",
        "closurecode": null,
        "workorderid": "123",
        "completedtime": "0",
        "requesttemplate": "Default Request",
        "requester": "Catrin Folkesson",
        "createdtime": "1556092814544",
        "technician_loginname": "adams",
        "editing_status": "0",
        "level": "Tier 1",
        "country": "India",
        "is_catalog_template": "false",
        "sla": "High SLA",
        "item": null,
        "closurecomments": null,
        "mode": "SMS",
        "editorid": "null",
        "impactdetails": null,
        "urgency": "High"
    }
    

### Get Request

#### Description

Retrieve information about a request.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The ID of the request.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "isvipuser": "No",
        "subcategory": null,
        "resolvedtime": "0",
        "site": "Chicago",
        "timespentonreq": "0hrs 0min",
        "technician": "Shawn Adams",
        "responseduebytime": "1556101814544",
        "shortdescription": "Testing the API adding request",
        "fr_duetime": "1556101814544",
        "subject": "Testing API 2",
        "impact": "Affects Business",
        "city": "London",
        "group": null,
        "approval_status": null,
        "area": null,
        "requesttype": "Convert the Incident to Change",
        "yettoreplycount": null,
        "priority": "High",
        "respondedtime": "0",
        "asset": null,
        "createdby": "Demo",
        "duebytime": "1556164814544",
        "department": null,
        "status": "Work Inprogress",
        "category": "General",
        "fcr": "false",
        "description": "Testing the API adding request",
        "closurecode": null,
        "workorderid": "123",
        "completedtime": "0",
        "requesttemplate": "Default Request",
        "requester": "Catrin Folkesson",
        "createdtime": "1556092814544",
        "technician_loginname": "adams",
        "editing_status": "0",
        "level": "Tier 1",
        "country": "India",
        "is_catalog_template": "false",
        "sla": "High SLA",
        "item": null,
        "closurecomments": null,
        "mode": "SMS",
        "editorid": "null",
        "impactdetails": null,
        "urgency": "High"
    }
    

### Ping

#### Description

Test connectivity to ServiceDesk Plus instance.

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

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Update Request

#### Description

Update a request.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The ID of the request to update.  
Requester | String | N/A | The requester of the request. If not specified, set to the user of the API key.  
Description | String | N/A | The description of the request.  
Status | String | N/A | The status of the request.  
Technician | String | N/A | The name of the technician assigned to the request.  
Priority | String | N/A | The priority of the request.  
Urgency | String | N/A | The urgency of the request.  
Category | String | N/A | The category of the request.  
Request Template | String | N/A | The template of the request.  
Request Type | String | N/A | The type of the request. Example: Incident, Service Request  
Due By Time (ms) | String | N/A | The due date of the request in milliseconds.  
Mode | String | N/A | The mode of the request.  
Level | String | N/A | The level of the request.  
Site | String | N/A | The site of the request.  
Group | String | N/A | The group of the request.  
Impact | String | N/A | The impact of the request.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "isvipuser": "No",
        "subcategory": null,
        "resolvedtime": "0",
        "site": "Chicago",
        "timespentonreq": "0hrs 0min",
        "technician": "Shawn Adams",
        "responseduebytime": "1556101814544",
        "shortdescription": "Testing the API adding request",
        "fr_duetime": "1556101814544",
        "subject": "Testing API 2",
        "impact": "Affects Business",
        "city": "London",
        "group": null,
        "approval_status": null,
        "area": null,
        "requesttype": "Convert the Incident to Change",
        "yettoreplycount": null,
        "priority": "High",
        "respondedtime": "0",
        "asset": null,
        "createdby": "Demo",
        "duebytime": "1556164814544",
        "department": null,
        "status": "Work Inprogress",
        "category": "General",
        "fcr": "false",
        "description": "Testing the API adding request",
        "closurecode": null,
        "workorderid": "123",
        "completedtime": "0",
        "requesttemplate": "Default Request",
        "requester": "Catrin Folkesson",
        "createdtime": "1556092814544",
        "technician_loginname": "adams",
        "editing_status": "0",
        "level": "Tier 1",
        "country": "India",
        "is_catalog_template": "false",
        "sla": "High SLA",
        "item": null,
        "closurecomments": null,
        "mode": "SMS",
        "editorid": "null",
        "impactdetails": null,
        "urgency": "High"
    }
    

### Wait for Field Update

#### Description

Wait for a request field to change to the desired value.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The ID of the request.  
Field Name | String | N/A | The name of the field to be updated.  
Values | String | N/A | Desired values for the given field.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
new_value | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Wait for Status Update

#### Description

Wait for the status of a request to update to a desired status.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Request ID | String | N/A | The ID of the request.  
Statuses | String | N/A | Desired request statuses, comma separated.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
new_status | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
