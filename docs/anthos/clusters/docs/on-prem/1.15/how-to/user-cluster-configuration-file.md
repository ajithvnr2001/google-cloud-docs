---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file/
title: User cluster configuration file \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:13.485269+00:00
---

# User cluster configuration file  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  User cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-cluster-configuration-file)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/user-cluster-configuration-file)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes the fields in the Google Distributed Cloud user cluster configuration file.

## Generating a template for your configuration file

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your user cluster configuration file. And `gkeadm` filled in some of the fields for you.

If you did not use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your user cluster configuration file.

To generate a template for your user cluster configuration file:
    
    
    gkectl create-config cluster --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace the following:

`OUTPUT_FILENAME`: a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.

`VERSION`: the desired version number. For example: `gkectl create-config cluster --gke-on-prem-version=1.10.0-gke.8`.

**Template**

Click to see the generated template.
    
    
    apiVersion: v1
    kind: UserCluster
    # (Required) A unique name for this cluster
    name: ""
    # (Required) GKE on-prem version (example: 1.3.0-gke.16)
    gkeOnPremVersion: ""
    # # (Optional) Specify the prepared secret configuration which can be added or edited
    # # only during cluster creation
    # preparedSecrets:
    #   # reference to the secret namespace for a group of secrets; it should be prepared
    #   # beforehand by 'gkectl prepare secrets' command; it is immutable.
    #   namespace: ""
    # (Required if using HA admin cluster) Enable controlplane v2. Default is true
    enableControlplaneV2: true
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
    #   datastore: ""
    #   # (Optional/Preview) Storage policy to use for user cluster VM storage and default
    #   # StorageClass
    #   storagePolicyName: ""
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
        type: dhcp
        # # (Required when using "static" mode) The absolute or relative path to the yaml file
        # # to use for static IP allocation. Hostconfig part will be overwritten by network.hostconfig
        # # if specified
        # ipBlockFilePath: ""
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
      #   type: dhcp
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
    # (Required) Load balancer configuration
    loadBalancer:
      # (Required) The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlPlaneVIP: ""
        # Shared by all services for ingress traffic
        ingressVIP: ""
      # (Required) Which load balancer to use "F5BigIP" "Seesaw" "ManualLB" or "MetalLB".
      # Uncomment the corresponding field below to provide the detailed spec
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
      #   # # (Optional) NodePort for addon service (only needed for admin cluster Prometheus
      #   # # and Grafana federation feature)
      #   # addonsNodePort: 0
      # # (Required when using "F5BigIP" kind) Specify the already-existing partition and
      # # credentials
      # f5BigIP:
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
      #   partition: ""
      #   # # (Optional) Specify a pool name if using SNAT
      #   # snatPoolName: ""
      # # (Required when using "Seesaw" kind; NOT supported for HA admin cluster) Specify
      # # the Seesaw configs
      # seesaw:
      #   # (Required) The absolute or relative path to the yaml file to use for IP allocation
      #   # for LB VMs. Must contain one or two IPs. Hostconfig part will be overwritten by
      #   # network.hostconfig if specified.
      #   ipBlockFilePath: ""
      #   # (Required) The Virtual Router IDentifier of VRRP for the Seesaw group. Must be
      #   # between 1-255 and unique in a VLAN.
      #   vrid: 0
      #   # (Required) The IP announced by the master of Seesaw group
      #   masterIP: ""
      #   # (Required) The number CPUs per machine
      #   cpus: 4
      #   # (Required) Memory size in MB per machine
      #   memoryMB: 3072
      #   # (Optional) Network that the LB interface of Seesaw runs in (default: cluster network)
      #   vCenter:
      #     # vSphere network name
      #     networkName: ""
      #   # (Optional) Run two LB VMs to achieve high availability (default: false)
      #   enableHA: false
      #   # (Optional) Avoid using VRRP MAC and rely on gratuitous ARP to do failover. In
      #   # this mode MAC learning is not needed but the gateway must refresh arp table based
      #   # on gratuitous ARP. It's recommended to turn this on to avoid MAC learning configuration.
      #   # In vsphere 7+ it must be true to enable HA. It is supported in GKE on-prem version
      #   # 1.7+. (default: false)
      #   disableVRRPMAC: true
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
    # # (Optional) Enable support for multiple networking interfaces
    # multipleNetworkInterfaces: false
    # # (Optional) Enable advanced dataplane v2 networking features such as Egress NAT Gateway
    # # and it requires enableDataplaneV2 to be set
    # advancedNetworking: false
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
      replicas: 1
      # # Enable auto resizing on master
      # autoResize:
      #   # Whether to enable auto resize for master. Defaults to false.
      #   enabled: false
      # vsphere:
      #   # (Optional) vSphere datastore the master nodes will be created on (default: vCenter.datastore)
      #   datastore: ""
      #   # (Optional/Preview) Storage policy to use for user master VM storage and datadisk
      #   storagePolicyName: ""
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
      # # (Optional) boot disk size; must be at least 40 (default: 40)
      # bootDiskSizeGB: 40
      # (Optional) Specify the type of OS image; available options can be set to "ubuntu"
      # "ubuntu_containerd" "cos" or "windows". Default is "ubuntu_containerd".
      osImageType: ubuntu_containerd
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
      #   # (Optional/Preview) Storage policy to use for nodepool
      #   storagePolicyName: ""
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
    # # (Optional) Configure additional authentication.
    # authentication:
    #   # (Optional) Provide an additional serving certificate for the API server
    #   sni:
    #     certPath: ""
    #     keyPath: ""
    # (Required) Specify which GCP project to register your GKE OnPrem cluster to
    gkeConnect:
      projectID: ""
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
    # (Required) Specify which GCP project to connect your logs and metrics to
    stackdriver:
      # The project ID for logs and metrics. It should be the same with gkeconnect.projectID.
      projectID: ""
      # A GCP region where you would like to store logs and metrics for this cluster.
      clusterLocation: us-central1
      enableVPC: false
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
    # # (Optional/Preview) Configure the GKE usage metering feature
    # usageMetering:
    #   bigQueryProjectID: ""
    #   # The ID of the BigQuery Dataset in which the usage metering data will be stored
    #   bigQueryDatasetID: ""
    #   # The absolute or relative path to the key file for a GCP service account used by
    #   # gke-usage-metering to report to BigQuery
    #   bigQueryServiceAccountKeyPath: ""
    #   # # (Optional) The prepared credentials for big query service account key
    #   # bigQueryServiceAccountKey:
    #   #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
    #   #   # prepare secrets' command
    #   #   secretRef:
    #   #     # The version for this prepared secret; it can be specified as 'latest' or integer
    #   #     # string; it will be defaulted to latest version if it is not specified when creating
    #   #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
    #   #     # to be empty when rotating credentials
    #   #     version: ""
    #   # Whether or not to enable consumption-based metering
    #   enableConsumptionMetering: false
    # # (Optional) Configure kubernetes apiserver audit logging
    # cloudAuditLogging:
    #   # The project ID for logs and metrics. It should be the same with gkeconnect.projectID.
    #   projectID: ""
    #   # A GCP region where you would like to store audit logs for this cluster.
    #   clusterLocation: ""
    #   # The absolute or relative path to the key file for a GCP service account used to
    #   # send audit logs from the cluster
    #   serviceAccountKeyPath: ""
    #   # # (Optional) The prepared credentials for cloud audit logging service account key
    #   # serviceAccountKey:
    #   #   # reference to the credential secret; it should be prepared beforehand by 'gkectl
    #   #   # prepare secrets' command
    #   #   secretRef:
    #   #     # The version for this prepared secret; it can be specified as 'latest' or integer
    #   #     # string; it will be defaulted to latest version if it is not specified when creating
    #   #     # a cluster; it is allowed to be empty when creating a cluster; it is not allowed
    #   #     # to be empty when rotating credentials
    #   #     version: ""
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
    

