---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-forms/
title: Integrate Google Forms with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:16.411147+00:00
---

# Integrate Google Forms with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-forms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Forms with Google SecOps 

This document explains how to integrate Google Forms with Google Security Operations (Google SecOps).

## Before you begin

Before you configure the **Google Forms** integration in Google SecOps, make sure your Google Cloud and Google Workspace environments are prepared for API access and impersonation.

For the integration to function correctly, three elements must align to manage permissions:

  1. **Service account** : Acts as the bridge between systems.

  2. **Delegated user** : The identity the service account impersonates to access form data.

  3. **Permissions** : The scopes and roles that define what the identity is allowed to do.




If the user you are impersonating already has the necessary administrative permissions, creating a custom role is not required. However, many organizations prefer to create a dedicated service user with a custom role to adhere to the principle of least privilege.

Complete the following prerequisite steps:

  1. Create a service account.
  2. Create a JSON key.
  3. Enable the required APIs for your project.
  4. Optional: Create a custom role for the integration.
  5. Optional: Assign the custom role to a user.
  6. Delegate domain-wide authority to your service account.



### Create a service account

The service account represents a non-human user that provides a secure way for the integration to authenticate and be authorized to access your data.

  1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Select **add_2 Create credentials > Service account**.

  3. Under **Service account details** , enter a name in the **Service account name** field.

  4. Optional: Edit the service account ID.

  5. Click **Done**.




### Create a JSON key

Google SecOps requires a JSON key file to prove the identity of the service account and establish a secure connection.

  1. Select your service account and go to **Keys**.

  2. Click **Add key > Create new key**.

  3. For the key type, select **JSON** and click **Create**. A **Private key saved to your computer** dialog appears and a copy of the private key downloads to your computer.




### Enable the required APIs for your project

You must enable the specific Google Cloud APIs that allow the integration to interact with Google Forms and the Google Workspace directory.

  1. In the Google Cloud console, go to **APIs & Services**.

[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)

  2. Click **add Enable APIs and Services**.

  3. Enable the following APIs for your project:

     * **Admin SDK API**

     * **Google Forms API**




### Optional: Create a custom role for the integration

**Note:** This step is only required if you are using a dedicated service user for the integration or if your existing user account lacks these specific Admin API privileges.

If the user account you're using for impersonation doesn't already have the necessary administrative permissions, you can create a custom role with limited privileges. To support the integration, the user requires Admin API privileges for the following:

  * **Organization Units**

  * **Users**

  * **Groups**



  1. In the Google Admin console, go to [**Account > Admin Roles**](https://admin.google.com/u/1/ac/list/roles).

  2. Select **Create new role**.

  3. Provide a name for the new custom role and click **Continue**.

  4. On **Select Privileges** , locate the **Admin API privileges** section.

  5. Select the checkboxes for **Organization Units** , **Users** , and **Groups**.

  6. Click **Continue > Create Role**.




### Optional: Assign the custom role to a user

If you created a custom role in the previous step, you must now assign it to the specific email address being used for impersonation.

  1. In the Google Admin console, go to **Directory > Users**.

  2. Select the user you intend to use for the integration (an existing administrator or a new dedicated user).

  3. Open settings for the user and click **Admin roles and privileges > edit Edit**.

  4. Select the custom role you created and switch the toggle to **Assigned**.

  5. Click **Save**.




### Delegate domain-wide authority to your service account

Domain-wide delegation allows your service account to access data across your entire Google Workspace domain by impersonating the authorized user.

  1. From your domain's Google Admin console, go to **Security > Access and data control > API controls**.

  2. In the **Domain wide delegation** pane, select **Manage Domain Wide Delegation**.

  3. Click **Add new**.

  4. In the **Client ID** field, enter the client ID of the service account created in the first step.

  5. In the **OAuth Scopes** field, enter the following comma-delimited list of required scopes:
         
         https://mail.google.com/,
         https://www.googleapis.com/auth/admin.directory.customer.readonly,
         https://www.googleapis.com/auth/admin.directory.domain.readonly,
         https://www.googleapis.com/auth/admin.directory.group,
         https://www.googleapis.com/auth/admin.directory.group.member,
         https://www.googleapis.com/auth/admin.directory.orgunit,
         https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly,
         https://www.googleapis.com/auth/admin.directory.user,
         https://www.googleapis.com/auth/admin.directory.user.alias,
         https://www.googleapis.com/auth/apps.groups.settings,
         https://www.googleapis.com/auth/cloud-platform,
         https://www.googleapis.com/auth/forms.body.readonly,
         https://www.googleapis.com/auth/forms.responses.readonly
         

  6. Click **Authorize**.




## Integration parameters

The Google Forms integration requires the following parameters:

Parameter | Description  
---|---  
`Delegated Email` | _Required_ An email address to use for the impersonation and access control.  
`Service Account JSON` | _Required_ The content of the service account key JSON file.   
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to Google Forms is valid. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the Ping action to test the connectivity to Google Forms.

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
`Successfully connected to the Google Forms server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Forms server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Google Forms – Responses Connector

Use the **Google Forms – Responses Connector** to pull responses from Google Forms.

The **Google Forms – Responses Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `Product Name`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `event_type`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to the default environment.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | _Required_ The timeout limit in seconds for the Python process running the current script.The default value is 300 seconds.   
`Delegated Email` | _Required_ An email address to use for the impersonation and access control.  
`Service Account JSON` | _Required_ The content of the service account key JSON file.   
`Form IDs To Track` | _Required_ A comma-separated list of Google Forms IDs to track for responses. To retrieve a form's unique ID, open the form in the **Forms editor** (not the public response link) and copy the string located between `/d/` and `/edit` in the full address shown in your browser's bar.  
`Alert Severity` | _Optional_ A severity level to assign to all alerts that the connector creates based on the ingested Google Forms response. The possible values are as follows:

  * `Informational`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

The default value is `Low`.  
`Max Hours Backwards` | _Required_ A number of hours before the first connector iteration to retrieve responses from. This parameter applies either to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is 1 hour.  
`Max Responses To Fetch` | _Required_ The maximum number of responses to process for every connector iteration.The maximum number is 100.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Not selected by default.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to Google Forms is valid.Not selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The **Google Forms – Responses Connector** supports proxies.

##### Connector events

The following example shows the JSON output of a Google SecOps event that the **Google Forms – Responses Connector** generated:
    
    
    {
       "responseId": "RESPONSE_ID",
       "createTime": "2024-09-05T11:43:13.892Z",
       "lastSubmittedTime": "2024-09-05T11:43:13.892123Z",
       "event_type": "Question",
       "questionId": "78099fe3",
       "textAnswers": {
           "answers": [
               {
                   "value": "Option 1"
               }
           ]
       }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
