---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-iam/
title: Integrate IAM with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:53.494936+00:00
---

# Integrate IAM with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate IAM with Google SecOps

This document explains how to integrate Identity and Access Management with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for IAM is called _Google Cloud IAM_.

## Use cases

The **IAM** integration supports the following use cases:

  * **Automated service account lifecycle management** : Automatically create, enable, or disable service accounts during onboarding and offboarding processes to ensure access is granted only when necessary.

  * **Rapid identity incident response** : Immediately delete or disable compromised service accounts and roles during a security incident to prevent unauthorized access to cloud resources.

  * **Identity governance and enrichment** : Enrich User entities in Google SecOps with detailed service account metadata, such as display names and project IDs, to provide analysts with immediate context during investigations.

  * **Policy auditing and enforcement** : Retrieve and audit access control policies to ensure they align with the principle of least privilege, and programmatically set new policies to remediate unauthorized changes.

  * **Role-based access control (RBAC) management** : Create and manage custom IAM roles with specific permission sets across your organization to maintain granular control over cloud environment access.




## Before you begin

Before you configure the **IAM** integration in Google SecOps, complete the following prerequisite steps:

  1. Create a custom IAM role: Define a role with the specific permissions required to manage service accounts and roles.

  2. Create a service account: Create the identity that the integration uses to perform actions.

  3. Select an authentication method: Choose between the recommended Workload Identity or a service account JSON key.




### Create and configure a custom IAM role

To maintain the principle of least privilege, complete the following steps to create a custom role containing only the specific permissions necessary for this integration:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **add Create custom role**.

  3. Provide a **Title** , **Description** , and **ID**.

  4. Set the **Role launch stage** to `General Availability`.

  5. Click **Add Permissions** and add the following specific permissions:

     * `iam.serviceAccounts.list`
     * `iam.serviceAccounts.create`
     * `iam.serviceAccounts.get`
     * `iam.serviceAccounts.getIamPolicy`
     * `iam.serviceAccounts.setIamPolicy`
     * `iam.serviceAccounts.disable`
     * `iam.serviceAccounts.enable`
     * `iam.serviceAccounts.delete`
     * `iam.roles.list`
     * `iam.roles.get`
     * `iam.roles.create`
     * `iam.roles.delete`
  6. Click **Create**.




### Create a service account

The integration uses a service account to authenticate and execute IAM actions within your project.

To create a service account, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create Service Account**.

  3. Enter a name and description, then click **Create and Continue**.

  4. In the **Grant this service account access to project** section, assign the custom role you created in the previous step to this service account. Click **Done**. 




### Select and configure an authentication method

Google SecOps supports two authentication paths for this integration:

  * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens using service account impersonation. It is more secure as it eliminates the need for long-lived JSON keys.

  * **Option 2:Service account JSON key**: This method uses a static key file. Use this only if a Workload Identity is not available in your environment.




#### Authenticate using a Workload Identity (recommended)

To use a Workload Identity, you must authorize your Google SecOps instance to impersonate the service account you created.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **IAM** integration.

  3. Enter your service account email in the **Workload Identity Email** field.

  4. Click **Save** and then click **Test**. The test is expected to fail initially.

  5. Click close_small next to the failed test to view the error message.

  6. Search for the unique email address (formatted as `gke-init-python@...` or `soar-python@...`) found near the end of the error message. Copy this address.




