---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file/
title: Admin cluster configuration file \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:13.303623+00:00
---

# Admin cluster configuration file  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Admin cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/admin-cluster-configuration-file)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/admin-cluster-configuration-file)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes the fields in the admin cluster configuration file for Google Distributed Cloud.

## Generating a template for your configuration file

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your admin cluster configuration file. Also, `gkeadm` filled in some of the fields for you.

If you did not use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your admin cluster configuration file.

To generate a template for your admin cluster configuration file:
    
    
    gkectl create-config admin --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace `OUTPUT_FILENAME` with a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `admin-cluster.yaml` and puts it in the current directory.

Replace `VERSION` with the desired version number, which must be equal to or less than your `gkectl` version. For example: `gkectl create-config admin --gke-on-prem-version=1.6.2-gke.0`. If you omit this flag, the generated config template is populated with values based on the latest cluster version.

**Template**

Click to see the generated template.
    
    
    apiVersion: v1
    kind: AdminCluster
    # (Optional) A unique name for this admin cluster. This will default to a random name
    # prefixed with 'gke-admin-'
    name: ""
    # (Required) Absolute path to a GKE bundle on disk
    bundlePath: ""
    # (Required) vCenter configuration
    vCenter:
      address: ""
      datacenter: ""
      cluster: ""
      # Resource pool to use. Specify [VSPHERE_CLUSTER_NAME]/Resources to use the default
      # resource pool
      resourcePool: ""
      datastore: ""
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
      # (Required when adminMaster.Replicas is not 3) Provide the name for the persistent
      # disk to be used by the deployment (ending in .vmdk). Any directory in the supplied
      # path must be created before deployment. Required for non-HA admin cluster. Invalid
      # for HA admin cluster as the path is generated automatically under the root directory
      # "anthos" in the specified datastore.
      dataDisk: ""
    # (Required) Network configuration
    network:
      # # (Required when using "static" ipMode.type; or "Seesaw" loadBalancer.kind; or using
      # # amdin cluster HA mode) This section overrides ipMode.ipBlockFilePath values when
      # # ipMode.type=static. It's also used for seesaw nodes
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
        # (Required) Define what IP mode to use ("dhcp" or "static")
        type: dhcp
        # # (Required when using "static" mode) The absolute or relative path to the yaml file
        # # to use for static IP allocation. Hostconfig part will be overwritten by network.hostconfig
        # # if specified
        # ipBlockFilePath: ""
      # (Required) The Kubernetes service CIDR range for the cluster. Must not overlap
      # with the pod CIDR range
      serviceCIDR: 10.96.232.0/24
      # (Required) The Kubernetes pod CIDR range for the cluster. Must not overlap with
      # the service CIDR range
      podCIDR: 192.168.0.0/16
      vCenter:
        # vSphere network name
        networkName: ""
      # # (Preview/Required when setting adminMaster.replicas to 3 for HA admin cluster) Specify
      # # the IPs to use for control plane machines for HA admin cluster. NOTE: HA admin cluster
      # # is in Preview
      # controlPlaneIPBlock:
      #   netmask: ""
      #   gateway: ""
      #   ips:
      #   - ip: ""
      #     hostname: ""
    # (Required) Load balancer configuration
    loadBalancer:
      # (Required) The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlPlaneVIP: ""
        # # (Optional) Used for the in-cluster Prometheus and Grafana stack to route user cluster
        # # metrics back to the admin cluster
        # addonsVIP: ""
      # (Required) Which load balancer to use "F5BigIP" "Seesaw" "ManualLB" or "MetalLB".
      # Uncomment the corresponding field below to provide the detailed spec
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
      #   # # (Optional) NodePort for addon service (only needed for admin cluster Prometheus
      #   # # and Grafana federation feature)
      #   # addonsNodePort: 31405
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
      #   cpus: 2
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
    # Spread admin addon nodes and user masters across different physical hosts (requires
    # at least three hosts)
    antiAffinityGroups:
      # Set to false to disable DRS rule creation
      enabled: true
    # # (Optional/Preview) Specify the admin master node configuration which can be added
    # # or edited only during cluster creation (default: 4 CPUs; 16384 MB memory; 1 replica)
    # adminMaster:
    #   cpus: 4
    #   memoryMB: 16384
    #   # How many machines of this type to deploy
    #   replicas: 1
    # # Specify the addon node configuration which can be added or edited only during cluster
    # # creation
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
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerServiceAccountKeyPath: ""
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
      # (Optional) Disable vsphere resource metrics collection from vcenter.  False by
      # default
      disableVsphereResourceMetrics: false
    # # (Optional) Configure kubernetes apiserver audit logging
    # cloudAuditLogging:
    #   # The project ID for logs and metrics. It should be the same with gkeconnect.projectID.
    #   projectID: ""
    #   # A GCP region where you would like to store audit logs for this cluster.
    #   clusterLocation: ""
    #   # The absolute or relative path to the key file for a GCP service account used to
    #   # send audit logs from the cluster
    #   serviceAccountKeyPath: ""
    # # (Optional/Preview) Configure backups for admin cluster. Backups will be stored under
    # # /anthos-backups/. Not supported for HA admin cluster.
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
    # or "cos". Default is "ubuntu_containerd".
    osImageType: ""
    # # (Optional) Storage specification for the cluster
    # storage:
    