## Filling in your configuration file

In your configuration file, enter field values as described in the following sections.

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
    
    
    gkeOnPremVersion: "1.14.0-gke.1"
    

## `preparedSecrets.namespace`

If you want to use [prepared credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials), fill in this field. Otherwise remove this field or leave it commented out.

Optional  
Immutable  
String  
Possible values: A string that begins with "gke-onprem-secrets-"

The name of a Kubernetes namespace in the admin cluster where prepared Secrets are kept for this user cluster.

Example:
    
    
    preparedSecrets:
      namespace: "gke-onprem-secrets-alice"
    

## `enableControlplaneV2`

Optional  
Immutable  
Boolean  
Prepopulated: true Default: true

If you want to create a user cluster that has [Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2) enabled, set this to `true`. Otherwise, set it to `false`.

Example:
    
    
    enableControlplaneV2: true
    

## `vCenter`

This section holds information about your vSphere environment and your connection to vCenter Server.

If you want a field in this section to be the same as what you specified for your admin cluster, remove the field or leave it commented out.

If you want a field to be different from what you specified for your admin cluster, fill it in here. Any fields that you fill in here in the `vCenter` section override the corresponding fields in your admin cluster configuration file.

### `vCenter.address`

Preview  
Optional  
Immutable  
String  
Default: Inherit from the admin cluster

