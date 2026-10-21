---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/old-configuration-file/
title: Old cluster configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:29.570776+00:00
---

# Old cluster configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/old-configuration-file/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Old cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the fields in the cluster configuration file that was used in Google Distributed Cloud versions 1.3 and earlier.

In Google Distributed Cloud version 1.4, the configuration files changed substantially. The new files are called version 1 configuration files. The configuration files that were used in Google Distributed Cloud versions earlier than 1.4 are called version 0 configuration files.

If you want to use new features that are introduced in Google Distributed Cloud version 1.4, you must use v1 configuration files.

The v0 configuration files are compatible with the tools in Google Distributed Cloud 1.4. For example, you can pass a v0 configuration file to the `gkectl create cluster` command in Google Distributed Cloud 1.4. Also, you can run commands that convert your v0 configuration files to v1 configuration files.

## Converting configuration files

Google Distributed Cloud 1.4 uses separate configuration files for the admin and user clusters. That is, you use one configuration file to create your admin cluster and a different configuration file to create a user cluster.

To convert a v0 configuration file to a v1 admin cluster configuration file:
    
    
    gkectl create-config admin --from [OLD_CONFIG_PATH] --config [OUTPUT_PATH]
    

where:

  * [OLD_CONFIG_PATH] is the path of your v0 configuration file.

  * [OUTPUT_PATH] is a path of your choice for the generated v1 admin cluster configuration file. If you omit this flag, `gkectl` names the file `admin-cluster.yaml` and puts it in the current directory.




To convert a v0 configuration file to a v1 user cluster configuration file:
    
    
    gkectl create-config cluster --from [OLD_CONFIG_PATH] --config [OUTPUT_PATH]
    

  * [OLD_CONFIG_PATH] is the path of your v0 configuration file.

  * [OUTPUT_PATH] is a path of your choice for the generated v1 user cluster configuration file. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.




## Template for the v0 configuration file