## Filling in your configuration file

In your configuration file, enter field values as described in the following sections.

## `name`

Optional  
String  
Default: A random name with prefix "gke-admin-"

A name of your choice for the cluster.

Example:
    
    
    name: "my-admin-cluster"
    

## `bundlePath`

Required  
Mutable  
String

The path of your Google Distributed Cloud bundle file.

The Google Distributed Cloud full bundle file contains all of the components in a particular release of Google Distributed Cloud. When you create an admin workstation, it comes with a full bundle at:
    
    
    /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz
    

Example:
    
    
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.10.0-gke.8.full.tgz"
    

## `vCenter`

Required  
Immutable  


This sections holds information about your vSphere environment and your connection to vCenter Server.

### `vCenter.address`

Required  
Immutable  
String

The IP address or the hostname of your vCenter server.

For more information, see [Finding your vCenter server address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vcenter-server-address).

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
    

If your resource pool is nested under another resource pool, set this to the full path to your resource pool.

Example:
    
    
    vCenter:
      resourcePool: "my-vsphere-cluster/Resources/parent-resource-pool/child-resource-pool"
    

### `vCenter.datastore`

Required  
Immutable  
String

The name of a [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) for your admin cluster.

The value you specify must be a name, not a path. Do not include any folders in the value.

Example:
    
    
    vCenter:
      datastore: "my-datastore"
    

### `vCenter.caCertPath`

Required  
Mutable  
String

The path of the CA certificate for your vCenter server.

For more information, see [Getting your vCenter CA certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vcenter-ca-cert-path).

For information about updating this field for an existing cluster, see [Update vCenter certificate references](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate).

Example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert.pem"
    

### `vCenter.credentials.fileRef.path`

Required  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account should have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements-basic).

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `vCenter.credentials.fileRef.entry`

Required  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your vCenter credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

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
    

If your vm folder is nested under another vm folder, set this to the full path to your vm folder.

Example:
    
    
    vCenter:
      folder: "/my-datacenter/vm/vm-folder/nested-vm-folder"
    

Note that you must include the first "/" in your vm folder full path.

### `vCenter.dataDisk`

Required  
Immutable  
String

Google Distributed Cloud creates a virtual machine disk (VMDK) to hold Kubernetes object data. The installer creates the VMDK for you, but you must provide a relative path for the VMDK in the `vCenter.dataDisk` field.

The value you specify is relative to `/.../DATA_CENTER/datastore/`.

If you want the VMDK to be in the `/.../DATA_CENTER/datastore/` folder, the value is the name of the VMDK.

