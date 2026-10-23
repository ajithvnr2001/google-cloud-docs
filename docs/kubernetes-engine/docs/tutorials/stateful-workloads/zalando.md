---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/zalando/
title: Deploy PostgreSQL to GKE using Zalando \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:11.709741+00:00
---

# Deploy PostgreSQL to GKE using Zalando  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/zalando/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy PostgreSQL to GKE using Zalando Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

The guide shows you how to use the [Zalando Postgres operator](https://github.com/zalando/postgres-operator) to deploy Postgres clusters to Google Kubernetes Engine (GKE).

[PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system with several decades of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

This guide is intended for platform administrators, cloud architects, and operations professionals interested in running PostgreSQL as a database application on GKE instead of using [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).

## Objectives

  * Plan and deploy GKE infrastructure for Postgres
  * Deploy and configure the Zalando Postgres operator
  * Configure Postgres using the operator to ensure availability, security, observability and performance



### Benefits

Zalando offers the following benefits:

  * A declarative and Kubernetes-native way to manage and configure the PostgreSQL clusters
  * High availability provided by [Patroni](https://patroni.readthedocs.io/en/latest/)
  * Backup management support using [Cloud Storage buckets](https://postgres-operator.readthedocs.io/en/latest/administrator/#google-cloud-platform-setup)
  * Rolling updates on Postgres cluster changes, including quick minor version updates
  * Declarative [User](https://github.com/zalando/postgres-operator/blob/master/docs/user.md#defining-database-roles-in-the-operator) management with password generation and rotation using custom resources
  * Support for [TLS](https://postgres-operator.readthedocs.io/en/latest/user/#custom-tls-certificates), certificate rotation, and [connection pools](https://postgres-operator.readthedocs.io/en/latest/user/#connection-pooler)
  * Cluster [cloning](https://postgres-operator.readthedocs.io/en/latest/user/#clone-directly) and data replication



### Deployment architecture

In this tutorial, you use the Zalando Postgres operator to deploy and configure a highly available Postgres cluster to GKE. The cluster has one leader replica and two standby (read-only) replicas managed by [Patroni](https://github.com/zalando/patroni). Patroni is an open source solution maintained by Zalando to provide high-availability and auto-failover capabilities to Postgres. In case of leader failure, one standby replica is automatically promoted to a leader role.

You also deploy a highly available regional GKE cluster for Postgres, with multiple >Kubernetes nodes spread across several availability zones. This setup helps ensure fault tolerance, scalability, and geographic redundancy. It allows for rolling updates and maintenance while providing SLAs for uptime and availability. For more information, see [Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).

The following diagram shows a Postgres cluster running on multiple nodes and zones in a GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-zalando-postgresql.svg)

In the diagram, the Postgres `StatefulSet` is deployed across three nodes in three different zones. You can control how GKE deploys to nodes by setting the required Pod [affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) rules on the [`postgresql`](https://github.com/zalando/postgres-operator/blob/master/manifests/complete-postgres-manifest.yaml) custom resource specification. If one zone fails, using the recommended configuration, GKE reschedules Pods on other available nodes in your cluster. For persisting data, you use SSD disks (`premium-rwo` [StorageClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#create_a_storageclass)), which are [recommended](https://docs.cloud.google.com/compute/docs/disks/performance) in most cases for highly loaded databases due to their [low latency and high IOPS](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/disks-image-pricing)
  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

[Cloud Shell](https://docs.cloud.google.com/shell) is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), [Helm](https://helm.sh/), and [Terraform](https://docs.cloud.google.com/docs/terraform). If you don't use Cloud Shell, you must install the gcloud CLI.

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

  7. Enable the Compute Engine, IAM, GKE, Backup for GKE APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com iam.googleapis.com container.googleapis.com gkebackup.googleapis.com

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

  13. Enable the Compute Engine, IAM, GKE, Backup for GKE APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com iam.googleapis.com container.googleapis.com gkebackup.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer, roles/container.admin, roles/iam.serviceAccountAdmin, roles/compute.admin, roles/gkebackup.admin, roles/monitoring.viewer `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



### Set up your environment

To set up your environment, follow these steps

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=postgres
         export REGION=us-central1
         

Replace `PROJECT_ID` with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  2. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  3. Change to the working directory:
         
         cd kubernetes-engine-samples/databases/postgres-zalando
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a private, highly-available, regional GKE cluster.

You can install the operator using a [Standard or Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) cluster.

###  Standard 

The following diagram shows a private regional Standard GKE cluster deployed across three different zones:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-zalando-standard-architecture.svg)

Deploy this infrastructure:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-standard init
    terraform -chdir=terraform/gke-standard apply \
      -var project_id=${PROJECT_ID} \
      -var region=${REGION} \
      -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

When prompted, type `yes`. It might take several minutes for this command to complete and for the cluster to show a ready status.

Terraform creates the following resources:

  * A VPC network and private subnet for the Kubernetes nodes
  * A router to access the internet through NAT
  * A private GKE cluster in the `us-central1` region
  * A node pools with auto scaling enabled (one to two nodes per zone, one node per zone minimum)
  * A `ServiceAccount` with logging and monitoring permissions
  * Backup for GKE for disaster recovery
  * Google Cloud Managed Service for Prometheus for cluster monitoring



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
    ...
    

###  Autopilot 

The following diagram shows a private regional Autopilot GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-zalando-autopilot-architecture.svg)

Deploy the infrastructure:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=terraform/gke-autopilot init
    terraform -chdir=terraform/gke-autopilot apply \
      -var project_id=${PROJECT_ID} \
      -var region=${REGION} \
      -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

When prompted, type `yes`. It might take several minutes for this command to complete and for the cluster to show a ready status.

Terraform creates the following resources:

  * A VPC network and private subnet for the Kubernetes nodes
  * A router to access the internet through NAT
  * A private GKE cluster in the `us-central1` region
  * A `ServiceAccount` with logging and monitoring permission
  * Google Cloud Managed Service for Prometheus for cluster monitoring



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 12 added, 0 changed, 0 destroyed.
    ...
    

### Connect to the cluster

Configure `kubectl` to communicate with the cluster:
    
    
    gcloud container clusters get-credentials ${KUBERNETES_CLUSTER_PREFIX}-cluster --location ${REGION}
    

## Deploy the Zalando operator to your cluster

Deploy the Zalando operator to your Kubernetes cluster using a Helm chart.

  1. Add the Zalando operator Helm Chart repository:
         
         helm repo add postgres-operator-charts https://opensource.zalando.com/postgres-operator/charts/postgres-operator
         

  2. Create a namespace for the Zalando operator and the Postgres cluster:
         
         kubectl create ns postgres
         kubectl create ns zalando
         

  3. Deploy the Zalando operator using the Helm command-line tool:
         
         helm install postgres-operator postgres-operator-charts/postgres-operator -n zalando \
             --set configKubernetes.enable_pod_antiaffinity=true \
             --set configKubernetes.pod_antiaffinity_preferred_during_scheduling=true \
             --set configKubernetes.pod_antiaffinity_topology_key="topology.kubernetes.io/zone" \
             --set configKubernetes.spilo_fsgroup="103"
         

You can't configure `podAntiAffinity` settings directly on the custom resource representing the Postgres cluster. Instead, set `podAntiAffinity` settings globally for all Postgres clusters in the operator settings.

  4. Check the deployment status of the Zalando operator using Helm:
         
         helm ls -n zalando
         

The output is similar to the following:
         
         NAME                 NAMESPACE    REVISION    UPDATED                                STATUS      CHART                       APP VERSION
         postgres-operator    zalando     1           2023-10-13 16:04:13.945614 +0200 CEST    deployed    postgres-operator-1.10.1    1.10.1
         




## Deploy Postgres

The basic configuration for the Postgres cluster instance includes the following components:

  * Three Postgres replicas: one leader and two standby replicas.
  * CPU resource allocation of one CPU request and two CPU limits, with 4 GB memory requests and limits.
  * Tolerations, `nodeAffinities`, and `topologySpreadConstraints` configured for each workload, ensuring proper distribution across Kubernetes nodes, utilizing their respective node pools and different availability zones.



This configuration represents the minimal setup required to create a production-ready Postgres cluster.

The following manifest describes a Postgres cluster:
    
    
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: my-cluster
    spec:
      dockerImage: ghcr.io/zalando/spilo-15:3.0-p1
      teamId: "my-team"
      numberOfInstances: 3
      users:
        mydatabaseowner:
        - superuser
        - createdb
        myuser: []
      databases:
        mydatabase: mydatabaseowner
      postgresql:
        version: "15"
        parameters:
          shared_buffers: "32MB"
          max_connections: "10"
          log_statement: "all"
          password_encryption: scram-sha-256
      volume:
        size: 5Gi
        storageClass: premium-rwo
      enableShmVolume: true
      podAnnotations:
        cluster-autoscaler.kubernetes.io/safe-to-evict: "true"
      tolerations:
      - key: "app.stateful/component"
        operator: "Equal"
        value: "postgres-operator"
        effect: NoSchedule
      nodeAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
            - key: "app.stateful/component"
              operator: In
              values:
              - "postgres-operator"
      resources:
        requests:
          cpu: "1"
          memory: 4Gi
        limits:
          cpu: "2"
          memory: 4Gi
      sidecars:
        - name: exporter
          image: quay.io/prometheuscommunity/postgres-exporter:v0.14.0
          args:
          - --collector.stat_statements
          ports:
          - name: exporter
            containerPort: 9187
            protocol: TCP
          resources:
            limits:
              cpu: 500m
              memory: 256M
            requests:
              cpu: 100m
              memory: 256M
          env:
          - name: "DATA_SOURCE_URI"
            value: "localhost/postgres?sslmode=require"
          - name: "DATA_SOURCE_USER"
            value: "$(POSTGRES_USER)"
          - name: "DATA_SOURCE_PASS"
            value: "$(POSTGRES_PASSWORD)"

This manifest has the following fields:

  * `spec.teamId`: a prefix for the cluster objects that you choose
  * `spec.numberOfInstances`: the total number of instances for a cluster
  * `spec.users`: the user list with [privileges](https://www.postgresql.org/docs/current/sql-createrole.html)
  * `spec.databases`: the database list in the format `dbname: ownername`
  * `spec.postgresql`: postgres parameters
  * `spec.volume`: Persistent Disk parameters
  * `spec.tolerations`: the tolerations Pod template that allows cluster Pods to be scheduled on `pool-postgres` nodes
  * `spec.nodeAffinity`: the `nodeAffinity` Pod template that tells GKE that cluster Pods prefer to be scheduled on `pool-postgres` nodes.
  * `spec.resources`: requests and limits for cluster Pods
  * `spec.sidecars`: a list of sidecar containers, which contains `postgres-exporter`



For more information, see [Cluster manifest reference](https://postgres-operator.readthedocs.io/en/latest/reference/cluster_manifest/) in the Postgres documentation.

### Create a basic Postgres cluster

  1. Create a new Postgres cluster using the basic configuration:
         
         kubectl apply -n postgres -f manifests/01-basic-cluster/my-cluster.yaml
         

This command creates a PostgreSQL Custom Resource of the Zalando operator with:

     * CPU and memory requests and limits
     * Taints and affinities to distribute the provisioned Pod replicas across GKE nodes.
     * A database
     * Two users with database owner permissions
     * A user with no permissions
  2. Wait for GKE to start the required workloads:
         
         kubectl wait pods -l cluster-name=my-cluster  --for condition=Ready --timeout=300s -n postgres
         

This command might take a few minutes to complete.

  3. Verify that GKE created the Postgres workloads:
         
         kubectl get pod,svc,statefulset,deploy,pdb,secret -n postgres
         

The output is similar to the following:
         
         NAME                                    READY   STATUS  RESTARTS   AGE
         pod/my-cluster-0                        1/1     Running   0         6m41s
         pod/my-cluster-1                        1/1     Running   0         5m56s
         pod/my-cluster-2                        1/1     Running   0         5m16s
         pod/postgres-operator-db9667d4d-rgcs8   1/1     Running   0         12m
         
         NAME                        TYPE        CLUSTER-IP  EXTERNAL-IP   PORT(S)   AGE
         service/my-cluster          ClusterIP   10.52.12.109   <none>       5432/TCP   6m43s
         service/my-cluster-config   ClusterIP   None        <none>      <none>  5m55s
         service/my-cluster-repl     ClusterIP   10.52.6.152 <none>      5432/TCP   6m43s
         service/postgres-operator   ClusterIP   10.52.8.176 <none>      8080/TCP   12m
         
         NAME                        READY   AGE
         statefulset.apps/my-cluster   3/3   6m43s
         
         NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
         deployment.apps/postgres-operator   1/1     1           1           12m
         
         NAME                                                MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         poddisruptionbudget.policy/postgres-my-cluster-pdb   1              N/A             0                   6m44s
         
         NAME                                                            TYPE                DATA   AGE
         secret/my-user.my-cluster.credentials.postgresql.acid.zalan.do  Opaque              2   6m45s
         secret/postgres.my-cluster.credentials.postgresql.acid.zalan.do   Opaque            2   6m44s
         secret/sh.helm.release.v1.postgres-operator.v1                  helm.sh/release.v1   1      12m
         secret/standby.my-cluster.credentials.postgresql.acid.zalan.do  Opaque              2   6m44s
         secret/zalando.my-cluster.credentials.postgresql.acid.zalan.do  Opaque              2   6m44s
         




The operator creates the following resources:

  * A Postgres StatefulSet, which controls three Pod replicas for Postgres
  * A `PodDisruptionBudgets`, ensuring a minimum of one available replica
  * The `my-cluster` Service, which targets the leader replica only
  * The `my-cluster-repl` Service, which exposes the Postgres port for incoming connections and for replication between Postgres replicas
  * The `my-cluster-config` headless Service, to get the list of running Postgres Pod replicas
  * Secrets with user credentials for accessing the database and replication between Postgres nodes



## Authenticate to Postgres

You can create Postgres users and assign them database permissions. For example, the following manifest describes a custom resource that assigns users and roles:
    
    
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: my-cluster
    spec:
      ...
      users:
        mydatabaseowner:
        - superuser
        - createdb
        myuser: []
      databases:
        mydatabase: mydatabaseowner
    

In this manifest:

  * The `mydatabaseowner` user has the [`SUPERUSER` and `CREATEDB`](https://www.postgresql.org/docs/16/sql-createrole.html) roles, which permit full administrator rights (i.e. manage Postgres configuration, create new databases, tables, and users). You shouldn't share this user with clients. For example Cloud SQL [doesn't allow](https://docs.cloud.google.com/sql/docs/postgres/users) customers to have access to users with the `SUPERUSER` role.
  * The `myuser` user has no roles assigned. This follows the [best practice](https://wiki.postgresql.org/wiki/Client_Authentication) of using the `SUPERUSER` to create users with least privileges. Granular rights are granted to `myuser` by `mydatabaseowner`. To maintain security, you should only share `myuser` credentials with client applications.



### Store passwords

You should use the `scram-sha-256` [recommended method for storing passwords](https://www.postgresql.org/docs/current/auth-password.html). For example, the following manifest describes a custom resource that specifies `scram-sha-256` encryption using the `postgresql.parameters.password_encryption` field:
    
    
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: my-cluster
    spec:
      ...
      postgresql:
        parameters:
          password_encryption: scram-sha-256
    

### Rotate user credentials

You can [rotate user credentials](https://postgres-operator.readthedocs.io/en/latest/administrator/#password-rotation-in-k8s-secrets) that are stored in Kubernetes Secrets with Zalando. For example, the following manifest describes a custom resource that defines user credential rotation using the `usersWithSecretRotation` field:
    
    
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: my-cluster
    spec:
      ...
      usersWithSecretRotation:
      - myuser
      - myanotheruser
      - ...
    

### Authentication example: connect to Postgres

This section shows you how to deploy an example Postgres client and connect to the database using the password from a Kubernetes Secret.

  1. Run the client Pod to interact with your Postgres cluster:
         
         kubectl apply -n postgres -f manifests/02-auth/client-pod.yaml
         

The credentials of the `myuser` and `mydatabaseowner` users are taken from the related Secrets and mounted as environment variables to the Pod.

  2. Connect to the Pod when it is ready:
         
         kubectl wait pod postgres-client --for=condition=Ready --timeout=300s -n postgres
         kubectl exec -it postgres-client -n postgres -- /bin/bash
         

  3. Connect to Postgres and attempt to create a new table using `myuser` credentials:
         
         PGPASSWORD=$CLIENTPASSWORD psql \
           -h my-cluster \
           -U $CLIENTUSERNAME \
           -d mydatabase \
           -c "CREATE TABLE test (id serial PRIMARY KEY, randomdata VARCHAR ( 50 ) NOT NULL);"
         

The command should fail with an error similar to the following:
         
         ERROR:  permission denied for schema public
         LINE 1: CREATE TABLE test (id serial PRIMARY KEY, randomdata VARCHAR...
         

The command fails because users without assigned privileges by default can only login to Postgres and list databases.

  4. Create a table with `mydatabaseowner` credentials and grant **all** privileges on the table to `myuser`:
         
         PGPASSWORD=$OWNERPASSWORD psql \
           -h my-cluster \
           -U $OWNERUSERNAME \
           -d mydatabase \
           -c "CREATE TABLE test (id serial PRIMARY KEY, randomdata VARCHAR ( 50 ) NOT NULL);GRANT ALL ON test TO myuser;GRANT ALL ON SEQUENCE test_id_seq TO myuser;"
         

The output is similar to the following:
         
         CREATE TABLE
         GRANT
         GRANT
         

  5. Insert random data into the table using `myuser` credentials:
         
         for i in {1..10}; do
           DATA=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13)
           PGPASSWORD=$CLIENTPASSWORD psql \
           -h my-cluster \
           -U $CLIENTUSERNAME \
           -d mydatabase \
           -c "INSERT INTO test(randomdata) VALUES ('$DATA');"
         done
         

The output is similar to the following:
         
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         INSERT 0 1
         

  6. Get the values that you inserted:
         
         PGPASSWORD=$CLIENTPASSWORD psql \
           -h my-cluster \
           -U $CLIENTUSERNAME \
           -d mydatabase \
           -c "SELECT * FROM test;"
         

The output is similar to the following:
         
         id |  randomdata
         ----+---------------
           1 | jup9HYsAjwtW4
           2 | 9rLAyBlcpLgNT
           3 | wcXSqxb5Yz75g
           4 | KoDRSrx3muD6T
           5 | b9atC7RPai7En
           6 | 20d7kC8E6Vt1V
           7 | GmgNxaWbkevGq
           8 | BkTwFWH6hWC7r
           9 | nkLXHclkaqkqy
          10 | HEebZ9Lp71Nm3
         (10 rows)
         

  7. Exit the Pod shell:
         
         exit
         




## Understand how Prometheus collects metrics for your Postgres cluster

The following diagram shows how Prometheus metrics collecting works:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-zalando-metrics-architecture.svg)

In the diagram, a GKE private cluster contains:

  * A Postgres Pod that gathers metrics on path `/` and port `9187`
  * Prometheus-based collectors that process the metrics from the Postgres Pod
  * A `PodMonitoring` resource that sends metrics to Cloud Monitoring



Google Cloud Managed Service for Prometheus supports metrics collection in the Prometheus format. Cloud Monitoring uses an [integrated dashboard](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/postgresql) for Postgres metrics.

Zalando exposes cluster metrics in the Prometheus format using the [postgres_exporter component](https://github.com/prometheus-community/postgres_exporter) as a [sidecar container](https://postgres-operator.readthedocs.io/en/latest/user/#sidecar-support).

  1. Create the [`PodMonitoring`](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) resource to scrape metrics by `labelSelector`:
         
         kubectl apply -n postgres -f manifests/03-prometheus-metrics/pod-monitoring.yaml
         

  2. In the Google Cloud console, go to the **GKE Clusters Dashboard** page.

[Go to GKE Clusters Dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/gmp_gke_cluster)

The dashboard shows a non-zero metrics ingestion rate.

  3. In the Google Cloud console, go to the **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  4. Open the **PostgreSQL Prometheus Overview dashboard**. The dashboard shows the number of fetched rows. It might take several minutes for the dashboard to auto-provision.

  5. Connect to the client Pod:
         
         kubectl exec -it postgres-client -n postgres -- /bin/bash
         

  6. Insert random data:
         
         for i in {1..100}; do
           DATA=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13)
           PGPASSWORD=$CLIENTPASSWORD psql \
           -h my-cluster \
           -U $CLIENTUSERNAME \
           -d mydatabase \
           -c "INSERT INTO test(randomdata) VALUES ('$DATA');"
         done
         

  7. Refresh the page. The **Rows** and **Blocks** graphs update to show the actual database state.

  8. Exit the Pod shell:
         
         exit
         




## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Set environment variables.
         
         export PROJECT_ID=${PROJECT_ID}
         export KUBERNETES_CLUSTER_PREFIX=postgres
         export REGION=us-central1
         

  2. Run the `terraform destroy` command:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform  -chdir=terraform/FOLDER destroy \
           -var project_id=${PROJECT_ID} \
           -var region=${REGION} \
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
         

  5. Delete the GitHub repository:
         
         rm -r ~/kubernetes-engine-samples/
         




## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
