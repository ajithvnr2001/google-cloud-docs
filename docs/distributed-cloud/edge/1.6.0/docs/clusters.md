---
url: https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/clusters/
title: Create and manage clusters \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:48.461005+00:00
---

# Create and manage clusters  |  Google Distributed Cloud connected, version 1.6.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/clusters/

Select versionkeyboard_arrow_down

  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
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
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/overview)



Send feedback 

#  Create and manage clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud cluster resources.

For more information about Distributed Cloud clusters, see [How Distributed Cloud works](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/how-it-works).

Distributed Cloud Servers only support local control plane clusters. You cannot create Cloud control plane clusters on Distributed Cloud Servers.

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## Local control plane clusters on Distributed Cloud 1.5.x

After Google updates your Distributed Cloud deployment to version 1.5.0 or later, you must manually delete and recreate all local control plane clusters that you have created with Distributed Cloud version 1.4.0. Otherwise, unexpected behavior and data loss can occur. Clusters configured to use a cloud control plane continue to run normally after Google has updated Distributed Cloud deployment to version 1.5.0 or later.

## Create a cluster

To create a Distributed Cloud cluster, complete the steps in this section. Creating a cluster is one of multiple steps required to [deploy a workload on Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/deploy).

To create a cluster with a local control plane that can run workloads while temporarily disconnected from Google Cloud, first read [Survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/survivability). 

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

You must upgrade your Google Cloud SDK to version 450.0.0 or later to create local control plane clusters running Distributed Cloud software version 1.5.0. Otherwise, creating such clusters will fail.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click **Create cluster**.

  3. On the **Create a cluster** page, click the **On-premises** tab.

  4. Next to the **Distributed Cloud Edge** option, click **Configure**.

  5. On the **Cluster basics** page, provide the following information:

     * **Name** : a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
     * **Location** : the Google Cloud region in which you want to create this cluster.
     * **Default max pods per node** : the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
     * **Labels** : lets you add one or more labels to this cluster by clicking add**Add label**.
  6. In the left navigation, click **Networking**.

  7. On the **Networking** page, provide the following information:

     * **Cluster default pod address range** : the desired IPv4 CIDR block for Kubernetes Pods that run on this cluster. 
     * **Service address range** : the desired IPv4 CIDR block for Kubernetes Services that run on this cluster.

For more information, see [Distributed Cloud Pod and Service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/address-allocation).

  8. In the left navigation, click **Authorization**.

  9. On the **Authorization** page, provide the name of the user account within the target Google Cloud project that is authorized to modify cluster resources.

  10. In the left navigation, click **Maintenance policy**.

**Warning:** A Distributed Cloud cluster does not have a default maintenance window. This means that a software update can potentially bring down a critical workload. To ensure high availability, you must configure _staggered maintenance windows_ for your Distributed Cloud clusters so that software updates occur at different times and your workloads remain available.
  11. On the **Maintenance policy** page, provide the following information:

     * **Enable Maintenance Window** : select this checkbox to configure a maintenance window for the cluster. To prevent unexpected downtime caused by Distributed Cloud software updates, we strongly recommend that you always configure a maintenance window for each Distributed Cloud cluster that you create. For more information, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/availability#cluster-maintenance).
     * **Start time** : the desired date and time at which the maintenance window starts for this cluster.
     * **End time** : the desired date and time at which the maintenance window ends for this cluster.
     * **RRule** : the frequency of the maintenance window in the `FREQ=WEEKLY|DAILY;BYDAY=MO,TU,WE,TH,FR,SA,SU` format: 
       * `FREQ` can be `DAILY` or `WEEKLY`.
       * `BYDAY`: a comma-delimited list of days during which maintenance can occur if `FREQ` is set to `WEEKLY`. If you omit the `BYDAY` parameter, Google chooses the day of the week for you.
       * If you set `FREQ` to `DAILY`, maintenance windows occur every day during the specified hours.
  12. Assign a node pool to the cluster by doing one of the following:

     * To assign an existing node pool to this cluster, in the **Node pools** section in the left navigation, select the existing node pool and verify that the node pool configuration on the **Node pool details** page is correct.
     * To create a new node pool to assign to this cluster, click add_box**Add node pool** and provide the following information on the **Node pool details** page: 
       * **Node pool name** : a unique name that identifies this node pool.
       * **Node pool labels** : click add**Add label** to add one or more labels to this node pool.
       * **Worker nodes preference** : select the Distributed Cloud nodes to assign to this node pool.
  13. To create the Distributed Cloud cluster, click **Create**.




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
        --control-plane-kms-key=CONTROL_PLANE_KMS_KEY \
        --control-plane-node-location=CONTROL_PLANE_LOCATION \
        --control-plane-node-count=CONTROL_PLANE_NODE_COUNT \
        --control-plane-machine-filter=CONTROL_PLANE_NODE_FILTER \
        --control-plane-shared-deployment-policy=CONTROL_PLANE_NODE_SHARING \
        --external-lb-ipv4-address-pools=IPV4_DATA_PLANE_ADDRESSES \
        --version SOFTWARE_VERSION \
        --offline-reboot-ttl REBOOT_TIMEOUT
    
     