If you set `adminMaster.replicas` to `3`, then you must NOT set this field. For HA admin cluster, the data disk paths for the 3 admin control plane machines will be auto generated under `/anthos/ADMIN_CLUSTER/default/``.

Example:
    
    
    vCenter:
      dataDisk: "my-disk.vmdk"
    

Otherwise, the value is a relative path that includes one or more folders along with the VMDK name.

Example:
    
    
    vCenter:
      dataDisk: "data-disks/data-disk-1.vmdk"
    

If you are using a vSAN datastore, the VMDK must be in a folder that you have already created.

You can use `govc` to create a folder:
    
    
    govc datastore.mkdir -namespace=true data-disks
    

**Important:** Do not put a forward slash in front of the folder name.

## `network`

Required  
Immutable  


This section holds information about your admin cluster network.

### `network.hostConfig`

Immutable  


This section is required if one or more of the following are true:

  * `network.ipMode.type` is set to `"static"`
  * `loadBalancer.kind` is set to `"Seesaw"`
  * `adminMaster.replicas` is set to `3`



This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes. If you are using the Seesaw load balancer, this information also applies to your Seesaw VMs.

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
        ipBlockFilePath: "/my-config-folder/admin-cluster-ipblock.yaml"
    

### `network.serviceCIDR`

Required  
Immutable  
String  
Smallest possible range: /24  
Largest possible range: /12  
Prepopulated: "10.96.232.0/24"  
Default: "10.96.232.0/24"

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
Default: "192.168.0.0/16"

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

Required  
Immutable  
String

The name of the vSphere network for your cluster nodes.

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

Preview

If you want to create a high-availability admin cluster, fill in this section. Otherwise, remove this section or leave it commented out.

A high-availability admin cluster has three nodes that run control-plane components.

If you fill in this section, you must also set `adminMaster.replicas` to `3`.

#### `network.controlPlaneIPBlock.netmask`

Preview  
Required for a high-availability control plane  
Immutable  
String

The netmask for the network that has your control-plane nodes.

Example:
    
    
    network:
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
    

#### `network.controlPlaneIPBlock.gateway`

Preview  
Required for a high-availability control plane  
Immutable  
String

The IP address of the default gateway for your control-plane nodes.

Example:
    
    
    network:
      controlPlaneIPBlock:
        gateway: "172.16.22.1"
    

#### `network.controlPlaneIPBlock.ips`

Preview  
Required for a high-availability control plane  
Immutable  
Array of three objects, each of which has an IP address and an optional hostname.

These are the IP addresses that will be assigned to your control-plane nodes.

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
    

### `loadBalancer.vips.addonsVIP`

Optional  
Immutable  
String

The IP address you have chosen to configure on the load balancer for the Prometheus and Grafana add-ons. User clusters use this VIP for metrics communication with the admin cluster.

Example:
    
    
    loadBalancer:
      vips:
        addonsVIP: "203.0.113.4"
    

### `loadBalancer.kind`

Required  
Immutable  
String  
Prepopulated: "MetalLB"

String. Set this to `"ManualLB"`, `"F5BigIP"`, `"Seesaw"`, or `"MetalLB"`

If you set `adminMaster.replicas` to `3`, then you cannot use the Seesaw load balancer.

Example:
    
    
    loadBalancer:
      kind: "MetalLB"
    

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"ManualLB"`, fill in this section. Otherwise, remove this section.  
Immutable  


#### `loadBalancer.manualLB.ingressHTTPNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.konnectivityServerNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.controlPlaneNodePort`

Required if `loadBalancer.kind` = `"ManualLB"` and `adminMaster.replicas` = `1`  
Immutable  
Integer  
Prepopulated: 30968

The Kubernetes API server in the admin cluster is exposed by a Kubernetes Service. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value.

For example:
    
    
    loadBalancer:
      manualLB:
        controlPlaneNodePort: 30968
    

#### `loadBalancer.manualLB.addonsNodePort`

Required if `loadBalancer.kind` = `"ManualLB"`  
Immutable  
Integer  
Prepopulated: 31405

The add-ons server in the admin cluster is exposed by a Kubernetes Service. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value.

Example:
    
    
    loadBalancer:
      manualLB:
        addonsNodePort: 31405
    

### `loadBalancer.f5BigIP`

If you set `loadbalancer.kind` to `"f5BigIP"`, fill in this section. Otherwise, remove this section.

#### `loadBalancer.f5BigIP.address`

Required if `loadBalancer.kind` = `"f5BigIp"`  
Immutable  
String

