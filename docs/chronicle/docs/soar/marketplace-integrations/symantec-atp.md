---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-atp/
title: Symantec ATP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:56.688190+00:00
---

# Symantec ATP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-atp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec ATP

This document provides guidance on how to integrate Symantec ATP with Google SecOps.

## Configure Symantec ATP to work with Google Security Operations

### To generate an OAuth client:

  1. In Symantec ATP Manager, navigate to **Settings,** and then **Data Sharing**.
  2. Click **Add Application** in the OAuth Clients section.
  3. Please type the name of the application that you intend to register in the App Name field, and then select the API version you will be using (default setting is version 2).
  4. If you select enabling version 2 APIs, a **Role** option will appear. Select the user role for the app from the drop-down menu.
  5. Click **Generate**.
  6. The client ID and client secret will appear.
  7. Click **Done**.

**Note:** For more information on generating an OAuth client, see this [article](https://support.symantec.com/us/en/article.HOWTO128830.html).

## Configure Symantec ATP integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add Comment to Incident

#### Description

Attach a comment to an incident.

  1. For the incident in which you want to make a comment, click on the **Comments** field.
  2. Type your comment in the New Comment box. Extended ASCII characters do not render properly in .csv format.
  3. Click **Add Comments**.



#### Parameters

**Parameter** | Type | Default Value | Description  
---|---|---|---  
Incident UUID | String | N/A | N/A  
Comment | String | N/A | N/A  
  
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
is_added | True/False | is_added:False  
  
##### JSON Result
    
    
    N/A
    

### Add to Blacklist

#### Description

Create a blacklist policy for an entity. Symantec maintains a worldwide blacklist of external computers and files that is updated regularly and integrated with Symantec Advanced Threat Protection (ATP). You can supplement this list by creating blacklist policies for external computers or the files that you deem untrustworthy. For example, you may want to create a blacklist policy for a file that recently appeared in your cybersecurity intelligence that Symantec has yet to identify as a threat.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Filehash
  * Hostname
  * IP Address
  * URL



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
    

### Add to Whitelist

#### Description

When you whitelist an external computer, ATP considers it trustworthy and does not inspect traffic to or from it from your endpoints (even if it's blacklisted). You can whitelist an external computer based on its IP address, subnet, domain, or URL.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Filehash
  * Hostname
  * IP Address
  * URL



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
    

### Close Incident

#### Description

Change incident status to closed. The outcome of the incident has to be specified in order to close it.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Incident UUID | String | N/A | N/A  
  
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
is_closed | True/False | is_closed:False  
  
##### JSON Result
    
    
    N/A
    

### Delete File

#### Description

When a file is selected for deletion in Advanced Threat Protection (ATP), it is not actually deleted, but will be quarantined by the selected endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Filehash | String | N/A | File hash to delete.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Filehash
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
command_ids | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Delete Whitelist Policy

#### Description

Delete a whitelist policy for an entity.

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
    

### Enrich Filehash

#### Description

Enrich a file hash entity.

#### Parameters

N/A

#### Use cases

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
max_file_health | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Events for Entity

#### Description

Fetch all events for an entity since time.

**Warning:** Only users with the admin rights or controller rights can perform any actions.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Minutes Back to Fetch | String | N/A | Fetch the event x minutes back.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
events_amount | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Events Free Query

#### Description

Fetch events by free query.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | Free query text.  
Limit | String | N/A | Limit of query results.  
  
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
events_amount | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Sandbox Commands Status

#### Description

Get commands status by the ID.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Command IDs | String | N/A | Command ID to fetch the status for.  
  
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
    

### Isolate Endpoint

#### Description

To isolate endpoints from ATP Manager, a quarantine firewall policy and host integrity policy in Symantec Endpoint Protection Manager is required.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
command_ids | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Verifies that the user has a connection to Symantec ATP via the user's device.

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
    

### Rejoin Endpoints

#### Description

To rejoin endpoints from ATP Manager, a quarantine firewall policy and host integrity policy in Symantec Endpoint Protection Manager is required.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
command_ids | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Revoke From Blacklist

#### Description

Delete a blacklist policy for a given entity.

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
    

### Submit Files to Sandbox

#### Description

Submit file hashes to sandbox.

#### Parameters

N/A

#### Use cases

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
command_ids | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Incident Comments

#### Description

Retrieve comments related to the incident.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Incident UUID | String | N/A | True | Specify the UUID of the incident.  
Max Comments To Return | Integer | 20 | False | Specify how many comments to return.Maximum is 1000 comments. This is a Symantec ATP limitation.  
  
#### Run On

This action doesn't run on entities.

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
        "next": "MSwyMDIwLTA1LTAzVDEyOjU4OjMwLjc2Mlo=",
        "result": [
            {
                "comment": "TExt",
                "time": "2020-05-03T09:57:10.348Z",
                "user_id": 2,
                "incident_responder_name": "Admin"
            }
        ],
        "total": 3
    }
    
    {
        "entity": "{Incident UUID} comments"
        "Entity Results": [
    "1": {
                "comment": "TExt",
                "time": "2020-05-03T09:57:10.348Z",
                "user_id": 2,
                "incident_responder_name": "Admin"
            },
    "2" : {
     {
                "comment": "TExt",
                "time": "2020-05-03T09:57:10.348Z",
                "user_id": 2,
                "incident_responder_name": "Admin"
            },
    "3":
     {
                "comment": "TExt",
                "time": "2020-05-03T09:57:10.348Z",
                "user_id": 2,
                "incident_responder_name": "Admin"
            }
    
    ]
    
               ],
        "total": 3
    }
    

#### Update Incident Resolution

#### Description

Update resolution on the incident.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Incident UUID | String | N/A | True | Specify the UUID of the incident.  
Resolution Status | DDL | INSUFFICIENT DATAPossible values:INSUFFICIENT DATASECURITY RISKFALSE POSITIVEMANAGED EXTERNALLYNOT SETBENIGNTEST | True | Specify what resolution status to set on the incident.  
  
#### Run On

This action doesn't run on entities.

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
    

### Delete BlackList Policy

#### Description

Delete a blacklist policy for a Google SecOps entity.

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
    

## Connectors

### Symantec ATP - Incidents Connector

#### Connector Permissions

In order for the connector to work you need the following permissions for your API token:

  * atp_view_incidents



#### Configure Symantec ATP - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | True | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | AlertName | True | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | False | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | False | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | True | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:port | True | API root of Symantec ATP server.  
Client ID | Password | N/A | True | Symantec ATP Client ID  
Client Secret | Password |  | True | Symantec ATP Client Secret  
Priority Filter | CSV | Low, Medium, High | True | Priority filter for the incidents. If you want to ingest all of the incidents specify:  
Low,Medium,High.  
Fetch Max Hours Backwards | Integer | 1 | False | Amount of hours from where to fetch incidents. Limit: 30 days. This is a Symantec ATP limitation.  
Max Incidents To Fetch | Integer | 25 | False | How many incidents to process per one connector iteration. Max: 1000.  
Use whitelist as a blacklist | Boolean | Unchecked | True | If enabled, whitelist will be used as a blacklist.  
Use SSL | Boolean | Checked | True | Option to enable SSL/TLS connection  
Proxy Server Address | String |  | False | The address of the proxy server to use  
Proxy Username | String |  | False | The proxy username to authenticate with  
Proxy Password | Password |  | False | The proxy password to authenticate with  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
