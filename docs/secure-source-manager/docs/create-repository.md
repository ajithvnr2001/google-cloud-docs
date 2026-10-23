---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-repository/
title: Create and update a repository \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:54.911859+00:00
---

# Create and update a repository  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Create and update a repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and update a repository using the Secure Source Manager web interface or Secure Source Manager API. 

If your Secure Source Manager instance hasn't been created yet, see [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance) to get started.

## Before you begin

  1. Create or request access to a Secure Source Manager instance. For more information, see [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).  

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. Install the `beta` Google Cloud CLI component: 
         
         gcloud components install alpha




### Required roles

To get the permissions that you need to create a repository, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Repository Creator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Creator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoCreator) (`roles/securesourcemanager.repoCreator`) on the instance project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Create a repository

### Web interface

  1. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

     * INSTANCE_ID with the instance name.
     * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION with the instance's region.
  2. Authenticate using your Secure Source Manager credentials if needed.

  3. Click the **\+ Create new repository** icon in the navigation menu.

  4. Fill out the repository details:

     1. **Repository ID** : Enter a name for the repository.

**Note:** Repository IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lowercase letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the repository.
     2. **Description** : Optional: Enter a description of the repository.

**Caution:** Don't put sensitive or identifying data in the description or other similar resource fields. These fields are treated as Service Data in accordance with the Google Cloud [Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).
     3. **Default branch** : Name of the default branch.

  5. **Service account** : Optional: Enter the service account to associate with the repository. This user-managed service account is used for integrations such as Cloud Build. For more information, see [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build). 

  6. **Initialize repository** : Optional: Select this option if you want to initialize the repository and add .gitignore, license, and README files.

  7. **.gitignore** : Optional: Choose which files to **not** track using the drop-down menu templates.

  8. **license** : Optional: Select a common license from the drop-down menu.

  9. Click **Create repository**. 




###  gcloud 

  1. Create a repository using the gcloud CLI by running the following command:
         
         gcloud source-manager repos create REPOSITORY_ID \
             --region=LOCATION \
             --project=PROJECT_ID \
             --instance=INSTANCE_ID \
             --description=DESCRIPTION \
             --default-branch=BRANCH \
             --gitignores=GITIGNORES \
             --license=LICENSE \
             --readme=README \
             --service-account=SERVICE_ACCOUNT
         

Replace the following:

     * `REPOSITORY_ID` with the name for your repository.

**Note:** Repository IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lowercase letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the repository.
     * `LOCATION` with the region where you want to create the repository. For more information about supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).

     * `PROJECT_ID` with the project ID of the Secure Source Manager instance you want to create the repository in.

     * `INSTANCE_ID` with the instance ID of the instance you are creating the repository in. To list the Secure Source Manager instances in your project, see [List and view instances](https://docs.cloud.google.com/secure-source-manager/docs/list-view-instances).

     * `DESCRIPTION` with a description of the repository. This is optional and can be omitted.

**Caution:** Don't put sensitive or identifying data in the description or other similar resource fields. These fields are treated as Service Data in accordance with the Google Cloud [Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).
     * `BRANCH` with the default branch name. This is optional and can be omitted. Default branch name when not set is `main`.

     * `GITIGNORES` with a comma-separated list of gitignore template names. This is optional and can be omitted. To view the full list of available templates, see the [repository initialization configuration reference](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#InitialConfig).

     * `LICENSE` with the license template name to apply to your repository. This is optional and can be omitted. To view the full list of available license templates, see the [repository initialization configuration reference](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#InitialConfig).

     * `README` with `default` to create a README file from the default template. This is optional and can be omitted. If omitted, a README file won't be created.

     * `SERVICE_ACCOUNT` with the email address of the service account you want to associate with the repository. This is optional and can be omitted.




###  API 

  1. Create a repository using a REST call by running the following command:
         
         curl \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/repositories?repository_id=REPOSITORY_ID \
             -d '{
               "instance": "projects/PROJECT_ID/locations/REGION/instances/INSTANCE_ID",
               "serviceAccount": "SERVICE_ACCOUNT"
             }'
         

Replace the following:

     * `REGION` with the region of your Secure Source Manager instance. For more information about supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).
     * `INSTANCE_ID` with your Secure Source Manager instance ID.
     * `PROJECT_ID` with the project ID of your Secure Source Manager instance. For more information about where to find your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `REPOSITORY_ID` with the name for your repository.
     * `SERVICE_ACCOUNT` with the email address of the service account you want to associate with the repository.

Additional values can be specified using the HTTP POST data flag, `-d'{}'` including initializing the repository, adding a specific `.gitignore` file, or licenses. For more information, see the [Reference documentation](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest).

**Caution:** Don't put sensitive or identifying data in the description or other similar resource fields. These fields are treated as Service Data in accordance with the Google Cloud [Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).**Note:** Repository IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lowercase letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the repository.

If you want your output to be human-readable, you can pipe it to JSON using `json_pp`.

For example:
    
    curl \
        -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://securesourcemanager.googleapis.com/v1/projects/my-project-id/locations/us-central1/repositories?repository_id=my-repo \
        -d '{
          "instance": "projects/my-project-id/locations/us-central1/instances/prod-test-instance",
          "serviceAccount": "my-service-account@my-project-id.iam.gserviceaccount.com",
          "initialConfig": {
            "defaultBranch": "main"
          }
        }' | json_pp
    

