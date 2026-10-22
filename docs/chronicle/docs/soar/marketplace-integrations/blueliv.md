---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/blueliv/
title: BlueLiv \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:50.997227+00:00
---

# BlueLiv  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/blueliv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BlueLiv

This document describes how to integrate BlueLiv with Google Security Operations.

## Integration guide

The integration purpose is to ingest the threats from BlueLiv, using the relevant filters to only show the desired threats within Google Security Operations, using the Threats Connector, and then have additional actions performed on those threats according to the relevant use cases.

In this quick guide we will go through a few things to make the usage of the integration easier for Google SecOps customers.

**Integration configuration**

We will go over the parameters and where to find those so it will be easier for you to configure the integration:

  * API Root - this is the URL you are using in order to view the BlueLiv homepage, when the suffix /api/v2 added to it. For example: `https://tcdach.blueliv.com/api/v2` should be the value on this parameter.
  * User name - same user name you use to connect to the BlueLiv homepage.
  * Password - same password you use to connect to the BlueLiv homepage.
  * Organization ID - you can easily spot the organization ID on the URL you are using in order to browse the product itself, so for example:

For this example, here the organization ID is `117`:

`https://tcdach.blueliv.com/dashboard/organizations/117/indexed`




After going through the integration parameters, we can deep dive to the other terms in our integration.

**Module Types**

BlueLiv have divided the threats section to module types, and on this integration we use those types to help the SOAR platform and ingest only the relevant information if you want to filter by module type. The following module types are currently available in BlueLiv:

  * Credentials
  * Social Media
  * Credit Cards
  * Domain Protection
  * Malware
  * Data Leakage
  * Hacktivism
  * Dark Web
  * Custom
  * Media Tracker
  * Mobile Apps

**Note:** You can have a number of modules with the same type, for example: Data Leakage, Siemplify Leakage are the Data Leakage type modules. You can easily see that by looking at the icon right next to the module name in the navigation bar.

**Threat ID and Module ID**

`https://tcdach.blueliv.com/dashboard/organizations/117/modules/1303/resource/31024379`

Every threat you can find in BlueLiv has a UID, a number that represents it. This one can also be easily spotted in the URL. A threat is also called a resource. For example, here the threat UID is `31024379`.

Also, for every module that you have on BlueLiv you have a UID, a number that represents it. For example, here the threat UID is `1303`.

## Recommendation regarding configuration

Blueliv only allows one open session a time. It is recommended to use different users for integration configuration and connectors for stability purposes. Note: each connector would need a separate user.

## Use Cases

  1. Proactive cyber threat monitoring
  2. Brand Protection
  3. Data Breach Protection
  4. Fraud Prevention
  5. Counterfeit Detection



## Configure BlueLiv integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://example  
.blueliv.com/api/v2 | Yes | API Root of the BlueLiv instance.  
User Name | String | N/A | Yes | User Name of BlueLiv.  
Password | Password | N/A | Yes | Password of the user  
Organization ID | String | N/A | Yes | Specify the Organization ID to use in BlueLiv  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the IronScales server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to BlueLiv with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If both API calls were successful:** "Successfully connected to the BlueLiv server with the provided connection parameters!" **The action should fail and stop a playbook execution:** **If only first call was ok and second one didn't work:** "Successfully logged in with the user name and password, but seems like the Organization ID is not correct. Please check the Organization ID parameter in the Integration Configuration page and try again " **if not successful:** "Failed to connect to the BlueLiv! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Threat Context module of Blueliv. Supported entities: IP, Hash, URL, Threat Actor, Threat Campaign, Threat Signature, Domain, CVE.

**Note:** Only MD5, SHA1, SHA256 and SHA512 hashes are supported.

#### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Lowest Score To Mark as Suspicious | 5 | Yes | Specify what should be the lowest score for the entity to be marked as suspicious. Maximum: 10.  
Create Insight | True | No | If enabled, action will create insights containing information about entities.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hash
  * URL
  * Threat Actor
  * Threat Campaign
  * Threat Signature
  * CVE



##### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### Case Wall

**Case** | **Success** | **Fail** | **Message**  
---|---|---|---  
If enriched some entities | true | false | Successfully enriched the following entities using information from Blueliv: {entity.identifier}  
If not enriched some | true | false | Action wasn't able to enrich the following entities using information from Blueliv: {entity.identifier}  
if not enriched all | false | false | No entities were enriched using information from Blueliv.  
Fatal error, invalid creds, API root | false | true | Error executing action "Enrich Entities". Reason: {error traceback}  
If "Threat Context" module is not available | false | True | Error executing action "Enrich Entities". Reason: your instance doesn't support "Threat Context" module.  
  
### Add Comment to a Threat

#### Description

The action will add a desired text comment to a specific threat.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Module Type | String | N/A | Yes | Specify the module type the resource belongs to.  
Module ID | String | N/A | Yes | Specify the module ID the resource belongs to.  
Resource ID | String | N/A | Yes | Specify the Resource ID to add the comment to.  
Comment Text | String | N/A | Yes | Provide the comment you would like to add to the resource.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful:** "Successfully added the comment to threat ID: "+{threat_ID} **The action should fail and stop a playbook execution:** **If not successful:** "Failed to perform action "Add Comment to a Threat {0}".format(exception.stacktrace) | General  
Case Wall table | **Name:** "Threat ID "+{threat_id}+" Comments: **Column:**

  * Comment Row
  * Comment ID
  * Content 
  * Creation Date
  * Commenter 

|   
  
### Mark Threat as a Favorite

#### Description

The action will mark the specified threat as a favorite threat in BlueLiv.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **DDL Values** | **Is Mandatory** | **Description**  
---|---|---|---|---|---  
Module Type | String | N/A |  | Yes | Specify the module type the resource belongs to.  
Module ID | String | N/A |  | Yes | Specify the module ID the resource belongs to.  
Resource ID | String | N/A |  | Yes | Specify the Resource ID to add the comment to.  
Favorite Status | DDL | User Starred | Not Starred User Starred Group Starred Full Starred | Yes | Provide the Favorite status you would like to apply on the specified threat.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful:** "Successfully marked threat ID: "+{threat_ID}+" as favorite" **The action should fail and stop a playbook execution:** **If not successful:** "Failed to perform action "Mark Threat as a Favorite {0}".format(exception.stacktrace) | General  
  
### Add Labels to Threats

#### Description

The action will add the specified label name to the specified threat IDs.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Module Type | String | N/A | Yes | Specify the module type the resource belongs to.  
Module ID | String | N/A | Yes | Specify the module ID the resource belongs to.  
Resource ID | String | N/A | Yes | Specify the Resource IDs, i na comma separated list, to add the labels to.  
Label Names | String | N/A | Yes | Specify the label names you would like to apply to the specified threats, in a comma-separated list. Please pay attention to lowercase and uppercase.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If some labels weren't found successfully:** "Couldn't find the following labels in BlueLiv":+(unsuccessful_label names_list)+". Please check the label names you have provided in the action parameters and try again" **If some threats weren't found:** "Couldn't find the following threats in BlueLiv":+(unsuccessful_threat_IDs)+". Please check the threat IDs you have provided in the action parameters and try again" **If was successful:** "Successfully added the following labels:" +(successful_label_names_list)+" to the following "threat IDs: "+(successful_threat_IDs_list) **The action should fail and stop a playbook execution:** **If no labels were found successfully:** "Couldn't find any of the following labels in BlueLiv":+(unsuccessful_label names_list)+". Please check the label names you have provided in the action parameters and try again" **If no Threats were found successfully:** "Couldn't find any of the following Threats in BlueLiv":+(unsuccessful_threat_IDs_list)+". Please check the threat IDs you have provided in the action parameters and try again" **If not successful:** "Failed to perform action "Add Labels to Threats".format(exception.stacktrace) | General  
  