##### Grant impersonation permissions

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the service account you created for this integration.

  3. Go to the **Permissions** tab and click **Grant Access**.

  4. Paste the unique email address you copied into the **New principals** field.

  5. Assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`). Click **Save**.




#### Authenticate using a JSON key

If using a Workload Identity isn't available in your environment, you can authenticate the integration using a service account JSON key. This method relies on a static, long-lived secret file to establish the connection between the platform and your Google Cloud resources.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add Key > Create new key**.

  4. Select `JSON` as the key type and click **Create**. The file downloads to your computer.

  5. Copy the entire content of the JSON file.

  6. When you configure this integration in the platform, paste the content into the **Service Account Json File Content** field.




## Integration parameters

The **IAM** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Optional. The base URL of the IAM instance. The default value is `https://iam.googleapis.com`.  
`Account Type` | Optional. The type of the Google Cloud account. This value corresponds to the `type` parameter in the authentication JSON file. The default value is `service_account`.  
`Project ID` | Optional. The project ID of the Google Cloud account. This value corresponds to the `project_id` parameter in the authentication JSON file.  
`Quota Project ID` | Optional. The project ID used for quota and billing purposes when making API requests.  
`Private Key ID` | Optional. The private key ID of the Google Cloud account. This value corresponds to the `private_key_id` parameter in the authentication JSON file.  
`Private Key` | Optional. The private key of the Google Cloud account. This value corresponds to the `private_key` parameter in the authentication JSON file.  
`Client Email` | Optional. The client email of the Google Cloud account. This value corresponds to the `client_email` parameter in the authentication JSON file.  
`Client ID` | Optional. The client ID of the Google Cloud account. This value corresponds to the `client_id` parameter in the authentication JSON file.  
`Auth URI` | Optional. The authentication URI for the Google Cloud account. This value corresponds to the `auth_uri` parameter in the authentication JSON file. The default value is `https://accounts.google.com/o/oauth2/auth`.  
`Token URI` | Optional. The token URI for the Google Cloud account. This value corresponds to the `token_uri` parameter in the authentication JSON file. The default value is `https://oauth2.googleapis.com/token`.  
`Auth Provider X509 URL` | Optional. The auth provider X.509 certificate URL. This value corresponds to the `auth_provider_x509_cert_url` parameter in the authentication JSON file. The default value is `https://www.googleapis.com/oauth2/v1/certs`.  
`Client X509 URL` | Optional. The client X.509 certificate URL. This value corresponds to the `client_x509_cert_url` parameter in the authentication JSON file.  
`Organization ID` | Optional. The unique identifier for your Google Cloud organization.  
`Service Account Json File Content` | Optional. The full JSON content of the service account key file. If this parameter is provided, individual connection parameters (such as `Private Key ID` and `Private Key`) are ignored.  
`Workload Identity Email` | Optional. The email address associated with the Workload Identity service account.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the IAM server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Create Role

Create an Identity and Access Management role.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Role ID | String | N/A | Yes | Specify role id for newly created Identity and Access Management role.  
Role Definition | String | N/A | Yes | Specify JSON policy document to use as the role definition.  
  
#### Run On

The action doesn't run on entities.

#### Example For Role Policy JSON
    
    
    {
       "name": "projects/silver-shift-275007/roles/iam_test_role_api",
       "title": "iam_test_role_api",
       "description": "test role",
       "includedPermissions": [
           "storagetransfer.projects.getServiceAccount"
       ],
       "stage": "GA",
       "etag": "BwXBu1RHiPw="
    }
    

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "name": "projects/[PROJECT_ID]/roles/[ROLE_NAME]",
       "title": "[ROLE_TITLE]",
       "description": "[ROLE_DESCRIPTION]",
       "includedPermissions": [
           "storagetransfer.projects.getServiceAccount"
       ],
       "stage": "GA",
       "etag": "[ETAG_VALUE]"
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Identity and Access Management <roleid> was created successfully.
  * **If provided role_id already exists(is_success =false)**
    * Provided role id<role_id> already exists.
  * **If provided role JSON is not valid (is_success =false)**
    * Provided role definition JSON document <role json> is not valid.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Role". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Create Service Account

