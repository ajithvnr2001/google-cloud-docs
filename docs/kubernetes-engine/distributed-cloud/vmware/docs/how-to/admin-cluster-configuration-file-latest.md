---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest/
title: Admin cluster configuration file 1.30 and higher \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:01.632238+00:00
---

# Admin cluster configuration file 1.30 and higher  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Admin cluster configuration file 1.30 and higher Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the fields in the admin cluster configuration file for versions 1.30 and higher Google Distributed Cloud.

## Generating a template for your configuration file

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your admin cluster configuration file. Also, `gkeadm` filled in some of the fields for you.

If you did not use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your admin cluster configuration file.

To generate a template for your admin cluster configuration file:
    
    
    gkectl create-config admin --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace the following:

  * `OUTPUT_FILENAME`: a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `admin-cluster.yaml` and puts it in the current directory.

  * `VERSION`: the Google Distributed Cloud version number. For example: `gkectl create-config admin --gke-on-prem-version=1.36.100-gke.144`. This version must be equal to or less than your `gkectl` version. If you omit this flag, the generated config template is populated with values based on the latest 1.36 patch.




**Template**

Click to see the generated template for version 1.36.
    
    
    apiVersion: v1
    kind: AdminCluster
    # (Optional) A unique name for this admin cluster. This will default to a random name
    # prefixed with 'gke-admin-'
    name: ""
    # (Required) Absolute path to a GKE bundle on disk
    bundlePath: ""
    # (Optional) Enable advanced cluster options
    enableAdvancedCluster: true
    # # (Optional/Preview) The absolute or relative path to the yaml file to use for topology
    # # domains. Require advanced cluster is enabled
    # infraConfigFilePath: ""
    # # (Optional/Preview) Specify the prepared secret configuration which can be added
    # # or edited only during cluster creation
    # preparedSecrets:
    #   # enable prepared credentials for the admin cluster; it is immutable
    #   enabled: false
    # (Required) vCenter configuration
    vCenter:
      address: ""
      datacenter: ""
      cluster: ""
      # Resource pool to use. Specify [VSPHERE_CLUSTER_NAME]/Resources to use the default
      # resource pool
      resourcePool: ""
      # Storage policy to use for cluster VM storage and default StorageClass. Do not
      # specify it together with datastore
      storagePolicyName: ""
      # # Datastore to use for cluster VM storage and default StorageClass. Do not specify
      # # it together with storagePolicyName
      # datastore: ""
      # Provide the path to vCenter CA certificate pub key for SSL verification
      caCertPath: ""
      # The credentials to connect to vCenter
      credentials:
        # reference to external credentials file
        fileRef:
          # read credentials from this file
          path: ""
          # entry in the credential file
          entry: ""
      # (Optional) vSphere folder where cluster VMs will be located. Defaults to the
      # datacenter wide folder if unspecified.
      folder: ""
      # # (Only used in 1.16 and older versions for non-HA admin cluster) Provide the name
      # # for the persistent disk to be used by the deployment (ending in .vmdk). Any directory
      # # in the supplied path must be created before deployment. Required for non-HA admin
      # # cluster. Invalid for HA admin cluster as the path is generated automatically under
      # # the root directory "anthos" in the specified datastore.
      # dataDisk: ""
    # (Required) Network configuration
    network:
      # (Required when using "static" ipMode.type; or "Seesaw" loadBalancer.kind; or using
      # amdin cluster HA mode) This section overrides ipMode.ipBlockFilePath values when
      # ipMode.type=static. It's also used for seesaw nodes
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
      serviceCIDR: 10.96.232.0/24
      # (Required) The Kubernetes pod CIDR range for the cluster. Must not overlap with
      # the service CIDR range
      podCIDR: 192.168.0.0/16
      vCenter:
        # vSphere network name
        networkName: ""
      # (Required for HA admin cluster) Specify the IPs to use for control plane machines
      # for HA admin cluster.
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
      # (Required) Which load balancer to use "ManualLB" or "MetalLB".
      kind: MetalLB
      # # (Required when using "ManualLB" kind) Specify pre-defined nodeports
      # manualLB:
      #   # NodePort for ingress service's http (only needed for user cluster)
      #   ingressHTTPNodePort: 0
      #   # NodePort for ingress service's https (only needed for user cluster)
      #   ingressHTTPSNodePort: 0
      #   # NodePort for konnectivity server service (only needed for controlplane v1 user
      #   # cluster)
      #   konnectivityServerNodePort: 0
      #   # NodePort for control plane service (not needed for HA admin cluster or controlplane
      #   # V2 user cluster)
      #   controlPlaneNodePort: 30968
    # Spread admin addon nodes and user masters across different physical hosts (requires
    # at least three hosts)
    antiAffinityGroups:
      # Set to false to disable DRS rule creation
      enabled: true
    # Specify the admin master node configuration (default: 4 CPUs; 16384 MB memory; 3
    # replicas). The replicas field has to be 3 for new admin cluster creation
    adminMaster:
      cpus: 4
      memoryMB: 16384
      # How many machines of this type to deploy
      replicas: 3
      # # (Optional/Preview) Topology domains that admin cluster master nodes will be deployed
      # # to. Only 1 element is allowed. Advanced cluster must be enabled and infraConfigFilePath
      # # must be filled in admin cluster
      # topologyDomains:
      # - ""
      # # (Optional) Control plane load balancer configuration. Only supported when advanced
      # # cluster is enabled
      # controlPlaneLoadBalancer:
      #   # # (Optional) The control plane load balancer mode for advanced cluster. Possible values
      #   # # are bundled or manual. Default value is bundled for advanced cluster without topology
      #   # # domains; and is manual for advanced cluster with topology domains.
      #   # mode: ""
    # # (Only used in 1.16 and older versions) Specify the addon node configuration which
    # # can be added or edited only during cluster creation
    # addonNode:
    #   # Enable auto resize for addon node
    #   autoResize:
    #     # Whether to enable auto resize for master. Defaults to false.
    #     enabled: false
    # (Optional) Specify the proxy configuration
    proxy:
      # The URL of the proxy
      url: ""
      # The domains and IP addresses excluded from proxying
      noProxy: ""
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
    #   # The absolute or relative path to the CA certificate for this registry
    #   caCertPath: ""
    # (Required): The absolute or relative path to the GCP service account key for pulling
    # GKE images
    componentAccessServiceAccountKeyPath: ""
    # (Required) Specify which GCP project to register your GKE OnPrem cluster to
    gkeConnect:
      projectID: ""
      # # (Optional) The location of the GKE Hub and Connect service where the cluster is
      # # registered to. It can be any GCP region or "global". Default to "global" when unspecified.
      # location: us-central1
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerServiceAccountKeyPath: ""
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
    # # (Optional/Preview) Configure backups for admin cluster. Backups will be stored under
    # # /anthos-backups/.
    # clusterBackup:
    #   # # datastore where admin cluster backups are desired
    #   # datastore: ""
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
    # (Optional) Specify the type of OS image; available options can be set to "ubuntu_containerd"
    # "cos" "ubuntu_cgv2" or "cos_cgv2". Default is "ubuntu_containerd".
    osImageType: ubuntu_cgv2
    
    

