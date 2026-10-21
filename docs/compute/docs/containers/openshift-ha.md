---
url: https://docs.cloud.google.com/compute/docs/containers/openshift-ha/
title: Best practices for high availability \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:25:37.628432+00:00
---

# Best practices for high availability  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/openshift-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Best practices for high availability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices to achieve high availability (HA) with [Red Hat OpenShift Container Platform](https://www.redhat.com/en/technologies/cloud-computing/openshift/container-platform) workloads on Compute Engine. This document focuses on application-level strategies to help you ensure that your workloads remain highly available when failures occur. These strategies help you eliminate single points of failure and implement mechanisms for automatic failover and recovery. 

This document is intended for platform and application architects and assumes that you have some experience in deploying OpenShift. For more information about how to deploy OpenShift, see the [Red Hat documentation](https://www.redhat.com/en/technologies/cloud-computing/openshift/deploy-red-hat-openshift).

This document is part of a series that focuses on the application-level strategies that ensure your workloads remain highly available and quickly recoverable in the face of failures. The documents in this series are as follows:

  * [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr)
  * Best practices for high availability (this page)
  * [Disaster recovery strategies for active-passive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups)
  * [Disaster recovery strategies for active-inactive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups)



## Spread deployments across multiple zones

We recommend that you deploy OpenShift across multiple zones within a Google Cloud region. This approach helps ensure that if a zone experiences an outage, the cluster's control plane nodes continue to function in the other zones the deployment is spread across. To deploy OpenShift across multiple zones, specify a list of Google Cloud zones from the same region in your [`install-config.yaml` file](https://docs.openshift.com/container-platform/4.17/installing/installing_gcp/installing-gcp-customizations.html#installation-gcp-config-yaml_installing-gcp-customizations).

For fine-grained control over the locations where nodes are deployed, we recommend defining VM placement policies which ensure that the VMs are spread across [different failure domains](https://docs.openshift.com/container-platform/4.17/machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.html#cpmso-yaml-failure-domain-gcp_cpmso-config-options-gcp) in the same zone. Applying a [spread placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-placement-policies) to your cluster nodes helps reduce the number of nodes that are simultaneously impacted by location-specific disruptions. For more information on how to create a spread policy for existing clusters, see [Create and apply spread placement policies to VMs](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies#apply-to-vm).

Similarly, to prevent multiple pods from being scheduled on the same node, we recommend that you use [pod anti-affinity rules](https://docs.openshift.com/container-platform/3.11/admin_guide/scheduling/pod_affinity.html#admin-guide-sched-affinity-config-pod-pref). These rules spread application replicas across multiple zones. The following example demonstrates how to implement pod anti-affinity rules:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      namespace: my-app-namespace
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          # Pod Anti-Affinity: Prefer to schedule new pods on nodes in different zones.
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchLabels:
                    app: my-app
                topologyKey: topology.kubernetes.io/zone
          containers:
          - name: my-app-container
            image: quay.io/myorg/my-app:latest
            ports:
            - containerPort: 8080
    

For stateless services like web front ends or REST APIs, we recommend that you [run multiple pod replicas](https://docs.openshift.com/container-platform/4.17/applications/deployments/what-deployments-are.html#deployments-kube-deployments_what-deployments-are) for each service or route. This approach ensures that traffic is automatically routed to pods in available zones.

## Proactively manage load to prevent resource over-commitment

We recommend that you proactively manage your application's load to prevent resource over-commitment. Over-commitment can lead to poor service performance under load. You can help prevent over-commitment by setting resource request limits. For a more detailed explanation, see [managing resources for your pod](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/). Additionally, you can automatically scale replicas up or down based on CPU, memory, or custom metrics, using the [horizontal pod autoscaler](https://docs.openshift.com/container-platform/4.9/nodes/pods/nodes-pods-autoscaling.html).

We also recommend that you use the following load balancing services:

  * **OpenShift ingress operator**. Ingress operator deploys HAProxy-based ingress controllers to handle routing to your pods. Specifically, we recommend that you [configure global access for Ingress controller](https://docs.openshift.com/container-platform/4.17/networking/networking_operators/ingress-operator.html#nw-ingress-controller-configuration-gcp-global-access_configuring-ingress), which enables clients in any region within the same VPC network and region as the load balancer, to reach the workloads running on your cluster. Additionally, we recommend that you [implement ingress controller health checks](https://docs.openshift.com/container-platform/4.17/networking/networking_operators/ingress-operator.html#nw-ingress-controller-config-tuningoptions-healthcheckinterval_configuring-ingress) to monitor the health of your pods and restart failing pods.
  * **Google Cloud Load Balancing**. Load Balancing distributes traffic across Google Cloud zones. [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) that meets your application's needs.



## Define pod disruption budgets

We recommend that you define disruption budgets to specify the minimum number of pods that your application requires to be available during disruptions like maintenance events or updates. The following example shows how to define a disruption budget:
    
    
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: my-app-pdb
      namespace: my-app-namespace
    spec:
      # Define how many pods need to remain available during a disruption.
      # At least one of "minAvailable" or "maxUnavailable" must be specified.
      minAvailable: 2
      selector:
        matchLabels:
          app: my-app
    

For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

## Use storage that supports HA and data replication

For stateful workloads that require persistent data storage outside of containers, we recommend the following best practices.

### Disk best practices

If you require disk storage use one of the following:

  * **Block storage:** [Compute Engine regional Persistent Disk with synchronous replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk)
  * **Shared file storage:** [Filestore](https://docs.cloud.google.com/filestore/docs/create-instance-gcloud) with [snapshots and backups enabled](https://docs.cloud.google.com/filestore/docs/compare-snapshots-and-backups)



After you select a storage option, install its driver in your cluster:

  * [Persistent Disk CSI driver](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/using-container-storage-interface-csi#persistent-storage-csi-gcp-pd)
  * [Filestore CSI Driver](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/using-container-storage-interface-csi#installing-the-gcp-filestore-csi-driver-operator)



The CSI Persistent Disk operator provides a storage class that you can use to create Persistent volume claims (PVC). For Filestore, you must [create the Filestore storage class](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/using-container-storage-interface-csi#persistent-storage-csi-google-cloud-file-create-sc_persistent-storage-csi-google-cloud-file).

### Database best practices

If you require a database use one of the following:

  * **Fully-managed database** : We recommend that you use [Cloud SQL](https://docs.cloud.google.com/sql/docs) or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs) to manage database HA on your behalf. If you use Cloud SQL, you can use the [Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator) to simplify connection management between your application and the database.
  * **Self-managed database** : We recommend that you use a database that supports HA and that you deploy its operator to enable HA. For more information, see the documentation related to your database operator, such as [AlloyDB Omni for Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes), [Redis Enterprise for Kubernetes](https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator), [MariaDB Operator](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/HA.md), or [CloudNative PostgreSQL Operator](https://github.com/cloudnative-pg/cloudnative-pg/blob/main/docs/src/quickstart.md).



After you install your database operator, configure a cluster with multiple instances. The following example shows the configuration for a cluster with the following attributes:

  * A PostgreSQL cluster named `my-postgres-cluster` is created with three instances for high availability.
  * The cluster uses the `regionalpd-balanced` storage class for durable and replicated storage across zones.
  * A database named `mydatabase` is initialized with a user `myuser`, whose credentials are stored in a Kubernetes secret called `my-database-secret`.
  * Superuser access is disabled for enhanced security.
  * Monitoring is enabled for the cluster.


    
    
    apiVersion: postgresql.cnpg.io/v1
    kind: Cluster
    metadata:
      name: my-postgres-cluster
      namespace: postgres-namespace
    spec:
      instances: 3
      storage:
        size: 10Gi
        storageClass: regionalpd-balanced
      bootstrap:
        initdb:
          database: mydatabase
          owner: myuser
          secret:
            name: my-database-secret
      enableSuperuserAccess: false
      monitoring:
        enabled: true
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: my-database-secret
      namespace: postgres-namespace
    type: Opaque
    data:
      username: bXl1c2Vy # Base64-encoded value of "myuser"
      password: c2VjdXJlcGFzc3dvcmQ= # Base64-encoded value of "securepassword"
    

## Externalize application state

We recommend that you move session state or caching to shared in-memory stores (for example, Redis) or persistent datastores (for example, Postgres, MySQL) that are configured to run in HA mode.

## Summary of best practices

In summary, implement the following best practices to achieve high availability with OpenShift:

  * Spread deployments across multiple zones
  * Proactively manage load to prevent resource over-commitment
  * Define pod disruption budgets
  * Use HA data replication features
  * Externalize application state



## What's next

  * Learn how to [install OpenShift on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_google_cloud/index).
  * Learn more about [Red Hat solutions on Google Cloud](https://cloud.google.com/solutions/redhat).
  * Learn about the different [architectural options for DR with OpenShift on Google Cloud](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
