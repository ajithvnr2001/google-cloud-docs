---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-topology-domains/
title: Create an admin cluster for use in topology domains \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:31.549916+00:00
---

# Create an admin cluster for use in topology domains  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-topology-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create an admin cluster for use in topology domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows how to create an admin cluster for use in Google Distributed Cloud [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). The admin cluster manages user clusters that run your workloads. Google Distributed Cloud version 1.31 or higher is required to use topology domains.

Setting up a topology domain requires that you enable [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field). Note the following limitations with the advanced cluster preview:

  * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.
  * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.



This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more details about the admin cluster, see the [installation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview).

## Procedure overview

These are the primary steps involved in creating an admin cluster:

  1. Fill in your admin configuration file
    Specify the details for your new admin cluster by completing an admin cluster configuration file.
  2. Fill in your vSphere infrastructure configuration file
    Specify the details about your topology domains in a vSphere infrastructure configuration file.
  3. Fill in your IP block file
    Specify the IP addresses for the gateway, netmask, and control-plane nodes in an IP block file.
  4. Get OS images 
    Download the normal Google Distributed Cloud bundle. Then run `gkectl prepare`, which imports the OS images to vSphere, and pushes container images to the private registry if applicable.
  5. Create an admin cluster.
    Use `gkectl` to create a new admin cluster as specified in your completed configuration files. When Google Distributed Cloud creates an admin cluster, it deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster to temporarily host the Kubernetes controllers needed to create the admin cluster. This transient cluster is called a _bootstrap cluster_. User clusters are created and upgraded by their managing admin without the use of a bootstrap cluster.
  6. Verify that your admin cluster is running.
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running admin cluster that you can use to create and manage user clusters in topology domains.

