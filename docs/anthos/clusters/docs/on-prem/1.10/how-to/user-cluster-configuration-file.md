---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-configuration-file/
title: User cluster configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:55.490113+00:00
---

# User cluster configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-configuration-file/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  User cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

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
    # # (Optional) vCenter configuration (default: inherit from the admin cluster)
    # vCenter:
    #   datacenter: ""
    #   cluster: ""
    #   # Resource pool to use. Specify [VSPHERE_CLUSTER_NAME]/Resources to use the default
    #   # resource pool
    #   resourcePool: ""
    #   datastore: ""
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
    #   # (Optional) vSphere folder where cluster VMs will be located. Defaults to the the
    #   # datacenter wide folder if unspecified.
    #   folder: ""
    # (Required) Network configuration; vCenter section is optional and inherits from
    # the admin cluster if not specified
    network:
      # # (Optional) This section overrides ipBlockFile values. Use with ipType "static" mode.
      # # Used for seesaw nodes as well
      # hostConfig:
      #   # List of DNS servers
      #   dnsServers:
      #   - ""
      #   # List of NTP servers
      #   ntpServers:
      #   - ""
      #   # # List of DNS search domains
      #   # searchDomainsForDNS:
      #   # - ""
      ipMode:
        # (Required) Define what IP mode to use ("dhcp" "static" or "none"(multinic only))
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
      #   # (Required) Define what IP mode to use ("dhcp" "static" or "none"(multinic only))
      #   type: dhcp
      #   # # (Required when using "static" mode) The absolute or relative path to the yaml file
      #   # # to use for static IP allocation. Hostconfig part will be overwritten by network.hostconfig
      #   # # if specified
      #   # ipBlockFilePath: ""
    # (Required) Load balancer configuration
    loadBalancer:
      # (Required) The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlPlaneVIP: ""
        # Shared by all services for ingress traffic
        ingressVIP: ""
      # (Required) Which load balancer to use "F5BigIP" "Seesaw" "ManualLB" or "MetalLB"(Preview).
      # Uncomment the corresponding field below to provide the detailed spec
      kind: Seesaw
      # # (Required when using "ManualLB" kind) Specify pre-defined nodeports
      # manualLB:
      #   # NodePort for ingress service's http (only needed for user cluster)
      #   ingressHTTPNodePort: 30243
      #   # NodePort for ingress service's https (only needed for user cluster)
      #   ingressHTTPSNodePort: 30879
      #   # NodePort for konnectivity server service (only needed for user cluster)
      #   konnectivityServerNodePort: 30563
      #   # NodePort for control plane service
      #   controlPlaneNodePort: 30562
      #   # NodePort for addon service (only needed for admin cluster)
      #   addonsNodePort: 0
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
      #   partition: ""
      #   # # (Optional) Specify a pool name if using SNAT
      #   # snatPoolName: ""
      # (Required when using "Seesaw" kind) Specify the Seesaw configs
      seesaw:
        # (Required) The absolute or relative path to the yaml file to use for IP allocation
        # for LB VMs. Must contain one or two IPs. Hostconfig part will be overwritten
        # by network.hostconfig if specified.
        ipBlockFilePath: ""
        # (Required) The Virtual Router IDentifier of VRRP for the Seesaw group. Must
        # be between 1-255 and unique in a VLAN.
        vrid: 0
        # (Required) The IP announced by the master of Seesaw group
        masterIP: ""
        # (Required) The number CPUs per machine
        cpus: 4
        # (Required) Memory size in MB per machine
        memoryMB: 3072
        # (Optional) Network that the LB interface of Seesaw runs in (default: cluster
        # network)
        vCenter:
          # vSphere network name
          networkName: ""
        # (Optional) Run two LB VMs to achieve high availability (default: false)
        enableHA: false
        # (Optional) Avoid using VRRP MAC and rely on gratuitous ARP to do failover. In
        # this mode MAC learning is not needed but the gateway must refresh arp table
        # based on gratuitous ARP. It's recommended to turn this on to avoid MAC learning
        # configuration. In vsphere 7+ it must be true to enable HA. It is supported in
        # GKE on-prem version 1.7+. (default: false)
        disableVRRPMAC: true
      # # (Required when using "MetalLB" kind in user clusters) Specify the MetalLB configs
      # metalLB:
      #   # (Required) A list of non-overlapping IP pools used by load balancer typed services.
      #   # Must include ingressVIP of the cluster.
      #   addressPools:
      #   # (Required) Name of the address pool
      #   - name: ""
      #     # (Required) The addresses that are part of this pool. Each address must be either
      #     # in the CIDR form (1.2.3.0/24) or range form (1.2.3.1-1.2.3.5).
      #     addresses:
      #     - ""
      #     # # (Optional) Avoid using IPs ending in .0 or .255. This avoids buggy consumer devices
      #     # # mistakenly dropping IPv4 traffic for those special IP addresses (default: false)
      #     # avoidBuggyIPs: false
      #     # # (Optional) Prevent IP addresses to be automatically assigned from this pool (default:
      #     # # false)
      #     # manualAssign: false
    # # (Optional) Enable dataplane v2
    # enableDataplaneV2: false
    # # (Optional) Enable support for multiple networking interfaces
    # multipleNetworkInterfaces: false
    # # (Optional) Enable advanced dataplane v2 networking features such as Egress NAT Gateway
    # # and it requires enableDataplaneV2 to be set
    # advancedNetworking: false
    # # (Optional) Storage specification for the cluster
    # storage:
    #   # Whether to disable vSphere CSI components deployment. The feature is enabled by
    #   # default.
    #   vSphereCSIDisabled: false
    # (Optional) User cluster master nodes must have either 1 or 3 replicas (default:
    # 4 CPUs; 16384 MB memory; 1 replica)
    masterNode:
      cpus: 4
      memoryMB: 8192
      # How many machines of this type to deploy
      replicas: 1
      # # (Optional/Preview) Enable auto resizing on master
      # autoResize:
      #   # Whether to enable auto resize for master. Defaults to false.
      #   enabled: false
      # vsphere:
      #   # (Optional) vSphere datastore the master nodes will be created on (default: vCenter.datastore)
      #   datastore: ""
    # (Required) List of node pools. The total un-tainted replicas across all node pools
    # must be greater than or equal to 3
    nodePools:
    - name: pool-1
      cpus: 4
      memoryMB: 8192
      # How many machines of this type to deploy
      replicas: 3
      # # (Optional) boot disk size; must be at least 40 (default: 40)
      # bootDiskSizeGB: 40
      # (Optional) Specify the type of OS image; available options can be set to "ubuntu"
      # "ubuntu_containerd" or "cos". Default is "ubuntu_containerd".
      osImageType: ubuntu_containerd
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
      #   # (Optional) vSphere tags to be attached to the virtual machines in the node pool.
      #   # It is supported in GKE on-prem version 1.7+
      #   tags:
      #   - category: ""
      #     name: ""
      # # (Optional/Preview) Horizontal autoscaling for the nodepool; replicas should not
      # # be edited while updating the nodepool if this is turned on
      # autoscaling:
      #   # min number of replicas in the NodePool
      #   minReplicas: 0
      #   # max number of replicas in the NodePool
      #   maxReplicas: 0
      # # (Optional/Preview) Allow traffic of LoadBalancer typed services flow through nodes
      # # of this pool. Can only be true in MetalLB mode. Default is false.
      # enableLoadBalancer: false
    # Spread nodes across at least three physical hosts (requires at least three hosts)
    antiAffinityGroups:
      # Set to false to disable DRS rule creation
      enabled: true
    # # (Optional/Preview) Track user cluster VMs with vSphere tags
    # enableVMTracking: false
    # # (Optional) Configure additional authentication.
    # # Please note that OIDC and LDAP configuration will be removed starting in Anthos
    # # 1.10.
    # # Please refer to https://cloud.google.com/anthos/gke/docs/on-prem/1.6/how-to/oidc#oidc_spec
    # # for dynamic configuration changes after cluster creation.
    # authentication:
    #   # (Optional) Configure OIDC authentication
    #   oidc:
    #     # URL for OIDC Provider.
    #     issuerURL: ""
    #     # (Optional) Default is http://kubectl.redirect.invalid
    #     kubectlRedirectURL: ""
    #     # ID for OIDC client application.
    #     clientID: ""
    #     # (Optional) Secret for OIDC client application.
    #     clientSecret: ""
    #     # (Optional) JWT claim to use as the username.
    #     username: ""
    #     # (Optional) Prefix prepended to username claims.
    #     usernamePrefix: ""
    #     # (Optional) JWT claim to use as group name.
    #     group: ""
    #     # (Optional) Prefix prepended to group claims.
    #     groupPrefix: ""
    #     # (Optional) Additional scopes to send to OIDC provider as comma separated list.
    #     # Default is "openid".
    #     scopes: ""
    #     # (Optional) Additional key-value parameters to send to OIDC provider as comma
    #     # separated list.
    #     extraParams: ""
    #     # (Optional) Set value to string "true" or "false". Default is false.
    #     deployCloudConsoleProxy: ""
    #     # # (Optional) The absolute or relative path to the CA file
    #     # caPath: ""
    #   # (Optional) Provide an additional serving certificate for the API server
    #   sni:
    #     certPath: ""
    #     keyPath: ""
    # (Required) Specify which GCP project to connect your GKE clusters to
    gkeConnect:
      projectID: ""
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerServiceAccountKeyPath: ""
    # (Optional) Specify which GCP project to connect your logs and metrics to
    stackdriver:
      projectID: ""
      # A GCP region where you would like to store logs and metrics for this cluster.
      clusterLocation: us-central1
      enableVPC: false
      # The absolute or relative path to the key file for a GCP service account used to
      # send logs and metrics from the cluster
      serviceAccountKeyPath: ""
      # (Optional) Disable vsphere resource metrics collection from vcenter.  False by
      # default
      disableVsphereResourceMetrics: false
    # # (Optional/Alpha) Configure the GKE usage metering feature
    # usageMetering:
    #   bigQueryProjectID: ""
    #   # The ID of the BigQuery Dataset in which the usage metering data will be stored
    #   bigQueryDatasetID: ""
    #   # The absolute or relative path to the key file for a GCP service account used by
    #   # gke-usage-metering to report to BigQuery
    #   bigQueryServiceAccountKeyPath: ""
    #   # Whether or not to enable consumption-based metering
    #   enableConsumptionMetering: false
    # # (Optional/Preview) Configure kubernetes apiserver audit logging
    # cloudAuditLogging:
    #   projectID: ""
    #   # A GCP region where you would like to store audit logs for this cluster.
    #   clusterLocation: ""
    #   # The absolute or relative path to the key file for a GCP service account used to
    #   # send audit logs from the cluster
    #   serviceAccountKeyPath: ""
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
Immutable string

