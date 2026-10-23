---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-access-instance/
title: Quickstart: Create and access an instance \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:30.046606+00:00
---

# Quickstart: Create and access an instance  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-access-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and access an instance

Create a Secure Source Manager instance and access its web interface to prepare for creating repositories and granting users access.

**Note:** Secure Source Manager doesn't support domain-scoped projects. If your project ID contains a colon (`:`), you must create a new project before using Secure Source Manager.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Secure Source Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable securesourcemanager.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Secure Source Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable securesourcemanager.googleapis.com




### Required roles

To get the permissions that you need to create a Secure Source Manager instance, ask your administrator to grant you the [Instance Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`) IAM role on the Google Cloud project. 

**Note:** The [Secure Source Manager Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`) or [IAM basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of Owner (`roles/owner`) on your project also contains permissions to create an instance. You shouldn't grant administrator roles or basic roles in a production environment, but you can grant them in a development or test environment.

Secure Source Manager roles don't appear in the Google Cloud console until they have been granted to a principal. To grant a Secure Source Manager role for the first time, see [Grant and revoke IAM roles](https://docs.cloud.google.com/secure-source-manager/docs/grant-iam-roles).

## Create an instance

  1. Run the following command to create an instance named `my-instance` in the `us-central1` [location](https://docs.cloud.google.com/secure-source-manager/docs/locations). You might be asked to authenticate to the gcloud CLI.
         
         gcloud source-manager instances create my-instance \
             --region=us-central1
         

Where:

     * `my-instance` is the name of the instance.
     * `us-central1` is the region where you are creating the instance.

A long-running create instance operation starts. The output looks similar to the following:
    
    Create request issued for [my-instance].
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata
      apiVersion: v1
      createTime: '2023-02-27T20:57:52.315609549Z'
      requestedCancellation: false
      target: projects/PROJECT_ID/locations/us-central1/instances/my-instance
      verb: create
    name: projects/PROJECT_ID/locations/us-central1/operations/operation-1234567894561-5ec69948c0f2b-60dd727f-a9b97a2e
    

It can take up to 60 minutes to create the instance.

  2. Note the `OPERATION_NAME` which is the full resource name of the operation received in response to your request. It has the following format and is required when checking the status of the operation in the next step:
         
         projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID

For example: `projects/PROJECT_ID/locations/us-central1/operations/operation-1234567894561-5ec69948c0f2b-60dd727f-a9b97a2e` where `PROJECT_ID` is your Google Cloud project.

  3. Check the status of the `create` operation by running the following command:
         
         gcloud source-manager operations describe OPERATION_NAME \
             --region=us-central1
         

Replace `OPERATION_NAME` with the operation name returned in your create command response.

Once the instance is ready, the response will look similar to the following:
         
         {
         "name": "projects/PROJECT_ID/locations/us-central1/operations/operation-123456789012-5ec69948c0f2b-60dd727f-a9b97a2e",
         "metadata": {
           "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata",
           "createTime": "2022-11-01T14:31:32.420469714Z",
           "endTime": "2022-11-01T14:48:34.140378114Z",
           "target": "projects/PROJECT_ID/locations/us-central1/instances/my-instance",
           "verb": "create",
           "requestedCancellation": false,
           "apiVersion": "v1"
         },
         "done": true,
         "response": {
           "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.Instance",
           "name": "projects/PROJECT_ID/locations/us-central1/instances/my-instance",
           "createTime": "2022-11-01T14:31:32.416413630Z",
           "updateTime": "2022-11-01T14:31:32.416413630Z"
           },
           "state": "ACTIVE",
           "hostConfig": {
             "html": "my-instance-098765432109.us-central1.sourcemanager.dev",
             "api": "my-instance-098765432109-api.us-central1.sourcemanager.dev",
             "gitHttp": "my-instance-098765432109-git.us-central1.sourcemanager.dev"
           }
         }
         }
         

Where:

     * `my-instance-098765432109.us-central1.sourcemanager.dev` is the instance HTML URL.
     * `PROJECT_ID` is your project ID.
**Note:** It's possible for the status check to report completion before the instance is fully operational. If you encounter errors accessing the instance after creation, wait 60 minutes and try again before reaching out for assistance from Secure Source Manager Support at [secure-source-manager-support@google.com](mailto:secure-source-manager-support@google.com).
  4. Copy the HTML URL from the successfully created check status command. You will need this URL to access the instance using a web browser.




## Access an instance

After the instance is created, you can access the instance through its web interface using a browser.

**Note:** To [create repositories](https://docs.cloud.google.com/secure-source-manager/docs/create-repository) in the instance you need the Repo Creator role (`roles/securesourcemanager.repoCreator`) on the instance project and the Instance Repository Creator role (`roles/securesourcemanager.instanceRepositoryCreator`) on the Secure Source Manager instance.

  1. To get the HTML URL for your instance, run the following command again:
         
         gcloud source-manager operations describe OPERATION_NAME \
             --region=us-central1
         

  2. Copy the HTML URL from the successful response from the `gcloud source-manager operations describe` command into your browser address bar.

  3. An Oauth 2.0 screen appears asking if you want to give `sourcemanager.dev` access to your Google Cloud account.

  4. Click the **Allow** button.

  5. The Secure Source Manager web interface opens. You can create and view repositories and all associated issues and pull requests from the web interface.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Create and clone a repository](https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository)
  * [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access)
  * [Add repository users](https://docs.cloud.google.com/secure-source-manager/docs/add-repository-users)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
