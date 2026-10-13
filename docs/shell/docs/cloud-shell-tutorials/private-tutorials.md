---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/private-tutorials/
title: Create private tutorials in Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:18.389527+00:00
---

# Create private tutorials in Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/private-tutorials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/quickstart)



Send feedback 

#  Create private tutorials in Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell supports the creation of private tutorials, enabling you to design tutorials specifically for your audience.

After you've authored tutorials using the [Writing tutorials in Cloud Shell](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/tutorials) guide and followed the best practices detailed in the [Tutorial style guide](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/style-guide), you can host your tutorial in a private Git repository to make it available to your users.

You can use any Git repository hosting service you prefer. This guide uses [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview), a regionally deployed, single-tenant managed source code repository hosted on Google Cloud, to demonstrate the steps.

**Note:** To use Secure Source Manager, you must enable billing on your Google Cloud project. For details on the cost of using Secure Source Manager, see [Secure Source Manager pricing](https://cloud.google.com/products/secure-source-manager/pricing).

## Create a private Git repository

Secure Source Manager instances are deployed to an available Google Cloud region and are accessible through their instance URIs. Repositories are created in the Secure Source Manager instance by using a web interface, or the Secure Source Manager API.

To create a Secure Source Manager repository to host your private tutorial, complete the following steps.

  1. Launch the Cloud Shell terminal. For a standalone Cloud Shell session, use [shell.cloud.google.com](https://shell.cloud.google.com).

  2. Create a Secure Source Manager instance if you don't already have one:
         
         gcloud source-manager instances create INSTANCE_ID \
             --region=LOCATION
         

Replace the following:

     * `INSTANCE_ID`: the ID of the Secure Source Manager instance.
     * `LOCATION`: the region where you are creating the instance—for example, `us-central1`.

It can take up to 60 minutes to create the instance.

  3. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar:
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev
         

Replace `PROJECT_NUMBER` with the instance's Google Cloud project number.

  4. Create a private repository:
         
         gcloud source-manager repos create REPO_ID \
             --instance=INSTANCE_ID \
             --region=LOCATION
         

Replace `REPO_ID` with the ID of the Secure Source Manager repository.

For information about the permissions required to create a repository, see [Required roles](https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository#required_roles).

  5. Add the Secure Source Manager authentication helper to your global Git config. For more information, see [Set up your credentials](https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository#set_up_your_credentials).

  6. Clone your repository to Cloud Shell:
         
         git clone https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev/PROJECT_ID/REPO_ID.git
         

Replace `PROJECT_ID` with the instance's Google Cloud project ID.

  7. Move your tutorial file to your locally created repository:
         
         mv PATH_TO_TUTORIAL REPO_ID/PATH_TO_TUTORIAL
         

Replace `PATH_TO_TUTORIAL` with the path to your private tutorial.

  8. Go to your local repository:
         
         cd REPO_ID
         

  9. Add, commit, and push the tutorial files:
         
         git add .
         git commit -m "Add private tutorial to Secure Source Manager"
         git push origin main
         

  10. You can view your Secure Source Manager repository in the web interface. For more information, see [List and view repositories](https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories).




## Create an Open in Cloud Shell link

To help your users reach your tutorial, you can use the Cloud Shell's Open in Cloud Shell feature that lets you define how users access your tutorial. For details on how to customize your link, see the [Open in Cloud Shell guide](https://docs.cloud.google.com/shell/docs/open-in-cloud-shell).

For a tutorial hosted in a Secure Source Manager repository, you'll need to define the `cloudshell_git_repo` parameter with the HTTPS URL of your repository. For example:
    
    
    https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev/PROJECT_ID/REPO_ID.git
    

You can style this link as a button and embed it in your documentation for your users to find. For example:
    
    
    [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev/PROJECT_ID/REPO_ID.git)
    

## Customize tutorials with add-on tools

You can further customize your private tutorial experience by providing your users with custom tooling to work with your tutorial.

To do so, you can create a Docker image that functions as a custom Cloud Shell environment with all the additional packages and custom configurations you want made available to your user.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
