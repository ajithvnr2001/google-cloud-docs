---
url: https://docs.cloud.google.com/dotnet/docs/getting-started/deploying-to-gke-using-github-actions-windows/
title: Deploy a .NET Framework app to Google Kubernetes Engine using a GitHub Actions workflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:06.448530+00:00
---

# Deploy a .NET Framework app to Google Kubernetes Engine using a GitHub Actions workflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/getting-started/deploying-to-gke-using-github-actions-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Deploy a .NET Framework app to Google Kubernetes Engine using a GitHub Actions workflow Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to use a [GitHub Actions](https://www.visualstudio.com/team-services/), workflow to deploy an ASP.NET Model-View-Controller (MVC) web application that uses [.NET Framework](https://dotnet.microsoft.com/en-us/download/dotnet-framework) to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) (GKE).

This tutorial is intended for developers and DevOps engineers who have basic knowledge of Microsoft .NET, GitHub Actions, and GKE. You also require a GitHub account to execute this tutorial.

## Objectives

Deploy an ASP.NET MVC web application that uses .NET Framework 4 and runs on Windows to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine).

**Note:** For information on deploying an ASP.NET Core web application that uses .NET 6.0 and runs on Linux, see [Deploy a .NET app to Google Kubernetes Engine using a GitHub Actions workflow](https://docs.cloud.google.com/dotnet/docs/getting-started/deploying-to-gke-using-github-actions).

The following diagram shows the [GitHub Actions](https://www.visualstudio.com/team-services/), workflow to deploy an ASP.NET MVC web application to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) (GKE).

![Conceptual diagram of the GitHub Actions workflow](https://docs.cloud.google.com/static/dotnet/docs/images/github_actions_tutorial.png)

This tutorial shows you how to complete the following tasks to reach your objective: 

  * Create a GitHub repository
  * Configure authentication
  * Deploy a GKE cluster and an Artifact Registry repository
  * Create a GitHub Actions workflow



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

**Note:** Additional fees might apply [for using GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)




## Create a GitHub repository

Create a fork of the `dotnet-docs-samples` repository in your GitHub account. This step is necessary because we are building with GitHub Actions.

  1. Go to the [`dotnet-docs-samples`](https://github.com/GoogleCloudPlatform/dotnet-docs-samples) GitHub repository.
  2. Click **Fork**.
  3. On the **Create a new fork** page, set the following:

     * **Owner** \- Your GitHub account
     * **Repository name** \- `dotnet-docs-samples`
  4. Click **Create fork**.




## Configure authentication

Prepare your Google Cloud project so that GitHub Actions can authenticate and access resources in the Google Cloud project.

### Create a workload identity federation pool and provider

To allow GitHub Actions authenticate Google Cloud and deploy to GKE, use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). By using workload identity federation, you can avoid the need to store and manage [service account keys](https://docs.cloud.google.com/iam/docs/service-accounts#service_account_keys) for your GitHub Actions workload.

Using workload identity federation requires a workload identity pool and provider. We recommend that you [use a dedicated project to manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#dedicated-project). In this tutorial, for the sake of simplicity, create the pool and provider in the same project as your GKE cluster:

  1. Open the Google Cloud console.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. Create a new workload identity pool:
         
         gcloud iam workload-identity-pools create github-actions \
             --location="global" \
             --description="GitHub Actions tutorial" \
             --display-name="GitHub Actions"
         

  4. Add GitHub Actions as a workload identity pool provider:
         
         gcloud iam workload-identity-pools providers create-oidc github-actions-oidc \
             --location="global" \
             --workload-identity-pool=github-actions \
             --issuer-uri="https://token.actions.githubusercontent.com/" \
             --attribute-mapping="google.subject=assertion.sub" \
             --attribute-condition="assertion.repository_owner=='ORGANIZATION'"
         

Replace `ORGANIZATION` with the name of your GitHub organization.




### Create a service account

  1. In Cloud Shell, create a service account that GitHub Actions can use to publish Docker images and deploy to GKE:
         
         SERVICE_ACCOUNT=$(gcloud iam service-accounts create github-actions-workflow \
           --display-name "GitHub Actions workflow" \
           --format "value(email)")
         

  2. Grant the [Artifact Registry writer role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/artifactregistry.writer`) to the service account to allow GitHub actions to push to Artifact Registry:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
           --member serviceAccount:$SERVICE_ACCOUNT \
           --role roles/artifactregistry.writer
         

  3. Grant the [Google Kubernetes Engine developer role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/container.developer`) to the service account to allow GitHub actions to push to Artifact Registry:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
           --member serviceAccount:$SERVICE_ACCOUNT \
           --role roles/container.developer
         




### Allow the GitHub Actions workflow to use the service account

Allow the GitHub Actions workflow to impersonate and use the service account:

  1. Initialize an environment variable that contains the [subject](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-a-specific-branch) used by the GitHub Actions workflow. A subject is similar to a username that uniquely identifies the GitHub repository and branch:
         
         SUBJECT=repo:OWNER/dotnet-docs-samples:ref:refs/heads/main
         

Replace `OWNER` with your GitHub username.

  2. Grant the subject permission to impersonate the service account:
         
         PROJECT_NUMBER=$(gcloud projects describe $(gcloud config get-value core/project) --format='value(projectNumber)')
         
         gcloud iam service-accounts add-iam-policy-binding $SERVICE_ACCOUNT \
           --role=roles/iam.workloadIdentityUser \
           --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/github-actions/subject/$SUBJECT"
         




## Deploy a GKE cluster and an Artifact Registry repository

  1. Create a repository for Docker images:
         
         gcloud artifacts repositories create clouddemo \
           --repository-format=docker \
           --location=us-central1
         

  2. Allow the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) to access the repository:
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value core/project) \
           --member=serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --role=roles/artifactregistry.reader
         

  3. Create the cluster:
         
         gcloud container clusters create clouddemo-windows \
           --enable-ip-alias \
           --zone us-central1-a
         
         gcloud container node-pools create clouddemo-windows-pool \
           --cluster=clouddemo-windows \
           --image-type=WINDOWS_LTSC_CONTAINERD \
           --no-enable-autoupgrade \
           --machine-type=n1-standard-2 \
           --zone us-central1-a
         

This command might take several minutes to complete.

  4. Get the project name and project number of the cluster:
         
         echo "Project ID: $(gcloud config get-value core/project)"
         echo "Project Number: $(gcloud projects describe $(gcloud config get-value core/project) --format=value\(projectNumber\))"
         

You need these values later.




## Create a GitHub Actions workflow

You can now use GitHub Actions to set up continuous integration. For each commit that's pushed to the Git repository, a GitHub Actions workflow builds the code and packages the build artifacts into a Docker container. The container is then published to Artifact Registry.

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

The repository also contains a Kubernetes manifest:
    
    
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

Create a GitHub Actions workflow that does the following:

  * Authenticate to Google Cloud using workload identity federation and the service account that you created earlier.
  * Build a Docker image and deploy it to Artifact Registry.
  * Deploy the Docker image to GKE.



To create the GitHub Actions workflow, do the following:

  1. On [GitHub](https://github.com/), go to your fork of the `dotnet-docs-samples` repository.
  2. Click **Add file** > **Create new file**.
  3. In the **Name your file** text field, enter the following name:
         
         .github/workflows/deploy-gke.yaml
         

  4. Copy the following code into the file:

**Note:** On Windows, variables need to prefixed with `env: ($env:FOO instead of $FOO)!`
         
         name: Build and Deploy to GKE
         
         on:
           push:
             branches:
               - main
         
         env:
           PROJECT_ID: PROJECT_ID
           PROJECT_NUMBER: PROJECT_NUMBER
         
           CLUSTER: clouddemo-windows
           CLUSTER_ZONE: us-central1-a
         
           REPOSITORY: clouddemo
           REPOSITORY_REGION: us-central1
         
           IMAGE: clouddemo
         
         jobs:
           build:
             runs-on: windows-2019  # Matches WINDOWS_LTSC in GKE
             permissions:
               id-token: write
               contents: read
         
             steps:
             - name: Checkout
               uses: actions/checkout@v3
         
             #
             # Authenticate to Google Cloud using workload identity federation
             #
             - id: 'auth'
               name: 'Obtain access token by using workload identity federation'
               uses: 'google-github-actions/auth@v0'
               with:
                 create_credentials_file: true
                 token_format: access_token
                 workload_identity_provider: projects/${{ env.PROJECT_NUMBER }}/locations/global/workloadIdentityPools/github-actions/providers/github-actions-oidc
                 service_account: github-actions-workflow@${{ env.PROJECT_ID }}.iam.gserviceaccount.com
         
             - name: Connect to Artifact Registry
               run: |-
                 echo ${{ steps.auth.outputs.access_token }} | docker login -u oauth2accesstoken --password-stdin https://${{ env.REPOSITORY_REGION }}-docker.pkg.dev
         
             - name: Connect to GKE
               uses: google-github-actions/get-gke-credentials@v0
               with:
                 cluster_name: ${{ env.CLUSTER }}
                 location: ${{ env.CLUSTER_ZONE }}
         
             #
             # Build the .NET code
             #
             - name: Setup MSBuild
               uses: microsoft/setup-msbuild@v1
         
             - name: Setup NuGet
               uses: NuGet/setup-nuget@v1
         
             - name: Restore NuGet packages
               run: nuget restore applications/clouddemo/net4/CloudDemo.Mvc.sln
         
             - name: Build solution
               run: msbuild /t:Rebuild /p:Configuration=Release /p:DeployOnBuild=true /p:PublishProfile=FolderProfile /nologo applications/clouddemo/net4/CloudDemo.Mvc.sln
         
             #
             # Build the Docker image and push it to Artifact Registry
             #
             - name: Create image tag
               run: echo "IMAGE_TAG=${{ env.REPOSITORY_REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.IMAGE }}:$env:GITHUB_SHA" >> $env:GITHUB_ENV
         
             - name: Lock image version in deployment.yaml
               shell: pwsh
               run: (Get-Content applications\clouddemo\net4\deployment.yaml) -replace "CLOUDDEMO_IMAGE","${{ env.IMAGE_TAG }}" | Out-File -Encoding ASCII applications\clouddemo\net4\deployment.yaml
         
             - name: Build Docker image
               run: docker build --tag "${{ env.IMAGE_TAG }}" applications/clouddemo/net4
         
             - name: Publish Docker image to Google Artifact Registry
               run: docker push "${{ env.IMAGE_TAG }"
         
             #
             # Deploy to GKE
             #
             - name: Deploy to GKE
               run: kubectl apply -f applications/clouddemo/net4/deployment.yaml
         

Replace the following values:

     * `PROJECT_ID`: the project ID of the project that contains the GKE cluster.
     * `PROJECT_NUMBER`: the project number of the project that contains the GKE cluster.
  5. In the **Commit new file** section, enter a commit message, for example, `Add workflow` and click **Commit new file**.

  6. In the menu, click **Actions** and wait for the workflow to complete.

The workflow might take several minutes to complete.

  7. In the Google Cloud console, refresh the **Services & Ingress** page.

[Go to Services & Ingress](https://console.cloud.google.com/kubernetes/ingresses)

  8. Go to the **Ingress** tab.

  9. Locate the Ingress service for the **clouddemo** cluster and wait for its status to switch to **Ok**. This might take several minutes.

  10. Open the link in the **Frontends** column of the same row. The load balancer take a few minutes to become available, so the CloudDemo app might not load at first. When the load balancer ready, you'll see the CloudDemo app with the custom title, this time running in the production cluster.




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources.

### Delete the GitHub repository

To delete the GitHub repository, see [Deleting a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository). Deleting the repository causes all source code changes to be lost.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * [Deploy, manage, and scale containerized applications on Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs).
  * Review the best practices in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
