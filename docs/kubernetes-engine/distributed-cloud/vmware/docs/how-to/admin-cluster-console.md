---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-console/
title: Create an admin cluster using the Google Cloud console \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:57.508076+00:00
---

# Create an admin cluster using the Google Cloud console  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create an admin cluster using the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Use Google Cloud console to create an admin cluster for Google Distributed Cloud software only for VMware to use a graphical user interface for structured guidance. You can also create an admin cluster using [`gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-gkectl) or [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-console).

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  * Make sure you have set up and can sign in to your admin workstation as described in [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

  * Make sure the JSON key files for the service accounts are on your admin workstation.

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available for the three control-plane nodes and a control-plane VIP. If you plan to create any [kubeception user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster), then you must have enough IP addresses available for the control-plane nodes of those user clusters.

  * Review the [load balancing overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. For manual load balancers, you must set up the load balancer before you create your admin cluster.

  * If you are using `gkectl` to create the admin cluster, decide whether you want to use a public or private registry for Google Distributed Cloud components. For information on using a private Docker registry, see [`privateRegistry`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section). Neither Terraform nor the Google Cloud console support using a private Docker registry for system components.

  * Decide what type of operating system you want to run on your admin cluster nodes.

  * If your organization requires outbound traffic to pass through a proxy server, make sure to [allowlist](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#allowlist_addresses) required APIs and the Artifact Registry address.

  * In version 1.29 and higher, server-side preflight checks are enabled by default. Server-side preflight checks require additional firewall rules. In [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters), search for "Preflight checks" and make sure all required firewall rules are configured. Server-side preflight checks are run on the bootstrap cluster instead of locally on the admin workstation.




## Procedure overview

Before you create the admin cluster, you need to run the `gkectl register bootstrap` command on your admin workstation. This command deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (_kind_) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create the admin cluster. When you create the admin cluster, the controllers on the bootstrap cluster will provision nodes, run preflight checks, and register the admin cluster to the fleet. The bootstrap cluster is automatically deleted after the admin cluster is successfully created.

The following are the high-level steps for creating an admin cluster using the console:

  1. In the console, you enter information that the `gkectl register bootstrap` requires. The console displays the `gkectl register bootstrap` command with the information that you entered. The displayed command also includes flags for paths that you will need to specify before you run the command.

  2. On your admin workstation, you run `gkectl register bootstrap` to create the bootstrap cluster. When the command finishes creating the bootstrap cluster, the output lets you know to finish the admin cluster configuration. The process continues to run until the admin cluster is created.

  3. You return to the console to finish entering the information needed to create the cluster. During cluster creation, the `gkectl register bootstrap` command outputs progress information and writes logs on your admin workstation. When the admin cluster is created, the bootstrap cluster is automatically deleted.




## Begin configuring the cluster

  1. In the console, go to the **Create a cluster on VMware** page.

[Go to Create a cluster on VMware](https://console.cloud.google.com/kubernetes/vmware/add)

  2. Select the Google Cloud project that you want to create the cluster in.

When you create the bootstrap cluster in a following section, the selected project ID is displayed in the `gkectl register bootstrap` command in the `--project-id` flag.

  3. Make sure **Create an admin cluster** is selected.

  4. Click **Next: Install bootstrap environment**.




### Install bootstrap environment

In this section you enter the information that the `gkectl register bootstrap` command requires. As you enter values in the UI fields, the console copies the values to the corresponding flags for the `gkectl register bootstrap` command that is displayed in the **Bootstrap environment from admin workstation** section at the bottom of the page.

### Bootstrap environment basics

  1. Enter a **Name** for the admin cluster. The console uses the cluster name as the value for the `--target-cluster-name` flag in the `gkectl register bootstrap` command displayed at the bottom of the page. The name has a maximum length of 20 characters.

  2. In the **Google Cloud API Location** field, select a Google Cloud [region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api) from the list. This setting specifies the region where the following APIs and services run:

     * GKE On-Prem API (`gkeonprem.googleapis.com`)
     * Fleet service (`gkehub.googleapis.com`)
     * Connect service (`gkeconnect.googleapis.com`)

This setting also controls the region in which the following are stored:

     * The cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The **Google Cloud API Location** field corresponds to the `--location` flag in the `gkectl register bootstrap` command.

  3. In the **Admin cluster version** field, enter the version to use to create the cluster. The version you select here must match the version of the bundle that you specify in the `--bundle-path` flag in the `gkectl register bootstrap` command.




### vCenter configuration

If you used `gkeadm` to create your admin workstation, open your admin workstation configuration file so you can copy values from the `vCenter` section to the fields in the console. Note that the generated admin cluster configuration file also contains this information.

Most of the fields in this section are immutable. Refer to the [`vCenter` section](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-section) in the admin cluster configuration file reference if you need to know if a field is mutable or immutable.

  1. In the **Address** field, enter the [vCenter Server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address).

     * **Admin workstation configuration file** : Use the value from the `vCenter.credentials.address` field.

     * The **Address** field corresponds to the `--vcenter-address` flag in the `gkectl register bootstrap` command.

  2. In the **Datacenter** field, enter the name of your [vCenter data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html).

     * **Admin workstation configuration file** : Use the value from the `vCenter.datacenter` field.

     * The **Datacenter** field corresponds to the `--vcenter-datacenter` flag in the `gkectl register bootstrap` command.

  3. In the **Cluster Name** field, enter the name of your [vCenter cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

     * **Admin workstation configuration file** : Use the value from the `vCenter.cluster` field.

     * The **Cluster Name** field corresponds to the `--vcenter-cluster` flag in the `gkectl register bootstrap` command.

  4. In the **Resource pool** field, enter the name or path of your [vCenter resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

     * **Admin workstation configuration file** : Use the value from the `vCenter.resourcePool` field.

     * The **Resource pool** field corresponds to the `--vcenter-resource-pool` flag in the `gkectl register bootstrap` command.

  5. Configure a storage option, by enter one of the following:

     * **Datastore** field: Enter the name of your [vCenter datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html). The value you specify must be a name, not a path. If you need to enter a path, enter it in the **Folder** field.

       * **Admin workstation configuration file** : Use the value from the `vCenter.datastore` field.

       * The **Datastore** field corresponds to the `--vcenter-datastore` flag in the `gkectl register bootstrap` command.

     * **Storage policy name** field: Enter the name of the [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the cluster nodes. For more information, see [Configure a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

       * **Admin workstation configuration file** : Use the value from the `vCenter.storagePolicyName` field.

       * The **Storage policy name** field corresponds to the `--vcenter-storage-policy` flag in the `gkectl register bootstrap` command.

You must enter a value in either the **Datastore** field or the **Storage Policy Name** field, but not both.

  6. Optionally, in the **Folder** field, enter the name of the [vCenter folder](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-folders) where your cluster VMs will be located.

     * **Admin workstation configuration file** : Use the value from the `vCenter.folder` field.

     * The **Folder** field corresponds to the `--vcenter-folder` flag in the `gkectl register bootstrap` command.

  7. In the **Network** field, enter the name of your [vCenter network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-networking.html).

     * **Admin workstation configuration file** : Use the value from the `vCenter.network` field.

     * The **Network** field corresponds to the `--vcenter-network` flag in the `gkectl register bootstrap` command.

  8. In the **CA certificate path** field, enter the path to the [root CA certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path) for your vCenter Server.

     * If you used `gkeadm` to create your admin workstation, `gkeadm` copied the CA certificate file that you had locally to your admin workstation.

     * The **CA certificate path** field corresponds to the `--vcenter-ca-cert-path` in the `gkectl register bootstrap` command.




### Get the CA certificate

After you create the bootstrap cluster, you will need to provide the vCenter CA certificate in PEM format in the **CA certificate data** field on the **Cluster basics** page. Run the following command to display the certificate:
    
    
    cat CA_CERT_PATH
    

Replace `CA_CERT_PATH` with the path to the root CA certificate for your vCenter Server. If you run this command locally, use the path in `vCenter.caCertPath` in your admin workstation configuration file.

Copy the entire certificate to a text editor so that you will be ready to paste it in the **CA certificate data** field on the **Cluster basics** page after the bootstrap cluster is created.

### Bootstrap environment from admin workstation

When you run the `gkectl register bootstrap` command, it prompts you for the vCenter account username and password. Make sure you have the credentials available. If you used `gkeadm` to create the admin workstation, the username and password are in the file `credential.yaml`.

  1. Scroll to the **Bootstrap environment from admin workstation** section to display the `gkectl register bootstrap` command.

Leave this page open while you go to your admin workstation to create the bootstrap cluster.

  2. Copy and paste the `gkectl register bootstrap` command into a text editor so that you can specify values for the following flags:
         
         ./gkectl register bootstrap \
               ...
               --bundle-path=BUNDLE_PATH \
               ...
               --component-access-service-account-key-path=COMPONENT_ACCESS_SA_PATH \
               --register-service-account-key-path=CONNECT_REGISTER_SA_PATH \
               --stackdriver-service-account-key-path=LOG_MON_SA_PATH \
               --cloud-audit-logging-service-account-key-path=CLOUD_AUDIT_SA_PATH \
               --admin-kubeconfig-out=KUBECONFIG_NAME
         

Replace the following with admin workstation paths:

     * `BUNDLE_PATH`: the path to the bundle file. If you used `gkeadm` to create the admin workstation, the bundle file is located in `/var/lib/gke/bundles/`. The file name depends on the Google Distributed Cloud version, for example, `gke-onprem-vsphere-1.31.0-gke.889-full.tgz`.
     * `COMPONENT_ACCESS_SA_PATH`: the path to key file for the component access service account.
     * `CONNECT_REGISTER_SA_PATH`: the path to the key file for the connect-register service account.
     * `LOG_MON_SA_PATH`: the path to the key file for the logging-monitoring service account.
     * `CLOUD_AUDIT_SA_PATH`: the path to the audit logging service account. If you didn't create an audit logging service account, specify the path to the key file for the logging-monitoring service account.
     * `KUBECONFIG_NAME`: the name for kubeconfig file that the `gkectl register bootstrap` command creates. If you don't specify this flag, the command creates the file with the name `kubeconfig` in the current working directory. If there's an existing file called `kubeconfig`, the command overwrites the file.

Additionally, if you used `gkeadm` to create your admin workstation, `gkectl` was downloaded to the `/usr/bin/` directory. In this case, remove `./` from the beginning of the command since `gkectl` isn't in the current working directory.

  3. Use SSH to connect to your admin workstation.

  4. Copy the command and paste it in a terminal window on your admin workstation.

  5. When prompted, enter (or copy and paste) the vCenter username. The username isn't echoed back to the screen.

  6. When prompted, enter (or copy and paste) the vCenter password. The password isn't echoed back to the screen.




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
    

## Finish configuring the admin cluster

Return to the console and do the following steps:

  1. On the **Install bootstrap environment** page, click **Check Connection**.

On success, the console displays check_circle **Connection established**.

The connection to the bootstrap cluster must be established before you continue. If the connection isn't established, check the arguments that you specified to the `gkectl register bootstrap` command:

     * Make sure that the value for `--target-cluster-name` matches the **Admin cluster name** displayed in the **Bootstrap environment basics** section.

     * Make sure the value for `--project-id` matches the ID of the project that you selected in the console.

If you need to change the bootstrap cluster name, the project ID, or other flag values, do the following:

     1. Enter `Ctrl-C` to exit out of `gkectl register bootstrap`.
     2. Delete the bootstrap cluster:
            
            gkectl delete bootstrap \
              --target-cluster-name=ADMIN_CLUSTER_NAME \
              --project-id=PROJECT_ID \
              --location=REGION \
              --register-service-account-key-path=CONNECT_REGISTER_SA_PATH
            

     3. Re-run the `gkectl register bootstrap` command.

  2. Click **Next: Cluster basics** to begin configuring the admin cluster.




### Cluster basics

  1. In the **CA certificate data** field, copy and paste the entire vCenter CA certificate in PEM format as described previously in the Get the CA certificate section.

  2. In the **Authorization** section, enter the email addresses of users who you want to grant the read-only Kubernetes `clusterrole/view` role. Notice that your email address is automatically added. The role-based access control (RBAC) policies that are applied let users run read-only commands through the [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

  3. Click **Next Control Plane**.




### Control plane

  1. Review the default settings in **Control plane** section and change them as needed.

  2. In the **Control plane node IPs** section, enter the IP addresses in the following fields:

     * **Gateway** : The IP address of the default gateway for the subnet that has your cluster nodes.

     * **Netmask** : The netmask for the subnet that has your cluster nodes.

     * **IP addresses** : Enter the IP address and optionally, the hostname for the three control-plane nodes.

  3. Click **Next: Networking**.




### Networking

In this section you specify the networking information needed to create the admin cluster.

  1. In the **Service and Pod CIDRs** section, either accept the default values for the Kubernetes Service and Pod IP address ranges, or enter different CIDR address ranges.

     * **Service CIDR** : Smallest possible range: `/24`. Largest possible range: `/12`.

     * **Pod CIDR** : Smallest possible range: `/18`. Largest possible range: /8`.

  2. In the **Host config** section, specify the NTP servers, DNS servers, and optionally the DNS search domains used by the VMs that are your cluster nodes. After the cluster is created, you cannot modify these values.

  3. Click **Next: Load balancer**.




### Load balancer

In this section, you select the type of load balancer to use. For additional information, see [Overview of load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance).

  1. In the **Load balancer type** list, select a load balancer:

     * **Bundled with MetalLB** : The MetalLB load balancer is bundled with and requires less configuration than manual load balancing. The MetalLB components run on your cluster nodes, so you don't have to create separate VMs for your load balancer.

     * **Manual** : You can use any load balancer of your choice as long as you set it up _before_ creating the cluster. With any load balancer that you set up manually, you must configure mappings between virtual IPs (VIPs), node addresses, and nodePort values.

  2. In the **Control plane VIP** field, enter the VIP to be used for traffic sent to the Kubernetes API server.

  3. Click **Verify and Create**.

The console displays status messages as it verifies the settings and creates the cluster in your data center.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.




Details about the cluster creation process are output on your admin workstation. If the preflight checks pass, you see something like the following:
    
    
    [2023-03-22 23:12:47+0000] Waiting for cluster kubeconfig to become ready OK
    [2023-03-22 23:15:47+0000] Writing kubeconfig file
    [2023-03-22 23:15:47+0000] kubeconfig of cluster being created is present at gkectl-workspace/abm-cluster-1/abm-cluster-1-kubeconfig
    [2023-03-22 23:15:47+0000] Please restrict access to this file as it contains authentication credentials of your cluster.
    [2023-03-22 23:15:47+0000] Waiting for cluster to become ready OK
    [2023-03-22 23:20:17+0000] Please run
    [2023-03-22 23:20:17+0000] kubectl --kubeconfig gkectl-workspace/abm-cluster-1/abm-cluster-1-kubeconfig get nodes
    [2023-03-22 23:20:17+0000] to get cluster nodes status.
    [2023-03-22 23:20:17+0000] Waiting for node pools to become ready OK
    [2023-03-22 23:20:37+0000] Waiting for metrics to become ready in GCP OK
    [2023-03-22 23:25:38+0000] Waiting for cluster API provider to install in the created admin cluster OK
    [2023-03-22 23:25:48+0000] Moving admin cluster resources to the created admin cluster
    [2023-03-22 23:25:51+0000] Waiting for node update jobs to finish OK
    [2023-03-22 23:27:41+0000] Flushing logs... OK
    [2023-03-22 23:27:41+0000] Deleting membership... OK
    [2023-03-22 23:27:42+0000] Deleting bootstrap cluster.
    

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