Create an Identity and Access Management Service Account.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Service Account ID | String | String | Yes | Specify service account id to create.  
Service Account Display Name | String | String | No | Specify service account display name to create.  
Service Account Description | String | String | No | Specify service account description to create.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "name": "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
       "projectId": "PROJECT_ID",
       "uniqueId": "UNIQUE_ID",
       "email": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
       "displayName": "SERVICE_ACCOUNT_DISPLAY_NAME",
       "etag": "ETAG_VALUE",
       "description": "SERVICE_ACCOUNT_DESCRIPTION",
       "oauth2ClientId": "UNIQUE_ID"
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Google Cloud Service Account was created successfully <unique id>.
  * **If action failed to run because provided service account already exists(is_success =false)**
    * Provided service account <unique id> already exists.

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Service Account". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Delete Role

Delete an Identity and Access Management Role.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Role ID | String | N/A | Yes | Specify role id for newly created Identity and Access Management role.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "name": "projects/[PROJECT_ID]/roles/[ROLE_NAME]",
       "title": "[ROLE_TITLE]",
       "description": "[ROLE_DESCRIPTION]",
       "includedPermissions": [
           "storagetransfer.projects.getServiceAccount"
       ],
       "stage": "GA",
       "etag": "[ETAG_VALUE]",
       "deleted": true
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Identity and Access Management <roleid> was successfully deleted.
****
  * **If provided role_id not exists(is_success =false)**
    * Provided role id<role_id> does not exist.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Role". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Delete Service Account

Delete service account. Action expects Identity and Access Management service account email as a Google SecOps User entity.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **if successful at least one of the provided entities:** "Successfully deleted the following service accounts: {0}".format([entity.Identifier]).



  * **If fail to delete all of the provided entities:** "No service accounts were deleted."



  * **If fail to find data in Identity and Access Management to delete specific entities:** "Action was not able to find a match in Identity and Access Management for the provided entities: {0}".format([entity.identifier])

******The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Service Account". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Disable Service Account

Disable service account. Action expects Identity and Access Management service account email as a Google SecOps User entity.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **if successful at least one of the provided entities:** "Successfully disabled the following service accounts: {0}".format([entity.Identifier]).

****

  * **If fail to disable all of the provided entities:** "No service accounts were disabled."

****

  * **If fail to find data in Google Cloud IAM to disable specific entities:** "Action was not able to find a match in Google Cloud IAM for the provided entities: {0}".format([entity.identifier])

******The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Disable Service Account". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Enable Service Account

Enable service account. Action expects Identity and Access Management service account email as a Google SecOps User entity.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **if successful at least one of the provided entities:** "Successfully enabled the following service accounts: {0}".format([entity.Identifier]).



  * **If fail to enable all of the provided entities:** "No service accounts were enabled."

****

  * **If fail to find data in Identity and Access Management to enable specific entities:** "Action was not able to find a match in Identity and Access Management for the provided entities: {0}".format([entity.identifier])

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Enable Service Account". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### Enrich Entities

Enrich Google SecOps User entities with service accounts information from Identity and Access Management. Action expects Identity and Access Management service account email as a Google SecOps User entity.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
      "name": "projects/[PROJECT_ID]/serviceAccounts/[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com",
      "projectId": "[PROJECT_ID]",
      "uniqueId": "[UNIQUE_ID]",
      "email": "[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com",
      "displayName": "[DISPLAY_NAME]",
      "etag": "[ETAG]",
      "description": "[DESCRIPTION]",
      "oauth2ClientId": "[UNIQUE_ID]"
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Google_IAM_name |   
Google_IAM_project_id | ..  
Google_IAM_unique_id |   
Google_IAM_email |   
Google_IAM_display_name |   
Google_IAM_description |   
Google_IAM_oauth2_client_id |   
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **if successful and at least one of the provided entities were enriched:** "Successfully enriched entities: {0}".format([entity.Identifier]).
  * **If fail to enrich all of the provided entities:** "No entities were enriched."
  * **If fail to find data in Identity and Access Management to enrich specific entities:** "Action was not able to find a match in Identity and Access Management to enrich provided entities: {0}".format([entity.identifier])  
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | **General**  
**Table (Enrichment)** | **Table Name:** {entity} Enrichment Table**Columns:** Key, Value | **Entity**  
  
