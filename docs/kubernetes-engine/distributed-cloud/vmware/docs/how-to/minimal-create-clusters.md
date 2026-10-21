---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-create-clusters/
title: Create basic clusters \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:38.370699+00:00
---

# Create basic clusters  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-create-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create basic clusters Stay organized with collections  Save and categorize content based on your preferences. 

This is the second part of a guide that walks you through a small proof-of-concept installation of Google Distributed Cloud. The first part is [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure), which shows you how to plan your IP addresses and set up the necessary vSphere and Google Cloud infrastructure for your deployment. This document builds on the setup and planning you did in the previous section and shows you how to create an admin workstation, admin cluster, and user cluster in your vSphere environment, using templates that you can fill in here in this document. You can then go on to [deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app).

As with the infrastructure setup of this basic installation, the clusters you set up using this document might not be suitable for your actual production needs and use cases. For much more information, best practices, and instructions for production installations, see the [installation guides](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview).

In version 1.33 and higher, all new clusters are created as [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). Be sure to review [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support) and [Cluster creation and upgrade differences](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#cluster_creation_and_upgrade_differences).

## Before you begin

  1. Ensure that you have set up your vSphere and Google Cloud environments as described in [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

  2. If you want to use Terraform to create the user cluster, you need [Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli) either on your admin workstation or another computer.




## Procedure overview

These are the primary steps involved in this setup:

  1. **Log in to the Google Cloud CLI** with an account that has the necessary permissions to create service accounts.

  2. **Gather information** that you need to configure Google Distributed Cloud, including your vCenter username and password, and the IP addresses that you prepared in the previous section.

  3. **Create an admin workstation** that has the resources and tools you need to create admin and user clusters, including the additional service accounts you need to finish the setup.

  4. **Create an admin cluster** to manage and update your user cluster.

  5. **Create a user cluster** to run your workloads.




## 1\. Log in to the Google Cloud CLI

Setting up Google Distributed Cloud requires multiple [service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#service-accounts) with different permissions. So you must be logged in to the Google Cloud CLI with an account that has the necessary permissions to create and configure service accounts, as `gkeadm` uses your current gcloud CLI `account` [property](https://docs.cloud.google.com/sdk/docs/properties) when doing this setup.

  1. Log in to the gcloud CLI. You can use any Google Account but it must have the [required permissions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#required_permissions). If you have followed the previous part of this guide you have probably already logged in with an appropriate account to create your component access service account.
         
         gcloud auth login
         

  2. Verify that your gcloud CLI `account` property is set correctly:
         
         gcloud config list
         

The output shows the value of your SDK `account` property. For example:
         
         [core]
         account = my-name@google.com
         disable_usage_reporting = False
         Your active configuration is: [default]
         

  3. Make sure you have the latest gcloud CLI components installed:
         
         gcloud components update
         

Depending on how you installed the gcloud CLI, you might see the following message: "You cannot perform this action because the gcloud CLI component manager is disabled for this installation. You can run the following command to achieve the same result for this installation:" Follow the instructions to copy and paste the command to update the components.




## 2\. Gather information

Use the information that you prepared in [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure) to edit the placeholders in the following table:

**Caution:** The editable placeholders in this table aren't persistent. Any values you enter in the table are reset if you close this browser tab. If the placeholders in the table are _not_ editable, refresh this page.vSphere details  
---  
The username of your vCenter account | USERNAME  
The password of your vCenter account | PASSWORD  
Your [vCenter Server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address) | ADDRESS  
The path to the [root CA certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path) for your vCenter Server, on the machine you're going to use to create your admin workstation | CA_CERT_PATH  
The name of your [vSphere data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) | DATA_CENTER  
The name of your [vSphere cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) | VSPHERE_CLUSTER  
The name or path of your [vSphere resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html). For more information, see [vcenter.resourcePool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-resourcepool-field). | RESOURCE_POOL  
The name of your [vSphere datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) | DATASTORE  
The name of your [vSphere network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-networking.html) | NETWORK  
IP addresses  
One IP address for your admin workstation | ADMIN_WS_IP  
Three IP addresses for your admin cluster control-plane nodes. |  ADMIN_CONTROL_PLANE_NODE_IP_1  
ADMIN_CONTROL_PLANE_NODE_IP_2  
ADMIN_CONTROL_PLANE_NODE_IP_3  
An IP address for the control-plane node in the user cluster. |  USER_CONTROL_PLANE_NODE_IP  
  
Four IP addresses for your user cluster worker nodes. This includes an address for an extra node that can be used during upgrade and update.  |  USER_NODE_IP_1  
USER_NODE_IP_2  
USER_NODE_IP_3  
USER_NODE_IP_4  
A virtual IP address (VIP) for the admin cluster Kubernetes API server | ADMIN_CONTROL_PLANE_VIP  
A VIP for the user cluster Kubernetes API server | USER_CONTROL_PLANE_VIP  
An Ingress VIP for the user cluster | USER_INGRESS_VIP  
Two VIPs for Services of type LoadBalancer in your user cluster. |  SERVICE_VIP_1  
SERVICE_VIP_2  
The IP address of a DNS server that is reachable from your admin workstation and cluster nodes |  DNS_SERVER_IP  
The IP address of an NTP server that is reachable from your admin workstation and cluster nodes |  NTP_SERVER_IP  
The IP address of the default gateway for the subnet that has your admin workstation and cluster nodes |  DEFAULT_GATEWAY_IP  
The netmask for the subnet that has your admin workstation and cluster nodes  
Example: `255.255.255.0` |  NETMASK  
If your network is behind a proxy server, the URL of the proxy server. For more information, see [proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-section). **Fill this in manually in your admin workstation configuration file if needed**. |  PROXY_URL  
CIDR ranges for Services and Pods   
The admin cluster and user cluster each need a CIDR range for Services and a CIDR range for Pods. Use the following prepopulated values unless you need to change them to [avoid overlap](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#avoid_overlap\)) with other elements in your network:   
A CIDR range for Services in the admin cluster | 10.96.232.0/24  
A CIDR range for Pods in the admin cluster | 192.168.0.0/16  
A CIDR range for Services in the user cluster | 10.96.0.0/20  
A CIDR range for Pods in the user cluster | 192.168.0.0/16  
Google Cloud details  
The ID of your chosen [Cloud project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#cloud-resources) | PROJECT_ID  
The path to the JSON key file for the [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#cloud-resources) that you set up in the previous section, on the machine that you're going to use to create your admin workstation. | COMPONENT_ACCESS_SA_KEY_PATH  
The email address that is associated with your Google Cloud account. For example: `alex@example.com`. | `GOOGLE_ACCOUNT_EMAIL`  
  
## 3\. Create an admin workstation

Before you can create any clusters, you need to create an admin workstation and then connect to it using SSH. The admin workstation is a standalone VM with the tools and resources you need to create Google Distributed Cloud clusters in your vSphere environment. You use the `gkeadm` command-line tool to create the admin workstation.

### Download gkeadm

Download `gkeadm` to your current directory:
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/1.36.100-gke.144/linux/gkeadm ./
    chmod +x gkeadm
    

You need the `gkeadm` version (which is also the version of Google Distributed Cloud) to create your admin and user cluster config files. To check the version of `gkeadm`, run the following:
    
    
    ./gkeadm version
    

The following example output shows the version.
    
    
    gkeadm 1.36.100 (1.36.100-gke.144)
    

Although you can [download another version of `gkeadm`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/download-gkeadm), this guide assumes that you are installing 1.36.100-gke.144, and uses that version in all configuration files and commands.

### Create your credentials file

Create and save a file named `credential.yaml` in your current directory with the following content:
    
    
    apiVersion: v1
    kind: CredentialFile
    items:
    - name: vCenter
      username: "USERNAME"
      password: "PASSWORD"
    

### Create your admin workstation configuration file

Create and save a file named `admin-ws-config.yaml`, again in your current directory, with the following content:
    
    
    gcp:
      componentAccessServiceAccountKeyPath: "COMPONENT_ACCESS_SA_KEY_PATH"
    vCenter:
      credentials:
        address: "ADDRESS"
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
      datacenter: "DATA_CENTER"
      datastore: "DATASTORE"
      cluster: "VSPHERE_CLUSTER"
      network: "NETWORK"
      resourcePool: "RESOURCE_POOL"
      caCertPath: "CA_CERT_PATH"
    proxyUrl: ""
    adminWorkstation:
      name: "minimal-installation-admin-workstation"
      cpus: 4
      memoryMB: 8192
      diskGB: 100
      dataDiskName: gke-on-prem-admin-workstation-data-disk/minimal-installation-data-disk.vmdk
      dataDiskMB: 512
      network:
        ipAllocationMode: "static"
        hostConfig:
          ip: "ADMIN_WS_IP"
          gateway: "DEFAULT_GATEWAY_IP"
          netmask: "NETMASK"
          dns:
          - "DNS_SERVER_IP"
      proxyUrl: ""
      ntpServer: ntp.ubuntu.com
    

### Create your admin workstation

Create your admin workstation using the following command:
    
    
    ./gkeadm create admin-workstation --auto-create-service-accounts
    

Running this command:

  * Creates your admin workstation
  * Automatically creates any additional service accounts you need for your installation
  * Creates template configuration files for your admin and user clusters



The output gives detailed information about the creation of your admin workstation and provides a command that you can use to get an SSH connection to your admin workstation. For example:
    
    
    ...
    Admin workstation is ready to use.
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    ********************************************************************
    

In the preceding output, the IP address is an example. The IP address of your admin workstation will be different. Make a note of the IP address of your admin workstation. You will need it in the next step.

For more detailed information about creating an admin workstation, see [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

### Connect to your admin workstation

Use the command displayed in the preceding output to get an SSH connection to your admin workstation. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    

If you need to find this command again, `gkeadm` generates a file called `gke-admin-ws-...` in the directory on your local machine where you ran `gkeadm create admin-workstation`. This contains details about your admin workstation, including the SSH command.

On your admin workstation, enter `exit` to terminate the SSH connection and return to your local machine.

### Copy the audit logging key to your admin workstation

In the previous section, you created a JSON key file for your [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#service-accounts).

Copy the JSON key file to the home directory on your admin workstation. For example, on your local machine:
    
    
    scp -i /usr/local/google/home/me/.ssh/gke-admin-workstation audit-logging-key.json ubuntu@172.16.20.49:~
    

### View files on your admin workstation

Once again, get an SSH connection to your admin workstation.

On your admin workstation, list the files in the home directory:
    
    
    ls -1
    

The output should include:

  * `admin-cluster.yaml`, a template config file for creating your admin cluster.
  * `user-cluster.yaml`, a template config file for creating your user cluster.
  * The vCenter certificate file that you specified in your admin workstation configuration
  * The `credential.yaml` file that you specified in your admin workstation configuration.
  * The JSON key file for your audit logging service account.
  * JSON key files for two service accounts that `gkeadm` created for you: a connect-register service account and a logging-monitoring service account, as well as the key file for the component access service account you created earlier.



For example:
    
    
    admin-cluster.yaml
    admin-ws-config.yaml
    audit-logging-key.json
    sa-key.json
    connect-register-sa-2203040617.json
    credential.yaml
    log-mon-sa-2203040617.json
    logs
    vc01-cert.pem
    user-cluster.yaml
    

You'll need to specify some of these filenames in your configuration files to create clusters. Use the filenames as values for the placeholders in the following table:

Connect-register service account key filename  
Example: `connect-register-sa-2203040617.json` | CONNECT_REGISTER_SA_KEY  
---|---  
Logging-monitoring service account key filename  
Example: `log-mon-sa-2203040617.json` | LOG_MON_SA_KEY  
Audit logging service account key filename  
Example: `audit-logging-key.json` | AUDIT_LOG_SA_KEY  
Component access service account key filename  
Example: `sa-key.json` | COMPONENT_ACCESS_SA_KEY  
vCenter certificate filename  
Example: `vc01-cert.pem` | CA_CERT_FILE  
  
## 4\. Create an admin cluster

Now that you have an admin workstation configured with your vCenter and other details, you can use it to create an admin cluster in your vSphere environment. Ensure you have an SSH connection to your admin workstation, as described previously, before starting this step. All of the following commands are run on the admin workstation.

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal name server in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

### Create your admin cluster configuration file

Open `admin-cluster.yaml` and replace the content with the following:
    
    
    apiVersion: v1
    kind: AdminCluster
    name: "minimal-installation-admin-cluster"
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.36.100-gke.144-full.tgz"
    vCenter:
      address: "ADDRESS"
      datacenter: "DATA_CENTER"
      cluster: "VSPHERE_CLUSTER"
      resourcePool: "RESOURCE_POOL"
      datastore: "DATASTORE"
      caCertPath: "CA_CERT_FILE"
      credentials:
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
    network:
      hostConfig:
        dnsServers:
        - "DNS_SERVER_IP"
        ntpServers:
        - "NTP_SERVER_IP"
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
      vCenter:
        networkName: "NETWORK"
      controlPlaneIPBlock:
        netmask: "NETMASK"
        gateway: "DEFAULT_GATEWAY_IP"
        ips:
        - ip: "ADMIN_CONTROL_PLANE_NODE_IP_1"
          hostname: "admin-cp-vm-1"
        - ip: "ADMIN_CONTROL_PLANE_NODE_IP_2"
          hostname: "admin-cp-vm-2"
        - ip: "ADMIN_CONTROL_PLANE_NODE_IP_3"
          hostname: "admin-cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "ADMIN_CONTROL_PLANE_VIP"
      kind: "MetalLB"
    adminMaster:
      cpus: 4
      memoryMB: 16384
      replicas: 3
    antiAffinityGroups:
      enabled: false
    componentAccessServiceAccountKeyPath: "COMPONENT_ACCESS_SA_KEY"
    gkeConnect:
      projectID: "PROJECT_ID"
      registerServiceAccountKeyPath: "CONNECT_REGISTER_SA_KEY"
    stackdriver:
      projectID: "PROJECT_ID"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "LOG_MON_SA_KEY"
      disableVsphereResourceMetrics: false
    cloudAuditLogging:
      projectID: "PROJECT_ID"
      clusterLocation: us-central1
      serviceAccountKeyPath: "AUDIT_LOG_SA_KEY"
    
    

#### Validate the admin cluster configuration file

Verify that the your admin cluster configuration file is valid and can be used for cluster creation:
    
    
    gkectl check-config --config admin-cluster.yaml
    

### Import OS images to vSphere

Run `gkectl prepare` with your completed config file to import node OS images to vSphere:
    
    
    gkectl prepare --config admin-cluster.yaml --skip-validation-all
    

Running this command imports the images to vSphere and marks them as VM templates, including the image for your admin cluster.

This command can take a few minutes to return.

### Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config admin-cluster.yaml
    

#### Resume admin cluster creation after a failure

If the admin cluster creation fails or is canceled, you can run the `create` command again:
    
    
    gkectl create admin --config admin-cluster.yaml
    

### Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

### Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig kubeconfig
    

The output shows the admin cluster nodes. For example:
    
    
    admin-cp-vm-1   Ready    control-plane,master ...
    admin-cp-vm-2   Ready    control-plane,master ...
    admin-cp-vm-3   Ready    control-plane,master ...
    

### Enable RBAC authorization

To grant your user account the Kubernetes `clusterrole/cluster-admin` role on the cluster, run the following command:
    
    
    gcloud container fleet memberships generate-gateway-rbac \
        --membership=minimal-installation-admin-cluster \
        --role=clusterrole/cluster-admin \
        --users=GOOGLE_ACCOUNT_EMAIL \
        --project=PROJECT_ID \
        --kubeconfig=kubeconfig \
        --context=minimal-installation-admin-cluster \
        --apply

The output of this command is similar to the following, which is truncated for readability:
    
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    Applying the generate RBAC policy to cluster with kubeconfig: kubeconfig, context: minimal-installation-admin-cluster
    Writing RBAC policy for user: GOOGLE_ACCOUNT_EMAIL to cluster.
    Successfully applied the RBAC policy to cluster.
    

Among other things, the RBAC policy lets you log in to your cluster in the Google Cloud console using your Google Identity to see more cluster details.

### Automatic enrollment in the GKE On-Prem API

Because the GKE On-Prem API is enabled in your project, the cluster is automatically enrolled in the GKE On-Prem API. Enrolling your admin cluster in the GKE On-Prem API lets you use standard tools—the Google Cloud console, the Google Cloud CLI, or [Terraform](https://www.terraform.io/)—to create, upgrade, update, and delete user clusters that the admin cluster manages. Enrolling your cluster also lets you run `gcloud` commands to [get information about your cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).

## 5\. Create a user cluster

This section provides steps for creating the user cluster using the console, `gkectl`, Terraform, or the gcloud CLI.

### `gkectl`

Ensure you have an SSH connection to your admin workstation, as described previously, before starting this procedure. All of the following commands are run on the admin workstation.

### Create your user cluster IP block file

  1. Create a file named `user-ipblock.yaml`.

  2. Copy and paste the following content into `user-ipblock.yaml` and save the file:
         
         blocks:
           - netmask: "NETMASK"
             gateway: "DEFAULT_GATEWAY_IP"
             ips:
             - ip: "USER_NODE_IP_1"
               hostname: "user-vm-1"
             - ip: "USER_NODE_IP_2"
               hostname: "user-vm-2"
             - ip: "USER_NODE_IP_3"
               hostname: "user-vm-3"
             - ip: "USER_NODE_IP_4"
               hostname: "user-vm-4"
         




### Create your user cluster configuration file

  1. Create a file named `user-cluster.yaml` in the same directory as `user-ipblock.yaml`.

  2. Copy and paste the following content into `user-cluster.yaml` and save the file:



    
    
    apiVersion: v1
    kind: UserCluster
    name: "minimal-installation-user-cluster"
    gkeOnPremVersion: "1.36.100-gke.144"
    enableControlplaneV2: true
    network:
      hostConfig:
        dnsServers:
        - "DNS_SERVER_IP"
        ntpServers:
        - "NTP_SERVER_IP"
      ipMode:
        type: "static"
        ipBlockFilePath: "user-ipblock.yaml"
      serviceCIDR: "10.96.0.0/20"
      podCIDR: "192.168.0.0/16"
      controlPlaneIPBlock:
        netmask: "NETMASK"
        gateway: "DEFAULT_GATEWAY_IP"
        ips:
        - ip: "USER_CONTROL_PLANE_NODE_IP"
          hostname: "cp-vm-1"
    loadBalancer:
      vips:
        controlPlaneVIP: "USER_CONTROL_PLANE_VIP"
        ingressVIP: "USER_INGRESS_VIP"
      kind: "MetalLB"
      metalLB:
        addressPools:
        - name: "uc-address-pool"
          addresses:
          - "USER_INGRESS_VIP/32"
          - "SERVICE_VIP_1/32"
          - "SERVICE_VIP_2/32"
    enableDataplaneV2: true
    nodePools:
    - name: "uc-node-pool"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      enableLoadBalancer: true
    antiAffinityGroups:
      enabled: false
    gkeConnect:
      projectID: "PROJECT_ID"
      registerServiceAccountKeyPath: "CONNECT_REGISTER_SA_KEY"
    stackdriver:
      projectID: "PROJECT_ID"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "LOG_MON_SA_KEY"
      disableVsphereResourceMetrics: false
    autoRepair:
      enabled: true
    

### Validate the configuration and create the cluster

Support for the `gkectl check-config` command on advanced user clusters was added in the following versions: 1.32.700+, 1.33.300+, and 1.34.0 and higher. If you are installing a lower version on an advanced cluster, the command will fail.

  1. Verify that the your user cluster configuration file is valid and can be used for cluster creation:
         
         gkectl check-config --kubeconfig kubeconfig --config user-cluster.yaml

  2. Create the user cluster:
         
         gkectl create cluster --kubeconfig kubeconfig --config user-cluster.yaml

Cluster creation takes approximately 30 minutes.




### Locate the user cluster kubeconfig file

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

### Verify that your user cluster is running

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    cp-vm-1     Ready    control-plane,master
    user-vm-1   Ready
    user-vm-2   Ready
    user-vm-3   Ready
    

### Enable RBAC authorization

To grant your user account the Kubernetes `clusterrole/cluster-admin` role on the cluster, run the following command:
    
    
    gcloud container fleet memberships generate-gateway-rbac \
      --membership=minimal-installation-user-cluster \
      --role=clusterrole/cluster-admin \
      --users=GOOGLE_ACCOUNT_EMAIL \
      --project=PROJECT_ID \
      --kubeconfig=USER_CLUSTER_KUBECONFIG \
      --context=minimal-installation-user-cluster \
      --apply

The output of this command is similar to the following, which is truncated for readability:
    
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    Applying the generate RBAC policy to cluster with kubeconfig: kubeconfig, context: minimal-installation-admin-cluster
    Writing RBAC policy for user: GOOGLE_ACCOUNT_EMAIL to cluster.
    Successfully applied the RBAC policy to cluster.
    

Among other things, the RBAC policy lets you log in to your cluster in the Google Cloud console using your Google Identity to see more cluster details.

### Automatic enrollment in the GKE On-Prem API

Because the GKE On-Prem API is enabled in your project, the cluster is automatically enrolled in the GKE On-Prem API. This lets you use the console or the gcloud CLI to view cluster details and manage the cluster lifecycle. For example, you run can `gcloud` commands to [get information about your user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).

### Console

  1. In the Google Cloud console, go to the **Create a Google Distributed Cloud cluster** page.

[Go to Create a Google Distributed Cloud cluster](https://console.cloud.google.com/kubernetes/vmware/add)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.




The following sections guide you through configuring the user cluster.

### Prerequisites

  1. Familiarize yourself with the information on the **Prerequisites** page.

  2. At the bottom of the page, click **Next**.




### Cluster basics

  1. For **Name** , enter a name for the user cluster: for example, `minimal-installation-user-cluster`.

  2. For **Admin cluster** , select **minimal-installation-admin-cluster**.

  3. For **GCP API Location** field, select the **us-central1**.

  4. For **Version** , select 1.36.100-gke.144.

  5. You don't need to open the **Authorization** section or the **vCenter configuration** section.

  6. Click **Next**.




### Control Plane

  1. Under **Control plane node IPs** , for **Gateway** , enter DEFAULT_GATEWAY_IP.

  2. For **Subnet mask** , enter NETMASK.

  3. Under **IP addresses** , for **IP address 1** , enter USER_CONTROL_PLANE_NODE_IP. Leave **Hostname 1** blank.

  4. Click **Next**.




### Networking

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. A user cluster needs to have one IP address for each node and an additional IP address for a temporary node that is needed during cluster upgrades, updates, and auto repair. For more information, see [How many IP addresses does a user cluster need?](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_a_user_cluster_need).

  1. Under **Worker node IPs** , for **IP mode** , make sure that **Static** is selected.

  2. For **Gateway** , enter DEFAULT_GATEWAY_IP.

  3. For **Subnet mask** , enter NETMASK.

  4. Under **IP addresses** , enter these addresses:



  * USER_NODE_IP_1
  * USER_NODE_IP_2
  * USER_NODE_IP_3
  * USER_NODE_IP_4



Leave the **Hostname** fields blank.

  1. For **Service CIDR** , enter 10.96.0.0/20. For **Pod CIDR** , enter 192.168.0.0/16.

  2. For **DNS Server 1** , enter DNS_SERVER_IP.

  3. For **NTP Server 1** , enter NTP_SERVER_IP.

  4. Leave **DNS search domain** blank.

  5. Click **Next**.




### Load balancer

  1. For **Load balancer type** , select **Bundled with MetalLB**.

  2. Under **Address pools** , use the default name.

  3. Under **IP addresses** , for **IP address range 1** , enter USER_INGRESS_VIP/32.

Click **Add IP address range**. For **IP address range 1** , enter SERVICE_VIP_1/32

Click **Add IP address range**. For **IP address range 2** , enter SERVICE_VIP_2/32

  4. For **Assignment of IP addresses** , select **Automatic**.

  5. Leave **Avoid buggy IP addresses** unchecked.

  6. Under **Virtual IPs** , for **Control plane VIP** enter USER_CONTROL_PLANE_VIP. **Ingress VIP** is already filled in.

  7. Click **Continue**.




### Features

  1. Leave all the defaults in place.

  2. Click **Next**.




### Node pools

  1. Leave all the defaults in place.

  2. Click **Verify and Complete** to create the user cluster. It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster in your data center.

If an error is encountered verifying the settings, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

For more information about possible errors and how to fix them, see [Troubleshoot clusters enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/on-prem-api).




### Terraform

This section shows you how to create a user cluster and a node pool using Terraform. For more information and other examples, see the following:

  * [`google_gkeonprem_vmware_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster)

  * [google_gkeonprem_vmware_node_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_node_pool)

  * [terraform.tfvars.sample](https://github.com/GoogleCloudPlatform/anthos-samples/blob/HEAD/anthos-onprem-terraform/avmw_user_cluster_metallb/terraform.tfvars.sample)



  1. Create a directory and a new file within that directory. The filename must have the `.tf` extension. In this guide, the file is called `main.tf`.
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf
         

  2. Verify the user cluster Terraform resource:

The following Terraform resource example is filled in with the values that you entered in the planning table in the preceding section.
         
         resource "google_gkeonprem_vmware_cluster" "cluster-basic" {
           name = "minimal-installation-user-cluster"
           project = "PROJECT_ID"
           location = "us-central1"
           admin_cluster_membership = "projects/PROJECT_ID/locations/global/memberships/minimal-installation-admin-cluster"
           description = "User cluster config with MetalLB, static IPs, and Controlplane V2"
           enable_control_plane_v2 = "true"
           on_prem_version = "1.36.100-gke.144"
           control_plane_node {
             cpus = 4
             memory = 8192
             replicas = 1
           }
           network_config {
             service_address_cidr_blocks = ["10.96.0.0/20"]
             pod_address_cidr_blocks = ["192.168.0.0/16"]
             host_config {
               dns_servers = ["DNS_SERVER_IP"]
               ntp_servers = ["NTP_SERVER_IP"]
             }
             static_ip_config {
               ip_blocks {
                 netmask = "NETMASK"
                 gateway = "DEFAULT_GATEWAY_IP"
                 ips {
                   ip = "USER_NODE_IP_1"
                   hostname = "user-vm-1"
                 }
                 ips {
                   ip = "USER_NODE_IP_2"
                   hostname = "user-vm-2"
                 }
                 ips {
                   ip = "USER_NODE_IP_3"
                   hostname = "user-vm-3"
                 }
                 ips {
                   ip = "USER_NODE_IP_4"
                   hostname = "user-vm-4"
                 }
               }
             }
             control_plane_v2_config {
               control_plane_ip_block {
                 netmask = "NETMASK"
                 gateway = "DEFAULT_GATEWAY_IP"
                 ips {
                   ip = "USER_CONTROL_PLANE_NODE_IP"
                   hostname = "cp-vm-1"
                 }
               }
             }
           }
           load_balancer {
             vip_config {
               control_plane_vip = "USER_CONTROL_PLANE_VIP"
               ingress_vip = "USER_INGRESS_VIP"
             }
             metal_lb_config {
               address_pools {
                 pool = "uc-address-pool"
                 manual_assign = "true"
                 addresses = ["USER_INGRESS_VIP/32", "SERVICE_VIP_1/32", "SERVICE_VIP_2/32"]
               }
             }
           }
           authorization {
             admin_users {
             username = "GOOGLE_ACCOUNT_EMAIL"
           }
         }
           provider = google-beta
         }
         
         resource "google_gkeonprem_vmware_node_pool" "my-node-pool-1" {
           name = "uc-node-pool"
           project = "PROJECT_ID"
           vmware_cluster = "minimal-installation-user-cluster"
           location = "us-central1"
           config {
             replicas = 3
             image_type = "ubuntu_containerd"
             enable_load_balancer = "true"
           }
           depends_on = [
             google_gkeonprem_vmware_cluster.cluster-basic
           ]
           provider = google-beta
         }
         

  3. Copy the Terraform resource to `main.tf` and save the file.

  4. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider.

  5. Review the configuration and make changes if needed:
         
         terraform plan
         

  6. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

When prompted, enter `yes`.

It takes about 15 minutes (or more depending on your network) to create the basic user cluster and node pool.




### gcloud

Create the cluster:
    
    
    gcloud container vmware clusters create minimal-installation-user-cluster \
      --project=PROJECT_ID \
      --admin-cluster-membership=projects/PROJECT_ID/locations/global/memberships/minimal-installation-admin-cluster \
      --location=us-central1 \
      --version=1.36.100-gke.144 \
      --admin-users=GOOGLE_ACCOUNT_EMAIL \
      --service-address-cidr-blocks=10.96.0.0/20 \
      --pod-address-cidr-blocks=192.168.0.0/16 \
      --metal-lb-config-address-pools='pool=uc-address-pool,avoid-buggy-ips=False,manual-assign=False,addresses=USER_INGRESS_VIP/32;SERVICE_VIP_1/32;SERVICE_VIP_2/32' \
      --control-plane-vip=USER_CONTROL_PLANE_VIP \
      --ingress-vip=USER_INGRESS_VIP \
      --static-ip-config-ip-blocks='gateway=DEFAULT_GATEWAY_IP,netmask=NETMASK,ips=USER_NODE_IP_1;USER_NODE_IP_2;USER_NODE_IP_3;USER_NODE_IP_4' \
      --dns-servers=DNS_SERVER_IP \
      --ntp-servers=NTP_SERVER_IP \
      --enable-control-plane-v2 \
      --enable-dataplane-v2 \
      --control-plane-ip-block='gateway=DEFAULT_GATEWAY_IP,netmask=NETMASK,ips=USER_CONTROL_PLANE_NODE_IP'
    

The output from the command is similar to the following:
    
    
    Waiting for operation [projects/example-project-12345/locations/us-central1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
    

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation with the following command:
    
    
    gcloud container vmware operations describe OPERATION_ID \
      --project=PROJECT_ID \
      --location=us-central1
    

For more information, see [gcloud container vmware operations](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/operations).

It takes 15 minutes or more to create the user cluster. You can view the cluster in the console on the [Google Kubernetes Engine Clusters overview page](https://console.cloud.google.com/kubernetes/list/overview).

Create a node pool:
    
    
    gcloud container vmware node-pools create  uc-node-pool \
      --cluster=minimal-installation-user-cluster \
      --project=PROJECT_ID \
      --location=us-central1 \
      --image-type=ubuntu_containerd  \
      --boot-disk-size=40 \
      --cpus=4 \
      --memory=8192 \
      --replicas=3 \
      --enable-load-balancer
    

## What's next

You have now completed this minimal installation of Google Distributed Cloud. As an optional follow-up, you can see your installation in action by [deploying an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
