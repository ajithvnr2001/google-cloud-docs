---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows/
title: Creating a cluster using Windows Server node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:24.346901+00:00
---

# Creating a cluster using Windows Server node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Creating a cluster using Windows Server node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In this page, you learn how to create a Google Kubernetes Engine (GKE) cluster with [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) running Microsoft Windows Server. With this cluster, you can use Windows Server containers. Microsoft Hyper-V containers are not currently supported. Similar to Linux containers, Windows Server containers provide process and namespace isolation.

A Windows Server node requires more resources than a typical Linux node. Windows Server nodes need the extra resources to run the Windows OS and for the Windows Server components that cannot run in containers. Since Windows Server nodes require more resources, your [allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#node_allocatable) are lower than they would be with Linux nodes.

## Creating a cluster using Windows Server node pools

In this section, you create a cluster that uses a Windows Server container.

To create this cluster you need to complete the following tasks:

  1. Choose your Windows Server node image.
  2. Update and configure `gcloud`.
  3. Create a cluster and node pools.
  4. Get `kubectl` credentials.
  5. Wait for cluster initialization.

**Note:** The `gcloud` commands for these tasks assume you are using a Linux machine.

## Set up IAM service accounts for GKE

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

  1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the **Project number** field, click content_copy **Copy to clipboard**.
  3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click person_add **Grant access**.
  5. In the **New principals** field, specify the following value: 
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
  6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  7. Click **Save**.



### gcloud

  1. Find your Google Cloud project number: 
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
         
         12345678901
         

  2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




### Choose your Windows Server node image

To run on GKE, Windows Server container node images need to be built on the recommended Windows Server version 2022 (LTSC), or Windows Server version 2019 (LTSC), which is deprecated by GKE and can't be used for node pools running GKE version 1.37 or later. A single cluster can have multiple Windows Server node pools using different Windows Server versions, but each individual node pool can only use one Windows Server version.

Consider the following when choosing your node image:

  * **Updates** : use LTSC2022, because LTSC2019 is deprecated by GKE. Understand the following about LTSC2019: 
    * **No node image updates** : GKE doesn't provide node image updates for LTSC2019 due to stability issues with updates to the underlying image since Microsoft ended **Mainstream Support** for the image. GKE node images are pinned to the December 2025 version of the underlying image. For more information, see [Windows Server 2019](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019).
    * **Compatibility with 1.37** : For GKE version 1.37 and later, you can't use LTSC2019. You can't create new node pools with LTSC2019 and with 1.37 or upgrade existing LTSC2019 node pools to 1.37.
  * **Support timing** : 
    * The support timing for a Windows Server node image is subject to the support timing provided by Microsoft, as described in [Support policy for OS images](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy). You can find the support end date for GKE Windows node images by using the `gcloud container get-server-config` command as described in the Mapping GKE and Windows versions section.
  * **Version compatibility and complexity** : 
    * Both [Windows Server Core](https://hub.docker.com/_/microsoft-windows-servercore) and [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver) can be used as a base image for your containers.
    * Building your Windows Server container images as multi-arch images that can target multiple Windows Server versions can help you manage this versioning complexity.



### Update and configure `gcloud`

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have the correct permission to create clusters. At minimum, you should be a [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container).



### Create a cluster and node pools

To run Windows Server containers, your cluster must have at least one Windows and one Linux node pool. **You cannot create a cluster using only a Windows Server node pool.** The Linux node pool is required to run critical cluster add- ons.

Before you create a cluster using Windows Server node pools, review the Upgrading Windows Server node pools section.

Because of its importance, we recommend turning on autoscaling to ensure your Linux node pool has sufficient capacity to run cluster add-ons.

**Note:** Clusters using Windows Server node pools do not support all Kubernetes and GKE features. See the limitations section for more information.

### gcloud

Create a cluster with the following fields:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-ip-alias \
        --num-nodes=NUMBER_OF_NODES \
        --cluster-version=VERSION_NUMBER \
        --release-channel CHANNEL
    

Replace the following:

  * `CLUSTER_NAME`: the name you choose for your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `--enable-ip-alias` turns on [alias IP](https://docs.cloud.google.com/vpc/docs/alias-ip). Alias IP is required for Windows Server nodes. To read more about its benefits, see [Understanding native container routing with Alias IPs](https://cloud.google.com/blog/products/networking/understanding-native-container-routing-with-alias-ips).
  * `NUMBER_OF_NODES`: the number of Linux nodes you create. You should provide sufficient compute resources to run cluster add-ons. This is an optional field and if omitted, uses the default value of `3`.
  * `VERSION_NUMBER`: the specific cluster version you want to use. If you don't specify a release channel, GKE enrolls your cluster in the most mature release channel where that version is available.
  * `CHANNEL`: the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to enroll the cluster in, which can be one of `rapid`, `regular`, `stable`, or `None` ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)). By default, the cluster is enrolled in the `regular` release channel.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

Create the Windows Server node pool with the following fields:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --image-type=WINDOWS_LTSC_CONTAINERD \
        --machine-type=MACHINE_TYPE_NAME \
        --windows-os-version=WINDOWS_OS_VERSION
    

Replace the following:

  * `NODE_POOL_NAME`: the name you choose for your Windows Server node pool.
  * `CLUSTER_NAME`: the name of the cluster you created above.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `MACHINE_TYPE_NAME`: defines the machine type. `n1-standard-2` is the minimum recommended machine type as Windows Server nodes require additional resources. Machine types `f1-micro` and `g1-small` are not supported. Each machine type is billed differently. For more information, refer to the [machine type price sheet](https://cloud.google.com/compute/pricing#standard_machine_types).
  * `WINDOWS_OS_VERSION`: this is an optional flag that defines the Windows OS version to use for image type `WINDOWS_LTSC_CONTAINERD`. For GKE version 1.37 and later, you can only use LTSC2022 (`ltsc2022`). For 1.36 or earlier, we recommend that you explicitly set the value to `ltsc2022`. Otherwise, GKE uses LTSC2019 (`ltsc2019`), which is not recommended as it's deprecated by GKE.

**Note:** The Windows Server 2022 node image and Windows Server 2019 node image (deprecated by GKE) share the same image type `WINDOWS_LTSC_CONTAINERD`. The default LTSC image that GKE uses to create Windows_LTSC_Containerd node pools through the Google Cloud console or CLI is `ltsc2019`.

The following example shows how you can create a Windows Server 2022 node pool:
    
    
    gcloud container node-pools create node_pool_name \
        --cluster=cluster_name \
        --location=us-central1 \
        --image-type=WINDOWS_LTSC_CONTAINERD \
        --windows-os-version=ltsc2022
    

The following example shows how you can update an existing Windows node pool to use Windows Server 2022 OS image:
    
    
    gcloud container node-pools create node_pool_name \
        --cluster=cluster_name \
        --location=us-central1 \
        --windows-os-version=ltsc2022
    

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the **Cluster basics** section, complete the following: 
     1. Enter the **Name** for your cluster.
     2. For the **Location type** , select a [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
     3. Under **Release channels** , select a **Release channel** and, optionally, a **Target version**.
  3. From the navigation pane, under **Node Pools** , click **default-pool** to create your Linux node pool. When configuring this node pool, you should provide sufficient compute resources to run cluster add-ons. You must also have available [resource quota](https://docs.cloud.google.com/compute/quotas) for the nodes and their resources (such as firewall routes).
  4. At the top of the page, click _add_box_ **Add Node Pool** to create your Windows Server node pool.
  5. In the **Node pool details** section, complete the following: 
     1. Enter a **Name** for the [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
     2. Enter the **Number of nodes** to create in the node pool.
  6. From the navigation pane, under **Node Pools** , click **Nodes**.

     1. From the **Image type** drop-down list, select the following node image:

        * Windows Long Term Servicing Channel with containerd

For more information, see the Choose your Windows node image section.

     2. Choose the default [**Machine configuration**](https://docs.cloud.google.com/compute/docs/machine-types) to use for the instances. `n1-standard-2` is the minimum recommended size as Windows Server nodes require additional resources. Machine types `f1-micro` and `g1-small` are not supported. Each machine type is billed differently. For more information, refer to the [machine type price sheet](https://cloud.google.com/compute/pricing#standard_machine_types).

  7. From the navigation pane, under **Cluster** , select **Networking**.

     1. Under **Advanced networking options** , ensure **Enable VPC-native traffic routing (uses alias IP)** is selected. Alias IP is required for Windows Server nodes. To read more about its benefits, see [Understanding native container routing with Alias IPs](https://cloud.google.com/blog/products/networking/understanding-native-container-routing-with-alias-ips).
  8. Click **Create**.




### Terraform

To create a GKE Standard cluster and a Windows Server node pool using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-regional-cluster"
      location = "us-west1"
    
      initial_node_count = 1
    }
    
    resource "google_container_node_pool" "default" {
      name     = "windows-node-pool"
      cluster  = google_container_cluster.default.name
      location = google_container_cluster.default.location
    
      node_config {
        image_type = "WINDOWS_LTSC_CONTAINERD"
      }
    }

This example uses Windows Server LTSC with containerd. This is the image type for both Windows Server 2022 and Windows Server 2019 OS image (deprecated by GKE). For more information about node images, see Choose your Windows node image.

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

After you create a Windows Server node pool, the cluster goes into a `RECONCILE` state for several minutes as the control plane is updated.

### Get kubectl credentials

Use the `get-credentials` command to enable `kubectl` to work with the cluster you created.
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION
    

For more information on the `get-credentials` command, see the SDK [get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials) documentation.

### Wait for cluster initialization

Before using the cluster, wait for several seconds until `windows.config.common-webhooks.networking.gke.io` is created. This webhook adds scheduling tolerations to Pods created with the `kubernetes.io/os: windows` node selector to ensure they are allowed to run on Windows Server nodes. It also validates the Pod to ensure that it only uses features supported on Windows.

To ensure the webhook is created, run the following command:
    
    
    kubectl get mutatingwebhookconfigurations
    

The output should show the webhook running:
    
    
    NAME                                              CREATED AT
    windows.config.common-webhooks.networking.gke.io  2019-12-12T16:55:47Z
    

Now that you have a cluster with two node pools (one Linux and one Windows), you can [deploy a Windows application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app).

## Mapping GKE and Windows versions

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Microsoft releases new LTSC versions every two to three years. These new versions are typically available in new GKE minor versions. Within a [GKE minor version](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#versioning_scheme) the LTSC versions usually remain fixed.

To see the version mapping between GKE versions and Windows Server versions, use the `gcloud beta container get-server-config` command:
    
    
    gcloud beta container get-server-config
    

The version mapping is returned in the `windowsVersionMaps` field of the response. To filter the response to see the version mapping for specific GKE versions in your cluster, perform the following steps in a Linux shell or in Cloud Shell.

  1. Set the following variables:
         
         CLUSTER_NAME=CLUSTER_NAME \
         NODE_POOL_NAME=NODE_POOL_NAME \
         CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `NODE_POOL_NAME`: the name of the Windows Server node pool.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  2. Obtain the node pool version and store it in the `NODE_POOL_VERSION` variable:
         
         NODE_POOL_VERSION=`gcloud container node-pools describe $NODE_POOL_NAME \
         --cluster=$CLUSTER_NAME \
         --location=$CONTROL_PLANE_LOCATION \
         --format="value(version)"`
         

  3. Obtain the Windows Server versions for `NODE_POOL_VERSION`:
         
         gcloud beta container get-server-config \
             --location=$CONTROL_PLANE_LOCATION \
             --format="yaml(windowsVersionMaps.\"$NODE_POOL_VERSION\")"
         

The output is similar to the following:
         
         windowsVersionMaps:
           1.18.6-gke.6601:
             windowsVersions:
             - imageType: WINDOWS_SAC
               osVersion: 10.0.18363.1198
               supportEndDate:
                 day: 10
                 month: 5
                 year: 2022
             - imageType: WINDOWS_LTSC
               osVersion: 10.0.17763.1577
               supportEndDate:
                 day: 9
                 month: 1
                 year: 2024
         

  4. Obtain the Windows Server version for the `WINDOWS_LTSC` image type:
         
         gcloud beta container get-server-config \
           --flatten=windowsVersionMaps.\"$NODE_POOL_VERSION\".windowsVersions \
           --filter="windowsVersionMaps.\"$NODE_POOL_VERSION\".windowsVersions.imageType=WINDOWS_LTSC" \
           --format="value(windowsVersionMaps.\"$NODE_POOL_VERSION\".windowsVersions.osVersion)"
         

The output is similar to the following:
         
         10.0.17763.1577
         




## Upgrading Windows Server node pools

The [Windows Server container version compatibility requirements](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-20H2%2Cwindows-10-1909) mean that your container images might need to be rebuilt to match the Windows Server version for a new GKE version before upgrading your node pools. Review the following recommendations about upgrading this type of node pool:

  * Prevent node auto-upgrades, if necessary, with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).
  * Ensure that your container images remain compatible with your nodes by checking the version mapping and building your Windows Server container images as multi-arch images that can target multiple Windows Server versions. You can then update your container deployments to target the multi-arch images that will work on both the current and the next GKE version before manually invoking a GKE node pool upgrade.
  * If you're preventing node auto-upgrades, perform [manual node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) regularly because nodes cannot be more than two minor versions behind the control plane version.
  * To proactively receive updates about new GKE versions and the Windows OS versions they use, [subscribe to upgrade notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).
  * Let GKE perform [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) only if you continuously build multi-arch Windows Server container images that target the latest Windows Server versions. Node auto-upgrades are not likely to cause problems with the Windows Server LTSC node image type but there is still a risk of encountering version incompatibility issues.



## Windows Updates

Windows Updates are disabled for Windows Server nodes. Automatic updates can cause node restarts at unpredictable times, and any Windows Updates installed after a node starts would be lost when the node is recreated by GKE. GKE makes Windows Updates available by periodically updating the Windows Server node images used in new GKE releases. There can be a delay between when Windows Updates are released by Microsoft and when they are available in GKE. When critical security updates are released, GKE updates the Windows Server node images as quickly as possible.

## Control how Windows Pods and Services communicate

You can control how Windows Pods and Services communicate using [network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).

You can have a Windows Server container on clusters that have network policy enabled in GKE versions 1.22.2 and later. This feature is available for clusters that use the `WINDOWS_LTSC` or `WINDOWS_LTSC_CONTAINERD` node image types.

If your control planes or nodes are running earlier versions, you can migrate your node pools to a version that supports network policy by upgrading your node pools and your control plane to GKE version 1.22.2 or later. This option is only available if you created your cluster with the `--enable-dataplane-v2` flag.

After you enable network policy, all previously configured policies, including policies that did not work on Windows Server containers before you enabled the feature, become active.

Some clusters cannot be used with Windows Server containers on clusters with network policy enabled. See the limitations section for more details.

## Viewing and querying logs

Logging is enabled automatically in GKE clusters. You can view the logs of the containers and the logs from other services on the Windows Server nodes using [Kubernetes Engine monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine).

The following is an example of a filter to get the container log:
    
    
    resource.type="k8s_container"
    resource.labels.cluster_name="your_cluster_name"
    resource.labels.namespace_name="your_namespace_id"
    resource.labels.container_name="your_container_name"
    resource.labels.Pod_name="your_Pod_name"
    

## Accessing a Windows Server node using Remote Desktop Protocol (RDP)

You can connect to a Windows Server node in your cluster using RDP. For instructions on how to connect, see [Connecting to Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) in the Compute Engine documentation.

## Building multi-arch images

You can build the multi-arch images manually or use a Cloud Build builder. For instructions, see [Building Windows multi-arch images](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images).

## Using gMSA

The following steps show you how to use a Group Managed Service Account (gMSA) with your Windows Server node pools.

  1. Configure Windows Server nodes in your cluster to automatically join your AD domain. For instructions, see [Configure Windows Server nodes to automatically join an Active Directory domain](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/auto-join-windows-nodepools).

  2. Create and grant a gMSA access to the security group automatically created by the domain join service. This step needs to be done in a machine with administrative access to your AD domain.
         
         $instanceGroupUri = gcloud container node-pools describe NODE_POOL_NAME --cluster CLUSTER_NAME --format="value(instanceGroupUrls)"
         $securityGroupName = ([System.Uri]$instanceGroupUri).Segments[-1]
         $securityGroup = dsquery group -name $securityGroupName
         $gmsaName = GMSA_NAME
         $dnsHostName = DNS_HOST_NAME
         
         New-ADServiceAccount -Name $gmsaName -DNSHostName $dnsHostName -PrincipalsAllowedToRetrieveManagedPassword $securityGroup
         
         Get-ADServiceAccount $gmsaName
         Test-ADServiceAccount $gmsaName
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your Windows Server node pool. The automatically created security group has the same name as your Windows Server node pool.
     * `CLUSTER_NAME`: the name of your cluster.
     * `GMSA_NAME`: the name you choose for the new gMSA.
     * `DNS_HOST_NAME`: the Fully Qualified Domain Name (FQDN) of the service account you created. For example, if `GMSA_NAME` is `webapp01` and the domain is `example.com`, then `DNS_HOST_NAME` is `webapp01.example.com`.
  3. Configure your gMSA by following the instructions in the [Configure GMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/) tutorial.




## Deleting Windows Server node pools

Delete a Windows Server node pool by using `gcloud` or the Google Cloud console.

### gcloud
    
    
    gcloud container node-pools delete NODE_POOL_NAME \
        --cluster=CLUSTER_NAME
        --location=CONTROL_PLANE_LOCATION
    

### Console

To delete a Windows Server node pool using the Google Cloud console, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Beside the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. Select the **Nodes** tab.

  4. Under the **Node Pools** section, click _delete_ **Delete** next to the node pool you want to delete.

  5. When prompted to confirm, click **Delete** again.




## Limitations

The following features aren't supported with Windows Server node pools:

  * Compute and node features:

    * [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
    * [Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#cluster-level-enablement)
    * [Machine series above the third generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology)
    * [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
    * [Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
    * [Z4M machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)
    * [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)
    * [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters)
    * Accelerators, including [GPUs](https://docs.cloud.google.com/compute/docs/gpus) and [TPUs](https://docs.cloud.google.com/tpu/docs/tpus)
  * Networking features:

    * [Configuring the maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) greater than the default limit of 110
    * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
    * [Node Local DNS cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
    * [Network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging)
    * [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent). Windows nodes perform IP masquerading for external destinations, but the agent is not supported.
    * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network). IPv6 networking is not supported on Windows nodes.
    * [Private use of Class E IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_reserved_ip_ranges)
    * [Private use of public IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis)
    * Full [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) support. Windows nodes with GKE Dataplane V2 are limited to network policy enforcement, in addition to the limitations described in the referenced document.
  * Security features:

    * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
    * Linux-specific security features (for example, Seccomp, Apparmor, and SELinux)
  * Kubernetes features

    * Host namespaces (for example, hostNetwork, hostPID, and hostIPC). These aren't supported by the Windows operating system.
    * [Kubernetes `service.spec.sessionAffinity`](https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)
    * Features listed in the [Compatibility and limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#supported-functionality-and-limitations) section of the "Windows containers in Kubernetes" document
  * Storage features:

    * The default fstype (ext4), which is used with the balanced persistent disk type. For more information, see [StorageClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses).
    * [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)
    * [Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) with NVMe interfaces for Ephemeral Storage
  * Observability features:

    * Kubernetes Pod labels are missing from workload logs for Windows nodes if the [kubelet read-only port](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port) is disabled because the logging agent cannot retrieve Pod labels.
  * Microsoft features:

    * [Microsoft Hyper-V isolation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container#hyper-v-isolation)
  * Miscellaneous:

    * Docker-based [CloudSQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy)
    * You can't create a cluster with only Windows Server node pools; at least one Linux node pool is required.



For specific limitations with other Google Cloud products that you might want to use with GKE clusters, refer to the respective documentation for that product.

## Troubleshooting

For troubleshooting guidance specific to Windows Server node pools, see [Troubleshoot Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/windows-server-node-pools).

For general guidance, see the Kubernetes documentation on [debugging Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/#debugging-pods) and [Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/#debugging-services).

## What's next

  * Learn how to [deploy a Windows application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app).
  * Read Microsoft's [short introduction](https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/) on Windows containers.
  * Read [Microsoft's guidance](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/net-core-net-framework-containers/net-container-os-targets) on choosing the container base images.
  * Read about Microsoft on Windows [container version compatibility](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
