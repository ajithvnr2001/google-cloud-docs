---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/axonius/
title: Integrate Axonius with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:58:40.752503+00:00
---

# Integrate Axonius with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/axonius/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Axonius with Google SecOps 

This document describes how to integrate Axonius with Google Security Operations (Google SecOps).

## Use Cases

Perform enrichment actions.

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{root} | Yes | Axonius API root  
API Key | String | N/A | Yes | Axonius API Key  
API Secret | Password | N/A | Yes | Axonius API Secret  
Verify SSL | Checkbox | Checked | Yes | If selected, the integration validates the SSL certificate when connecting to the Axonius server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to Axonius.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful:** "Successfully connected to the Axonius server with the provided connection parameters!" **The action should fail and stop a playbook execution:** **If not successful:** "Failed to connect to the Axonius server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Enrich entities using information from Axonius. Supported entities include Hostname, IP Address, Mac Address, User, and Email Addresses (user entities that match email regular expression).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Endpoint Insight | Checkbox | True | No | If enabled, action will create an insight containing information about the endpoints.  
Create User Insight | Checkbox | True | No | If enabled, action will create an insight containing information about the user.  
Max Notes To Return | Integer | 50 | No | Specify how many notes to show in the case wall table.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * Mac Address
  * User
  * Email



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### JSON Result - for Endpoint:
    
    
    {
        "adapters": [
            {
                "accurate_for_datetime": "Sun, 21 Mar 2021 03:44:19 GMT",
                "client_used": "DOMAIN\\axoniusSvc",
                "raw": {
                    "ad_distinguished_name": "CN=DESKTOP-ID,OU=Computers,DC=demo,DC=local",
                    "ad_object_class": [
                        "top",
                        "person",
                        "organizationalperson",
                        "user",
                        "computer"
                    ],
                    "ad_sAMAccountName": "",
                    "ad_site_location": "Richmond",
                    "ad_site_name": "",
                    "device_disabled": false,
                    "device_managed_by": "Example User",
                    "domain": "example.example",
                    "hostname": "HOSTNAME",
                    "id": "CN=ID,OU=Computers,DC=demo,DC=local",
                    "last_seen": "Tue, 16 Mar 2021 19:44:05 GMT",
                    "name": "NAME",
                    "network_interfaces": [
                        {
                            "ips": [
                                "IP"
                            ],
                            "ips_raw": [
                                "IP_RAW"
                            ],
                            "ips_v4": [
                                "IP_V4"
                            ],
                            "ips_v4_raw": [
                                "IP_V4_RAW"
                            ]
                        }
                    ],
                    "os": {
                        "bitness": 64,
                        "distribution": "10",
                        "is_windows_server": false,
                        "os_str": "windows 10 pro 64-bit",
                        "type": "Windows",
                        "type_distribution": "Windows 10"
                    },
                    "part_of_domain": true
                },
                "plugin_name": "",
                "plugin_type": "Adapter",
                "plugin_unique_name": "",
                "quick_id": "active_directory_adapter_0!CN=ID,OU=OU,DC=DOMAIN,DC=DOMAIN",
                "type": "entitydata"
            },
            {
                "accurate_for_datetime": "Sun, 21 Mar 2021 03:43:52 GMT",
                "client_used": "https://DOMAIN",
                "raw": {
                    "hostname": "HOSTNAME",
                    "id": "ID",
                    "last_seen": "Sun, 21 Mar 2021 01:50:28 GMT",
                    "name": "NAME",
                    "network_id": "NETWORK_ID",
                    "network_interfaces": [
                        {
                            "ips": [
                                "IP"
                            ],
                            "ips_raw": [
                                "IP_RAW"
                            ],
                            "ips_v4": [
                                "IP_V4"
                            ],
                            "ips_v4_raw": [
                                "IP_V4_RAW"
                            ],
                            "mac": "01:23:45:AB:CD:EF",
                            "manufacturer": "(Intel Corporate)"
                        }
                    ]
                },
                "plugin_name": "Example",
                "plugin_type": "Adapter",
                "plugin_unique_name": "Example",
                "quick_id": "ID",
                "type": "entitydata"
            }
        ],
    "Notes": [],
        "internal_axon_id": "",
        "labels": []
    }
    

