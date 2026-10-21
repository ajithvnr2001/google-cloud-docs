---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-configuration-file/
title: User cluster configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:54.423964+00:00
---

# User cluster configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-configuration-file/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  User cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

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

`VERSION`: the desired version number. For example: `gkectl create-config cluster --gke-on-prem-version=1.9.0-gke.8`.

**Warning:** The generated template incorrectly lists the `gkeConnect` section as optional. The `gkeConnect` section is required.

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
    # (Required) Load balancer configuration
    loadBalancer:
      # (Required) The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlPlaneVIP: ""
        # Shared by all services for ingress traffic
        ingressVIP: ""
      # (Required) Which load balancer to use "F5BigIP" "Seesaw" or "ManualLB". Uncomment
      # the corresponding field below to provide the detailed spec
      kind: Seesaw
      # # (Required when using "ManualLB" kind) Specify pre-defined nodeports
      # manualLB:
      #   # NodePort for ingress service's http (only needed for user cluster)
      #   ingressHTTPNodePort: 30243
      #   # NodePort for ingress service's https (only needed for user cluster)
      #   ingressHTTPSNodePort: 30879
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
    # # (Optional) Enable dataplane v2
    # enableDataplaneV2: false
    # (Optional/Preview) Enable anthos network gateway
    enableAnthosNetworkGateway: false
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
    # (Optional) Specify which GCP project to connect your GKE clusters to
    gkeConnect:
      projectID: ""
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerServiceAccountKeyPath: ""
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

String. A name of your choice for your user cluster. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



For example:
    
    
    name: "my-user-cluster"
    

## `gkeOnPremVersion`

String. The Google Distributed Cloud version for your user cluster. For example:
    
    
    gkeOnPremVersion: "1.9.0-gke.1"
    

## `vCenter`

If you want all aspects of your vCenter environment to be the same as what you specified for your admin cluster, remove this section or leave it commented out.

If you want some aspects of your vCenter environment to be different from what you specified for your admin cluster, fill in the relevant fields in this section. Any fields that you set here in the `vCenter` section override the corresponding fields in your admin cluster configuration file.

### `vCenter.datacenter`

String. The name of the vCenter data center for your user cluster. If not specified, the cluster is created in the admin cluster data center.

For example:
    
    
    vCenter:
      datascenter: "MY-USER-DATACENTER"
    

If specified, then you must also include the `vCenter.datastore` and `vCenter.networkName` fields, and you must specify either `vCenter.cluster` or `vCenter.resourcePool`. See [Create a user cluster in a separate data center](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-user-cluster-in-separate-datacenter).

### `vCenter.resourcePool`

String. The name of the vCenter resource pool for your user cluster. If you are using a non-default resource pool, provide the name of your vCenter resource pool. For example:
    
    
    vCenter:
      resourcePool: "MY-USER-POOL"
    

If you are using the default resource pool, provide the following value:
    
    
    vCenter:
      resourcePool: "VSPHERE_CLUSTER/Resources"
    

Replace `VSPHERE_CLUSTER` with the name of your vSphere cluster.

See [Specifying the root resource pool for a standalone host](https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs/data-sources/resource_pool).

If not specified, and if you have specified `vCenter.datacenter`, you must provide a value for `vCenter.cluster`.

### `vCenter.datastore`

String. The name of the vCenter datastore for your user cluster. For example:
    
    
    vCenter:
      datastore: "MY-USER-DATASTORE"
    

### `vCenter.cluster`

String. The name of your vSphere cluster.

For example:
    
    
    vCenter:
      cluster: USER_VSPHERE_CLUSTER
    

If `vCenter.cluster` is not specified, you must specify a value for `vCenter.resourcePool`.

### `vCenter.folder`