A name of your choice for your user cluster. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



Example:
    
    
    name: "my-user-cluster"
    

## `gkeOnPremVersion`

Required  
Mutable string

The Google Distributed Cloud version for your user cluster.

Example:
    
    
    gkeOnPremVersion: "1.10.0-gke.1"
    

## `vCenter`

This section holds information about your vSphere environment and your connection to vCenter Server.

If you want a field in this section to be the same as what you specified for your admin cluster, remove the field or leave it commented out.

If you want a field to be different from what you specified for your admin cluster, fill it in here. Any fields that you fill in here in the `vCenter` section override the corresponding fields in your admin cluster configuration file.

### `vCenter.datacenter`

Immutable string  
Default: Inherit from the admin cluster

The name of a [vCenter data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html) that has the physical ESXi hosts where your user cluster VMs will run.

Example:
    
    
    vCenter:
      datacenter: "my-datacenter-2"
    

If specified, then you must also specify `vCenter.datastore` and `vCenter.networkName`, and you must specify either `vCenter.cluster` or `vCenter.resourcePool`. See [Create a user cluster in a separate data center](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-user-cluster-in-separate-datacenter).

### `vCenter.cluster`

Immutable string  
Default: Inherit from the admin cluster

The name of a [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html) that has the ESXi hosts where your user cluster VMs will run. This vSphere cluster is a set of physical ESXi hosts that form a subset of the physical ESXi hosts in your vCenter data center.