The IP address or the hostname of the instance of vCenter Server that you want to use for this user cluster.

For more information, see [Finding your vCenter server address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vcenter-server-address).

If you specify a value that is different from the instance of vCenter Server used by the admin cluster, then `Controlplane V2` must be enabled, and you must provide values for `network.vCenter.networkName` and all the required fields in the section `vCenter`.

Examples:
    
    
    vCenter:
      address: "203.0.113.101"
    
    
    
    vCenter:
      address: "my-vcenter-server-2.my-domain.example"
    

### `vCenter.datacenter`

Optional  
Immutable  
String  
Default: Inherit from the admin cluster

The relative path of a [vSphere data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html).

If you specify a value for this field, then you must also specify `vCenter.datastore` and `vCenter.networkName`, and you must specify either `vCenter.cluster` or `vCenter.resourcePool`.

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

Optional  
Immutable  
String  
Default: Inherit from the admin cluster

The relative path of a [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html) that represents the ESXi hosts where your user cluster VMs will run. This vSphere cluster represents a subset of the physical ESXi hosts in your vCenter data center.

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

Optional  
Immutable  
String  
Default: Inherit from the admin cluster

A [vCenter resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) for your user cluster VMs.

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

The name of a [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) for your user cluster.

The value you specify must be a name, not a path. Do not include any folders in the value.

Example:
    
    
    vCenter:
      datastore: "my-uc-datastore"
    

### `vCenter.storagePolicyName`

Preview  
Optional  
String

The name of a [VM storage policy](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3F124146-E387-4613-8BCA-6F1375E2CA64.html) for the cluster nodes.

You can also specify a VM storage policy for the nodes in a particular node pool. But the policy specified here applies to any node pool that doesn't have its own policy.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy).

### `vCenter.caCertPath`

Optional  
Mutable  
String  
Default: Inherit from the admin cluster

The path of the CA certificate for your vCenter server. For more information, see [Getting your vCenter CA certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vcenter-ca-cert-path).

Example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert-2.pem"
    

For information on how to update this field, see [Update vCenter certificate references](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate).

### `vCenter.credentials.fileRef.path`

Optional  
Mutable  
String  
Default: Inherit from the admin cluster

If you provide a value for preparedSecrets.namespace, do not provide a value for this field. Instead, provide a value for vCenter.credentials.secretRef.version.

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account must have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements-basic).

You can use `gkectl update credentials` to update this field in an existing cluster. For more information, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

For information about updating your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-directory/my-credentials-2.yaml"
    

### `vCenter.credentials.fileRef.entry`

Optional  
Mutable  
String  
Default: Inherit from the admin cluster

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account.

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vcenter-credentials-2"
    

### `vCenter.credentials.secretRef.version`

Required if you provided a value for preparedSecrets.namespace  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

If you provide a value for preparedSecrets.namespace, fill in this field. Otherwise, remove this field or leave it commented out.

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds the username and password for the instance of vCenter Server that you intend to use for this user cluster.

Example:
    
    
    vCenter:
      credentials:
        secretRef:
          version: "1"
    

### `vCenter.folder`

Optional  
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

Optional  
Mutable  
String  
Default: Inherit from the admin cluster

The path of the JSON key file for your component access service account.

Example:
    
    
    componentAccessServiceAccountKeyPath: "my-key-folder/uc-access-key.json"
    

## `componentAccessServiceAccountKey.secretRef.version`

Optional  
Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your component access service account.

Example:
    
    
    componentAccessServiceAccountKey:
      secretRef:
        version: "1"
    

## `privateRegistry`

Fill in this section only if your admin cluster is using private registry and you want your user cluster to use a different private registry. Otherwise, remove this section or leave it commented out.

If you want to have some different settings from admin cluster settings:

  * Different username, password, certificate

  * (**Only available for Control Plane V2**) Different private registry address




Fill the `privateRegistry` fields here. The new settings are picked up during cluster creation and update.

### `privateRegistry.address`

Required for private registry  
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

Required for private registry  
Mutable  
String  
Default: Inherit from the admin cluster

If you are planning to use prepared secret for the private registry, do not provide a value for this field. Instead, provide a value for privateRegistry.credentials.secretRef.version.

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to access your private Docker registry.

