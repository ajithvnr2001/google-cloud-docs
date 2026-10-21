---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-cluster-configuration-file/
title: Admin cluster configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:54.557377+00:00
---

# Admin cluster configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-cluster-configuration-file/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Admin cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

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
      # (Optional) vSphere folder where cluster VMs will be located. Defaults to the the
      # datacenter wide folder if unspecified.
      folder: ""
      # Provide the name for the persistent disk to be used by the deployment (ending
      # in .vmdk). Any directory in the supplied path must be created before deployment
      dataDisk: ""
    # (Required) Network configuration
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
      serviceCIDR: 10.96.232.0/24
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
        # # (Optional) Used for admin cluster addons (needed for multi cluster features). Must
        # # be the same across clusters
        # addonsVIP: ""
      # (Required) Which load balancer to use "F5BigIP" "Seesaw" or "ManualLB". Uncomment
      # the corresponding field below to provide the detailed spec
      kind: Seesaw
      # # (Required when using "ManualLB" kind) Specify pre-defined nodeports
      # manualLB:
      #   # NodePort for ingress service's http (only needed for user cluster)
      #   ingressHTTPNodePort: 0
      #   # NodePort for ingress service's https (only needed for user cluster)
      #   ingressHTTPSNodePort: 0
      #   # NodePort for control plane service
      #   controlPlaneNodePort: 30968
      #   # NodePort for addon service (only needed for admin cluster)
      #   addonsNodePort: 31405
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
        cpus: 2
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
    # Spread admin addon nodes and user masters across different physical hosts (requires
    # at least three hosts)
    antiAffinityGroups:
      # Set to false to disable DRS rule creation
      enabled: true
    # # (Optional/Preview) Specify the admin master node configuration which can be added
    # # or edited only during cluster creation
    # adminMaster:
    #   # Number of cpus
    #   cpus: 4
    #   # Memory size in MB
    #   memoryMB: 16384
    # # (Optional/Preview) Specify the addon node configuration which can be added or edited
    # # only during cluster creation
    # addonNode:
    #   # Enable auto resize for addon node
    #   autoResize:
    #     # Whether to enable auto resize for master. Defaults to false.
    #     enabled: false
    connectivity: connected
    # (Optional) Specify the proxy configuration
    proxy:
      # The URL of the proxy
      url: ""
      # The domains and IP addresses excluded from proxying
      noProxy: ""
    # # (Optional) Use a private Docker registry to host GKE images
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
    # (Optional/Preview) Specify which GCP project to connect your GKE clusters to
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
    # # (Optional) Configure kubernetes apiserver audit logging
    # cloudAuditLogging:
    #   projectID: ""
    #   # A GCP region where you would like to store audit logs for this cluster.
    #   clusterLocation: ""
    #   # The absolute or relative path to the key file for a GCP service account used to
    #   # send audit logs from the cluster
    #   serviceAccountKeyPath: ""
    # # (Optional/Preview) Configure backups for admin cluster. Backups will be stored under
    # # /anthos-backups/
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

## Filling in your configuration file

In your configuration file, enter field values as described in the following sections.

## `name`

String. A name of your choice for the cluster. The default value is a random name prefixed with `gke-admin-`. For example:
    
    
    name: "my-admin-cluster"
    

## `bundlePath`

String. The path of your Google Distributed Cloud bundle file.

The Google Distributed Cloud full bundle file contains all of the components in a particular release of Google Distributed Cloud. When you create an admin workstation, it comes with a full bundle at:
    
    
    /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz
    

For example:
    
    
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.9.0-gke.8.full.tgz"
    

## `vCenter`

This section holds information about your vCenter environment.

### `vCenter.address`

String. The IP address or the hostname of your vCenter server.

Before you fill in the `address` field, download and inspect the serving certificate of your vCenter server. Enter the following command to download the certificate and save it to a file named `vcenter.pem`.
    
    
    true | openssl s_client -connect VCENTER_IP:443 -showcerts 2>/dev/null | sed -ne '/-BEGIN/,/-END/p' > vcenter.pem
    

Replace `VCENTER_IP` with the IP address of your vCenter Server.

Open the certificate file to see the Subject Common Name and the Subject Alternative Name:
    
    
    openssl x509 -in vcenter.pem -text -noout