String. The name of the folder under the vCenter.datacenter`.

For example:
    
    
    vCenter:
      folder: USER_FOLDER
    

### `vCenter.caCertPath`

String. When a client, like GKE on-prem, sends a request to your vCenter server, the server must prove its identity to the client by presenting a certificate or a certificate bundle. To verify the certificate or bundle, GKE on-prem must have the root certificate in the chain of trust.

Set `vCenter.caCertPath` to the path of the root certificate. For example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/user-vcenter-ca-cert.pem"
    

Your VMware installation has a certificate authority (CA) that issues a certificate to your vCenter server. The root certificate in the chain of trust is a self-signed certificate created by VMware.

If you do not want to use the VMWare CA, which is the default, you can configure VMware to use a different certificate authority.

If your vCenter server uses a certificate issued by the default VMware CA, download the certificate as follows:
    
    
    curl -k "https://SERVER_ADDRESS/certs/download.zip" > download.zip
    

Replace `SERVER_ADDRESS` with the address of your vCenter server.

Install the `unzip` command and unzip the certificate file:
    
    
    sudo apt-get install unzip
    unzip downloads.zip
    

If the `unzip` command doesn't work the first time, enter the command again.

Find the certificate file in `certs/lin`.

If your certificate changes, you can [update the reference to the new certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/update-vcenter-certificate).

### `vCenter.credentials.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account should have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vsphere-requirements-basic). For example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-directory/user-creds.yaml"
    

### `vCenter.credentials.fileRef.entry`

String. The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account. For example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vcenter-creds"
    

### `vCenter.folder`

String. The name of the vCenter folder where your cluster VMs will be located. For example:
    
    
    vCenter:
      folder: "MY-FOLDER"
    

## `network`

This section holds information about your user cluster network.

### `network.hostConfig`

This section holds information about NTP servers, DNS servers, and DNS search domains used by your cluster.

If you provided a value for one or both of the following fields, then fill in this section. Otherwise, remove this section.

  * `loadBalancer.seesaw.ipBlockFilePath`
  * `network.ipMode.ipBlockFilePath`

**Important:** If you include `network.hostConfig` in the admin cluster configuration file, then the entire `hostconfig` section of the [`ipBlockfile`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file) will be ignored.

#### `network.hostConfig.dnsServers`

Array of strings. The addresses of DNS servers for the hosts to use. For example:
    
    
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
    

#### `network.hostConfig.ntpServers`

Array of strings. The addresses of time servers for the hosts to use. For example:
    
    
    network:
      hostConfig:
        ntpServers:
        - "216.239.35.0"
    

#### `network.hostConfig.searchDomainsForDNS`

Array of strings. DNS search domains for the hosts to use. These domains are used as part of a domain search list. For example:
    
    
    network:
      hostConfig:
        searchDomainsForDNS:
        - "my.local.com"
    

### `network.ipMode.type`

String. If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`. For example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

If you set `ipMode.type` to `"static"`, fill in this field. If you set `ipMode.type` to `"dhcp"`, remove this field.

String. The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file) for your cluster. For example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/user-cluster-ipblock.yaml"
    

### `network.serviceCIDR` and `network.podCIDR`

Strings. Your user cluster must have a range of IP addresses to use for Services and a range of IP addresses to use for Pods. These ranges are specified by the `network.serviceCIDR` and `network.podCIDR` fields. These fields are populated with default values. If you like, you can change the populated values to values of your choice.

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

Example:
    
    
    network:
      serviceCIDR: "10.96.0.0/20"
      podCIDR: "192.168.0.0/16"
    

### `network.vCenter.networkName`

String. The name of the vSphere network for your user cluster nodes.

If the name contains a special character, you must use an escape sequence for it.

Special characters | Escape sequence  
---|---  
Slash (`/`) | `%2f`  
Backslash (`\`) | `%5c`  
Percent sign (`%`) | `%25`  
  
If the network name is not unique, it is possible to specify a path to the network, such as /DATACENTER/network/NETWORK_NAME.

For example:
    
    
    network:
      vCenter:
        networkName: "MY-USER-CLUSTER-NETWORK"
    

## `loadBalancer`

This section holds information about the load balancer for your user cluster.

### `loadBalancer.vips.controlPlaneVIP`

The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. For example:
    
    
    loadBalancer:
      vips:
        controlplaneVIP: "203.0.113.3"
    

### `loadBalancer.vips.ingressVIP`

The IP address that you have chosen to configure on the load balancer for ingress traffic. For example:
    
    
    loadBalancer:
      vips:
        ingressVIP: "203.0.113.4"
    

### `loadBalancer.kind`

String. Set this to `"Seesaw"`, `"F5BigIP"`, or `"ManualLB"` For example:
    
    
    loadBalancer:
      kind: "Seesaw"
    

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"manualLB"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.manualLB.ingressHTTPNodePort`