The response resembles the following:
    
    {
      "name": "operations/266bf4c7-13fe-11ed-be24-da823b7355d0",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata",
        "createTime": "2022-08-04T14:02:59.810496928Z",
        "endTime": "2022-08-04T14:03:00.558354528Z",
        "target": "projects/654987321654/locations/us-central1/repositories/my-repo",
        "verb": "create",
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.Repository",
        "name": "projects/my-project-id/locations/us-central1/repositories/my-repo",
        "instance": "projects/654987321654/locations/us-central1/instances/prod-test-instance",
        "serviceAccount": "my-service-account@my-project-id.iam.gserviceaccount.com",
        "createTime": "2022-08-04T14:03:00Z",
        "uris": {
          "html": "https://prod-test-instance-654987321654.us-central1.sourcemanager.dev/my-project-id/my-repo",
          "gitHttps": "https://prod-test-instance-654987321654-git.us-central1.sourcemanager.dev/my-project-id/my-repo.git"
        }
    }
    

Where:

     * `654987321654` is the repository project number.
     * `my-project-id` is the repository project ID.
     * `my-repo` is the `REPOSITORY_ID` that you set in the create command. The `uris` field contains the URLs to access the repository via the web browser or via Git protocol HTTPS access.
  2. Access your new repository with the HTML URI in the response. Code review, issue tracking, and pull requests are supported in the Secure Source Manager web interface. 




The repository is created in your Secure Source Manager instance.

When you create a new repository, you are granted the Repo Admin role (`roles/securesourcemanager.repoAdmin`). The new IAM permission might take up to 2 minutes to propagate, so if you get a permissions error when you try to access the repository after creation, wait a few minutes and try again.

Repositories you've created are listed in the Secure Source Manager web interface on the **My repositories** page.

## Update a repository

### Web interface

  1. Go to the repository page in the Secure Source Manager web interface.
  2. Click **Repository settings** in the navigation menu.
  3. In the **Basic settings** section, enter the service account email address in the **Service account** field.
  4. Click **Save changes**.



###  gcloud 

  1. To update the repository service account, run the following command:
         
         gcloud source-manager repos update REPOSITORY_ID \
             --region=LOCATION \
             --project=PROJECT_ID \
             --service-account=SERVICE_ACCOUNT
         

Replace the following:

     * `REPOSITORY_ID` with the name of the repository you want to update.
     * `LOCATION` with the region where the repository is located.
     * `PROJECT_ID` with the project ID.
     * `SERVICE_ACCOUNT` with the email address of the service account you want to associate with the repository.



###  API 

  1. To update the repository service account using a REST call, run the following command:
         
         curl --request PATCH \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_ID?updateMask=serviceAccount \
             -d '{"serviceAccount": "SERVICE_ACCOUNT"}'
         

Replace the following:

     * `PROJECT_ID` with the project ID.
     * `REGION` with the region.
     * `REPOSITORY_ID` with the repository ID.
     * `SERVICE_ACCOUNT` with the service account email.



## What's next

  * [Grant users repository access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access)
  * [Use Git source code management](https://docs.cloud.google.com/secure-source-manager/docs/use-git) with Secure Source Manager.
  * [List and view repositories](https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories) in the Secure Source Manager web interface.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