The output shows the `Subject` Common Name (CN). This might be an IP address, or it might be a hostname. For example:
    
    
    Subject: ... CN = 203.0.113.100
    
    
    Subject: ... CN = my-vcenter-server.my-domain.example

The output might also include one or more DNS names under `Subject Alternative Name`:
    
    
    X509v3 Subject Alternative Name:
        DNS:vcenter.my-domain.example

Choose the `Subject` Common Name or one of the DNS names under `Subject Alternative Name` to use as the value of `vcenter.address` in your configuration file. For example:
    
    
    vCenter:
      address: "203.0.113.100"
    
    
    
    vCenter:
      address: "my-vcenter-server.my-domain.example"
    

**Note:** As of Google Distributed Cloud version 1.9, the admin cluster data center and any user cluster data center can be different. By default, a user cluster uses the same data center as the admin cluster.

### `vCenter.datacenter`

String. The name of your vCenter datacenter for the admin cluster. For example:
    
    
    vCenter:
      datacenter: "MY-DATACENTER"
    

### `vCenter.cluster`

String. The name of your vSphere cluster. For example:
    
    
    vCenter:
      cluster: "MY-CLUSTER"
    

### `vCenter.resourcePool`

String. The name of your vCenter resource pool. For example:

If you are using a non-default resource pool, provide the name of your vCenter resource pool. For example:
    
    
    vCenter:
      resourcePool: "MY-POOL"
    

If you are using the default resource pool, provide the following value:
    
    
    vCenter:
      resourcePool: "VSPHERE_CLUSTER/Resources"
    

Replace `VSPHERE_CLUSTER` with the name of your vSphere cluster.

### `vCenter.datastore`

String. The name of your vCenter datastore. For example:
    
    
    vCenter:
      datastore: "MY-DATASTORE"
    

See [Specifying the root resource pool for a standalone host](https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs/data-sources/resource_pool).

### `vCenter.caCertPath`

String. When a client, like Google Distributed Cloud, sends a request to your vCenter server, the server must prove its identity to the client by presenting a certificate or a certificate bundle. To verify the certificate or bundle, Google Distributed Cloud must have the root certificate in the chain of trust.

Set `vCenter.caCertPath` to the path of the root certificate. For example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert.pem"
    

Your VMware installation has a certificate authority (CA) that issues a certificate to your vCenter server. The root certificate in the chain of trust is a self-signed certificate created by VMware.

If your certificate changes, you can [update the reference to the new certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/update-vcenter-certificate).

If you do not want to use the VMWare CA, which is the default, you can configure VMware to [use a different certificate authority](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.psc.doc/GUID-3D0DE463-D0EC-442E-B524-64759D063E25.html).

If your vCenter server uses a certificate issued by the default VMware CA, download the certificate as follows:
    
    
    curl -k "https://SERVER_ADDRESS/certs/download.zip" > download.zip
    

Replace `SERVER_ADDRESS` with the address of your vCenter server.

Install the `unzip` command and unzip the certificate file:
    
    
    sudo apt-get install unzip
    unzip downloads.zip
    

If the unzip command doesn't work the first time, enter the command again.

Find the certificate file in `certs/lin`.

### `vCenter.credentials.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account should have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vsphere-requirements-basic). For example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

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
    

### `vCenter.dataDisk`

String. Google Distributed Cloud creates a virtual machine disk (VMDK) to hold Kubernetes object data. The installer creates the VMDK for you, but you must provide a name for the VMDK in the `vCenter.dataDisk` field. For example:
    
    
    vCenter:
      dataDisk: "my-disk.vmdk"
    

If you are using a vSAN datastore, you must put the VMDK in a folder, and you must manually create the folder ahead of time. You could use `govc` to create a folder:
    
    
    govc datastore.mkdir -namespace=true my-folder
    

Then set `vCenter.dataDisk` to the path of the VMDK, including the folder.

Example:
    
    
    vDenter:
      dataDisk: "my-folder/my-disk.vmdk"
    

**Important:** Do not put a forward slash in front of the folder name.

## `network`

This section holds information about your admin cluster network.

### `network.hostConfig`

This section holds information about NTP servers, DNS servers, and DNS search domains used by your cluster.

If you provided a value for one or both of the following fields, then fill in this section. Otherwise, remove this section:

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

String. If you want your cluster nodes to get their IP address from a DHCP server, set this to `"dhcp"`. If you want your cluster nodes to have static IP addresses chosen from a list that you provide, set this to `"static"`.

