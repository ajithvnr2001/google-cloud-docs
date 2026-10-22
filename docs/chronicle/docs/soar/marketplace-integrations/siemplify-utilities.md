---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify-utilities/
title: Integrate SiemplifyUtilities with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:46.565474+00:00
---

# Integrate SiemplifyUtilities with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify-utilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate SiemplifyUtilities with Google SecOps

This document explains how to integrate SiemplifyUtilities with Google Security Operations (Google SecOps).

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/SiemplifyUtilities.zip).

## Use cases

The **SiemplifyUtilities** integration can address the following use cases:

  * **Export and sharing** : Use Google SecOps capabilities with the **Export Entities as OpenIOC File** action to quickly generate standardized **OpenIOC files** from security entities (such as IPs, Filehashes, or URLs) and share them with threat intelligence platforms or other security teams.

  * **List manipulation for logic** : Use Google SecOps capabilities with the **List Operations** action to perform complex logic operations (such as **intersection** , **union** , **subtract**) on two different lists of values within a Playbook, providing advanced filtering or combining of data sources.

  * **Data Transformation and Analysis** : Use Google SecOps capabilities with the **Extract top From JSON** action to process and prioritize large, nested JSON datasets by sorting them based on a specific nested key (like a severity score) and returning only the top relevant results for immediate analysis.

  * **Email Forensics** : Use Google SecOps capabilities with the **Parse EML to JSON** action to convert raw, base64-encoded email messages (EML or MSG files) into a structured JSON format, making the email's headers, body, attachments, and links accessible for automated parsing and investigation.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

None.

For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Count Entities in Scope

Use the **Count Entities in Scope** to retrieve the number of entities in a specific scope.

This action runs on all Google SecOps entities.

#### Action inputs

The **Count Entities in Scope** action requires the following parameters:

Parameter | Description  
---|---  
`Entity Type` | Required. The type of the target entities.  
  
#### Action outputs

The **Count Entities in Scope** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Count Entities in Scope** action can return the following output messages:

Output message | Message description  
---|---  
`There are NUMBER_OF_ENTITIES entities from ENTITY_TYPE type.` | The action succeeded.  
`Error executing action "Count Entities in Scope". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Count Entities in Scope** action:

Script result name | Value  
---|---  
`list_count` | `NUMBER_OF_ENTITIES`  
  
### Count List

Use the **Count List** action to retrieve the number of items on a list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Count List** action requires the following parameters:

Parameter | Description  
---|---  
`Input String` | Optional. A comma-separated list of strings, such as `value1,value2,value3`.  
`Delimiter` | Optional. The symbol used to separate individual values within the `Input String`.  
  
#### Action outputs

The **Count List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Count List** action can return the following output messages:

Output message | Message description  
---|---  
`List length is: NUMBER_OF_ENTITIES` | The action succeeded.  
`Error executing action "Count List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Count List** action:

Script result name | Value  
---|---  
`list_count` | `NUMBER_OF_ENTITIES`  
  
### Delete File

Use the **Delete File** action to delete a selected file from the file system.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete File** action requires the following parameters:

Parameter | Description  
---|---  
`File Path` | Required. The absolute path of the file to delete.  
  
#### Action outputs

The **Delete File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Delete File** action:
    
    
    {
    "filepath": ""
    "status": "deleted/not found"
    }
    

##### Output messages

The **Delete File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted file.` | The action succeeded.  
`Error executing action "Delete File". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete File** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Export Entities as OpenIOC File

Use the **Export Entities as OpenIOC File** action to package supported security artifacts from the current case into a standard OpenIOC file format. This file can be used for sharing, threat intelligence, or importing into other security tools.

This action runs on the following Google SecOps entities:

  * `Filehash`

  * `IP Address`

  * `URL`

  * `Hostname`

  * `User`




#### Action inputs

The **Export Entities as OpenIOC File** action requires the following parameters:

Parameter | Description  
---|---  
`Export Folder Path` | Required. The local path of the folder where the generated OpenIOC file will be saved.  
  
#### Action outputs

The **Export Entities as OpenIOC File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Export Entities as OpenIOC File** action:
    
    
    {
        "absolute_file_path": OpenIOC_{random_guid}.txt
    }
    

##### Output messages