Example:
    
    
    vCenter:
      cluster: "my-vsphere-cluster-2"
    

### `vCenter.resourcePool`

Immutable string  
Default: Inherit from the admin cluster

The name of a [vCenter resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) for your user cluster VMs.

Example:
    
    
    vCenter:
      resourcePool: "my-resource-pool-2"
    

To use the default resource pool, set this to VSPHERE_CLUSTER/Resources.

Example:
    
    
    vCenter:
      resourcePool: "my-vsphere-cluster-2/Resources"
    

For more information, see [Specifying the root resource pool for a standalone host](https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs/data-sources/resource_pool).

### `vCenter.datastore`

Immutable string  
Default: Inherit from the admin cluster

The name of a [vCenter datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) for your user cluster VMs.

Example:
    
    
    vCenter:
      datastore: "my-datastore-2"
    

### `vCenter.caCertPath`

Mutable string  
Default: Inherit from the admin cluster

The path of the CA certificate for your vCenter server. For more information, see [Getting your vCenter CA certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/vcenter-ca-cert-path).

Example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert-2.pem"
    

For information on how to update this field, see [Update vCenter certificate references](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/update-vcenter-certificate).

### `vCenter.credentials.fileRef.path`

Mutable string  
Default: Inherit from the admin cluster

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account must have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/vsphere-requirements-basic).

You can use `gkectl update credentials` to update this field in an existing cluster. For more information, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/rotating-service-account-keys).

For information about updating your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-directory/my-credentials-2.yaml"
    

### `vCenter.credentials.fileRef.entry`

Mutable string  
Default: Inherit from the admin cluster

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account.

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vcenter-credentials-2"
    

### `vCenter.folder`

Immutable string  
Default: Inherit from the admin cluster

The name of a vCenter folder where your cluster VMs will be located.