For example:
    
    
    network:
      ipMode:
        type: "static"
    

### `network.ipMode.ipBlockFilePath`

If you set `ipMode.type` to `"static"`, fill in this field.

If you set `ipMode.type` to `"dhcp"`, remove this field.

String. The path of the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file) for your admin cluster nodes. For example:
    
    
    network:
      ipMode:
        ipBlockFilePath: "/my-config-folder/admin-cluster-ipblock.yaml"
    

### `network.serviceCIDR` and `network.podCiDR`

Strings. The admin cluster must have a range of IP addresses to use for Services and a range of IP addresses to use for Pods. These ranges are specified by the `network.serviceCIDR` and `network.podCIDR` fields. These fields are populated with default values. If you like, you can change the populated values to values of your choice.

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
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
    

### `network.vCenter.networkName`

String. The name of the vSphere network for your cluster nodes.

If the name contains a special character, you must use an escape sequence for it.

Special characters | Escape sequence  
---|---  
Slash (`/`) | `%2f`  
Backslash (`\`) | `%5c`  
Percent sign (`%`) | `%25`  
  
If the network name is not unique, it is possible to specify a path to the network, such as `/DATACENTER/network/NETWORK_NAME`.

For example:
    
    
    network:
      vCenter:
        networkName: "MY-CLUSTER-NETWORK"
    

## `loadBalancer`

This section holds information about the load balancer for your admin cluster.

### `loadBalancer.vips.controlPlaneVIP`

String. The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the admin cluster. For example:
    
    
    loadBalancer:
      vips:
        controlplaneVIP: "203.0.113.3"
    

### `loadBalancer.vips.addonsVIP`

String. The IP address you have chosen to configure on the load balancer for add-ons. For example:
    
    
    loadBalancer:
      vips:
        addonsVIP: "203.0.113.4"
    

### `loadBalancer.kind`

String. Set this to `"Seesaw"`, `"F5BigIP"`, or `"ManualLB"` For example:
    
    
    loadBalancer:
      kind: "Seesaw"
    

### `loadBalancer.manualLB`

If you set `loadbalancer.kind` to `"ManualLB"`, fill in this section. Otherwise, remove this section.

#### `loadBalancer.manualLB.ingressHTTPNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.ingressHTTPSNodePort`

Remove this field from your configuration file. It is not used in an admin cluster.

#### `loadBalancer.manualLB.controlPlaneNodePort`

Integer. The Kubernetes API server in the admin cluster is implemented as a Service of type `NodePort`. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value. For example:
    
    
    loadBalancer:
      manualLB:
        contolPlaneNodePort: 30968
    

#### `loadBalancer.manualLB.addonsNodePort`

Integer. The add-ons server in the admin cluster is implemented as a Service of type `NodePort`. You must choose a `nodePort` value for the Service.

Set this field to the `nodePort` value. For example:
    
    
    loadBalancer:
      manualLB:
        addonsNodePort: 31405
    

### `loadBalancer.f5BigIP`

If you set `loadbalancer.kind` to `"f5BigIP"`, fill in this section. Otherwise, remove this section.

#### `loadBalancer.f5BigIP.address`

String. The address of your F5 BIG-IP load balancer. For example:
    
    
    loadBalancer:
      f5BigIP:
        address: "203.0.113.2"
    

#### `loadBalancer.f5BigIP.credentials.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to connect to your F5 BIG-IP load balancer.

The user account must have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

Example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: ""my-config-folder/admin-creds.yaml"
    

#### `loadBalancer.f5BigIP.credentialsfileRef.entry`

String. The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file), that holds the username and password of your F5 BIG-IP account. For example:
    
    
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            entry: "f5-creds"
    

#### `loadBalancer.f5BigIP.partition`

String. The name of a BIG-IP partition that you created for your admin cluster. For example:
    
    
    loadBalancer:
      f5BigIP:
        partition: "my-f5-admin-partition"
    

#### `loadBalancer.f5BigIP.snatPoolName`

String. If you are using SNAT, the name of your SNAT pool. If you are not using SNAT, remove this field. For example:
    
    
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

Integer. The number of megabytes of memory for each of your Seesaw VM. For example:
    
    
    loadBalancer:
      seesaw:
        memoryMB: 8192
    