The **Export Entities as OpenIOC File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created an OpenIOC file based on provided entities.` `Action wasn't able to create an OpenIOC file, because there are no entities in the action execution scope.` | The action succeeded.  
`Error executing action "Export Entities as OpenIOC File". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
### Extract top From JSON

Use the **Extract top From JSON** action to sort an input JSON by a specific key and return the top-ranked branches or records.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Extract top From JSON** action requires the following parameters:

Parameter | Description  
---|---  
`JSON Data` | Required. The JSON data to process.  
`Key To Sort By` | Required. The nested key used for sorting, with segments separated by dots. Use `*` as a wildcard. For example, `Host.*.wassap_list.Severity`.  
`Field Type` | Required. The data type of the key specified for sorting. The possible values are as follows:

  * `int`
  * `string`
  * `Date`

  
`Reverse (DESC -> ASC)` | Optional. If selected, the sort order is **Descending**. If not selected, the sort order is **Ascending**. Enabled by default.  
`Top Rows` | Optional. The number of top records (rows) to retrieve from the sorted JSON output.  
  
#### Action outputs

The **Extract top From JSON** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Extract top From JSON** action:
    
    
    [
        {
            "HOST": {
                "DETECTION":{
                    "QID": "82003",
                    "SEVERITY": "1",
                    "RESULTS": "Timestamp of host (network byte ordering): 03:40:14 GMT"
                },
                "IP": "1.1.1.1",
                "LAST_SCAN_DATETIME": "2018-08-13T10:24:35Z",
                "OS": "Windows 10"
            },
            "DATETIME": "2018-08-29T14:01:12Z"
        }, {
            "HOST":{
                "DETECTION": {
                    "PORT": "443",
                    "QID": "11827",
                    "PROTOCOL": "tcp",
                    "RESULTS": "X-Frame-Options or Content-Security-Policy: frame-ancestors HTTP Headers missing on port 443.",
                    "SEVERITY": "2"
                },
                "IP": "1.1.1.1",
                "LAST_SCAN_DATETIME": "2018-08-13T08:31:58Z",
                "OS": "Linux 3.13"
            },
            "DATETIME": "2018-08-29T14:01:12Z"
        }, {
            "HOST": {
                "DETECTION": {
                    "PORT": "53",
                    "QID": "15033",
                    "PROTOCOL": "udp",
                    "RESULTS": "--- IPv4 --- ",
                    "SEVERITY": "4"
                },
                "IP": "1.1.1.1",
                "LAST_SCAN_DATETIME": "2018-08-13T08:31:58Z",
                "OS": "Linux 3.13"
            },
            "DATETIME": "2018-08-29T14:01:12Z"
        }
    ]
    

##### Output messages

The **Extract top From JSON** action can return the following output messages:

Output message | Message description  
---|---  
`Results: RESULTS.` `No branches were found.` | The action succeeded.  
`Error executing action "Extract top From JSON". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Extract top From JSON** action:

Script result name | Value  
---|---  
`result` | `RESULTS`  
  
### Filter JSON

Use the **Filter JSON** action to filter a JSON object based on a specified condition and extract specific results.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Filter JSON** action requires the following parameters:

Parameter | Description  
---|---  
`JSON Data` | Required. The JSON dictionary data to apply the filter to.  
`Root Key Path` | Optional. The dot-separated starting path for the JSON search.  
`Condition Path` | Required. The dot-separated path to the field whose value is evaluated against the `filter` condition.  
`Condition Operator` | Required. The comparison operator to use in the condition. The possible values are as follows:

  * `=`
  * `!=`
  * `>`
  * `<`
  * `>=`
  * `<=`
  * `in`
  * `not in`

  
`Condition Value` | Required. The specific value to use in the `filter` condition.  
`Output Path` | Optional. The dot-separated path to the specific data elements to return from the filtered JSON.  
`Delimiter` | Optional. The character used to join the output values if multiple elements are returned. The default value is `,`.  
  
#### Action outputs

The **Filter JSON** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Filter JSON** action:
    
    
    {
        "a": {
            "HOST": [
                {
                    "DETECTION": {
                        "QID": "82003",
                        "SEVERITY": "1",
                        "RESULTS": "Timestamp of host (network byte ordering): 03:40:14 GMT"
                    },
                    "IP": "1.1.1.1",
                    "LAST_SCAN_DATETIME": "2018-08-13T10:24:35Z",
                    "OS": "Windows 10"
                }
            ],
            "DATETIME": "2018-08-29T14:01:12Z"
        }
    }
    

##### Output messages

The **Filter JSON** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully filtered JSON.` | The action succeeded.  
`Error executing action "Filter JSON". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Filter JSON** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Deployment URL

Use the **Get Deployment URL** action to retrieve the deployment URL for your current Google SecOps instance.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Get Deployment URL** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Get Deployment URL** action:
    
    
    {
    "url": ""
    }
    

##### Output messages

The **Get Deployment URL** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved deployment URL.` | The action succeeded.  
`Error executing action "Get Deployment URL". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Deployment URL** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Operations

Use the **List Operations** action to perform set operations between two provided comma-separated lists.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Operations** action requires the following parameters:

Parameter | Description  
---|---  
`First List` | Required. The first list of comma-separated values for the `set` operation.  
`Second List` | Required. The second list of comma-separated values for the `set` operation.  
`Delimiter` | Optional. The symbol or character used to separate values in both the `First List` and `Second List`. The default value is `,`.  
`Operator` | Required. The type of `set` operation to perform. The possible values are as follows:

  * `intersection`
  * `union`
  * `subtract`
  * `xor` (exclusive OR).

  
  
