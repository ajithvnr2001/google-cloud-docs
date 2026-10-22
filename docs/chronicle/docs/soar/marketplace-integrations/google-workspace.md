---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace/
title: Integrate Google Workspace with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:15.088104+00:00
---

# Integrate Google Workspace with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Workspace with Google SecOps

This document explains how to integrate Google Workspace with Google Security Operations.

**Important:** G Suite was rebranded to Google Workspace. In the Google SecOps platform, the integration for Google Workspace is called _G Suite_.

## Use cases

Integrating Google Workspace with Google SecOps can help you solve the following use case:

  * **User offboarding and account security:** use the Google SecOps capabilities to trigger a workflow for revoking the Google Workspace access, suspend accounts, and forward emails for offboarded users to another employee.



## Before you begin

Before you configure the Google Workspace integration in Google SecOps, complete the following prerequisite steps:

  1. Create a service account.
  2. Delegate domain-wide authority to your service account.
  3. Enable the Admin SDK API for your project.
  4. Grant the necessary Google Cloud IAM role to your service account.
  5. Choose and configure one of the following authentication methods: 
     * **Option 1:JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity isn't available in your environment.
     * **Option 2:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store any secrets.



### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your project.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**.

  3. Provide a name and description and click **Done** to finish creating the account.




### Delegate domain-wide authority to your service account

  1. From your domain's Google Admin console, go to **menu Main menu > Security > Access and data control > API controls**.
  2. In the **Domain wide delegation** pane, select **Manage Domain Wide Delegation**.
  3. Click **Add new**.
  4. In the **Client ID** field, enter the client ID obtained from the preceding service account creation steps.
  5. In the **OAuth Scopes** field, enter the following comma-delimited list of the scopes required for your application:
         
         https://mail.google.com/,
         https://www.googleapis.com/auth/cloud-platform,
         https://www.googleapis.com/auth/admin.directory.user,
         https://www.googleapis.com/auth/admin.directory.group.member,
         https://www.googleapis.com/auth/admin.directory.customer.readonly,
         https://www.googleapis.com/auth/admin.directory.domain.readonly,
         https://www.googleapis.com/auth/admin.directory.group,
         https://www.googleapis.com/auth/admin.directory.orgunit,
         https://www.googleapis.com/auth/admin.directory.user.alias,
         https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly,
         https://www.googleapis.com/auth/apps.groups.settings,
         https://www.googleapis.com/auth/admin.directory.user.security,
         https://www.googleapis.com/auth/admin.reports.audit.readonly,
         https://www.googleapis.com/auth/admin.directory.device.chromebrowsers.readonly,
         https://www.googleapis.com/auth/chrome.management.appdetails.readonly,
         https://www.googleapis.com/auth/chrome.management.policy
         

  6. Click **Authorize**.




### Enable the Admin SDK API for your project

  1. In the Google Cloud console, go to **APIs & Services**.

[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)

  2. Click **Enable APIs and Services**.

  3. Enable the **Admin SDK API** for your project.




### Configure a JSON key

Choose this method or the Workload Identity method to authenticate the integration. Use the JSON key method only if Workload Identity isn't available in your environment, as Workload Identity is the recommended and more secure approach. This method relies on a static, long-lived secret key file that requires manual management and rotation.

Use the following procedure to generate the JSON key file required to authenticate the integration:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key**.

  4. Select **Create new key**.

  5. For the key type, select **JSON** and click **Create**. The JSON file downloads to your computer.

  6. Copy the entire content of this file and paste it into `User's Service Account JSON` during integration configuration.




#### Configure Google Workspace permissions

Use the following procedure to define the administrative privileges the integration requires to manage organizational resources:

  1. In the Google Admin console, go to **Account > Admin Roles**.
  2. Click **Create new role**.
  3. Provide a name for the new custom role and click **Continue**.
  4. On the **Select Privileges** page, go to the **Admin API** privileges section.
  5. Under **Admin API privileges** , select the following privileges:

     * `Organization Units`
     * `Users`
     * `Groups`
  6. Click **Continue**.

  7. To create a new custom role, click **Create Role**.




##### Assign the custom role to a user

Use the following procedure to assign the role to a user account, authorizing the integration to perform actions on your behalf:

  1. To create a new user, go to **Directory > Users** page.
  2. Add a new user that is associated with the service account.
  3. Open settings for the newly created user. The user account tab opens.
  4. Click **Admin roles and privileges**.
  5. Click edit **Edit**.
  6. Select the custom role you created.
  7. For the selected role, switch the toggle to **Assigned**.



### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store or rotate long-lived secrets.

#### Identify the unique instance identity

To use Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This is the final step that allows the instance to securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the integration you're configuring, and enter your service account email in the `Workload Identity Email` field.

  3. Enter the email you want the integration to impersonate in the `Delegated Email` field.

  4. Click **Save > Test**. The test is expected to fail. 

  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).

**Note:** It may take a few minutes after completing this step for the test to pass.



## Integration parameters

The Google Workspace integration requires the following parameters:

Parameter | Description  
---|---  
`Verify SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to Google Workspace. Selected by default.  
`User's Service Account JSON` | Optional.The content of the service account key JSON file. Only configure this parameter if you are authenticating using a JSON key. To configure this parameter, provide the full content of the service account key JSON file that you downloaded when you created a service account.  
`Delegated Email` | Required.The email address for the integration to use.  
`Workload Identity Email` | Optional.The client email address of your service account. Only configure this parameter if you are authenticating using a Workload Identity.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Add Members To Group

Use the **Add Members To Group** action to add users to a group.

This action runs on the `User` entity.

The **Add Members To Group** action solves the following use cases:

  * Automated onboarding and offboarding.
  * Incident response by granting temporary access.
  * Dynamic project collaboration.



#### Action inputs

