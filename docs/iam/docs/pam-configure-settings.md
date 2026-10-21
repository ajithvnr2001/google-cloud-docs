---
url: https://docs.cloud.google.com/iam/docs/pam-configure-settings/
title: Configure Privileged Access Manager settings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:11.257180+00:00
---

# Configure Privileged Access Manager settings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-configure-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Privileged Access Manager settings Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As a Privileged Access Manager settings administrator, you can configure some additional settings for the approval workflow and notification preferences. 

The settings that you configure at the organization or folder level are automatically applied to their child resources, unless you explicitly override the settings at the child resource level.

You can enable automated approvals to allow service accounts and agent identities to be designated as eligible approvers. The automated approvals setting impacts how automation and programmatic access can be integrated into the approval workflows for privileged access.

The automated approvals setting lets administrators add service accounts, agent identities, and [identities in workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation) as approvers when creating or modifying an entitlement.

You can customize resource-wide notification preferences for various Privileged Access Manager events by selectively disabling notifications for specific events and specific personas, or disabling all notifications.

## Before you begin

To get the permissions that you need to configure Privileged Access Manager settings, ask your administrator to grant you the following IAM roles: 

  * Configure settings for your project, folder, or organization: [PAM Settings Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsAdmin) (`roles/privilegedaccessmanager.settingsAdmin`) on your organization 
  * View settings for your project, folder, or organization: [PAM Settings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsViewer) (`roles/privilegedaccessmanager.settingsViewer`) on your project, folder, or organization 



These predefined roles contain the permissions required to configure Privileged Access Manager settings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure Privileged Access Manager settings:

  * Configure settings: `privilegedaccessmanager.settings.update`
  * View settings: 
    * `privilegedaccessmanager.settings.get`
    * `privilegedaccessmanager.settings.fetchEffective`



## Automated approvals

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project.

  3. Click the **Settings** tab. In the **Settings source** section, **Inherit from parent** is selected by default.

  4. To override settings inherited from the parent resource on a child resource, in the **Automated approvals** section, select **Override inheritance**.

  5. To enable automated approvals, turn on the **Enable Agent Identity and Service Account as Approvers** toggle and click **Save**.

**Note:** If you disable the automated approvals setting, grants that require approvals from service accounts or agent identities won't get approved. If your entitlements have only service accounts or agent identities as approvers, then those entitlements won't be effective.



### gcloud

The `gcloud alpha pam settings update` command configures additional Privileged Access Manager. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: Optional. The resource type that you want to update the settings for. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `SA_AS_APPROVER`: A boolean value in the `serviceAccountApproverSettings` field that indicates whether service accounts and agent identities are allowed to approve grants. The default value is `false`. 
    * If you specify the `serviceAccountApproverSettings` field with a value, then that setting is applied to your resource.
    * If you specify the `serviceAccountApproverSettings` field but leave it empty, then the default settings are applied to your resource.
    * If you don't specify the `serviceAccountApproverSettings` field at all, then your resource inherits the settings from the parent resource.