## Required fields and default values

If a field is marked as _Required_ , then the completed configuration file must have a value filled in for the field.

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

Set `enableAdvancedCluster` to `false` if you don't want to enable advanced cluster when creating a new cluster. When this flag is set to `true` (advanced cluster enabled), Google Distributed Cloud software deploys controllers that allow for a more extensible architecture. Enabling advanced cluster gives you access to new features and capabilities, such as [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). This field is required if `infraConfigFilePath` is configured.

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

Set `enableAdvancedClusters` to `true` to enable advanced cluster when creating a new cluster. When this flag is enabled, the underlying Google Distributed Cloud software deploys controllers that allow for a more extensible architecture. Enabling advanced cluster gives you access to new features and capabilities, such as [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). This field is required if `infraConfigFilePath` is configured.

### 1.30 and lower

Not available.

## `name`

Optional  
String  
Default: A random name starting with prefix "gke-admin-"

A name of your choice for the cluster.

Example:
    
    
    name: "my-admin-cluster"
    

## `bundlePath`

Required  
Mutable  
String

The path of your Google Distributed Cloud bundle file. You can specify either a full bundle or a regular bundle. For a detailed comparison, see [About Google Distributed Cloud bundles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles).

When you create an admin workstation, it comes pre-installed with a full bundle:
    
    
    /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz
    

Example full bundle:
    
    
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.30.0-gke.1-full.tgz"
    

If you prefer to use a regular bundle (which requires downloading images at runtime), specify its path after downloading it:

Example regular bundle:
    
    
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.30.0-gke.1.tgz"
    

## `preparedSecrets.enabled`

If `infraConfigFilePath` is configured, remove this field.