Example:
    
    
    privateRegistry:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `privateRegistry.credentials.fileRef.entry`

Required for private registry  
Mutable  
String  
Default: Inherit from the admin cluster

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your private Docker registry account.
    
    
    privateRegistry:
      credentials:
        fileRef:
          entry: "private-registry-creds"
    

### `privateRegistry.credentials.secretRef.version`

Required if you want to use prepared secret for private registry  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

If you provide a value for preparedSecrets.namespace and want to use prepared secret for private registry, fill in this field. Otherwise, remove this field or leave it commented out.

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds the username and password for the instance of vCenter Server that you intend to use for this user cluster.

Example:
    
    
    privateRegistry:
      credentials:
        secretRef:
          version: "1"
    

### `privateRegistry.caCertPath`

Required for private registry  
Mutable  
String  
Default: Inherit from the admin cluster

When Docker pulls an image from your private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). Docker uses the CA's certificate to validate the registry's certificate.

Set this field to the path of the CA's certificate.

Example:
    
    
    privateRegistry:
      caCertPath: "my-cert-folder/registry-ca.crt"
    

## `network`

This section holds information about your user cluster network.

### `network.hostConfig`

This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes. If you are using the Seesaw load balancer, this information also applies to your Seesaw VMs.

This section is required if one or more of the following are true:

  * `network.ipMode.type` is set to `static`
  * `enableControlplaneV2` is set to `true` or allowed to default to `true`.
  * `loadBalancer.kind` is set to `"Seesaw"`



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

Optional  
Immutable  
Array of strings

DNS search domains for the hosts to use. These domains are used as part of a domain search list.

Example:
    
    
    network:
      hostConfig:
        searchDomainsForDNS:
        - "my.local.com"
    

### `network.ipMode.type`

Required  
Immutable  
String  
Prepopulated: "dhcp"  
Default: "dhcp"

If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`.

Example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

Required if `network.ipMode.type` = `static`  
Immutable  
String

The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your cluster.

Example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/user-cluster-ipblock.yaml"
    

### `network.serviceCIDR`

Required  
Immutable  
String  
Prepopulated: "10.96.0.0/20"  


A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range.

Example:
    
    
    network:
      serviceCIDR: "10.96.0.0/20"
    

### `network.podCIDR`

Required  
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

Required if `vCenter.address` is different from the vCenter address you are are using for the admin cluster.  
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

The path of an IP block file that holds IP addresses to be used for this network interface on the nodes that have this network interface.

Example:
    
    
    network:
      additionalNodeInterfaces:
      - name: "my-node-interface-1"
        type: "static"
        ipBlockFilePath: "my-ipblock-file-1"
    

### `network.controlPlaneIPBlock`

If you set `enableControlplaneV2` to `true`, fill in this section. Otherwise, remove this section or leave it commented out.

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
Array of objects, each of which has an IP address and an optional hostname.

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

This section holds information about the load balancer for your user cluster.

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

Required  
Immutable  
String

The IP address that you have chosen to configure on the load balancer for the ingress proxy.

Example:
    
    
    loadBalancer:
      vips:
        ingressVIP: "203.0.113.4"
    

### `loadBalancer.kind`

Required  
Immutable  
String  
Prepopulated: "MetalLB"

Set this to `"ManualLB"`, `"F5BigIP"`, `"Seesaw"`, or `"MetalLB"`.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"manualLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.manualLB.ingressHTTPNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable  
Integer  
Prepopulated: 30243

The ingress proxy in a user cluster is exposed by a [Kubernetes Services of type `LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer). The Service has a [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) for HTTP. You must choose a `nodePort` value for the HTTP ServicePort.

Set this field to the `nodePort` value.

Example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPNodePort: 32527
    

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable  
Integer  
Prepopulated: 30879

The ingress proxy in a user cluster is exposed by a Service of type LoadBalancer. The Service has a ServicePort for HTTPS. You must choose a `nodePort` value for the HTTPS ServicePort.

Set this field to the `nodePort` value. Example:
    
    
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
    

#### `loadBalancer.manualLB.addonsNodePort`

Remove this field. It is not used in a user cluster.

### `loadBalancer.f5BigIP`

If you set `loadbalancer.kind` to `"f5BigIP"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.f5BigIP.address`

Required if `loadBalancer.kind` = `"f5BigIP"`  
String

The address of your F5 BIG-IP load balancer.

Example:
    
    
    loadBalancer:
      f5BigIP:
          address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.path`

Required if `loadBalancer.kind` = `"f5BigIP"`  
String

The path of a [credentials file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

For information about updating your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: ""my-config-folder/user-creds.yaml"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.entry`

