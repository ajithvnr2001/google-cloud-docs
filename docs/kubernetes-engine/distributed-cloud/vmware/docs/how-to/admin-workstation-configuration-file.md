---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file/
title: Admin workstation configuration file \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:00.412862+00:00
---

# Admin workstation configuration file  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Admin workstation configuration file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the fields in the admin workstation configuration file for Google Distributed Cloud.

## Generating a template for your configuration file

[Download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads) the `gkeadm` command-line tool.

To generate a template:
    
    
    ./gkeadm create config --config=OUTPUT_FILENAME
    

Replace `OUTPUT_FILENAME` with a path of your choice for the generated template. If you omit this flag, `gkeadm` names the file `admin-ws-config.yaml` and puts it in the current directory.

**Template**

Click to see the generated template.
    
    
    gcp:
      # Path of the component access service account's JSON key file
      componentAccessServiceAccountKeyPath: ""
    # Specify which vCenter resources to use
    vCenter:
      # The credentials and address GKE On-Prem should use to connect to vCenter
      credentials:
        address: ""
        # reference to vCenter credentials file
        fileRef:
          # read credentials from this file
          path: credential.yaml
          # entry in the credential file
          entry: vCenter
      datacenter: ""
      datastore: ""
      cluster: ""
      network: ""
      # vSphere vm folder to deploy vms into. defaults to datacenter top level folder
      folder: ""
      resourcePool: ""
      # Provide the path to vCenter CA certificate pub key for SSL verification
      caCertPath: ""
    # The URL of the proxy for the jump host
    proxyUrl: ""
    adminWorkstation:
      name: gke-admin-ws-230809-173521
      cpus: 4
      memoryMB: 8192
      # The boot disk size of the admin workstation in GB. It is recommended to use a
      # disk with at least 100 GB to host images decompressed from the bundle.
      diskGB: 100
      # Name for the persistent disk to be mounted to the home directory (ending in .vmdk).
      # Any directory in the supplied path must be created before deployment.
      dataDiskName: gke-on-prem-admin-workstation-data-disk/gke-admin-ws-230809-173521-data-disk.vmdk
      # The size of the data disk in MB.
      dataDiskMB: 512
      network:
        # The IP allocation mode: 'dhcp' or 'static'
        ipAllocationMode: ""
        # # The host config in static IP mode. Do not include if using DHCP
        # hostConfig:
        #   # The IPv4 static IP address for the admin workstation
        #   ip: ""
        #   # The IP address of the default gateway of the subnet in which the admin workstation
        #   # is to be created
        #   gateway: ""
        #   # The subnet mask of the network where you want to create your admin workstation
        #   # (e.g. 255.255.255.0)
        #   netmask: ""
        #   # The list of DNS nameservers to be used by the admin workstation
        #   dns:
        #   - ""
      # The URL of the proxy for the admin workstation
      proxyUrl: ""
      ntpServer: ntp.ubuntu.com

## Filling in your configuration file

In your configuration file, enter field values as described in the following sections.

## `gcp`

This section holds information about your component access service account.

### `gcp.componentAccessServiceAccountKeyPath`

String. The path of the JSON key file for your component access service account. For information on creating a JSON key file, see [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account).

For example:
    
    
    gcp:
      componentAccessServiceAccountKeyPath: "my-key-folder/component-access-key.json"
    

## `vCenter`

This section holds information about your vSphere environment.

### `vCenter.credentials.address`

String. The IP address or the hostname of your vCenter server.

Before you fill in the `address` field, download and inspect the serving certificate of your vCenter server. Enter the following command to download the certificate and save it to a file named `vcenter.pem`.
    
    
    true | openssl s_client -connect VCENTER_IP:443 -showcerts 2>/dev/null | sed -ne '/-BEGIN/,/-END/p' > vcenter.pem

Replace `VCENTER_IP` with the IP address of your vCenter Server.

Open the certificate file to see the Subject Common Name and the Subject Alternative Name:
    
    
    openssl x509 -in vcenter.pem -text -noout

The output shows the `Subject` Common Name (CN). This might be an IP address, or it might be a hostname. For example:
    
    
    Subject: ... CN = 203.0.113.100
    
    
    Subject: ... CN = my-host.my-domain.example

The output might also include one or more DNS names under `Subject Alternative Name`:
    
    
    X509v3 Subject Alternative Name:
        DNS:vcenter.my-domain.example

Choose the `Subject` Common Name or one of the DNS names under `Subject Alternative Name` to use as the value of `vcenter.credentials.address` in your configuration file. For example:
    
    
    vCenter:
      credentials:
        address: "203.0.113.1"
        ...
    
    
    
    vCenter:
      credentials:
        address: "my-host.my-domain.example"
        ...
    