### Get Service Account IAM Policy

Gets the access control policy for the service account. Action expects Identity and Access Management service account email as a Google SecOps User entity. Note that policy may be empty if no policy is assigned to the service account.

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "version": 1,
       "etag": "[ETAG_VALUE]",
       "bindings": [
           {
               "role": "roles/iam.securityReviewer",
               "members": [
                   "user:[USER_EMAIL]"
               ]
           }
       ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * "Successfully fetched Identity and Access Management policy for the following Google Cloud Service Accounts: <email id1, email id 2...>
  * **If action didnt find info for the entity (for example non existent in Google Identity and Access Management email provided:**
    * Action was not able to fetch Identity and Access Management policy the following Google Cloud Service Accounts: <email id1, email id2 ..>
  * **If fail to find Identity and Access Management policy for all of the provided entities:** "Identity and Access Management policy was not found for any of the provided entities."

******The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Get Service Account IAM Policy". Reason: {0}''.format(error.Stacktrace) | **General**  
  
### List Roles

List Identity and Access Management roles based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
View | DDL | Basic | No | Specify which view should be used to return role information.  
Max Rows to Return | Integer | 50 | No | Specify how many roles action should return.  
List Project Custom Roles Only? | Checkbox | Unchecked | No | If enabled action will return only custom roles defined for the current project id.  
Show Deleted | Checkbox | Unchecked | No | If enabled action will also return deleted roles.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "roles": [
           {
               "name": "roles/accessapproval.approver",
               "title": "Access Approval Approver",
               "description": "Ability to view or act on access approval requests and view configuration",
               "stage": "BETA",
               "etag": "[ETAG_VALUE]"
           },
           {
               "name": "roles/accessapproval.configEditor",
               "title": "Access Approval Config Editor",
               "description": "Ability update the Access Approval configuration",
               "stage": "BETA",
               "etag": "[ETAG_VALUE]"
           }
       ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If successfully listed roles(is_success = true):** "Successfully fetched Identity and Access Management roles."

****

  * **If no available values(is_success = false):** "No roles were returned for the specified input parameters."

******The action should fail and stop a playbook execution:****if fatal error, invalid zone, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "List Roles". Reason: {0}''.format(error.Stacktrace) | **General**  
**Table** | **Table Name:** IAM Roles**Table Columns:** Role NameRole TitleRole DescriptionRole StageRole EtagRole Permissions | **General**  
  
### List Service Accounts

List Identity and Access Management service accounts based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Service Account Display Name | String | N/A | No | Specify service account display name to return. Parameter accepts multiple values as a comma separated string.  
Service Account Email | String | N/A | No | Specify service account email to return. Parameter accepts multiple values as a comma separated string.  
Max Rows to Return | Integer | 50 | No | Specify how many roles action should return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
      "accounts": [
        {
          "name": "projects/[PROJECT_ID]/serviceAccounts/[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com",
          "projectId": "[PROJECT_ID]",
          "uniqueId": "[UNIQUE_ID]",
          "email": "[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com",
          "displayName": "[DISPLAY_NAME]",
          "etag": "[ETAG_VALUE]",
          "description": "[SERVICE_ACCOUNT_DESCRIPTION]",
          "oauth2ClientId": "[UNIQUE_ID]"
        }
      ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If successfully listed service accounts (is_success = true):**  
****"Successfully fetched Google Cloud service accounts."
  * **If no available values(is_success = false):** "No service accounts were returned for the specified input parameters."  
****

**The action should fail and stop a playbook execution:****if fatal error, invalid zone, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "List Service Accounts". Reason: {0}''.format(error.Stacktrace) | **General**  
**Table** | **Table Name:** Google Cloud Service Accounts**Table Columns:** Service Account NameService Account Unique IDService Account EmailService Account Display NameService Account DescriptionService Account Oauth2 Client ID | **General**  
  
### Ping

Test connectivity to the Identity and Access Management service with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** "Successfully connected to the Identity and Access Management service with the provided connection parameters!"

******The action should fail and stop a playbook execution:**

  * **if critical error, like wrong credentials or lost connectivity:** "Failed to connect to the Identity and Access Management service! Error is {0}".format(exception.stacktrace)

| General  
  
### Rotate Service Account Keys

Use the **Rotate Service Account Keys** action to rotate user-managed keys associated with a service account. During rotation, all existing keys are deleted and a new key is created.

This action runs on the following Google SecOps entities:

  * `Deployment`

  * `Username`

**Note:** The supported formats for these entities are the IAM service account email and the resource name.



#### Action inputs

The **Rotate Service Account Keys** action requires the following parameters:

Parameter | Description  
---|---  
`Service Account` | Optional. A comma-separated list of service accounts for which to rotate keys. This parameter works alongside entities. If provided, the action rotates keys for these specific accounts in addition to any service account entities identified in the action scope.  
  
#### Action outputs

The **Rotate Service Account Keys** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Rotate Service Account Keys** action:
    
    
    [
        {
           "Entity": "123",
           "EntityResult": {
                   "name": "projects/example-project/serviceAccounts/sample-sa@example-project.iam.gserviceaccount.com/keys/b333bbda7826af991a4d4cc4e3f83325103580ca",
                   "validAfterTime": "2023-09-12T11:02:31Z",
                   "validBeforeTime": "9999-12-31T23:59:59Z",
                   "keyAlgorithm": "KEY_ALG_RSA_2048",
                   "keyOrigin": "GOOGLE_PROVIDED",
                   "keyType": "USER_MANAGED"
            }
        },
        {
           "Entity": "1234",
           "EntityResult": {
                   "name": "projects/example-project/serviceAccounts/sample-sa@example-project.iam.gserviceaccount.com/keys/b333bbda7826af991a4d4cc4e3f83325103580ca",
                   "validAfterTime": "2023-09-12T11:02:31Z",
                   "validBeforeTime": "9999-12-31T23:59:59Z",
                   "keyAlgorithm": "KEY_ALG_RSA_2048",
                   "keyOrigin": "GOOGLE_PROVIDED",
                   "keyType": "USER_MANAGED"
            }
        }
    ]
    

##### Output messages

The **Rotate Service Account Keys** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully rotated keys for service account SERVICE_ACCOUNT_EMAIL in IAM.` `The following service accounts were not found in IAM: SERVICE_ACCOUNT_KEYS.` `None of the provided service accounts were found in IAM.` | The action succeeded.  
`Error executing action "Rotate Service Account Keys". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Rotate Service Account Keys** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Service Account IAM Policy

Sets the access control policy on the specified service account. Action expects Identity and Access Management service account email as a Google SecOps account entity. Note that policy provided in action replaces any existing policy.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Policy | String | N/A | Yes | Specify JSON policy document to set for service account.  
  
#### Run On

This action runs on the Account entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "version": 1,
       "etag": "[ETAG_VALUE]",
       "bindings": [
           {
               "role": "roles/iam.securityReviewer",
               "members": [
                   "user:[USER_EMAIL]"
               ]
           }
       ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:**

  * **If some are successful (is_success=True):**
    * Successfully set Identity and Access Management policy for the following Google Cloud Service Accounts: <email id1, ...>
  * **If some failed:**
    * Action was not able to set Identity and Access Management policy the following Google Cloud Service Accounts: <email id1, ....>
****
  * **If all failed:**
    * No Service Account Identity and Access Management policies were set.
****
  * **If provided policy JSON is not valid (is_success =false)**
    * Provided policy JSON document <policy> is not valid.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Set Service Account IAM Policy". Reason: {0}''.format(error.Stacktrace) | **General**  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
