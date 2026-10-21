---
url: https://docs.cloud.google.com/firewall/docs/configure-security-profiles/
title: Create and manage threat prevention security profiles \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:27.533861+00:00
---

# Create and manage threat prevention security profiles  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create and manage threat prevention security profiles Stay organized with collections  Save and categorize content based on your preferences. 

To protect your Google Cloud resources from threats, you define and enforce threat prevention security profiles. This document describes how to create, view, list, modify, and delete these profiles by using the Google Cloud console or the Google Cloud CLI.

This document is intended for network administrators and security engineers who configure network security and threat prevention policies.

Google Cloud supports threat prevention security profiles at two levels:

  * **Organization-level security profiles** : Enable centralized threat prevention rules that can be applied across multiple projects in your organization.
  * **Project-level security profiles** : Enable project-specific threat prevention rules tailored to the workloads within a single project.



For more information, see the [Security profiles overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles).

**Note:** To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions: 

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.



### Roles

To get the permissions that you need to create, view, update, or delete security profiles, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-security-profiles#iam-roles) on your organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a threat prevention security profile

Create a security profile of type `threat-prevention` and specify the name of the security profile as a string or as a unique URL identifier.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization or project where you want to create the security profile.

  3. Select the **Security profiles** tab.

  4. Click **Create profile**.

  5. Enter a name in the **Name** field. Don't include sensitive information such as personally identifiable information or security data in the security profile name.

  6. Optional: Enter a description in the **Description** field.

  7. To create a Cloud Next Generation Firewall Enterprise security profile, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. To create a threat prevention security profile, in the **Type** section, select **Threat prevention**.

  9. Click **Continue**.




Optionally, add severity and threat overrides:

  1. Under **Severity overrides** , click **Edit** next to the severity level that you want to override.
  2. In the **Override action** list, select the appropriate action for the severity level.
  3. To add a threat signature override, click **Add signature by ID**.
  4. In the **Signature ID** field, enter the threat ID that you want to override. You can view the threat IDs on the [threat dashboard](https://docs.cloud.google.com/firewall/docs/view-threats).
  5. In the **Override action** list, select the appropriate action for the threat ID.
  6. Click **Create**.



###  gcloud 

To create a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create):
    
    
    gcloud network-security security-profiles threat-prevention create NAME \
      [--organization ORGANIZATION_ID | --project PROJECT_ID] \
      [--billing-project QUOTA_PROJECT_ID] \
      --description DESCRIPTION \
      --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

Don't include sensitive information such as personally identifiable information or security data in the security profile name.
  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `DESCRIPTION`: an optional description for the threat prevention security profile.


**Note:** To add severity or threat overrides by using Google Cloud CLI, see Add override actions in a threat prevention security profile.

## List and view details of a security profile

You can list all threat prevention security profiles created in an organization or a project. You can also view the details of a security profile, such as its profile type, purpose, and description.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.list` to list security profiles
  * `networksecurity.securityProfiles.describe` to view the details of a security profile



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. To filter for threat prevention security profiles, in the **Filter** field, specify **Profile type** as **Threat prevention**.

The tab shows a list of Threat prevention security profiles.

  5. Click a security profile of type **Threat prevention** to view its details.




###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your project.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Click a security profile of type **Threat prevention** to view the profile details.




###  gcloud 

To list all threat prevention security profiles, use the [`gcloud network-security security-profiles threat-prevention list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/list):
    
    
    gcloud network-security security-profiles threat-prevention list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

