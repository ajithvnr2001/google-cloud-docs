---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify/
title: Integrate Siemplify with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:37.261019+00:00
---

# Integrate Siemplify with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Siemplify with Google SecOps 

This document explains how to integrate Siemplify with Google Security Operations (Google SecOps). 

## Use cases

The **Siemplify** integration can address the following use cases:

  * **Phishing investigation** : Use Google SecOps capabilities to automate the process of analyzing phishing emails, extracting indicators of compromise (IOCs), and enriching them with threat intelligence.

  * **Malware containment** : Use Google SecOps capabilities to automatically isolate infected endpoints, initiate scans, and quarantine malicious files upon detection of malware.

  * **Vulnerability management** : Use Google SecOps capabilities to orchestrate vulnerability scans, prioritize vulnerabilities based on risk, and automatically create tickets for remediation.

  * **Threat hunting** : Use Google SecOps capabilities to automate running of threat hunting queries across various security tools and datasets.

  * **Security alert triage** : Use Google SecOps capabilities to automatically enrich security alerts with contextual information, correlate them with other events, and prioritize them based on severity.

  * **Incident response** : Use Google SecOps capabilities to orchestrate the entire incident response process, from initial detection to containment and eradication.

  * **Compliance reporting** : Use Google SecOps capabilities to automate the collection and analysis of security data for compliance reporting.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

The **Siemplify** integration requires the following parameters:

Parameter | Description  
---|---  
`Monitors Mail Recipients` | Required. A comma-separated list of email addresses for validation in the integration's email-related workflows. This list is used to define the recipients for processing. The default value is `example@mail.com,example1@mail.com`.  
`Elastic Server Address` | Required. The address of the Elastic server used to connect to the Siemplify database. This is typically the address of the host machine where the Elastic instance runs. The default value is `localhost`.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Entity Insight

Use the **Add Entity Insight** action to add an insight to a Google SecOps entity in Siemplify.

This action runs on all Google SecOps entities.

#### Action inputs

The **Add Entity Insight** action requires the following parameters:

Parameter | Description  
---|---  
`Message` | Required. The message to add to the entity. This parameter supports HTML elements, such as:

  * Headings (`<h1>``</h1>`, `<h2>``</h2>`)
  * Paragraphs (`<p>``</p>`)
  * Text formatting (`<b>``</b>`, `<i>``</i>`, `<br>`)
  * Links (`<a href="example.com">``</a>`).

  
  
#### Action outputs

The **Add Entity Insight** action provides the following outputs:

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

The **Add Entity Insight** action can return the following output messages:

Output message | Message description  
---|---  
`Added insight with message MESSAGE to ENTITY_ID.` | The action succeeded.  
`Error executing action "Add Entity Insight". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Entity Insight** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add General Insight

Use the **Add General Insight** action to add a general insight to the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add General Insight** action requires the following parameters:

Parameter | Description  
---|---  
`Title` | Required. The title of the insight.  
`Message` | Required. The message to add to the entity. This parameter supports HTML elements, such as:

  * Headings (`<h1>``</h1>`, `<h2>``</h2>`)
  * Paragraphs (`<p>``</p>`)
  * Text formatting (`<b>``</b>`, `<i>``</i>`, `<br>`)
  * Links (`<a href="example.com">``</a>`).

  
`Triggered By` | Optional. A free-text field to provide a justification for the insight, explaining why it was added to the case.  
  
#### Action outputs

The **Add General Insight** action provides the following outputs:

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

The **Add General Insight** action can return the following output messages:

Output message | Message description  
---|---  
`Added insight with message MESSAGE.` | The action succeeded.  
`Error executing action "Add General Insight". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add General Insight** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Tags To Similar Cases

Use the **Add Tags To Similar Cases** action to add tags to similar cases.

To find similar cases, the action uses the `siemplify.get_similar_cases()` function to retrieve a list of case IDs based on a set of criteria and parameters.

The logical `AND` operator is applied to the `Rule Generator`, `Port`, `Category Outcome`, and `Entity Identifier` parameters to filter for cases that match all specified criteria.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Tags To Similar Cases** action requires the following parameters:

Parameter | Description  
---|---  
`Rule Generator` | Optional. If selected, the action searches for similar cases using the rule generator. Enabled by default.  
`Port` | Optional. If selected, the action searches for similar cases using port numbers. Enabled by default.  
`Category Outcome` | Optional. If selected, the action searches for similar cases using the category outcome. Enabled by default.  
`Entity Identifier` | Optional. If selected, the action searches for similar cases using the entity identifier. Enabled by default.  
`Days Back` | Required. The number of days prior to the current date to search through for similar cases.  
`Tags` | Required. A comma-separated list of tags to apply to the similar cases found.  
  
#### Action outputs

The **Add Tags To Similar Cases** action provides the following outputs:

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

The **Add Tags To Similar Cases** action can return the following output messages:

Output message | Message description  
---|---  
`Found NUMBER_OF_SIMILAR_CASES similar cases. **Successfully added tags: TAG_NAMES to cases CASE_IDS**` | The action succeeded.  
`Error executing action "Add Tags To Similar Cases". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Tags To Similar Cases** action:

Script result name | Value  
---|---  
`SimilarCasesIds` | A list of similar case IDs.  
  
### Add to Custom List

Use the **Add to Custom List** action to add an entity identifier to a categorized custom list and perform future comparisons in other actions.

This action runs on all Google SecOps entities.

#### Action inputs

The **Add to Custom List** action requires the following parameters:

Parameter | Description  
---|---  
`Category` | Required. The name of the custom list category to add the entity identifier to.  
  
#### Action outputs

The **Add to Custom List** action provides the following outputs:

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

The **Add to Custom List** action can return the following output messages:

Output message | Message description  
---|---  
`The alert's entities ENTITY_IDS were added to custom list category: CATEGORY.` | The action succeeded.  
`Error executing action "Add to Custom List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add to Custom List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Assign Case

Use the **Assign Case** action to assign the case to a specific user or user group.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Assign Case** action requires the following parameters:

Parameter | Description  
---|---  
`Assigned User` | Optional. The user or user group to assign the case to (accepts a `User` object). If both `Assigned User` and `Assignee` are provided, the action uses `Assigned User`.  
`Assignee` | Optional. The user or user group to assign the case to (accepts a string value). If both `Assigned User` and `Assignee` are provided, the action uses `Assigned User`.  
`Case ID` | Optional. A comma-separated list of case IDs to update. If no value is provided, the action updates the case from which it is executed.  
  
#### Action outputs

The **Assign Case** action provides the following outputs:

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

The **Add to Custom List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated case CASE_ID.` | The action succeeded.  
`Error executing action "Assign Case". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Assign Case** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Attach Playbook to Alert

Use the **Attach Playbook to Alert** action to attach a specific playbook to the alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Attach Playbook to Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Playbook Name` | Required. The name of the playbook to attach to the current alert. The playbook needs to be enabled for the action to succeed.  
`Allow Duplicates` | Optional. If selected, the playbook can be attached to the alert more than once. Enabled by default.  
  
#### Action outputs

The **Attach Playbook to Alert** action provides the following outputs:

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

The **Search Graphs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully attached the PLAYBOOK_NAME playbook to the alert CURRENT_ALERT_NAME.` | The action succeeded.  
`Error executing action "Attach Playbook to Alert". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Attach Playbook to Alert** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Attach Playbook to Case

Use the **Attach Playbook to Case** action to attach a playbook to the case in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Attach Playbook to Case** action requires the following parameters:

Parameter | Description  
---|---  
`Playbook Name` | Required. The name of the playbook to attach to the case.  
  
#### Action outputs

The **Attach Playbook to Case** action provides the following outputs:

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

The **Attach Playbook to Case** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully attached the PLAYBOOK_NAME playbook to the case.` | The action succeeded.  
`The PLAYBOOK_NAME playbook was already attached to the case.` | The action failed.The specified playbook does not exist in the platform.  
`Error executing action "Attach Playbook to Case". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or permissions.  
  
##### Script result

The following table lists the value for the script result output when using the **Attach Playbook to Case** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Case Comment

Use the **Case Comment** action to add a comment to the case in which the current alert is grouped.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Case Comment** action requires the following parameters:

Parameter | Description  
---|---  
`Comment` | Required. The comment to add to the case.  
  
#### Action outputs

The **Case Comment** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Comment added to case: **CASE_COMMENT.**` | The action succeeded.  
`Error executing action "Case Comment". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Case Comment** action:

Script result name | Value  
---|---  
`SuccessStatus` | `true` or `false`  
  
### Case Tag

Use the **Case Tag** action to add a tag to to the case in which the current alert is grouped.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Case Tag** action requires the following parameters:

Parameter | Description  
---|---  
`Tag` | Required. The tag to add to the case. If `Delimiter` is provided, the input splits based on the delimiter and multiple tags are added to the case.  
`Delimiter` | Optional. The delimiter to split the value of `Tag`. If no value is provided, the delimiter is not applied.  
  
#### Action outputs

The **Case Tag** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Case Tag** action:
    
    
    {
       "added_tags": ["123", "321"]
    }
    

##### Output messages

The **Case Tag** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added tags to the case CASE_ID.` | The action succeeded.  
`Error executing action "Add Vote To Entity". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Case Tag** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Change Alert Priority

Use the **Change Alert Priority** action to update the priority of an alert in a case.

This action doesn't run on Google SecOps entities. 

**Note:** In Google SecOps, the highest alert priority determines the case priority by default. 

For example, if the case priority is `Medium`, it means that at least one alert among all alerts that are grouped in the case has a `Medium` priority, while others have lower priorities, such as `Low` or `Informative`.

If you update the case priority to `Low`, Google SecOps overwrites the case priority to `Low`.

If you update the priority of an alert in a case to `High`, Google SecOps automatically sets the case priority to `High`.

#### Action inputs

The **Change Alert Priority** action requires the following parameters:

Parameter | Description  
---|---  
`Alert Priority` | Required. The new priority for the alert. If the alert priority is updated to be higher than the current case priority, the case's priority will automatically update to match the new, higher priority. The possible values are as follows:

  * `Informative`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

  
  
#### Action outputs

The **Change Alert Priority** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`The alert priority was set to NEW_PRIORITY_LEVEL.` | The action succeeded.  
`Error executing action "Change Alert Priority". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Change Alert Priority** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Change Case Stage

Use the **Change Case Stage** action to change the case stage.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Change Case Stage** action requires the following parameters:

Parameter | Description  
---|---  
`Stage` | Required. The stage to move the case to. The possible values are as follows:

  * `Triage`
  * `Assessment`
  * `Investigation`
  * `Incident`
  * `Improvement`
  * `Research`

  
  
#### Action outputs

The **Change Case Stage** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Case stage was successfully changed to NEW_CASE_STAGE.` | The action succeeded.  
`Error executing action "Change Case Stage". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Change Case Stage** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Change Priority

Use the **Change Priority** action to change the priority of the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Change Priority** action requires the following parameters:

Parameter | Description  
---|---  
`Priority` | Required. The priority to set for the case. The possible values are as follows:

  * `Informative`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

  
  
#### Action outputs

The **Change Priority** action provides the following outputs:

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

The **Change Priority** action can return the following output messages:

Output message | Message description  
---|---  
`The case priority was set to NEW_CASE_PRIORITY` | The action succeeded.  
`Error executing action "Change Priority". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Change Priority** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Close Alert

Use the **Close Alert** action to close the alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Close Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Reason` | Required. The primary classification for the alert closure. The possible values are as follows:

  * `Malicious`
  * `NotMalicious`
  * `Maintenance`
  * `Inconclusive`

  
`Root Cause` | Required. The detailed explanation of the technical issue that led to the alert.  
`Comment` | Required. The notes, summary of the investigation, or additional context for the alert closure.  
`Assign to User` | Optional. A user to assign the alert to after it's closure.  
`Tags` | Optional. A comma-separated list of tags to attach to the alert for classification, filtering, and future searchability.  
`Custom Fields` | Optional. A JSON object containing custom fields to update when the alert is closed.  
`Append Custom Field Values` | Optional. If selected, the action appends the provided JSON values to the existing custom fields. If not selected, the action overwrites the existing values with those provided in the JSON object. Disabled by default.  
  
#### Action outputs

The **Close Alert** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`The alert was closed. **Root Cause: ROOT_CAUSE **Comment: ALERT_COMMENT **Reason: REASON******` | The action succeeded.  
`Error executing action "Close Alert". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Close Alert** action:

Script result name | Value  
---|---  
`StatusResult` | `true` or `false`  
  
### Close Case

Use the **Close Case** action to close the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Close Case** action requires the following parameters:

Parameter | Description  
---|---  
`Reason` | Required. The primary classification for the alert closure. The possible values are as follows:

  * `Malicious`
  * `NotMalicious`
  * `Maintenance`
  * `Inconclusive`

  
`Root Cause` | Required. A detailed explanation of the technical issue that led to the alert.  
`Comment` | Required. The notes, summary of the investigation, or additional context for the alert closure.  
`Custom Fields` | Optional. A JSON object containing custom fields to update when the case is closed.  
`Append Custom Field Values` | Optional. If selected, the action appends the provided JSON values to the existing custom fields. If not selected, the action overwrites the existing values with those provided in the JSON object. Disabled by default.  
  
#### Action outputs

The **Close Case** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`The case was closed. **Root Cause: ROOT_CAUSE **Comment: REASON****` | The action succeeded.  
`Error executing action "Close Case". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Close Case** action:

Script result name | Value  
---|---  
`StatusResult` | `true` or `false`  
  
### Create Entity

Use the **Create Entity** action to create a new entity and add it to an alert.

This action runs on all Google SecOps entities.

**Note:** For the Google SecOps platform version 5.6.2 and later, you can choose the delimiter directly in the action's inputs and ignore the database configuration. 

For the Google SecOps platform version 5.6.0 up to 5.6.2, the delimiter can be configured in either the Create Entity action or the database.

To use a custom (non-default) delimiter, choose one of the following options:

  * Change the default delimiter (`,`) to your custom delimiter in both the action inputs and the database.
  * Change the delimiter in the database and keep the `Delimiter` parameter empty in this action.



#### Action inputs

The **Create Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Entities Identifies` | Required. A comma-separated list of entity identifiers to create in the case, such as `VALUE1, VALUE2, VALUE3`.  
`Delimiter` | Optional. A delimiter used to split the input from `Entities Identifies` into multiple identifiers. If no value is provided, the action treats the input as a single entity identifier. The default value is `,`.  
`Entity Type` | Required. The type of the entity to create, such as `HOST NAME`, `USER NAME`, or `IP Set`.  
`Is Internal` | Optional. If selected, the action marks entities as part of an internal network. Not enabled by default.  
`Is Suspicious` | Optional. If selected, the action marks entities as suspicious. Not enabled by default.  
  
#### Action outputs

The **Create Entity** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Create Entity** action:
    
    
    [
        {
            "additional_properties": {
                "OriginalIdentifier": "ACCOUNT_ID"
            },
            "alert_identifier": "ACCESS DISABLED ACCOUNTS",
            "case_identifier": 7113,
            "creation_time": 0,
            "entity_type": "USERUNIQNAME",
            "identifier": "ACCOUNT_ID",
            "is_artifact": false,
            "is_enriched": false,
            "is_internal": false,
            "is_pivot": false,
            "is_suspicious": false,
            "is_vulnerable": false,
            "modification_time": 0
        }
    ]
    

##### Output messages

The **Create Entity** action can return the following output messages:

Output message | Message description  
---|---  
`ENTITY_IDS created successfully.` | The action succeeded.  
`Error executing action "Create Entity". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Entity** action:

Script result name | Value  
---|---  
`StatusResult` | `true` or `false`  
  
### Create Gemini Case Summary

Use the **Create Gemini Case Summary** action to create a new Gemini case summary and add it to an alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Create Gemini Case Summary** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Gemini Case Summary** action:
    
    
    {
      "summary": "On the Linux agent instance-1 (IP addresses 10.150.0.3 and 34.85.128.214), user vanshikavw_google_com initiated the process curl (SHA1 hash 3395856ce81f2b7382dee72602f798b642f14140) to create the malware file /home/vanshikavw_google_com/eicar_test_vanshikavw-test-new.\n*  VirusTotal identifies the SHA1 hash 3395856ce81f2b7382dee72602f798b642f14140 as a virus.eicar/test.\n*  CURL is associated with multiple actors, including APT27, APT34, APT41, APT44, APT9, FIN11, FIN13, FIN6, TEMP.Armageddon, Turla Team, UNC1151, UNC1860, UNC215, UNC2165, UNC2500, UNC251, UNC2595, UNC2633, UNC2900, UNC2975, UNC3569, UNC3661, UNC3944, UNC4483, UNC4936, UNC4962, UNC5007, UNC5051, UNC5055, UNC5156, UNC5221, UNC5266, UNC5330, UNC5371, UNC5470, UNC5859, and UNC961.\n*  CURL is known to use MITRE ATT&CK techniques such as T1113, T1095, T1036, T1553, T1222, T1055, T1140, T1070, T1027, T1622, T1057, T1010, T1083, T1518, T1082, T1016, T1059, T1496, and T1588.\n*  A GTI MALWARE search did not find any information about eicar_test_vanshikavw-test-new.\n*  A GTI IP_ADDRESS search did not find any information about 10.150.0.3 or 34.85.128.214.", 
      "next_steps": ["Isolate instance-1 to prevent any potential lateral movement or further compromise of the network, as the curl process is associated with multiple threat actors.", 
      "Investigate the user account vanshikavw_google_com to determine if the user's credentials have been compromised or if the user initiated the curl process intentionally, as the curl process is associated with multiple threat actors.", 
      "Analyze the network traffic to and from the IP addresses 10.150.0.3 and 34.85.128.214 for any suspicious communication patterns, as the curl process is associated with multiple threat actors.", 
      "Examine the process execution logs on instance-1 for any other unusual or unauthorized activities, as the curl process is associated with multiple threat actors.", 
      "Review the configuration of the Linux agent on instance-1 to ensure that it is properly secured and that no unauthorized modifications have been made, as the curl process is associated with multiple threat actors."], 
      "reasons": ["The case involves a Linux agent instance-1 (IP addresses 10.150.0.3 and 34.85.128.214) where user vanshikavw_google_com initiated the process curl to create the file /home/vanshikavw_google_com/eicar_test_vanshikavw-test-new.", 
      "The SHA1 hash 3395856ce81f2b7382dee72602f798b642f14140 of the curl process is identified by VirusTotal as virus.eicar/test, indicating it is a known test virus.", 
      "The process CURL is associated with multiple threat actors, including APT27, APT34, APT41, APT44, APT9, FIN11, FIN13, FIN6, TEMP.Armageddon, Turla Team, UNC1151, UNC1860, UNC215, UNC2165, UNC2500, UNC251, UNC2595, UNC2633, UNC2900, UNC2975, UNC3569, UNC3661, UNC3944, UNC4483, UNC4936, UNC4962, UNC5007, UNC5051, UNC5055, UNC5156, UNC5221, UNC5266, UNC5330, UNC5371, UNC5470, UNC5859, and UNC961, suggesting a potential link to malicious activity.", 
      "CURL is known to use various MITRE ATT&CK techniques such as T1113, T1095, T1036, T1553, T1222, T1055, T1140, T1070, T1027, T1622, T1057, T1010, T1083, T1518, T1082, T1016, T1059, T1496, and T1588, indicating a wide range of potential malicious behaviors.", 
      "The file eicar_test_vanshikavw-test-new was not found in GTI MALWARE searches, and the IP addresses 10.150.0.3 and 34.85.128.214 were not found in GTI IP_ADDRESS searches."]
    }
    

##### Output messages

The **Create Gemini Case Summary** action can return the following output messages:

Output message | Message description  
---|---  
`Case summary generation completed.` | The action succeeded.  
`Error executing action "Create Gemini Case Summary". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Gemini Case Summary** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Create Or Update Entity Properties

Use the **Create Or Update Entity Properties** action to create or change the properties of entities in the entity scope.

This action runs on all Google SecOps entities.

#### Action inputs

The **Create Or Update Entity Properties** action requires the following parameters:

Parameter | Description  
---|---  
`Entity Field` | Required. The entity field to create or update.  
`Field Value` | Required. The value of the specified entity field.  
  
#### Action outputs

The **Create Or Update Entity Properties** action provides the following outputs:

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

The **Create Or Update Entity Properties** action can return the following output messages:

Output message | Message description  
---|---  
`Property ENTITY_FIELD were changed for the following entities: ENTITY_ID.` | The action succeeded.  
`Error executing action "Create Or Update Entity Properties". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Or Update Entity Properties** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Export Case

Use the **Export Case** action to create an archive containing case information and attachments.

This action doesn't run on Google SecOps entities. 

**Note:** The case wall attachment can't be larger than 5 MB.

#### Action inputs

The **Export Case** action requires the following parameters:

Parameter | Description  
---|---  
`Export Method` | Optional. The destination and retrieval method for the action's archive. If `Case Wall` is selected, the archive is created and placed on the case wall. The possible values are as follows:

  * `Case Wall`
  * `File System`

The default value is `Case Wall`.  
`Fields To Export` | Optional. A comma-separated list of case fields to include in the export, such as `alertCards`, `tags`, or `stageSlaExpirationUnixTimeInMs`. If no value is provided, the action exports the case with all available metadata.  
`Include Attachments` | Optional. If selected, the action includes attachments in the archive. Enabled by default.  
`Attachment Names` | Optional. A comma-separated list of attachments to include in the archive. If no value is provided, the action exports all attachments and you must enable `Include Attachments`.  
  
#### Action outputs

The **Export Case** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Export Case** action:
    
    
    {
       "file_path": "/tmp/case_1_Default_Environment_1919191919.zip",
       "export_type": "case_wall/file_system"
    }
    

##### Output messages

The **Export Case** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully exported case CASE_ID.` | The action succeeded.  
`Error executing action "Export Case". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Export Case** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Case Alerts

Use the **Get Case Alerts** action to retrieve alerts related to specified cases.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Case Alerts** action requires the following parameters:

Parameter | Description  
---|---  
`Case ID` | Required. A comma-separated list of case IDs for which the action retrieves the associated alerts.  
`Alert ID` | Optional. A comma-separated list of alert IDs, limiting the alerts returned. This parameter is only used when `Case ID` contains values.  
`Fields To Return` | Optional. A comma-separated list of fields to return in the JSON result. To retrieve nested values, use `Nested Keys Delimiter` to chain nested keys and list indexes. For example, if the delimiter is "`.`": `key1.nested_key1.0.nested_key2, key2, key3.1.nested_key1` If no value is provided, all fields are returned.  
`Nested Keys Delimiter` | Optional. The character used to separate nested keys and list indexes when defining fields to return. This parameter can't be a comma (`,`).  
  
### Get Case Details

Use the **Get Case Details** action to get all data from a case (including comments, entity information, insights, playbooks that ran, alert information, and events).

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Case Details** action requires the following parameters:

Parameter | Description  
---|---  
`Case Id` | Optional. The ID of the case to retrieve details from. If no value is provided, the action will use the current case.  
`Fields to Return` | Optional. A comma-separated list of fields to return. If nothing is provided, all fields are returned. Specific nested values can be retrieved by using the `Nested Keys Delimiter` parameter to separate keys and list indexes.  
`Nested Keys Delimiter` | Optional. The character used to separate nested keys when requesting specific fields. This lets you retrieve values from nested objects. The delimiter cannot be a comma(`,`).  
  
#### Action outputs

The **Get Case Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Case Details** action:
    
    
    {
        "id": 1001,
        "creationTimeUnixTimeInMs": 1749547533606,
        "modificationTimeUnixTimeInMs": 1750073142090,
        "name": "Security-Incident-Phishing-01",
        "isImportant": false,
        "isIncident": false,
        "startTimeUnixTimeInMs": 1749547529741,
        "endTimeUnixTimeInMs": 1749547529741,
        "assignedUser": "@Tier1_Analyst",
        "description": "Potential phishing email detected with suspicious attachment.",
        "isTestCase": false,
        "incidentId": null,
        "lastModifyingUserId": "secops_admin",
        "createTime": 1749547533606,
        "updateTime": 1750073142090,
        "alertCount": 1,
        "type": "External",
        "overflowCase": false,
        "status": "Opened",
        "score": 21,
        "involvedSuspiciousEntity": false,
        "workflowStatus": "Completed",
        "source": "Security_Server",
        "products": [],
        "tasks": [],
        "displayName": "Phishing email detector",
        "stage": "Triage",
        "priority": "PriorityLow",
        "important": false,
        "assignee": "@Tier1_Analyst",
        "incident": false,
        "environment": "Production Environment",
        "relatedAlerts": [],
        "tags": [
            "Phishing"
        ],
        "alertCards": [
            {
                "id": 1024,
                "creationTimeUnixTimeInMs": 1749547533634,
                "modificationTimeUnixTimeInMs": 1750073142082,
                "identifier": "alert-phish-778899",
                "status": 0,
                "name": "SUSPICIOUS PHISHING EMAIL",
                "priority": 40,
                "workflowsStatus": 2,
                "slaExpirationUnixTime": 1749547833634,
                "slaCriticalExpirationUnixTime": 1749547773634,
                "startTime": 1749547529741,
                "endTime": 1749547529741,
                "alertGroupIdentifier": "group-id-554433",
                "eventsCount": 1,
                "title": "SUSPICIOUS PHISHING EMAIL",
                "ruleGenerator": "Phishing email detector",
                "deviceProduct": "Phishing email detector",
                "deviceVendor": "Corporate Email Gateway",
                "playbookAttached": "Phishing Response Playbook",
                "playbookRunCount": 1,
                "isManualAlert": false,
                "sla": {
                    "slaExpirationTime": 1749547833634,
                    "criticalExpirationTime": 1749547773634,
                    "expirationStatus": 0,
                    "remainingTimeSinceLastPause": null
                },
                "fieldsGroups": [],
                "sourceUrl": null,
                "sourceRuleUrl": null,
                "siemAlertId": null,
                "relatedCases": [],
                "lastSourceUpdateUnixTimeInMs": null,
                "nestingDepth": 0,
                "eventCount": 1,
                "caseId": 1001,
                "createTime": 1750684686624,
                "updateTime": 1750684686949,
                "product": "Microsoft:AccessDisabledAccounts",
                "displayName": "ACCESS DISABLED ACCOUNTS",
                "vendor": "Microsoft",
                "environment": "Production Environment",
                "ticketId": "c4db60fa-b510-414a-a462-c3f215809f96",
                "sourceSystemName": "Cloud App Security",
                "manual": false,
                "additionalProperties": "{\"Name\":\"Access Disabled Accounts\",\"Type\":\"ALERT\",\"EndTime\":\"1750684684139\",\"Alert_Id\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"TicketId\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"DisplayId\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"StartTime\":\"1750684684139\",\"IsArtifact\":\"False\",\"IsEnriched\":\"False\",\"IsTestCase\":\"False\",\"Description\":\"Access Disabled Accounts\",\"Environment\":\"Production Environment\",\"IsSuspicious\":\"False\",\"IsVulnerable\":\"False\",\"DataAccessScope\":null,\"IsInternalAsset\":\"False\",\"AlertBaseEventIds\":\"d85ca9a7-58a7-4329-b615-ebe3dcfc6fd1\",\"EstimatedStartTime\":\"1750684684139\"}",
                "securityEventCards": [
                    {
                        "fields": [
                            {
                                "order": 0,
                                "groupName": "Highlighted Fields",
                                "isIntegration": false,
                                "isHighlight": true,
                                "items": [
                                    {
                                        "originalName": "DestinationHostName",
                                        "name": "Destination Host Name",
                                        "value": "WORKSTATION-01.LOCAL"
                                    }
                                ]
                            }
                        ],
                        "identifier": "d7ab8656-c862-498c-a266-69718e46b1b7",
                        "caseId": 1001,
                        "alertIdentifier": "SECURITY_RISK_FOUND_ID_998877",
                        "name": "Virus found",
                        "product": "symantec:endpoint:protection",
                        "port": null,
                        "sourceSystemName": "ArcSight ESM",
                        "outcome": null,
                        "time": 1766566370354,
                        "type": "Virus found",
                        "artifactEntities": []
                    }
                ],
                "involvedRelations": [],
                "sourceIdentifier": "GCP_Ingestion",
                "playbookStatus": 0
            }
        ],
        "isOverflowCase": false,
        "isManualCase": false,
        "slaExpirationUnixTime": 1749547833634,
        "slaCriticalExpirationUnixTime": 1749547773634,
        "stageSlaExpirationUnixTimeInMs": null,
        "stageSlaCriticalExpirationUnixTimeInMs": null,
        "canOpenIncident": false,
        "sla": {
            "slaExpirationTime": 1749547833634,
            "criticalExpirationTime": 1749547773634,
            "expirationStatus": 0,
            "remainingTimeSinceLastPause": null
        },
        "stageSla": {
            "slaExpirationTime": null,
            "criticalExpirationTime": null,
            "expirationStatus": 2,
            "remainingTimeSinceLastPause": null
        },
        "relatedAlertTicketId": null,
        "relatedAlertCards": [],
        "activities": [
            {
                "id": "Activity-Insight-16",
                "creatorUserId": "security_bot",
                "activityId": 16,
                "activityType": "CaseInsight",
                "caseId": 1001,
                "createTime": 1750068343993,
                "updateTime": 1750068343993,
                "alertIdentifier": "alert-phish-778899",
                "activityDataJson": {
                    "TriggeredBy": "SecurityAutomator",
                    "EntityIdentifier": "URGENT: ACTION REQUIRED ON SALARY",
                    "EntityData": {
                        "CaseId": 1001,
                        "AlertIdentifier": "alert-phish-778899",
                        "AlertStatus": 0,
                        "Identifier": "URGENT: ACTION REQUIRED ON SALARY",
                        "EntityType": "EMAILSUBJECT",
                        "IsInternal": true,
                        "IsSuspicious": false,
                        "IsArtifact": true,
                        "IsPivot": false,
                        "Environment": "Production Environment",
                        "FieldsGroups": [
                            {
                                "Order": 0,
                                "GroupName": "Default",
                                "IsIntegration": false,
                                "IsHighlight": false,
                                "Items": [
                                    {
                                        "OriginalName": "Network_Priority",
                                        "Name": "Network Priority",
                                        "Value": "0"
                                    }
                                ]
                            }
                        ],
                        "HighlightedFieldsGroups": [],
                        "IsManuallyCreated": false,
                        "SourceUrl": null
                    },
                    "Title": "Phishing Subject Insight",
                    "Content": "Detected unusual keywords in subject line.",
                    "Severity": 0,
                    "InsightType": 1,
                    "AdditionalDataType": null,
                    "AdditionalData": null,
                    "AdditionalDataTitle": null,
                    "AlertIdentifiers": [
                        "ALERT_PHISH_INSTANCE_ID_001"
                    ],
                    "EntityType": "EMAILSUBJECT",
                    "CreatorUserId": "system",
                    "CreatorFullName": "System Administrator",
                    "Id": 16,
                    "Type": 6,
                    "CaseId": 1001,
                    "IsFavorite": false,
                    "ModificationTimeUnixTimeInMs": 1750068343993,
                    "CreationTimeUnixTimeInMs": 1750068343993,
                    "AlertIdentifier": "ALERT_PHISH_INSTANCE_ID_001"
                },
                "favorite": false
            }
        ],
        "entityCards": [
            {
                "identifier": "WORKSTATION-01.LOCAL",
                "type": "HOSTNAME",
                "suspicious": false,
                "linkedEntities": [
                    {
                        "identifier": "192.168.1.50",
                        "type": "ADDRESS",
                        "suspicious": false,
                        "linkedEntities": [],
                        "direction": 0
                    }
                ]
            }
        ],
        "entities": [
            {
                "caseId": 1001,
                "type": "FILEHASH",
                "enriched": false,
                "artifact": true,
                "vulnerable": false,
                "suspicious": false,
                "attacker": false,
                "pivot": false,
                "internal": true,
                "manuallyCreated": false,
                "fields": [
                    {
                        "highlighted": false,
                        "displayName": "Default",
                        "hidden": false,
                        "items": [
                            {
                                "name": "Network Priority",
                                "originalName": "Network_Priority",
                                "value": "0"
                            }
                        ]
                    }
                ],
                "identifier": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "id": 505,
                "alertIdentifier": "SECURITY_RISK_FOUND_ID_998877",
                "environment": "Production Environment",
                "additionalProperties": "{\"Type\":\"FILEHASH\",\"IsArtifact\":\"True\",\"IsEnriched\":\"False\",\"IsTestCase\":\"False\",\"IsVulnerable\":\"False\",\"IsInternalAsset\":\"False\",\"OriginalIdentifier\":\"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\"}",
                "alertGroupIdentifier": "group-id-virus-scan-results",
                "networkPriority": 0
            }
        ],
        "totalSize": 1,
        "moveEnvironment": {},
        "insights": [
            {
                "alertIdentifier": "SECURITY_RISK_FOUND_ID_998877",
                "caseId": 1001,
                "triggeredBy": "Analyst_John",
                "title": "Endpoint Discovery",
                "content": "Host workstation matched known internal asset list.",
                "entity": {
                    "caseId": 1001,
                    "alertIdentifier": "SECURITY_RISK_FOUND_ID_998877",
                    "alertStatus": 0,
                    "identifier": "WORKSTATION-01.LOCAL",
                    "entityType": "HOSTNAME",
                    "isInternal": true,
                    "isSuspicious": false,
                    "isArtifact": false,
                    "isPivot": false,
                    "environment": "Production Environment",
                    "highlightedFieldsGroups": [],
                    "isManuallyCreated": false,
                    "sourceUrl": null,
                    "fields": [
                        {
                            "order": 0,
                            "groupName": "Entity",
                            "isIntegration": false,
                            "isHighlight": false,
                            "items": [
                                {
                                    "originalName": "IsPivot",
                                    "name": "Is Pivot",
                                    "value": "False"
                                }
                            ]
                        }
                    ]
                },
                "severity": 0,
                "type": 6,
                "additionalDataType": null,
                "additionalData": null,
                "additionalDataTitle": null,
                "creatorUserName": "analyst_admin",
                "entityIdentifier": "WORKSTATION-01.LOCAL",
                "insightType": 1,
                "alertIdentifiers": [
                    "SECURITY_RISK_FOUND_ID_998877"
                ],
                "entityType": "HOSTNAME",
                "creatorUserId": "user_id_101",
                "id": 444,
                "isFavorite": false,
                "modificationTimeUnixTimeInMs": 1766569221777,
                "creationTimeUnixTimeInMs": 1766569221777
            }
        ]
    }
    

##### Output messages

The **Get Case Details** action can return the following output messages:

Output message | Message description  
---|---  
`Finished executing "Get Case Details" successfully` | The action succeeded.  
`Error executing action "Get Case Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Case Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Connector Context Value