Integer. The ingress service in a user cluster is implemented as a [Kubernetes Services of type `LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer). The Service has a [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) for HTTP. You must choose a `nodePort` value for the HTTP ServicePorts.

Set this field to the `nodePort` value. For example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPNodePort: 32527
    

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Integer. The ingress service in a user cluster is implemented as a Service of type LoadBalancer. The Service has a ServicePort for HTTPS. You must choose a `nodePort` value for the HTTPS ServicePort.

Set this field to the `nodePort` value. For example:
    
    
    loadBalancer:
      manualLB:
        ingressHTTPSNodePort: 30139
    

#### `loadBalancer.manualLB.controlPlaneNodePort`

Integer. The Kubernetes API server in the admin cluster is implemented as a Service of type `NodePort`. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value. For example:
    
    
    loadBalancer:
      manualLB:
        controlPlaneNodePort: 30968
    

#### `loadBalancer.manualLB.addonsNodePort`

Remove this field. It is not used in a user cluster.

### `loadBalancer.f5BigIP`

If you set `loadbalancer.kind` to `"f5BigIP"`, fill in this section. Otherwise, remove this section or leave it commented out.

#### `loadBalancer.f5BigIP.address`

String. The address of your F5 BIG-IP load balancer. For example:
    
    
    loadBalancer:
      f5BigIP:
          address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

Example:
    
    
    loadBalancer:
      f5BigIP:
        fileRef:
          path: ""my-config-folder/user-creds.yaml"
    

#### `loadBalancer.f5BigIP.fileRef.entry`

String. The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account. For example:
    
    
    loadBalancer:
      f5BigIP:
        fileRef:
          entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

String. The name of a BIG-IP partition that you created for your admin cluster. For example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

String. If you are using SNAT, the name of your SNAT pool. If you are not using SNAT, remove this field or leave it commented out. For example:
    
    
    loadBalancer:
      f5BigIP:
        snatPoolName: "my-snat-pool"
    

### `loadBalancer.seesaw`

If you set `loadbalancer.kind` to `"Seesaw"`, fill in this section. Otherwise, remove this section.

For information on setting up the Seesaw load balancer, see [Seesaw load balancer quickstart](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/seesaw-load-balance-quickstart) and [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/bundled-load-balance).

#### `loadBalancer.seesaw.ipBlockFilePath`

String. Set this to the path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file) for your Seesaw VMs. For example:
    
    
    loadBalancer:
      seesaw:
        ipBlockFilePath: "config-folder/admin-seesaw-ipblock.yaml"
    

#### `loadBalancer.seesaw.vrid`

Integer. The [virtual router identifier](https://datatracker.ietf.org/doc/html/rfc5798) of your Seesaw VM. This identifier, which is an integer of your choice, must be unique in a VLAN. Valid range is 1-255. For example:
    
    
    loadBalancer:
      seesaw:
        vrid: 125
    

#### `loadBalancer.seesaw.masterIP`

String. The virtual IP address configured on your [Master Seesaw VM](https://datatracker.ietf.org/doc/html/rfc5798#section-1). For example:
    
    
    loadBalancer:
      seesaw:
        masterIP: 172.16.20.21
    

#### `loadBalancer.seesaw.cpus`

Integer. The number of CPUs for each of your Seesaw VMs. For example:
    
    
    loadBalancer:
      seesaw:
        cpus: 8
    

#### `loadBalancer.seesaw.memoryMB`

Integer. The number of mebibytes of memory for each of your Seesaw VMs. For example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

#### `loadBalancer.seesaw.vCenter.networkName`

String. The name of the vCenter network that contains your Seesaw VMs. For example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

#### `loadBalancer.seesaw.enableHA`

Boolean. If you want to create a highly-available Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs. For example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

#### `loadBalancer.seesaw.disableVRRPMAC`

Boolean. If you set this to `true`, the Seesaw load balancer does not use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. We recommend that you set this to `true`. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`. For example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

## `enableDataplaneV2`

Boolean. If you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2), set this to `true`. Otherwise set this to `false`. For example:
    
    
    enableDataplaneV2: true
    