Replace the following:

  * `CLUSTER_ID`: a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the cluster is created and in which the Kubernetes control plane for the cluster is provisioned.
  * `FLEET_PROJECT_ID`: the ID of the Fleet host project in which the cluster is registered. If this flag is omitted, the Distributed Cloud cluster project is used as the Fleet host project.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/address-allocation) that run on this cluster.
  * `MAX_PODS_PER_NODE` (optional): the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
  * `RELEASE_CHANNEL`: (optional): specifies the release channel for the version of the Distributed Cloud software you want this cluster to run. Valid values are `REGULAR` (enable automatic cluster upgrades) and `NONE` (disable automatic cluster upgrades). If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This flag only applies if you have integrated Distributed Cloud with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/security#cmek).




If you are creating a cluster with a _local control plane_ , in addition to replacing the previous variables, also replace the following:

  * `CONTROL_PLANE_LOCATION`: instructs Distributed Cloud to deploy the control plane workloads for this cluster locally. The value is the name of the target Distributed Cloud zone.
  * `CONTROL_PLANE_NODE_COUNT` (optional): specifies the number of nodes on which to run the local control plane workloads. Valid values are `3` for high availability and `1` for standard operation. If omitted, defaults to `3`.
  * `CONTROL_PLANE_NODE_FILTER` (optional): specifies a regex-formatted list of nodes that run the local control plane workloads. If omitted, Distributed Cloud selects the nodes automatically at random.
  * `CONTROL_PLANE_NODE_SHARING`: (optional) specifies whether application workloads can run on the nodes that run the local control plane workloads. Valid values are `DISALLOWED` an `ALLOWED`. If omitted, If omitted, defaults to `DISALLOWED`.
  * `IPV4_DATA_PLANE_ADDRESSES`: specifies a comma-delimited list of IPv4 addresses, address ranges, or subnetworks for ingress traffic for Services that run behind the Distributed Cloud load balancer when the cluster is running in survivability mode.
  * `SOFTWARE_VERSION`: specifies the Distributed Cloud software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.0`. If omitted, defaults to the server-default software version, which typically is the latest available version of Distributed Cloud. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster.
  * `REBOOT_TIMEOUT`: (requires `gcloud alpha`) specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established. This is a preview-level feature.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.




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
      "externalLoadBalancerIpv4AddressPools": [
        "IPV4_DATA_PLANE_ADDRESSES"
      ],
      "targetVersion": "SOFTWARE_VERSION",
      "offlineRebootTtl": "REBOOT_TIMEOUT",
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: a unique name that identifies this cluster. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `FLEET_PROJECT_ID`: the ID of the Fleet host project in which the cluster is registered. This can be either a separate project or the Distributed Cloud project to which this cluster belongs (`PROJECT_ID`). Fleet registration is mandatory.
  * `LABELS`: a list of labels to apply to this cluster resource.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.
  * `CLUSTER_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Pods](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/address-allocation) that run on this cluster.
  * `SERVICE_IPV4_CIDR_BLOCK`: the desired [IPv4 CIDR block for Kubernetes Services](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/address-allocation) that run on this cluster.
  * `MAX_PODS_PER_NODE`: the desired maximum number of Kubernetes Pods to execute on each node in this cluster.
  * `RELEASE_CHANNEL`: specifies the release channel for the version of the Distributed Cloud software you want this cluster to run. Valid values are `REGULAR` and `NONE`. If omitted, defaults to `REGULAR`.
  * `CONTROL_PLANE_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this cluster's control plane node. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/security#cmek).




If you are creating a cluster with a _local control plane_ , in addition to replacing the previous variables, also replace the following:

  * `CONTROL_PLANE_LOCATION`: instructs Distributed Cloud to deploy the control plane workloads for this cluster locally. The value is the name of the target Distributed Cloud zone.
  * `CONTROL_PLANE_NODE_COUNT`: specifies the number of nodes on which to run the local control plane workloads. Valid values are `3` for high availability and `1` for standard operation.
  * `CONTROL_PLANE_NODE_FILTER` (optional): specifies a regex-formatted list of nodes that run the local control plane workloads. If omitted, Distributed Cloud selects the nodes automatically at random.
  * `CONTROL_PLANE_NODE_SHARING`: specifies whether application workloads can run on the nodes that run the local control plane workloads. Valid values are `DISALLOWED` an `ALLOWED`. If omitted, defaults to `DISALLOWED`.
  * `IPV4_DATA_PLANE_ADDRESSES`: specifies a comma-delimited list of IPv4 addresses, address ranges, or subnetworks for ingress traffic for Services that run behind the Distributed Cloud load balancer on a local control plane cluster. Does not apply to Cloud control plane clusters.
  * `SOFTWARE_VERSION`: specifies the Distributed Cloud software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.0`. If omitted, defaults to the server-default software version, which typically is the latest available version of Distributed Cloud. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster.
  * `REBOOT_TIMEOUT`: (requires `v1alpha1`) specifies a time window in seconds during which a cluster node can rejoin a cluster after rebooting while the cluster is running in survivability mode. If omitted, defaults to `0` which does not allow rebooted nodes to rejoin the cluster until connection to Google Cloud has been re-established. This is a preview-level feature.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.