Click to see a template for the v0 cluster configuration file.
    
    
    # Absolute path to a GKE bundle on disk
    # Absolute path to a GKE bundle on disk
    bundlepath: ""
    # Specify which vCenter resources to use for deployment
    vcenter:
      # The credentials and address GKE should use to connect to vCenter
      credentials:
        address: ""
        username: ""
        password: ""
      datacenter: ""
      datastore: ""
      cluster: ""
      network: ""
      resourcepool: ""
      # Provide the name for the persistent disk to be used by the deployment (ending
      # in .vmdk). Any directory in the supplied path must be created before deployment.
      # Not required when adding additional user clusters
      datadisk: ""
      # Provide the path to vCenter CA certificate pub key for SSL verification
      cacertpath: ""
    # Specify the proxy configuration.
    proxy:
      # The URL of the proxy
      url: ""
      # The domains and IP addresses excluded from proxying
      noproxy: ""
    # Specify admin cluster settings for a fresh Anthos clusters on VMware deployment. Omit this section
    # and use the --kubeconfig flag when adding a new user cluster to an existing deployment
    admincluster:
      # In-Cluster vCenter configuration
      vcenter:
        # If specified it overwrites the network field in global vcenter configuration
        network: ""
      # # The absolute or relative path to the yaml file to use for static IP allocation.
      # # Do not include if using DHCP
      # ipblockfilepath: ""
      # # Specify pre-defined nodeports if using "manual" load balancer mode
      # manuallbspec:
      #   ingresshttpnodeport: 0
      #   ingresshttpsnodeport: 0
      #   controlplanenodeport: 30968
      #   addonsnodeport: 31405
      # Specify the already-existing partition and credentials to use with F5
      bigip:
        # To re-use credentials across clusters we recommend using YAML node anchors.
        # See https://yaml.org/spec/1.2/spec.html#id2785586
        credentials:
          address: ""
          username: ""
          password: ""
        partition: ""
        # # Optionally specify a pool name if using SNAT
        # snatpoolname: ""
      # The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlplanevip: ""
        # # Used for admin cluster addons (needed for multi cluster features). Must be the same
        # # across clusters
        # addonsvip: ""
      # The Kubernetes service CIDR range for the cluster. Must not overlap with the pod
      # CIDR range
      serviceiprange: 10.96.232.0/24
      # The Kubernetes pod CIDR range for the cluster. Must not overlap with the service
      # CIDR range
      podiprange: 192.168.0.0/16
      # Spread nodes across at least three physical hosts (requires at least three hosts)
      antiaffinitygroups:
        # Set to false to disable DRS rule creation
        enabled: true
    # Specify settings when deploying a new user cluster. Used both with a fresh deployment
    # or when adding a new cluster to an existing deployment.
    usercluster:
      # In-Cluster vCenter configuration
      vcenter:
        # If specified it overwrites the network field in global vcenter configuration
        network: ""
      # # The absolute or relative path to the yaml file to use for static IP allocation.
      # # Do not include if using DHCP
      # ipblockfilepath: ""
      # # Specify pre-defined nodeports if using "manual" load balancer mode
      # manuallbspec:
      #   ingresshttpnodeport: 30243
      #   ingresshttpsnodeport: 30879
      #   controlplanenodeport: 30562
      #   addonsnodeport: 0
      # Specify the already-existing partition and credentials to use with F5
      bigip:
        # To re-use credentials across clusters we recommend using YAML node anchors.
        # See https://yaml.org/spec/1.2/spec.html#id2785586
        credentials:
          address: ""
          username: ""
          password: ""
        partition: ""
        # # Optionally specify a pool name if using SNAT
        # snatpoolname: ""
      # The VIPs to use for load balancing
      vips:
        # Used to connect to the Kubernetes API
        controlplanevip: ""
        # Shared by all services for ingress traffic
        ingressvip: ""
        # # Used for admin cluster addons (needed for multi cluster features). Must be the same
        # # across clusters
        # addonsvip: ""
      # A unique name for this cluster
      clustername: ""
      # User cluster master nodes must have either 1 or 3 replicas
      masternode:
        cpus: 4
        memorymb: 8192
        # How many machines of this type to deploy
        replicas: 1
      # The number of worker nodes to deploy and their size. Min. 3 replicas
      workernode:
        cpus: 4
        memorymb: 8192
        # How many machines of this type to deploy
        replicas: 3
      # Spread nodes across at least three physical hosts (requires at least three hosts)
      antiaffinitygroups:
        # Set to false to disable DRS rule creation
        enabled: true
      # The Kubernetes service CIDR range for the cluster
      serviceiprange: 10.96.0.0/12
      # The Kubernetes pod CIDR range for the cluster
      podiprange: 192.168.0.0/16
      # # Uncomment this section to use OIDC authentication
      # oidc:
      #   issuerurl: ""
      #   kubectlredirecturl: ""
      #   clientid: ""
      #   clientsecret: ""
      #   username: ""
      #   usernameprefix: ""
      #   group: ""
      #   groupprefix: ""
      #   scopes: ""
      #   extraparams: ""
      #   # Set value to string "true" or "false"
      #   usehttpproxy: ""
      #   # # The absolute or relative path to the CA file (optional)
      #   # capath: ""
      # # Optionally provide an additional serving certificate for the API server
      # sni:
      #   certpath: ""
      #   keypath: ""
      # # Specify whether or not to enable the GKE usage metering feature
      # usagemetering:
      #   bigqueryprojectid: ""
      #   # The ID of the BigQuery Dataset in which the usage metering data will be stored
      #   bigquerydatasetid: ""
      #   # The absolute or relative path to the key file for a GCP service account used by
      #   # gke-usage-metering to report to BigQuery
      #   bigqueryserviceaccountkeypath: ""
      #   # Whether or not to enable the consumption-based metering feature
      #   enableconsumptionmetering: false
    # Which load balancer mode to use "Manual" or "Integrated"
    lbmode: Integrated
    # Specify which GCP project to connect your GKE clusters to
    gkeconnect:
      projectid: ""
      # The absolute or relative path to the key file for a GCP service account used to
      # register the cluster
      registerserviceaccountkeypath: ""
      # The absolute or relative path to the key file for a GCP service account used by
      # the GKE connect agent
      agentserviceaccountkeypath: ""
    # Specify which GCP project to connect your logs and metrics to
    stackdriver:
      projectid: ""
      # A GCP region where you would like to store logs and metrics for this cluster.
      clusterlocation: ""
      enablevpc: false
      # The absolute or relative path to the key file for a GCP service account used to
      # send logs and metrics from the cluster
      serviceaccountkeypath: ""
    # Specify Cloud Run configuration
    cloudrun:
      enabled: false
    # # Optionally use a private Docker registry to host GKE images
    # privateregistryconfig:
    #   # Do not include the scheme with your registry address
    #   credentials:
    #     address: ""
    #     username: ""
    #     password: ""
    #   # The absolute or relative path to the CA certificate for this registry
    #   cacertpath: ""
    # The absolute or relative path to the GCP service account key that will be used to
    # pull GKE images
    gcrkeypath: ""
    # # Configure kubernetes apiserver audit logging
    # cloudauditlogging:
    #   projectid: ""
    #   # A GCP region where you would like to store audit logs for this cluster.
    #   clusterlocation: ""
    #   # The absolute or relative path to the key file for a GCP service account used to
    #   # send audit logs from the cluster
    #   serviceaccountkeypath: ""

