---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize/
title: Learning Path: Scalable applications - Centralize changes with Config Sync \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:49.120786+00:00
---

# Learning Path: Scalable applications - Centralize changes with Config Sync  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Centralize changes with Config Sync Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This set of tutorials is for IT administrators and Operators that want to deploy, run, and manage modern application environments that run on Google Kubernetes Engine. As you progress through this set of tutorials you learn how to configure monitoring and alerts, scale workloads, and simulate failure, all using the Cymbal Bank sample microservices application:

  1. [Create a cluster and deploy a sample application](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment)
  2. [Monitor with Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor)
  3. [Scale workloads](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale)
  4. [Simulate a failure](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure)
  5. Centralize change management (this tutorial)



## Overview and objectives

As you build new services and applications, you might want to test changes in different environments. As your organization grows, you might need different cluster configurations for different teams. Managing multiple clusters with different configurations can be challenging. You can use GitOps tools like Config Sync to help you manage these challenges.

In the [Create a cluster tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment), you created a cluster and deployed the Cymbal Bank application to that cluster.

In this tutorial, you learn how to store the Kubernetes manifests for your application in a centralized Git repository and how to use tools like Config Sync to deploy an application to multiple clusters in a fleet. You learn how to complete the following tasks:

  * Create a Git repository and connect it to Cloud Build

  * Create a cluster, register it to a fleet, and install Config Sync on your fleet of clusters

  * Use a fleet package to deploy Cymbal Bank and other resources on a cluster or across a fleet




## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs and load balancers.

## Before you begin

To learn how to store, make changes, and deploy resources from a Git repository, you must complete the [first tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) to create a GKE cluster that uses Autopilot mode and deploy the Cymbal Bank sample microservices-based application.

We recommend that you complete this set of tutorials for Cymbal Bank in order. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

To use Config Sync to deploy Kubernetes manifests from a Git repository to your clusters, you must enable the following APIs:
    
    
    gcloud services enable configdelivery.googleapis.com cloudbuild.googleapis.com developerconnect.googleapis.com
    

## Create a Git repository and connect it to Cloud Build

A fleet package is a collection of Kubernetes resource manifests. By bundling those manifests together as a package, you can deploy an application to multiple clusters in a fleet directly from a Git repository. With this workflow, you get the following benefits:

  * Improved scalability by deploying resources across a fleet instead of manually applying them cluster by cluster.
  * Safer updates with progressive rollouts.
  * Additional workflows from centrally sourcing configuration files in Git, like version control and approvals.



To demonstrate how to store and make changes in Git, you fork the Cymbal Bank repository and connect it to Cloud Build.

### Fork the Cymbal Bank repository

In this tutorial, you make changes to your Git repository to demonstrate how Config Sync helps you safely manage changes to Kubernetes resources and deploy them. To make those changes directly, you must fork the Git repository instead of cloning it.

**Key Term:** **Cloning** a repository creates a local copy that you sync with the remote. This is useful when you are contributing directly to a repository. **Forking** creates a separate copy of a repository that you own. Use forking when you want to use the repository's code and make changes without impacting the original project.

To fork the repository, complete the following steps:

  1. In GitHub, go to the [Cymbal Bank (`bank-of-anthos`) sample repository](https://github.com/GoogleCloudPlatform/bank-of-anthos).

  2. Click **Fork** to get a copy of the repository with source files.

![Alt text](https://docs.cloud.google.com/static/kubernetes-engine/images/git-fork-example.png)

  3. If needed, sign in to your GitHub account. If you have access to other organizations or teams on GitHub, make sure that you're forking the repository to your personal account.




You now have a fork of the Cymbal Bank repository. All of the Kubernetes manifests that you deploy are located in the `/kubernetes-manifests` folder.

### Connect the repository to Cloud Build

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) is a service that can execute builds on Google Cloud, which you can use for GitOps-style continuous delivery. Config Sync's fleet package service uses Cloud Build to fetch the Kubernetes resources from your Git repository and deploy them to your clusters. When you use a fleet package, you need to set up Cloud Build only once per repository that you want to sync. The fleet package API automatically creates the build triggers through Cloud Build.

To connect your GitHub repository to Cloud Build:

  1. Open the Cloud Build page in the Google Cloud console, and then select **Repositories**.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories/2nd-gen)

  2. Ensure that you are on the 2nd gen **Repositories** page. If needed, select **View repositories (2nd gen)**.

  3. Click **Create host connection**.

  4. In the **Region** menu, select **us-central1 (Iowa)** as your region.

