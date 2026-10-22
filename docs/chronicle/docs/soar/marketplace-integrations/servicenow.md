---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/servicenow/
title: Integrate ServiceNow with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:51.257181+00:00
---

# Integrate ServiceNow with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate ServiceNow with Google SecOps 

This document explains how to integrate ServiceNow with Google Security Operations (Google SecOps).

## Use cases

The **ServiceNow** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated incident ticketing** : Automatically create ServiceNow incidents from security alerts originating in your SIEM or other security tools.

  * **Incident enrichment and response** : Streamline incident response workflows by reducing manual ticketing and enriching incidents with relevant information from the originating alert.

  * **Phishing remediation** : Automate repetitive phishing investigation steps such as gathering email headers, investigating attachments, and searching for similar emails, which accelerates response times.

  * **Vulnerability remediation orchestration** : Orchestrate vulnerability remediation workflows by automatically creating ServiceNow change requests for patching or mitigating actions based on vulnerability scan results.

  * **User lifecycle automation** : Automate user provisioning and de-provisioning tasks in various systems (access control, email platforms, applications) based on triggers from ServiceNow workflows.

  * **Threat intelligence context** : Enrich security alerts with threat intelligence data sourced directly from the ServiceNow platform, providing more context for analysts to prioritize response actions.




## Before you begin

Before you configure the integration in the Google SecOps platform, ensure you have completed the following prerequisites:

  * **ServiceNow user account** : A dedicated user account with sufficient permissions to query, create, and update target records.
  * **ServiceNow roles** : Ensure the account has the required system roles (`sn_incident_write` and `itil`) and a custom user access configuration to allow access to read journal comments.
  * **Network connectivity** : A network configuration that allows traffic from Google SecOps IP addresses or your remote agent infrastructure to reach your ServiceNow instance endpoint.
  * **Authentication details** : Determine your organization's authentication policy. You can authenticate using standard Basic Authentication or OAuth 2.0 authentication.



### Configure user access in ServiceNow

To allow the integration to synchronize comments, update fields, and execute actions seamlessly, you must perform the following administrative tasks in the ServiceNow platform.

