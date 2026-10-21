---
url: https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles/
title: Create and manage Advanced malware sandbox security profiles \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:27.741287+00:00
---

# Create and manage Advanced malware sandbox security profiles  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create and manage Advanced malware sandbox security profiles Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to create, view, update, and delete Advanced malware sandbox (WildFire) [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of the `WILDFIRE_ANALYSIS` type by using the Google Cloud console and the Google Cloud CLI.

`WILDFIRE_ANALYSIS` security profiles define file inspection rules, supported file categories, and inline cloud analysis options for advanced malware sandboxing. For more information about how security profiles work within policy groups, see the [Security profile overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles).

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.



### Roles

To get the permissions that you need to create, view, update, or delete security profiles, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-security-profiles#iam-roles) on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To monitor long-running operations triggered by the tasks on this page, you also need the Compute Network User (`roles/compute.networkUser`) role or a custom role containing the following permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Create an Advanced malware sandbox security profile

When you create an Advanced malware sandbox security profile, you can specify the name of the security profile as a string or as a unique URL identifier.

You can construct the unique URL identifier for the security profile in the following formats:

  * **Organization-scoped** :
        
        organizations/ORGANIZATION_ID/locations/global/securityProfiles/SECURITY_PROFILE_NAME
        

  * **Project-scoped** :
        
        projects/PROJECT_ID/locations/global/securityProfiles/SECURITY_PROFILE_NAME
        




When you use a unique URL identifier, it must contain the security profile name, the organization or project, and the location (which is always set to `global`). Using a unique URL identifier lets you reference the security profile in other resources (such as security profile groups) or run `gcloud` commands without specifying the organization, project, or location flags separately.