### `vCenter.credentials.fileRef.path`

String. The path of a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) that holds the username and password of your vCenter user account. The user account should have the Administrator role or equivalent privileges. See [vSphere requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges).

When you run `gkeadm create config`, it creates a template for an admin workstation configuration file named `admin-ws-config.yaml`. It also creates a template for a credentials configuration file named `credential.yaml`.

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "credential.yaml"
    

### `vCenter.credentials.fileRef.entry`

String. The name of the credentials block, in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file), that holds the username and password of your vCenter user account.

In `credential.yaml`, `gkeadm` automatically creates a credentials block named `vCenter`.

Example:
    
    
    vCenter:
      credentials:
        fileRef:
          entry: "vCenter"
    

### `vCenter.datacenter`

String. The name of your vCenter datacenter. For example:
    
    
    vCenter:
      datacenter: "MY-DATACENTER"
    

### `vCenter.datastore`

String. The name of your vCenter datastore. For example:
    
    
    vCenter:
      datastore: "MY-DATASTORE"
    

### `vCenter.cluster`

String. The name of your vCenter cluster. For example:
    
    
    vCenter:
      cluster: "MY-CLUSTER"
    

### `vCenter.network`

String. The name of the vCenter network where you want to create your admin workstation. For example:
    
    
    vCenter:
      network: "MY-VM-NETWORK"
    

### `vCenter.folder`

String. The folder in your datacenter where your cluster VMs will be located. For example:
    
    
    vCenter:
      folder: "MY-FOLDER"
    

### `vCenter.resourcePool`

String. If you are using a non-default resource pool, provide the name of your vCenter resource pool. For example:
    
    
    vCenter:
      resourcePool: "MY-POOL"
    

If you are using the default resource pool, provide the following value:
    
    
    vCenter:
      resourcePool: "MY_CLUSTER/Resources"
    

Replace `MY_CLUSTER` with the name of your vCenter cluster.

