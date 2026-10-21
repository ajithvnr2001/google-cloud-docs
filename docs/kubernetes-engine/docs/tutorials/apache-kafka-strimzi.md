---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/apache-kafka-strimzi/
title: Deploy Apache Kafka to GKE using Strimzi \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:08.830127+00:00
---

# Deploy Apache Kafka to GKE using Strimzi  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/apache-kafka-strimzi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy Apache Kafka to GKE using Strimzi Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

The guide shows you how to use the [Strimzi](http://www.strimzi.io) operator to deploy Apache [Kafka](https://kafka.apache.org/) clusters.

Kafka is an open-source, distributed messaging system designed to handle high-volume, high-throughput, and real-time streaming data. It lets you build streaming data pipelines for reliable data transfer across different systems and applications, to support processing and analysis tasks.

Operators are software extensions that make use of custom resources to manage applications and their components. To learn more about the motivation for using operators, see [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) in the open source Kubernetes documentation. The Strimzi operator offers flexibility in deployment options and lets you use Kubernetes taints and tolerances to run Kafka on dedicated nodes.

This guide is intended for platform administrators, cloud architects, and operations professionals interested in deploying Kafka clusters on GKE.

This solution is a good starting point if you want to learn how to deploy Kafka clusters using a third-party operator to automate management and reduce errors.

## Objectives

  * Plan and deploy GKE infrastructure for Apache Kafka
  * Deploy and configure the Strimzi operator
  * Configure Apache Kafka using the Strimzi operator



### Benefits

Strimzi includes the following benefits:

  * Strimzi operators provide a simplified and Kubernetes-native approach to managing Kafka clusters. Strimzi utilizes custom resources that represent Kafka topics and users, making cluster management much more straightforward and aligned with Kubernetes best practices.
  * Strimzi prioritizes security by default by generating certificates for listeners and supporting secure authentication methods such as TLS, SCRAM-SHA, and OAuth. Strimzi also handles NetworkPolicies for all Kafka listeners.
  * Strimzi doesn't rely on external dependencies. It includes Kafka and [ZooKeeper](https://zookeeper.apache.org/) clusters with built-in metrics exporters, saving you from dealing with additional tools. You can also fine-tune broker configurations to meet specific requirements.



## Deployment architecture

A Kafka cluster consists of one or more servers, known as _brokers_ , which collaborate to manage incoming data streams and facilitate publish-subscribe messaging for Kafka clients, referred to as _consumers_.

Every data partition within the Kafka cluster is assigned a _leader broker_ , which is responsible for managing all read and write operations to that partition. The partition can also have one or more _follower brokers_ which passively replicate the actions of the leader broker.

In a typical setup, ZooKeeper coordinates Kafka clusters by helping choose a leader among the brokers and ensuring a smooth failover in case of any issues.

You can also deploy Kafka configuration without Zookeeper by activating KRaft mode, but this method is not considered production-ready by the Strimzi community because it does not include support for KafkaTopic resources, credential authentication, and more.

### Availability and disaster recovery

This tutorial uses separate [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [zones](https://docs.cloud.google.com/compute/docs/regions-zones) for Kafka and ZooKeeper clusters to ensure high availability and prepare for disaster recovery.

Using multiple nodes and zones is crucial for achieving a high-available Kubernetes cluster in Google Cloud for the following reasons:

  * Fault tolerance: Multiple nodes distribute the workload across the cluster, ensuring that if one node fails, the other nodes can take over the tasks, preventing downtime and service interruptions.
  * Scalability: Using multiple nodes helps ensure horizontal scaling can add or remove nodes as needed, which helps ensure optimal resource allocation and accommodating increased traffic or workload demands.
  * High availability: Using multiple zones within a region helps ensure redundancy and minimizes the risk of a single point of failure. If an entire availability zone experiences an outage, the cluster can continue running in other zones, maintaining service availability.
  * Geographic redundancy: By spanning nodes across regions, the cluster's data and services are geographically distributed, providing resilience against natural disasters, power outages, or other local disruptions that might impact a single zone.
  * Rolling updates and maintenance: Using multiple zones helps ensure that rolling updates and maintenance can be performed on individual nodes without impacting the overall availability of the cluster. This helps ensure continuous service while allowing for necessary updates and patches to be applied seamlessly.
  * Service Level Agreements (SLAs): Google Cloud provides SLAs for multi-zone deployments, offering a minimum level of uptime and availability.



### Deployment diagram

The following diagram shows a Kafka cluster running on multiple nodes and zones in a GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/strimzi-pods-allocation-kafka.svg)

In the diagram, the Kafka `StrimziPodSet` is deployed across three nodes in three different zones. You can control this configuration by setting the required Pod [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) and [topology spread](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) rules on the `StrimziPodSet` custom resource specification.

If one Zone fails, using the recommended configuration, GKE reschedules Pods on new nodes and replicates data from the remaining replicas, for both Kafka and Zookeeper.

The following diagram shows a ZooKeeper `StrimziPodSet` deployed across three nodes in three different zones:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/strimzi-pods-allocation.svg)

### The `StrimziPodSet` custom resource

This tutorial uses the [`StrimziPodSet`](https://strimzi.io/docs/operators/in-development/configuring.html#type-StrimziPodSet-reference) custom resource introduced in version 0.29 of Strimzi instead of `StatefulSets`.

The `StrimziPodSet` resources offers enhanced scalability for the cluster and lets you pass configuration options, allowing you to make more granular changes to Pods. The `StrimziPodSet` resource is enabled by default in Strimzi versions 0.35 and later.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/disks-image-pricing)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)
  * [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/pricing#backup-for-gke)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

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

  7. Enable the Compute Engine, IAM, GKE, Backup for GKE, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com iam.googleapis.com container.googleapis.com gkebackup.googleapis.com cloudresourcemanager.googleapis.com

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

  13. Enable the Compute Engine, IAM, GKE, Backup for GKE, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com iam.googleapis.com container.googleapis.com gkebackup.googleapis.com cloudresourcemanager.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer, roles/logging.logWriter, roles/container.clusterAdmin, roles/container.serviceAgent, roles/iam.serviceAccountAdmin, roles/serviceusage.serviceUsageAdmin, roles/iam.serviceAccountAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), [Helm](https://helm.sh/) and [Terraform](https://docs.cloud.google.com/docs/terraform).

To set up your environment with Cloud Shell, follow these steps:

  1. Launch a Cloud Shell session from the Google Cloud console, by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](https://console.cloud.google.com/). This launches a session in the bottom pane of the Google Cloud console.

  2. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=kafka
         export REGION=us-central1
         

Replace `PROJECT_ID`: your Google Cloud with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Change to the working directory:
         
         cd kubernetes-engine-samples/streaming/
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a highly-available, regional GKE cluster with private nodes. The following steps allow public access to the control plane. To restrict access, configure the cluster with the [control plane exposed on the internal endpoint only](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).

You can install the operator using a [Standard or Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) cluster.

###  Standard 

The following diagram shows a regional Standard cluster with private nodes GKE cluster deployed across three different zones:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-kafka-standard.svg)