The **Add Members To Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Address` | Required.An email address of the group to add new members to.   
`User Email Addresses` | Optional.A comma-separated list of users to add to the group.The action executes values that you configure for this parameter alongside the `User` entity.   
  
#### Action outputs

The **Add Members To Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Add Members To Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Block Extension

Use the **Block Extension** action to block a specified Chrome extension in an organizational unit.

This action doesn't run on Google SecOps entities. 

**Note:** A Chrome Enterprise license is required to use this action.

#### Action inputs

The **Block Extension** action requires the following parameters:

Parameter | Description  
---|---  
`Organization Unit Name` | Required. The name of the organizational unit in which to block the extension.  
`Extension ID` | Required. The ID of the extension to block.  
  
#### Action outputs

The **Block Extension** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Block Extension** action:
    
    
    [
            {
                "targetKey": {
                    "targetResource": "orgunits/example-org-unit-id",
                    "additionalTargetKeys": {
                        "app_id": "chrome:exampleextensionid"
                    }
                },
                "value": {
                    "policySchema": "chrome.users.apps.InstallType",
                    "value": {
                        "appInstallType": "BLOCKED"
                    }
                },
                "sourceKey": {
                    "targetResource": "orgunits/example-org-unit-id"
                },
                "addedSourceKey": {
                    "targetResource": "orgunits/example-org-unit-id"
                }
            }
    ]
    

##### Output messages

The **Block Extension** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully blocked extension EXTENSION_ID in Organization Unit ORGANIZATION_NAME using Google Workspace.` | The action succeeded.  
`Error executing action "Block Extension". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Block Extension** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create Group

Use the **Create Group** action to create groups for your organization in the Google Admin console, Groups API, or Google Cloud Directory Sync as a Google Workspace Groups administrator.

If you use **Groups for Business** , you can also create groups for your organization in [**Google Groups**](http://groups.google.com/).

This action runs on all Google SecOps entities.

You can use the **Create Group** action in the following use cases:

  * Create incident response teams.
  * Contain phishing campaigns.
  * Onboard new users and user groups.
  * Collaborate on projects.
  * Configure access control for sensitive data.



#### Action inputs

The **Create Group** action requires the following parameters:

Parameter | Description  
---|---  
`Email Address` | Required.An email address of the new group.  
`Name` | Optional.A name of the new group.  
`Description` | Optional.A description of the new group.  
  
#### Action outputs

The **Create Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Create Group** action:
    
    
    [
       {
          "kind":"admin#directory#group",
          "id":"ID",
          "etag":"TAG/var>",
          "email":"user@example.com",
          "name":"example",
          "description":"",
          "adminCreated":"True"
       }
    ]
    

##### Script result

The following table describes the values for the script result output when using the **Create Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create OU

Use the **Create OU** action to create a new organizational unit (OU).

This action runs on all Google SecOps entities.

You can use the **Create OU** action to solve the following use cases:

  * Onboard new departments.
  * Isolate compromised accounts.
  * Implement geographic-based policies for data residency.



#### Action inputs

The **Create OU** action requires the following parameters:

Parameter | Description  
---|---  
`Customer ID` | Required.A unique ID of the customer's Google Workspace account.To configure the account `customerId`, you can also use the following placeholder: `my_customer`.  
`Name` | Optional.A name of the new OU.  
`Description` | Optional.A description of the new OU.  
`Parent OU Path` | Required.A full path to the parent OU of a new OU.  
  
#### Action outputs

The **Create OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Create OU** action:
    
    
    [
       {
          "kind":"admin#directory#orgUnit",
          "etag":"TAG",
          "name":"example",
          "orgUnitPath":"/example_folder",
          "orgUnitId":"id:ID",
          "parentOrgUnitPath":"/",
          "parentOrgUnitId":"id:ID"
       }
    ]
    

##### Script result

The following table describes the values for the script result output when using the **Create OU** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create User

Use the **Create User** action to create a new user.

When you add a user to your Google Workspace account, you provide them with an email address at your business domain and an account that they can use to access the Google Workspace services.

This action runs on all Google SecOps entities.

You can use the **Create User** action to solve the following use cases:

  * Automate onboarding for the new users.
  * Provide temporary access for contract employees.
  * Use sandboxes for incident response.



#### Action inputs

The **Create User** action requires the following parameters:

Parameter | Description  
---|---  
`Given Name` | Required.The user's first name.  
`Family Name` | Required.The user's last name.  
`Password` | Required.The password of the new user.  
`Email Address` | Required.The primary email address of the user.  
`Phone` | Optional.The phone number of the user.  
`Gender` | Optional.The gender of the user.The valid values are as follows: `female`, `male`, `other`, `unknown`.  
`Department` | Optional.The name of the user's department.  
`Organization` | Optional.The name of the user's organization.  
`Change Password At Next Login` | Optional.If selected, the system requires the user to change their password on the next login attempt.Not selected by default.  
  
#### Action outputs

The **Create User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Create User** action:
    
    
    [
       {
          "kind":"admin#directory#user",
          "id":"ID",
          "etag":"TAG",
          "primaryEmail":"example@example.com",
          "name":{
             "givenName":"FIRST_NAME",
             "familyName":"LAST_NAME"
          },
          "isAdmin":"False",
          "isDelegatedAdmin":"False",
          "creationTime":"2020-12-22T13:44:29.000Z",
          "organizations":[
             {
                "name":"ExampleOrganization"
             }
          ],
          "phones":[
             {
                "value":"(800)&nbsp;555&#8209;0175"
             }
          ],
          "gender":{
             "type":"male"
          },
          "customerId":"ID",
          "orgUnitPath":"/",
          "isMailboxSetup":"False"
       }
    ]
    

##### Script result

The following table describes the values for the script result output when using the **Create User** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Extension

Use the **Delete Extension** action to delete a specified Chrome extension from an organizational unit.

This action doesn't run on Google SecOps entities. 

**Note:** A Chrome Enterprise license is required to use this action.

#### Action inputs

The **Delete Extension** action requires the following parameters:

Parameter | Description  
---|---  
`Organization Unit Name` | Required. The name of the organizational unit from which to delete the extension.  
`Extension ID` | Required. The ID of the extension to delete.  
  
#### Action outputs

The **Delete Extension** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Delete Extension** action:
    
    
    [
      {
        "deleted_extensions": ["chrome:exampleextensionid"]
      }
    ]
    

##### Output messages

The **Delete Extension** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted extension EXTENSION_ID from Organization Unit ORGANIZATION_NAME using Google Workspace.` | The action succeeded.  
`Error executing action "Delete Extension". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Extension** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Group

Use the **Delete Group** action to delete a Google Workspace directory group.

This action doesn't run on Google SecOps entities.

You can use the **Delete Group** action to solve the following use cases:

  * Automate the offboarding of users.
  * Remediate security incidents.
  * Perform cleanups for stale groups.



#### Action inputs

The **Delete Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Address` | Required.An email address of the group to delete.  
  
