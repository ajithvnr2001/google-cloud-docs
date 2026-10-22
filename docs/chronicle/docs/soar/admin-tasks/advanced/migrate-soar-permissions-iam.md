---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam/
title: Migrate SOAR permissions to IAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:22.048634+00:00
---

# Migrate SOAR permissions to IAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate SOAR permissions to IAM

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document guides both Google Security Operations unified customers and SOAR standalone users who need to migrate their environment from existing SOAR permission groups to Google Cloud Identity and Access Management (IAM) for access control. For a video walkthrough of this procedure, see [SOAR IAM Migration video](https://youtu.be/UBfwcgDvc0s)

**Note:** The migration tool can help you propose new custom IAM bindings for existing **SOAR Settings** permissions. For more information, see [Feature RBAC](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

The Google Cloud console verification process automates the transition from SOAR permissions to Google Cloud IAM by doing the following key steps:

  * Reads existing permissions configurations, including custom permission groups and user assignments.
  * Generates custom IAM roles that replicate the existing permissions groups.
  * Maps existing users and groups to newly created IAM roles to make sure all access privileges are retained. 
  * Creates IAM policies to bind users and groups to their assigned roles.



## Before you begin

Before starting the migration, confirm the following requirements are met:

  * If you are a Google SecOps unified customer, make sure you are using Cloud IAM to manage roles and permissions for the SIEM side of the platform. For more information, see [Migrate legacy RBAC to feature RBAC](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-rbac-to-feature-rbac).

  * Make sure you are using the same identity (email or account) for both Google Cloud console and SOAR. 

  * **IdP group mapping** : If you are using Workforce Identity Federation for authentication, verify that all users are mapped to Identity Provider (IdP) groups in the **Group Mapping** page. For information on IdP group mapping, see [Map users in the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform). The migration tool uses these mappings to create a script that binds user mails or groups to IAM principals.

  * **Email group mapping** If you are using Cloud Identity for authentication, verify that that all users are mapped to email groups in the **Group Mapping** page. For information on email mapping, see [Map users in the platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party). The migration tool uses these mappings to create a script that binds user mails or groups to IAM principals.

  * Optional: SOAR API key. If you don't have SOAR permissions to map the current user in the **Group Mappings** page, you can ask a SOAR administrator to provide a SOAR API key and use that to generate the scripts instead. 




The SOAR admin should carry out the steps in the following procedure:

  1. In the Google SecOps platform, go to **SOAR Settings > Advanced > Permission Groups (API Keys)**.
  2. Create a Permission Group making sure that the **Settings** module and the options under Settings are all checked.
  3. Go to **SOAR Settings > Advanced > API Keys**.
  4. Add a new API key making sure to select the Permission Group that you created.
  5. Copy the generated API key. 


  * **Permissions** : Confirm you have the necessary permissions:

    * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#chronicle.admin)
    * [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#chroniclesm.admin)
    * [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#chronicle.soarAdmin)

**Warning:** After you enable IAM, then all Chronicle predefined roles will be activated with SOAR permissions. Chronicle API Admin will now include SOAR Admin permissions. If you don't want the principals (users / groups) assigned to the Chronicle predefined roles to have SOAR permissions or if you want to limit their permissions, we recommend you assign them to a custom role that explicitly excludes SOAR permissions.

After the migration, if there are unresolved issues, click **Disable IAM** to revert the migration from Permission Groups to IAM roles. The newly created IAM roles and bindings won't be deleted.

For a complete list of permissions needed for each role, see [Required IAM permissions](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam#required_permissions_for_every_role).

There are two ways to migrate SOAR permissions:

  * Using Google Cloud CLI
  * Using Terraform



## Migrate SOAR permissions using Google Cloud CLI

To migrate your SOAR permissions to Google Cloud IAM, follow these steps:

  1. In the Google Cloud console, go to Google SecOps administration settings.
  2. Click the **SOAR IAM Migration** tab. ![SOAR IAM Migration](https://docs.cloud.google.com/static/chronicle/images/soar/soariam1new.png)
  3. In the **Migrate role bindings** section, copy the Google Cloud CLI commands. When given the option to specify a new condition, select 2. None. . 
  4. On the Google Cloud toolbar, click **Activate Cloud Shell**.
  5. In the terminal window, paste the Google Cloud CLI commands and press **Enter**. ![Paste commands](https://docs.cloud.google.com/static/chronicle/images/soar/soariam2.png)
  6. Make sure the scripts are executed successfully. 
  7. Return to the Google Cloud console, and in the **Finished with this task** section, click **Enable IAM**. ![Paste commands](https://docs.cloud.google.com/static/chronicle/images/soar/soariam3.png)



## Migrate SOAR permissions using Terraform

To migrate your SOAR permissions to Google Cloud IAM using terraform, follow these steps:

  1. In the Google Cloud console, go to Google SecOps administration settings.
  2. Click the **SOAR IAM Migration** tab. ![SOAR IAM Migration](https://docs.cloud.google.com/static/chronicle/images/soar/soariam1new.png)
  3. In the **Migrate role bindings** section, copy the Google Cloud CLI commands.
  4. Go to your Terraform repository and map the Google Cloud CLI commands to their corresponding Terraform equivalents. The following table maps Google Cloud CLI create custom role command with Terraform commands.

gcloud Flag | Terraform Argument | Notes  
---|---|---  
`ROLE_ID` (Positional) | `role_id` | In Terraform, don't include the `projects/PROJECT_ID/roles/` prefix. Only use the ID string (for example, `myCustomRole`).  
`--project` | `project` | The ID of the project where the custom role is defined.  
`--title` | `title` | A human-readable title for the role.  
`--description` | `description` | A summary of the role's purpose and permissions.  
`--permissions` | `permissions` | `gcloud` accepts a comma-separated string. Terraform requires a list of strings: `["perm.a", "perm.b"]`.  
`--stage` | `stage` | Valid values: `ALPHA`, `BETA`, `GA`, `DEPRECATED`, `DISABLED`, `EAP`.  
**Note:** Ensure that each --flag from your command line is correctly paired with its corresponding argument within the Terraform resource block.

**Google Cloud CLI mapping to Terraform example**

Google Cloud CLI command: 
    
    
    gcloud iam roles create SOAR_Custom_managedUser_google.com --project="{customer project}" 
    --title="SOAR Custom managedUser Role" 
    --description="SOAR Custom role generated for IDP Mapping Group ManagedUser" 
    --stage=GA 
    --permissions=chronicle.cases.get
    

Terraform command:
    
    
    resource "google_project_iam_custom_role" "{terraform_name}" {
      role_id     = "SOAR_Custom_managedUser_google.com"
      title       = "SOAR Custom managedUser Role"
      project     = "{customer project}"
      stage       = "GA"
      permissions = [
        #This is an example!
        "chronicle.cases.get"
      ]
    }
    

### IAM Policy Bindings (Assign Roles)

When you use **Google Cloud CLI projects add-iam-policy-binding** , you grant a specific role to a specific member (user, service account, or group). The following table maps Google Cloud CLI commands with Terraform commands. Map the commands in order to assign IAM roles. 

gcloud Flag | Terraform Argument | Notes  
---|---|---  
`PROJECT_ID` (Positional) | `project` | The ID of the target project.  
`--member` | `member` | The principal identity (for example, `user:email`, `serviceAccount:email`, `group:email`).  
`--role` | `role` | The role ID. Use the full path for custom roles (`projects/ID/roles/NAME`) and the short name for standard roles (`roles/NAME`).  
  
**Assigning role example**

Google Cloud CLI command: 
    
    
    gcloud projects add-iam-policy-binding
     {customer project}
    --member="user:alice@example.com" 
    --role="projects/{customer project}/roles/SOAR_Custom_managedUser_google.com"
    

Terraform command:
    
    
    resource "google_project_iam_member" "{terraform_name}" {
      project = "{customer project}"
      role    = "projects/{customer project}/roles/SOAR_Custom_managedUser_google.com"
      member  = "user:alice@example.com"
    }
    

**Note:** Google doesn't recommend using **google_project_iam_binding** (singular "binding" matches the Google Cloud CLI command name), as it will remove anyone else who has that role if they aren't listed in your code. Use **google_project_iam_member** instead. **Important:** The **Permission Group** column continues to be displayed on the **Group Mapping** page after migration for backwards compatibility with legacy SOAR API. Do not delete these assignments. The column will be automatically removed by November 30, 2026 without any customer impact. 

## Post migration

After you have switched to using IAM permissions, each curl command that you use to call an API must be sent either with a mapped service account (mapped in IDP mapping groups) or with a user who has logged in to the platform at least once. 

## FAQ

  * For a detailed list on issues and best practices, see [FAQ on IAM role migration](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq#migration_permissions_to).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
