---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-cloud-app-security/
title: Trend Micro Cloud App Security \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:34.665752+00:00
---

# Trend Micro Cloud App Security  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-cloud-app-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trend Micro Cloud App Security

This document provides guidance on how to integrate Trend Micro Cloud App Security with Google SecOps.

## Product Use Cases

Perform active actions - enrich entities, search email, update block list, mitigate emails/accounts..

## How to generate API token

  1. Navigate to **Administration > Automation and Integration APIs**.
  2. Press on the "Add" button.
  3. Select "For External Application".
  4. Provide "Name" and select all checkboxes.
  5. Press on the "Create Token".
  6. Copy "Token".
  7. Update "API Key" parameter in the integration configuration.
  8. Test the connectivity.



## Configure Trend Micro Cloud App Security integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api-eu.tmcas.trendmicro.com | Yes | API root of the Trend Micro Cloud App Security instance.  
API Key | Password | N/A | Yes | API Key of the Trend Micro Cloud App Security instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Trend Micro Cloud App Security server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trend Micro Cloud App Security with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
Output message* | **If Successful (is success = true) -** Successfully connected to the Trend Micro Cloud App Security server with the provided connection parameters!**If not Successful (is success = false) -** Failed to connect to the Trend Micro Cloud App Security server! Error: {0}".format(exception.stacktrace) | General  
  
### Add Entities To Blocklist

#### Description

Add entities to a blocklist in Trend Micro Cloud App Security. Supported entities: URL, Hash and Email (User entity that matches email address pattern).

**Note:** Only SHA-1 hashes are supported.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
N/A | N/A | N/A | N/A  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hash
  * Email



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 entity | true | false | Successfully added the following entities to blocklist in Trend Micro Cloud App Security: {\n entity.identifier}  
if not successful for 1 entity | true | false | Action wasn't able to add the following entities to blocklist in Trend Micro Cloud App Security: {\n entity.identifier}  
If duplicates | true | false | The following entities are already a part of blocklist in Trend Micro Cloud App Security: {\n entity.identifier}  
not successful for all | false | false | No entities were added using information from Trend Micro Cloud App Security  
Fatal error, invalid creds, API root | false | true | Error executing action "Add Entities To Blocklist". Reason: {error traceback}  
  
### Mitigate Emails

#### Description

Delete or quarantine emails using Trend Micro Cloud App Security. Note: for Gmail you can only delete emails.

**Note:** Currently action only initiates a mitigation, but doesn't check the status of mitigation execution.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
Message IDs | N/A | Yes | Specify a comma-separated list of message ids that need to be mitigated.  
Mitigation Action | DeletePossible Values:DeleteQuarantine | Yes | Specify what mitigation action should be applied.  
Service | GmailPossible ValuesGmailExchange | Yes | Specify the service the is used for emails.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 message_id | True | false | Successfully mitigated the following emails in Trend Micro Cloud App Security: {\n unique message ids}  
if not successful for 1 message_id | True | false | Action wasn't able to mitigate the following emails in Trend Micro Cloud App Security: {\n unique message ids}  
not successful for all | false | false | No emails were mitigated Trend Micro Cloud App Security.  
Fatal error, invalid creds, API root | false | true | Error executing action "Mitigate Emails". Reason: {error traceback}  
If "Quarantine" is selected and "Gmail" is the service | false | true | Error executing action "Mitigate Emails". Reason: you can only delete emails in gmail service.  
  
### Entity Email Search

#### Description

Search emails based on entities in Trend Micro Cloud App Security. Supported entities: URL, Hash, Email (User entity that matches email address pattern), Email Subject, File Name, IP.

**Note:** Only SHA-1 and SHA256 hashes are supported.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
Max Days Backwards | 30 | No | Specify how many days backwards to look for emails. Maximum is 90. Default: 30.  
Max Emails To Return | 100 | No | Specify how many emails to return. Default: 100.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hash
  * Email
  * Email Subject
  * File Name
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    emails=[{list of unique emails}]
    

##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if data is available: | true | false | Successfully returned information about emails related to the provided entities in Trend Micro Cloud App Security.  
if data is not available | false | false | No information about emails related to entities were found in Trend Micro Cloud App Security.  
Fatal error, invalid creds, API root | false | true | Error executing action "Entity Email Search". Reason: {error traceback}  
If "Max Days Backwards" > 90 | false | true | Error executing action "Entity Email Search". Reason: "Max Days Backwards" should be in range from 1 to 90.  
  
### Enrich Entities

#### Description

Enrich entities with information from Trend Micro Cloud App Security. Supported entities: URL, Hash and Email (User entity that matches email address pattern).

**Note:** This action will use the domain part out of the URL during the enrichment.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
N/A | N/A | N/A | N/A  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hash
  * Email



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    blocked_url = [URL entities that were found]
    blocked_hashes = [hashes entities that were found]
    blocked_senders = [User entities that were found]
    

##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 entity | true | false | Successfully retrieved information about the following entities from Trend Micro Cloud App Security: {\n entity.identifier}  
if not successful for 1 entity | true | false | Action wasn't able to retrieve information about the following entities from Trend Micro Cloud App Security: {\n entity.identifier}  
not successful for all | false | false | No entities were enriched using information from Trend Micro Cloud App Security  
Fatal error, invalid creds, API root | false | true | Error executing action "Enrich Entities". Reason: {error traceback}  
  
### Mitigate Accounts

#### Description

Perform mitigation actions on the user account via Trend Micro Cloud App Security.

**Note:** Only Exchange accounts are supported.

#### Parameters

Name | Default Value | Is Mandatory | Description  
---|---|---|---  
Email Addresses | N/A | Yes | Specify a comma-separated list of email addresses that need to be mitigated.  
Mitigation Action | Disable AccountEnable MFAReset PasswordRevoke Sign In Sessions | Yes | Specify a what mitigation action should be applied.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful for 1 email address. | true | false | Successfully mitigated the following accounts in Trend Micro Cloud App Security: {\n email addresses}  
if not successful for 1 entity | true | false | Action wasn't able to mitigate the following accounts in Trend Micro Cloud App Security: {\n email addresses}  
not successful for all | false | false | No account were mitigated using information from Trend Micro Cloud App Security.  
Async Message | false | false | Waiting for mitigation actions to finish…  
Fatal error, invalid creds, API root | false | true | Error executing action "Mitigate Account". Reason: {error traceback}  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