To view the details of a threat prevention security profile, use the [`gcloud network-security security-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/describe):
    
    
    gcloud network-security security-profiles describe NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID where the security profile exists. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID where the security profile exists. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.




## Delete a threat prevention security profile

You can delete a threat prevention security profile by specifying its name, location, and organization or project. However, if a security profile is referenced by a security profile group, that security profile cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  3. Select the threat prevention security profile that you want to delete, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/delete):
    
    
    gcloud network-security security-profiles threat-prevention delete NAME \
      --organization ORGANIZATION_ID | --project PROJECT_ID \
      [--billing-project QUOTA_PROJECT_ID] \
      --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.




## Import a threat prevention security profile

You can import a threat prevention security profile (either custom-created or previously exported) from a YAML file. When importing a threat prevention security profile, if a profile with the same name already exists, Cloud NGFW updates the existing profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.update` (required only if a profile with the same name already exists)



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  gcloud 

To import a threat prevention security profile from a YAML file, use the [`gcloud network-security security-profiles import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/import):
    
    
    gcloud network-security security-profiles import NAME \
      --organization ORGANIZATION_ID | --project PROJECT_ID \
      [--billing-project QUOTA_PROJECT_ID] \
      --source FILE_NAME \
      --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `FILE_NAME`: the path to the YAML file containing the configuration export data for the threat prevention security profile. For example, `threat-prevention-sp.yaml`.

The YAML file must not contain any output-only fields. Alternatively, you can omit the `source` flag to read from the standard input.




## Export a threat prevention security profile

You can export a threat prevention security profile to a YAML file. For example, instead of using the user-interface to modify a large security profile, you can use this functionality to export the security profile, modify it quickly, and import it back.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.describe`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  gcloud 

To export a threat prevention security profile to a YAML file, use the [`gcloud beta network-security security-profiles export` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/export):
    
    
    gcloud network-security security-profiles export NAME \
      --organization ORGANIZATION_ID | --project PROJECT_ID \
      [--billing-project QUOTA_PROJECT_ID] \
      --destination FILE_NAME \
      --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `FILE_NAME`: the path to the YAML file into which Cloud NGFW will export the configuration for the threat prevention security profile. For example, `threat-prevention-sp.yaml`.

The exported configuration data doesn't contain any output-only fields. Alternatively, you can omit the `destination` flag to write to the standard output.




## Add override actions in a threat prevention security profile

You can override the actions associated with specific [threat signatures](https://docs.cloud.google.com/firewall/docs/about-threats#default-threat-signatures) or [severity levels](https://docs.cloud.google.com/firewall/docs/about-threats#threat-severity-level) in an existing threat prevention security profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.update`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization or project.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Select the security profile where you want to override actions, and then click **Edit**.

  5. Under **Severity overrides** , click **Edit** next to the severity level that you want to override.

  6. In **Override action** list, select the appropriate action for the severity level.

  7. Click **Confirm**.

  8. Click **Save**.




###  gcloud 

To add an override to a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention add-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override):
    
    
    gcloud network-security security-profiles threat-prevention add-override NAME \
      --location global \
      [--organization ORGANIZATION_ID | --project PROJECT_ID] \
      [--billing-project QUOTA_PROJECT_ID] \
      [--severities SEVERITIES | --threat-ids THREAT_IDS | --antivirus PROTOCOLS] \
      --action ACTION
    

**Note:** You can specify action overrides for the `--severities` flag, the `--threat-ids` flag, or the `--antivirus` flag in a single command. To specify action overrides with two or more override flags, run separate commands.

Replace the following:

  * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `SEVERITIES`: a comma-separated list of severity levels to override the action for. The firewall endpoint applies the configured `--action` flag to all threats of the specified severity levels.

The severity can be any of following:

    * `INFORMATIONAL`
    * `LOW`
    * `MEDIUM`
    * `HIGH`
    * `CRITICAL`
  * `THREAT_IDS`: a comma-separated list of threat signature IDs to override the action for. The firewall endpoint applies the configured `--action` flag to all threats of the specified threat IDs.

  * `PROTOCOLS`: a comma-separated list of network protocols to monitor for the antivirus threat. For more information, see [supported protocols](https://docs.cloud.google.com/firewall/docs/about-threats#supported-protocols).

  * `ACTION`: the action for the specified threat IDs or severities. For more information, see [supported actions](https://docs.cloud.google.com/firewall/docs/about-threats#supported-actions).

**Note:** For specific threat types, not all actions are allowed.



## List override actions in a threat prevention security profile

You can list all the override actions in a threat prevention security profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.list`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select the organization or project.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Select the security profile to view the configured severity override actions and threat signature override actions.




###  gcloud 

To list override actions in a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention list-overrides` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/list-overrides):
    
    
    gcloud network-security security-profiles threat-prevention list-overrides NAME \
      --location global \
      [--organization ORGANIZATION_ID | --project PROJECT_ID]
    

Replace the following:

  * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.




## Update override actions in a threat prevention security profile

You can update existing override actions for severity levels or threat signatures in a threat prevention security profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.update`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select the organization or project.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Select the security profile, and then click **Edit**.

  5. Under **Severity overrides** , click **Edit** next to the severity level where you want to update override action.

  6. In the **Override action** list, select the appropriate action for the severity level.

  7. Click **Confirm**.

  8. Click **Save**.




###  gcloud 

To update an override action in a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention update-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/update-override):
    
    
    gcloud network-security security-profiles threat-prevention update-override NAME \
      --location global \
      [--organization ORGANIZATION_ID | --project PROJECT_ID] \
      [--billing-project QUOTA_PROJECT_ID] \
      [--severities SEVERITIES | --threat-ids THREAT_IDS | --antivirus PROTOCOLS] \
      --action ACTION
    

**Note:** You can specify action overrides for the `--severities` flag, the `--threat-ids` flag, or the `--antivirus` flag in a single command. To specify action overrides with two or more override flags, run separate commands.

Replace the following:

  * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `SEVERITIES`: a comma-separated list of severity levels you want to update overrides for.

The severity can be any of following:

    * `INFORMATIONAL`
    * `LOW`
    * `MEDIUM`
    * `HIGH`
    * `CRITICAL`
  * `THREAT_IDS`: a comma-separated list of threat signature IDs you want to update overrides for.

  * `PROTOCOLS`: a comma-separated list of network protocols to monitor for the antivirus threat.

The following protocols are supported:

    * `SMTP`
    * `SMB`
    * `POP3`
    * `IMAP`
    * `HTTP2`
    * `HTTP`
    * `FTP`
  * `ACTION`: the default action for the specified threat IDs or severities.

The action can be one of the following:

    * `DEFAULT`
    * `ALLOW`
    * `DENY`
    * `ALERT`
**Note:** For specific threat types, not all actions are allowed.



## Delete override actions from a threat prevention security profile

You can delete existing override actions for severity levels or threat signatures from a threat prevention security profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level threat prevention security profiles, and at either the project level or the organization level for project-level threat prevention security profiles 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization or project.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Select the security profile, and then click **Edit**.

  5. Under **Severity overrides** , click **Edit** next to the severity level where you want to delete the override action.

  6. In the **Override action** list, select **Default**.

  7. Click **Confirm**.

  8. Under **Signature overrides** , select the threat ID that you want to delete.

  9. Click **Delete**.

  10. Click **Save**.




###  gcloud 

To delete an override action from a threat prevention security profile, use the [`gcloud network-security security-profiles threat-prevention delete-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/delete-override):
    
    
    gcloud network-security security-profiles threat-prevention delete-override NAME \
      --location global \
      [--organization ORGANIZATION_ID | --project PROJECT_ID] \
      [--billing-project QUOTA_PROJECT_ID] \
      [--severities SEVERITIES | --threat-ids THREAT_IDS | --antivirus PROTOCOLS]
    

**Note:** You can specify action overrides for the `--severities` flag, the `--threat-ids` flag, or the `--antivirus` flag in a single command. To specify action overrides with two or more override flags, run separate commands.

Replace the following:

  * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profiles.

  * `SEVERITIES`: a comma-separated list of severity levels you want to delete overrides for.

The severity can be any of following:

    * `INFORMATIONAL`
    * `LOW`
    * `MEDIUM`
    * `HIGH`
    * `CRITICAL`
  * `THREAT_IDS`: a comma-separated list of threat signature IDs you want to delete overrides for.

  * `PROTOCOLS`: a comma-separated list of network protocols to monitor for the antivirus threat.

The following protocols are supported:

    * `SMTP`
    * `SMB`
    * `POP3`
    * `IMAP`
    * `HTTP2`
    * `HTTP`
    * `FTP`



## What's next

  * [Create security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)
  * [Manage security profile groups](https://docs.cloud.google.com/firewall/docs/manage-security-profile-groups)
  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Manage firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