#### JSON Result - for Users:
    
    
    {
        "adapters": [
            {
                "accurate_for_datetime": "Sun, 21 Mar 2021 03:45:01 GMT",
                "client_used": "DOMAIN\\axoniusSvc",
                "raw": {
                    "account_disabled": false,
                    "ad_display_name": "",
                    "ad_distinguished_name": "CN=example, DC=example",
                    "ad_sid": "S-1-5-21-70119-3234025",
                    "ad_uac_dont_expire_password": false,
                    "ad_uac_password_not_required": false,
                    "display_name": "",
                    "domain": "example.example",
                    "employee_id": "ID",
                    "first_name": "Example",
                    "id": "CN=example, DC=example",
                    "is_admin": false,
                    "is_local": false,
                    "is_locked": false,
                    "last_name": "Example",
                    "last_password_change": "Wed, 17 Mar 2021 09:12:11 GMT",
                    "last_seen": "Thu, 18 Mar 2021 09:25:08 GMT",
                    "mail": "email@example.com",
                    "password_never_expires": false,
                    "password_not_required": false,
                    "user_city": "Boston",
                    "user_telephone_number": "(800) 555-0175",
                    "username": "user@example.com"
                },
                "user_city": "Boston",
                "user_telephone_number": "(800) 555-0175",
                "username": "user@example.com",
                "plugin_name": "active_directory_adapter",
                "plugin_type": "Adapter",
                "plugin_unique_name": "active_directory_adapter_0",
                "quick_id": "active_directory_adapter_0!CN=example,DC=example",
                "type": "entitydata"
            }
        ],
    "Notes": [],
        "internal_axon_id": "",
        "labels": []
    }
    

#### Entity Enrichment - for Endpoints:

Enrichment Field Name | Logic - When to apply  
---|---  
object_classes | When available in JSON  
site_name | When available in JSON  
device_disabled | When available in JSON  
device_managed_by | When available in JSON  
hostname | When available in JSON  
ad_distinguished_name | When available in JSON  
asset_name | When available in JSON  
ips | When available in JSON  
os | When available in JSON  
id | When available in JSON  
link | When available in JSON  
  
#### Entity Enrichment - for Users:

Enrichment Field Name | Logic - When to apply  
---|---  
account_disabled | When available in JSON  
ad_display_name | When available in JSON  
ad_distinguished_name | When available in JSON  
ad_sid | When available in JSON  
employee_id | When available in JSON  
is_admin | When available in JSON  
is_local | When available in JSON  
is_locked | When available in JSON  
mail | When available in JSON  
user_telephone_number | When available in JSON  
id | When available in JSON  
link | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If enriched some(is_success = true):** "Successfully enriched the following entities using Axonius:\n".format(entity.identifier) **If didn't enrich some (is_success = true):** "Action wasn't able to enriche the following entities using Axonius:\n".format(entity.identifier) **If didn't enrich all (is_success = false):** "No entities were enriched". **The action should fail and stop a playbook execution:** **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Entity Table |  | Entity  
Case Wall Table (if attributes/data/data list has values) | **Name: {entity.identifier}:** Notes **Column:**

  * Username
  * Note
  * Time

| General  
  
### Add Note

Add a note to entities in Axonius. Supported entities include Hostname, IP Address, Mac Address, User, and Email Addresses (user entities that match email regular expression).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Note | String | N/A | Yes | Specify what note needs to be added.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * Mac Address
  * User
  * Email Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### JSON Result
    
    
    {
        "data": {
            "attributes": {
                "accurate_for_datetime": "2021-03-21T15:55:10.876568+00:00",
                "note": "example",
                "user_id": "",
                "user_name": "internal/apiNAME",
                "uuid": ""
            },
            "type": "notes_details_schema"
        }
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If at least success for one(is_success = true):** "Successfully added note to the following entities in Axonius: {0}".format(entities) **If at least fail for one(is_success = true):** "Action wasn't able to add a note to the following entities in Axonius: {0}".format(entities) **If fail for all (is_success = false):** "Note wasn't added to the provided entities.". **The action should fail and stop a playbook execution:** **If a fatal error, like wrong credentials, no connection to the server, other:** "Error executing action "Add Note". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Tags

Add tags to entities in Axonius. Supported entities: Hostname, IP, Mac Address, User, Email Addresses (User entities that match email regex).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Tags | CSV |  | Yes | Specify a comma-separated list of tags that must be added to the entities.   
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * Mac Address
  * User
  * Email Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If at least success for one(is_success = true):** "Successfully added tags to the following entities in Axonius: {0}".format(entities) **If at least fail for one(is_success = true):** "Action wasn't able to add tags to the following entities in Axonius: {0}".format(entities) **If fail for all (is_success = false):** "Tags weren't added to the provided entities.". **The action should fail and stop a playbook execution:****If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Add Tags". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove Tags

Remove tags from entities in Axonius. Supported entities: Hostname, IP, Mac Address, User, Email Addresses (User entities that match email regex).

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Tags | CSV |  | Yes | Specify a comma-separated list of tags that must be removed from the entities.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * Mac Address
  * User
  * Email Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If at least success for one(is_success = true):** "Successfully removed tags from the following entities in Axonius: {0}".format(entities) **if at least fail for one(is_success = true):** "Action wasn't able to remove tags from the following entities in Axonius: {0}".format(entities) **If fail for all (is_success = false):** "Tags weren't removed from the provided entities.". **The action should fail and stop a playbook execution:** **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Remove Tags". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