If you disable this setting, the grants that require approvals from service accounts or agent identities won't get approved. If your entitlements have only service accounts or agent identities as approvers, those entitlements aren't effective.

  * `request.json`: A file containing the modified settings. To create this file, [get](https://docs.cloud.google.com/iam/docs/pam-view-export-settings#export-settings) the existing settings, save the response in file named `request.json`, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the settings. 



Save the following content in a file called `filename.yaml`: 
    
    
    emailNotificationSettings:
      customNotificationBehavior:
        adminNotifications:
          grantActivated: NOTIFICATION_MODE_1
          grantActivationFailed: DISABLED
          grantEnded: ENABLED
          grantExternallyModified: ENABLED
        approverNotifications:
          pendingApproval: NOTIFICATION_MODE_2
        requesterNotifications:
          entitlementAssigned: ENABLED
          grantActivated: ENABLED
          grantExpired: NOTIFICATION_MODE_3
          grantRevoked: ENABLED
    etag:'"ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md"'
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/settings
    serviceAccountApproverSettings:
      enabled: SA_AS_APPROVER

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam settings update \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID \
        --settings-file FILENAME.yaml

#### Windows (PowerShell)
    
    
    gcloud alpha pam settings update `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID `
        --settings-file FILENAME.yaml

#### Windows (cmd.exe)
    
    
    gcloud alpha pam settings update ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --settings-file FILENAME.yaml

You should receive a response similar to the following:
    
    
    Parsed [location] resource: RESOURCE_TYPE/RESOURCE_ID/locations/global
    Request issued for: [global]
    Updated location [global].
    createTime: '2025-05-18T10:10:10.101010101Z'
    emailNotificationSettings:
      customNotificationBehavior:
        adminNotifications:
          grantActivated: ENABLED
          grantActivationFailed: DISABLED
          grantEnded: ENABLED
          grantExternallyModified: ENABLED
        approverNotifications:
          pendingApproval: ENABLED
        requesterNotifications:
          entitlementAssigned: ENABLED
          grantActivated: ENABLED
          grantExpired: ENABLED
          grantRevoked: ENABLED
    etag: "ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md1"
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/settings
    serviceAccountApproverSettings:
      enabled: true
    updateTime: '2025-05-18T10:10:40.101010101Z'
    

### REST

The Privileged Access Manager API's `updateSettings` method configures additional Privileged Access Manager. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that you want to update the settings for, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `UPDATED_FIELDS`: A comma-separated list of fields that need to be updated in the settings. For example, `emailNotificationSettings,serviceAccountApproverSettings`. 

To update all fields that can be modified, set the update mask to `*`.

  * `SA_AS_APPROVER`: A boolean value in the `serviceAccountApproverSettings` field that indicates whether service accounts and agent identities are allowed to approve grants. The default value is `false`. 
    * If you specify the `serviceAccountApproverSettings` field with a value, then that setting is applied to your resource.
    * If you specify the `serviceAccountApproverSettings` field but leave it empty, then the default settings are applied to your resource.
    * If you don't specify the `serviceAccountApproverSettings` field at all, then your resource inherits the settings from the parent resource.

If you disable this setting, the grants that require approvals from service accounts or agent identities won't be approved. If your entitlements have only service accounts or agent identities as approvers, those entitlements aren't effective.

  * `request.json`: A file containing the modified settings. To create this file, [get](https://docs.cloud.google.com/iam/docs/pam-view-export-settings#export-settings) the existing settings, save the response in file named `request.json`, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the settings. 



HTTP method and URL: 
    
    
    PATCH https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS

Request JSON body: 
    
    
    {
      "emailNotificationSettings": {
        "customNotificationBehavior": {
          "adminNotifications": {
            "grantActivated": "NOTIFICATION_MODE_1",
            "grantActivationFailed": "DISABLED",
            "grantEnded": "ENABLED",
            "grantExternallyModified": "ENABLED"
          },
          "approverNotifications": {
            "pendingApproval": "NOTIFICATION_MODE_2"
          },
          "requesterNotifications": {
            "entitlementAssigned": "ENABLED",
            "grantActivated": "ENABLED",
            "grantExpired": "NOTIFICATION_MODE_3",
            "grantRevoked": "ENABLED"
          }
        }
      },
      "etag": "\"ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md\"",
      "name": "SCOPE/locations/global/settings",
      "serviceAccountApproverSettings": {
        "enabled": SA_AS_APPROVER
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "SCOPE/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-25T01:55:02.544562950Z",
        "target": "SCOPE/locations/global/settings",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    
    
    

To check on the progress of an update operation, you can send a `GET` request to the following endpoint:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations

### Terraform

You can use [Terraform](https://www.terraform.io/) to configure Privileged Access Manager settings. For more information, see [google_privileged_access_manager_settings](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/privileged_access_manager_settings) in the Terraform documentation.

## Customize notification preferences

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project.

  3. Click the **Settings** tab.

  4. In the **Notifications** section, **Inherit from parent** is selected by default.

The following table shows the default notification preferences:

Event | Admin | Requester | Approver  
---|---|---|---  
Entitlement assigned | - | ✓ | -  
Grant requires approval | - | - | ✓  
Grants are activated | ✓ | ✓ | -  
Grants are denied | - | ✓ | -  
Grants are expired | - | ✓ | -  
Grants have ended | ✓ | ✓ | -  
Grants are revoked | - | ✓ | -  
Grants are externally modified | ✓ | ✓ | -  
Grants activation failed | ✓ | ✓ | -  
  5. To override settings inheritance from the parent, turn on the **Send notifications for the following events** toggle.

  6. To disable notifications for the required PAM event and persona, clear the corresponding checkboxes, and click **Save**.

  7. To disable all the notifications, clear **Send notifications for the following events** , and click **Save**.




### gcloud

The `gcloud alpha pam settings update` command configures additional Privileged Access Manager. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: Optional. The resource type that you want to update the settings for. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `NOTIFICATION_MODE`: In the `emailNotificationSettings` field, use `ENABLED` to send notification emails for the event, or `DISABLED` to prevent them. 
    * If you specify the `emailNotificationSettings` field with a value, then that setting is applied to your resource.
    * If you specify the `emailNotificationSettings` field but leave it empty, then the default settings are applied to your resource.
    * If you don't specify the `emailNotificationSettings` field at all, then your resource inherits the settings from the parent resource.
  * `request.json`: A file containing the modified settings. To create this file, [get](https://docs.cloud.google.com/iam/docs/pam-view-export-settings#export-settings) the existing settings, save the response in file named `request.json`, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the settings. 



Save the following content in a file called `filename.yaml`: 
    
    
    emailNotificationSettings:
      customNotificationBehavior:
        adminNotifications:
          grantActivated: NOTIFICATION_MODE_1
          grantActivationFailed: DISABLED
          grantEnded: ENABLED
          grantExternallyModified: ENABLED
        approverNotifications:
          pendingApproval: NOTIFICATION_MODE_2
        requesterNotifications:
          entitlementAssigned: ENABLED
          grantActivated: ENABLED
          grantExpired: NOTIFICATION_MODE_3
          grantRevoked: ENABLED
    etag:'"ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md"'
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/settings
    serviceAccountApproverSettings:
      enabled: SA_AS_APPROVER

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam settings update \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID \
        --settings-file FILENAME.yaml

#### Windows (PowerShell)
    
    
    gcloud alpha pam settings update `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID `
        --settings-file FILENAME.yaml

#### Windows (cmd.exe)
    
    
    gcloud alpha pam settings update ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --settings-file FILENAME.yaml

You should receive a response similar to the following:
    
    
    Parsed [location] resource: RESOURCE_TYPE/RESOURCE_ID/locations/global
    Request issued for: [global]
    Updated location [global].
    createTime: '2025-05-18T10:10:10.101010101Z'
    emailNotificationSettings:
      customNotificationBehavior:
        adminNotifications:
          grantActivated: ENABLED
          grantActivationFailed: DISABLED
          grantEnded: ENABLED
          grantExternallyModified: ENABLED
        approverNotifications:
          pendingApproval: ENABLED
        requesterNotifications:
          entitlementAssigned: ENABLED
          grantActivated: ENABLED
          grantExpired: ENABLED
          grantRevoked: ENABLED
    etag: "ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md1"
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/settings
    serviceAccountApproverSettings:
      enabled: true
    updateTime: '2025-05-18T10:10:40.101010101Z'
    

### REST

The Privileged Access Manager API's `updateSettings` method configures additional Privileged Access Manager. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that you want to update the settings for, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `UPDATED_FIELDS`: A comma-separated list of fields that need to be updated in the settings. For example, `emailNotificationSettings,serviceAccountApproverSettings`. 

To update all fields that can be modified, set the update mask to `*`.

  * `NOTIFICATION_MODE`: In the `emailNotificationSettings` field, use `ENABLED` to send notification emails for the event or `DISABLED` to prevent them. 
    * If you specify the `emailNotificationSettings` field with a value, then that setting is applied to your resource.
    * If you specify the `emailNotificationSettings` field but leave it empty, then the default settings are applied to your resource.
    * If you don't specify the `emailNotificationSettings` field at all, then your resource inherits the settings from the parent resource.
  * `request.json`: A file containing the modified settings. To create this file, [get](https://docs.cloud.google.com/iam/docs/pam-view-export-settings#export-settings) the existing settings, save the response in file named `request.json`, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the settings. 



HTTP method and URL: 
    
    
    PATCH https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS

Request JSON body: 
    
    
    {
      "emailNotificationSettings": {
        "customNotificationBehavior": {
          "adminNotifications": {
            "grantActivated": "NOTIFICATION_MODE_1",
            "grantActivationFailed": "DISABLED",
            "grantEnded": "ENABLED",
            "grantExternallyModified": "ENABLED"
          },
          "approverNotifications": {
            "pendingApproval": "NOTIFICATION_MODE_2"
          },
          "requesterNotifications": {
            "entitlementAssigned": "ENABLED",
            "grantActivated": "ENABLED",
            "grantExpired": "NOTIFICATION_MODE_3",
            "grantRevoked": "ENABLED"
          }
        }
      },
      "etag": "\"ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md\"",
      "name": "SCOPE/locations/global/settings",
      "serviceAccountApproverSettings": {
        "enabled": SA_AS_APPROVER
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings?updateMask=UPDATED_FIELDS" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "SCOPE/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-25T01:55:02.544562950Z",
        "target": "SCOPE/locations/global/settings",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    
    
    

To check on the progress of an update operation, you can send a `GET` request to the following endpoint:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations

### Terraform

You can use [Terraform](https://www.terraform.io/) to configure Privileged Access Manager settings. For more information, see [google_privileged_access_manager_settings](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/privileged_access_manager_settings) in the Terraform documentation.

## What's next

  * [View and export Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