#### Action outputs

The **Delete Group** action provides the following outputs:

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

The **Delete Group** action provides the following output messages:

Output message | Message description  
---|---  
`Google Workspace group GROUP_EMAIL deleted.` `Action was not able to find Google Workspace group for deletion. ` | The action succeeded.  
`Failed to connect to the Google Workspace! Error is ERROR_DESCRIPTION` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Delete Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete OU

Use the **Delete OU** action to delete an organizational unit.

You cannot delete an organization if it has users, devices, or child organizations. Before deleting an organization, move any users and devices to other organizations, and remove any child organizations.

This action runs on all Google SecOps entities.

You can use the **Delete OU** action to solve the following use cases:

  * Automate the offboarding of users.
  * Remediate security incidents.
  * Manage project resources and perform project cleanups.



#### Action inputs

The **Delete OU** action requires the following parameters:

Parameter | Description  
---|---  
`Customer ID` | Required.A unique ID of the customer's Google Workspace account.To configure the account `customerId`, you can also use the following placeholder: `my_customer`.  
`OU Path` | Required.A full path to the organizational unit.If the organizational unit is located under a root (/) path, provide the organizational unit name without a path.  
  
#### Action outputs

The **Delete OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Delete OU** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete User

Use the **Delete User** action to delete user accounts.

After you delete a user, they cannot access or use any Google Workspace services for your organization.

You can use the **Delete User** action to solve the following use cases:

  * Offboard departing employees.
  * Remediate compromised accounts.
  * Automate the cleanup of temporary accounts.



This action runs on all Google SecOps entities.

#### Action inputs

The **Delete User** action requires the following parameters:

Parameter | Description  
---|---  
`Email Address` | Required.An email address of the user to delete.  
  
#### Action outputs

The **Delete User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Delete User** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Entities

Use the **Enrich Entities** action to enrich Google SecOps entities with information from Google Workspace.

This action runs on the `User` entity.

You can use the **Enrich Entities** action to solve the following use cases:

  * Investigate users.
  * Analyze phishing emails.
  * Investigate data exfiltration attempts.
  * Detect malware.



#### Action inputs

None.

#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment

The **Enrich Entities** action support the following entity enrichment:

Enrichment field name | Enrichment logic  
---|---  
`Phones` | Returns if it exists in a JSON result.  
`isDelegatedAdmin` | Returns if it exists in a JSON result.  
`suspended` | Returns if it exists in a JSON result.  
`id` | Returns if it exists in a JSON result.  
`nonEditableAliases` | Returns if it exists in a JSON result.  
`archived` | Returns if it exists in a JSON result.  
`isEnrolledIn2Sv` | Returns if it exists in a JSON result.  
`includeInGlobalAddressList` | Returns if it exists in a JSON result.  
`Relations` | Returns if it exists in a JSON result.  
`isAdmin` | Returns if it exists in a JSON result.  
`etag` | Returns if it exists in a JSON result.  
`lastLoginTime` | Returns if it exists in a JSON result.  
`orgUnitPath` | Returns if it exists in a JSON result.  
`agreedToTerms` | Returns if it exists in a JSON result.  
`externalIds` | Returns if it exists in a JSON result.  
`ipWhitelisted` | Returns if it exists in a JSON result.  
`kind` | Returns if it exists in a JSON result.  
`isEnforcedIn2Sv` | Returns if it exists in a JSON result.  
`isMailboxSetup` | Returns if it exists in a JSON result.  
`emails` | Returns if it exists in a JSON result.  
`organizations` | Returns if it exists in a JSON result.  
`primaryEmail` | Returns if it exists in a JSON result.  
`name` | Returns if it exists in a JSON result.  
`gender` | Returns if it exists in a JSON result.  
`creationTime` | Returns if it exists in a JSON result.  
`changePasswordAtNextLogin` | Returns if it exists in a JSON result.  
`customerId` | Returns if it exists in a JSON result.  
  
##### JSON result

The following example describes the JSON result output received when using the **Enrich Entities** action:
    
    
    [{
        "Phones":
           [{
              "customType": "",
              "type": "custom",
              "value": "(800)&nbsp;555&#8209;0175"
           }],
       "isDelegatedAdmin": false,
       "suspended": false,
       "id": "ID",
       "nonEditableAliases": ["user@example.com"],
       "archived": false,
       "isEnrolledIn2Sv": true,
       "includeInGlobalAddressList": true,
       "Relations":
            [{
              "type": "manager",
              "value": "user@example.com"
            }],
       "isAdmin": false,
       "etag": "E_TAG_VALUE",
       "lastLoginTime": "2019-02-11T12:24:41.000Z",
       "orgUnitPath": "/OU-1",
       "agreedToTerms": true,
       "externalIds": [{"type": "organization",
                        "value": ""}],
       "ipWhitelisted": false,
       "kind": "admin#directory#user",
       "isEnforcedIn2Sv": true,
       "isMailboxSetup": true,
       "emails":
           [{
              "primary": true,
              "address": "user@example.com"
            },
            {
              "address": "user@example.com"
            }],
        "organizations":
            [{
               "department": "R&D",
               "customType": "", "name": "Company"
             }],
         "primaryEmail": "user@example.com",
         "name":
             {
                "fullName": "NAME SURNAME",
                "givenName": "NAME",
                "familyName": "SURNAME"
             },
         "gender": {"type": "male"},
         "creationTime": "2017-10-26T06:57:13.000Z",
         "changePasswordAtNextLogin": false,
         "customerId": "CUSTOMER_ID"
    }]
    

##### Script result

The following table describes the values for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Extension Details

Use the **Get Extension Details** action to retrieve information about a specified Chrome extension.

This action doesn't run on Google SecOps entities. 

**Note:** A Chrome Enterprise license is required to use this action.

#### Action inputs

The Get Extension Details action requires the following parameters:

Parameter | Description  
---|---  
`Extension ID` | Required. A comma-separated list of extension IDs to enrich.  
`Max Requesting Users To Return` | Required. The maximum number of users to return who requested the extension installation. The maximum value is `1000`.  
`Max Requesting Devices To Return` | Required. The maximum number of devices to return where the extension installation was requested. The maximum value is `1000`.  
  