Example:
    
    
    vCenter:
      folder: "my-folder-2"
    

## `network`

This section holds information about your user cluster network.

### `network.hostConfig`

This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes. If you are using the Seesaw load balancer, this information also applies to your Seesaw VMs.

**Important:** If you include `network.hostConfig` in the admin cluster configuration file, then the entire `hostconfig` section of the [`ipBlockfile`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) will be ignored.

#### `network.hostConfig.dnsServers`

Optional  
Immutable array of strings

The addresses of DNS servers for the VMs.

Example:
    
    
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
    

#### `network.hostConfig.ntpServers`

Optional  
Immutable array of strings

The addresses of time servers for the VMs to use.

Example:
    
    
    network:
      hostConfig:
        ntpServers:
        - "216.239.35.0"
    

#### `network.hostConfig.searchDomainsForDNS`

Optional  
Immutable array of strings

DNS search domains for the hosts to use. These domains are used as part of a domain search list.

Example:
    
    
    network:
      hostConfig:
        searchDomainsForDNS:
        - "my.local.com"
    

### `network.ipMode.type`

Required  
Immutable string  
Prepopulated: "dhcp"  
Default: "dhcp"

If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`.

Example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

Required if `network.ipMode.type` = `static`  
Immutable string

The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) for your cluster.

Example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/user-cluster-ipblock.yaml"
    

### `network.serviceCIDR`

Required  
Immutable string  
Prepopulated: "10.96.0.0/20"  


A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range.

Example:
    
    
    network:
      serviceCIDR: "10.96.0.0/20"
    

### `network.podCIDR`

Required  
Immutable string  
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

Required  
Immutable string

The name of the vSphere network for your user cluster nodes.

If the name contains a special character, you must use an escape sequence for it.

Special characters | Escape sequence  
---|---  
Slash (`/`) | `%2f`  
Backslash (`\`) | `%5c`  
Percent sign (`%`) | `%25`  
  
If the network name is not unique, you can specify a path to the network, such as `/datacenter-2/network/my-network`.

For example:
    
    
    network:
      vCenter:
        networkName: "my-user-cluster-network"
    

### `network.vCenter.additionalNodeInterfaces`

If you set `multipleNetworkInterfaces` to `true`, fill in this section. Otherwise, remove this section or leave it commented out.

An array of objects, each of which describes a network interface that can be used on all or some of your cluster nodes.

#### `network.vCenter.additionalNodeInterfaces[i].networkName`

Required if `multipleNetworkInterfaces` = `true`  
Immutable string

The name of the vSphere network that this additional node interface will connect to.

Example:
    
    
    network:
      vCenter:
        additionalNodeInterfaces:
        - networkName: "my-node-interface-1"
    

#### `network.vCenter.additionalNodeInterfaces[i].type`

Required if `multipleNetworkInterfaces` = `true`  
Immutable string

Example:
    
    
    network:
      vCenter:
        additionalNodeInterfaces:
        - name: "my-node-interface-1"
          type: "static"
    

#### `network.vCenter.additionalNodeInterfaces[i].ipBlockFilePath`

Required if `network.vCenter.additionalNodeInterfaces[i].type` = `static`  
Immutable string

The path of an IP block file that holds IP addresses to be used for this network interface on the nodes that have this network interface.

Example:
    
    
    network:
      vCenter:
        additionalNodeInterfaces:
        - name: "my-node-interface-1"
          type: "static"
          ipBlockFilePath: "my-ipblock-file-1"
    

## `loadBalancer`

This section holds information about the load balancer for your user cluster.

### `loadBalancer.vips.controlPlaneVIP`

Required  
Immutable string

The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster.

Example:
    
    
    loadBalancer:
      vips:
        controlplaneVIP: "203.0.113.3"
    

### `loadBalancer.vips.ingressVIP`

Required  
Immutable string

The IP address that you have chosen to configure on the load balancer for the ingress proxy.

Example:
    
    
    loadBalancer:
      vips:
        ingressVIP: "203.0.113.4"
    

### `loadBalancer.kind`

Required  
Immutable string

Set this to `"ManualLB"`, `"F5BigIP"`, `"Seesaw"`, or `"MetalLB"`.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"manualLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.manualLB.ingressHTTPNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable integer

The ingress proxy in a user cluster is exposed by a [Kubernetes Services of type `LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer). The Service has a [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) for HTTP. You must choose a `nodePort` value for the HTTP ServicePort.

Set this field to the `nodePort` value.

Example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPNodePort: 32527
    

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable integer

The ingress proxy in a user cluster is exposed by a Service of type LoadBalancer. The Service has a ServicePort for HTTPS. You must choose a `nodePort` value for the HTTPS ServicePort.

Set this field to the `nodePort` value. Example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPSNodePort: 30139
    