The address of your F5 BIG-IP load balancer. For example:
    
    
    loadBalancer:
      f5BigIP:
        address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.path`

Required if `loadBalancer.kind` = `"f5BigIp"`  
Mutable  
String

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: ""my-config-folder/admin-creds.yaml"
    

#### `loadBalancer.f5BigIP.credentialsfileRef.entry`

Required if `loadBalancer.kind` = `"f5BigIp"`  
Mutable  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account.

You can use `gkectl update` to update this field in an existing cluster.

For information on how to update your F5 BIG-IP credentials, see [Updating cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

Required if `loadBalancer.kind` = `"f5BigIp"`  
Immutable  
String

The name of a BIG-IP partition that you created for your admin cluster.

Example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

Optional  
Relevant if `loadBalancer.kind` = `"f5BigIp"`  
Immutable  
String

If you are using SNAT, the name of your SNAT pool. If you are not using SNAT, remove this field.

Example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

If you set `loadbalancer.kind` to `"Seesaw"`, fill in this section. Otherwise, remove this section.  
Immutable  


For information on setting up the Seesaw load balancer, see [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance).

#### `loadBalancer.seesaw.ipBlockFilePath`

Required if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
String

The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/admin-seesaw-ipblock.yaml"
    

#### `loadBalancer.seesaw.vrid`

Required if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
Integer  
Possible values: 1 - 255

The [virtual router identifier](https://datatracker.ietf.org/doc/html/rfc5798) of your Seesaw VM. This identifier, which is an integer of your choice, must be unique in a VLAN.

Example:
    
    
    loadBalancer:
      seesaw:
        vrid: 125
    

#### `loadBalancer.seesaw.masterIP`

Required if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
Integer

String. The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1).

Example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

#### `loadBalancer.seesaw.cpus`

Required if `loadBalancer.kind` = `"Seesaw"`  
Mutable  
Integer  
Prepopulated: 2  
Default: 

The number of CPUs for each of your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        cpus: 8
    

#### `loadBalancer.seesaw.memoryMB`

Required if `loadBalancer.kind` = `"Seesaw"`  
Mutable  
Integer  
Prepopulated: 3072 Default: 1024

The number of mebibytes of memory for each of your Seesaw VM.

Example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

#### `loadBalancer.seesaw.vCenter.networkName`

Optional  
Relevant if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
String

The name of the vCenter network that contains your Seesaw VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

#### `loadBalancer.seesaw.enableHA`

Optional  
Relevant if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
Boolean  
Prepopulated: false  
Default: false

If you want to create a highly-available (HA) Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs.

Example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

#### `loadBalancer.seesaw.disableVRRPMAC`

Optional  
Relevant if `loadBalancer.kind` = `"Seesaw"`  
Immutable  
Boolean  
Prepopulatd: false  
Default: false

If you set this to `true`, the Seesaw load balancer does not use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. We recommend that you set this to `true`. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`.

Example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

## `antiAffinityGroups.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`.

Example:
    
    
    antiAffinityGroups:
      enabled: true
    

If this field is `true`, Google Distributed Cloud creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster nodes, causing them to be spread across at least three physical ESXi hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least four ESXi hosts available.




Even though the rule requires that the cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available. This protects you from losing your admin cluster control plane. For example, suppose you have only three ESXi hosts, and your admin cluster control-plane node is on an ESXi host that fails. The DRS rule will prevent the control-plane node from being placed on one of the remaining two ESXi hosts.

Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least four hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

## `adminMaster`

Preview  
Optional  
Immutable  


Fill in this section if you want to do any of the following:

  * Specify CPUs for the control-plane nodes of the admin cluster
  * Specify memory for the control-plane nodes of the admin cluster
  * **Preview** : Create high-availability admin cluster



Otherwise, remove this section or leave it commented out.

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

Preview  
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
    

## `addonNode.autoResize.enabled`

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

If your network is behind a proxy server, fill in this section. Otherwise, remove this section or leave it commented out.  
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

If you have a private container registry, fill in this section. Otherwise, remove this section or leave it commented out.

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

The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to access your private registry.

Example:
    
    
    privateRegistry:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `privateRegistry.credentials.fileRef.entry`

Required for private registry  
Mutable  
String

The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file), that holds the username and password of your private registry account.
    
    
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


When you fill in the `gkeConnect` section, the admin cluster is automatically registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) after it is created. This section holds information about the Google Cloud project and service account needed to register the cluster.

During cluster creation or update, several [RBAC policies](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/admin-cluster-rbac-policies) are configured on the admin cluster. These RBAC policies are needed so that you can create user clusters in the Google Cloud console.

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

Example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

## `gkeOnPremAPI`

Optional  
Available in 1.15.3 or higher.

