---
url: https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate/
title: Quickstart: Issue a certificate \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:34.962195+00:00
---

# Quickstart: Issue a certificate  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issue a certificate using the Google Cloud console

This quickstart guide shows you how to generate or issue certificates through Certificate Authority Service using the Google Cloud console.

Learn to manage private certificate authorities (CAs) securely without provisioning or maintaining infrastructure.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Certificate Authority Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Certificate Authority Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com)




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [CA Service Operation Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.caManager) (`roles/privateca.caManager`)
  * [CA Service Certificate Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.certificateManager) (`roles/privateca.certificateManager`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a CA pool

A CA pool is a collection of multiple CAs. A CA pool provides the ability to rotate trust chains without any outage or downtime for workloads. A CA pool lives in a single [Google Cloud location](https://cloud.google.com/about/locations) that you cannot change after creation.

To create a CA pool with the default settings, do the following:

  1. Go to the **Certificate Authority Service** page in the Google Cloud console.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Under the **CA pool manager** tab, click add_box**Create pool**.

  3. On the **Create CA pool** page, add a name for the CA pool.

**Note:** Resource names can contain letters, numbers, hyphens (-), and underscores (_) and can be up to 63 characters long.
  4. Click **Region** , and select **us-east1 (South Carolina)** as the region of the CA pool.

  5. Click **Next** for each step.

  6. Click **Done**.




You can see this CA pool in the list of CA pools under the **CA pool manager** tab.

## Create a root CA

A CA pool is empty on creation. You must add a CA to the CA pool to request certificates.

A root CA has a self-signed certificate that resides in the client's trust store. This section explains how you can add a root CA to the CA pool you created.

To add a root CA to your CA pool, do the following:

  1. On the **Certificate Authority Service** page, click **CA manager**.
  2. Click the **Create CA** arrow_drop_down expander arrow, and then select **Create CA in an existing CA pool**.
  3. Select the CA pool you created.
  4. Click **Continue**.
  5. In the **Select CA type** section, click **Continue**.
  6. In the **Organization (O)** field, enter the name of your organization.
  7. In the **CA common name (CN)** field, enter the name of the CA. Note the CA name because you will need it for requesting a certificate.
  8. Click **Continue** for each step.
  9. Review the details of the CA, and click **Done**.



## Optional: Create a subordinate CA pool

A subordinate CA pool lets you organize and manage multiple subordinate CAs. The root CA validates and signs all CAs within a subordinate CA pool.

To create a subordinate CA pool with the default settings, do the following:

  1. On the **Certificate Authority Service** page, click **CA pool manager**.
  2. Click add_box**Create pool**.
  3. On the **Create CA pool** page, add a name for the subordinate CA pool.

**Note:** Resource names can contain letters, numbers, hyphens (-), and underscores (_) and can be up to 63 characters long.
  4. Click **Region** , and select **us-east1 (South Carolina)** as the region of the subordinate CA pool.

  5. Click **Next** for each step.

  6. Click **Done**.




Ensure that the subordinate CA pool is available in the list of CA pools under the **CA pool manager** tab.

## Optional: Create a subordinate CA signed by your root CA

Subordinate CAs are responsible for distributing certificates to the _end entities_ that need them, such as web servers, users, and devices. Subordinate CAs create a layer of separation between the highly sensitive root CA and the day-to-day certificate issuance.

To generate a subordinate CA that's signed by a root CA that you created earlier, do the following:

  1. On the **Certificate Authority Service** page, click **CA manager**.
  2. Click the **Create CA** arrow_drop_down expander arrow, and then select **Create CA in an existing CA pool**.
  3. Select the subordinate CA pool that you created.
  4. Click **Continue**.
  5. Click **Subordinate CA**.
  6. Click **Root CA is in Google Cloud**.
  7. In the **Signing Certificate Authority** field, click **Browse**.
  8. From the **Select a CA** dialog, select the root CA created in the [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate#create-ca) section.
  9. Click **Confirm**.
  10. In the **Valid for** field, enter the duration that you want the subordinate CA certificate to be valid for.
  11. Click **Continue**.
  12. In the **Organization (O)** field, enter the name of your organization.
  13. In the **CA common name (CN)** field, enter the name of the subordinate CA. Note the subordinate CA name because you will need it for requesting a certificate.
  14. Click **Continue** for each step.
  15. Review the details of the subordinate CA, and click **Done**.



## Request a certificate

To request a certificate using the CA, do the following:

  1. On the **Certificate Authority Service** page, click **Request a certificate**.
  2. Click **Enter details**.
  3. Under **Add domain name** , enter the fully qualified domain name of the site you want to secure with this certificate.
  4. Click **Next**.
  5. Under **Configure key size and algorithm** , click **Continue**.

You will see the generated certificate that you can copy or download. To copy the certificate, click content_copy.

  6. Click **Done**.




## Clean up

Clean up by revoking the certificate and deleting the CA pool, the CA, and the project you created for this quickstart.

  1. Revoke the certificate.

     1. Click the **Private certificate manager** tab. 
     2. In the list of certificates, click more_vert**View more** in the row of the certificate you want to delete. 
     3. Click **Revoke**. 
     4. In the dialog that opens, click **Confirm**. 
  2. Delete the CA.

You can delete a CA only after you have revoked all the certificates issued by it.

After you have revoked the certificate, do the following:

     1. In the list of CAs, select the CA you want to delete. 
     2. Click delete**Delete**. The **Delete Certificate Authority** dialog appears. 
     3. Optional: Select one or both the following checkboxes if the conditions apply to you: 
        * **Delete this CA, even if there are active certificates**

This option lets you delete a CA with active certificates. Deleting a CA with active certificates might cause websites, applications, or systems relying on those certificates to fail. We recommend that you revoke all active certificates issued by a CA before you delete the CA.

        * **Skip the 30 day grace period and delete this CA immediately**

The 30-day grace period allows you time to revoke all certificates issued by this CA and verify that no systems depend on this CA. We recommend that use this option _only_ in non-production or test environments to prevent potential outages and data loss.

     4. Click **Confirm**. 

The CA state changes to `Deleted`. The CA is permanently deleted 30 days after you initiate the deletion.

  3. Delete the CA pool.

You can delete a CA pool only after CA Service permanently deletes the CA.

After you have deleted the CA in the CA pool, do the following:

     1. Click the **CA pool manager** tab. 
     2. In the list of CA pools, select the CA pool you want to delete. 
     3. Click delete**Delete**. 
     4. In the dialog box that opens, click **Confirm**. 
  4. To delete the project, do the following:

**Caution** : Deleting a project has the following effects: 
        * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
        * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

     1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

     2. In the project list, select the project that you want to delete, and then click **Delete**. 
     3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).
  * Learn more about [creating a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).
  * Learn more about [creating CAs](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).
  * Learn more about [requesting certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).
  * Learn how to [control the type of certificates a CA pool can issue](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