Dataplane V2 is only available in user clusters.

See [Dataplane V2 Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting) for troubleshooting steps.

## `enableWindowsDataplaneV2`

Boolean. Preview.

If you want to enable [Windows Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for a cluster with Windows nodes, set this to `true`. Otherwise set this to `false`. For example:
    
    
    enableWindowsDataplaneV2: true
    

Windows Dataplane V2 is only available in user clusters.

See [Dataplane V2 Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting) for troubleshooting steps. See [User guide for Windows Server OS node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9//how-touser-guide-for-windows-server-os-node-pools) to set up node pools containing Windows Server OS nodes.

## `enableAnthosNetworkGateway`

Boolean. Preview.

If you want to enable Anthos network gateway, set this to `true`. Otherwise, set it to `false`. You must set this to `true` if you want to configure an [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/egress-nat-gateway). For example:
    
    
    enableAnthosNetworkGateway: true
    

## `masterNode`

This section holds information about the nodes, in the admin cluster, that serve as control plane nodes for your user cluster.

## masterNode.vsphere.datastore

String. The datastore for the user control plane node for this user cluster. For example:
    
    
    masterNode:
       vsphere:
          datastore: USER_MASTER_DATASTORE
    

By default, if unspecified, this value defaults to the user cluster datastore when the user cluster uses the admin cluster datacenter.

If the user cluster uses a different datacenter, this field is required, and no default is applied.

### `masterNode.cpus`

Integer. The number of CPUs for each admin cluster node that serve as control planes for this user cluster. For example:
    
    
    masterNode:
      cpus: 8
    

### `masterNode.memoryMB`

Integer. The mebibytes of memory for each admin cluster node that serves as a control plane for this user cluster. Must be a multiple of 4. For example:
    
    
    masterNode:
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `masterNode.replicas`

Integer. The number of control plane nodes for this user cluster. Set this field to 1 or 3. For example:
    
    
    masterNode:
      replicas: 3
    

### `masterNode.autoResize.enabled`

Boolean. Set this to `true` to enable automatic resizing of the control-plane nodes for the user cluster. Note that the control-plane nodes for the user cluster are in the admin cluster. For example:
    
    
    masterNode:
      autoResize:
        enabled: true
    

### `masterNode.vsphere.datastore`

String. The datastore where the master nodes will be created. For example:
    
    
    masterNode:
      vSphere:
        datastore: "MY-DATASTORE"
    

## `nodePools`

Array of objects, each of which describes a node pool.

### `nodePools[i].name`

String. A name of your choice for the node pool. The name must:

  * contain at most 40 characters
  * contain only lowercase alphanumeric characters or a hyphen (`-`)
  * start with an alphabetic character
  * end with an alphanumeric character



For example:
    
    
    nodePools:
    - name: "my-node-pool"
    

### `nodePools[i].cpus`

Integer. The number of CPUs for each node in the pool. For example:
    
    
    nodePools"
    - name: "my-node-pool"
      cpus: 8
    

### `nodePools[i].memoryMB`

Integer. The mebibytes of memory for each node in the pool. Must be a multiple of 4. For example:
    
    
    nodePools"
    - name: "my-node-pool"
      memoryMB: 8192
    

**Note:** This field specifies the number of mebibytes of memory, not the number of megabytes. One mebibyte is 2^20 = 1,048,576 bytes. One megabyte is 10^6 = 1,000,000 bytes.

### `nodePools[i].replicas`

Integer. The number of nodes in the pool. For example:
    
    
    nodePools:
    - name: "my-node-pool"
      replicas: 5
    

### `nodePools[i].bootDiskSizeGB`

Integer. The size of the boot disk in gigabytes for each node in the pool. This configuration is available starting from Google Distributed Cloud version 1.5.0. For example:
    
    
    nodePools
    - name: "my-node-pool"
      bootDiskSizeGB: 40
    

### `nodePools[i].osImageType`

String. The type of OS image to run on the VMs in the node pool. Possible values are "ubuntu_containerd", "ubuntu", and "cos". For example:
    
    
    nodePools
    - name: "my-node-pool"
      osImageType: "ubuntu_containerd"
    

### `nodePools[i].labels`

Mapping. Labels to apply to each node in the pool. For example:
    
    
    nodePools:
    - name: "my-node-pool"
      labels:
        environment: "production"
        tier: "cache"
    

### `nodePools[i].taints`

Array of objects, each of which describes a taint. For example:
    
    
    nodePools:
    - name: "my-node-pool"
      taints:
      - key: "staging"
        value: "true"
        effect: "NoSchedule"
    

### `nodePools[i].vsphere.datastore`

String. The name of the vCenter datastore on which each node in the pool will be created. For example:
    
    
    nodePools:
    - name: "my-node-pool"
      vsphere:
        datastore: "my-datastore"
    

### `nodePools[i].vsphere.tags`

Array of objects, each of which describes a [vSphere tag](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html) to be placed on VMs in the node pool. Each tag has a category and a name. For example:
    
    
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

Preview.

If you want to enable automatic scaling for the node pool, fill in this section. Otherwise, remove this section.

#### `nodePools[i].autoscaling.minReplicas`

Integer. The minimum number of nodes that the autoscaler can set for the pool. Must be at least 1. For example:
    
    
    nodePools:
    - name: "my-node-pool"
      autoscaling:
        minReplicas: 5
    

#### `nodePools.autoscaling.maxReplicas`

Integer. The maximum number of nodes that the autoscaler can set for the pool.
    
    
    nodePools:
    - name: "my-node-pool"
      autoscaling:
        maxReplicas: 10
    

## `antiAffinityGroups.enabled`

Boolean. Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`. For example:
    
    
    antiAffinityGroups:
      enabled: true
    

Google Distributed Cloud automatically creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster's nodes, causing them to be spread across at least three physical hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least three physical hosts available.




Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least three hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

## `enableVMTracking`
    
    
    enableVMTracking: true
    

## `authentication`

This section holds information about how cluster users are authenticated and authorized.

### `authentication.oidc`

Do not use this section. Instead, after cluster creation, edit the ClientConfig custom resource as described in [Configuring clusters for Anthos Identity Service with OIDC ](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

### `authentication.sni`

If you want to provide an additional serving certificate for the cluster's Kubernetes API server, fill in this section. Otherwise, remove this section or leave it commented out.

#### `authentication.sni.certPath`

String. The path to a serving certificate for the Kubernetes API server. For example:
    
    
    authentication:
      sni:
        certPath: "my-cert-folder/example.com.crt"
    

#### `authentication.sni.keyPath`

String. Path to the certificate's private key file. For example:
    
    
    authentication:
      sni:
        keyPath: "my-cert-folder/example.com.key"
    

## `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/concepts/logging-and-monitoring) for your cluster, fill in this section. Otherwise delete it or leave it commented out.

### `stackdriver.projectID`

String. The ID of the Google Cloud project where you want to view logs. For example:
    
    
    stackdriver:
      projectID: "my-logs-project"
    

### `stackdriver.clusterLocation`

String. The Google Cloud region where you want to store logs. It is a good idea to choose a region that is near your on-premises data center. For example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.enableVPC`

Boolean. If your cluster's network is controlled by a [VPC](https://docs.cloud.google.com/vpc), set this to this field to`true`. This ensures that all telemetry flows through Google's restricted IP addresses. Otherwise, set this field to `false`. For example:
    
    
    stackdriver:
      enableVPC: false
    

### `stackdriver.serviceAccountKeyPath`

String. The path of the JSON key file for your logging-monitoring service account. For example:
    
    
    stackdriver:
      serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
    

### `stackdriver.disableVsphereResourceMetrics`

Boolean. Set this to `true` to disable the collection of metrics from vSphere. Otherwise, set it to `false`. For example:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

## `gkeConnect`

This section holds information about the Google Cloud project and service account you want to use to [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet.

This section is required.

### `gkeConnect.projectID`

String. The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/multiple-gcp-projects#fleet_host_project). For example:
    
    
    gkeConnect:
      projectID: "my-connect-project-123"
    

### `gkeConnect.registerServiceAccountKeyPath`

String. The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/service-accounts#connect_register_service_account). For example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

## `usageMetering`

If you want to enable usage metering for your cluster, then fill in this section. Otherwise, remove this section or leave it commented out.

### `usageMetering.bigQueryProjectID`

String. The ID of the Google Cloud project where you want to store usage metering data. For example:
    
    
    usageMetering:
      bigQueryProjectID: "my-bq-project"
    

### `usageMetering.bigQueryDatasetID`

String. The ID of the BigQuery dataset where you want to store usage metering data. For example:
    
    
    usageMetering:
      bigQueryDatasetID: "my-bq-dataset"
    

### `usageMetering.bigQueryServiceAccountKeyPath`

String. The path of the JSON key file for your BigQuery service account. For example:
    
    
    usageMetering:
      bigQueryServiceAccountKeyPath: "my-key-folder/bq-key.json"
    

### `usageMetering.enableConsumptionMetering`

Boolean. Set this to `true` if you want to enable consumption-based metering. Otherwise set this to false. For example:
    
    
    usageMetering:
      enableConsumptionMetering: true
    

## `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in this section. Otherwise, remove this section or leave it commented out.

### `cloudAuditLogging.projectID`

String. The project ID of the Google Cloud project where you want to store audit logs. For example:
    
    
    cloudAuditLogging:
      projectID: "my-audit-project"
    

### `cloudAuditLogging.clusterLocation`

String. The Google Cloud region where you want to store audit logs. It is a good idea to choose a region that is near your on-premises data center. For example:
    
    
    cloudAuditLogging:
      clusterLocation: "us-central1"
    

### `cloudAuditLogging.serviceAccountKeyPath`

String. The path of the JSON key file for your audit-logging service account. For example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## `autoRepair.enabled`

Boolean. Set this to `true` to enable node auto repair. Otherwise, set it to `false`. For example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to encrypt secrets without the need for an external KMS (Key Management Service), or any other dependencies, make sure this section is filled out. Otherwise, remove or comment out this section.

### `secretsEncryption.mode`

String. Secret encryption mode. Set this to `"GeneratedKey"`.
    
    
    secretsEncryption:
      mode: "GeneratedKey"
    

### `secretsEncryption.generatedKey.keyVersion`

Integer. An integer of your choice to use for the key version number. It's recommended that you start with `1`. For example:
    
    
    secretsEncryption:
      generatedKey:
        keyVersion: 1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