See [Specifying the root resource pool for a standalone host](https://registry.terraform.io/providers/hashicorp/vsphere/next/docs/data-sources/resource_pool).

### `vCenter.caCertPath`

String. When a client, like Google Distributed Cloud, sends a request to your vCenter server, the server must prove its identity to the client by presenting a certificate or a certificate bundle. To verify the certificate or bundle, Google Distributed Cloud must have the root certificate in the chain of trust.

Set `vCenter.caCertPath` to the path of the root certificate. For example:
    
    
    vCenter:
      caCertPath: "/usr/local/google/home/me/certs/vcenter-ca-cert.pem"
    

Your VMware installation has a certificate authority (CA) that issues a certificate to your vCenter server. The root certificate in the chain of trust is a self-signed certificate created by VMware.

If you do not want to use the VMWare CA, which is the default, you can configure VMware to [use a different certificate authority](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html).

If your vCenter server uses a certificate issued by the default VMware CA, download the certificate as follows:
    
    
    curl -k "https://SERVER_ADDRESS/certs/download.zip" > download.zip
    

Replace `SERVER_ADDRESS` with the address of your vCenter server.

Install the `unzip` command and unzip the certificate file:
    
    
    sudo apt-get install unzip
    unzip download.zip
    

If the unzip command doesn't work the first time, enter the command again.

Find the certificate file in `certs/lin`.

## `proxyUrl`

String: If the machine you are using to run `gkeadm` uses a proxy server for access to the internet, set this field to the URL of the proxy server. Include the port number even if it's the same as the scheme's default port. For example:
    
    
    proxyUrl: "https://my-proxy.example.local:80"
    

## `adminWorkstation`

This section holds information about your admin workstation.

### `adminWorkstation.name`

String. A name for your admin workstation. This field is populated with a generated value. You can keep the generated value or provide a different name of your choice. For example:
    
    
    adminWorkstation
      name: "gke-admin-ws-200617-113711"
    

### `adminWorkstation.cpus`

Integer. The number of virtual CPUs for your admin workstation. For example:
    
    
    adminWorkstation:
      cpus: 4
    

### `adminWorkstation.memoryMB`

Integer. The number of megabytes of memory for your admin workstation. For example:
    
    
    adminworkstation:
      memoryMB: 8192
    

### `adminWorkstation.diskGB`

Integer. The size, in gigabytes, of the boot disk for the admin workstation. We recommend at least 100 GB, and in version 1.28 and later, 100 GB is required. For example:
    
    
    adminWorkstation:
      diskGB: 100
    

### `adminWorkstation.dataDiskName`

String. A name for the persistent disk to be mounted to the home directory. This field is populated with a generated value. You can keep the generated value or provide a name of your choice. Must end with `.vmdk`. Any directory in the supplied path must be created before deployment. If no value is set for this field, it defaults to:
    
    
    gke-on-prem-admin-workstation-data-disk/ADMIN_WORKSTATION_NAME-data-disk.vmdk
    

For example:
    
    
    adminWorkstation:
      dataDiskName: "gke-on-prem-admin-workstation-data-disk/gke-admin-ws-200617-113711-data-disk.vmdk"
    

### `adminWorkstation.dataDiskMB`

Integer. The size in megabytes of the data disk. If no value is set for this field, it defaults to `512`. For example:
    
    
    adminWorkstation:
      dataDiskMB: 512
    

### `adminWorkstation.network.ipAllocationMode`

String. If you want your admin workstation to get its IP address from a DHCP server, set this to `"dhcp"`. If you want your admin workstation to have a static IP address of your choice, set this to `"static"`. For example:
    
    
    adminWorkstation:
      network:
        ipAllocationMode: "static"
    

### `adminWorkstation.network.hostconfig`

If you set `ipAllocationMode` to `"static"`, fill in the fields in this section.

If you set `ipAllocationMode` to `"dhcp"`, remove this section or leave it commented out.

#### `adminWorkstation.network.hostConfig.ip`

String. An IP address of your choice for your admin workstation. For example:
    
    
    adminWorkstation:
      network:
        hostconfig:
          ip: "172.16.5.1"
    

**Note:** If your system uses a Docker runtime, note that the default network of the docker daemon is 172.17.0.0/16. Make sure that the IP address you select for `adminWorkstation.network.hostConfig.ip` is not in that network.

#### `adminWorkstation.network.hostConfig.gateway`

String. The IP address of the default gateway for the network that contains your admin workstation. For example:
    
    
    adminWorkstation:
      network:
        hostconfig:
          gateway: "172.16.6.254"
    

#### `adminWorkstation.network.hostConfig.netmask`

String. The netmask for the network that contains your admin workstation. For example:
    
    
    adminWorkstation:
      network:
        hostConfig:
          netmask: "255.255.248.0"
    

#### `adminWorkstation.network.hostConfig.dns`

String array. An array of IP addresses for DNS servers that your admin workstation can use. For example:
    
    
    adminWorkstation:
      network:
        hostconfig:
          dns:
          - "172.16.255.1"
          - "172.16.255.2"
    

### `adminWorkstation.proxyUrl`

String. If your network is behind a proxy server, and you want both your admin workstation and your admin cluster to use the same proxy server, then set `adminworkstation.proxyURL` to the URL of the proxy server. Include the port number even if it's the same as the scheme's default port. For example:
    
    
    adminworkstation:
      proxyUrl: "http://aw-proxy.example:80"
    

### `adminWorkstation.ntpServer`

String. The hostname or IP address of the Network Time Protocol server that your admin workstation should use. For example:
    
    
    adminWorkstation:
      ntpServer: "216.239.35.0"
    

If you leave this empty, Google Distributed Cloud uses `"ntp.ubuntu.com"`.

## Example of a completed configuration file

Here is an example of a completed admin workstation configuration file:
    
    
    gcp:
      componentAccessServiceAccountKeyPath: "my-key-folder/component-access-key.json"
    vCenter:
      credentials:
        address: "203.0.113.1"
        username: "administrator.vsphere.local"
        password: "#STyZ2T#Ko2o"
      datacenter: "MY-DATACENTER"
      datastore: "MY-DATASTORE"
      cluster: "MY-CLUSTER"
      network: "MY-VM-NETWORK"
      resourcePool: "MY-POOL"
      caCertPath: "/usr/local/google/home/me/certs/the-root.cert"
    proxyUrl: ""
    adminWorkstation:
      name: "my-admin-workstation"
      cpus: 4
      memoryMB: 8192
      diskGB: 50
      dataDiskName: "gke-on-prem-admin-workstation-data-disk/gke-admin-ws-200617-113711-data-disk.vmdk"
      dataDiskMB: 512
      network:
        ipAllocationMode: "static"
        hostConfig:
          ip: "172.16.5.1"
          gateway: "172.16.6.254"
          netmask: "255.255.248.0"
          dns:
          - "172.16.255.1"
          - "172.16.255.2
      proxyUrl: ""
      ntpServer: "216.239.35.0"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
