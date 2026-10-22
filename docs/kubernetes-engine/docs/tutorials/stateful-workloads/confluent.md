---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/confluent/
title: Deploy Apache Kafka to GKE using Confluent \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:42.226093+00:00
---

# Deploy Apache Kafka to GKE using Confluent  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/confluent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy Apache Kafka to GKE using Confluent Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

The guide shows you how to use the [Confluent for Kubernetes (CFK)](https://docs.confluent.io/operator/current/overview.html) operator to deploy Apache [Kafka](https://kafka.apache.org/) clusters on Google Kubernetes Engine (GKE).

Kafka is an open source, distributed publish-subscribe messaging system for handling high-volume, high-throughput, and real-time streaming data. You can use Kafka to build streaming data pipelines that move data reliably across different systems and applications for processing and analysis.

This guide is intended for platform administrators, cloud architects, and operations professionals interested in deploying Kafka clusters on GKE.

You can also use the CFK operator to deploy other components of the [Confluent Platform](https://docs.confluent.io/platform/current/overview.html), such as the web-based Confluent Control center, Schema Registry, or KsqlDB. However, this guide focuses only on Kafka deployments.

**Note:** The CFK operator and most of the Confluent platform components are distributed under a [Сonfluent Enterprise License](https://docs.confluent.io/platform/current/installation/license.html), and license restrictions require users to have an active [subscription](https://www.confluent.io/subscription/) after 30 days trial to keep using the operator. The Developer License also is available for an indefinite duration, however it's limited to a single broker configuration per cluster.

## Objectives

  * Plan and deploy GKE infrastructure for Apache Kafka
  * Deploy and configure the CFK operator
  * Configure Apache Kafka using the CFK operator to ensure availability, security, observability, and performance



### Benefits

CFK offers the following benefits:

  * Automated rolling updates for configuration changes.
  * Automated rolling upgrades with no impact to Kafka availability.
  * If a failure occurs, CFK restores a Kafka Pod with the same Kafka broker ID, configuration, and persistent storage volumes.
  * Automated rack awareness to spread replicas of a partition across different racks (or zones), improving availability of Kafka brokers and limiting the risk of data loss.
  * Support for aggregated metrics export to Prometheus.



## Deployment architecture

Each data partition in a Kafka cluster has one _leader_ broker and can have one or more _follower_ brokers. The leader broker handles all reads and writes to the partition. Each follower broker passively replicates the leader broker.

In a typical Kafka setup, you also use an open source service called [ZooKeeper](https://zookeeper.apache.org/) to coordinate your Kafka clusters. This service helps by electing a leader among the brokers and triggering failover in case of failures.

You can also deploy Kafka configuration without Zookeeper by activating [KRaft mode](https://docs.confluent.io/operator/current/co-deploy-cfk.html#deploy-co-with-kraft), but this method is not considered production-ready due to lack of support for [KafkaTopic resources](https://docs.confluent.io/operator/current/co-manage-topics.html), and credential authentication.

### Availability and disaster recovery

This tutorial uses separate [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [zones](https://docs.cloud.google.com/compute/docs/regions-zones) for Kafka and ZooKeeper clusters to ensure high availability and prepare for disaster recovery.

Highly available Kubernetes clusters in Google Cloud rely on regional clusters spanning multiple nodes and availability zones. This configuration improves fault tolerance, scalability, and geographic redundancy. This configuration also lets you perform rolling updates and maintenance while providing SLAs for uptime and availability. For more information, see [Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).

### Deployment diagram

The following diagram shows a Kafka cluster running on multiple nodes and zones in a GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/confluent-pods-allocation-kafka.svg)

In the diagram, the Kafka StatefulSet is deployed across three nodes in three different zones. You can control this configuration by setting the required Pod [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) and [topology spread](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) rules on the `Kafka` custom resource specification.

If one zone fails, using the recommended configuration, GKE reschedules Pods on new nodes and replicates data from the remaining replicas, for both Kafka and Zookeeper.

The following diagram shows a ZooKeeper `StatefulSet` deployed across three nodes in three different zones:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/confluent-pods-allocation-zookeeper.svg)

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)
  * [Compute Engine](https://cloud.google.com/compute/disks-image-pricing)



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

  7. Enable the GKE, Backup for GKE, Compute Engine, Identity and Access Management, and Resource Manager APIs, if any are not already enabled: 

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

  13. Enable the GKE, Backup for GKE, Compute Engine, Identity and Access Management, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com iam.googleapis.com container.googleapis.com gkebackup.googleapis.com cloudresourcemanager.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `role/storage.objectViewer, role/logging.logWriter, roles/container.clusterAdmin, role/container.serviceAgent, roles/iam.serviceAccountAdmin, roles/serviceusage.serviceUsageAdmin, roles/iam.serviceAccountAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), [Helm](https://helm.sh/), and [Terraform](https://docs.cloud.google.com/docs/terraform).

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
         
         cd kubernetes-engine-samples/streaming
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a private, highly-available, regional GKE cluster. The following steps allow public access to the control plane. To restrict access, create a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept).

You can install the operator using a [Standard or Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) cluster.

###  Standard 

The following diagram shows a private regional Standard GKE cluster deployed across three different zones:

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
  * A private GKE cluster in the `us-central1` region.
  * 2 node pools with autoscaling enabled (1-2 nodes per zone, 1 node per zone minimum)
  * A `ServiceAccount` with logging and monitoring permissions.
  * Backup for GKE for disaster recovery.
  * Google Cloud Managed Service for Prometheus for cluster monitoring.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials kafka-cluster --region us-central1"
    

###  Autopilot 

The following diagram shows a private regional Autopilot GKE cluster:

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
  * A private GKE cluster in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions
  * Google Cloud Managed Service for Prometheus for cluster monitoring.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 12 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    kubectl_connection_command = "gcloud container clusters get-credentials kafka-cluster --region us-central1"
    

### Connect to the cluster

Configure `kubectl` to communicate with the cluster:
    
    
    gcloud container clusters get-credentials ${KUBERNETES_CLUSTER_PREFIX}-cluster --region ${REGION}
    

## Deploy the CFK operator to your cluster

In this section, you deploy the Confluent for Kubernetes (CFK) operator using a Helm chart and then deploy a Kafka cluster.

  1. Add the Confluent Helm Chart repository:
         
         helm repo add confluentinc https://packages.confluent.io/helm
         

  2. Add a namespace for the CFK operator and the Kafka cluster:
         
         kubectl create ns kafka
         

  3. Deploy the CFK cluster operator using Helm:
         
         helm install confluent-operator confluentinc/confluent-for-kubernetes -n kafka
         

To enable CFK to manage resources across all namespaces, add the parameter `--set-namespaced=false` to the Helm command.

  4. Verify that the Confluent operator has been deployed successfully using Helm:
         
         helm ls -n kafka
         

The output is similar to the following:
         
         NAME                  NAMESPACE  REVISION UPDATED                                  STATUS      CHART                                APP VERSION
         confluent-operator    kafka      1        2023-07-07 10:57:45.409158 +0200 CEST    deployed    confluent-for-kubernetes-0.771.13    2.6.0
         




## Deploy Kafka

In this section, you deploy Kafka in a basic configuration and then try various advanced configuration scenarios to address availability, security, and observability requirements.

### Basic configuration

The basic configuration for the Kafka instance includes the following components:

  * Three replicas of Kafka brokers, with a minimum of two available replicas required for cluster consistency.
  * Three replicas of ZooKeeper nodes, forming a cluster.
  * Two Kafka listeners: one without authentication, and one utilizing TLS authentication with a certificate generated by CFK.
  * Java _MaxHeapSize_ and _MinHeapSize_ set to 4 GB for Kafka.
  * CPU resource allocation of 1 CPU request and 2 CPU limits, and 5 GB memory requests and limits for Kafka (4 GB for the main service and 0.5 GB for the metrics exporter) and 3 GB for Zookeeper (2 GB for the main service and 0.5 GB for the metrics exporter).
  * 100 GB of storage allocated to each Pod using the `premium-rwo` storageClass, 100 for Kafka Data and 90/10 for Zookeeper Data/Log.
  * Tolerations, nodeAffinities, and podAntiAffinities configured for each workload, ensuring proper distribution across nodes, utilizing their respective node pools and different zones.
  * Communication inside the cluster secured by self-signed certificates using a Certificate Authority that you provide.



This configuration represents the minimal setup required to create a production-ready Kafka cluster. The following sections demonstrate custom configurations to address aspects such as cluster security, Access Control Lists (ACLs), topic management, certificate management and more.

### Create a basic Kafka cluster

  1. Generate a CA pair:
         
         openssl genrsa -out ca-key.pem 2048
         openssl req -new -key ca-key.pem -x509 \
           -days 1000 \
           -out ca.pem \
           -subj "/C=US/ST=CA/L=Confluent/O=Confluent/OU=Operator/CN=MyCA"
         

Confluent for Kubernetes provides auto-generated certificates for Confluent Platform components to use for TLS network encryption. You must generate and provide a Certificate Authority (CA).

  2. Create a Kubernetes Secret for the certificate authority:
         
         kubectl create secret tls ca-pair-sslcerts --cert=ca.pem --key=ca-key.pem -n kafka
         

The name of the Secret is [predefined](https://github.com/confluentinc/confluent-kubernetes-examples/blob/master/security/production-secure-deploy-auto-gen-certs/README.rst)

  3. Create a new Kafka cluster using the basic configuration:
         
         kubectl apply -n kafka -f kafka-confluent/manifests/01-basic-cluster/my-cluster.yaml
         

This command creates a Kafka custom resource and Zookeeper custom resource of the CFK operator that include CPU and memory requests and limits, block storage requests, and taints and affinities to distribute the provisioned Pods across Kubernetes nodes.

  4. Wait a few minutes while Kubernetes starts the required workloads:
         
         kubectl wait pods -l app=my-cluster --for condition=Ready --timeout=300s -n kafka
         

  5. Verify that the Kafka workloads were created:
         
         kubectl get pod,svc,statefulset,deploy,pdb -n kafka
         

The output is similar to the following:
         
         NAME                                    READY   STATUS  RESTARTS   AGE
         pod/confluent-operator-864c74d4b4-fvpxs   1/1   Running   0        49m
         pod/my-cluster-0                        1/1   Running   0        17m
         pod/my-cluster-1                        1/1   Running   0        17m
         pod/my-cluster-2                        1/1   Running   0        17m
         pod/zookeeper-0                         1/1   Running   0        18m
         pod/zookeeper-1                         1/1   Running   0        18m
         pod/zookeeper-2                         1/1   Running   0        18m
         
         NAME                          TYPE      CLUSTER-IP   EXTERNAL-IP   PORT(S)                                                        AGE
         service/confluent-operator    ClusterIP   10.52.13.164   <none>      7778/TCP                                                       49m
         service/my-cluster            ClusterIP   None         <none>      9092/TCP,8090/TCP,9071/TCP,7203/TCP,7777/TCP,7778/TCP,9072/TCP   17m
         service/my-cluster-0-internal   ClusterIP   10.52.2.242  <none>      9092/TCP,8090/TCP,9071/TCP,7203/TCP,7777/TCP,7778/TCP,9072/TCP   17m
         service/my-cluster-1-internal   ClusterIP   10.52.7.98   <none>      9092/TCP,8090/TCP,9071/TCP,7203/TCP,7777/TCP,7778/TCP,9072/TCP   17m
         service/my-cluster-2-internal   ClusterIP   10.52.4.226  <none>      9092/TCP,8090/TCP,9071/TCP,7203/TCP,7777/TCP,7778/TCP,9072/TCP   17m
         service/zookeeper             ClusterIP   None         <none>      2181/TCP,7203/TCP,7777/TCP,3888/TCP,2888/TCP,7778/TCP          18m
         service/zookeeper-0-internal  ClusterIP   10.52.8.52   <none>      2181/TCP,7203/TCP,7777/TCP,3888/TCP,2888/TCP,7778/TCP          18m
         service/zookeeper-1-internal  ClusterIP   10.52.12.44  <none>      2181/TCP,7203/TCP,7777/TCP,3888/TCP,2888/TCP,7778/TCP          18m
         service/zookeeper-2-internal  ClusterIP   10.52.12.134   <none>      2181/TCP,7203/TCP,7777/TCP,3888/TCP,2888/TCP,7778/TCP          18m
         
         NAME                        READY   AGE
         statefulset.apps/my-cluster   3/3   17m
         statefulset.apps/zookeeper  3/3   18m
         
         NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
         deployment.apps/confluent-operator   1/1   1          1         49m
         
         NAME                                  MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         poddisruptionbudget.policy/my-cluster   N/A           1               1                   17m
         poddisruptionbudget.policy/zookeeper  N/A           1               1                   18m
         




The operator creates the following resources:

  * Two StatefulSets for Kafka and ZooKeeper.
  * Three Pods for Kafka broker replicas.
  * Three Pods for ZooKeeper replicas.
  * Two `PodDisruptionBudget` resources, ensuring a maximum one unavailable replica for cluster consistency.
  * The Service `my-cluster` which serves as the bootstrap server for Kafka clients connecting from within the Kubernetes cluster. All internal Kafka listeners are available in this Service.
  * The Service `zookeeper` which allows Kafka brokers to connect to ZooKeeper nodes as clients.



## Authentication and user management

This section shows you how to enable the authentication and authorization to secure Kafka Listeners and share credentials with clients.

Confluent for Kubernetes supports various authentication methods for Kafka, such as:

  * [SASL/PLAIN authentication](https://docs.confluent.io/operator/current/co-authenticate.html#co-authenticate-kafka-plain): Clients use a username and password for authentication. The username and password are stored server-side in a Kubernetes secret.
  * [SASL/PLAIN with LDAP authentication](https://docs.confluent.io/operator/current/co-authenticate.html#co-authenticate-kafka-plain-ldap): Clients use a username and password for authentication. The credentials are stored in an LDAP server.
  * [mTLS authentication](https://docs.confluent.io/operator/current/co-authenticate.html#co-authenticate-kafka-mtls): Clients use TLS certificates for authentication.



### Limitations

  * CFK does not provide Custom Resources for user management. However, you can store credentials in Secrets and refer to Secrets to in listener specs.
  * Although there's no Custom Resource to manage ACLs directly, the official [Confluent for Kubernetes](https://docs.confluent.io/platform/current/kafka/authorization.html) provides guidance on configuring ACLs using the Kafka CLI.



### Create a user

This section shows you how to deploy a CFK operator that demonstrates user management capabilities, including:

  * A Kafka cluster with password-based authentication (SASL/PLAIN) enabled on one of the listeners
  * A `KafkaTopic`with 3 replicas
  * User credentials with read and write permissions


  1. Create a Secret with user credentials:
         
         export USERNAME=my-user
         export PASSWORD=$(openssl rand -base64 12)
         kubectl create secret generic my-user-credentials -n kafka \
           --from-literal=plain-users.json="{\"$USERNAME\":\"$PASSWORD\"}"
         

Credentials should be stored in the following format:
         
         {
         "username1": "password1",
         "username2": "password2",
         ...
         "usernameN": "passwordN"
         }
         

  2. Configure Kafka cluster to use a listener with password-based authentication SCRAM-SHA-512 authentication on port 9094:
         
         kubectl apply -n kafka -f kafka-confluent/manifests/02-auth/my-cluster.yaml
         

  3. Set up a topic and a client Pod to interact with your Kafka cluster and execute Kafka commands:
         
         kubectl apply -n kafka -f kafka-confluent/manifests/02-auth/my-topic.yaml
         kubectl apply -n kafka -f kafka-confluent/manifests/02-auth/kafkacat.yaml
         

GKE mounts the Secret `my-user-credentials` to the client Pod as a [Volume](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod).

  4. When the client Pod is ready, connect to it and start producing and consuming messages using the provided credentials:
         
         kubectl wait pod kafkacat --for=condition=Ready --timeout=300s -n kafka
         kubectl exec -it kafkacat -n kafka -- /bin/sh
         

  5. Produce a message using the `my-user` credentials and then consume the message to verify its receipt.
         
         export USERNAME=$(cat /my-user/plain-users.json|cut -d'"' -f 2)
         export PASSWORD=$(cat /my-user/plain-users.json|cut -d'"' -f 4)
         echo "Message from my-user" |kcat \
           -b my-cluster.kafka.svc.cluster.local:9094 \
           -X security.protocol=SASL_SSL \
           -X sasl.mechanisms=PLAIN \
           -X sasl.username=$USERNAME \
           -X sasl.password=$PASSWORD  \
           -t my-topic -P
         kcat -b my-cluster.kafka.svc.cluster.local:9094 \
           -X security.protocol=SASL_SSL \
           -X sasl.mechanisms=PLAIN \
           -X sasl.username=$USERNAME \
           -X sasl.password=$PASSWORD  \
           -t my-topic -C
         

The output is similar to the following:
         
         Message from my-user
         % Reached end of topic my-topic [1] at offset 1
         % Reached end of topic my-topic [2] at offset 0
         % Reached end of topic my-topic [0] at offset 0
         

Type `CTRL+C` to stop the consumer process. If you get a `Connect refused` error, wait a few minutes and then try again.

  6. Exit the Pod shell
         
         exit
         




## Backups and disaster recovery

Using the Confluent operator, you can implement efficient backup strategies by following certain patterns.

You can use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) to backup:

  * Kubernetes resource manifests.
  * Confluent API custom resources and their definitions extracted from the Kubernetes API server of the cluster undergoing backup.
  * Volumes that correspond to PersistentVolumeClaim resources found in the manifests.



You can also perform a manual backup of your Kafka cluster. You should backup:

  * The Kafka configuration, which includes all custom resources of the Confluent API such as `KafkaTopics`or`Connect`
  * The data, which is stored in the PersistentVolumes of the Kafka brokers



Storing Kubernetes resource manifests, including Confluent configurations, in Git repositories can eliminate the need for a separate backup for Kafka configuration as the resources can be reapplied to a new Kubernetes cluster when necessary.

To safeguard Kafka data recovery in scenarios where a Kafka server instance, or Kubernetes cluster where Kafka is deployed, is lost, we recommend that you configure the Kubernetes storage class used for provisioning volumes for Kafka brokers with the `reclaimPolicy` option set to `Retain`. We also recommended that you take [snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) of Kafka broker volumes.

The following manifest describes a StorageClass that uses the `reclaimPolicy` option `Retain`:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: premium-rwo-retain
    ...
    reclaimPolicy: Retain
    volumeBindingMode: WaitForFirstConsumer
    

The following example shows the StorageClass added to the `spec` of a Kafka cluster custom resource:
    
    
    ...
    spec:
      ...
      dataVolumeCapacity: 100Gi
      storageClass:
      name: premium-rwo-retain
    

With this configuration, PersistentVolumes provisioned using the storage class are not deleted even when the corresponding PersistentVolumeClaim is deleted.

To recover the Kafka instance on a new Kubernetes cluster using the existing configuration and broker instance data:

  1. Apply the existing Confluent custom resources (`Kafka`, `KafkaTopic`, `Zookeeper`, etc.) to a new Kubernetes cluster
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

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
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

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
