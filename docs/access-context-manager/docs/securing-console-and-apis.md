---
url: https://docs.cloud.google.com/access-context-manager/docs/securing-console-and-apis/
title: Set up Context-Aware Access \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:03.169905+00:00
---

# Set up Context-Aware Access  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/securing-console-and-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Set up Context-Aware Access Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up Context-Aware Access, bind access levels to a Google group, and deploy Endpoint Verification. You can use Context-Aware Access to do the following:

  * Define access policies on Google Cloud resources based on attributes like user identity, network, location, and device state.

  * Control session length and reauthentication methods for ongoing access.

**Preview — Session controls feature only**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 




Context-Aware Access is enforced any time that a user accesses a client application that requires a Google Cloud scope, including the Google Cloud console on the web and the Google Cloud CLI.

### Before you begin

  1. Create access levels. You can create [basic access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) or [custom access levels](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level). Learn more about [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels).

  2. [Create a Google group](https://support.google.com/a/answer/9400082?visit_id=639047244761499354-1303090581&rd=2) that contains the users that you want the access levels to apply to. To apply Context-Aware Access restrictions, you bind the group to the access levels. To access the resource, users in this group must satisfy at least one of the access levels that you created. Context-Aware Access policies apply only to users within your organization.

**Important:** We recommend that you exclude at least one `Organization Admin` or `Organization Owner` from this group to reduce the risk of an accidental lockout.



## Required roles

Grant the [Cloud Access Binding Admin (`roles/accesscontextmanager.gcpAccessAdmin`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager) at the organization level. This role is required to create Access Context Manager access bindings.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the project selector menu, select your organization ID.

  3. Click **Grant access** and configure the following:

     * **New principals** : Specify the user or group that you want to grant the permissions to.

     * **Select a role** : Select **Access Context Manager > Cloud Access Binding Admin**.

  4. Click **Save**.


**Note:** For read-only access to the bindings, you can assign the **Cloud Access Binding Reader** role.

###  gcloud 

  1. Make sure that you're authenticated with sufficient privileges to add IAM permissions at the organization level. At a minimum, you need the [**Organization Administrator**](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up) role.

After you've confirmed that you have the correct permissions, sign in by running the following command:
         
         gcloud auth login
         

  2. Grant the Cloud Access Binding Admin (`roles/accesscontextmanager.gcpAccessAdmin`) role by running the following command:
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
             --member=PRINCIPAL \
             --role=roles/accesscontextmanager.gcpAccessAdmin
         

Replace the following:

     * `ORGANIZATION_ID`: the ID for your organization. You can use the following command to find the organization ID:
    
    gcloud organizations list
      ```
    
    * <code><var>PRINCIPAL</var></code>: the user or group that you want to
    grant the role to.
    




## Bind Google groups to access levels

To enforce Context-Aware Access restrictions on who can access Google Cloud resources, you need to bind a Google group to one or more access levels. Users in the specified group are granted access only if they satisfy the conditions that are defined in the bound access levels.

### Bind a group to the access level

You can bind the group to the access level using the Google Cloud console or the gcloud CLI.

### Console

To bind the group to the access level using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the Chrome Enterprise Premium page.

  
[Go to Chrome Enterprise Premium](https://console.cloud.google.com/security/caa)

If prompted, select your organization.

  2. Click **Manage Access for Google Cloud console and APIs**. The page lists the existing access bindings.

  3. Click **Create Binding**.

  4. In the **Principals** section, click **Add**.

  5. Enter the email address of the Google group that you want to bind.

  6. In the **Access levels** section, select the access levels that members of the group must satisfy to gain access. Multiple access levels are logically ORed. The logical OR means that to access the resource, the user must meet the conditions of at least one of the selected levels.

  7. To save the access binding, click **Save**.




The binding might take a few minutes to propagate. After the binding is active, members of the group are subject to the configured access level requirements when they access the Google Cloud console or use tools like the gcloud CLI that interact with Google Cloud APIs.

### gcloud

To bind the group to the access level, run the following command:
    
    
    gcloud access-context-manager cloud-bindings create \
      --group-key=GROUP_EMAIL \
      --level=ACCESS_LEVEL_ID \
      --organization=ORGANIZATION_ID
    

Replace the following:

  * `GROUP_EMAIL`: The email address of the Google group to bind—for example, `my-restricted-users@example.com`.

  * `ACCESS_LEVEL_ID`: The full resource name of the access level to apply. The resource name is in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.




You can find `POLICY_ID` by listing the policies by running the following command:
    
    
    gcloud access-context-manager policies list --organization ORGANIZATION_ID
    

  * `ORGANIZATION_ID`: Optional. Your Google Cloud organization ID. The organization ID is required only if you haven't set the default organization in your gcloud CLI configuration.



### List group bindings

To list existing bindings, run the following command:
    
    
    gcloud access-context-manager cloud-bindings list \
        --organization ORGANIZATION_ID
    

## Deploy Endpoint Verification

[Deploying Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console) is an optional step that lets you integrate device attributes into your access control policies. You can use this capability to enhance the security of your organization by granting or denying access to resources based on device attributes such as OS version and configuration.

Endpoint Verification runs as a Chrome extension on macOS, Windows, and Linux and lets you create access control policies based on device characteristics like model and OS version, and security characteristics like the presence of disk encryption, a firewall, a screen lock, and OS patches.

## What's next

  * Learn how to [require certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access), which adds an additional layer of security by ensuring that only authorized devices can access resources, even if the credentials are compromised.

  * [Deploy the Endpoint Verification extension](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console) as an administrator to your organization's company-owned devices by using the Google Cloud console.

  * Let [users install the Endpoint Verification extension themselves](https://docs.cloud.google.com/endpoint-verification/docs/self-install-extension).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
