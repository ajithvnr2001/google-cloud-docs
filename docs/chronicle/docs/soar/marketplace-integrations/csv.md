---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/csv/
title: Integrate CSV with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:45.924549+00:00
---

# Integrate CSV with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/csv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate CSV with Google SecOps

This document describes how to integrate CSV with Google Security Operations.

This document explains how to integrate CSV with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/CSV.zip).

## Use cases

In Google SecOps, the **CSV** integration supports the following use cases:

  * **File-based threat hunting** : Rapidly search through local or remote CSV log files for specific strings or malicious entities to identify historically logged threats.

  * **Automated alert generation** : Automatically ingest records from legacy systems that output data in CSV format, converting them into actionable alerts with custom severity mapping.

  * **Data portability and reporting** : Programmatically transform JSON results from other playbook actions into CSV format for streamlined export to external reporting tools or local storage.

  * **Automated entity enrichment** : Use CSV files as a local threat intelligence source to automatically enrich entities and mark them as suspicious during playbook execution.

  * **Cross-system data synchronization** : Efficiently process files with varied character encodings, such as legacy Excel formats, to ensure data consistency across disparate security tools.




## Before you begin

Before you configure the integration in Google SecOps, verify that you have the following:

  * **Internal platform capabilities** : This integration provides built-in file processing capabilities and doesn't require external third-party API keys or credentials for authentication.

  * **File system permissions** : If a Remote Agent is used, the integration requires specific permissions to access and manage files on the host system. Run the following command on the agent machine to grant the necessary permissions for your target directory: `chown scripting:scripting "directory_path"`

**Note:** Use of a Remote Agent is optional. If you aren't using a Remote Agent, file system permission configuration isn't required.



### Integration parameters

The **CSV** integration requires the following parameters:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Save JSON to CSV

Save a JSON object to CSV.

**Note:** This action is only recommended for use with **Remote Agents** to ensure the generated file is saved to an expected and accessible location.

#### Parameters

Parameter name | Type | Default value | Mandatory | Description  
---|---|---|---|---  
JSON Object | JSON | N/A | Yes | Specifies the JSON object to save as CSV.  
Overwrite | Boolean | False | No | If enabled, the action overwrites the existing file.  
File Path | String | N/A | Yes | Specifies the absolute file path for the newly created CSV file. If only the filename is provided, the action stores the file in a `/tmp/` folder.  
  
#### Run On

N/A

#### Action Results

##### Script Result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {"filepath": "{file name}"}
    

##### Case Wall

The action provides the following output messages:

Output message | Message description  
---|---  
Successfully transformed the JSON object and saved it to the provided file path. | Action is successful.  
File wasn't found for the provided path. | The file does not exist.  
No activity was found for the provided service accounts in Google Cloud Policy Intelligence | The action could not find data for any of the listed service accounts.   
Error executing action "Save JSON To CSV". | The action returned an error.Check connection to the server, input parameters, or credentials.  
  
### Search by String

Search for strings in CSV files.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
CSV Path | String | N/A | Yes | Specify the file path to the CSV file or a folder path that contains all of the CSV files. If folder is provide, action will iterate over all CSV files in the folder.  
CSV Column | String | N/A | No | Specify a comma-separated list of columns that can contain entity information. If nothing is provided, action will search in all of the columns.  
Days Backwards | String | 10 | No | Specify how many days backwards to process the CSV files.  
Search Value | String | N/A | No | Specify a string that needs to be searched. If "Search Multiple String" is enabled, this parameter is treated as a comma-separated list of strings that need to be searched.  
Return the first row only. | Checkbox | Unchecked | No | If enabled, action will only return 1 row in the first file that matched the entity.  
File Encoding Types | String | utf-8, latin-1, iso-8859-1 | Yes | A comma separated list CSV encoding types used for decoding your CSV files, e.g. utf-8, latin-1, iso-8859-1, utf-16... Order in which the encoding types are given sets the order in which they are used for decoding files, e.g.(from example above) the utf-8 has the highest priority and will be used primarily for decoding all the files, if there is a CSV file that uses some other encoding then the next in the order: latin-1 encoding will be used, and so on, until the last encoding is used.  
Search Multiple String | Checkbox | Unchecked | No | If enabled, "Search Value" will work as a comma-separated list of values, instead of a single string.  
Fields To Return | CSV | N/A | No | Specify a comma-separated list of values that need to be returned.  
  