## List clusters in a region

To list the Distributed Cloud clusters provisioned in a Google Cloud region, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

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
  * `REGION`: the Google Cloud region in which you created your Distributed Cloud cluster.



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

To get information about a Distributed Cloud cluster, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

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
  * `REGION`: the Google Cloud region in which you created your Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.clusters.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.



## Get the available software versions for a cluster

To find out which Distributed Cloud software versions are available on your Distributed Cloud zone to create clusters, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container get-server-config` command:
    
    
    gcloud edge-cloud container get-server-config --location=REGION
    

Replace `REGION`: with the Google Cloud region in which you created your Distributed Cloud zone.

###  API 

Make a `GET` request to the `projects.locations.serverConfig` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/serverConfig
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.



## Upgrade the software version of a local control plane cluster

To upgrade the software version of a Distributed Cloud local control plane cluster, complete the steps in this section. This feature is not available for Cloud control plane clusters.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

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
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `UPGRADE_SCHEDULE`: specifies when to trigger the software upgrade. The only valid value is `IMMEDIATELY`.
  * `SOFTWARE_VERSION`: specifies the Distributed Cloud software version that you want this cluster to run in the format `1.X.Y` where `X` is the minor version, and `Y` is the patch version, for example `1.5.1`. To get the software versions available for cluster creation, including the server-default version, see Get the available software versions for a cluster.



A software upgrade typically takes about 2 hours per each node that's part of the cluster's node pool. The command returns an operation that lets you track the progress of the software upgrade. While the software upgrade is in progress, the status of the cluster is set to `Reconciling` and returns to `Running` once the upgrade completes. A cluster status of `Error` indicates the software upgrade failed. In such cases, run the upgrade process again. See Get information about a cluster for information about checking the cluster's status.

## Obtain credentials for a cluster

To obtain credentials for a Distributed Cloud cluster, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters get-credentials` command:
    
    
    gcloud edge-cloud container clusters get-credentials CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.



###  API 

Make a `GET` request to the `projects.locations.clusters` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud zone is created.
  * `CLUSTER_ID`: the name of the target cluster.



## Configure a maintenance window for a cluster

This section describes how to specify a maintenance window and clear a maintenance window for a Distributed Cloud cluster.

**Warning:** A Distributed Cloud cluster does not have a default maintenance window. This means that a software update can potentially bring down a critical workload. To ensure high availability, you must configure _staggered maintenance windows_ for your Distributed Cloud clusters so that software updates occur at different times and your workloads remain available.

### Specify a maintenance window for a cluster

To specify a maintenance window for a Distributed Cloud cluster, complete the steps in this section. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/availability#cluster-maintenance).

For date and time formats, use [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

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
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
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
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
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



For more information, see [Resource: cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#resource:-cluster).

### Clear the maintenance window for a cluster

To clear the maintenance window for a Distributed Cloud cluster, complete the steps in this section. For more information about cluster maintenance, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/availability#cluster-maintenance).

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

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
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `UPDATE_MASK`: a comma-separated list of fully qualified field names to update in this request in [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `USERNAME`: the name of the user account within the target Google Cloud project authorized to modify cluster resources.



For more information, see [Resource: cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#resource:-cluster).

## Delete a cluster

To delete a Distributed Cloud cluster, complete the steps in this section. Before you can delete a cluster, you must first do the following:

  * [Delete all the node pools assigned to the cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/nodepools#delete_a_node_pool).
  * [Delete all the VPN connections used by the cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/vpn-connections#delete).



To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters delete` command:
    
    
    gcloud edge-cloud container clusters delete CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.



###  API 

Make a `DELETE` request to the `projects.locations.clusters.delete` method:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?requestId=REQUEST_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud cluster is created.
  * `CLUSTER_ID`: the name of the target cluster.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.



## What's next

  * [Deploy workloads on Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/deploy)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/machines)
  * [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/nodepools)
  * [Create and manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/vpn-connections)
  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/virtual-machines)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