Required if `loadBalancer.kind` = `"f5BigIP"`  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

Required if `loadBalancer.kind` = `"f5BigIP"`  
String

The name of a BIG-IP partition that you created for your user cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-user-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

Required if `loadBalancer.kind` = `"f5BigIP"` and you are using SNAT  
String

The name of your SNAT pool.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

If you set `loadbalancer.kind` to `"Seesaw"`, fill in this section. Otherwise, remove this section or leave it commented out.

Note the following limitations:

  * If a [high-availability admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#adminmaster-replicas-field) manages this user cluster, then this user cluster can't use the Seesaw load balancer.
  * User clusters with Controlplane V2 enabled can't use the Seesaw load balancer.



For information on setting up the Seesaw load balancer, see [Seesaw load balancer quickstart](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/seesaw-load-balance-quickstart) and [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance).

#### `loadBalancer.seesaw.ipBlockFilePath`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/user-seesaw-ipblock.yaml"
    

#### `loadBalancer.seesaw.vrid`

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

Required if `loadBalancer.kind` = `Seesaw`  
Immutable  
String

The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1).

Example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

#### `loadBalancer.seesaw.cpus`

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

Required if `loadBalancer.kind` = `Seesaw`  
Mutable  
Integer  
Prepopulated: 3072  


The number of mebibytes of memory for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

**Note** : This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

#### `loadBalancer.seesaw.vCenter.networkName`

Optional  
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

Optional  
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

Optional  
Immutable  
Relevant if `loadBalancer.kind` = `Seesaw`  
Boolean  
Prepopulated: true  
Default: true

If you set this to `true`, the Seesaw load balancer does not use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. We recommend that you set this to `true`. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`.

Example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

### `loadBalancer.metalLB`

If you set `loadbalancer.kind` to `"MetalLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

#### `loadBalancer.metalLB.addressPools`

Required if `loadBalancer.kind` = 'MetalLB`  
Mutable  


Array of objects, each of which holds information about an address pool to be used by the MetalLB load balancer.

##### `loadBalancer.metalLB.addressPools[i].name`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable  
String

A name of your choice for the address pool.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
    

##### `loadBalancer.metalLB.addressPools[i].addresses`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable  


Array of strings, each of which is a range of addresses. Each range must be in CIDR format or hyphenated range format.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
          addresses:
          - "192.0.2.0/26"
          - "192.0.2.64-192.0.2.72"
    

##### `loadBalancer.metalLB.addressPools[i].avoidBuggyIPs`

Optional  
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

Optional  
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

Optional  
Immutable  
Boolean  
Prepopulated: true  
Default: false

If you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2), or if you want to use [Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2), set this to `true`. Otherwise set this to `false`.

Example:
    
    
    enableDataplaneV2: true
    

See [Dataplane V2 Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting) for troubleshooting steps.

## `multipleNetworkInterfaces`

Optional  
Immutable  
Boolean  
Prepopulated: false  
Default: false

If you want to enable multiple network interfaces for Pods, set this to `true`. Otherwise set this to `false`.

For more information, see [Configure multiple network interfaces for Pods](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multi-nic).

Example:
    
    
    multipleNetworkInterfaces: true
    

## `advancedNetworking`

Optional  
Immutable  
boolean  
Prepopulated: false  
Default: false

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/egress-nat-gateway), set this to `true`. Otherwise set it to `false`.

If you set this field to `true`, you must also set `enableDataplaneV2` to `true`.

Example:
    
    
    advancedNetworking: true
    

## `storage.vSphereCSIDisabled`

If you want to disable the deployment of vSphere CSI components, set this to `true`. Otherwise, set it to `false`.

Optional  
Mutable  
Boolean  
Prepopulated: false  
Default: false

Example:
    
    
    storage:
      vSphereCSIDisabled: false
    

## `masterNode`

This section holds information about the nodes that serve as control-plane nodes for this user cluster.

### `masterNode.cpus`

Optional  
Mutable  
Integer  
Prepopulated: 4  
Default: 4

The number of CPUs for each node that serves as a control plane for this user cluster.

Example:
    
    
    masterNode:
      cpus: 8
    

### `masterNode.memoryMB`

Optional  
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

Optional  
Immutable  
Integer  
Possible values: 1 or 3  
Prepopulated: 1  
Default: 1

The number of control-plane nodes for this user cluster. This number cannot be changed once you have created the cluster. If you want to update the number of replicas later, you must recreate the user cluster.

