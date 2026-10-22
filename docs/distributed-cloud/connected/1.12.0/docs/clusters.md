---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/clusters/
title: Create and manage clusters \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:21.666493+00:00
---

# Create and manage clusters  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/clusters/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Create and manage clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud connected cluster resources. For more information about Distributed Cloud connected clusters, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## Prerequisites

Before you can create a Distributed Cloud connected cluster, you must enable the required APIs in the target Google Cloud project. To do so, you must have one of the following roles in the Google Cloud project:

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`)



For more information about these roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic). For information about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

To create a Distributed Cloud connected cluster, enable the following APIs:

  * `anthos.googleapis.com`
  * `anthosaudit.googleapis.com`
  * `anthosgke.googleapis.com`
  * `cloudresourcemanager.googleapis.com`
  * `connectgateway.googleapis.com`
  * `container.googleapis.com`
  * `edgecontainer.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkehub.googleapis.com`
  * `gkeonprem.googleapis.com`
  * `iam.googleapis.com`
  * `kubernetesmetadata.googleapis.com`
  * `logging.googleapis.com`
  * `monitoring.googleapis.com`
  * `opsconfigmonitoring.googleapis.com`
  * `serviceusage.googleapis.com`
  * `stackdriver.googleapis.com`
  * `storage.googleapis.com`
  * `sts.googleapis.com`



For information about enabling APIs, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

When you create a Distributed Cloud connected cluster, the following rules apply:

  * You must create Distributed Cloud connected clusters in their own Google Cloud project. Distributed Cloud connected clusters cannot coexist in the same Google Cloud project with any other type of clusters, including non-Distributed Cloud connected clusters. Mixing Distributed Cloud connected clusters with any other type of clusters in the same Google Cloud project can result in data loss.
  * If you reassign a node between Distributed Cloud connected clusters, that node is wiped clean and reset to the default configuration.
  * By default, the local control plane workloads run in high availability mode with three replicas that span across three nodes chosen automatically by Distributed Cloud. This is true unless there are fewer than three nodes in the cluster, or you specifically configure the cluster to use one node to run the local control plane workloads. You also have the option to specify the three nodes for high availability mode by using the `--control-plane-machine-filter` flag. No other node combinations are supported.
  * The nodes that run the local control plane workloads also run your application workloads.
  * The IP addresses of local control plane endpoints are accessible on your local network. You must ensure that your local network's security configuration prevents external access to those IP addresses.



### Recommended topics

Before creating a cluster, also familiarize yourself with the following topics:

  * [Survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/survivability)
  * [Configure the Pod runtime class](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#runtime-class)



## Create a cluster

To create a Distributed Cloud connected cluster, complete the steps in this section. Creating a cluster is one of multiple steps required to [deploy a workload on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the Kubernetes **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click **Create**.

  3. On the **Create a cluster** page, click the **On-premises** tab.

  4. Next to the **Distributed Cloud Edge** option, click **Configure**.

  5. On the **Cluster basics** page, provide the following information:

     * **Name** : a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
     * **Location** : the Google Cloud region in which you want to create this cluster.
     * **Default max pods per node** : the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
     * **Labels** : lets you add one or more labels to this cluster by clicking add**Add label**.
  6. In the left navigation, click **Control plane**.

  7. On the **Control plane** page, provide the following information:

     * Select **Local** for control plane location.
     * Select the target Distributed Cloud connected project.
     * Select the target Distributed Cloud connected zone.
     * Optionally, specify filtering criteria to select specific Distributed Cloud machines to add to the cluster.
     * Specify whether you want this to be a high availability cluster.
     * Specify whether you want to allow shared deployment of workloads. This allows your workloads to run on the nodes running the cluster's control plane.
  8. In the left navigation, click **Networking**.

  9. On the **Networking** page, provide the following information:

     * **Cluster default pod address range** : the desired IPv4 CIDR block for Kubernetes Pods that run on this cluster.
     * **Service address range** : the desired IPv4 CIDR block for Kubernetes Services that run on this cluster.

For more information, see [Distributed Cloud Pod and Service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation).

  10. In the left navigation, click **Authorization**.

  11. On the **Authorization** page, provide the name of the user account within the target Google Cloud project that is authorized to modify cluster resources.

  12. Assign a node pool to the cluster by doing one of the following:

     * To assign an existing node pool to this cluster, in the **Node pools** section in the left navigation, select the existing node pool and verify that the node pool configuration on the **Node pool details** page is correct.
     * To create a new node pool to assign to this cluster, click add_box**Add node pool** and provide the following information on the **Node pool details** page: 
       * **Node pool name** : a unique name that identifies this node pool.
       * **Node pool labels** : click add**Add label** to add one or more labels to this node pool.
       * **Worker nodes preference** : select the Distributed Cloud connected nodes to assign to this node pool.
  13. To create the Distributed Cloud connected cluster, click **Create**.




###  gcloud 

Use the `gcloud edge-cloud container clusters create` command:
    
    
    gcloud edge-cloud container clusters create CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --fleet-project=FLEET_PROJECT_ID \
        --cluster-ipv4-cidr=CLUSTER_IPV4_CIDR_BLOCK \
        --services-ipv4-cidr=SERVICE_IPV4_CIDR_BLOCK \
        --default-max-pods-per-node=MAX_PODS_PER_NODE \
        --release-channel RELEASE_CHANNEL \
        --control-plane-node-storage-schema CONTROL_PLANE_STORAGE_SCHEMA \
        --control-plane-kms-key=CONTROL_PLANE_KMS_KEY \
        --control-plane-node-location=CONTROL_PLANE_LOCATION \
        --control-plane-node-count=CONTROL_PLANE_NODE_COUNT \
        --control-plane-machine-filter=CONTROL_PLANE_NODE_FILTER \
        --control-plane-shared-deployment-policy=CONTROL_PLANE_NODE_SHARING \
        --external-lb-address-pools=IPV4_DATA_PLANE_ADDRESSES \
        --version SOFTWARE_VERSION \
        --offline-reboot-ttl REBOOT_TIMEOUT \
        --default-container-runtime RUNTIME_CLASS \
        --enable-google-group-authentication GROUP_AUTHENTICATION
     

Replace the following:

  * `CLUSTER_ID`: a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the cluster is created.
  * `FLEET_PROJECT_ID`: the ID of the Fleet host project in which the cluster is registered. If this flag is omitted, the Distributed Cloud connected cluster project is used as the Fleet host project.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `MAX_PODS_PER_NODE` (optional): the maximum number of Kubernetes Pods that can run on each node in this cluster. If omitted, defaults to `110`. This number can be limited by the size of the Pod's CIDR block.
  * `RELEASE_CHANNEL`: (optional): specifies the release channel for the version of the Distributed Cloud software you want this cluster to run. Valid values are `REGULAR` (enable automatic cluster upgrades) and `NONE` (disable automatic cluster upgrades). If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_STORAGE_SCHEMA` (optional): specifies the local storage schema for the control plane nodes on this cluster. For more information, see [Configure local storage schemas](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/storage#schemas).
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This flag only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/security#cmek).

  * `CONTROL_PLANE_LOCATION`: instructs Distributed Cloud to deploy the control plane workloads for this cluster locally. The value is the name of the target Distributed Cloud connected zone.

  * `CONTROL_PLANE_NODE_COUNT` (optional): specifies the number of nodes on which to run the local control plane workloads. Valid values are `3` for high availability and `1` for standard operation. If omitted, defaults to `3`.

  * `CONTROL_PLANE_NODE_FILTER` (optional): specifies a regex-formatted list of nodes that run the local control plane workloads. If omitted, Distributed Cloud selects the nodes automatically at random.

  * `CONTROL_PLANE_NODE_SHARING`: (optional) specifies whether application workloads can run on the nodes that run the local control plane workloads. Valid values are `DISALLOWED` an `ALLOWED`. If omitted, defaults to `DISALLOWED`.

  * `IPV4_DATA_PLANE_ADDRESSES`: specifies the IPv4 addresses, address ranges, or subnetworks for ingress traffic for Services that run behind the Distributed Cloud load balancer when the cluster is running in survivability mode. Accepts either a comma-delimited list, or a configuration file in YAML or JSON format. For more information, see [Load balancing](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/networking#load-balancing).

  * `SOFTWARE_VERSION`: specifies the Distributed Cloud connected software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.1`. If omitted, defaults to the server-default software version, which typically is the latest available version of Distributed Cloud connected. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster. You must set the `RELEASE_CHANNEL` flag to `NONE` to specify a cluster software version.

  * `REBOOT_TIMEOUT`: specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established. The minimum timeout value is `1800` or 30 minutes. You can also use the ISO 8601 format for this value (for example, `1dT1h2m3s`).

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time. This risk increases with the length of the timeout window.

  * `RUNTIME_CLASS`: specifies the default runtime class for workloads in this cluster. Valid values are `runc` and `gvisor`. If omitted, defaults to `runc`. Can be overridden by specifying the runtime class in the Pod configuration as described in [Configure the Pod runtime class](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#runtime-class). This is a preview-level feature.

Specifying the `gvisor` runtime class switches the Pod to the Open Container Initiative (OCI) secure runtime based on [gVisor](https://gvisor.dev/). gVisor is a sandboxing solution that introduces strong isolation between the workload and its host. This a preview-level runtime class.

  * `GROUP_AUTHENTICATION`: specifies whether you can access the cluster by authenticating with a Google group rather than an individual account. Valid values are `true` and `false`. If omitted, defaults to `false`.




###  API 

Make a `POST` request to the `projects.locations.clusters` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_ID&requestId=REQUEST_ID&fleetId=FLEET_PROJECT_ID
    
    {
      "labels": { LABELS,
      },
      "authorization": {
        "adminUsers": {
          "username": "USERNAME"
        }
      },
      "fleet": {
        "project": "FLEET_PROJECT_ID"
      },
      "networking": {
        "clusterIpv4CidrBlocks": CLUSTER_IPV4_CIDR_BLOCK,
        "servicesIpv4CidrBlocks": SERVICE_IPV4_CIDR_BLOCK,
          },
      "defaultMaxPodsPerNode": MAX_PODS_PER_NODE,
      "releaseChannel": "RELEASE_CHANNEL",
      "controlPlaneEncryption": {
       "kmsKey": CONTROL_PLANE_KMS_KEY,
      },
      "controlPlane": {
        "local": {
          "nodeLocation": "CONTROL_PLANE_LOCATION",
          "nodeCount": CONTROL_PLANE_NODE_COUNT,
          "machineFilter": "CONTROL_PLANE_NODE_FILTER",
          "sharedDeploymentPolicy": "CONTROL_PLANE_NODE_SHARING"
        }
      },
      "externalLoadBalancerIpAddressPools": [
        "IPV4_DATA_PLANE_ADDRESSES"
      ],
      "targetVersion": "SOFTWARE_VERSION",
      "offlineRebootTtl": "REBOOT_TIMEOUT",
      "defaultContainerRuntime": "RUNTIME_CLASS",
      "enableGoogleGroupAuthentication": "GROUP_AUTHENTICATION",
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `FLEET_PROJECT_ID`: the ID of the Fleet host project in which the cluster is registered. This can be either a separate project or the Distributed Cloud connected project to which this cluster belongs (`PROJECT_ID`). Fleet registration is mandatory.
  * `LABELS`: a list of labels to apply to this cluster resource.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `MAX_PODS_PER_NODE`: the maximum number of Kubernetes Pods that can run on each node in this cluster. If omitted, defaults to `110`. This number can also be limited by the size of the Pod's CIDR block.
  * `RELEASE_CHANNEL`: (optional): specifies the release channel for the version of the Distributed Cloud connected software you want this cluster to run. Valid values are `REGULAR` (enable automatic cluster upgrades) and `NONE` (disable automatic cluster upgrades). If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/security#cmek).

  * `CONTROL_PLANE_LOCATION`: instructs Distributed Cloud to deploy the control plane workloads for this cluster locally. The value is the name of the target Distributed Cloud zone.

  * `CONTROL_PLANE_NODE_COUNT`: specifies the number of nodes on which to run the local control plane workloads. Valid values are `3` for high availability and `1` for standard operation.

  * `CONTROL_PLANE_NODE_FILTER` (optional): specifies a regex-formatted list of nodes that run the local control plane workloads. If omitted, Distributed Cloud selects the nodes automatically at random.

  * `CONTROL_PLANE_NODE_SHARING`: specifies whether application workloads can run on the nodes that run the local control plane workloads. Valid values are `DISALLOWED` an `ALLOWED`. If omitted, defaults to `DISALLOWED`.

  * `IPV4_DATA_PLANE_ADDRESSES`: specifies the IPv4 addresses, address ranges, or subnetworks for ingress traffic for Services that run behind the Distributed Cloud load balancer when the cluster is running in survivability mode. Accepts either a comma-delimited list, or a payload in YAML or JSON format. For more information, see [Load balancing](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/networking#load-balancing).

  * `SOFTWARE_VERSION`: specifies the Distributed Cloud software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.1`. If omitted, defaults to the server-default software version, which typically is the latest available version of Distributed Cloud connected. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster. You must set the `RELEASE_CHANNEL` field to `NONE` to specify a cluster software version.

  * `REBOOT_TIMEOUT`: specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.

  * `RUNTIME_CLASS`: specifies the default runtime class for workloads in this cluster. Valid values are `runc` and `gvisor`. If omitted, defaults to `runc`. Can be overridden by specifying the runtime class in the Pod configuration as described in [Configure the Pod runtime class](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#runtime-class). This is a preview-level feature.

Specifying the `gvisor` runtime class switches the Pod to the Open Container Initiative (OCI) secure runtime based on [gVisor](https://gvisor.dev/). gVisor is a sandboxing solution that introduces strong isolation between the workload and its host. This is a preview-level runtime class.

  * `GROUP_AUTHENTICATION`: specifies whether you can access the cluster by authenticating with a Google group rather than an individual account. Valid values are `true` and `false`. If omitted, defaults to `false`.




## List clusters in a region

To list the Distributed Cloud connected clusters provisioned in a Google Cloud region, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Examine the list of clusters.




###  gcloud 

Use the `gcloud edge-cloud container clusters list` command:
    
    
    gcloud edge-cloud container clusters list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which you created your Distributed Cloud connected cluster.



###  API 

Make a `GET` request to the `projects.locations.clusters.list` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_ID&filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a cluster

To get information about a Distributed Cloud connected cluster, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the desired cluster.

A fold-out panel with detailed information about the cluster appears in the right pane.




###  gcloud 

Use the `gcloud edge-cloud container clusters describe` command:
    
    
    gcloud edge-cloud container clusters describe CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which you created your Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.clusters.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.



## Get the available software versions for a cluster

To find out which Distributed Cloud connected software versions are available on your Distributed Cloud connected zone to create clusters, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container get-server-config` command:
    
    
    gcloud edge-cloud container get-server-config --location=REGION
    

Replace `REGION`: with the Google Cloud region in which you created your Distributed Cloud connected zone.

###  API 

Make a `GET` request to the `projects.locations.serverConfig` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/serverConfig
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.



## Upgrade the software version of a cluster

To upgrade the software version of a Distributed Cloud connected cluster, complete the steps in this section.

### Specify software upgrade stage size

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before completing the steps in this section, see [Software update staggering](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/availability#update-staggering).

To specify the number of nodes that can go down for software upgrades simultaneously, use the following command:
    
    
     gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --max-unavailable-worker-nodes=MAX_UNAVAILABLE_NODES
        

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster has been created.
  * `MAX_UNAVAILABLE_NODES`: specifies the maximum number of worker nodes that can go down for a software upgrade simultaneously.



To reset this value back to default, use the following command:
    
    
     gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --clear-max-unavailable-worker-nodes
        

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster has been created.



### Upgrade a cluster to a newer version of Distributed Cloud connected software

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters upgrade` command:
    
    
    gcloud edge-cloud container clusters upgrade CLUSTER_ID \
       --location=REGION \
       --project=PROJECT_ID \
       --schedule=UPGRADE_SCHEDULE \
       --version=SOFTWARE_VERSION
    
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster has been created.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `UPGRADE_SCHEDULE`: specifies when to trigger the software upgrade. The only valid value is `IMMEDIATELY`.
  * `SOFTWARE_VERSION`: specifies the Distributed Cloud software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.1`. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster.



###  API 

Make a `POST` request to the `projects.locations.clusters.upgrade` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:upgrade?requestId=REQUEST_ID
    {
      "name": "projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID",
      "targetVersion": "SOFTWARE_VERSION",
        "schedule": "UPGRADE_SCHEDULE",
    }
    
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `UPGRADE_SCHEDULE`: specifies when to trigger the software upgrade. The only valid value is `IMMEDIATELY`.
  * `SOFTWARE_VERSION`: specifies the Distributed Cloud connected software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.1`. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster.



A software upgrade typically takes about 2 hours per each node that's part of the cluster's node pool. The command returns an operation that lets you track the progress of the software upgrade. While the software upgrade is in progress, the status of the cluster is set to `Reconciling` and returns to `Running` once the upgrade completes. A cluster status of `Error` indicates the software upgrade failed. In such cases, run the upgrade process again. See Get information about a cluster for information about checking the cluster's status.

## Modify a cluster

To modify a Distributed Cloud connected cluster, complete the steps in this section. If you are modifying the storage encryption configuration for the cluster, you cannot update any other parameters in the same update operation.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters update` command:
    
    
    gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster-ipv4-cidr=CLUSTER_IPV4_CIDR_BLOCK \
        --services-ipv4-cidr=SERVICES_IPV4_CIDR_BLOCK \
        --default-max-pods-per-node=MAX_PODS_PER_NODE \
        --release-channel=RELEASE_CHANNEL \
        --control-plane-kms-key=CONTROL_PLANE_KMS_KEY \
        --offline-reboot-ttl=REBOOT_TIMEOUT \
        --max-unavailable-worker-nodes=MAX_UNAVAILABLE_NODES \
        --default-container-runtime RUNTIME_CLASS \
        --enable-google-group-authentication GROUP_AUTHENTICATION
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `MAX_PODS_PER_NODE`: the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
  * `RELEASE_CHANNEL` (optional): specifies the release channel for the version of the Distributed Cloud connected software you want this cluster to run. Valid values are `REGULAR` (enable automatic cluster upgrades) and `NONE` (disable automatic cluster upgrades). If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/security#cmek).

  * `REBOOT_TIMEOUT`: specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.

  * `MAX_UNAVAILABLE_NODES` (optional): specifies the maximum number of worker nodes that can go down for a software upgrade simultaneously. If omitted, defaults to X. This is a preview-level feature.

  * `RUNTIME_CLASS`: specifies the default runtime class for workloads in this cluster. Valid values are `runc` and `gvisor`. If omitted, defaults to `runc`. Can be overridden by specifying the runtime class in the Pod configuration as described in [Configure the Pod runtime class](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#runtime-class). If you change the runtime class at either Pod or cluster level, you must restart the affected Pods for the change to take effect.

Specifying the `gvisor` runtime class switches the Pod to the Open Container Initiative (OCI) secure runtime based on [gVisor](https://gvisor.dev/). gVisor is a sandboxing solution that introduces strong isolation between the workload and its host.

  * `GROUP_AUTHENTICATION`: specifies whether you can access the cluster by authenticating with a Google group rather than an individual account. Valid values are `true` and `false`. If omitted, defaults to `false`.




###  API 

Make a `PATCH` request to the `projects.locations.clusters.patch` method:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/REGION/clusters/?updateMask=UPDATE_MASK&requestId=REQUEST_ID
    {
     "labels": { LABELS,
      },
      "networking": {
       "ClusterIpv4CidrBlocks": CLUSTER_IPV4_CIDR_BLOCK,
       "servicesIpv4CidrBlocks": SERVICE_IPV4_CIDR_BLOCK,
       },
      "authorization": {
        "adminUsers": {
           "username": USERNAME
        }
      },
      "defaultMaxPodsPerNode": MAX_PODS_PER_NODE,
      "releaseChannel": RELEASE_CHANNEL,
      "controlPlaneEncryption": {
       "kmsKey": CONTROL_PLANE_KMS_KEY,
      },
      "offlineRebootTtl": "REBOOT_TIMEOUT",
      "defaultContainerRuntime": "RUNTIME_CLASS",
      "enableGoogleGroupAuthentication": "GROUP_AUTHENTICATION",
      }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `UPDATE_MASK`: a comma-separated list of fully qualified field names to update in this request in [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation) that run on this cluster.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.
  * `MAX_PODS_PER_NODE`: the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
  * `RELEASE_CHANNEL`: (optional): specifies the release channel for the version of the Distributed Cloud connected software you want this cluster to run. Valid values are `REGULAR` (enable automatic cluster upgrades) and `NONE` (disable automatic cluster upgrades). If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/security#cmek).

  * `REBOOT_TIMEOUT`: (requires `v1alpha1`) specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established. This is a preview-level feature.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.

  * `RUNTIME_CLASS`: specifies the default runtime class for workloads in this cluster. Valid values are `runc` and `gvisor`. If omitted, defaults to `runc`. Can be overridden by specifying the runtime class in the Pod configuration as described in [Configure the Pod runtime class](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#runtime-class). If you change the runtime class at either Pod or cluster level, you must restart the affected Pods for the change to take effect.

Specifying the `gvisor` runtime class switches the Pod to the Open Container Initiative (OCI) secure runtime based on [gVisor](https://gvisor.dev/). gVisor is a sandboxing solution that introduces strong isolation between the workload and its host.

  * `GROUP_AUTHENTICATION`: specifies whether you can access the cluster by authenticating with a Google group rather than an individual account. Valid values are `true` and `false`. If omitted, defaults to `false`.




## Obtain credentials for a cluster

To obtain credentials for a Distributed Cloud connected cluster, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters get-credentials` command:
    
    
    gcloud edge-cloud container clusters get-credentials CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --offline-credential
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.



To generate an offline credential for the cluster, specify the `--offline-credential` flag.

###  API 

Make a `GET` request to the `projects.locations.clusters` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud zone is created.
  * `CLUSTER_ID`: the name of the target cluster.



### Obtain cluster credentials through Connect gateway

Connect gateway acts as a proxy for accessing your cluster using the `kubectl` CLI tool. Each user account requesting cluster credentials through Connect gateway must have the permissions described in [Connect gateway roles and permissions](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#connectgateway).

Before requesting credentials through Connect gateway, you must first install the `gke-gcloud-auth-plugin` plugin using the following command:
    
    
     gcloud components install gke-gcloud-auth-plugin
    

To obtain cluster credentials through Connect gateway, use the following command:
    
    
     gcloud container hub memberships get-credentials CLUSTER_ID --project=PROJECT_ID
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.



## Configure a maintenance window for a cluster

This section describes how to specify and clear the following types of maintenance windows for a Distributed Cloud connected cluster:

  * **Maintenance window.** Specifies a time window during which Google can perform maintenance and software upgrades on your Distributed Cloud connected cluster.
  * **Maintenance exclusion window.** Specifies a time window during which Google cannot perform maintenance or software upgrades on your Distributed Cloud connected cluster. To configure a maintenance exclusion window, you must first configure a maintenance window. A maintenance exclusion window takes precedence over the cluster's maintenance window.

**Warning:** A Distributed Cloud connected cluster does not have a default maintenance window. This means that a software update can potentially bring down a critical workload. To ensure high availability, we strongly recommend that you configure staggered maintenance windows and configure maintenance exclusion windows for your clusters.

### Specify a maintenance window for a cluster

To specify a maintenance window for a Distributed Cloud connected cluster, complete the steps in this section. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/availability#cluster-maintenance).

For date and time formats, use [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  Console 

If you are using the Google Cloud console, you can only specify a maintenance window when you create a cluster. To specify a maintenance window on an existing cluster, you must use the Google Cloud CLI or the Distributed Cloud Edge Container API.

###  gcloud 

Use the `gcloud edge-cloud container clusters update` command:
    
    
    gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --maintenance-window-start=MAINTENANCE_START \
        --maintenance-window-end=MAINTENANCE_END \
        --maintenance-window-recurrence=MAINTENANCE_FREQUENCY
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `MAINTENANCE_START`: the start time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.
  * `MAINTENANCE_END`: the end time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.
  * `MAINTENANCE_FREQUENCY`: the frequency of the maintenance window in the `FREQ=WEEKLY|DAILY;BYDAY=MO,TU,WE,TH,FR,SA,SU` format: 
    * `BYDAY`: a comma-delimited list of days during which maintenance can occur if `FREQ` is set to `WEEKLY`. If you omit the `BYDAY` parameter, Google chooses the day of the week for you.
    * If you set `FREQ` to daily, maintenance windows occur every day during the specified hours.



###  API 

Make a `PATCH` request to the `projects.locations.clusters.update` method:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?updateMask=maintenancePolicy&requestId=REQUEST_ID
    {
     "maintenance_policy": {
       "window": {
         "recurring_window": {
           "window": {
             "start_time": "MAINTENANCE_START",
             "end_time": "MAINTENANCE_END"
             },
           "recurrence": "MAINTENANCE_FREQUENCY"
         }
       }
     }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `UPDATE_MASK`: a comma-separated list of fully qualified field names to update in this request in [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `CLUSTER_ID`: the name of the target cluster.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.
  * `MAINTENANCE_START`: the start time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.
  * `MAINTENANCE_END`: the end time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.
  * `MAINTENANCE_FREQUENCY`: the frequency of the maintenance window in the `FREQ=WEEKLY|DAILY;BYDAY=MO,TU,WE,TH,FR,SA,SU` format: 
    * `FREQ` can be `DAILY` or `WEEKLY`.
    * `BYDAY`: a comma-delimited list of days during which maintenance can occur if `FREQ` is set to `WEEKLY`. If you omit the `BYDAY` parameter, Google chooses the day of the week for you.
    * If you set `FREQ` to daily, maintenance windows occur every day during the specified hours.



For more information, see [Resource: cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/container/rest/v1/projects.locations.clusters#resource:-cluster).

### Clear the maintenance window for a cluster

To clear the maintenance window for a Distributed Cloud connected cluster, complete the steps in this section. Clearing a maintenance window for a cluster also clears all corresponding maintenance exclusion windows for that cluster. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/availability#cluster-maintenance).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters update` command:
    
    
    gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --clear-maintenance-window
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.



###  API 

Make a `PATCH` request to the `projects.locations.clusters.update` method:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?updateMask=maintenancePolicy&requestId=REQUEST_ID
    {
     "maintenance_policy": null
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `UPDATE_MASK`: a comma-separated list of fully qualified field names to update in this request in [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.



For more information, see [Resource: cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/container/rest/v1/projects.locations.clusters#resource:-cluster).

### Specify a maintenance exclusion window for a cluster

To specify a maintenance exclusion window for a Distributed Cloud connected cluster, complete the steps in this section. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/availability#cluster-maintenance).

For date and time formats, use [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters update` command:
    
    
    gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --add-maintenance-exclusion-name=EXCLUSION_NAME \
        --add-maintenance-exclusion-start=EXCLUSION_START \
        --add-maintenance-exclusion-end=EXCLUSION_END
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `EXCLUSION_NAME`: a descriptive name for this maintenance exclusion window.
  * `EXCLUSION_START`: the start time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.
  * `EXCLUSION_END`: the end time of the maintenance window in the `YYYY-MM-DDTHH:MM:SSZ` format.



### Clear the maintenance exclusion window for a cluster

To clear the maintenance exclusion window for a Distributed Cloud connected cluster, complete the steps in this section. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/availability#cluster-maintenance).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters update` command:
    
    
    gcloud edge-cloud container clusters update CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --remove-maintenance-exclusion-window=MAINTENANCE_EXCLUSION_WINDOW
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `MAINTENANCE_EXCLUSION_WINDOW`: the name of the maintenance exclusion window you want to clear.



## Delete a cluster

To delete a Distributed Cloud connected cluster, complete the steps in this section. Before you can delete a cluster, you must first [Delete all the node pools assigned to the cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/nodepools#delete_a_node_pool).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters delete` command:
    
    
    gcloud edge-cloud container clusters delete CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.



###  API 

Make a `DELETE` request to the `projects.locations.clusters.delete` method:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?requestId=REQUEST_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/machines)
  * [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/nodepools)
  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/virtual-machines)
  * [Use fleet packages in Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/fleet-packages-guide)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
