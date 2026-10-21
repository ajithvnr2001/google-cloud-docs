---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-apex-central/
title: Trend Micro Apex Central \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:20.702877+00:00
---

# Trend Micro Apex Central  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-apex-central/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trend Micro Apex Central

This document provides guidance on how to integrate Trend Micro Apex Central with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/TrendMicroApexCentral.zip).

## How to obtain API Key

For more information about how to obtain API Key, see [Adding an Application](https://automation.trendmicro.com/apex-central/Guides/Using-Apex-Central-A).

## Configure Trend Micro Apex Central integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | http://x.x.x.x | Yes | API root of the Trend Micro Apex Central instance.  
Application ID | String | N/A | Yes | Application ID of the Trend Micro Apex Central instance.  
API Key | Password | N/A | Yes | API Key of the Trend Micro Apex Central instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trend Micro Apex Central server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trend Micro Apex Central with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

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
Output message* | **If successful:**   
****print Successfully connected to the Trend Micro Apex Central server with the provided connection parameters!******Not successful:** Failed to connect to the Trend Micro Apex Central server! Error: {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities with information from Trend Micro Apex Central. Supported entities: IP Address, MAC Address, Hostname, URL, Hash.

**Note:** Only SHA-1 hashes are supported.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
Create Endpoint Insight | True | No | If enabled, action will create an insight consisting of the information regarding the endpoints that were enriched.  
Create UDSO Insight | True | No | If enabled, action will create an insight consisting of the information regarding the entities that matched UDSO.  
Mark UDSO Entities | True | Noentity | If enable, action will mark all of the entities that were seen in the User-Defined Suspicious Objects list as suspicious.  
Extract Domain | False | No | If enabled, action will extract domain part of the URL entity and use it for enrichment.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Mac Address
  * Hostname
  * URL
  * Hash



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Entity Enrichment

**Host, IP, MAC**

Enrichment Field Name | Logic - When to apply  
---|---  
ip_address | Returns if it exists in JSON result.  
mac_address | Returns if it exists in JSON result.  
hostname | Returns if it exists in JSON result.  
has_endpoint_sensor | Returns if it exists in JSON result.  
isolation_status | Returns if it exists in JSON result.  
ad_domain | Returns if it exists in JSON result.  
  
**URL, Hash, IP**

Enrichment Field Name | Logic - When to apply  
---|---  
type | Returns if it exists in JSON result.  
note | Returns if it exists in JSON result.  
action | Returns if it exists in JSON result.  
expiration | Returns if it exists in JSON result.  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful for 1 entity -** Successfully retrieved information about the following entities from Trend Micro Apex Central: {\n entity.identifier}



  * **if not successful for 1 entity -** Action wasn't able to retrieve information about the following entities from Trend Micro Apex Central: {\n entity.identifier}



  * **not successful for all -** No entities were enriched using information from Trend Micro Apex Central

**The action should fail and stop a playbook execution:**

  * **Fatal error, invalid creds, API root -** Error executing action "Enrich Entities". Reason: {error traceback}

| General  
Case Wall Table | **Name:** Found Endpoints**Column:** IP AddressMAC AddressHostnameHas Endpoint SensorIsolation StatusAD Domain | (Host, IP, MAC)  
Case Wall Table | **Name:** Found UDSO**Column:** EntityNoteAction | (URL, Hash, IP)  
  
### Create File UDSO

#### Description

Create a User-defined suspicious object based on a file in Trend Micro Apex Central.

#### Known Issues

When working with .eml files, the action will not return the JSON result.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
File Paths | N/A | Yes | Specify a comma-separated list of file paths that needs to be used to created a UDSO.  
Action | BlockPossible Values:BlockLogQuarantine | Yes | Specify what action should be applied to the UDSO.  
Note | N/A | False | Specify an additional note for the provided UDSO. Warning: the note can't contain more than 256 characters.  
Expire In (Days) | N/A | False | Specify in how many days the UDSO should expire. If nothing is provided, UDSO will never expire.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 file | true | false | Successfully created UDSO based on the following files in Trend Micro Apex Central: {\n file paths}  
if not successful for 1 entity | true | false | Action wasn't able to create UDSO based on the following files in Trend Micro Apex Central: {\n file paths}  
If already exist | true | false | The following UDSO already exist in Trend Micro Apex Central: {\n file paths}  
not successful for all | false | false | No UDSO were created in Trend Micro Apex Central.  
Fatal error, invalid creds, API root | false | true | Error executing action "Create File UDSO". Reason: {error traceback}  
If note > 256 chars | false | true | Error executing action "Create File UDSO". Reason: note can't contain more than 256 characters.  
  
### Create Entity UDSO

#### Description

Create a User-defined suspicious object based on the entities in Trend Micro Apex Central. Supported entities: IP, URL, Hash.

**Note:** Only SHA-1 hashes are supported.**Note:** IP is of IPV4 type. URL has to start with http:// or https:// (maximum length of 2047 character). File Hash (SHA-1 only and maximum length of 40 characters).

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
Action | BlockPossible Values:BlockLog | Yes | Specify what action should be applied to the UDSO.  
Note | N/A | False | Specify an additional note for the provided UDSO. Warning: the note can't contain more than 256 characters.  
Expire In (Days) | N/A | False | Specify in how many days the UDSO should expire. If nothing is provided, UDSO will never expire.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * URL
  * Hash



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 entity | true | false | Successfully created UDSO based on the following entities in Trend Micro Apex Central: {\n entity.identifier}  
if not successful for 1 entity | true | false | Action wasn't able to create UDSO based on the following entities in Trend Micro Apex Central: {\n entity.identifier}  
If already exist | true | false | The following UDSO already exist in Trend Micro Apex Central: {\n entity.identifier}  
not successful for all | false | false | No UDSO were created in Trend Micro Apex Central.  
Fatal error, invalid creds, API root | false | true | Error executing action "Create Entity UDSO". Reason: {error traceback}  
If note > 256 chars | false | true | Error executing action "Create Entity UDSO". Reason: note can't contain more than 256 characters.  
  
### Unisolate Endpoints

#### Description

Unisolate endpoints in Trend Micro Apex Central. Supported entities: IP, Mac, Hostname.

**Note:** this action can take several minutes to finish, so consider increasing the timeout in the IDE.

#### Parameters

Name | Default Value | Is mandatory | Description  
---|---|---|---  
N/A | N/A | N/A | N/A  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Mac Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 entity | true | false | Successfully unisolated the following endpoints in Trend Micro Apex Central: {\n entity.identifier}  
if not successful for 1 entity | true | false | Action wasn't able to unisolate the following endpoints in Trend Micro Apex Central: {\n entity.identifier}  
not successful for all | false | false | No endpoints were unisolated in Trend Micro Apex Central.  
Async Message | false | false | Initiated endpoint unisolation on the following endpoints: {entity.identifier}. Waiting for the unisolation to finish.  
Timeout message | false | false | Action initiated unisolation, but it's still pending for the following endpoints: {entity.identifier}.Please consider increasing the timeout in the IDE.  
Fatal error, invalid creds, API root | false | true | Error executing action "Unisolate Endpoints". Reason: {error traceback}  
  
### Isolate Endpoints

#### Description

Isolate endpoints in Trend Micro Apex Central. Supported entities: IP, Mac, Hostname.

**Note:** this action can take several minutes to finish, so consider increasing the timeout in the IDE.

#### Parameters

Name | Default Value | Is mandatory | Description  
---|---|---|---  
N/A | N/A | N/A | N/A  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Mac Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 entity | true | false | Successfully isolated the following endpoints in Trend Micro Apex Central: {\n entity.identifier}  
if not successful for 1 entity | true | false | Action wasn't able to isolate the following endpoints in Trend Micro Apex Central: {\n entity.identifier}  
not successful for all | false | false | No endpoints were isolated in Trend Micro Apex Central.  
Async Message | false | false | Initiated endpoint isolation on the following endpoints: {entity.identifier}. Waiting for the isolation to finish.  
Timeout message | true | false | Action initiated isolation, but it's still pending for the following endpoints: {entity.identifier}.Please consider increasing the timeout in the IDE.  
Fatal error, invalid creds, API root | false | true | Error executing action "Isolate Endpoints". Reason: {error traceback}  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