#### `loadBalancer.manualLB.controlPlaneNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable integer

The Kubernetes API server of a user cluster runs in the admin cluster, and is exposed by a Service of type `LoadBalancer`. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value.

Example:
    
    
    loadBalancer:
      manualLB:
        controlPlaneNodePort: 30968
    

#### `loadBalancer.manualLB.konnectivityServerNodePort`

Required if `loadBalancer.kind` = `ManualLB`  
Immutable integer

The Kubernetes API server of a user cluster runs in the admin cluster, and is exposed by a Service of type `LoadBalancer`. The Konnectivity server reuses this service with a different `nodePort` value. You must choose a `nodePort` value for the Konnectivity server.

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
Immutable string

The address of your F5 BIG-IP load balancer.

Example:
    
    
    loadBalancer:
      f5BigIP:
          address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.fileRef.path`

Required if `loadBalancer.kind` = `"f5BigIP"`  
Mutable string

The path of a [credentials file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

For information about updating your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        fileRef:
          path: ""my-config-folder/user-creds.yaml"
    

#### `loadBalancer.f5BigIP.fileRef.entry`

Required if `loadBalancer.kind` = `"f5BigIP"`  
Immutable string

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

Example:
    
    
    loadBalancer:
      f5BigIP:
        fileRef:
          entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

Required if `loadBalancer.kind` = `"f5BigIP"`  
Immutable string

The name of a BIG-IP partition that you created for your admin cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

Required if `loadBalancer.kind` = `"f5BigIP"` and you are using SNAT  
Immutable string

The name of your SNAT pool.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

If you set `loadbalancer.kind` to `"Seesaw"`, fill in this section. Otherwise, remove this section or leave it commented out.

For information on setting up the Seesaw load balancer, see [Seesaw load balancer quickstart](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/seesaw-load-balance-quickstart) and [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance).

#### `loadBalancer.seesaw.ipBlockFilePath`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable string

The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) for your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/user-seesaw-ipblock.yaml"
    

#### `loadBalancer.seesaw.vrid`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable integer  
Possible values: 1 - 255  
Prepopulated: 0  


The [virtual router identifier](https://datatracker.ietf.org/doc/html/rfc5798) of your Seesaw VM. This identifier, which is an integer of your choice, must be unique in a VLAN.

Example:
    
    
    loadBalancer:
      seesaw:
        vrid: 125
    

#### `loadBalancer.seesaw.masterIP`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable string

The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1).

Example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

#### `loadBalancer.seesaw.cpus`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable integer  
Prepopulated: 4  


The number of CPUs for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        cpus: 8
    

#### `loadBalancer.seesaw.memoryMB`

Required if `loadBalancer.kind` = `Seesaw`  
Immutable Integer  
Prepopulated: 3072  


The number of mebibytes of memory for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

**Note** : This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

#### `loadBalancer.seesaw.vCenter.networkName`

Optional  
Immutable string  
Default: Same as the cluster nodes

The name of the vCenter network that contains your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

#### `loadBalancer.seesaw.enableHA`

Optional  
Relevant if `loadBalancer.kind` = `Seesaw`  
Immutable boolean  
Prepopulated: false  
Default: false

If you want to create a high-availability (HA) Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

#### `loadBalancer.seesaw.disableVRRPMAC`

Optional  
Relevant if `loadBalancer.kind` = `Seesaw`  
Immutable boolean  
Prepopulated: true  
Default: true

If you set this to `true`, the Seesaw load balancer does not use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. We recommend that you set this to `true`. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`.

Example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

### `loadBalancer.metalLB`

If you set `loadbalancer.kind` to `"MetalLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance-metallb).

#### `loadBalancer.metalLB.addressPools`

Required if `loadBalancer.kind` = 'MetalLB`

Mutable array of objects, each of which holds information about an address pool to be used by the MetalLB load balancer.

##### `loadBalancer.metalLB.addressPools[i].name`

Required if `loadBalancer.kind` = `MetalLB`  
Mutable string

A name of your choice for the address pool.

Example:
    
    
    loadBalancer:
      metalLB:
        addressPools:
        - name: "my-address-pool-1"
    

##### `loadBalancer.metalLB.addressPools[i].addresses`

Required if `loadBalancer.kind` = `MetalLB`  


Mutable array of strings, each of which is a range of addresses. Each range must be in CIDR format or hyphenated range format.

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
Mutable boolean  
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
Mutable boolean  
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
Immutable boolean  
Prepopulated: false  
Default: false

If you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2), set this to `true`. Otherwise set this to `false`.

Example:
    
    
    enableDataplaneV2: true
    

See [Dataplane V2 Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting) for troubleshooting steps.

## `enableWindowsDataplaneV2`

Preview  
Optional  
Immutable boolean  
Prepopulated: false  
Default: false

