---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/configure-private-service-connect/
title: Create a private instance with Private Service Connect \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:43.677310+00:00
---

# Create a private instance with Private Service Connect  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/configure-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a private instance with Private Service Connect

Learn how to create a Cloud Data Fusion private instance with Private Service Connect.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=data-fusion--configure-private-service-connect)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Data Fusion, BigQuery, Cloud Storage, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. Get the roles and permissions required to create a network attachment and a Cloud Data Fusion instance. For more information, see [Required roles and permissions](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect#roles-permissions).
  8. Make sure that you have created a [VPC](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) or a [Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc) network. 



## Create a private instance with Private Service Connect

  1. Go to the Cloud Data Fusion **Instances** page, and click **Create instance**.

[Create an instance](https://console.cloud.google.com/data-fusion/instance-create)

  2. In the **Instance name** field, enter a name for your new instance.

  3. In the **Description** field, enter a description for your instance.

  4. From the **Region** drop-down, select the Google Cloud region in which you want to create the instance.

  5. From the **Version** drop-down, select `6.10` or later.

  6. Select an **Edition**.

  7. Expand **Advance options** and do the following:

     1. Select **Enable private IP**.

     2. For **Connectivity type** , select **Private Service Connect**.

**Note:** The option to select the connectivity type appears only if you selected a Cloud Data Fusion version that supports Private Service Connect.
     3. From the **Network attachment** drop-down, select a network attachment.

If a network attachment is not present, create a new one:

        1. Click **Create network attachment**.
        2. In the **Name** field, enter a name for your network attachment.
        3. From the **Network** drop-down, select a VPC or a Shared VPC network.
        4. The **Region** field is auto-updated. Its value is same as the the Cloud Data Fusion instance. You can't edit this field.
        5. From the **Subnetwork** drop-down, select a subnetwork range.

**Note:** The provisioning of a secondary range for a subnet isn't required for Cloud Data Fusion. Each Cloud Data Fusion instance requests up to 32 IP addresses from the network attachment. Ensure that the subnet has enough IP addresses to support the number of Cloud Data Fusion instances that you plan to create.
        6. For **Connection preference** , the option **Accept connections for selected projects** is auto-selected.

When you create the Cloud Data Fusion instance, the Cloud Data Fusion tenant project is automatically added to the **Accepted projects** list.

Note: The option **Automatically accept connections for all projects** is less secure because it allows any service to obtain IP addresses from your subnet. 

        7. Click **Create**.

        8. On the **Create instance** page, from the **Network attachment** drop-down, select the newly created network attachment.

  8. Click **Create**. It takes up to 30 minutes for the instance creation process to complete.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the Cloud Data Fusion instance

Follow these instructions to [ delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Create your first pipeline](https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline).
  * Learn more about [Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect) in Cloud Data Fusion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
