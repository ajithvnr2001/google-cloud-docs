---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/misp/
title: Integrate MISP with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:11:36.407656+00:00
---

# Integrate MISP with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/misp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate MISP with Google SecOps

This document explains how to integrate MISP with Google Security Operations.

## Use cases

The **MISP** integration uses Google SecOps capabilities to support the following use cases:

  * **Enrich indicators of compromise** : Automatically retrieve context for URLs, hostnames, IP addresses, and file hashes from your MISP instance to identify known malicious actors.

  * **Automate event creation and sharing** : Create new MISP events directly from playbooks and publish them to sharing groups to alert your security community of new threats.

  * **Manage event classification** : Dynamically add or remove tags from events and attributes to maintain an accurate and up-to-date threat landscape.

  * **Investigate related threats** : Search for and retrieve information about events related to specific entities to understand the broader scope of an ongoing investigation.

  * **Analyze suspicious files** : Upload files to MISP events for collaborative analysis or download existing event attachments for internal sandbox evaluation.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following requirements met in your MISP environment:

  * **MISP API key** : You must have a valid automation key to authenticate the connection. You can obtain this from the event actions menu within your MISP UI. For more information, see [Automation and MISP API](https://www.circl.lu/doc/misp/automation/).

  * **API root address** : Ensure you have the IP address or hostname of your MISP instance available for configuration.

  * Optional: **CA certificate** : If your environment requires SSL verification using a specific certificate, ensure you have the CA certificate file available. You must provide this value as a Base64 encoded string during configuration.

  * **Integration version** : Verify that you are running the latest version of the MISP integration to ensure all actions and parameters are supported.




## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://<IP> | Yes | Address of the MISP instance.  
API Key | String | N/A | Yes | Generated in MISP's console.  
Use SSL | Checkbox | Unchecked | No | Use this checkbox, if your MISP connection requires an SSL verification (unchecked by default).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Attribute

Add an entity as an attribute to a MISP event.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | The ID of the event.  
Category | String | External analysis | No | The category of the attribute. Default: External analysis.  
Distribution | String | 1 | No | The distribution of the attribute. Default: 1.  
For Intrusion Detection System | Checkbox | Unchecked | No | Whether the attribute is used for Intrusion Detection System. Default: false.  
Comment | String | N/A | No | The comment to add to the attribute.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address
  * Filehash



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
    

### Create Event

Create a new MISP event.

#### Known Limitation

Currently, MISP API doesn't allow event to be immediately published upon creation. You need to first create an event and then use action "Publish Event".

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event Name | String | N/A | Yes | The name of the event.  
Threat Level | String | 0 | No | The threat level of the event. Default: 0.  
Distribution | String | 1 | No | The distribution of the attribute. Default: 1.  
Analysis | String | 0 | No | The analysis level of the event [0-2]: Default: 0.  
Publish | Checkbox | Checked | No | Whether to publish the event or not.  
Comment | String | N/A | No | The comment of the event.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
event_id | N/A | N/A  
  
### Add Tag to an Event

Add a tag to an event action allows a user to add a tag to a specific event in MISP. This adds a classification to the event based on the category of the security threat posed by the IOC associated with the event.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | The unique identifier specifying the event to add tag to.  
Tag Name | String | N/A | Yes | The name of the tag to add to an event.  
  
#### Use cases

**Classify an event:** Update the event through adding a tag.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "saved": true,
            "success": "Tag(s) added.",
            "check_publish": true
        }
    ]
    

### Download File

Download files related to event in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | No | Specify the ID or UUID of the event from which you want to download files  
Download Folder Path | String | N/A |  | Specify the absolute path to the folder, which should store files. If nothing is specified, action will create an attachment instead.   
Note: JSON result is only available, when you provide proper value for this parameter.  
Overwrite | Checkbox | Unchecked |  | If enabled, action will overwrite existing files.  
  
#### Run On

This action runs on the Filehash entity.

##### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
    
    "absolute_paths": ["/etc/file1.txt", "/etc/file2.txt"]
    
    }
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If success:** "Successfully downloaded the following files from the event with {0} {1} in MISP:\n{2}".format(ID/UUID, event_id, result/filename from the response)**if no files were found:** "No files were found for the event with {0} {1} in MISP:\n{2}".format(ID/UUID, event_id)**if "Download Folder Path" is not specified and some of the files exceeded platform limit for attachments:** "Action wasn't able to download the following files, because they exceeded the limit of 3 MB: \n {0}. \n Please specify a folder path in the parameter "Download Folder Path" in order to download them.".(result/filename)**Critical Error (fail action)** "Error executing action "Download File". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Download File". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id)**If overwrite is false and one of the files already exists:** "Error executing action "Download File". Reason: The following files already exist: {0}. Please remove them or set parameter "Overwrite" to true.".format(absolute path to the file) | General  
  
### Enrich Entities

Enrich entities based on the attributes in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
Number of attributes to return | String | N/A | Specify how many attributes to return for entities.  
Filtering condition |  |  | Specify the filtering condition for the action. If "Last" is selected, action will use the oldest attribute for enrichment, if "First" is selected, action will use the newest attribute for enrichment.  
Threat Level Threshold | DDL | LowPossible Values:HighMediumLowUndefined | Specify what should be the threshold for the threat level of the event, where the entity was found. If related event exceeds or matches threshold, entity will be marked as suspicious.  
Attribute Search Limit | Integer | 50 | Specify how many attributes to search for per entity. This parameter has an impact on which attribute will be selected for enrichment. Default: 50.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address
  * Filehash



##### Action Results

##### Entity Enrichment

