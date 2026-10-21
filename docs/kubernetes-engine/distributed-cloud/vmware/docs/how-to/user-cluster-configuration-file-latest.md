---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest/
title: User cluster configuration file 1.30 and higher \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:02.257371+00:00
---

# User cluster configuration file 1.30 and higher  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  User cluster configuration file 1.30 and higher Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the fields in the user cluster configuration file for versions 1.30 and higher Google Distributed Cloud.

## Generating a template for your configuration file

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your user cluster configuration file. Also `gkeadm` filled in some of the fields for you.

If you did not use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your user cluster configuration file.

To generate a template for your user cluster configuration file:
    
    
    gkectl create-config cluster --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace the following:

`OUTPUT_FILENAME`: a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.

`VERSION`: the Google Distributed Cloud version number. For example: `gkectl create-config cluster --gke-on-prem-version=1.36.100-gke.144`.

**Template**

Click to see the generated template for version 1.36.
    
    
    apiVersion: v1
    kind: UserCluster
    # (Required) A unique name for this cluster
    name: ""
    # (Required) GKE on-prem version (example: 1.3.0-gke.16)
    gkeOnPremVersion: 1.34.0-gke.566
    # # (Optional) Specify the prepared secret configuration which can be added or edited
    # # only during cluster creation
    # preparedSecrets:
    #   # reference to the secret namespace for a group of secrets; it should be prepared
    #   # beforehand by 'gkectl prepare secrets' command; it is immutable.
    #   namespace: ""
    # (Optional) Enable controlplane v2. Default is true
    enableControlplaneV2: true
    # (Optional) Enable advanced cluster options
    enableAdvancedCluster: true
    # # (Optional) vCenter configuration (default: inherit from the admin cluster)
    # vCenter:
    #   # # (Optional) vCenter server to use. Controlplane v2 needs to be enabled when the address
    #   # # is different from that in the admin cluster configuration
    #   # address: ""
    #   datacenter: ""
    #   cluster: ""
    #   # Resource pool to use. Specify [VSPHERE_CLUSTER_NAME]/Resources to use the default
    #   # resource pool
    #   resourcePool: ""
    #   # Storage policy to use for cluster VM storage and default StorageClass. Do not
    #   # specify it together with datastore
    #   storagePolicyName: ""
    #   # # Datastore to use for cluster VM storage and default StorageClass. Do not specify
    #   # # it together with storagePolicyName
    #   # datastore: ""
    #   # Provide the path to vCenter CA certificate pub key for SSL verification
    #   caCertPath: ""
    #   # The credentials to connect to vCenter
    #   credentials:
    #     # reference to external credentials file
    #     fileRef:
    #       # read credentials from this file
    #       path: ""
    #       # entry in the credential file
    #       entry: ""
    #     # # (Optional) reference to the credential secret; it should be prepared beforehand
    #     # # by 'gkectl prepare secrets' command
    #     # secretRef:
    #     #   # The version for this prepared secret; it can be specified as 'latest' or integer
    #     #   # string; it will be defaulted to latest version if it is not specified when creating
    #     #   # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
    #     #   # to be empty when rotating credentials
    #     #   version: ""
    #   # (Optional) vSphere folder where cluster VMs will be located. Defaults to the the
    #   # datacenter wide folder if unspecified.
    #   folder: ""
    # # (Optional) The absolute or relative path to the GCP service account key for pulling
    # # GKE images (default: inherit from the admin cluster)
    # componentAccessServiceAccountKeyPath: ""
    # # (Optional) The prepared credentials for component access service account key
    # componentAccessServiceAccountKey:
    #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
    #   # prepare secrets' command
    #   secretRef:
    #     # The version for this prepared secret; it can be specified as 'latest' or integer
    #     # string; it will be defaulted to latest version if it is not specified when creating
    #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
    #     # to be empty when rotating credentials
    #     version: ""
    # # (Optional) Use a private registry to host GKE images
    # privateRegistry:
    #   # Do not include the scheme with your registry address
    #   address: ""
    #   credentials:
    #     # reference to external credentials file
    #     fileRef:
    #       # read credentials from this file
    #       path: ""
    #       # entry in the credential file
    #       entry: ""
    #     # # (Optional) reference to the credential secret; it should be prepared beforehand
    #     # # by 'gkectl prepare secrets' command
    #     # secretRef:
    #     #   # The version for this prepared secret; it can be specified as 'latest' or integer
    #     #   # string; it will be defaulted to latest version if it is not specified when creating
    #     #   # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
    #     #   # to be empty when rotating credentials
    #     #   version: ""
    #   # The absolute or relative path to the CA certificate for this registry
    #   caCertPath: ""
    # (Required) Network configuration; vCenter section is optional and inherits from
    # the admin cluster if not specified
    network:
      # (Required when using "static" ipMode.type; "Seesaw" loadBalancer.kind; or setting
      # enableControlplaneV2 to "true") This section overrides ipMode.ipBlockFilePath
      # values when ipMode.type=static. It's also used for control-plane nodes when controlplane
      # v2 is enabled and seesaw nodes
      hostConfig:
        # List of DNS servers
        dnsServers:
        - ""
        # List of NTP servers
        ntpServers:
        - ""
        # # List of DNS search domains
        # searchDomainsForDNS:
        # - ""
      ipMode:
        # (Required) Define what IP mode to use ("dhcp" or "static")
        type: static
        # (Required when using "static" mode) The absolute or relative path to the yaml
        # file to use for static IP allocation. Hostconfig part will be overwritten by
        # network.hostconfig if specified
        ipBlockFilePath: ""
      # (Required) The Kubernetes service CIDR range for the cluster. Must not overlap
      # with the pod CIDR range
      serviceCIDR: 10.96.0.0/20
      # (Required) The Kubernetes pod CIDR range for the cluster. Must not overlap with
      # the service CIDR range
      podCIDR: 192.168.0.0/16
      vCenter:
        # vSphere network name
        networkName: ""
      # # (Optional) List of additional node network interfaces feature enabled by multipleNetworkInterfaces
      # additionalNodeInterfaces:
      # # vSphere network name
      # - networkName: ""
      #   # (Required) Define what IP mode to use ("dhcp" "static" or "none")
      #   type: static
      #   # # (Required when using "static" mode) The absolute or relative path to the yaml file
      #   # # to use for static IP allocation. Hostconfig part will be overwritten by network.hostconfig
      #   # # if specified
      #   # ipBlockFilePath: ""
      # (Required when setting enableControlplaneV2 to "true") Specify the IPs to use
      # for control-plane nodes when controlplane v2 is enabled. 1 IP is needed for non-HA
      # cluster and 3 for HA cluster. Non-empty controlPlaneIPBlock is not allowed when
      # controlplane v2 is disabled
      controlPlaneIPBlock:
        netmask: ""
        gateway: ""
        ips:
        - ip: ""
          hostname: ""
        - ip: ""
          hostname: ""
        - ip: ""
          hostname: ""
    # (Required) Load balancer configuration
    loadBalancer:
      # (Required) The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlPlaneVIP: ""
        # Shared by all services for ingress traffic
        ingressVIP: ""
      # (Required) Which load balancer to use "ManualLB" or "MetalLB".
      kind: MetalLB
      # # (Required when using "ManualLB" kind) Specify pre-defined nodeports
      # manualLB:
      #   # NodePort for ingress service's http (only needed for user cluster)
      #   ingressHTTPNodePort: 30243
      #   # NodePort for ingress service's https (only needed for user cluster)
      #   ingressHTTPSNodePort: 30879
      #   # NodePort for konnectivity server service (only needed for controlplane v1 user
      #   # cluster)
      #   konnectivityServerNodePort: 30563
      #   # NodePort for control plane service (not needed for HA admin cluster or controlplane
      #   # V2 user cluster)
      #   controlPlaneNodePort: 30562
      # (Required when using "MetalLB" kind in user clusters) Specify the MetalLB configs
      metalLB:
        # (Required) A list of non-overlapping IP pools used by load balancer typed services.
        # Must include ingressVIP of the cluster.
        addressPools:
        # (Required) Name of the address pool
        - name: address-pool-1
          # (Required) The addresses that are part of this pool. Each address must be
          # either in the CIDR form (1.2.3.0/24) or range form (1.2.3.1-1.2.3.5).
          addresses:
          - ""
          # # (Optional) Avoid using IPs ending in .0 or .255. This avoids buggy consumer devices
          # # mistakenly dropping IPv4 traffic for those special IP addresses (default: false)
          # avoidBuggyIPs: false
          # # (Optional) Prevent IP addresses to be automatically assigned from this pool (default:
          # # false)
          # manualAssign: false
    # (Optional) Enable dataplane v2
    enableDataplaneV2: true
    # # (Optional) DataplaneV2 configuration
    # dataplaneV2:
    #   # (Optional) Specify dataplanev2 forward mode (snat or dsr)
    #   forwardMode: snat
    # # (Optional) Enable support for multiple networking interfaces
    # multipleNetworkInterfaces: false
    # # (Optional) Enable advanced dataplane v2 networking features such as Egress NAT Gateway
    # # and it requires enableDataplaneV2 to be set
    # advancedNetworking: false
    # # (Optional) Disable installation of bundled ingress
    # disableBundledIngress: false
    # # (Optional) Storage specification for the cluster
    # storage:
    #   # # Whether to disable vSphere CSI components deployment. The feature is enabled by
    #   # # default
    #   # vSphereCSIDisabled: false
    # (Optional) User cluster master nodes must have either 1 or 3 replicas (default:
    # 4 CPUs; 8192 MB memory; 1 replica)
    masterNode:
      cpus: 4
      memoryMB: 8192
      # How many machines of this type to deploy
      replicas: 3
      # # (Optional/Preview) Topology domains that user cluster master nodes will be deployed
      # # to. Only 1 element is allowed. Advanced cluster must be enabled and infraConfigFilePath
      # # must be filled in admin cluster
      # topologyDomains:
      # - ""
      # # Enable auto resizing on master
      # autoResize:
      #   # Whether to enable auto resize for master. Defaults to false.
      #   enabled: false
      # vsphere:
      #   # (Optional) vSphere datastore the master nodes will be created on (default: vCenter.datastore)
      #   datastore: ""
      #   # (Optional) Storage policy to use for user master VM storage and datadisk (default:
      #   # vCenter.storagePolicyName)
      #   storagePolicyName: ""
      # # (Optional) Control plane load balancer configuration. Only supported when advanced
      # # cluster is enabled
      # controlPlaneLoadBalancer:
      #   # # (Optional) The control plane load balancer mode for advanced cluster. Possible values
      #   # # are bundled or manual. Default value is bundled for advanced cluster without topology
      #   # # domains; and is manual for advanced cluster with topology domains.
      #   # mode: ""
    # (Required) List of node pools. The total un-tainted replicas across all node pools
    # must be greater than or equal to 3
    nodePools:
    - name: pool-1
      # # (Optional) GKE on-prem version (example: 1.13.0-gke.16); it will be defaulted to
      # # cluster version if it is not specified; it can be used to roll back a node pool
      # # if it is specified as the previous node pool version
      # gkeOnPremVersion: ""
      cpus: 4
      memoryMB: 8192
      # How many machines of this type to deploy
      replicas: 3
      # # (Optional/Preview) Topology domains that node pool nodes will be deployed to. Only
      # # 1 element is allowed. Advanced cluster must be enabled and infraConfigFilePath must
      # # be filled in admin cluster
      # topologyDomains:
      # - ""
      # # (Optional) boot disk size; must be at least 40 (default: 40)
      # bootDiskSizeGB: 40
      # (Optional) Specify the type of OS image; available options can be set to "ubuntu"
      # "ubuntu_containerd" "cos" "ubuntu_cgv2" "cos_cgv2" or "windows". Default is "ubuntu_containerd".
      osImageType: ubuntu_cgv2
      # # (Required when using "windows" osImageType) Specify the OS image template in vCenter
      # osImage: ""
      # # Labels to apply to Kubernetes Node objects
      # labels: {}
      # # Taints to apply to Kubernetes Node objects
      # taints:
      # - key: ""
      #   value: ""
      #   effect: ""
      # vsphere:
      #   # (Optional) vSphere datastore the node pool will be created on (default: vCenter.datastore)
      #   datastore: ""
      #   # (Optional) Storage policy to use for nodepool (default: vCenter.storagePolicyName)
      #   storagePolicyName: ""
      #   # (Optional) Existing host groups used for VM/Host affinity. VM groups will be created
      #   # to bind with these host groups via vm-host affinity rules
      #   hostgroups:
      #   - ""
      #   # (Optional) vSphere tags to be attached to the virtual machines in the node pool.
      #   # It is supported in GKE on-prem version 1.7+
      #   tags:
      #   - category: ""
      #     name: ""
      # # (Optional) Horizontal autoscaling for the nodepool; replicas should not be edited
      # # while updating the nodepool if this is turned on
      # autoscaling:
      #   # min number of replicas in the NodePool
      #   minReplicas: 0
      #   # max number of replicas in the NodePool
      #   maxReplicas: 0
      # (Optional) Allow traffic of LoadBalancer typed services flow through nodes of
      # this pool. This is only needed for MetalLB mode. Set it to true for at least one
      # node pool in the cluster. Default is false.
      enableLoadBalancer: true
      # # (Optional/Preview) Update strategy for this node pool (it will overwrite nodePoolUpdatePolicy.updateStrategy
      # # setting)
      # updateStrategy:
      #   # # (Optional/Preview) Rolling update strategy for machines of the node pool
      #   # rollingUpdate:
      #   #   # # (Optional/Preview) The maximum number of machines that can be scheduled simultaneously
      #   #   # # during update/upgrade (default: 1)
      #   #   # maxSurge: "1"
    # Spread nodes across at least three physical hosts (requires at least three hosts)
    antiAffinityGroups:
      # Set to false to disable DRS rule creation
      enabled: true
    # # (Optional/Preview) Track user cluster VMs with vSphere tags
    # enableVMTracking: false
    # # Configure node pool update policy for the cluster
    # nodePoolUpdatePolicy:
    #   # (Optional/Preview) Number of node pools to update at a time. 0 means no limit.
    #   # 1 means updating one by one.
    #   maximumConcurrentNodePoolUpdate: 0
    #   # # (Optional/Preview) Cluster wide default node pool update strategy. A node pool will
    #   # # use this setting if it doesn't set specific updateStrategy
    #   # updateStrategy:
    #   #   # # (Optional/Preview) Rolling update strategy for machines of the node pool
    #   #   # rollingUpdate:
    #   #   #   # # (Optional/Preview) The maximum number of machines that can be scheduled simultaneously
    #   #   #   # # during update/upgrade (default: 1)
    #   #   #   # maxSurge: "1"
    # # (Optional) Additional configurations passed to kube-scheduler. Require advanced
    # # cluster is enabled
    # schedulerConfiguration:
    #   # (Optional) Default TopologySpreadConstraint rule applied to the pod scheduling.
    #   # See https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
    #   # for details.
    #   defaultTopologySpreadConstraint:
    #     typemeta:
    #       kind: ""
    #       apiversion: ""
    #     defaultconstraints:
    #     - maxskew: 0
    #       topologykey: ""
    #       whenunsatisfiable: ""
    #       labelselector:
    #         matchlabels: {}
    #         matchexpressions:
    #         - key: ""
    #           operator: ""
    #           values:
    #           - ""
    #       mindomains: 0
    #       nodeaffinitypolicy: ""
    #       nodetaintspolicy: ""
    #       matchlabelkeys:
    #       - ""
    #     defaultingtype: ""
    # # (Optional) Configure additional authentication.
    # authentication:
    #   # (Optional) Provide an additional serving certificate for the API server
    #   sni:
    #     certPath: ""
    #     keyPath: ""
    # # (Optional) Configure BinAuthz to enable deploy-time security control to the container
    # # images.
    # binaryAuthorization:
    #   # (Optional) Set value to string "disabled" or "project_singleton_policy_enforce".
    #   # Default is "disabled".
    #   evaluationMode: ""
    # (Required) Specify which GCP project to register your GKE OnPrem cluster to
    gkeConnect:
      projectID: ""
      # # (Optional) The location of the GKE Hub and Connect service where the cluster is
      # # registered to. It can be any GCP region or "global". Default to "global" when unspecified.
      # location: us-central1
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerServiceAccountKeyPath: ""
      # # (Optional) The prepared credentials for register service account key
      # registerServiceAccountKey:
      #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
      #   # prepare secrets' command
      #   secretRef:
      #     # The version for this prepared secret; it can be specified as 'latest' or integer
      #     # string; it will be defaulted to latest version if it is not specified when creating
      #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
      #     # to be empty when rotating credentials
      #     version: ""
    # # (Optional) Specify if you wish to explicitly enable/disable the cloud hosted gkeonprem
    # # API to enable/disable cluster lifecycle management from gcloud UI and Terraform.
    # gkeOnPremAPI:
    #   enabled: false
    # (Required) Specify which GCP project to connect your logs and metrics to
    stackdriver:
      # The project ID for logs and metrics. It should be the same with gkeconnect.projectID.
      projectID: ""
      # A GCP region where you would like to store logs and metrics for this cluster.
      clusterLocation: us-central1
      # The absolute or relative path to the key file for a GCP service account used to
      # send logs and metrics from the cluster
      serviceAccountKeyPath: ""
      # # (Optional) The prepared credentials for stackdriver service account key
      # serviceAccountKey:
      #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
      #   # prepare secrets' command
      #   secretRef:
      #     # The version for this prepared secret; it can be specified as 'latest' or integer
      #     # string; it will be defaulted to latest version if it is not specified when creating
      #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
      #     # to be empty when rotating credentials
      #     version: ""
      # (Optional) Disable vsphere resource metrics collection from vcenter.  False by
      # default
      disableVsphereResourceMetrics: false
    # (Optional) Configure kubernetes apiserver audit logging
    cloudAuditLogging:
      # The project ID for logs and metrics. It should be the same with gkeconnect.projectID.
      projectID: ""
      # A GCP region where you would like to store audit logs for this cluster.
      clusterLocation: us-central1
      # The absolute or relative path to the key file for a GCP service account used to
      # send audit logs from the cluster
      serviceAccountKeyPath: ""
      # # (Optional) The prepared credentials for cloud audit logging service account key
      # serviceAccountKey:
      #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
      #   # prepare secrets' command
      #   secretRef:
      #     # The version for this prepared secret; it can be specified as 'latest' or integer
      #     # string; it will be defaulted to latest version if it is not specified when creating
      #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
      #     # to be empty when rotating credentials
      #     version: ""
    # Enable auto repair for the cluster
    autoRepair:
      # Whether to enable auto repair feature. Set false to disable.
      enabled: true
    # # Encrypt Kubernetes secrets at rest
    # secretsEncryption:
    #   # Secrets Encryption Mode. Possible values are: GeneratedKey
    #   mode: GeneratedKey
    #   # GeneratedKey Secrets Encryption config
    #   generatedKey:
    #     # # key version
    #     # keyVersion: 1
    #     # # disable secrets encryption
    #     # disabled: false
    
    

