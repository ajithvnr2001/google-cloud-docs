---
url: https://docs.cloud.google.com/build/docs/access-github-from-build/
title: Accessing GitHub from a build via SSH keys \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:25.304822+00:00
---

# Accessing GitHub from a build via SSH keys  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/access-github-from-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Accessing GitHub from a build via SSH keys Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to use [Secret Manager](https://docs.cloud.google.com/build/docs/how-to/using-encrypted-resources) with Cloud Build to access private [GitHub](https://github.com) repositories from a build. Secret Manager is a Google Cloud service that securely stores API keys, passwords, and other sensitive data.

**Note:** You need to use Secret Manager to connect to private GitHub repositories only when running manual builds. When you run builds using Cloud Build triggers, you can automatically connect to any private repository you own without storing your credentials in Secret Manager. For information on creating triggers, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## Objectives

  * Set up a GitHub SSH key.
  * Add the public SSH key to a private repository's deploy keys.
  * Store the private SSH key in Secret Manager.
  * Submit a build that accesses the key from Secret Manager and uses it to access the private repository.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Secret Manager
  * Cloud Build



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,cloudbuild.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,cloudbuild.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Optional. Complete the [Secret Manager quickstart](https://docs.cloud.google.com/secret-manager/docs/create-secret) to become familiar with this product. 



## Create a SSH key

  1. Open a terminal window.

  2. Create a new directory named `workingdir` and navigate into it:
         
         mkdir workingdir
         cd workingdir
         

  3. Create a new GitHub SSH key, where github-email is your GitHub email address:
         
         ssh-keygen -t rsa -b 4096 -N '' -f id_github -C github-email
         

This command creates a new SSH key `workingdir/id_github` without a passphrase for your SSH key. Cloud Build **cannot** use your SSH key if it is protected with a passphrase.




## Store the private SSH key in Secret Manager

When you [create an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/), an `id_github` file is created in your environment. Because anyone can authenticate to your account with this file, you must store the file in Secret Manager before using it in a build.

**Note:** Ensure your private key file ends with a newline before using it. Secret Manager might remove trailing whitespace, and SSH requires a newline at the end of the file for it to be considered valid.

To store your SSH key in Secret Manager, do the following:

  1. Go to the Secret Manager page in the Google Cloud console:

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create Secret**.

  3. On the **Create secret** page, under **Name** , enter a name for the secret.

  4. In the **Secret value** field, click **Upload** and upload your `workingdir/id_github` file.

  5. Leave the **Regions** section unchanged.

  6. Click the **Create secret** button.




This will upload your `id_github` file to Secret Manager.

## Add the public SSH key to your private repository's deploy keys

  1. Login to [GitHub](https://github.com).

  2. In the upper-right corner, click your profile photo, then click **Your profile**.

  3. On your profile page, click **Repositories** , then click the name of your repository.

  4. From your repository, click **Settings**.

  5. In the sidebar, click **Deploy Keys** , then click **Add deploy key**.

  6. Provide a title, paste your public SSH key from `workingdir/id_github.pub`.

  7. Select **Allow write access** if you want this key to have write access to the repository. A deploy key with write access lets a deployment push to the repository.

  8. Click **Add key**.

  9. Delete the SSH key from your disk:
         
         rm id_github*
         




## Grant permissions

You must grant permission to access Secret Manager to the service account you are using for the build.

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. From the drop-down list, select the service account whose roles you want to change.

  3. Set the status of the `Secret Manager Secret Accessor` role to **Enable**.




## Add the public SSH key to known hosts

Most machines contain a file named `known_hosts`, which contains known keys for remote hosts. The keys are often collected from the remote hosts when connecting to them for the first time, but they can also be added manually. The keys in this file are used to verify the identity of the remote host and protect against impersonation.

For Cloud Build to connect to GitHub, you must add the public SSH key to the `known_hosts` file in Cloud Build's build environment. You can do this by adding the key to a temporary `known_hosts.github` file, and then copying the contents of `known_hosts.github` to the `known_hosts` file in Cloud Build's build environment.

In your `workingdir` directory (the same directory where your `cloudbuild.yaml` is located), create a file named `known_hosts.github`. This file must be included in the source code you submit to Cloud Build so that it is available during the build execution. If you are using a Git repository with a trigger, you should commit this file to your repository. Add the public SSH key to this file:
    
    
    ssh-keyscan -t rsa github.com > known_hosts.github
    

In the next section when you configure the build, you'll add instructions in the Cloud Build config file to copy the contents of `known_hosts.github` to the `known_hosts` file in Cloud Build's build environment.

**Note:** For security, verify the host fingerprints in the `known_hosts` file against GitHub's published [SSH host key fingerprints](https://help.github.com/articles/github-s-ssh-key-fingerprints/).

## Configure the build

To configure the build:

  1. Create a build config file named `cloudbuild.yaml` with two steps: the first `gcloud` step accesses the SSH key in Secret Manager and saves it as `id_rsa` in a volume named `ssh`, along with a copy of the `known_hosts.github`. The volume is used to persist files across the build steps. The second `git` step uses the key in `id_rsa` to connect to the repository at `git@github.com:git-username/git-repository`.
         
         # Access the id_github file from Secret Manager, and setup SSH
         steps:
         - name: 'gcr.io/cloud-builders/git'
           secretEnv: ['SSH_KEY']
           entrypoint: 'bash'
           args:
           - -c
           - |
             echo "$$SSH_KEY" >> /root/.ssh/id_rsa
             chmod 400 /root/.ssh/id_rsa
             cp known_hosts.github /root/.ssh/known_hosts
           volumes:
           - name: 'ssh'
             path: /root/.ssh
         
         # Clone the repository
         - name: 'gcr.io/cloud-builders/git'
           args:
           - clone
           - --recurse-submodules
           - git@github.com:GIT_USERNAME/GIT_REPOSITORY
           volumes:
           - name: 'ssh'
             path: /root/.ssh
         
         availableSecrets:
           secretManager:
           - versionName: projects/PROJECT_ID/secrets/SECRET_NAME/versions/latest
             env: 'SSH_KEY'
         




Replace the placeholder values in the preceding commands with the following:

  * `GIT_USERNAME`: The GitHub username of the repository owner.
  * `GIT_REPOSITORY`: The name of the GitHub repository you want to access.
  * `PROJECT_ID`: The ID of the Google Cloud project where you've stored your secrets.
  * `SECRET_NAME`: The name of the secret you created in Secret Manager.



To learn about YAML multiline strings used in the preceding snippet, see [YAML multiline](https://yaml-multiline.info/).

## Submit the build

To submit the build, run the following command:
    
    
    gcloud builds submit --config=cloudbuild.yaml .
    

The output is similar to the following:
    
    
    Creating temporary tarball archive of 3 file(s) totalling 4.1 KiB before compression.
    Uploading tarball of [.] to [gs://[PROJECT-ID]_cloudbuild/source/1504288639.02---.tgz]
    Created [https://cloudbuild.googleapis.com/v1/projects/[PROJECT-ID]/builds/871b68bc---].
    Logs are available at [https://console.cloud.google.com/cloud-build/builds/871b68bc---?project=[PROJECT-ID]].
    ----------------------------- REMOTE BUILD OUTPUT ------------------------------
    starting build "871b68bc-cefc-4411-856c-2a2b7c7d2487"
    
    FETCHSOURCE
    Fetching storage object: gs://[PROJECT-ID]_cloudbuild/source/1504288639.02---.tgz#1504288640827178
    Copying gs://[PROJECT-ID]_cloudbuild/source/1504288639.02---.tgz#1504288640827178...
    / [1 files][  3.9 KiB/  3.9 KiB]
    Operation completed over 1 objects/3.9 KiB.
    BUILD
    Step #0: Already have image (with digest): gcr.io/cloud-builders/gcloud
    Starting Step #0
    Finished Step #0
    Step #1: Already have image (with digest): gcr.io/cloud-builders/git
    Starting Step #1
    Step #1: # github.com SSH-2.0-libssh_0.7.0
    Finished Step #1
    Step #2: Already have image (with digest): gcr.io/cloud-builders/git
    Starting Step #2
    Step #2: Cloning into '[REPOSITORY-NAME]'...
    Step #2: Warning: Permanently added the RSA host key for IP address 'XXX.XXX.XXX.XXX' to the list of known hosts.
    Finished Step #2
    PUSH
    DONE
    -----------------------------------------------------------------------------------------------------------------
    
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                              IMAGES  STATUS
    871b68bc-cefc-4411-856c-2a2b7c7d2487  XXXX-XX-XXT17:57:21+00:00  13S       gs://[PROJECT-ID]_cloudbuild/source/1504288639.02---.tgz  -                                 SUCCESS
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

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



### Delete the deploy key from your repository

  1. On GitHub, navigate to the main page of the repository.

  2. Under your repository name, click **Settings**.

  3. In the left sidebar, click **Deploy keys**.

  4. On the **Deploy keys** page, look for the deploy keys associated with your repository and click **Delete**.




## What's next

  * Learn how to create [GitHub triggers](https://docs.cloud.google.com/build/docs/create-github-app-triggers).
  * Learn more about using [encrypted resources in Cloud Build](https://docs.cloud.google.com/build/docs/how-to/using-encrypted-resources).
  * Learn more about [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
