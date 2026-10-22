---
url: https://docs.cloud.google.com/code/docs/shell/manage-secrets/
title: Create and manage secrets with Cloud Code \u00a0|\u00a0 Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:11.673398+00:00
---

# Create and manage secrets with Cloud Code  |  Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/manage-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Create and manage secrets with Cloud Code Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create and manage secrets using Cloud Code's Secret Manager integration.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=shell--secret_manager_cloud_code_create_secret)

* * *

## Before you begin

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

## Create your Cloud Run service

Use Cloud Shell Editor as your environment for creating your Cloud Run service and secret. The editor comes preloaded with the tools needed for cloud development.

To create your service:

     1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

     2. In the Quick Pick menu that appears, select click **New Application** , and then click **Cloud Run Application**.

     3. From the list of Cloud Run samples, select **Python (Flask): Cloud Run**.

     4. Select a folder for your sample and then click **Create New Application**. 

After Cloud Shell Editor loads your service in a new workspace, view its files in the explorer view.

## Create a secret

[Secret Manager](https://cloud.google.com/secret-manager/) allows you to securely store, manage, and access secrets as binary blobs or text strings. Additionally, it manages your secrets, meaning you don't have to deal with virtual machines or operating services.

To create a secret with Cloud Code's Secret Manager integration:

     1. Click Secret Manager and give it a moment to load.
     2. If prompted to authorize Cloud Shell to make Google Cloud API calls, click **Authorize**.
     3. Click add Create Secret.
     4. If prompted, select your Google Cloud project from the dropdown selector.
     5. If prompted, enable the Secret Manager API.
     6. In the **Secret Manager - Create Secret** tab that appears, enter the following in the **Name** field:
            
            my-secret
            

     7. In the **Secret Value** field, enter:
            
            Hello secret!
            

     8. Click **Create Secret** and a message that your secret was successfully created appears.

## Add a secret to your code

Secrets are great for storing configuration information such as database passwords, API keys, or TLS certificates needed by an application at runtime.

To add a secret to your code:

     1. Open the Cloud API view and select the  Secret Manager API.

This opens a Google Cloud API Detail tab with **Secret Manager API** as the heading.

     2. In the **Install Client Library** section, click the **Python** tab and click play_arrow **Run in terminal**. This installs the `google-cloud-secret-manager` client library.

     3. Open requirements.txt and add the following line to the bottom of the file:
            
            google-cloud-secret-manager==VERSION_NUMBER
            

You can find the version number in the console after you run the installation in the previous step. For example, the console might show: `Successfully installed google-cloud-secret-manager-2.23.1`

Your changes are automatically saved.

     4. To get the latest value of your secret, open app.py and copy and paste the following function:  after the hello function:
            
            def access_secret_version(secret_version_id):
                """Return the value of a secret's version"""
                from google.cloud import secretmanager
            
                # Create the Secret Manager client.
                client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
            
                # Access the secret version.
                response = client.[access_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version)(name=secret_version_id)
            
                # Return the decoded payload.
                return response.payload.data.decode('UTF-8')
            
            

     5. To call the `access_secret_version` function, replace the message variable with the following:
            
            message = access_secret_version("<SECRET_VERSION_ID>")
            

     6. If you still have the **Secret Manager - Create Secret** tab open, file_copy **Copy** the ID.

To get the ID of a secret version at any time, navigate to Secret Manager > [SECRET_NAME] > Versions, hold the pointer over over your version, and click **Copy resource ID**.

     7. To add the version ID, replace the placeholder `<SECRET_VERSION_ID>` with your copied version ID.

## Run on Cloud Run emulator

To test your new secret, run your Cloud Run service locally on the Cloud Run emulator.

     1. Launch the Cloud Code menu from the status bar.
     2. To build and deploy your service to the emulator, select **Run on Cloud Run Emulator**.
     3. In the Run/Debug on Cloud Run Emulator tab that appears, click **Run**.
     4. When running the configuration for the first time, this process can take up to 5 minutes. The **Output** panel displays the progress as your app is built and deployed.

     5. After your app is built, launch your app by clicking the localhost link that appears in your **Output** panel. Your secret's value is displayed under the success graphic.

## View and create a new secret version

Cloud Code's Secret Manager view gives you a quick look at your project's secrets, with actions for managing them.

### Viewing the value of a secret version

     1. Click the Secret Manager view.
     2. Expand your secret by clicking on it.
     3. In the **Versions** folder, right-click the numbered version that you want to view the value of and select **Show Version Value**.

Note that you can't edit a secret version. To update a secret's value, you must create a new _version_.

### Create a new secret version

The value of a secret is stored in a secret version. A secret can have many versions. This is helpful in situations where a secret changes. Updating a secret with a new version means you don't have to update your code.

     1. Click the Secret Manager view.
     2. Right-click your secret's name and select **Create Secret Version**.
     3. In the **Secret Manager - Create Version** tab that appears, enter a new value and click **Create Version**.
     4. After the **Secret Manager - Create Secret** tab opens, click file_copy **Copy** top copy the ID.
     5. To add the newer version ID, replace the current version that appears the message variable in app.py with the newer version ID that you copied.

If you always want your code to use the latest version, replace the version number at the end of your version ID with `latest`.

## View and manage secrets

### Disable a secret version

Secret versions are enabled by default after creation, meaning they can be accessed. A disabled secret is inaccessible, but you can always restore access to it at any time.

To disable a secret version:

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** section.
     2. Expand your secret by clicking on it.
     3. Under the **Versions** folder, right-click the numbered version you want to disable.
     4. Select **Disable Version**.

### Destroy a secret version

When you destroy a secret version, it can't be accessed. Destroying a secret version is permanent.

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** section.
     2. Expand your secret by clicking on it.
     3. Under the **Versions** folder, right-click the version you want to destroy.
     4. Select **Destroy Version**.

## Cleaning up

To delete just the cluster you created for this quickstart:

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** section.
     2. Hold the pointer over your cluster name and then click open_in_new **Open in Google Cloud console**.
     3. Click **Delete** and then click **Delete**.

To delete your project (and associated resources, including any clusters):

     1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

     2. Select the project that you created for this quickstart and then click **Delete**.

     3. Type the project ID to confirm and then click **Shut down**.

This shuts down the project and schedules it for deletion.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