For more information about unique URL identifiers, see [Security profile specifications](https://docs.cloud.google.com/firewall/docs/about-security-profiles#security-profile-specification).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) at the organization level 



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab.

  4. Click **Create profile**.

  5. Enter a name in the **Name** field.

Don't include sensitive information such as personally identifiable information or security data in the security profile name.

  6. Optional: Enter a description in the **Description** field.

  7. To create a Cloud Next Generation Firewall Enterprise security profile, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. To create a Advanced malware sandbox security profile, in the **Type** section, select **Advanced malware sandbox (WildFire)**.

  9. To prevent the transfer of known malware, select the **Hold on real-time signature look up** checkbox.

  10. Optional: To set the Advanced malware sandbox overrides, do one or both of the following:

     * In the **Signature overrides** section, do the following:

       1. Click **Add signature by ID**.
       2. Enter the signature ID for which you want to override actions.

**Note:** The signature ID must be an integer between 0 and 4,294,967,295 inclusive.
       3. From the **Override action** drop-down list, select one of the following:

          * **Default** : the packet takes the predefined default action specific to that individual threat signature.
          * **Allow** : the packet matching the firewall policy rule allows the connection.
       4. Click **Add signature**.

     * In the **Protocol overrides** section, do the following:

**Note:** By default, the override action for each protocol is set to default.
       1. Click _edit_ **Edit** for the **Protocol** that you want to override. For example, `HTTP`, `SMTP`, or `FTP`.
       2. From the **Action** drop-down list, select the action. For example, `Alert`, `Allow`, or `Deny`.
       3. From the **Inline ML action** drop-down list, select the action. For example, `Alert`, `Allow`, or `Deny`.
       4. Click **Confirm**.
  11. Optional: In the **Submission rules** section, do the following:

     1. Click **Create rule**.
     2. For **File types** , select **Any** or **Specific**.
     3. For **Direction** , do one of the following:

        * **Upload and download** : the firewall monitors traffic in both the upload and download directions for submission rules.
        * **Upload** : the firewall monitors only outgoing traffic (uploads) for files to submit.
        * **Download** : the firewall monitors only incoming traffic (downloads) for files to submit.
     4. Click **Create**.

  12. Optional: In the **Inline cloud analysis rules** section, do the following:

     1. Click **Create rule**.
     2. For **File types** , select **Any** or **PE**.
     3. For **Direction** , do one of the following:

        * **Upload and download** : the firewall monitors traffic in both the upload and download directions for inline cloud analysis.
        * **Download** : the firewall monitors only incoming traffic (downloads) for inline cloud analysis.
     4. From the **Action** drop-down list, select one of the following:

        * **Alert** : the packet is allowed to communicate, but the firewall rule generates a `threat_log` entry sent to the consumer project.
        * **Allow** : the packet matching the firewall policy rule allows the connection.
        * **Deny** : the packet and all subsequent packets belonging to the same connection drop completely. The firewall rule also generates a `threat_log` entry.
     5. Click **Create**.

  13. Optional: In the **Inline ML configuration** section, do the following:

**Note:** By default, the Advanced malware sandbox inline ML configuration action for each file type is set to default.
     1. Click _edit_ **Edit** for the **File type** that you want to configure. For example, `ELF`, `Shell`, or `Macho`.
     2. From the **Action** drop-down list, select the action. For example, `Alert` or `Enable`.
     3. Click **Confirm**.
  14. Optional: In the **Inline ML file exceptions** section, do the following:

     1. Click **Add exception**.
     2. Enter the filename that you want to exclude from Advanced malware sandbox inline machine learning (ML) analysis.
     3. Enter the ML partial hash of the file that you want to exclude from Advanced malware sandbox inline ML analysis.
     4. Click **Create**.
  15. Click **Create**.




###  gcloud 

  1. To create an Advanced malware sandbox security profile, run the [`gcloud beta network-security security-profiles wildfire-analysis create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/create):
         
         gcloud beta network-security security-profiles wildfire-analysis create NAME \
             --location=LOCATION \
             --organization=ORGANIZATION_ID \
             --project=PROJECT_ID \
             --description=DESCRIPTION
         

Replace the following:

     * `NAME`: the name of the Advanced malware sandbox security profile; you can specify the name as a string or as a unique URL identifier.

Don't include sensitive information such as personally identifiable information or security data in the security profile name.

If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` and `ORGANIZATION` flags.

     * `LOCATION`: the location of the Advanced malware sandbox security profile.

Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.

     * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

     * `PROJECT_ID`: the project ID of the Advanced malware sandbox security profile.

     * `DESCRIPTION`: an optional description for the Advanced malware sandbox security profile.

  2. Optional: To add and manage signature overrides, you can use one or more of the following options:

     * To add a protocol-level override to block HTTP or SMTP threats, run the [`gcloud beta network-security security-profiles wildfire-analysis add-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-override):
    
    gcloud beta network-security security-profiles wildfire-analysis add-override NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --wildfire=HTTP,SMTP \
        --action=DENY
    

     * To add an inline ML protocol override, run the [`gcloud beta network-security security-profiles wildfire-analysis add-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-override):
    
    gcloud beta network-security security-profiles wildfire-analysis add-override NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --wildfire-inline-ml=HTTP \
        --action=DENY
    

     * To add a threat ID override, run the [`gcloud beta network-security security-profiles wildfire-analysis add-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-override):
    
    gcloud beta network-security security-profiles wildfire-analysis add-override NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --threat-ids=599805 \
        --action=ALLOW
    

Replace the following parameters based on your selection:

     * `NAME`: the name of the Advanced malware sandbox security profile.
     * `ORGANIZATION_ID`: the organization ID.
     * `BILLING_PROJECT_ID`: the project ID used for billing and quotas.
     * `--wildfire`: the protocols to override the action for. Must be one of: `SMTP`, `SMB`, `POP3`, `IMAP`, `HTTP2`, `HTTP`, `FTP`.
     * `--wildfire-inline-ml`: local inline ML threats protocol override option.
     * `--threat-ids`: threat signature IDs to override. Note that the action must be `Default` or `Allow`.
     * `ACTION`: action to apply. Must be one of: `Default`, `Allow`, `Deny`, or `Alert`.
  3. Optional: To configure submission rules, run the [`gcloud beta network-security security-profiles wildfire-analysis add-submission-rule` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-submission-rule):
         
         gcloud beta network-security security-profiles wildfire-analysis add-submission-rule NAME \
             --location=LOCATION \
             --organization=ORGANIZATION_ID \
             --project=BILLING_PROJECT_ID \
             --file-types=FILE_TYPE1,FILE_TYPE2,... \
             --direction=DIRECTION
         

Replace the following:

     * `NAME`: the name of the Advanced malware sandbox security profile.
     * `LOCATION`: the location of the Advanced malware sandbox security profile.

Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.

     * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

     * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.

     * `FILE_TYPE1,FILE_TYPE2`: types of files that will be submitted to Advanced malware sandbox for analysis. File type must be one of: `ANY_FILE`, `APK`, `ARCHIVE`, `EMAIL_LINK`, `FLASH`, `JAR`, `LINUX`, `MS_OFFICE`, `PDF`, `PE`, `SCRIPT`. Note that if `ANY_FILE` is specified, no other types should be specified.

     * `DIRECTION`: direction of traffic that will be checked for files to submit to Advanced malware sandbox. Direction must be one of: `Upload`, `Download`, `Both`.

  4. Optional: To configure inline cloud analysis rules, run the [`gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-inline-cloud-analysis-rule):
         
         gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule NAME \
             --location=LOCATION \
             --organization=ORGANIZATION_ID \
             --project=BILLING_PROJECT_ID \
             --file-types=FILE_TYPE1,FILE_TYPE2,... \
             --direction=DIRECTION \
             --action=ACTION
         

Replace the following:

     * `NAME`: the name of the Advanced malware sandbox security profile.
     * `LOCATION`: the location of the Advanced malware sandbox security profile.

Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.

     * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

     * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.

     * `FILE_TYPE1,FILE_TYPE2`: types of files that will be submitted to Advanced malware sandbox for analysis. `FILE_TYPE` must be one of: `ANY_FILE`, `PE`. Note that if `ANY_FILE` is specified, no other types should be specified.

     * `DIRECTION`: direction of traffic that will be checked for files to submit to Advanced malware sandbox. Direction must be one of: `Upload`, `Download`, `Both`.

     * `ACTION`: action to take when a threat is detected by Advanced malware sandbox inline cloud analysis. Action must be one of: `Allow`, `Alert`, `Deny`.

  5. Optional: To add inline ML file exceptions, run the [`gcloud beta network-security security-profiles wildfire-analysis add-inline-ml-exception` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-inline-ml-exception):
         
         gcloud beta network-security security-profiles wildfire-analysis add-inline-ml-exception NAME \
             --location=LOCATION \
             --organization=ORGANIZATION_ID \
             --project=BILLING_PROJECT_ID \
             --partial-hash=PARTIAL_HASH \
             --filename=FILENAME
         

Replace the following:

     * `NAME`: the name of the Advanced malware sandbox security profile.
     * `LOCATION`: the location of the Advanced malware sandbox security profile.

Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.

     * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

     * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.

     * `PARTIAL_HASH`: the ML partial hash of the file.

     * `FILENAME`: the name of the file to exclude.




## List Advanced malware sandbox security profiles

You can list all the Advanced malware sandbox security profiles in an organization.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.list`



**Roles**

  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. To filter security profiles by profile type, enter **Profile type** and then select **Advanced malware sandbox (WildFire)** in the **Filter** search box.




###  gcloud 

To list all the Advanced malware sandbox security profiles, use the [`gcloud beta network-security security-profiles wildfire-analysis list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/list):
    
    
    gcloud beta network-security security-profiles wildfire-analysis list \
        --organization ORGANIZATION_ID \
        --location LOCATION
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profiles are created.

  * `LOCATION`: the location of the Advanced malware sandbox security profiles. Location is always set to `global`.




## Update an Advanced malware sandbox security profile

You can update the details of a specific Advanced malware sandbox security profile in an organization.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.describe`



**Roles**

  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Click a security profile of type **Advanced malware sandbox (WildFire)** to view the profile details.

  5. Click **Edit**.




###  gcloud 

To update the details of a Advanced malware sandbox security profile, use the [`gcloud beta network-security security-profiles wildfire-analysis update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/update):
    
    
    gcloud beta network-security security-profiles wildfire-analysis update NAME \
        --organization ORGANIZATION_ID \
        --project PROJECT_ID \
        --location LOCATION \
        [--[no-]wildfire-realtime-lookup |
         --[no-]analyze-windows-executables |
         --[no-]analyze-powershell-script-1 |
         --[no-]analyze-powershell-script-2 |
         --[no-]analyze-elf |
         --[no-]analyze-ms-office |
         --[no-]analyze-shell |
         --[no-]analyze-ooxml |
         --[no-]analyze-macho]
    

