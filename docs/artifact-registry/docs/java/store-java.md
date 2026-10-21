---
url: https://docs.cloud.google.com/artifact-registry/docs/java/store-java/
title: Quickstart: Store Java packages in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:16.958846+00:00
---

# Quickstart: Store Java packages in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/java/store-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Java packages in Artifact Registry

This quickstart shows you how to set up a private Artifact Registry Maven repository and upload a package to it.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?tutorial=artifact-registry__java-quickstart)

* * *

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

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)




## Required roles

To get the permissions that you need to create and manage Artifact Registry Java package repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Launch Cloud Shell

In this quickstart, you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud. 

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Java. The gcloud CLI provides the primary command-line interface for Google Cloud.

Launch Cloud Shell:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. On the Google Cloud console toolbar, click **Activate Cloud Shell** : ![](https://docs.cloud.google.com/static/artifact-registry/docs/images/cloud-shell.png)




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

## Create a Java package repository

Create the repository for your Java artifacts. 

  1. Create the repository:



###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify `quickstart-java-repo` as the repository name.

  4. Choose **Maven** as the format and **Standard** as the mode.

  5. Under **Location Type** , select **Region** and then choose the location `us-central1`.

  6. Click **Create**.

The repository is added to the repository list.




###  gcloud 

  1. Run the following command to create a new Java package repository in the current project named `quickstart-java-repo` in the location `us-central1`.
         
         gcloud artifacts repositories create quickstart-java-repo --repository-format=maven \
         --location=us-central1 --description="Java package repository"
         

  2. Run the following command to verify that your repository was created:
         
         gcloud artifacts repositories list
         

For more information about Artifact Registry commands, run the command `gcloud artifacts`.




## Configure Maven

  1. Choose a simple Maven project that you want to use.

If you don't have a simple project available, you can create the [Maven in 5 minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html) project.

This quickstart assumes that your simple project does not have additional parent or plugin dependencies stored in Artifact Registry. For details about configuring a Maven project with dependencies in Artifact Registry, see [Authenticating with a credential helper](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#auth-helper).

  2. To simplify `gcloud` commands, set the default repository to `quickstart-java-repo` and the default location to `us-central1`. After the values are set, you do not need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the command:
         
         gcloud config set artifacts/repository quickstart-java-repo
         

To set the location, run the command:
         
         gcloud config set artifacts/location us-central1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.

  3. Run the following command to print the settings for the default `quickstart-java-repo` repository.
         
         gcloud artifacts print-settings mvn
         

The output of the `gcloud` command looks like the following snippet, where PROJECT is your project ID.
         
         <distributionManagement>
           <snapshotRepository>
             <id>artifact-registry</id>
             <url>artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo</url>
           </snapshotRepository>
           <repository>
             <id>artifact-registry</id>
             <url>artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo</url>
           </repository>
         </distributionManagement>
         
         <repositories>
           <repository>
             <id>artifact-registry</id>
             <url>artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo</url>
             <releases>
               <enabled>true</enabled>
             </releases>
             <snapshots>
               <enabled>true</enabled>
             </snapshots>
           </repository>
         </repositories>
         
         <build>
           <extensions>
             <extension>
               <groupId>com.google.cloud.artifactregistry</groupId>
               <artifactId>artifactregistry-maven-wagon</artifactId>
               <version>2.2.5</version>
             </extension>
           </extensions>
         </build>
         

  4. Add the settings to the `pom.xml` file for your Maven project. The following outline shows the relative placement of each main element. See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.
         
         <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                               http://maven.apache.org/xsd/maven-4.0.0.xsd">
         
           <!-- Build Settings -->
           <build>
             ...
             <extensions>...</extensions>
           </build>
         
           <!-- Environment Settings -->
           <repositories>...</repositories>
           <distributionManagement>...</distributionManagement>
         </project>
         




Your Maven project can now upload packages to your repository.

## Configure Gradle

Create a simple Gradle project to deploy a package to the Artifact Registry repository you created. If you don't have a test Gradle build, you can follow the introductory [Gradle tutorial](https://guides.gradle.org/creating-new-gradle-builds/) to create a simple Gradle build. 

To simplify `gcloud` commands, set the default repository to `quickstart-java-repo` and the default location to `us-central1`. After the values are set, you do not need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the command:
    
    
    gcloud config set artifacts/repository quickstart-java-repo
    

To set the location, run the command:
    
    
    gcloud config set artifacts/location us-central1
    

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.

  1. Add settings to connect the repository to the `build.gradle` file. The following command prints settings to add for the default `quickstart-java-repo` repository.
         
         gcloud artifacts print-settings gradle
         

The output of the `gcloud` command looks like the following example, where PROJECT is your project ID.
         
         plugins {
           id "maven-publish"
           id "com.google.cloud.artifactregistry.gradle-plugin" version "2.2.5"
               }
         
         publishing {
           repositories {
             maven {
               url "artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo"
             }
           }
         }
         
         repositories {
           maven {
             url "artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo"
           }
         }
         

  2. Verify that the `build.gradle` file includes a [publications](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:publications) section. If it does not, add it to your `build.gradle` file.

The `publications` section is a child of `publishing` as shown in the following example:
         
         publishing {
           publications {
                mavenJava(MavenPublication) {
                   groupId  'maven.example.id'
                   from components.java
                }
           }
           repositories {
             maven {
               url "artifactregistry://us-central1-maven.pkg.dev/PROJECT/quickstart-java-repo"
             }
           }
         }
         

You can also add repository configuration to your `init.gradle` or `settings` files. For details about these options, see [Setting up authentication](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#gradle).

## Upload a package to the repository

For Maven, you can use `mvn deploy` and `mvn release` to add packages to the repository.

**Note:** The `mvn archetype` command is not supported if used exclusively from the Artifact Registry repository.

For Gradle, use the `gradle publish` command to upload a package to the repository. 

## View the package in the repository

To verify that your package was added to the repository: 

###  Console 

     1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

     2. In the repository list, click the `quickstart-java-repo` repository.

The **Packages** page lists the packages in the repository.

###  gcloud 

     1. To list the packages in the `quickstart-java-repo` repository, run the following command:
            
            gcloud artifacts packages list --repository=quickstart-java-repo
            

The output will be similar to the following:
            
            Listing items under project <project-id>, location us-central1,\
            repository quickstart-java-repo.
            
            PACKAGE: maven.example.id:gradle-demo
            CREATE_TIME: 2022-01-20T22:46:07
            UPDATE_TIME: 2022-01-20T22:46:07
            

Where `maven.example.id:gradle-demo` is the **package ID**

To view versions for a package, run the following command: 
            
            gcloud artifacts versions list --package=PACKAGE
            

Where PACKAGE is the package ID. 




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any packages you want to keep are available in another location.

To delete the repository: 

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the `quickstart-java-repo` repository.

  3. Click **Delete**.




###  gcloud 

  1. To delete the `quickstart-java-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-java-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




## What's next

  * [Learn more about configuring authentication](https://docs.cloud.google.com/artifact-registry/docs/java/authentication)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/java/manage-packages)
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore our [research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
