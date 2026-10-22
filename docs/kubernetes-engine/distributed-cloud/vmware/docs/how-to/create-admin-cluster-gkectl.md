---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-gkectl/
title: Create an admin cluster using `gketl` \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:13.131069+00:00
---

# Create an admin cluster using `gketl`  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-gkectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create an admin cluster using `gketl` Stay organized with collections  Save and categorize content based on your preferences. 

Create an admin cluster for Google Distributed Cloud software only for VMware using `gkectl`. Use `gkectl` if you need to manage your entire admin cluster lifecycle locally within your on-premises environment to meet strict security, compliance, or air-gapped requirements. You can also create an admin cluster using [Terraform](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-terraform) or [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-console).

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

These are the primary steps involved in creating an admin cluster:

  1. Fill in your configuration files. Specify the details for your new admin credentials configuration file, and possibly an IP block file.

  2. Import OS images to vSphere, and push container images to the private registry if applicable. Run `gkectl prepare`.

  3. Create an admin cluster. Use `gkectl` to create a new admin cluster as specified in your completed configuration files. When Google Distributed Cloud creates an admin cluster, it deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster to temporarily host the Kubernetes controllers needed to create the admin cluster. This transient cluster is called a _bootstrap cluster_. User clusters are created and upgraded by their managing admin without the use of a bootstrap cluster.

  4. Verify that your admin cluster is running. Use `kubectl` to view your cluster nodes.




At the end of this procedure, you will have a running admin cluster that you can use to create and manage user clusters.

If you use VPC Service Controls, you might see errors when you run some `gkectl` commands, such as `"Validation Category: GCP - [UNKNOWN] GCP service: [Stackdriver] could not get GCP services"`. To avoid these errors, add the `--skip-validation-gcp` parameter to your commands.

### Fill in your configuration file

  * Make sure that your admin workstation has the required version of `gkectl`. Typically, you use the same version of `gkectl` as the version that will be used when you create the cluster. You specify the cluster version in the `gkeOnPremVersion` field in the cluster configuration file. The following version rules are enforced during cluster creation:

    * The `gkectl` minor version can't be lower than the minor version for the cluster. For example, creating a 1.30 cluster using `gkectl` version 1.29 isn't allowed. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to create a cluster with a higher patch version, such as 1.29.1000-gke.94.

    * The `gkectl` minor version can't be more than two minor versions higher than the cluster version. For example, if you are creating a 1.28 cluster, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.

If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.




If you used `gkeadm` to create your admin workstation, it generated a configuration file named `admin-cluster.yaml`.

If you didn't use `gkeadm` to create your admin workstation, then generate `admin-cluster.yaml` by running this command on your admin workstation:
    
    
    gkectl create-config admin
    

This configuration file is for creating your admin cluster.

Familiarize yourself with the configuration file by scanning the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

#### `name`

