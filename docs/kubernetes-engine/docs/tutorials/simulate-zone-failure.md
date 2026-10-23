---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/simulate-zone-failure/
title: Simulate a zone failure in GKE regional clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:37.080083+00:00
---

# Simulate a zone failure in GKE regional clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/simulate-zone-failure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Simulate a zone failure in GKE regional clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

A common regulatory requirement is that a company can demonstrate their disaster recovery (DR) capability. For applications that run in the cloud, this requirement includes the reliability and availability of services when servers hosted in one zone become unavailable for a period of time. This document is for Admins and architects, Operators, and Backup and disaster recovery (DR) administrators that want to learn how to simulate a zone failover when using a Google Kubernetes Engine (GKE) Standard regional cluster.

[GKE regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) are created in a user-chosen region, and run the control plane on VMs situated in multiple zones within the chosen region. GKE Autopilot clusters are always regional, and GKE Standard clusters can be regional or zonal. This tutorial uses a GKE Standard regional cluster. Cluster nodes communicate with the control plane through a load balancer, which means that the node location and the control plane VM location don't always match. In the Google Cloud console, you can't disable a particular zone when you use a regional cluster. For more information, see [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

This tutorial provides three different methods for simulating zone failure. You can simulate a zone failure and verify the correct application response using whichever method is required for your own compliance purposes.

The methods in this document also apply to [zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters), including single-zone and multi-zonal. These methods only affect the nodes in targeted zones, and the GKE control plane isn't affected.

## Objectives

  * Create a regional GKE Standard cluster using the default configuration.
  * Deploy a sample microservices application to the regional cluster.
  * Simulate a zone outage using one of the following three methods: 
    * Reduce the node pool's zones in a regional cluster.
    * Use a single-zone node pool.
    * Cordon and drain the target failure-zone's nodes.
  * Verify the microservices availability.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * Compute Engine
  * GKE Standard mode cluster



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  7. Enable the Kubernetes Engine API, Compute Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com compute.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  13. Enable the Kubernetes Engine API, Compute Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com compute.googleapis.com




## Create a regional Standard cluster

Before simulating a zone failure, create a regional cluster with a multi-zone node pool. The cluster's control plane and nodes are replicated across multiple zones in the specified region.

Use the Google Cloud CLI to create the cluster:

  1. Create a new GKE Standard cluster using the default configuration:
         
         gcloud container clusters create CLUSTER_NAME \
           --location CONTROL_PLANE_LOCATION \
           --num-nodes 2
         

Replace the following parameters:

     * `CLUSTER_NAME`: the name for your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster, such as `us-central1`.

GKE takes a few minutes to create the cluster and verify everything works correctly. Two nodes are created in each zone of the region that you specify.

  2. Check the zones of each node created in the previous step:
         
         kubectl get node -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The output looks like the following example:
         
         NAME                                    ZONE                INT_IP
         regional-cluster-1-default-pool-node1   asia-southeast1-c   10.128.0.37
         regional-cluster-1-default-pool-node2   asia-southeast1-c   10.128.0.36
         regional-cluster-1-default-pool-node3   asia-southeast1-b   10.128.0.38
         regional-cluster-1-default-pool-node4   asia-southeast1-b   10.128.0.33
         regional-cluster-1-default-pool-node5   asia-southeast1-a   10.128.0.35
         regional-cluster-1-default-pool-node6   asia-southeast1-a   10.128.0.34
         

  3. Connect to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION
         




## Deploy a sample microservices application

To see the effect of the simulated failover in this document, deploy a sample microservices-based application to your cluster. In this document, you use the [sample Cymbal Bank application](https://github.com/GoogleCloudPlatform/bank-of-anthos):

  1. In your shell, clone the following GitHub repository and change into the directory:
         
         git clone https://github.com/GoogleCloudPlatform/bank-of-anthos.git
         cd bank-of-anthos/
         

  2. Deploy the Cymbal Bank sample application to the GKE cluster you created in the previous section:
         
         kubectl apply -f ./extras/jwt/jwt-secret.yaml
         kubectl apply -f ./kubernetes-manifests
         

  3. Wait for the Pods to be ready:
         
         kubectl get pods
         

  4. After a few minutes, you should see the Pods in a `Running` state:
         
         NAME                                  READY   STATUS    RESTARTS   AGE
         accounts-db-0                         1/1     Running   0          16s
         balancereader-7dc7d9ff57-sstm5        0/1     Running   0          15s
         contacts-7ddc76d94-rr28x              0/1     Running   0          14s
         frontend-747b84bff4-2mtlv             0/1     Running   0          13s
         ledger-db-0                           1/1     Running   0          13s
         ledgerwriter-f6cc7889d-9qjfg          0/1     Running   0          13s
         loadgenerator-57d4cb57cc-zqvqb        1/1     Running   0          13s
         transactionhistory-5dd7c7fd77-lwkv8   0/1     Running   0          12s
         userservice-cd5ddb4bb-wwhml           0/1     Running   0          12s
         

  5. When the Pods are all in a `Running` state, get the frontend Service external IP address:
         
         kubectl get service frontend | awk '{print $4}'
         

  6. In a web browser window, open the IP address shown in the output of the `kubectl get service` command to access your instance of Cymbal Bank.

The default credentials are automatically populated, so you can sign in to the app and explore some of the sample transactions and balances. There are no specific actions you need to take, other than to confirm that the Cymbal Bank runs successfully. It might take a minute or two for all the Services to correctly start and let you sign in. Wait until all the Pods are in a `Running` state and you can successfully sign in to the Cymbal Bank site before you move on to the next section and simulate a zone failure.




## Simulate a zone failure

In this section, you simulate a failure with one of the zones. There are three different ways you can simulate this failover. You only need to choose one method. Simulate a zone failure and verify the correct application response using whichever method is required for your own compliance purposes.

**Note:** If your applications contain stateful workloads, such as databases, make sure that the data is stored in a detached Persistent Disk Volume and that read replicas are deployed across multiple zones. Check this data storage before you delete a node pool (simulate a zone failure), or consider using regional Persistent Disk. For additional protection, you can also use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke). StatefulSets data consistency, reliability, and mitigation strategy is outside the scope of this document. If you don't consider these storage factors, there's a risk of potential loss of data. Consult the documentation for your specific database or stateful application, such as PostgreSQL, SQL Server, MongoDB, Redis, or Cassandra to learn about their recommended high availability and disaster recovery strategies.

### Reduce node pool zones

By default, a node pool of a regional cluster has nodes that span across all zones of its region. In the following diagram, Cloud Load Balancing distributes traffic to a node pool that spans three zones. Each zone has two nodes, and your Pods can run in nodes in any of these zones.

![A load balancer directs traffic to a regional cluster that runs across three zones. Each zone has two nodes in it.](https://docs.cloud.google.com/static/kubernetes-engine/images/reduce-node-pools.svg)

In this section, you simulate a zone failure by updating the node pool to only run in two out of three zones. This approach verifies that your application can respond to the loss of a zone by correctly redistributing Pods and traffic across other zones.

To update the node pool to only run in certain zones and simulate failure, complete the following steps:

  1. Check the availability of regional cluster and Services:
         
         kubectl get pods -o wide ; kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The result is similar to the following example output:
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP          NODE
         accounts-db-0                         1/1     Running   0          6m30s   10.28.1.5   regional-cluster-1-default-pool-node3
         balancereader-7dc7d9ff57-shwg5        1/1     Running   0          6m30s   10.28.5.6   regional-cluster-1-default-pool-node1
         contacts-7ddc76d94-qv4x5              1/1     Running   0          6m29s   10.28.4.6   regional-cluster-1-default-pool-node2
         frontend-747b84bff4-xvjxq             1/1     Running   0          6m29s   10.28.3.6   regional-cluster-1-default-pool-node6
         ledger-db-0                           1/1     Running   0          6m29s   10.28.5.7   regional-cluster-1-default-pool-node1
         ledgerwriter-f6cc7889d-mttmb          1/1     Running   0          6m29s   10.28.1.6   regional-cluster-1-default-pool-node3
         loadgenerator-57d4cb57cc-7fvrc        1/1     Running   0          6m29s   10.28.4.7   regional-cluster-1-default-pool-node2
         transactionhistory-5dd7c7fd77-cmc2w   1/1     Running   0          6m29s   10.28.3.7   regional-cluster-1-default-pool-node6
         userservice-cd5ddb4bb-zfr2g           1/1     Running   0          6m28s   10.28.5.8   regional-cluster-1-default-pool-node1
         
         NAME                                    ZONE                INT_IP
         regional-cluster-1-default-pool-node5   asia-southeast1-c   10.148.0.6
         regional-cluster-1-default-pool-node6   asia-southeast1-c   10.148.0.7
         regional-cluster-1-default-pool-node2   asia-southeast1-a   10.148.0.8
         regional-cluster-1-default-pool-node1   asia-southeast1-a   10.148.0.9
         regional-cluster-1-default-pool-node3   asia-southeast1-b   10.148.0.5
         regional-cluster-1-default-pool-node4   asia-southeast1-b   10.148.0.4
         

In this example, all the Cymbal Bank workloads are deployed in all zones. To simulate a failure, you disable one of the zones, such as `asia-southeast1-c`, where the frontend service is deployed.

  2. Simulate a zone outage. Update the existing node pool (`default-pool`) to only specify two zones out of the three zones:
         
         gcloud container node-pools update default-pool \
             --cluster=CLUSTER_NAME \
             --node-locations=ZONE_A, ZONE_B \
             --location=CONTROL_PLANE_LOCATION
         

Replace `ZONE_A, ZONE_B` with the two zones where you want the node pool to continue to running.

  3. Verify microservices availability after you update the node pool:
         
         kubectl get pods -o wide ; kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The output should look like the following example:
         
         NAME                                    ZONE                INT_IP
         regional-cluster-1-default-pool-node2   asia-southeast1-a   10.148.0.8
         regional-cluster-1-default-pool-node1   asia-southeast1-a   10.148.0.9
         regional-cluster-1-default-pool-node3   asia-southeast1-b   10.148.0.5
         regional-cluster-1-default-pool-node4   asia-southeast1-b   10.148.0.4
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP          NODE
         accounts-db-0                         1/1     Running   0          28m     10.28.1.5   regional-cluster-1-default-pool-node3
         balancereader-7dc7d9ff57-shwg5        1/1     Running   0          28m     10.28.5.6   regional-cluster-1-default-pool-node1
         contacts-7ddc76d94-qv4x5              1/1     Running   0          28m     10.28.4.6   regional-cluster-1-default-pool-node2
         frontend-747b84bff4-mdnkd             1/1     Running   0          9m21s   10.28.1.7   regional-cluster-1-default-pool-node3
         ledger-db-0                           1/1     Running   0          28m     10.28.5.7   regional-cluster-1-default-pool-node1
         ledgerwriter-f6cc7889d-mttmb          1/1     Running   0          28m     10.28.1.6   regional-cluster-1-default-pool-node3
         loadgenerator-57d4cb57cc-7fvrc        1/1     Running   0          28m     10.28.4.7   regional-cluster-1-default-pool-node2
         transactionhistory-5dd7c7fd77-w2vqs   1/1     Running   0          9m20s   10.28.4.8   regional-cluster-1-default-pool-node2
         userservice-cd5ddb4bb-zfr2g           1/1     Running   0          28m     10.28.5.8   regional-cluster-1-default-pool-node1
         

In this example output, `asia-southeast1-c` is no longer in use. The frontend service you access from a browser with the URL `http://EXTERNAL_IP` is still accessible. A user would still be able to do deposit and payment actions, even though one of the zones is no longer available.




### Use a single-zone node pool

In this section, you simulate a zone failure by deleting two of the node pools. This approach verifies that your application can respond to the loss of a node pool by correctly redistributing Pods and traffic across a node pool in another zone. To simulate a zone outage on a regional cluster, you expand the basic cluster previously created, running the Cymbal Bank application across multiple node pools. This method of simulating the zone interruption more closely reflects an actual zone failure than the first example of updating active zones in a node pool, as it's more common for multiple node pools to exist in a cluster:

![A load balancer directs traffic to a regional cluster that runs across three node pools. The default node pool runs across all zones, and the other two node pools each run in a single zone.](https://docs.cloud.google.com/static/kubernetes-engine/images/single-zone-node-pool.svg)

The cluster that you build in this section to simulate a single-zone node pool failure includes the following components:

  * Default node pool — usually created when you create a regional GKE Standard cluster — that's a multi-zonal node pool (`default-pool`).

This cluster with the single `default-pool` is what you created earlier in this document.

  * Additional node pools (`zonal-node-pool-1` and `zonal-node-pool-2`) that also run services for the example Cymbal Bank application.




The dotted lines in the diagram show how traffic only serves `zonal-node-pool-2` after you simulate a failure in `default-pool` and `zonal-node-pool-1`.

To create additional node pools and simulate failure, complete the following steps:

  1. Check availability of the regional cluster:
         
         gcloud container node-pools list \
             --cluster=CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION
         
         kubectl get node -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The result is similar to the following example output:
         
         NAME: default-pool
         MACHINE_TYPE: e2-medium
         DISK_SIZE_GB: 100
         NODE_VERSION: 1.27.8-gke.1067004
         
         NAME                                         ZONE.               INT_IP
         regional-cluster-1-default-pool-node5-pzmc   asia-southeast1-c   10.148.0.6
         regional-cluster-1-default-pool-node6-qf1l   asia-southeast1-c   10.148.0.7
         regional-cluster-1-default-pool-node2-dlk2   asia-southeast1-a   10.148.0.8
         regional-cluster-1-default-pool-node1-pkfd   asia-southeast1-a   10.148.0.9
         regional-cluster-1-default-pool-node3-6b6n   asia-southeast1-b   10.148.0.5
         regional-cluster-1-default-pool-node4-h0lc   asia-southeast1-b   10.148.0.4
         

In this example output, all Cymbal Bank Pods are deployed in all zones under the same cluster and run in the existing `default-pool`.

  2. Create two new single-zone node pools:
         
         gcloud beta container node-pools create zonal-node-pool-1 \
           --cluster CLUSTER_NAME \
           --location CONTROL_PLANE_LOCATION \
           --num-nodes 4 \
           --node-locations ZONE_A
         
         gcloud beta container node-pools create zonal-node-pool-2 \
             --cluster CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION \
             --num-nodes 4 \
             --node-locations ZONE_B
         

Replace `ZONE_A` and `ZONE_B` with the two zones where you want the new single-zone node pools to run.

  3. To simulate a zone failure, delete the `default-pool` regional node pool and one of the new single-zone node pools:
         
         gcloud container node-pools delete default-pool \
             --cluster=CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         
         gcloud container node-pools delete zonal-node-pool-1 \
             --cluster=CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

During the `node-pool` deletion process, workloads are shut down and rescheduled to another available node pool. When this process happens, the Services and Deployments aren't available. This behavior means that downtime windows need to be specified for DR reporting or documentation.

Verify the continued availability of the microservices:
         
         kubectl get pods -o wide ; kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The output should look similar like the following example:
         
         NAME                                  ZONE                INT_IP
         regional-cluster-1-node-pool3-node1   asia-southeast1-b   10.148.0.8
         regional-cluster-1-node-pool3-node2   asia-southeast1-b   10.148.0.9
         regional-cluster-1-node-pool3-node3   asia-southeast1-b   10.148.0.5
         regional-cluster-1-node-pool3-node4   asia-southeast1-b   10.148.0.4
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP          NODE
         accounts-db-0                         1/1     Running   0          28m     10.28.1.5   regional-cluster-1-zonal-node-pool-2-node3
         balancereader-7dc7d9ff57-shwg5        1/1     Running   0          28m     10.28.5.6   regional-cluster-1-zonal-node-pool-2-node1
         contacts-7ddc76d94-qv4x5              1/1     Running   0          28m     10.28.4.6   regional-cluster-1-zonal-node-pool-2-node2
         frontend-747b84bff4-mdnkd             1/1     Running   0          9m21s   10.28.1.7   regional-cluster-1-zonal-node-pool-2-node3
         ledger-db-0                           1/1     Running   0          28m     10.28.5.7   regional-cluster-1-zonal-node-pool-2-node4
         ledgerwriter-f6cc7889d-mttmb          1/1     Running   0          28m     10.28.1.6   regional-cluster-1-zonal-node-pool-2-node3
         loadgenerator-57d4cb57cc-7fvrc        1/1     Running   0          28m     10.28.4.7   regional-cluster-1-zonal-node-pool-2-node2
         transactionhistory-5dd7c7fd77-w2vqs   1/1     Running   0          9m20s   10.28.4.8   regional-cluster-1-zonal-node-pool-2-node2
         userservice-cd5ddb4bb-zfr2g           1/1     Running   0          28m     10.28.5.8   regional-cluster-1-zonal-node-pool-2-node1
         

In this example output, as the `default-pool` and the `zonal-node-pool-1` no longer exist, all Services run in `zonal-node-pool-2`.




### Cordon and drain nodes in a zone

In this section, you cordon and drain specific nodes in your cluster. You cordon and drain all the nodes in a single zone, which simulates the loss of the Pods that run on those nodes across the zone:

![A load balancer directs traffic to a regional cluster that runs across three zones. Each zone contains two nodes, and the Cymbal Bank sample application Pods run across all zones and nodes.](https://docs.cloud.google.com/static/kubernetes-engine/images/cordon-and-drain.svg)

In this diagram, you cordon and drain the nodes in the first zone. The nodes in the other two zones continue to run. This approach verifies that your application can respond to the loss of all of the nodes in a zone by correctly redistributing Pods and traffic across nodes that run in other zones.

To cordon and drain the nodes in one of the zones, simulating failure, complete the following steps:

  1. Check availability of the regional cluster and Services. Look at the node names of the target failure zone. You want to specify a zone where the frontend Pods run:
         
         kubectl get pods -o wide
         

The output should look like the following example:
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP           NODE
         accounts-db-0                         1/1     Running   0          4m7s    10.96.4.4    regional-cluster-1-default-pool-node2
         balancereader-7dc7d9ff57-lv4z7        1/1     Running   0          4m7s    10.96.1.5    regional-cluster-1-default-pool-node1
         contacts-7ddc76d94-wxvg5              1/1     Running   0          4m7s    10.96.6.11   regional-cluster-1-default-pool-node3
         frontend-747b84bff4-gvktl             1/1     Running   0          4m7s    10.96.1.4    regional-cluster-1-default-pool-node1
         ledger-db-0                           1/1     Running   0          4m7s    10.96.4.5    regional-cluster-1-default-pool-node2
         ledger-db-1                           1/1     Running   0          3m50s   10.96.0.13   regional-cluster-1-default-pool-node5
         ledgerwriter-f6cc7889d-4hqbm          1/1     Running   0          4m6s    10.96.0.12   regional-cluster-1-default-pool-node5
         loadgenerator-57d4cb57cc-fmq52        1/1     Running   0          4m6s    10.96.4.6    regional-cluster-1-default-pool-node2
         transactionhistory-5dd7c7fd77-72zpx   1/1     Running   0          4m6s    10.96.6.12   regional-cluster-1-default-pool-node3
         userservice-cd5ddb4bb-b7862           1/1     Running   0          4m6s    10.96.1.6    regional-cluster-1-default-pool-node1
         

  2. Associate the Pods listed in the previous output with the node's zone:
         
         kubectl get node -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The output should look like the following example:
         
         NAME                                    ZONE                INT_IP
         regional-cluster-1-default-pool-node1   asia-southeast1-b   10.148.0.41
         regional-cluster-1-default-pool-node2   asia-southeast1-b   10.148.0.42
         regional-cluster-1-default-pool-node3   asia-southeast1-a   10.148.0.37
         regional-cluster-1-default-pool-node4   asia-southeast1-a   10.148.0.38
         regional-cluster-1-default-pool-node5   asia-southeast1-c   10.148.0.40
         regional-cluster-1-default-pool-node6   asia-southeast1-c   10.148.0.39
         

In the previous example output, the frontend Pods are located in `regional-cluster-1-default-pool-node1` in zone `asia-southeast1-b`.

In the next step, you trace all nodes in zone `asia-southeast1-b`, which in this example output are `regional-cluster-1-default-pool-node1` and `regional-cluster-1-default-pool-node2`

  3. Cordon and drain target nodes in one of the zones. In this example, that's the two nodes in `asia-southeast1-b`:
         
         kubectl drain regional-cluster-1-default-pool-node1 \
             --delete-emptydir-data --ignore-daemonsets
         
         kubectl drain regional-cluster-1-default-pool-node2 \
             --delete-emptydir-data --ignore-daemonsets
         

This command marks the nodes as unschedulable, and simulates node failures. Kubernetes reschedules Pods to other nodes in functioning zones.

  4. Look at where the new frontend Pods and other example Cymbal Bank Pods that were previously running on the node in the failure zone are now rescheduled:
         
         kubectl get pods -o wide ; kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The output should look like the following example:
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP           NODE
         accounts-db-0                         1/1     Running   0          4m7s    10.96.4.4    regional-cluster-1-default-pool-node4
         balancereader-7dc7d9ff57-lv4z7        1/1     Running   0          4m7s    10.96.1.5    regional-cluster-1-default-pool-node6
         contacts-7ddc76d94-wxvg5              1/1     Running   0          4m7s    10.96.6.11   regional-cluster-1-default-pool-node3
         frontend-747b84bff4-gvktl             1/1     Running   0          4m7s    10.96.1.4    regional-cluster-1-default-pool-node3
         ledger-db-0                           1/1     Running   0          4m7s    10.96.4.5    regional-cluster-1-default-pool-node6
         ledger-db-1                           1/1     Running   0          3m50s   10.96.0.13   regional-cluster-1-default-pool-node5
         ledgerwriter-f6cc7889d-4hqbm          1/1     Running   0          4m6s    10.96.0.12   regional-cluster-1-default-pool-node5
         loadgenerator-57d4cb57cc-fmq52        1/1     Running   0          4m6s    10.96.4.6    regional-cluster-1-default-pool-node4
         transactionhistory-5dd7c7fd77-72zpx   1/1     Running   0          4m6s    10.96.6.12   regional-cluster-1-default-pool-node3
         userservice-cd5ddb4bb-b7862           1/1     Running   0          4m6s    10.96.1.6    regional-cluster-1-default-pool-node3
         
         NAME                                    ZONE                INT_IP
         regional-cluster-1-default-pool-node3   asia-southeast1-a   10.148.0.37
         regional-cluster-1-default-pool-node4   asia-southeast1-a   10.148.0.38
         regional-cluster-1-default-pool-node5   asia-southeast1-c   10.148.0.40
         regional-cluster-1-default-pool-node6   asia-southeast1-c   10.148.0.39
         

In this example output, there are no example Cymbal Bank Pods that run on cordoned nodes, and all Pods only now run in the other two zones.

Pod Disruption Budgets (PDBs) on the nodes might block node draining. Assess PDB policies before the cordon and drain action. To understand more about PDB and its relation with managing disruption, see how to ensure reliability and uptime for your GKE cluster.

**Note:** After you have simulated the failure, you can use `kubectl uncordon` to allow Pods to be scheduled on the nodes again.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial:

### Delete the project

The easiest way to eliminate billing is to delete the project you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [simulate a zone outage for a regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage).
  * Learn about [disaster recovery on Google Cloud](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook).
  * Pod Disruption Budget [considerations](https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster).
  * Learn about [zonal versus regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk).
  * Learn how to [run high availability databases in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).
  * Find out more about [Disaster Recovery best practices on Google Cloud](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * Learn about [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
