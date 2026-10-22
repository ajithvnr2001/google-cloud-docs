---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-load-balancer-k8s/
title: Configure a load balancer for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:06.163889+00:00
---

# Configure a load balancer for AlloyDB Omni on Kubernetes  |  AlloyDB Omni for Kubernetes: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-load-balancer-k8s/

This page documents AlloyDB Omni version **17.5.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/overview)



Send feedback 

#  Configure a load balancer for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-load-balancer-k8s)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-load-balancer-k8s)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/configure-load-balancer-k8s)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-load-balancer-k8s)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/configure-load-balancer-k8s)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-load-balancer-k8s)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-load-balancer-k8s)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-load-balancer-k8s)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/configure-load-balancer-k8s)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/configure-load-balancer-k8s)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/configure-load-balancer-k8s)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-load-balancer-k8s)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-load-balancer-k8s)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/configure-load-balancer-k8s)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/configure-load-balancer-k8s)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/configure-load-balancer-k8s)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/configure-load-balancer-k8s)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-load-balancer-k8s)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/configure-load-balancer-k8s)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-load-balancer-k8s)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/configure-load-balancer-k8s)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-load-balancer-k8s)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/configure-load-balancer-k8s)

This page summarizes how to configure a load balancer in AlloyDB Omni using the AlloyDB Omni `spec`. In Google Kubernetes Engine (GKE), a load balancer created by default is of the external type and bound with the external IP address to permit connections from the internet. However, if the `networking.gke.io/load-balancer-type: "internal"` annotation is included in the `metadata.annotations[]` field of the load balancer manifest, then GKE creates an internal load balancer. 

Different platforms provide their own annotations for creating the specific type of a load balancer. AlloyDB Omni lets you specify load balancer annotations using the `spec` section of the database cluster manifest. The database controller adds those annotations to the load balancer `spec` when creating a database cluster.

## Create an internal load balancer using the database spec

You can create an internal load balancer by configuring the `dbLoadBalancerOptions` field in the `spec` section of your `DBCluster` manifest.

###  Kubernetes 

Annotations define the type and properties of a load balancer. An internal load balancer requires the presence of the following annotation:
    
    
    networking.gke.io/load-balancer-type: "internal"
    

To create an internal load balancer that permits connections from outside the GKE cluster within the same project, apply the following manifest:
    
    
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-DB_CLUSTER_NAME
    type: Opaque
    data:
      DB_CLUSTER_NAME: "ENCODED_PASSWORD"
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
      databaseVersion: "15.5.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-DB_CLUSTER_NAME
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        dbLoadBalancerOptions:
          annotations:
            **networking.gke.io/load-balancer-type: "internal"**
      **allowExternalIncomingTraffic: true**
    EOF

Replace the following:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/deploy-kubernetes#create).



In this manifest:

  * **networking.gke.io/load-balancer-type: "internal"** : the GKE internal load balancer annotation to your database cluster
  * **allowExternalIncomingTraffic: true** : the `allowExternalIncomingTraffic` field is set to `true` to allow incoming traffic from outside the Kubernetes cluster



## Get the database cluster and connectivity details

###  Kubernetes 

To verify that the database cluster resource is in the `Ready` status, use the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog -n NAMESPACE -w

The output is similar to the following:
    
    
    NAME               PRIMARYENDPOINT   PRIMARYPHASE   DBCLUSTERPHASE
    DB_CLUSTER_NAME    10.95.0.84        Ready          DBClusterReady
    

Verify that the annotation and IP address of the internal load balancer exist in the load balancer service, as follows:
    
    
    kubectl get svc LOAD_BALANCER_SERVICE_NAME -n NAMESPACE -o yaml

Replace the following:

  * `LOAD_BALANCER_SERVICE_NAME`: the name of your load balancer service that creates a unique IP address accessible by external networks.
  * `NAMESPACE`: the name of the Kubernetes namespace for your load balancer service.



The output is similar to the following:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        cloud.google.com/neg: '{"ingress":true}'
        **networking.gke.io/load-balancer-type: internal**
      creationTimestamp: "2024-02-22T15:26:18Z"
      finalizers:
      − gke.networking.io/l4-ilb-v1
      − service.kubernetes.io/load-balancer-cleanup
      labels:
        alloydbomni.internal.dbadmin.gdc.goog/dbcluster: DB_CLUSTER_NAME
        alloydbomni.internal.dbadmin.gdc.goog/dbcluster-ns: NAMESPACE
        alloydbomni.internal.dbadmin.gdc.goog/instance: ad98-foo
        alloydbomni.internal.dbadmin.gdc.goog/task-type: database
        egress.networking.gke.io/enabled: "true"
      name: LOAD_BALANCER_SERVICE_NAME
      namespace: NAMESPACE
     ownerReferences:
      − apiVersion: alloydbomni.dbadmin.goog/v1
        blockOwnerDeletion: true
        controller: true
        kind: DBCluster
        name: DB_CLUSTER_NAME
        uid: 2dd76c9f-7698-4210-be41-6d2259840a85
      resourceVersion: "33628320"
      uid: 1f45362b-6d6f-484d-ad35-11c14e91933e
    spec:
      allocateLoadBalancerNodePorts: true
      clusterIP: 10.60.4.76
      clusterIPs:
      − 10.60.4.76
      externalTrafficPolicy: Cluster
      internalTrafficPolicy: Cluster
      ipFamilies:
      − IPv4
      ipFamilyPolicy: SingleStack
      loadBalancerSourceRanges:
      − 0.0.0.0/0
      ports:
      − name: db
        nodePort: 31453
        port: 5432
        protocol: TCP
        targetPort: 5432
      selector:
        alloydbomni.internal.dbadmin.gdc.goog/dbcluster: DB_CLUSTER_NAME
        alloydbomni.internal.dbadmin.gdc.goog/dbcluster-ns: NAMESPACE
        alloydbomni.internal.dbadmin.gdc.goog/instance: ad98-foo
        alloydbomni.internal.dbadmin.gdc.goog/task-type: database
        egress.networking.gke.io/enabled: "true"
      sessionAffinity: None
      type: LoadBalancer
    status:
      loadBalancer:
        ingress:
        − **ip: 10.95.0.84**

The output has the following attributes:

  * `networking.gke.io/load-balancer-type: internal`: an internal load balancer must exist in the load balancer service
  * `ip`: the primary endpoint value in the verification output of the database cluster matches to the ingress controller value of the load balancer



## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