## Filling in a v0 configuration file

If you are using a v0 configuration file, enter field values as described in this section.

### bundlepath

The Google Distributed Cloud _bundle_ file contains all of the components in a particular release of Google Distributed Cloud. When you create an admin workstation, it comes with a _full bundle_ at `/var/lib/gke/bundles/gke-onprem-vsphere-[VERSION]-full.tgz`. This bundle's version matches the version of [the OVA you imported](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation#import) to create the admin workstation.

**Note:** When you install Google Distributed Cloud, your `gkectl` and bundle versions must be the same. If you created an admin workstation using an OVA that is at a different version than the version you want to install, the admin workstation's full bundle is likely outdated and you should upgrade your admin workstation.

Set the value of `bundlepath` to the path of your admin workstation's bundle file. That is, set `bundlepath` to:
    
    
    /var/lib/gke/bundles/gke-onprem-vsphere-[VERSION]-full.tgz

where [VERSION] is the version of Google Distributed Cloud that you are installing. The latest version is 1.6.0-gke.7.

Note that you are free to keep your bundle file in a different location or give it a different name. Just make sure that in your configuration file, the value of `bundlepath` is the path to your bundle file, whatever that might be.

### vCenter specification

The `vcenter` specification holds information about your vCenter Server instance. Google Distributed Cloud needs this information to communicate with your vCenter Server.

#### vcenter.credentials.address

The `vcenter.credentials.address` field holds the IP address or the hostname of your vCenter server.

Before you fill in the `vsphere.credentials.address field`, download and inspect the serving certificate of your vCenter server. Enter the following command to download the certificate and save it to a file named `vcenter.pem`.
    
    
    true | openssl s_client -connect [VCENTER_IP]:443 -showcerts 2>/dev/null | sed -ne '/-BEGIN/,/-END/p' > vcenter.pem

Open the certificate file to see the Subject Common Name and the Subject Alternative Name:
    
    
    openssl x509 -in vcenter.pem -text -noout

The output shows the `Subject` Common Name (CN). This might be an IP address, or it might be a hostname. For example:
    
    
    Subject: ... CN = 203.0.113.100
    
    
    Subject: ... CN = my-host.my-domain.example

The output might also include one or more DNS names under `Subject Alternative Name`:
    
    
    X509v3 Subject Alternative Name:
        DNS:vcenter.my-domain.example

Choose the `Subject` Common Name or one of the DNS names under `Subject Alternative Name` to use as the value of `vcenter.credentials.address` in your configuration file. For example:
    
    
    vcenter:
      credentials:
        address: "203.0.113.1"
        ...
    
    
    
    vcenter:
      credentials:
        address: "my-host.my-domain.example"
        ...
    

You must choose a value that appears in the certificate. For example, if the IP address does not appear in the certificate, you cannot use it for `vcenter.credentials.address`.

#### vcenter.credential.username, .password

Google Distributed Cloud needs to know your vCenter Server's username, and password. To provide this information, set the `username` and `password` values under `vcenter.credentials`. For example:
    
    
    vcenter:
      credentials:
        username: "my-name"
        password: "my-password"
    

#### vcenter.datacenter, .datastore, .cluster, .network

