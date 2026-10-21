---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/config-samples/
title: Cluster configuration samples \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:00.980911+00:00
---

# Cluster configuration samples  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/config-samples/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Cluster configuration samples Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/config-samples)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/config-samples)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document provides YAML samples of the most common Google Distributed Cloud cluster configurations. The sample cluster configuration files provide permutations of the following features and capabilities:

  * [Edge profile](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/hardware#resource_requirements_for_standalone_clusters_using_the_edge_profile)
  * [High availability](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#high_availability)
  * [Open ID Connect (OIDC)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/identity-manage#oidc)
  * [Lightweight Directory Access Protocol (LDAP)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/identity-manage#ldap)
  * Load balancer options: 
    * [External, manually configured load balancing](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/manual-lb)
    * [Bundled Layer 2 load balancing](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb)
    * [Bundled Layer 2 load balancing outside the Control Plane](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb#loadbalancernodepoolspec)
    * [Bundled load balancing with Border Gateway Protocol (BGP)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp)
  * [Multiple NodePools](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/add-remove-node-pools)
  * SSH key overrides
  * [Registry mirror](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/registry-mirror)
  * [Behind a proxy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/proxy)
  * [Private package repository](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/package-server)

**Note:** You can manage identity outside of cluster configuration files with the GKE Identity Service. For more information about using GKE Identity Service to set up OIDC or LDAP, see [Introducing Anthos Identity Service](https://docs.cloud.google.com/anthos/identity).

## How to use the samples

This collection of YAML samples is intended primarily as an educational reference that illustrates how various features look when properly configured. If you want to use these samples to create your own clusters, you need to make changes. Many of the values used, such as the values for the `storage` section, are defaults and work for most clusters. However, other values, such as `spec.authentication.oidc.clientID` and `spec.gkeConnect.projectID`, are specific to your project and environment.

Familiarize yourself with the related feature documentation before attempting to use any of the YAML content provided in this document.

## Features in each sample

The following table list basic configuration information for each sample:

Samples  
---  
Standalone clusters  
Basic edge profile | 

  * Single node
  * Edge profile
  * No node pools

  
High-availability edge profile | 

  * High availability with three nodes
  * Edge profile
  * Bundled Layer 2 load balancing
  * No node pools

  
Hybrid clusters  
Basic hybrid cluster | 

  * Non-high availability
  * Bundled Layer 2 load balancing

  
High-availability hybrid cluster | 

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing

  
High-availability hybrid cluster with load balancing outside the Control Plane | 

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing outside the Control Plane

  
Admin clusters  
Basic admin cluster | 

  * Non-high availability
  * Bundled Layer 2 load balancing

  
Admin cluster with manual load balancing | 

  * Non-high availability
  * External, manually configured load balancing

  
High-availability admin cluster | 

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing

  
User clusters  
Basic user cluster | 

  * Non-high availability
  * Bundled Layer 2 load balancing

  
High-availability user cluster with multiple node pools | 

  * SSH key overrides
  * High availability
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing
  * Multiple node pools

  
High-availability user cluster with OIDC | 

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing

  
High-availability user cluster with LDAP and BGP load balancing | 

  * High availability
  * LDAP
  * Bundled load balancing with BGP

  
  
## Standalone clusters

Note the following capabilities of a standalone cluster:

  * It can administer itself
  * It can run workloads
  * It can't create or manage other/user clusters



Standalone clusters are suited for cluster installations that require a small footprint or in situations where you want to run clusters in network-isolated partitions.

For more information about standalone clusters, see [Standalone cluster deployment](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#standalone_cluster_deployment) and [Create standalone clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/standalone-cluster-creation).

### Basic edge profile

Note the following features and options in this standalone cluster configuration:

  * Single node
  * Edge profile
  * No node pools


    
    
    gcrKeyPath: baremetal/gcr.json
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-edge-basic
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: edge-basic
      namespace: cluster-edge-basic
    spec:
      type: standalone**  profile: edge**
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20
      loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71
          ingressVIP: 10.200.0.72
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.72-10.200.0.90
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 110
    

### High-availability edge profile

Note the following features and options in this standalone cluster configuration:

  * High availability with three nodes
  * Edge profile
  * Bundled Layer 2 load balancing
  * No node pools


    
    
    gcrKeyPath: baremetal/gcr.json
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-edge-ha
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: edge-ha
      namespace: cluster-edge-ha
    spec:
      type: standalone**  profile: edge**
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2
          - address: 10.200.0.3
          - address: 10.200.0.4**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71
          ingressVIP: 10.200.0.72
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.72-10.200.0.90**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 110
    

## Hybrid clusters

Note the following capabilities of a hybrid cluster:

  * It can administer itself
  * It can run workloads
  * It can manage other user clusters



Hybrid clusters function like admin clusters that can run user workloads. Just like admin clusters, hybrid clusters can manage other user clusters. For more information about standalone clusters, see [Hybrid cluster deployment](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#hybrid_cluster_deployment) and [Create hybrid clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation).

### Basic hybrid cluster

Note the following features and options in this hybrid cluster configuration:

  * Non-high availability
  * Bundled Layer 2 load balancing


    
    
    gcrKeyPath: baremetal/gcr.json
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-hybrid-basic
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: hybrid-basic
      namespace: cluster-hybrid-basic
    spec:
      type: hybrid
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71
          ingressVIP: 10.200.0.72
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.72-10.200.0.90**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-hybrid-basic
    spec:
      clusterName: hybrid-basic
      nodes:
      - address:  10.200.0.10
      - address:  10.200.0.11
      - address:  10.200.0.12
    

### High-availability hybrid cluster

Note the following features and options in this hybrid cluster configuration:

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing


    
    
    **registryMirrors :
      - endpoint: https://10.194.2.13:5007/v2/test-namespace
        caCertPath: /root/cert.pem
        pullCredentialConfigPath: /root/dockerconfig.json**
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-hybrid-ha
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: hybrid-ha
      namespace: cluster-hybrid-ha
    spec:
      type: hybrid
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2
          - address: 10.200.0.3
          - address: 10.200.0.4**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  proxy:
        url: http://10.194.2.140:3128
        noProxy:
        - 127.0.0.1
        - localhost****  osEnvironmentConfig:
        addPackageRepo: false****  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71
          ingressVIP: 10.200.0.72
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.72-10.200.0.90**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      authentication:**    oidc:
          issuerURL: "https://infra.example.dev/adfs"
          clientID: "be654652-2c45-49ff-9d7c-3663cee9ba51"
          clientSecret: "clientSecret"
          kubectlRedirectURL: "http://localhost:44320/callback"
          username: "unique_name"
          usernamePrefix: "oidc:"
          group: "groups"
          groupPrefix: "oidc:"
          scopes: "allatclaims"
          extraParams: "resource=token-groups-claim"
          deployCloudConsoleProxy: true
          certificateAuthorityData: base64EncodedCACertificate
          proxy: http://10.194.2.140:3128**
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-hybrid-ha
    spec:
      clusterName: hybrid-ha
      nodes:
      - address:  10.200.0.10
      - address:  10.200.0.11
      - address:  10.200.0.12
    

### High-availability hybrid cluster with load balancing outside the Control Plane

Note the following features and options in this hybrid cluster configuration:

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing outside the Control Plane


    
    
    **registryMirrors :
      - endpoint: https://10.194.2.13:5007/v2/test-namespace
        caCertPath: /root/cert.pem
        pullCredentialConfigPath: /root/dockerconfig.json**
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-hybrid-ha-lb
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: hybrid-ha-lb
      namespace: cluster-hybrid-ha-lb
    spec:
      type: hybrid
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2
          - address: 10.200.0.3
          - address: 10.200.0.4**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  proxy:
        url: http://10.194.2.140:3128
        noProxy:
        - 127.0.0.1
        - localhost****  osEnvironmentConfig:
        addPackageRepo: false****  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71
          ingressVIP: 10.200.0.72
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.72-10.200.0.90
        nodePoolSpec:
          nodes:
          - address: 10.200.0.5
          - address: 10.200.0.6
          - address: 10.200.0.7**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      authentication:**    oidc:
          issuerURL: "https://infra.example.dev/adfs"
          clientID: "be654652-2c45-49ff-9d7c-3663cee9ba51"
          clientSecret: "clientSecret"
          kubectlRedirectURL: "http://localhost:44320/callback"
          username: "unique_name"
          usernamePrefix: "oidc:"
          group: "groups"
          groupPrefix: "oidc:"
          scopes: "allatclaims"
          extraParams: "resource=token-groups-claim"
          deployCloudConsoleProxy: true
          certificateAuthorityData: base64EncodedCACertificate
          proxy: http://10.194.2.140:3128**
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-hybrid-ha-lb
    spec:
      clusterName: hybrid-ha-lb
      nodes:
      - address:  10.200.0.10
      - address:  10.200.0.11
      - address:  10.200.0.12
    

## Admin clusters

An admin cluster is used to manage other user clusters. Use admin clusters if you have a fleet of clusters in the same data center that you want to manage from a centralized place, and for larger deployments that need isolation between different teams or between development and production workloads.

For more information about admin clusters, see [Multi-cluster deployment](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#multi-cluster_deployment) and [Create admin clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/admin-cluster-creation).

### Basic admin cluster

Note the following features and options in this admin cluster configuration:

  * Non-high availability
  * Bundled Layer 2 load balancing


    
    
    gcrKeyPath: baremetal/gcr.json
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-basic
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: admin-basic
      namespace: cluster-admin-basic
    spec:
      type: admin
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    

### Admin cluster with manual load balancing

Note the following features and options in this admin cluster configuration:

  * Non-high availability
  * External, manually configured load balancing


    
    
    gcrKeyPath: baremetal/gcr.json
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-manlb
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: admin-manlb
      namespace: cluster-admin-manlb
    spec:
      type: admin
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: manual
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    

### High-availability admin cluster

Note the following features and options in this admin cluster configuration:

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing


    
    
    **registryMirrors :
      - endpoint: https://10.194.2.13:5007/v2/test-namespace
        caCertPath: /root/cert.pem
        pullCredentialConfigPath: /root/dockerconfig.json**
    sshPrivateKeyPath: .ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: baremetal/connect-agent.json
    gkeConnectRegisterServiceAccountKeyPath: baremetal/connect-register.json
    cloudOperationsServiceAccountKeyPath: baremetal/cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-ha
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: admin-ha
      namespace: cluster-admin-ha
    spec:
      type: admin
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.2
          - address: 10.200.0.3
          - address: 10.200.0.4**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  proxy:
        url: http://10.194.2.140:3128
        noProxy:
        - 127.0.0.1
        - localhost****  osEnvironmentConfig:
        addPackageRepo: false****  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.71**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      authentication:**    oidc:
          issuerURL: "https://infra.example.dev/adfs"
          clientID: "be654652-2c45-49ff-9d7c-3663cee9ba51"
          clientSecret: "clientSecret"
          kubectlRedirectURL: "http://localhost:44320/callback"
          username: "unique_name"
          usernamePrefix: "oidc:"
          group: "groups"
          groupPrefix: "oidc:"
          scopes: "allatclaims"
          extraParams: "resource=token-groups-claim"
          deployCloudConsoleProxy: true
          certificateAuthorityData: base64EncodedCACertificate
          proxy: http://10.194.2.140:3128**
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    

## User clusters

A user cluster runs your containerized workloads. User clusters must contain one or more worker nodes that run user workloads. Use user clusters if you have a fleet of clusters in the same data center that you want to manage from a centralized place. User clusters are also recommended for larger deployments that need isolation between different teams or between development and production workloads.

For more information about admin clusters, see [Multi-cluster deployment](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#multi-cluster_deployment) and [Create user clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/user-cluster-creation).

### Basic user cluster

Note the following features and options in this user cluster configuration:

  * Non-high availability
  * Bundled Layer 2 load balancing


    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-user-basic
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user-basic
      namespace: cluster-user-basic
    spec:
      type: user
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.20**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.91
          ingressVIP: 10.200.0.92
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.92-10.200.0.100**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-user-basic
    spec:
      clusterName: user-basic
      nodes:
      - address:  10.200.0.30
      - address:  10.200.0.31
      - address:  10.200.0.32
    

### High-availability user cluster with multiple node pools

Note the following features and options in this user cluster configuration:

  * SSH key overrides
  * High availability
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing
  * Multiple node pools


    
    
    **registryMirrors :
      - endpoint: https://10.194.2.13:5007/v2/test-namespace
        caCertPath: /root/cert.pem
        pullCredentialConfigPath: /root/dockerconfig.json**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-user-ha-np
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user-ha-np
      namespace: cluster-user-ha-np
    spec:
      type: user
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.20
          - address: 10.200.0.21
          - address: 10.200.0.22**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  proxy:
        url: http://10.194.2.140:3128
        noProxy:
        - 127.0.0.1
        - localhost****  osEnvironmentConfig:
        addPackageRepo: false****  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.91
          ingressVIP: 10.200.0.92
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.92-10.200.0.100**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250**  credential:
        sshKeySecret:
          name: ssh-key
          namespace: cluster-user-ha-np**
    ---** apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-user-ha-np
    spec:
      clusterName: user-ha-np
      nodes:
      - address:  10.200.0.30
      - address:  10.200.0.31
      - address:  10.200.0.32
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np2
      namespace: cluster-user-ha-np
    spec:
      clusterName: user-ha-np
      nodes:
      - address:  10.200.0.33
      - address:  10.200.0.34
      - address:  10.200.0.35**
    

### High-availability user cluster with OIDC

Note the following features and options in this user cluster configuration:

  * High availability
  * OIDC
  * Behind a proxy
  * Registry mirror
  * Private package repository
  * Bundled Layer 2 load balancing off the Control Plane


    
    
    **registryMirrors :
      - endpoint: https://10.194.2.13:5007/v2/test-namespace
        caCertPath: /root/cert.pem
        pullCredentialConfigPath: /root/dockerconfig.json**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-user-ha-oidc
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user-ha-oidc
      namespace: cluster-user-ha-oidc
    spec:
      type: user
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.20
          - address: 10.200.0.21
          - address: 10.200.0.22**
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  proxy:
        url: http://10.194.2.140:3128
        noProxy:
        - 127.0.0.1
        - localhost****  osEnvironmentConfig:
        addPackageRepo: false****  loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.91
          ingressVIP: 10.200.0.92
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.92-10.200.0.100
        nodePoolSpec:
          nodes:
          - address: 10.200.0.25
          - address: 10.200.0.26
          - address: 10.200.0.27**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      authentication:**    oidc:
          issuerURL: "https://infra.example.dev/adfs"
          clientID: "be654652-2c45-49ff-9d7c-3663cee9ba51"
          clientSecret: "clientSecret"
          kubectlRedirectURL: "http://localhost:44320/callback"
          username: "unique_name"
          usernamePrefix: "oidc:"
          group: "groups"
          groupPrefix: "oidc:"
          scopes: "allatclaims"
          extraParams: "resource=token-groups-claim"
          deployCloudConsoleProxy: true
          certificateAuthorityData: base64EncodedCACertificate
          proxy: http://10.194.2.140:3128**
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-user-ha-oidc
    spec:
      clusterName: user-ha-oidc
      nodes:
      - address:  10.200.0.30
      - address:  10.200.0.31
      - address:  10.200.0.32
    

### High-availability user cluster with LDAP and BGP load balancing

Note the following features and options in this user cluster configuration:

  * High availability
  * LDAP
  * Bundled load balancing with BGP


    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-user-ha-ldap
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user-ha-ldap
      namespace: cluster-user-ha-ldap
    spec:
      type: user
      profile: default
      anthosBareMetalVersion: 1.16.8
      gkeConnect:
        projectID: project-fleet**  controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.20
          - address: 10.200.0.21
          - address: 10.200.0.22**
      clusterNetwork:**    advancedNetworking: true**
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20**  loadBalancer:
        mode: bundled
        type: bgp
        localASN: 65001
        bgpPeers:
        - ip: 10.8.0.10
          asn: 65002
        - ip: 10.8.0.11
          asn: 65002
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.91
          ingressVIP: 10.200.0.92
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.92-10.200.0.100**
      clusterOperations:
        projectID: project-fleet
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
      authentication:**  - name: ldap
        ldap:
          connectionType: ldaps
          group:
            baseDN: ou=Groups,dc=onpremidp,dc=example,dc=net
            filter: (objectClass=*)
            identifierAttribute: dn
          host: ldap.google.com:636
          user:
            baseDN: ou=Users,dc=onpremidp,dc=example,dc=net
            filter: (objectClass=*)
            identifierAttribute: uid
            loginAttribute: uid
          serviceAccountSecret:
            name: google-ldap-client-secret
            namespace: anthos-identity-service
            type: tls**
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-user-ha-ldap
    spec:
      clusterName: user-ha-ldap
      nodes:
      - address:  10.200.0.30
      - address:  10.200.0.31
      - address:  10.200.0.32
    ---** apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-user-ha-ldap
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.2.100**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