## Required fields and default values

If a field is marked as _Required_ , then the completed configuration file must have a value filled in for the field.

Some fields are conditionally required. For example, `loadBalancer.metalLB.addressPools` is required if `loadBalancer.kind` is equal to `MetalLB`.

If a _Default_ value is given for a field, then the cluster will use that value if you don't enter anything for the field. You can override a default value by entering a value.

If a field is not marked as Required, then the field is optional. You can fill it in if it is relevant for you, but you don't have to fill it in.

## Filling in your configuration file

In your configuration file, enter field values as described in the following sections.

## `enableAdvancedCluster`

### 1.33 and higher

All new clusters are created as advanced clusters. If you include this field in your configuration file when creating a new cluster, it must be set to `true`. If you set this field to `false`, cluster creation will be blocked.

### 1.32

Optional  
Mutable (from `false` to `true` is allowed)  
Boolean  
Prepopulated: true  
Default: true

Set `enableAdvancedCluster` to `false` if you don't want to enable advanced cluster when creating a new cluster. When this flag is set to `true` (advanced cluster enabled), the underlying Google Distributed Cloud software deploys controllers that allow for a more extensible architecture. Enabling advanced cluster gives you access to new features and capabilities, such as [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). This field must have the same value as the admin cluster's `enableAdvancedCluster` field.

Be sure to review [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support) before enabling advanced cluster.

To update an existing cluster to advanced cluster, see [Update a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster). After updating to advanced cluster, disabling isn't allowed.

### 1.31

**Available only for new clusters**  
Preview  
Optional  
Immutable  
Boolean  
Prepopulated: false  
Default: false

Set `enableAdvancedCluster` to `true` if you want to enable advanced cluster when creating a new cluster. When this flag is set to `true` (advanced cluster enabled), the underlying Google Distributed Cloud software deploys controllers that allow for a more extensible architecture. Enabling advanced cluster gives you access to new features and capabilities, such as [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). This field must have the same value as the admin cluster's `enableAdvancedCluster` field.

### 1.30 and lower

Not available.

## `name`

Required  
String

A name of your choice for your user cluster. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



Example:
    
    
    name: "my-user-cluster"
    

## `gkeOnPremVersion`

Required  
Mutable  
String

