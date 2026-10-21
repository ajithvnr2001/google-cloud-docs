---
url: https://docs.cloud.google.com/dotnet/docs/creating-cicd-pipeline-vsts-compute-engine/
title: Creating a CI/CD pipeline with Azure Pipelines and Compute Engine \u00a0|\u00a0 .NET \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:04.693427+00:00
---

# Creating a CI/CD pipeline with Azure Pipelines and Compute Engine  |  .NET  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/creating-cicd-pipeline-vsts-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Creating a CI/CD pipeline with Azure Pipelines and Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2023-03-09 UTC

This tutorial shows how to use [Azure Pipelines](https://azure.microsoft.com/en-au/services/devops/pipelines/) and [Compute Engine](https://docs.cloud.google.com/compute) to create a continuous integration/continuous deployment (CI/CD) pipeline for an ASP.NET MVC web application. The application uses Microsoft Internet Information Services and runs on Windows Server.

The CI/CD pipeline uses two separate environments, one for testing and one for production.

At the beginning of the pipeline, developers commit changes to the example codebase. This action triggers the pipeline to build the application, package it as a zip file, and upload the zip file to Cloud Storage.

The package is then automatically released to the development environment by using a [rolling update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups). After the release has been tested, a release manager can then promote the release so that it's deployed into the production environment.

This tutorial is intended for developers and DevOps engineers. It assumes that you have basic knowledge of .NET Framework, Windows Server, IIS, Azure Pipelines, and Compute Engine. The tutorial also requires you to have administrative access to an Azure DevOps account.

## Objectives

  * Use Compute Engine [Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) to implement rolling deployments.
  * Set up a CI/CD pipeline in Azure Pipelines to orchestrate the building, creating, and deployment processes.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

Check the [Azure DevOps pricing page](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) for any fees that might apply to using Azure DevOps.

## Before you begin

It's usually advisable to use separate projects for development and production workloads so that identity and access management (IAM) roles and permissions can be granted individually. For the sake of simplicity, this tutorial uses a single project for the development and production environments.

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Compute Engine and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,storage.googleapis.com)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure you have an Azure DevOps account and have administrator access to it. If you don't yet have an Azure DevOps account, you can sign up on the [Azure DevOps home page](https://go.microsoft.com/fwlink/?LinkId=307137). 

**Note:** You can use either a command-line Git client or Visual Studio to follow this tutorial. If you use Visual Studio, make sure that it's connected to your Azure DevOps account.

### Create an Azure DevOps project