#### `loadBalancer.seesaw.vCenter.networkName`

String. The name of the vCenter network that contains your Seesaw VMs. For example:
    
    
    loadBalancer:
      seesaw:
        vCenter:
          networkName: "my-seesaw-network"
    

#### `loadBalancer.seesaw.enableHA`

Boolean. If you want to create a highly-available (HA) Seesaw load balancer, set this to `true`. Otherwise set this to `false`. An HA Seesaw load balancer uses a [(Master, Backup) pair](https://datatracker.ietf.org/doc/html/rfc5798#section-3) of VMs. For example:
    
    
    loadBalancer:
      seesaw:
        enableHA: true
    

#### `loadBalancer.seesaw.disableVRRPMAC`

Boolean. If you set this to `true`, the Seesaw load balancer does not use [MAC learning](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/bundled-load-balance#mac_learning) for failover. Instead, it uses [gratuitous ARP](https://datatracker.ietf.org/doc/html/rfc2002#section-4.6). If you set this to `false`, the Seesaw load balancer uses MAC learning. We recommend that you set this to `true`. If you are using vSphere 7 or later, and you have a high-availability Seesaw load balancer, then you must set this to `true`. For example:
    
    
    loadBalancer:
      seesaw:
        disableVRRPMAC: true
    

## `antiAffinityGroups.enabled`

Boolean. Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`. For example:
    
    
    antiAffinityGroups:
      enabled: true
    

Google Distributed Cloud automatically creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster's nodes, causing them to be spread across at least three physical hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least three physical hosts available.




Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least three hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false`.

## `adminMaster`

Preview.

If you want to specify CPU and memory for the control-plane node of the admin cluster, fill in this section. Otherwise, remove this section.

### `adminMaster.cpus`

Integer. The number of CPUs for the control-plane node of the admin cluster. For example:
    
    
    adminMaster:
      cpus: 4
    

### `adminMaster.memoryMB`

Integer. The number of megabytes of memory for the control-plane node of the admin cluster. For example:
    
    
    adminMaster:
      memoryMB: 16384
    

## `addonNode.autoResize.enabled`

Boolean. Set this to `true` to enable automatic resizing of the add-on nodes in the admin cluster. For example:
    
    
    addonNode:
      autoResize:
        enabled: true
    

## `connectivity`

String. Optional. Specify the connectivity to Google Cloud. The only possible value for connectivity is "connected". For example:
    
    
    connectivity: "connected"
    

## `proxy`

If your network is behind a proxy server, fill in this section. Otherwise, remove this section.

### `proxy.url`

String. The HTTP address of your proxy server. Include the port number even if it's the same as the scheme's default port. For example:
    
    
    proxy:
      url: "http://my-proxy.example.local:80"
    

The proxy server you specify here is used by your Google Distributed Cloud clusters. Also, your admin workstation is automatically configured to use this same proxy server unless you set the `HTTPS_PROXY` environment variable on your admin workstation.

If you specify `proxy.url`, you must also specify `proxy.noProxy`.

After the proxy configuration for the admin cluster has been set, it cannot be modified or deleted, unless the cluster is rebuilt.

### `proxy.noProxy`

String. A comma-separated list of IP addresses, IP address ranges, host names, and domain names that should not go through the proxy server. When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request is sent directly. For example:
    
    
    proxy:
      noProxy: "10.151.222.0/24, my-host.example.local,10.151.2.1"
    

## `privateRegistry`

If you have a private Docker registry, fill in this section. Otherwise, remove this section. The settings you select in the `privateregistry` section are reflected not only to the admin cluster, but also to the user clusters.

### `privateRegistry.address`

String. The IP address or FQDN (Fully Qualified Domain Name) of the machine that runs your private Docker registry. For example:
    
    
    privateRegistry:
      address: "203.0.113.10"
    
    
    
    privateRegistry:
      address: "fqdn.example.com"
    

### `privateRegistry.credentials.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file) that holds the username and password of an account that Google Distributed Cloud can use to access your private Docker registry. For example:
    
    
    privateRegistry:
      credentials:
        fileRef:
          path: "my-config-folder/admin-creds.yaml"
    

### `privateRegistry.credentials.fileRef.entry`

String. The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file), that holds the username and password of your private Docker registry account.
    
    
    privateRegistry:
      credentials:
        fileRef:
          entry: "private-registry-creds"
    

### `privateRegistry.caCertPath`

String. When Docker pulls an image from your private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). Docker uses the CA's certificate to validate the registry's certificate.

