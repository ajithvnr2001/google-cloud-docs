---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-terraform/
title: Create an admin cluster using Terraform \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:34:42.358565+00:00
---

# Create an admin cluster using Terraform  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create an admin cluster using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create an admin cluster for Google Distributed Cloud software only for VMware if already you use Terraform to manage your Google Cloud and on-premise VMware resources. You can also create an admin cluster using [`gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-gkectl) or [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-console).

## Before you begin

  * Make sure you have set up and can sign in to your admin workstation as described in [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

  * Make sure the JSON key files for the service accounts are on your admin workstation.

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available for the three control-plane nodes and a control-plane VIP. If you plan to create any [kubeception user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster), then you must have enough IP addresses available for the control-plane nodes of those user clusters.

  * Review the [load balancing overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. For manual load balancers, you must set up the load balancer before you create your admin cluster.

  * If you are using `gkectl` to create the admin cluster, decide whether you want to use a public or private registry for Google Distributed Cloud components. For information on using a private Docker registry, see [`privateRegistry`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section). Neither Terraform nor the Google Cloud console support using a private Docker registry for system components.

  * Decide what type of operating system you want to run on your admin cluster nodes.

  * If your organization requires outbound traffic to pass through a proxy server, make sure to [allowlist](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#allowlist_addresses) required APIs and the Artifact Registry address.

  * In version 1.29 and higher, server-side preflight checks are enabled by default. Server-side preflight checks require additional firewall rules. In [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters), search for "Preflight checks" and make sure all required firewall rules are configured. Server-side preflight checks are run on the bootstrap cluster instead of locally on the admin workstation.




### Procedure overview

Before you create the admin cluster, you need to run the `gkectl register bootstrap` command on your admin workstation. This command deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (_kind_) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create the admin cluster. When you create the admin cluster, the controllers on the bootstrap cluster will provision nodes, run preflight checks, and register the admin cluster to the fleet. The bootstrap cluster is automatically deleted after the admin cluster is successfully created.

The following are the high-level steps for creating an admin cluster using Terraform:

  1. Fill in your configuration file. Use the [google_gkeonprem_vmware_admin_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_admin_cluster) resource and the example that follows to create the `main.tf` configuration file.

  2. Create a `bootstrap` cluster. Run the `gkectl register bootstrap` to create the bootstrap cluster. When the command finishes creating the bootstrap cluster, the output lets you know to finish the admin cluster configuration. The process continues to run until the admin cluster is created.

  3. Create an admin cluster. In another terminal window or on another computer that has access to the GKE On-Prem API, run `terraform` commands to create a new admin cluster as specified in your completed `main.tf` configuration file.




### Fill in your configuration file

The following example shows creating a high-availability (HA) admin cluster with three control-plane nodes with MetalLB. In 1.28 and higher, new admin clusters must be highly available. Because of this requirement, you must set `control_plane_node.replicas` to 3.

For more information and other examples, see the [`google_gkeonprem_vmware_admin_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_admin_cluster). For information on using a private registry for system images, see [Configure a private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).

Fill in the placeholder variables in the following example, then copy and paste it to `main.tf`. If you used `gkeadm` to create your admin workstation, open your admin workstation configuration file so you can copy values from the `vCenter` section to the corresponding placeholder variables.
    
    
    resource "google_gkeonprem_vmware_admin_cluster" "admin-cluster-metallb" {
      provider = google-beta
      name = "ADMIN_CLUSTER_NAME"
      project = "PROJECT_ID"
      location = "REGION"
      description = "DESCRIPTION"
      bootstrap_cluster_membership = "projects/PROJECT_ID/locations/REGION/memberships/bootstrap-ADMIN_CLUSTER_NAME"
      on_prem_version = "VERSION"
      image_type = "IMAGE_TYPE"
      vcenter {
        address = "VCENTER_ADDRESS"
        datacenter = "DATA_CENTER"
        cluster = "VCENTER_CLUSTER"
        resource_pool = "RESOURCE_POOL"
        datastore = "DATASTORE"
        ca_cert_data = "CA_CERT_DATA"
      }
      network_config {
        service_address_cidr_blocks = ["10.96.232.0/24"]
        pod_address_cidr_blocks = ["192.168.0.0/16"]
        vcenter_network = "NETWORK"
        dhcp_ip_config {
          enabled = true
        }
        host_config {
          dns_servers = ["DNS_SERVERS"]
          ntp_servers = ["NTP_SERVERS"]
        }
        ha_control_plane_config {
          control_plane_ip_block {
            gateway = "GATEWAY"
            netmask = "NETMASK"
            ips {
              hostname = "CONTROL_PLANE_HOST_1"
              ip       = "CONTROL_PLANE_NODE_IP_1"
            }
            ips {
              hostname = "CONTROL_PLANE_HOST_2"
              ip       = "CONTROL_PLANE_NODE_IP_2"
            }
            ips {
              hostname = "CONTROL_PLANE_HOST_3"
              ip       = "CONTROL_PLANE_NODE_IP_3"
            }
          }
        }
      }
      control_plane_node {
         cpus = NUM_CPUS
         memory = MEMORY
         replicas = 3
      }
      load_balancer {
        vip_config {
          control_plane_vip = "CONTROL_PLANE_VIP"
        }
        metal_lb_config {
          enabled = true
        }
      }
    }
    

Replace the following:

  * `ADMIN_CLUSTER_NAME`: the name for the admin cluster. The name has a maximum length of 20 characters.

  * `PROJECT_ID`: the Google Cloud project ID.

  * `REGION`: the Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api).

The `location` field corresponds to the `--location` flag in the `gkectl register bootstrap` command.

  * `DESCRIPTION`: a description of the admin cluster.

  * `VERSION`: the Google Distributed Cloud version for the cluster. Creating a cluster using Terraform is supported only on versions 1.28 and higher. The version you specify here must match the version of the bundle that you specify in the `--bundle-path` flag in the `gkectl register bootstrap` command. For a list of versions, see [Google Distributed Cloud versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

  * `IMAGE_TYPE`: the type of OS image to run on your admin cluster nodes. Specify one of the following: "`ubuntu_containerd`", "`cos`", "`ubuntu_cgv2`", or "`cos_cgv2`".

  * `VCENTER_ADDRESS`: the [vCenter Server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address).

    * **Admin workstation configuration file** : Use the value from the `vCenter.credentials.address` field.

    * The `vcenter.address` field corresponds to the `--vcenter-address` flag in the `gkectl register bootstrap` command.

  * `DATA_CENTER`: the name of your [vCenter data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html).

    * **Admin workstation configuration file** : Use the value from the `vCenter.datacenter` field.

    * The `vcenter.datacenter` field corresponds to the `--vcenter-datacenter` flag in the `gkectl register bootstrap` command.

  * `VCENTER_CLUSTER`: the name of your [vCenter cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

    * **Admin workstation configuration file** : Use the value from the `vCenter.cluster` field.

    * The `vcenter.cluster` field corresponds to the `--vcenter-cluster` flag in the `gkectl register bootstrap` command.

  * `RESOURCE_POOL`: the name or path of your [vCenter resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

    * **Admin workstation configuration file** : Use the value from the `vCenter.resourcePool` field.

    * The `vcenter.resource_pool` field corresponds to the `--vcenter-resource-pool` flag in the `gkectl register bootstrap` command.

  * `DATASTORE`: the name of your [vCenter datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html). The value you specify must be a name, not a path. If you need to enter a path, add the following field: `folder = "FOLDER"`

    * **Admin workstation configuration file** : Use the value from the `vCenter.datastore` field.

    * The `vcenter.datastore` field corresponds to the `--vcenter-datastore` flag in the `gkectl register bootstrap` command.

If you want to use a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the cluster nodes, remove the `vcenter.datastore` field and add `vcenter.storage_policy_name` instead. Additionally, add the `--vcenter-storage-policy` flag to the `gkectl register bootstrap` command. You must specify a value for either `vcenter.datastore` or `vcenter.storage_policy_name`, but not both.

  * `FOLDER`: the name of the [vCenter folder](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-folders) where your cluster VMs will be located. If you aren't using a folder, remove this field.

    * **Admin workstation configuration file** : Use the value from the `vCenter.folder` field.

    * The `vcenter.folder` field corresponds to the `--vcenter-folder` flag in the `gkectl register bootstrap` command.

  * `CA_CERT_DATA`: the vCenter CA certificate in PEM format but with all the newlines replaced with the string `\n`.

    1. Run the following command to replace newlines with `\n`:
           
           awk 'ORS="\\n" {print}' CA_CERT_PATH_LOCAL
           

Replace `CA_CERT_PATH_LOCAL` with the path to the [root CA certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path) for your vCenter Server. If you used `gkeadm` to create your admin workstation, you can use the value from the `caCertPath` field in the admin workstation configuration file, which is the path on your local computer. `gkeadm` copied the CA certificate file to your admin workstation. You must specify the admin workstation path in the `--vcenter-ca-cert-path` flag in the `gkectl register bootstrap` command.

    2. Copy the output of the previous command and paste it into the `CA_CERT_DATA` placeholder variable.

  * `NETWORK`: the name of your [vCenter network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-networking.html).

    * **Admin workstation configuration file** : use the value from the `vCenter.network` field.

    * The `network_config.vcenter_network` field corresponds to the `--vcenter-network` flag in the `gkectl register bootstrap` command.

  * `GATEWAY`: the IP address of the default gateway for the subnet that has your control-plane cluster nodes.

  * `NETMASK`: the netmask for the subnet that has your control-plane cluster nodes.

  * `DNS_SERVERS`: the IP address of the DNS server.

  * `NTP_SERVERS`: the IP address of the time (NTP) server.

  * Enter the IP addresses and optionally, the hostname for the three control-plane nodes in the `control_plane_ip_block.ips` section. If you don't enter a hostname, remove the `hostname` fields from the config.

  * `NUM_CPUS` : the number of vCPUs for each control-plane node in the admin cluster. Must be a minimum of 4.

  * `MEMORY`: number of mebibytes of memory for each control-plane node in the admin cluster. Must be a minimum of 8192, but we recommend 16384.

  * `CONTROL_PLANE_VIP`: the IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the admin cluster.




#### Optional: Configure a private registry

By default during cluster creation or upgrade, Google Distributed Cloud pulls system images from `gcr.io/gke-on-prem-release` using the [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account). Optionally, you can provide your own container registry server so that system images are pulled from your private registry server instead.

To configure a private registry do the following:

  1. Add the following to the admin cluster configuration file:
         
         private_registry_config {
           address = "ADDRESS"
           ca_cert = "CA_CERT"
         }
         

Replace the following:

     * `ADDRESS`: the IP address or FQDN (Fully Qualified Domain Name) of the machine that runs your private registry.

     * `CA_CERT`: the CA certificate data of the public key but with all the newlines replaced with the string `\n`.

     1. Run the following command to replace newlines with `\n`:
            
            awk 'ORS="\\n" {print}' PUBLIC_KEY_PATH
            

Replace `PUBLIC_KEY_PATH` with the path to the public key.

     2. Copy the output of the previous command and paste it into the `CA_CERT` placeholder variable.

  2. If your network is behind a proxy server, add the following:
         
         proxy {
           url: "PROXY_SERVER_ADDRESS"
           no_proxy: "BYPASS_LIST"
         }
         

Replace the following:

     * `PROXY_SERVER_ADDRESS`: the HTTP address of your proxy server. Include the port number even if it's the same as the scheme's default port.

     * `BYPASS_LIST`: a comma-separated list of IP addresses, IP address ranges, host names, and domain names that shouldn't go through the proxy server.

Example:
    
    url: "http://my-proxy.example.local:80"
    no_proxy: "192.0.2.0/24,my-host.example.local,198.51.100.0"
    

When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request bypasses the proxy server and is sent directly to the destination.




For more information about using a private registry, including differences between normal clusters and advanced clusters, see [Configure a private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).

#### Verify the configuration file and plan

In the directory where `main.tf` is located, run the following commands:

  1. Initialize Terraform:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. Fix any errors in `maint.tf` if needed.

  2. Create the Terraform plan:
         
         terraform plan -out tfplan
         

Review the configuration and make changes if needed.




Before you apply the plan, you must first create the bootstrap cluster as described in the next section.

### Create the bootstrap cluster

When you run the `gkectl register bootstrap` command, it prompts you for the vCenter account username and password. Make sure you have the credentials available. If you used `gkeadm` to create the admin workstation, the username and password are in the file `credential.yaml`.

  1. Log on to your admin workstation using SSH.

  2. Authenticate with the Google Cloud CLI:
         
         gcloud auth login
         

  3. Run the following command to create the bootstrap cluster. Many of the flag values are the same as in the `main.tf` fields. Note, however, the command takes additional values that you must specify in the provided placeholder variables.
         
         gkectl register bootstrap \
             --target-cluster-name=ADMIN_CLUSTER_NAME \
             --project-id=PROJECT_ID \
             --location=REGION \
             --vcenter-address=VCENTER_ADDRESS \
             --vcenter-datacenter=DATA_CENTER \
             --vcenter-cluster=VCENTER_CLUSTER \
             --vcenter-resource-pool=RESOURCE_POOL \
             --vcenter-datastore=DATASTORE \
             --vcenter-network=NETWORK \
             --vcenter-ca-cert-path=CA_CERT_PATH \
             --bundle-path=BUNDLE_PATH \
             --component-access-service-account-key-path=COMPONENT_ACCESS_SA_PATH \
             --register-service-account-key-path=CONNECT_REGISTER_SA_PATH \
             --stackdriver-service-account-key-path=LOG_MON_SA_PATH \
             --cloud-audit-logging-service-account-key-path=CLOUD_AUDIT_SA_PATH \
             --admin-kubeconfig-out=KUBECONFIG_NAME
         

Replace the following with admin workstation paths:

     * `CA_CERT_PATH`: the path to the root CA certificate for your vCenter Server.
     * `BUNDLE_PATH`: the path to the bundle file. If you used `gkeadm` to create the admin workstation, the bundle file is located in `/var/lib/gke/bundles/`. The file name depends on the Google Distributed Cloud version, for example, `gke-onprem-vsphere-1.31.0-gke.889-full.tgz`.
     * `COMPONENT_ACCESS_SA_PATH`: the path to key file for the component access service account.
     * `CONNECT_REGISTER_SA_PATH`: the path to the key file for the connect-register service account.
     * `LOG_MON_SA_PATH`: the path to the key file for the logging-monitoring service account.
     * `CLOUD_AUDIT_SA_PATH`: the path to the audit logging service account. If you didn't create an audit logging service account, specify the path to the key file for the logging-monitoring service account.
     * `KUBECONFIG_NAME`: the name for kubeconfig file that the `gkectl register bootstrap` command creates. If you don't specify this flag, the command creates the file with the name `kubeconfig` in the current working directory. If there's an existing file called `kubeconfig`, the command overwrites the file.

Modify the command as needed for the following flags:

     * If you specified a folder in `main.tf`, add the following flag: `--vcenter-folder=FOLDER`
     * If you specified a VM storage policy in `main.tf`, remove `--vcenter-datastore` and add the following flag: `--vcenter-storage-policy-name=STORAGE_POLICY_NAME`
     * If your admin workstation will be on a network that's behind a proxy server, add the following flags:

       * `--proxy-url=PROXY_URL`
       * `--no-proxy=NO_PROXY`

Replace the following:

       * PROXY_URL: the URL of the proxy server.
       * NO_PROXY: the value of the domains and IP addresses excluded from proxying, separated by comma.

If you add a flag, make sure you add the command line continuation backslash character (\\).

  4. When prompted, enter (or copy and paste) the vCenter username. The username isn't echoed back to the screen.

  5. When prompted, enter (or copy and paste) the vCenter password. The password isn't echoed back to the screen.




The command runs numerous validations. After `gkectl` successfully creates the bootstrap cluster, you see output similar to the following, which is truncated for readability:
    
    
    Running workstation validations
    - Validation Category: Workstation
        - [SUCCESS] Workstation OS
        - [SUCCESS] Workstation Hardware
        - [SUCCESS] Workstation Package
        - [SUCCESS] Workstation NTP
        - [SUCCESS] Workstation Docker
    ...
    All validation results were SUCCESS.
    Unpacking GKE on-prem bundle: /var/lib/gke/bundles/gke-onprem-vsphere-1.31.0-gke.889-full.tgz
    ...
    Successfully created and registered the bootstrap cluster
    ...
    Waiting for preflight checks to run or OnPremAdminCluster to be applied...... -
    

The process continues to run until the admin cluster is created.

**Caution:** Leave the command running while you create the admin cluster. After the cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.

If you exit out of the `gkectl register bootstrap` command before the admin cluster is created, the admin cluster creation fails, and you will need to delete the bootstrap cluster using the following command:
    
    
    gkectl delete bootstrap \
        --target-cluster-name=ADMIN_CLUSTER_NAME \
        --project-id=PROJECT_ID \
        --location=REGION \
         --register-service-account-key-path=CONNECT_REGISTER_SA_PATH
    

### Create the admin cluster

Apply the Terraform plan to create the admin cluster:
    
    
    terraform apply "tfplan"
    

It takes about 15 minutes or more to create the admin cluster. You can view the cluster in the Google Cloud console on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page.

## Connect to the admin cluster

The `gkectl register bootstrap` command creates a `kubeconfig` file for the admin cluster on your admin workstation. If you didn't specify the `--admin-kubeconfig-out` flag when you ran `gkectl register bootstrap`, the command creates a kubeconfig file called `kubeconfig` in the directory in which you ran the command.

You need to restrict access to this `kubeconfig` because it contains authentication credentials for the cluster.

Additionally, you can run read-only `kubectl` commands through the connect gateway.

  1. Run the following command on a computer that has gcloud CLI on it to get a `kubeconfig` entry that can access the cluster through the connect gateway.
         
         gcloud container fleet memberships get-credentials ADMIN_CLUSTER_NAME \
             --project=PROJECT_ID
         

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: PROJECT_ID
         A new kubeconfig entry "connectgateway_PROJECT_ID_global_ADMIN_CLUSTER_NAME" has been generated and set as the current context.
         

  2. You can now run read-only `kubectl` commands through the connect gateway, such as the following:
         
         kubectl get pods -A
         

If you need full administrative privileges to the admin cluster, see [Set up the connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