To deploy this infrastructure, run the following commands from the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=kafka/terraform/gke-standard init
    terraform -chdir=kafka/terraform/gke-standard apply -var project_id=${PROJECT_ID} \
      -var region=${REGION} \
      -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

When prompted, type `yes`. It might take several minutes for this command to complete and for the cluster to show a ready status.

Terraform creates the following resources:

  * A VPC network and private subnet for the Kubernetes nodes.
  * A router to access the internet through NAT.
  * A GKE cluster with private nodes in the `us-central1` region.
  * 2 node pools with autoscaling enabled (1-2 nodes per zone, 1 node per zone minimum)
  * A `ServiceAccount` with logging and monitoring permissions.
  * Backup for GKE for disaster recovery.
  * Google Cloud Managed Service for Prometheus for cluster monitoring.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials strimzi-cluster --region us-central1"
    

###  Autopilot 

The following diagram shows a regional Autopilot cluster with private nodes GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-kafka-autopilot.svg)

To deploy the infrastructure, run the following commands from the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=kafka/terraform/gke-autopilot init
    terraform -chdir=kafka/terraform/gke-autopilot apply -var project_id=${PROJECT_ID} \
      -var region=${REGION} \
      -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

When prompted, type `yes`. It might take several minutes for this command to complete and for the cluster to show a ready status.

Terraform creates the following resources:

  * VPC network and private subnet for the Kubernetes nodes.
  * A router to access the internet through NAT.
  * A GKE cluster with private nodes in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions
  * Google Cloud Managed Service for Prometheus for cluster monitoring.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 12 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials strimzi-cluster --region us-central1"
    

### Connecting to the cluster

Configure `kubectl` to communicate with the cluster:
    
    
    gcloud container clusters get-credentials ${KUBERNETES_CLUSTER_PREFIX}-cluster --region ${REGION}
    

## Deploy the Strimzi operator to your cluster