Google Distributed Cloud needs some information about the structure of your vSphere environment. Set the values under `vcenter` to provide this information. For example:
    
    
    vcenter:
      datacenter: "MY-DATACENTER"
      datastore: "MY-DATASTORE"
      cluster: "MY-VSPHERE-CLUSTER"
      network: "MY-VIRTUAL-NETWORK"
    

**Note:** You can specify different vCenter networks for admin and user clusters in the `admincluster.vcenter.network` and `usercluster.vcenter.network` fields, respectively.

#### vcenter.resourcepool

A vSphere [resource pool](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) is a logical grouping of vSphere VMs in your vSphere cluster. If you are using a resource pool other than the default, provide its name to `vcenter.resourcepool`. For example:
    
    
    vcenter:
      resourcepool: "my-pool"
    

If you want Google Distributed Cloud to deploy its nodes to the vSphere cluster's default resource pool, provide an empty string to `vcenter.resourcepool`. For example:
    
    
    vcenter:
      resourcepool: ""
    

#### vcenter.datadisk

Google Distributed Cloud creates a virtual machine disk (VMDK) to hold the Kubernetes object data for the admin cluster. The installer creates the VMDK for you, but you must provide a name for the VMDK in the `vcenter.datadisk` field. For example:
    
    
    vcenter:
      datadisk: "my-disk.vmdk"
    

vSAN datastore: Creating a folder for the VMDK
    

If you are using a vSAN datastore, you need to put the VMDK in a folder. You must manually create the folder ahead of time. To do so, you could use `govc` to create a folder:
    
    
    govc datastore.mkdir -namespace=true my-gke-on-prem-folder

Then set `vcenter.datadisk` to the path of the VMDK, including the folder. For example:
    
    
    vcenter:
    datadisk: "my-gke-on-prem-folder/my-disk.vmdk"
    

**Important:** Do not put a forward slash in front of the folder name.