If you want to enable [Windows Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for a cluster with Windows nodes, set this to `true`. Otherwise set this to `false`.

If `enableWindowsDataplaneV2` is set to `true`, the containerd runtime is enabled, instead of the Docker runtime.

Example:
    
    
    enableWindowsDataplaneV2: true
    

See [Dataplane V2 Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting) for troubleshooting steps. See [User guide for Windows Server OS node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-guide-for-windows-server-os-node-pools) to set up node pools containing Windows Server OS nodes.

## `multipleNetworkInterfaces`

Preview  
Optional  
Immutable boolean  
Prepopulated: false  
Default: false

If you want to enable multiple network interfaces for Pods, set this to `true`. Otherwise set this to `false`.

For more information, see [Configure multiple network interfaces for Pods](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/multi-nic).

Example:
    
    
    multipleNetworkInterfaces: true
    

## `advancedNetworking`

Preview  
Optional  
boolean  
Prepopulated: false  
Default: false

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/egress-nat-gateway), set this to `true`. Otherwise set it to `false`.

If you set this field to `true`, you must also set `enableDataplaneV2` to `true`.

Example:
    
    
    advancedNetworking: true
    

## `masterNode`

This section holds information about the nodes, in the admin cluster, that serve as control-plane nodes for this user cluster.

## masterNode.vsphere.datastore

Optional if `vCenter.datacenter` inherits from the admin cluster  
Required if `vCenter.datacenter` is not equal to the admin cluster's data center  
Immutable string

Default: If `vCenter.datacenter` inherits from the admin cluster, this defaults to `vCenter.datastore` as specified in this configuration file.

Default: If `vCenter.datacenter` is different from the admin cluster's data center, this has no default value.

The vSphere datastore for the control-plane node(s) of this user cluster.

Example:
    
    
    masterNode:
       vsphere:
          datastore: "control-plane-datastore"
    

### `masterNode.cpus`

Optional  
Mutable integer  
Prepopulated: 4  
Default: 4

The number of CPUs for each admin cluster node that serves as a control plane for this user cluster.

Example:
    
    
    masterNode:
      cpus: 8
    

### `masterNode.memoryMB`

Optional  
Mutable integer  
Prepopulated: 8192  
Default: 8192

The mebibytes of memory for each admin cluster node that serves as a control plane for this user cluster. Must be a multiple of 4.

Example:
    
    
    masterNode:
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `masterNode.replicas`

Optional  
Immutable integer  
Possible values: 1 or 3  
Prepopulated: 1  
Default: 1

The number of control-plane nodes for this user cluster. This number cannot be changed once you have created the cluster. If you want to update the number of replicas later, you must recreate the user cluster.

Control-plane nodes for the user cluster are in the admin cluster.

Example:
    
    
    masterNode:
      replicas: 3
    

### `masterNode.autoResize.enabled`

Optional  
Mutable boolean  
Prepopulated: false  
Default: false

Set this to `true` to enable automatic resizing of the control-plane nodes for the user cluster. Otherwise, set this to `false`.

Control-plane nodes for the user cluster are in the admin cluster.