In this section, you deploy the Strimzi operator using a Helm chart. There are also [several other ways](https://strimzi.io/docs/operators/in-development/full/deploying.html#con-strimzi-installation-methods_str) to deploy Strimzi.

  1. Add the Strimzi Helm Chart repository:
         
         helm repo add strimzi https://strimzi.io/charts/
         

  2. Add a namespace for the Strimzi Operator and the Kafka cluster:
         
         kubectl create ns kafka
         

  3. Deploy the Strimzi cluster operator using Helm:
         
         helm install strimzi-operator strimzi/strimzi-kafka-operator -n kafka
         

To deploy Strimzi Cluster Operator and Kafka clusters to different namespaces, add the parameter `--set watchNamespaces="{kafka-namespace,kafka-namespace-2,...}"` to the helm command.

  4. Verify that the Strimzi Cluster Operator has been deployed successfully using Helm:
         
         helm ls -n kafka
         

The output is similar to the following:
         
         NAME            NAMESPACE    REVISION    UPDATED                              STATUS    CHART                        APP VERSION
         strimzi-operator    kafka      1       2023-06-27 11:22:15.850545 +0200 CEST    deployed    strimzi-kafka-operator-0.35.0    0.35.0
         




## Deploy Kafka

After the operator is deployed to the cluster, you are ready to deploy a Kafka cluster instance.

In this section, you deploy Kafka in a basic configuration and then try various advanced configuration scenarios to address availability, security, and observability requirements.

### Basic configuration

The basic configuration for the Kafka instance includes the following components:

  * Three replicas of Kafka brokers, with a minimum of two available replicas required for cluster consistency.
  * Three replicas of ZooKeeper nodes, forming a cluster.
  * Two Kafka listeners: one without authentication, and one utilizing TLS authentication with a certificate generated by Strimzi.
  * Java _MaxHeapSize_ and _MinHeapSize_ set to 4 GB for Kafka and 2 GB for ZooKeeper.
  * CPU resource allocation of 1 CPU request and 2 CPU limits both for Kafka and ZooKeeper, along with 5 GB memory requests and limits for Kafka (4 GB for the main service and 0.5 GB for the metrics exporter) and 2.5 GB for ZooKeeper (2 GB for the main service and 0.5 GB for the metrics exporter).
  * Entity-operator with the following requests and limits: 
    * `tlsSidecar`: 100 m/500 m CPU and 128 Mi memory.
    * `topicOperator`: 100 m/500 m CPU and 512 Mi memory.
    * `userOperator`: 500 m CPU and 2 Gi memory.
  * 100 GB of storage allocated to each Pod using the `premium-rwo` `storageClass`.
  * Tolerations, nodeAffinities, and podAntiAffinities configured for each workload, ensuring proper distribution across nodes, utilizing their respective node pools and different zones.
  * Communication inside the cluster secured by self-signed certificates: separate Certificate Authorities (CAs) for cluster and clients (mTLS). You can also configure to use a different Certificate Authority.



This configuration represents the minimal setup required to create a production-ready Kafka cluster. The following sections demonstrate custom configurations to address aspects such as cluster security, Access Control Lists (ACLs), topic management, certificate management and more.

### Create a basic Kafka cluster

  1. Create a new Kafka cluster using the basic configuration:
         
         kubectl apply -n kafka -f kafka-strimzi/manifests/01-basic-cluster/my-cluster.yaml
         

This command creates a Kafka custom resource of the Strimzi operator that includes CPU and memory requests and limits, block storage requests, and a combination of taints and affinities to distribute the provisioned Pods across Kubernetes nodes.

  2. Wait a few minutes while Kubernetes starts the required workloads:
         
         kubectl wait kafka/my-cluster --for=condition=Ready --timeout=600s -n kafka
         

  3. Verify that the Kafka workloads were created:
         
         kubectl get pod,service,deploy,pdb -l=strimzi.io/cluster=my-cluster -n kafka
         

The output is similar to the following:
         
         NAME                                            READY   STATUS  RESTARTS   AGE
         pod/my-cluster-entity-operator-848698874f-j5m7f   3/3   Running   0        44m
         pod/my-cluster-kafka-0                          1/1   Running   0        5m
         pod/my-cluster-kafka-1                          1/1   Running   0        5m
         pod/my-cluster-kafka-2                          1/1   Running   0        5m
         pod/my-cluster-zookeeper-0                      1/1   Running   0        6m
         pod/my-cluster-zookeeper-1                      1/1   Running   0        6m
         pod/my-cluster-zookeeper-2                      1/1   Running   0        6m
         
         NAME                                TYPE      CLUSTER-IP   EXTERNAL-IP   PORT(S)                             AGE
         service/my-cluster-kafka-bootstrap  ClusterIP   10.52.8.80   <none>      9091/TCP,9092/TCP,9093/TCP          5m
         service/my-cluster-kafka-brokers    ClusterIP   None         <none>      9090/TCP,9091/TCP,9092/TCP,9093/TCP   5m
         service/my-cluster-zookeeper-client   ClusterIP   10.52.11.144   <none>      2181/TCP                            6m
         service/my-cluster-zookeeper-nodes  ClusterIP   None         <none>      2181/TCP,2888/TCP,3888/TCP          6m
         
         NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
         deployment.apps/my-cluster-entity-operator   1/1   1          1         44m
         
         NAME                                            MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         poddisruptionbudget.policy/my-cluster-kafka     2             N/A             1                   5m
         poddisruptionbudget.policy/my-cluster-zookeeper   2             N/A             1                   6m
         




The operator creates the following resources:

  * Two `StrimziPodSets` for Kafka and ZooKeeper.
  * Three Pods for Kafka broker replicas.
  * Three Pods for ZooKeeper replicas.
  * Two `PodDisruptionBudgets`, which helps ensure a minimum availability of two replicas for cluster consistency.
  * A Service named `my-cluster-kafka-bootstrap`, which serves as the bootstrap server for Kafka clients connecting from within the Kubernetes cluster. All internal Kafka listeners are available in this Service.
  * A headless Service named `my-cluster-kafka-brokers` that enables DNS resolution of Kafka broker Pod IP addresses directly. This service is used for inter broker communication.
  * A Service named `my-cluster-zookeeper-client` that lets Kafka brokers connect to ZooKeeper nodes as clients.
  * A headless Service named `my-cluster-zookeeper-nodes` that enables DNS resolution of ZooKeeper Pod IP addresses directly. This service is used to connect between ZooKeeper replicas.
  * A Deployment named `my-cluster-entity-operator` that contains the [topic-operator and user-operator](https://strimzi.io/docs/operators/latest/configuring.html#assembly-kafka-entity-operator-str) and facilitates the management of custom resources `KafkaTopics` and `KafkaUsers`.



You can also configure two `NetworkPolicies` to facilitate connectivity to Kafka listeners from any Pod and Namespace. These policies would also restrict connections to ZooKeeper to brokers, and enable communication between the cluster Pods and internal Service ports exclusive to cluster communication.

## Authentication and user management

This section shows you how to enable the authentication and authorization to secure Kafka Listeners and share credentials with clients.

Strimzi provides a Kubernetes-native method for user management using a separate [`User Operator`](https://strimzi.io/docs/operators/latest/configuring.html#user-operator-str) and its corresponding Kubernetes custom resource, [`KafkaUser`](https://strimzi.io/docs/operators/latest/configuring.html#type-KafkaUser-reference), which defines the user configuration. The user configuration includes settings for authentication and authorization, and provisions the corresponding user in Kafka.

Strimzi can create Kafka listeners and users that support several [authentication mechanisms](https://strimzi.io/docs/operators/latest/configuring.html#type-KafkaUserSpec-reference) such as username and password-based authentication (SCRAM-SHA-512) or TLS. You can also use OAuth 2.0 authentication, which is often considered a better approach compared to using passwords or certificates for authentication because of security and external credential management.

### Deploy a Kafka cluster

This section shows you how to deploy a Strimzi operator that demonstrates user management capabilities, including:

  * A Kafka cluster with password-based authentication (SCRAM-SHA-512) enabled on one of the listeners.
  * A `KafkaTopic`with 3 replicas.
  * A `KafkaUser` with an ACL that specifies that user has read and write permissions to the topic.


  1. Configure your Kafka cluster to use a listener with password-based SCRAM-SHA-512 authentication on port 9094 and simple authorization:
         
         kubectl apply -n kafka -f kafka-strimzi/manifests/03-auth/my-cluster.yaml
         

  2. Create a `Topic`, `User` and a client Pod to execute commands against the Kafka cluster:
         
         kubectl apply -n kafka -f kafka-strimzi/manifests/03-auth/topic.yaml
         kubectl apply -n kafka -f kafka-strimzi/manifests/03-auth/my-user.yaml
         

The `Secret` `my-user` with the user credentials is mounted to the client Pod as a [Volume](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod).

These credentials confirm that the user has permissions to publish messages to the topic using the listener with the password-based authentication (SCRAM-SHA-512) enabled.

  3. Create a client pod:
         
         kubectl apply -n kafka -f kafka-strimzi/manifests/03-auth/kafkacat.yaml
         

  4. Wait a few minutes for the client Pod becomes `Ready` then connect to it:
         
         kubectl wait --for=condition=Ready pod --all -n kafka --timeout=600s
         kubectl exec -it kafkacat -n kafka -- /bin/sh
         

  5. Produce a new message with `my-user` credentials and try to consume it:
         
         echo "Message from my-user" |kcat \
           -b my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9094 \
           -X security.protocol=SASL_SSL \
           -X sasl.mechanisms=SCRAM-SHA-512 \
           -X sasl.username=my-user \
           -X sasl.password=$(cat /my-user/password) \
           -t my-topic -P
         kcat -b my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9094 \
           -X security.protocol=SASL_SSL \
           -X sasl.mechanisms=SCRAM-SHA-512 \
           -X sasl.username=my-user \
           -X sasl.password=$(cat /my-user/password) \
           -t my-topic -C
         

The output is similar to the following:
         
         Message from my-user
         % Reached end of topic my-topic [0] at offset 0
         % Reached end of topic my-topic [2] at offset 1
         % Reached end of topic my-topic [1] at offset 0
         

Type `CTRL+C` to stop the consumer process.

  6. Exit the Pod shell
         
         exit
         




## Backups and disaster recovery

Although the Strimzi operator does not offer built-in backup functionality, you can implement efficient backup strategies by following certain patterns.

You can use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) to backup:

  * Kubernetes resource manifests.
  * Strimzi API custom resources and their definitions extracted from the Kubernetes API server of the cluster undergoing backup.
  * Volumes that correspond to PersistentVolumeClaim resources found in the manifests.



You can also perform a backup of a Kafka cluster that has been deployed using the Strimzi operator. You should backup:

  * The Kafka configuration, which includes all custom resources of the Strimzi API such as `KafkaTopics`and `KafkaUsers`.
  * The data, which is stored in the PersistentVolumes of the Kafka brokers.



Storing Kubernetes resource manifests, including Strimzi configurations, in Git repositories can eliminate the need for a separate backup for Kafka configuration, because the resources can be reapplied to a new Kubernetes cluster when necessary.

To safeguard Kafka data recovery in scenarios where a Kafka server instance, or a Kubernetes cluster where Kafka is deployed, is lost, we recommend that you configure the Kubernetes storage class used for provisioning volumes for Kafka brokers with the `reclaimPolicy` option set to `Retain`. We also recommend that you take [snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) of Kafka broker volumes.

The following manifest describes a StorageClass that uses the `reclaimPolicy` option `Retain`:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: premium-rwo-retain
    ...
    reclaimPolicy: Retain
    volumeBindingMode: WaitForFirstConsumer
    

The following example shows the StorageClass added to the `spec` of a Kafka cluster custom resource:
    
    
    # ...
    spec:
      kafka:
        # ...
        storage:
          type: persistent-claim
          size: 100Gi
          class: premium-rwo-retain
    

With this configuration, PersistentVolumes provisioned using the storage class are not deleted even when the corresponding PersistentVolumeClaim is deleted.

To recover the Kafka instance on a new Kubernetes cluster using the existing configuration and broker instance data:

  1. Apply the existing Strimzi Kafka custom resources (`Kakfa`, `KafkaTopic`, `KafkaUser`, etc.) to a new Kubernetes cluster
  2. Update the PersistentVolumeClaims with the name of the new Kafka broker instances to the old PersistentVolumes using the `spec.volumeName` property on the PersistentVolumeClaim.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the individual resources

If you used an existing project and you don't want to delete it, delete the individual resources.

  1. Set environment variables.
         
         export PROJECT_ID=${PROJECT_ID}
         export KUBERNETES_CLUSTER_PREFIX=kafka
         export REGION=us-central1
         

  2. Run the `terraform destroy` command:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform -chdir=kafka/terraform/FOLDER destroy -var project_id=${PROJECT_ID}   \
           -var region=${REGION}  \
           -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
         

Replace `FOLDER` with either `gke-autopilot` or `gke-standard`.

When prompted, type `yes`.

  3. Find all unattached disks:
         
         export disk_list=$(gcloud compute disks list --filter="-users:* AND labels.name=${KUBERNETES_CLUSTER_PREFIX}-cluster" --format "value[separator=|](name,zone)")
         

This step is needed because, by default Strimzi uses the `deleteClaim: false` parameter for storage. If you delete the cluster, all disks remain available.

  4. Delete the disks:
         
         for i in $disk_list; do
           disk_name=$(echo $i| cut -d'|' -f1)
           disk_zone=$(echo $i| cut -d'|' -f2|sed 's|.*/||')
           echo "Deleting $disk_name"
           gcloud compute disks delete $disk_name --zone $disk_zone --quiet
         done
         




## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 
  * [Learn how to backup your clusters by using Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