Include this section if you want to enroll the admin cluster in the GKE On-Prem API.

Enrolling your admin cluster in the GKE On-Prem API lets you use standard tools—the Google Cloud console, the Google Cloud CLI, or [Terraform](https://www.terraform.io/)—to upgrade user clusters that the admin cluster manages. Enrolling your cluster also lets you run `gcloud` commands to [get information about your clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster#get_cluster_information).

The GKE On-Prem API stores cluster state metadata in Google Cloud. This metadata lets the API manage the lifecycle of user clusters. The standard tools use the GKE On-Prem API, and collectively they are referred to as the _GKE On-Prem API clients_. For information on using standard tools to create user clusters, see [Create a user cluster using GKE On-Prem API clients](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api). When you create user clusters using an GKE On-Prem API client, the clusters are automatically enrolled in the GKE On-Prem API.

If you set `gkeOnPremAPI.enabled` to `true`, before creating or updating the cluster using `gkectl`, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster#before_you_begin) to enable and initialize the GKE On-Prem API.

After you add this section and create or update the admin cluster, if subsequently you remove the section and update the cluster, the update will fail.

### `gkeOnPremAPI.enabled`

Required if the `gkeOnPremAPI` section is included.  
Mutable  
Boolean Prepopulated: true

Set to `true` if you want to enroll the cluster in the GKE On-Prem API.

After the cluster is enrolled in the GKE On-Prem API, if you need to unenroll the cluster, make the following change and then update the cluster:
    
    
    gkeOnPremAPI:
      enabled: false
    

### `gkeOnPremAPI.location`

Immutable  
String  
Prepopulated: "us-central1"

The Google Cloud region where the GKE On-Prem API runs and stores cluster metadata. Choose one of the [supported regions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/supported-regions-on-prem-api). We recommend that you use the same region that is configured in `stackdriver.clusterLocation`. Must be a non-empty string if `gkeOnPremAPI.enabled` is `true`. If `gkeOnPremAPI.enabled` is `false`, don't include this field.

## `stackdriver`

Required by default  
Mutable

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring) for your cluster, fill in this section. Otherwise remove this section.

This section is required by default. That is, if you don't include this section, you must include the `--skip-validation-stackdriver` flag when you run `gkectl create admin`.

This section is required in the admin cluster if you want to manage the lifecycle of [user clusters in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api).

### `stackdriver.projectID`

Required for Logging and Monitoring  
Immutable  
String

The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#logging_monitoring_project).

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

If your cluster's network is controlled by a [VPC](https://docs.cloud.google.com/vpc), set this to`true`. This ensures that all telemetry flows through Google's restricted IP addresses. Otherwise, set this to `false`.

Example:
    
    
    stackdriver:
      enableVPC: false
    

### `stackdriver.serviceAccountKeyPath`

Required for Logging and Monitoring  
Mutable  
String

The path of the JSON key file for your logging-monitoring service account.

For information on how to update this field in an existing cluster, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

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

This section is required in the admin cluster if you want to manage the lifecycle of [user clusters in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api).

Example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in this section. Otherwise, remove this section or leave it commented out.  
Mutable  


This section is required in the admin cluster if you want to manage the lifecycle of [user clusters in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api).

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

For information on how to update this field in an existing cluster, see [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## `clusterBackup.datastore`

Preview  
Optional  
Mutable  
String

If you want to enable [backing up of the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl), set this to the vSphere datastore where you want to save cluster backups.

If you set `adminMaster.replicas` to `3`, then you cannot enable this feature. So you must not set a value for this field.

Example:
    
    
    clusterBackup:
      datastore: "my-datastore"
    

## `autoRepair.enabled`

Optional  
Mutable  
Boolean  
Prepopulated: true

Set this to `true` to enable [node auto repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair). Otherwise, set this to `false`.

To update the value of this field, use `gkectl update admin`.

Example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to encrypt Secrets without the need for an external KMS (Key Management Service), or any other dependencies, fill in this section. Otherwise, remove this section or leave it commented out.  
Immutable

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
String  
Possible values: "ubuntu_containerd" or "cos"  
Prepopulated: "ubuntu_containerd"  
Default: "ubuntu_containerd"

The type of OS image to run on your admin cluster nodes.

Example:
    
    
    osImageType: "cos"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
