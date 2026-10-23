---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-qdrant/
title: Deploy a Qdrant vector database on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:54.000824+00:00
---

# Deploy a Qdrant vector database on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-qdrant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy a Qdrant vector database on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to deploy a [Qdrant](https://qdrant.tech/documentation/) vector database cluster on Google Kubernetes Engine (GKE).

[Vector databases](https://cloud.google.com/discover/what-is-a-vector-database) are data stores specifically designed to manage and search through large collections of high-dimensional vectors. These vectors represent data like text, images, audio, video or any data that can be numerically encoded. Unlike traditional databases that rely on exact matches, vector databases specialize in finding similar items or identifying patterns within massive datasets. These characteristics make Qdrant a suitable choice for a variety of applications, including neural network or semantic-based matching, faceted search, and more. Qdrant not only functions as a vector database but also as a vector similarity search engine.

This tutorial is intended for cloud platform [administrators and architects](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins), [ML engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer), and MLOps (DevOps) professionals interested in deploying Qdrant database clusters on GKE.

## Benefits

Qdrant offers the following benefits:

  * Wide range of libraries for various programming languages and open API to integrate with other services.
  * Horizontal scaling, and support for sharding and replication that simplifies scaling and high availability.
  * Container and Kubernetes support that enables deployment and management in modern cloud-native environments.
  * Flexible payloads with [advanced filtering](https://qdrant.tech/documentation/concepts/filtering/) to tailor search criteria precisely.
  * [Different quantization options](https://qdrant.tech/documentation/guides/quantization/) and other optimizations to reduce infrastructure costs and improve performance.



## Objectives

In this tutorial, you learn how to:

  * Plan and deploy GKE infrastructure for Qdrant.
  * Deploy the [StatefulHA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha) operator to ensure Qdrant high availability.
  * Deploy and configure the Qdrant cluster.
  * Upload a demo dataset and run a simple search query.
  * Collect metrics and run a dashboard.



## Deployment architecture

This architecture sets up a fault-tolerant, scalable GKE cluster for Qdrant across multiple availability zones, ensuring uptime and availability with rolling updates and minimal disruption. It includes using the [StatefulHA operator](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/highavailabilityapplication) for efficient failover management. For more information, see [Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).

### Architecture diagram

The following diagram shows a Qdrant cluster running on multiple nodes and zones in a GKE cluster:

![Qdrant deployment architecture](https://docs.cloud.google.com/static/kubernetes-engine/images/qdrant-architecture.svg)

In this architecture, the Qdrant `StatefulSet` is deployed across three nodes in three different zones.

  * You can control how GKE distributes Pods across nodes by configuring the required Pod [affinity rules](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) and [topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) in the Helm chart values file.
  * If one zone fails, GKE reschedules Pods on new nodes based on the recommended configuration.



For data persistence, the architecture in this tutorial has the following characteristics:

  * It uses [regional](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) SSD disks (custom`regional-pd` [StorageClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#create_a_storageclass)) for persisting data. We [recommend](https://docs.cloud.google.com/compute/docs/disks/performance) regional SSD disks for databases due to their low latency and high IOPS.
  * All disk data is replicated between primary and secondary zones in the region, increasing tolerance to potential zone failures.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)
  * [Backup for GKE](https://cloud.google.com/backup-disaster-recovery/pricing)



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

  7. Enable the Resource Manager, Compute Engine, GKE, IAM Service Account Credentials, and Backup for GKE APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com gkebackup.googleapis.com

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

  13. Enable the Resource Manager, Compute Engine, GKE, IAM Service Account Credentials, and Backup for GKE APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com gkebackup.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer, roles/container.admin, roles/iam.serviceAccountAdmin, roles/compute.admin, roles/gkebackup.admin, roles/monitoring.viewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Set up your environment

To set up your environment with Cloud Shell, follow these steps:

  1. Set environment variables for your project, region, and a Kubernetes cluster resource prefix:

For the purpose of this tutorial, use `us-central1` region to create your deployment resources.
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=qdrant
         export REGION=us-central1
         

     * Replace `PROJECT_ID` with your Google Cloud project ID.
  2. Check the version of Helm:
         
         helm version
         

Update the version if it's older than 3.13:
         
         curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
         

  3. Clone the sample code repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Navigate to the `qdrant` directory to start creating deployment resources:
         
         cd kubernetes-engine-samples/databases/qdrant
         




## Create your cluster infrastructure

This section involves running a Terraform script to create a private, highly-available, regional GKE cluster to deploy your Qdrant database.

You can choose to deploy Qdrant using a [Standard or Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode). Each has its own advantages and different pricing models.

###  Autopilot 

The following diagram shows an Autopilot regional GKE cluster deployed across three different zones.

![GKE Autopilot cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-autopilot-qdrant.svg)

To deploy the cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-autopilot init
    terraform -chdir=terraform/gke-autopilot apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

The following variables are replaced at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN`: Replaced by an access token retrieved by `gcloud auth print-access-token` command to authenticate interactions with various Google Cloud APIs
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in Set up your environment section and assigned to the new relevant variables for the Autopilot cluster you are creating.



When prompted, type `yes`.

The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials qdrant-cluster --region us-central1"
    

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



###  Standard 

The following diagram shows a Standard private regional GKE cluster deployed across three different zones.

![GKE Standard cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-standard-qdrant.svg)

To deploy the cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-standard init
    terraform -chdir=terraform/gke-standard apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

The following variables are replaced at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN` is replaced by an access token retrieved by `gcloud auth print-access-token` command to authenticate interactions with various Google Cloud APIs.
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in Set up your environment section and assigned to the new relevant variables for the Standard cluster that you are creating.



When prompted, type `yes`. It might take several minutes for these commands to complete and for the cluster to show a ready status.

The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 10 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials qdrant-cluster --region us-central1"
    

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
    

## Deploy the Qdrant database to your cluster

In this tutorial, you deploy the Qdrant database (in [distributed mode](https://qdrant.tech/documentation/guides/distributed_deployment/)) and the Stateful HA operator to your GKE cluster cluster using the [Helm chart](https://github.com/qdrant/qdrant-helm).

The deployment creates a GKE cluster with the following configuration:

  * Three replicas of the Qdrant nodes.
  * Tolerations, node affinities, and topology spread constraints are configured to ensure proper distribution across Kubernetes nodes. This leverages the node pools and different availability zones.
  * A RePD volume with the SSD disk type is provisioned for data storage.
  * A Stateful HA operator is used to manage failover processes and ensure high availability. A StatefulSet is a Kubernetes controller that maintains a persistent unique identity for each of its Pods.
  * For authentication, the database creates a Kubernetes secret containing the API key.



To use the Helm chart to deploy Qdrant database, follow these steps:

  1. Enable the [StatefulHA add-on](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha#enable):

###  Autopilot 

GKE automatically enables the `StatefulHA` add-on at cluster creation.

###  Standard 

Run the following command:
         
         gcloud container clusters update ${KUBERNETES_CLUSTER_PREFIX}-cluster \
             --project=${PROJECT_ID} \
             --location=${REGION} \
             --update-addons=StatefulHA=ENABLED
         

It might take 15 minutes for this command to complete and for the cluster to show a ready status.

  2. Add the Qdrant database Helm Chart repository before you can deploy it on your GKE cluster:
         
         helm repo add qdrant https://qdrant.github.io/qdrant-helm
         

  3. Create namespace `qdrant` for the database:
         
         kubectl create ns qdrant
         

  4. Apply the manifest to create a regional persistent SSD disk `StorageClass`:
         
         kubectl apply -n qdrant -f manifests/01-regional-pd/regional-pd.yaml
         

The `regional-pd.yaml` manifest describes the persistent SSD disk `StorageClass`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         allowVolumeExpansion: true
         metadata:
           name: ha-regional
         parameters:
           replication-type: regional-pd
           type: pd-ssd
           availability-class: regional-hard-failover
         provisioner: pd.csi.storage.gke.io
         reclaimPolicy: Retain
         volumeBindingMode: WaitForFirstConsumer

  5. Deploy a Kubernetes configmap with a `metrics` sidecar configuration and a Qdrant cluster by using Helm:
         
         kubectl apply -n qdrant -f manifests/03-prometheus-metrics/metrics-cm.yaml
         helm install qdrant-database qdrant/qdrant -n qdrant \
         -f manifests/02-values-file/values.yaml
         

The `metrics-cm.yaml` manifest describes the `metrics` sidecar `ConfigMap`:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: nginx-conf
         data:
           default.conf.template: |
             server {
               listen 80;
               location / {
                 proxy_pass http://localhost:6333/metrics;
                 proxy_http_version 1.1;
                 proxy_set_header Host $http_host;
                 proxy_set_header api-key ${QDRANT_APIKEY};
                 proxy_set_header X-Forwarded-For $remote_addr;
               }
             }

The `values.yaml` manifest describes the Qdrant cluster configuration :
         
         replicaCount: 3
         
         config:
           service:
             enable_tls: false
           cluster:
             enabled: true
           storage:
             optimizers:
               deleted_threshold: 0.5
               vacuum_min_vector_number: 1500
               default_segment_number: 2
               max_segment_size_kb: null
               memmap_threshold_kb: null
               indexing_threshold_kb: 25000
               flush_interval_sec: 5
               max_optimization_threads: 1
         
         livenessProbe:
           enabled: true
           initialDelaySeconds: 60
         
         resources:
           limits:
             cpu: "2"
             memory: 4Gi
           requests:
             cpu: "1"
             memory: 4Gi
         
         tolerations:
           - key: "app.stateful/component"
             operator: "Equal"
             value: "qdrant"
             effect: NoSchedule
         
         affinity:
           nodeAffinity:
             preferredDuringSchedulingIgnoredDuringExecution:
             - weight: 1
               preference:
                 matchExpressions:
                 - key: "app.stateful/component"
                   operator: In
                   values:
                   - "qdrant"
         
         topologySpreadConstraints:
           - maxSkew: 1
             topologyKey: "topology.kubernetes.io/zone"
             whenUnsatisfiable: ScheduleAnyway
             labelSelector:
               matchLabels:
                 app.kubernetes.io/name: qdrant
                 app.kubernetes.io/instance: qdrant
         
         podDisruptionBudget:
           enabled: true
           maxUnavailable: 1
         
         persistence:
           accessModes: ["ReadWriteOnce"]
           size: 10Gi
           storageClassName: ha-regional
         
         apiKey: true
         
         sidecarContainers:
           - name: metrics
             image: nginx:1.29
             resources:
               requests:
                 memory: "128Mi"
                 cpu: "250m"
               limits:
                 memory: "128Mi"
                 cpu: "500m"
             ports:
             - containerPort: 80
             env:
             - name: QDRANT_APIKEY 
               valueFrom:
                 secretKeyRef:
                   name: qdrant-database-apikey          
                   key: api-key
             volumeMounts:
                 - name: nginx-conf
                   mountPath: /etc/nginx/templates/default.conf.template
                   subPath: default.conf.template
                   readOnly: true
         additionalVolumes:
           - name: nginx-conf
             configMap:
               name: nginx-conf
               items:
                 - key: default.conf.template
                   path: default.conf.template 

This configuration enables the cluster mode, allowing you to setup a highly available and distributed Qdrant cluster.

  6. Add a label to Qdrant statefulset:
         
         kubectl label statefulset qdrant-database examples.ai.gke.io/source=qdrant-guide -n qdrant
         

  7. Deploy an internal load balancer to access your Qdrant database that's running in the same VPC as your GKE cluster:
         
         kubectl apply -n qdrant -f manifests/02-values-file/ilb.yaml
         

The `ilb.yaml` manifest describes the `LoadBalancer` Service:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             #cloud.google.com/neg: '{"ingress": true}'
             networking.gke.io/load-balancer-type: "Internal"
           labels:
             app.kubernetes.io/name: qdrant
           name: qdrant-ilb
         spec:
           ports:
           - name: http
             port: 6333
             protocol: TCP
             targetPort: 6333
           - name: grpc
             port: 6334
             protocol: TCP
             targetPort: 6334
           selector:
             app: qdrant
             app.kubernetes.io/instance: qdrant-database
           type: LoadBalancer

  8. Check the deployment status:
         
         helm ls -n qdrant
         

The output is similar to the following, if the `qdrant` database is successfully deployed:
         
         NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
         qdrant-database  qdrant          1               2024-02-06 20:21:15.737307567 +0000 UTC deployed        qdrant-0.7.6    v1.7.4
         

  9. Wait for GKE to start the required workloads:
         
         kubectl wait pods -l app.kubernetes.io/instance=qdrant-database --for condition=Ready --timeout=300s -n qdrant
         

This command might take a few minutes to complete successfully.

  10. Once GKE starts the workloads, verify that GKE has created the Qdrant workloads:
         
         kubectl get pod,svc,statefulset,pdb,secret -n qdrant
         

  11. Start the `HighAvailabilityApplication` (HAA) resource for Qdrant:
         
         kubectl apply -n qdrant -f manifests/01-regional-pd/ha-app.yaml
         

The `ha-app.yaml` manifest describes the `HighAvailabilityApplication` resource:
         
         kind: HighAvailabilityApplication
         apiVersion: ha.gke.io/v1
         metadata:
           name: qdrant-database
           namespace: qdrant
         spec:
           resourceSelection:
             resourceKind: StatefulSet
           policy:
             storageSettings:
               requireRegionalStorage: true
             failoverSettings:
               forceDeleteStrategy: AfterNodeUnreachable
               afterNodeUnreachable:
                 afterNodeUnreachableSeconds: 20 # 60 seconds total

The following GKE resources are created for the Qdrant cluster:

     * The Qdrant `StatefulSet` that controls three Pod replicas.
     * `A PodDisruptionBudget`, ensuring a maximum of one unavailable replica.
     * The `qdrant-database` Service, exposing the Qdrant port for inbound connections and replication between nodes.
     * The `qdrant-database-headless` Service, providing the list of running Qdrant Pods.
     * The `qdrant-database-apikey` Secret, facilitating secure database connection.
     * Stateful HA operator Pod and `HighlyAvailableApplication` resource, actively monitoring the Qdrant application. The `HighlyAvailableApplication` resource defines failover rules to apply against Qdrant.
  12. To check if the failover rules are applied, describe the resource and confirm `Status: Message: Application is protected`.
         
         kubectl describe highavailabilityapplication qdrant-database -n qdrant
         

The output is similar to the following:
         
         Status:
         Conditions:
             Last Transition Time:  2023-11-30T09:54:52Z
             Message:               Application is protected
             Observed Generation:   1
             Reason:                ApplicationProtected
             Status:                True
             Type:                  Protected
         




## Run queries with Vertex AI Colab Enterprise notebook

Qdrant organizes vectors and payloads in collections. Vector embedding is a technique that represents words or entities as numerical vectors while maintaining their semantic relationships. This is important for similarity searches as it enables finding similarities based on meaning rather than exact matches, making tasks like search and recommendation systems more effective and nuanced.

This section shows you how to [upload Vectors](https://qdrant.tech/articles/fastembed/) into a new Qdrant [Collection](https://qdrant.tech/documentation/concepts/collections/) and run a search queries.

In this example, you use a dataset from a CSV file that contains a list of books in different genres. You create a Colab Enterprise notebook to perform a search query on the Qdrant database.

For more information about Vertex AI Colab Enterprise, see [Colab Enterprise documentation](https://docs.cloud.google.com/colab/docs/introduction).

### Create a runtime template

To create a Colab Enterprise runtime template:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime Templates** page and make sure your project is selected:

[Go to Runtime Templates](https://console.cloud.google.com/vertex-ai/colab/runtime-templates)

  2. Click _add_box_ **New Template**. The **Create new runtime template** page appears.

  3. In the **Runtime basics** section: 

     * In the **Display name** field, enter `qdrant-connect`.
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
         
         https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/databases/qdrant/manifests/04-notebook/vector-database.ipynb
         

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

![Prometheus metrics collection](https://docs.cloud.google.com/static/kubernetes-engine/images/qdrant-prometheus-metrics.svg)

The GKE private cluster in the diagram contains the following components:

  * Qdrant Pods that expose metrics on the path `/` and port `80`. These metrics are provided by the sidecar container named `metrics`.
  * Prometheus-based collectors that process the metrics from the Qdrant Pods.
  * A PodMonitoring resource that sends the metrics to Cloud Monitoring.



To export and view the metrics, follow these steps:

  1. Create the [`PodMonitoring`](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) resource to scrape metrics by `labelSelector`:
         
         kubectl apply -n qdrant -f manifests/03-prometheus-metrics/pod-monitoring.yaml
         

The `pod-monitoring.yaml` manifest describes the `PodMonitoring` resource:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: qdrant
         spec:
           selector:
             matchLabels:
               app: qdrant
               app.kubernetes.io/instance: qdrant-database
           endpoints:
           - port: 80
             interval: 30s
             path: / 

  2. [Create a Cloud Monitoring dashboard](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create) with the configurations defined in `dashboard.json` :
         
         gcloud --project "${PROJECT_ID}" monitoring dashboards create --config-from-file monitoring/dashboard.json
         

  3. After the command runs successfully, go to the Cloud Monitoring [Dashboards](https://docs.cloud.google.com/monitoring/dashboards):

[Go to Dashboards overview](https://console.cloud.google.com/monitoring/dashboards)

  4. From the list of dashboards, open the `Qdrant Overview` dashboard. It might take 1-2 minutes to collect and display metrics.

The dashboard shows a count of key metrics:

     * Collections
     * Embedded vectors
     * Pending operations
     * Running nodes



## Back up your cluster configuration

The [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) feature lets you schedule regular backups of your entire GKE cluster configuration, including the deployed workloads and their data.

In this tutorial, you configure a backup plan for your GKE cluster to perform backups of all workloads, including Secrets and Volumes, every day at 3 AM. To ensure efficient storage management, backups older than three days would be automatically deleted.

To configure [Backup plans](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#gcloud), follow these steps:

  1. Enable the Backup for GKE feature for your cluster:
         
         gcloud container clusters update ${KUBERNETES_CLUSTER_PREFIX}-cluster \
         --project=${PROJECT_ID} \
         --location=${REGION} \
         --update-addons=BackupRestore=ENABLED
         

  2. Create a backup plan with a daily schedule for all namespaces within the cluster:
         
         gcloud beta container backup-restore backup-plans create ${KUBERNETES_CLUSTER_PREFIX}-cluster-backup \
         --project=${PROJECT_ID} \
         --location=${REGION} \
         --cluster="projects/${PROJECT_ID}/locations/${REGION}/clusters/${KUBERNETES_CLUSTER_PREFIX}-cluster" \
         --all-namespaces \
         --include-secrets \
         --include-volume-data \
         --cron-schedule="0 3 * * *" \
         --backup-retain-days=3
         

The command uses the relevant environment variables at runtime.

The cluster name's format is relative to your project and region as follows:
         
         projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME
         

When prompted, type `y.`The output is similar to the following:
         
         Create request issued for: [qdrant-cluster-backup]
         Waiting for operation [projects/PROJECT_ID/locations/us-central1/operations/operation-1706528750815-610142ffdc9ac-71be4a05-f61c99fc] to complete...⠹
         

This operation might take a few minutes to complete successfully. After the execution is complete, the output is similar to the following:
         
         Created backup plan [qdrant-cluster-backup].
         

  3. You can see your newly created backup plan `qdrant-cluster-backup` listed on the Backup for GKE console.

[Go to Backup for GKE](https://console.cloud.google.com/kubernetes/backups/backupPlans)




If you want to restore the saved backup configurations, see [Restore a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).

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
         export KUBERNETES_CLUSTER_PREFIX=qdrant
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

  * Explore [Qdrant on GKE marketplace](https://console.cloud.google.com/marketplace/product/qdrant-public/qdrant).
  * Explore [Qdrant open source](https://github.com/qdrant/qdrant) software.
  * Try out the [Qdrant operator](https://github.com/ganochenkodg/qdrant-operator) that offers [API keys management](https://github.com/ganochenkodg/qdrant-operator/blob/main/docs/authentication.md), TLS support with [certificate management](https://github.com/ganochenkodg/qdrant-operator/blob/main/docs/tls.md), and [backup scheduling](https://github.com/ganochenkodg/qdrant-operator/blob/main/docs/backup-restore.md).
  * Learn about the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * Discover solutions for running [data-intensive workloads with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