For more information, see [Enable node resizing for the control-plane nodes of a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/node-auto-resize#enable_node_resizing_for_the_control-plane_nodes_of_a_user_cluster).

Example:
    
    
    masterNode:
      autoResize:
        enabled: true
    

### `masterNode.vsphere.datastore`

Optional  
Immutable string  
Default: The value of `vCenter.datastore`

The datastore where the control-plane nodes for this user cluster will be created.

Example:
    
    
    masterNode:
      vSphere:
        datastore: "control-plane-datastore"
    

## `nodePools`

Required  
Array of objects, each of which describes a node pool.

For more information, see [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/managing-node-pools).

### `nodePools[i].name`

Required  
Mutable string

A name of your choice for the node pool. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



Example:
    
    
    nodePools:
    - name: "my-node-pool-1"
    

### `nodePools[i].cpus`

Required  
Mutable integer  
Prepopulated: 4

The number of vCPUs for each node in the pool.

Example:
    
    
    nodePools"
    - name: "my-node-pool"
      cpus: 8
    

### `nodePools[i].memoryMB`

Required  
Mutable integer  
Prepopulated: 8192

The mebibytes of memory for each node in the pool. Must be a multiple of 4.

Example:
    
    
    nodePools"
    - name: "my-node-pool"
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `nodePools[i].replicas`

Required  
Mutable integer  
Prepopulated: 3  
Possible values: The total number of untainted nodes across all node pools in the array must be at least 3.

The number of nodes in the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      replicas: 5
    

### `nodePools[i].bootDiskSizeGB`

Optional  
Mutable integer  
Prepopulated: 40  
Default: 40

The size of the boot disk in gibibytes for each node in the pool.

Example:
    
    
    nodePools
    - name: "my-node-pool"
      bootDiskSizeGB: 40
    

### `nodePools[i].osImageType`

Optional  
Mutable string  
Possible values: "ubuntu", "ubuntu_containerd", "cos", "windows"  
Prepopulated: "ubuntu_containerd"  
Default: "ubuntu_containerd"

The type of OS image to run on the VMs in the node pool.

Example:
    
    
    nodePools
    - name: "my-node-pool"
      osImageType: "ubuntu_containerd"
    

### `nodePools[i].osImage`

Required if `nodePools[i].osImageType` = `windows`  
Mutable string  


The name of a Windows VM template. The template must be based on a Windows Server 2019 ISO that has the en-US language/region tag.

For more information, see [User guide for Windows Server OS node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-guide-for-windows-server-os-node-pools).

### `nodePools[i].labels`

Optional  
Mutable mapping

Labels to apply to each Kubernetes Node object in the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      labels:
        environment: "production"
        tier: "cache"
    

### `nodePools[i].taints`

Optional  
Mutable array of objects, each of which describes a taint.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      taints:
      - key: "staging"
        value: "true"
        effect: "NoSchedule"
    

### `nodePools[i].vsphere.datastore`

Optional  
Mutable string  
Default: The value of `vCenter.datastore`

The name of the vCenter datastore where the nodes will be created.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        datastore: "my-datastore"
    

### `nodePools[i].vsphere.tags`

Optional  
Mutable array of objects, each of which describes a [vSphere tag](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html) to be placed on the VMs in the node pool.

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



### `nodePools[i].autoscaling`

Preview  
Optional

If you want to enable automatic scaling for the node pool, fill in this section. Otherwise, remove this section or leave it commented out.

#### `nodePools[i].autoscaling.minReplicas`

Optional  
Mutable integer  
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
Mutable integer  
Prepopulated: 0

The maximum number of nodes that the autoscaler can set for the pool.

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      autoscaling:
        maxReplicas: 10
    

#### `nodePools[i].enableLoadBalancer`

Preview  
Optional  
Relevant if `loadBalancer.kind` = `"MetalLB"`  
Mutable boolean  
Prepopulated: false  
Default: false

Set this to `true` if you want to allow the MetalLB speaker to run on the nodes in the pool. Otherwise, set it to `false`.

For more information, see [Bundled load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance-metallb).

Example:
    
    
    nodePools:
    - name: "my-node-pool"
      enableLoadBalancer: true
    

## `antiAffinityGroups.enabled`

Required  
Mutable boolean  
Prepopulated: true

Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`.

Example:
    
    
    antiAffinityGroups:
      enabled: true
    

Google Distributed Cloud automatically creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster's nodes, causing them to be spread across at least three physical hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least three physical hosts available.




Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least three hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

## `enableVMTracking`

Preview  
Optional  
Prepopulated: false

Set this to `true` to enable VM tracking with vSphere tags. Otherwise, set it to `false`.

For more information, see [Enable VM tracking](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/vm-track-tags).

Example:
    
    
    enableVMTracking: true
    

## `authentication`

This section holds information about how cluster users are authenticated and authorized.

### `authentication.oidc`

Do not use this section. Instead, after cluster creation, edit the ClientConfig custom resource as described in [Configuring clusters for Anthos Identity Service with OIDC ](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

### `authentication.sni`

Optional  


If you want to provide an additional serving certificate for the cluster's Kubernetes API server, fill in this section. Otherwise, remove this section or leave it commented out.

#### `authentication.sni.certPath`

Optional  
Immutable string

The path of a serving certificate for the Kubernetes API server.

Example:
    
    
    authentication:
      sni:
        certPath: "my-cert-folder/example.com.crt"
    

#### `authentication.sni.keyPath`

Optional  
Immutable string

The path of the certificate's private key file.

Example:
    
    
    authentication:
      sni:
        keyPath: "my-cert-folder/example.com.key"
    

## `gkeConnect`

Required

This section holds information about the Google Cloud project and service account you want to use to [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet.

### `gkeConnect.projectID`

Required  
Immutable string

The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/multiple-gcp-projects#fleet_host_project).

Example:
    
    
    gkeConnect:
      projectID: "my-fleet-host-project-123"
    

### `gkeConnect.registerServiceAccountKeyPath`

Required  
Mutable string

The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/service-accounts#connect_register_service_account).

To update the value of this field, use `gkectl update cluster`.

For information about changing your connect-register service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/rotating-service-account-keys).

Example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

## `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/concepts/logging-and-monitoring) for your cluster, fill in this section. Otherwise remove this section or leave it commented out.

### `stackdriver.projectID`

Required for Logging and Monitoring  
Immutable string