Use the **Get Connector Context Value** action to retrieve a value from a specified key in the Google SecOps database for a connector context.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Connector Context Value** action requires the following parameters:

Parameter | Description  
---|---  
`Connector Identifier` | Required. The unique identifier of the connector to retrieve the context value from.  
`Key Name` | Required. The key under which the context value is stored.  
`Create Case Wall Table` | Optional. If selected, the action creates a case wall table with the retrieved context value. The table won't be created if the retrieved value exceeds the character limit. Enabled by default.  
  
#### Action outputs

The **Get Connector Context Value** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case Wall table

The **Get Connector Context Value** action can generate the following table:

Table name: **Connector**

Table columns:

  * **Connector identifier**
  * **Key**
  * **Value**



##### Output messages

The **Get Connector Context Value** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found context value for the provided context key CONTEXT_KEY for the connector identifier CONNECTOR_IDENTIFIER. ` `Context value was not found for the provided context key CONTEXT_KEY and connector identifier CONNECTOR_IDENTIFIER.` `Action can't return the Case Wall table as the context values are too big.` | The action succeeded.  
`Error executing action "Get Connector Context Value". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Connector Context Value** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Custom Field Values

Use the **Get Custom Field Values** action to retrieve current values of a custom field based on the specified scope.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Custom Field Values** action requires the following parameters:

Parameter | Description  
---|---  
`Scope` | Required. The scope to retrieve the custom fields from. The possible values are as follows:

  * `Case`
  * `Alert`
  * `All`

  
  
#### Action outputs

The **Get Custom Field Values** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Custom Field Values** action:
    
    
    [{
       "Case": {
           "Case Custom Field Name 1": "Updated Custom Field Value",
           "Case Custom Field Name 2": "Updated Custom Field Value"
       },
       "Alert": {
           "Alert Custom Field Name 1": "Updated Custom Field Value",
           "Alert Custom Field Name 2": "Updated Custom Field Value"
       }
    }]
    

##### Output messages

The **Get Custom Field Values** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned SCOPE custom fields.` `No custom fields were found in scope SCOPE.` | The action succeeded.  
`Error executing action "Get Custom Field Values". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Custom Field Values** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Scope Context Value

Use the **Get Scope Context Value** action to retrieve a value from the Google SecOps database that is stored under a specified key and context.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Scope Context Value** action requires the following parameters:

Parameter | Description  
---|---  
`Context Scope` | Required. The context scope to retrieve the value from. The possible values are as follows:

  * `Not specified`
  * `Alert`
  * `Case`
  * `Global`

The default value is `Not specified`.  
`Key Name` | Required. The key under which the value is stored in the specified context.  
`Create Case Wall Table` | Optional. If selected, the action creates a case wall table with the retrieved context value. The table won't be created if the retrieved value exceeds the character limit. Enabled by default.  
  
#### Action outputs

The **Get Scope Context Value** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case Wall table

The **Get Scope Context Value** action can generate the following table:

Table name: **SCOPE**

Table columns:

  * **Key**
  * **Value**



##### Output messages

The **Get Scope Context Value** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found context value for the provided context key CONTEXT_KEY with scope CONTEXT_SCOPE.` `No context values were found for the provided context scope CONTEXT_SCOPE.` `Context value was not found for the provided context key CONTEXT_KEY with scope CONTEXT_SCOPE.` `Action can't return the Case Wall table as the context values are too big.` | The action succeeded.  
`Error executing action "Get Scope Context Value". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Scope Context Value** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Similar Cases

Use the **Get Similar Cases** action to search for similar cases and return their IDs.

The action applies the logical `AND` operator to the `Rule Generator`, `Port`, `Category Outcome`, `Entity Identifier`, `Include Open Cases`, and `Include Closed Cases` parameters to filter for cases that match all specified criteria.

This action runs on all Google SecOps entities.

#### Action inputs

The **Get Similar Cases** action requires the following parameters:

Parameter | Description  
---|---  
`Rule Generator` | Optional. If selected, the action searches for similar cases using the rule generator. Enabled by default.  
`Port` | Optional. If selected, the action searches for similar cases using port numbers. Enabled by default.  
`Category Outcome` | Optional. If selected, the action searches for similar cases using the category outcome. Enabled by default.  
`Entity Identifier` | Optional. If selected, the action searches for similar cases using the entity identifier. Enabled by default.  
`Days Back` | Required. The number of days prior to the current date for the action to search through.  
`Include Open Cases` | Optional. If selected, the action includes open cases in the search. Enabled by default.  
`Include Closed Cases` | Optional. If selected, the action includes closed cases in the search. Enabled by default.  
  
#### Action outputs

The **Get Similar Cases** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Similar Cases** action:
    
    
    {
      "results": [{
        "id": 23874, 
        "name": "Malware", 
        "tags": ["hi", "Simulated Case"], 
        "start time": "2024-09-25 05:43:41.999000+00:00", 
        "start time unix": 1727243021999, 
        "last modified": "2025-06-19 13:24:01.062000+00:00", 
        "priority": "Informative", 
        "assigned user": "@Tier1", 
        "matching_criteria": {
            "ruleGenerator": true, 
            "port": true, 
            "outcome": true, 
            "entities": true
          }, 
        "matched_entities": [
          {"entity": "INSTANCE-1", "type": "HOSTNAME", "isSuspicious": false}, 
          {"entity": "10.150.0.3", "type": "ADDRESS", "isSuspicious": false}, {"entity": "172.17.0.1", "type": "ADDRESS", "isSuspicious": false}, {"entity": "VANSHIKAVW_GOOGLE_COM", "type": "USERUNIQNAME", "isSuspicious": false}, 
          {"entity": "CURL", "type": "PROCESS", "isSuspicious": false}, {"entity": "EICAR_TEST_VANSHIKAVW-TEST-NEW", "type": "FILENAME", "isSuspicious": false}, 
          {"entity": "3395856CE81F2B7382DEE72602F798B642F14140", "type": "FILEHASH", "isSuspicious": false}, 
          {"entity": "34.85.128.214", "type": "ADDRESS", "isSuspicious": false}, 
          {"entity": "/HOME/VANSHIKAVW_GOOGLE_COM/EICAR_TEST_VANSHIKAVW-TEST-NEW", "type": "FILENAME", "isSuspicious": false}
          ], 
          "status": "Open"}], 
          "stats": 
          {"Malicious": 0.0, "Is Important": 0.0, "Is Incident": 0.0, "Status Open": 100.0}, 
          "platform_url": "https://soarapitest.backstory.chronicle.security/"
    }
    

##### Output messages

The **Get Similar Cases** action can return the following output messages:

Output message | Message description  
---|---  
`Processed NUMBER_OF_CASES similar cases: CASE_IDS_LIST` | The action succeeded.  
`Error executing action "Get Similar Cases". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Similar Cases** action:

Script result name | Value  
---|---  
`SimilarCasesIds` | A list of similar case IDs.  
  
### Instruction

Use the **Instruction** action to provide instructions to an analyst directly on the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Instruction** action requires the following parameters:

Parameter | Description  
---|---  
`Instruction` | Required. The instructions for the analyst.  
  
#### Action outputs

The **Instruction** action provides the following outputs:

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

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Please perform the following instructions: INSTRUCTION.` | The action succeeded.  
`Error executing action "Instruction". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Instruction** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Is In Custom List

Use the **Is In Custom List** action to check if an entity exists within a designated custom list.

This action runs on all Google SecOps entities.

#### Action inputs

The **Is In Custom List** action requires the following parameters:

Parameter | Description  
---|---  
`Category` | Required. The name of the custom list category to search.  
  
#### Action outputs

The **Is In Custom List** action provides the following outputs:

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

The **Is In Custom List** action can return the following output messages:

Output message | Message description  
---|---  
`This alert contains entities in the given custom list category: CATEGORY. This alert does not contain entities in the given custom list category: CATEGORY.` | The action succeeded.  
`Error executing action "Is In Custom List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Is In Custom List** action:

Script result name | Value  
---|---  
`ScriptResult` | `true` or `false`  
  
### Mark As Important

Use the **Mark As Important** action to mark the case as important.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Mark As Important** action provides the following outputs:

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

The **Mark As Important** action can return the following output messages:

Output message | Message description  
---|---  
`The case was automatically marked as important.` | The action succeeded.  
`Error executing action "Mark As Important". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Mark As Important** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Open Web Url

Use the **Open Web Url** action to generate a browser link.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Open Web Url** action requires the following parameters:

Parameter | Description  
---|---  
`Title` | Required. The title of the URL.  
`URL` | Required. The target URL.  
  
#### Action outputs

The **Open Web Url** action provides the following outputs:

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

The **Open Web Url** action can return the following output messages:

Output message | Message description  
---|---  
`URL_TITLE URL_LINK` | The action succeeded.  
`Error executing action "Open Web Url". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Open Web Url** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Pause Alert SLA

Use the **Pause Alert SLA** action to pause the Service Level Agreement (SLA) timer for the alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Pause Alert SLA** action requires the following parameters:

Parameter | Description  
---|---  
`Message` | Optional. The reason for pausing the alert SLA.  
  
#### Action outputs

The **Pause Alert SLA** action provides the following outputs:

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

The **Pause Alert SLA** action can return the following output messages:

Output message | Message description  
---|---  
`The alert SLA was paused.` | The action succeeded.  
`Error executing action "Pause Alert SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Pause Alert SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Pause Case SLA

Use the **Pause Case SLA** action to pause the Service Level Agreement (SLA) timer for the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Pause Case SLA** action requires the following parameters:

Parameter | Description  
---|---  
`Message` | Optional. The reason for pausing the case SLA.  
  
#### Action outputs

The **Pause Case SLA** action provides the following outputs:

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

The **Pause Case SLA** action can return the following output messages:

Output message | Message description  
---|---  
`The Case SLA was paused successfully.` | The action succeeded.  
`Error executing action "Pause Case SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Pause Case SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Permitted Alert Time

Use the **Permitted Alert Time** action to check if the start time of the alert complies with user-defined time conditions.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Permitted Alert Time** action requires the following parameters:

Parameter | Description  
---|---  
`Timestamp Type` | Optional. The type of timestamp to use for comparison. The possible values are as follows:

  * `Alert Start Time`
  * `Alert Creation Time`
  * `Case Creation Time`

The default value is `Alert Start Time`.  
`Permitted Start Time` | Required. The start time of the permitted period for alerts, such as `0:00:00`.  
`Permitted End Time` | Required. The end time of the permitted period for alerts, such as `0:00:00`.  
`Monday` | Optional. If selected, the action includes Mondays in the permitted days for alerts. Not enabled by default.  
`Tuesday` | Optional. If selected, the action includes Tuesdays in the permitted days for alerts. Enabled by default.  
`Wednesday` | Optional. If selected, the action includes Wednesdays in the permitted days for alerts. Enabled by default.  
`Thursday` | Optional. If selected, the action includes Thursdays in the permitted days for alerts. Not enabled by default.  
`Friday` | Optional. If selected, the action includes Fridays in the permitted days for alerts. Not enabled by default.  
`Saturday` | Optional. If selected, the action includes Saturdays in the permitted days for alerts. Not enabled by default.  
`Sunday` | Optional. If selected, the action includes Sundays in the permitted days for alerts. Not enabled by default.  
`Input Timezone` | Optional. This action supports standard time zones, such as `UTC`, in addition to IANA zones, such as `America/New_York`. If you provide an IANA zone, the action automatically adjusts for daylight saving.  
  
#### Action outputs

The **Permitted Alert Time** action provides the following outputs:

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

The **Permitted Alert Time** action can return the following output messages:

Output message | Message description  
---|---  
`Case Time of ALERT_TIMEis within condition parameters of between START_TIME - END_TIME on LIST_OF_PERMITTED_DAYS` | The action succeeded.  
`Error executing action "Permitted Alert Time". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Permitted Alert Time** action:

Script result name | Value  
---|---  
`Permitted` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Siemplify.

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

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Email address is syntactically correct.` | The action succeeded.  
`Error executing action "Ping". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Raise Incident

Use the **Raise Incident** action to mark a true positive case as `Critical` and raise the case incident.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Raise Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Soc Role` | Optional. The Google SecOps SOC role to assign the case to.  
  
#### Action outputs

The **Raise Incident** action provides the following outputs:

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

The **Raise Incident** action can return the following output messages:

Output message | Message description  
---|---  
`The case raised to CASE_STAGE status.` | The action succeeded.  
`Error executing action "Raise Incident". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Raise Incident** action:

Script result name | Value  
---|---  
Script Result | `true` or `false`  
  
### Remove Tag

Use the **Remove Tag** action to remove tags from the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Tag** action requires the following parameters:

Parameter | Description  
---|---  
`Tag` | Required. A comma-separated list of tags to remove from the case.  
  
#### Action outputs

The **Remove Tag** action provides the following outputs:

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

The **Remove Tag** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed the following tags from case CASE_ID:TAGS` | The action succeeded.  
`It is not possible to remove the tag.` `Error executing action "Remove Tag". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Tag** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove From Custom List

Use the **Remove From Custom List** action to remove entities associated with an alert from a custom list category.

This action runs on all Google SecOps entities.

#### Action inputs

The **Remove From Custom List** action requires the following parameters:

Parameter | Description  
---|---  
`Category` | Required. The name of the custom list category to remove the entity identifier from.  
  
#### Action outputs

The **Remove From Custom List** action provides the following outputs:

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

The **Remove From Custom List** action can return the following output messages:

Output message | Message description  
---|---  
`The alert's entities ENTITY_ID were removed from custom list category: CATEGORY` `The given category does not exist.` | The action succeeded.  
`Error executing action "Remove From Custom List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove From Custom List** action:

Script result name | Value  
---|---  
`ScriptResult` | `true` or `false`  
  
### Resume Alert SLA

Use the **Resume Alert SLA** action to unpause and restart the Service Level Agreement (SLA) timer for the alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Resume Alert SLA** action provides the following outputs:

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

The **Resume Alert SLA** action can return the following output messages:

Output message | Message description  
---|---  
`The alert SLA was resumed.` | The action succeeded.  
`Error executing action "Resume Alert SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Resume Alert SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Resume Case SLA

Use the **Resume Case SLA** action to unpause and restart the Service Level Agreement (SLA) timer for the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Resume Case SLA** action provides the following outputs:

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

The **Resume Case SLA** action can return the following output messages:

Output message | Message description  
---|---  
`The Case SLA was resumed successfully.` | The action succeeded.  
`Error executing action "Resume Case SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Resume Case SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search Cases

Use the **Search Cases** action to search for cases using dynamic filter criteria.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Cases** action requires the following parameters:

Parameter | Description  
---|---  
`Assignee` | Optional. A comma-separated list of users assigned to the case used to filter the search results.  
`Status` | Optional. A selection of case statuses used to filter the search results. The possible values are as follows:

  * `Opened`
  * `Closed`

  
`Playbook Status` | Optional. A selection of playbook statuses used to filter the search results. The possible values are as follows:

  * `In Progress`
  * `Completed`
  * `Failed`

  
`Severity` | Optional. A selection of case severity levels used to filter the search results. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

  
`Environment` | Optional. A comma-separated list of environments used to filter the search results. Multiple values are evaluated using "OR" logic. This parameter supports "Contains" matching through the use of the `~` symbol (for example, `environment,~environment`).  
`Case Names` | Optional. A comma-separated list of case names used to filter the search results. Multiple values are evaluated using "OR" logic. This parameter supports "Contains" matching through the use of the `~` symbol (for example, `case,~case`).  
`Alert Names` | Optional. A comma-separated list of alert names used to filter the search results Multiple values are evaluated using "OR" logic. This parameter supports "Contains" matching through the use of the `~` symbol (for example, `alert,~alert`).  
`Product Names` | Optional. A comma-separated list of product names used to filter the search results. Multiple values are evaluated using "OR" logic. This parameter supports "Contains" matching through the use of the `~` symbol (for example, `product,~product`).  
`Tag Names` | Optional. A comma-separated list of tag names used to filter the search results. Multiple values are evaluated using "OR" logic.  
`Timestamp Type` | Optional. The type of timestamp used to determine whether `Time Frame` targets the creation time or the modification time of the case. The possible values are as follows:

  * `Modification Time`
  * `Creation Time`

The default value is `Modification Time`.  
`Time Frame` | Optional. The time range used to limit the search results. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

If `Custom` is selected, the `Start Time` parameter is mandatory. The default value is `Last Hour`.  
`Start Time` | Conditional. The starting point of the time range for the search results in ISO 8601 format. If `Time Frame` is set to `Custom`, this parameter is mandatory.  
`End Time` | Optional. The ending point of the time range for the search results in ISO 8601 format. If `Time Frame` is set to `Custom` and no value is provided, this parameter defaults to the current time.  
  
#### Action outputs

The **Search Cases** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search Cases** action:
    
    
    [
        {
            "name": "projects//locations//instances//cases/4",
            "relatedAlerts": [],
            "dataAccessScopes": [],
            "id": 4,
            "lastModifyingUserId": "9c6562ad-f74f-424f-a2f7-c0d2d8629bbb",
            "createTime": 1769592095506,
            "updateTime": 1769689090290,
            "alertCount": 1,
            "type": "External",
            "overflowCase": false,
            "status": "Opened",
            "involvedSuspiciousEntity": false,
            "workflowStatus": "Completed",
            "source": "Server",
            "tags": [
                {
                    "displayName": "Simulated Case",
                    "priority": 0
                }
            ],
            "products": [
                {
                    "displayName": "Windows:AccessDisabledAccounts",
                    "alert": "ACCESS DISABLED ACCOUNTS_5FB4AAF2-1CB2-49F7-850D-EECCAB91B203"
                }
            ],
            "tasks": [],
            "displayName": "Access Disabled Accounts",
            "stage": "Triage",
            "priority": "PriorityHigh",
            "important": false,
            "assignee": "@Administrator",
            "incident": false,
            "environment": "Default Environment",
            "moveEnvironment": {}
        }
    ]
    

##### Output messages

The **Search Cases** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned cases based on the provided criteria.` | The action succeeded.  
`Error executing action "Search Cases". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Cases** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Alert SLA

Use the **Set Alert SLA** action to set the SLA timer for the alert.

**Note:** This action overrides any existing SLA for the alert.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Alert SLA** action requires the following parameters:

Parameter | Description  
---|---  
`SLA Period` | Required. The total duration of the SLA before it is considered breached. The total SLA period cannot exceed 30 days. The default value is `5`.  
`SLA Time Unit` | Required. The time unit for the SLA period. The possible values are as follows:

  * `Minutes`
  * `Hours`
  * `Days`

The default value is `Minutes`.  
`SLA Time To Critical Period` | Required. The duration of the SLA before it enters a critical state. The default value is `4`.  
`SLA Time To Critical Unit` | Required. The time unit for the critical SLA period. The possible values are as follows:

  * `Minutes`
  * `Hours`
  * `Days`

The default value is `Minutes`.  
  
#### Action outputs

The **Set Alert SLA** action provides the following outputs:

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

The **Set Alert SLA** action can return the following output messages:

Output message | Message description  
---|---  
`Alert ALERT_NAME of case CASE_ID was set with SLA of SLA_PERIOD SLA_TIME_UNIT and critical period of CRITICAL_PERIOD CRITICAL_TIME_UNIT.` | The action succeeded.  
`Error executing action "Set Alert SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Alert SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Case SLA

Use the **Set Case SLA** action to set the SLA for the case.

This action has the highest priority and overrides the existing SLA defined for the specific case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Case SLA** action requires the following parameters:

Parameter | Description  
---|---  
`SLA Period` | Required. The total duration of the SLA before it is considered breached. The total SLA period cannot exceed 30 days. The default value is `5`.  
`SLA Time Unit` | Required. The time unit for the SLA period. The possible values are as follows:

  * `Minutes`
  * `Hours`
  * `Days`

The default value is `Minutes`.  
`SLA Time To Critical Period` | Optional. The duration of the SLA before it enters a critical state. The default value is `4`.  
`SLA Time To Critical Unit` | Required. The time unit for the critical SLA period. The possible values are as follows:

  * `Minutes`
  * `Hours`
  * `Days`

The default value is `Minutes`.  
  
#### Action outputs

The **Set Case SLA** action provides the following outputs:

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

The **Search ASM Issues** action can return the following output messages:

Output message | Message description  
---|---  
`Case CASE_ID was set with SLA of SLA_PERIOD SLA_TIME_UNIT and critical period of CRITICAL_PERIOD CRITICAL_TIME_UNIT.` | The action succeeded.  
`Error executing action "Set Case SLA". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Case SLA** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Custom Fields

Use the **Set Custom Fields** action to set values for custom fields.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Custom Fields** action requires the following parameters:

Parameter | Description  
---|---  
`Scope` | Required. The scope to set for the custom fields. The possible values are as follows:

  * `Case`
  * `Alert`

The default value is `Case`.  
`Custom Fields Data` | Required. The updated values for the custom fields. You can update multiple custom fields in a single action run. The default value is:
    
    
        {
          "Custom Field Name 1":"Custom Field Value 1",
          "Custom Field Name 2":"Custom Field Value 2"
        }  
  
`Append Values` | Optional. If selected, the action appends the inputs from `Custom Fields Data` to the existing values of the custom fields. If not selected, the action overwrites the existing values with the inputs from the `Custom Fields Data` parameter. Not enabled by default.  
  
#### Action outputs

The **Set Custom Fields** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Set Custom Fields** action:
    
    
    {
      "Custom Field Name": "Updated Custom Field Value",
      "Custom Field Name": "Updated Custom Field Value",
    }
    

##### Output messages

The **Set Custom Fields** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the following SCOPE custom fields: UPDATED_CUSTOM_FIELD_NAMES` | The action succeeded.  
`Error executing action "Set Custom Fields". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Custom Fields** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Risk Score

Use the **Set Risk Score** action to update the risk score of the case.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Risk Score** action requires the following parameters:

Parameter | Description  
---|---  
`Risk Score` | Required. The risk score to set for the case.  
  
#### Action outputs

The **Set Risk Score** action provides the following outputs:

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

The **Set Risk Score** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully set Risk Score for case CASE_ID` | The action succeeded.  
`Error executing action "Set Risk Score". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Risk Score** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Scope Context Value

Use the **Set Scope Context Value** action to set a value for a key that is stored in the Google SecOps database.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Scope Context Value** action requires the following parameters:

Parameter | Description  
---|---  
`Context Scope` | Required. The context scope to retrieve data from. The possible values are as follows:

  * `Not specified`
  * `Alert`
  * `Case`
  * `Global`

The default value is `Not specified`.  
`Key Name` | Required. The key name to retrieve the corresponding value from.  
`Key Value` | Required. The value to store under the specified key.  
  
#### Action outputs

The **Set Scope Context Value** action provides the following outputs:

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

The **Set Scope Context Value** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully set context value for the context key CONTEXT_KEY with scope CONTEXT_SCOPE.` | The action succeeded.  
`Error executing action "Set Scope Context Value". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Scope Context Value** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update Case Description

Use the **Update Case Description** action to update the case description.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Case Description** action requires the following parameters:

Parameter | Description  
---|---  
`Description` | Required. The description to set for the case.  
  
#### Action outputs

The **Update Case Description** action provides the following outputs:

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

The **Update Case Description** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the case description.` | The action succeeded.  
`Error executing action "Update Case Description". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Case Description** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Wait For Custom Fields

Use the **Wait For Custom Fields** action to wait for custom field values to continue playbook execution.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Wait For Custom Fields** action requires the following parameters:

Parameter | Description  
---|---  
`Scope` | Required. The scope to set for the custom fields. The possible values are as follows:

  * `Case`
  * `Alert`

The default value is `Case`.  
`Custom Fields Data` |  Required. The conditions for custom fields that must be met to resume a playbook. The custom field names and their required values need to be configured as a JSON object. If you set conditions for multiple fields, the action waits for all fields to match their respective conditions.

  * To resume when a custom field has any value, configure an empty string: 
        
        {"Custom Field Name": ""}

  * To resume when a custom field equals a specific value, such as `VALUE_1`, specify the value: 
        
        {"Custom Field Name": "VALUE_1"}


The default value shows the expected JSON format:
    
    
    {
      "Custom Field Name 1": "Custom Field Value 1",
      "Custom Field Name 2": "Custom Field Value 2"
    }
          
  
#### Action outputs

The **Wait For Custom Fields** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Wait For Custom Fields** action:
    
    
    {
    "Custom Field Name": "Updated Custom Field Value",
    "Custom Field Name": "Updated Custom Field Value",
    }
    

##### Output messages

The **Wait For Custom Fields** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully waited for the following SCOPE custom fields: UPDATED_CUSTOM_FIELD_NAMES` `Waiting for SCOPE custom fields updates...` | The action succeeded.  
`Error executing action "Wait For Custom Fields". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Wait For Custom Fields** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Siemplify - Actions Monitor

Use the **Siemplify - Actions Monitor** job to receive notifications about actions that have failed at least three separate times in the last three hours.

#### Job parameters

The **Siemplify - Actions Monitor** job requires the following parameters:

Parameter | Description  
---|---  
`Run Interval In Seconds` | Optional. The interval, in seconds, for the job to run. This parameter determines how often the integration checks for failed playbook actions. The default value is `900`.  
`Is Enabled` | Optional. If selected, the job is active and will run on schedule. When not selected, the job is disabled and won't execute.  Enabled by default.  
  
### Siemplify - Cases Collector DB

Use the **Siemplify - Cases Collector DB** job to retrieve and process security cases from a designated publisher.

#### Job parameters

The **Siemplify - Cases Collector DB** job requires the following parameters:

Parameter | Description  
---|---  
`Publisher Id` | Required. The ID of the publisher from which to collect cases and logs.  
`Verify SSL` | Optional. If selected, the job verifies that the SSL certificate of the publisher is valid. Not enabled by default.  
  
### Siemplify - Logs Collector

Use the **Siemplify - Logs Collector** job to retrieve and process logs from a specified publisher.

#### Job inputs

The **Siemplify - Logs Collector** job requires the following parameters:

Parameter | Description  
---|---  
`Publisher Id` | Required. The ID of the publisher from which to collect the logs.  
`Verify SSL` | Optional. If selected, the job verifies that the publisher's SSL certificate is valid. Not enabled by default.  
  
### Siemplify - Response Integration & Connector Upgrade

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

Use the **Response Integration & Connector Upgrade** job to automatically maintain your environment by upgrading response integrations and connectors to their latest versions, or by generating notifications when new versions become available in the Content Hub.

#### Job behavior

The job scans the Content Hub to identify integrations and connectors that aren't running the latest version. Depending on the selected `Mode`, the job performs the following:

  * **Filtering logic** : The job uses the following criteria to determine which components to exclude during the scan.

    * **Staging environment** : The job only scans integrations that are already installed. If `Update Staging Only` is enabled, the job only processes integrations within a manually created staging environment. You must configure your staging environment and assign relevant integrations before the job can identify updates in this mode.
**Note:** This concept applies exclusively to integration instances. Updating an integration in staging doesn't affect its associated connectors.
    * **Integrations** : The job checks against both the identifier and the display name when applying the `Integrations To Ignore` list.

    * **Connectors** : Filtering only applies to the display name, as connector identifiers aren't unique.

  * **Notification mode** : When set to `Notification` mode, the job identifies available updates and generates a system notification with the following structure. 

> New Response Integration version available for:  
>  {Integration Name}: {previous version} -> {new version}  
>   
>  Connector updates available for:  
>  {Connector display name} 

These notifications appear under **notifications Notifications > System Notifications** in the Google SecOps platform.

  * **Upgrade mode** : When set to `Upgrade` mode, the job automatically applies the updates and generates a confirmation notification with the following structure. 

> The following Response Integrations were updated to the latest version:  
>  {Response Integration name}  
>   
>  The following connectors were updated to the latest version:  
>  {Connector display name} 




#### Job inputs

The **Siemplify - Response Integration & Connector Upgrade** job requires the following parameters:

Parameter | Description  
---|---  
`Update Staging Only` | Optional. If selected, the job only updates or notifies for integrations within a manually configured staging environment. This allows you to test updates before pushing changes to production. Enabled by default.  
`Update Enabled Connectors Only` | Optional. If selected, the job only upgrades or generates notifications for connectors that are currently enabled. Disabled connector instances are ignored during the scan. Not selected by default.  
`Mode` | Required. The operational mode for the job. The possible values are as follows:

  * `Notification`: The job scans for updates and generates a platform notification without applying changes.
  * `Upgrade`: The job scans for updates, automatically applies them (mimicking the manual update process in the UI), and generates a confirmation notification.

The default value is `Notification`.  
`Integrations To Ignore` | Optional. A comma-separated list of integration identifiers to skip during the upgrade process. You must use the unique identifier found in the integration details (for example, `GoogleCloudAPI`) rather than the display name.  
`Connectors To Ignore` | Optional. A comma-separated list of connector display names to skip during the upgrade process. This allows for granular control over which specific connector instances are updated.  
`Overwrite Custom Integration` | Optional. If selected, the job upgrades custom integrations originally based on commercial or community versions (including commercial integrations that were exported and then imported back into the platform). **Important:** Enabling this parameter may overwrite custom code changes within the integration. Enabled by default.  
`Ignore Ontology Mapping Update For Integrations` | Optional. A comma-separated list of integration identifiers for which the upgrade process preserves existing ontology mappings. You must use the unique identifier found in the integration details (for example, `GoogleCloudAPI`) rather than the display name. **Note:** Use this parameter to protect custom entity extraction logic or mapping tweaks from being overwritten during an upgrade.   
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