## Before you begin

  * Make sure you have set up and can sign in to your admin workstation as described in [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation). The admin workstation has the tools you need to create your admin cluster. Do all the steps in this document on your admin workstation.

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available for the three control-plane nodes and a control-plane VIP.

  * Configure your load balancer for [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance). Your load balancer must be set up before you create the admin cluster.

  * Look ahead at the `privateRegistry` section, and decide whether you want to use a public or private registry for Google Distributed Cloud components.

  * Look ahead at the osImageType field, and decide what type of operating system you want to run on your admin cluster nodes.

  * If your organization requires outbound traffic to pass through a proxy server, make sure to [allowlist](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#allowlist_addresses) required APIs and the Artifact Registry address.

  * Gather the information that you need to access each instance of vCenter Server. You need this information to fill in the [`Secret`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#secret-section) section and the [`VSphereInfraConfig.credentials.vCenters`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#credentials-vcenters-section) section in the vSphere infrastructure configuration file. See the following for how to obtain the needed information:

    * [vCenter user account privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges)
    * [Determine your vCenter server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address)
    * [Getting your vCenter CA root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path)



## Fill in your admin cluster configuration file

If you used `gkeadm` to create your admin workstation, it generated a configuration file named `admin-cluster.yaml`.

If you didn't use `gkeadm` to create your admin workstation, then generate `admin-cluster.yaml` by running this command on your admin workstation:
    
    
    gkectl create-config admin
    

This configuration file is for creating your admin cluster.

Familiarize yourself with the configuration file by scanning the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

If you want to specify a name for your admin cluster, fill in the [`name`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#name-field) field.

### `bundlePath`

The bundle is a zipped file that contains cluster components. It is included with the admin workstation. This field is already filled in for you.

### `enableAdvancedCluster`

Set [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`. This enables advanced clusters, which is required to set up topology domains.

### `infraConfigFilePath`

Add the full path to the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file) in the [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) field.

### `vCenter`

Remove this entire section. Instead, you configure the vCenter Server information in the vSphere infrastructure configuration file.

### `network`

  * Remove the following from the configuration file:

    * The entire `network.hostConfig` section. This information is configured in the vSphere infrastructure configuration file per topology domain.
    * The `network.vCenter.networkName` field. This field is configured in the vSphere infrastructure configuration file per topology domain.
    * The entire `network.controlPlaneIPBlock` section. The IP addresses for the gateway, netmask, and the control plane nodes are configured in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file).
  * Set [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) to the path to the IP block file.

  * Set [`network.ipMode.type`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode-type-field) to `static`.

  * The [network.podCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-podcidr-field%7D) and [network.serviceCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-servicecidr-field) fields have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.




### `loadBalancer`

  * Set `loadBalancer.kind` to `"ManualLB"`, and remove the [`manualLB`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-manuallb-section) section.

  * Set aside a VIP for the Kubernetes API server of your admin cluster. Provide your VIP as the value for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field)




For more information, see [VIPs in the admin cluster subnet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses#example_ip_addresses_vips_in_the_admin_cluster_subnet).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) to `false`. Distributed Resource Scheduler (DRS) anti-affinity rules aren't supported with topology domains.

### `adminMaster`

  * If you want to specify CPU and memory for the control-plane nodes of the admin cluster, fill in the `cpus` and `memoryMB` fields in the [`adminMaster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-section) section.

  * Admin clusters must have three control-plane nodes. Set the `replicas` field in the `adminMaster` section to `3`.

  * If you want to specify a specific topology domain for the control plane nodes to use, add the topology domain name to the [`adminMaster.topologyDomains`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-topology-domains-field) field. If you don't specify a name here, you must set a name in [`vSphereInfraConfig.defaultTopologyDomain`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-default-topology-domain) in the vSphere infrastructure configuration file.




### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-section) section.

### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * Artifact Registry

  * Your own private Docker registry.

If you want to use your own private registry, fill in the [`privateRegistry`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section) section.




### `componentAccessServiceAccountKeyPath`

Google Distributed Cloud uses your component access service account to download cluster components from Artifact Registry. This field holds the path of a JSON key file for your component access service account.

This field is already filled in for you.

### `gkeConnect`

[Register your admin cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet by filling in the [`gkeConnect`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) section. The ID in `gkeConnect.projectID` must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails.

You can optionally specify a region where the fleet and Connect services run in `gkeConnect.location`. If you don't include this field, the cluster uses the global instances of these services.

If you include `gkeConnect.location`, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.

### `gkeOnPremAPI`

This section describes how clusters are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).

The `gkectl` command line tool is the only available [cluster lifecycle management tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools) for clusters using topology domains. Although the Google Cloud console, the Google Cloud CLI, and Terraform aren't supported for clusters using topology domains, you can optionally enroll the cluster in the GKE On-Prem API when it is created.

If the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are enrolled in the GKE On-Prem API automatically in the region configured in `stackdriver.clusterLocation`. The `gkeOnPremAPI.location` region must be the same as the region specified in `cloudAuditLogging.clusterLocation`, `gkeConnect.location`, and `stackdriver.clusterLocation`. If the regions aren't the same, cluster creation fails.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




### `stackdriver`

Fill in the [`stackdriver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#stackdriver-section) section to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) for your cluster.

Note the following requirements:

  * The ID in `stackdriver.projectID` must be the same as the ID in `gkeConnect.projectID` and `cloudAuditLogging.projectID`.

  * The Google Cloud region set in `stackdriver.clusterLocation` must be the same as the region set in `cloudAuditLogging.clusterLocation` and `gkeConnect.location`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#cloudauditlogging-section) section.

Note the following requirements for new clusters:

  * Because `enableAdvancedCluster` is set to `true`, you must specify the same path in `cloudAuditLogging.serviceAccountKeyPath` and `stackdriver.serviceAccountKeyPath`.

  * The ID in `cloudAuditLogging.projectID` must be the same as the ID in `gkeConnect.projectID` and `stackdriver.projectID`.

  * The Google Cloud region set in `cloudAuditLogging.clusterLocation` must be the same as the region set in `stackdriver.clusterLocation` and `gkeConnect.location` (if the field is included in your configuration file). Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### `clusterBackup`

Remove this section. [Backing up the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl), to a vSphere datastore isn't supported.

### `autoRepair`

If you want to [enable automatic node repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) for your admin cluster, set [`autoRepair.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field) to `true`.

### `secretsEncryption`

Because `enableAdvancedCluster` is set to `true`, remove this section.

### `osImageType`

Set the [`osImageType`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#osimagetype). to `ubuntu_cgv2`.

### `preparedSecrets`

Remove the `preparedSecrets` field. [Prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) aren't supported when topology domains is enabled.

### Example of filled-in configuration files

Here is an example of a filled-in admin cluster configuration file. The configuration enables some, but not all, of the available features.

#### vc-01-admin-cluster.yaml
    
    
    apiVersion: v1
    kind: AdminCluster
    name: "gke-admin-01"
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.31.0-gke.1-full.tgz"
    enableAdvancedCluster: true
    infraConfigFilePath: "/my-config-folder/vsphere-infrastructure-config.yaml"
    network:
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
      ipMode:
        type: "static"
        ipBlockFilePath: "/my-config-folder/admin-cluster-ipblock.yaml"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.59"
      kind: "ManualLB"
    antiAffinityGroups:
      enabled: false
    adminMaster:
      cpus: 4
      memoryMB: 16384
      replicas: 3
      topologyDomains: "admin-cluster-domain"
    componentAccessServiceAccountKeyPath: "sa-key.json"
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    autoRepair:
      enabled: true
    osImageType: "ubuntu_cgv2"
    

## Fill in your vSphere infrastructure configuration file

Copy the template for the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file) to the file in the directory that you specified in the `infraConfigFilePath` field in the admin cluster configuration file. There is only one vSphere infrastructure configuration file for the admin cluster and all managed user clusters.

### `Secret`

Fill in the [`Secret`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#secret-section) section in the vSphere infrastructure configuration file. This section describes the vSphere credentials Secret which stores credentials of each vCenter Server.

### `VSphereInfraConfig.name`

Fill in the [`VSphereInfraConfig,name`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#vsphere-infra-config-name) field.

### `VSphereInfraConfig.credentials.vCenters`

For each `Secret`, add a corresponding [`VSphereInfraConfig.credentials.vCenters`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#credentials-vcenters-section) section.

### `VSphereInfraConfig,topologyDomains`

Fill in the [`VSphereInfraConfig.topologyDomains`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-section) section to define the topology domains.

## Fill in your IP block file

Copy the template for the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) to the file in the directory that you specified in the `network.ipMode.ipBlockFilePath` field in the admin cluster configuration file. Add the IP addresses for the gateway, netmask, and the three control plane nodes. For each control-plane node IP address, add `isControlPlane: true` as shown in the [example for topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file#example_2).

## Get OS images

  1. Download the normal Google Distributed Cloud bundle to the admin workstation:
         
         gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz /var/lib/gke/bundles/gke-onprem-vsphere-VERSION.tgz
         

Replace `VERSION` with the Google Distributed Cloud [version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history) that you want to install.

This command downloads the normal bundle. Don't download the full bundle because it isn't supported with advanced clusters.

  2. Run `gkectl prepare` to initialize your vSphere environment:
         
         gkectl prepare --config ADMIN_CLUSTER_CONFIG
         

Replace `ADMIN_CLUSTER_CONFIG` with the path of the admin cluster configuration.

The `gkectl prepare` command performs the following preparatory tasks:

     * Imports OS images to vSphere and marks them as VM templates.

     * If you are using a private Docker registry, pushes the container images to your registry.

     * Optionally, validates the container images' build attestations, thereby verifying the images were built and signed by Google and are ready for deployment.

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).



## Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

### Resume creation of the admin cluster after a failure

If the admin cluster creation fails or is canceled, you can run the `create` command again:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

### Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

The kubeconfig file contains the name of your admin cluster. To view the cluster name, you can run:
    
    
    kubectl config get-clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

The output shows the name of the cluster. For example:
    
    
    NAME
    gke-admin-tqk8x
    

If you like, you can change the name and location of your kubeconfig file.

## Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.

The output shows the admin cluster nodes. For example:
    
    
    admin-cp-vm-1   Ready    control-plane,master   ...
    admin-cp-vm-2   Ready    control-plane,master   ...
    admin-cp-vm-3   Ready    control-plane,master   ...
    

## Configure your `PodTemplate`

The topology label is populated to labels of nodes in the topology domain. Unless your topology domain setup used the default constraint, [`"topology.kubernetes.io/zone"`](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone) as the topology key, you need to configure the topology key in the pod template of your Deployment, StatefulSet, or ReplicaSet, as applicable.

For example, suppose you defined the key in the topology label as `"topology.examplepetstore.com/zone"`. In the `PodTemplate`, you specify the key as the value for the `topologySpreadConstraints.topologyKey` field. This lets the Kubernetes scheduler distribute Pods across the topology domain to ensure high availability and prevent over-concentration in any single area in case of failure.

For more information on configuring `topologySpreadConstraints`, see [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) in the Kubernetes documentation.

## Back up files

We recommend that you back up your admin cluster kubeconfig file. That is, copy the kubeconfig file from your admin workstation to another location. Then if you lose access to the admin workstation, or if the kubeconfig file on your admin workstation gets accidentally deleted, you still have access to the admin cluster.

We also recommend that you back up the private SSH key for your admin cluster. Then if you lose access to the admin cluster, you can still use SSH to connect to the admin cluster nodes. This will allow you to troubleshoot and investigate any issues with connectivity to the admin cluster.

Extract the SSH key from the admin cluster to a file named `admin-cluster-ssh-key`:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secrets -n kube-system sshkeys \
        -o jsonpath='{.data.vsphere_tmp}' | base64 -d > admin-cluster-ssh-key
    

Now you can back up `admin-cluster-ssh-key` to another location of your choice.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade).

## What's next

[Create a user cluster for use in topology domain](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