You use Azure DevOps to manage the source code, run builds and tests, and orchestrate the deployment to Compute Engine. To begin, you create a project in your Azure DevOps account.

  1. Go to the Azure DevOps home page (https://dev.azure.com/YOUR_AZURE_DEVOPS_ACCOUNT_NAME).
  2. Click **New Project**.
  3. Enter a project name, such as `CloudDemo`.
  4. Set **Visibility** to **Private** , and then click **Create**.
  5. After you create the project, in the menu on the left, click **Repos**.
  6. Click **Import** to fork the `dotnet-docs-samples` repository from GitHub, and then set the following values: 
     * **Repository type** : `Git`
     * **Clone URL** : `https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git`
  7. Click **Import**.

When the import process is done, you see the source code of the `dotnet-docs-samples` repository.

  8. In the menu, click **Repos > Branches**.

  9. Move the mouse over the `main` branch. A **...** button appears on the right.

  10. Click **... > Set as default branch**.




## Build continuously

You can now use Azure Pipelines to set up a build pipeline. For each commit that's pushed to the Git repository, Azure Pipelines builds the code, packages it into a zip file, and publishes the resulting package to internal Azure Pipelines storage.

Later, you configure a release pipeline that uses the packages from Azure Pipelines storage and deploys them to Compute Engine.

### Create a build definition

Create a new build definition in Azure Pipelines that uses YAML syntax:

  1. Using Visual Studio or a command-line `git` client, [clone your new Git repository](https://docs.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops&tabs=visual-studio).
  2. In the root of the repository, create a file named `azure-pipelines.yml`.
  3. Copy the following code and paste into the file:
         
         resources:
         - repo: self
           fetchDepth: 1
         trigger:
         - main
         variables:
           artifactName: 'CloudDemo.Mvc'
         jobs:
         - job: Build
           displayName: Build application
           condition: succeeded()
           pool:
             vmImage: windows-latest
             demands:
             - msbuild
             - visualstudio
           variables:
             Solution: 'applications/clouddemo/net4/CloudDemo.Mvc.sln'
             BuildPlatform: 'Any CPU'
             BuildConfiguration: 'Release'
             ArtifactName: 'CloudDemo.Web'
           steps:
           - task: NuGetCommand@2
             displayName: 'NuGet restore'
             inputs:
               restoreSolution: '$(Solution)'
           - task: VSBuild@1
             displayName: 'Build solution'
             inputs:
               solution: '$(Solution)'
               msbuildArgs: '/p:DeployOnBuild=true /p:WebPublishMethod=Package /p:PackageAsSingleFile=true /p:SkipInvalidConfigurations=true /p:PackageLocation="$(build.artifactstagingdirectory)\\"'
               platform: '$(BuildPlatform)'
               configuration: '$(BuildConfiguration)'
           - task: PublishBuildArtifacts@1
             displayName: 'Publish Artifact'
             inputs:
               PathtoPublish: '$(build.artifactstagingdirectory)/CloudDemo.Mvc.zip'
               ArtifactName: '$(ArtifactName)'

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

A new build is triggered. It might take about 2 minutes for the build to complete. At the end of the build, the application package `CloudDemo.Mvc.zip`, which contains all files of the web application, is available in the internal Azure Pipelines artifact storage area.




## Deploying continuously

Now that Azure Pipelines is automatically building your code for each commit, you can turn your attention toward deployment.

Unlike some other continuous integration systems, Azure Pipelines distinguishes between building and deploying, and it provides a specialized set of tools that are labeled Release Management for all deployment-related tasks.

Azure Pipelines Release Management is built around these concepts:

  * A _release_ refers to a set of artifacts that make up a specific version of your app and that are usually the result of a build process.
  * _Deployment_ refers to the process of taking a release and deploying it into a specific environment.
  * A deployment performs a set of _tasks_ , which can be grouped in jobs.
  * _Stages_ let you segment your pipeline and can be used to orchestrate deployments to multiple environments—for example, development and testing environments.



You set up your release pipeline to be triggered whenever a new build is completed. The pipeline consists of three stages:

  1. In the first stage, the pipeline takes the application package from the Azure Pipelines artifact storage area and publishes it to a Cloud Storage bucket so that the package is accessible by Compute Engine.
  2. In the second stage, the pipeline updates the development environment by using a [rolling update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).
  3. In the final stage, after approval, the pipeline updates the production environment by using a rolling update.



### Create a Cloud Storage bucket for build artifacts

Create a Cloud Storage bucket for storing application packages. Later, you configure Compute Engine so that new VM instances can automatically pull application packages from this bucket.

  1. In the Google Cloud console, switch to your newly created project.
  2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  3. To save time, set default values for your project ID and Compute Engine zone:
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/zone ZONE

Replace PROJECT_ID with the ID of your Google Cloud project, and replace ZONE with the name of the zone that you're going to use for creating resources. If you are unsure about which zone to pick, use `us-central1-a`.

Example:
         
         gcloud config set project devops-test-project-12345
         gcloud config set compute/zone us-central1-a

  4. Create a new Cloud Storage bucket for application packages:
         
         gcloud storage buckets create gs://$(gcloud config get-value core/project)-artifacts
         

If you don't want to keep the application packages of all builds, you might consider configuring an object lifecycle rule to delete files that are past a certain age.




### Set up a service account for Azure Pipelines

Create a [Google Cloud service account](https://docs.cloud.google.com/iam/docs/service-accounts) that Azure Pipelines can use to access your Google Cloud project.

  1. Create a service account for Azure Pipelines:
         
         AZURE_PIPELINES_SERVICE_ACCOUNT=$(gcloud iam service-accounts create azure-pipelines --format "value(email)")
         

  2. Grant the Storage Object Viewer (`roles/storage.objectViewer`) and Storage Object Creator (`roles/storage.objectCreator`) [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the `azure-pipelines` service account so that Azure Pipelines can upload application packages to Cloud Storage:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
             --member serviceAccount:$AZURE_PIPELINES_SERVICE_ACCOUNT \
             --role roles/storage.objectViewer
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
             --member serviceAccount:$AZURE_PIPELINES_SERVICE_ACCOUNT \
             --role roles/storage.objectCreator
         

  3. Grant the Compute Admin (`roles/compute.admin`) role to the `azure-pipelines` service account so that Azure Pipelines can manage VM instances:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
             --member serviceAccount:$AZURE_PIPELINES_SERVICE_ACCOUNT \
             --role roles/compute.admin
         

  4. Generate a service account key:
         
         gcloud iam service-accounts keys create azure-pipelines-key.json \
           --iam-account=$AZURE_PIPELINES_SERVICE_ACCOUNT
         
         cat azure-pipelines-key.json | base64 -w 0;echo
         
         rm azure-pipelines-key.json
         

You need the service account key in one of the following steps.




### Configure the development environment

Before you can configure the steps in Azure Pipelines to automate the deployment, you must prepare the development environment. This preparation includes creating a managed instance group that will manage the web server VM instances. It also includes creating an HTTP load balancer.

  1. In Cloud Shell, create a service account for the managed instance group:
         
         DEV_SERVICE_ACCOUNT=$(gcloud iam service-accounts create clouddemo-dev --format "value(email)")
         

  2. Grant the [Storage Object Viewer IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) (`roles/storage.objectViewer`) to the service account so that VM instances can download application packages from Cloud Storage:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
             --member serviceAccount:$DEV_SERVICE_ACCOUNT \
             --role roles/storage.objectViewer
         

  3. Grant the `azure-pipelines` service account permission to use the `clouddemo-dev` service account:
         
         gcloud iam service-accounts add-iam-policy-binding $DEV_SERVICE_ACCOUNT \
             --member serviceAccount:$AZURE_PIPELINES_SERVICE_ACCOUNT \
             --role roles/iam.serviceAccountUser
         

  4. Create an instance template that uses a standard Windows Server 2019 Core image. You will use this template only initially, because each build will produce a new template.
         
         gcloud compute instance-templates create clouddemo-initial \
             --machine-type n1-standard-2 \
             --image-family windows-2019-core \
             --image-project windows-cloud \
             --service-account $DEV_SERVICE_ACCOUNT \
             --scopes https://www.googleapis.com/auth/devstorage.read_only \
             --tags gclb-backend
         

  5. Create an HTTP health check. Because the application does not have a dedicated health check endpoint, you can query the path `/`.
         
         gcloud compute http-health-checks create clouddemo-dev-http \
             --check-interval=10s --unhealthy-threshold=10 \
             --request-path=/
         

  6. Create a managed instance group that's based on the initial instance template. For simplicity's sake, the following commands create a zonal managed instance group. However, you can use the same approach for regional managed instance groups that distribute VM instances across more than one zone.
         
         gcloud compute instance-groups managed create clouddemo-dev \
             --template=clouddemo-initial \
             --http-health-check=clouddemo-dev-http \
             --initial-delay=2m \
             --size=1 && \
         gcloud compute instance-groups set-named-ports clouddemo-dev --named-ports http:80
         

  7. Create a load balancer backend service that uses the HTTP health check and managed instance group that you created previously:
         
         gcloud compute backend-services create clouddemo-dev-backend \
             --http-health-checks clouddemo-dev-http \
             --port-name http --protocol HTTP --global && \
         gcloud compute backend-services add-backend clouddemo-dev-backend \
             --instance-group clouddemo-dev --global \
             --instance-group-zone=$(gcloud config get-value compute/zone)
         

  8. Create a load balancer frontend:
         
         gcloud compute url-maps create clouddemo-dev --default-service clouddemo-dev-backend && \
         gcloud compute target-http-proxies create clouddemo-dev-proxy --url-map=clouddemo-dev && \
         gcloud compute forwarding-rules create clouddemo-dev-fw-rule --global --target-http-proxy clouddemo-dev-proxy --ports=80
         

  9. Create a firewall rule that [allows the Google load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/http#firewall_rules) to send HTTP requests to instances that have been annotated with the `gclb-backend` tag. You will later apply this tag to the web service VM instances.
         
         gcloud compute firewall-rules create gclb-backend --source-ranges=130.211.0.0/22,35.191.0.0/16 --target-tags=gclb-backend --allow tcp:80
         




### Configure the production environment

Setting up the production environment requires a sequence of steps similar to those for configuring the development environment.

  1. In Cloud Shell, create an HTTP health check:
         
         gcloud compute http-health-checks create clouddemo-prod-http \
             --check-interval=10s --unhealthy-threshold=10 \
             --request-path=/
         

  2. Create another managed instance group that is based on the initial instance template that you created earlier:
         
         gcloud compute instance-groups managed create clouddemo-prod \
             --template=clouddemo-initial \
             --http-health-check=clouddemo-prod-http \
             --initial-delay=2m \
             --size=1 && \
         gcloud compute instance-groups set-named-ports clouddemo-prod --named-ports http:80
         

  3. Create a load balancer backend service that uses the HTTP health check and managed instance group that you created previously:
         
         gcloud compute backend-services create clouddemo-prod-backend --http-health-checks clouddemo-prod-http --port-name http --protocol HTTP --global && \
         gcloud compute backend-services add-backend clouddemo-prod-backend --instance-group clouddemo-prod --global --instance-group-zone=$(gcloud config get-value compute/zone)
         

  4. Create a load balancer frontend:
         
         gcloud compute url-maps create clouddemo-prod --default-service clouddemo-prod-backend && \
         gcloud compute target-http-proxies create clouddemo-prod-proxy --url-map=clouddemo-prod && \
         gcloud compute forwarding-rules create clouddemo-prod-fw-rule --global --target-http-proxy clouddemo-prod-proxy --ports=80
         




### Configure the release pipeline

Create a new release definition:

  1. In the Azure DevOps menu, select **Pipelines** > **Releases**.
  2. Click **New pipeline**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Publish`.
  5. At the top of the screen, name the release `clouddemo-ComputeEngine`.
  6. In the pipeline diagram, next to **Artifacts** , click **Add**.
  7. Select **Build** and add the following settings:

     * **Source** : Select the Git repository that contains the `azure-pipelines.yml` file.
     * **Default version** : `Latest`
     * **Source alias** : `CloudDemo.Web`
  8. Click **Add**.

  9. On the **Artifact** box, click **Continuous deployment trigger** (the lightning bolt icon) to add a deployment trigger.

  10. Under **Continuous deployment trigger** , set the switch to **Enabled**.

  11. Click **Save**.

  12. Enter a comment if you want, and then confirm by clicking **OK**.




The pipeline now looks like this:

![Screenshot of the pipeline in Azure Pipelines](https://docs.cloud.google.com/static/architecture/images/creating-cicd-pipeline-with-compute-engine-pipeline1.png)

#### Publish to Cloud Storage

Now that you have created the release definition, you can add the steps to publish the application package to Cloud Storage.

  1. In Azure Pipelines, switch to the **Tasks** tab.
  2. Click **Agent job** and configure the following settings: 
     * **Agent pool** : **Azure Pipelines**
     * **Agent specification** : **ubuntu-latest**
  3. Next to **Agent job** , click **Add a task to agent job** add.
  4. Select the **bash** task and click **Add**.
  5. Click the newly added task and configure the following settings:

     * **Display name** : `Publish to Cloud Storage`
     * **Type** : **inline**
     * **Script** :
           
           cat << "EOF" > CloudDemo.Mvc.deploy.ps1
               $ErrorActionPreference = "Stop"
           
               # Download application package from Cloud Storage
               gcloud storage cp gs://$(CloudDemo.ProjectId)-artifacts/CloudDemo.Mvc-$(Build.BuildId)-$(Release.ReleaseId).zip $env:TEMP\app.zip
           
               # Install IIS
               Enable-WindowsOptionalFeature -Online -FeatureName `
                   NetFx4Extended-ASPNET45, `
                   IIS-WebServerRole, `
                   IIS-WebServer, `
                   IIS-CommonHttpFeatures, `
                   IIS-HttpErrors, `
                   IIS-HttpRedirect, `
                   IIS-ApplicationDevelopment, `
                   IIS-HealthAndDiagnostics, `
                   IIS-HttpLogging, `
                   IIS-LoggingLibraries, `
                   IIS-RequestMonitor, `
                   IIS-HttpTracing, `
                   IIS-Security, `
                   IIS-RequestFiltering, `
                   IIS-Performance, `
                   IIS-WebServerManagementTools, `
                   IIS-IIS6ManagementCompatibility, `
                   IIS-Metabase, `
                   IIS-DefaultDocument, `
                   IIS-ApplicationInit, `
                   IIS-NetFxExtensibility45, `
                   IIS-ISAPIExtensions, `
                   IIS-ISAPIFilter, `
                   IIS-ASPNET45, `
                   IIS-HttpCompressionStatic
           
               # Extract application package to wwwroot
               New-Item -ItemType directory -Path $env:TEMP\app
               Add-Type -AssemblyName System.IO.Compression.FileSystem
               [System.IO.Compression.ZipFile]::ExtractToDirectory("$env:TEMP\app.zip", "$env:TEMP\app")
               Remove-Item $env:TEMP\app.zip
               Move-Item -Path $(dir -recurse $env:TEMP\app\**\PackageTmp | % { $_.FullName }) -Destination c:\inetpub\wwwroot\app -force
           
               # Configure IIS web application pool and application
               Import-Module WebAdministration
               New-WebAppPool clouddemo-net4
               Set-ItemProperty IIS:\AppPools\clouddemo-net4 managedRuntimeVersion v4.0
               New-WebApplication -Name clouddemo -Site 'Default Web Site' -PhysicalPath c:\inetpub\wwwroot\app -ApplicationPool clouddemo-net4
           
               # Grant read/execute access to the application pool user
               &icacls C:\inetpub\wwwroot\app\ /grant "IIS AppPool\clouddemo-net4:(OI)(CI)(RX)"
           EOF
           
           gcloud auth activate-service-account \
               --quiet \
               --key-file <(echo $(ServiceAccountKey) | base64 -d)
           
           gcloud storage cp $(System.ArtifactsDirectory)/CloudDemo.Web/CloudDemo.Web/CloudDemo.Mvc.zip gs://$(CloudDemo.ProjectId)-artifacts/CloudDemo.Mvc-$(Build.BuildId)-$(Release.ReleaseId).zip
           gcloud storage cp CloudDemo.Mvc.deploy.ps1 gs://$(CloudDemo.ProjectId)-artifacts/CloudDemo.Mvc-$(Build.BuildId)-$(Release.ReleaseId).deploy.ps1
           

This script does the following:

     1. Generates a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows) that configures IIS.
     2. Configures the Google Cloud CLI to use the service account key from the environment variable to authenticate to Google Cloud.
     3. Uploads the application package and startup script to Cloud Storage.
  6. Switch to the **Variables** tab and add the following variables.

**Name** | **Value** | **Secret**  
---|---|---  
`ServiceAccountKey` | Service account key created for `azure-pipelines-deployer` earlier. | Yes  
`CloudDemo.ProjectId` | Project ID of your Google Cloud project. |   
`CloudDemo.Zone` | The zone that you specified earlier when running `gcloud config set compute/zone` (for example, `us-central1-a`) |   
  7. Click **Save**.

  8. Enter a comment if you want, and then confirm by clicking **OK**.




#### Deploy the development environment

You can now add the steps to initiate a rolling deployment to the development environment.

  1. In Azure Pipelines, switch to the **Pipeline** tab.
  2. In the **Stages** box, select **Add** > **New stage**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Dev`.
  5. Click the lightning bolt icon of the newly created stage.
  6. Configure the following settings:

     * **Select trigger** : `After stage`
     * **Stages** : `Publish`
  7. Hold the mouse over the **Tasks** tab and click **Tasks** > **Dev**.

  8. Click **Agent job** and configure the following settings:

     * **Agent pool** : **Azure Pipelines**
     * **Agent specification** : **ubuntu-latest**
  9. Next to **Agent job** , click **Add a task to agent job** add.

  10. Select the **bash** task and click **Add**.

  11. Click the newly added task and configure the following settings:

     * **Display name** : `Rolling deploy`
     * **Type** : **inline**
     * **Script** :
           
           INSTANCE_TEMPLATE=clouddemo-$(Build.BuildId)-$(Release.ReleaseId)
           
           gcloud auth activate-service-account \
               --quiet \
               --key-file <(echo $(ServiceAccountKey) | base64 -d)
           
           gcloud compute instance-templates create $INSTANCE_TEMPLATE \
             --machine-type n1-standard-2 \
             --image-family windows-2019-core \
             --image-project windows-cloud \
             --service-account clouddemo-dev@$(CloudDemo.ProjectId).iam.gserviceaccount.com \
             --scopes https://www.googleapis.com/auth/devstorage.read_only \
             --tags gclb-backend \
             --metadata sysprep-specialize-script-url=gs://$(CloudDemo.ProjectId)-artifacts/CloudDemo.Mvc-$(Build.BuildId)-$(Release.ReleaseId).deploy.ps1 \
             --project $(CloudDemo.ProjectId) \
           
           gcloud compute instance-groups managed set-instance-template clouddemo-dev \
             --template $INSTANCE_TEMPLATE \
             --project $(CloudDemo.ProjectId) \
             --zone $(CloudDemo.Zone)
           
           gcloud compute instance-groups managed rolling-action start-update clouddemo-dev \
             --version template=$INSTANCE_TEMPLATE \
             --type proactive \
             --max-unavailable 0 \
             --project $(CloudDemo.ProjectId) \
             --zone $(CloudDemo.Zone)
           

This script does the following:

     1. Configures the Google Cloud CLI to use the service account key from the environment variable to authenticate to Google Cloud.
     2. Creates a new instance template that uses the startup script generated by the previous stage.
     3. Updates the existing instance group to use the new instance template. Note that this command does not yet cause any of the existing VMs to be replaced or updated. Instead, it ensures that any future VMs in this instance group are created from the new template.
     4. Starts a rolling update, causing the existing instance group to replace existing VMs with new VMs in a rolling fashion.
  12. Click **Save**.

  13. Enter a comment if you want, and confirm by clicking **OK**.




#### Deploy the production environment

Finally, you need to configure the deployment to the production environment.

  1. In Azure Pipelines, switch to the **Pipeline** tab.
  2. In the **Stages** box, select **Add** > **New stage**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Prod`.
  5. Click the lightning bolt icon of the newly created stage.
  6. Configure the following settings:

     * **Select trigger** : `After stage`
     * **Stages** : `Dev`
     * **Pre-deployment approvals** : (enabled)
     * **Approvers** : Select your own user name.
  7. Hold the mouse over the **Tasks** tab and click **Tasks** > **Prod**.

  8. Click **Agent job** and configure the following settings:

     * **Agent pool** : **Azure Pipelines**
     * **Agent specification** : **ubuntu-latest**
  9. Next to **Agent job** , click **Add a task to agent job** add to add a step to the phase.

  10. Select the **bash** task and click **Add**.

  11. Click the newly added task and configure the following settings:

     * **Display name** : `Rolling deploy`
     * **Type** : **inline**
     * **Script** :
           
           INSTANCE_TEMPLATE=clouddemo-$(Build.BuildId)-$(Release.ReleaseId)
           
           gcloud auth activate-service-account \
               --quiet \
               --key-file <(echo $(ServiceAccountKey) | base64 -d)
           
           gcloud compute instance-templates create $INSTANCE_TEMPLATE \
             --machine-type n1-standard-2 \
             --image-family windows-2019-core \
             --image-project windows-cloud \
             --service-account clouddemo-prod@$(CloudDemo.ProjectId).iam.gserviceaccount.com \
             --scopes https://www.googleapis.com/auth/devstorage.read_only \
             --tags gclb-backend \
             --metadata sysprep-specialize-script-url=gs://$(CloudDemo.ProjectId)-artifacts/CloudDemo.Mvc-$(Build.BuildId)-$(Release.ReleaseId).deploy.ps1 \
             --project $(CloudDemo.ProjectId) \
           
           gcloud compute instance-groups managed set-instance-template clouddemo-prod \
             --template $INSTANCE_TEMPLATE \
             --project $(CloudDemo.ProjectId) \
             --zone $(CloudDemo.Zone)
           
           gcloud compute instance-groups managed rolling-action start-update clouddemo-prod \
             --version template=$INSTANCE_TEMPLATE \
             --type proactive \
             --max-unavailable 0 \
             --project $(CloudDemo.ProjectId) \
             --zone $(CloudDemo.Zone)
           

  12. Click **Save**.

  13. Enter a comment if you want, and confirm by clicking **OK**.




### Run the pipeline

Now that you've configured the entire pipeline, you can test it by performing a source code change:

  1. On your local computer, open the file `applications\clouddemo\net4\CloudDemo.Mvc\Views\Home\Index.cshtml` from the Git repository that you cloned earlier.
  2. Change the value of `ViewBag.Title` from `Home Page` to `This app runs on GKE`.
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
            

  4. In the Azure DevOps menu, select **Pipelines**.

A build is triggered.

  5. After the build is finished, select **Pipelines** > **Releases**. A release process is initiated.

  6. Click **Release-1** to open the details page, and wait for the status of the **Dev** stage to switch to **Succeeded**.

  7. In the Google Cloud console, select **Network Services** > **Load balancing** > **clouddemo-dev**.

Note the IP address of the frontend.

  8. Open a new browser window and navigate to the following address:
         
         http://IP_ADDRESS/clouddemo/
         

where `IP_ADDRESS` is the IP address of the frontend.

Observe that the application has been deployed and is using the custom title.

You might see an error at first because the load balancer takes a few minutes to become available.

  9. In Azure Pipelines, click the **Approve** button located under the **Prod** stage to promote the deployment to the production environment.

If you don't see the button, you might need to first approve or reject a previous release.

  10. Enter a comment if you want, and then confirm by clicking **Approve**.

  11. Wait for the status of the **Prod** environment to switch to **Succeeded**.

  12. In the Google Cloud console, select **Network Services** > **Load balancing** > **clouddemo-prod**.

Note the IP address of the frontend.

  13. Open a new browser window and navigate to the following address:
         
         http://IP_ADDRESS/clouddemo/
         

where `IP_ADDRESS` is the IP address of the frontend.

Observe that the application has been deployed and is using the custom title.




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

  * Read about [best practices for managing images](https://docs.cloud.google.com/architecture/image-management-best-practices).
  * Learn how to [deploy a highly available SQL Server group on Compute Engine](https://docs.cloud.google.com/architecture/deploy-multi-subnet-sql-server).
  * Read about [.NET on Google Cloud Platform](https://docs.cloud.google.com/dotnet/docs).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-03-09 UTC."],[],[]] 