**Caution:** You can select only **us-central1 (Iowa)** as the region. The Cloud Build connection and fleet package must be in the same region. Fleet packages ([Preview](https://cloud.google.com/products#product-launch-stages)) supports only `us-central1`.
  5. In the **Name** field, type `cymbal-bank-connection` as the name for your connection.

  6. Click **Connect**.

  7. If this is your first time connecting Cloud Build to your GitHub account, complete the following steps:

     1. Accept the request for your GitHub OAuth token. The token is stored in Secret Manager for use with Cloud Build GitHub Connection. Click **Continue**.
     2. Install Cloud Build into your GitHub repository. Select **Install in a new account**.
     3. In the new GitHub window that opens, select the GitHub account in which you created the fork of Cymbal Bank earlier. In a production environment, you might select other accounts or repositories that you have delegated access to.
     4. Follow any authentication prompts to confirm your identity in GitHub.
     5. In the GitHub window for Cloud Build repository access, choose **Only select repositories**.
     6. From the drop-down menu that lists repositories, select your fork of `bank-of-anthos`.
     7. Click **Save**.
  8. In the Cloud Build page in the Google Cloud console, click **Link repository** to connect a new Git repository to Cloud Build.

  9. In the **Connection** menu, select `cymbal-bank-connection`.

  10. In the **Repositories** menu, select your `bank-of-anthos` fork.

  11. Select **Link**.


**Success:** You have now linked a GitHub repository to Cloud Build.

## Create clusters

In the first tutorial in this series, you created one cluster and deployed the Cymbal Bank application to that cluster. In a real scenario, it's unlikely that you would have only one cluster to manage. GKE lets you group together clusters in a fleet: a logical group of clusters that can be managed together. Within a fleet, you might further group your clusters with some clusters representing different environments or belonging to different teams. For example, you might have a development cluster, a staging cluster, and a production cluster. In a large organization, individual teams might have their own clusters for different environments. As IT administrators or Operators, this might mean you have to manage dozens of clusters!

When it comes to deploying applications, or individual resources like custom policies, across all of these clusters, GKE features like Config Sync can help you manage those deployments at scale.

To help demonstrate how to deploy resources to different environments or across a fleet of clusters, you create a new cluster and deploy the Cymbal Bank application to it:

  1. Create a GKE cluster that simulates a development environment:
         
         gcloud container clusters create-auto scalable-apps-dev \
           --project=PROJECT_ID \
           --region=REGION \
           --fleet-project=PROJECT_ID \
           --release-channel=rapid
         

Replace the following:

     * `PROJECT_ID` with the automatically-generated ID of the project that you created in the previous section. The project ID is often different from the project name. For example, your project might be _scalable-apps_ , but your project ID might be _scalable-apps-567123_.
     * `REGION` with the region that you want to create your cluster in, such as `us-central1`.
  2. Labels are key-value pairs that you can add to GKE resources to help organize them. For fleet packages, you can use fleet membership labels to customize which clusters the fleet package targets. Other types of labels aren't supported.

Add a label to the fleet membership:
         
         gcloud container fleet memberships update scalable-apps-dev \
             --update-labels=env=dev
         

When you create the fleet package later in this tutorial, this label ensures that the resources are only deployed on the `scalable-apps-dev` cluster and not the `scalable-apps` cluster from the first tutorial in this series.




## Install Config Sync

Install Config Sync on both clusters:

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Click _add_ **Install Config Sync**.
  3. Keep **Manual upgrades** selected.
  4. The version menu should default to the latest version of Config Sync. If needed, select the most recent version.
  5. Under **Installation options** , select **Install Config Sync on entire fleet (recommended)**.
  6. Click **Install Config Sync**.
  7. In the **Settings** tab for Config Sync, look at the _Status_ field of the cluster list. After a few minutes, the status shows as "Pending" until the cluster is correctly configured for Config Sync. It can take up to 10 minutes for the status to change to _Enabled_.

**Success:** You now have Config Sync installed on both clusters in your fleet.

## Deploy Cymbal Bank

In the first tutorial in this series, you used `kubectl` commands to apply the application configurations to your cluster. In this tutorial, you use Config Sync's fleet packages feature to deploy those same configurations to a new cluster. In a later section, you'll see an example of how to add a new resource to your Git repository and deploy those resources across a fleet of clusters.

### Set up a service account for Cloud Build

A service account is a special kind of account typically used by an application, rather than a person. As a best practice when creating service accounts, you should create service accounts for a single, specific service or task, and give the service account granular roles. In this tutorial, you create a service account to grant Cloud Build permissions to fetch Kubernetes resources from your Git repository and deploy them to your clusters.

To create the service account and grant the required permissions, complete the following steps:

  1. Create the service account:
         
         gcloud iam service-accounts create "cymbal-bank-service-account"
         

  2. Grant the service account permission to fetch resources from your Git repository by adding an IAM policy binding for the Resource Bundle Publisher role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:cymbal-bank-service-account@PROJECT_ID.iam.gserviceaccount.com" \
            --role='roles/configdelivery.resourceBundlePublisher'
         

If prompted, select `None` as the condition for the policy.

  3. Grant the service account permission to write logs by adding an IAM policy binding for the [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:cymbal-bank-service-account@PROJECT_ID.iam.gserviceaccount.com" \
            --role='roles/logging.logWriter'
         

If prompted, select `None` as the condition for the policy.




### Create a release for the Cymbal Bank application

A fleet package requires a semantic version tag to know which version of your repository to deploy from. It's a good idea to create new releases when you make changes to your repository, as this helps with version control and makes it easier to roll back to a stable version if needed.

**Key Term:** **Semantic versioning** is a schema for version numbers with the format `MAJOR.MINOR.PATCH` where the schema conveys meaning about the types of changes from one version to the next. For more information, see [Semantic Versioning](https://semver.org/).

  1. In a web browser window of your GitHub fork of Cymbal Bank, under the **Releases** section of the sidebar, click **Create a new release**.

  2. Select the **Choose a tag** menu and type `v1.0.0` as the tag. Click **Create new tag**.

  3. Click **Publish release**.




### Set up authentication

[Just like the first tutorial in this series](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment), you must create a JWT to handle user authentication and a Kubernetes Secret to store the JWT for the new cluster that you created. It's a good idea for each cluster to have a unique JWT for authentication.

  1. In your Cloud Shell, create the JWT:
         
         openssl genrsa -out jwtRS256.key 4096
         openssl rsa -in jwtRS256.key -outform PEM -pubout -out jwtRS256.key.pub
         

  2. Create the Kubernetes Secret:
         
         kubectl create secret generic jwt-key --from-file=./jwtRS256.key --from-file=./jwtRS256.key.pub
         




### Deploy the Cymbal Bank application with a fleet package

A `FleetPackage` resource is a declarative API to deploy multiple Kubernetes manifests to a fleet of clusters.

To create a fleet package, you define a `FleetPackage` spec that points to the repository with your Kubernetes resources that you connected to Cloud Build. Then you apply the `FleetPackage` resource, which fetches the resources from Git and deploys them across the fleet.

  1. In your Cloud Shell, set the default location for the `configdelivery` Google Cloud CLI commands. As with connecting your repository to Cloud Build, you must use `us-central1` while the fleet packages feature is in preview:
         
         gcloud config set config_delivery/location us-central1
         

  2. Create a file named `fleetpackage-spec.yaml` with the following content:
         
         resourceBundleSelector:
           cloudBuildRepository:
             name: projects/PROJECT_ID/locations/us-central1/connections/cymbal-bank-connection/repositories/REPOSITORY_NAME
             tag: v1.0.0
             serviceAccount: projects/PROJECT_ID/serviceAccounts/cymbal-bank-service-account@PROJECT_ID.iam.gserviceaccount.com
             variantsPattern: kubernetes-manifests
         target:
           fleet:
             project: projects/PROJECT_ID
             selector:
               matchLabels:
                 env: dev
         rolloutStrategy:
           rolling:
             maxConcurrent: 1
         variantSelector:
           variantNameTemplate: kubernetes-manifests
         

Replace `REPOSITORY_NAME` with the name of your repository, as it appears in the Cloud Build connection.

The selector fields match the fleet membership label that you created earlier. This helps ensure that the Cymbal Bank application is only deployed on the `scalable-apps-dev` cluster. The `scalable-apps` cluster from the first tutorial is unaffected. In the next section, you'll see an example of a fleet package that targets all clusters in a fleet.

The rollout strategy field controls how resources are deployed across clusters. In this example, you're deploying only to one cluster so this field doesn't change how the rollout proceeds. But if you had many clusters, this setting ensures that the resource files are all applied to one cluster before moving on to the next cluster. This lets you monitor how the rollout is progressing.

  3. Create the fleet package:
         
         gcloud container fleet packages create cymbal-bank-fleet-package \
             --source=fleetpackage-spec.yaml \
             --project=PROJECT_ID
         

  4. Verify that the fleet package was created:
         
         gcloud container fleet packages list
         

The output lists the status of the build trigger. After a few seconds, the `MESSAGE` field updates with output similar to the following:
         
         MESSAGES: Build status: WORKING. The release is still being built; see the build status on the following page:
         

You can click the link provided to view the streaming logs for the Cloud Build job. It can take a few minutes for Cloud Build to process the build trigger.

  5. When the build trigger successfully completes, the output of `gcloud container fleet packages list` is similar to the following:
         
         NAME: cymbal-bank-fleet-package
         STATE: ACTIVE
         CREATE_TIME: 2024-07-09T15:15:56
         ACTIVE_ROLLOUT: rollout-20240709-153621
         LAST_COMPLETED_ROLLOUT:
         MESSAGES:
         

The fleet package starts rolling out the Kubernetes resources across your fleet.

  6. In the Google Kubernetes Engine page of the Google Cloud console, select your `scalable-apps-dev` cluster, then go to the **Workloads** page to see an aggregated view of the workloads that are being deployed on all your GKE clusters:

[Open the Workloads page](https://console.cloud.google.com/kubernetes/workload/overview)

You might see some errors while Autopilot adjusts your Pods to meet resource requests. After a few minutes, you should see your Pods start running with the status **OK**.

  7. To view the Cymbal Bank web interface, complete the following steps:

     1. In the Google Kubernetes Engine page of the Google Cloud console, go to the **Gateways, Services & Ingress** page.

[Go to the Gateways, Services & Ingress page](https://console.cloud.google.com/kubernetes/gateways)

     2. To find the Cymbal Bank ingress, click the tab for "Services" and find the service with the name `frontend`.

     3. Click the _Endpoint_ link for the `frontend` ingress, such as `198.51.100.143:80`, to open to the Cymbal Bank web interface.


**Success:** You've deployed Cymbal Bank to a development cluster by using a fleet package. Now you have the Cymbal Bank app running in two different clusters.

## Deploy resources across a fleet

Next, imagine a scenario where you want to extend your Cymbal Bank application with a new microservice. You want to deploy this microservice across all your current clusters and any future clusters added to the fleet. By using a fleet package, you can deploy to multiple clusters and get automatic deployment on new clusters.

### Add new resources to your Git repository

To demonstrate adding a new service to your application, you create a basic nginx deployment and add it to your clusters:

  1. In a web browser window of your GitHub fork of Cymbal Bank, click **Add file** and then **Create new file**.

  2. Name your file `new-resource/nginx.yaml` and paste the following contents into it:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-deployment
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: nginx
           template:
             metadata:
               labels:
                 app: nginx
             spec:
               containers:
               - image: nginx:1.14.2
                 name: nginx
                 ports:
                 - containerPort: 80
         

  3. Click **Commit changes...**

  4. In the confirmation dialog, keep **Commit directly to the`main` branch** selected and then click **Commit changes**.

**Note:** In a real scenario, you'd probably create a new pull request instead so that your change can be reviewed and approved.
  5. On the main page of your forked Cymbal Bank repository, select **Releases** from the sidebar.

  6. At the top of the page, choose **Draft a new release.**

  7. Select the **Choose a tag** menu and type `v1.1.0` as the tag. Click **Create new tag.**

  8. Click **Publish release**.




### Deploy a resource to clusters with a fleet package

To deploy the new resource, create a new fleet package:

  1. This fleet package targets all of the clusters in your fleet since it doesn't contain a selector field. This also means any future clusters added to the fleet will have the nginx deployment automatically added.

In your Cloud Shell, create a file named `new-deployment-fleet-package.yaml` with the following content:
         
         resourceBundleSelector:
           cloudBuildRepository:
             name: projects/PROJECT_ID/locations/us-central1/connections/cymbal-bank-connection/repositories/REPOSITORY_NAME
             tag: v1.1.0
             serviceAccount: projects/PROJECT_ID/serviceAccounts/cymbal-bank-service-account@PROJECT_ID.iam.gserviceaccount.com
             variantsPattern: kubernetes-manifests/new-resource
         target:
           fleet:
             project: projects/PROJECT_ID
         rolloutStrategy:
           rolling:
             maxConcurrent: 1
         variantSelector:
           variantNameTemplate: new-resource
         

  2. Create the fleet package to start the rollout:
         
         gcloud container fleet packages create new-deployment-fleet-package \
             --source=new-deployment-fleet-package.yaml \
             --project=PROJECT_ID
         

  3. Verify that the fleet package was created:
         
         gcloud container fleet packages list
         

You can click the link provided to view the streaming logs for the Cloud Build job.

The fleet package starts rolling out the Kubernetes resources across your fleet. It can take a few minutes for the rollout to begin and complete.

  4. In the Google Kubernetes Engine page of the Google Cloud console, go to the **Workloads** page to see an aggregated view of the workloads that are being deployed on all your GKE clusters:

[Open the Workloads page](https://console.cloud.google.com/kubernetes/workload/overview)


**Success:** You used a single fleet package to add a new deployment sourced in a Git repository to two clusters.

You can continue to explore different deployment strategies with fleet packages. For example, you can try adding different types of resources to your forked repository and using different fleet package configurations to deploy them. You can also use a fleet package to delete any resources you deployed across your clusters. For more information about fleet packages, see [Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages) in the Config Sync documentation.

## Delete resources across a fleet

Just like you can deploy resources across a fleet, you can delete resources across a fleet with a fleet package.

To remove individual resources, the high-level steps are the following:

  1. Delete the resource from your Git repository.
  2. Create a new Git release and create a new tag.
  3. Update the fleet package `tag` field.
  4. Run the [fleet package update command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#update).



Alternatively, you can delete the fleet package itself, which also deletes any resources that were managed by the fleet package.

For example, if you want to remove the nginx deployment from the previous section, run the following command:
    
    
    gcloud container fleet packages delete new-deployment-fleet-package --force
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the project you created.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



You can delete your forked repository by completing the following steps:

  1. In a web browser window of your GitHub fork of Cymbal Bank, under your repository name, click **Settings**.

  2. On the General settings page (which is selected by default), go to the Danger Zone section and click **Delete this repository**.

  3. Click **I want to delete this repository**.

  4. Read the warnings and click **I have read and understand these effects**.

  5. To verify that you're deleting the correct repository, in the text field, type the name of the forked Cymbal Bank repository.

  6. Click **Delete this repository**.




## What's next

Before you start to create your own GKE cluster environment similar to the one you learned about in this set of tutorials, [review some of the production considerations](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-considerations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