#### Use cases

Search for strings in CSV files.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
count_rows_csv | Any number of rows | count_rows += 1  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "Field2": "Value2",
                "Field3": "Value3",
                "Field1": "Value1",
                "Field4": "Value4",
                "Field5": "Value5"
            },
            "Entity": "host"
        }, {
            "EntityResult": {
                "Field2": "Value2",
                "Field3": "Value3",
                "Field1": "Value1",
                "Field4": "Value4",
                "Field5": "Value5"
            }, "Entity": "1.1.1.1"
        }
    ]
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _For records that are found:_ **"** Successfully found information about the following strings: \n (search_string)"___If no records are found for some strings: "_ Action wasn't able to find information about the following strings:"___If no success for every records: "_ No information was found for the provided items."_If all encodings are invalid:_ **"** Error executing action "CSV Search by String". Provided encodings are invalid. Please check the spelling." | General  
  
### Search by Entity

Search for entities in CSV files and enrich them.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
CSV Path | String | N/A | Yes | Specify the file path to the CSV file or a folder path that contains all of the CSV files. If folder is provide, action will iterate over all CSV files in the folder.  
CSV Column | String | N/A | Yes | Specify a comma-separated list of columns that can contain entity information. If nothing is provided, action will search in all of the columns.  
Days Back | String | 10 | Yes | Specify how many days backwards to process the CSV files.  
Mark As Suspicious | Checkbox | Unchecked | No | If enabled, action will mark entity as suspicious, if it was found in file.  
Return the first row only. | Checkbox | Unchecked | No | If enabled, action will only return 1 row in the first file that matched the entity.  
File Encoding Types | String | utf-8, latin-1, iso-8859-1 | Yes | A comma separated list CSV encoding types used for decoding your CSV files, e.g. utf-8, latin-1, iso-8859-1, utf-16... Order in which the encoding types are given sets the order in which they are used for decoding files, e.g.(from example above) the utf-8 has the highest priority and will be used primarily for decoding all the files, if there is a CSV file that uses some other encoding then the next in the order: latin-1 encoding will be used, and so on, until the last encoding is used.  
Enrich Entities | Checkbox | Checked | No | If enabled, action will add information from CSV file and add it to the enrichment table of entity.  
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight, if entity was found in the file.  
Fields To Return | CSV | N/A | No | Specify a comma-separated list of values that need to be returned.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
count_rows_csv | Any number of rows | count_rows += 1  
  
##### JSON result
    
    
    [
        {
            "EntityResult": [{
                "domain": "example.dom",
                "fileHash": "cbbc5aea3d4c7ec193aa2ff3b52df36ebb12338b18c9bb53fc4896115efaf78d",
                "reporter": "Symantec Antivirus",
                "app": "Arcsight",
                "id": "1011",
                "eventTime": "9/4/2017 10:00",
                "antivirusAction": "blocked",
                "virusName": "ECAT",
                "rule": "malicious",
                "eventName": "Virus detected",
                "User": "Ziv",
                "eventHostName": "WS-ZivDevComp",
                "File Source Path": "C:\\\\Users\\\\Default\\\\Desktop\\\\stringTimeRaw.csv",
                "machineAddress": "192.168.11.11"
            }, {
                "domain": "SmartCompany.dom",
                "fileHash": "cbbc5aea3d4c7ec193aa2ff3b52df36ebb12338b18c9bb53fc4896115efaf78d",
                "reporter": "Symantec Antivirus",
                "app": "ESM",
                "id": "1012",
                "eventTime": "9/4/2017 10:00",
                "antivirusAction": "allowed",
                "virusName": "ECAT",
                "rule": "malicious",
                "eventName": "Virus detected",
                "User": "GG",
                "eventHostName": "WS-GGDevComp",
                "File Source Path": "C:\\\\Users\\\\Default\\\\Desktop\\\\stringTimeRaw.csv",
                "machineAddress": "192.168.11.11"
            }],
            "Entity": "192.168.11.11"
        }
    ]
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _For entities that are found:_ **"** Successfully found information about the following entities: \n (entity.identifier)"_For entities that are not found:_ "No information was found about the following entities: \n (entity.identifier)"_If no success for every entity:_ "No information was found for the provided entities."_If all encodings are invalid:_ ****"Error executing action "CSV Search by String". Provided encodings are invalid. Please check the spelling." | General  
  