Entities are marked as suspicious if the threat level of the event exceeds 0. Otherwise: False

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                    "Event":
                    {
                        "orgc_id": "1",
                        "ShadowAttribute": [],
                        "id": "3",
                        "threat_level_id": "3",
                        "event_creator_email": "john_doe@example.com",
                        "uuid": "5c5bff1b-a414-4a83-8755-035f0a000016",
                        "Object": [],
                        "Orgc": {
                            "uuid": "5c5ac66e-3884-4031-afd7-46f5bb9ebcaa",
                            "name": "ORGNAME",
                            "id": "1"
                        },
                        "Org": {
                            "uuid": "5c5ac66e-3884-4031-afd7-46f5bb9ebcaa",
                            "name": "ORGNAME",
                            "id": "1"
                        },
                        "RelatedEvent": [],
                        "sharing_group_id": "0",
                        "timestamp": "1549533154",
                        "date": "2019-02-07",
                        "disable_correlation": "False",
                        "info": "Test event",
                        "locked": "False",
                        "publish_timestamp": "1549533214",
                        "Attribute": [
                            {
                                "category": "Network activity",
                                "comment": " ",
                                "uuid": "5c5bffe2-9298-4098-ae31-035d0a000016",
                                "deleted": "False",
                                "timestamp": "1549533154",
                                "to_ids": "False",
                                "distribution": "3",
                                "object_id": "0",
                                "event_id": "3",
                                "ShadowAttribute": [],
                                "sharing_group_id": "0",
                                "value": "1.1.1.1",
                                "disable_correlation": "False",
                                "object_relation": "None",
                                "type": "ip-src",
                                "id": "1",
                                "Galaxy": []
                            }],
                        "attribute_count": "1",
                        "org_id": "1",
                        "analysis": "2",
                        "extends_uuid": " ",
                        "published": "True",
                        "distribution": "3",
                        "proposal_email_lock": "False",
                        "Galaxy": []
                    }}],
            "Entity": "1.1.1.1"
        }
    ]
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **For attributes that were found: (is_success=true)** "Successfully enriched the following entities using MISP: \n{0}".format(entity.identifier)******For attributes that were not found (is_success=true)** "Action wasn't able to enrich the following entities using MISP: \n{0}".format(entity.identifier)******If all attributes were not found (is_success=false)** "No entities were enriched using MISP"******If attributes are suspicious (is_success=true)** "The following attributes were marked as suspicious using MISP: \n {0}".format(entity.identifier) | General  
CSV Table | **Table Columns:**

  * ID 
  * Event ID 
  * Category 
  * Type 
  * UUID
  * Timestamp
  * Distribution 
  * IDS 

|   
  
### Get Related Events

Retrieve information about events that are related to entities in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
Mark As Suspicious | Checkbox | Checked | If enabled, action will mark entity as suspicious, if there is at least one related event to it.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address
  * Filehash



#### Action Results

##### Entity Enrichment

If records of related events are available, then entities are marked as suspicious. otherwise: False.