**Note:** You must specify one of the following flags in a single command: `--wildfire-realtime-lookup`, `--analyze-windows-executables`, `--analyze-powershell-script-1`, `--analyze-powershell-script-2`, `--analyze-elf`, `--analyze-ms-office`, `--analyze-shell`, `--analyze-ooxml`, or `--analyze-macho`.

Replace the following:

  * `NAME`: the name of the security profile of type `WILDFIRE_ANALYSIS` that you want to update.

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `NAME` flag, you can omit the `ORGANIZATION_ID` flag.

  * `LOCATION`: the location of the Advanced malware sandbox security profile. Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.




## View an Advanced malware sandbox security profile

You can view a specific Advanced malware sandbox security profile in an organization.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.describe`



**Roles**

  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Click a security profile of type **Advanced malware sandbox (WildFire)** to view the profile details.




###  gcloud 

To view the details of an Advanced malware sandbox security profile, use the [`gcloud beta network-security security-profiles wildfire-analysis describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/describe):
    
    
    gcloud beta network-security security-profiles wildfire-analysis describe NAME \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the security profile of type `WILDFIRE_ANALYSIS` that you want to describe; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID where the Advanced malware sandbox security profile exists. If you use a unique URL identifier for the `NAME` flag, you can omit the `ORGANIZATION_ID` flag.

  * `PROJECT_ID`: the project ID where the Advanced malware sandbox security profile exists. If you use a unique URL identifier for the `NAME` flag, you can omit the `PROJECT_ID` flag.

  * `LOCATION`: the location of the Advanced malware sandbox security profile. Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.