The Google Distributed Cloud version for your user cluster.

Example:
    
    
    gkeOnPremVersion: "1.29.0-gke.1456"
    

## `preparedSecrets.namespace`

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove this field. Otherwise, if you want to use [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials), fill in this field.

Immutable  
String  
Possible values: A string that begins with "gke-onprem-secrets-"

The name of a Kubernetes namespace in the admin cluster where prepared Secrets are stored for this user cluster.

Example:
    
    
    preparedSecrets:
      namespace: "gke-onprem-secrets-alice"
    

## `enableControlplaneV2`

### 1.30 and higher

Mutable (from `false` to `true` is allowed)  
Boolean  
Prepopulated: true  
Default: true

In version 1.30 and higher, Controlplane V2 is required for new user clusters. If you include this field in your configuration file, it must be set to `true`.

To migrate an existing cluster to Controlplane V2, see [Migrate a user cluster to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features). After migrating to Controlplane V2, disabling Controlplane V2 isn't allowed.

With Controlplane V2, the control plane for a user cluster runs on one or more nodes in the user cluster itself. The benefits of Controlplane V2 include:

  * Architectural consistency between admin and user clusters.

  * Failure isolation. An admin cluster failure doesn't affect user clusters.

  * Operational separation. An admin cluster upgrade doesn't cause downtime for user clusters.

  * Deployment separation. You can put the admin and user clusters in different failure domains or geographical sites. For example, a user cluster in an edge location could be in a different geographical site from the admin cluster.




### 1.29 and lower

Immutable  
Boolean  
Prepopulated: true  
Default: true

To enable Controlplane V2, set `enableControlplaneV2` to `true` or remove the setting from your user cluster configuration file. Otherwise, set it to `false`. With Controlplane V2, the control plane for a user cluster runs on one or more nodes in the user cluster itself. When Controlplane V2 isn't enabled, the user cluster control plane runs in the admin cluster.

We recommend that you enable Controlplane V2.

Example:
    
    
    enableControlplaneV2: true
    

## `vCenter`

This section contains information about your vSphere environment and your connection to vCenter Server.

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove this entire section.

If you included the `vCenter` section in the admin cluster configuration file:

  * If you want a field in this section to be the same as what you specified for your admin cluster, remove the field or leave it commented out.

  * If you want a field to be different from what you specified for your admin cluster, fill it in here. Any fields that you fill in here in the `vCenter` section override the corresponding fields in your admin cluster configuration file.




### `vCenter.address`

Immutable  
String  
Default: Inherit from the admin cluster

The IP address or the hostname of the instance of vCenter Server that you want to use for this user cluster.

For more information, see [Finding your vCenter server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address).

If you specify a value that is different from the instance of vCenter Server used by the admin cluster, then `Controlplane V2` must be enabled, and you must provide values for `network.vCenter.networkName` and all the required fields in the `vCenter` section.

Examples:
    
    
    vCenter:
      address: "203.0.113.101"
    
    
    
    vCenter:
      address: "my-vcenter-server-2.my-domain.example"
    

### `vCenter.datacenter`

Immutable  
String  
Default: Inherit from the admin cluster

The relative path of a [vSphere data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html).

If you specify a value for this field, then you must also specify:

  * `vCenter.networkName`
  * Either `vCenter.datastore` or `vCenter.storagePolicyName`
  * Either `vCenter.cluster` or `vCenter.resourcePool`



The value you specify is relative to the root folder named `/`.

If your data center is in the root folder, the value is the name of the data center.

Example:
    
    
    vCenter:
      datacenter: "my-uc-data-center"
    

Otherwise, the value is a relative path that includes one or more folders along with the name of the data center.

Example:
    
    
    vCenter:
      datacenter: "data-centers/data-center-2"
    

### `vCenter.cluster`

Immutable  
String  
Default: Inherit from the admin cluster

The relative path of a [vSphere cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) that represents the ESXi hosts where your user cluster VMs will run. This vSphere cluster represents a subset of the physical ESXi hosts in your vCenter data center.

If you specify a value for this field, then you must also specify:

  * `vCenter.networkName`
  * `vCenter.datacenter`
  * Either `vCenter.datastore` or `vCenter.storagePolicyName`



The value you specify is relative to `/.../DATA_CENTER/vm/`.

If your vSphere cluster is in the `/.../DATA_CENTER/vm/` folder, the value is the name of the vSphere cluster

Example:
    
    
    vCenter:
      cluster: "my-uc-vsphere-cluster"
    

Otherwise, the value is a relative path that includes one or more folders along with the name of the vSphere cluster.

Example:
    
    
    vCenter:
      cluster: "clusters/vsphere-cluster-2"
    

### `vCenter.resourcePool`

Immutable  
String  
Default: Inherit from the admin cluster

A [vCenter resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) for your user cluster VMs.

If you want to use the default resource pool, set this to `VSPHERE_CLUSTER/Resources`.

Example:
    
    
    vCenter:
      resourcePool: "my-uc-vsphere-cluster/Resources"
    

The value you specify is relative to `/.../DATA_CENTER/host/.../VSPHERE_CLUSTER/Resources/`

If your resource pool is a direct child of `/.../DATA_CENTER/host/.../VSPHERE_CLUSTER/Resources/` the value is the name of the resource pool.

Example:
    
    
    vCenter:
      resourcePool: "my-uc-resource-pool"
    

Otherwise, the value is a relative path that has two or more resource pools.

Example:
    
    
    vCenter:
      resourcePool: "uc-resource-pool-1/uc-resource-pool-2"
    

### `vCenter.datastore`

Optional  
Immutable  
String  
Default: Inherit from the admin cluster

The name of a [vSphere datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for your user cluster.

The value you specify must be a name, not a path. Don't include any folders in the value.

Example:
    
    
    vCenter:
      datastore: "my-datastore"
    

If you specify a value for this field, don't specify a value for `vCenter.storagePolicyName`. The `vCenter.datastore` field is immutable except when you set the field to an empty string when you [migrate a datastore to Storage Policy Based Management (SPBM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm).

### `vCenter.storagePolicyName`

Optional  
Immutable  
String

The name of a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the cluster nodes.

You can also specify a VM storage policy for the nodes in a particular node pool. But the policy specified here applies to any node pool that doesn't have its own policy.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

If you specify a value for this field, don't specify a value for `vCenter.datastore`.

### `vCenter.caCertPath`

Mutable  
String  
Default: Inherit from the admin cluster

The path of the CA certificate for your vCenter server. For more information, see [Getting your vCenter CA certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path).

Example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert-2.pem"
    

For information on how to update this field, see [Update vCenter certificate references](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate).

### `vCenter.credentials.fileRef.path`

Mutable  
String  
Default: Inherit from the admin cluster

If you provide a value for preparedSecrets.namespace, do not provide a value for this field. Instead, provide a value for vCenter.credentials.secretRef.version.

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that contains the username and password of your vCenter user account. The user account must have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements).

You can use `gkectl update credentials` to update this field in an existing cluster. For more information, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

For information about updating your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-directory/my-credentials-2.yaml"
    

### `vCenter.credentials.fileRef.entry`

Mutable  
String  
Default: Inherit from the admin cluster

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that contains the username and password of your vCenter user account.

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vcenter-credentials-2"
    

### `vCenter.credentials.secretRef.version`

String  
Possible values: An integer string or "latest"  
Default value: "latest"

If you provide a value for preparedSecrets.namespace, fill in this field. Otherwise, remove this field or leave it commented out.

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains the username and password for the instance of vCenter Server that you intend to use for this user cluster.

Example:
    
    
    vCenter:
      credentials:
        secretRef:
          version: "1"
    

### `vCenter.folder`

Immutable  
String  
Default: Inherit from the admin cluster

The relative path of a vSphere folder that you have already created. This folder will hold your user cluster VMs.

If you do not specify a value, your user cluster VMs will be put in `/.../DATA_CENTER/vm/`.

If you specify a value, it is relative to `/.../DATA_CENTER/vm/`.

The value can be the name of a folder.

Example:
    
    
    vCenter:
      folder: "my-uc-folder"
    

Or the value can be a relative path that includes more than one folder.

Example:
    
    
    vCenter:
      folder: "folders/folder-2"
    

## `componentAccessServiceAccountKeyPath`

Mutable  
String  
Default: Inherit from the admin cluster

The path of the JSON key file for your component access service account.

Example:
    
    
    componentAccessServiceAccountKeyPath: "my-key-folder/uc-access-key.json"
    

## `componentAccessServiceAccountKey.secretRef.version`

Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains a JSON key for your component access service account.

Example:
    
    
    componentAccessServiceAccountKey:
      secretRef:
        version: "1"
    

## `privateRegistry`

Fill in this section if your admin cluster is using a [private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section), and you want your user cluster to use a different private registry or different settings. If you want to use a different private registry address, your cluster must have Controlplane V2 enabled. The new settings are picked up during cluster creation and update.

If you want to use the same settings as the admin cluster, remove this section or leave it commented out. If you leave this section empty, the system images default to gcr.io/gke-on-prem-release.

### `privateRegistry.address`

Immutable  
String  
Default: Inherit from the admin cluster

The IP address or FQDN (Fully Qualified Domain Name) of the machine that runs your private Docker registry.

Examples:
    
    
    privateRegistry:
      address: "203.0.113.10"
    
    
    
    privateRegistry:
      address: "fqdn.example.com"
    

### `privateRegistry.credentials.fileRef.path`

Mutable  
String  
Default: Inherit from the admin cluster

If you are planning to use prepared secret for the private registry, do not provide a value for this field. Instead, provide a value for privateRegistry.credentials.secretRef.version.

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that contains the username and password of an account that Google Distributed Cloud can use to access your private Docker registry.

Example:
    
    
    privateRegistry:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `privateRegistry.credentials.fileRef.entry`

Mutable  
String  
Default: Inherit from the admin cluster

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that contains the username and password of your private Docker registry account.
    
    
    privateRegistry:
      credentials:
        fileRef:
          entry: "private-registry-creds"
    

### `privateRegistry.credentials.secretRef.version`

String  
Possible values: An integer string or "latest"  
Default value: "latest"

If you provide a value for preparedSecrets.namespace and want to use prepared secret for a private registry, fill in this field. Otherwise, remove this field or leave it commented out.

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains the username and password for the instance of vCenter Server that you intend to use for this user cluster.

Example:
    
    
    privateRegistry:
      credentials:
        secretRef:
          version: "1"
    

### `privateRegistry.caCertPath`

Mutable  
String  
Default: Inherit from the admin cluster

When Docker pulls an image from your private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). Docker uses the CA's certificate to validate the registry's certificate.

Set this field to the path of the CA's certificate.