Example:
    
    
    masterNode:
      replicas: 3
    

### `masterNode.autoResize.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to enable automatic resizing of the control-plane nodes for the user cluster. Otherwise, set this to `false`.

For more information, see [Enable node resizing for the control-plane nodes of a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize#enable_node_resizing_for_the_control-plane_nodes_of_a_user_cluster).

Example:
    
    
    masterNode:
      autoResize:
        enabled: true
    

### `masterNode.vsphere.datastore`

Optional  
Immutable  
String  
Default: The value of `vCenter.datastore`

The datastore where the control-plane nodes for this user cluster will be created.

Example:
    
    
    masterNode:
      vSphere:
        datastore: "control-plane-datastore"
    

If you specify a value for this field, do not specify a value for `masterNode.vsphere.storagePolicyName`.

### `masterNode.vsphere.storagePolicyName`

Optional  
Immutable  
String  
Default: The value of `vCenter.storagePolicyName`

The name of a [VM storage policy](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3F124146-E387-4613-8BCA-6F1375E2CA64.html) for the control-plane nodes.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy).

Example:
    
    
    masterNode:
      vSphere:
        storagePolicyName: "control-plane-storage-policy"
    

If you specify a value for this field, do not specify a value for `masterNode.vsphere.datastore`.

## `nodePools`

Required  
Mutable  
Array of objects, each of which describes a node pool.

For more information, see [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools).

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

When you upgrade a user cluster, you can specify that selected node pools remain at the previous version.

If you want this node pool to remain at the previous version, set this to the previous version. Otherwise, remove this field or set it to the empty string. For more information, see [Upgrade node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrade-node-pools).

Preview  
Optional  
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

Optional  
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

Optional  
Mutable  
String  
Possible values: "ubuntu_containerd", "cos", "windows"  
Prepopulated: "ubuntu_containerd"  
Default: "ubuntu_containerd"

The type of OS image to run on the VMs in the node pool.

Example:
    
    
    nodePools
    - name: "my-node-pool"
      osImageType: "ubuntu_containerd"
    

### `nodePools[i].osImage`

Required if `nodePools[i].osImageType` = `windows`  
Mutable  
String  


The name of a Windows VM template. The template must be based on a Windows Server 2019 ISO that has the en-US language/region tag.

For more information, see [User guide for Windows Server OS node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-guide-for-windows-server-os-node-pools).

### `nodePools[i].labels`

Optional  
Mutable  
Mapping

Labels to apply to each Kubernetes Node object in the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      labels:
        environment: "production"
        tier: "cache"
    

### `nodePools[i].taints`

Optional  
Mutable  
Array of objects, each of which describes a [Kubernetes taint](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-taints) that is applied to each node in the pool. Taints are key-value pairs associated with an `effect`. Taints are used with tolerations for Pod scheduling. Specify one of the following for the `effect`: `NoSchedule`, `PreferNoSchedule`, `NoExecute`.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      taints:
      - key: "staging"
        value: "true"
        effect: "NoSchedule"
    

### `nodePools[i].vsphere.datastore`

Optional  
Mutable  
String  
Default: The value of `vCenter.datastore`

The name of the vCenter datastore where the nodes will be created.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        datastore: "my-datastore"
    

### `nodePools[i].vsphere.storagePolicyName`

Optional  
Mutable  
String  
Default: The value of `vCenter.storagePolicyName`

The name of a [VM storage policy](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3F124146-E387-4613-8BCA-6F1375E2CA64.html) for the nodes in the pool.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy).

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        storagePolicyName: "my-storage-policy"
    

### `nodePools[i].vsphere.tags`

Optional  
Mutable  
Array of objects, each of which describes a [vSphere tag](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html) to be placed on the VMs in the node pool.

Each tag has a category and a name.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        tags:
        - category: "purpose"
          name: "testing"
    

If you want to attach tags to all VMs in a node pool, your vCenter user account must have these [vSphere tagging privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-2F8C5B02-7EF6-428A-BDB6-B2CC3D307097.html):

  * vSphere Tagging.Assign or Unassign vSphere Tag
  * vSphere Tagging.Assign or Unassign vSphere Tag on Object (vSphere 7)



### `nodePools[i].vsphere.hostgroups`

Fill in this section if you want to configure your cluster to use [VM-Host affinity](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-vm-host-affinity).

Optional  
Mutable   
Array of strings, each of which is the name of a [host DRS group](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-D89CEBB5-5C43-4FAC-83D1-E7CB576FF86D.html).