For example, to describe a security profile named `MySecurityProfile` by using its unique URL identifier, run the following command:
    
    
    gcloud beta network-security security-profiles wildfire-analysis describe organizations/123456789012/locations/global/securityProfiles/MySecurityProfile
    

## Delete an Advanced malware sandbox security profile

You can delete a Advanced malware sandbox security profile by specifying its name, location, and organization. However, if a security profile group references the Advanced malware sandbox security profile, you must remove the security profile from the security profile group before you can delete it.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.delete`



**Roles**

  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  4. Select the Advanced malware sandbox security profile that you want to delete, and then click **Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

To delete a Advanced malware sandbox security profile, use the [`gcloud beta network-security security-profiles wildfire-analysis delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/delete):
    
    
    gcloud beta network-security security-profiles wildfire-analysis delete NAME \
        --organization ORGANIZATION_ID \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the Advanced malware sandbox security profile that you want to delete; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `NAME` flag, you can omit the `ORGANIZATION_ID` flag.

  * `LOCATION`: the location of the Advanced malware sandbox security profile. Location is always set to `global`. If you use a unique URL identifier for the `NAME` flag, you can omit the `LOCATION` flag.




### Delete a signature override

###  gcloud 

To delete a signature override or exception, run the [`gcloud beta network-security security-profiles wildfire-analysis delete-override` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/delete-override):
    
    
    gcloud beta network-security security-profiles wildfire-analysis delete-override NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --threat-ids=599805
    

Replace the following:

  * `NAME`: the name of the Advanced malware sandbox security profile.

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

  * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.




### Delete a submission rule

###  gcloud 

To delete a submission rule, run the [`gcloud beta network-security security-profiles wildfire-analysis delete-submission-rule` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/delete-submission-rule):
    
    
    gcloud beta network-security security-profiles wildfire-analysis delete-submission-rule NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --file-types=ANY_FILE \
        --direction=both
    

Replace the following:

  * `NAME`: the name of the Advanced malware sandbox security profile.

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

  * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.




### Delete an inline ML exception

###  gcloud 

To delete an inline ML exception, run the [`gcloud beta network-security security-profiles wildfire-analysis delete-inline-ml-exception` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/delete-inline-ml-exception):
    
    
    gcloud beta network-security security-profiles wildfire-analysis delete-inline-ml-exception NAME \
        --location=global \
        --organization=ORGANIZATION_ID \
        --project=BILLING_PROJECT_ID \
        --partial-hash=PARTIAL_HASH \
        --filename=FILENAME
    

Replace the following:

  * `NAME`: the name of the Advanced malware sandbox security profile.

  * `ORGANIZATION_ID`: the organization where the Advanced malware sandbox security profile is created. If you use a unique URL identifier for the `name` flag, you can omit the `ORGANIZATION_ID` flag.

  * `BILLING_PROJECT_ID`: the project ID to use for billing and quotas.

  * `PARTIAL_HASH`: the ML partial hash of the file.

  * `FILENAME`: the name of the file to exclude.




## What's next

  * [Create and manage security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)
  * [Create and manage firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