Preview  
Optional  
Immutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` if you want to use [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) in the admin cluster. Otherwise, set it to `false` or omit the field.

Example:
    
    
    preparedSecrets:
      enabled: true
    

## `vCenter`

This sections holds information about your vSphere environment and your connection to vCenter Server.

If `infraConfigFilePath` is configured, remove this entire section. Otherwise, this section is required and immutable.

### `vCenter.address`

Required  
Immutable  
String

The IP address or the hostname of your vCenter server.

For more information, see [Finding your vCenter server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address).

Examples:
    
    
    vCenter:
      address: "203.0.113.100"
    
    
    
    vCenter:
      address: "my-vcenter-server.my-domain.example"
    

### `vCenter.datacenter`

Required  
Immutable  
String

The relative path of a [vSphere data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html).

The value you specify is relative to the root folder named `/`.

If your data center is in the root folder, the value is the name of the data center.

Example:
    
    
    vCenter:
      datacenter: "my-data-center"
    

Otherwise, the value is a relative path that includes one or more folders along with the name of the data center.

Example:
    
    
    vCenter:
      datacenter: "data-centers/data-center-1"
    

### `vCenter.cluster`

Required  
Immutable  
String

The relative path of a [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html) that represents the ESXi hosts where your admin cluster VMs will run. This vSphere cluster represents a subset of the physical ESXi hosts in your vCenter data center.

The value you specify is relative to `/.../DATA_CENTER/vm/`.

If your vSphere cluster is in the `/.../DATA_CENTER/vm/` folder, the value is the name of the vSphere cluster.

Example:
    
    
    vCenter:
      cluster: "my-vsphere-cluster"
    

Otherwise, the value is a relative path that includes one or more folders along with the name of the vSphere cluster.

Example:
    
    
    vCenter:
      cluster: "clusters/vsphere-cluster-1"
    

### `vCenter.resourcePool`

Required  
Immutable  
String

A [vCenter resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) for your admin cluster VMs.

If you want to use the default resource pool, set this to `VSPHERE_CLUSTER/Resources`.

Example:
    
    
    vCenter:
      resourcePool: "my-vsphere-cluster/Resources"
    

If you want to use a resource pool that you have already created, set this to the relative path of your resource pool.

The value you specify is relative to `/.../DATA_CENTER/host/.../VSPHERE_CLUSTER/Resources/`

If your resource pool is a direct child of `/.../DATA_CENTER/host/.../VSPHERE_CLUSTER/Resources/` the value is the name of the resource pool.

Example:
    
    
    vCenter:
      resourcePool: "my-resource-pool"
    

Otherwise, the value is a relative path that has two or more resource pools.

Example:
    
    
    vCenter:
      resourcePool: "resource-pool-1/resource-pool-2"
    

### `vCenter.datastore`

Required if `vCenter.storagePolicyName` isn't specified  
Immutable  
String

The name of a [vSphere datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for your admin cluster.

The value you specify must be a name, not a path. Don't include any folders in the value.

Example:
    
    
    vCenter:
      datastore: "my-datastore"
    

You must specify a value for either `vCenter.datastore` or `vCenter.storagePolicyName`, but not both. If you specify a value for this field, don't specify a value for `vCenter.storagePolicyName`. The `vCenter.datastore` field is immutable except when you set the field to an empty string when you [migrate a datastore to Storage Policy Based Management (SPBM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm).

### `vCenter.storagePolicyName`

Required if `vCenter.datastore` isn't specified  
Immutable  
String

The name of a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the cluster nodes.

The admin cluster must be highly-available (HA) to work with the storage policy.

For more information, see [Configure a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

You must specify a value for either `vCenter.datastore` or `vCenter.storagePolicyName`, but not both. If you specify a value for this field, don't specify a value for `vCenter.datastore`.

### `vCenter.caCertPath`

Required  
Mutable  
String

The path of the CA certificate for your vCenter server.

For more information, see [Getting your vCenter CA certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path).

For information about updating this field for an existing cluster, see [Update vCenter certificate references](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate).

Example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert.pem"
    

### `vCenter.credentials.fileRef.path`

Required  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account should have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements).

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `vCenter.credentials.fileRef.entry`

Required  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vcenter-creds"
    

### `vCenter.folder`

Optional  
Immutable  
String  
Default: The datacenter-wide folder

The relative path of a vSphere folder that you have already created. This folder will hold your admin cluster VMs.

If you do not specify a value, your admin cluster VMs will be put in `/.../DATA_CENTER/vm/`.

If you specify a value, it is relative to `/.../DATA_CENTER/vm/`.

The value can be the name of a folder.

Example:
    
    
    vCenter:
      folder: "my-folder"
    

Or the value can be a relative path that includes more than one folder.

Example:
    
    
    vCenter:
      folder: "folders/folder-1"
    

### `vCenter.dataDisk`

Don't provide a value for this field. Either delete the field or leave it commented out.

## `network`

Required  
Immutable  


This section holds information about your admin cluster network.

### `network.hostConfig`

This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes.

If `infraConfigFilePath` is configured, remove this entire section. Otherwise, this section is required and immutable.

#### `network.hostConfig.dnsServers`

Required if `network.hostConfig` section is filled in.  
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

Required if `network.hostConfig` section is filled in.  
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

DNS search domains for the VMs to use. These domains are used as part of a domain search list.

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

If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`.

In most cases you should specify `static` because you always have to provide IP addresses for the admin cluster's control-plane nodes. DHCP is used only to provide IP addresses in the following cases:

  * If [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) isn't enabled in user clusters, then you can use DHCP for the user cluster's control-plane nodes, which are in the admin cluster.

  * In version 1.16 and lower, add-on nodes for non-HA admin clusters can get their IP addresses from DHCP. In version 1.28 and higher, admin clusters are required to be HA, and they don't have add-on nodes.




Example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

The absolute or relative path of the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your cluster.

If `infraConfigFilePath` is configured, this field is required.

This field is also required in the following cases:

  * 1.16 and lower non-HA admin cluster: list the IP addresses for the control-plane node and add-on nodes in an IP block file.

  * 1.16 and lower HA admin cluster: list the IP addresses for add-on nodes in an IP block file.

  * 1.29 and lower kubeception user clusters: list the IP addresses for the user cluster control-plane nodes in the admin cluster IP block file.




Immutable  
String

Example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/admin-cluster-ipblock.yaml"
    

### `network.serviceCIDR`

Required  
Immutable  
String  
Smallest possible range: /24  
Largest possible range: /12  
Prepopulated: "10.96.232.0/24"  


A range of IP addresses, in CIDR format, to be used for Services in your cluster.

Example:
    
    
    network:
      serviceCIDR: "10.96.232.0/24"
    

### `network.podCIDR`

Required  
Immutable  
String  
Smallest possible range: /18  
Largest possible range: /8  
Prepopulated: "192.168.0.0/16"  