The array can have only one element.

### `nodePools[i].vsphere.hostgroups[j].hostgroup`

Optional  
Mutable  
String

The name of an existing [host DRS group](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-D89CEBB5-5C43-4FAC-83D1-E7CB576FF86D.html)
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        hostgroups:
        - "my-hostgroup"
    

### `nodePools[i].autoscaling`

Optional  
Mutable  


If you want to enable automatic scaling for the node pool, fill in this section. Otherwise, remove this section or leave it commented out.

#### `nodePools[i].autoscaling.minReplicas`

Optional  
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

Optional  
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

Optional  
Relevant if `loadBalancer.kind` = `"MetalLB"`  
Mutable  
Boolean  
Prepopulated: true  
Default: false

Set this to `true` if you want to allow the MetalLB speaker to run on the nodes in the pool. Otherwise, set it to `false`.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      enableLoadBalancer: true
    

## `antiAffinityGroups.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`.

Example:
    
    
    antiAffinityGroups:
      enabled: true
    

If this field is `true` Google Distributed Cloud creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster's nodes, causing them to be spread across at least three physical ESXi hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least four ESXi hosts available.




Even though the rule requires that the cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available.

Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least four hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

## `enableVMTracking`

Preview  
Optional  
Immutable  
Prepopulated: false

Set this to `true` to enable VM tracking with vSphere tags. Otherwise, set it to `false`.

For more information, see [Enable VM tracking](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vm-track-tags).

Example:
    
    
    enableVMTracking: true
    

## `nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate`

Optional  
Integer  
Possible values: 0 or 1 Prepopulated: 0

The number of node pools to update at a time. A value of `1` specifies that one node pool can be updated at a time. A value of `0` specifies that an unlimited number of node pools can be updated at a time.

Example:
    
    
    nodePoolUpdatePolicy:
      maximumConcurrentNodePoolUpdate: 1
    

## `authentication`

This section holds information about how cluster users are authenticated and authorized.

### `authentication.oidc`