#### Action outputs

The **Get Extension Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Extension Details** action:
    
    
    [
      {
        "Entity": "Example Extension Name",
        "EntityResult": {
          "name": "customers/example-customer-id/apps/chrome/exampleextensionid",
          "displayName": "Example Extension Name",
          "description": "A description for an example extension.",
          "appId": "exampleextensionid",
          "revisionId": "11.3.0.0",
          "type": "CHROME",
          "iconUri": "https://lh3.googleusercontent.com/KxYKwMcAzhn_DBMVIb0mtvIOsAME2d8-csv5d_vnKYX6PL3D6BGbVy3hH68ky8nM9yTDGAPl6B77pA7tpu4_jeUkXw",
          "detailUri": "https://chromewebstore.google.com/detail/exampleextensionid",
          "firstPublishTime": "2011-12-14T06:57:01.918Z",
          "latestPublishTime": "2025-07-01T02:05:04.252Z",
          "publisher": "example-publisher",
          "reviewNumber": "5423",
          "reviewRating": 4,
          "chromeAppInfo": {
            "supportEnabled": true,
            "minUserCount": 3000000,
            "permissions": [
              {
                "type": "offscreen"
              },
              {
                "type": "scripting",
                "documentationUri": "https://developer.chrome.com/docs/extensions/reference/scripting/",
                "accessUserData": false
              },
              {
                "type": "storage",
                "documentationUri": "https://developer.chrome.com/docs/extensions/reference/storage/",
                "accessUserData": false
              },
              {
                "type": "tabs",
                "documentationUri": "https://developer.chrome.com/docs/extensions/reference/tabs#type-Tab",
                "accessUserData": true
              }
            ],
            "siteAccess": [
              {
                "hostMatch": "https://*/*"
              },
              {
                "hostMatch": "http://*/*"
              }
            ],
            "isTheme": false,
            "googleOwned": true,
            "isCwsHosted": true,
            "kioskEnabled": false,
            "isKioskOnly": false,
            "type": "EXTENSION",
            "isExtensionPolicySupported": false,
            "manifestVersion": "3",
            "requestingUserDetails": [
              {
                "email": "user@example.com",
                "justification": "Example justification for the request."
              }
            ],
            "requestingDeviceDetails": [
              {
                "device": "example-device-id",
                "justification": "Example justification for the request."
              }
            ]
          }
        }
      }
    ]
    

##### Output messages

The **Get Extension Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the following extensions in Google Workspace: EXTENSION_IDS.` `Action wasn't able to return information about the following extension in Google Workspace: EXTENSION_IDS.` `No information about the provided extensions were found.` | The action succeeded.  
`Error executing action "Get Extension Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Extension Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Group Details

Use the **Get Group Details** action to retrieve information about a group in Google Workspace.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Get Group Details** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Addresses` | Required.A comma-separated list of group emails to examine.   
  
#### Action outputs

The **Get Group Details** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Get Group Details** action:
    
    
    {
            "Entity": "group@example.com",
            "EntityResult": {
                "kind": "groupsSettings#groups",
                "email": "group@example.com",
                "name": "GROUP_NAME",
                "description": "DESCRIPTION",
                "whoCanJoin": "CAN_REQUEST_TO_JOIN",
                "whoCanViewMembership": "ALL_MEMBERS_CAN_VIEW",
                "whoCanViewGroup": "ALL_MEMBERS_CAN_VIEW",
                "whoCanInvite": "ALL_MANAGERS_CAN_INVITE",
                "whoCanAdd": "ALL_MANAGERS_CAN_ADD",
                "allowExternalMembers": "false",
                "whoCanPostMessage": "ANYONE_CAN_POST",
                "allowWebPosting": "true",
                "primaryLanguage": "en_US",
                "maxMessageBytes": 26214400,
                "isArchived": "false",
                "archiveOnly": "false",
                "messageModerationLevel": "MODERATE_NONE",
                "spamModerationLevel": "MODERATE",
                "replyTo": "REPLY_TO_IGNORE",
                "includeCustomFooter": "false",
                "customFooterText": "",
                "sendMessageDenyNotification": "false",
                "defaultMessageDenyNotificationText": "",
                "showInGroupDirectory": "true",
                "allowGoogleCommunication": "false",
                "membersCanPostAsTheGroup": "false",
                "messageDisplayFont": "DEFAULT_FONT",
                "includeInGlobalAddressList": "true",
                "whoCanLeaveGroup": "ALL_MEMBERS_CAN_LEAVE",
                "whoCanContactOwner": "ANYONE_CAN_CONTACT",
                "whoCanAddReferences": "NONE",
                "whoCanAssignTopics": "NONE",
                "whoCanUnassignTopic": "NONE",
                "whoCanTakeTopics": "NONE",
                "whoCanMarkDuplicate": "NONE",
                "whoCanMarkNoResponseNeeded": "NONE",
                "whoCanMarkFavoriteReplyOnAnyTopic": "NONE",
                "whoCanMarkFavoriteReplyOnOwnTopic": "NONE",
                "whoCanUnmarkFavoriteReplyOnAnyTopic": "NONE",
                "whoCanEnterFreeFormTags": "NONE",
                "whoCanModifyTagsAndCategories": "NONE",
                "favoriteRepliesOnTop": "true",
                "whoCanApproveMembers": "ALL_MANAGERS_CAN_APPROVE",
                "whoCanBanUsers": "OWNERS_AND_MANAGERS",
                "whoCanModifyMembers": "OWNERS_AND_MANAGERS",
                "whoCanApproveMessages": "OWNERS_AND_MANAGERS",
                "whoCanDeleteAnyPost": "OWNERS_AND_MANAGERS",
                "whoCanDeleteTopics": "OWNERS_AND_MANAGERS",
                "whoCanLockTopics": "OWNERS_AND_MANAGERS",
                "whoCanMoveTopicsIn": "OWNERS_AND_MANAGERS",
                "whoCanMoveTopicsOut": "OWNERS_AND_MANAGERS",
                "whoCanPostAnnouncements": "OWNERS_AND_MANAGERS",
                "whoCanHideAbuse": "NONE",
                "whoCanMakeTopicsSticky": "NONE",
                "whoCanModerateMembers": "OWNERS_AND_MANAGERS",
                "whoCanModerateContent": "OWNERS_AND_MANAGERS",
                "whoCanAssistContent": "NONE",
                "customRolesEnabledForSettingsToBeMerged": "false",
                "enableCollaborativeInbox": "false",
                "whoCanDiscoverGroup": "ALL_IN_DOMAIN_CAN_DISCOVER",
                "defaultSender": "DEFAULT_SELF"
            }
        }
    