If you want to specify a name for your admin cluster, fill in the [`name`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#name-field) field.

#### `bundlePath`

The bundle is a zipped file that contains cluster components. It is included with the admin workstation. This field is already filled in for you.

#### `vCenter`

The fields in this section are already filled in with values that you entered when you created your admin workstation.

#### `enableAdvancedCluster`

In version 1.31, if you want to enable the advanced cluster feature, set [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

Note the following differences between versions:

  * In version 1.31, the advanced cluster feature is in preview:

    * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.

    * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.

  * In version 1.32, the advanced cluster feature is GA.

    * By default, admin clusters are created as advanced clusters. You have to explicitly set `enableAdvancedCluster` to `false` if you want to create a non-advanced cluster.

    * For clusters that have the advanced clusters feature enabled, cluster upgrades are supported.

  * In version 1.33 and higher, all clusters are created as advanced clusters. If you set `enableAdvancedCluster` to `false`, cluster creation fails.




#### `network`

Fill in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section) section and the `network.hostConfig` section. Also set [`adminMaster.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-replicas-field) to `3`.

The [network.podCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-podcidr-field%7D) and [network.serviceCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-servicecidr-field) fields have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.

Fill in the rest of the fields in the [network section of the configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-section) as needed.

#### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your admin cluster. Provide your VIP as the value for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field)

For more information, see [VIPs in the admin cluster subnet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses#example_ip_addresses_vips_in_the_admin_cluster_subnet).

Decide what type of load balancing you want to use. The options are:

  * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancerkind) to `"MetalLB"`.

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and remove the [`manualLB`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-manuallb-section) section.




For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance).

#### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) to `true` or `false` according to your preference.

Use this field to specify whether you want Google Distributed Cloud to create VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster nodes, causing them to be spread across at least three physical hosts in your data center.

#### `adminMaster`

If you want to specify CPU and memory for the control-plane nodes of the admin cluster, fill in the `cpus` and `memoryMB` fields in the [`adminMaster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-section) section.

Admin clusters must have three control plane nodes. Set the `replicas` field in the `adminMaster` section to `3`.

#### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-section) section.

#### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * Artifact Registry

  * Your own private Docker registry.

If you want to use your own private registry, fill in the [`privateRegistry`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section) section.




For more information about using a private registry, including differences between normal clusters and advanced clusters, see [Configure a private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).

#### `componentAccessServiceAccountKeyPath`

Google Distributed Cloud uses your component access service account to download cluster components from Artifact Registry. This field holds the path of a JSON key file for your component access service account.

This field is already filled in for you.

#### `gkeConnect`

[Register your admin cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet by filling in the [`gkeConnect`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) section. If you include the `stackdriver` and `cloudAuditLogging` sections in the configuration file, the ID in `gkeConnect.projectID` must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails.

In 1.28 and later, you can optionally specify a region where the Fleet and Connect services run in `gkeConnect.location`. If you don't include this field, the cluster uses the global instances of these services.

If you include `gkeConnect.location`, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.

#### `gkeOnPremAPI`

If the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) automatically in the region configured in `stackdriver.clusterLocation`. The `gkeOnPremAPI.location` region must be the same as the region specified in `cloudAuditLogging.clusterLocation`, `gkeConnect.location`, and `stackdriver.clusterLocation`. If the regions aren't the same, cluster creation fails.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




#### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#stackdriver-section) section.

This section is required by default. That is, if you don't fill in this section, then you must include the `--skip-validation-stackdriver` flag when you run `gkectl create admin`.

Note the following requirements:

  * If you [enable advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field), you must specify the same path in `cloudAuditLogging.serviceAccountKeyPath` and `stackdriver.serviceAccountKeyPath`.

  * The ID in `stackdriver.projectID` must be the same as the ID in `gkeConnect.projectID` and `cloudAuditLogging.projectID`.

  * The Google Cloud region set in `stackdriver.clusterLocation` must be the same as the region set in `cloudAuditLogging.clusterLocation` and `gkeConnect.location`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

#### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#cloudauditlogging-section) section.

Note the following requirements:

  * If you enable advanced cluster, you must specify the same path in `cloudAuditLogging.serviceAccountKeyPath` and `stackdriver.serviceAccountKeyPath`.

  * The ID in `cloudAuditLogging.projectID` must be the same as the ID in `gkeConnect.projectID` and `stackdriver.projectID`.

  * The Google Cloud region set in `cloudAuditLogging.clusterLocation` must be the same as the region set in `stackdriver.clusterLocation` and `gkeConnect.location` (if the field is included in your configuration file). Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

#### `clusterBackup`

If you want to enable [backing up of the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl), set [`clusterBackup.datastore`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#clusterbackup-datastore-field) to the [vSphere datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) where you want to save cluster backups.

If you enable advanced cluster, remove this section. Backing up the admin cluster to a vSphere datastore isn't supported.

#### `autoRepair`

If you want to [enable automatic node repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) for your admin cluster, set [`autoRepair.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field) to `true`.

#### `secretsEncryption`

If you want to enable [always-on Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption), fill in the [`secretsEncryption`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#secretsencryption-section) section.

If you enable advanced cluster, set `secretsEncryption.enabled` to `false`. Always-on Secrets encryption isn't supported.

#### `osImageType`

Decide what type of OS image you want to use for the admin cluster nodes, and fill in the [`osImageType`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#osimagetype) section accordingly.

If you enable advanced cluster, set `osImageType` to either `ubuntu_cgroupv2` or `ubuntu_containerd`.

### Example of filled-in configuration files

Here is an example of a filled-in admin cluster configuration file. The configuration enables some, but not all, of the available features.

#### vc-01-admin-cluster.yaml
    
    
    apiVersion: v1
    kind: AdminCluster
    name: "gke-admin-01"
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.28.0-gke.1-full.tgz"
    enableAdvancedCluster: true
    vCenter:
      address: "vc01.example"
      datacenter: "vc-01"
      cluster: "vc01-workloads-1"
      resourcePool: "vc-01-pool-1"
      datastore: "vc01-datastore-1"
      caCertPath: "/usr/local/google/home/me/certs/vc01-cert.pem"
      credentials:
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
      folder: "vc01-folder-1"
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: static
        ipBlockFilePath: network.hostconfig
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
      vCenter:
        networkName: "vc01-net-1"
      controlPlaneIPBlock:
        netmask: "255.255.248.0"
        gateway: "21.0.143.254"
        ips:
        - ip: "21.0.140.226"
          hostname: "admin-cp-vm-1"
        - ip: "21.0.141.48"
          hostname: "admin-cp-vm-2"
        - ip: "21.0.141.65"
          hostname: "admin-cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.59"
      kind: "MetalLB"
    antiAffinityGroups:
      enabled: true
    adminMaster:
      cpus: 4
      memoryMB: 16384
      replicas: 3
    componentAccessServiceAccountKeyPath: "sa-key.json"
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    cloudAuditLogging:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
    autoRepair:
      enabled: true
    osImageType: "ubuntu_cgv2"
    

#### Validate your configuration file

After you've filled in your admin cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --config ADMIN_CLUSTER_CONFIG
    

Replace ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-yyy` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/preflight-checks).

### Get OS images

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config ADMIN_CLUSTER_CONFIG
    

The `gkectl prepare` command performs the following preparatory tasks:

  * Imports OS images to vSphere and marks them as VM templates.

  * If you are using a private Docker registry, pushes the container images to your registry.

  * Optionally, validates the container images' build attestations, thereby verifying the images were built and signed by Google and are ready for deployment.




If you configured your [`bundlePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) to use a full bundle, `gkectl prepare` uses the OS and container images included in the bundle, bypassing the need to download them from external networks. This is recommended for environments behind a slow proxy or with limited internet access. For more information, see [About Google Distributed Cloud bundles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles).

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal name server in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

### Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

If you use VPC Service Controls, you might see errors when you run some `gkectl` commands, such as `"Validation Category: GCP - [UNKNOWN] GCP service: [Stackdriver] could not get GCP services"`. To avoid these errors, add the `--skip-validation-gcp` parameter to your commands.

#### Resume creation of the admin cluster after a failure

If the admin cluster creation fails or is canceled, you can run the `create` command again:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

#### Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

The kubeconfig file contains the name of your admin cluster. To view the cluster name, you can run:
    
    
    kubectl config get-clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

The output shows the name of the cluster. For example:
    
    
    NAME
    gke-admin-tqk8x
    

If you like, you can change the name and location of your kubeconfig file.

#### Manage the `checkpoint.yaml` file

This section applies only to non-HA admin clusters. The `checkpoint.yaml` file isn't used the creation of HA admin clusters.

When you ran the `gkectl create admin` command to create the admin cluster, it created a checkpoint file in the same datastore folder as the admin cluster data disk. By default, this file has the name DATA_DISK_NAME`‑checkpoint.yaml`. If the length of DATA_DISK_NAME is greater than or equal to 245 characters, then, due to the vSphere limit on filename length, the name is DATA_DISK_NAME`.yaml`.

This file contains the admin cluster state and credentials, and is used for future upgrades. Don't delete this file unless you are following the process for [deleting an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster).

If you have enabled VM encryption in your instance of vCenter Server, then you must have the [Cryptographic operations.Direct Access](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) privilege before you create or upgrade your admin cluster. Otherwise the checkpoint will not be uploaded. If you cannot obtain this privilege, then you can disable uploading the checkpoint file by using the hidden flag `--disable-checkpoint` when you run a relevant command.

The `checkpoint.yaml` file is automatically updated when you run the `gkectl upgrade admin` command, or when you run a `gkectl update` command that affects the admin cluster.

### Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.

The output shows the admin cluster nodes. For example:
    
    
    admin-cp-vm-1   Ready    control-plane,master   ...
    admin-cp-vm-2   Ready    control-plane,master   ...
    admin-cp-vm-3   Ready    control-plane,master   ...
    

### Back up files

We recommend that you back up your admin cluster kubeconfig file. That is, copy the kubeconfig file from your admin workstation to another location. Then if you lose access to the admin workstation, or if the kubeconfig file on your admin workstation gets accidentally deleted, you still have access to the admin cluster.

We also recommend that you back up the private SSH key for your admin cluster. Then if you lose access to the admin cluster, you can still use SSH to connect to the admin cluster nodes. This will allow you to troubleshoot and investigate any issues with connectivity to the admin cluster.

Extract the SSH key from the admin cluster to a file named `admin-cluster-ssh-key`:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secrets -n kube-system sshkeys \
        -o jsonpath='{.data.vsphere_tmp}' | base64 -d > admin-cluster-ssh-key
    

Now you can back up `admin-cluster-ssh-key` to another location of your choice.

### RBAC policies

When you fill in the [`gkeConnect` section](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) in your admin cluster configuration file, the cluster is registered to your [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs) during creation or update. To enable fleet management functionality, Google Cloud deploys the [Connect agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) and creates a Google service account that represents the project that the cluster is registered to. The Connect agent establishes a connection with the service account to handle requests to the cluster's Kubernetes API server. This enables access to cluster and workload management features in Google Cloud, including access to the [Google Cloud console](https://docs.cloud.google.com/cloud-console), which lets you interact with your cluster.

The admin cluster's Kubernetes API server needs to be able to authorize requests from the Connect agent. To ensure this, the following [role-based access control (RBAC) policies](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) are configured on the service account:

  * An [**impersonation policy**](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) that authorizes the Connect agent to send requests to the Kubernetes API server on behalf of the service account.

  * A **permissions policy** that specifies the operations that are allowed on other Kubernetes resources.




The service account and RBAC policies are needed so that you can manage the lifecycle of your user clusters in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
