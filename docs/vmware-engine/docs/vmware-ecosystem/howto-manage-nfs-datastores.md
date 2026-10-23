---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores/
title: Use NFS volumes as vSphere Datastores in VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:19.152788+00:00
---

# Use NFS volumes as vSphere Datastores in VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use NFS volumes as vSphere Datastores in VMware Engine

This page describes how to use NFS volumes as vSphere Datastores in VMware Engine. You can create and manage NFS Datastores backed by Filestore instances, Google Cloud NetApp Volumes volumes, or third-party NFS shares using the VMware Engine API, the Google Cloud CLI, or Terraform. The API endpoint is `vmwareengine.googleapis.com`. API and gcloud CLI operations for creating, updating, deleting, mounting, and unmounting Datastores are asynchronous. When you initiate one of these operations, VMware Engine returns an operation object that you can use to track the status of your request.

## Monitor an operation

To track the status of an operation, use the API or the gcloud CLI.

###  API 
    
    
    curl -X GET \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the operation.
  * `OPERATION_ID`: The ID of the operation being tracked.



###  gcloud 
    
    
    gcloud vmware operations describe OPERATION_ID --location=LOCATION --project=PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the operation.
  * `OPERATION_ID`: The ID of the operation being tracked.



## Create an NFS Datastore

To create a Datastore backed by a Filestore instance, a Google Cloud NetApp Volumes volume, or a third-party NFS share, use Terraform, the API, or gcloud CLI. To create a datastore using the API, make the following `POST` request:
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores?datastoreId=DATASTORE_ID
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location for the Datastore.
  * `DATASTORE_ID`: The name of your Datastore.



The request body must be a JSON object containing the details of the NFS volume that will back the Datastore.

  * **`description`:** (Optional) A brief description of your Datastore.
  * **`nfs_datastore`:** (Required) A container for the NFS Datastore configuration.



### Filestore

The following sections describe how to create a Filestore-backed Datastore using the API, the gcloud CLI, or Terraform.

###  API 

For a Datastore backed by Filestore, provide the following in `google_file_service`:

  * **`filestore_instance`:** (Required) The full resource name of the Filestore instance in the format `projects/{project}/locations/{location}/instances/{instance}`.



**Example request body:**
    
    
    {
      "description": "Filestore Datastore example",
      "nfs_datastore": {
        "google_file_service": {
          "filestore_instance": "projects/FILESTORE_PROJECT_ID/locations/LOCATION/instances/INSTANCE_NAME"
        }
      }
    }
    

Replace the following:

  * `FILESTORE_PROJECT_ID`: The project ID where your Filestore instance resides.
  * `LOCATION`: The location of the Filestore instance. This must be the same as the Datastore location specified in the request URL.
  * `INSTANCE_NAME`: The name of your Filestore instance.



###  gcloud 
    
    
    gcloud vmware datastores create DATASTORE_ID \
    --location=LOCATION --project=PROJECT_ID \
    --filestore=projects/FILESTORE_PROJECT_ID/locations/LOCATION/instances/INSTANCE_NAME
    

Replace the following:

  * `DATASTORE_ID`: The name of your Datastore.
  * `LOCATION`: The location for the Datastore and the Filestore instance.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `FILESTORE_PROJECT_ID`: The project ID where your Filestore instance resides.
  * `INSTANCE_NAME`: The name of your Filestore instance.



###  Terraform 

For more information, see the [`google_vmwareengine_datastore`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_datastore) Terraform resource.
    
    
    resource "google_vmwareengine_datastore" "DATASTORE_ID" {
      name        = "DATASTORE_ID"
      location    = "LOCATION"
      description = "DESCRIPTION"
    
      nfs_datastore {
        google_file_service {
          filestore_instance = "projects/FILESTORE_PROJECT_ID/locations/LOCATION/instances/INSTANCE_NAME"
        }
      }
    }
    

Replace the following:

  * `DATASTORE_ID`: The name of your Datastore.
  * `LOCATION`: The location for the Datastore and the Filestore instance.
  * `DESCRIPTION`: A description for the Datastore.
  * `FILESTORE_PROJECT_ID`: The project ID where your Filestore instance resides.
  * `INSTANCE_NAME`: The name of your Filestore instance.



### Google Cloud NetApp Volumes

The following sections describe how to create a Datastore backed by Google Cloud NetApp Volumes using the API or gcloud CLI.

###  API 