#### Action outputs

The **List Operations** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **List Operations** action:
    
    
    {
        "results": {
            "count": 6,
            "data": [
                "item",
                "item1",
                "item2"
            ]
        }
    }​​
    

##### Script result

The following table lists the value for the script result output when using the **List Operations** action:

Script result name | Value  
---|---  
`result_list` | `RESULTS`  
  
### Parse EML to JSON

Use the **Parse EML to JSON** action to convert the content of an EML or MSG email file into a structured JSON object within Google SecOps.

**Note:** This action supports parsing both EML and MSG file types. If the file contains attachments, the action supports attachments only within EML files.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Parse EML to JSON** action requires the following parameters:

Parameter | Description  
---|---  
`EML Content` | Required. The base64-encoded content of the EML or MSG file.  
`Blacklisted Headers` | Optional. A comma-separated list of headers to exclude from the final JSON output.  
`Use Blacklist As Whitelist` | Optional. If selected, the list provided in `Blacklisted Headers` acts as a whitelist, including only those listed headers in the JSON output.  
  
#### Action outputs

The **Parse EML to JSON** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Parse EML to JSON** action:
    
    
    {
        "HTML Body": "<div><br></div>",
        "Attachments": {},
        "Recipients": "john_doe@example.com",
        "CC": "",
        "Links": {
            "urls_1": "https://lh4.googleusercontent.com/rE6-WYjfFuiHbHUV33G31NCtUeBl9YGnw4bvlorqMeNaC60qWagqtohFwCpq2eJxlMYMJPPDAqqXRZW6Oja8GqOjt3jB3aB6tzJP-jdtbCBoj-m3vu49tttHmWpXGJUSI6UuTUYS",
            "urls_2": "https://lh4.googleusercontent.com/Uih5TalWnJjBbG_QaRICp8emX5wIakbCmstEDP3YHT7l45qdjIllcxg_Ddapvrh5DqGKszK3KKM5M0kEoC1YX6TgbWKJKPX0OxD5BeWr3uu6SRAHs7lwP20khjHSlxsIM46egQ-M"
        },
        "BCC": "",
        "To": "john_doe@example.com",
        "Date": "Mon, 13 Aug 2018 13:20:34 +0300",
        "From": "john_doe@example.com",
        "Subject": "TEST6:::Test:::ADVANCE NOTICE: 07.08.2018-Disable Accounts-user\\\r\\\\n Office Il Office"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Parse EML To JSON** action:

Script result name | Value  
---|---  
`parsed_eml` | `RESULTS`  
  
The action's JSON output for the `with` field is restructured to separate the ID value into a dedicated field. This change applies to version 10 and later of the integration as described in the following table: 

Integration Version | Field Structure and Description | Example JSON  
---|---|---  
**Version 9 and earlier** | The ID and the protocol are combined into the `with` field. | `{"with": "smtp id ID"}`  
**Version 10 and later** | The ID is stored in the new `id` field, and the `with` field contains only the protocol. | `{"id": "ID", "with": "SMTP"}`  
**Note:** If your existing playbooks use the output of the `Parse EML to JSON` action, you must update the playbook logic. Reference the new `id` field instead of parsing the ID from the `with` field

### Ping

Use the **Ping** action to test the connectivity to SiemplifyUtilities.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Connection Established.` | The action succeeded.  
`Failed to connect to SiemplifyUtilities. Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Query Joiner

Use the **Query Joiner** action to dynamically construct a structured query string by combining a list of search values, a target field, and a logical operator.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Query Joiner** action requires the following parameters:

Parameter | Description  
---|---  
`Values` |  **Required.** A comma-separated list of values to search for, such as `value1,value2,value3`.  
`Query Field` |  **Required.** The target field name to search in, such as `SrcIP`, `DestHost`, or `UserName`.  
`Query Operator` |  **Required.** The logical operator that combines the values, such as `AND` or `OR`.  
`Add Quotes` |  Optional. If selected, the action adds single quotes (`'`) around each item in `Values`.  
`Add Double Quotes` |  Optional. If selected, the action adds double quotes (`"`) around each item in `Values`.  
`Add Backticks` |  Optional. If selected, the action adds backticks (```) around each item in `Values`. This is useful for escaping complex strings or special characters (such as long URLs), to prevent query compilation errors.  
`Delimiter` |  Optional. The character that separates the items in `Values`. If no value is provided, the default delimiter is a comma (`,`).  
  
#### Action outputs

The **Query Joiner** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Query Joiner** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully formed query: QUERY_FIELD= VALUE_1 OPERATOR QUERY_FIELD= VALUE_2 OPERATOR QUERY_FIELD= VALUE_3` | The action succeeded.  
`Error executing action "Query Joiner". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Query Joiner** action:

Script result name | Value  
---|---  
`query` | `QUERY_FIELD= VALUE_1 OPERATOR QUERY_FIELD= VALUE_2 OPERATOR QUERY_FIELD= VALUE_3`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
