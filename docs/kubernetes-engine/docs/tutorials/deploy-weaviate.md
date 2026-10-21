---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-weaviate/
title: Deploy a Weaviate vector database on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:24:11.412682+00:00
---

# Deploy a Weaviate vector database on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-weaviate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy a Weaviate vector database on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to deploy a [Weaviate](https://weaviate.io/) vector database cluster on Google Kubernetes Engine (GKE).

Weaviate is an open-source vector database with low-latency performance and basic support for different media types such as text and images. It supports semantic search, question answering, and classification. Weaviate is fully built on Go and it stores both objects and vectors, allowing the use of vector search, keyword search, and a combination of both as a hybrid search. From an infrastructure perspective, Weaviate is a cloud-native and fault-tolerant database. Fault tolerance is delivered by leaderless architecture where each node of the database cluster can serve read and write requests which in turn excludes a single point of failure.

This tutorial is intended for cloud platform [administrators and architects](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins), [ML engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer), and MLOps (DevOps) professionals interested in deploying vector database clusters on GKE.

## Benefits

Weaviate offers the following benefits:

  * Libraries for various programming languages and open API to integrate with other services.
  * Horizontal scaling.
  * A balance between cost-effectiveness and query speed, especially when dealing with large datasets. You can choose how much data is stored in memory versus on disk.



## Objectives