Enrichment Field Name | Logic - When to apply  
---|---  
Event | Returns if it exists in JSON result  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                    "Event":
                    {
                        "orgc_id": "1",
                        "ShadowAttribute": [],
                        "id": "3",
                        "threat_level_id": "3",
                        "event_creator_email": "john_doe@example.com",
                        "uuid": "5c5bff1b-a414-4a83-8755-035f0a000016",
                        "Object": [],
                        "Orgc": {
                            "uuid": "5c5ac66e-3884-4031-afd7-46f5bb9ebcaa",
                            "name": "ORGNAME",
                            "id": "1"
                        },
                        "Org": {
                            "uuid": "5c5ac66e-3884-4031-afd7-46f5bb9ebcaa",
                            "name": "ORGNAME",
                            "id": "1"
                        },
                        "RelatedEvent": [],
                        "sharing_group_id": "0",
                        "timestamp": "1549533154",
                        "date": "2019-02-07",
                        "disable_correlation": "False",
                        "info": "Test event",
                        "locked": "False",
                        "publish_timestamp": "1549533214",
                        "Attribute": [
                            {
                                "category": "Network activity",
                                "comment": " ",
                                "uuid": "5c5bffe2-9298-4098-ae31-035d0a000016",
                                "deleted": "False",
                                "timestamp": "1549533154",
                                "to_ids": "False",
                                "distribution": "3",
                                "object_id": "0",
                                "event_id": "3",
                                "ShadowAttribute": [],
                                "sharing_group_id": "0",
                                "value": "1.1.1.1",
                                "disable_correlation": "False",
                                "object_relation": "None",
                                "type": "ip-src",
                                "id": "1",
                                "Galaxy": []
                            }],
                        "attribute_count": "1",
                        "org_id": "1",
                        "analysis": "2",
                        "extends_uuid": " ",
                        "published": "True",
                        "distribution": "3",
                        "proposal_email_lock": "False",
                        "Galaxy": []
                    }}],
            "Entity": "1.1.1.1"
        }
    ]
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If one event found for at least one entity:** "Successfully retrieved information about the related events for the following entities: \n{0}".format(entity.identifier)**If no event found for at least one entity:** "Action wasn't able to retrieve information about the related events for the following entities: \n{0}".format(entity.identifier**If no events for all: "** No related events were found for the provided entities." | General  
  
### Upload File

Upload a file to a MISP event.

#### Parameters

Name | Type | Default | Description  
---|---|---|---  
Event ID | String | N/A | Specify the ID or UUID of the event to which you want to upload this file.  
File Path | String | N/A | Specify a comma-separated list of absolute filepaths of the files that you want to upload to MISP.  
Category |  |  | Specify the category for the uploaded file. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Distribution | String | Community | Specify the distribution for the uploaded file.   
Possible values: 0 - Organisation, 1 - Community, 2 - Connected, 3 - All. You can either provide a number or a string.  
Threat Level | String | High | Specify the threat level for the uploaded file.   
Possible values: 1 - High, 2 - Medium, 3 - Low, 4 - Undefined. You can either provide a number or a string.  
Analysis | String | Initial | Specify the analysis of the event.  
Possible values: 0 - Initial, 1 - Ongoing, 2 - Completed. You can either provide a number or a string.  
Info | String | N/A | Specify additional info for the uploaded file.  
For Intrusion Detection System | Checkbox | Unchecked | If enabled, uploaded file will be used for intrusion detection systems.  
Comment | String | N/A | Specify additional comments related to the uploaded file.  
  
##### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Event": {
            "id": "106",
            "orgc_id": "1",
            "org_id": "1",
            "date": "2021-01-15",
            "threat_level_id": "1",
            "info": "vanuhi 1015",
            "published": false,
            "uuid": "1cd22aa2-57e8-4fc8-bac6-721c1be2c27d",
            "attribute_count": "10",
            "analysis": "0",
            "timestamp": "1610893968",
            "distribution": "1",
            "proposal_email_lock": false,
            "locked": false,
            "publish_timestamp": "0",
            "sharing_group_id": "0",
            "disable_correlation": false,
            "extends_uuid": "",
            "event_creator_email": "admin@admin.test",
            "Org": {
                "id": "1",
                "name": "ORGNAME",
                "uuid": "09b0dde1-2934-4310-a107-74b6f534f041",
                "local": true
            },
            "Orgc": {
                "id": "1",
                "name": "ORGNAME",
                "uuid": "09b0dde1-2934-4310-a107-74b6f534f041",
                "local": true
            },
            "Attribute": [],
            "ShadowAttribute": [],
    "Object": [
                {
                    "id": "446",
                    "name": "file",
                    "meta-category": "file",
                    "description": "File object describing a file with meta-information",
                    "template_uuid": "688c46fb-5edb-40a3-8273-1af7923e2215",
                    "template_version": "20",
                    "event_id": "106",
                    "uuid": "0188ba5d-68eb-4b5c-8e05-6fd49f8eee9a",
                    "timestamp": "1610691647",
                    "distribution": "1",
                    "sharing_group_id": "0",
                    "comment": "",
                    "deleted": false,
                    "first_seen": null,
                    "last_seen": null,
                    "ObjectReference": [],
                    "Attribute": [
                        {
                            "id": "1859",
                            "type": "malware-sample",
                            "category": "External analysis",
                            "to_ids": true,
                            "uuid": "7920cd28-5082-47ce-9c3e-3ccbd5dae138",
                            "event_id": "106",
                            "distribution": "1",
                            "timestamp": "1610703650",
                            "comment": "",
                            "sharing_group_id": "0",
                            "deleted": false,
                            "disable_correlation": false,
                            "object_id": "446",
                            "object_relation": "malware-sample",
                            "first_seen": null,
                            "last_seen": null,
                            "value": "vanuhi.txt|7bd55b0a276e076cbaf470e64359adb8",
                            "Galaxy": [],
                            "data": "UEsDBAoACQAAAJgyL1Kgt+vZDwAAAAMAAAAgABwAN2JkNTViMGEyNzZlMDc2Y2JhZjQ3MGU2NDM1OWFkYjhVVAkAAz80AWA/NAFgdXgLAAEEIQAAAAQhAAAADCVIVuu0HeIv/PqGdn5EUEsHCKC369kPAAAAAwAAAFBLAwQKAAkAAACYMi9SGoPq+xYAAAAKAAAALQAcADdiZDU1YjBhMjc2ZTA3NmNiYWY0NzBlNjQzNTlhZGI4LmZpbGVuYW1lLnR4dFVUCQADPzQBYD80AWB1eAsAAQQhAAAABCEAAABLQfOZfPB0svIGywREZ5dDLdomR6gPUEsHCBqD6vsWAAAACgAAAFBLAQIeAwoACQAAAJgyL1Kgt+vZDwAAAAMAAAAgABgAAAAAAAEAAACkgQAAAAA3YmQ1NWIwYTI3NmUwNzZjYmFmNDcwZTY0MzU5YWRiOFVUBQADPzQBYHV4CwABBCEAAAAEIQAAAFBLAQIeAwoACQAAAJgyL1Iag+r7FgAAAAoAAAAtABgAAAAAAAEAAACkgXkAAAA3YmQ1NWIwYTI3NmUwNzZjYmFmNDcwZTY0MzU5YWRiOC5maWxlbmFtZS50eHRVVAUAAz80AWB1eAsAAQQhAAAABCEAAABQSwUGAAAAAAIAAgDZAAAABgEAAAAA",
                            "ShadowAttribute": [],
                            "Sighting": [
                                {
                                    "id": "1733",
                                    "attribute_id": "1859",
                                    "event_id": "106",
                                    "org_id": "1",
                                    "date_sighting": "1611207638",
                                    "uuid": "feb085f1-1923-4327-a73d-b60a948377e4",
                                    "source": "",
                                    "type": "0",
                                    "Organisation": {
                                        "id": "1",
                                        "uuid": "09b0dde1-2934-4310-a107-74b6f534f041",
                                        "name": "ORGNAME"
                                    },
                                    "attribute_uuid": "7920cd28-5082-47ce-9c3e-3ccbd5dae138"
                                }
                            ]
                        }
                }
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **If successful for one entity:** "Succesfully uploaded the provided files to the event {0} in MISP".format(event_id)**Critical Error (fail action)** "Error executing action "Upload File". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Distribution** _"_ **(fail action):** "Error executing action "Upload File". Reason: Invalid value was provided for the parameter "Distribution". Acceptable numbers: 0,1,2,3. Acceptable strings: Organisation, Community, Connected, All".**If invalid parameter is specified in "Threat Level" (fail action):** "Error executing action "Upload File". Reason: Invalid value was provided for the parameter "Threat Level". Acceptable numbers: 1,2,3,4. Acceptable strings: High, Medium, Low, Undefined".**If invalid parameter is specified in "Category" (fail action):** "Error executing action "Upload File". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If invalid parameter is specified in "Analysis" (fail action):** "Error executing action "Upload File". Reason: Invalid value was provided for the parameter "Analysis". Acceptable numbers: 0,1,2. Acceptable strings: Initial, Ongoing, Completed".**if at least one of the files is not available** "Error executing action "Upload File". Reason: the following files were not accessible: \n {0}".format(file paths, that were not accessible.)**Event ID is not found (fail action)** "Error executing action "Upload File". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Ping

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

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Remove Tag From an Event

Remove tags from event in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event, from which you want to remove tags.  
Tag Name | CSV | N/A | Yes | Specify a comma-separated list of tags that you want to remove from events.  
  
#### Use cases

**Re-classify event:** Remove tag for reclassification.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "saved": true,
            "success": "Tag removed.",
            "check_publish": true
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **If successfully removed all tag from an event:** "Successfully removed the following tags from the event with {0} {1} in MISP: {2}.".format(ID/UUID, event_id, tags)**If not successfully removed some tags from an event:** "Action wasn't able to remove the following tags from the event with {0} {1} in MISP: {2}.".format(ID/UUID, event_id, tags)**If not successful for all:** "No tags were removed from the event with {0} {1} in MISP".format(ID/UUID, event_id)**If at least one tag was not found:** "The following tags were not found in MISP: \n{0}".format(list of tags that were not found in MISP)**If all tags were not found:** "None of the provided tags were found in MISP."**Critical Error (fail action)** "Error executing action "Remove Tag from an Event". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Remove Tag from an Event". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Add Tag to an Attribute

This action allows a user to add a tag to a specific attribute in MISP. This adds a classification to the attribute based on the category of a security threat posed by the IOC in the attribute.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | Integer | N/A | Yes | The identifier of the event that the attribute is associated with. Example: 1.  
Tag Name | String | N/A | Yes | The name of the tag to add to an attribute.  
Attribute Name | String | N/A | Yes | The name identifier of the attribute to tag.  
Category | String | N/A | Yes | The category which the attribute belongs to. e.g. Payload Delivery.  
Type | String | N/A | Yes | The type of the attribute. e.g. filename.  
Object UUID | String | N/A | No | The unique identifier for an object in the event.  
  
#### Use cases

**Classify attribute based on IOC type:** Add tag to attribute.

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
    
    
    [
        {
            "name": "Global tag unique___test(7) successfully attached to Attribute(9).",
            "message": "Global tag unique___test(7) successfully attached to Attribute(9).",
            "url": "/tags/attachTagToObject"
        }
    ]
    

### Remove Tag From an Attribute

Remove tags from attributes in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | No | Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if "Attribute Search" is set to "Provided Event".  
Tag Name | CSV | N/A | Yes | Specify a comma-separated list of tags that you want to remove from attributes.  
Attribute Name | CSV | N/A | No | Specify a comma-separated list of attribute identifiers from which you want to remove tags.   
Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
Category | CSV | N/A | No | Specify a comma-separated list of categories. If specified, action will only remove tags from attributes that have matching category. If nothing is specified, action will ignore categories in attributes.   
Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Type | CSV | N/A | No | Specify a comma-separated list of attribute types. If specified, action will only remove tags from attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes.   
Example values: md5, sha1, ip-src, ip-dst  
Object UUID | CSV | N/A |  | Specify the UUID of the object that contains the desired attribute.  
Attribute Search | DDL | Provided EventPossible values:All EventsProvided Event | Yes | Specify, where action should search for attributes. If "Provided Event" is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in "Event ID" parameter. If "All Events", action will search for attributes among all events and remove tags from all attributes that match our criteria.  
Attribute UUID | CSV |  |  | Specify a comma-separated list of attribute UUIDs from which you want to remove new tags. Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
  
#### Use cases

**Re-classify attribute:** Remove tag for reclassification

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "name": "Tag unique___test(7) successfully removed from Attribute(9).",
            "message": "Tag unique___test(7) successfully removed from Attribute(9).",
            "url": "/tags/removeTagFromObject"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type>  
---|---|---  
Output message* | **If successfully removed tags from at least one attribute:** "Successfully removed tags from the following attributes in MISP:\n{0}".format(attribute name/object UUID)**if not successfully removed tags from at least one attribute:** "Action didn't removed tags from the following attributes in MISP:\n{0}".format(attribute name/object UUID)**If not successful for all:** "No tags were removed from the provided attributes in MISP"**If at least one tag was not found:** "The following tags were not found in MISP: \n{0}".format(list of tags that were not found in MISP)**If all tags were not found:** "None of the provided tags were found in MISP."**Critical Error (fail action)** "Error executing action "Remove Tag from an Attribute". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Category" (fail action):** "Error executing action "Remove Tag from an Attribute". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If "Provided Event" is selected, but Event ID is not selected:** "Error executing action "Remove Tag from an Attribute". Reason: Event ID needs to be provided, if "Provided Event" is selected for the parameter "Attribute Search"".**Event ID is not found (fail action)** "Error executing action "Remove Tag from an Attribute". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Publish Event

The action allows the user to publish an event. Publishing an event shares it to the sharing group selected, making it visible to all members.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event that you want to publish.  
  
#### Use cases

**Publish an event:**

  1. Create even
  2. Add event attributes
  3. Publish event



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "Event": {
                "id": "3",
                "orgc_id": "1",
                "org_id": "1",
                "date": "2019-12-27",
                "threat_level_id": "1",
                "info": "Connection to .ch",
                "published": true,
                "uuid": "5e05dd29-7b90-474d-b5f6-51ae0a00024b",
                "attribute_count": "0",
                "analysis": "1",
                "timestamp": "1577774920",
                "distribution": "3",
                "proposal_email_lock": false,
                "locked": false,
                "publish_timestamp": "1577774846",
                "sharing_group_id": "0",
                "disable_correlation": false,
                "extends_uuid": "5e05db24-1e98-4bb9-bd56-51fd0a00024b",
                "event_creator_email": "admin@admin.test",
                "Org": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5dfc9b8f-c320-4b6d-ac1c-4f4e8bdc3fef",
                    "local": true
                },
                "Orgc": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5dfc9b8f-c320-4b6d-ac1c-4f4e8bdc3fef",
                    "local": true
                },
                "Attribute": [],
                "ShadowAttribute": [],
                "RelatedEvent": [],
                "Galaxy": [],
                "Object": [],
                "Tag": [
                    {
                        "id": "7",
                        "name": "unique___test",
                        "colour": "#9648c4",
                        "exportable": true,
                        "user_id": "0",
                        "hide_tag": false,
                        "numerical_value": null,
                        "local": 0
                    }
                ]
            }
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **If successful:** "Successfully published event with {0} {1} in MISP.".format(ID/UUID, event_id)**If not successful:** "Event with {0} {1} was not published in MISP".format(ID/UUID, event_id)**Critical Error (fail action)** "Error executing action "Publish Event". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Publish Event". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Unpublish Event

The action allows the user to unpublish an event. Unpublishing an event prevents it from being visible to the shared groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event that you want to unpublish.  
  
##### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "Event": {
                "id": "3",
                "orgc_id": "1",
                "org_id": "1",
                "date": "2019-12-27",
                "threat_level_id": "1",
                "info": "Connection to .ch",
                "published": false,
                "uuid": "5e05dd29-7b90-474d-b5f6-51ae0a00024b",
                "attribute_count": "0",
                "analysis": "1",
                "timestamp": "1577774920",
                "distribution": "3",
                "proposal_email_lock": false,
                "locked": false,
                "publish_timestamp": "1577774846",
                "sharing_group_id": "0",
                "disable_correlation": false,
                "extends_uuid": "5e05db24-1e98-4bb9-bd56-51fd0a00024b",
                "event_creator_email": "admin@admin.test",
                "Org": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5dfc9b8f-c320-4b6d-ac1c-4f4e8bdc3fef",
                    "local": true
                },
                "Orgc": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5dfc9b8f-c320-4b6d-ac1c-4f4e8bdc3fef",
                    "local": true
                },
                "Attribute": [],
                "ShadowAttribute": [],
                "RelatedEvent": [],
                "Galaxy": [],
                "Object": [],
                "Tag": [
                    {
                        "id": "7",
                        "name": "unique___test",
                        "colour": "#9648c4",
                        "exportable": true,
                        "user_id": "0",
                        "hide_tag": false,
                        "numerical_value": null,
                        "local": 0
                    }
                ]
            }
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **If successful:** "Successfully unpublished event with {0} {1} in MISP.".format(ID/UUID, event_id)**If not successful:** "Event with {0} {1} was not unpublished in MISP".format(ID/UUID, event_id)**Critical Error (fail action)** "Error executing action "Unpublish Event". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Unpublish Event". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Delete an Attribute