##### Output messages

The **Get Group Details** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following groups using information from Google Workspace: GROUPS ` `Action wasn't able to enrich the following group using information from Google Workspace: GROUPS` `None of the groups were enriched.` | The action succeeded.  
`Error executing action "Get Group Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Group Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Host Browser Details

Use the **Get Host Browser Details** action to retrieve information about browsers associated with a specified Google SecOps `Hostname` entity.

This action runs on the Google SecOps `Hostname` entity.

**Note:** A Chrome Enterprise license is required to use this action.

#### Action inputs

None.

#### Action outputs

The **Get Host Browser Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Host Browser Details** action:
    
    
    {
       "Entity": "example.host.com",
       "EntityResult": [
          {
             "deviceId": "example-device-id",
             "kind": "admin#directory#browserdevice",
             "lastPolicyFetchTime": "2025-07-25T12:11:17.546Z",
             "osPlatform": "Linux",
             "osArchitecture": "x86_64",
             "osVersion": "6.12.27-1rodete1-amd64",
             "machineName": "example.host.com",
             "lastRegistrationTime": "2025-07-07T07:45:20.504Z",
             "extensionCount": "15",
             "policyCount": "23",
             "lastDeviceUser": "example-user",
             "lastActivityTime": "2025-07-26T12:13:55.385Z",
             "osPlatformVersion": "Linux 6.12.27-1rodete1-amd64",
             "browserVersions": [
                "140.0.7259.2 (Dev)"
             ],
             "lastStatusReportTime": "2025-07-26T07:46:00.919Z",
             "lastDeviceUsers": [
                {
                   "userName": "example-user",
                   "lastStatusReportTime": "2025-07-26T07:46:00.919Z"
                }
             ],
             "machinePolicies": [
                {
                   "source": "MACHINE_LEVEL_USER_CLOUD",
                   "name": "CloudReportingEnabled",
                   "value": "true"
                }
             ],
             "browsers": [
                {
                   "browserVersion": "140.0.7259.2",
                   "channel": "DEV",
                   "lastStatusReportTime": "2025-07-26T07:46:00.919Z",
                   "executablePath": "/opt/google/chrome-unstable",
                   "profiles": [
                      {
                         "name": "Example User Profile",
                         "id": "/home/example_user/.config/google-chrome/Default",
                         "lastStatusReportTime": "2025-07-26T07:46:00.919Z",
                         "lastPolicyFetchTime": "2025-07-25T12:11:17.546Z",
                         "chromeSignedInUserEmail": "user@example.com",
                         "extensions": [
                            {
                               "extensionId": "exampleextensionid",
                               "version": "2.0.6",
                               "permissions": [
                                  "alarms",
                                  "contextMenus",
                                  "management",
                                  "storage",
                                  "https://accounts.google.com/*",
                                  "https://appengine.google.com/*",
                                  "https://example.com/*",
                                  "https://example.org/*",
                                  "https://example-api.com/*",
                                  "https://docs.example.com/*",
                                  "https://internal.example.net/*",
                                  "https://partners.example.com/*",
                                  "https://www.google.com/*"
                               ],
                               ],
                               "name": "Example Extension",
                               "description": "This is a description for an example extension.",
                               "appType": "EXTENSION",
                               "homepageUrl": "https://chromewebstore.google.com/detail/exampleextensionid",
                               "installType": "ADMIN",
                               "manifestVersion": 3
                            }
                         ],
                         "userPolicies": [
                            {
                               "source": "USER_CLOUD",
                               "name": "CloudProfileReportingEnabled",
                               "value": "true"
                            }
                         ]
                      }
                   ],
                   "pendingInstallVersion": "140.0.7312.0"
                }
             ],
             "virtualDeviceId": "example-virtual-device-id",
             "orgUnitPath": "/",
             "deviceIdentifiersHistory": {
                "records": [
                   {
                      "identifiers": {
                         "machineName": "example.host.com"
                      },
                      "firstRecordTime": "2025-06-03T08:06:33.895Z",
                      "lastActivityTime": "2025-07-26T07:46:01.325Z"
                   }
                ]
             }
          }
       ]
    }
    

##### Output messages

The **Get Host Browser Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned browsers related to the following hostnames in Google Workspace: HOSTNAME.` `No browsers were associated with the following hostnames in Google Workspace: HOSTNAME.` `No browsers were associated with provided hostnames.` | The action succeeded.  
`Error executing action "Get Host Browser Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Host Browser Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Group Members

Use the **List Group Members** action to list the members of a Google Workspace group.

This action runs on all Google SecOps entities.

You can use the **List Group Members** action to solve the following use cases:

  * Automate user onboarding and offboarding.
  * Perform a security audit.
  * Respond to incidents.
  * Support the dynamic resource access.



#### Action inputs

The **List Group Members** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Address` | Required.An email address of the group.  
`Include Derived Membership` | Optional.If selected, the action lists indirect memberships of users in the group.Selected by default.  
  
#### Action outputs

The **List Group Members** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **List Group Members** action:
    
    
    {
       "status": "ACTIVE",
       "kind": "admin#directory#member",
       "email": "user1@example.com",
       "etag": "E_TAG_VALUE",
       "role": "MEMBER",
       "type": "USER",
       "id": "ID"
      },{
       "status": "ACTIVE",
       "kind": "admin#directory#member",
       "email": "user2@example.com",
       "etag": "E_TAG_VALUE",
       "role": "MEMBER",
       "type": "USER", "id": "ID"
    }
    

##### Script result

The following table describes the values for the script result output when using the **List Group Members** action:

Script result name | Value  
---|---  
`members` | `True` or `False`  
  
### List Group Privileges