In version 1.1.1 and earlier, a [known issue](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/release-notes#vsan-data-disk-uuid-issue) requires that you provide the folder's universally unique identifier (UUID) path, rather than its file path, to `vcenter.datadisk`. Copy this from the output of the above `govc` command.

Then, provide the folder's UUID in the `vcenter.datadisk` field. Do not put a forward slash in front of the UUID. For example:
    
    
    vcenter:
    datadisk: "14159b5d-4265-a2ba-386b-246e9690c588/my-disk.vmdk"
    

This issue has been fixed in versions 1.1.2 and later.

#### vcenter.cacertpath

When a client, like Google Distributed Cloud, sends a request to vCenter Server, the server must prove its identity to the client by presenting a certificate or a certificate bundle. To verify the certificate or bundle, Google Distributed Cloud must have the root certificate in the chain of trust.

Set `vcenter.cacertpath` to the path of the root certificate. For example:
    
    
    vcenter:
      cacertpath: "/my-cert-folder/the-root.crt"
    

Your VMware installation has a certificate authority (CA) that issues a certificate to your vCenter server. The root certificate in the chain of trust is a self-signed certificate created by VMware.

If you do not want to use the VMWare CA, which is the default, you can configure VMware to [use a different certificate authority](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.psc.doc/GUID-3D0DE463-D0EC-442E-B524-64759D063E25.html).

If your vCenter server uses a certificate issued by the default VMware CA, there are several ways you can get the root certificate:

  * curl -k "https://[SERVER_ADDRESS]/certs/download.zip" > download.zip

where [SERVER_ADDRESS] is the address of your vCenter server.

  * In a browser, enter the address of your vCenter server. In the gray box at the right, click **Download trusted root CA certificates**.

  * Enter this command to get the serving certificate:
        
        true | openssl s_client -connect [SERVER_ADDRESS]:443 -showcerts

In the output, find a URL like this: https://[SERVER_ADDRESS]/afd/vecs/ca. Enter the URL in a browser. This downloads the root certificate.




The downloaded file is named `downloads.zip`.

Unzip the file:
    
    
    unzip downloads.zip

If the unzip command doesn't work the first time, enter the command again.

Find the certificate file in `certs/lin`.

### Proxy specification

If your network is behind a proxy server, populate the `proxy` field with HTTPS proxy and the addresses that should be excluded from proxying. For example:
    
    
    proxy:
      url: "https://username:password@domain"
      noproxy: "10.0.1.0/24,private-registry.example,10.0.2.1"
    

  * `proxy.url` is the URL of the HTTPS proxy.
  * `proxy.noproxy` includes the CIDR ranges, IP addresses, domains, and hostnames that should not be proxied. For example, calls to the IP addresses of cluster nodes should not be proxied. So if you have a subnet that contains only cluster nodes, you could list the CIDR range of the subnet in the `noproxy` field. Note that if `privateregistryconfig` is specified, that address is automatically added to prevent calls to your private registry.



### Admin cluster specification

The `admincluster` specification holds information that Google Distributed Cloud needs to create the admin cluster.

#### admincluster.vcenter.network

In `admincluster.vcenter.network`, you can specify a vCenter network for your admin cluster nodes. Note that this overrides the global setting you provided in `vcenter`. For example:
    
    
    admincluster:
      vcenter:
        network: MY-ADMIN-CLUSTER-NETWORK
    

#### admincluster.ipblockfilepath

Since you are using static IP addresses, you must have a host configuration file as described in Configuring static IPs. Provide the path to your host configuration file in the `admincluster.ipblockfilepath` field. For example:
    
    
    admincluster:
      ipblockfilepath: "/my-config-folder/my-admin-hostconfig.yaml"
    

#### admincluster.manuallbspec.ingresshttpnoodeport, .ingresshttpsnodeport

Remove these fields. They are not used in the admin cluster.

#### admincluster.manuallbspec.controlplanenodeport, .addonsnodeport (manual load balancing mode)

The Kubernetes API server in the admin cluster is implemented as a Service of type `NodePort`. If you are using manual load balancing, you must choose a `nodePort` value for the Service. Specify the `nodePort` value in `controlplanenodeport` For example:
    
    
    admincluster:
      manuallbspec:
        controlplanenodeport: 30968
    

The addons server in the admin cluster is implemented as a Service of type `NodePort`. If you are using manual load balancing, you must choose a `nodePort` value for the Service. Specify the `nodePort` value in `controlplanenodeport` For example:
    
    
    admincluster:
      manuallbspec:
        addonsnodeport: 30562
    

#### admincluster.bigip.credentials (integrated load balancing mode)

If you are not using integrated load balancing mode, leave `admincluster.bigip` commented out.

If you are using integrated load balancing mode, Google Distributed Cloud needs to know the IP address or hostname, username, and password of your F5 BIG-IP load balancer. Set the values under `admincluster.bigip` to provide this information. For example:
    
    
    admincluster:
      bigip:
        credentials:
          address: "203.0.113.2"
          username: "my-admin-f5-name"
          password: "rJDlm^%7aOzw"
    

#### admincluster.bigip.partition (integrated load balancing mode)

If you are using integrated load balancing mode, you must create a BIG-IP partition for your admin cluster. Set `admincluster.bigip.partition` to the name of your partition. For example:
    
    
    admincluster:
      bigip:
        partition: "my-admin-f5-partition"
    

#### admincluster.vips

Regardless of whether you are using integrated or manual load balancing for the admin cluster, you need to fill in the `admincluster.vips` field.

Set the value of `admincluster.vips.controlplanevip` to the [IP address that you have chosen to configure on the load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/requirements#vips) for the Kubernetes API server of the admin cluster. Set the value of `addonsvip` to the IP address you have chosen to configure on the load balancer for the add-ons. For example:
    
    
    admincluster:
      vips:
        controlplanevip: 203.0.113.3
        addonsvip: 203.0.113.4
    

#### admincluster.serviceiprange and admincluster.podiprange

The admin cluster must have a [range of IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/requirements#cidrs) to use for Services and a range of IP addresses to use for Pods. These ranges are specified by the `admincluster.serviceiprange` and `admincluster.podiprange` fields. These fields are populated when you run `gkectl create-config`. If you like, you can change the populated values to values of your choice.

The Service and Pod ranges must not overlap. Also, the Service and Pod ranges must not overlap with IP addresses that are used for nodes in any cluster.

Example:
    
    
    admincluster:
      serviceiprange: 10.96.232.0/24
      podiprange: 192.168.0.0/16
    

### admincluster.antiaffinitygrous.enabled

Boolean. Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`. For example:
    
    
    admincluster:
      antiAffinityGroups:
        enabled true
    

### User cluster specification

The user cluster specification, `usercluster`, holds information that Google Distributed Cloud needs to create the initial user cluster.

#### `usercluster.vcenter.network`

In `usercluster.vcenter.network`, you can specify a vCenter network for your user cluster nodes. Note that this overrides the global setting you provided in `vcenter`. For example:
    
    
    usercluster:
      vcenter:
        network: MY-USER-CLUSTER-NETWORK
    

#### `usercluster.ipblockfilepath`

Since you are using static IP addresses, you must have a host configuration file as described in Configuring static IPs. Provide the path to your host configuration file in the `usercluster.ipblockfilepath` field. For example:
    
    
    usercluster:
      ipblockfilepath: "/my-config-folder/my-user-hostconfig.yaml"
    

#### `usercluster.manuallbspec` (manual load balancing mode)

The ingress controller in the user cluster is implemented as a [Service of type NodePort](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#service_of_type_nodeport). The Service has one [ServicePort](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) for HTTP and another ServicePort for HTTPS. If you are using manual load balancing mode, you must choose `nodePort` values for these ServicePorts. Specify the `nodePort` values in `ingresshttpnodeport` and `ingresshttpsnodeport`. For example:
    
    
    usercluster:
      manuallbspec:
        ingresshttpnodeport: 30243
        ingresshttpsnodeport: 30879
    

The Kubernetes API server in the user cluster is implemented as a Service of type `NodePort`. If you are using manual load balancing, you must choose a `nodePort` value for the Service. Specify the `nodePort` value in `controlplanenodeport`. For example:
    
    
    usercluster:
      manuallbspec:
        controlplanenodeport: 30562
    

#### `usercluster.bigip.credentials` (integrated load balancing mode)

If you are using [integrated load balancing mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/requirements#f5_big-ip_requirements), Google Distributed Cloud needs to know the IP address or hostname, username, and password of the F5 BIG-IP load balancer that you intend to use for the user cluster. Set the values under `usercluster.bigip` to provide this information. For example:
    
    
    usercluster:
      bigip:
        credentials:
          address: "203.0.113.5"
          username: "my-user-f5-name"
          password: "8%jfQATKO$#z"
    

#### `usercluster.bigip.partition` (integrated load balancing mode)

If you are using integrated load balancing mode, you must create a BIG-IP partition for your user cluster. Set `usercluster.bigip.partition` to the name of your partition. For example:
    
    
    usercluster:
      bigip:
        partition: "my-user-f5-partition"
    

#### `usercluster.vips`

Regardless of whether you are using integrated or manual load balancing for the user cluster, you need to fill in the `usercluster.vips` field.

Set the value of `usercluster.vips.controlplanevip` to the IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. Set the value of `ingressvip` to the IP address you have chosen to configure on the load balancer for the user cluster's ingress controller. For example:
    
    
    usercluster:
      vips:
        controlplanevip: 203.0.113.6
        ingressvip: 203.0.113.7
    

#### `usercluster.clustername`

Set the value of `usercluster.clustername` to a name of your choice. Choose a name that is no longer than 40 characters. For example:
    
    
    usercluster:
      clustername: "my-user-cluster-1"
    

#### `usercluster.masternode.cpus` and `usercluster.masternode.memorymb`

The `usercluster.masternode.cpus` and `usercluster.masternode.memorymb` fields specify how many CPUs and how much memory, in megabytes, is allocated to each control plane node of the user cluster. For example:
    
    
    usercluster:
      masternode:
        cpus: 4
        memorymb: 8192
    

#### `usercluster.masternode.replicas`

The `usercluster.masternode.replicas` field specifies how many control plane nodes you want the user cluster to have. A user cluster's control plane node runs the user control plane, the Kubernetes control plane components. This value must be `1` or `3`:

  * Set this field to `1` to run one user control plane.
  * Set this field to `3` if you want to have a [high availability (HA) user control plane](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/concepts/ha) composed of three control plane nodes that each run a user control plane.



#### `usercluster.workernode.cpus` and `usercluster.workernode.memorymb`

The `usercluster.workernode.cpus` and `usercluster.workernode.memorymb` fields specify how many CPUs and how much memory, in megabytes, is allocated to each worker node of the user cluster. For example:
    
    
    usercluster:
      workernode:
        cpus: 4
        memorymb: 8192
        replicas: 3
    

#### `usercluster.workernode.replicas`

The `usercluster.workernode.replicas` field specifies how many worker nodes you want the user cluster to have. The worker nodes run the cluster workloads.

#### `usercluster.antiaffinitygrous.enabled`

Boolean. Set this to `true` to enable DRS rule creation. Otherwise, set this to `false`. For example:
    
    
    antiAffinityGroups:
      enabled true
    

#### `usercluster.serviceiprange` and `usercluster.podiprange`

The user cluster must have a [range of IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/requirements#cidrs) to use for Services and a range of IP addresses to use for Pods. These ranges are specified by the `usercluster.serviceiprange` and `usercluster.podiprange` fields. These fields are populated when you run `gkectl create-config`. If you like, you can change the populated values to values of your choice.

The Service and Pod ranges must not overlap. Also, the Service and Pod ranges must not overlap with IP addresses that are used for nodes in any cluster.

Example:
    
    
    usercluster:
      serviceiprange: 10.96.233.0/24
      podiprange: 172.16.0.0/12
    

#### usercluster.oidc

If you intend for clients of the user cluster to use OIDC authentication, set values for the fields under `usercluster.oidc`. Configuring OIDC is optional.

To learn how to configure OIDC, see [Authenticating with OIDC](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/oidc).

About installing version 1.0.2-gke.3
    

Version 1.0.2-gke.3 introduces the following OIDC fields (`usercluster.oidc`). These fields enable logging in to a cluster from Google Cloud console:

  * usercluster.oidc.kubectlredirecturl
  * usercluster.oidc.clientsecret
  * usercluster.oidc.usehttpproxy



In version 1.0.2-gke.3, if you want to use OIDC, the `clientsecret` field is required even if you don't want to log in to a cluster from Google Cloud console. In that case, you can provide a placeholder value for `clientsecret`:
    
    
    oidc:
    clientsecret: "secret"

#### usercluster.sni

**Note:** Some legacy browsers and devices might not support SNI.

[Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication) (SNI), an extension to Transport Layer Security (TLS), allows servers to present multiple certificates on a single IP address and TCP port, depending on the client-indicated hostname.

If your CA is already distributed as a trusted CA to clients outside your user cluster and you want to rely on this chain to identify trusted clusters, you can configure the Kubernetes API server with an additional certificate that is presented to external clients of the load balancer IP address.

To use SNI with your user clusters, you need to have your own CA and [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) (PKI). You provision a separate serving certificate for each user cluster, and Google Distributed Cloud adds each additional serving certificate to its respective user cluster.

To configure SNI for the Kubernetes API server of the user cluster, provide values for `usercluster.sni.certpath` (path to the external certificate) and `usercluster.sni.keypath` (path to the external certificate's private key file). For example:
    
    
    usercluster:
      sni:
        certpath: "/my-cert-folder/example.com.crt"
        keypath: "/my-cert-folder/example.com.key"
    

### `usagemetering`

If you want to enable usage metering for your cluster, then fill in this section. Otherwise, remove this section.

#### `usagemetering.bigqueryprojectid`

String. The ID of the Google Cloud project where you want to store usage metering data. For example:
    
    
    usagemetering:
      bigqueryprojectid: "my-bq-project"
    

#### `usagemetering.bigquerydatasetid`

String. The ID of the BigQuery dataset where you want to store usage metering data. For example:
    
    
    usagemetering:
      bigquerydatasetid: "my-bq-dataset"
    

#### `usagemetering.bigqueryserviceaccountkepPath`

String. The path of the JSON key file for your BigQuery service account. For example:
    
    
    usagemetering:
      bigqueryserviceaccountkeypath: "my-key-folder/bq-key.json"
    

#### `usagemetering.enableconsumptionmetering`

Boolean. Set this to `true` if you want to enable consumption-based metering. Otherwise set this to `false`. For example:
    
    
    usagemetering:
      enableconsumptionmetering: true
    

### `lbmode`

You can use integrated load balancing or [manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/manual-load-balance). Your choice of load balancing mode applies to your admin cluster and your initial user cluster. It also applies to any additional user clusters that you create in the future.

Specify your load balancing choice by setting the value of `lbmode` to `Integrated` or `Manual`. For example:
    
    
    lbmode: Integrated

### `gkeconnect`

The `gkeconnect` specification holds information that Google Distributed Cloud needs to set up management of your on-prem clusters from Google Cloud console.

Set `gkeconnect.projectid` to the project ID of the Google Cloud project where you want to manage your on-prem clusters.

Set the value of `gkeconnect.registerserviceaccountkeypath` to the path of the JSON key file for your [register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-accounts). Set the value of `gkeconnect.agentserviceaccountkeypath` to the path of the JSON key file for your [connect service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/getting-started#create_sa).

Example:
    
    
    gkeconnect:
      projectid: "my-project"
      registerserviceaccountkeypath: "/my-key-folder/register-key.json"
      agentserviceaccountkeypath: "/my-key-folder/connect-key.json"
    

**Note:** In versions prior to 1.1.0-gke.6, the Connect agent used the proxy server specified in the `gkeconnect.proxy` field. Starting with version 1.1.0-gke.6, the Connect agent uses the proxy server specified in the global `proxy` field. For more information, see the [release notes](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/release-notes#january_3_2020).

### `stackdriver`

**Note:** The `stackdriver.proxyconfigsecretname` field is removed as of version 1.1.0-gke.6. Don't include it in your configuration file.

The `stackdriver` specification holds information that Google Distributed Cloud needs to store log entries generated by your on-prem clusters.

Set `stackdriver.projectid` to the project ID of the Google Cloud project where you want to view Stackdriver logs that pertain to your on-prem clusters.

Set `stackdriver.clusterlocation` to a Google Cloud region where you want to store Stackdriver logs. It is a good idea to choose a region that is near your on-prem data center.

Set `stackdriver.enablevpc` to `true` if you have your cluster's network controlled by a [VPC](https://docs.cloud.google.com/vpc). This ensures that all telemetry flows through Google's restricted IP addresses.

Set `stackdriver.serviceaccountkeypath` to the path of the JSON key file for your [Stackdriver Logging service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/getting-started#create_sa).

Example:
    
    
    stackdriver:
      projectid: "my-project"
      clusterlocation: "us-west1"
      enablevpc: false
      serviceaccountkeypath: "/my-key-folder/stackdriver-key.json"
    

### `cloudrun.enabled`

Boolean. Set this to `true` if you want to enable Cloud Run. Otherwise set this to `false`. For example:
    
    
    cloudrun:
      enabled: true
    

### `privateregistryconfig`

**Note:** If you are creating a cluster at version 1.1.1-gke.2, see the [known issue](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/release-notes#docker_registry_issue) affecting use of a Docker registry.

If you have a private Docker registry, the `privateregistryconfig` field holds information that Google Distributed Cloud uses to push images to your private registry. If you don't specify a private registry, `gkectl` pulls Google Distributed Cloud's container images from its Container Registry repository, `gcr.io/gke-on-prem-release`, during installation.

Under `privatedockerregistry.credentials`, set `address` to the IP address of the machine that runs your private Docker registry. Set `username` and `password` to the username and password of your private Docker registry. The value that you set for `address` gets automatically added to `proxy.noproxy`.

When Docker pulls an image from your private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). Docker uses the CA's certificate to validate the registry's certificate.

Set `privateregistryconfig.cacertpath` to the path of the CA's certificate. For example:
    
    
    privateregistryconfig:
      cacertpath: /my-cert-folder/registry-ca.crt
    

### `gcrkeypath`

Set the value of `gcrkeypath` to the path of the JSON key file for your [component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-accounts).

For example:
    
    
    gcrkeypath: "/my-key-folder/component-access-key.json"
    

### `cloudauditlogging`

If you want to send your Kubernetes audit logs to your Google Cloud project, populate the `cloudauditlogging` specification. For example:
    
    
    cloudauditlogging:
      projectid: "my-project"
      # A GCP region where you would like to store audit logs for this cluster.
      clusterlocation: "us-west1"
      # The absolute or relative path to the key file for a GCP service account used to
      # send audit logs from the cluster
      serviceaccountkeypath: "/my-key-folder/audit-logging-key.json"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