Delete attributes in MISP. Supported hashes: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SSDeep.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | No | Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if "Attribute Search" is set to "Provided Event".  
Attribute Name | CSV | N/A | No | Specify a comma-separated list of attribute identifiers that you want to delete.   
Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
Category | CSV | N/A | No | Specify a comma-separated list of categories. If specified, action will only delete attributes that have matching category. If nothing is specified, action will ignore categories in attributes.   
Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Type | CSV | N/A | No | Specify a comma-separated list of attribute types. If specified, action will only delete attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes.   
Example values: md5, sha1, ip-src, ip-dst  
Object UUID | String | N/A | No | The unique identifier for an object in the event.  
Attribute Search | DDL | Provided EventPossible values:All EventsProvided Event | Yes | Specify, where action should search for attributes. If "Provided Event" is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in "Event ID" parameter. If "All Events", action will search for attributes among all events and delete all attributes that match our criteria.  
Attribute UUID | CSV |  |  | Specify a comma-separated list of attribute UUIDs that you want to delete.   
Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
  
#### Use cases

Remove an attribute from an event.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "message": "Attribute deleted."
        }
    ]
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If successfully added Sighting to at least one attribute:** "Successfully deleted the following attributes in MISP:\n{0}".format(attribute name/object UUID)**if not successfully added Sighting to at least one attribute:** "Action didn't delete the following attributes in MISP:\n{0}".format(attribute name/object UUID)**If not successful for all:** "No attributes were deleted in MISP"_Critical Error (fail action)_ "Error executing action "Delete an Attribute". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Category" (fail action):** "Error executing action "Delete an Attribute". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If "Provided Event" is selected, but Event ID is not selected:** "Error executing action "Delete an Attribute". Reason: Event ID needs to be provided, if "Provided Event" is selected for the parameter "Attribute Search"".**Event ID is not found (fail action)** "Error executing action "Delete an Attribute". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Delete an Event