### Remove Labels From Threats

#### Description

The action will remove the specified labels from the specified threat IDs.

##### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Module Type | N/A | Yes | Specify the module type the resource belongs to.  
Module ID |  | Yes | Specify the module ID the resource belongs to  
Resource ID |  | Yes | Specify a comma-separated list of resource IDs from which you want to remove labels.  
Label Names |  | Yes | Specify a comma-separated list of labels that need to be removed. Please pay attention to lowercase and uppercase.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Case** | **Success** | **Fail** | **Message**  
---|---|---|---  
If some labels weren't found | true | false | "Couldn't find the following labels in BlueLiv: \n {labels}. Please check the label names you have provided in the action parameters and try again."  
If some threats weren't found | true | false | Couldn't find the following threats from module {module} {threat IDs}: {threat IDs}. Please check the threat IDs you have provided in the action parameters and try again  
If successful for some: | true | false | Successfully removed the following labels from the following threat {threat ID} in Blueliv: {successful_labels}  
If some were not applied already: | true | false | The following labels were already not a part of the threat {threat ID} in Blueliv: {labels already not a part}  
If no labels are found | false | true | Error executing action "Remove Labels From Threats". Reason: None of the labels were found. Please check the spelling.  
If no threats were found | false | true | Error executing action "Remove Labels From Threats". Reason: None of the threats were found. Please check the spelling.  
Fatal error, invalid creds, API root | false | true | Error executing action "Remove Labels From Threats". Reason: {error traceback}  
If module type or id is not valid | false | true | Error executing action "Remove Labels From Threats". Reason: invalid module ID or module type was provided.  
  
### List Entity Threats

#### Description

List threats related to entities in Blueliv. Supported entities: All.

#### Known Limitations

Blueliv API might not return any results, even if the string matches the threat name identically. Example is shown below:

https://pastebin.com/YRkUCLGc - URL is shown, when searching using the "pastebin" keyword.