### Ping

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

N/A

##### JSON result
    
    
    N/A
    

## Connectors

### CSV Connector

Fetch data from CSV files located in a specific folder, and convert this data to alerts in Google SecOps system.

This topic illustrates the mechanism and configuration by which Google SecOps produces CSV files along with supported working flows and actions taken within the platform.

#### Use cases

**A customer has CSVs coming from a system, and the files could be from different encodings.**
    
    
    *   Add support for comma-separated encodings in the Encoding field in the
        connector.
        *   The connector should try the different encodings by their order in
            the field (first encoding - highest priority, last - lowest
            priority) with try/except. If no matching encoding was found -
            consider the file as an error and notify.
        *   Put a default value for the fields - a list of most common CSV
            encodings by priority (utf8, latin1, and iso...)
    

#### Access to CSV files

Google SecOps access to CSV files: setup a folder for the CSV files.

#### CSV Records Forwarding to Google SecOps

**Working with CSV files records**

When configuring Google SecOps to work with CSV files as an alert source, you will be requested to provide a specific folder where the CSVs will be fetched from. Google SecOps will retrieve any record within a CSV file and forward them to be translated, and contextualized as alerts for cases.

**How to map severity in the connector**

In order to map severity you need to specify what field should be used to get value for severity in the "Severity Field Name" parameter. In the response you can get 3 types of values: integers, floats and strings. For integers and floats, you don't need to do any additional configuration. The connector will read those values and map them according to the Google SecOps standards. A quick reminder of how integer values are mapped:

  * 100 - Critical
  * 100 > x >= 80 High
  * 80 > x >=60 Medium
  * 60 > x >=40 Low
  * 40 > x Informational



If in the response, we are working with strings then additional configuration is required. In the folder, where connector scripts are located you will have a config file name severity_map_config.json. This file defines mapping rules for the severity.

Initially, the file will look like this: `1 2 3` `{ "Default": 50 }`

Imagine a situation, where the needed values are located in the event.severity. event.severity can contain the following values: "Malicious", "Benign", "Unknown".

First, we have to specify in the "Severity Field Name" parameter that we will use event.severity. Secondly, we have to update the config file. After changes, this is how severity_map_config.json file should look like: `1 2 3 4 5 6 7 8` `{ "event.severity": { "Malicious": 100, "Unknown": 60, "Benign": -1 }, "Default": 50 }`

Now, when the connector will get an event with `event.severity` = "Malicious" it will give it Critical severity.

#### Configure CSV Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | device_product | Yes | The field name used to determine the device product.  
Event Field Name | String | name | No | The field name used to determine the event name (sub-type).  
Script Timeout (Seconds) | String | 60 | Yes | The timeout limit (in seconds) for the python process running current script.  
CSV Folder Path | String | N/A | Yes | Folder path that contains all of the csv files that need to be ingested.  
CSV Limit | String | N/A | No | How many CSV files to process per one iteration.  
Rule Generator Field Name | String | N/A | No | Name of the field that contains information about the rule generator.  
Time Field Name | String | N/A | No | Name of the field that contains information about the event time.  
CSV Has Header | Checkbox | Checked | Yes | Indicates whether the csv file has header.  
File Encoding Type | String | utf-8 | Yes | Set the CSV encoding type, e.g. iso-8859-1, latin1, utf-8, utf-16.  
Alert Field Name | String | N/A | No | Name of the field that contains information about alert name.  
Severity Field Name | String | N/A | No | Name of the field that contains information about severity.   
**Note:** you can map severity based on the values in the response. For that you need to go to the connector execution folder and modify severity_mapping_config.json. Check documentation for reference.  
**Note:** Character encoding is the way that presents characters in a saved file. The Universal Standard is Unicode (or utf-8), however, some files might be encoded in a legacy format (e.g. old versions of Excel), which would require manual setting of the encoding. Some encodings can overlap, so there is a chance to read a csv in a wrong encoding. Therefore, encodings cannot be guessed 100% correctly.

#### Connector Rules

##### Proxy Support

The connector doesn't support Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