Delete event in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event that you want to delete.  
  
#### Use cases

Delete an event permanently.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "name": "Event deleted.",
            "message": "Event deleted.",
            "url": "/events/delete/4"
        }
    ]
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If successful:** "Successfully deleted event with {0} {1} in MISP".format(ID/UUID, event_id)**Critical Error (fail action)** "Error executing action "Delete an Event". Reason: {0}".format(traceback)**Event ID is not found (fail action)** "Error executing action "Delete an Event". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Create File Misp Object

The action allows the user to organize file attributes related to an event in a single object which describes a file with its meta-information. The object with the attributes is then attached to a specified event.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | The unique identifier of the event to add the object. Example: 1  
Filename | String | N/A | No | The filename of the file.  
MD5 | String | N/A | No | The md5 hash value of the file.  
SHA1 | String | N/A | No | The sha1 hash value of the file.  
SHA256 | String | N/A | No | The sha256 hash value of the file.  
SSDEEP | String | N/A | No | The ssdeep value of the file Example: 96:p5aAS1tN0M3t9AnTNuG6TNOt5PR1TNZdkljOXTNSnKTF3X7KsTFW+kLtW6K8i7bI:p5mb4rgQhRp7GljCbF3LKqFjkwxtU  
Imphash | String | N/A | No | The MD5 hash value calculated from the imported table.  
  
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

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Create IP-Port Misp Object