![](https://lh6.googleusercontent.com/qsRbvp8V8Oa8FtRveGpgm6v7P2YCqzNCWwS2MxfjQQU2oWotqcsTuLxgGG-S5POobm75tTzwv3SF65iN6E2A-9RbEB9m-cNVr5cU6DNDLJ6Ppb8j-82Y50KIVEXFtFrbPyG3_Z8w=s0)

https://pastebin.com/YRkUCLGc - is not shown, when searching using the "https://pastebin.com/YRkUCLGc" keyword.

![](https://lh5.googleusercontent.com/1x_Cc_gIx-oIejwzbD4rmgLLuuw-s9NbldxyEbyWBbQDqz6bM-nmZzYC2Y5mMzBO2PmOvVcfkA9iK9BXr-wQtmnZ6AvKFjftA7HONsZ5vDeAI1Z_VF7DUCIwCZjFc1UXl1_nwOw3=s0)

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Label Filter | CSV | N/A | No | Specify a comma-separated list of labels, that will be used to filter threats. Note: label filter works with "OR" logic.  
Module Filter | CSV | N/A | No | Specify a comma-separated list of modules, that will be used to filter threats.  
Max Threats To Return | Integer | 50 | No | Specify how many threats to return per entity. If nothing is specified, action will return 50 threats.  
  
#### Run On

This action runs on all entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "id": xxxxxxx,
        "module_id": xxxx,
        "module_name": "Data Leakage",
        "module_short_name": "xxx-xxxxx",
        "module_type": "DATA_LEAKAGE",
        "url": "xxx",
        "content_type": "text/html",
        "countries_id": "xx",
        "analysis_result": "INFORMATIVE",
        "analysis_calc_result": "INFORMATIVE",
        "created_at": 1626163680000,
        "checked_at": 1626163680000,
        "changed_at": 1626163680000,
        "user_rating": 0,
        "read": true,
        "fav": "NOT_STARRED",
        "issued": false,
        "labels": [
            {
                "id": 36116,
                "name": "GithubCodeByFilename",
                "background_color": 16777215,
                "text_color": 0,
                "type": "GLOBAL"
            },
            {
                "id": 160,
                "name": "Public",
                "background_color": 45960,
                "text_color": 16777215,
                "type": "GLOBAL"
            }
        ],
        "tlpStatus": "AMBER",
        "searchPhrase": "credit card",
        "followedUp": false,
        "history": []
    },
    

##### Case Wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If data is available for one(is_success = true):** "Successfully listed available threats to the following entities in Blueliv: {entity.identifier}". **If no threats for one (is_success=true):** "No related threats were found to the following entities in Blueliv: {entity.identifier}" **If no threats for one (is_success=true):** "No related threats were found to the provided entities in Blueliv" **The action should fail and stop a playbook execution:** **If fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Entity Threats". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Title:** {entity.identifier} Module Name URL Title Labels Created At  | Entity  
  
## Connector

### BlueLiv - Threats Connector

#### Description

Pull security threats from BlueLiv. Connector fetches all of the latest threats from BlueLiv modules.

Whitelist and blacklist filters work with BlueLiv module types. For example, if you want to get threats only from Hacktivism modules, you can turn on the whitelist and type in the "Hacktivism" type name.

For each module type, there's a different structure of data being ingested into Google SecOps. Please modify the mapping in your Google SecOps instance to best suit your needs. Please make sure to see the different "event_type" values for each event coming back from BlueLiv.

For the _Malware_ threat type, we currently provide the basic event data only. We will add an additional event very soon, to better handle the special data that comes back from a _Malware_ threat type.

#### Configure BlueLiv - Threats Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Product Field Name | String | ProductName | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API URL | String | https://example.blueliv.com/api/v2 | Yes | API Root of the BlueLiv instance.  
User Name | String | N/A | Yes | User name for BlueLiv  
Password | Password | N/A | Yes | User password for BlueLiv  
Organization ID | String | N/A | Yes | Specify the Organization ID to use in BlueLiv  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max threats To Fetch | Integer | 10 | No | How many threats to process per one connector iteration.   
Note - Maximum value here is 100.  
Severity | String | Medium | Yes | Severity will be one from the following values Low, Medium, High, Critical.  
Will be assigned to Google SecOps alerts created from this connector.   
Analysis results to ingest | String (Values: NOT_AVAILABLE, NOT_IMPORTANT, NOT_PROCESSABLE, POSITIVE, NEGATIVE, INFORMATIVE, IMPORTANT) | N/A | No | Filter the threats by the analyst analysis to this threat, only ingest threats with the chosen analysis result. Provide a comma separated list of the desired analysis results to ingest.  
Possible values: NOT_AVAILABLE, NOT_IMPORTANT, NOT_PROCESSABLE, POSITIVE, NEGATIVE, INFORMATIVE, IMPORTANT  
Labels to filter by | String (comma separated list) | N/A | No | Please provide a comma separated list of the label names you want to filter by. Please pay attention to uppercase and lowercase letters and write the labels exactly as they appear in BlueLiv UI.  
Reading status to ingest | String (Values: "Only Read", "Only Unread") | N/A | No | Filter the threats by their reading status, so that the connector will ingest according to it. If no value is provided we will fetch both. Options: "Only Read", "Only Unread".  
Should Ingest only starred threats? | Checkbox | Unchecked | No | If checked, only starred (favorite) threats will be ingested  
Should Ingest threats related to incidents? | String (values:, Only Incidents, Only Non Incidents) | N/A | No | Should connector filter the threats by checking the relationship to an incident. If no value is provided we will fetch both .Options are: Only Incidents- will ingest only threats related to incidents, Only Non Incidents - will ingest only threats that are not related to incidents  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the BlueLiv server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