The ID of your [logging-monitoring project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/multiple-gcp-projects#logging_monitoring_project). This is the Google Cloud project where you will view logs and metrics.

Example:
    
    
    stackdriver:
      projectID: "my-logs-project"
    

### `stackdriver.clusterLocation`

Required for Logging and Monitoring  
Immutable string  
Prepopulated: "us-central1"

The Google Cloud region where you want to store logs. It is a good idea to choose a region that is near your on-premises data center.

Example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.enableVPC`

Optional  
Immutable boolean  
Prepopulated: false

If your cluster's network is controlled by a [VPC](https://docs.cloud.google.com/vpc), set this to`true`. This ensures that all telemetry flows through Google's restricted IP addresses. Otherwise, set this to `false`.

Example:
    
    
    stackdriver:
      enableVPC: false
    

### `stackdriver.serviceAccountKeyPath`

Required for Logging and Monitoring  
Mutable string

The path of the JSON key file for your logging-monitoring service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your logging-monitoring service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/rotating-service-account-keys).

Example:
    
    
    stackdriver:
      serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
    

### `stackdriver.disableVsphereResourceMetrics`

Optional  
Immutable boolean  
Prepopulated: false  
Default: false

Set this to `true` to disable the collection of metrics from vSphere. Otherwise, set it to `false`.

Example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `usageMetering`

Alpha  
Optional

If you want to enable usage metering for your cluster, then fill in this section. Otherwise, remove this section or leave it commented out.

### `usageMetering.bigQueryProjectID`

Alpha Required for usage metering  
Immutable string

The ID of the Google Cloud project where you want to store usage metering data.

Example:
    
    
    usageMetering:
      bigQueryProjectID: "my-bq-project"
    

### `usageMetering.bigQueryDatasetID`

Alpha Required for usage metering  
Immutable string

The ID of the BigQuery dataset where you want to store usage metering data. Example:
    
    
    usageMetering:
      bigQueryDatasetID: "my-bq-dataset"
    

### `usageMetering.bigQueryServiceAccountKeyPath`

Alpha Required for usage metering  
Mutable string.

The path of the JSON key file for your BigQuery service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your BigQuery service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/rotating-service-account-keys).

Example:
    
    
    usageMetering:
      bigQueryServiceAccountKeyPath: "my-key-folder/bq-key.json"
    

### `usageMetering.enableConsumptionMetering`

Alpha Required for usage metering  
Immutable boolean  
Prepopulated: false

Set this to `true` if you want to enable consumption-based metering. Otherwise set this to false.

Example:
    
    
    usageMetering:
      enableConsumptionMetering: true
    

## `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in this section. Otherwise, remove this section or leave it commented out.

### `cloudAuditLogging.projectID`

Required for Cloud Audit Logs  
Immutable string

The project ID of the Google Cloud project where you want to store audit logs.

Example:
    
    
    cloudAuditLogging:
      projectID: "my-audit-project"
    

### `cloudAuditLogging.clusterLocation`

Required for Cloud Audit Logs  
Immutable string

The Google Cloud region where you want to store audit logs. It is a good idea to choose a region that is near your on-premises data center

Example:
    
    
    cloudAuditLogging:
      clusterLocation: "us-central1"
    

### `cloudAuditLogging.serviceAccountKeyPath`

Preview  
Required for Cloud Audit Logs  
Mutable string

The path of the JSON key file for your audit-logging service account.

To update the value of this field, use `gkectl update cluster`.

For information about changing your audit-logging service account key, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/rotating-service-account-keys).

Example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## `autoRepair.enabled`

Required  
Mutable boolean  
Prepopulated: true

Set this to `true` to enable node auto repair. Otherwise, set it to `false`.

Example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to encrypt Secrets without the need for an external KMS (Key Management Service), or any other dependencies, fill in this section. Otherwise, remove this section or leave it commented out.

### `secretsEncryption.mode`

Required for Secrets encryption  
Immutable string  
Possible value: "GeneratedKey"  
Prepopulated: "GeneratedKey"

The Secret encryption mode.
    
    
    secretsEncryption:
      mode: "GeneratedKey"
    

### `secretsEncryption.generatedKey.keyVersion`

Required for Secrets encryption  
Mutable integer  
Prepopulated: 1

An integer of your choice to use for the key version number. We recommend that you start with `1`.

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        keyVersion: 1
    

### `secretsEncryption.generatedKey.disabled`

Required for Secrets encryption  
Mutable boolean  
Prepopulated: false

Set this to `true` to disable Secrets encryption. Otherwise set it to `false`.

For information about updating this field for an existing cluster, see [Always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/always-on-secrets-encryption).

Example:
    
    
    secretsEncryption:
      generatedKey:
        disabled: false
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