In this tutorial, you learn how to:

  * Plan and deploy GKE infrastructure for Weaviate.
  * Deploy and configure the Weaviate database in a GKE cluster.
  * Run a Notebook to generate and store example vector embeddings within your database, and perform vector-based search queries.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), [kubectl](https://kubernetes.io/docs/reference/kubectl/), [Helm](https://helm.sh/) and[ Terraform](https://docs.cloud.google.com/docs/terraform) command-line tools. If you don't use Cloud Shell, you must install the Google Cloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Resource Manager, Compute Engine, GKE, and IAM Service Account Credentials APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Resource Manager, Compute Engine, GKE, and IAM Service Account Credentials APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/compute.securityAdmin, roles/compute.viewer, roles/container.clusterAdmin, roles/container.admin, roles/iam.serviceAccountAdmin, roles/iam.serviceAccountUser, roles/monitoring.viewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Set up your environment

To set up your environment with Cloud Shell, follow these steps:

  1. Set environment variables for your project, region, and a Kubernetes cluster resource prefix:
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=weaviate
         export REGION=us-central1
         

Replace `PROJECT_ID` with your Google Cloud project ID.

This tutorial uses `us-central1` region to create your deployment resources.

  2. Check the version of Helm:
         
         helm version
         

Update the version if it's older than 3.13:
         
         curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
         

  3. Clone the sample code repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Navigate to the `weaviate` directory:
         
         cd kubernetes-engine-samples/databases/weaviate
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a private, highly-available, regional GKE cluster to deploy your Weaviate database.

You can choose to deploy Weaviate using a [Standard or Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode). Each has its own advantages and different pricing models.

###  Autopilot 

The following diagram shows an Autopilot GKE cluster deployed in the project.

![GKE Autopilot cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/weaviate-gke-autopilot.svg)

To deploy the cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-autopilot init
    terraform -chdir=terraform/gke-autopilot apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

GKE replaces the following variables at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN` uses the `gcloud auth print-access-token` command to retrieve an access token that authenticates interactions with various Google Cloud APIs
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in the Set up your environment section and assigned to the new relevant variables for the Autopilot cluster you are creating.



When prompted, type `yes`.

The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials weaviate-cluster --region us-central1"
    

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



###  Standard 

The following diagram shows a Standard private regional GKE cluster deployed across three different zones.

![GKE Standard cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/weaviate-gke-standard.svg)

To deploy the cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-standard init
    terraform -chdir=terraform/gke-standard apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

GKE replaces the following variables at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN` uses the `gcloud auth print-access-token` command to retrieve an access token that authenticates interactions with various Google Cloud APIs.
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in Set up your environment section and assigned to the new relevant variables for the Standard cluster that you are creating.



When prompted, type `yes`. It might take several minutes for these commands to complete and for the cluster to show a ready status.

The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 10 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials weaviate-cluster --region us-central1"
    

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region with autoscaling enabled (one to two nodes per zone).
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



### Connect to the cluster

Configure `kubectl` to fetch credentials and communicate with your new GKE cluster:
    
    
    gcloud container clusters get-credentials \
        ${KUBERNETES_CLUSTER_PREFIX}-cluster --location ${REGION}
    

## Deploy the Weaviate database to your cluster

To use Helm chart to deploy the Weaviate database to your GKE cluster, follow these steps:

  1. Add the Weaviate database Helm Chart repository before you can deploy it on your GKE cluster:
         
         helm repo add weaviate https://weaviate.github.io/weaviate-helm
         

  2. Create the namespace `weaviate` for the database:
         
         kubectl create ns weaviate
         

  3. Create a secret to store the API key:
         
         kubectl create secret generic apikeys --from-literal=AUTHENTICATION_APIKEY_ALLOWED_KEYS=$(openssl rand -base64 32) -n weaviate
         

  4. Deploy an internal load balancer to access Weaviate from within the virtual network:
         
         kubectl apply -n weaviate -f manifests/05-ilb/ilb.yaml
         

The `ilb.yaml` manifest describes the load balancer service:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             #cloud.google.com/neg: '{"ingress": true}'
             networking.gke.io/load-balancer-type: "Internal"
           labels:
             app.kubernetes.io/name: weaviate
           name: weaviate-ilb
         spec:
           ports:
           - name: http
             port: 8080
             protocol: TCP
             targetPort: 8080
           - name: grpc
             port: 50051
             protocol: TCP
             targetPort: 50051
           selector:
             app: weaviate
           type: LoadBalancer

  5. Apply the manifest to deploy Weaviate cluster:
         
         helm upgrade --install "weaviate" weaviate/weaviate \
         --namespace "weaviate" \
         --values ./manifests/01-basic-cluster/weaviate_cluster.yaml
         

The `weaviate_cluster.yaml` manifest describes the Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.:
         
         initContainers:
           sysctlInitContainer:
             enabled: false
           extraInitContainers: {}
         resources: 
            requests:
              cpu: '1'
              memory: '4Gi'
            limits:
              cpu: '2'
              memory: '4Gi'
         replicas: 3
         storage:
           size: 10Gi
           storageClassName: "premium-rwo"
         service:
           name: weaviate
           ports:
             - name: http
               protocol: TCP
               port: 80
           type: ClusterIP
         grpcService:
           enabled: true
           name: weaviate-grpc
           ports:
             - name: grpc
               protocol: TCP
               port: 50051
           type: ClusterIP
         authentication:
           anonymous_access:
             enabled: false
         authorization:
           admin_list:
             enabled: true
             users:
               - admin@example.com
         modules:
           text2vec-palm:
             enabled: true
         env:
           AUTHENTICATION_APIKEY_ENABLED: 'true'
           AUTHENTICATION_APIKEY_USERS: 'admin@example.com'
           PROMETHEUS_MONITORING_ENABLED: true
         envSecrets:
           AUTHENTICATION_APIKEY_ALLOWED_KEYS: apikeys
         tolerations:
           - key: "app.stateful/component"
             operator: "Equal"
             value: "weaviate"
             effect: NoSchedule

Wait for a few minutes for the Weaviate cluster to fully start.

  6. Check the Deployment status:
         
         kubectl get weaviate -n weaviate --watch
         

The output is similar to following, if the `weaviate` database is successfully deployed:
         
         NAME: weaviate
         LAST DEPLOYED: Tue Jun 18 13:15:53 2024
         NAMESPACE: weaviate
         STATUS: deployed
         REVISION: 1
         TEST SUITE: None
         

  7. Wait for Kubernetes to start the resources:
         
         kubectl wait pods -l app.kubernetes.io/name=weaviate --for condition=Ready --timeout=300s -n weaviate
         




## Run queries with Vertex AI Colab Enterprise notebook

This section explains how to connect to your Weaviate database using Colab Enterprise. You can use a dedicated runtime template to deploy to the `weaviate-vpc`, so the notebook can communicate with resources in the GKE cluster.

For more information about Vertex AI Colab Enterprise, see [Colab Enterprise documentation](https://docs.cloud.google.com/colab/docs/introduction).

### Create a runtime template

To create a Colab Enterprise runtime template:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime Templates** page and make sure your project is selected:

[Go to Runtime Templates](https://console.cloud.google.com/vertex-ai/colab/runtime-templates)

  2. Click _add_box_ **New Template**. The **Create new runtime template** page appears.

  3. In the **Runtime basics** section: 

     * In the **Display name** field, enter `weaviate-connect`.
     * In the **Region** drop-down list, select `us-central1`. It's the same region as your GKE cluster.
  4. In the **Configure compute** section: 

     * In the **Machine type** drop-down list, select `e2-standard-2`.
     * In the **Disk size** field, enter `30`.
  5. In the **Networking and security** section:

     * In the **Network** drop-down list, select the network where your GKE cluster resides.
     * In the **Subnetwork** drop-down list, select a corresponding subnetwork.
     * Clear the **Enable public internet access** checkbox.
  6. To finish creating the runtime template, click **Create**. Your runtime template appears in the list on the **Runtime templates** tab.




### Create a runtime

To create a Colab Enterprise runtime:

  1. In the runtime templates list for the template you just created, in the **Actions** column, click _more_vert_ and then click **Create runtime**. The **Create Vertex AI Runtime** pane appears.

  2. To create a runtime based on your template, click **Create**.

  3. On the **Runtimes** tab that opens, wait for the status to transition to **Healthy**.




### Import the notebook

To import the notebook in Colab Enterprise:

  1. Go to the **My Notebooks** tab and click **Import**. The **Import notebooks** pane appears.

  2. In **Import source** , select **URL**.

  3. Under **Notebook URLs** , enter the following link:
         
         https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/databases/weaviate/manifests/02-notebook/vector-database.ipynb
         

  4. Click **Import**.




### Connect to the runtime and run queries

To connect to the runtime and run queries:

  1. In the notebook, next to the **Connect** button, click _arrow_drop_down_ **Additional connection options**. The **Connect to Vertex AI Runtime** pane appears.

  2. Select **Connect to a runtime** and then select **Connect to an existing Runtime**.

  3. Select the runtime that you launched and click **Connect**.

  4. To run the notebook cells, click the ![](https://docs.cloud.google.com/static/colab/images/icon-run-cell.png)**Run cell** button next to each code cell.




The notebook contains both code cells and text that describes each code block. Running a code cell executes its commands and displays an output. You can run the cells in order, or run individual cells as needed.

## View Prometheus metrics for your cluster

The GKE cluster is configured with [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which enables collection of metrics in the Prometheus format. This service provides a fully managed solution for monitoring and alerting, allowing for collection, storage, and analysis of metrics from the cluster and its applications.

The following diagram shows how Prometheus collects metrics for your cluster:

![Prometheus metrics collection](https://docs.cloud.google.com/static/kubernetes-engine/images/weaviate-monitoring.svg)

The GKE private cluster in the diagram contains the following components:

  * Weaviate Pods that expose metrics on the path `/metrics` and port `2112`.
  * Prometheus-based collectors that process the metrics from the Weaviate Pods.
  * A PodMonitoring resource that sends the metrics to Cloud Monitoring.



To export and view the metrics, follow these steps:

  1. Create the [`PodMonitoring`](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) resource to scrape metrics by `labelSelector`:
         
         kubectl apply -n weaviate -f manifests/03-prometheus-metrics/pod-monitoring.yaml
         

The `pod-monitoring.yaml` manifest describes the `PodMonitoring` resource:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: weaviate
         spec:
           selector:
             matchLabels:
               app: weaviate
           endpoints:
           - port: 2112
             interval: 30s
             path: /metrics

  2. To import a custom [Cloud Monitoring dashboard](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create) with the configurations defined in `dashboard.json`:
         
         gcloud --project "${PROJECT_ID}" monitoring dashboards create --config-from-file monitoring/dashboard.json
         

  3. After the command runs successfully, go to the Cloud Monitoring [Dashboards](https://docs.cloud.google.com/monitoring/dashboards):

[Go to Dashboards overview](https://console.cloud.google.com/monitoring/dashboards)

  4. From the list of dashboards, open the `Weaviate Overview` dashboard. It might take some time to collect and display metrics. The dashboard shows amount of Shards, Vectors and operations latency




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to avoid billing is to delete the project you created for this tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you deleted the project, your clean up is complete. If you didn't delete the project, proceed to delete the individual resources.

### Delete individual resources

  1. Set environment variables.
         
         export PROJECT_ID=${PROJECT_ID}
         export KUBERNETES_CLUSTER_PREFIX=weaviate
         export REGION=us-central1
         

  2. Run the `terraform destroy` command:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform  -chdir=terraform/FOLDER destroy \
         -var project_id=${PROJECT_ID} \
         -var region=${REGION} \
         -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
         

Replace `FOLDER` with either `gke-autopilot` or `gke-standard`, depending on the type of GKE cluster you created.

When prompted, type `yes`.

  3. Find all unattached disks:
         
         export disk_list=$(gcloud compute disks list --filter="-users:* AND labels.name=${KUBERNETES_CLUSTER_PREFIX}-cluster" --format "value[separator=|](name,region)")
         

  4. Delete the disks:
         
         for i in $disk_list; do
          disk_name=$(echo $i| cut -d'|' -f1)
          disk_region=$(echo $i| cut -d'|' -f2|sed 's|.*/||')
          echo "Deleting $disk_name"
          gcloud compute disks delete $disk_name --region $disk_region --quiet
         done
         

  5. Delete the GitHub repository:
         
         rm -r ~/kubernetes-engine-samples/
         




## What's next

  * Explore [Weaviate on GKE marketplace](https://console.cloud.google.com/marketplace/product/mp-container-public/weaviate-gcp-k8s).
  * Learn about the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * Discover solutions for running [data-intensive workloads with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