Do not use this section. Instead, after cluster creation, edit the ClientConfig custom resource as described in [Configuring clusters for Anthos Identity Service with OIDC ](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

### `authentication.sni`

Optional  


If you want to provide an additional serving certificate for the cluster's Kubernetes API server, fill in this section. Otherwise, remove this section or leave it commented out.

#### `authentication.sni.certPath`

Optional  
String

The path of a serving certificate for the Kubernetes API server.

Example:
    
    
    authentication:
      sni:
        certPath: "my-cert-folder/example.com.crt"
    

#### `authentication.sni.keyPath`

Optional  
String

The path of the certificate's private key file.

Example:
    
    
    authentication:
      sni:
        keyPath: "my-cert-folder/example.com.key"
    

## `gkeConnect`

Required  
Immutable  


This section holds information about the Google Cloud project and service account you want to use to [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet.

### `gkeConnect.projectID`

Required  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#fleet_host_project).

Example:
    
    
    gkeConnect:
      projectID: "my-fleet-host-project"
    

### `gkeConnect.registerServiceAccountKeyPath`

Required  
Mutable  
String

The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#connect_register_service_account).

To update the value of this field, use `gkectl update cluster`.

For information about changing your connect-register service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

### `gkeConnect.registerServiceAccountKey.secretRef.version`

Required if using [prepared credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials)  
Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your connect-register service account.

Example:
    
    
    gkeConnect:
      registerServiceAccountKey:
        secretRef:
          version: "1"
    

## `gkeOnPremAPI`

Optional  
Available in 1.15.3 or higher.

Include this section if you want to enroll the user cluster in the GKE On-Prem API.

Enrolling your user cluster in the GKE On-Prem API lets you use the Google Cloud console or the Google Cloud CLI to view cluster details and to manage the cluster lifecycle. For example, you run can `gcloud` commands to [get information about your user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster#get_cluster_information).

The GKE On-Prem API stores cluster state metadata in Google Cloud. This metadata lets the standard tools—the console, the gcloud CLI, and [Terraform](https://www.terraform.io/)—use the GKE On-Prem API to manage the user cluster lifecycle, and collectively these tools are referred to as the _GKE On-Prem API clients_. If you prefer to use a standard tool to create the user cluster, see [Create a user cluster using GKE On-Prem API clients](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api). When you create a user cluster using an GKE On-Prem API client, the cluster is automatically enrolled in the GKE On-Prem API.

If you set `gkeOnPremAPI.enabled` to `true`, before creating or updating the cluster using `gkectl`, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster#before_you_begin) to enable and initialize the GKE On-Prem API.

After you add this section and create or update the cluster, if subsequently you remove the section and update the cluster, the update will fail.

### `gkeOnPremAPI.enabled`

Required if the `gkeOnPremAPI` section is included.  
Mutable  
Boolean  
Prepopulated: true

Set to `true` if you want to enroll the cluster in the GKE On-Prem API. After the cluster is enrolled in the GKE On-Prem API, if you need to unenroll the cluster, make the following change and then update the cluster:
    
    
    gkeOnPremAPI:
      enabled: false
    

### `gkeOnPremAPI.location`

Required if the `gkeOnPremAPI` section is included.  
Immutable  
String  
Prepopulated: "us-central1"

The Google Cloud region where the GKE On-Prem API runs and stores cluster metadata. Choose one of the [supported regions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/supported-regions-on-prem-api). We recommend that you use the same region that is configured in `stackdriver.clusterLocation`. Must be a non-empty string if `gkeOnPremAPI.enabled` is `true`. If `gkeOnPremAPI.enabled` is `false`, don't include this field.

## `stackdriver`

Required by default  
Mutable  


If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring) for your cluster, fill in this section. Otherwise remove this section or leave it commented out.

This section is required by default. That is, if you don't include this section, you must include the `--skip-validation-stackdriver` flag when you run `gkectl create cluster`.

This section is required in the user cluster if you want to manage the lifecycle of the [user clusters in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api).

### `stackdriver.projectID`

Required for Logging and Monitoring  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#fleet_host__project).

Example:
    
    
    stackdriver:
      projectID: "my-fleet-host-project"
    

### `stackdriver.clusterLocation`

Required for Logging and Monitoring  
Immutable  
String  
Prepopulated: "us-central1"

The Google Cloud region where you want to store logs. It is a good idea to choose a region that is near your on-premises data center.

Example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.enableVPC`

Optional  
Immutable  
Boolean  
Prepopulated: false

If your cluster's network is controlled by a [VPC](https://docs.cloud.google.com/vpc), set this to `true`. This ensures that all telemetry flows through Google's restricted IP addresses. Otherwise, set this to `false`.

Example:
    
    
    stackdriver:
      enableVPC: false
    

### `stackdriver.serviceAccountKeyPath`

Required for Logging and Monitoring  
Mutable  
String

The path of the JSON key file for your logging-monitoring service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your logging-monitoring service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Example:
    
    
    stackdriver:
      serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
    

### `stackdriver.serviceAccountKey.secretRef.version`

Required if using [prepared credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials)  
Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your logging monitoring service account.

Example:
    
    
    stackdriver:
      serviceAccountKey:
        secretRef:
          version: "1"
    

### `stackdriver.disableVsphereResourceMetrics`

Optional  
Mutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to disable the collection of metrics from vSphere. Otherwise, set it to `false`.

Example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `usageMetering`

Preview  
Immutable  
Optional

If you want to enable usage metering for your cluster, then fill in this section. Otherwise, remove this section or leave it commented out.

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

For information about changing your BigQuery service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Example:
    
    
    usageMetering:
      bigQueryServiceAccountKeyPath: "my-key-folder/bq-key.json"
    

### `usageMetering.bigQueryServiceAccountKey.secretRef.version`

Required if using [prepared credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials)  
Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your BigQuery service account.

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

The ID of your fleet host project.

Example:
    
    
    cloudAuditLogging:
      projectID: "my-fleet-host-project"
    

### `cloudAuditLogging.clusterLocation`

Required for Cloud Audit Logs  
Immutable  
String

The Google Cloud region where you want to store audit logs. It is a good idea to choose a region that is near your on-premises data center

Example:
    
    
    cloudAuditLogging:
      clusterLocation: "us-central1"
    

### `cloudAuditLogging.serviceAccountKeyPath`

Required for Cloud Audit Logs  
Mutable  
String

The path of the JSON key file for your audit-logging service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your audit-logging service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

### `cloudAuditLogging.serviceAccountKey.secretRef.version`

Optional  
Mutable  
String  
Possible values: An integer string or "latest"  
Default value: "latest"

The version of a [prepared Secret](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) in the admin cluster that holds a JSON key for your audit logging service account.

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

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        keyVersion: 1
    

### `secretsEncryption.generatedKey.disabled`

Optional for Secrets encryption  
Mutable  
Boolean  
Prepopulated: false

Set this to `true` to disable Secrets encryption. Otherwise set it to `false`.

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        disabled: false
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
