---
url: https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager/
title: Connect to Secure Source Manager \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:27:11.534478+00:00
---

# Connect to Secure Source Manager  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Connect to Secure Source Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create connections to Secure Source Manager and link to Secure Source Manager repositories. This integration lets you use Developer Connect features such as dashboard views of your Secure Source Manager repositories, and use of the Developer Connect proxy to perform `git` operations, such as secure read operations.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Developer Connect, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  8. Optional: Create a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/create-key) (CMEK) for encrypting the authentication secrets that Developer Connect creates.
  9. Optional: To use the command-line instructions in this guide, complete the following steps: 
     1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
     2. Create a [Developer Connect service account](https://docs.cloud.google.com/developer-connect/docs/access-control#sa) by running the following command, where PROJECT_ID is your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects): 
            
            gcloud beta services identity create \
                        --service=developerconnect.googleapis.com \
                        --project=PROJECT_ID
                    




### Secure Source Manager requirements

  * Ensure you have an [operational Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable) deployed to a Google Cloud region.
  * The Developer Connect connection and Secure Source Manager instance must be in the same region.
  * Grant the Developer Connect service agent (P4SA) the `roles/securesourcemanager.developerConnectLinker` role in the Secure Source Manager instance's project. 



### Required roles

To get the permissions that you need to create connections and links, ask your administrator to grant you the following IAM roles: 

  * To create a connection and link to a repository: [](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin)[Developer Connect Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#developerconnect.admin) (`roles/developerconnect.admin`) on on the project where you want to create Developer Connect resources. 
  * To grant permissions to the Developer Connect service agent: [](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)[Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on on the project where Secure Source Manager is running. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a connection

This section describes how to create a connection between Developer Connect and Secure Source Manager. If you're using the Google Cloud console, then you can also start adding links to repositories as you finish setting up your connection.

To create a new Secure Source Manager connection, select one of the following options:

###  Console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Click **Create connection**.

  3. Select **Secure Source Manager** as your source provider.

  4. For **Region** , choose a region for your connection. This must be the same region as your Secure Source Manager instance.

  5. For **Name** , enter a name for your connection.

  6. In the **Instance** list, select an instance.

  7. Click **Show more** to see optional configuration settings.

  8. Optional: To disable the Developer Connect proxy, clear the **Enable Developer Connect proxy** checkbox.

**Note:** Only `git` read operations are supported when using the Developer Connect proxy with Secure Source Manager. HTTP proxy functionality is not supported for Secure Source Manager.
  9. Click **Continue**.

  10. You can link to repositories now, or do this later by editing the connection. To link to repositories, select repositories from the list.

  11. Click **Link**.




Developer Connect creates the repository links and displays them in the Google Cloud console.

###  gcloud 

To create a Developer Connect connection with Google Cloud CLI, run the following command:
    
    
    gcloud developer-connect connections create CONNECTION_ID \
      --location=REGION \
      --project=CONNECTION_PROJECT_ID \
      --secure-source-manager-instance-config=projects/INSTANCE_PROJECT_ID/locations/REGION/instances/INSTANCE_ID
    

Where:

  * CONNECTION_ID is the ID of the Developer Connect connection you want to create.
  * REGION is the region for your connection. This must be the same region as your Secure Source Manager instance.
  * CONNECTION_PROJECT_ID is the ID of the Google Cloud project where you want to create your connection.
  * INSTANCE_PROJECT_ID is the ID of the Google Cloud project where your Secure Source Manager instance is located.
  * INSTANCE_ID is the ID of your Secure Source Manager instance.



###  curl 

To create a Developer Connect connection with `curl`, make the following API call:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    https://developerconnect.googleapis.com/v1/projects/CONNECTION_PROJECT_ID/locations/REGION/connections?connection_id=CONNECTION_ID \
    -X POST -H "Content-Type: application/json" \
    -d '{"secure_source_manager_instance_config":{"instance":"projects/INSTANCE_PROJECT_ID/locations/REGION/instances/INSTANCE_ID"}}'
    

Where:

  * CONNECTION_ID is the ID of the Developer Connect connection you want to create.
  * REGION is the region for your connection. This must be the same region as your Secure Source Manager instance.
  * CONNECTION_PROJECT_ID is the ID of the Google Cloud project where you want to create your connection.
  * INSTANCE_PROJECT_ID is the ID of the Google Cloud project where your Secure Source Manager instance is located.
  * INSTANCE_ID is the ID of your Secure Source Manager instance.



## Add repository links to existing connections

Once you have established a connection to Secure Source Manager, you can link to repositories. You can repeat these steps later to link additional repositories as needed.

To create repository links on an existing Secure Source Manager connection, select one of the following options:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the **Repositories** page](https://console.cloud.google.com/developer-connect/git-repository-links)

  2. Click **Link repository**.

The **Link Git repositories** pane opens.

  3. In the connections list, choose your Secure Source Manager connection.

  4. Click **Continue**.

  5. In the repositories list, select the repositories you want to link to.

  6. Click **Create**.




Developer Connect creates the repository links and displays them in the Google Cloud console.

###  gcloud 

For more information on managing git repository links with `gcloud`, see [gcloud developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links).

## Use Developer Connect proxy in Cloud Build

To use the Developer Connect proxy in Cloud Build take the following steps:

  1. Grant the Secure Source Manager service agent the `roles/developerconnect.viewer` role, or any role that has the `developerconnect.gitRepositoryLinks.get` permission, on the Developer Connect project.
  2. Link your Secure Source Manager repository to a Developer Connect `gitRepositoryLink`. See Link to a Secure Source Manager repository for instructions.
  3. In the `.cloudbuild/trigger.yaml` file in your repository root directory, add a new entry to point to the target `gitRepositoryLink` resource.

For example:
         
         triggers:
         - name: test-trigger
           project: my-project
           configFilePath: cloudbuild.yaml
           eventType: push
           serviceAccount: projects/my-project/serviceAccounts/my-sa@my-project.iam.gserviceaccount.com
           devConnectGitRepositoryLink: projects/my-project/locations/us-central1/connections/my-ssm-connection/gitRepositoryLinks/my-repo-link
         




## Operational scope and limitations

After you configure the connection, you can perform secure `git` read operations, such as a `clone`, on Secure Source Manager instances by using the Developer Connect proxy URI.

The Developer Connect proxy does not support `git push` operations. The system prevents write operations that use the identity of the DevConnect P4SA.

You can update other configs of the connection, for example to enable or disable the Developer Connect proxy, but you cannot point the existing connection to a different Secure Source Manager instance.

## What's next

  * Learn more about [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview).
  * Learn more about [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