Use the **List Group Privileges** action to list roles and privileges that are related to the Google Workspace group.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Group Privileges** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Addresses` | Optional.A comma-separated list of groups to examine.  
`Check Roles` | Optional.A comma-separated list of roles to check that are related to the group.  
`Check Privileges` | Optional.A comma-separated list of permissions that to check that are related to the group.This parameter requires you to select the **Expand Privileges** parameter. If you configured the **Check Roles** parameter, the action checks the privileges only for the roles that you listed.  
`Expand Privileges` | Optional.If selected, the action returns information about all unique privileges that are related to the group.  
`Max Roles To Return` | Required.The maximum number of roles that are related to the group to return.The default value is `100`.  
`Max Privileges To Return` | Required.The maximum number of privileges that are related to the group to return.The default value is `100`.  
  
#### Action outputs

The **List Group Privileges** action provides the following outputs:

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

The following example describes the JSON result output received when using the **List Group Privileges** action:
    
    
    {
        "Entity": "user@example.com",
        "EntityResult": {
            "roles": [
                "Role1",
                "_GROUPS_EDITOR_ROLE",
                "example-role"
            ],
            "unique_privileges": [
                "VIEW_SITE_DETAILS",
                "ACCESS_EMAIL_LOG_SEARCH",
                "ACCESS_ADMIN_QUARANTINE",
                "ACCESS_RESTRICTED_QUARANTINE",
                "ADMIN_QUALITY_DASHBOARD_ACCESS",
                "MANAGE_DLP_RULE",
                "DASHBOARD_ACCESS",
                "MANAGE_GSC_RULE",
                "VIEW_GSC_RULE",
                "SECURITY_HEALTH_DASHBOARD_ACCESS",
                "SIT_CALENDAR_VIEW_METADATA",
                "SIT_CHAT_VIEW_METADATA",
                "SIT_CHROME_VIEW_METADATA",
                "SIT_DEVICE_UPDATE_DELETE",
                "SIT_DEVICE_VIEW_METADATA",
                "SIT_DRIVE_UPDATE_DELETE"
            ]
        }
    }
    

##### Output messages

The **List Group Privileges** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched information for the following groups using information from Google Workspace: GROUPS` `Action wasn't able to fetch information for the following groups using information from Google Workspace: GROUPS` `None of the specific roles/privileges were found for the following groups in Google Workspace: GROUPS` `None of the specific roles/privileges were found for the provided groups in Google Workspace.` `No information was found for the provided groups in Google Workspace.` | The action succeeded.  
`Error executing action "List Group Privileges". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Group Privileges** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List OU of Account

Use the **List OU of Account** action to list organizational units of an account.

This action runs on all Google SecOps entities.

You can use the **List OU of Account** action to solve the following use cases:

  * Automate user offboarding.
  * Perform a targeted security auditing.
  * Automate a group membership management.
  * Streamline user provisioning.
  * Automate compliance reporting and auditing.



#### Integration inputs

The **List OU of Account** action requires the following parameters:

Parameter | Description  
---|---  
`Customer ID` | Required.A unique ID of the customer Google Workspace account.To represent the `customerId` value of the account, use the `my_customer` placeholder.  
`Organization Unit Path` | Optional. The path of the organizational unit to return. The default value is `/`.  
`Max Organization Units` | Required. The maximum amount of organizational units to return. The maximum value is `100`. The default value is `50`.  
  
#### Action outputs

The **List OU of Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **List OU of Account** action:
    
    
    [{
       "kind": "admin#directory#orgUnit",
       "parentOrgUnitPath": "/",
       "name": "OU-1",
       "etag": "E_TAG_VALUE",
       "orgUnitPath": "/OU-1",
       "parentOrgUnitId": "id:1455",
       "blockInheritance": false,
       "orgUnitId": "id:123",
       "description": ""
    }]
    

##### Script result

The following table describes the values for the script result output when using the **List OU of Account** action:

Script result name | Value  
---|---  
`organizational_units` | `True` or `False`  
  
### List User Privileges

Use the **List User Privileges** action to list roles and privileges that are related to the user in Google Workspace.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **List User Privileges** action requires the following parameters:

Parameter | Description  
---|---  
`User Email Addresses` | Optional.A comma-separated list of users to examine.The action executes values that you configure for this parameter alongside the `User` entity.  
`Check Roles` | Optional.A comma-separated list of roles to check that are related to the user.  
`Check Privileges` | Optional.A comma-separated list of permissions to verify that are related to the user.This parameter requires you to select the **Expand Privileges** parameter. If you configured the **Check Roles** parameter, the action checks the privileges only for the roles that you listed.  
`Include Inherited Roles` | Optional.If selected, the action additionally returns user roles that are inherited from groups.  
`Expand Privileges` | Optional.If selected, the action returns information about all unique privileges that are related to the user.  
`Max Roles To Return` | Required.The maximum number of roles that are related to the user to return.The default value is `100`.  
`Max Privileges To Return` | Required.The maximum number of privileges that are related to the user to return.The default value is `100`.  
  
#### Action outputs

The **List User Privileges** action provides the following outputs:

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

The following example describes the JSON result output received when using the **List User Privileges** action:
    
    
    {
        "Entity": "user@example.com",
        "EntityResult": {
            "roles": [
                "Role1",
                "_GROUPS_EDITOR_ROLE",
                "example-role"
            ],
            "unique_privileges": [
                "VIEW_SITE_DETAILS",
                "ACCESS_EMAIL_LOG_SEARCH",
                "ACCESS_ADMIN_QUARANTINE",
                "ACCESS_RESTRICTED_QUARANTINE",
                "ADMIN_QUALITY_DASHBOARD_ACCESS",
                "MANAGE_DLP_RULE",
                "DASHBOARD_ACCESS",
                "MANAGE_GSC_RULE",
                "VIEW_GSC_RULE",
                "SECURITY_HEALTH_DASHBOARD_ACCESS",
                "SIT_CALENDAR_VIEW_METADATA",
                "SIT_CHAT_VIEW_METADATA",
                "SIT_CHROME_VIEW_METADATA",
                "SIT_DEVICE_UPDATE_DELETE",
                "SIT_DEVICE_VIEW_METADATA",
                "SIT_DRIVE_UPDATE_DELETE"
            ]
        }
    }
    

##### Output messages

The **List User Privileges** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following users using information from Google Workspace: USERS` `Action wasn't able to enrich the following users using information from Google Workspace: USERS` `None of the specific roles/privileges were found for the following users in Google Workspace: USERS` `None of the specific roles/privileges were found for the provided users in Google Workspace.` `None of the provided users were enriched in Google Workspace. ` | The action succeeded.  
`Error executing action "List User Privileges". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List User Privileges** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Users

Use the **List Users** action to list users present in an account.

This action doesn't run on Google SecOps entities.

You can use the **List Users** action to solve the following use cases:

  * Identify potentially compromised accounts.
  * Automate offboarding processes.
  * Audit and manage user access privileges
  * Investigate suspicious activities.
  * Manage user licenses and resources.



#### Action inputs

The **List Users** action requires the following parameters:

Parameter | Description  
---|---  
`Customer ID` | Optional.A unique ID of the customer Google Workspace account.If you don't provide this parameter value, the action automatically uses the `my_customer` placeholder to represent a customer ID of the account.  
`Domain` | Optional.A domain to search for users.  
`Manager Email` | Optional.An email address of a user's manager.  
`Return Only Admin Accounts?` | Optional.If selected, the action returns only administrator accounts.Not selected by default.  
`Return Only Delegated Admin Accounts?` | Optional.If selected, the action returns only delegated administrator accounts.Not selected by default.  
`Return Only Suspended Users?` | Optional.If selected, the action returns only suspended accounts.Not selected by default.  
`Org Unit Path` | Optional.A full path of an organization unit from which to retrieve the users. The path matches all organization unit chains listed under the target unit.  
`Department` | Optional.A department within the organization from which to retrieve the users.  
`Record Limit` | Optional.The maximum number of data records for the action to return.The default value is `20`.  
`Custom Query Parameter` | Optional.A custom query parameter to add to the list users search call, such as `orgName='Human Resources'`. You can configure this parameter with the `email` field, or leave the `email` field empty and configure the `Email Addresses` parameter. If you configure both the `email` field and the `Email Addresses` parameter, the generated query fails.  
`Return only users without 2fa?` | Optional.If selected, the action only returns users who don't have the two-factor authentication (2FA) enabled.Not selected by default.  
`Email Addresses` | Optional.A comma-separated list of email addresses to search. If you configure this parameter, don't configure the `email` field in the `Custom Query Parameter` parameter.If you configure this parameter, the action ignores the `Record Limit` parameter.  
  
#### Action outputs

The **List Users** action provides the following outputs:

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

The **List Users** action provides the following table on a Case Wall:

Table name: **Google G Suite Users**

Table columns:

  * **ID**
  * **Email**
  * **Given Name**
  * **Family Name**
  * **Is Admin?**
  * **Is Delegated Admin?**
  * **Creation Time**
  * **Last Login Time**
  * **Suspended?**
  * **Archived?**
  * **Change Password At Next Login?**
  * **Customer ID**
  * **Org Unit Path**
  * **Is Mailbox set?**
  * **Recovery Email**



##### JSON result

The following example describes the JSON result output received when using the **List Users** action:
    
    
    {
        "kind": "admin#directory#users",
        "etag": "E_TAG_VALUE",
        "users": [
            {
                "kind": "admin#directory#user",
                "id": "ID",
                "etag": "E_TAG_VALUE",
                "primaryEmail": "user@example.com",
                "name": {
                    "givenName": "NAME",
                    "familyName": "SURNAME",
                    "fullName": "NAME SURNAME"
                },
                "isAdmin": true,
                "isDelegatedAdmin": false,
                "lastLoginTime": "2020-12-22T06:40:34.000Z",
                "creationTime": "2020-07-22T09:23:28.000Z",
                "agreedToTerms": true,
                "suspended": false,
                "archived": false,
                "changePasswordAtNextLogin": false,
                "ipWhitelisted": false,
                "emails": [
                    {
                        "address": "user@example.com",
                        "primary": true
                    },
                    {
                        "address": "user@example.com"
                    }
                ],
                "nonEditableAliases": [
                    "user@example.com"
                ],
                "customerId": "CUSTOMER_ID",
                "orgUnitPath": "/Management",
                "isMailboxSetup": true,
                "isEnrolledIn2Sv": false,
                "isEnforcedIn2Sv": false,
                "includeInGlobalAddressList": true,
                "recoveryEmail": "email@example.com"
            }
        ]
    }
    

##### Output messages

The **List Users** action provides the following output messages:

Output message | Message description  
---|---  
`Action successfully returned the Google Workspace Directory user list.` `No users were returned.` | The action succeeded.  
`Failed to connect to the Google Workspace! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Users** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to Google Workspace.

