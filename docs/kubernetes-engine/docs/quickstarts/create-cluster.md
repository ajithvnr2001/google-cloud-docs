---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster/
title: Quickstart: Create a cluster and deploy a workload \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:00.372449+00:00
---

# Quickstart: Create a cluster and deploy a workload  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster and deploy a workload in the Google Cloud console

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

A Kubernetes _cluster_ provides compute, storage, networking, and other services for applications, similar to a virtual data center. Apps and their associated services that run in Kubernetes are called _workloads_.

This tutorial lets you quickly see a running Google Kubernetes Engine cluster and sample workload, all set up using the Google Cloud console. You can then explore the workload in the Google Cloud console before going on to our [more in-depth learning path](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps), or to start planning and creating your own production-ready cluster.

If you'd prefer to set up your sample cluster and workload by using Terraform, see [Create a cluster with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/kubernetes/list/overview?walkthrough_id=kubernetes--create-cluster)

* * *

## Before you begin

Take the following steps to enable the Kubernetes Engine API: 

  1. Visit the [ Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes) in the Google Cloud console. 
  2. Create or select a project. 
  3. Wait for the API and related services to be enabled. This can take several minutes. 
  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

Make sure that you have the following role or roles on the project: Compute Admin, Kubernetes Engine Admin, Service Account User 

#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



## Create a cluster in GKE Autopilot mode

In Autopilot mode, Google manages your cluster configuration, including scaling, security, and other preconfigured settings. Clusters in Autopilot mode are optimized to run most production workloads and provision compute resources based on your Kubernetes manifests.

  1. In the Google Cloud console, go to the GKE **Create an Autopilot cluster** page.

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. Under **Cluster basics** , do the following:

     1. In the **Name** field, enter the following name:
            
            hello-world-cluster
            

     2. Keep the default values for the rest of the settings and click **Create** to start creating the cluster.

  3. When you're redirected to the **Kubernetes clusters** page, you can watch the progress of your cluster as it is being configured, deployed, and verified.

  4. Wait until you see a check mark next to the **hello-world-cluster** page title.




## Deploy a sample app to your cluster

Deploy a sample "hello world" web app provided by Google and stored as a container in Artifact Registry.

  1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click **Deploy**.

  3. In **Deployment name** , enter the following name:
         
         hello-world-app
         

  4. In Kubernetes Cluster, select **hello-world-cluster**.

  5. Click **Next: Container details**

  6. Leave **Existing container image** selected, and in **Image path** enter the following path:
         
         us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

This simple "hello world" app is packaged into a single container, but larger apps typically consist of several related containers that can be deployed together and run as a single workload.

  7. Click **Next: Expose (optional)**

  8. In the **Expose** section, create a load balancing Kubernetes Service to direct external requests to your app:

     1. Select **Expose deployment as a new service**.

     2. Leave **Port 1** set to **80**.

     3. In **Target port 1** , enter **8080**.

     4. Click **Deploy**.

GKE automatically assigns an available external IP address to the Service.

This Service is considered to be part of the hello-world-app workload.

  9. For Autopilot clusters, you might see an error message, such as `Does not have minimum availability`. This occurs because Autopilot deletes and then re-creates the nodes. Wait a few minutes, then click refreshRefresh to update the page.

  10. Wait until the deployment completes and you see the **Deployment details** page.




## View a live demo in your browser

  1. In the Google Cloud console, go to the **Deployment details** page for **hello-world-app** :

     1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

     2. In the **Name** column, click the name of the workload you deployed, **hello-world-app**.

  2. In the Endpoints column, click the IP address, which is publicly available.

GKE opens a new browser tab and sends a request to your app. Dismiss any secure-site warnings, and you should see **Hello, world!** in the new browser tab.

If **Endpoints** is empty, your organization might have a policy that prevents external access.




You have successfully created a GKE cluster in Autopilot mode and deployed a sample workload.

## Clean up to avoid billing charges

If you plan to take additional tutorials or to [explore your sample further](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster), wait until you're finished to perform this cleanup step. You can continue to use the sample Kubernetes cluster in most GKE tutorials.

If you created a new project to learn about GKE and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing GKE project, delete the resources you created to avoid incurring charges to your account:

  1. Go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the row containing **hello-world-cluster** , and click **Delete**.

  3. In the **Delete hello-world-cluster** window, do the following:

     1. In the **hello-world-cluster** field, enter `hello-world-cluster`.

     2. Click **Delete**.

If you receive an error message about the cluster being repaired, you can wait for the process to complete, and then delete the cluster. This operation might take some time to complete.

  4. If you created a logs sink and bucket when following instructions in other tutorials:

     1. Go to the Cloud Logging **Logs storage** page.

[Go to Logs storage](https://console.cloud.google.com/logs/storage)

     2. Select **hello-world-cluster-bucket** and click **Delete**.

     3. Go to the Logging **Log router** page.

[Go to Log router](https://console.cloud.google.com/logs/router)

     4. Select **hello-world-cluster-sink** and click **Delete**.




## What's next

  * [Explore your cluster and workload](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster) to learn about the some of the key workload settings and resources that you deployed.

  * Try our more in-depth [Learning path: Scalable apps](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps).

  * Learn how to get started with real life cluster administration in our [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