Set this field to the path of the CA's certificate. For example:
    
    
    privateRegistry:
      caCertPath: "my-cert-folder/registry-ca.crt"
    

## `componentAccessServiceAccountKeyPath`

String. The path of the JSON key file for your component access service account. For example:
    
    
    componentAccessServiceAccountKeyPath: "my-key-folder/access-key.json"
    

## `gkeConnect`

Optional.

This section holds information about the Google Cloud project and service account you want to use to [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet.

### `gkeConnect.projectID`

String. The ID of your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/multiple-gcp-projects#fleet_host_project). For example:
    
    
    gkeConnect:
      projectID: "my-connect-project-123"
    

### `gkeConnect.registerServiceAccountKeyPath`

String. The path of the JSON key file for your [connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/service-accounts#connect_register_service_account). For example:
    
    
    gkeConnect:
      registerServiceAccountKeyPath: "my-key-folder/connect-register-key.json"
    

## `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/concepts/logging-and-monitoring) for your cluster, fill in this section. Otherwise delete it or leave it commented out.

### `stackdriver.projectID`

String. The project ID of the Google Cloud project where you want to view logs. For example:
    
    
    stackdriver:
      projectID: "my-logs-project"
    

### `stackdriver.clusterLocation`

String. The Google Cloud region where you want to store logs. It is a good idea to choose a region that is near your on-prem data center. For example:
    
    
    stackdriver:
      clusterLocation: "us-central1"
    

### `stackdriver.enableVPC`

Boolean. If your cluster's network is controlled by a [VPC](https://docs.cloud.google.com/vpc), set this field to `true`. This ensures that all telemetry flows through Google's restricted IP addresses. Otherwise, set this field to `false`. For example:
    
    
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
    

#### Updating the value of `stackdriver.disableVsphereResourceMetrics`

## `cloudAuditLogging`

If you want to enable [Cloud Audit Logs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/audit-logging) for your cluster, fill in this section. Otherwise, remove this section.

### `cloudAuditLogging.projectID`

String. The project ID of the Google Cloud project where you want to view audit logs. For example:
    
    
    cloudAuditLogging:
      projectID: "my-audit-project"
    

### `cloudAuditLogging.clusterLocation`

String. The Google Cloud region where you want to store audit logs. It is a good idea to choose a region that is near your on-prem data center. For example:
    
    
    cloudAuditLogging:
      clusterLocation: "us-central1"
    

### `cloudAuditLogging.serviceAccountKeyPath`

String. The path of the JSON key file for your audit-logging service account. For example:
    
    
    cloudAuditLogging:
      serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## `clusterBackup.datastore`

Preview.

String. If you want to enable [backing up of the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/back-up-and-restore-an-admin-cluster-with-gkectl), set this to the vSphere datastore where you want to save cluster backups.

For example:
    
    
    clusterBackup:
      datastore: "my-datastore"
    

## `autoRepair.enabled`

Boolean. Set this to `true` to enable [node auto repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/node-auto-repair). Otherwise, set this to `false`. For example:
    
    
    autoRepair:
      enabled: true
    

## `secretsEncryption`

If you want to enable [always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/always-on-secrets-encryption), fill in this section. Otherwise, remove or comment out this section.

### `secretsEncryption.mode`

String. Secret encryption mode. Set this to `"GeneratedKey"`.
    
    
    secretsEncryption:
      mode: "GeneratedKey"
    

### `secretsEncryption.generatedKey.keyVersion`

Integer. An integer of your choice to use for the key version number. We recommend `1`. Do not include this field if you have included `secretsEncryption.generatedKey.disabled`. For example:
    
    
    secretsEncryption:
      mode: "GeneratedKey"
      generatedKey:
        keyVersion: 1
    

When you want to rotate the key, increment `keyVersion` by 1, and run `gkectl update`

### `secretsEncryption.generatedKey.disabled`

Boolean. To disable always-on Secrets encryption, set this to `true`. Do not include this field if you have included `secretsEncryption.generatedKey.keyVersion`. For example:
    
    
    secretsEncryption:
      mode: "GeneratedKey"
      generatedKey:
        disabled: true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
