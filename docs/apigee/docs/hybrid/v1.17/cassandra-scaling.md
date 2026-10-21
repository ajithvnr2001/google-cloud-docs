---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-scaling/
title: Scaling Cassandra \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:36:46.003892+00:00
---

# Scaling Cassandra  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-scaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Scaling Cassandra Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-scaling.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-scaling.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-scaling.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-scaling.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-scaling.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-scaling.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-scaling.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-scaling.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-scaling.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-scaling.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-scaling.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-scaling.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-scaling.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-scaling.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-scaling.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-scaling.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-scaling.html)



This topic discusses how to scale up Cassandra horizontally and vertically, and how to scale down Cassandra. 

##  Scaling Cassandra horizontally 

To scale up Cassandra horizontally

  1. Make sure that your `apigee-data` node pool has additional capacity, as needed, before scaling Cassandra. See also [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-dedicated-nodes).
  2. Set the value of the `cassandra.replicaCount` configuration property in your overrides file. The value of `replicaCount` must be a multiple of `3`. To determine your desired `replicaCount` value, consider the following: 
     * Estimate the traffic demands for your proxies.
     * Load test and make reasonable predictions of your CPU utilization.
     * You can specify different `replicaCount` values in different regions.
     * You can expand the `replicaCount` in the future in your overrides file.

For information about this property, see the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#cassandra). See also [Manage runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/customize-services).

