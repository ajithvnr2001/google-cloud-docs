---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/create-folder/
title: Create a partner-managed folder \u00a0|\u00a0 Sovereign Controls by Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:36.742511+00:00
---

# Create a partner-managed folder  |  Sovereign Controls by Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/create-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs)
  * [ Guides ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/overview)



Send feedback 

#  Create a partner-managed folder Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through creating a new folder for Sovereign Controls by Partners. You must create this folder before creating any other resources that are intended for use with Sovereign Controls by Partners.

## Before you begin

Before you can create a new folder, ensure that you've done the following:

  * Completed onboarding to Google Cloud and received an email instructing you to create a partner-managed folder.
  * If your organization enforces the `iam.allowedPolicyMemberDomains` organization policy constraint, you must allow the following additional domain IDs before creating your Sovereign Controls by Partners folder:

    * The partner's Google Cloud organization ID or Google Workspace customer ID
    * Google's customer ID, which is `C02h8e9nw`

By allowing these IDs, your partner and Google can grant IAM roles in your organization as necessary to manage your workloads. If your partner hasn't provided their organization ID or customer ID during the onboarding process, request it from them. If you attempt to create a folder before allowing these IDs, the operation fails with the following error: `One or more users named in the policy do not belong to a permitted customer.`

See the [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#predefined-constraint) page for more information about updating the `iam.allowedPolicyMemberDomains` constraint.

  * Ensure that you understand the restrictions and limitations associated with the data boundary that your partner is offering.




## Create a new folder

  1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. If prompted, select your organization.
  3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page. **Note:** Sovereign Controls by Partners is an Assured Workloads offering, and shares similar capabilities and features. 
  4. In the step to **Add folder details** : 
     * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders for Sovereign Controls by Partners, consider the following: 
       * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. If you have existing Assured Workloads folders, consider using another naming convention to differentiate your Sovereign Controls by Partners folder from them. 
       * Don't include sensitive data or personally identifiable information (PII) in the folder name. 
     * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
     * In **Folder location** , select the location in the resource hierarchy where the folder will be created. A Sovereign Controls by Partners folder can be created as a child of an organization or of another folder.
     * Click **Next**.
  5. In the step to **Choose a control package option** , select **Sovereign Controls**.
  6. Select your partner-managed solution from the drop-down menu.
  7. Select a sub-billing account if your partner created one for you.
  8. In **Select resource location** , choose the [location](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
  9. Review the details about your selections and click **Next**.
  10. In the step to **Configure additional settings** , you must create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Sovereign Controls by Partners doesn't automatically create any cryptographic keys for you. **Note** : Once your key management project has been created, complete the steps to create a [coordinated external key](https://docs.cloud.google.com/kms/docs/create-external-key#create-coordinated). When you create a coordinated external key for Cloud EKM, note that manually created key versions aren't automatically set as the primary key version. To set it as a primary key, see [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key#set_primary).
  11. Depending on which sovereign partner you've chosen, you may have an additional **Manage partner permissions** step. In this step, you can choose to grant your partner access to the following data: 
     * **Monitoring** : This includes permissions to view [Assured Workloads monitoring](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder) information about your folder. This includes any unresolved or resolved compliance violations, and any exceptions you've granted for those violations.
     * **Access Transparency and emergency access logs** : This includes permissions to view Access Transparency logs and emergency access logs for your folder.
     * **Access Transparency support case details** : This includes permissions to include additional support case details used as an access reason within Access Transparency logs for your folder. Permission for Access Transparency and emergency access logs is needed for this permission to take effect.
     * **Access Approval information** : This includes permissions to view Access Approval logs for your folder.
For more information about how these permissions are granted or revoked, see the Partner permissions section. 
  12. After you've made your selections, click **Next**.
  13. In the step to **Review and create folder** , review the details about your new Sovereign Controls by Partners folder and ensure that they are correct. Then, click **Create Folder**. 



After completing these steps, Sovereign Controls by Partners creates the following resources:

  * A Sovereign Controls by Partners folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/supported-products) to adhere with the your partner offering. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
  * A CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. 



## Partner permissions

If you choose to grant your partner access to [Assured Workloads monitoring](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder) and access history data, you can revoke this access at any time. To grant or revoke access for all types of data, complete the following steps:

  1. In the Google Cloud console, go to the **Assured Workloads** page.

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. Click the name of your Sovereign Controls by Partners folder to view the folder's details.

  3. From the **Assured Workloads Folder Details** page, click the **Configure Partner Permissions** button in the info **Partner permissions** section.

  4. In the **Configure partner permissions** panel, select the checkboxes to grant or revoke permission for each type of data, and then click **Save**.




Your partner's access to this data will be granted or revoked depending on your selections.

### Monitoring

To enable partner access to your folder's Assured Workloads monitoring data, an Identity and Access Management (IAM) role is granted to the **Cloud Controls Partner Service Agent**. Like [all service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), the Cloud Controls Partner Service Agent acts on behalf of Sovereign Controls by Partners. It is visible in the IAM policy for your Sovereign Controls by Partners folder, and uses the following email format, where FOLDER_ID is the ID of that folder:

` service-folder-[FOLDER_ID]@gcp-sa-cloudcontrolspartner.iam.gserviceaccount.com `

The service agent is granted the **Cloud Controls Partner Monitoring Service Agent** (`roles/cloudcontrolspartner.monitoringServiceAgent`) IAM role on your folder. See the [IAM reference](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringServiceAgent) for more information about this role and its permissions.

## Next steps

  * Learn how to [configure partner-managed KMS](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/configure-kms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
