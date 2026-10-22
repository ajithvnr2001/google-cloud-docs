---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/jira/
title: Integrate Jira with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:43.380443+00:00
---

# Integrate Jira with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/jira/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Jira with Google SecOps

This document explains how to integrate Jira with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Jira.zip).

## Use cases

The **Jira** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated ticketing** : Automatically create Jira issues from Google SecOps alerts using the Jira Connector to streamline the handoff between security and IT teams.

  * **Bidirectional synchronization** : Maintain consistency across platforms by automatically syncing comments and status changes between Jira tickets and Google SecOps cases using dedicated sync jobs.

  * **Incident enrichment** : Attach evidence, logs, and screenshots directly to Jira issues using the Upload Attachment action to provide full context to remediators.

  * **Dynamic task management** : Update, assign, or link related Jira issues directly from the Google SecOps playbook to automate standard operating procedures (SOPs).




## Before you begin

Before you configure the **Jira** integration in the Google SecOps platform, verify that you have the following:

  * **Product compatibility** : Access to either a Jira Cloud instance or a Jira Data Center (On-Prem) environment.

  * **Authentication method** : Choose an authentication method.

    * **Basic authentication (Jira Cloud)** : Requires a username (email) and an Atlassian API Token.
    * **Service account authentication (Jira Cloud)** : Requires a Service Account Token and your Cloud ID.
    * **Standard authentication (Jira Data Center)** : Requires a valid username and password.
  * **API root URL** : The format of the API root depends on your authentication method.

    * **Standard** /**Basic** : The base URL of your Jira instance (for example, `https://yourdomain.atlassian.net`).
    * **Service account** : The Atlassian API proxy URL, which must include your Cloud ID (for example, `https://api.atlassian.com/ex/jira/{cloud_id}`).



### Set up authentication for Jira Cloud

To connect to Jira Cloud using an API token, follow the instructions in the [Atlassian documentation](https://id.atlassian.com/manage/api-tokens) to generate a token.

### Set up authentication for service accounts

To use token-based authentication (Bearer Token) for Jira Cloud:

  1. See [Understand service accounts](https://support.atlassian.com/user-management/docs/understand-service-accounts/) for more details on creating a service account using the [Atlassian Admin console](https://admin.atlassian.com/).

  2. Retrieve your Cloud ID by navigating to: `https://<your_tenant>.atlassian.net/_edge/tenant_info` (where `<your_tenant>` is your specific Atlassian instance name).

  3. When configuring the integration, leave the **Username** field blank to trigger Bearer Token authentication.




## Integration parameters

The **Jira** integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | Required. The base URL of the Jira instance. **Note:** If authenticating using a service account token, the URL must follow this format: `https://api.atlassian.com/ex/jira/{cloud_id}`.   
`Username` | Optional. The username (email) used to connect to Jira. The requirement for this parameter depends on the chosen authentication method:

  * If provided, the system uses Basic authentication.
  * If left empty, the system defaults to Bearer Token authentication (required for service accounts).

For more information on authentication methods, see Before you begin.  
`Api Token` | Required. The authentication credential used to connect to Jira. This field accepts API tokens, service account tokens, or standard passwords (for Data Center).  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Jira server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Comment

Use the **Add Comment** action to compose and add a comment to an existing Jira issue.

This is an effective way to document findings, provide updates, and collaborate with team members directly from Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Comment** action requires the following parameters:

Parameter | Description  
---|---  
`Issue Key` | Required. The unique identifier of the Jira issue (for example, `PROJ-123`).  
`Comment` | Required. The text to add to the Jira issue.  
  
#### Action outputs

The **Add Comment** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment** action:

Script result name | Value  
---|---  
`comment_id` | The unique ID of the newly created comment in Jira.  
  
### Assign Issue

Use the **Assign Issue** action to assign a Jira issue to a specific user.

**Note:** Identification requirements differ across Jira products:

  * Jira Cloud: Matches the assignee by email address first, then by display name.
  * Jira Data Center: Matches the assignee by Jira username.



This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Assign Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue Key` | Required. The unique identifier of the Jira issue (for example, `PROJ-123`).  
`Assignee` | Required. The name or email address of the user to assign the issue to.  
`Jira Username` | Optional. The Jira username of the person initiating the assignment action.  
  
#### Action outputs

The **Assign Issue** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Assign Issue** action:

Script result name | Value  
---|---  
`success` | `true` or `false`  
  
### Create Alert Issue

Use the **Create Alert Issue** action to create a new ticket in Jira for a specific alert.

This action is primarily used within playbooks to escalate security incidents to IT or engineering teams for further investigation or remediation.

**Note:** The Jira API doesn't support creating issues in "next-gen" (team-managed) projects. Ensure you are targeting a standard "classic" (company-managed) project.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Alert Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Project Key` | Required. The unique shorthand key of the Jira project where the issue is created (such as `SEC`).  
`Summary` | Required. A brief title or summary of the issue.  
`Issue Type` | Required. The name of the issue type (such as `Task`, `Bug`, or `Incident`).  
  
#### Action outputs

The **Create Alert Issue** action provides the following outputs:

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

The following example shows the JSON result output received when the action successfully creates an issue:
    
    
    {
       "summary": "Sample issue",
       "description": "Create Enrich entities action using Insights API (IOC search). Write connector for alerts.",
       "project": {
          "key": "PR",
          "name": "Project 1",
          "projectTypeKey": "software"
       },
       "issuetype": {
         "name": "Task",
         "subtask": false
       },
       "status": {
          "name": "DONE",
          "statusCategory": {
             "name": "Done",
             "key": "done"
          }
       },
       "priority": {
          "name": "Medium",
          "id": "3"
       },
       "creator": {
          "displayName": "user1",
          "emailAddress": "john_doe@example.com"
       },
       "assignee": {
          "displayName": "user2",
          "emailAddress": "john_doe@example.com"
       },
       "created": "2018-06-19T15:23:13.701+0300",
       "updated": "2018-09-18T10:02:06.347+0300"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Create Alert Issue** action:

Script result name | Value  
---|---  
`issue_key` | The unique shorthand key of the newly created Jira issue (for example, `SEC-456`).  
  
### Create Issue

Use the **Create Issue** action to create a new ticket in a Jira project.

This action provides extensive customization options, including the ability to specify components, labels, and custom fields using JSON, making it suitable for complex ticket creation workflows.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Issue** action requires the following parameters:

**Note:** Identification requirements for `Assignee` and `Jira Username` differ across Jira products.

See Before you begin for specific instructions on the required identifier format for your environment.

Parameter | Description  
---|---  
`Project Key` | Required. The unique shorthand key of the Jira project where the issue is created (such as `SEC`).  
`Summary` | Required. A brief title or summary of the issue.  
`Description` | Optional. A detailed description of the issue.  
`Issue Type` | Required. The name of the issue type (such as `Task`, `Bug`, or `Incident`).  
`Jira Username` | Optional. The Jira username of the person initiating the action.  
`Assignee` | Optional. The identifier of the user to whom the issue is assigned.  
`Components` | Optional. A comma-separated list of Jira components to associate with the issue.  
`Labels` | Optional. A comma-separated list of labels to add to the issue.  
`Custom Fields` | Optional. A JSON object containing additional fields and values to set during creation (for example, `{"customfield_10001": "Value"}`). Values provided in this parameter take priority and overwrite other field mappings if a conflict occurs.  
  
#### Action outputs

The **Create Issue** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Issue** action:
    
    
    {
       "summary": "Sample issue",
       "description": "Create Enrich entities action using Insights API (IOC search). Write connector for alerts. In a couple of days we will have access to an instance.",
       "project": {
          "key": "PR",
          "name": "Project 1",
          "projectTypeKey": "software"
       },
       "issuetype": {
          "name": "Task",
          "description": "A task that needs to be done.",
          "subtask": false
       },
       "status": {
          "name": "DONE",
          "statusCategory": {
             "name": "Done",
             "key": "done",
             "colorName": "green"
          }
       },
       "priority": {
          "name": "Medium",
          "id": "3"
       },
       "resolution": {
          "name": "Done",
          "description": "Work has been completed on this issue."
       },
       "creator": {
          "displayName": "user1",
          "emailAddress": "john_doe@example.com",
          "active": true,
          "timeZone": "Asia/Jerusalem"
       },
       "assignee": {
          "displayName": "user2",
          "emailAddress": "john_doe@example.com",
          "active": true
       },
       "reporter": {
          "displayName": "user1",
          "emailAddress": "john_doe@example.com"
       },
       "labels": [
          "Label1"
       ],
       "attachment": [
          {
             "id": "1001",
             "filename": "file.rar",
             "mimeType": "binary/octet-stream",
             "size": 15420,
             "created": "2018-06-19T15:23:07.369+0300"
          }
       ],
       "created": "2018-06-19T15:23:13.701+0300",
       "updated": "2018-09-18T10:02:06.347+0300",
       "resolutiondate": "2018-09-18T10:02:06.340+0300",
       "watches": {
          "watchCount": 1,
          "isWatching": false
       }
    }
    

##### Script result

The following table lists the value for the script result output when using the **Create Issue** action:

Script result name | Value  
---|---  
`issue_key` | The unique shorthand key of the newly created Jira issue (for example, `SEC-789`).  
  
### Delete Issue

Use the **Delete Issue** action to permanently remove an issue from Jira.

This action is typically used to clean up duplicate tickets or remove test data generated during playbook development.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue Key` | Required. The unique shorthand key of the Jira issue to delete (for example, `SEC-123`).  
  
#### Action outputs

The **Delete Issue** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Issue** action:

Script result name | Value  
---|---  
`success` | `true` or `false`  
  
### Download Attachments

Use the **Download Attachments** action to retrieve all files attached to a specific Jira issue. If an attachment is an `.eml` file, the action also downloads any files contained within that email.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Download Attachments** action requires the following parameters:

Parameter | Description  
---|---  
`Issue Key` | Required. The unique shorthand key of the Jira issue (for example, `SEC-123`).  
`Download Path` | Optional. The local or internal path to the folder where the action saves the downloaded attachments. The required format depends on your deployment type:

  * **SaaS Deployment** : The path is internal to the hosted platform, such as `/attachments/`.
  * **Remote Agent Deployment** : The path must be an absolute, valid directory path on the local machine where the remote agent is installed. For example, `C:\temp\attachments` for Windows or `/var/tmp/attachments/` for Linux.

  
`Download Attachments to the Case Wall` | Optional. If selected, the action downloads the Jira issue attachments directly to the current Google SecOps case wall. There is a size limitation for attachments added to the case wall. Large files may fail to upload. Disabled by default.  
  
#### Action outputs

The **Download Attachments** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Download Attachments** action:
    
    
    [
      {
        "download_path": "downloads/Security_Evidence.eml",
        "attachment_details": {
          "id": "10007",
          "filename": "Security_Evidence.eml",
          "author": {
            "displayName": "Security Analyst",
            "emailAddress": "analyst@example.com",
            "active": true,
            "timeZone": "Asia/Calcutta"
          },
          "created": "2024-05-25T20:27:09.066+0530",
          "size": 12049140,
          "mimeType": "message/rfc822"
        }
      },
      {
        "download_path": "downloads/Logs_Attachment.txt",
        "attachment_details": {
          "id": "10005",
          "filename": "Logs_Attachment.txt",
          "author": {
            "displayName": "System Admin",
            "emailAddress": "admin@example.com",
            "active": true,
            "timeZone": "Asia/Calcutta"
          },
          "created": "2024-05-16T11:48:24.141+0530",
          "size": 43,
          "mimeType": "text/plain"
        }
      }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Download Attachments** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Issues

Use the **Get Issues** action to retrieve full details for one or more Jira issues.

This action is useful for enriching Google SecOps cases with current ticket metadata (such as status, assignee, and priority).

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Issues** action requires the following parameters:

Parameter | Description  
---|---  
`Issue Keys` | Required. A comma-separated list of Jira issue keys to fetch (for example, `SEC-123, SEC-456`).  
  
#### Action outputs

The **Get Issues** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Issues** action:
    
    
    {
      "issues_details_list": [
        {
          "key": "TES-65",
          "summary": "New summary",
          "description": "Detailed description of the security incident.",
          "project": {
            "key": "TES",
            "name": "test-project1",
            "projectTypeKey": "software"
          },
          "issuetype": {
            "name": "Bogue",
            "subtask": false
          },
          "status": {
            "name": "Fini",
            "statusCategory": {
              "name": "Terminé",
              "key": "done"
            }
          },
          "priority": {
            "name": "Medium",
            "id": "3"
          },
          "assignee": {
            "displayName": "Vasil Daskalov",
            "emailAddress": "vasil.daskalov@siemplify.co"
          },
          "creator": {
            "displayName": "admin@siemplifylab.local",
            "emailAddress": "admin@siemplifylab.local"
          },
          "created": "2021-08-31T12:15:22.089+0000",
          "updated": "2021-11-11T13:16:50.552+0000",
          "resolution": {
            "name": "Terminé",
            "description": "Ce ticket a été traité."
          },
          "labels": [],
          "components": []
        }
      ]
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get Issues** action:

Script result name | Value  
---|---  
`issues_details_list` | A list containing the full metadata for the requested Jira issues.  
  
### Link Issues

Use the **Link Issues** action to establish a relationship between multiple Jira issues.

This action is primarily used within playbooks to connect related security incidents or to track dependencies between investigation tickets.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Link Issues** action requires the following parameters:

Parameter | Description  
---|---  
`Inward Issue ID` | Required. A comma-separated list of inward issue IDs. For example, if `Relation Type` is set to `Blocks`, this issue displays the relationship `is blocked by` in the Jira UI.  
`Outward Issue IDs` | Required. The shorthand key of the outward Jira issue. For example, if `Relation Type` is set to `Blocks`, this issue displays the relationship `blocks` in the Jira UI.  
`Relation Type` | Required. The type of link to create between the issues. You can find a list of available relation types by running the List Relation Types action. The default value is `Blocks`.  
  
#### Action outputs

The **Link Issues** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Link Issues** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully linked issue ISSUE_ID with the following issues in Jira: ISSUE_IDS.` Action wasn't able to find the following destination issues in Jira: ISSUE_IDS. | The action succeeded  
`Error executing action "Link Issues". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Link Issues** action:

Script result name | Value  
---|---  
`success` | `true` or `false`  
  
### List Issues

Use the **List Issues** action to search for and retrieve a list of Jira issue keys based on specific filtering criteria.

This action is useful for identifying existing tickets that match an alert context to avoid duplication or to perform bulk updates within a playbook.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Issues** action provides the following optional filtering parameters. If no parameters are provided, the action returns all issues accessible by the integration user.

Parameter | Description  
---|---  
`Project Names` | Optional. A comma-separated list of project names to search within.  
`Summary` | Optional. If provided, the action filters issues by the specific summary or title.  
`Description` | Optional. If provided, the action filters issues by text contained in the description.  
`Issue Types` | Optional. A comma-separated list of issue types (for example, `Bug,Task`). The default value is `Bug`.  
`Priorities` | Optional. A comma-separated list of priority levels to filter by (for example, `High,Medium`).  
`Created From` | Optional. If provided, the action filters for issues created on or after this date (in the format `YYYY/MM/DD`).  
`Updated From` | Optional. If provided, the action filters for issues updated on or after this date (in the format `YYYY/MM/DD`).  
`Assignees` | Optional. A comma-separated list of assignee identifiers to filter by.  
`Reporter` | Optional. A comma-separated list of reporter identifiers to filter by.  
`Statuses` | Optional. A comma-separated list of issue statuses to filter by (for example, `Open,In Progress`).  
`Created Before` | Optional. The latest creation date to filter by. Format: `YYYY/MM/DD` or relative offset (for example, `-24h`, `-7d`). If not provided, filter will not be used.  
`Custom JQL` | Optional. Custom JQL query. If provided, all other filters will be ignored.  
  
#### Action outputs

The **List Issues** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Issues** action:
    
    
    [ 
      "PR-123", 
      "PR-124",
      "SEC-789"
    ]
    

##### Script result

The following table lists the value for the script result output when using the **List Issues** action:

Script result name | Value  
---|---  
`issues` | A list containing the unique shorthand keys of the Jira issues found.  
  
### List Relation Types

Use the **List Relation Types** action to retrieve a list of all available link relationship types configured in your Jira instance.

This action is useful for validating valid input values for the Link Issues action.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Relation Types** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | Optional. The field used to filter the relation types. If the **Filter Logic** is set to `Equal` or `Contains`, you must select a field other than `Select One` to avoid an execution error. The possible values are as follows:

  * `Name`
  * `Inward`
  * `Outward`

The default value is `Select One`.  
`Filter Logic` | Optional. The logical operator applied to the filter. The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | Optional. The specific string value used for filtering based on the selected `Filter Key` and `Filter Logic`. If no value is provided, the filter is not applied even if a key and logic are selected.  
`Max Records To Return` | Optional. The maximum number of records to return in the results. The default value is `50`.  
  
#### Action outputs

The **List Relation Types** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Relation Types** action provides the following table:

Table name: **Available Relation**

Table columns:

  * **Name**
  * **Inward**
  * **Outward**



##### JSON result

The following example shows the JSON result output received when using the **List Relation Types** action:
    
    
    [{
        "id": "10000",
        "name": "Blocks",
        "inward": "is blocked by",
        "outward": "blocks"
    }]
    

##### Output messages

The **List Relation Types** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found relation types for the provided criteria in Jira.` `The filter was not applied, because parameter "Filter Value" has an empty value.` | The action succeeded.  
`Error executing action "List Relation types". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Relation Types** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Jira.

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
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`success` | `true` or `false`  
  
### Update Issue

#### Description

Update an issue. For the new Jira API, the action tries to find a match for the assignee to assign an issue based on user email, and then tries with the displayName field.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Issue Key | String | N/A | Yes | The key of the issue to update.  
Status | String | N/A | No | Specify the relevant transition name, to transition this issue to the new desired status.  
Summary | String | N/A | No | The new summary of the issue.  
Description | String | N/A | No | The new description of the issue.  
Issue Type | String | N/A | No | The new type of the issue.  
Assignee | String | N/A | No | The new assignee of the issue.  
Jira Username | String | N/A | No | The Jira username of the action initiator.  
Components | String | N/A | No | The components field of the issue. This parameter accepts multiple values as a comma-separated string.  
Custom Fields | JSON | NA | No | Specify a JSON object containing all of the fields and values that are used during issue creation. **Note:** This parameter has priority and all of the fields are overwritten with the value that is provided for this parameter. Example: {"field":"value"}  
Labels | String | N/A | No | The components field of the issue. This parameter accepts multiple values as a comma-separated string.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
Success | True/False | Success:False  
  
##### JSON Result
    
    
    {
       "comment":
         {
           "total": 0,
           "startAt": 0,
           "comments": [],
           "maxResults": 0
          },
       "creator":
         {
           "displayName": "user1",
           "name": "user1",
           "self": "",
           "avatarUrls":
              {
                "24x24": "",
                "16x16": "",
                "48x48": "",
                "32x32": ""
               },
            "emailAddress": "john_doe@example.com",
            "key": "user1user",
            "active": true,
            "timeZone": "Asia/Jerusalem",
            "accountId": "0"
           },
       "aggregatetimeestimate": null,
       "labels": ["Label1"],
       "aggregatetimespent": null,
       "watches":
          {
            "self": "",
            "watchCount": 1,
            "isWatching": false
           },
       "assignee":
          {
            "displayName": "user2",
            "name": "user2",
            "self": "",
            "avatarUrls":
               {
                  "24x24": "",
                  "16x16": "",
                  "48x48": "",
                  "32x32": ""
                },
            "emailAddress": "john_doe@example.com",
            "key": "user2",
            "active": true,
            "timeZone": "Asia/Jerusalem",
            "accountId": ""
           },
       "lastViewed": "2019-01-22T10:14:02.910+0200",
       "issuelinks": [],
       "Worklog":
          {
            "worklogs": [],
            "total": 0,
            "startAt": 0,
            "maxResults": 20
           },
       "aggregateprogress":
          {
            "progress": 0,
            "total": 0
           },
       "Priority":
          {
            "iconUrl": "",
            "self": "",
            "name": "Medium",
            "id": "3"
           },
       "votes":
           {
              "hasVoted": false,
              "self": "",
              "votes": 0
            },
       "workratio": -1,
       "fixVersions": [],
       "environment": null,
       "timespent": null,
       "attachment":
          [{
              "mimeType": "binary/octet-stream",
              "created": "2018-06-19T15:23:07.369+0300",
              "self": "",
              "author":
                 {
                   "displayName": "user1",
                   "name": "user1",
                   "self": "",
                   "avatarUrls":
                      {
                         "24x24": "",
                         "16x16": "",
                         "48x48": "",
                         "32x32": ""
                       },
                   "emailAddress": "john_doe@example.com",
                   "key": "user1",
                   "active": true,
                   "timeZone": "Asia/Jerusalem",
                   "accountId": "0"
                  },
               "filename": "file.rar",
               "content": "",
               "id": "0",
               "size": 0
            }],
       "progress":
            {
              "progress": 0,
              "total": 0
             },
       "duedate": null,
       "status":
            {
              "statusCategory":
                  {
                     "name": "Done",
                     "self": "",
                     "id": 3,
                     "key": "done",
                     "colorName": "green"
                   },
              "description": "",
              "self": "",
              "iconUrl": "",
              "id": "0",
              "name": "DONE"
             },
       "updated": "2018-09-18T10:02:06.347+0300",
       "subtasks": [],
       "description": "Create Enrich entities action using Insights API (IOC search)\\n\\nWrite connector for laerts\\n\\nIn a couple of days we will have access to an instance",
       "reporter":
             {
               "displayName": "user1",
               "name": "user1",
               "self": "",
               "avatarUrls":
                   {
                     "24x24": "",
                     "16x16": "",
                     "48x48": "",
                     "32x32": ""
                   },
               "emailAddress": "john_doe@example.com",
               "key": "user1",
               "active": true,
               "timeZone": "Asia/Jerusalem",
               "accountId": "0"
              },
        "timeoriginalestimate": null,
        "aggregatetimeoriginalestimate": null,
        "created": "2018-06-19T15:23:13.701+0300",
        "versions": [],
        "resolutiondate": "2018-09-18T10:02:06.340+0300",
        "summary": "Sample issue",
        "project":
              {
                 "name": "Project 1",
                 "self": "",
                 "projectTypeKey": "software",
                 "avatarUrls":
                     {
                       "24x24": "",
                       "16x16": "",
                       "48x48": "",
                       "32x32": ""
                      },
                 "key": "PR",
                 "id": "0"
               },
        "timetracking": {},
        "components": [],
        "issuetype":
              {
                 "name": "Task",
                 "self": "",
                 "iconUrl": "",
                 "subtask": false,
                 "avatarId": 10318,
                 "id": "10002",
                 "description": "A task that needs to be done."
               },
        "security": null,
        "resolution":
               {
                 "id": "10000",
                 "self": "",
                 "description": "Work has been completed on this issue.",
                  "name": "Done"
                 },
        "timeestimate": null
    }
    

### Upload Attachment

#### Description

Add an attachment to an issue.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Issue Key | String | N/A | Yes | File Paths.  
File Paths | String | N/A | Yes | The absolute paths of the files to upload, separated by commas. The required format depends on your deployment type:

  * **SaaS Deployment** : The path is internal to the hosted platform, such as `/attachments/`.
  * **Remote Agent Deployment** : The path must be an absolute, valid directory path on the local machine where the remote agent is installed. For example, `C:\temp\attachments` for Windows or `/var/tmp/attachments/` for Linux.

  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Search Users

Search users in Jira. 

**Note:** To obtain more accurate results, provide the `User Email Addresses` parameter. 

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`User Email Addresses` | _Optional_ Comma-separated list of email addresses to return the users for.  
`User Names` | _Optional_ Comma-separated list of usernames to return the users for.  
`Project` | _Optional_ Name of the project to search email addresses in. If provided, only `Project Assignable Users` is returned.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | Available  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    [
     {
       "Entity": "example",
       "EntityResult": {
         "_resource": "user?accountId={0}",
         "_options": {
           "server": "https://siemplify.atlassian.net",
           "auth_url": "/rest/auth/1/session",
           "context_path": "/",
           "rest_path": "api",
           "rest_api_version": "2",
           "agile_rest_path": "agile",
           "agile_rest_api_version": "1.0",
           "verify": false,
           "resilient": true,
           "async": false,
           "async_workers": 5,
           "client_cert": null,
           "check_update": false,
           "delay_reload": 0,
           "headers": {
             "Cache-Control": "no-cache",
             "Content-Type": "application/json",
             "X-Atlassian-Token": "no-check"
           }
         },
         "_session": "<jira.resilientsession.ResilientSession object>",
         "_base_url": "{server}/rest/{rest_path}/{rest_api_version}/{path}",
         "raw": {
           "self": "https://siemplify.atlassian.net/rest/api/2/user?accountId=example-account-id",
           "accountId": "example-account-id",
           "accountType": "atlassian",
           "emailAddress": "example.user",
           "avatarUrls": {
             "48x48": "https://example.com"
           },
           "displayName": "Example",
           "active": true,
           "timeZone": "UTC",
           "locale": "en_US"
         },
         "self": "https://siemplify.atlassian.net/rest/api/2/user?accountId=example-account-id",
         "accountId": "example-account-id",
         "accountType": "atlassian",
         "emailAddress": "example.user",
         "avatarUrls": "<jira.resources.PropertyHolder object>",
         "displayName": "Example",
         "active": true,
         "timeZone": "UTC",
         "locale": "en_US"
       }
     }
    ]
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found the following users in Jira for project PROJECT_NAME: USER_LIST` `The following users were not found in Jira for project PROJECT_NAME: USER_LIST` `None of the provided users were found in the project PROJECT_NAME` | Action succeeded.  
`Error executing action "Search Users". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### Closed Reason Mapping Configuration

The `Closed Reason Mapping` parameter requires a JSON structure. You can map static values or pass dynamic Jira field names (for example, `resolution`, `customfield_10010`). If an extracted dynamic reason is invalid or missing, the job automatically uses the specified `Fallback` mapping.

Example JSON configuration:
    
    
    {
      "Done": {
        "reason": "Maintenance",
        "root_cause": "Other"
      },
      "Fallback": {
        "reason": "Maintenance",
        "root_cause": "Other"
      }
    }
    

## Connectors

### Jira Connector

#### Description

Fetch issues from Jira to Google SecOps.

#### Configure Jira Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter | Description  
---|---  
`DeviceProductField` | Required. The field name used to determine the device product. The default value is `device_product`.  
`EventClassId` | Optional. The field name used to determine the event name (sub-type). The default value is `name`.  
`PythonProcessTimeout` | Required. The timeout limit (in seconds) for the python process running current script. The default value is `60`.  
`API Root` | Required. The API root of the Jira instance. **Note:** If authenticating using service account token, the URL must follow this format: `https://api.atlassian.com/ex/jira/{cloud_id}`. The default value is `https://{jira_address}`.  
`Username` | Optional. The username (email) used to connect to Jira. The requirement for this parameter depends on the chosen authentication method:

  * If provided, the system uses Basic authentication.
  * If left empty, the system defaults to Bearer Token authentication (required for service accounts).

For more information on authentication methods, see Before you begin.  
`API Token` | Required. The authentication credential used to connect to Jira. **Note:** This field accepts API tokens, service account tokens, or standard passwords (for Data Center).   
`Days Backwards` | Optional. Max number of days backwards to pull alerts from. The default value is `5`.  
`Max Tickets Per Cycle` | Optional. Max tickets to fetch and process in one connector cycle. The default value is `10`.  
`Project Names` | Optional. Project names separated by a comma.  
`Issue Statuses` | Optional. Issues' statuses separated by a comma.  
`Assignees` | Optional. Users' full names separated by a comma.  
`Issue Types` | Optional. Issue types separated by a comma.  
`Issue Priorities` | Optional. Issue priorities separated by a comma.  
`Issue Components` | Optional. Issue components separated by a comma.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The proxy username to authenticate with.  
`Proxy Password` | Optional. The proxy password to authenticate with.  
`Environment Field Name` | Optional. Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regex pattern to run on the value found in the "Environment Field Name" field. Used to allow the user to manipulate the environment field using regex logic. The default value is `.*`.  
`Use Jira Project as Environment` | Optional. Use Jira project as environment or use Environment Field Name as environment.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Jira server. Enabled by default.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

##### Dynamic list and blocklist

The connector supports dynamic list and blocklist rules only for specific labels inside Jira.

## Jobs

### Sync Closure Job

#### Description

Close tickets in Jira if corresponding Google SecOps alerts or cases were closed, and synchronize closure status and custom fields from Jira back to Google SecOps.

**Important:** Set the context key **`JIRA_ISSUE_KEY`** at both the case level and the alert level when testing or running the job on manual cases.

#### Parameters

Parameter | Description  
---|---  
`API Root` | Required. Jira instance API root URL. **Note:** If authenticating using a service account token, the URL must follow this format: `https://api.atlassian.com/ex/jira/{cloud_id}`. The default value is `https://{jira_address}`.  
`Username` | Optional. The username (email) used to connect to Jira. The requirement for this parameter depends on the chosen authentication method:

  * If provided, the system uses Basic authentication.
  * If left empty, the system defaults to Bearer Token authentication (required for service accounts).

  
`API Token` | Required. The authentication credential used to connect to Jira. **Note:** This field accepts API tokens, service account tokens, or standard passwords (for Data Center).   
`Project Names` | Required. Jira project names separated by a comma that job should monitor. The default value is `project names separated by a comma`.  
`Environment` | Optional. The environment name.  
`Days Backwards` | Required. Maximum number of days to sync tickets status backward. The default value is `1`.  
`Job Scope` | Required. Scope for the job synchronization. Options:

  * `Case`: Syncs Jira issues at the case level. Ensure the context contains the `JIRA_ISSUE_KEY`.
  * `Alert`: Syncs Jira issues at the alert level. For connector-created cases, the Jira ticket key is extracted automatically. For simulated cases, manually set the context key to `JIRA_ISSUE_KEY`.

The default value is `Alert`.  
`Supported Closed Statuses` | Required. Comma-separated list of Jira closed statuses treated as closed in Google SecOps (for example, `Done, Closed`).

  * **SecOps to Jira:** The job uses the first value in the list (for example, `Done`) as the resolution status when closing the Jira ticket.
  * **Jira to SecOps:** The closing status of the Jira ticket must exist within this list for synchronization to occur.

The default value is `Done`.  
`Closed Reason Mapping` | Required. JSON dictionary mapping Jira closed statuses to Google SecOps closure reasons and root causes. Supports mapping to custom fields and requires a mandatory `Fallback` key. For configuration details and examples, see Closed reason and custom field mapping.  
`Custom Fields Mapping` | Optional. JSON object defining mappings between Google SecOps custom field display names and Jira custom field names for data sync from Jira to Google SecOps. For configuration details and examples, see Closed reason and custom field mapping.  
  
#### Closed reason and custom field mapping

Use the following details and examples to configure custom mappings for closed reasons and custom fields.

**Closed Reason Mapping**

Defines how Jira closure statuses map to Google SecOps case or alert closure reasons and root causes.

  * **Standard JSON Mapping Example:**
        
        {
          "Done": {
            "reason": "Malicious",
            "root_cause": "Other"
          },
          "Fallback": {
            "reason": "Maintenance",
            "root_cause": "Other"
          }
        }
        

If a Jira ticket closes with the status `Done`, the Google SecOps case or alert closes with reason `Malicious` and root cause `Other`. If the ticket closes with a status not explicitly mapped (for example, `Closed`), the system defaults to the `Fallback` settings.

  * **Custom Field Mapping Example:**

If you have custom fields in Jira named `Jira reason` and `Jira rootcause`, configure the JSON mapping as follows:
        
        {
          "Done": {
            "reason": "Jira reason",
            "root_cause": "Jira rootcause"
          },
          "Fallback": {
            "reason": "Maintenance",
            "root_cause": "Other"
          }
        }
        

**Requirements:**

    * The value extracted from the `Jira reason` custom field must resolve to one of the following exact strings: `Malicious`, `Maintenance`, `Inconclusive`, or `Not malicious`. Otherwise, the system reverts to the `Fallback` values.
    * For the `Case` job scope, root cause values must be configured in the admin settings. For the `Alert` job scope, no admin configuration is required, and any value provided in the custom field is accepted.



**Custom Fields Mapping**

This mapping functions exclusively to synchronize custom field values from Jira to Google SecOps. Specify key-value pairs where the key is the Google SecOps custom field display name and the value is the Jira custom field name:
    
    
    {
      "SOAR Custom field": "Jira ticket id"
    }
    

In this example, the value from the Jira field `Jira ticket id` syncs directly to the Google SecOps field `SOAR Custom field`.

### Sync Comments Job

#### Description

Sync comments between the Google SecOps case and the corresponding Jira ticket. Synchronizing is bidirectional—that is, from Google SecOps to Jira and from Jira to Google SecOps.

When the job creates a comment, it applies the prefix. If a Google SecOps user comments in the Google SecOps case, the job creates and synchronizes the user comment in the corresponding Jira ticket using the **Chronicle Comment Prefix** parameter.

This feature is added for two purposes:

  1. Visibility.
  2. Prevent comments added by the job from being synced again to the other side, and cause a loop.

**Note:** This job only supports Google SecOps cases with the `Jira` tag. 

The job uses the `TICKET_ID` value stored in the case context to identify the corresponding issue in Jira. This value is automatically populated in the case context when a ticket is created using the Create Issue or Create Alert Issue actions.

#### Parameters

Parameter | Description  
---|---  
`API Root` | Required. Jira instance API root URL. **Note:** If authenticating using a service account token, the URL must follow this format: `https://api.atlassian.com/ex/jira/{cloud_id}`. The default value is `https://{jira_address}`.  
`Username` | Optional. The username (email) used to connect to Jira. The requirement for this parameter depends on the chosen authentication method:

  * If provided, the system uses Basic authentication.
  * If left empty, the system defaults to Bearer Token authentication (required for service accounts).

  
`API Token` | Required. The authentication credential used to connect to Jira. **Note:** This field accepts API tokens, service account tokens, or standard passwords (for Data Center).   
`Project Names` | Required. Jira project names separated by a comma that job should monitor. The default value is `project names separated by comma`.  
`Environment` | Optional. The environment name.  
`Siemplify Comment Prefix` | Required. Prefix that is added by the sync job to comments created for Jira tickets. The default value is `Google SecOps:`.  
`Jira Comment Prefix` | Required. Prefix that is added by the sync job to the Google SecOps alert case comments. The default value is `Jira Comment Sync Job:`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