For specific instructions on how to navigate the ServiceNow interface, see the official [ServiceNow product documentation](https://docs.servicenow.com/).

  1. **Create a custom role** : Navigate to **Roles > New** and create a new role dedicated to handling API comment access.
  2. **Create a new Access Control List (ACL) rule** : The integration requires read access to the `sys_journal_field` table to track comments and work notes. Navigate to **Access Controls > New**. You must sign in with an account that has elevated permissions to create this rule.
  3. **Configure the ACL parameters** :

     * Set **Type** to `record`.
     * Set **Operation** to `read`.
     * In the **Name** fields, select **Journal Entry`sys_journal_field`** from the first drop-down, and select **\-- None --** from the second drop-down.
**Important:** The second drop-down must be explicitly set to `-- None --`. If you select `*` (wildcard), the API will fail to retrieve comments.
     * Go to the **Requires role** list at the bottom of the form and add your newly created custom comment role. Click **Submit**.
  4. **Assign roles to the integration account** : Navigate to **Users** , open your dedicated integration account, and grant the following roles:

     * The custom role you created to read comments.
     * `sn_incident_write`: Required for basic interaction, such as the **Get Incident** and **Update Incident** actions.
     * `itil`: Required for CMDB actions and related asset configuration management lookup functions.
**Note:** These roles provide the baseline permissions needed to interact with standard incidents and configuration entities. Accessing other ServiceNow tables may require additional role configuration based on your environment's unique ACL constraints.



## Authentication configuration options

The ServiceNow integration supports three different authentication methods. Choose one of the following configuration options that aligns with your organization's security requirements.

### Option 1: OAuth 2.0 Client Credentials Flow (Recommended)

This method uses an OAuth 2.0 Client Credentials Grant alongside user impersonation to safely restrict data access without exposing a static user password to the platform.

#### Phase 1: Create an OAuth endpoint in ServiceNow

  1. Search for **Application Registries** in the ServiceNow navigation menu and click **New**.
  2. Select **New Inbound Integration Experience**.
  3. From the connection type list, select **OAuth - Client credentials grant**.
  4. In the **Name** field, provide a descriptive name for the endpoint configuration.
  5. Provide the **OAuth Provider** name or identifier required to establish the identity profile context.
  6. In the **OAuth application user** field, select the dedicated ServiceNow user account that will be impersonated and used for all automated API activities.
  7. Click **Submit** or **Save**.
  8. Re-open the newly created registry record to copy and secure the generated **Client ID** and **Client Secret**.

**Note:** If you open this credential object directly from the classic "Application Registry" view, the **Default Grant type** field automatically populates as `Resource Owner Password Credentials`. Keep this default setting as-is.

#### Phase 2: Configure inside Google SecOps

  1. In **Google SecOps** , navigate to **Response > Integrations Setup** and open the ServiceNow configuration window.
  2. Enter your **Api Root** (replacing the default placeholder domain with your actual ServiceNow instance URL).
  3. Provide the **Client ID** and **Client Secret** generated during Phase 1.
  4. Ensure the **Username** , **Password** , and **Refresh Token** fields are left completely blank.
  5. Enable the **Use Oauth Authentication** checkbox setting.
  6. Click **Test** to validate parameters using a connectivity ping test. If successful, click **Save**.



### Option 2: Basic Authentication

This method uses direct credential validation. It is straightforward to set up but may be restricted if your enterprise enforces multi-factor authentication (MFA) or blocks basic auth headers.

  1. In ServiceNow, verify that your integration user has a local **Username** and **Password**.
  2. When configuring the integration in Google SecOps, provide the **Api Root** (replacing the default placeholder domain with your actual ServiceNow instance URL), **Username** , and **Password**.
  3. Leave the OAuth-related fields blank and ensure `Use Oauth Authentication` is turned off (checkbox cleared).
  4. Click **Test** to validate the connection parameters. If successful, click **Save**.



### Option 3: Refresh Token Flow

Use this method if your organization requires OAuth security controls using a refresh token chain to programmatically fetch access tokens behind the scenes.

  1. Complete Phase 1 in your ServiceNow instance to generate a **Client ID** and **Client Secret**.
  2. Complete the steps in the Generate a Refresh Token section to retrieve a valid authorization token string.
  3. In **Google SecOps** , open your ServiceNow integration instance configuration window.
  4. Populate the parameters completely using your configured credentials: 
     * **Api Root** (replacing the default placeholder domain with your actual ServiceNow instance URL).
     * **Username**
     * **Password**
     * **Client ID**
     * **Client Secret**
  5. Select the **Use Oauth Authentication** checkbox.
  6. Paste the token string you retrieved from the Generate a Refresh Token section workflow into the **Refresh Token** field.
  7. Click **Test** to validate the connection parameters. If successful, click **Save**.



#### Generate a Refresh Token (Google SecOps)

To generate the refresh token, you must temporarily configure the integration to run a helper action.

  1. In **Google SecOps** , go to **Response > Integrations Setup**.
  2. Ensure the **Use Oauth Authentication** checkbox remains unmarked for this initial setup step.
  3. Configure a temporary ServiceNow integration instance using the **Api Root** , **Username** , **Password** , **Client ID** , and **Client Secret** , and click **Save**.
  4. Simulate a case or open an existing case.
  5. Run the ServiceNow **Get Oauth Token** action [manually](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action) on the case.
  6. Copy the `refresh_token` value from the action's JSON result to use in the **Refresh Token** field when configuring the final integration instance.



## Integration parameters

The ServiceNow integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | Required. The API root of the ServiceNow instance. The default value is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | Required. The username of the ServiceNow account.  
`Password` | Required. The password of the ServiceNow account.  
`Incident Table` | Optional. The API table name or path to use for incident-related actions and record retrieval. By default, the integration uses the `table/incident` path.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
`Client ID` | Optional. The client ID for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Client Secret` | Optional. The client secret for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Refresh Token` | Optional. The refresh token for the ServiceNow integration, required for OAuth 2.0 authentication using a refresh token. This configured refresh token expires every 90 days. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Use Oauth Authentication` | Optional. If selected, the integration uses OAuth 2.0 to authenticate. OAuth 2.0 authentication requires setting either the client credentials (`Client ID` and `Client Secret`) or `Refresh Token`. Disabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Attachment

Use the **Add Attachment** action to add attachments to a table record in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Attachment** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the table containing the record where the attachment is added.  
`Record Sys ID` | Required. The system ID (`sys_id`) of the record where the attachment is added.  
`File Path` | Required. A comma-separated list of absolute paths for the files to attach.  
`Mode` | Optional. The behavior of the action when a file with the same name already exists on record. The possible values are as follows:

  * `Add New Attachment`: The action adds the file as a new, separate attachment. Files with the same name are allowed.
  * `Overwrite Existing Attachment`: The action replaces the existing attachment that shares the same name.

The default value is `Add New Attachment`.  
  
#### Action outputs

The **Add Attachment** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Attachment** action:
    
    
    {
        "result": {
            "size_bytes": "742",
            "file_name": "placeholder_document.txt",
            "sys_mod_count": "0",
            "average_image_color": "",
            "image_width": "",
            "sys_updated_on": "2025-01-01 10:00:00",
            "sys_tags": "",
            "table_name": "incident",
            "sys_id": "TEST_SYS_ID_ATTACH_123456789",
            "image_height": "",
            "sys_updated_by": "admin",
            "download_link": "https://placeholder.service-now.com/api/now/attachment/TEST_SYS_ID_ATTACH_123456789/file",
            "content_type": "multipart/form-data",
            "sys_created_on": "2025-01-01 10:00:00",
            "size_compressed": "438",
            "compressed": "true",
            "state": "pending",
            "table_sys_id": "TEST_SYS_ID_RECORD_ABCDEFG",
            "chunk_size_bytes": "700000",
            "hash": "test_hash_0000000000000000000000000000000000000000000000000000000000000000",
            "sys_created_by": "admin"
        }
    }
    

##### Output messages

The **Add Attachment** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following attachments to the record with a Sys ID RECORD_SYS_ID from a table TABLE_NAME in ServiceNow: FILE_PATHS` `Action wasn't able to add the following attachments to the record with a Sys ID RECORD_SYS_ID from a table TABLE_NAME in ServiceNow: FILE_PATHS` `No attachments were added to the record with a Sys ID RECORD_SYS_ID from a table TABLE_NAME in ServiceNow: FILE_PATHS` | The action succeeded.  
`Error executing action "Add Attachment". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Attachment** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Comment

Use the **Add Comment** action to add a comment to a ServiceNow incident.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Comment** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The number of the incident to add the comment to, in the format `INCINCIDENT_NUMBER`.  
`Comment` | Required. The comment to add to the incident.  
  
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

The following table lists the values for the script result output when using the **Add Comment** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Comment and Wait for Reply

Use the **Add Comment and Wait for Reply** action to add a comment to a ServiceNow incident, then pause the playbook execution until a new comment or reply is added to that incident. The output of the action is the content of the new comment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Comment and Wait for Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The number of the incident to add the comment to, in the format `INCINCIDENT_NUMBER`.  
`Comment` | Required. The comment to add to the incident.  
  
#### Action outputs

The **Add Comment and Wait for Reply** action provides the following outputs:

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

The following table lists the value for the script result output when using the **Add Comment and Wait for Reply** action:

Script result name | Value  
---|---  
`new_comment` |   
  
### Add Comment To Record

Use the **Add Comment To Record** action to add a comment or work note to a specific table record in ServiceNow.

This action doesn't run on Google SecOps entities. 

**Note:** If you enable the `Wait For Reply` parameter, the action runs in asynchronous mode. When using asynchronous mode, adjust the script timeout value in the Google SecOps IDE based on the expected wait time for a reply.

#### Action inputs

The **Add Comment To Record** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the table to add the comment or note to.  
`Type` | Required. The type of comment or note to add. The possible values are as follows:

  * `Comment`
  * `Work Note`

The default value is `Comment`.  
`Record Sys ID` | Required. The system ID (`sys_id`) to add the comment or work note to.  
`Text` | Required. The content of the comment or work note.  
`Wait For Reply` | Optional. If selected, the action runs asynchronously and pauses execution until a new comment or work note is added to the record. The action tracks comments if you add a comment, and work notes if you add a work note. **Note:** If enabled, this action runs in asynchronous mode. Adjust the script timeout value in the Google SecOps IDE based on the expected wait time for a reply. Disabled by default.  
  
#### Action outputs

The **Add Comment To Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Comment To Record** action:
    
    
    {
        "sys_id": "4355183607523010ff23f6fd7c1ed0a8",
        "sys_created_on": "2021-09-03 10:29:48",
        "name": "incident",
        "element_id": "552c48888c033300964f4932b03eb092",
        "sys_tags": "",
        "value": "Test comment content.",
        "sys_created_by": "admin",
        "element": "comments"
    }
    

##### Output messages

The **Add Comment To Record** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added  COMMENT_OR_NOTE " CONTENT" to TABLE_NAME with Sys_ID SYS_ID in ServiceNow. ` | The action succeeded.  
`Error executing action "Add Comment To Record". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Record** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Parent Incident

Use the **Add Parent Incident** action to add a parent incident for incidents in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Parent Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Parent Incident Number` | Required. The parent incident number, in the format `INCINCIDENT_NUMBER` (for example, `INC0000051`). The action adds all incidents in `Child Incident Numbers` as children for the parent incident.  
`Child Incident Numbers` | Required. A comma-separated list of incident numbers to set as child incidents for the specified parent incident, in the format `INCINCIDENT_NUMBER` (for example, `INC0000051`).  
  
#### Action outputs

The **Add Parent Incident** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Parent Incident** action:
    
    
    {
        "result": [
            {
                "parent": "",
                "made_sla": "true",
                "caused_by": "",
                "watch_list": "",
                "upon_reject": "cancel",
                "sys_updated_on": "2020-10-20 07:19:11",
                "child_incidents": "0",
                "hold_reason": "",
                "approval_history": "",
                "skills": "",
                "number": "INC0010009",
                "resolved_by": "",
                "sys_updated_by": "admin",
                "opened_by": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "user_input": "",
                "sys_created_on": "2020-10-20 07:19:11",
                "sys_domain": {
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "1",
                "sys_created_by": "admin",
                "knowledge": "false",
                "order": "",
                "calendar_stc": "",
                "closed_at": "",
                "cmdb_ci": "",
                "delivery_plan": "",
                "contract": "",
                "impact": "3",
                "active": "true",
                "work_notes_list": "",
                "business_service": "",
                "priority": "5",
                "sys_domain_path": "/",
                "rfc": "",
                "time_worked": "",
                "expected_start": "",
                "opened_at": "2020-10-20 07:18:56",
                "business_duration": "",
                "group_list": "",
                "work_end": "",
                "caller_id": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "reopened_time": "",
                "resolved_at": "",
                "approval_set": "",
                "subcategory": "",
                "work_notes": "",
                "short_description": "Assessment :  Assessor",
                "close_code": "",
                "correlation_display": "",
                "delivery_task": "",
                "work_start": "",
                "assignment_group": "",
                "additional_assignee_list": "",
                "business_stc": "",
                "description": "",
                "calendar_duration": "",
                "close_notes": "",
                "notify": "1",
                "service_offering": "",
                "sys_class_name": "incident",
                "closed_by": "",
                "follow_up": "",
                "parent_incident": {
                    "link": "https://example.service-now.com/api/now/table/incident/ID",
                    "value": "ID"
                },
                "sys_id": "2a100a1c2fc42010c518532a2799b621",
                "contact_type": "",
                "reopened_by": "",
                "incident_state": "1",
                "urgency": "3",
                "problem_id": "",
                "company": "",
                "reassignment_count": "0",
                "activity_due": "",
                "assigned_to": "",
                "severity": "3",
                "comments": "",
                "approval": "not requested",
                "sla_due": "",
                "comments_and_work_notes": "",
                "due_date": "",
                "sys_mod_count": "0",
                "reopen_count": "0",
                "sys_tags": "",
                "escalation": "0",
                "upon_approval": "proceed",
                "correlation_id": "",
                "location": "",
                "category": "inquiry"
            }
        ]
    }
    

##### Output messages

The **Add Parent Incident** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully set PARENT_INCIDENT_NUMBER as the "Parent Incident" for the following incidents in ServiceNow: CHILD_INCIDENT_NUMBERS.` | The action succeeded.  
`Error executing action "Add Parent Incident". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
### Close Incident

Use the **Close Incident** action to close a ServiceNow incident.

This action doesn't run on Google SecOps entities. 

**Important:** To run this action, you must assign the `sn_incident_write` role to the user in ServiceNow. For more details, go to Configure user access in ServiceNow.

#### Action inputs

The **Close Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The number of the incident to close, in the format `INCINCIDENT_NUMBER`.  
`Close Reason` | Required. The reason for closing the incident.  
`Resolution Code` | Required. The resolution code for the incident. The possible values are as follows:

  * `Duplicate`
  * `Known error`
  * `No resolution provided`
  * `Resolved by caller`
  * `Resolved by change`
  * `Resolved by problem`
  * `Resolved by request`
  * `Solution provided`
  * `Workaround provided`
  * `User error`

The default value is `Solution provided`.  
`Close Notes` | Required. The close notes for the incident.  
  
#### Action outputs

The **Close Incident** action provides the following outputs:

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

The following table lists the value for the script result output when using the **Close Incident** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Create Alert Incident

Use the **Create Alert Incident** action to create a new incident in ServiceNow based on the details of the alert that initiates the playbook run.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Alert Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Impact` | Required. The impact level of the incident. **Important:** You must use the ServiceNow Value, for example, `1`, instead of the Label, for example, `1 - High`. The possible values are as follows:

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Urgency` | Required. The urgency level of the incident. **Important:** You must use the ServiceNow Value (for example, `1`) instead of the Label (for example, `1 - High`). The possible values are as follows

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Category` | Optional. The category of the incident. **Important:** You must use the ServiceNow Value, for example, `database`, instead of the Label, for example, `Database`.   
`Assignment Group ID` | Optional. The full name of the group to assign the incident to.  
`Assigned User ID` | Optional. The full name of the user to assign the incident to.  
`Description` | Optional. The incident description.  
  
#### Action outputs

The **Create Alert Incident** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Alert Incident** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": " ",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010005",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "0",
        "notify": "1",
        "resolved_by": " ",
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": " ",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "1",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by":
        "admin", "caused_by": " ",
        "comments": " ",
        "closed_by": " ",
        "priority": "1",
        "state": "1",
        "sys_id": "ID",
        "opened_at": "2020-07-10 05:13:25",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": "4187b92c-7aaa-40ec-a032-833dd5a854e6",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": " ",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": " ",
        "business_duration": " ",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 05:13:25",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": " ",
        "caller_id": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "active": "true",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": "2020-07-10 07:13:25",
        "severity": "3",
        "incident_state": "1",
        "resolved_at": " ",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 05:13:25",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": " ",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "1",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Create Alert Incident** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Create Incident

Use the **Create Incident** action to create a new incident in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Short Description` | Required. The short description of the incident.  
`Impact` | Required. The impact level of the incident. **Important:** You must use the ServiceNow Value, for example, `1`, instead of the Label, for example, `1 - High`. The possible values are as follows:

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Urgency` | Required. The urgency level of the incident. **Important:** You must use the ServiceNow Value (for example, `1`) instead of the Label (for example, `1 - High`). The possible values are as follows

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Category` | Optional. The category of the incident. **Important:** You must use the ServiceNow Value, for example, `database`, instead of the Label, for example, `Database`.   
`Assignment Group ID` | Optional. The full name of the group to assign the incident to.   
`Assigned User ID` | Optional. The full name of the user to assign the incident to.   
`Description` | Optional. The incident description.  
`Custom Fields` | Optional. A JSON-formatted string containing field names and their corresponding values to update (for example, `{"location":"London", "category":"database"}`). You can use this parameter to modify fields not explicitly defined as action inputs.  
  
#### Action outputs

The **Create Incident** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Incident** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": " ",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010005",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "0",
        "notify": "1",
        "resolved_by": " ",
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": " ",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "1",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by":
        "admin", "caused_by": " ",
        "comments": " ",
        "closed_by": " ",
        "priority": "1",
        "state": "1",
        "sys_id": "ID",
        "opened_at": "2020-07-10 05:13:25",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": "4187b92c-7aaa-40ec-a032-833dd5a854e6",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": " ",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": " ",
        "business_duration": " ",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 05:13:25",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": " ",
        "caller_id": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "active": "true",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": "2020-07-10 07:13:25",
        "severity": "3",
        "incident_state": "1",
        "resolved_at": " ",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 05:13:25",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": " ",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "1",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Create Incident** action:

Script result name | Value  
---|---  
`incident_number` | `INCIDENT_NUMBER`  
  
### Create Record

Use the **Create Record** action to create new records in different ServiceNow tables.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Record** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Optional. The name of the ServiceNow table where the new record is created (for example, `incident`).  
`Object Json Data` | Optional. The JSON object containing the field-value pairs required to define the new record (such as incident fields or CMDB item attributes).  
  
#### Action outputs

The **Create Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Record** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": " ",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010021",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "0",
        "notify": "1",
        "resolved_by": " ",
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": " ",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "3",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by": "admin",
        "caused_by": " ",
        "comments": " ",
        "closed_by": " ",
        "priority": "5",
        "state": "1",
        "sys_id": "ID",
        "opened_at": "2020-07-10 08:24:34",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": " ",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": " ",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": " ",
        "business_duration": " ",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 08:24:34",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": " ",
        "caller_id": " ",
        "active": "true",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": " ",
        "severity": "3",
        "incident_state": "1",
        "resolved_at": " ",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 08:24:34",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": " ",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "3",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Create Record** action:

Script result name | Value  
---|---  
`object_sys_id` | `OBJECT_SYS_ID`  
  
### Download Attachments

Use the **Download Attachments** action to download files and documents that are attached to a specific ServiceNow record to a local folder in your Google SecOps environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Download Attachments** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table that contains the record to download attachments from (such as `incident`).  
`Record Sys ID` | Required.The system ID (`sys_id`) of the record from which the attachments are downloaded.  
`Download Folder Path` | Required. The absolute path to the folder in the Google SecOps environment where the downloaded attachments are saved.  
`Overewrite` | Optional. If selected, the action overwrites files with the same name. Disabled by default.  
  
#### Action outputs

The **Download Attachments** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Download Attachments** action:
    
    
    {
        "result": [
            {"absolute_file_path" : ["PATH"]
                "size_bytes": "187",
                "file_name": "example.txt",
                "sys_mod_count": "1",
                "average_image_color": "",
                "image_width": "",
                "sys_updated_on": "2020-10-19 09:58:39",
                "sys_tags": "",
                "table_name": "problem",
                "sys_id": "SYS_ID",
                "image_height": "",
                "sys_updated_by": "system",
                "download_link": "https://example.service-now.com/api/now/attachment/ID/file",
                "content_type": "text/plain",
                "sys_created_on": "2020-10-19 09:58:38",
                "size_compressed": "172",
                "compressed": "true",
                "state": "available",
                "table_sys_id": "57771d002f002010c518532a2799b6cc",
                "chunk_size_bytes": "700000",
                "hash": "a4fbb8ab71268903845b59724835274ddc66e095de553c5e0c1da8fecd04ee45",
                "sys_created_by": "admin"
            }
        ]
    }
    

##### Output messages

The **Download Attachments** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded the following attachments related to the record with Sys ID SYS_ID from table TABLE_NAME in ServiceNow: FILENAME` `Action wasn't able to download the following attachments related to the record with Sys ID SYS_ID from table TABLE_NAME in ServiceNow: FILENAME` `Action wasn't able to download attachments related to the record with Sys ID SYS_ID from table TABLE_NAME in ServiceNow: FILENAME` | The action succeeded.  
`Error executing action "Download Attachments". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Download Attachments** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Child Incident Details

Use the **Get Child Incident Details** action to retrieve information about child incidents based on the parent incident in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Child Incident Details** action requires the following parameters:

Parameter | Description  
---|---  
`Parent Incident Number` | Required. The number of the parent incident from which to retrieve the child incident details, in the format `INCINCIDENT_NUMBER`.  
`Max Child Incident To Return` | Optional. The maximum number of child incidents the action returns from the parent incident. The default value is `50`.  
  
#### Action outputs

The **Get Child Incident Details** action provides the following outputs:

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

The **Get Child Incident Details** action provides the following table:

Table name: **Child Incident Details**

Table columns:

  * **Sys ID** (mapped as `sys_id`)
  * **Number** (mapped as `number`)
  * **Short Description** (mapped as `short_description`)
  * **Created At** (mapped as `sys_created_on`)



##### JSON result

The following example shows the JSON result output received when using the **Get Child Incident Details** action:
    
    
    {
        "result": [
            {
                "parent": "",
                "made_sla": "true",
                "caused_by": "",
                "watch_list": "",
                "upon_reject": "cancel",
                "sys_updated_on": "2020-10-20 07:19:11",
                "child_incidents": "0",
                "hold_reason": "",
                "approval_history": "",
                "skills": "",
                "number": "INC0010009",
                "resolved_by": "",
                "sys_updated_by": "admin",
                "opened_by": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "user_input": "",
                "sys_created_on": "2020-10-20 07:19:11",
                "sys_domain": {
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "1",
                "sys_created_by": "admin",
                "knowledge": "false",
                "order": "",
                "calendar_stc": "",
                "closed_at": "",
                "cmdb_ci": "",
                "delivery_plan": "",
                "contract": "",
                "impact": "3",
                "active": "true",
                "work_notes_list": "",
                "business_service": "",
                "priority": "5",
                "sys_domain_path": "/",
                "rfc": "",
                "time_worked": "",
                "expected_start": "",
                "opened_at": "2020-10-20 07:18:56",
                "business_duration": "",
                "group_list": "",
                "work_end": "",
                "caller_id": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "reopened_time": "",
                "resolved_at": "",
                "approval_set": "",
                "subcategory": "",
                "work_notes": "",
                "short_description": "Assessment :  ATF Assessor",
                "close_code": "",
                "correlation_display": "",
                "delivery_task": "",
                "work_start": "",
                "assignment_group": "",
                "additional_assignee_list": "",
                "business_stc": "",
                "description": "",
                "calendar_duration": "",
                "close_notes": "",
                "notify": "1",
                "service_offering": "",
                "sys_class_name": "incident",
                "closed_by": "",
                "follow_up": "",
                "parent_incident": {
                    "link": "https://example.service-now.com/api/now/table/incident/ID",
                    "value": "ID"
                },
                "sys_id": "2a100a1c2fc42010c518532a2799b621",
                "contact_type": "",
                "reopened_by": "",
                "incident_state": "1",
                "urgency": "3",
                "problem_id": "",
                "company": "",
                "reassignment_count": "0",
                "activity_due": "",
                "assigned_to": "",
                "severity": "3",
                "comments": "",
                "approval": "not requested",
                "sla_due": "",
                "comments_and_work_notes": "",
                "due_date": "",
                "sys_mod_count": "0",
                "reopen_count": "0",
                "sys_tags": "",
                "escalation": "0",
                "upon_approval": "proceed",
                "correlation_id": "",
                "location": "",
                "category": "inquiry"
            }
        ]
    }
    

##### Output messages

The **Get Child Incident Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about child incidents related to the PARENT_INCIDENT_NUMBER  incident in ServiceNow.` `Action wasn't able to retrieve information about the child incidents in ServiceNow. Reason: incident PARENT_INCIDENT_NUMBER was not found.` `No child incidents were found.` | The action succeeded.  
`Error executing action "Get Child Incident Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Child Incident Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get CMDB Record Details

Use the **Get CMDB Record Details** action to get detailed CMDB records from the same class in ServiceNow.

This action doesn't run on Google SecOps entities. 

**Important:** This action requires you to assign the `itil` role to the user in ServiceNow. For more details, see Configure user access in ServiceNow.

#### Action inputs

The **Get CMDB Record Details** action requires the following parameters:

Parameter | Description  
---|---  
`Class Name` | Required. The name of the CMDB class from which to retrieve records, such as `cmdb_ci_appl`. For more information on class names, see [View and edit class definition and metadata](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/t_ViewTableDefinitions.html).  
`Sys ID` | Required. A comma-separated list of the system IDs (`sys_id`) of the CMDB records for which to retrieve details.  
`Max Records To Return` | Optional. The maximum number of record relations to return for each relation type (such as `relates to` or `depends on`). The default value is `50`.  
  
#### Action outputs

The **Get CMDB Record Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get CMDB Record Details** action:
    
    
    {
        "result": {
            "outbound_relations": [
                {
                    "sys_id": "56f3a7ad7f701200bee45f19befa910f",
                    "type": {
                        "display_value": "Members::Member of",
                        "link": "https://example.service-now.com/api/now/table/cmdb_rel_type/ID",
                        "value": "ID"
                    },
                    "target": {
                        "display_value": "Example",
                        "link": "https://example.service-now.com/api/now/cmdb/instance/cmdb_ci/ID",
                        "value": "ID"
                    }
                }
            ],
            "attributes": {
                "attested_date": "",
                "skip_sync": "false",
                "operational_status": "1",
                "caption": "",
                "cluster_type": "",
                "sys_updated_on": "2016-01-06 19:04:07",
                "attestation_score": "",
                "discovery_source": "",
                "first_discovered": "",
                "sys_updated_by": "example.user",
                "cluster_status": "",
                "due_in": "",
                "sys_created_on": "2016-01-06 16:47:15",
                "sys_domain": {
                    "display_value": "global",
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "install_date": "",
                "invoice_number": "",
                "gl_account": "",
                "sys_created_by": "example.user",
                "warranty_expiration": "",
                "cluster_version": "",
                "asset_tag": "",
                "fqdn": "",
                "change_control": "",
                "owned_by": "",
                "checked_out": "",
                "sys_domain_path": "/",
                "delivery_date": "",
                "maintenance_schedule": "",
                "install_status": "1",
                "cost_center": "",
                "attested_by": "",
                "supported_by": "",
                "dns_domain": "",
                "name": "SAP-LB-Win-Cluster",
                "assigned": "",
                "purchase_date": "",
                "subcategory": "Cluster",
                "short_description": "",
                "assignment_group": "",
                "managed_by": "",
                "managed_by_group": "",
                "last_discovered": "",
                "can_print": "false",
                "sys_class_name": "cmdb_ci_win_cluster",
                "manufacturer": "",
                "sys_id": "SYS_ID",
                "cluster_id": "",
                "po_number": "",
                "checked_in": "",
                "sys_class_path": "/!!/!5/!$",
                "vendor": "",
                "mac_address": "",
                "company": "",
                "model_number": "",
                "justification": "",
                "department": "",
                "assigned_to": "",
                "start_date": "",
                "cost": "",
                "comments": "",
                "sys_mod_count": "1",
                "serial_number": "",
                "monitor": "false",
                "model_id": "",
                "ip_address": "",
                "duplicate_of": "",
                "sys_tags": "",
                "cost_cc": "USD",
                "support_group": "",
                "order_date": "",
                "schedule": "",
                "environment": "",
                "due": "",
                "attested": "false",
                "unverified": "false",
                "correlation_id": "",
                "attributes": "",
                "location": "",
                "asset": "",
                "category": "Resource",
                "fault_count": "0",
                "lease_id": ""
            },
            "inbound_relations": [
                {
                    "sys_id": "3b3d95297f701200bee45f19befa910c",
                    "type": {
                        "display_value": "Depends on::Used by",
                        "link": "https://example.service-now.com/api/now/table/cmdb_rel_type/ID",
                        "value": "ID"
                    },
                    "target": {
                        "display_value": "IP-Router-3",
                        "link": "https://example.service-now.com/api/now/cmdb/instance/cmdb_ci/ID",
                        "value": "ID"
                    }
                }
            ]
        }
    }
    

##### Output messages

The **Get CMDB Record Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details for CMDB records in the Class CLASS_NAME from ServiceNow for the following Sys IDs: SYS_ID_LIST. ` `Action wasn't able to return details for CMDB records in the Class CLASS_NAME from ServiceNow for the following Sys IDs: SYS_ID_LIST` `Action wasn't able to return details for CMDB records in the Class CLASS_NAME in ServiceNow. Reason: Class CLASS_NAME was not found.` `Action wasn't able to return details for CMDB record with Sys ID SYS_ID in the Class CLASS_NAME in Service Now. Reason: Record with Sys ID SYS_ID was not found in Class CLASS_NAME.` `Information about the provided Sys IDs was not found.` | The action succeeded.  
`Error executing action "Get CMDB Record Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get CMDB Record Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Incident

Use the **Get Incident** action to retrieve information about a ServiceNow incident.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The unique identifier of the ServiceNow incident to retrieve, in the format `INCINCIDENT_NUMBER`.  
  
#### Action outputs

The **Get Incident** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Incident** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": "2012",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010041",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "10",
        "notify": "1",
        "resolved_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": "2020-07-10 12:53:06",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "1",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by": "admin",
        "caused_by": " ",
        "comments": " ",
        "closed_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "priority": "1",
        "state": "7",
        "sys_id": "SYS_ID",
        "opened_at": "2020-07-10 12:18:04",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": "sdf",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": "0",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": "Closed by Caller",
        "business_duration": "1970-01-01 00:00:00",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 13:13:57",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": "1970-01-01 00:35:02",
        "caller_id": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "active": "false",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": "2020-07-10 14:33:28",
        "severity": "3",
        "incident_state": "7",
        "resolved_at": "2020-07-10 12:53:06",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 12:18:04",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": "Closed/Resolved by Caller",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "1",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get Incident** action:

Script result name | Value  
---|---  
`incident_number` | `INCIDENT_NUMBER`  
  
### Get Oauth Token

Use the **Get Oauth Token** action to get an OAuth refresh token for ServiceNow.

This action doesn't run on Google SecOps entities. 

**Note:**

This action requires you to set the following integration parameters:

  * `Username`
  * `Password`
  * `Client ID`
  * `Client Secret`



#### Action inputs

None.

#### Action outputs

The **Get Oauth Token** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Oauth Token** action:
    
    
    {
        "access_token": "Na4Kb1oWpFcYNUnyAjsYldiTMxYF1Cz79Q",
        "refresh_token": "0ryCENbbvfggZbNG9rFFd8_C8X0UgAQSMQkPJNStGwEEt0qNt-F1lw",
        "scope": "useraccount",
        "token_type": "Bearer",
        "expires_in": 1799
    }
    

##### Output messages

The **Get Oauth Token** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully generated Oauth tokens for ServiceNow. Now navigate to the configuration tab and put "refresh_token" value in the "Refresh Token" parameter. Note: "Username" and "Password" parameters can be emptied.` | The action succeeded.  
`Error executing action "Get Oauth Token". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Oauth Token** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Record Details

Use the **Get Record Details** action to retrieve information about specific table records in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Record Details** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table that contains the record to retrieve information from (such as `incident`).  
`Record Sys ID` | Required. The system ID (`sys_id`) of the specific ServiceNow record for which to retrieve details.  
`Fields` | Optional. A comma-separated list of specific fields (columns) to return from the retrieved record (such as `sys_id,number,short_description`). If no value is provided, the action returns the default fields for the record.  
  
#### Action outputs

The **Get Record Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Record Details** action:
    
    
    {
        "result": [
            {
                "parent": "",
                "made_sla": "true",
                "caused_by": "",
                "watch_list": "",
                "upon_reject": "cancel",
                "sys_updated_on": "2020-10-20 07:19:11",
                "child_incidents": "0",
                "hold_reason": "",
                "approval_history": "",
                "skills": "",
                "number": "INC0010009",
                "resolved_by": "",
                "sys_updated_by": "admin",
                "opened_by": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "user_input": "",
                "sys_created_on": "2020-10-20 07:19:11",
                "sys_domain": {
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "1",
                "sys_created_by": "admin",
                "knowledge": "false",
                "order": "",
                "calendar_stc": "",
                "closed_at": "",
                "cmdb_ci": "",
                "delivery_plan": "",
                "contract": "",
                "impact": "3",
                "active": "true",
                "work_notes_list": "",
                "business_service": "",
                "priority": "5",
                "sys_domain_path": "/",
                "rfc": "",
                "time_worked": "",
                "expected_start": "",
                "opened_at": "2020-10-20 07:18:56",
                "business_duration": "",
                "group_list": "",
                "work_end": "",
                "caller_id": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "reopened_time": "",
                "resolved_at": "",
                "approval_set": "",
                "subcategory": "",
                "work_notes": "",
                "short_description": "Assessment :  ATF Assessor",
                "close_code": "",
                "correlation_display": "",
                "delivery_task": "",
                "work_start": "",
                "assignment_group": "",
                "additional_assignee_list": "",
                "business_stc": "",
                "description": "",
                "calendar_duration": "",
                "close_notes": "",
                "notify": "1",
                "service_offering": "",
                "sys_class_name": "incident",
                "closed_by": "",
                "follow_up": "",
                "parent_incident": {
                    "link": "https://example.service-now.com/api/now/table/incident/ID",
                    "value": "ID"
                },
                "sys_id": "SYS_ID",
                "contact_type": "",
                "reopened_by": "",
                "incident_state": "1",
                "urgency": "3",
                "problem_id": "",
                "company": "",
                "reassignment_count": "0",
                "activity_due": "",
                "assigned_to": "",
                "severity": "3",
                "comments": "",
                "approval": "not requested",
                "sla_due": "",
                "comments_and_work_notes": "",
                "due_date": "",
                "sys_mod_count": "0",
                "reopen_count": "0",
                "sys_tags": "",
                "escalation": "0",
                "upon_approval": "proceed",
                "correlation_id": "",
                "location": "",
                "category": "inquiry"
            }
        ]
    }
    

##### Output messages

The **Get Record Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about the TABLE_NAME record with a Sys ID RECORD_SYS_ID in ServiceNow.` `Action wasn't able to retrieve information about the TABLE_NAME record with a Sys ID RECORD_SYS_ID in ServiceNow. Reason: ERROR_REASON.` | The action succeeded.  
`Error executing action "Get Record Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Record Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get User Details

Use the **Get User Details** action to retrieve information about the user using the `sys_id` parameter in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get User Details** action requires the following parameters:

Parameter | Description  
---|---  
`User Sys IDs` | Optional. A comma-separated list of the system IDs corresponding to the users for whom to retrieve details (such as `sys_id_1,sys_id_2`).  
`Emails` | Optional. A comma-separated list of email addresses corresponding to the users for whom to retrieve details (such as `email1@example.com,email2@example.com`).  
  
#### Action outputs

The **Get User Details** action provides the following outputs:

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

The **Get User Details** action provides the following table:

Table name: **User Details**

Table columns:

  * **Sys ID** (mapped as `sys_id`)
  * **Name** (mapped as `name`)
  * **Username** (mapped as `user_name`)
  * **Email** (mapped as `email`)



##### JSON result

The following example shows the JSON result output received when using the **Get User Details** action:
    
    
    {
        "result": [
            {
                "calendar_integration": "1",
                "country": "",
                "last_position_update": "",
                "user_password": "example",
                "last_login_time": "",
                "source": "",
                "sys_updated_on": "2020-08-29 02:42:42",
                "building": "",
                "web_service_access_only": "false",
                "notification": "2",
                "enable_multifactor_authn": "false",
                "sys_updated_by": "user@example",
                "sys_created_on": "2012-02-18 03:04:52",
                "agent_status": "",
                "sys_domain": {
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "",
                "vip": "false",
                "sys_created_by": "admin",
                "longitude": "",
                "zip": "",
                "home_phone": "",
                "time_format": "",
                "last_login": "",
                "default_perspective": "",
                "geolocation_tracked": "false",
                "active": "true",
                "sys_domain_path": "/",
                "cost_center": {
                    "link": "https://example.service-now.com/api/now/table/cmn_cost_center/ID",
                    "value": "ID"
                },
                "phone": "",
                "name": "Example User",
                "employee_number": "",
                "password_needs_reset": "false",
                "gender": "Male",
                "city": "",
                "failed_attempts": "",
                "user_name": "example.user",
                "latitude": "",
                "roles": "",
                "title": "",
                "sys_class_name": "sys_user",
                "sys_id": "SYS_ID",
                "internal_integration_user": "false",
                "ldap_server": "",
                "mobile_phone": "",
                "street": "",
                "company": {
                    "link": "https://example.service-now.com/api/now/table/core_company/ID",
                    "value": "ID"
                },
                "department": {
                    "link": "https://dev98773.service-now.com/api/now/table/cmn_department/ID",
                    "value": "ID"
                },
                "first_name": "Example",
                "email": "example@example.com",
                "introduction": "",
                "preferred_language": "",
                "manager": "",
                "business_criticality": "3",
                "locked_out": "false",
                "sys_mod_count": "4",
                "last_name": "User",
                "photo": "",
                "avatar": "063e38383730310042106710ce41f13b",
                "middle_name": "",
                "sys_tags": "",
                "time_zone": "",
                "schedule": "",
                "on_schedule": "",
                "date_format": "",
                "location": {
                    "link": "https://example.service-now.com/api/now/table/cmn_location/ID",
                    "value": "ID"
                }
            }
        ]
    }
    

##### Output messages

The **Get User Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about users from ServiceNow with the following Sys IDs: SYS_ID_LIST.` `Action wasn't able to retrieve information about the users in ServiceNow with the following Sys IDs: SYS_ID_LIST.` `Information about the users with specified Sys IDs was not found in ServiceNow.` | The action succeeded.  
`Error executing action "Get User Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get User Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List CMDB Records

Use the **List CMDB Records** action to list CMDB records from the same class in ServiceNow.

This action doesn't run on Google SecOps entities. 

**Important:** This action requires you to assign the `itil` role to the user in ServiceNow. For more details, go to Configure user access in ServiceNow.

#### Generating the query filter

The `Query Filter` parameter accepts standard ServiceNow encoded query strings (`sysparm_query`). You can generate these strings directly within the ServiceNow interface (for example, by creating a filter on a list view and selecting **Copy query**) or by constructing them manually.

For instructions on how to generate and use these strings, see [Encoded query strings](https://docs.servicenow.com/bundle/washingtondc-platform-user-interface/page/use/common-ui-elements/concept/c_EncodedQueryStrings.html) in the ServiceNow documentation.

#### Action inputs

The **List CMDB Records** action requires the following parameters:

Parameter | Description  
---|---  
`Class Name` | Required. The name of the CMDB class from which to retrieve records, such as `cmdb_ci_appl`. For more information on ServiceNow class names, see [View and edit class definition and metadata](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/t_ViewTableDefinitions.html).  
`Query Filter` | Optional. The encoded query string used to filter the records returned (such as `sys_idLIKE1^sys_idSTARTSWITH0`). You can generate valid query strings using the **Copy query** option in ServiceNow list views. For more information, see [Encoded query strings](https://docs.servicenow.com/bundle/washingtondc-platform-user-interface/page/use/common-ui-elements/concept/c_EncodedQueryStrings.html).  
`Max Records To Return` | Optional. The maximum number of records to retrieve based on the applied filters. The default value is `50`.  
  
#### Action outputs

The **List CMDB Records** action provides the following outputs:

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

The **List CMDB Records** action provides the following table:

Table name: **CLASS_NAME Records**

Table columns:

  * **Name** (mapped as `name`)
  * **Sys ID** (mapped as `sys_id`)



##### JSON result

The following example shows the JSON result output received when using the **List CMDB Records** action:
    
    
    {
        "result": [
            {
                "sys_id": "SYS_ID",
                "name": "Example server"
            }
        ]
    }
    

##### Output messages

The **List CMDB Records** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed CMDB records for the Class CLASS_NAME in ServiceNow.` `Action wasn't able to list CMDB records for the Class CLASS_NAME in ServiceNow. Reason: Class CLASS_NAME was not found in Service Now.".format(Class name)` | The action succeeded.  
`Error executing action "List CMDB Records". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List CMDB Records** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Record Comments

Use the **List Record Comments** action to list comments related to a specific table record in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Record Comments** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table that contains the record for which to list comments (such as `incident`).  
`Record Sys ID` | Required. The system ID (`sys_id`) of the record for which to list comments.  
`Type` | Required. The type of comments or notes to retrieve. The possible values are as follows:

  * `Comment`
  * `Work Note`

The default value is `Comment`.  
`Max Results To Return` | Optional. The maximum number of comments or work notes to return. The default value is `50`.  
  
#### Action outputs

The **List Record Comments** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Record Comments** action:
    
    
    {
        "sys_id": "SYS_ID",
        "sys_created_on": "2021-09-03 10:29:48",
        "name": "incident",
        "element_id": "552c48888c033300964f4932b03eb092",
        "sys_tags": "",
        "value": "test",
        "sys_created_by": "admin",
        "element": "comments"
    }
    

##### Output messages

The **List Record Comments** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned CONTENT_TYPE related to  TABLE_NAME with Sys ID SYS_ID in ServiceNow.` `No  CONTENT_TYPE were found for TABLE_NAME with Sys ID SYS_ID in ServiceNow.` | The action succeeded.  
`Error executing action "List Record Comments". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Record Comments** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Records Related To User

Use the **List Records Related To User** action to list records from a table that are related to a user in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Records Related To User** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table to search for related records (such as `incident`).  
`Usernames` | Required. A comma-separated list of usernames for which to retrieve the related records.  
`Max Days Backwards` | Required. The number of days back from the current date to search for related records. The default value is `1`.  
`Max Records To Return` | Optional. The maximum number of records to return for every user. The default value is `50`.  
  
#### Action outputs

The **List Records Related To User** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Records Related To User** action:
    
    
    {
        "result": [
            {
                "parent": "",
                "made_sla": "true",
                "caused_by": "",
                "watch_list": "",
                "upon_reject": "cancel",
                "sys_updated_on": "2020-10-19 14:18:40",
                "child_incidents": "0",
                "hold_reason": "",
                "approval_history": "",
                "skills": "",
                "number": "INC0010008",
                "resolved_by": "",
                "sys_updated_by": "admin",
                "opened_by": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "user_input": "",
                "sys_created_on": "2020-10-19 14:18:40",
                "sys_domain": {
                    "link": "https://example.service-now.com/api/now/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "1",
                "sys_created_by": "admin",
                "knowledge": "false",
                "order": "",
                "calendar_stc": "",
                "closed_at": "",
                "cmdb_ci": "",
                "delivery_plan": "",
                "contract": "",
                "impact": "3",
                "active": "true",
                "work_notes_list": "",
                "business_service": "",
                "priority": "5",
                "sys_domain_path": "/",
                "rfc": "",
                "time_worked": "",
                "expected_start": "",
                "opened_at": "2020-10-19 14:18:20",
                "business_duration": "",
                "group_list": "",
                "work_end": "",
                "caller_id": {
                    "link": "https://example.service-now.com/api/now/table/sys_user/ID",
                    "value": "ID"
                },
                "reopened_time": "",
                "resolved_at": "",
                "approval_set": "",
                "subcategory": "",
                "work_notes": "",
                "short_description": "TEST",
                "close_code": "",
                "correlation_display": "",
                "delivery_task": "",
                "work_start": "",
                "assignment_group": "",
                "additional_assignee_list": "",
                "business_stc": "",
                "description": "",
                "calendar_duration": "",
                "close_notes": "",
                "notify": "1",
                "service_offering": "",
                "sys_class_name": "incident",
                "closed_by": "",
                "follow_up": "",
                "parent_incident": "",
                "sys_id": "SYS_ID",
                "contact_type": "",
                "reopened_by": "",
                "incident_state": "1",
                "urgency": "3",
                "problem_id": "",
                "company": {
                    "link": "https://example.service-now.com/api/now/table/core_company/ID",
                    "value": "ID"
                },
                "reassignment_count": "0",
                "activity_due": "",
                "assigned_to": "",
                "severity": "3",
                "comments": "",
                "approval": "not requested",
                "sla_due": "",
             "comments_and_work_notes": "",
                "due_date": "",
                "sys_mod_count": "0",
                "reopen_count": "0",
                "sys_tags": "",
                "escalation": "0",
                "upon_approval": "proceed",
                "correlation_id": "",
                "location": "",
                "category": "inquiry"
            }
        ]
    }
    

##### Output messages

The **List Records Related To User** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved related records from the table TABLE_NAME in ServiceNow for the following users:  USERNAME_LIST. ` `Action wasn't able to retrieve related records from the table TABLE_NAME in ServiceNow for the following users:  USERNAME_LIST. ` `No related table records were retrieved for the provided users. ` | The action succeeded.  
`Error executing action "List Records Related To User". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Records Related To User** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to ServiceNow.

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
`is_success` | `true` or `false`  
  
### Update Incident

Use the **Update Incident** action to update the incident information.

This action doesn't run on Google SecOps entities. 

**Important:** To run this action, you must assign the `sn_incident_write` role to the user in ServiceNow. For more details, go to Configure user access in ServiceNow.

#### Action inputs

The **Update Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The unique identifier of the ServiceNow incident to update, in the format `INCINCIDENT_NUMBER`.  
`Short Description` | Optional. A short description for the incident.  
`Impact` | Optional. An impact level for the incident. **Important:** You must use the ServiceNow Value, for example, `1`, instead of the Label, for example, `1 - High`. The possible values are as follows:

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Urgency` | Optional. An urgency level for the incident. **Important:** You must use the ServiceNow Value (for example, `1`) instead of the Label (for example, `1 - High`). The possible values are as follows

  * `1` for High
  * `2` for Medium
  * `3` for Low

The default value is `1`.  
`Category` | Optional. A category for the incident. **Important:** You must use the ServiceNow Value, for example, `database`, instead of the Label, for example, `Database`.   
`Assignment Group ID` | Optional. The full name of a group to assign the incident to.  
`Assigned User ID` | Optional. The full name of a user to assign the incident to.  
`Description` | Optional. The description for the incident.  
`Incident State` | Optional. The underlying ServiceNow Value for the incident state (for example, `1` or `in_progress`) instead of the Label (for example, `New` or `In Progress`).  
`Custom Fields` | Optional. A JSON-formatted string containing field names and their corresponding values to update (for example, `{"location":"London", "category":"database"}`). You can use this parameter to modify fields not explicitly defined as action inputs.  
  
#### Action outputs

The **Update Incident** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Update Incident** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": "2012",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010041",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "10",
        "notify": "1",
        "resolved_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": "2020-07-10 12:53:06",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "1",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by": "admin",
        "caused_by": " ",
        "comments": " ",
        "closed_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "priority": "1",
        "state": "7",
        "sys_id": "SYS_ID",
        "opened_at": "2020-07-10 12:18:04",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": "sdf",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": "0",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": "Closed by Caller",
        "business_duration": "1970-01-01 00:00:00",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 13:13:57",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": "1970-01-01 00:35:02",
        "caller_id": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "active": "false",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": "2020-07-10 14:33:28",
        "severity": "3",
        "incident_state": "7",
        "resolved_at": "2020-07-10 12:53:06",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 12:18:04",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": "Closed/Resolved by Caller",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "1",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Update Incident** action:

Script result name | Value  
---|---  
`incident_number` | `INCIDENT_NUMBER`  
  
### Update Record

Use the **Update Record** action to modify existing records belonging to various tables in ServiceNow.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Record** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Optional. The name of the ServiceNow table that contains the record to update (such as `incident`).  
`Object Json Data` | Required. A JSON object containing the field-value pairs to apply to the record (such as `{"short_description": "Updated description"}`).  
`Record Sys ID` | Required. The system ID (`sys_id`) of the specific record to update.  
  
#### Action outputs

The **Update Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Update Record** action:
    
    
    {
        "sys_tags": " ",
        "user_input": " ",
        "calendar_stc": " ",
        "subcategory": " ",
        "watch_list": " ",
        "follow_up": " ",
        "made_sla": "true",
        "sys_created_by": "admin",
        "sla_due": " ",
        "number": "INC0010021",
        "group_list": " ",
        "reassignment_count": "0",
        "assigned_to": " ",
        "sys_mod_count": "0",
        "notify": "1",
        "resolved_by": " ",
        "upon_reject": "cancel",
        "additional_assignee_list": " ",
        "category": "inquiry",
        "closed_at": " ",
        "parent_incident": " ",
        "cmdb_ci": " ",
        "contact_type": " ",
        "impact": "3",
        "rfc": " ",
        "expected_start": " ",
        "knowledge": "false",
        "sys_updated_by": "admin",
        "caused_by": " ",
        "comments": " ",
        "closed_by": " ",
        "priority": "5",
        "state": "1",
        "sys_id": "SYS_ID",
        "opened_at": "2020-07-10 08:24:34",
        "child_incidents": "0",
        "work_notes": " ",
        "delivery_task": " ",
        "short_description": " ",
        "comments_and_work_notes": " ",
        "time_worked": " ",
        "upon_approval": "proceed",
        "company": " ",
        "business_stc": " ",
        "correlation_display": " ",
        "sys_class_name": "incident",
        "delivery_plan": " ",
        "escalation": "0",
        "description": " ",
        "parent": " ",
        "close_notes": " ",
        "business_duration": " ",
        "problem_id": " ",
        "sys_updated_on": "2020-07-10 08:24:34",
        "approval_history": " ",
        "approval_set": " ",
        "business_service": " ",
        "reopened_by": " ",
        "calendar_duration": " ",
        "caller_id": " ",
        "active": "true",
        "approval": "not requested",
        "service_offering": " ",
        "sys_domain_path": "/",
        "hold_reason": " ",
        "activity_due": " ",
        "severity": "3",
        "incident_state": "1",
        "resolved_at": " ",
        "location": " ",
        "due_date": " ",
        "work_start": " ",
        "work_end": " ",
        "work_notes_list": " ",
        "sys_created_on": "2020-07-10 08:24:34",
        "correlation_id": " ",
        "contract": " ",
        "reopened_time": " ",
        "opened_by": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user/ID",
            "value": "ID"
        },
        "close_code": " ",
        "assignment_group": " ",
        "sys_domain": {
            "link": "https://example.service-now.com/api/now/v1/table/sys_user_group/global",
            "value": "global"
        },
        "order": " ",
        "urgency": "3",
        "reopen_count": "0"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Update Record** action:

Script result name | Value  
---|---  
`record_sys_id` | `RECORD_SYS_ID`  
  
### Wait For Comments

Use the **Wait For Comments** action to pause the playbook execution until a comment or work note is added to a specific table record in ServiceNow.

**Note:** This action operates asynchronously. You should adjust the script timeout value in the Google SecOps IDE if the expected wait time for a comment exceeds the default timeout.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Wait For Comments** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table that contains the record from which to wait for comments (such as `incident`).  
`Record Sys ID` | Required. The system ID (`sys_id`) of the record to monitor for comments.  
`Type` | Required. The type of comments or notes the action should wait for. The possible values are as follows:

  * `Comment`
  * `Work Note`

The default value is `Comment`.  
`Wait Mode` | Required. The condition that determines when the action stops waiting and proceeds. The possible values are as follows:

  * `Until Timeout`: The action waits for the entire timeout period and then returns all accumulated comments.
  * `Until First Message`: The action waits until the first new comment or work note is posted after the action starts.
  * `Until Specific Text`: The action waits until a comment or work note containing the text specified in `Text` is posted. **Note:** If selected, you must also set `Text`. 

The default value is `Until Timeout`.  
`Text` | Optional. The specific string of text the action waits for within a new comment or work note. This parameter is only used when `Until Specific Text` is selected for the value of `Wait Mode`.  
  
#### Action outputs

The **Wait For Comments** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Wait For Comments** action:
    
    
    {
        "sys_id": "SYS_ID",
        "sys_created_on": "2021-09-03 10:29:48",
        "name": "incident",
        "element_id": "552c48888c033300964f4932b03eb092",
        "sys_tags": "",
        "value": "test",
        "sys_created_by": "admin",
        "element": "comments"
    }
    

##### Output messages

The **Wait For Comments** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned  CONTENT_TYPE related to TABLE_NAME with Sys ID SYS_ID in ServiceNow.` `No new CONTENT_TYPE were added during the timeframe of action execution to TABLE_NAME with Sys ID SYS_ID in ServiceNow.` | The action succeeded.  
`Error executing action "Wait For Comments". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Wait For Comments** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Wait for Field Update

Use the **Wait for Field Update** action to pause the playbook execution until a specific field in a ServiceNow data record is updated to one of the expected values.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Wait for Field Update** action requires the following parameters:

Parameter | Description  
---|---  
`Table Name` | Required. The name of the ServiceNow table that contains the record to monitor (such as `incident`).  
`Record Sys ID` | Required. The system ID (`sys_id`) of the record to monitor for the field update.  
`Field - Column Name` | Required. The name of the column (field) that the action monitors for changes.  
`Field - Values` | Required. A comma-separated list of values that, if found in the monitored field, causes the action to stop waiting and proceed (such as `In Progress,Resolved`).  
  
#### Action outputs

The **Wait for Field Update** action provides the following outputs:

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

The following table lists the value for the script result output when using the **Wait for Field Update** action:

Script result name | Value  
---|---  
`updated_field` | `UPDATED_FIELD`  
  
### Wait for Status Update

Use the **Wait for Status Update** action to pause the playbook execution until a specific ServiceNow incident status (state) is updated to one of the expected values.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Wait for Status Update** action requires the following parameters:

Parameter | Description  
---|---  
`Incident Number` | Required. The unique identifier of the ServiceNow incident to monitor, in the format `INCINCIDENT_NUMBER`.  
`Statuses` | Required. A comma-separated list of incident statuses (states) that, if reached, cause the action to stop waiting and proceed (such as `In Progress,Resolved`).  
  
#### Action outputs

The **Wait for Status Update** action provides the following outputs:

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

The following table lists the value for the script result output when using the **Wait for Status Update** action:

Script result name | Value  
---|---  
`new_status` | `STATUS`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### ServiceNow Connector

Use the **ServiceNow Connector** to retrieve incidents from ServiceNow.

**Note:** This connector supports proxies, dynamic lists, and blocklists.

#### Working with the dynamic query list

In the **ServiceNow Connector** , the dynamic list modifies the `sysparm_query` that the connector uses to query ServiceNow. This provides the ability to filter records based on any supported field for the record type.

To define a filter, configure each dynamic list item to contain one field-value pair in the following format: `FIELD_NAME=VALUE.`

For example: `category=security`.

When `Use whitelist as a blacklist` is enabled, the connector inverts the query logic, causing the dynamic list to function as a blocklist instead of as a filter.

#### Connector inputs

The **ServiceNow Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `sys_class_name`.  
`Rule Generator` | Optional. The name of the field whose value defines the specific query or rule set to apply during record retrieval.  
`Api Root` | Required. The API root of the ServiceNow instance. The default value is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | Required. The username of the ServiceNow account.  
`Password` | Required. The password of the ServiceNow account.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
`Use sys_domain Environment` | Optional. If selected, the connector uses the ServiceNow `sys_domain` field as the environment for the ingested case. If this field is missing or unavailable, the connector defaults to the value specified in the `Environment` parameter.  
`Days Backwards` | Optional. The number of days back from the current time to retrieve records. This parameter is used for the initial connector run, or as a fallback value if a previous connector timestamp has expired. The default value is `5`.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism.  
`Max Incidents Per Cycle` | Optional. The maximum number of incidents to retrieve during each connector iteration. The default value is `10`.  
`Environments Whitelist` | Optional. A comma-separated list of environments (domains) for the connector to ingest into Google SecOps, such as `env1,env2`.  
`Use whitelist as a blacklist` | Optional. If selected, the connector uses the dynamic list as a blocklist. Disabled by default.  
`PythonProcessTimeout` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `60`.  
`Incident Table` | Optional. The API table name or path to use for incident-related actions and record retrieval. By default, the integration uses the `table/incident` path.  
`Client ID` | Optional. The client ID for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Client Secret` | Optional. The client secret for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Refresh Token` | Optional. The refresh token for the ServiceNow integration, required for OAuth 2.0 authentication using a refresh token. This configured refresh token expires every 90 days. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Assignment Group` | Optional. The name of the assignment group whose records the connector should ingest.  
`Use Oauth Authentication` | Optional. If selected, the integration uses OAuth 2.0 to authenticate. OAuth 2.0 authentication requires setting either the client credentials (`Client ID` and `Client Secret`) or `Refresh Token`. Disabled by default.  
`Server Time Zone` | Optional. The time zone configured on the ServiceNow server (such as `UTC` or `Asia/Jerusalem`). The default value is `UTC`.  
`Table Name` | Optional.The name of the table to retrieve records from, such as `incident`.  
`Event Name` | Optional. The name of the Google SecOps event created when a record is ingested (such as `ServiceNowEvent`).  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
`Get User Information` | Optional. If selected, the connector additionally retrieves the information about users that are related to the incident. Disabled by default.  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### ServiceNow - Sync Closed Incidents

Use the **ServiceNow - Sync Closed Incidents** job to synchronize closed ServiceNow incidents with corresponding Google SecOps alerts and cases.

This job processes ServiceNow incidents ingested as alerts and cases containing the `ServiceNow` tag and a `TICKET_ID` context value with the incident number.

#### Job parameters

The **ServiceNow - Sync Closed Incidents** job requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Mandatory_ The API root of the ServiceNow instance. Default is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | _Mandatory_ The username of the ServiceNow instance.  
`Password` | _Mandatory_ The password of the ServiceNow instance.  
`Verify SSL` | _Optional_ If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
`Client ID` | _Optional_ The client ID for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Client Secret` | _Optional_ The client secret for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Refresh Token` | _Optional_ The refresh token for the ServiceNow integration, required for OAuth 2.0 authentication using a refresh token. This configured refresh token expires every 90 days. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Use OAuth Authentication` | _Optional_ If selected, the integration uses OAuth 2.0 to authenticate. OAuth 2.0 authentication requires setting either the client credentials (`Client ID` and `Client Secret`) or `Refresh Token`. Disabled by default.  
`Max Hours Backwards` | _Optional_ The number of hours back from the current time to search for and synchronize closed incidents. Default is `24`.  
`Table Name` | _Mandatory_ The name of the database table to search for closed incidents (for example, `incident`).  
  
### ServiceNow - Sync Incidents

Use the **ServiceNow - Sync Incidents** job to synchronize ServiceNow incident fields and attachments with related cases and alerts in Google SecOps.

To run this job, the ServiceNow integration user must have the ITIL (`itil`) role. For more information, see [Base system roles](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/roles/reference/r_BaseSystemRoles.html#d143244e3179) in the ServiceNow documentation.

#### Job requirements

For the job to function correctly, make sure the following are configured on the Google SecOps case or alert (depending on the `Sync Level` parameter):

  * **Tag** : The case must have the `ServiceNow Incident Sync` tag.
  * **Context value** : The case or alert must have a `TICKET_ID` context key containing a comma-separated list of ServiceNow incident numbers (for example, `INC0000050,INC0000051`). Set the `TICKET_ID` context value using the [**Set Scope Context Value**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify#set-scope-context-value) action from the Siemplify Utilities integration.



#### Job parameters

The **ServiceNow - Sync Incidents** job requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Mandatory_ The API root of the ServiceNow instance. Default is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | _Optional_ The username of the ServiceNow instance. When authenticating using basic password authentication, this parameter is required.  
`Password` | _Optional_ The password of the ServiceNow instance. When authenticating using basic password authentication, this parameter is required.  
`Sync Level` | _Mandatory_ The level at which the job synchronizes data. Possible values: `Case`, `Alert`. Default is `Case`.  
`Max Hours Backwards` | _Mandatory_ The maximum number of hours back from the current time to search for cases to synchronize. Default is `24`.  
`Verify SSL` | _Optional_ If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
`Use OAuth Authentication` | _Optional_ If selected, the job uses OAuth authentication instead of basic authentication. When selected, the `Client ID`, `Client Secret`, and `Refresh Token` parameters are required. Disabled by default.  
`Client ID` | _Optional_ The Client ID of the ServiceNow application. Required if `Use OAuth Authentication` is selected.  
`Client Secret` | _Optional_ The Client Secret of the ServiceNow application. Required if `Use OAuth Authentication` is selected.  
`Refresh Token` | _Optional_ The refresh token for the ServiceNow application. Required if `Use OAuth Authentication` is selected.  
  
### Sync Table Record Comments

Use the **Sync Table Record Comments** job to synchronize comments between ServiceNow table records and Google SecOps cases.

#### Job parameters

The **Sync Table Record Comments** job requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Mandatory_ The API root of the ServiceNow instance. Default is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | _Mandatory_ The username of the ServiceNow instance.  
`Password` | _Mandatory_ The password of the ServiceNow instance.  
`Verify SSL` | _Optional_ If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
`Client ID` | _Optional_ The client ID for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Client Secret` | _Optional_ The client secret for the ServiceNow integration, required for OAuth 2.0 authentication using client credentials. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Refresh Token` | _Optional_ The refresh token for the ServiceNow integration, required for OAuth 2.0 authentication using a refresh token. This configured refresh token expires every 90 days. You can authenticate using either the refresh token or client credentials. If both the refresh token and client credentials are configured, the integration uses the refresh token for authentication.  
`Use OAuth Authentication` | _Optional_ If selected, the integration uses OAuth 2.0 to authenticate. OAuth 2.0 authentication requires setting either the client credentials (`Client ID` and `Client Secret`) or `Refresh Token`. Disabled by default.  
`Table Name` | _Mandatory_ The name of the ServiceNow table to search for records to synchronize comments from (for example, `incident`).  
  
### Sync table record comments by tag

Use the **Sync Table Record Comments By Tag** job to synchronize comments between ServiceNow table records and Google SecOps cases.

#### Job requirements

For the job to function correctly, the Google SecOps case must possess the following two tags:

  * `ServiceNow TABLE_NAME` (where `<var class="readonly">TABLE_NAME</var>` is the name of the ServiceNow table, such as `incident`).
  * `ServiceNow TicketId: TICKET_ID` (where `<var class="readonly">TICKET_ID</var>` is the corresponding record's system ID or number).



#### Job parameters

The **Sync Table Record Comments By Tag** job requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Mandatory_ The API root of the ServiceNow instance. Default is `https://INSTANCE.service-now.com/api/now/v1/`.  
`Username` | _Mandatory_ The username of the ServiceNow instance.  
`Password` | `Mandatory`The password of the ServiceNow instance.  
`Table Name` | _Mandatory_ The name of the database table to search, such as `incident`.  
`Verify SSL` | _Optional_ If selected, the integration validates the SSL certificate when connecting to the ServiceNow server. Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
