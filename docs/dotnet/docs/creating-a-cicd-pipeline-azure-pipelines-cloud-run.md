---
url: https://docs.cloud.google.com/dotnet/docs/creating-a-cicd-pipeline-azure-pipelines-cloud-run/
title: Creating a CI/CD pipeline with Azure Pipelines and Cloud Run \u00a0|\u00a0 .NET \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:57.125956+00:00
---

# Creating a CI/CD pipeline with Azure Pipelines and Cloud Run  |  .NET  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/creating-a-cicd-pipeline-azure-pipelines-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Creating a CI/CD pipeline with Azure Pipelines and Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to use [Azure Pipelines](https://azure.microsoft.com/en-au/services/devops/pipelines/), [Cloud Run](https://docs.cloud.google.com/run), and [Container Registry](https://docs.cloud.google.com/container-registry) to create a continuous integration/continuous deployment (CI/CD) pipeline for an ASP.NET MVC Core web application.

The CI/CD pipeline uses two Google Cloud projects, one for development and one for production, as the following diagram shows.

![Architecture of how the Azure build and release pipelines interact with the Google Cloud production and development pipelines.](https://docs.cloud.google.com/static/architecture/images/creating-a-cicd-pipeline-azure-pipelines-cloud-run-architecture.svg)

At the beginning of the pipeline, developers commit changes to the example codebase. This action triggers the pipeline to create a release and to deploy it to Cloud Run in the development cluster. A release manager then promotes the release so that it's deployed to the production project.

This tutorial is intended for developers and DevOps engineers. It assumes that you have basic knowledge of .NET, Azure Pipelines, Cloud Run, and `git`. To complete this tutorial, you need administrative access to an Azure DevOps account.

## Objectives

  * Connect Artifact Registry to Azure Pipelines for publishing Docker images.
  * Prepare a [.NET sample app](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/master/applications/clouddemo/netcore) for deployment into Cloud Run.
  * Set up authentication between Azure Pipelines and Google Cloud.
  * Use Azure Pipelines release management to orchestrate Cloud Run deployments.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run](https://docs.cloud.google.com/run/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

Check the [Azure DevOps pricing page](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) for any fees that might apply to using Azure DevOps.

## Before you begin

You use two separate projects in this tutorial, one for development and one for production. Using separate projects lets you test releases before deploying them to production and also lets you individually manage Identity and Access Management (IAM) roles and permissions.

  1. Create a Google Cloud project for development. The tutorial refers to this project as the _development project_.
  2. Create a Google Cloud project for production. The tutorial refers to this project as the _production project_.
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have an Azure DevOps account and that you have administrator access to it. If you don't yet have an Azure DevOps account, you can sign up on the [Azure DevOps home page](https://go.microsoft.com/fwlink/?LinkId=307137).



### Create an Azure DevOps project

You use Azure DevOps to manage the source code, run builds and tests, and orchestrate the deployment to Cloud Run. To begin, you create a project in your Azure DevOps account.

  1. Go to the Azure DevOps home page (https://dev.azure.com/YOUR_AZURE_DEVOPS_ACCOUNT_NAME).
  2. Click **New Project**.
  3. Enter a project name, such as `CloudDemo`.
  4. Set **Visibility** to **Private** , and then click **Create project**.
  5. After you create the project, in the menu on the left, click **Repos**.
  6. Click **Import** to fork the `dotnet-docs-samples` repository from GitHub, and then set the following values: 
     * **Repository type** : `Git`
     * **Clone URL** : `https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git`
  7. Click **Import**.

When the import process is done, you see the source code of the `dotnet-docs-samples` repository.




## Connecting Azure Pipelines to Artifact Registry

Before you can set up continuous integration for the `CloudDemo` app, you must connect Azure Pipelines to Artifact Registry. This connection allows Azure Pipelines to publish container images to Artifact Registry.

### Set up a service account for publishing images

Create a [Google Cloud service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your production project:

  1. In the Google Cloud console, switch to the production project.
  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Initialize the following environment variables:
         
         DEV_PROJECT_ID=DEV_PROJECT_ID
         PROD_PROJECT_ID=PROD_PROJECT_ID
         

Replace the following:

     * `DEV_PROJECT_ID`: the project ID of your development project
     * `PROD_PROJECT_ID`: the project ID of your production project
  4. Enable the Artifact Registry API in the production project:
         
         gcloud services enable artifactregistry.googleapis.com \
             --project=$PROD_PROJECT_ID
         

  5. Create an Artifact Registry repository to store Docker your images:
         
         gcloud artifacts repositories create docker  \
             --project=$PROD_PROJECT_ID \
             --repository-format=docker \
             --location REGION
         

Replace `REGION` with the region of your Artifact Registry repository, for example `us-central1`.

  6. Create a service account that Azure Pipelines uses to publish Docker images:
         
         gcloud iam service-accounts create azure-pipelines-publisher \
             --display-name="Azure Pipelines Publisher" \
             --project=$PROD_PROJECT_ID
         

  7. Grant the [Artifact Registry Writer role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) (`roles/artifactregistry.writer`) to the service account to allow Azure Pipelines to push to Artifact Registry:
         
         AZURE_PIPELINES_PUBLISHER=azure-pipelines-publisher@$PROD_PROJECT_ID.iam.gserviceaccount.com
         
         gcloud projects add-iam-policy-binding $PROD_PROJECT_ID \
             --member serviceAccount:$AZURE_PIPELINES_PUBLISHER \
             --role roles/artifactregistry.writer \
             --project=$PROD_PROJECT_ID
         

  8. Generate a service account key:
         
         gcloud iam service-accounts keys create azure-pipelines-publisher.json \
             --iam-account $AZURE_PIPELINES_PUBLISHER \
             --project=$PROD_PROJECT_ID
         
         tr -d '\n' < azure-pipelines-publisher.json > azure-pipelines-publisher-oneline.json
         

  9. View the content of the service account key file:
         
         echo $(<azure-pipelines-publisher-oneline.json)
         

You need the service account key in one of the following steps.




### Create a service connection for Artifact Registry

In Azure Pipelines, create a new service connection for Artifact Registry:

  1. In the Azure **DevOps** menu, select **Project settings** , and then select **Pipelines** > **Service connections**.
  2. Click **Create service connection**.
  3. From the list, select **Docker Registry** , and then click **Next**.
  4. In the dialog, enter values for the following fields:

     * **Registry type** : **Others**
     * **Docker Registry** : `https://REGION-docker.pkg.dev/PROD_PROJECT_ID/docker/`

Replace the following:

       * `REGION`: the region of your Artifact Registry repository
       * `PROD_PROJECT_ID`: the name of your production project
     * **Docker ID** : `_json_key`

     * **Password** : Paste the content of `azure-pipelines-publisher-oneline.json`.

     * **Service connection name** : `gcr-tutorial`

  5. Click **Save** to create the connection.




## Building continuously

You can now use Azure Pipelines to set up continuous integration. For each commit that's pushed to the Git repository, Azure Pipelines builds the code and packages the build artifacts into a Docker container. The container is then published to Artifact Registry.

The repository already contains the following Dockerfile:
    
    
    #
    # Copyright 2020 Google LLC
    #
    # Licensed to the Apache Software Foundation (ASF) under one
    # or more contributor license agreements.  See the NOTICE file
    # distributed with this work for additional information
    # regarding copyright ownership.  The ASF licenses this file
    # to you under the Apache License, Version 2.0 (the
    # "License"); you may not use this file except in compliance
    # with the License.  You may obtain a copy of the License at
    # 
    #   http://www.apache.org/licenses/LICENSE-2.0
    # 
    # Unless required by applicable law or agreed to in writing,
    # software distributed under the License is distributed on an
    # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    # KIND, either express or implied.  See the License for the
    # specific language governing permissions and limitations
    # under the License.
    #
    
    FROM mcr.microsoft.com/dotnet/aspnet:6.0
    EXPOSE 8080
    
    #------------------------------------------------------------------------------
    # Copy publishing artifacts.
    #------------------------------------------------------------------------------
    
    WORKDIR /app
    COPY CloudDemo.MvcCore/bin/Release/net6.0/publish/ /app/
    
    ENV ASPNETCORE_URLS=http://0.0.0.0:8080
    
    #------------------------------------------------------------------------------
    # Run application in Kestrel.
    #------------------------------------------------------------------------------
    
    ENTRYPOINT ["dotnet", "CloudDemo.MvcCore.dll"]

You now create a new pipeline that uses YAML syntax:

  1. Using Visual Studio or a command-line `git` client, [clone your new Git repository](https://docs.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops&tabs=visual-studio).
  2. In the root of the repository, create a file named `azure-pipelines.yml`.
  3. Copy the following code into the file:
         
         resources:
         - repo: self
           fetchDepth: 1
         pool:
           vmImage: ubuntu-22.04
         trigger:
         - master
         variables:
           TargetFramework: 'net6.0'
           BuildConfiguration: 'Release'
           DockerImageName: 'PROD_PROJECT_ID/docker/CloudDemo'
         steps:
         - task: DotNetCoreCLI@2
           displayName: Publish
           inputs:
             projects: 'applications/clouddemo/netcore/CloudDemo.MvcCore.sln'
             publishWebProjects: false
             command: publish
             arguments: '--configuration $(BuildConfiguration) --framework=$(TargetFramework)'
             zipAfterPublish: false
             modifyOutputPath: false
         - task: PublishBuildArtifacts@1
           displayName: 'Publish Artifact'
           inputs:
             PathtoPublish: '$(build.artifactstagingdirectory)'
         - task: Docker@2
           displayName: 'Login to Container Registry'
           inputs:
             command: login
             containerRegistry: 'gcr-tutorial'
         - task: Docker@2
           displayName: 'Build and push image'
           inputs:
             Dockerfile: 'applications/clouddemo/netcore/Dockerfile'
             command: buildAndPush
             repository: '$(DockerImageName)'

Replace `PROJECT_ID` with the name of your production project, and then save the file.

Because Cloud Run is a Linux-based environment, the pipeline uses Linux-based build agents.

  4. Commit your changes and push them to Azure Pipelines.

###  Visual Studio 

     1. Open Team Explorer and click the **Home** icon.
     2. Click **Changes**.
     3. Enter a commit message like `Add pipeline definition`.
     4. Click **Commit All and Push**.

###  Command line 

     1. Stage all modified files:
            
            git add -A
            

     2. Commit the changes to the local repository:
            
            git commit -m "Add pipeline definition"
            

     3. Push the changes to Azure DevOps:
            
            git push
            

  5. In the Azure DevOps menu, select **Pipelines** and then click **Create Pipeline**.

  6. Select **Azure Repos Git**.

  7. Select your repository.

  8. On the **Review your pipeline YAML** page, click **Run**.

A new build is triggered. It might take about two minutes for the build to complete.

  9. To verify that the image has been published to Artifact Registry, switch to your production project in the Google Cloud console, select **Artifact Registry** > **docker** , and then click **CloudDemo**.

A single image and the tag of this image are displayed. The tag corresponds to the numeric ID of the build that was run in Azure Pipelines.




## Deploying continuously

With Azure Pipelines automatically building your code and publishing Docker images for each commit, you can now turn your attention to deployment.

Unlike some other continuous integration systems, Azure Pipelines distinguishes between building and deploying, and it provides a specialized set of tools labeled Release Management for all deployment-related tasks.

Azure Pipelines Release Management is built around these concepts:

  * A _release_ refers to a set of artifacts that make up a specific version of your app and that are usually the result of a build process.
  * _Deployment_ refers to the process of taking a release and deploying it into a specific environment.
  * A deployment performs a set of _tasks_ , which can be grouped in jobs.
  * _Stages_ let you segment your pipeline and can be used to orchestrate deployments to multiple environments—for example development and testing environments.



You set up your release pipeline to be triggered whenever a new build is completed. The pipeline consists of two stages: development and production. In each stage, the release pipeline uses the Docker image that the build pipeline produces, and then the pipeline deploys it to Cloud Run.

The build pipeline that you configured previously tags each Docker image with the build ID before publishing it to Artifact Registry. Therefore, in the release pipeline, you use the `$BUILD_BUILDID` variable to identify the right Docker image to deploy.

### Configure Cloud Run

[Cloud Run](https://docs.cloud.google.com/run) is a fully managed, serverless environment, so you don't need to provision any infrastructure. To help keep your Cloud Run deployments secure, you need to set up IAM.

Deploying and running a Cloud Run service involves multiple identities, as the following diagram shows.

![Identities that run as service accounts in a Cloud Run deployment.](https://docs.cloud.google.com/static/architecture/images/creating-a-cicd-pipeline-azure-pipelines-cloud-run-identities.svg)

Each of these identities is implemented as a service account and is used for a specific purpose, as the following table describes.

**Service account** | **Used by** | **Purpose** | **Roles required**  
---|---|---|---  
Azure Pipelines Publisher | Build pipeline | Publish Docker images to Artifact Registry | `roles/artifactregistry.writer` (production project only)  
Azure Pipelines Deployer | Release pipeline | Initiate Cloud Run deployments | `roles/run.admin`  
|  | Launch CloudDemo service | `roles/iam.serviceAccountUser`  
Cloud Run service agent | Cloud Run | Pull Docker images from Artifact Registry | `roles/artifactregistry.reader` (production project only)  
CloudDemo runner ([runtime service account](https://docs.cloud.google.com/run/docs/securing/service-identity?hl=en#runtime_service_account)) | CloudDemo service | Access resources on Google Cloud | None  
**Note:** The CloudDemo app does not use any Google Cloud services such as Cloud Storage, Cloud Logging, or Cloud SQL. But if it did, you could assign the necessary roles to the _CloudDemo runner_ service account.

You created and configured the Azure Pipelines Publisher service account. In the following sections, you create and configure the remaining service accounts.

#### Configure the Cloud Run service account

  1. Open Cloud Shell.

  2. Initialize the following environment variables:
         
         DEV_PROJECT_ID=DEV_PROJECT_ID
         PROD_PROJECT_ID=PROD_PROJECT_ID
         

Replace the following:

     * `DEV_PROJECT_ID`: the project ID of your development project
     * `PROD_PROJECT_ID`: the project ID of your production project
  3. Enable the Cloud Run and Compute Engine APIs in both the development and product projects:
         
         gcloud services enable run.googleapis.com --project=$DEV_PROJECT_ID
         gcloud services enable run.googleapis.com --project=$PROD_PROJECT_ID
         

Enabling these APIs causes the Cloud Run service agent accounts to be created in your projects.

  4. Grant the two Cloud Run service agent accounts access to Artifact Registry in the production project where your Docker images are stored:
         
         DEV_PROJECT_NUMBER=$(gcloud projects describe $DEV_PROJECT_ID \
             --format='value(projectNumber)')
         PROD_PROJECT_NUMBER=$(gcloud projects describe $PROD_PROJECT_ID \
             --format='value(projectNumber)')
         
         gcloud projects add-iam-policy-binding $PROD_PROJECT_ID \
             --member=serviceAccount:service-$DEV_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com \
             --role roles/artifactregistry.reader
         
         gcloud projects add-iam-policy-binding $PROD_PROJECT_ID \
             --member=serviceAccount:service-$PROD_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com \
             --role roles/artifactregistry.reader
         




#### Configure the CloudDemo runner account

You can now configure the CloudDemo runner account, which is a custom [runtime service account](https://docs.cloud.google.com/run/docs/securing/service-identity#runtime_service_account) for the CloudDemo service:

  * Create a service account named `CloudDemo-runner`:
        
        gcloud iam service-accounts create clouddemo-runner \
            --display-name="CloudDemo Runner" \
            --project=$DEV_PROJECT_ID
        
        gcloud iam service-accounts create clouddemo-runner \
            --display-name="CloudDemo Runner" \
            --project=$PROD_PROJECT_ID
        
        DEV_CLOUDDEMO_RUNNER=clouddemo-runner@$DEV_PROJECT_ID.iam.gserviceaccount.com
        
        PROD_CLOUDDEMO_RUNNER=clouddemo-runner@$PROD_PROJECT_ID.iam.gserviceaccount.com
        




#### Configure the Azure Pipelines Deployer account

Finally, create and configure the Azure Pipelines Deployer account, which the Azure release pipeline uses to deploy to Cloud Run.

  1. Create a service account named `azure-pipelines-deployer`:
         
         gcloud iam service-accounts create azure-pipelines-deployer \
             --display-name="Azure Pipelines Deployer" \
             --project=$PROD_PROJECT_ID
         
         AZURE_PIPELINES_DEPLOYER=azure-pipelines-deployer@$PROD_PROJECT_ID.iam.gserviceaccount.com
         

  2. Assign [the required IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) to deploy new Cloud Run services or revisions in the development project:
         
         gcloud projects add-iam-policy-binding $DEV_PROJECT_ID \
             --member serviceAccount:$AZURE_PIPELINES_DEPLOYER \
             --role roles/run.admin
         
         gcloud iam service-accounts add-iam-policy-binding \
             $DEV_CLOUDDEMO_RUNNER \
             --member=serviceAccount:$AZURE_PIPELINES_DEPLOYER \
             --role="roles/iam.serviceAccountUser" \
             --project=$DEV_PROJECT_ID
         

  3. Assign the same set of roles for the production project:
         
         gcloud projects add-iam-policy-binding $PROD_PROJECT_ID \
             --member serviceAccount:$AZURE_PIPELINES_DEPLOYER \
             --role roles/run.admin
         
         gcloud iam service-accounts add-iam-policy-binding \
             $PROD_CLOUDDEMO_RUNNER \
             --member=serviceAccount:$AZURE_PIPELINES_DEPLOYER \
             --role="roles/iam.serviceAccountUser" \
             --project=$PROD_PROJECT_ID
         

  4. Generate a service account key:
         
         gcloud iam service-accounts keys create azure-pipelines-deployer.json \
             --iam-account=$AZURE_PIPELINES_DEPLOYER \
             --project=$PROD_PROJECT_ID
         
         cat azure-pipelines-deployer.json | base64 -w 0
         

You use the output of this command when you configure the release pipeline.




### Configure the release pipeline

You can now return to Azure Pipelines to automate the deployment, which includes the following steps:

  * Deploying to the development environment.
  * Requesting manual approval before initiating a deployment to the production environment.
  * Deploying to the production environment.



#### Create a release definition

First, create a release definition:

  1. In the Azure DevOps menu, select **Pipelines** > **Releases**.
  2. Click **New pipeline**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Development`.
  5. At the top of the screen, name the pipeline `CloudDemo`.
  6. In the pipeline diagram, next to **Artifacts** , click **Add**.
  7. Select **Build** , and then add the following settings: 
     * **Source type** : **Build**
     * **Source (build pipeline)** : Select the build definition (there should be only one option)
     * **Default version** : **Latest**
     * **Source Alias** : `build`
  8. Click **Add**.
  9. On the **Artifact** box, click **Continuous deployment trigger** (the lightning bolt icon) to add a deployment trigger.
  10. Under **Continuous deployment trigger** , set the switch to **Enabled**.
  11. Click **Save**.
  12. Enter a comment if you want, and then confirm by clicking **OK**.

The pipeline displays similar to the following.

![Pipeline view of automated deployment setup.](https://docs.cloud.google.com/static/architecture/images/creating-a-cicd-pipeline-azure-pipelines-cloud-run-pipeline.png)




#### Deploy to the development project

With the release definition created, you can now configure the Cloud Run deployment to the development project.

  1. In the menu, switch to the **Tasks** tab.
  2. Click **Agent job**.
  3. Set **Agent specification** to **ubuntu-22.04**.
  4. Next to **Agent job** , click **Add a task to agent job** add to add a step to the phase.
  5. Select the **Command line** task and click **Add**.
  6. Click the newly added task and configure the following settings:

     1. **Display name** : `Deploy image to development project`
     2. **Script** :
            
            gcloud auth activate-service-account \
                --quiet \
                --key-file <(echo $(ServiceAccountKey) | base64 -d) && \
            gcloud run deploy clouddemo \
                --quiet \
                --service-account=clouddemo-runner@$(CloudRun.ProjectId.Development).iam.gserviceaccount.com \
                --allow-unauthenticated \
                --image=$(CloudRun.Region)-docker.pkg.dev/$(ContainerRegistry.ProjectId)/docker/clouddemo:$BUILD_BUILDID \
                --platform=managed \
                --region=$(CloudRun.Region) \
                --project=$(CloudRun.ProjectId.Development)
            

This command obtains a service account key from an environment variable and then uses the gcloud CLI to deploy the application to Cloud Run. The gcloud CLI is available by default on Azure Pipelines agents.

  7. Switch to the **Variables** tab and add the following variables.

**Name** | **Value** | **Secret**  
---|---|---  
`ServiceAccountKey` | Service account key created for `azure-pipelines-deployer` earlier. | Yes  
`ContainerRegistry.ProjectId` | Project ID of your production project. |   
`CloudRun.Region` | Region you selected earlier to deploy Artifact Registry resources in. |   
`CloudRun.ProjectId.Development` | Project ID of your development project. |   
`CloudRun.ProjectId.Production` | Project ID of your production project. |   
  8. Click **Save**.

  9. Enter a comment if you want, and then confirm by clicking **OK**.




#### Deploy to the production cluster

Finally, you configure the deployment to the production project:

  1. In the menu, switch to the **Pipeline** tab.
  2. In the Stages box, select **Add** > **New stage**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Production`.
  5. Click the lightning bolt icon of the newly created stage.
  6. Configure the following settings:

     1. **Select trigger** : **After stage**
     2. **Stages** : **Development**
     3. **Pre-deployment approvals** : (enabled)
     4. **Approvers** : Select your username.

The pipeline displays a view similar to the following.

![Pipeline view of cluster deployment setup.](https://docs.cloud.google.com/static/architecture/images/creating-a-cicd-pipeline-azure-pipelines-cloud-run-pipeline2.png)

  7. Switch to the **Tasks** tab.

  8. Hold the mouse over the **Tasks** tab and select **Tasks** > **Production**.

  9. Click **Agent job**.

  10. Set **Agent specification** to **ubuntu-22.04**.

  11. Click **Add a task to agent job** add to add a step to the phase.

  12. Select the **Command line** task, and then click **Add**.

  13. Click the newly added task and configure the following settings:

     1. **Display name** : `Deploy image to production project`
     2. **Script** :
            
            gcloud auth activate-service-account \
                --quiet \
                --key-file <(echo $(ServiceAccountKey) | base64 -d) && \
            gcloud run deploy clouddemo \
                --quiet \
                --service-account=clouddemo-runner@$(CloudRun.ProjectId.Production).iam.gserviceaccount.com \
                --allow-unauthenticated \
                --image=$(CloudRun.Region)-docker.pkg.dev/$(ContainerRegistry.ProjectId)/docker/clouddemo:$BUILD_BUILDID \
                --platform=managed \
                --region=$(CloudRun.Region) \
                --project=$(CloudRun.ProjectId.Production)
            

  14. Click **Save**.

  15. Enter a comment if you want, and then confirm by clicking **OK**.




### Run the pipeline

Now that you've configured the entire pipeline, you can test it by performing a source code change:

  1. On your local computer, open the file `applications\clouddemo\netcore\CloudDemo.MvcCore\Views\Home\Index.cshtml` from the Git repository you cloned earlier.
  2. Change the value of `ViewBag.Title` from `Home Page` to `Home Page Cloud Run`.
  3. Commit your changes, and then push them to Azure Pipelines.

###  Visual Studio 

     1. Open Team Explorer and click the **Home** icon.
     2. Click **Changes**.
     3. Enter a commit message like `Change site title`.
     4. Click **Commit All and Push**.

###  Command line 

     1. Stage all modified files:
            
            git add -A
            

     2. Commit the changes to the local repository:
            
            git commit -m "Change site title"
            

     3. Push the changes to Azure Pipelines:
            
            git push
            

  4. In the Azure DevOps menu, select **Pipelines**. A build is triggered.

  5. After the build is finished, select **Pipelines** > **Releases**. A release process is initiated.

  6. Click **Release-1** to open the details page, and wait for the status of the **Development** stage to switch to **Succeeded**.

  7. In the Google Cloud console, switch to the development project.

  8. In the menu, select **Compute** > **Cloud Run**.

The **clouddemo** service is deployed successfully.

![Deployment status in Cloud Run.](https://docs.cloud.google.com/static/architecture/images/creating-a-cicd-pipeline-azure-pipelines-cloud-run-status.png)

  9. Click **clouddemo** to view more details.

A URL is displayed which shows that Cloud Run provisioned the service.

  10. Open the URL in a new browser tab to verify that the CloudDemo app is deployed and uses the custom title.

  11. In Azure Pipelines, click **Approve** (adjacent to the **Production** stage) to promote the deployment to the production environment.

  12. (Optional) Enter a comment.

  13. Confirm by clicking **Approve** , and wait for the status of the **Production** environment to switch to **Succeeded**.

  14. In the Google Cloud console, switch to the production project.

  15. In the menu, select **Compute** > **Cloud Run**.

The **clouddemo** service is deployed to the production project.

  16. Click **clouddemo** to view more details.

A URL displays which shows that Cloud Run provisioned the service.

  17. Open the URL in a new browser tab to verify that the CloudDemo app is deployed to production and that it uses the custom title.




## Clean up

To avoid incurring further costs after you complete this tutorial, delete the entities that you created.

### Delete the Azure Pipelines project

To delete the Azure Pipelines project, see the [Azure DevOps Services documentation](https://docs.microsoft.com/en-us/vsts/accounts/delete-team-project?view=vsts). Deleting the Azure Pipelines project causes all source code changes to be lost.

### Delete the Google Cloud development and production projects

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Configure a custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) for your Cloud Run service.
  * Learn how you can use Azure Pipelines to [deploy the same app to Google Kubernetes Engine](https://docs.cloud.google.com/solutions/creating-cicd-pipeline-vsts-kubernetes-engine) instead.
  * Read more about [deploying Deploying .NET apps on Google Cloud](https://docs.cloud.google.com/solutions/deploy-dotnet-applications).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
