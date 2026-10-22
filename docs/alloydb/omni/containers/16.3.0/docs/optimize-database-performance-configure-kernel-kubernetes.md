---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/optimize-database-performance-configure-kernel-kubernetes/
title: Configure kernel parameters for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:12.113633+00:00
---

# Configure kernel parameters for AlloyDB Omni on Kubernetes  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/optimize-database-performance-configure-kernel-kubernetes/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)



Send feedback 

#  Configure kernel parameters for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/optimize-database-performance-configure-kernel-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/optimize-database-performance-configure-kernel-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/optimize-database-performance-configure-kernel-kubernetes)

This page provides information about setting up Kubernetes nodes that host AlloyDB Omni database clusters for the optimal performance of the AlloyDB Omni Kubernetes operator and the AlloyDB Omni database engine. 

Configuring kernel parameters lets AlloyDB Omni use system memory and IO resources more efficiently when handling heavy workloads.

## Prerequisite

Before you start, make sure your Kubernetes nodes run Linux kernel 6.1 or higher, specifically a kernel that supports the `MADV_COLLAPSE` and `MADV_POPULATE_WRITE` flags. For more information about these flags, see [Linux `madwise` documentation](https://man7.org/linux/man-pages/man2/madvise.2.html).

## Apply recommended kernel settings to Kubernetes nodes

The following table lists required kernel parameters and their corresponding values for Kubernetes nodes that run database cluster pods:

File | Value  
---|---  
`/sys/kernel/mm/transparent_hugepage/shmem_enabled`  
For information about shared memory, see [Transparent Hugepage Support](https://www.kernel.org/doc/Documentation/vm/transhuge.txt) | `within_size` or `always`  
`/proc/sys/vm/max_map_count`  
For information about the number of memory map areas a process can create, see [Documentation for `/proc/sys/vm`](https://docs.kernel.org/admin-guide/sysctl/vm.html#max-map-count) | Greater than or equal to `1073741824`  
  
To configure the kernel parameters on your Kubernetes nodes using a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), do the following:

  1. Apply labels to the nodes where you plan to run database clusters using instructions in [Add a label to a node](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node).

  2. To set the kernel parameters on the nodes labeled `LABEL_KEY=LABEL_VALUE`, create a DaemonSet:
         
         cat << EOF | kubectl apply -f -
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: alloydb-omni-kernel-tuning
           namespace: DS_NAMESPACE
         spec:
           selector:
             matchLabels:
               name: alloydb-omni-kernel-tuning
           template:
             metadata:
               labels:
                 name: alloydb-omni-kernel-tuning
             spec:
               volumes:
                 - name: host-sys
                   hostPath:
                     path: /sys
               nodeSelector:
                 LABEL_KEY: "LABEL_VALUE"
               restartPolicy: Always
               terminationGracePeriodSeconds: 1
               initContainers:
                 - name: enable-thp-mmc
                   image: INIT_IMAGE
                   volumeMounts:
                     - name: host-sys
                       mountPath: /sys
                   securityContext:
                     privileged: true
                   command: ["sh", "-c", "sysctl -w vm.max_map_count=MAX_MAP_COUNT && echo within_size >/sys/kernel/mm/transparent_hugepage/shmem_enabled"]
               containers:
                 - name: CONTAINER_NAME
                   image: CONTAINER_IMAGE
                   command: ["watch", "-n", "600", "cat", "/sys/kernel/mm/transparent_hugepage/shmem_enabled"]
         EOF
         

Replace the following:

     * `DS_NAMESPACE`: the namespace where you want to deploy the DaemonSet—for example, `default`.
     * `LABEL_KEY`: the identifier for the label—for example, `workload`.
     * `LABEL_VALUE`: the data associated with the identifier for the label—for example, `database`.
     * `INIT_IMAGE`: the name of the image used for the init container.
     * `MAX_MAP_COUNT`: the maximum number of memory map areas a process can create—for example, `1073741824`.
     * `CONTAINER_NAME`: the name of the main container—for example, `main`.
     * `CONTAINER_IMAGE`: the name of the image used for the main container—for example, `latest`.
  3. After deploying the DaemonSet, to verify that all pods in your Kubernetes cluster are in the `Running` state and that you have one pod for each node with the label `LABEL_KEY=LABEL_VALUE`, use the following command:
         
         kubectl get pods -l LABEL_KEY=LABEL_VALUE
         

An example output looks as follows:
         
         NAME                               READY   STATUS    RESTARTS   AGE
         alloydb-omni-kernel-tuning-2dkwh   1/1     Running   0          22s
         alloydb-omni-kernel-tuning-pgkbj   1/1     Running   0          19s
         

  4. To verify the kernel flag is successfully applied, for each of the pods identified after deploying the DaemonSet, run the following command:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the pod you want to examine the logs of.

An example output looks as follows:
         
         always [within_size] advise never deny force
         




## Run database clusters on Kubernetes nodes with recommended kernel parameters

To deploy database clusters on Kubernetes nodes with recommended kernel parameters, add a `nodeAffinity` section to one of the following sections of your database cluster manifest:

  * `primarySpec.schedulingConfig` for primary instances
  * `spec.schedulingConfig` for read pool instances


    
    
          nodeaffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: LABEL_KEY
                  operator: In
                  values:
                  - "LABEL_VALUE"
    

For more information about running database clusters on specific Kubernetes nodes, see [Assign nodes to a database cluster using scheduling](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/assign-nodes-cluster-scheduling).

### Verify the application of kernel parameters

To verify kernel parameters are applied to database pods, do the following:

  1. If high availability is enabled, specifically `spec.availability.numberOfStandbys` is set to a value greater than zero, verify that the database custom resource shows `DBClusterReady` in the **DBCLUSTERPHASE** column and `True` in the **HAREADYSTATUS** column.
         
         kubectl get dbcluster -n DBCLUSTER_NAMESPACE DBCLUSTER_NAME
         

Replace the following:

     * `DBCLUSTER_NAME`: the name of the database cluster you verify.
     * `DBCLUSTER_NAMESPACE`: the name of the specific namespace where your database cluster resides.

An example output looks as follows:
    
    NAME               PRIMARYENDPOINT   PRIMARYPHASE   DBCLUSTERPHASE   HAREADYSTATUS   HAREADYREASON
    dbcluster-sample   10.29.21.240      Ready          DBClusterReady   True            Ready
    

  2. List Kubernetes pods that belong to the database cluster:
         
         kubectl get pods -n DBCLUSTER_NAMESPACE -l alloydbomni.internal.dbadmin.goog/dbcluster=DBCLUSTER_NAME
         

  3. To check shared memory information, run the following command:
         
         kubectl exec -n DBCLUSTER_NAMESPACE POD_NAME -- grep Shmem /proc/meminfo
         

  4. The output must contain numbers other than zero in all of the entries.

An example output looks as follows:
         
         Shmem:          126255872 kB
         ShmemHugePages: 18403328 kB
         ShmemPmdMapped:  2961408 kB
         

If you see `0 kB` shows in any of the entries, restart the corresponding pod:
         
         kubectl delete pod -n DBCLUSTER_NAMESPACE POD_NAME
         

  5. Repeat steps 1 through 5 after the pod is in the `Running` state.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
