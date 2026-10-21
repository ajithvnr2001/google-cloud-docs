---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql/
title: Deploy a stateful MySQL cluster on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:27.505323+00:00
---

# Deploy a stateful MySQL cluster on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy a stateful MySQL cluster on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document is intended for database administrators, cloud architects, and operations professionals interested in deploying a highly available MySQL topology on Google Kubernetes Engine.

Follow this tutorial to learn how to deploy a [MySQL InnoDB Cluster](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-innodb-cluster.html) and a [MySQL InnoDB ClusterSet](https://dev.mysql.com/doc/mysql-shell/8.0/en/innodb-clusterset.html), in addition to [MySQL Router](https://dev.mysql.com/doc/mysql-router/8.0/en/) middleware on your GKE cluster, and how to perform upgrades.

## Objectives

In this tutorial, you will learn how to: 

  * Create and deploy a stateful Kubernetes service.
  * Deploy a MySQL InnoDB Cluster for high availability.
  * Deploy Router middleware for database operation routing.
  * Deploy a MySQL InnoDB ClusterSet for disaster tolerance.
  * Simulate a MySQL cluster failover.
  * Perform a MySQL version upgrade.



The following sections describe the architecture of the solution you will build in this tutorial.

#### MySQL InnoDB Cluster

In your regional GKE cluster, using a StatefulSet, you deploy a MySQL database instance with the necessary naming and configuration to create a MySQL InnoDB Cluster. To provide fault tolerance and high availability, you deploy three database instance Pods. This ensures that the majority of Pods on different zones are available at any given time for a successful primary election using a consensus protocol, and makes your MySQL InnoDB Cluster tolerant of single zonal failures.

![Architecture diagram showing the relationship between applications, MySQL Router, and MySQL Cluster](https://docs.cloud.google.com/static/kubernetes-engine/images/mysql_innodb_cluster.svg)**Figure 1** : Example architecture of a single MySQL InnoDB Cluster

Once deployed, you designate one Pod as the primary instance to serve both read and write operations. The other two Pods are secondary read-only replicas. If the primary instance experiences an infrastructure failure, you can promote one of these two replica Pods to become the primary.

In a separate namespace, you deploy three MySQL Router Pods to provide connection routing for improved resilience. Instead of directly connecting to the database service, your applications connect to MySQL Router Pods. Each Router Pod is aware of the status and purpose of each MySQL InnoDB Cluster Pod, and routes application operations to the respective healthy Pod. The routing state is cached in the Router Pods and updated from the cluster metadata stored on each node of the MySQL InnoDB Cluster. In the case of an instance failure, the Router adjusts the connection routing to a live instance.

#### MySQL InnoDB ClusterSet

You can create a MySQL InnoDB ClusterSet from an initial MySQL InnoDB Cluster. This lets you increase disaster tolerance if the primary cluster is no longer available.

![Diagram shows how the primary and replica MySQL InnoDB Clusters are kept in sync through asynchronous replication.](https://docs.cloud.google.com/static/kubernetes-engine/images/clusterset.svg)**Figure 2** : Example multi-region ClusterSet architecture which contains one primary cluster and one replica cluster

If the MySQL InnoDB Cluster primary instance is no longer available, you can promote a replica cluster in the ClusterSet to primary. When using MySQL Router middleware, your application does not need to track the health of the primary database instance. Routing is adjusted to send connections to the new primary after the election has occurred. However, it is your responsibility to ensure that applications connecting to your MySQL Router middleware follow best practices for resilience, so that connections are retried if an error occurs during cluster failover.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)
  * [Compute Engine](https://cloud.google.com/compute/disks-image-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)




### Set up roles

  1. Grant roles to your user account. Run the following command once for each of the following IAM roles: `role/storage.objectViewer, role/logging.logWriter, role/artifactregistry.Admin, roles/container.clusterAdmin, role/container.serviceAgent, roles/serviceusage.serviceUsageAdmin, roles/iam.serviceAccountAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



### Set up your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with Docker and the `kubectl` and gcloud CLI.

To use Cloud Shell to set up your environment:

  1. Set environment variables.
         
         export PROJECT_ID=PROJECT_ID
         export CLUSTER_NAME=gkemulti-west
         export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * CONTROL_PLANE_LOCATION: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. For this tutorial, the region is `us-west1`. Typically, you want a region that is close to you.
  2. Set the default environment variables.
         
         gcloud config set project PROJECT_ID
          gcloud config set compute/region CONTROL_PLANE_LOCATION
         

  3. Clone the code repository.
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Change to the working directory.
         
         cd kubernetes-engine-samples/databases/gke-stateful-mysql/kubernetes
         




## Create a GKE cluster

In this section, you create a [regional GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters). Unlike a zonal cluster, a regional cluster's control plane is replicated into several zones, so an outage in a single zone doesn't make the control plane unavailable.

To create a GKE cluster, follow these steps:

### Autopilot

  1. In Cloud Shell, create a GKE Autopilot cluster in the `us-west1` region.
         
         gcloud container clusters create-auto $CLUSTER_NAME \
             --location=$CONTROL_PLANE_LOCATION
         

  2. Get the GKE cluster credentials.
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
           --location=$CONTROL_PLANE_LOCATION
         

  3. Deploy a Service across three zones. This tutorial uses a Kubernetes Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: prepare-three-zone-ha
           labels:
             app: prepare-three-zone-ha
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: prepare-three-zone-ha
           template:
             metadata:
               labels:
                 app: prepare-three-zone-ha
             spec:
               affinity:
                 # Tell Kubernetes to avoid scheduling a replica in a zone where there
                 # is already a replica with the label "app: prepare-three-zone-ha"
                 podAntiAffinity:
                   requiredDuringSchedulingIgnoredDuringExecution:
                   - labelSelector:
                       matchExpressions:
                       - key: app
                         operator: In
                         values:
                         - prepare-three-zone-ha
                     topologyKey: "topology.kubernetes.io/zone"
               containers:
               - name: prepare-three-zone-ha
                 image: busybox:latest
                 command:
                     - "/bin/sh"
                     - "-c"
                     - "while true; do sleep 3600; done"
                 resources:
                   limits:
                     cpu: "500m"
                     ephemeral-storage: "10Mi"
                     memory: "0.5Gi"
                   requests:
                     cpu: "500m"
                     ephemeral-storage: "10Mi"
                     memory: "0.5Gi"
         
         kubectl apply -f prepare-for-ha.yaml
         

By default, Autopilot provisions resources in two zones. The Deployment defined in `prepare-for-ha.yaml` ensures that Autopilot provisions nodes across three zones in your cluster, by setting `replicas:3`, `podAntiAffinity` with `requiredDuringSchedulingIgnoredDuringExecution`, and `topologyKey: "topology.kubernetes.io/zone"`.

  4. Check the status of the Deployment.
         
         kubectl get deployment prepare-three-zone-ha --watch
         

When you see three Pods in the ready state, cancel this command with `CTRL+C`. The output is similar to the following:
         
         NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
         prepare-three-zone-ha   0/3     3            0           9s
         prepare-three-zone-ha   1/3     3            1           116s
         prepare-three-zone-ha   2/3     3            2           119s
         prepare-three-zone-ha   3/3     3            3           2m16s
         

  5. Run this script to validate that your Pods have been deployed across three zones.
         
         bash ../scripts/inspect_pod_node.sh default
         

Each line of the output corresponds to a Pod, and the second column indicates the zone. The output is similar to the following:
         
         gk3-gkemulti-west1-default-pool-eb354e2d-z6mv us-west1-b prepare-three-zone-ha-7885d77d9c-8f7qb
         gk3-gkemulti-west1-nap-25b73chq-739a9d40-4csr us-west1-c prepare-three-zone-ha-7885d77d9c-98fpn
         gk3-gkemulti-west1-default-pool-160c3578-bmm2 us-west1-a prepare-three-zone-ha-7885d77d9c-phmhj
         




### Standard

  1. In Cloud Shell, create a GKE Standard cluster in the `us-west1` region.
         
         gcloud container clusters create $CLUSTER_NAME \
           --location=$CONTROL_PLANE_LOCATION \
           --machine-type="e2-standard-2" \
           --disk-type="pd-standard" \
           --num-nodes="5"
         

  2. Get the GKE cluster credentials.
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
           --location=$CONTROL_PLANE_LOCATION
         




## Deploy MySQL StatefulSets

In this section, you deploy one MySQL StatefulSet. A StatefulSet is a Kubernetes controller that maintains a persistent unique identity for each of its Pods.

Each StatefulSet consists of three MySQL replicas.

To deploy the MySQL StatefulSet, follow these steps:

  1. Create a namespace for the StatefulSet.
         
         kubectl create namespace mysql1
         

  2. Create the MySQL secret.
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: mysql-secret
         type: Opaque
         data:
           password: UGFzc3dvcmQkMTIzNDU2 # Password$123456
           admin-password: UGFzc3dvcmQkMTIzNDU2 # Password$123456
         
         kubectl apply -n mysql1 -f secret.yaml
         

The password is deployed with each Pod, and is used by management scripts and commands for MySQL InnoDB Cluster and ClusterSet deployment in this tutorial.

  3. Create the StorageClass.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: fast-storageclass
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         reclaimPolicy: Retain
         allowVolumeExpansion: true
         parameters:
           type: pd-balanced
         
         kubectl apply -n mysql1 -f storageclass.yaml
         

This storage class uses the `pd-balanced` Persistent Disk type that balances performance and cost. The `volumeBindingMode` field is set to `WaitForFirstConsumer` meaning that GKE delays provisioning of a PersistentVolume until the Pod is created. This setting ensures that the disk is provisioned in the same zone where the Pod is scheduled.

  4. Deploy the StatefulSet of MySQL instance Pods.
         
         apiVersion: apps/v1
         kind: StatefulSet
         metadata:
           name: dbc1
           labels:
             app: mysql
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: mysql
           serviceName: mysql
           template:
             metadata:
               labels:
                 app: mysql
             spec:
               topologySpreadConstraints:
               - maxSkew: 1
                 topologyKey: "topology.kubernetes.io/zone"
                 whenUnsatisfiable: DoNotSchedule
                 labelSelector:
                   matchLabels:
                     app: mysql
               affinity:
                 podAntiAffinity:
                   requiredDuringSchedulingIgnoredDuringExecution:
                   - labelSelector:
                       matchExpressions:
                       - key: app
                         operator: In
                         values:
                         - mysql
                     topologyKey: "kubernetes.io/hostname"
               containers:
               - name: mysql
                 image: mysql/mysql-server:8.0.28
                 command:
                 - /bin/bash
                 args:
                 - -c
                 - >-
                   /entrypoint.sh
                   --server-id=$((20 +  $(echo $HOSTNAME | grep -o '[^-]*$') + 1))
                   --report-host=${HOSTNAME}.mysql.mysql1.svc.cluster.local
                   --binlog-checksum=NONE
                   --enforce-gtid-consistency=ON
                   --gtid-mode=ON
                   --default-authentication-plugin=mysql_native_password
                 env:
                 - name: MYSQL_ROOT_PASSWORD
                   valueFrom:
                     secretKeyRef:
                       name: mysql-secret
                       key: password
                 - name: MYSQL_ADMIN_PASSWORD
                   valueFrom:
                     secretKeyRef:
                       name: mysql-secret
                       key: admin-password
                 - name: MYSQL_ROOT_HOST
                   value: '%'
                 ports:
                 - name: mysql
                   containerPort: 3306
                 - name: mysqlx
                   containerPort: 33060
                 - name: xcom
                   containerPort: 33061
                 resources:
                   limits:
                     cpu: "500m"
                     ephemeral-storage: "1Gi"
                     memory: "1Gi"
                   requests:
                     cpu: "500m"
                     ephemeral-storage: "1Gi"
                     memory: "1Gi"
                 volumeMounts:
                 - name: mysql
                   mountPath: /var/lib/mysql
                   subPath: mysql
                 readinessProbe:
                   exec:
                     command:
                     - bash
                     - "-c"
                     - |
                       mysql -h127.0.0.1 -uroot -p$MYSQL_ROOT_PASSWORD -e'SELECT 1'
                   initialDelaySeconds: 30
                   periodSeconds: 2
                   timeoutSeconds: 1
                 livenessProbe:
                   exec:
                     command:
                     - bash
                     - "-c"
                     - |
                       mysqladmin -uroot -p$MYSQL_ROOT_PASSWORD ping
                   initialDelaySeconds: 30
                   periodSeconds: 10
                   timeoutSeconds: 5
           updateStrategy:
             rollingUpdate:
               partition: 0
             type: RollingUpdate
           volumeClaimTemplates:
           - metadata:
               name: mysql
               labels:
                 app: mysql
             spec:
               storageClassName: fast-storageclass
               volumeMode: Filesystem
               accessModes:
               - ReadWriteOnce
               resources:
                 requests:
                   storage: 10Gi
         
         kubectl apply -n mysql1 -f c1-mysql.yaml
         

This command deploys the StatefulSet consisting of three replicas. In this tutorial, the primary MySQL cluster is deployed across three zones in `us-west1`. The output is similar to the following:
         
         service/mysql created
         statefulset.apps/dbc1 created
         

In this tutorial, the resource limits and requests are set to minimal values to save cost. When planning for a production workload, make sure to set these values appropriately for your organization's needs.

  5. Verify the StatefulSet is created successfully.
         
         kubectl get statefulset -n mysql1 --watch
         

It can take about 10 minutes for the StatefulSet to be ready.

  6. When all three pods are in a ready state, exit the command using `Ctrl+C`. If you see `PodUnscheduleable` errors due to insufficient CPU or memory, wait a few minutes for the control plane to resize to accommodate the large workload.

The output is similar to the following:
         
         NAME   READY   AGE
         dbc1   1/3     39s
         dbc1   2/3     50s
         dbc1   3/3     73s
         

  7. To inspect the placement of your Pods on the GKE cluster nodes, run this script:
         
         bash ../scripts/inspect_pod_node.sh mysql1 mysql
         

The output shows the Pod name, the GKE node name, and the zone where the node is provisioned, and looks similar to the following:
         
         gke-gkemulti-west-5-default-pool-4bcaca65-jch0 us-west1-b dbc1-0
         gke-gkemulti-west-5-default-pool-1ac6e8b5-ddjx us-west1-c dbc1-1
         gke-gkemulti-west-5-default-pool-1f5baa66-bf8t us-west1-a dbc1-2
         

The columns in the output represent the hostname, cloud zone, and Pod name, respectively.

The `topologySpreadConstraints` policy in the StatefulSet specification (`c1-mysql.yaml`) directs the scheduler to place the Pods evenly across the failure domain (`topology.kubernetes.io/zone`).

The `podAntiAffinity` policy enforces the constraint that Pods are required to not be placed on the same GKE cluster node (`kubernetes.io/hostname`). For the MySQL instance Pods, this policy results in the Pods being deployed evenly across the three zones in the Google Cloud region. This placement enables high availability of the MySQL InnoDB Cluster by placing each database instance in a separate failure domain.




## Prepare the primary MySQL InnoDB Cluster

To configure a MySQL InnoDB Cluster, follow these steps:

  1. In the [Cloud Shell](https://docs.cloud.google.com/shell) terminal, set the group replication configurations for the MySQL instances to be added to your cluster.
         
         bash ../scripts/c1-clustersetup.sh
         
         
         POD_ORDINAL_START=${1:-0}
         POD_ORDINAL_END=${2:-2}
         for i in $(seq ${POD_ORDINAL_START} ${POD_ORDINAL_END}); do
           echo "Configuring pod mysql1/dbc1-${i}"
           cat <<'  EOF' | kubectl -n mysql1 exec -i dbc1-${i} -- bash -c 'mysql -uroot -proot --password=${MYSQL_ROOT_PASSWORD}'
         INSTALL PLUGIN group_replication SONAME 'group_replication.so';
         RESET PERSIST IF EXISTS group_replication_ip_allowlist;
         RESET PERSIST IF EXISTS binlog_transaction_dependency_tracking;
         SET @@PERSIST.group_replication_ip_allowlist = 'mysql.mysql1.svc.cluster.local';
         SET @@PERSIST.binlog_transaction_dependency_tracking = 'WRITESET';
           EOF
         done

The script will remotely connect into each of the three MySQL instances to set and persist the following environment variables:

     * `group_replication_ip_allowlist`: allows the instance within the cluster to connect to any instance in the group.
     * `binlog_transaction_dependency_tracking='WRITESET'`: allows parallelized transactions which won't conflict.

In MySQL versions earlier than 8.0.22, use `group_replication_ip_whitelist` instead of `group_replication_ip_allowlist`.

  2. Open a second terminal, so that you do not need to create a shell for each Pod.

  3. Connect to MySQL Shell on the Pod `dbc1-0`.
         
         kubectl -n mysql1 exec -it dbc1-0 -- \
             /bin/bash \
             -c 'mysqlsh --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-0.mysql.mysql1.svc.cluster.local"'
         

  4. Verify the MySQL group replication allowlist for connecting to other instances.
         
         \sql SELECT @@group_replication_ip_allowlist;
         

The output is similar to the following:
         
         +----------------------------------+
         | @@group_replication_ip_allowlist |
         +----------------------------------+
         | mysql.mysql1.svc.cluster.local   |
         +----------------------------------+
         

  5. Verify the `server-id` is unique on each of the instances.
         
         \sql SELECT @@server_id;
         

The output is similar to the following:
         
         +-------------+
         | @@server_id |
         +-------------+
         |          21 |
         +-------------+
         

  6. Configure each instance for MySQL InnoDB Cluster usage and create an administrator account on each instance.
         
         \js
         dba.configureInstance('root@dbc1-0.mysql.mysql1.svc.cluster.local', {password: os.getenv("MYSQL_ROOT_PASSWORD"),clusterAdmin: 'icadmin', clusterAdminPassword: os.getenv("MYSQL_ADMIN_PASSWORD")});
         dba.configureInstance('root@dbc1-1.mysql.mysql1.svc.cluster.local', {password: os.getenv("MYSQL_ROOT_PASSWORD"),clusterAdmin: 'icadmin', clusterAdminPassword: os.getenv("MYSQL_ADMIN_PASSWORD")});
         dba.configureInstance('root@dbc1-2.mysql.mysql1.svc.cluster.local', {password: os.getenv("MYSQL_ROOT_PASSWORD"),clusterAdmin: 'icadmin', clusterAdminPassword: os.getenv("MYSQL_ADMIN_PASSWORD")});
         

All instances must have the same username and password in order for the MySQL InnoDB Cluster to function properly. Each command produces output similar to the following:
         
         ...
         
         The instance 'dbc1-2.mysql:3306' is valid to be used in an InnoDB cluster.
         
         Cluster admin user 'icadmin'@'%' created.
         The instance 'dbc1-2.mysql.mysql1.svc.cluster.local:3306' is already
         ready to be used in an InnoDB cluster.
         
         Successfully enabled parallel appliers.
         

  7. Verify that the instance is ready to be used in a MySQL InnoDB Cluster.
         
         dba.checkInstanceConfiguration()
         

The output is similar to the following:
         
         ...
         
         The instance 'dbc1-0.mysql.mysql1.svc.cluster.local:3306' is valid to be used in an InnoDB cluster.
         
         {
             "status": "ok"
         }
         

Optionally, you can connect to each MySQL instance and repeat this command. For example, run this command to check the status on the `dbc1-1` instance:
         
         kubectl -n mysql1 exec -it dbc1-0 -- \
             /bin/bash \
             -c 'mysqlsh --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-1.mysql.mysql1.svc.cluster.local" \
             --js --execute "dba.checkInstanceConfiguration()"'
         




## Create the primary MySQL InnoDB Cluster

Next, create the MySQL InnoDB Cluster using the MySQL Admin `createCluster` command. Start with the `dbc1-0` instance, which will be the primary instance for the cluster, then add two additional replicas to the cluster.

To initialize the MySQL InnoDB Cluster, follow these steps:

  1. Create the MySQL InnoDB Cluster.
         
         var cluster=dba.createCluster('mycluster');
         

Running the `createCluster` command triggers these operations:

     * Deploy the metadata schema.
     * Verify that the configuration is correct for Group Replication.
     * Register it as the seed instance of the new cluster.
     * Create necessary internal accounts, such as the replication user account.
     * Start Group Replication.

This command initializes a MySQL InnoDB Cluster with the host `dbc1-0` as the primary. The cluster reference is stored in the cluster variable.

The output looks similar to the following:
    
    A new InnoDB cluster will be created on instance 'dbc1-0.mysql:3306'.
    
    Validating instance configuration at dbc1-0.mysql:3306...
    
    This instance reports its own address as dbc1-0.mysql.mysql1.svc.cluster.local:3306
    
    Instance configuration is suitable.
    NOTE: Group Replication will communicate with other instances using
    'dbc1-0.mysql:33061'. Use the localAddress
    option to override.
    
    Creating InnoDB cluster 'mycluster' on
    'dbc1-0.mysql.mysql1.svc.cluster.local:3306'...
    
    Adding Seed Instance...
    Cluster successfully created. Use Cluster.addInstance() to add MySQL
    instances.
    At least 3 instances are needed for the cluster to be able to withstand
    up to one server failure.
    

  2. Add the second instance to the cluster.
         
         cluster.addInstance('icadmin@dbc1-1.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"), recoveryMethod: 'clone'});
         

  3. Add the remaining instance to the cluster.
         
         cluster.addInstance('icadmin@dbc1-2.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"), recoveryMethod: 'clone'});
         

The output is similar to the following:
         
         ...
         The instance 'dbc1-2.mysql:3306' was successfully added to the cluster.
         

  4. Verify the cluster's status.
         
         cluster.status()
         

This command shows the status of the cluster. The topology consists of three hosts, one primary and two secondary instances. Optionally, you can call `cluster.status({extended:1})`.

The output is similar to the following:
         
         {
             "clusterName": "mysql1",
             "defaultReplicaSet": {
                 "name": "default",
                 "primary": "dbc1-0.mysql:3306",
                 "ssl": "REQUIRED",
                 "status": "OK",
                 "statusText": "Cluster is ONLINE and can tolerate up to ONE failure.",
                 "topology": {
                     "dbc1-0.mysql:3306": {
                         "address": "dbc1-0.mysql:3306",
                         "memberRole": "PRIMARY",
                         "mode": "R/W",
                         "readReplicas": {},
                         "replicationLag": null,
                         "role": "HA",
                         "status": "ONLINE",
                         "version": "8.0.28"
                     },
                     "dbc1-1.mysql:3306": {
                         "address": "dbc1-1.mysql:3306",
                         "memberRole": "SECONDARY",
                         "mode": "R/O",
                         "readReplicas": {},
                         "replicationLag": null,
                         "role": "HA",
                         "status": "ONLINE",
                         "version": "8.0.28"
                     },
                     "dbc1-2.mysql:3306": {
                         "address": "dbc1-2.mysql:3306",
                         "memberRole": "SECONDARY",
                         "mode": "R/O",
                         "readReplicas": {},
                         "replicationLag": null,
                         "role": "HA",
                         "status": "ONLINE",
                         "version": "8.0.28"
                     }
                 },
                 "topologyMode": "Single-Primary"
             },
             "groupInformationSourceMember": "dbc1-0.mysql:3306"
         }
         

Optionally, you can call `cluster.status({extended:1})` to obtain additional status details.




### Create a sample database

To create a sample database, follow these steps:

  1. Create a database and load data into the database.
         
         \sql
         create database loanapplication;
         use loanapplication
         CREATE TABLE loan (loan_id INT unsigned AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(30) NOT NULL, lastname VARCHAR(30) NOT NULL , status VARCHAR(30) );
         

  2. Insert sample data into the database. To insert data, you must be connected to the primary instance of the cluster.
         
         INSERT INTO loan (firstname, lastname, status) VALUES ( 'Fred','Flintstone','pending');
         INSERT INTO loan (firstname, lastname, status) VALUES ( 'Betty','Rubble','approved');
         

  3. Verify that the table contains the three rows inserted in the previous step.
         
         SELECT * FROM loan;
         

The output is similar to the following:
         
         +---------+-----------+------------+----------+
         | loan_id | firstname | lastname   | status   |
         +---------+-----------+------------+----------+
         |       1 | Fred      | Flintstone | pending  |
         |       2 | Betty     | Rubble     | approved |
         +---------+-----------+------------+----------+
         2 rows in set (0.0010 sec)
         




## Create a MySQL InnoDB ClusterSet

You can create a MySQL InnoDB ClusterSet to manage replication from your primary cluster to replica clusters, using a dedicated ClusterSet replication channel.

A MySQL InnoDB ClusterSet provides disaster tolerance for MySQL InnoDB Cluster deployments by linking a primary MySQL InnoDB Cluster with one or more replicas of itself in alternate locations, such as multiple zones and multiple regions.

If you closed MySQL Shell, create a new shell by running this command in a new Cloud Shell terminal:
    
    
      kubectl -n mysql1 exec -it dbc1-0 -- \
          /bin/bash -c 'mysqlsh \
          --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-0.mysql.mysql1.svc.cluster.local"'
    

To create a MySQL InnoDB ClusterSet, follow these steps:

  1. In your MySQL Shell terminal, obtain a cluster object.
         
         \js
         cluster=dba.getCluster()
         

The output is similar to the following:
         
         <Cluster:mycluster>
         

  2. Initialize a MySQL InnoDB ClusterSet with the existing MySQL InnoDB Cluster stored in the cluster object as the primary.
         
         clusterset=cluster.createClusterSet('clusterset')
         

The output is similar to the following:
         
         A new ClusterSet will be created based on the Cluster 'mycluster'.
         
         * Validating Cluster 'mycluster' for ClusterSet compliance.
         
         * Creating InnoDB ClusterSet 'clusterset' on 'mycluster'...
         
         * Updating metadata...
         
         ClusterSet successfully created. Use ClusterSet.createReplicaCluster() to add Replica Clusters to it.
         
         <ClusterSet:clusterset>
         

  3. Check the status of your MySQL InnoDB ClusterSet.
         
         clusterset.status()
         

The output is similar to the following:
         
         {
             "clusters": {
                 "mycluster": {
                     "clusterRole": "PRIMARY",
                     "globalStatus": "OK",
                     "primary": "dbc1-0.mysql:3306"
                 }
             },
             "domainName": "clusterset",
             "globalPrimaryInstance": "dbc1-0.mysql:3306",
             "primaryCluster": "mycluster",
             "status": "HEALTHY",
             "statusText": "All Clusters available."
         }
         

Optionally, you can call `clusterset.status({extended:1})` to obtain additional status details, including information about the cluster.

  4. Exit MySQL Shell.
         
         \q
         




## Deploy a MySQL Router

You can deploy a MySQL Router to direct client application traffic to the proper clusters. Routing is based on the connection port of the application issuing a database operation:

  * _Writes_ are routed to the primary Cluster instance in the primary ClusterSet.
  * _Reads_ can be routed to any instance in the primary Cluster.



When you start a MySQL Router, it is bootstrapped against the MySQL InnoDB ClusterSet deployment. The MySQL Router instances connected with the MySQL InnoDB ClusterSet are aware of any controlled switchovers or emergency failovers and direct traffic to the new primary cluster.

To deploy a MySQL Router, follow these steps:

  1. In the Cloud Shell terminal, deploy the MySQL Router.
         
         kubectl apply -n mysql1 -f c1-router.yaml
         

The output is similar to the following:
         
         configmap/mysql-router-config created
         service/mysql-router created
         deployment.apps/mysql-router created
         

  2. Check the readiness of the MySQL Router deployment.
         
         kubectl -n mysql1 get deployment mysql-router --watch
         

When all three Pods are ready, the output is similar to the following:
         
         NAME           READY   UP-TO-DATE   AVAILABLE   AGE
         mysql-router   3/3     3            0           3m36s
         

If you see a `PodUnschedulable` error in the console, wait a minute or two while GKE provisions more nodes. Refresh, and you should see `3/3 OK`.

  3. Start MySQL Shell on any member of the existing cluster.
         
         kubectl -n mysql1 exec -it dbc1-0 -- \
             /bin/bash -c 'mysqlsh --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-0.mysql"'
         

This command connects to the `dbc1-0` Pod, then starts a shell connected to the `dbc1-0` MySQL instance.

  4. Verify the router configuration.
         
         clusterset=dba.getClusterSet()
         clusterset.listRouters()
         

The output is similar to the following:
         
         {
           "domainName": "clusterset",
           "routers": {
             "mysql-router-7cd8585fbc-74pkm::": {
                 "hostname": "mysql-router-7cd8585fbc-74pkm",
                 "lastCheckIn": "2022-09-22 23:26:26",
                 "roPort": 6447,
                 "roXPort": 6449,
                 "rwPort": 6446,
                 "rwXPort": 6448,
                 "targetCluster": null,
                 "version": "8.0.27"
             },
             "mysql-router-7cd8585fbc-824d4::": {
               ...
             },
             "mysql-router-7cd8585fbc-v2qxz::": {
               ...
             }
           }
         }
         

  5. Exit MySQL Shell.
         
         \q
         

  6. Run this script to inspect the placement of the MySQL Router Pods.
         
         bash ../scripts/inspect_pod_node.sh mysql1 | sort
         

The script shows the node and Cloud Zone placement of the all of the Pods in the `mysql1` namespace, where the output is similar to the following:
         
         gke-gkemulti-west-5-default-pool-1ac6e8b5-0h9v us-west1-c mysql-router-6654f985f5-df97q
         gke-gkemulti-west-5-default-pool-1ac6e8b5-ddjx us-west1-c dbc1-1
         gke-gkemulti-west-5-default-pool-1f5baa66-bf8t us-west1-a dbc1-2
         gke-gkemulti-west-5-default-pool-1f5baa66-kt03 us-west1-a mysql-router-6654f985f5-qlfj9
         gke-gkemulti-west-5-default-pool-4bcaca65-2l6s us-west1-b mysql-router-6654f985f5-5967d
         gke-gkemulti-west-5-default-pool-4bcaca65-jch0 us-west1-b dbc1-0
         

You can observe that the MySQL Router Pods are distributed equally across the zones; that is, not placed on the same node as a MySQL Pod, or on the same node as another MySQL Router Pod.




## Manage GKE and MySQL InnoDB Cluster upgrades

Updates for both MySQL and Kubernetes are released on a regular schedule. Follow operational best practices to update your software environment regularly. By default, GKE manages cluster and node pool upgrades for you. Kubernetes and GKE also provide additional features to facilitate MySQL software upgrades.

### Plan for GKE upgrades

You can take proactive steps and set configurations to mitigate risk and facilitate a smoother cluster upgrade when you are running stateful services, including:

  * **Standard clusters** : Follow [GKE best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters). Choose an appropriate [upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to ensure the upgrades happen during the period of the maintenance window:

    * Choose [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) if cost optimization is important and if your workloads can tolerate a graceful shutdown in less than 60 minutes.
    * Choose [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) if your workloads are less tolerant of disruptions, and a temporary cost increase due to higher resource usage is acceptable.

To learn more, see [Upgrade a cluster running a stateful workload](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/upgrading-stateful-workload#configure_a_node_pool_upgrade_strategy). Autopilot clusters are [automatically upgraded](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot), based on the release channel you selected.

  * Use [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to ensure upgrades happen when you intend them. Before the maintenance window, ensure your database backups are successful.

  * Before allowing traffic to the upgraded MySQL nodes, use Readiness Probes and Liveness Probes to ensure they are ready for traffic.

  * Create Probes that assess whether replication is in sync before accepting traffic. This can be done through custom scripts, depending on the complexity and scale of your database.




#### Set a Pod Disruption Budget (PDB) policy

When a MySQL InnoDB Cluster is running on GKE, there must be a sufficient number of instances running at any time to meet the quorum requirement.

In this tutorial, given a MySQL cluster of three instances, two instances must be available to form a quorum. A `PodDisruptionBudget` policy allows you to limit the number of Pods that can be terminated at any given time. This is useful for both steady state operations of your stateful services and for cluster upgrades.

To ensure that a limited number of Pods are concurrently disrupted, you set the PDB for your workload to `maxUnavailable: 1`. This ensures that at any point in the service operation, no more than one Pod is not running.

**Note:** You can also set the `minAvailable` value to ensure that a minimum number of Pods are running. However, if using `minAvailable` alone, to guarantee cluster availability, make sure that the value is increased if the size of the cluster increases. In contrast, the `maxUnavailable` value provides quorum protection for the cluster without any changes; the tradeoff is that only one instance can be disrupted for upgrade at a time.

The following `PodDisruptionBudget` policy manifest sets the maximum unavailable Pods to one for your MySQL application.
    
    
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: mysql-pdb
    spec:
      maxUnavailable: 1
      selector:
        matchLabels:
          app: mysql

To apply the PDB policy to your cluster, follow these steps:

  1. Apply the PDB policy using `kubectl`.
         
         kubectl apply -n mysql1 -f mysql-pdb-maxunavailable.yaml
         

  2. View the status of the PDB.
         
         kubectl get poddisruptionbudgets -n mysql1 mysql-pdb -o yaml
         

In the `status` section of the output, see the `currentHealthy` and `desiredHealthy` Pods counts. The output is similar to the following:
         
         status:
         ...
           currentHealthy: 3
           desiredHealthy: 2
           disruptionsAllowed: 1
           expectedPods: 3
         ...
         




### Plan for MySQL binary upgrades

Kubernetes and GKE provide features to facilitate upgrades for the MySQL binary. However, you need to perform some operations to prepare for the upgrades.

Keep the following considerations in mind before you begin the upgrade process:

  * Upgrades should first be carried out in a test environment. For production systems, you should perform further testing in a pre-production environment.
  * For some binary releases, you cannot downgrade the version once an upgrade has been performed. Take the time to understand the implications of an upgrade.
  * Replication sources can replicate to a newer version. However, copying from a newer to an older version is typically not supported.
  * Make sure you have a complete database backup before deploying the upgraded version.
  * Keep in mind the ephemeral nature of Kubernetes Pods. Any configuration state stored by the Pod that is not on the persistent volume will be lost when the Pod is redeployed.
  * For MySQL binary upgrades, use the same PDB, node pool update strategy, and Probes as described earlier.



In a production environment, you should follow these best practices:

  * Create a container image with the new version of MySQL.
  * Persist the image build instructions in a source control repository.
  * Use an automated image build and testing pipeline such as Cloud Build, and store the image binary in an image registry such as Artifact Registry.



To keep this tutorial simple, you will not build and persist a container image; instead, you use the public MySQL images.

#### Deploy the upgraded MySQL binary

To perform the MySQL binary upgrade, you issue a declarative command that modifies the image version of the StatefulSet resource. GKE performs the necessary steps to stop the current Pod, deploy a new Pod with the upgraded binary, and attach the persistent disk to the new Pod.

  1. Verify that the PDB was created.
         
         kubectl get poddisruptionbudgets -n mysql1
         

  2. Get the list of stateful sets.
         
         kubectl get statefulsets -n mysql1
         

  3. Get the list of running Pods using the `app` label.
         
         kubectl get pods --selector=app=mysql -n mysql1
         

  4. Update the MySQL image in the stateful set.
         
         kubectl  -n mysql1 \
             set image statefulset/dbc1 \
             mysql=mysql/mysql-server:8.0.30
         

The output is similar to the following:
         
         statefulset.apps/mysql image updated
         

  5. Check the status of the terminating Pods and new Pods.
         
         kubectl get pods --selector=app=mysql -n mysql1
         




#### Validate the MySQL binary upgrade

During the upgrade, you can verify the status of the rollout, the new Pods, and the existing Service.

  1. Confirm the upgrade by running the `rollout status` command.
         
         kubectl rollout status statefulset/dbc1 -n mysql1
         

The output is similar to the following:
         
         partitioned roll out complete: 3 new pods have been updated...
         

  2. Confirm the image version by inspecting the stateful set.
         
         kubectl get statefulsets -o wide -n mysql1
         

The output is similar to the following:
         
         NAME   READY   AGE   CONTAINERS   IMAGES
         dbc1   3/3     37m   mysql        mysql/mysql-server:8.0.30
         

  3. Check the status of the cluster.
         
         kubectl -n mysql1 \
              exec -it dbc1-0 -- \
                /bin/bash \
                  -c 'mysqlsh \
                  --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-1.mysql.mysql1.svc.cluster.local" \
                  --js \
                  --execute "print(dba.getClusterSet().status({extended:1})); print(\"\\n\")"'
         

For each cluster instance, look for the status and version values in the output. The output is similar to the following:
         
         ...
           "status": "ONLINE",
           "version": "8.0.30"
         ...
         




#### Rollback the last app deployment rollout

**Warning:** Some binary versions cannot be downgraded. Understand the implications and constraints before performing a binary upgrade.

When you revert the deployment of an upgraded binary version, the rollout process is reversed and a new set of Pods is deployed with the previous image version.

To revert the deployment to the previous working version, use the `rollout undo` command:
    
    
    kubectl rollout undo statefulset/dbc1 -n mysql1
    

The output is similar to the following:
    
    
    statefulset.apps/dbc1 rolled back
    

## Scale your database cluster horizontally

To scale your MySQL InnoDB Cluster horizontally, you add additional nodes to the GKE cluster node pool (only required if you are using Standard), deploy additional MySQL instances, then add each instance to the existing MySQL InnoDB Cluster.

### Add nodes to your Standard cluster

This operation is not needed if you are using a Autopilot cluster.

To add nodes to your Standard cluster, follow the instructions below for Cloud Shell or the Google Cloud console. For detailed steps, see [Resize a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool)

### gcloud

In Cloud Shell, resize the default node pool to eight instances in each managed instance group.
    
    
    gcloud container clusters resize ${CLUSTER_NAME} \
         --node-pool default-pool \
         --num-nodes=8
    

### Console

To add nodes to your Standard cluster:

  1. Open the `gkemulti-west1` Cluster page in the Google Cloud console.
  2. Select **Nodes** , and click on **default pool**.
  3. Scroll down to **Instances groups**.
  4. For each instance group, resize the `Number of nodes` value from 5 to 8 nodes.



### Add MySQL Pods to the primary cluster

To deploy additional MySQL Pods to scale your cluster horizontally, follow these steps:

  1. In Cloud Shell, update the number of replicas in the MySQL deployment from three replicas to five replicas.
         
         kubectl scale  -n mysql1 --replicas=5 -f c1-mysql.yaml
         

  2. Verify the progress of the deployment.
         
         kubectl -n mysql1 get pods --selector=app=mysql -o wide
         

To determine whether the Pods are ready, use the `--watch` flag to watch the deployment. If you are using Autopilot clusters and see `Pod Unschedulable` errors, this might indicate GKE is provisioning nodes to accommodate the additional Pods.

  3. Configure the group replication settings for the new MySQL instances to add to the cluster
         
         bash ../scripts/c1-clustersetup.sh 3 4
         

The script submits the commands to the instances running on the Pods with ordinals 3 through 4.

  4. Open MySQL Shell.
         
         kubectl -n mysql1 \
           exec -it dbc1-0 -- \
               /bin/bash \
                 -c 'mysqlsh \
                 --uri="root:$MYSQL_ROOT_PASSWORD@dbc1-0.mysql"'
         

  5. Configure the two new MySQL instances.
         
         dba.configureInstance('root:$MYSQL_ROOT_PASSWORD@dbc1-3.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"),clusterAdmin: 'icadmin', clusterAdminPassword: os.getenv("MYSQL_ADMIN_PASSWORD")});
         dba.configureInstance('root:$MYSQL_ROOT_PASSWORD@dbc1-4.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"),clusterAdmin: 'icadmin', clusterAdminPassword: os.getenv("MYSQL_ADMIN_PASSWORD")});
         

The commands check if the instance is configured properly for MySQL InnoDB Cluster usage and perform the necessary configuration changes.

  6. Add one of the new instances to the primary cluster.
         
         cluster = dba.getCluster()
         cluster.addInstance('icadmin@dbc1-3.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"), recoveryMethod: 'clone'});
         

  7. Add a second new instance to the primary cluster.
         
         cluster.addInstance('icadmin@dbc1-4.mysql', {password: os.getenv("MYSQL_ROOT_PASSWORD"), recoveryMethod: 'clone'});
         

  8. Obtain the ClusterSet status, which also includes the Cluster status.
         
         clusterset = dba.getClusterSet()
         clusterset.status({extended: 1})
         

The output is similar to the following:
         
         "domainName": "clusterset",
         "globalPrimaryInstance": "dbc1-0.mysql:3306",
         "metadataServer": "dbc1-0.mysql:3306",
         "primaryCluster": "mycluster",
         "status": "HEALTHY",
         "statusText": "All Clusters available."
         

  9. Exit MySQL Shell.
         
         \q
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to avoid billing is to delete the project you created for the tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * Learn more about how the [Google Cloud Observability MySQL integration](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mysql) collects performance metrics related to InnoDB.
  * Learn more about [backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke), a service for backing up and restoring workloads in GKE.
  * Explore [Persistent Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in more detail.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