The action allows the user to organize IP-port attributes related to an event in a single object which describes an IP address (or domain or hostname) and a port seen as a tuple (or as a triple) in a specific time frame . The object with the attributes is then attached to a specified event.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | The unique identifier of the event to add the object. Example: 1  
Dst-port | String | N/A | No | Destination port.  
Src-port | String | N/A | No | Source port.  
Domain | String | N/A | No | Domain.  
Hostname | String | N/A | No | Hostname.  
IP-Src | String | N/A | No | Source IP Address.  
IP-Dst | String | N/A | No | Destination IP Address.  
  
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

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Create network-connection Misp Object

Create a network-connection Object in MISP. Requires one of the following: Dst-port, Src-port, IP-Src, IP-Dst to be provided or "Use Entities" parameter set to true.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event to which you want to add network-connection objects.  
Dst-port | String | N/A | No | Specify the destination port, which you want to add to the event.  
Src-port | String | N/A | No | Specify the source port, which you want to add to the event.  
Hostname-dst | String | N/A | No | Specify the source destination, which you want to add to the event.  
Hostname-src | String | N/A | No | Specify the source hostname, which you want to add to the event.  
IP-Src | String | N/A | No | Specify the source IP, which you want to add to the event.  
IP-Dst | String | N/A | No | Specify the destination IP, which you want to add to the event.  
Layer3-protocol | String | N/A | No | Specify the related layer 3 protocol, which you want to add to the event.  
Layer4-protocol | String | N/A | No | Specify the related layer 4 protocol, which you want to add to the event.  
Layer7-protocol | String | N/A | No | Specify the related layer 7 protocol, which you want to add to the event.  
Use Entities | Checkbox | Unchecked | No | If enabled, action will use entities in order to create objects. Supported entities: IP Address. "Use Entities" has priority over other parameters.  
IP Type | DDL | Source IPPossible values:Source IPDestination IP |  | Specify what attribute type should be used with IP entities.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If success and "Use Entities" is not true:** "Successfully created new network-connection object for event with {0} {1} in MISP.".format(ID/UUID, event_id)**If not success and "Use Entities" is not true:** "Action wasn't able to created new network-connection object for event with {0} {1} in MISP. Reason: {2}".format(ID/UUID)**If success for one and "Use Entities" is true:** "Successfully created new network-connection objects for event with {0} {1} in MISP based on the following entities: \n{0}".format(ID/UUID, event_id, entity.identifiers)**If not success for one and "Use Entities" is true:** "Action wasn't able to create new network-connection objects for event with {0} {1} in MISP based on the following entities: \n{0}".format(ID/UUID, event_id, entity.identifiers)******If not success for all and "Use Entities" is true:** "Action wasn't able to create new network-connection objects for event with {0} {1} in MISP based on the provided entities.".format(ID/UUID, event_id)**Critical Error (fail action)** "Error executing action "Create network-connection Misp Object". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Create network-connection Misp Object". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id)**If none of the Dst-port, Src-port, IP-Src, IP-Dst are provided and "Use Entities" == false:** "Error executing action "Create network-connection Misp Object". Reason: One of the: "Dst-port", "Src-port", "IP-Src", "IP-Dst" should be provided or "Use Entities" parameter set to true". | General  
  
### Create Url Misp Object

Create a URL Object in MISP. Requires "URL" to be provided or "Use Entities" parameter set to true.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event to which you want to add URL objects.  
URL | String | N/A | No | Specify the URL, which you want to add to the event.  
Port | String | N/A | No | Specify the port, which you want to add to the event.  
First seen | String | N/A | No | Specify, when the URL was first seen.   
Format: 2020-12-22T13:07:32Z  
Last seen | String | N/A | No | Specify, when the URL was last seen.   
Format: 2020-12-22T13:07:32Z  
Domain | String | N/A | No | Specify the domain, which you want to add to the event.  
Text | String | N/A | No | Specify the additional text, which you want to add to the event.  
IP | String | N/A | No | Specify the IP, which you want to add to the event.  
Host | String | N/A | No | Specify the Host, which you want to add to the event.  
Use Entities | Checkbox | Unchecked |  | If enabled, action will use entities in order to create objects. Supported entities: URL. "Use Entities" has priority over other parameters.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If success and "Use Entities" is not true:** "Successfully created new URL object for event with {0} {1} in MISP.".format(ID/UUID, event_id)**If not success and "Use Entities" is not true:** "Action wasn't able to created URL object for event with {0} {1} in MISP. Reason: {2}".format(ID/UUID)**If success for one and "Use Entities" is true:** "Successfully created new URL objects for event with {0} {1} in MISP based on the following entities: \n{0}".format(ID/UUID, event_id, entity.identifiers)**If not success for one and "Use Entities" is true:** "Action wasn't able to create new URL objects for event with {0} {1} in MISP based on the following entities: \n{0}".format(ID/UUID, event_id, entity.identifiers)**If not success for all and "Use Entities" is true:** "Action wasn't able to create new URL objects for event with {0} {1} in MISP based on the provided entities.".format(ID/UUID, event_id)**Critical Error (fail action)** "Error executing action "Create Url Misp Object". Reason: {0}".format(stacktrace)**Event ID is not found (fail action)** "Error executing action "Create Url Misp Object". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id)**If none of the URL are provided and "Use Entities" == false:** "Error executing action "Create Url Misp Object". Reason: Either "URL" should be provided or "Use Entities" parameter set to true". | General  
  
### Create Virustotal-Report Object