This action runs on all Google SecOps entities.

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
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Extension

**Important:** This action requires the following authorization scope: `https://www.googleapis.com/auth/chrome.management.policy`

Use the **Remove Extension** action to uninstall a specific Chrome extension from all registered browsers within a designated organizational unit.

This action doesn't run on Google SecOps entities. 

**Note:** A Chrome Enterprise license is required to use this action.

#### Action inputs

The **Remove Extension** action requires the following parameters:

Parameter | Description  
---|---  
`Organization Unit Name` | Required. The name of the organizational unit from which to remove the extension.  
`Extension ID` | Required. The ID of the extension to remove.  
  
#### Action outputs

The **Remove Extension** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Remove Extension** action:
    
    
    [
      {
        "removed_extensions": ["chrome:exampleextensionid"]
      }
    ]
    

##### Output messages

The **Remove Extension** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed extension EXTENSION_ID from Organization Unit ORGANIZATION_NAME using Google Workspace.` | The action succeeded.  
`Error executing action "Remove Extension". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Extension** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Members From Group

Use the **Remove Members From Group** action to remove members from a Google Workspace group.

This action runs on the Google SecOps `User` entity.

You can use the **List Users** action to solve the following use cases:

  * Automate user offboarding.
  * Execute dynamic group management.
  * Remediate access control issues.



#### Action inputs

