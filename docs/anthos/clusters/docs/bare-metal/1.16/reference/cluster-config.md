---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config/
title: Generated cluster configuration file \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:57.774043+00:00
---

# Generated cluster configuration file  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Generated cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-config)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



The following is a sample of the YAML file that gets created when you run the `bmctl create config` command. For more information about this command, and how you use it to create different kinds of cluster configurations, see the following topics:

  * [Installation overview: choosing a deployment model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep)
  * [Creating admin clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/admin-cluster-creation)
  * [Creating user clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/user-cluster-creation)
  * [Creating hybrid clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation)
  * [Creating standalone clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/standalone-cluster-creation)

**Note:** Some of the fields in the cluster configuration file are immutable once the cluster is created. For more information, see the [Cluster configuration field reference](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#cluster_configuration_fields).

### Cluster configuration file
    
    
    # bmctl configuration variables. Because this section is valid YAML but not a valid Kubernetes
    # resource, this section can only be included when using bmctl to
    # create the initial admin/hybrid cluster. Afterwards, when creating user clusters by directly
    # applying the cluster and node pool resources to the existing cluster, you must remove this
    # section.
    gcrKeyPath: <path to GCR service account key>
    sshPrivateKeyPath: <path to SSH private key, used for node access>
    gkeConnectAgentServiceAccountKeyPath: <path to Connect agent service account key>
    gkeConnectRegisterServiceAccountKeyPath: <path to Hub registration service account key>
    cloudOperationsServiceAccountKeyPath: <path to Cloud Operations service account key>
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-example
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: example
      namespace: cluster-example
    spec:
      # Cluster type. This can be:
      #   1) admin:  to create an admin cluster. This can later be used to create user clusters.
      #   2) user:   to create a user cluster. Requires an existing admin cluster.
      #   3) hybrid: to create a hybrid cluster that runs admin cluster components and user workloads.
      #   4) standalone: to create a cluster that manages itself, runs user workloads, but does not manage other clusters.
      type: admin
      # Cluster profile. This can be either 'default' or 'edge'.
      # The edge profile is tailored for deployments on the edge locations
      # and should be used together with the 'standalone' cluster type.
      profile: default
      # Anthos cluster version.
      anthosBareMetalVersion: 1.16.8
      # GKE connect configuration
      gkeConnect:
        projectID: <GCP project ID>
      # Control plane configuration
      controlPlane:
        nodePoolSpec:
          nodes:
          # Control plane node pools. Typically, this is either a single machine
          # or 3 machines if using a high availability deployment.
          - address: <Machine 1 IP>
      # Cluster networking configuration
      clusterNetwork:
        # Pods specify the IP ranges from which pod networks are allocated.
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        # Services specify the network ranges from which service virtual IPs are allocated.
        # This can be any RFC1918 range that does not conflict with any other IP range
        # in the cluster and node pool resources.
        services:
          cidrBlocks:
          - 10.96.0.0/20
      # Load balancer configuration
      loadBalancer:
        # Load balancer mode can be either 'bundled' or 'manual'.
        # In 'bundled' mode a load balancer will be installed on load balancer nodes during cluster creation.
        # In 'manual' mode the cluster relies on a manually-configured external load balancer.
        mode: bundled
        # Load balancer port configuration
        ports:
          # Specifies the port the load balancer serves the Kubernetes control plane on.
          # In 'manual' mode the external load balancer must be listening on this port.
          controlPlaneLBPort: 443
        # There are two load balancer virtual IP (VIP) addresses: one for the control plane
        # and one for the L7 Ingress service.
        # If you use Layer2 load balancing, the VIPs must be in the same subnet as the load balancer nodes.
        # If you use bundled BGP-based load balancing (mode: 'bundled' and type: 'bgp'), the VIPs
        # must not come from the same subnet as any of the nodes in the cluster.
        # These IP addresses do not correspond to physical network interfaces.
        vips:
          # ControlPlaneVIP specifies the VIP to connect to the Kubernetes API server.
          # This address must not be in the address pools below.
          controlPlaneVIP: 10.0.0.8
          # IngressVIP specifies the VIP shared by all services for ingress traffic.
          # Allowed only in non-admin clusters.
          # This address must be in the address pools below.
          # ingressVIP: 10.0.0.2
        # AddressPools is a list of non-overlapping IP ranges for the data plane load balancer.
        # All addresses must be in the same subnet as the load balancer nodes.
        # Address pool configuration is only valid for 'bundled' LB mode in non-admin clusters.
        # addressPools:
        # - name: pool1
        #   addresses:
        #   # Each address must be either in the CIDR form (1.2.3.0/24)
        #   # or range form (1.2.3.1-1.2.3.5).
        #   - 10.0.0.1-10.0.0.4
        # A load balancer node pool can be configured to specify nodes used for load balancing.
        # These nodes are part of the Kubernetes cluster and run regular workloads as well as load balancers.
        # If the node pool config is absent then the control plane nodes are used.
        # Node pool configuration is only valid for 'bundled' LB mode.
        # nodePoolSpec:
        #  nodes:
        #  - address: <Machine 1 IP>
      # Proxy configuration
      # proxy:
      #   url: http://[username:password@]domain
      #   # A list of IPs, hostnames or domains that should not be proxied.
      #   noProxy:
      #   - 127.0.0.1
      #   - localhost
      # Logging and Monitoring
      clusterOperations:
        # Cloud project for logs and metrics.
        projectID: <GCP project ID>
        # Cloud location for logs and metrics.
        location: us-central1
      # Storage configuration
      storage:
        # lvpNodeMounts specifies the config for local PersistentVolumes backed by mounted disks.
        # These disks need to be formatted and mounted by the user, which can be done before or after
        # cluster creation.
        lvpNodeMounts:
          # path specifies the host machine path where mounted disks will be discovered and a local PV
          # will be created for each mount.
          path: /mnt/localpv-disk
          # storageClassName specifies the StorageClass that PVs will be created with. The StorageClass
          # is created during cluster creation.
          storageClassName: local-disks
        # lvpShare specifies the config for local PersistentVolumes backed by subdirectories in a shared filesystem.
        # These subdirectories are automatically created during cluster creation.
        lvpShare:
          # path specifies the host machine path where subdirectories will be created on each host. A local PV
          # will be created for each subdirectory.
          path: /mnt/localpv-share
          # storageClassName specifies the StorageClass that PVs will be created with. The StorageClass
          # is created during cluster creation.
          storageClassName: local-shared
          # numPVUnderSharedPath specifies the number of subdirectories to create under path.
          numPVUnderSharedPath: 5
      # NodeConfig specifies the configuration that applies to all nodes in the cluster.
      nodeConfig:
        # podDensity specifies the pod density configuration.
        podDensity:
          # maxPodsPerNode specifies at most how many pods can be run on a single node.
          maxPodsPerNode: 250
      # GKEOnPremAPI (Optional) Specify if you wish to explicitly enable/disable the cloud hosted gkeonprem
      # API to enable/disable cluster lifecycle management from gcloud UI and Terraform.
      # gkeOnPremAPI:
        # enabled: false
        # location is the Cloud location for the cluster resource metadata where the cluster will be enrolled.
        # location: us-central1
      # Authentication; uncomment this section if you wish to enable authentication to the cluster with OpenID Connect.
      # authentication:
      #   oidc:
      #     # issuerURL specifies the URL of your OpenID provider, such as "https://accounts.google.com". The Kubernetes API
      #     # server uses this URL to discover public keys for verifying tokens. Must use HTTPS.
      #     issuerURL: <URL for OIDC Provider; required>
      #     # clientID specifies the ID for the client application that makes authentication requests to the OpenID
      #     # provider.
      #     clientID: <ID for OIDC client application; required>
      #     # clientSecret specifies the secret for the client application.
      #     clientSecret: <Secret for OIDC client application; optional>
      #     # kubectlRedirectURL specifies the redirect URL (required) for the gcloud CLI, such as
      #     # "http://localhost:[PORT]/callback".
      #     kubectlRedirectURL: <Redirect URL for the gcloud CLI; optional, default is "http://kubectl.redirect.invalid">
      #     # username specifies the JWT claim to use as the username. The default is "sub", which is expected to be a
      #     # unique identifier of the end user.
      #     username: <JWT claim to use as the username; optional, default is "sub">
      #     # usernamePrefix specifies the prefix prepended to username claims to prevent clashes with existing names.
      #     usernamePrefix: <Prefix prepended to username claims; optional>
      #     # group specifies the JWT claim that the provider will use to return your security groups.
      #     group: <JWT claim to use as the group name; optional>
      #     # groupPrefix specifies the prefix prepended to group claims to prevent clashes with existing names.
      #     groupPrefix: <Prefix prepended to group claims; optional>
      #     # scopes specifies additional scopes to send to the OpenID provider as a comma-delimited list.
      #     scopes: <Additional scopes to send to OIDC provider as a comma-separated list; optional>
      #     # extraParams specifies additional key-value parameters to send to the OpenID provider as a comma-delimited
      #     # list.
      #     extraParams: <Additional key-value parameters to send to OIDC provider as a comma-separated list; optional>
      #     # proxy specifies the proxy server to use for the cluster to connect to your OIDC provider, if applicable.
      #     # Example: https://user:password@10.10.10.10:8888. If left blank, this defaults to no proxy.
      #     proxy: <Proxy server to use for the cluster to connect to your OIDC provider; optional, default is no proxy>
      #     # deployCloudConsoleProxy specifies whether to deploy a reverse proxy in the cluster to allow Google Cloud
      #     # Console access to the on-premises OIDC provider for authenticating users. If your identity provider is not
      #     # reachable over the public internet, and you wish to authenticate using Google Cloud console, then this field
      #     # must be set to true. If left blank, this field defaults to false.
      #     deployCloudConsoleProxy: <Whether to deploy a reverse proxy for Google Cloud console authentication; optional>
      #     # certificateAuthorityData specifies a Base64 PEM-encoded certificate authority certificate of your identity
      #     # provider. It's not needed if your identity provider's certificate was issued by a well-known public CA.
      #     # However, if deployCloudConsoleProxy is true, then this value must be provided, even for a well-known public
      #     # CA.
      #     certificateAuthorityData: <Base64 PEM-encoded certificate authority certificate of your OIDC provider; optional>
      # Node access configuration; uncomment this section if you wish to use a non-root user
      # with passwordless sudo capability for machine login.
      # nodeAccess:
      #   loginUser: <login user name>
    ---
    # Node pools for worker nodes
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-my-cluster
    spec:
      clusterName: my-cluster
      nodes:
      - address: <Machine 2 IP>
      - address: <Machine 3 IP>
    

The following section isn't included in the generated cluster configuration file, but provides useful information for configuring your node pools. The fields `spec.taints` and `spec.labels` in the NodePool spec are used for Pod scheduling. For more information about these fields, see [Add a new node pool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/add-remove-node-pools#add_a_new_node_pool).
    
    
    ...
      # Taints and labels are reconciled to the nodes of the node pool unless the node has
      # “baremetal.cluster.gke.io/label-taint-no-sync” annotated.
      taints:
      - key: <key1>
        value: <value1>
        # The effect can be either 'NoSchedule', 'PreferNoSchedule', or 'NoExecute'.
        # 'NoSchedule' means no pod will be able to schedule onto the node unless it has a matching toleration.
        # 'PreferNoSchedule' means the system avoids placing a pod that does not tolerate the taint on the node, but it is
        # not required.
        # `NoExecute` means pods that do not tolerate the taint will be evicted immediately, and pods that do tolerate the
        #  taint will never be evicted.
        effect: NoSchedule
      labels:
        key1: <value1>
        key2: <value2>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