Create a Virustotal-Report Object in MISP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID or UUID of the event to which you want to add URL objects.  
Permalink | String | N/A | Yes | Specify the link to the VirusTotal report, which you want to add to the event.  
Comment | String | N/A | No | Specify the comment, which you want to add to the event.  
Detection Ratio | String | N/A | No | Specify the detection ration, which you want to add to the event.  
Community Score | String | N/A | No | Specify the community score, which you want to add to the event.  
First Submission | String | N/A | No | Specify first submission of the event.   
Format: 2020-12-22T13:07:32Z  
Last Submission | String | N/A | No | Specify last submission of the event.   
Format: 2020-12-22T13:07:32Z  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If success :** "Successfully created new Virustotal-Report object for event with {0} {1} in MISP.".format(ID/UUID, event_id)**If not success :** "Action wasn't able to created Virustotal-Report object for event with {0} {1} in MISP. Reason: {2}".format(ID/UUID)**Critical Error (fail action)** "Error executing action "Create Virustotal-Report Misp Object". Reason: {0}".format(stacktrace)******Event ID is not found (fail action)** "Error executing action "Create Virustotal-Report Misp Object". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### List Event Objects

Retrieve information about available objects in MISP event.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify a comma-separated list of IDs and UUIDs of the events, for which you want to retrieve details.  
Max Objects to Return | Integer | 50 | No | Specify how many objects to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "Object": [
        {
            "id": "1",
            "name": "ftm-Associate",
            "meta-category": "followthemoney",
            "description": "Non-family association between two people",
            "template_uuid": "6119ecb3-dedd-44b6-b88f-174585b0b1bf",
            "template_version": "1",
            "event_id": "1",
            "uuid": "2a3e260f-d3b2-4164-b2b1-2f6f5b559970",
            "timestamp": "1594632232",
            "distribution": "5",
            "sharing_group_id": "0",
            "comment": "",
            "deleted": false,
            "first_seen": null,
            "last_seen": null,
            "ObjectReference": [],
        },
        {
            "id": "2",
            "name": "ftm-Associate",
            "meta-category": "followthemoney",
            "description": "Non-family association between two people",
            "template_uuid": "6119ecb3-dedd-44b6-b88f-174585b0b1bf",
            "template_version": "1",
            "event_id": "1",
            "uuid": "800d8634-175a-4bc2-a4d7-aca200c8c132",
            "timestamp": "1594632463",
            "distribution": "5",
            "sharing_group_id": "0",
            "comment": "",
            "deleted": false,
            "first_seen": null,
            "last_seen": null,
            "ObjectReference": [],
        }
    

##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If at least object found for 1 event:** "Successfully listed objects for the following events: \n{0}".format(event_ids)  
******If event with specified id was not found (is_success = false):**  
****print "Action was not able to list objects. Reason: Event with ID {0} was not found in MISP.".format(event_id)  
**If no object found for 1 event:** "Action wasn't able to find objects for the following events:\n {0}".format(event_ids)******If no object found for all events: "** No objects were found for the provided events."  
******The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ **** print "Error executing action "List Event Objects". Reason: {0}''.format(error.Stacktrace) | General  
CSV Table | **Table name:** Event {0} Objects**Table Columns:**

  * Object UUID (mapped as uuid)
  * Name (mapped as name)
  * Category (mapped as meta-category)
  * Description (mapped as description)
  * Comment (mapped as comment)

|   
  
### Get Event Details

Retrieve details about events in MISP.

#### Parameters

Parameter Display Name | Type | Is Mandatory | Description  
---|---|---|---  
Event ID | String | Yes | Specify a comma-separated list of IDs or UUIDs of the events for which you want retrieve details.  
Return Attributes Info | Checkbox | Checked | If enabled, action will create a case wall table for all of the attributes that are a part of the event.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If action completed successfully for at least one of the provided ids:_ Print "Successfully retrieved information for the following events: <>"_If action failed to run for at least one of the provided incident ids:_ Print "Failed to retrieved information for the following events: <>******The action should fail and stop a playbook execution:**  
_if fatal error, SDK error, like wrong credentials, no connection, other:_  
_P_ rint "Error executing action "Get Event Details". Reason: {0}''.format(error.Stacktrace  
****  
******The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ **** print "Error executing action "List Event Objects". Reason: {0}''.format(error.Stacktrace) | General  
CSV Table | **Table Name:** Event {0} Attributes Details".format(event_id)**Columns:**

  1. ID 
  2. Value 
  3. Comment 
  4. Type
  5. Category 
  6. UUID 
  7. Distribution 
  8. Timestamp 

|   
  
### List Sightings of an Attribute

List available sightings for attributes in MISP.

#### Parameters

Parameter Name | Type | Default Value | Mandatory | Description  
---|---|---|---|---  
Attribute Name | CSV |  | No | Specify a comma-separated list of attribute identifiers for which you want to list sightings. Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
Event ID | String |  | No | Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if "Attribute Search" is set to "Provided Event".  
search Category | CSV |  | No | Specify a comma-separated list of categories. If specified, action will only list sightings for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Type | CSV |  | No | Specify a comma-separated list of attribute types. If specified, action will only list sightings for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst  
Attribute Search | DDL | Provided EventPossible values:All Events | Yes | Specify, where action should search for attributes. If "Provided Event" is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in "Event ID" parameter. If "All Events", action will search for attributes among all events and list sightings for all attributes that match our criteria.  
Attribute UUID | CSV |  | No | Specify a comma-separated list of attribute UUIDs for which you want to list sightings. Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
  
##### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **If successfully listed sightings to at least one attribute:** "Successfully listed sightings for the following attributes in MISP:\n{0}".format(attribute name/attribute UUID)**if not successfully listed sightings for at least one attribute:** "Action didn't list sightings for the following attributes in MISP:\n{0}".format(attribute name/attribute UUID)**If not successful for all or no sightings for all attributes:** "No sightings were found for the provided attributes in MISP"**Critical Error (fail action)** __"Error executing action "List Sightings of an Attribute". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Category" (fail action):** "Error executing action "List Sightings of an Attribute". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If "Provided Event" is selected, but Event ID is not selected:** "Error executing action "List Sightings of an Attribute". Reason: Event ID needs to be provided, if "Provided Event" is selected for the parameter "Attribute Search"". | General  
  
### Set IDS Flag for an Attribute

Set IDS flag for attributes in MISP.

#### Parameters

Parameter Name | Type | Default Value | Mandatory | Description  
---|---|---|---|---  
searchsearch Attribute Name | CSV |  | No | Specify a comma-separated list of attribute identifiers for which you want to set an IDS flag. Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
Event ID | String |  | No | Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if "Attribute Search" is set to "Provided Event".  
Category | CSV |  | No | Specify a comma-separated list of categories. If specified, action will only set IDS flag for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Type | CSV |  | No | Specify a comma-separated list of attribute types. If specified, action will only set IDS flag for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst  
Attribute Search | DDL | Provided EventPossible values:All Events | Yes | Specify, where action should search for attributes. If "Provided Event" is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in "Event ID" parameter. If "All Events", action will search for attributes among all events and set IDS flag for all attributes that match our criteria.  
Attribute UUID | CSV |  | No | Specify a comma-separated list of attribute UUIDs for which you want to set an IDS flag.   
Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
  
#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If successfully added IDS flag to at least one attribute:** "Successfully set IDS flag for the following attributes in MISP:\n{0}".format(attribute name/object UUID)**if not successfully added IDS flag to at least one attribute:** "Action didn't set IDS flag for the following attributes in MISP:\n{0}".format(attribute name/object UUID)**If not successful for all:** "IDS flag was not set for the provided attributes in MISP"**Critical Error (fail action)** "Error executing action "Set IDS Flag for an Attribute". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Category" (fail action):** "Error executing action "Set IDS Flag for an Attribute". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If "Provided Event" is selected, but Event ID is not selected:** "Error executing action "Set IDS Flag for an Attribute". Reason: Event ID needs to be provided, if "Provided Event" is selected for the parameter "Attribute Search"".**Event ID is not found (fail action)** "Error executing action "Set IDS Flag for an Attribute". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
### Unset IDS Flag for an Attribute

Unset IDS flag for attributes in MISP.

#### Parameters

Name | Type | Default Value | Mandatory | Description  
---|---|---|---|---  
Attribute Name | CSV |  | No | Specify a comma-separated list of attribute identifiers for which you want to unset an IDS flag.   
Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
Event ID | String |  | No | Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if "Attribute Search" is set to "Provided Event".  
Category | CSV |  | No | Specify a comma-separated list of categories. If specified, action will only unset IDS flag for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.  
Type | CSV |  | No | Specify a comma-separated list of attribute types. If specified, action will only unset IDS flag for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst  
Attribute Search | DDL | Provided EventPossible values:All Events | True | Specify, where action should search for attributes. If "Provided Event" is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in "Event ID" parameter. If "All Events", action will search for attributes among all events and unset IDS flag for all attributes that match our criteria.  
Attribute UUID | CSV |  | No | Specify a comma-separated list of attribute UUIDs for which you want to unset an IDS flag. Note: If both "Attribute Name" and "Attribute UUID" are specified, action will work with "Attribute UUID" values.  
  
#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### Case Wall

Result Type | Value Description | Type  
---|---|---  
Output message* | **If successfully removed IDS flag to at least one attribute:** "Successfully unset IDS flag for the following attributes in MISP:\n{0}".format(attribute name/object UUID)**if not successfully removed IDS flag to at least one attribute:** "Action didn't unset IDS flag for the following attributes in MISP:\n{0}".format(attribute name/object UUID)**If not successful for all:** "IDS flag was not unset for the provided attributes in MISP"**Critical Error (fail action)** "Error executing action "Unset IDS Flag for an Attribute". Reason: {0}".format(stacktrace)**If invalid parameter is specified in "Category" (fail action):** "Error executing action "Unset IDS Flag for an Attribute". Reason: Invalid value was provided for the parameter "Category". Acceptable values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation".**If "Provided Event" is selected, but Event ID is not selected:** "Error executing action "Unset IDS Flag for an Attribute". Reason: Event ID needs to be provided, if "Provided Event" is selected for the parameter "Attribute Search"".**Event ID is not found (fail action)** "Error executing action "Unset IDS Flag for an Attribute". Reason: Event with {0} {1} was not found in MISP".format(ID/UUID, event_id) | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

## MISP - Attributes Connector

Pull attributes from MISP.

#### Configure MISP - Attributes Connector on Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Param Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
DeviceProductField | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
EventClassId | String | alertType | Yes | Enter the source field name in order to retrieve the Event Field name.  
PythonProcessTimeout | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | N/A | Yes | API Root for MISP account.  
API Key | Password |  | Yes | API Key of the MISP account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch attributes.  
Max Attributes Per Cycle | Integer | 50 | Yes | How many attributes to process per one connector iteration.  
Lowest Threat Level To Fetch | Integer | 1 | Yes | Lowest severity that will be used to fetch alerts. Possible values: 1-4.  
Attribute Type Filter | String |  | No | Filter attributes by their type, comma separated. If provided, only attributes with whitelisted type will be processed.  
Category Filter | String |  | No | Filter attributes by their category, comma separated. If provided, only attributes with whitelisted category will be processed.  
Galaxy Filter | String |  | No | Filter attributes by their parent event's galaxy, comma separated. If provided, only attributes that belong to an event with a whitelisted galaxy will be processed.  
Verify SSL | Checkbox |  | Yes | If enabled, verify the SSL certificate for the connection to the CheckPoint Cloud Guard server is valid.  
Environment Field Name | String |  | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the \"Environment Field Name\" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