The **Remove Members From Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Email Address` | Required.An email of the group from which to remove the members.  
`User Email Addresses` | Optional.A comma-separated list of users to remove from the group.The action executes values that you configure for this parameter alongside the `User` entity.   
  
#### Action outputs

The **Remove Members From Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Members From Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Revoke User Sessions

Use the **Revoke User Sessions** action to revoke the user web and device sessions and reset their sign-in cookies in Google Workspace.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Revoke User Sessions** action requires the following parameters:

Parameter | Description  
---|---  
`User Email Addresses` | Optional.A comma-separated list of users to sign out. The action runs the values from this parameter with Google SecOps `User` entities.  
  
#### Action outputs

The **Revoke User Sessions** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Revoke User Sessions** action:
    
    
    [
       {
           "Entity": "ENTITY_ID",
           "EntityResult": {
               "Status": "done"
           }
       }
    ]
    

##### Output messages

The **Revoke User Sessions** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully signed out the following users using Google Workspace: USERS` `Action wasn't able to sign out the following users using Google Workspace: USERS` `None of the provided users were found in Google Workspace.` | The action succeeded.  
`Error executing action "Revoke User Sessions". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Revoke User Sessions** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search User Activity Events

Use the **Search User Activity Events** action to retrieve activity events from an application for a specified Google SecOps `User` entity.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Search User Activity Events** action requires the following parameters:

Parameter | Description  
---|---  
`User Email Addresses` | Optional. A comma-separated list of additional user email addresses to process. The action processes all users in this list in addition to a `User` entity (if one is provided).  
`Application Names` | Required. A list of applications to query for activity events. For a full list of supported applications, see the [ApplicationName documentation](https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list#applicationname).  
`Event Type Filter` | Optional. A comma-separated list of event types to retrieve.  
`Time Frame` | Optional. The timeframe for the activity search. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

If `Custom` is selected, the `Start Time` parameter is required. The default value is `Last Hour`.  
`Start Time` | Optional. The start of the time range for the activity search. This parameter is required if `Custom` is selected for the `Time Frame` parameter. Configure the value in ISO 8601 format.  
`End Time` | Optional. The end of the time range for the activity search. This parameter is optional when `Custom` is selected for the `Time Frame` parameter and defaults to the current time if not provided. Configure the value in ISO 8601 format.  
`Max Events To Return` | Required. The maximum number of events to return per user. The action processes a maximum of `1000` events per user, per application. The default value is `200`. The maximum value is `1000`.  
  
#### Action outputs

The **Search User Activity Events** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search User Activity Events** action:
    
    
    {
       "Entity": "user@example.com",
       "EntityResult": [
          {
             "applicationName": "login",
             "type": "login",
             "name": "login_success",
             "parameters": [
                {
                   "name": "login_type",
                   "value": "google_password"
                },
                {
                   "name": "login_challenge_method",
                   "multiValue": [
                      "password"
                   ]
                },
                {
                   "name": "is_suspicious",
                   "boolValue": false
                }
             ]
          },
          {
             "applicationName": "token",
             "type": "auth",
             "name": "authorize",
             "parameters": [
                {
                   "name": "client_id",
                   "value": "example-client-id.apps.googleusercontent.com"
                },
                {
                   "name": "app_name",
                   "value": "Google Chrome"
                },
                {
                   "name": "client_type",
                   "value": "NATIVE_DESKTOP"
                },
                {
                   "name": "scope_data",
                   "multiMessageValue": [
                      {
                         "parameter": [
                            {
                               "name": "scope_name",
                               "value": "https://www.google.com/accounts/OAuthLogin"
                            },
                            {
                               "name": "product_bucket",
                               "multiValue": [
                                  "IDENTITY"
                               ]
                            }
                         ]
                      }
                   ]
                },
                {
                   "name": "scope",
                   "multiValue": [
                      "https://www.google.com/accounts/OAuthLogin"
                   ]
                }
             ]
          }
       ]
    }
    

##### Output messages

The **Search User Activity Events** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found events for the following users in Google Workspace: USERS.` `No events were found for the following users in Google Workspace: USERS.` `No events were found for the provided users in Google Workspace.` | The action succeeded.  
`Error executing action "Search User Activity Events". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search User Activity Events** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update OU

Use the **Update OU** action to update an organizational unit (OU).

This action runs on all Google SecOps entities.

You can use the **Update OU** action to solve the following use cases:

  * Manage security groups.
  * Automate onboarding and offboarding of users.
  * Implement data separation policies.



#### Action inputs

The **Update OU** action requires the following parameters:

Parameter | Description  
---|---  
`Customer ID` | Required.A unique ID of the customer Google Workspace account.To represent the `customerId` value of the account, use the `my_customer` placeholder.  
`Name` | Optional.A name of the OU.  
`Description` | Optional.A description of the OU.  
`OU Path` | Required.A full path to the OU.If the OU is located under the root path, `/`, provide only the OU name without a path.  
  
#### Action outputs

The **Update OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Update OU** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update User

Use the **Update User** action to update a Google Workspace directory user.

This action doesn't run on Google SecOps entities.

You can use the **Update User** action to solve the following use cases:

  * Disable a compromised account.
  * Enforce a password reset after detecting suspicious activity.
  * Update department information after completing an employee transfer.
  * Suspend inactive accounts.



#### Action inputs

The **Update User** action requires the following parameters:

Parameter | Description  
---|---  
`Email Address` | Required.A comma-separated list of primary email addresses that are used to identify what users to update.  
`Given Name` | Optional.The user's first name.  
`Family Name` | Optional.The user's last name.  
`Password` | Optional.The password of the new user.  
`Phone` | Optional.The phone number of the user.The action updates the `custom` phone number type.  
`Gender` | Optional.The gender of the user.The valid values are as follows: `female`, `male`, `other`, `unknown`.  
`Department` | Optional.The name of the user's department.  
`Organization` | Optional.The name of the user's organization.  
`Change Password At Next Login` | Optional.If selected, the system requires the user to change their password on the next login attempt.Not selected by default.  
`User Status` | Optional.The user status to update.By default, the action doesn't change the user status.The possible values are as follows:

  * `Not Changed`
  * `Blocked`
  * `Unblocked`

  
  
#### Action outputs

The **Update User** action provides the following outputs:

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

The **Update User** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated the following users in Google Workspace: EMAIL_ADDRESSES.` `Action wasn't able to update the following users in Google Workspace: EMAIL_ADDRESSES` `None of the provided users were updated.` | The action succeeded.  
`Error executing action "Update User". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Update User** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