Example:
    
    
    privateRegistry:
      caCertPath: "my-cert-folder/registry-ca.crt"
    

## `network`

This section contains information about your user cluster network.

### `network.hostConfig`

### 1.30 and higher

This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes.

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (available in 1.31 and higher), remove this entire section. Otherwise, this section is required if one or more of the following are true:

  * `network.ipMode.type` is set to `static`.
  * `enableControlplaneV2` is set to `true` or allowed to default to `true`. Note that Conrolplane V2 is required for new user clusters.



### 1.29 and lower

This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes. If you are using the Seesaw load balancer, this information also applies to your Seesaw VMs.

This section is required if one or more of the following are true:

  * `network.ipMode.type` is set to `static`.
  * `enableControlplaneV2` is set to `true` or allowed to default to `true`. The Seesaw load balancer isn't supported on clusters with Controlplane V2 enabled.
  * `loadBalancer.kind` is set to `"Seesaw"`.



#### `network.hostConfig.dnsServers`

Required  
Immutable  
Array of strings.  
The maximum number of elements in the array is three.

The addresses of DNS servers for the VMs.

Example:
    
    
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
    

#### `network.hostConfig.ntpServers`

Required  
Immutable  
Array of strings

The addresses of time servers for the VMs to use.

Example:
    
    
    network:
      hostConfig:
        ntpServers:
        - "216.239.35.0"
    

#### `network.hostConfig.searchDomainsForDNS`

Immutable  
Array of strings

DNS search domains for the hosts to use. These domains are used as part of a domain search list.

Example:
    
    
    network:
      hostConfig:
        searchDomainsForDNS:
        - "my.local.com"
    

### `network.ipMode.type`

Immutable  
String  
Prepopulated: "static"  
Default: "dhcp"

If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`. If `enableControlplaneV2` is set to `true`, this setting applies to only worker nodes.

Example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

This field is required if `network.ipMode.type` = `static` or if [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file.

Immutable  
String

The absolute or relative path of the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your cluster.

Example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/user-cluster-ipblock.yaml"
    

### `network.serviceCIDR`

Immutable  
String  
Prepopulated: "10.96.0.0/20"  
>

A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range.

Example:
    
    
    network:
      serviceCIDR: "10.96.0.0/20"
    

### `network.podCIDR`

Immutable  
String  
Prepopulated: "192.168.0.0/16"  
Default: "192.168.0.0/16"

A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range.

Example:
    
    
    network:
      podCIDR: "192.168.0.0/16"
    

The Service range must not overlap with the Pod range.

The Service and Pod ranges must not overlap with any address outside the cluster that you want to reach from inside the cluster.

For example, suppose your Service range is 10.96.232.0/24, and your Pod range is 192.168.0.0/16. Any traffic sent from a Pod to an address in either of those ranges will be treated as in-cluster and will not reach any destination outside the cluster.

In particular, the Service and Pod ranges must not overlap with:

  * IP addresses of nodes in any cluster

  * IP addresses used by load balancer machines

  * VIPs used by control-plane nodes and load balancers

  * IP address of vCenter servers, DNS servers, and NTP servers




We recommend that your Service and Pod ranges be in the [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) address space.

Here is one reason for the recommendation to use RFC 1918 addresses. Suppose your Pod or Service range contains external IP addresses. Any traffic sent from a Pod to one of those external addresses will be treated as in-cluster traffic and will not reach the external destination.

### `network.vCenter.networkName`

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove this field. Otherwise, this field is required if `vCenter.address` is different from the vCenter address you are using for the admin cluster.

Immutable  
String

The name of the vSphere network for your user cluster nodes.

Example:
    
    
    network:
      vCenter:
        networkName: "my-network"
    

If the name contains a special character, you must use an escape sequence for it.

Special characters | Escape sequence  
---|---  
Slash (`/`) | `%2f`  
Backslash (`\`) | `%5c`  
Percent sign (`%`) | `%25`  
  
If the network name is not unique in your data center, you can specify a full path.

Example:
    
    
    network:
      vCenter:
        networkName: "/my-uc-datacenter/network/my-network"
    

### `network.additionalNodeInterfaces`

If you set `multipleNetworkInterfaces` to `true`, fill in this section. Otherwise, remove this section or leave it commented out.

Immutable

An array of objects, each of which describes a network interface that can be used on all or some of your cluster nodes.

#### `network.additionalNodeInterfaces[i].networkName`

Required if `multipleNetworkInterfaces` = `true`  
Immutable  
String

The name of the vSphere network that this additional node interface will connect to.

Example:
    
    
    network:
      additionalNodeInterfaces:
      - networkName: "my-node-interface-1"
    

#### `network.additionalNodeInterfaces[i].type`

Required if `multipleNetworkInterfaces` = `true`  
Immutable  
String

Example:
    
    
    network:
      additionalNodeInterfaces:
      - name: "my-node-interface-1"
        type: "static"
    

#### `network.additionalNodeInterfaces[i].ipBlockFilePath`

Required if `network.additionalNodeInterfaces[i].type` = `static`  
Immutable  
String

The path of an IP block file that contains IP addresses to be used for this network interface on the nodes that have this network interface.

Example:
    
    
    network:
      additionalNodeInterfaces:
      - name: "my-node-interface-1"
        type: "static"
        ipBlockFilePath: "my-ipblock-file-1"
    

### `network.controlPlaneIPBlock`

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove this entire section.

Otherwise, whether you include this section depends on the value you set in `enableControlplaneV2`:

  * If `enableControlplaneV2` is `true`, fill in this section.
  * If `enableControlplaneV2` is `false`, remove this section.



### `network.controlPlaneIPBlock.netmask`

Required if `enableControlplaneV2` = `true`  
Immutable  
String

Example:
    
    
    network:
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
    

### `network.controlPlaneIPBlock.gateway`

Required if `enableControlplaneV2` = `true`  
Immutable  
String

Example:
    
    
    network:
      controlPlaneIPBlock:
        gateway: "172.16.21.1"
    

### `network.controlPlaneIPBlock.ips`

Required if `enableControlplaneV2` = `true`  
Immutable  
Array of objects, each of which has an IP address and a hostname. The hostname is required when you migrate from Controlplane V1 to Controlplane V2; otherwise optional. Hostnames must be unique across the vCenter.

For a high-availability (HA) user cluster, the array has three elements. For a non-HA user cluster, the array has one element.

Example:
    
    
    network:
      controlPlaneIPBlock:
        ips:
        - ip: "172.16.21.6"
          hostname: "cp-vm-1"
        - ip: "172.16.21.7"
          hostname: "cp-vm-2"
        - ip: "172.16.21.8"
          hostname: "cp-vm-3"
    

## `loadBalancer`

This section contains information about the load balancer for your user cluster.

### `loadBalancer.vips.controlPlaneVIP`

Required  
Immutable  
String

The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster.

Example:
    
    
    loadBalancer:
      vips:
        controlplaneVIP: "203.0.113.3"
    

### `loadBalancer.vips.ingressVIP`

Required if `disableBundledIngress` = `false`  
Immutable  
String

The IP address that you have chosen to configure on the load balancer for the ingress proxy.

Example:
    
    
    loadBalancer:
      vips:
        ingressVIP: "203.0.113.4"
    

### `loadBalancer.kind`

Specify the kind of load balancer to use.

### 1.32 and higher

Required  
Immutable  
String  
Prepopulated: "MetalLB"

The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) field is configured in the admin cluster configuration file.

  * With topology domains: set this to `"ManualLB"`. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use topology domains.

  * Without topology domains: set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer or `"MetalLB"` for our bundled solution. Optionally, you can configure a different kind of load balancer for control-plane traffic. For more information, see `masterNode.controlPlaneLoadBalancer`.




### 1.31

Required  
Immutable  
String  
Prepopulated: "MetalLB"

The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) field is configured in the admin cluster configuration file.

  * With topology domains: set this to `"ManualLB"`. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use topology domains.

  * Without topology domains: set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer or `"MetalLB"` for our bundled solution.




### 1.30

Required  
Immutable  
String  
Prepopulated: "MetalLB"

Set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer (such as F5 BIG-IP or Citrix) or `"MetalLB"` for our bundled solution.

Although you can upgrade a cluster that has `kind` set to `"F5BigIP"` or `"Seesaw"`, you can't create new clusters. For information on migrating load balancing configurations, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### 1.29 and earlier

Required  
Immutable  
String  
Prepopulated: "MetalLB"

Set this to `"ManualLB"`, `"F5BigIP"`, `"Seesaw"`, or `"MetalLB"`.

To enable Dataplane V2 and Controlplane V2, we recommend that you use `"ManualLB"` if you have a third-party load balancer (such as F5 BIG-IP or Citrix) or `"MetalLB"` for our bundled solution.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

When you create user clusters using the Google Cloud console, the gcloud CLI, or Terraform, the kind of load balancer for the admin cluster and its user clusters must be the same. The only exception is if the admin cluster uses Seesaw, then the user clusters can use MetalLB. If you want your admin and user clusters to use different kinds of load balancers, you must create user clusters using the `gkectl` command-line tool.

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"manualLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.manualLB.ingressHTTPNodePort`

Required if `loadBalancer.kind` = `ManualLB` (see Version note)  
Immutable  
Integer  
Prepopulated: 30243