For a Datastore backed by Google Cloud NetApp Volumes, provide the following in `google_file_service`:

  * **`netapp_volume`:** (Required) The full resource name of the Google Cloud NetApp Volumes volume in the format `projects/{project}/locations/{location}/volumes/{volume}`.



**Example request body:**
    
    
    {
      "description": "NetApp Volumes Datastore example",
      "nfs_datastore": {
        "google_file_service": {
          "netapp_volume": "projects/NETAPP_PROJECT_ID/locations/LOCATION/volumes/VOLUME_NAME"
        }
      }
    }
    

Replace the following:

  * `NETAPP_PROJECT_ID`: The project ID where your Google Cloud NetApp Volumes volume resides.
  * `LOCATION`: The location of the Google Cloud NetApp Volumes volume. This must be the same as the Datastore location specified in the request URL.
  * `VOLUME_NAME`: The name of your Google Cloud NetApp Volumes volume.



###  gcloud 
    
    
    gcloud vmware datastores create DATASTORE_ID \
    --location=LOCATION --project=PROJECT_ID \
    --netapp=projects/NETAPP_PROJECT_ID/locations/LOCATION/volumes/VOLUME_NAME
    

Replace the following:

  * `DATASTORE_ID`: The name of your Datastore.
  * `LOCATION`: The location for the Datastore and the Google Cloud NetApp Volumes volume.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `NETAPP_PROJECT_ID`: The project ID where your Google Cloud NetApp Volumes volume resides.
  * `VOLUME_NAME`: The name of your Google Cloud NetApp Volumes volume.



###  Terraform 

For more information, see the [`google_vmwareengine_datastore`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_datastore) Terraform resource.
    
    
    resource "google_vmwareengine_datastore" "DATASTORE_ID" {
      name        = "DATASTORE_ID"
      location    = "LOCATION"
      description = "DESCRIPTION"
    
      nfs_datastore {
        google_file_service {
          netapp_volume = "projects/NETAPP_PROJECT_ID/locations/LOCATION/volumes/VOLUME_NAME"
        }
      }
    }
    

Replace the following:

  * `DATASTORE_ID`: The name of your Datastore.
  * `LOCATION`: The location for the Datastore and the Google Cloud NetApp Volumes volume.
  * `DESCRIPTION`: A description for the Datastore.
  * `NETAPP_PROJECT_ID`: The project ID where your Google Cloud NetApp Volumes volume resides.
  * `VOLUME_NAME`: The name of your Google Cloud NetApp Volumes volume.



### Third-party NFS

The following sections describe how to create a Datastore backed by a third-party NFS share using the API or gcloud CLI.

###  API 

For a Datastore backed by a third-party NFS share, provide the following in `nfs_datastore`:

  * **`third_party_nfs`:** (Required) Contains configuration for third-party NFS. 
    * **`network`:** The VPC network name in format `projects/{project}/global/networks/{network}`.
    * **`file_share`:** The file share name.
    * **`servers`:** A list of server IP addresses.



