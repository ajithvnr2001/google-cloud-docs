---
url: https://docs.cloud.google.com/dotnet/docs/creating-cicd-pipeline-vsts-kubernetes-engine/
title: Creating a CI/CD pipeline with Azure Pipelines and Google Kubernetes Engine \u00a0|\u00a0 .NET \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:45.632434+00:00
---

# Creating a CI/CD pipeline with Azure Pipelines and Google Kubernetes Engine  |  .NET  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/creating-cicd-pipeline-vsts-kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Creating a CI/CD pipeline with Azure Pipelines and Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2022-11-29 UTC

This tutorial shows how to use [Azure Pipelines](https://www.visualstudio.com/team-services/), [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) (GKE), and Google [Container Registry](https://docs.cloud.google.com/container-registry) to create a continuous integration/continuous deployment (CI/CD) pipeline for an ASP.NET MVC web application. For the purpose of this tutorial, you can select between two example applications:

  * An ASP.NET Core web application that uses .NET 6.0 and runs on Linux
  * An ASP.NET MVC web application that uses .NET Framework 4 and runs on Windows



The CI/CD pipeline uses two separate GKE clusters, one for development and one for production, as the following diagram shows.

![Conceptual diagram of CI/CD pipeline showing how developers and end users interact with the application](https://docs.cloud.google.com/static/architecture/images/creating-cicd-pipeline-with-kubernetes-engine-architecture.svg)

At the beginning of the pipeline, developers commit changes to the example codebase. This action triggers the pipeline to create a release and to deploy it to the development cluster. A release manager can then promote the release so that it's deployed into the production cluster.

This tutorial is intended for developers and DevOps engineers. It assumes that you have basic knowledge of Microsoft .NET, Azure Pipelines, and GKE. The tutorial also requires you to have administrative access to an Azure DevOps account.

## Objectives

  * Connect Google Container Registry to Azure Pipelines for publishing Docker images.
  * Prepare a [.NET sample app](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/master/applications/clouddemo/) for deployment into GKE.
  * Authenticate securely against GKE without having to use legacy authentication.
  * Use Azure Pipelines release management to orchestrate GKE deployments.



### Out of scope

This tutorial doesn't cover connecting Azures Pipelines with a private GKE cluster, or connecting to private authorized networks. 

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Cloud Storage](https://cloud.google.com/storage/pricing) (for Container Registry)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

Check the [Azure DevOps pricing page](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) for any fees that might apply to using Azure DevOps.

## Before you begin

It's usually advisable to use separate projects for development and production workloads so that Identity and Access Management (IAM) roles and permissions can be granted individually. For the sake of simplicity, this tutorial uses a single project for both GKE clusters, one for development and one for production.

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Make sure you have an Azure DevOps account and have administrator access to it. If you don't yet have an Azure DevOps account, you can sign up on the [Azure DevOps home page](https://go.microsoft.com/fwlink/?LinkId=307137). 

**Note:** You can either use a command-line Git client or Visual Studio to follow this tutorial. If you use Visual Studio, make sure that it's connected to your Azure DevOps account.

### Creating an Azure DevOps project

You use Azure DevOps to manage the source code, run builds and tests, and orchestrate the deployment to GKE. To begin, you create a project in your Azure DevOps account.

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




## Connecting Azure Pipelines to Google Container Registry

Before you can set up continuous integration for the `CloudDemo` app, you must connect Azure Pipelines to Container Registry. This connection allows Azure Pipelines to publish container images to Container Registry.

### Set up a service account for publishing images

Create a [Google Cloud service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your project:

  1. Open the Google Cloud console.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. To save time typing your project ID and Compute Engine zone options, set default configuration values by running the following commands:
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/zone us-central1-a
         

Replace `PROJECT_ID` with the project ID of your project.

  4. Enable the Container Registry API in the project:
         
         gcloud services enable containerregistry.googleapis.com
         

  5. Create a service account that Azure Pipelines uses to publish Docker images:
         
         gcloud iam service-accounts create azure-pipelines-publisher \
             --display-name="Azure Pipelines Publisher"
         

  6. Grant the [Artifact Registry Administrator IAM role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) (`roles/artifactregistry.admin`) to the service account to allow Azure Pipelines to push to Container Registry:
         
         AZURE_PIPELINES_PUBLISHER=azure-pipelines-publisher@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com
         
         gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
             --member serviceAccount:$AZURE_PIPELINES_PUBLISHER \
             --role roles/artifactregistry.admin
         

  7. Generate a service account key:
         
         gcloud iam service-accounts keys create azure-pipelines-publisher.json \
             --iam-account $AZURE_PIPELINES_PUBLISHER
         
         tr -d '\n' < azure-pipelines-publisher.json > azure-pipelines-publisher-oneline.json
         

  8. View the content of the service account key file:
         
         echo $(<azure-pipelines-publisher-oneline.json)
         

You need the service account key in one of the following steps.




### Create a service connection for Google Container Registry

In Azure Pipelines, create a new service connection for Container Registry:

  1. In the Azure **DevOps** menu, select **Project settings** , and then select **Pipelines** > **Service connections**.
  2. Click **Create service connection**.
  3. From the list, select **Docker Registry** , and then click **Next**.
  4. In the dialog, enter values for the following fields: 
     * **Registry type** : **Others**
     * **Docker Registry** : `https://gcr.io/PROJECT_ID`, replacing `PROJECT_ID` with the name of your project (for example, `https://gcr.io/azure-pipelines-test-project-12345`).
     * **Docker ID** : `_json_key`
     * **Password** : Paste the content of `azure-pipelines-publisher-oneline.json`.
     * **Service connection name** : `gcr-tutorial`
  5. Click **Save** to create the connection.



## Building continuously

You can now use Azure Pipelines to set up continuous integration. For each commit that's pushed to the Git repository, Azure Pipelines builds the code and packages the build artifacts into a Docker container. The container is then published to Container Registry.

The repository already contains the following Dockerfile:

###  .NET/Linux 
    
    
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

###  .NET Framework/Windows 
    
    
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
    
    FROM mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
    EXPOSE 80
    SHELL ["powershell", "-command"]
    
    #------------------------------------------------------------------------------
    # Add LogMonitor so that IIS and Windows logs are emitted to STDOUT and can be 
    # picked up by Docker/Kubernetes.
    #
    # See https://github.com/microsoft/windows-container-tools/wiki/Authoring-a-Config-File
    # for details.
    #------------------------------------------------------------------------------
    
    ADD https://github.com/microsoft/windows-container-tools/releases/download/v1.1/LogMonitor.exe LogMonitor/
    ADD LogMonitorConfig.json LogMonitor/
    
    #------------------------------------------------------------------------------
    # Copy publishing artifacts to webroot.
    #------------------------------------------------------------------------------
    
    ADD CloudDemo.Mvc/bin/Release/PublishOutput/ c:/inetpub/wwwroot/
    
    #------------------------------------------------------------------------------
    # Configure IIS using the helper functions from deployment.ps1.
    #------------------------------------------------------------------------------
    
    ADD deployment.ps1 /
    RUN . /deployment.ps1; \
    	Install-Iis; \
    	Register-WebApplication -AppName "CloudDemo"; \
    	Remove-Item /deployment.ps1
    
    #------------------------------------------------------------------------------
    # Run IIS, wrapped by LogMonitor.
    #------------------------------------------------------------------------------
    
    ENTRYPOINT ["C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc"]

You now create a new pipeline that uses YAML syntax:

  1. Using Visual Studio or a command-line `git` client, [clone your new Git repository](https://docs.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops&tabs=visual-studio) and check out the `main` branch.
  2. In the root of the repository, create a file named `azure-pipelines.yml`.
  3. Copy the following code into the file:

###  .NET/Linux 
         
         resources:
         - repo: self
           fetchDepth: 1
         pool:
           vmImage: ubuntu-20.04
         trigger:
         - main
         variables:
           TargetFramework: 'net6.0'
           BuildConfiguration: 'Release'
           DockerImageName: 'PROJECT_ID/clouddemo'
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
         - task: CmdLine@1
           displayName: 'Lock image version in deployment.yaml'
           inputs:
             filename: /bin/bash
             arguments: '-c "awk ''{gsub(\"CLOUDDEMO_IMAGE\", \"gcr.io/$(DockerImageName):$(Build.BuildId)\", $0); print}'' applications/clouddemo/netcore/deployment.yaml > $(build.artifactstagingdirectory)/deployment.yaml"'
         - task: PublishBuildArtifacts@1
           displayName: 'Publish Artifact'
           inputs:
             PathtoPublish: '$(build.artifactstagingdirectory)'
         - task: Docker@2
           displayName: 'Login to Artifact Registry'
           inputs:
             command: login
             containerRegistry: 'gcr-tutorial'
         - task: Docker@2
           displayName: 'Build and push image'
           inputs:
             Dockerfile: 'applications/clouddemo/netcore/Dockerfile'
             command: buildAndPush
             repository: '$(DockerImageName)'

###  .NET Framework/Windows 
         
         resources:
         - repo: self
           fetchDepth: 1
         pool:
           vmImage: windows-2019     # Matches WINDOWS_LTSC in GKE
           demands:
           - msbuild
           - visualstudio
         trigger:
         - master
         variables:
           Solution: 'applications/clouddemo/net4/CloudDemo.Mvc.sln'
           BuildPlatform: 'Any CPU'
           BuildConfiguration: 'Release'
           DockerImageName: 'PROJECT_ID/clouddemo'
         steps:
         - task: NuGetCommand@2
           displayName: 'NuGet restore'
           inputs:
             restoreSolution: '$(Solution)'
         - task: VSBuild@1
           displayName: 'Build solution'
           inputs:
             solution: '$(Solution)'
             msbuildArgs: '/p:DeployOnBuild=true /p:PublishProfile=FolderProfile'
             platform: '$(BuildPlatform)'
             configuration: '$(BuildConfiguration)'
         - task: PowerShell@2
           displayName: 'Lock image version in deployment.yaml'
           inputs:
             targetType: 'inline'
             script: '(Get-Content applications\clouddemo\net4\deployment.yaml) -replace "CLOUDDEMO_IMAGE","gcr.io/$(DockerImageName):$(Build.BuildId)" | Out-File -Encoding ASCII $(build.artifactstagingdirectory)\deployment.yaml'
         - task: PublishBuildArtifacts@1
           displayName: 'Publish Artifact'
           inputs:
             PathtoPublish: '$(build.artifactstagingdirectory)'
         - task: Docker@2
           displayName: 'Login to Artifact Registry'
           inputs:
             command: login
             containerRegistry: 'gcr-tutorial'
         - task: Docker@2
           displayName: 'Build and push image'
           inputs:
             Dockerfile: 'applications/clouddemo/net4/Dockerfile'
             command: buildAndPush
             repository: '$(DockerImageName)'

Replace `PROJECT_ID` with the name of your project, and then save the file.

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

A new build is triggered. It might take about 6 minutes for the build to complete.

  9. To verify that the image has been published to Container Registry, switch to your project in the Google Cloud console, select **Container Registry** > **Images** , and then click **clouddemo**.

A single image and the tag of this image are displayed. The tag corresponds to the numeric ID of the build that was run in Azure Pipelines.




## Deploying continuously

With Azure Pipelines automatically building your code and publishing Docker images for each commit, you can now turn your attention to deployment.

Unlike some other continuous integration systems, Azure Pipelines distinguishes between building and deploying, and it provides a specialized set of tools labeled Release Management for all deployment-related tasks.

Azure Pipelines Release Management is built around these concepts:

  * A _release_ refers to a set of artifacts that make up a specific version of your app and that are usually the result of a build process.
  * _Deployment_ refers to the process of taking a release and deploying it into a specific environment.
  * A deployment performs a set of _tasks_ , which can be grouped in jobs.
  * _Stages_ let you segment your pipeline and can be used to orchestrate deployments to multiple environments—for example, development and testing environments.



The primary artifact that the CloudDemo build process produces is the Docker image. However, because the Docker image is published to Container Registry, the image is outside the scope of Azure Pipelines. The image therefore doesn't serve well as the definition of a release.

To deploy to Kubernetes, you also need a _manifest_ , which resembles a bill of materials. The manifest not only defines the resources that Kubernetes is supposed to create and manage, but also specifies the exact version of the Docker image to use. The Kubernetes manifest is well suited to serve as the artifact that defines the release in Azure Pipelines Release Management.

### Configure the Kubernetes deployment

To run the CloudDemo in Kubernetes, you need the following resources:

  * A _Deployment_ that defines a single pod that runs the Docker image produced by the build.
  * A _NodePort_ service that makes the pod accessible to a load balancer.
  * An _Ingress_ that exposes the application to the public internet by using a [Cloud HTTP(S) load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/http).



The repository already contains the following Kubernetes manifest that defines these resources:

###  .NET/Linux 
    
    
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
    
    apiVersion: v1
    kind: Service
    metadata:
      name: clouddemo-netcore
    spec:
      ports:
      - port: 80
        targetPort: 8080
        protocol: TCP
        name: http
      selector:
        app: clouddemo-netcore
      type: NodePort
    
    ---
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: clouddemo-netcore
    spec:
      defaultBackend:
        service:
          name: clouddemo-netcore
          port:
            number: 80
    
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: clouddemo-netcore
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: clouddemo-netcore
      template:
        metadata:
          labels:
            app: clouddemo-netcore
        spec:
          containers:
          - name: clouddemo-netcore
            image: CLOUDDEMO_IMAGE
            ports:
              - containerPort: 8080
            livenessProbe:      # Used by deployment controller
              httpGet:
                path: /health
                port: 8080
              initialDelaySeconds: 5
              periodSeconds: 5
            readinessProbe:     # Used by Ingress/GCLB
              httpGet:
                path: /health
                port: 8080
              initialDelaySeconds: 3
              periodSeconds: 5
            resources:
              limits:
                memory: 1024Mi
              requests:
                memory: 256Mi

###  .NET Framework/Windows 
    
    
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
    
    apiVersion: v1
    kind: Service
    metadata:
      name: clouddemo-net4
      annotations:
        cloud.google.com/neg: '{"ingress": false}' # Disable NEG
    
    spec:
      ports:
      - port: 80
        targetPort: 80
        protocol: TCP
        name: http
      selector:
        app: clouddemo-net4
      type: NodePort
    
    ---
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: clouddemo-net4
    spec:
      defaultBackend:
        service:
          name: clouddemo-net4
          port:
            number: 80
    
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: clouddemo-net4
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: clouddemo-net4
      template:
        metadata:
          labels:
            app: clouddemo-net4
        spec:
          nodeSelector:
            kubernetes.io/os: windows
          containers:
          - name: clouddemo-net4
            image: CLOUDDEMO_IMAGE
            ports:
              - containerPort: 80
            livenessProbe:      # Used by deployment controller
              httpGet:
                path: /health
                port: 80
              initialDelaySeconds: 120
              periodSeconds: 5
            readinessProbe:     # Used by Ingress/GCLB
              httpGet:
                path: /health
                port: 80
              initialDelaySeconds: 10
              periodSeconds: 5
            resources:
              limits:
                memory: 1024Mi
              requests:
                memory: 256Mi

### Set up the development and production environments

Before returning to Azure Pipelines Release Management, you need to create the GKE clusters.

#### Create GKE clusters

  1. Return to your Cloud Shell instance.

  2. Enable the GKE API for your project:
         
         gcloud services enable container.googleapis.com

  3. Create the development cluster by using the following command. Note that it might take a few minutes to complete:

###  .NET/Linux 
         
         gcloud container clusters create azure-pipelines-cicd-dev --enable-ip-alias
         

###  .NET Framework/Windows 
         
         gcloud container clusters create azure-pipelines-cicd-dev --enable-ip-alias
         
         gcloud container node-pools create azure-pipelines-cicd-dev-win \
             --cluster=azure-pipelines-cicd-dev \
             --image-type=WINDOWS_LTSC \
             --no-enable-autoupgrade \
             --machine-type=n1-standard-2
         

  4. Create the production cluster by using the following command. Note that it might take a few minutes to complete:

###  .NET/Linux 
         
         gcloud container clusters create azure-pipelines-cicd-prod --enable-ip-alias
         

###  .NET Framework/Windows 
         
         gcloud container clusters create azure-pipelines-cicd-prod --enable-ip-alias
         
         gcloud container node-pools create azure-pipelines-cicd-prod-win \
             --cluster=azure-pipelines-cicd-prod \
             --image-type=WINDOWS_LTSC \
             --no-enable-autoupgrade \
             --machine-type=n1-standard-2
         




#### Connect Azure Pipelines to the development cluster

Just as you can use Azure Pipelines to connect to an external Docker registry like Container Registry, Azure Pipelines supports integrating external Kubernetes clusters.

It is possible to authenticate to Container Registry using a Google Cloud service account, but using Google Cloud service accounts is not supported by Azure Pipelines for authenticating with GKE. Instead, you have to use a [Kubernetes service account](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens).

To connect Azure Pipelines to your development cluster, you therefore have to create a Kubernetes service account first.

  1. In Cloud Shell, connect to the development cluster:
         
         gcloud container clusters get-credentials azure-pipelines-cicd-dev

  2. Create a Kubernetes service account for Azure Pipelines:
         
         kubectl create serviceaccount azure-pipelines-deploy

  3. Create a Kubernetes secret containing a token credential for Azure Pipelines:
         
         kubectl create secret generic azure-pipelines-deploy-token --type=kubernetes.io/service-account-token --dry-run -o yaml \
           | kubectl annotate --local -o yaml -f - kubernetes.io/service-account.name=azure-pipelines-deploy \
           | kubectl apply -f -
         

  4. Assign the `cluster-admin` role to the service account by creating a cluster role binding:
         
         kubectl create clusterrolebinding azure-pipelines-deploy --clusterrole=cluster-admin --serviceaccount=default:azure-pipelines-deploy

  5. Determine the IP address of the cluster:
         
         gcloud container clusters describe azure-pipelines-cicd-dev --format=value\(endpoint\)
         

You will need this address in a moment.

  6. In the Azure DevOps menu, select **Project settings** and then select **Pipelines** > **Service connections**.

  7. Click **New service connection**.

  8. Select **Kubernetes** and click **Next**.

  9. Configure the following settings.

**Note:** To get some of these values, you must run `kubectl` commands in Cloud Shell and then copy the values into the Azure page.
     * **Authentication method** : **Service account**.
     * **Server URL** : `https://PRIMARY_IP`. Replace `PRIMARY_IP` with the IP address that you determined earlier.
     * **Secret** : The Kubernetes Secret that you created earlier. To get the Secret, run the following command, copy the Secret, and then copy the Secret into the Azure page. 
           
           kubectl get secret azure-pipelines-deploy-token -o yaml

     * **Service connection name** : `azure-pipelines-cicd-dev`.
  10. Click **Save**.




#### Connect Azure Pipelines to the production cluster

To connect Azure Pipelines to your production cluster, you can follow the same approach.

  1. In Cloud Shell, connect to the production cluster:
         
         gcloud container clusters get-credentials azure-pipelines-cicd-prod

  2. Create a Kubernetes service account for Azure Pipelines:
         
         kubectl create serviceaccount azure-pipelines-deploy

  3. Assign the `cluster-admin` role to the service account by creating a cluster role binding:
         
         kubectl create clusterrolebinding azure-pipelines-deploy --clusterrole=cluster-admin --serviceaccount=default:azure-pipelines-deploy

  4. Determine the IP address of the cluster:
         
         gcloud container clusters describe azure-pipelines-cicd-prod --format=value\(endpoint\)
         

You will need this address in a moment.

  5. In the Azure DevOps menu, select **Project settings** and then select **Pipelines** > **Service connections**.

  6. Click **New service connection**.

  7. Select **Kubernetes** and click **Next**.

  8. Configure the following settings:

**Note:** To get some of these values, you must run `kubectl` commands in Cloud Shell and then copy the values into the Azure page.
     * **Authentication method** : **Service account**.
     * **Server URL** : `https://PRIMARY_IP`. Replace `PRIMARY_IP` with the IP address that you determined earlier.
     * **Secret** : Run the following command in Cloud Shell and copy the output: 
           
           kubectl get secret $(kubectl get serviceaccounts azure-pipelines-deploy -o custom-columns=":secrets[0].name") -o yaml

     * **Service connection name** : `azure-pipelines-cicd-prod`.
  9. Click **Save**.




### Configure the release pipeline

After you set up the GKE infrastructure, you return to Azure Pipelines to automate the deployment, which includes the following:

  * Deploying to the development environment.
  * Requesting manual approval before initiating a deployment to the production environment.
  * Deploying to the production environment.



#### Create a release definition

As a first step, create a new release definition.

  1. In the Azure DevOps menu, select **Pipelines** > **Releases**.
  2. Click **New pipeline**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Development`.
  5. At the top of the screen, name the release **CloudDemo-KubernetesEngine**.
  6. In the pipeline diagram, next to **Artifacts** , click **Add**.
  7. Select **Build** and add the following settings:

     * **Source type** : **Build**
     * **Source (build pipeline)** : Select the build definition (there should be only one option)
     * **Default version** : `Latest`
     * **Source Alias:** `manifest`
  8. Click **Add**.

  9. On the **Artifact** box, click **Continuous deployment trigger** (the lightning bolt icon) to add a deployment trigger.

  10. Under **Continuous deployment trigger** , set the switch to **Enabled**.

  11. Click **Save**.

  12. Enter a comment if you want, and then confirm by clicking **OK**.

The pipeline displays similar to the following.

![Screenshot of the updated pipeline in Azure Pipelines](https://docs.cloud.google.com/static/architecture/images/creating-cicd-pipeline-with-kubernetes-engine-pipeline1.png)




#### Deploy to the development cluster

With the release definition created, you can now configure the deployment to the GKE development cluster.

  1. In the menu, switch to the **Tasks** tab.
  2. Click **Agent job** and configure the following settings:

     * **Agent pool** : **Azure Pipelines**
     * **Agent specification** : **ubuntu-18.04**
  3. Next to **Agent job** , click **Add a task to agent job** add to add a step to the phase.

  4. Select the **Deploy to Kubernetes** task and click **Add**.

  5. Click the newly added task and configure the following settings:

     * **Display name** : `Deploy`
     * **Action** : **deploy**
     * **Kubernetes service connection** : **azure-pipelines-cicd-dev**
     * **Namespace** : `default`
     * **Strategy** : **None**
     * **Manifests** : `manifest/drop/deployment.yaml`
  6. Click **Save**.

  7. Enter a comment if you want, and then confirm by clicking **OK**.




#### Deploy to the production cluster

Finally, you configure the deployment to the GKE production cluster.

  1. In the menu, switch to the **Pipeline** tab.
  2. In the Stages box, select **Add** > **New stage**.
  3. From the list of templates, select **Empty job**.
  4. When you're prompted for a name for the stage, enter `Production`.
  5. Click the lightning bolt icon of the newly created stage.
  6. Configure the following settings:

     * **Select trigger** : **After stage**
     * **Stages** : **Dev**
     * **Pre-deployment approvals** : (enabled)
     * **Approvers** : Select your own username.

The pipeline now looks like this:

![Screenshot of the updated pipeline in Azure Pipelines](https://docs.cloud.google.com/static/architecture/images/creating-cicd-pipeline-with-kubernetes-engine-pipeline2.png)

  7. Switch to the **Tasks** tab.

  8. Hold the mouse over the **Tasks** tab and select **Tasks** > **Production**.

  9. Click **Agent job** and configure the following settings:

     * **Agent pool** : **Azure Pipelines**
     * **Agent specification** : **ubuntu-18.04**
  10. Click **Add a task to agent job** add to add a step to the phase.

  11. Select the **Deploy to Kubernetes** task and click **Add**.

  12. Click the newly added task and configure the following settings:

     * **Display name** : `Deploy`
     * **Action** : **deploy**
     * **Kubernetes service connection** : **azure-pipelines-cicd-prod**
     * **Namespace** : `default`
     * **Strategy** : **None**
     * **Manifests** : `manifest/drop/deployment.yaml`
  13. Click **Save**.

  14. Enter a comment if you want, and then confirm by clicking **OK**.




### Run the pipeline

Now that you've configured the entire pipeline, you can test it by performing a source code change:

  1. On your local computer, open the file `Index.cshtml` from the Git repository you cloned earlier:

###  .NET/Linux 

The file is located in `applications\clouddemo\netcore\CloudDemo.MvcCore\Views\Home\`

###  .NET Framework/Windows 

The file is located in `applications\clouddemo\net4\CloudDemo.Mvc\Views\Home\`

  2. In line 26, change the value of `ViewBag.Title` from `Home Page` to `This app runs on GKE`.

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

  7. In the Google Cloud console, select **Kubernetes Engine** > **Services & Ingress** > **Ingress**.

  8. Locate the Ingress service for the **azure-pipelines-cicd-dev** cluster, and wait for its status to switch to **Ok**. This might take several minutes.

  9. Open the link in the **Frontends** column of the same row. You might see an error at first because the load balancer takes a few minutes to become available. When it's ready, observe that the CloudDemo has been deployed and is using the custom title.

  10. In Azure Pipelines, click the **Approve** button located under the **Prod** stage to promote the deployment to the production environment.

If you don't see the button, you might need to first approve or reject a previous release.

  11. Enter a comment if you want, and then confirm by clicking **Approve**.

  12. Wait for the status of the **Prod** environment to switch to **Succeeded**. You might need to manually refresh the page in your browser.

  13. In the Google Cloud console, refresh the **Services & Ingress** page.

  14. Locate the Ingress service for the **azure-pipelines-cicd-prod** cluster and wait for its status to switch to **Ok**. This might take several minutes.

  15. Open the link in the **Frontends** column of the same row. Again, you might see an error at first because the load balancer take a few minutes to become available. When it's ready, you see the CloudDemo app with the custom title again, this time running in the production cluster.




## Clean up

To avoid incurring further costs after you complete this tutorial, delete the entities that you created.

### Delete the Azure Pipelines project

To delete the Azure Pipelines project, see the [Azure DevOps Services documentation](https://docs.microsoft.com/en-us/vsts/accounts/delete-team-project?view=vsts). Deleting the Azure Pipelines project causes all source code changes to be lost.

### Delete the Google Cloud development and projects

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Configure [fine-grained access control for Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control).
  * Learn how to [deploy a highly available SQL Server group on Compute Engine](https://docs.cloud.google.com/solutions/deploy-multi-subnet-sql-server).
  * Read about [.NET on Google Cloud Platform](https://docs.cloud.google.com/dotnet/docs).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2022-11-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-11-29 UTC."],[],[]] 
