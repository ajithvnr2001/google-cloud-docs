---
url: https://docs.cloud.google.com/app-lifecycle-manager/create-upload-blueprint/
title: Create and upload a blueprint \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:09:56.512184+00:00
---

# Create and upload a blueprint  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/create-upload-blueprint/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Create and upload a blueprint Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A blueprint is a Terraform configuration packaged as an Open Container Initiative (OCI) image. The Terraform configuration specifies the infrastructure and application that App Lifecycle Manager deploys onto Google Cloud.

This page describes how to create an OCI image from existing Terraform configurations, and how to upload these to App Lifecycle Manager.

For details about these Terraform configurations, see [Blueprints in App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/blueprints).

## Before you begin

  1. Ensure you have [enabled App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/enable-service).
  2. In the project that you are using for App Lifecycle Manager, ensure you have an Artifact Registry repository that is set to the Docker format. For more details, see [Create a repository for App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/create-repository).
  3. Identify the Terraform configurations that you want to deploy using App Lifecycle Manager. 
     * For details about how to decide how to model the App offering using blueprints, see [Determine the model of the App offering](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering#saas-model)
     * For details about the requirements for the Terraform configuration, see [Blueprint requirements](https://docs.cloud.google.com/app-lifecycle-manager/blueprints#blueprint_requirements).



## Create and upload the blueprint

To deploy the Terraform configurations onto Google Cloud using App Lifecycle Manager, you need to:

  * Package the Terraform configurations into OCI images. These OCI images are called blueprints.
  * Put these OCI images in the Artifact Registry repository you identified or set up.



Depending on how you choose to create and upload the blueprint, you can do all of the steps manually, or App Lifecycle Manager can perform some of the steps.

You can create the OCI image and upload it to the repository using any of the following methods:

  * Upload a zip archive that contains the Terraform configuration. App Lifecycle Manager uses the zip archive to create the OCI image.

See details in the following section: Upload a zip archive.

  * Connect a Git repository that has the Terraform files. App Lifecycle Manager uses the files to create the OCI image. App Lifecycle Manager then uses Cloud Build to build and upload the blueprint whenever you update your repository.

See details in the following section: Connect to a Git repository.

  * Build the OCI image locally and push the image to the repository in Artifact Registry.

See details in the following section: Build and push an image manually.

  * Automate the creation and push of the OCI image to a repository in Artifact Registry. Automating this process helps you incorporate App Lifecycle Manager into a CI/CD pipeline.

See details in the following section: Automate blueprint creation.




### Upload a zip archive

You can create a zip archive of the Terraform files. You upload this archive to App Lifecycle Manager when you create a release or a unit kind. App Lifecycle Manager uses the zip archive to create the required OCI image.

To provide a blueprint using a zip archive, do the following:

  1. Navigate to your Terraform project directory.
  2. Create a zip archive containing the Terraform configuration. 
     * Ensure that: 
       * The zip archive contains only your Terraform files. For example, `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, and modules.
       * The zip archive _does not_ contain unnecessary files, for example `.git` directories, or a dockerfile.
     * The command to create a zip archive might look similar to this: `zip terraform-files.zip main.tf outputs.tf variables.tf versions.tf`
  3. Upload the zip archive when you create a release, or when you [create a unit kind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).



App Lifecycle Manager uses the zip archive to create the required OCI image, and pushes it to the Artifact Registry repository.

### Connect to a Git repository

If you store your Terraform configuration in a Git repository, then you can connect App Lifecycle Manager to this repository. App Lifecycle Manager uses the files to create the required OCI image when you create a unit kind or create a release.

To provide a blueprint using a Git repository, do the following:

  1. Ensure your Terraform files are located in the root directory of your Git repository.
  2. Connect your Git repository to App Lifecycle Manager when you create a release, or when you [create a unit kind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).



App Lifecycle Manager uses Developer Connect to connect to the Git repository. For more details about Developer Connect, see the [Developer Connect documentation](https://docs.cloud.google.com/developer-connect/docs/overview).

App Lifecycle Manager uses the Terraform files from the Git repository to create the required OCI image, and pushes it to the Artifact Registry repository.

This integration automates the blueprint creation process whenever you update your Terraform code in your repository. When there are changes in the linked Git repository, App Lifecycle Manager uses the changed files to automatically build a new OCI image and then pushes it to the Artifact Registry repository.

### Build and push an image manually

This method gives you fine-grained control over the blueprint creation process.

To create a blueprint manually, do the following steps:

  1. In the root directory of your Terraform files, create a file named `Dockerfile` with the following content:
         
         # syntax=docker/dockerfile:1-labs
         FROM scratch
         COPY --exclude=Dockerfile --exclude=.git --exclude=.gitignore . /
         

This `Dockerfile` uses a minimal base image (`scratch`). Consider including `dockerignore` to the command to exclude files that are not relevant, such as:

     * the `Dockerfile` itself
     * the `.git` directory
     * the `.gitignore` file
  2. If you don't have a Docker builder, then create a `docker-container` builder using `docker buildx` by using the following command:
         
         docker buildx create --name container --driver=docker-container
         

  3. Run the following `docker buildx build` command from your Terraform directory to build and push the blueprint to Artifact Registry:
         
         IMAGE_NAME=us-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/IMAGE_NAME:TAG
         ENGINE_TYPE=inframanager
         ENGINE_VERSION=TERRAFORM_VERSION
         
         docker buildx build -t $IMAGE_NAME \
           --builder=container \
           --push \
           --annotation "com.easysaas.engine.type=$ENGINE_TYPE" \
           --annotation "com.easysaas.engine.version=$ENGINE_VERSION" \
           --provenance=false .
         

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `REPOSITORY_NAME`: The name of your Artifact Registry repository.
     * `IMAGE_NAME`: A name for your blueprint image.
     * `TAG`: A tag for your image version (for example, `latest`, or `v1.0.0`). Choosing a descriptive tag helps you effectively manage versions of the blueprint.
     * `TERRAFORM_VERSION`: the supported version of Terraform to use. See [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of versions supported by Infrastructure Manager.

A command might look similar to the following example:
    
    IMAGE_NAME=us-docker.pkg.dev/saas-docs-testing/blueprints-repo/my-terraform-blueprint:v1.0.0
    ENGINE_TYPE=inframanager
    ENGINE_VERSION=1.5.7
    
    docker buildx build -t $IMAGE_NAME \
      --builder=container \
      --push \
      --annotation "com.easysaas.engine.type=$ENGINE_TYPE" \
      --annotation "com.easysaas.engine.version=$ENGINE_VERSION" \
      --provenance=false .
    




The OCI image is in the Artifact Registry repository.

To use this image with App Lifecycle Manager, select this image when you create a release, or when you [create a unit kind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).

### Automate blueprint creation

You can automate the creation of the OCI image and the push to Artifact Registry by using Cloud Build. You can set up a trigger so that whenever the Terraform code is changed, the OCI image is automatically built and pushed to Artifact Registry.

To set up this automation, do the following:

  1. In the root of your Terraform repository, create a `cloudbuild.yaml` file with the following configuration:
         
         steps:
         - id: 'Create Dockerfile'
           name: 'bash'
           args: ['-c', 'echo -e "# syntax=docker/dockerfile:1-labs\nFROM scratch\nCOPY --exclude=Dockerfile.Blueprint --exclude=.git --exclude=.gitignore . /" > Dockerfile.Blueprint']
         - id: 'Create docker-container driver'
           name: 'docker'
           args: ['buildx', 'create', '--name', 'container', '--driver=docker-container']
         - id: 'Build and Push docker image'
           name: 'docker'
           args: ['buildx', 'build', '-t', '${_IMAGE_NAME}', '--builder=container', '--push', '--annotation', 'com.easysaas.engine.type=${_ENGINE_TYPE}','--annotation', 'com.easysaas.engine.version=${_ENGINE_VERSION}', '--provenance=false','-f', 'Dockerfile.Blueprint', '.']
         serviceAccount: '${_SERVICE_ACCOUNT}'
         substitutions:
           _SERVICE_ACCOUNT: 'projects/PROJECT_ID/serviceAccounts/CLOUD_BUILD_SERVICE_ACCOUNT'
           _IMAGE_NAME: 'us-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/IMAGE_NAME:latest'
           _ENGINE_TYPE: 'inframanager'
           _ENGINE_VERSION: 'TERRAFORM_VERSION'
         options:
           logging: CLOUD_LOGGING_ONLY
         

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `CLOUD_BUILD_SERVICE_ACCOUNT`: The full name of your Cloud Build service account. For more details about App Lifecycle Manager and service accounts, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts)
     * `REPOSITORY_NAME`: The name of your Artifact Registry repository.
     * `IMAGE_NAME`: A name for your blueprint image.
     * `TAG`: A tag for your image version (for example, `latest`, or `v1.0.0`). Choosing a descriptive tag helps you effectively manage versions of the blueprint.
     * `TERRAFORM_VERSION`: the supported version of Terraform to use. See [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of versions supported by Infrastructure Manager.
  2. Start the Cloud Build job using the `gcloud builds submit` command from the directory containing your `cloudbuild.yaml` file:
         
         gcloud builds submit --config=cloudbuild.yaml --substitutions=_IMAGE_NAME='us-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/IMAGE_NAME:TAG'
         

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `REPOSITORY_NAME`: The name of your Artifact Registry repository.
     * `IMAGE_NAME`: A name for your blueprint image
     * `TAG`: A tag for your image version (for example, `latest`, or `v1.0.0`). Choosing a descriptive tag helps you effectively manage versions of the blueprint.
  3. You can set up a trigger so that whenever the Terraform code is changed, the OCI image is automatically built and pushed to Artifact Registry. For details, see [Create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




The OCI image is now in the Artifact Registry repository.

To use this image with App Lifecycle Manager, select this image when you create a release, or when you [create a unit kind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).

## What's next

  * To understand more about App Lifecycle Manager, see [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * To learn more about blueprints, see [Blueprints in App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/blueprints).
  * To get started with App Lifecycle Manager, begin with [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
