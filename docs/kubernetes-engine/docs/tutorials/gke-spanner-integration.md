---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gke-spanner-integration/
title: Deploy an app using GKE Autopilot and Spanner \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:44.658160+00:00
---

# Deploy an app using GKE Autopilot and Spanner  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gke-spanner-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy an app using GKE Autopilot and Spanner Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This tutorial shows you how to deploy a containerized web application on a Google Kubernetes Engine (GKE) Autopilot cluster with a Spanner database backend. You can build and deploy scalable, reliable web applications without managing complex infrastructure by using GKE Autopilot clusters and Spanner. GKE automatically provisions and manages your Kubernetes cluster resources, reducing operational overhead. Spanner is a fully managed, globally distributed relational database that provides high performance and availability with ACID transactions and SQL semantics.

Before reading this page, ensure that you're familiar with [Kubernetes](https://kubernetes.io).

This document is for developers and cloud platform administrators. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Why GKE and Spanner

As a developer, you might not want to spend time figuring out the amount of storage and compute resources your application needs, or predicting RAM and CPU consumption during periods of fluctuating demands, or worrying about application failure at peak load.

By using GKE Autopilot as a fully managed Kubernetes service, and Spanner as a fully managed database service, you can develop and deploy apps faster on a stable infrastructure that simplifies configuring and managing resources. GKE Autopilot handles configuring and scaling the infrastructure for hosting your app by adding or removing nodes to or from the cluster, based on the requirements at runtime. Similarly, Spanner can dynamically scale out and in with minimal manual intervention, as storage or compute requirements change.

For example, consider you are launching the next blockbuster game which you expect to go viral, and therefore attract heavy web traffic during its launch week. Spanner can help you accommodate this surging throughput by providing the ability to instantly increase, decrease, or reallocate compute resources while still maintaining maximum application availability with GKE Autopilot.

## Objectives

In this tutorial, you learn how to:

  * Create a Spanner database that stores a registry of players.

  * Deploy a sample web app called `hello-app-cloud-spanner`, with a graphical user interface.




The following table describes the Google Cloud resources you create or use, the variables they are identified with, and the values prescribed for them for the purpose of this tutorial:

Resource | Variable | Value  
---|---|---  
Google Cloud project ID | `PROJECT_ID` | The [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#:~:text=to%20be%20unique.-,Project%20ID,-%3A%20A%20globally%20unique) generated when you create a project.  Example: `my-gcp-project`  
Compute region | `COMPUTE_REGION` |  The [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where you want to create the Spanner instance and GKE cluster. We recommend that you choose a region closest to your customers' geographical location, but for this tutorial, use `us-west1`.   
Spanner instance | - | `hello-instance`  
Spanner database | - | `hello-database`  
GKE Autopilot cluster | `CLUSTER_NAME` | `hello-cluster`  
Kubernetes namespace | `NAMESPACE` | `hello-namespace`  
[Kubernetes service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#kubernetes-service-accounts) | `KUBERNETES_SERVICEACCOUNT` | `ksa-helloapp`  
  
For the purpose of this tutorial, we recommend creating new resources, which makes deleting them easy and risk free after you have deployed the sample app. However, if you have any existing namespaces and Kubernetes service accounts, you can use them.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/disks-image-pricing) instances used by GKE
  * [Spanner](https://cloud.google.com/spanner/pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Make sure to complete the following prerequisites:

### Select or create a project

You can use an existing project, or create a new one for this tutorial.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Enable the APIs

Enable the Artifact Registry, Compute Engine, GKE, IAM Service Account Credentials, and Spanner APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,compute.googleapis.com,container.googleapis.com,iamcredentials.googleapis.com,spanner.googleapis.com)

### Set up Cloud Shell

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run `gcloud` and `kubectl` commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line tool.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

A Cloud Shell session opens inside a frame lower on the console.

Before you run commands in this tutorial, make sure that your default project is set to the project ID where you want to deploy the sample app. If it's not already set, run the following command in the Cloud Shell:
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

### Grant IAM roles

Ensure that your Google Cloud account has the required [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions) for this tutorial.

Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountAdmin, roles/serviceusage.serviceUsageConsumer, roles/iam.serviceAccountUser, roles/iam.securityAdmin, roles/spanner.admin, roles/container.admin`
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
  * `ROLE`: The IAM role that you grant to your user account.



## Configure Spanner

To configure Spanner, you need to create a Spanner instance and a Spanner database.

### Create a Spanner instance

A Spanner instance is an allocation of resources that is used by Spanner databases created in that instance.

Create a Spanner instance called `hello-instance` with a regional configuration, and compute capacity of `100` processing units.
    
    
    gcloud spanner instances create hello-instance \
      --config=regional-COMPUTE_REGION \
      --description="Spanner sample instance" \
      --processing-units=100
    

Replace `COMPUTE_REGION` with `us-west1` for this tutorial.

### Create a Spanner database

A Spanner database includes your tables, views, and indexes. A database inherits properties from its parent instance, such as its [configuration](https://docs.cloud.google.com/spanner/docs/instance-configurations) (regional or multi-regional), available [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity), and storage.

Create a Spanner database called `hello-database` with a table called `Players`, by using the GoogleSQL dialect. Run the following query in your Cloud Shell:
    
    
    gcloud spanner databases create hello-database \
      --instance=hello-instance \
      --database-dialect=GOOGLE_STANDARD_SQL \
      --ddl="CREATE TABLE Players (
        PlayerUuid STRING(36) NOT NULL,
        FirstName STRING(1024),
        LastName STRING(1024),
        BirthDate DATE) PRIMARY KEY(PlayerUuid)"
    

## Create a GKE Autopilot cluster

After you've configured Spanner, create an Autopilot cluster and use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) to access your database in a secure and manageable way.

Create an Autopilot cluster named `hello-cluster`. Autopilot clusters have Workload Identity Federation for GKE enabled by default.
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
     --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: `hello-cluster`
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. For this tutorial, use the same region, `us-west1`, where you created the Spanner instance. We recommend that you create the Spanner instance and the GKE Autopilot cluster within the same region to reduce latency.



It can take up to 8-10 minutes to create the cluster.

The output is similar to the following:
    
    
    NAME: hello-cluster
    LOCATION: us-west1
    MASTER_VERSION: 1.26.5-gke.1200
    MASTER_IP: 192.0.2.1
    MACHINE_TYPE: e2-medium
    NODE_VERSION: 1.26.5-gke.1200
    NUM_NODES: 3
    STATUS: RUNNING
    

## Configure the cluster to use Workload Identity Federation for GKE

Configure your cluster to authenticate to Google Cloud using Workload Identity Federation for GKE before you deploy the app.

  1. [Get credentials](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials) to access your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
          --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: `hello-cluster`
     * `CONTROL_PLANE_LOCATION`: `us-west1`

This updates a `kubeconfig` file with appropriate credentials and endpoint information to point `kubectl` at your cluster.

  2. Create a namespace to use for the Kubernetes service account. You can also use the default namespace, or any existing namespace.
         
         kubectl create namespace NAMESPACE
         

Replace `NAMESPACE` with `hello-namespace`, the name for the new namespace you are creating.

  3. Create a Kubernetes service account for your application to use:
         
         kubectl create serviceaccount KUBERNETES_SERVICEACCOUNT \
          --namespace NAMESPACE
         

Replace the following:

     * `KUBERNETES_SERVICEACCOUNT`: `ksa-helloapp`, the name for the new Kubernetes service account you are creating.
     * `NAMESPACE`: `hello-namespace`
  4. Add an [IAM policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) for your Kubernetes ServiceAccount to read and write to Spanner:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
          --role="roles/spanner.admin" \
          --condition=None
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID
     * `PROJECT_NUMBER`: your Google Cloud project number
     * `NAMESPACE`: `hello-namespace`
     * `KUBERNETES_SERVICEACCOUNT`: `ksa-helloapp`

Example:
    
    gcloud projects add-iam-policy-binding my-gcp-project \
    --member="principal://iam.googleapis.com/projects/123456789012/locations/global/workloadIdentityPools/my-gcp-project.svc.id.goog/subject/ns/hello-namespace/sa/ksa-helloapp" \
    --role="roles/spanner.admin" \
    --condition=None




## Deploy the sample app to the cluster

Now that you have set up GKE and Spanner with the necessary services and authentication, you are ready to deploy the sample app `hello-app-cloud-spanner`.

  1. Clone the sample app from the GitHub repository to your Cloud Shell:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  2. Launch the Cloud Shell Editor by clicking ![Code Editor Button](https://docs.cloud.google.com/static/code/docs/shell/images/open-editor.png)**Open Editor** on the toolbar of the terminal window.

For more information, see [Cloud Shell Editor interface overview](https://docs.cloud.google.com/shell/docs/editor-overview).

  3. Open the Cloud Shell Editor's Explorer pane, and browse to the `kubernetes-engine-samples/databases/hello-app-cloud-spanner/k8s` directory.

  4. Open the `deployment.yaml` file, and update the `serviceAccountName` field by replacing `<KSA_NAME>` with `ksa-helloapp`, the name of your Kubernetes service account.

![Edit yaml to update the Kubernetes service account name.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-spanner-yaml-edited.png)**Figure 1.** Update Kubernetes service account name in the deployment file. 
  5. Close the Cloud Shell Editor, and return to the Cloud Shell terminal.

  6. In the Cloud Shell terminal, navigate to the `hello-app-cloud-spanner` directory:
         
         cd kubernetes-engine-samples/databases/hello-app-cloud-spanner
         

  7. Deploy the application:
         
         kubectl apply -f k8s/deployment.yaml -n=NAMESPACE
         

Replace `NAMESPACE` with `hello-namespace`.

  8. Wait for the application to be deployed with `STATUS` as `Running`:
         
         kubectl get pods -n=NAMESPACE --watch
         

Replace `NAMESPACE` with `hello-namespace`.

The output is similar to the following:
         
         NAME                    READY  STATUS       RESTARTS  AGE
         hello-app-cloud-spanner-765c9b8779-lfcrc  0/1   ContainerCreating  0     87s
         hello-app-cloud-spanner-765c9b8779-lfcrc  1/1   Running       0     3m15s
         

  9. Press Ctrl+C on your keyboard to return to the command prompt to run further commands.




### Expose the sample app to the internet

To expose a Kubernetes Service outside the cluster, create a Service of type [`LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases#ext-lb). This type of Service generates an external load balancer IP address for your Pods, reachable through the internet.

  1. Deploy the load balancer:
         
         kubectl apply -f k8s/service.yaml -n=NAMESPACE
         

Replace `NAMESPACE` with `hello-namespace`.

  2. Watch for an external IP address to be assigned:
         
         kubectl get service -n=NAMESPACE --watch
         

Replace `NAMESPACE` with `hello-namespace`.

  3. Once assigned, copy the `EXTERNAL-IP` (for example, `203.0.113.0`) and open it in a browser. A web interface opens that displays and manages the database of players.

  4. You can use the app GUI to create or delete player records, and they are saved in the Spanner database.

![Add or delete players.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-spanner-integration.png)**Figure 2.** Create or delete players in the registry.

Run the following query to verify if the Spanner database has been updated with your entries:
         
         gcloud spanner databases execute-sql hello-database \
          --instance=hello-instance \
          --sql="SELECT * FROM Players LIMIT 10"
         

The output is similar to the following:
         
         PlayerUuid: a1f34bbf-929c-498d-8b16-39bbb29d70e3
         FirstName: John
         LastName: Smith
         BirthDate: 1997-07-12
         
         PlayerUuid: d634e157-96ea-45f2-be3f-fb907ced188e
         FirstName: Jane
         LastName: Doe
         BirthDate: 2013-07-12
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your project

The easiest way to avoid billing is to delete the project you created for this tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you deleted the project, your clean up is complete. If you didn't delete the project, proceed to delete the GKE and Spanner resources.

### Delete GKE resources

  1. Delete the service. This deallocates the Google Cloud load balancer created for your Service:
         
         kubectl delete service hello-app-cloud-spanner -n=NAMESPACE
         

Replace `NAMESPACE` with `hello-namespace`.

  2. Delete the GKE cluster. This deletes the resources that constitute a cluster, such as the compute instances, disks, and network resources:
         
         gcloud container clusters delete CLUSTER_NAME --location=CONTROL_PLANE_LOCATION
         




### Delete Spanner resources

  1. Delete the Spanner database:
         
         gcloud spanner databases delete hello-database --instance=hello-instance
         

  2. Delete the Spanner instance:

**Caution** : Deleting an instance permanently removes the instance, and all its databases. 
         
         gcloud spanner instances delete hello-instance
         




## What's next

  * Learn how to [create a GKE cluster for your Agones install](https://agones.dev/site/docs/installation/creating-cluster/gke/).
  * Learn the [best practices for using Spanner as a gaming database](https://docs.cloud.google.com/spanner/docs/best-practices-gaming-database).
  * Learn the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
