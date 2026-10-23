---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-elasticsearch/
title: Deploy an Elasticsearch vector database on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:32.662652+00:00
---

# Deploy an Elasticsearch vector database on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy an Elasticsearch vector database on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to deploy an [Elasticsearch](https://www.elastic.co/elasticsearch) vector database cluster on Google Kubernetes Engine (GKE).

[Vector databases](https://cloud.google.com/discover/what-is-a-vector-database) are data stores specifically designed to manage and search through large collections of high-dimensional vectors. These vectors represent data like text, images, audio, video or any data that can be numerically encoded. Unlike relational databases that rely on exact matches, vector databases specialize in finding similar items or identifying patterns within massive datasets.

Elasticsearch is a vector database that combines search and analytics functionalities. It comes with an open REST API for managing your cluster, and supports structured queries, full-text queries, and complex queries. Elasticsearch lets you perform phrase, similarity, and prefix searches, with autocomplete suggestions.

This tutorial is intended for cloud platform [administrators and architects](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins), [ML engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer), and MLOps (DevOps) professionals interested in deploying Elasticsearch database clusters on GKE.

## Benefits

Elasticsearch offers the following benefits:

  * Wide range of libraries for various programming languages and open API to integrate with other services.
  * Horizontal scaling, and support for sharding and replication that simplifies scaling and high availability.
  * Multi-node cluster balancing for optimal resource utilization.
  * Container and Kubernetes support for seamless integration into modern cloud-native environments.



## Objectives

In this tutorial, you learn how to:

  * Plan and deploy GKE infrastructure for Elasticsearch.
  * Deploy and configure Elasticsearch in a GKE cluster.
  * Deploy the [StatefulHA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha) operator to ensure Elasticsearch high availability.
  * Run a notebook to generate and store example vector embeddings within your database, and perform vector-based search queries.
  * Collect and visualize metrics on a dashboard.



## Deployment architecture

In this tutorial, you deploy a highly available regional GKE cluster for Elasticsearch, with multiple Kubernetes nodes spread across several availability zones. This setup helps ensure fault tolerance, scalability, and geographic redundancy. It allows for rolling updates and maintenance while providing SLAs for uptime and availability. For more information, see [Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).

When a node becomes unreachable, a Pod on that node is not rescheduled immediately. With Pods using a StatefulSet, it can take more than eight minutes for application Pods to be deleted and rescheduled to new nodes.

To address this issue, the StatefulHA operator does the following:

  * Solves rescheduling lag, handles failover settings and shortens recovery time by using `.forceDeleteStrategy`: `AfterNodeUnreachable` settings.
  * Helps ensure that the StatefulSet application is using RePD.
  * Extends GKE with a custom [HighAvailabilityApplication](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/highavailabilityapplication) resource that's deployed in the same namespace as Elasticsearch. This enables the StatefulHA operator to monitor and respond to failover events.



The following diagram shows an Elasticsearch cluster running on multiple nodes and zones in a GKE cluster:

![Elasticsearch deployment architecture](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-elasticsearch-architecture.svg)

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)
  * [Backup for GKE](https://cloud.google.com/backup-disaster-recovery/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

Elasticsearch usage is free under the Server Side Public License (SSPL).

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

  7. Enable the Cloud Resource Manager, Compute Engine, GKE, IAM Service Account Credentials, and Backup for GKE APIs, if any are not already enabled: 

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

  13. Enable the Cloud Resource Manager, Compute Engine, GKE, IAM Service Account Credentials, and Backup for GKE APIs, if any are not already enabled: 

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
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=elasticsearch
         export REGION=us-central1
         

     * Replace `PROJECT_ID` with your Google Cloud project ID.

This tutorial uses `us-central1` region to create your deployment resources.

  2. Check the version of Helm:
         
         helm version
         

Update the version if it's older than 3.13:
         
         curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
         

  3. Clone the sample code repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Navigate to the `elasticsearch` directory to start creating deployment resources:
         
         cd kubernetes-engine-samples/databases/elasticsearch
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a private, highly-available, regional GKE cluster to deploy your Elasticsearch database.

You can choose to deploy Elasticsearch using a [Standard or Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode). Each has its own advantages and different pricing models.

###  Autopilot 

The following diagram shows an Autopilot GKE cluster deployed in the project.

![GKE Autopilot cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-elasticsearch-autopilot.svg)

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
    
    kubectl_connection_command = "gcloud container clusters get-credentials elasticsearch-cluster --region us-central1"
    

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



###  Standard 

The following diagram shows a Standard private regional GKE cluster deployed across three different zones.

![GKE Standard cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-elasticsearch-standard.svg)

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
    
    kubectl_connection_command = "gcloud container clusters get-credentials elasticsearch-cluster --region us-central1"
    

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
    

## Deploy the Elasticsearch database and StatefulHA operator

In this section, you deploy the Elasticsearch database (in cluster mode) and StatefulHA operator to your GKE cluster using the [ECK Operator Helm Chart](https://artifacthub.io/packages/helm/elastic/eck-operator).

The Deployment creates a GKE cluster with the following configuration:

  * Three replicas of the Elasticsearch nodes.
  * DaemonSet to change virtual memory settings, for optimal Elasticsearch performance. A DaemonSet is a Kubernetes controller that helps ensure that a copy of a Pod runs on each node in a cluster.
  * Configuration of NodeAffinity and PodAntiAffinity to ensure proper distribution across Kubernetes nodes, optimizing the use of node pools and maximizing availability across different zones.
  * A Stateful HA operator that manages failover processes and helps ensure high availability. A StatefulSet is a Kubernetes controller that maintains a persistent unique identity for each of its Pods.
  * For authentication, the database creates Kubernetes Secrets with authentication credentials, passwords, and certificates.



To use the Helm chart to deploy the Elasticsearch database, follow these steps:

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

  2. Create an Elastic Cloud on Kubernetes (ECK) Custom Resource Definition (CRD):
         
         kubectl apply -f https://download.elastic.co/downloads/eck/2.11.1/crds.yaml
         

  3. Deploy the ECK operator:
         
         kubectl apply -f https://download.elastic.co/downloads/eck/2.11.1/operator.yaml
         

  4. Create the namespace `elastic` for the database:
         
         kubectl create ns elastic
         

  5. Install the [`HighAvailabilityApplication`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha#resource) (HAA) resource, which defines failover rules for Elasticsearch..
         
         kubectl apply -n elastic -f manifests/01-regional-pd/ha-app.yaml
         

The `ha-app.yaml` manifest describes the `HighAvailabilityApplication` resource:
         
         kind: HighAvailabilityApplication
         apiVersion: ha.gke.io/v1
         metadata:
           name: elasticsearch-ha-es-main
           namespace: elastic
         spec:
           resourceSelection:
             resourceKind: StatefulSet
           policy:
             storageSettings:
               requireRegionalStorage: false
             failoverSettings:
               forceDeleteStrategy: AfterNodeUnreachable
               afterNodeUnreachable:
                 afterNodeUnreachableSeconds: 20 # 60 seconds total

  6. Apply the manifest to create a regional persistent SSD disk `StorageClass`:
         
         kubectl apply -n elastic -f manifests/01-regional-pd/regional-pd.yaml
         

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

  7. Deploy the DaemonSet resource to set virtual memory in each node:
         
         kubectl apply -n elastic -f manifests/02-elasticsearch/mmap-count.yaml
         

The `mmap-count.yaml` manifest describes the `DaemonSet`:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: max-map-count-setter
           labels:
             k8s-app: max-map-count-setter
         spec:
           selector:
             matchLabels:
               name: max-map-count-setter
           template:
             metadata:
               labels:
                 name: max-map-count-setter
             spec:
               initContainers:
                 - name: max-map-count-setter
                   image: docker.io/bash:5.2.21
                   resources:
                     limits:
                       cpu: 100m
                       memory: 32Mi
                   securityContext:
                     privileged: true
                     runAsUser: 0
                   command: ['/usr/local/bin/bash', '-e', '-c', 'echo 262144 > /proc/sys/vm/max_map_count']
               containers:
                 - name: sleep
                   image: docker.io/bash:5.2.21
                   command: ['sleep', 'infinity']

  8. Apply the manifest to deploy Elasticsearch cluster:
         
         kubectl apply -n elastic -f manifests/02-elasticsearch/elasticsearch.yaml
         

The `elasticsearch.yaml` manifest describes the Deployment:
         
         apiVersion: elasticsearch.k8s.elastic.co/v1
         kind: Elasticsearch
         metadata:
           name: elasticsearch-ha
         spec:
           version: 8.11.4
           nodeSets:
           - name: main
             count: 3
             volumeClaimTemplates:
             - metadata:
                 name: elasticsearch-data 
               spec:
                 accessModes:
                 - ReadWriteOnce
                 resources:
                   requests:
                     storage: 10Gi
                 storageClassName: ha-regional
             config:
             podTemplate:
               metadata:
                 labels:
                   app.stateful/component: elasticsearch
               spec:
                 initContainers:
                 - name: max-map-count-check
                   command: ['sh', '-c', "while true; do mmc=$(cat /proc/sys/vm/max_map_count); if [ ${mmc} -eq 262144 ]; then exit 0; fi; sleep 1; done"]
                 containers:
                 - name: metrics
                   image: quay.io/prometheuscommunity/elasticsearch-exporter:v1.7.0
                   command:
                     - /bin/elasticsearch_exporter
                     - --es.ssl-skip-verify
                     - --es.uri=https://$(ES_USER):$(ES_PASSWORD)@localhost:9200
                   securityContext:
                     runAsNonRoot: true
                     runAsGroup: 10000
                     runAsUser: 10000
                   resources:
                     requests:
                       memory: "128Mi"
                       cpu: "25m"
                     limits:
                       memory: "128Mi"
                       cpu: "100m"
                   ports:
                   - containerPort: 9114
                   env:
                   - name: ES_USER
                     value: "elastic"
                   - name: ES_PASSWORD
                     valueFrom:
                       secretKeyRef:
                         name: elasticsearch-ha-es-elastic-user
                         key: elastic
                 - name: elasticsearch
                   resources:
                     limits:
                       memory: 4Gi
                       cpu: 1
                 affinity:
                   nodeAffinity:
                     preferredDuringSchedulingIgnoredDuringExecution:
                       - weight: 1
                         preference:
                           matchExpressions:
                           - key: app.stateful/component
                             operator: In
                             values:
                             - elasticsearch
                   podAntiAffinity:
                     preferredDuringSchedulingIgnoredDuringExecution:
                     - weight: 1
                       podAffinityTerm:
                         labelSelector:
                           matchLabels:
                             app.stateful/component: elasticsearch
                         topologyKey: topology.kubernetes.io/zone

Wait for a few minutes for the Elasticsearch cluster to fully start.

  9. Check the deployment status:
         
         kubectl get elasticsearch -n elastic --watch
         

The output is similar to following, if the `elasticsearch` database is successfully deployed:
         
         NAME               HEALTH   NODES   VERSION   PHASE   AGE
         elasticsearch-ha   green    3       8.11.4    Ready   2m30s
         

Wait for `HEALTH` to show as `green`. Press `Ctrl+C` to exit the command if needed.

  10. Deploy an internal load balancer to access your Elasticsearch database that's running in the same VPC as your GKE cluster:
         
         kubectl apply -n elastic -f manifests/02-elasticsearch/ilb.yaml
         

The `ilb.yaml` manifest describes the `LoadBalancer` Service:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             #cloud.google.com/neg: '{"ingress": true}'
             networking.gke.io/load-balancer-type: "Internal"
           labels:
             app.kubernetes.io/name: elasticsearch
           name: elastic-ilb
         spec:
           ports:
           - name: https
             port: 9200
             protocol: TCP
             targetPort: 9200
           selector:
             common.k8s.elastic.co/type: elasticsearch
             elasticsearch.k8s.elastic.co/cluster-name: elasticsearch-ha
           type: LoadBalancer

  11. To check if the failover rules are applied, describe the resource and confirm `Status: Message: Application is protected`.
         
         kubectl describe highavailabilityapplication elasticsearch-ha-es-main -n elastic
         

The output is similar to following
         
         Status:
           Conditions:
             Last Transition Time:  2024-02-01T13:27:50Z
             Message:               Application is protected
             Observed Generation:   1
             Reason:                ApplicationProtected
             Status:                True
             Type:                  Protected
         Events:                    <none>
         

  12. Once GKE starts the workloads, verify that GKE has created the Elasticsearch workloads:
         
         kubectl get pod,svc,statefulset,pdb,secret,daemonset -n elastic
         

The output is similar to the following:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         pod/elasticsearch-ha-es-main-0   2/2     Running   0          7m16s
         pod/elasticsearch-ha-es-main-1   2/2     Running   0          7m16s
         pod/elasticsearch-ha-es-main-2   2/2     Running   0          7m16s
         pod/max-map-count-setter-28wt9   1/1     Running   0          7m27s
         pod/max-map-count-setter-cflsw   1/1     Running   0          7m27s
         pod/max-map-count-setter-gzq9k   1/1     Running   0          7m27s
         
         NAME                                        TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
         service/elasticsearch-ha-es-http            ClusterIP   10.52.8.28   <none>        9200/TCP   7m18s
         service/elasticsearch-ha-es-internal-http   ClusterIP   10.52.3.48   <none>        9200/TCP   7m18s
         service/elasticsearch-ha-es-main            ClusterIP   None         <none>        9200/TCP   7m16s
         service/elasticsearch-ha-es-transport       ClusterIP   None         <none>        9300/TCP   7m18s
         
         NAME                                        READY   AGE
         statefulset.apps/elasticsearch-ha-es-main   3/3     7m16s
         
         NAME                                                     MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         poddisruptionbudget.policy/elasticsearch-ha-es-default   2               N/A               1                     7m16s
         
         NAME                                                 TYPE     DATA   AGE
         secret/elasticsearch-ha-es-elastic-user              Opaque   1      7m18s
         secret/elasticsearch-ha-es-file-settings             Opaque   1      7m16s
         secret/elasticsearch-ha-es-http-ca-internal          Opaque   2      7m17s
         secret/elasticsearch-ha-es-http-certs-internal       Opaque   3      7m17s
         secret/elasticsearch-ha-es-http-certs-public         Opaque   2      7m17s
         secret/elasticsearch-ha-es-internal-users            Opaque   4      7m18s
         secret/elasticsearch-ha-es-main-es-config            Opaque   1      7m16s
         secret/elasticsearch-ha-es-main-es-transport-certs   Opaque   7      7m16s
         secret/elasticsearch-ha-es-remote-ca                 Opaque   1      7m16s
         secret/elasticsearch-ha-es-transport-ca-internal     Opaque   2      7m16s
         secret/elasticsearch-ha-es-transport-certs-public    Opaque   1      7m16s
         secret/elasticsearch-ha-es-xpack-file-realm          Opaque   4      7m18s
         
         NAME                                  DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
         daemonset.apps/max-map-count-setter   6         6         6       6            6           <none>          13m
         




The following GKE resources are created for the Elasticsearch cluster:

  * The Elasticsearch `StatefulSet` that controls three Pod replicas.
  * A DaemonSet to configure virtual memory settings.
  * Services to connect to Elasticsearch.
  * Secrets with superuser credentials and service-related certificates.
  * Stateful HA operator Pod and `HighlyAvailableApplication` resource, actively monitoring the Elasticsearch application.



## Run queries with Vertex AI Colab Enterprise notebook

This section explains how to generate embeddings into [Elasticsearch documents](https://www.elastic.co/guide/en/elasticsearch/reference/5.3/gs-basic-concepts.html#_document) and perform semantic search queries using the official Elasticsearch Python client in Colab Enterprise notebook. A document in Elasticsearch is composed of various fields, each paired with its corresponding value.

For more information about Vertex AI Colab Enterprise, see [Colab Enterprise documentation](https://docs.cloud.google.com/colab/docs/introduction).

**Best practice** : 

To effectively utilize Elasticsearch, we recommend that you structure your data into these documents, which are then indexed for search purposes.

In this example, you use a dataset from a CSV file that contains a list of books in different genres. Elasticsearch serves as a search engine, and the Pod you create serves as a client querying the Elasticsearch database.

You can use a dedicated runtime template to deploy to the `elasticsearch-vpc` VPC (Virtual Private Cloud), so the notebook can communicate with resources in your GKE cluster.

### Create a runtime template

To create a Colab Enterprise runtime template:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime Templates** page and make sure your project is selected:

[Go to Runtime Templates](https://console.cloud.google.com/vertex-ai/colab/runtime-templates)

  2. Click _add_box_ **New Template**. The **Create new runtime template** page appears.

  3. In the **Runtime basics** section: 

     * In the **Display name** field, enter `elastic-connect`.
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
         
         https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/databases/elasticsearch/manifests/03-notebook/vector-database.ipynb
         

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

![Prometheus metrics collection](https://docs.cloud.google.com/static/kubernetes-engine/images/elasticsearch-metrics.svg)

The GKE private cluster in the diagram contains the following components:

  * Elasticsearch Pods that expose metrics on the path `/` and port `9114`. These metrics are provided by the sidecar container named `metrics` that contains the [elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter).
  * Prometheus-based collectors that process the metrics from the Elasticsearch Pod.
  * A PodMonitoring resource that sends the metrics to Cloud Monitoring.



The cluster configuration defines a sidecar container with metrics exporter in the Prometheus format:
    
    
    apiVersion: elasticsearch.k8s.elastic.co/v1
    kind: Elasticsearch
    metadata:
      name: elasticsearch-ha
    spec:
      ...
      nodeSets:
      - name: main
        ...
        podTemplate:
          spec:
            containers:
            ...
            - name: metrics
              image: quay.io/prometheuscommunity/elasticsearch-exporter:v1.7.0
              command:
              - /bin/elasticsearch_exporter
              - --es.ssl-skip-verify
              - --es.uri=https://$(ES_USER):$(ES_PASSWORD)@localhost:9200
              ...
              env:
              - name: ES_USER
                value: "elastic"
              - name: ES_PASSWORD
                valueFrom:
                secretKeyRef:
                  name: elasticsearch-ha-es-elastic-user
                  key: elastic
    

To export and view the metrics, follow these steps:

  1. Create the [`PodMonitoring`](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) resource to scrape metrics by `labelSelector`:
         
         kubectl apply -n elastic -f manifests/04-prometheus-metrics/pod-monitoring.yaml
         

The `pod-monitoring.yaml` manifest describes the `PodMonitoring` resource:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: elasticsearch
         spec:
           selector:
             matchLabels:
               app.stateful/component: elasticsearch
               elasticsearch.k8s.elastic.co/cluster-name: elasticsearch-ha
           endpoints:
           - port: 9114
             interval: 30s
             path: /metrics

After a few minutes, the built-in dashboard "Elasticsearch Prometheus Overview" displays.

  2. To view more data-related graphs, import a custom [Cloud Monitoring dashboard](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create) with the configurations defined in `dashboard.json`:
         
         gcloud --project "${PROJECT_ID}" monitoring dashboards create --config-from-file monitoring/dashboard.json
         

  3. After the command runs successfully, go to the Cloud Monitoring [Dashboards](https://docs.cloud.google.com/monitoring/dashboards):

[Go to Dashboards overview](https://console.cloud.google.com/monitoring/dashboards)

  4. From the list of dashboards, open the `ElasticSearch Overview` dashboard. It might take 1-2 minutes to collect and display metrics.

The dashboard shows a count of key metrics:

     * Indexes
     * Documents and Shards
     * Pending operations
     * Running nodes with their health statuses



## Back up your cluster configuration

The [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) feature lets you schedule regular backups of your entire GKE cluster configuration, including the deployed workloads and their data.

In this tutorial, you configure a backup plan for your GKE cluster to perform backups of all workloads, including Secrets and Volumes, every day at 3 AM. To ensure efficient storage management, backups older than three days are automatically deleted.

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
         
         Create request issued for: [elasticsearch-cluster-backup]
         Waiting for operation [projects/PROJECT_ID/locations/us-central1/operations/operation-1706528750815-610142ffdc9ac-71be4a05-f61c99fc] to complete...⠹
         

This operation might take a few minutes to complete successfully. After the execution is complete, the output is similar to the following:
         
         Created backup plan [elasticsearch-cluster-backup].
         

  3. You can see your newly created backup plan `elasticsearch-cluster-backup` listed on the Backup for GKE console.

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
         export KUBERNETES_CLUSTER_PREFIX=elasticsearch
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

  * Explore [Elasticsearch open source](https://github.com/elastic/elasticsearch) software.
  * Learn about the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * Discover solutions for running [data-intensive workloads with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
