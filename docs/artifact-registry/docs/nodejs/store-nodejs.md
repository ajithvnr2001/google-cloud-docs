---
url: https://docs.cloud.google.com/artifact-registry/docs/nodejs/store-nodejs/
title: Quickstart: Store Node.js packages in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:37.736659+00:00
---

# Quickstart: Store Node.js packages in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/nodejs/store-nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Node.js packages in Artifact Registry

This quickstart shows you how to set up a private Artifact Registry Node.js package repository and upload a package to it.

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

  5. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/nodejs/store-nodejs)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/nodejs/store-nodejs)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  16. Install PowerShell, if you want to connect to a Node.js package repository from Windows.



## Required roles

To get the permissions that you need to create and manage Artifact Registry Node.js package repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Launch Cloud Shell

In this quickstart, you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The gcloud CLI provides the primary command-line interface for Google Cloud.

Launch Cloud Shell:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. On the Google Cloud console toolbar, click **Activate Cloud Shell** : ![](https://docs.cloud.google.com/static/artifact-registry/docs/images/cloud-shell.png)




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

## Create a Node.js package repository

Create the repository for your Node.js artifacts.

  1. Create the repository.

###  Console 

     1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

     2. Click **Create Repository**.

     3. Specify `quickstart-nodejs-repo` as the repository name.

     4. Choose **npm** as the format and **Standard** as the mode.

     5. Under **Location Type** , select **Region** and then choose the location `us-central1`.

     6. Click **Create**.

The repository is added to the repository list

###  gcloud 

     1. Run the following command to create a new Node.js package repository named `quickstart-nodejs-repo` in the location `us-central1` with the description "Node.js repository".
            
            gcloud artifacts repositories create quickstart-nodejs-repo --repository-format=npm \
            --location=us-central1 --description="Node.js package repository"
            

     2. Run the following command to verify that your repository was created.
            
            gcloud artifacts repositories list
            

For more information about Artifact Registry commands, run the command `gcloud artifacts`.

  2. To simplify `gcloud` commands, set the default repository to `quickstart-nodejs-repo` and the default location to `us-central1`. After the values are set, you don't need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the command:
         
         gcloud config set artifacts/repository quickstart-nodejs-repo
         

To set the location, run the command:
         
         gcloud config set artifacts/location us-central1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.




## Configure npm

To upload and download packages, you must configure your npm projects with settings to authenticate with the repository you created. For this quickstart, you'll upload a package and then install it in a second package as a dependency.

  1. Download the [emoji-regex](https://www.npmjs.com/package/emoji-regex) package, a package that provides a regular expression to match all emoji symbols and sequences.
         
         npm pack emoji-regex
         

The command downloads an archive of the package.

  2. Extract the archive into an `emoji-regex` directory. The following command is for an archive of `emoji-regex` version 10.1.0:
         
         mkdir emoji-regex && tar xvf emoji-regex-10.1.0.tgz -C emoji-regex --strip-components 1
         

  3. Create a second npm package that you'll use to install the `emoji-regex` package from Artifact Registry. For this package, use the `npm init` command to create a basic package.
         
         mkdir npm-package2
         cd npm-package2
         
         npm init -y
         

When prompted, accept default values.

  4. Configure both the `emoji-regex` and `npm-package2` projects to authenticate with the Artifact Registry repository that you created.

     1. Run the following command. The command returns configuration settings to add to your npm configuration file.
            
            gcloud artifacts print-settings npm --scope=@quickstart
            

The `quickstart` [scope](https://docs.npmjs.com/about-scopes) is associated with your repository. When you include the scope in commands to publish or install packages, npm uses your repository. When you publish or install packages without a scope, your configured default repository is used. For more information, see the Node.js [overview](https://docs.cloud.google.com/artifact-registry/docs/nodejs). 

The output of the `gcloud` command looks like the following example. PROJECT is your Google Cloud project ID.
            
            @quickstart:registry=https://us-central1-npm.pkg.dev/PROJECT/quickstart-nodejs-repo/
            //us-central1-npm.pkg.dev/PROJECT/quickstart-nodejs-repo/:always-auth=true
            

     2. Add the configuration settings from the previous step to the project `.npmrc` file in each npm project. The file in the same directory as the `package.json` file.

To learn more about the `.npmrc` file, see the Node.js [overview](https://docs.cloud.google.com/artifact-registry/docs/nodejs).

Each Artifact Registry Node.js package repository is associated with an npm registry endpoint `https://LOCATION-npm.pkg.dev/PROJECT/REPOSITORY`. If you create another Artifact Registry Node.js package repository, npm interacts with it as a separate registry with its own scope.

  5. Edit `package.json` in both the `emoji-regex` and `npm-package2` projects.

     1. Ensure that the value for `name` includes the `quickstart` scope.

        * For `emoji-regex`:
    
    "name": "@quickstart/emoji-regex"
    

        * For `npm-package2`:
    
    "name": "@quickstart/npm-package2"
    

     2. Under `scripts`, add a script for [google-artifactregistry-auth](https://www.npmjs.com/package/google-artifactregistry-auth), a client library that updates credentials for Artifact Registry repositories.
            
            "scripts": {
              "artifactregistry-login": "npx google-artifactregistry-auth --repo-config=./.npmrc --credential-config=./.npmrc"
            }
            




## Upload a package to the repository

  1. Refresh the access token for connecting to the repository.
         
         npm run artifactregistry-login
         

  2. Add your package to the repository. You can use an `npm` or `yarn` command.
         
         npm publish
         
         
         yarn publish
         




## View the package in the repository

To verify that your package was added to the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the `quickstart-nodejs-repo` repository.

The **Packages** page lists the packages in the repository.

  3. Click a package to view package versions.




###  gcloud 

To list the images in the default `quickstart-nodejs-repo` repository, run the following command:
    
    
     gcloud artifacts packages list
    

To view versions for a package, run the following command:
    
    
    gcloud artifacts versions list --package=PACKAGE
    

Where PACKAGE is the package ID.

## Installing packages

Install the `emoji-regex` package from your Artifact Registry repository in `npm-package2`.

In the `npm-package2` directory, run the `npm install` or `yarn add` command:
    
    
    npm install @quickstart/emoji-regex
    
    
    
    yarn add @quickstart/emoji-regex
    

The command installs the `emoji-regex` package in the `npm-package2` project. It also updates `package.json` to set `emoji-regex` as a dependency.
    
    
    "dependencies": {
      "@quickstart/emoji-regex": "^10.1.0"
    }
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove a repository, ensure that any packages that you want to keep are available in another location.

To delete the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the `quickstart-nodejs-repo` repository.

  3. Click **Delete**.




###  gcloud 

  1. To delete the `quickstart-nodejs-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-nodejs-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




## What's next

  * [Learn more about configuring authentication](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages)
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore our [research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