**The request body resembles the following:**
    
    
    {
      "description": "Third-party NFS Datastore example",
      "nfs_datastore": {
        "third_party_nfs": {
          "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
          "file_share": "FILE_SHARE_NAME",
          "servers": ["SERVER_ADDRESS_1"]
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `NETWORK_NAME`: The name of the VPC network for the third-party NFS Datastore.
  * `FILE_SHARE_NAME`: The file share name for the third-party NFS Datastore.
  * `SERVER_ADDRESS_1`: A server IP address for the third-party NFS Datastore. Add more addresses to the list if needed.



###  gcloud 
    
    
    gcloud vmware datastores create DATASTORE_ID \
    --third-party-nfs-network=NETWORK_NAME \
    --third-party-nfs-file-share=FILE_SHARE_NAME \
    --third-party-nfs-servers=SERVER_ADDRESSES \
    --location=LOCATION --project=PROJECT_ID
    

Replace the following:

  * `DATASTORE_ID`: The name of your Datastore.
  * `NETWORK_NAME`: The VPC network name for the third-party NFS Datastore.
  * `FILE_SHARE_NAME`: The file share name for the third-party NFS Datastore.
  * `SERVER_ADDRESSES`: A comma-separated list of server IP addresses for the third-party NFS Datastore.
  * `LOCATION`: The location for the Datastore.
  * `PROJECT_ID`: Your Google Cloud project ID.



## List or get Datastores

To list all Datastores for a given project and location, use the gcloud CLI or make a `GET` request:

###  API 

To list all Datastores for a given project and location, make a `GET` request:
    
    
    GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores
    

To retrieve details about a specific Datastore, make a `GET` request:
    
    
    GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the Datastore.
  * `DATASTORE_ID`: The name of the Datastore.



###  gcloud 

To list all Datastores for a given project and location, use the `gcloud vmware datastores list` command:
    
    
    gcloud vmware datastores list \
    --location=LOCATION --project=PROJECT_ID
    

To retrieve details about a specific Datastore, use the `gcloud vmware datastores describe` command:
    
    
    gcloud vmware datastores describe DATASTORE_ID \
    --location=LOCATION --project=PROJECT_ID
    

Replace the following:

  * `LOCATION`: The location of the Datastore.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `DATASTORE_ID`: The name of the Datastore.



## Mount a Datastore

After you create a Datastore, you must mount it to a vSphere cluster to make it available to ESXi hosts. To mount an NFS Datastore, use the gcloud CLI, the API, or Terraform.

**Note:** You can't delete the Datastore resource or the network peering until the Datastore is unmounted from the cluster.

###  API 
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID:mountDatastore
    

**Example request body:**
    
    
    {
      "datastore_mount_config": {
        "datastore": "projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID",
        "datastore_network": {
          "subnet": "projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/subnets/SERVICE_SUBNET_NAME",
          "connection_count": 4
        },
        "access_mode": "READ_WRITE",
        "nfs_version": "NFS_V3"
      }
    }
    

  * **`datastore`:** The resource name of the Datastore to mount.
  * **`subnet`:** The resource name of the service subnet to use for NFS traffic.
  * **`connection_count`:** (Optional) The number of connections. Default is `4`.
  * **`access_mode`:** (Optional) The access mode, `READ_WRITE` or `READ_ONLY`. Default is `READ_WRITE`.
  * **`nfs_version`:** (Optional) The NFS version. Default is `NFS_V3`.



Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the resources.
  * `PRIVATE_CLOUD_ID`: The name of the private cloud.
  * `CLUSTER_ID`: The name of the cluster.
  * `DATASTORE_ID`: The name of the Datastore to mount.
  * `SERVICE_SUBNET_NAME`: The name of the service subnet to use for NFS traffic.



###  gcloud 
    
    
    gcloud vmware private-clouds clusters mount-datastore CLUSTER_ID \
    --location=LOCATION --project=PROJECT_ID \
    --private-cloud=PRIVATE_CLOUD_ID \
    --datastore=projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID \
    --subnet=SERVICE_SUBNET_NAME
    

Alternatively, you can provide network configuration details using a JSON file with the `--datastore-network` flag:
    
    
    gcloud vmware private-clouds clusters mount-datastore CLUSTER_ID \
    --location=LOCATION --project=PROJECT_ID \
    --private-cloud=PRIVATE_CLOUD_ID \
    --datastore=projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID \
    --datastore-network=network-config.json
    

Where `network-config.json` contains:
    
    
    {
        "subnet": "SERVICE_SUBNET_NAME",
        "mtu": 1500,
        "connection-count": 4
    }
    

Replace the following:

  * `CLUSTER_ID`: The name of the cluster.
  * `LOCATION`: The location of the resources.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `PRIVATE_CLOUD_ID`: The name of the private cloud.
  * `DATASTORE_ID`: The name of the Datastore to mount.
  * `SERVICE_SUBNET_NAME`: The name of the service subnet to use for NFS traffic.



###  Terraform 

For more information, see the [`google_vmwareengine_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_cluster) Terraform resource, including examples for [mounting Filestore datastores](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_cluster#example-usage---vmware-engine-cluster-nfs-datastore-filestore) and [mounting Google Cloud NetApp Volumes datastores](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_cluster#example-usage---vmware-engine-cluster-nfs-datastore-netapp).
    
    
    resource "google_vmwareengine_cluster" "CLUSTER_ID" {
      name    = "CLUSTER_ID"
      parent  = "projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID"
      ...
      datastore_mount_config {
        datastore = "projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID"
        datastore_network {
          subnet           = "projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/subnets/SERVICE_SUBNET_NAME"
          connection_count = 4
          mtu              = 1500
        }
        nfs_version = "NFS_V3"
      }
    }
    

Replace the following:

  * `CLUSTER_ID`: The name of the cluster.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the resources.
  * `PRIVATE_CLOUD_ID`: The name of the private cloud.
  * `DATASTORE_ID`: The name of the Datastore to mount.
  * `SERVICE_SUBNET_NAME`: The name of the service subnet to use for NFS traffic.



**Note:** To mount the datastore on a vSphere cluster, ensure that you configure the `datastore_mount_config` block within the `google_vmwareengine_cluster` resource.

After a successful mount operation, you can view the mounted Datastore configuration in the cluster resource. The cluster resource includes a `DatastoreMountConfig` entry that corresponds to the mount. For example:
    
    
    ...
    datastoreMountConfig:
    - accessMode: READ_WRITE
      datastore: projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
      datastoreNetwork:
        connectionCount: 4
        mtu: 1500
        networkPeering: projects/PROJECT_ID/locations/global/networkPeerings/PEERING_NAME
        subnet: projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/subnets/SUBNET_NAME
      fileShare: FILE_SHARE_NAME
      nfsVersion: NFS_V3
      servers:
      - SERVER_IP
    ...
    

After a successful mount operation, the Datastore resource's `clusters` list is updated. You can describe a Datastore to see which clusters it is mounted on.

###  API 
    
    
    GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
    

###  gcloud 
    
    
    gcloud vmware datastores describe DATASTORE_ID --location=LOCATION --project=PROJECT_ID
    

After describing a Datastore, look for the `clusters` field in the response to see which clusters the Datastore is mounted on. The following example output shows a Datastore mounted on one cluster:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID",
      ...
      "clusters": [
        "projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID"
      ],
      ...
    }
    

## Mount an NFS datastore to the management cluster

The `datastore_mount_config` block used for mounting NFS datastores is an attribute of the `google_vmwareengine_cluster` resource. However, the Management Cluster is initially defined within the `management_cluster` block of the `google_vmwareengine_private_cloud` resource, not as a standalone `google_vmwareengine_cluster` resource. This means you cannot directly configure the `datastore_mount_config` for the Management Cluster upon creation of the Private Cloud.

To mount an NFS datastore on the Management Cluster using Terraform, you need to import the existing Management Cluster into your Terraform state as a separate `google_vmwareengine_cluster` resource after the Private Cloud is provisioned.

**Steps:**

  1. Import the Management Cluster: After the Private Cloud and Management Cluster exist, run the following Terraform command to import the Management Cluster into the state:


    
    
    terraform import google_vmwareengine_cluster.imported_management_cluster "projects/{your_project}/locations/{private_cloud_location}/privateClouds/{your_private_cloud_id}/clusters/{your_management_cluster_id}"
    

_Replace the placeholders`{your_project}`, `{private_cloud_location}`, `{your_private_cloud_id}`, and `{your_management_cluster_id}` with your specific environment details._

  1. **Define the Cluster Resource in Configuration:** Add a `resource "google_vmwareengine_cluster" "imported_management_cluster"` block to your Terraform configuration file. This block should accurately reflect the current configuration of the imported Management Cluster (e.g., node type, node count).

  2. **Add Datastore Mount Configuration:** Within the new `google_vmwareengine_cluster.imported_management_cluster` resource block, add the `datastore_mount_config` block to define the NFS datastore settings you want to mount.




**Example Configuration Snippet:**
    
    
    # Assume google_vmwareengine_private_cloud "my_pc" is already defined and created
    
    # Resource block for the imported Management Cluster
    resource "google_vmwareengine_cluster" "imported_management_cluster" {
      provider = google
      name     = "{your_management_cluster_id}" # Must match the imported cluster's ID
      parent   = google_vmwareengine_private_cloud.my_pc.id
    
      # Ensure these match the existing management cluster's configuration
      node_type_configs {
        node_type_id = "standard-72"
        node_count   = 3
        # Add other configs like custom_core_count if set
      }
    
      # Add the datastore mount configuration
      datastore_mount_config {
        datastore = data.google_vmwareengine_datastore.my_nfs_datastore.id
        datastore_network {
          subnet = data.google_vmwareengine_subnet.my_service_subnet.id
          connection_count = 4
          mtu = 1500
        }
        nfs_version = "NFS_V3"
        access_mode = "READ_WRITE"
        ignore_colocation = true
      }
    
      # Optional: Prevent accidental destruction of this imported resource
      lifecycle {
        ignore_changes = [
          # Ignore changes to attributes managed by the private_cloud resource
          # to prevent conflicts. Adjust as needed.
        ]
        prevent_destroy = true
      }
    }
    
    # Data sources for datastore and subnet would be defined elsewhere
    # data "google_vmwareengine_datastore" "my_nfs_datastore" { ... }
    # data "google_vmwareengine_subnet" "my_service_subnet" { ... }
    
    

## Update a Datastore

You can update only the `description` field of a Datastore. To update a Datastore, use the gcloud CLI or make a `PATCH` request:

###  API 
    
    
    PATCH https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
    

**Example request body:**
    
    
    {
      "description": "New datastore description"
    }
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the Datastore.
  * `DATASTORE_ID`: The ID of the Datastore.



###  gcloud 
    
    
    gcloud vmware datastores update DATASTORE_ID \
    --location=LOCATION --project=PROJECT_ID \
    --description="DESCRIPTION"
    

Replace the following:

  * `DATASTORE_ID`: The name of the Datastore.
  * `LOCATION`: The location of the Datastore.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `DESCRIPTION`: A description for the Datastore.



## Unmount a Datastore

To unmount an NFS Datastore from a cluster, use the gcloud CLI, the API, or Terraform:

###  API 
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID:unmountDatastore
    

**Example request body:**
    
    
    {
      "datastore": "projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID"
    }
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the resources.
  * `PRIVATE_CLOUD_ID`: The name of the private cloud.
  * `CLUSTER_ID`: The name of the cluster.
  * `DATASTORE_ID`: The name of the Datastore to unmount.



###  gcloud 
    
    
    gcloud vmware private-clouds clusters unmount-datastore CLUSTER_ID \
    --location=LOCATION --project=PROJECT_ID \
    --private-cloud=PRIVATE_CLOUD_ID \
    --datastore=projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
    

Replace the following:

  * `CLUSTER_ID`: The name of the cluster.
  * `LOCATION`: The location of the resources.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `PRIVATE_CLOUD_ID`: The name of the private cloud.
  * `DATASTORE_ID`: The name of the Datastore to unmount.



###  Terraform 

To unmount a Datastore using Terraform, remove the `datastore_mount_config` block associated with the Datastore from the `google_vmwareengine_cluster` resource in your Terraform configuration.

If the `datastore_mount_config` block is removed, Terraform unmounts the Datastore from the cluster during the next apply.

## Delete a Datastore

To delete a Datastore resource, use the gcloud CLI or make a `DELETE` request. The Datastore must not be mounted to any cluster.

**Note:** Deleting a Datastore removes the Datastore resource from VMware Engine, but does not delete the underlying NFS volume, such as a Filestore instance or Google Cloud NetApp Volumes volume.

###  API 
    
    
    DELETE https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datastores/DATASTORE_ID
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location of the Datastore.
  * `DATASTORE_ID`: The name of the Datastore to delete.



###  gcloud 
    
    
    gcloud vmware datastores delete DATASTORE_ID \
    --location=LOCATION --project=PROJECT_ID
    

Replace the following:

  * `DATASTORE_ID`: The name of the Datastore to delete.
  * `LOCATION`: The location of the Datastore.
  * `PROJECT_ID`: Your Google Cloud project ID.



## Troubleshooting

The following tables list common errors during Datastore creation and mounting:

### Create Datastore errors

The following table describes errors that you might encounter when creating Datastores:

Error message | Cause | Solution  
---|---|---  
The filestore NFS file-server instance can't be empty. | The `filestore_instance` field in the request body is empty. | Provide the full resource name of your Filestore instance.  
The netapp NFS file-server volume can't be empty. | The `netapp_volume` field in the request body is empty. | Provide the full resource name of your Google Cloud NetApp Volumes volume.  
Invalid Field format for field type filestore_instance | The `filestore_instance` field does not follow the required format. | Ensure the resource name is in the format `projects/{project}/locations/{location}/instances/{instance}`.  
Invalid Field format for field type netapp_volume… | The `netapp_volume` field does not follow the required format. | Ensure the resource name is in the format `projects/{project}/locations/{location}/volumes/{volume}`.  
Datastore and NFS volume are in different locations. | The Filestore instance or Google Cloud NetApp Volumes volume is in a different location than the Datastore you are trying to create. | Ensure both the NFS volume and the Datastore are in the same location.  
User missing required permissions "file.instances.get" | The service account does not have the necessary IAM permissions to access the Filestore instance. | Grant the `roles/file.viewer` role to the VMware Engine service agent.  
Permission 'netapp.volumes.get' denied on resource… | The service account does not have the necessary IAM permissions to access the Google Cloud NetApp Volumes volume. | Grant the `roles/netapp.viewer` role to the VMware Engine service agent.  
The Filestore instance ... does not exist. | The specified Filestore instance couldn't be found. | Verify that the Filestore instance exists and that the resource name is correct.  
The Netapp volume ... does not exist. | The specified Google Cloud NetApp Volumes volume couldn't be found. | Verify that the Google Cloud NetApp Volumes volume exists and that the resource name is correct.  
The Filestore instance has an unsupported tier | The Filestore instance uses a tier that this feature doesn't support. | Create a new Filestore instance with a supported tier: Zonal or Regional.  
The Filestore instance has an unsupported NFS version | The Filestore instance uses an unsupported NFS version. | Create a new Filestore instance with NFS version 3.  
The Netapp volume ... has an unsupported NFS version … | The Google Cloud NetApp Volumes volume is using an unsupported NFS version. | Create a new Google Cloud NetApp Volumes volume with NFS version 3.  
The Netapp volume ... has delete protection disabled. | The Google Cloud NetApp Volumes volume has delete protection disabled. | Enable delete protection on the Google Cloud NetApp Volumes volume.  
Can't create Datastore. Resource ... with the same configuration already exists. | A Datastore with the same name and configuration already exists. | Choose a different name for your Datastore or modify the configuration.  
  
### Mount and unmount Datastore errors

The following table describes errors that you might encounter when mounting or unmounting Datastores:

Error message | Cause | Solution  
---|---|---  
DatastoreFormat validation failed. | The specified Datastore format is not supported or is invalid. | Ensure the Datastore format is compatible with VMware Engine (for example, NFSv3).  
Invalid MTU range, should be 1300 to 9000 | The MTU (Maximum Transmission Unit) value provided for the Datastore network is outside the acceptable range of 1300 to 9000. | Specify an MTU value between 1300 and 9000.  
Datastore project is not equal to cluster project | The Google Cloud project ID of the Datastore does not match the Google Cloud project ID of the vSphere cluster. | Ensure the Datastore and the cluster belong to the same Google Cloud project.  
Invalid MTU, MTU should be consistent with the MTU of existing mounted Datastore in the cluster | The MTU of the new Datastore network is inconsistent with the MTU of other NFS Datastores already mounted on the same cluster. | Align the MTU of the new Datastore with the MTU of existing mounted Datastores in the cluster.  
Datastore should be present and should be in Ready state | The specified Datastore resource does not exist or is not in the `READY` state. | Verify that the Datastore has been created successfully and its status is `READY` using the Get or List Datastore API.  
For First party, referenced filestore or netapp should be present and should be in ready state | The underlying Filestore instance or Google Cloud NetApp Volumes volume is either missing or not in a `READY` state. | Ensure the referenced NFS volume exists and is in a `READY` state in its Google Cloud project.  
Network peering should exist in active state between file share VPC and VMware Engine network of cluster's private cloud | A VPC Network Peering connection is required between the VPC network where the NFS volume resides and the VMware Engine network of the private cloud, and this connection is either missing or not in an `ACTIVE` state. | Confirm that an active VPC Network Peering connection exists between the file share's VPC and the VMware Engine network of your private cloud.  
Mount operation fails on legacy networks | For legacy networks, the private connection to the NFS volume's tenant project is missing or inactive. | Ensure that an active private connection to the tenant project exists before you attempt to mount the Datastore. Don't delete a private connection that a mounted Datastore is using.  
For First party, export option should added to allow pc subnet used for mount | The export policy on the NFS volume does not include the private cloud's service subnet for access. | Modify the export policy of your NFS volume to allow access from the private cloud's service subnet that will be used for mounting.  
Subnet should be present with valid ip CIDR configured to it | The service subnet specified for the Datastore network is either missing or does not have a valid IP CIDR range configured. | Ensure the designated service subnet exists and has a properly configured IP CIDR range, sufficient to allocate IPs to all ESXi hosts in the cluster.  
Invalid Datastore format | The specified Datastore resource name is not in a recognized or correct format, preventing the unmount operation. | Verify that the Datastore resource name provided in the unmount request is accurate and follows the format `projects/{project}/locations/{location}/datastores/{datastore_id}`.  
Datastore not mounted on cluster | The Datastore you are attempting to unmount is not mounted on the specified cluster. | Before attempting to unmount, confirm that the Datastore is mounted on the target vSphere cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