A range of IP addresses, in CIDR format, to be used for Pods in your cluster.

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

The name of the vSphere network for your cluster nodes.

If `infraConfigFilePath` is configured, remove this field. Otherwise, this field is required and immutable.

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
        networkName: "/data-centers/data-center-1/network/my-network"
    

### `network.controlPlaneIPBlock`

Network information for the admin cluster's control-plane nodes.

If `infraConfigFilePath` is configured, remove this entire section. Otherwise, this section is required and immutable.

#### `network.controlPlaneIPBlock.netmask`

Required  
Immutable  
String

The netmask for the network that has your control-plane nodes.

Example:
    
    
    network:
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
    

#### `network.controlPlaneIPBlock.gateway`

Required  
Immutable  
String

The IP address of the default gateway for your control-plane nodes.

Example:
    
    
    network:
      controlPlaneIPBlock:
        gateway: "172.16.22.1"
    

#### `network.controlPlaneIPBlock.ips`

Required  
Immutable  
Array of three objects, each of which has an IP address and an optional hostname.

These are the IP addresses that will be assigned to your control-plane nodes. Hostnames are required for HA admin clusters.

Example:
    
    
    network:
      controlPlaneIPBlock:
        ips:
        - ip: "172.16.22.6"
          hostname: "admin-cp-vm-1"
        - ip: "172.16.22.7"
          hostname: "admin-cp-vm-2"
        - ip: "172.16.22.8"
          hostname: "admin-cp-vm-3"
    

## `infraConfigFilePath`

### 1.31

Specifying a path in this field enables [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up).

Preview  
Optional  
String  
Mutable  


Specify the full path of the vSphere infrastructure configuration file.

Example:
    
    
    infraConfigFilePath: "/my-config-folder/vsphere-infrastructure.yaml"
    

In addition to adding the path, copy the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file) to the applicable directory.

If you add a path to `infraConfigFilePath`, you need to make the following changes to your admin cluster and user cluster configuration files.

#### Admin cluster configuration file changes

  * Remove the following from your admin cluster configuration file. You configure this information in the vSphere infrastructure configuration file per topology domain.

    * `vCenter`: remove the entire `vCenter` section.
    * `network.hostConfig`: remove the entire `network.hostConfig` section.
    * `network.vCenter.networkName`: remove this field.
  * Make the following changes in your admin cluster configuration file:

    * `network.controlPlaneIPBlock`: remove the entire section. Instead, specify the IP addresses for the admin cluster control-plane nodes in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file).

    * `preparedSecrets`: remove this field. [Prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) aren't supported when topology domains is enabled. Remove this field.

  * The following fields are required:

    * `enableAdvancedCluster`: set to `true`.

    * `network.ipMode.ipBlockFilePath`: set to the full or relative path of the admin cluster IP block file.

    * `loadBalancer.kind`: set to `"ManualLB"`. `"ManualLB"` is the only available multi-subnet (layer 3) load balancing option that Google Distributed Cloud offers.