The ingress proxy in a user cluster is exposed by a [Kubernetes Service of type `LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer). The Service has a [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) for HTTP. Choose a `nodePort` value for the HTTP ServicePort, and set this field to the `nodePort` value.

**Version note** : In version 1.30 and higher, ingress node ports are optional for clusters using Controlplane V2.

Example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPNodePort: 32527
    

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Required if `loadBalancer.kind` = `ManualLB (see Version note)`  
Immutable  
Integer  
Prepopulated: 30879

The ingress proxy in a user cluster is exposed by a Service of type LoadBalancer. The Service has a ServicePort for HTTPS. Choose a `nodePort` value for the HTTPS ServicePort, and set this field to the `nodePort` value.

**Version note** : In version 1.30 and higher, ingress node ports are optional for clusters using Controlplane V2.

Example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPSNodePort: 30139
    

#### `loadBalancer.manualLB.controlPlaneNodePort`

Required if `loadBalancer.kind` = `ManualLB` and `enableControlplaneV2` = `false`  
Immutable  
Integer  
Prepopulated: 30562

The Kubernetes API server of a user cluster runs in the admin cluster, and is exposed by a Service of type `LoadBalancer`. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value.

Example:
    
    
    loadBalancer:
      manualLB:
        controlPlaneNodePort: 30968
    

#### `loadBalancer.manualLB.konnectivityServerNodePort`

Required if `loadBalancer.kind` = `ManualLB` and `enableControlplaneV2` = `false`  
Immutable  
Integer  
Prepopulated: 30563

The Kubernetes API server of a user cluster that uses kubeception runs in the admin cluster, and is exposed by a Service of type `LoadBalancer`. The Konnectivity server reuses this service with a different `nodePort` value. You must choose a `nodePort` value for the Konnectivity server.

Set this field to the `nodePort` value for the Konnectivity server.

Example:
    
    
    loadBalancer:
      manualLB:
        konnectivityServerNodePort: 30969
    

### `loadBalancer.f5BigIP`

### 1.30 and higher

In 1.30 and higher, the value `"F5BigIP"` isn't allowed for `loadbalancer.kind` for new user clusters. If the `loadBalancer.f5BigIP` section is in your configuration file, remove it or comment it out.

You can still use your F5 BIG-IP load balancer with new user clusters, but the configuration is different. For configuration details, see [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

If an existing cluster has this section configured, upgrades to version 1.32 are blocked. You must [migrate your clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to version 1.32.

### 1.29 and lower

If you set `loadbalancer.kind` to `"F5BigIP"`, fill in this section. Otherwise, remove this section or leave it commented out.

To enable new and advanced features, we recommend that you configure manual load balancing for your F5 BIG-IP load balancer. To enable manual load balancing, set `loadbalancer.kind` to`"ManualLB"` and fill in the `loadBalancer.manualLB` section. For more information, see [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

If you have an existing F5-BIG-IP load balancer and the cluster configuration uses this section, after you have upgraded to 1.29 or higher, we recommend that you [migrate to manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual).

#### `loadBalancer.f5BigIP.address`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The address of your F5 BIG-IP load balancer.

Example:
    
    
    loadBalancer:
      f5BigIP:
          address: "203.0.113.2"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The address of your F5 BIG-IP load balancer.

Example:
    
    
    loadBalancer:
      f5BigIP:
          address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.path`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The path of a [credentials file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

For information about updating your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: "my-config-folder/user-creds.yaml"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The path of a [credentials file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

For information about updating your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: "my-config-folder/user-creds.yaml"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.entry`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The name of a [BIG-IP partition](https://docs.cloud.google.com/solutions/partners/installing-f5-big-ip-adc-for-gke-on-prem#additional_configuration) that you created for your user cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-user-partition"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIP"`  
String

The name of a [BIG-IP partition](https://docs.cloud.google.com/solutions/partners/installing-f5-big-ip-adc-for-gke-on-prem#additional_configuration) that you created for your user cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-user-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIP"` and you are using SNAT  
String

The name of your SNAT pool.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIP"` and you are using SNAT  
String

The name of your SNAT pool.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

### 1.30 and higher

In 1.30 and higher, the value `"Seesaw"` isn't allowed for `loadbalancer.kind` for new user clusters because this load balancer isn't supported with new and advanced features. If the `loadBalancer.seesaw` section is in your configuration file, remove it or comment it out.

Instead, you can configure the bundled MetalLB load balancer. To enable the MetalLB load balancer, set `loadbalancer.kind` to`"MetalLB"` and fill in the `loadBalancer.metalLB` section. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

### 1.29 and lower

If you set `loadbalancer.kind` to `"Seesaw"`, fill in this section. Otherwise, remove this section or leave it commented out.

Note the following limitations with the SeeSaw load balancer:

  * If a [high-availability admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#adminmaster-replicas-field) manages this user cluster, then this user cluster can't use the Seesaw load balancer.
  * User clusters with Controlplane V2 enabled can't use the Seesaw load balancer.



To use these features, we recommend that you configure the MetalLB load balancer. To enable the MetalLB load balancer, set `loadbalancer.kind` to`"MetalLB"` and fill in the `loadBalancer.metalLB` section. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

#### `loadBalancer.seesaw.ipBlockFilePath`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The path of the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/user-seesaw-ipblock.yaml"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The path of the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/user-seesaw-ipblock.yaml"
    

#### `loadBalancer.seesaw.vrid`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
Integer  
Possible values: 1 - 255  
Prepopulated: 0  


The [virtual router identifier](https://datatracker.ietf.org/doc/html/rfc5798) of your Seesaw VM. This identifier, which is an integer of your choice, must be unique in a VLAN.

Example:
    
    
    loadBalancer:
      seesaw:
        vrid: 125
    

### 1.29 and lower

Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
Integer  
Possible values: 1 - 255  
Prepopulated: 0  


The [virtual router identifier](https://datatracker.ietf.org/doc/html/rfc5798) of your Seesaw VM. This identifier, which is an integer of your choice, must be unique in a VLAN.

Example:
    
    
    loadBalancer:
      seesaw:
        vrid: 125
    

#### `loadBalancer.seesaw.masterIP`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1).

Example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

### 1.29 and lower

Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1).

Example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

#### `loadBalancer.seesaw.cpus`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `Seesaw`  
Mutable  
Integer  
Prepopulated: 4  


The number of CPUs for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        cpus: 8
    

### 1.29 and lower

Required if `loadBalancer.kind` = `Seesaw`  
Mutable  
Integer  
Prepopulated: 4  


The number of CPUs for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        cpus: 8
    

#### `loadBalancer.seesaw.memoryMB`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `Seesaw`  
Mutable  
Integer  
Prepopulated: 3072  


The number of mebibytes of memory for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

**Note** : This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 220 = 1,048,576 bytes. One megabyte is 106 = 1,000,000 bytes.

### 1.29 and lower

Required if `loadBalancer.kind` = `Seesaw`  
Mutable  
Integer  
Prepopulated: 3072  


The number of mebibytes of memory for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

**Note** : This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 220 = 1,048,576 bytes. One megabyte is 106 = 1,000,000 bytes.

#### `loadBalancer.seesaw.vCenter.networkName`

### 1.30 and higher

**Not allowed for new clusters**  
Immutable  
String  
Default: Same as the cluster nodes

The name of the vCenter network that contains your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

### 1.29 and lower

Immutable  
String  
Default: Same as the cluster nodes

The name of the vCenter network that contains your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

#### `loadBalancer.seesaw.enableHA`

### 1.30 and higher

**Not allowed for new clusters**  
Immutable  
Relevant if `loadBalancer.kind` = `Seesaw`  
Boolean  
Prepopulated: false  
Default: false

If you want to create a high-availability (HA) Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

### 1.29 and lower

Immutable  
Relevant if `loadBalancer.kind` = `Seesaw`  
Boolean  
Prepopulated: false  
Default: false

If you want to create a high-availability (HA) Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

#### `loadBalancer.seesaw.disableVRRPMAC`

### 1.30 and higher

**Not allowed for new clusters**  
Immutable  
Relevant if `loadBalancer.kind` = `Seesaw`  
Boolean  
Prepopulated: true  
Default: true

If set to `true` (recommended), the Seesaw load balancer doesn't use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If this field is set this to `false`, the Seesaw load balancer uses MAC learning. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then this field must be set to `true`.

Example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

### 1.29 and lower

Immutable  
Relevant if `loadBalancer.kind` = `Seesaw`  
Boolean  
Prepopulated: true  
Default: true

If you set this to `true` (recommended), the Seesaw load balancer doesn't use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`.

Example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

### `loadBalancer.metalLB`

If you set `loadbalancer.kind` to `"MetalLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

#### `loadBalancer.metalLB.addressPools`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable (see exception)  


Array of objects, each of which contains information about an address pool to be used by the MetalLB load balancer.

### 1.32 and higher

The behavior of this field is the same when `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled). In both cases, the array isn't totally mutable. You can add address pools, but removing address pools from an existing address pool array isn't supported.

### 1.31

The behavior of this field depends on whether `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled):

  * If advanced cluster is enabled: the array isn't totally mutable. You can add address pools, but removing address pools from an existing address pool array isn't supported.

  * If advanced cluster isn't enabled: the array is mutable. You can add and remove address pools from an existing address pool array.




### 1.30 and earlier

You can add and remove address pools from an existing address pool array.

##### `loadBalancer.metalLB.addressPools[i].name`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable (see exception)  
String

A name of your choice for the address pool.

### 1.32 and higher

The behavior of this field is the same as when `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled). In both cases, changing the name after the cluster is created isn't supported.

### 1.31

The behavior of this field depends on whether `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled):

  * If advanced cluster is enabled: changing the name after the cluster is created isn't supported.

  * If advanced cluster isn't enabled: you can change the name of the pool after the cluster is created.




### 1.30 and earlier

You can change the name of the pool after the cluster is created.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
    

##### `loadBalancer.metalLB.addressPools[i].addresses`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable (see exception)  


Array of strings, each of which is a range of addresses. Each range must be in CIDR format or hyphenated range format.

### 1.32 and higher

The behavior of this field is the same as when `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled). In both cases, you can add addresses to an existing address pool, but removing addresses isn't supported.

### 1.31

The behavior of this field depends on whether `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled):

  * If advanced cluster is enabled: you can add addresses to an existing address pool, but removing addresses isn't supported.

  * If advanced cluster isn't enabled: you can add and remove addresses from an existing address pool.




### 1.30 and earlier

You can add and remove addresses from an existing address pool.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
          addresses:
          - "192.0.2.0/26"
          - "192.0.2.64-192.0.2.72"
    

##### `loadBalancer.metalLB.addressPools[i].avoidBuggyIPs`

Relevant if `loadBalancer.kind` = `MetalLB`  
Mutable  
Boolean  
Prepopulated: false  
Default: false

If you set this to `true`, the MetalLB controller will not assign IP addresses ending in .0 or .255 to Services. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
          - "192.0.2.0/26"
          - "192.0.2.64-192.0.2.72"
          avoidBuggyIPs: true
    

##### `loadBalancer.metalLB.addressPools[i].manualAssign`

Relevant if `loadBalancer.kind` = `MetalLB`  
Mutable  
Boolean  
Prepopulated: false  
Default: false

If you do not want the MetalLB controller to automatically assign IP addresses from this pool to Services, set this to `true`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool.

Otherwise, set this to `false`.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
          manualAssign: true
    

## `enableDataplaneV2`

### 1.30 and higher

Mutable (from `false` to `true` is allowed)  
Boolean  
Prepopulated: true  
Default: false

This field controls the Container Network Interface (CNI) that the cluster uses. Enabling Dataplane V2 is required to use Controlplane V2. You can change the field from `false` to `true` to enable Dataplane V2, but disabling Dataplane V2 isn't allowed.

  * In version 1.30 and higher, [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) is required for new user clusters and must be set to `true`. To migrate an existing 1.30 cluster to Dataplane V2, see [Migrate a user cluster to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features).

  * In version 1.31, Dataplane V2 is required for all clusters. Before upgrading to 1.31, follow the steps in [Enable Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#enable-dataplane-v2).




The benefits of Dataplane V2 include the following:

  * Dataplane V2 provides you with a more advanced and capable Container Network Interface (CNI) when compared with the previous CNI option, [Calico](https://github.com/projectcalico/calico). Calico is in maintenance mode, which means it receives only critical bug fixes and security updates, but no new feature development. In contrast, Dataplane V2 is actively developed and enhanced, ensuring that you have access to the latest networking innovations and capabilities.

  * Dataplane V2 is the preferred CNI for GKE and other Google Distributed Cloud products.




### 1.29 and lower

Immutable  
Boolean  
Prepopulated: true  
Default: false

If you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2), or if you want to use Controlplane V2, set this to `true`. Otherwise set this to `false`.

We recommend that you enable Dataplane V2.

Example:
    
    
      enableDataplaneV2: true
    

See [Troubleshoot Google Distributed Cloud NFS and DataPlane v2 issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/nfs-dataplane-v2) for troubleshooting steps.

## `dataplaneV2.forwardMode`

Mutable  
String  
Possible values: "snat", "dsr"  
Prepopulated: "snat"  
Default: "snat"

The forwarding mode for a cluster that has Dataplane V2 enabled.

With source network address translation (SNAT) mode, a packet is SNAT-translated when it is forwarded from a load balancer node to a backend Pod. The Pod cannot see the original source IP address, and the return packet must pass through the load balancer node.

With direct server return (DSR) mode, a packet retains its original source IP address when it is forwarded from a load balancer node to a backend Pod. The Pod can see the original source IP address, and the return packet goes directly to the client without passing through the load balancer node.

Example:
    
    
    dataplaneV2:
      forwardMode: "dsr"
    

## `multipleNetworkInterfaces`

Immutable  
Boolean  
Prepopulated: false  
Default: false

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, this field must be `false`.

If you want to enable multiple network interfaces for Pods, set this to `true`.

For more information, see [Configure multiple network interfaces for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic).

Example:
    
    
    multipleNetworkInterfaces: true
    

## `advancedNetworking`

Immutable  
boolean  
Prepopulated: false  
Default: false

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway), set this to `true`. Otherwise set it to `false`.

If you set this field to `true`, you must also set `enableDataplaneV2` to `true`.

Example:
    
    
    advancedNetworking: true
    

## `disableBundledIngress`

Set this to `true` if you want to [disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress) for the cluster. Otherwise, set it to `false`.

Boolean  
Mutable  
Prepopulated: false  
Default: false

Example:
    
    
    disableBundledIngress: true
    

## `storage.vSphereCSIDisabled`

If you want to disable the deployment of vSphere CSI components, set this to `true`. Otherwise, set it to `false`.

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, this field must be `true`.

Mutable  
Boolean  
Prepopulated: false  
Default: false

Example:
    
    
    storage:
      vSphereCSIDisabled: false
    

## `masterNode`

This section contains information about the nodes that serve as control-plane nodes for this user cluster.

### `masterNode.controlPlaneLoadBalancer`

### 1.32 and higher

Optionally, include this section to specify the kind of load balancer to use for control-plane traffic in the user cluster. Include `masterNode.controlPlaneLoadBalancer.mode` in your configuration file if you want to explicitly set the kind of load balancer to use rather than relying on the default value. Additionally, you must set `loadBalancer.kind` in your configuration file to specify the kind of load balancer to use for the data plane.

### `masterNode.controlPlaneLoadBalancer.mode`

Optional  
Immutable  
String  
Default: Depends on whether the cluster uses topology domains

The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) field is configured in the admin cluster configuration file.

  * With topology domains: specify `"manual"`, which is the default value. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up).

  * Without topology domains: specify either `"manual"` or `"bundled"`. Use `"manual"` if you have a third-party load balancer or `"bundled"` for our bundled solution, which uses [keepalived](http://keepalived.readthedocs.io) \+ [haproxy](http://www.haproxy.org/) running on the control-plane nodes. The default value is "`bundled"`.




Example:
    
    
    adminMaster:
      controlPlaneLoadBalancer:
        mode: "manual"
    

### 1.31 and lower

This section is unavailable. Instead, use `loadBalancer.kind` to specify the kind of load balancer for the user cluster to use.

### `masterNode.cpus`

Mutable  
Integer  
Prepopulated: 4  
Default: 4

The number of CPUs for each node that serves as a control plane for this user cluster.

Example:
    
    
    masterNode:
      cpus: 8
    

### `masterNode.memoryMB`

Mutable  
Integer  
Prepopulated: 8192  
Default: 8192

The mebibytes of memory for each node that serves as a control plane for this user cluster. Must be a multiple of 4.

Example:
    
    
    masterNode:
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `masterNode.replicas`

Immutable  
Integer  
Possible values: 1 or 3  
Prepopulated: 1  
Default: 1

The number of control-plane nodes for this user cluster. This number cannot be changed once you have created the cluster. If you want to update the number of replicas later, you must recreate the user cluster.

If the `enableAdvancedCluster` field is `true`, then you must set this field to `3`. Only highly-available (HA) user clusters are supported on advanced clusters.

Example:
    
    
    masterNode:
      replicas: 3
    

### `masterNode.autoResize.enabled`

Mutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to enable automatic resizing of the control-plane nodes for the user cluster. Otherwise, set this to `false`.

For more information, see [Enable node resizing for the control-plane nodes of a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize#enable_node_resizing_for_the_control-plane_nodes_of_a_user_cluster).

Example:
    
    
    masterNode:
      autoResize:
        enabled: true
    

### `masterNode.vsphere`

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove this entire section.

### `masterNode.vsphere.datastore`

Optional  
Immutable  
String  
Default: The value of `vCenter.datastore`

The datastore where the control-plane nodes for this user cluster will be created.

The value you specify must be a name, not a path. Don't include any folders in the value.

Example:
    
    
    masterNode:
      vSphere:
        datastore: "control-plane-datastore"
    

If you specify a value for this field, don't specify a value for `masterNode.vsphere.storagePolicyName`. The `masterNode.vsphere.datastore` field is immutable except when you set the field to an empty string when you [migrate a datastore to Storage Policy Based Management (SPBM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm).

### `masterNode.vsphere.storagePolicyName`

Optional  
Immutable  
String  
Default: The value of `vCenter.storagePolicyName`

The name of a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the control-plane nodes.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

Example:
    
    
    masterNode:
      vSphere:
        storagePolicyName: "control-plane-storage-policy"
    

If you specify a value for this field, don't specify a value for `masterNode.vsphere.datastore`.

### `masterNode.topologyDomains`

### 1.32 and higher

Preview  
Optional  
Array of strings | Allows one element or three different elements  
Immutable  
Default: `vSphereInfraConfig.defaultTopologyDomain` if specified in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

An array of topology domains. If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (which indicates the cluster will use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), optionally include this field. The number of topology domains in the array determines how the user cluster control-plane nodes are deployed, as follows:

  * One element: all user cluster control-plane nodes will be deployed in the specified topology domain.
  * Three elements: each user cluster control-plane node will be deployed in a different topology domain (that is, one node per topology domain).



### 1.31

Preview  
Optional  
Array of strings | But only one element is supported  
Immutable  
Default: `vSphereInfraConfig.defaultTopologyDomain` if specified in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

An array of topology domains. If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (which indicates the cluster will use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), optionally include this field. The user cluster control-plane nodes will be deployed in the specified topology domain.

### 1.30 and lower

Not available.

## `nodePools`

Required  
Mutable  
Array of objects, each of which describes a node pool.

For more information, see [Creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools).

### `nodePools[i].name`

Required  
Immutable  
String

A name of your choice for the node pool. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



Example:
    
    
    nodePools:
    - name: "my-node-pool-1"
    

### `nodePools[i].gkeOnPremVersion`

When you upgrade a user cluster, you can specify that selected worker node pools remain at the previous version.

If you want this worker node pool to remain at the previous version, set this to the previous version. Otherwise, remove this field or set it to the empty string. This option is only available for worker node pools. Load balancer node pools (node pools with `enableLoadBalancer: true`) must match the cluster `gkeOnPremVersion`. For more information, see [Upgrade a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster).

Mutable  
String  
Default: The cluster `gkeOnPremVersion`

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      gkeOnPremVersion: "1.13.0-gke.16"
    

### `nodePools[i].cpus`

Required  
Mutable  
Integer  
Prepopulated: 4

The number of vCPUs for each node in the pool.

Example:
    
    
    nodePools"
    - name: "my-node-pool"
      cpus: 8
    

### `nodePools[i].memoryMB`

Required  
Mutable  
Integer  
Prepopulated: 8192

The mebibytes of memory for each node in the pool. Must be a multiple of 4.

Example:
    
    
    nodePools"
    - name: "my-node-pool"
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `nodePools[i].replicas`

Required  
Mutable  
Integer  
Prepopulated: 3  
Possible values: The total number of untainted nodes across all node pools in the cluster must be at least 3.

The number of nodes in the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      replicas: 5
    

### `nodePools[i].bootDiskSizeGB`

Mutable  
Integer  
Prepopulated: 40  
Default: 40

The size of the boot disk in gibibytes for each node in the pool.

Example:
    
    
    nodePools
    - name: "my-node-pool"
      bootDiskSizeGB: 40
    

### `nodePools[i].osImageType`

Mutable  
String  
Possible values: For versions 1.34 and previous: "ubuntu_containerd", "cos"  
For 1.35 and newer: "ubuntu_cgv2", "cos_cgv2"  
Prepopulated: "ubuntu_cgv2"  
Default: "ubuntu_cgv2"

The type of OS image to run on the VMs in the node pool.

In version 1.32, Windows Server node pools are deprecated and will be unavailable in version 1.33 and higher. Support for Windows Server node pools ends on May 5, 2026. We recommend that you don't use "windows" as the OS image type on new clusters.

Note the following limitation with advanced clusters:

  * Version 1.31: if the `enableAdvancedCluster` field is `true`, only `ubuntu-cgroupv2` and `ubuntu_containerd` are supported on advanced clusters.

  * Version 1.32: All OS image types except "windows" are supported on advanced clusters.




Example:
    
    
    nodePools
    - name: "my-node-pool"
      osImageType: "ubuntu_cgv2"
    

### `nodePools[i].osImage`

Required if `nodePools[i].osImageType` = `windows`  
Mutable  
String  


The name of a Windows VM template. The template must be based on a Windows Server 2019 ISO that has the en-US language/region tag.

For more information, see [User guide for Windows Server OS node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools).

### `nodePools[i].labels`

Mutable  
Mapping

Labels to apply to each Kubernetes Node object in the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      labels:
        environment: "production"
        tier: "cache"
    

The kubelet can't apply labels to itself in certain namespaces for security reasons.

The reserved node label namespaces are : `kubernetes.io`, `k8s.io`, `googleapis.com`.

### `nodePools[i].taints`

Mutable  
Array of objects, each of which describes a [Kubernetes taint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-taints) that is applied to each node in the pool. Taints are key-value pairs associated with an `effect`. Taints are used with tolerations for Pod scheduling. Specify one of the following for the `effect`: `NoSchedule`, `PreferNoSchedule`, `NoExecute`.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      taints:
      - key: "staging"
        value: "true"
        effect: "NoSchedule"
    

### `nodePools[i].vsphere`

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, remove all fields in the `nodePools[i].vsphere` section except for `nodePools[i].vsphere.tags`.

### `nodePools[i].vsphere.datastore`

Mutable  
String  
Default: The value of `vCenter.datastore`

The name of the vCenter datastore where the nodes will be created.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        datastore: "my-datastore"
    

If you specify a value for this field, don't specify a value for `nodePools[i].vsphere.storagePolicyName`.

### `nodePools[i].vsphere.storagePolicyName`

Mutable  
String  
Default: The value of `vCenter.storagePolicyName`

The name of a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the nodes in the pool.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        storagePolicyName: "my-storage-policy"
    

If you specify a value for this field, don't specify a value for `nodePools[i].vsphere.datastore`.

### `nodePools[i].vsphere.hostgroups`

Fill in this section if you want to configure your cluster to use [VM host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity). If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file, configure host groups in the [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) field of the vSphere infrastructure configuration file instead.

Mutable   
Array of strings, each of which is the name of a [host DRS group](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

The array can have only one element.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        hostgroups:
        - "my-hostgroup"
    

### `nodePools[i].vsphere.tags`

Mutable  
Array of objects, each of which describes a [vSphere tag](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) to be placed on the VMs in the node pool.

Each tag has a category and a name.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        tags:
        - category: "purpose"
          name: "testing"
    

If you want to attach tags to all VMs in a node pool, your vCenter user account must have these [vSphere tagging privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security.html):

  * vSphere Tagging.Assign or Unassign vSphere Tag
  * vSphere Tagging.Assign or Unassign vSphere Tag on Object (vSphere 7)



### `nodePools[i].autoscaling`

Mutable  


If you want to enable automatic scaling for the node pool, fill in this section. Otherwise, remove this section or leave it commented out.

#### `nodePools[i].autoscaling.minReplicas`

Mutable  
Integer  
Possible values: Greater than or equal to 1  
Prepopulated: 0

The minimum number of nodes that the autoscaler can set for the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      autoscaling:
        minReplicas: 5
    

#### `nodePools[i].autoscaling.maxReplicas`

Mutable  
Integer  
Prepopulated: 0

The maximum number of nodes that the autoscaler can set for the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      autoscaling:
        maxReplicas: 10
    

### `nodePools[i].enableLoadBalancer`

Relevant if `loadBalancer.kind` = `"MetalLB"`  
Mutable  
Boolean  
Prepopulated: true  
Default: false

### 1.32 and higher

The behavior of this field is the same when `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled). In both cases, set this to `true` if you want to allow the MetalLB speaker to run on the nodes in the pool. Otherwise, set it to `false`.

### 1.31

The behavior of this field depends on whether `enableAdvancedCluster` is set to `true` (advanced cluster enabled) or `false` (advanced cluster isn't enabled):

  * If advanced cluster is enabled: this field has no effect because the MetalLB speaker will always run on the user cluster's control-plane nodes.

  * If advanced cluster isn't enabled: set this to `true` if you want to allow the MetalLB speaker to run on the nodes in the pool. Otherwise, set it to `false`.




### 1.29 and lower

Set this to `true` if you want to allow the MetalLB speaker to run on the nodes in the pool. Otherwise, set it to `false`.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

**Note:** Load balancer node pools (`enableLoadBalancer: true`) must have the same version as the cluster version (`gkeOnPremVersion`). Version skew and upgrading load balancer node pools separately from the cluster aren't supported.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      enableLoadBalancer: true
    

### `nodePools[i].updateStrategy.rollingUpdate.maxSurge`

Preview  
Mutable Integer Default: 1

The maximum number of machines in the node pool that can be updated simultaneously during an update or upgrade.
    
    
    nodePools:
    - name: "my-node-pool"
      updateStrategy:
        rollingUpdate:
          maxSurge: 3
    

### `nodePools[i].topologyDomains`

### 1.31 and higher

If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (which enables [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), optionally include this field.

Array of strings | But only one element is supported  
Immutable  
Default: `vSphereInfraConfig.defaultTopologyDomain` if specified in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

Nodes in this node pool will be put into the topology domain specified by this field. For each node pool, only one topology domain is allowed. All nodes in a node pool will be put into a single topology domain.

### 1.30 and lower

Not available.

## `schedulerConfiguration`

### 1.32 and higher

Preview  
Optional  


When setting up [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains), you can optionally set up additional configurations that will be passed to `kube-scheduler`.

### `schedulerConfiguration.defaultTopologySpreadConstraint`

Preview  
Optional  
Immutable

An object that defines a cluster-level default topology spread constraint rule that is applied to Pod scheduling. When the user cluster is created with topology domains, if this rule is configured, the `kube-scheduler` takes the default topology key and spreads Pods of Deployments, Statefulsets, and Replicasets on it by default. The structure is the same as the Kubernetes cluster-level default constraints.

Example:
    
    
    schedulerConfiguration:
      defaultTopologySpreadConstraint:
        defaultConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
        defaultingType: List
    

For details, see [Cluster-level default constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#cluster-level-default-constraints) in the Kubernetes documentation.

### 1.31 and lower

Not available.

## `antiAffinityGroups.enabled`

Mutable  
Boolean  
Prepopulated: true  
Default: true

If this field is `true` Google Distributed Cloud creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster's nodes, causing them to be spread across at least three physical ESXi hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security/defined-privileges/host-inventory-privileges.html) privilege.

  * There are at least four ESXi hosts available.




Even though the rule requires that the cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available.

Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#license_requirements), you cannot enable VMware DRS.

If you don't have DRS enabled, or if you don't have at least four hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

Note the following limitation with advanced clusters:

  * Version 1.31: if the `enableAdvancedCluster` field is `true`, anti-affinity rules aren't supported on advanced clusters, and you must set `antiAffinityGroups.enabled` to `false`.

  * Version 1.32: anti-affinity rules are supported on advanced clusters.




Example:
    
    
    antiAffinityGroups:
      enabled: false
    

## `enableVMTracking`

Preview  
Immutable  
Prepopulated: false

Set this to `true` to enable VM tracking with vSphere tags. Otherwise, set it to `false`.

For more information, see [Enable VM tracking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vm-track-tags).

Example:
    
    
    enableVMTracking: true
    

## `nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate`

Mutable  
Integer

The number of node pools to update at a time. A value of `1` specifies that one node pool can be updated at a time. A value of `0` specifies that an unlimited number of node pools can be updated at a time.

### Advanced cluster

Note the following limitation with advanced clusters:

  * **Version 1.31** : if the `enableAdvancedCluster` field is `true`, node pool update policies aren't supported on advanced clusters, so remove this section from your configuration file.

  * **Version 1.32** : node pool update policies are supported on advanced clusters.

  * The default value of `maximumConcurrentNodePoolUpdate` varies by version:

    * **Version 1.32.0-1.32.1000** : The default value is `1`.
    * **Version 1.32.1100+** : The default value is `0`.
    * **Version 1.33.0-1.33.600** : The default value is `1`.
    * **Version 1.33.700+** : The default value is `0`.
    * **Version 1.34.0-1.34.200** : The default value is `1`.
    * **Version 1.34.300+** : The default value is `0`.



### Non-advanced cluster

Possible values: 0 or 1  
Prepopulated: 0   
Default: 0

Example:
    
    
    nodePoolUpdatePolicy:
      maximumConcurrentNodePoolUpdate: 1
    

**Note:** Updating this configuration only doesn't impact workloads.

### nodePoolUpdatePolicy.updateStrategy.rollingUpdate.maxSurge

Preview  
Mutable Integer Default: 1

The maximum number of machines in a node pool that can be updated simultaneously during an update or upgrade. Applies to any node pool that doesn't specify its own update strategy.
    
    
    nodePools:
    - name: "my-node-pool"
      updateStrategy:
        rollingUpdate:
          maxSurge: 3
    

## `authentication`

This section contains information about how cluster users are authenticated and authorized.

### `authentication.oidc`

### Advanced cluster

#### `authentication.oidc.issuerURL`

Optional  
String  


URL where authorization requests are sent to your OpenID Connect (OIDC) provider. The Kubernetes API server uses this URL to discover public keys for verifying tokens. The URL must use HTTPS.

#### `authentication.oidc.kubectlRedirectURL`

Optional  
String  


The redirect URL that `kubectl` uses for authorization. When you enable OIDC, you must specify a `kubectlRedirectURL` value.

#### `authentication.oidc.clientID`

Optional  
String  


The ID for the client application that makes authentication requests to the OpenID provider.

#### `authentication.oidc.username`

Optional  
String  


JSON Web Token (JWT) claim to use as the username.

#### `authentication.oidc.usernamePrefix`

Optional  
String  


Prefix prepended to username claims.

#### `authentication.oidc.group`

Optional  
String  


JSON Web Token (JWT) claim that the provider uses to return your security groups.

#### `authentication.oidc.groupPrefix`

Optional  
String  


Prefix prepended to group claims to prevent clashes with existing names. For example, given a group `dev` and a prefix `oidc:`, `oidc:dev`.

#### `authentication.oidc.scopes`

Optional  
String  


Additional scopes to send to the OIDC as comma separated list.

#### `authentication.oidc.extraParams`

Optional  
String  


Additional key-value parameters to send to the OIDC as comma separated list.

#### `authentication.oidc.deployCloudConsoleProxy`

Optional  
Boolean  
Default: false

Specifies whether a reverse proxy is deployed in the cluster to connect Google Cloud console to an on-premises identity provider that is not publicly accessible over the internet. If your identity provider isn't reachable over the public internet, set this field to true to authenticate with Google Cloud console.

#### `authentication.oidc.caPath`

Optional  
String  


**Caution:** This field is only available in 1.32.800+, 1.33.400+, 1.34.100+.

The absolute or relative path to the CA file.

### Non-advanced cluster

Don't use this section. Instead, after cluster creation, edit the ClientConfig custom resource as described in [Set up fleet member clusters for OIDC authentication](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

### `authentication.sni`

If you want to provide an additional serving certificate for the cluster's Kubernetes API server, fill in this section. Otherwise, remove this section or leave it commented out.

**Note:** The SNI for Controlplane v2 user clusters is supported in version 1.28 and higher.

#### `authentication.sni.certPath`

Immutable  
String

The path of a serving certificate for the Kubernetes API server.

Example:
    
    
    authentication:
      sni:
        certPath: "my-cert-folder/example.com.crt"
    

#### `authentication.sni.keyPath`

Optional  
Immutable  
String

The path of the certificate's private key file.

Example:
    
    
    authentication:
      sni:
        keyPath: "my-cert-folder/example.com.key"
    

## `gkeConnect`

Required  
Immutable  


This section contains information about the Google Cloud project and service account you want to use to [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet.

### `gkeConnect.projectID`

Required  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). For new clusters, this project ID must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

Example:
    
    
    gkeConnect:
      projectID: "my-fleet-host-project"
    

### `gkeConnect.location`

Immutable  
String  
Default: global

Each cluster's fleet membership is managed by the Fleet service (`gkehub.googleapis.com`) and the Connect service (`gkeconnect.googleapis.com`). The location of the services can be global or regional. In 1.28 and later, you can optionally specify the Google Cloud region in which the Fleet and the Connect services run. If not specified, the global instances of the services are used. Note the following:

  * User clusters created prior to 1.28 are managed by the global Fleet and Connect services.

  * New clusters created using [the GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)— the Google Cloud console, the Google Cloud CLI, or Terraform—use the same region that you specify for the GKE On-Prem API.

  * For new clusters, if you include this field, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.


**Important:** If you plan to install Cloud Service Mesh on a regional cluster, you must install version 1.19.3 or later.

Example:
    
    
    gkeConnect:
      location: "us-central1"
    

### `gkeConnect.registerServiceAccountKeyPath`

Required  
Mutable  
String

The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account).

To update the value of this field, use `gkectl update cluster`.

For information about changing your connect-register service account key, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

### `gkeConnect.registerServiceAccountKey.secretRef.version`

Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains a JSON key for your connect-register service account.

Example:
    
    
    gkeConnect:
      registerServiceAccountKey:
        secretRef:
          version: "1"
    

## `gkeOnPremAPI`

In 1.16 and later, if the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) automatically in the region configured in `stackdriver.clusterLocation`.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




Enrolling your user cluster in the GKE On-Prem API lets you use the standard tools—the Google Cloud console, the Google Cloud CLI, and [Terraform](https://www.terraform.io/)— to manage the lifecycle of the cluster. Additionally, enrolling the cluster lets you use the console or the gcloud CLI to view cluster details. For example, you run can `gcloud` commands to [get information about your user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).

After you add this section and create or update the cluster, if subsequently you remove the section and update the cluster, the update will fail.

### `gkeOnPremAPI.enabled`

Mutable  
Boolean   
Default: `true`

By default, the cluster is enrolled in the GKE On-Prem API if the GKE On-Prem API is enabled in your project. Set to `false` if you don't want to enroll the cluster.

After the cluster is enrolled in the GKE On-Prem API, if you need to unenroll the cluster, make the following change and then update the cluster:
    
    
    gkeOnPremAPI:
      enabled: false
    

### `gkeOnPremAPI.location`

Immutable  
String  
Default: `stackdriver.clusterLocation`

The Google Cloud region where the GKE On-Prem API runs and stores cluster metadata. Choose one of the [supported regions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). You must use the same region that is configured in `gkeConnect.location`, `stackdriver.clusterLocation` and `cloudAuditLogging.clusterLocation`. If `gkeOnPremAPI.enabled` is `false`, don't include this field.

## `stackdriver`

Required  
Mutable  


This section contains required configurations for [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring).

### `stackdriver.projectID`

Required for Logging and Monitoring  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host__project). For new clusters, this project ID must be the same as the ID set in `gkeConnect.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

If needed, you can configure a log router in this project to route logs into log buckets in another project. For information on how to configure the log router, see [Supported destinations](https://docs.cloud.google.com/logging/docs/routing/overview#destinations).

Example:
    
    
    stackdriver:
      projectID: "my-fleet-host-project"
    

### `stackdriver.clusterLocation`

Required for Logging and Monitoring  
Immutable  
String  
Prepopulated: "us-central1"

The Google Cloud region where you want to route and store Cloud Monitoring metrics. We recommend that you choose a region that's near your on-premises data center.

You specify the Cloud Logging logs routing and storage location in the Log Router configuration. For more information about logs routing, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

The Stackdriver Operator (`stackdriver-operator`) attaches the value from this field to each log entry and metric before they're routed to Google Cloud. These attached labels can be useful for filtering your logs and metrics in the Logs Explorer and Metrics Explorer respectively.

For new clusters, if you include the `gkeOnPremAPI` and `cloudAuditLogging` sections in the configuration file, the region that you set here must be the same region that you set in `gkeConnect.location`, `gkeOnPremAPI.location`, and `cloudAuditLogging.clusterLocation`. If the regions aren't the same, cluster creation fails.

Example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.serviceAccountKeyPath`

Required for Logging and Monitoring  
Mutable  
String

The path of the JSON key file for your logging-monitoring service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your logging-monitoring service account key, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    stackdriver:
      serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
    

### `stackdriver.serviceAccountKey.secretRef.version`

Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains a JSON key for your logging monitoring service account.

Example:
    
    
    stackdriver:
      serviceAccountKey:
        secretRef:
          version: "1"
    

### `stackdriver.disableVsphereResourceMetrics`

Mutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to disable the collection of metrics from vSphere. Otherwise, set it to `false`.

Example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `usageMetering`

### 1.32 and higher

The usage metering feature is unsupported in version 1.32 and higher. Don't include this section when you create new clusters. However, existing clusters using this feature will continue to function. As the alternative, we recommend that you use the predefined dashboard, [Anthos Cluster Utilization Metering](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/predefined-dashboards), to understand resource usage at different levels. Contact Cloud Customer Care if the alternative does not satisfy your use cases.

### 1.30 and 1.31

We recommend that you don't use this preview feature when you create new clusters. However, existing clusters using this feature will continue to function. As the alternative, we recommend that you use the predefined dashboard, [Anthos Cluster Utilization Metering](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/predefined-dashboards), to understand resource usage at different levels.

If the `enableAdvancedCluster` field is `true`, remove this section. Usage metering isn't supported on advanced clusters.

### 1.29 and lower

Preview  
Immutable

We recommend that you don't use this preview feature when you create new clusters. However, existing clusters using this feature will continue to function. As the alternative, we recommend that you use the predefined dashboard, [Anthos Cluster Utilization Metering](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/predefined-dashboards), to understand resource usage at different levels.

### `usageMetering.bigQueryProjectID`

Preview  
Required for usage metering  
Immutable  
String

The ID of the Google Cloud project where you want to store usage metering data.

Example:
    
    
    usageMetering:
    bigQueryProjectID: "my-bq-project"
    

### `usageMetering.bigQueryDatasetID`

Preview  
Required for usage metering  
Immutable  
String

The ID of the BigQuery dataset where you want to store usage metering data. Example:
    
    
    usageMetering:
    bigQueryDatasetID: "my-bq-dataset"
    

### `usageMetering.bigQueryServiceAccountKeyPath`

Preview  
Required for usage metering  
Immutable  
String.

The path of the JSON key file for your BigQuery service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your BigQuery service account key, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    usageMetering:
    bigQueryServiceAccountKeyPath: "my-key-folder/bq-key.json"
    

### `usageMetering.bigQueryServiceAccountKey.secretRef.version`

Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your BigQuery service account.

Example:
    
    
    gkeConnect:
    bigQueryServiceAccountKey:
      secretRef:
        version: "1"
    

### `usageMetering.enableConsumptionMetering`

Preview  
Required for usage metering  
Immutable  
Boolean  
Prepopulated: false

Set this to `true` if you want to enable consumption-based metering. Otherwise set this to false.

Example:
    
    
    usageMetering:
    enableConsumptionMetering: true
    

## `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in this section. Otherwise, remove this section or leave it commented out.

### `cloudAuditLogging.projectID`

Required for Cloud Audit Logs  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). For new clusters, this project ID must be the same as the ID set in `gkeConnect.projectID` and `stackdriver.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

If needed, you can configure a log router in this project to route logs into log buckets in another project. For information on how to configure the log router, see [Supported destinations](https://docs.cloud.google.com/logging/docs/routing/overview#destinations).

Example:
    
    
    cloudAuditLogging:
      projectID: "my-fleet-host-project"
    

### `cloudAuditLogging.clusterLocation`

Required for Cloud Audit Logs  
Immutable  
String

The Google Cloud region where you want to store audit logs. It is a good idea to choose a region that is near your on-premises data center

For new clusters, if you include the `gkeOnPremAPI` and `stackdriver` sections in the configuration file, the region that you set here must be the same region that you set in `gkeConnect.location`, `gkeOnPremAPI.location`, and `stackdriver.clusterLocation`. If the regions aren't the same, cluster creation fails.

Example:
    
    
    cloudAuditLogging:
      clusterLocation: "us-central1"
    

### `cloudAuditLogging.serviceAccountKeyPath`

Required for Cloud Audit Logs  
Mutable  
String

The path of the JSON key file for your audit-logging service account.

If you will be creating the cluster with `enableAdvancedCluster` set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then set `cloudAuditLogging.serviceAccountKeyPath` to the same path as `stackdriver.serviceAccountKeyPath`.

To update the value of this field, use `gkectl update cluster`.

For information about changing your audit-logging service account key, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

### `cloudAuditLogging.serviceAccountKey.secretRef.version`

Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) in the admin cluster that contains a JSON key for your audit logging service account.

Example:
    
    
    cloudAuditLogging:
      serviceAccountKey:
        secretRef:
          version: "1"
    

## `autoRepair.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable node auto repair. Otherwise, set it to `false`.

Example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to encrypt Secrets without the need for an external KMS (Key Management Service), or any other dependencies, fill in this section. Otherwise, remove this section or leave it commented out.

If you will be creating the cluster with [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then remove this section. This feature isn't supported with advanced clusters.

### `secretsEncryption.mode`

Required for Secrets encryption  
Immutable  
String  
Possible value: "GeneratedKey"  
Prepopulated: "GeneratedKey"

The Secret encryption mode.
    
    
    secretsEncryption:
      mode: "GeneratedKey"
    

### `secretsEncryption.generatedKey.keyVersion`

Required for Secrets encryption  
Mutable  
Integer  
Prepopulated: 1

An integer of your choice to use for the key version number. We recommend that you start with `1`.

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        keyVersion: 1
    

### `secretsEncryption.generatedKey.disabled`

Mutable  
Boolean  
Prepopulated: false

Set this to `true` to disable Secrets encryption. Otherwise set it to `false`.

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        disabled: false
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
