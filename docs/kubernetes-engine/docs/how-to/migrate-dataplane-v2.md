---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-dataplane-v2/
title: Migrate VPC-native clusters to GKE Dataplane V2 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:19.209430+00:00
---

# Migrate VPC-native clusters to GKE Dataplane V2  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-dataplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Migrate VPC-native clusters to GKE Dataplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use this document to migrate your existing Google Kubernetes Engine (GKE) VPC-native clusters from Dataplane V1 to GKE Dataplane V2, monitor the migration, and roll it back if you need to.

This document is for Platform admins and operators and Networking specialists who manage network configurations for their GKE clusters.

Before you start, learn what happens during each migration phase and how to plan for workload disruption in [About migrating to GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-migrating-dataplane-v2).

## Before you begin

Before initiating the migration, verify that your cluster meets the eligibility requirements and consider the impact on your workloads.

Verify that your cluster meets these requirements:

  * The cluster is a VPC-native cluster.
  * The cluster is running version 1.35.3-gke.1155000 or later.
  * The node pools are running version 1.35.1-gke.1516000 or later.
  * If you use Cloud Service Mesh or open source Istio, your Istio version is 1.23 or later.



### Prepare your cluster

Complete the following tasks before you start the migration:

  * **NetworkPolicy removal** : remove your existing network policies. If GKE suddenly enforces network policies when it recreates your nodes, you might experience unintended network disruption.
  * **Calico network policies** : if you use a GKE Standard cluster with network policy (Calico) enabled, [disable network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#disable-network-policy-enforcement). You can't migrate these clusters directly.
  * **Active Assist recommendations** : check [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) or the cluster details page for recommendations that might conflict with the migration.
  * **IP address capacity** : verify that your cluster's Pod IP address range has enough capacity for your node pool upgrade strategies. For more information, see [GKE IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization). 
    * **Networking features** : enable networking features such as NodeLocal DNSCache or intranode visibility before you start the migration or after the migration is complete. You can't enable them during the migration.



### Understand the limitations

  * **Locked networking configurations** : after you start the migration, you can't change cluster-wide networking configurations until the migration is complete.
  * **Maintenance windows** : the migration follows your maintenance windows and maintenance exclusions, so it might appear to stall. To speed it up, you can patch node pools manually. For steps, see Expedite the migration.
  * **Optional GKE Dataplane V2 features** : configure optional GKE Dataplane V2 features, such as GKE Dataplane V2 observability or multi-network support for Pods, after the migration is complete.
  * **Terraform** : You can't use Terraform to migrate to GKE Dataplane V2.

**Caution:** The migration ignores your cluster disruption budget. Plan your migration accordingly. 

## Initiate the migration

To manually start the migration and bypass automated diagnostic checks, you can patch the cluster by using the Google Cloud CLI.

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --enable-dataplane-v2
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the compute location of the cluster.



## Observe the migration progress

You can monitor the migration status by checking the `datapathProvider` field. During the transition, this field shows `MIGRATE_TO_ADVANCED_DATAPATH`.

  1. Check the cluster status:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format='value(networkConfig.datapathProvider)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.
  2. Check the node pool status:
         
         gcloud container node-pools list \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --format='value(name, networkConfig.datapathProvider)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.
**Note:** If you use Autopilot or Standard with Autopilot ComputeClasses, you can't list `gk3-` node pools. 
  3. Check the `anetd` DaemonSet to verify that the agents are running:
         
         kubectl get ds -n kube-system anetd
         




## Expedite the migration

To bypass the automated rollout schedule, optionally patch node pools manually.

**Warning:** Only execute concurrent node pool patches after one or more node pools have been patched sequentially to verify that workloads are operating correctly. 

To manually patch a node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --datapath-provider=advanced-datapath
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the compute location of the cluster.

**Note:** If you use Autopilot or Standard with Autopilot ComputeClasses, you can't patch `gk3-` node pools. The control plane automatically manages these upgrades. 

## Finalize the migration

After all node pools have been migrated to GKE Dataplane V2, GKE automatically finalizes the migration. When the migration is complete, the command output shows a status of `ADVANCED_DATAPATH` and the cluster is running GKE Dataplane V2.

Observe the completion by checking the cluster status:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --format='value(networkConfig.datapathProvider)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the compute location of the cluster.



When the migration is complete, the output shows `ADVANCED_DATAPATH`.

## Roll back a migration

You can revert the migration to Dataplane V1 at any point before the finalization phase is complete. Reversing the migration is a symmetrical process to the forward migration: after you initiate the rollback, GKE automatically patches the node pools back to the legacy datapath, and then finalizes the cluster.

  1. **Observe`anetd` health**: before rolling back the migration, check if the agents are running to determine if the failure can be mitigated.
         
         kubectl get ds -n kube-system anetd
         

  2. **Cancel ongoing node pool operations** :

     1. Identify and cancel any running node pool operations that would block the cluster patch request.
            
            gcloud container operations list \
                --location=LOCATION \
                --filter="operationType=UPGRADE_NODES AND status=RUNNING AND targetLink:*/clusters/CLUSTER_NAME"
            

Replace the following:

        * `LOCATION`: the compute location of the cluster.
        * `CLUSTER_NAME`: the name of the cluster.
     2. Cancel the operation by using the operation ID:
            
            gcloud container operations cancel OPERATION_ID \
                --location=LOCATION
            

Replace the following:

        * `OPERATION_ID`: the ID of the running operation.
        * `LOCATION`: the compute location of the cluster.
  3. **Initiate the rollback** : issue a cluster patch request to revert the migration to Dataplane V1.
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --no-enable-dataplane-v2
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.
  4. **Observe the node pool rollout** : check the node pool status to verify the migration to the legacy datapath.
         
         gcloud container node-pools list \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --format='value(name, networkConfig.datapathProvider)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.

During the rollback, the command output shows a status of `LEGACY_DATAPATH` for patched node pools.

**Note:** If you use Autopilot or Standard with Autopilot ComputeClasses, you can't list `gk3-` node pools. 
  5. **Observe finalization** : after all node pools have been migrated to Dataplane V1, GKE automatically finalizes the migration. Observe the completion by checking the cluster status:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format='value(networkConfig.datapathProvider)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.

When the rollback is complete, the command output shows a status of `LEGACY_DATAPATH`.




## Troubleshoot the migration

This section provides information to help you troubleshoot and resolve common issues that you might encounter when migrating to GKE Dataplane V2.

### Node pool migration fails

When migrating node pools, GKE uses the configured surge upgrades or blue-green upgrades strategy to create new nodes before deleting the old ones. If your Google Cloud zone doesn't have enough resources to provision the new nodes, the migration fails with a `GCE_STOCKOUT` or `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error. GKE automatically re-attempts to migrate these node pools. If you patch the node pools manually, wait and try the migration again later when resources become available.

## What's next

  * To learn more about GKE Dataplane V2 observability, see [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