**Note:** The default replication factor for all keyspaces is three. As a result, we recommend scaling the replicas by a factor of three.
  3. Apply the changes. For example: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "datastore" has no deployed releases`, replace `upgrade` with `install` and try the command again.



##  Scaling Cassandra vertically 

This section explains how to scale the Cassandra pods vertically to accommodate higher CPU and memory requirements. 

###  Overview 

For an Apigee hybrid production deployment, we recommend that you create at least two separate node pools: one for stateful services (Cassandra) and one for stateless (runtime) services. For example, see [GKE production cluster requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/gke-cluster-setup).

For the stateful Cassandra node pool, we recommend starting with 8 CPU cores and 30 GB of memory. Once the node pool is provisioned, these settings cannot be changed. See also [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-production).

If you need to scale up the Cassandra pods to accommodate higher CPU and memory requirements, follow the steps described in this topic. 

###  Scaling up the Cassandra pods 

Follow these steps to increase the CPU and memory for the stateful node pool used for Cassandra: 

  1. Follow your Kubernetes platform's instructions to add a new node pool to the cluster. Supported platforms are listed in the [installation instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-before-begin).
  2. Verify that the new node pool is ready: 
         
         kubectl get nodes -l NODE_POOL_LABEL_NAME=NODE_POOL_LABEL_VALUE

Example command:
         
         kubectl get nodes -l cloud.google.com/gke-nodepool=apigee-data-new

Example output: 
         
         NAME                                                STATUS   ROLES    AGE     VERSION
         gke-apigee-data-new-441387c2-2h5n   Ready    <none>   4m28s   v1.14.10-gke.17
         gke-apigee-data-new-441387c2-6941   Ready    <none>   4m28s   v1.14.10-gke.17
         gke-apigee-data-new-441387c2-nhgc   Ready    <none>   4m29s   v1.14.10-gke.17

  3. Update your overrides file to use the new node pool for Cassandra and update the pod resources to the increased CPU count and memory size that you wish to use. For example, for a GKE cluster, use a configuration similar to the following. If you are on another Kubernetes platform, you need to adjust the `apigeeData.key` value accordingly: 
         
         nodeSelector:
           requiredForScheduling: true
           apigeeData:
             key: "NODE_POOL_LABEL_NAME"
             value: "NODE_POOL_LABEL_VALUE"
         
         cassandra:
           resources:
             requests:
               cpu: NODE_POOL_CPU_NUMBER
               memory: NODE_POOL_MEMORY_SIZE

For example: 
         
         nodeSelector:
           requiredForScheduling: true
           apigeeData:
             key: "cloud.google.com/gke-nodepool"
             value: "apigee-data-new"
         
         cassandra:
           resources:
             requests:
               cpu: 14
               memory: 16Gi

  4. Apply the overrides file to the cluster: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         




When you complete these steps, the Cassandra pods will begin rolling over to the new node pool. 

##  Scaling down Cassandra 

**CAUTION:** Scaling down cassandra clusters is more invasive than scaling up. Please proceed with caution when scaling down 

Apigee hybrid employs a ring of Cassandra nodes as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Cassandra provides persistent storage for certain Apigee entities on the runtime plane. For more information about Cassandra, see [About the runtime plane](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid#about-the-runtime-plane). 

Cassandra is a resource intensive service and should not be deployed on a pod with any other hybrid services. Depending on the load, you might want to scale the number of Cassandra nodes in the ring down in your cluster.

The general process for scaling down a Cassandra ring is:

  1. Make sure the Cassandra cluster is healthy and has enough storage to support scaling down.
  2. Update the `cassandra.replicaCount` property in `overrides.yaml`.
  3. Apply the configuration update.
  4. Delete the persistent volume claim or volume, depending on your cluster configuration.



###  What you need to know 

  * If any node other than the nodes to be decommissioned is unhealthy, do not proceed. Kubernetes will not be able to downscale the pods from the cluster.
  * Always scale down or up by a factor of three nodes. 



### Downscale Cassandra

  1. Validate that the cluster is healthy and all the nodes are up and running, as the following example shows: 
         
         kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra
         
         NAME                 READY   STATUS    RESTARTS   AGE
         apigee-cassandra-default-0   1/1     Running   0          2h
         apigee-cassandra-default-1   1/1     Running   0          2h
         apigee-cassandra-default-2   1/1     Running   0          2h
         apigee-cassandra-default-3   1/1     Running   0          16m
         apigee-cassandra-default-4   1/1     Running   0          14m
         apigee-cassandra-default-5   1/1     Running   0          13m
         apigee-cassandra-default-6   1/1     Running   0          9m
         apigee-cassandra-default-7   1/1     Running   0          9m
         apigee-cassandra-default-8   1/1     Running   0          8m
         
         kubectl -n APIGEE_NAMESPACE exec -it apigee-cassandra-default-0 nodetool status
         
         
         Datacenter: dc-us-east1

==================== Status=Up/Down |/ State=Normal/Leaving/Joining/Moving \-- Address Load Tokens Owns (effective) Host ID Rack UN 10.16.2.6 690.17 KiB 256 48.8% b02089d1-0521-42e1-bbed-900656a58b68 ra-1 UN 10.16.4.6 705.55 KiB 256 51.6% dc6b7faf-6866-4044-9ac9-1269ebd85dab ra-1 to UN 10.16.11.11 674.36 KiB 256 48.3% c7906366-6c98-4ff6-a4fd-17c596c33cf7 ra-1 UN 10.16.1.11 697.03 KiB 256 49.8% ddf221aa-80aa-497d-b73f-67e576ff1a23 ra-1 UN 10.16.5.13 703.64 KiB 256 50.9% 2f01ac42-4b6a-4f9e-a4eb-4734c24def95 ra-1 UN 10.16.8.15 700.42 KiB 256 50.6% a27f93af-f8a0-4c88-839f-2d653596efc2 ra-1 UN 10.16.11.3 697.03 KiB 256 49.8% dad221ff-dad1-de33-2cd3-f1.672367e6f ra-1 UN 10.16.14.16 704.04 KiB 256 50.9% 1feed042-a4b6-24ab-49a1-24d4cef95473 ra-1 UN 10.16.16.1 699.82 KiB 256 50.6% beef93af-fee0-8e9d-8bbf-efc22d653596 ra-1 **CAUTION:** If the cluster is not healthy or at least one node is not up and running, do not proceed with this process.
  2. Determine if the Cassandra cluster has enough storage to support scaling down. After scaling down, the Cassandra nodes should have no more than 75% of their storage full. 

For example, if your cluster has 6 Cassandra nodes and they are all approximately 50% full, downscaling to three nodes would leave all three at 100%, which would not leave any room for continued operation. 

If however, you have 9 Cassandra nodes, all approximately 50% full, downscaling to 6 nodes would leave each remaining node approximately 75% full. You can downscale. 

**Note:** It is common practice to maintain Cassandra nodes in multiples of three.
  3. Update or add the `cassandra.replicaCount` property in your `overrides.yaml` file. For example, if the current node count is 9, change it to 6: 
         
         cassandra:
           replicaCount: 6 # 

  4. Apply the configuration change to your cluster: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

  5. Verify that all of the remaining Cassandra nodes are running: 
         
         kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra
         
         NAME                 READY   STATUS    RESTARTS   AGE
         apigee-cassandra-default-0   1/1     Running   0          3h
         apigee-cassandra-default-1   1/1     Running   0          3h
         apigee-cassandra-default-2   1/1     Running   0          2h
         apigee-cassandra-default-3   1/1     Running   0          25m
         apigee-cassandra-default-4   1/1     Running   0          24m
         apigee-cassandra-default-5   1/1     Running   0          23m
         
         

  6. Verify that the `cassandra.replicaCount` value equals the number of nodes returned by the `nodetool status` command. 

For example, if you scaled Cassandra down to six nodes: 
         
         kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE -- nodetool -u JMX_USER -pw JMX_PASSWORD status
         
         Datacenter: us-east1
         ====================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load         Tokens       Owns (effective)  Host ID                               Rack
         UN  10.16.2.6    1009.17 KiB  256          73.8%             b02089d1-0521-42e1-bbed-900656a58b68  ra-1
         UN  10.16.4.6    1.65.55 KiB  256          75.6%             dc6b7faf-6866-4044-9ac9-1269ebd85dab  ra-1 to
         UN  10.16.11.11  999.36 KiB   256          72.8%             c7906366-6c98-4ff6-a4fd-17c596c33cf7  ra-1
         UN  10.16.1.11   1017.03 KiB  256          74.2%             ddf221aa-80aa-497d-b73f-67e576ff1a23  ra-1
         UN  10.16.5.13   1061.64 KiB  256          75.9%             2f01ac42-4b6a-4f9e-a4eb-4734c24def95  ra-1
         UN  10.16.8.15   1049.42 KiB  256          74.9%             a27f93af-f8a0-4c88-839f-2d653596efc2  ra-1
         
         

  7. After the Cassandra cluster is down-scaled, verify that pvcs (PersistentVolumeClaim) correspond to the remaining Cassandra nodes. 

Get the names of the pvcs: 
         
         kubectl get pvc -n APIGEE_NAMESPACE
         
         
         NAME                                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
         cassandra-data-apigee-cassandra-default-0   Bound    pvc-f9c2a5b9-818c-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   7h
         cassandra-data-apigee-cassandra-default-1   Bound    pvc-2956cb78-818d-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   7h
         cassandra-data-apigee-cassandra-default-2   Bound    pvc-79de5407-8190-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   7h
         cassandra-data-apigee-cassandra-default-3   Bound    pvc-d29ba265-81a2-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   5h
         cassandra-data-apigee-cassandra-default-4   Bound    pvc-0675a0ff-81a3-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   5h
         cassandra-data-apigee-cassandra-default-5   Bound    pvc-354afa95-81a3-11e9-8862-42010a8e014a   100Gi      RWO            apigee-gcepd   5h

In this example you should not see pvcs corresponding with the three down-scaled nodes: 

     * `cassandra-data-apigee-cassandra-8`
     * `cassandra-data-apigee-cassandra-7`
     * `cassandra-data-apigee-cassandra-6`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