#### User cluster configuration file changes

  * Remove the following from your user cluster configuration file. You configure this information in the vSphere infrastructure configuration file per topology domain.

    * `vCenter`: remove the entire `vCenter` section.
    * `network.hostConfig`: remove the entire `network.hostConfig` section.
    * `network.vCenter.networkName`: remove this field.
    * `masterNode.vsphere`: remove the entire section.
    * `nodePools[i].vsphere.datastore` and `nodePools[i].vsphere.storagePolicyName`: remove these fields.
  * Make the following changes in your user cluster configuration file:

    * `network.controlPlaneIPBlock`: remove the entire section. Instead, specify the IP addresses for the admin cluster control-plane nodes in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file).

    * `preparedSecrets`: remove this field. [Prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) aren't supported when topology domains is enabled.

    * `nodePools[i].vsphere.hostgroups`: remove this field. In versions 1.32.200 and 1.33 and later, use [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) to configure [VM host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity) for each topology domain in the vSphere infrastructure configuration file.

    * `multipleNetworkInterfaces`: set this field to `false`. Multiple network interfaces for Pods aren't supported when topology domains is enabled.

    * `storage.vSphereCSIDisabled`: set this field to `true` to disable the deployment of vSphere CSI components

  * The following fields are required:

    * [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field): set to `true` in the user cluster configuration file.

    * [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#ipblockfilepath-field): set to the full or relative path of the user cluster IP block file.

    * [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-kind-field): set to `"ManualLB"`. `"ManualLB"` is the only available multi-subnet (layer 3) load balancing option that Google Distributed Cloud offers.




### 1.30 and lower

Not available.

## `loadBalancer`

This section holds information about the load balancer for your admin cluster.

### `loadBalancer.vips.controlPlaneVIP`

Required  
Immutable  
String

The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the admin cluster.

Example:
    
    
    loadBalancer:
      vips:
        controlplaneVIP: "203.0.113.3"
    

### `loadBalancer.kind`

Specify the kind of load balancer to use.

### 1.32 and higher

Required  
Immutable  
String  
Prepopulated: "MetalLB"  


The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the `infraConfigFilePath` field is configured.

  * With topology domains: set this to `"ManualLB"`. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use topology domains.

  * Without topology domains: set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer or `"MetalLB"` for our bundled solution.




If `enableAdvancedCluster` is set to `true` (advanced cluster enabled), the kind of load balancer for the control-plane nodes is determined by `adminMaster.controlPlaneLoadBalancer`.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### 1.31

Required  
Immutable  
String  
Prepopulated: "MetalLB"  


The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the `infraConfigFilePath` field is configured.

  * With topology domains: set this to `"ManualLB"`. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use topology domains.

  * Without topology domains: set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer or `"MetalLB"` for our bundled solution.




Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### 1.30

Required  
Immutable  
String  
Prepopulated: "MetalLB"  


Set this to `"ManualLB"` or `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer (such as F5 BIG-IP or Citrix) or `"MetalLB"` for our bundled solution.

Note the following differences from previous versions:

  * In 1.30 and higher, the value `"F5BigIP"` isn't allowed for new admin clusters.

  * In 1.28 and higher, the value `"Seesaw"` isn't allowed for new admin clusters.




If you have an existing cluster that uses these load balancers, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### 1.29 and 1.28

Required  
Immutable  
String  
Prepopulated: "MetalLB"

Set this to `"ManualLB"`, `"F5BigIP"`, or `"MetalLB"`

To enable new and advanced features, we recommend that you use `"ManualLB"` if you have a third-party load balancer (such as F5 BIG-IP or Citrix) or `"MetalLB"` for our bundled solution.

In 1.28 and higher, the value `"Seesaw"` isn't allowed for new admin clusters. If you have an existing cluster that uses Seesaw load balancer, see [Migrate from the Seesaw load balancer to MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb).

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### 1.16 and lower

Required  
Immutable  
String  
Prepopulated: "MetalLB"

String. Set this to `"ManualLB"`, `"F5BigIP"`, `"Seesaw"`, or `"MetalLB"`

If you set `adminMaster.replicas` to `3`, then you can't use the Seesaw load balancer.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

When you create user clusters using the Google Cloud console, the gcloud CLI, or Terraform, the kind of load balancer for the admin cluster and its user clusters must be the same. The only exception is if the admin cluster uses Seesaw, then the user clusters can use MetalLB. If you want your admin and user clusters to use different kinds of load balancers, you must create user clusters using the `gkectl` command-line tool.

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"ManualLB"`, fill in this section. Otherwise, remove this section.  
Immutable  


#### `loadBalancer.manualLB.ingressHTTPNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.konnectivityServerNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

### `loadBalancer.f5BigIP`

### 1.30 and higher

In version 1.30 and higher, the value `"F5BigIP"` isn't allowed for `loadbalancer.kind` for new admin clusters. If the `loadBalancer.f5BigIP` section is in your configuration file, remove it or comment it out.

You can still use your F5 BIG-IP load balancer with new admin clusters, but the configuration is different. For configuration details, see [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

If an existing cluster has this section configured, upgrades to version 1.32 are blocked. You must [migrate your clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to version 1.32.

### 1.29

If you set `loadbalancer.kind` to `"F5BigIP"`, fill in this section. Otherwise, remove this section.

To enable new and advanced features, we recommend that you configure manual load balancing for your F5 BIG-IP load balancer. To enable manual load balancing, set `loadbalancer.kind` to`"ManualLB"` and fill in the `loadBalancer.manualLB` section. For more information, see [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

If you have an existing F5-BIG-IP load balancer and the cluster configuration uses this section, after you have upgraded to 1.29 or higher, we recommend that you [migrate to manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual).

### 1.28 and lower

If you set `loadbalancer.kind` to `"F5BigIP"`, fill in this section. Otherwise, remove this section.

To enable new and advanced features, we recommend that you configure manual load balancing for your F5 BIG-IP load balancer. To enable manual load balancing, set `loadbalancer.kind` to`"ManualLB"` and fill in the `loadBalancer.manualLB` section. For more information, see [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

#### `loadBalancer.f5BigIP.address`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

The address of your F5 BIG-IP load balancer. For example:
    
    
    loadBalancer:
      f5BigIP:
        address: "203.0.113.2"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

The address of your F5 BIG-IP load balancer. For example:
    
    
    loadBalancer:
      f5BigIP:
        address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.path`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIp"`  
Mutable  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: "my-config-folder/admin-creds.yaml"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIp"`  
Mutable  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: "my-config-folder/admin-creds.yaml"
    

#### `loadBalancer.f5BigIP.credentialsfileRef.entry`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIp"`  
Mutable  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIp"`  
Mutable  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

### 1.30 and higher

**Not allowed for new clusters**  
Required if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

The name of a BIG-IP partition that you created for your admin cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

### 1.29 and lower

Required if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

The name of a BIG-IP partition that you created for your admin cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

### 1.30 and higher

**Not allowed for new clusters**  
Optional  
Relevant if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

If you are using SNAT, the name of your SNAT pool. If you are not using SNAT, remove this field.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### 1.29 and lower

Optional  
Relevant if `loadBalancer.kind` = `"F5BigIp"`  
Immutable  
String

If you are using SNAT, the name of your SNAT pool. If you are not using SNAT, remove this field.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

Don't use this section. The Seesaw load balancer is not supported for new admin clusters in version 1.28 and higher. Instead, we recommend that you configure the MetalLB load balancer for new admin clusters. For more information on configuring MetalLB, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

Although we still support Seesaw for non-HA admin clusters that have been upgraded, we recommend that you [migrate to MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb).

## `antiAffinityGroups.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`.

If this field is `true`, Google Distributed Cloud creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster nodes, causing them to be spread across at least three physical ESXi hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least four ESXi hosts available.




Even though the rule requires that the cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available. This protects you from losing your admin cluster control plane. For example, suppose you have only three ESXi hosts, and your admin cluster control-plane node is on an ESXi host that fails. The DRS rule will prevent the control-plane node from being placed on one of the remaining two ESXi hosts.

Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you don't have DRS enabled, or if you don't have at least four hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

Note the following limitation with advanced clusters:

  * Version 1.31: if the `enableAdvancedCluster` field is `true`, anti-affinity rules aren't supported on advanced clusters, and you must set `antiAffinityGroups.enabled` to `false`.

  * Version 1.32: anti-affinity rules are supported on advanced clusters.




Example:
    
    
    antiAffinityGroups:
      enabled: true
    

## `adminMaster`

Immutable  


Configuration settings for the control-plane nodes in the admin cluster.

### `adminMaster.controlPlaneLoadBalancer`

### 1.32 and higher

Optionally, include this section to specify the kind of load balancer to use for control-plane traffic in the admin cluster. Include `adminMaster.controlPlaneLoadBalancer.mode` in your configuration file if you want to explicitly set the kind of load balancer to use rather than relying on the default value. Additionally, you must set `loadBalancer.kind` in your configuration file even though the field is a no-op in 1.32 and higher.

#### `adminMaster.controlPlaneLoadBalancer.mode`

Optional  
Immutable  
String  
Default: Depends on whether the cluster uses topology domains

The kind of load balancer that you can use depends on whether you will set up the cluster to use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The cluster is assumed to use topology domains if the `infraConfigFilePath` field is configured.

  * With topology domains: specify `"manual"`, which is the default value. You must configure a third-party load balancer (such as F5 BIG-IP or Citrix) if you want to use topology domains.

  * Without topology domains: specify either `"manual"` or `"bundled"`. Use `"manual"` if you have a third-party load balancer or `"bundled"` for our bundled solution, which uses [keepalived](http://keepalived.readthedocs.io) \+ [haproxy](http://www.haproxy.org/) running on the three admin cluster control-plane nodes. The default value is "`bundled"`.




Example:
    
    
    adminMaster:
      controlPlaneLoadBalancer:
        mode: "manual"
    

### 1.31 and lower

This section is unavailable. Instead, use `loadBalancer.kind` to specify the kind of load balancer for the admin cluster to use.

### `adminMaster.cpus`

Preview  
Optional  
Immutable  
Integer  
Prepopulated: 4  
Default: 4

The number of vCPUs for each control-plane node in the admin cluster.

Example:
    
    
    adminMaster:
      cpus: 4
    

### `adminMaster.memoryMB`

Preview  
Optional  
Immutable  
Integer  
Prepopulated: 16384  
Default: 16384

The number of mebibytes of memory for each control-plane node in the admin cluster.

Example:
    
    
    adminMaster:
      memoryMB: 16384
    

### `adminMaster.replicas`

### 1.28 and higher

Required for new clusters  
Immutable  
Integer  
Possible values: 3

The number of control-plane nodes in the admin cluster. In 1.28 and higher, new admin clusters must be highly available (HA). Set this field to `3` to create an HA admin cluster with 3 control plane nodes.

Example:
    
    
    adminMaster:
      replicas: 3
    

### 1.16 and lower

Optional  
Immutable  
Integer  
Possible values: 1 or 3  
Prepopulated: 1  
Default: 1

The number of control-plane nodes in the admin cluster. Set this to `3` if you want to create a high-availability admin cluster. Otherwise, set it to `1`.

If you set this to `3`, then you must also fill in the `network.controlPlaneIPBlock` section and the `network.hostConfig` section.

If you set this to `3`, then you cannot use the Seesaw load balancer.

Example:
    
    
    adminMaster:
      replicas: 3
    

### `adminMaster.topologyDomains`

### 1.32 and higher

Preview  
Optional  
Array of strings | Allows one element or three different elements  
Immutable  
Default: `vSphereInfraConfig.defaultTopologyDomain` if specified in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

An array of topology domains. If `infraConfigFilePath` is configured (which indicates the cluster will use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), optionally include this field. The number of topology domains in the array determines how the admin cluster control-plane nodes are deployed, as follows:

  * One element: all three admin cluster control-plane nodes will be deployed in the specified topology domain.
  * Three elements: each admin cluster control-plane node will be deployed in a different topology domain (that is, one node per topology domain).



### 1.31 and higher

**Available for new clusters only**  
Preview  
Array of strings | Allows only one element  
Optional  
Immutable  
Default: `vSphereInfraConfig.defaultTopologyDomain` if specified in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

An array of topology domains. If `infraConfigFilePath` is configured (which indicates the cluster will use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), optionally include this field. The admin cluster control-plane nodes will be deployed in the specified topology domain.

### 1.30 and lower

Not available.

## `addonNode.autoResize.enabled`

### 1.28 and higher

Don't include this setting in your configuration file when creating a new cluster. Admin clusters created in version 1.28 and higher must be highly available (HA) with three control plane nodes. In version 1.28 and higher, HA admin clusters don't have add-on nodes.

### 1.16 and lower

Optional  
Mutable  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to enable automatic resizing of the add-on nodes in the admin cluster. Othersise set it to `false`.

To update the value of this field, use `gkectl update admin`.

Example:
    
    
    addonNode:
      autoResize:
        enabled: true
    

## `proxy`

If your network is behind a proxy server, fill in this section. Otherwise, remove this section or leave it commented out. The proxy server you specify here is used by the user clusters that this admin cluster manages.  
Immutable

### `proxy.url`

Required if `proxy` section is filled in.  
Immutable  
String

The HTTP address of your proxy server. Include the port number even if it's the same as the scheme's default port.

Example:
    
    
    proxy:
      url: "http://my-proxy.example.local:80"
    

The proxy server you specify here is used by your Google Distributed Cloud clusters. Also, your admin workstation is automatically configured to use this same proxy server unless you set the `HTTPS_PROXY` environment variable on your admin workstation.

If you specify `proxy.url`, you must also specify `proxy.noProxy`.

After the proxy configuration for the admin cluster has been set, it cannot be modified or deleted, unless the cluster is rebuilt.

### `proxy.noProxy`

Optional  
Immutable  
String

A comma-separated list of IP addresses, IP address ranges, host names, and domain names that should not go through the proxy server. When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request is sent directly.

Example:
    
    
    proxy:
      noProxy: "10.151.222.0/24,my-host.example.local,10.151.2.1"
    

## `privateRegistry`

A [private container registry](https://docs.dockstore.org/en/stable/advanced-topics/docker-registries.html#public-vs-private-docker-registries) is a registry where access to container images is restricted to authenticated users. Fill in this section if your user clusters need to access workload images. When you configure the `privateRegistry` section, all user clusters managed by this admin cluster will pull workload images from the private registry that you configure here.

If you configure the `privateRegistry` section, when you run `gkectl prepare` before cluster creation or upgrade, `gkectl` pushes the Google Distributed Cloud system images to the private registry. During the cluster creation or upgrade, system images are pulled from the private registry. If you don't configure the `privateRegistry` section, system images are pulled from `gcr.io/gke-on-prem-release` using the [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account).

You might want to configure the `privateRegistry` section so that clusters pull system images from the private registry instead of `gcr.io/gke-on-prem-release` in the following cases:

  * You need to minimize connections to Google Cloud because of security concerns or regulatory requirements.
  * Your organization requires outbound traffic to pass through a proxy server, and the network speed to connect to Google Cloud is slow. 



If you want to use Google's Artifact Registry as a private registry, see [Use Artifact Registry as a private registry for workload images](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/artifact-registry) for the configuration steps.

### `privateRegistry.address`

Required for private registry  
Immutable  
String

The IP address or FQDN (Fully Qualified Domain Name) of the machine that runs your private registry.

Examples:
    
    
    privateRegistry:
      address: "203.0.113.10"
    
    
    
    privateRegistry:
      address: "fqdn.example.com"
    

### `privateRegistry.credentials.fileRef.path`

Required for private registry  
Mutable  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to access your private registry.

Example:
    
    
    privateRegistry:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `privateRegistry.credentials.fileRef.entry`

Required for private registry  
Mutable  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your private registry account.
    
    
    privateRegistry:
      credentials:
        fileRef:
          entry: "private-registry-creds"
    

### `privateRegistry.caCertPath`

Required for private registry  
Mutable  
String

When the container runtime pulls an image from your private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). The container runtime uses the CA's certificate to validate the registry's certificate.

Set this field to the path of the CA's certificate.

Example:
    
    
    privateRegistry:
      caCertPath: "my-cert-folder/registry-ca.crt"
    

## `componentAccessServiceAccountKeyPath`

Required  
Mutable  
String

The path of the JSON key file for your component access service account.

Example:
    
    
    componentAccessServiceAccountKeyPath: "my-key-folder/access-key.json"
    

## `gkeConnect`

Required  
Mutable  


When you fill in the `gkeConnect` section, the admin cluster is automatically registered to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) after it is created. This section holds information about the Google Cloud project and service account needed to register the cluster.

During cluster creation or update, several [RBAC policies](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster#rbac_policies) are configured on the admin cluster. These RBAC policies are needed so that you can create user clusters in the Google Cloud console.

### `gkeConnect.projectID`

Required  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). For new clusters, this project ID must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

Example:
    
    
    gkeConnect:
      projectID: "my-fleet-host-project"
    

### `gkeConnect.location`

Optional  
Immutable  
String  
Default: global

Each cluster's fleet membership is managed by the Fleet service (`gkehub.googleapis.com`) and the Connect service (`gkeconnect.googleapis.com`). The location of the services can be global or regional. In 1.28 and later, you can optionally specify the Google Cloud region in which the Fleet and the Connect services run. If not specified, the global instances of the services are used. Note the following:

  * Admin clusters created prior to 1.28 are managed by the global Fleet and Connect services.

  * For new clusters, if you include this field, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.




Example:
    
    
    gkeConnect:
      location: "us-central1"
    

### `gkeConnect.registerServiceAccountKeyPath`

Required  
Mutable  
String

The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account).

Example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

## `gkeOnPremAPI`

Optional  


In 1.16 and later, if the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) automatically in the region configured in `stackdriver.clusterLocation`.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




Enrolling your admin cluster in the GKE On-Prem API lets you use standard tools—the Google Cloud console, the Google Cloud CLI, or [Terraform](https://www.terraform.io/)—to upgrade user clusters that the admin cluster manages. Enrolling your cluster also lets you run `gcloud` commands to [get information about your clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).

After you add this section and create or update the admin cluster, if subsequently you remove the section and update the cluster, the update will fail.

### `gkeOnPremAPI.enabled`

Required if the `gkeOnPremAPI` section is included.  
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
Default:`stackdriver.clusterLocation`

The Google Cloud region where the GKE On-Prem API runs and stores cluster metadata. Choose one of the [supported regions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). You must use the same region that is configured in `cloudAuditLogging.clusterLocation`, `gkeConnect.location`, and `stackdriver.clusterLocation`. If `gkeOnPremAPI.enabled` is `false`, don't include this field.

## `stackdriver`

Required  
Mutable  


### `stackdriver.projectID`

Required for Logging and Monitoring  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#logging_monitoring_project). For new clusters, this project ID must be the same as the ID set in `gkeConnect.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

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

For new clusters, if you include the `gkeOnPremAPI` and `cloudAuditLogging` sections in the configuration file, the region that you set here must be the same region that you set in `cloudAuditLogging.clusterLocation`, `gkeConnect.location`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.

Example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.serviceAccountKeyPath`

Required for Logging and Monitoring  
Mutable  
String

The path of the JSON key file for your logging-monitoring service account.

If you will be creating the cluster with `enableAdvancedCluster` set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then `stackdriver.serviceAccountKeyPath` must be the same as `cloudAuditLogging.serviceAccountKeyPath`.

For information on how to update this field in an existing cluster, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    stackdriver:
      serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
    

### `stackdriver.disableVsphereResourceMetrics`

Optional  
Mutable  
Relevant for Logging and Monitoring  
Boolean  
Prepopulated: false  
Default: false

Set this to `true` to disable the collection of metrics from vSphere. Otherwise, set it to `false`.

This section is required in the admin cluster if you want to manage the lifecycle of [user clusters in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

Example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in this section. Otherwise, remove this section or leave it commented out.  
Mutable  


This section is required in the admin cluster if you want to manage the lifecycle of [user clusters in using GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

### `cloudAuditLogging.projectID`

Required for Cloud Audit Logs  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). For new clusters, this project ID must be the same as the ID set in `gkeConnect.projecID` and `stackdriver.projectID`. If the project IDs aren't the same, cluster creation fails. This requirement isn't applied to existing clusters.

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

If you will be creating the cluster with `enableAdvancedCluster` set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then `cloudAuditLogging.serviceAccountKeyPath` must be the same as `stackdriver.serviceAccountKeyPath`.

For information on how to update this field in an existing cluster, see [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

Example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## `clusterBackup.datastore`

Optional  
Mutable  
String

By default, cluster backup tar files are saved to the directory `gkectl-workspace/backups` on your admin workstation. If you want to store cluster backup files in vSphere, set this field to the vSphere datastore where you want to save the backups.

Example:
    
    
    clusterBackup:
      datastore: "my-datastore"
    

Note the following support differences for this field:

  * For advanced clusters:

    * Version 1.31: remove `clusterBackup.datastore` from your configuration file. Backing up clusters to a vSphere datastore isn't supported.

    * Version 1.32: `clusterBackup.datastore` is in Preview

    * Version 1.33 and higher: `clusterBackup.datastore` is GA.

  * For non-advanced clusters, `clusterBackup.datastore` remains in Preview.




For more information see the following:

  * Non-advanced clusters: [Back up and restore an admin cluster with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl)

  * Advanced clusters: [Back up and restore advanced clusters with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl)




## `autoRepair.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable [node auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair). Otherwise, set this to `false`.

To update the value of this field, use `gkectl update admin`.

Example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to encrypt Secrets without the need for an external KMS (Key Management Service), or any other dependencies, fill in this section. Otherwise, remove this section or leave it commented out.  
Immutable

If you will be creating the cluster with `enableAdvancedCluster` set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then remove this section. This feature isn't supported with advanced clusters.

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

An integer of your choice to use for the key version number. We recommended that you start with `1`.

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

Example:
    
    
    secretsEncryption:
      generatedKey:
        disabled: false
    

## `osImageType`

Optional  
Mutable  
String  
Possible values: For versions 1.34 and previous: "ubuntu_containerd", "cos"  
For 1.35 and newer: "ubuntu_cgv2", "cos_cgv2"  
Prepopulated: "ubuntu_cgv2"  
Default: "ubuntu_containerd"

The type of OS image to run on your admin cluster nodes.

Note the following limitation with advanced clusters:

  * Version 1.31: if the `enableAdvancedCluster` field is `true`, only `ubuntu-cgroupv2` and `ubuntu_containerd` are supported on advanced clusters.

  * Version 1.32: All OS image types are supported on advanced clusters.




**Note:** In versions 1.32 and lower, full bundles don't include cgroup v2 OS images. If you specify `ubuntu_cgv2` or `cos_cgv2`, you must use a regular bundle. For details, see [About Google Distributed Cloud bundles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles).

Example:
    
    
    osImageType: "cos_cgv2"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
