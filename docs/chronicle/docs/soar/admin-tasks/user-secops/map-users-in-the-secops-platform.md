---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform/
title: Map users with third-party identity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:29.703565+00:00
---

# Map users with third-party identity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map users with third-party identity

Supported in:

Google SecOps 

**Note:** "If you've already completed Stage 2 of SOAR migration to Google Cloud, you need to use IAM to manage feature access to Google SecOps including SOAR. The **Permission Group** column is still displayed post migration in the **Group Mapping** page for backward compatibility. Do not delete these assignments. The column will be removed by November 30, 2026 without any customer impact. For more information, see [Migrate to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

This document explains how to provision, authenticate, and map users with secure identification to the Google Security Operations platform. It outlines the configuration process with Google Workspace as the external Identity Provider (IdP), though the steps are similar for other IdPs. When you use the Cloud Identity Provider, you should configure the service with email groups instead of IdP groups. For details, see [Map users in Google SecOps platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party). 

## Set up SAML attributes for provisioning

This section only applies before [Stage 1 of SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After completing Stage 1 of the migration, refer to the [Google Cloud Third-Party Identity Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

To set up SAML attributes and groups in the external IdP, do the following:   


  1. In the Google Workspace, go to the **SAML Attributes** mapping section.
  2. Add the following mandatory attributes:
     * `first_name`
     * `last_name`
     * `user_email`
     * `groups`
  3. In **Google Groups** , enter the IdP group names. For example, `Google SecOps administrators` or `Gcp-security-admins`. Note these group names; you need them later for mapping in the Google SecOps platform. (In other external providers, such as Okta, this is referred to as _IdP Groups_).

  
![samlattrributes](https://docs.cloud.google.com/static/chronicle/images/soar/samlattributes.png)**Figure 1.** SAML attribute mapping 

## Set up IdP provisioning

This section only applies before [Stage 1 of SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to the [Google Cloud Third-Party Identity Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication). 

To set up IdP provisioning, follow the steps in [ Configure the IdP](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication#configure-idp) and [Create a workforce identity pool provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication#create_a_workforce_identity_provider). 

The following example is the `workforce pool` creation command for the app configuration described in [ Configure Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication#configure_workforce_identity_federation): 
    
    
    gcloud iam workforce-pools providers create-saml WORKFORCE_PROVIDER_ID \
      --workforce-pool=WORKFORCE_POOL_ID \
      --location="global" \
      --display-name=WORKFORCE_PROVIDER_DISPLAY_NAME \
      --description=WORKFORCE_PROVIDER_DESCRIPTION \
      --idp-metadata-path=PATH_TO_METADATA_XML \
      --attribute-mapping="google.subject=assertion.subject,attribute.first_name=assertion.attributes.first_name[0],attribute.last_name=assertion.attributes.last_name[0],attribute.user_email=assertion.attributes.user_email[0],google.groups=assertion.attributes.groups"

## Control user access

There are multiple ways to manage user access to different aspects of the platform: 

  * **Permissions groups** : Set user access levels by assigning them to specific permission groups. These groups determine which modules and submodules users can view or edit. For example, a user might have access to **Cases** and **Workdesk** pages, but be restricted from **Playbooks** and **Settings**. For more information, see [Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups). 
**Important:** Any permission group assigned to users must have at least one default landing module enabled in its **Permissions** settings. Examples include **Homepage** , **Dashboards** , or **Cases**. If you disable all default landing modules this will cause backend errors and result in an infinite login redirect loop.
  * **SOC roles** : Define the role of a group of users. You can assign users to SOC roles to streamline task management. Instead of assigning cases, actions, or playbooks to individuals, they can be assigned to a SOC role. Users can see cases assigned to them, their role, or additional roles. For more information, see [ Work with roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles). 
  * **Environments or environment groups** : Configure environments or environment groups to segment data across different networks or business units, commonly used by businesses and Managed Security Service Providers (MSSPs). Users can only access data within the environments or groups assigned to them. For more information, see [ Work with environments](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments).



## Map and authenticate users

The combination of permission groups, SOC roles, and environments determines the Google SecOps user journey for each IdP group in the Google SecOps platform. 

  * For customers who use a third-party provider, map each IdP group defined in the SAML settings on the **Group Mapping** page.
  * For customers who use Cloud Identity Provider, map email groups on the **Group Mapping** page. For more information, see [Map users in the Google SecOps platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).



You can map IdP groups with multiple permission groups, SOC roles, and environments. This makes sure that different users mapped to different IdP groups in the SAML provider inherit all required permission levels. For more information, including how Google SecOps manages this, see [Multiple permissions in IdP group mapping](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters).

You can also choose to map IdP groups to individual control access parameters. This enables a more granular level of mapping and can be helpful for large customers. For more information, see [Map IdP groups to access control parameters](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform#map-parameters).

By default, the Google SecOps platform includes an IdP group of default administrators. 

To map IdP groups, follow these steps: 

  1. In Google SecOps, go to **SOAR Settings > Advanced > Group Mapping**.
  2. Make sure you have the names of the IdP groups available.
  3. Click  **Add** **Add** and start mapping the parameters for each IdP group. 
  4. Once you've finished, click **Add**. Each time a user signs in to the platform, they are automatically added to the **User Management** page, found under **Settings > Organization**.



When users attempt to sign in to the Google SecOps platform, but their IdP group hasn't been mapped, for users not to be rejected, we recommend enabling the **Default Access Settings** and setting administrator permissions on this page. After the initial administrator setup is complete, we suggest adjusting the administrator permissions to a more minimal level.

##  Map IdP groups to access control parameters

This section describes how to map different IdP groups to one or more access control parameters within the **IdP Group Mapping** page. This approach is beneficial for customers who want to onboard and provision user groups based on specific customizations, rather than adhering to the standardization of the Google SecOps SOAR platform. While mapping groups to parameters may require you to create more groups initially, once the mapping is set, new users can join Google SecOps without the need to create additional groups.

For information about multiple permission in group mapping, see [Map users with multiple control access parameters](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters).

### Delete users

If you delete groups from here, make sure to delete the individual users from the **User Management** screen. For more information, see [Delete Google SecOps users](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-can-i-disabledelete-a-user-account-in-chronicle-soar). 

### Use Case: Assign unique permission fields to each IdP group

The following example illustrates how to use this feature to help onboard and provision users according to your company's needs.

Your company has three different personas: 

  * Security analysts (containing group members Sasha and Tal)
  * SOC engineers (containing group members Quinn and Noam)
  * NOC engineers (containing group members Kim and Kai)

Security analysts and SOC Engineers have the same Google SecOps Permission Groups (Analyst) and SOC Roles (Tier 1), but while the Security Analysts have permissions for the London environment, the SOC Engineers have permissions for the Manchester environment. Meanwhile, NOC Engineers have permissions for the **London** environment, but are assigned the **Basic** Permission Group and **Tier 2** SOC Role. 

This scenario is illustrated in the following table:

Persona | Permission Group | SOC Role | Environment  
---|---|---|---  
Security analysts | Analyst | Tier 1 | London  
SOC engineers | Analyst | Tier 1 | Manchester  
NOC engineers | Basic | Tier 2 | London  
  
For this example, assume that you already set up the necessary permission groups, SOC roles, and environments in Google SecOps.

Here is how you would set up the IdP groups in the SAML provider and in the Google SecOps platform: 

  1. In your SAML provider, create the following user groups: 
     * Security analysts (containing Sasha and Tal)
     * SOC engineers (containing Quinn and Noam)
     * NOC engineers (containing Kim and Kai)
     * London (containing Sasha, Tal, Kim and Kai)
     * Manchester (containing Quinn and Noam)
  2. Go to **Settings > SOAR Settings > Advanced > Group Mapping**.
  3. Click  **Add** **Add**.
  4. Enter the following details in the dialog:
     * IdP / User Group: `Security analysts`
     * Permission Group: ` Analyst`
     * SOC Role: `Tier 1 `
     * Environment: _leave blank_
  5. Enter the following details in the next dialog:
     * IdP Group: ` SOC engineers `
     * Permission Group: `Analyst`
     * SOC Role: ` Tier 1`
     * Environment: _leave blank_
  6. Enter the following details in the next dialog:
     * IdP Group: `NOC engineers`
     * Permission Group: ` Basic `
     * SOC Role: `Tier 2 `
     * Environment: _leave blank_
  7. Enter the following details in the next dialog:
     * IdP Group: `London`
     * Permission Group: _leave blank_
     * SOC Role: _leave blank_
     * Environment: `London`
  8. Enter the following details in the next dialog:
     * IdP Group: `Manchester`
     * Permission Group: _leave blank_
     * SOC Role: _leave blank_
     * Environment: `Manchester`



For customers using the Case Federation feature, see [ Set up federated case access for Google SecOps](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops).

## Map service accounts for API access

To grant a _service account access_ or _workload identity federation access_ to Google SecOps, you must map the identity to the platform's access control parameters. This mapping is a mandatory step to provide the identity with the necessary access to **SOC Roles** , and **Environments** required to perform automated tasks or API operations.

  1. Go to **SOAR Settings > Advanced > Group Mapping**.
  2. Click add **Add**.
  3. Complete the fields in the **Add Mapping** dialog to map the identity to the platform's access control parameters.

     1. In the **IdP / User group** field, enter one of the following: 
        * The full email address of your service account, if identity was set up using Cloud Identity.
        * The Workload Identity principal string, if identity was set up using Workforce Identity Federation.
     2. Configure the following access control fields:

Field | Description  
---|---  
**Permission groups** | Select the permission groups to define which modules and submodules the identity can access.  
**SOC roles** | Select the SOC roles to define the identity's role (such as Tier 1).  
**Environments** | Select the environments or environment groups the identity can access (such as **All Environments**).  
**Group members** | Enter the required user emails if applicable. Press **Enter** after adding each email.  
**Restricted actions** | Select the restricted actions to limit specific operations within modules.  
  4. Click **Add**.




For more information on setting up service accounts, see the [API migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
