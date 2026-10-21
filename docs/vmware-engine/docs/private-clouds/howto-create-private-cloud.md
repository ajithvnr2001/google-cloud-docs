---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud/
title: Creating a VMware Engine private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:22.577305+00:00
---

# Creating a VMware Engine private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating a VMware Engine private cloud

A private cloud is an isolated VMware stack that consists of ESXi hosts, vCenter, vSAN, NSX, and HCX. You manage private clouds through the Google Cloud console. When you create a private cloud, you get a single vSphere cluster and all the management VMs that are created in that cluster.

VMware Engine deploys management components in the network that you select for vSphere/vSAN subnets. The internal IP address range is divided into different subnets during the deployment.

## Before you begin

Before performing the tasks on this page, perform the following prerequisite steps.

  * Allocate a unique IP address range for vSphere/vSAN subnets of the private cloud you want to create. 
    * **Minimum CIDR range prefix:** _/24_
    * **Maximum CIDR range prefix:** _/20_
  * If you want [global address resolution using Cloud DNS](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises#global-address-resolution-cloud-dns), then [enable the Cloud DNS API](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name#before-you-begin) and complete Cloud DNS setup before you create your private cloud.



The vSphere/vSAN subnet address space must not overlap with any network that will communicate with the private cloud, such as on-premises networks and Google Cloud Virtual Private Cloud (VPC) networks. For more information about vSphere or vSAN subnets, see [VLANs and subnets on VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).

### Google Cloud CLI and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

## Create a standard private cloud

###  Console 

To create a standard private cloud using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the private cloud.

  3. Click **Create**.

  4. Enter a name for the private cloud.

  5. Select **Standard private cloud** for the private cloud type.

  6. Select the location where you want the private cloud deployed.

  7. Enter a name for the primary cluster.

  8. Select the node type for your primary cluster.

  9. Select the number of nodes for the private cloud. For production workloads, create your private cloud with at least 3 nodes. VMware Engine deletes private clouds that contain only 1 node after 60 days.

  10. Optional: Click the **Customize Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  11. Enter a CIDR range for the VMware management network. For information about restrictions on this range, see the Before you begin section.

  12. Click **Review and Create**.

  13. Review the settings. To change any settings, click **Back**.

  14. Click **Create** to begin provisioning the private cloud.




The following list describes each field during private cloud creation in more detail:

  * **Name:** Permanent unique identifier of the private cloud.
  * **Description:** Additional information that's visible on the details page of the private cloud.
  * **Region:** Geographical region where VMware Engine hosts your private cloud.
  * **Zone:** Subset of a region physically isolated from other zones in the same region. A zone is a single failure domain within a region.
  * **Primary cluster name:** Name given to the initial vSphere cluster in your private cloud. VMware management appliances of your private cloud run on this cluster.
  * **Node type:** Hardware configuration of nodes in your primary cluster.
  * **Nodes:** Number of nodes in your primary cluster.



  * **Management IP address range:** IP address range used for vCenter Server, NSX Manager, ESXi hosts, and other parts of the private cloud's infrastructure. This range is not used for workload VMs and must not overlap with any part of your VPC network or any other network which you plan to connect your private cloud to.
  * **VMware Engine network:** Network resource that handles private cloud connections according to a network policy. You and resources connected to this VMware Engine network can access the private cloud from within Google Cloud.



###  gcloud 

To create a standard private cloud using the Google Cloud CLI, follow these steps:

  1. Optional: List the available regions and zones for your project by running the [`gcloud vmware locations list`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/locations/list) command:
         
         gcloud vmware locations list \
             --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request
  2. Create a network for your private cloud by running the [`gcloud vmware networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/create):
         
         gcloud vmware networks create NETWORK_NAME \
             --location=global \
             --type=STANDARD \
             --description="DESCRIPTION"

Replace the following:

     * `NETWORK_NAME`: the network name for this VMware Engine network
     * `DESCRIPTION`: a description for this VMware Engine network

The request returns an operation ID.

  3. Check the status of the operation by running the [`gcloud vmware operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/operations/describe): When the operation returns as `DONE`, check the response to see if the operation was successful:
         
         gcloud vmware operations describe OPERATION_ID \
             --location=global

Replace the following:

     * `OPERATION_ID`: the ID from the previous step
  4. Create a three-node private cloud by running the [`gcloud vmware private-clouds create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create):
         
         gcloud vmware private-clouds create PRIVATE_CLOUD_ID \
           --location=ZONE \
           --cluster=CLUSTER_ID \
           --node-type-config=type=NODE_TYPE,count=NODE_COUNT \
           --management-range=`IP_ADDRESS` \
           --vmware-engine-network=NETWORK_NAME
         

Replace the following:

     * `PRIVATE_CLOUD_ID`: the name for the private cloud.
     * `ZONE`: the zone for the private cloud.
     * `CLUSTER_ID`: the name for the new cluster in this private cloud.
     * `NODE_TYPE`: the node type. For more information, see [Node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#node-types).
     * `NODE_COUNT`: the node count. Specify a value of three or more.
     * `IP_ADDRESS`: the IP address, for example `192.168.0.0/24`, for this request.
     * `NETWORK_NAME`: the network name for this cloud.

The request returns an operations ID you can use to check the progress of the operation.

  5. Check the status of the operation by running the [`gcloud vmware operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/operations/describe): When the operation returns as `DONE`, check the response to see if the operation was successful.
         
         gcloud vmware operations describe OPERATION_ID \
             --location=ZONE
         

Replace the following:

     * `OPERATION_ID`: the ID from the previous step
     * `ZONE`: the zone for the private cloud.
  6. Connect the VMware Engine Network to your VPC by [peering VPC connections](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpc-peering).

  7. Retrieve the vCenter and NSX credentials by running the [`gcloud vmware private-clouds vcenter credentials describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/vcenter/credentials/describe) and [`gcloud vmware private-clouds nsx credentials describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/nsx/credentials/describe) commands, respectively.
         
         gcloud vmware private-clouds vcenter credentials describe \
             --private-cloud=PRIVATE_CLOUD_ID \
             --location=ZONE
         
         gcloud vmware private-clouds nsx credentials describe \
             --private-cloud=PRIVATE_CLOUD_ID \
             --location=ZONE

Replace the following:

     * `PRIVATE_CLOUD_ID`: the ID for the private cloud
     * `ZONE`: the zone for the private cloud



### API

To create a standard private cloud using the VMware Engine API, follow these steps:

  1. Create a VMware Engine network by making a `POST` request:
         
         curl -X POST -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/vmwareEngineNetworks?vmwareEngineNetworkId=NETWORK_NAME -d '{"type": "standard"}'
         

Replace the following:

     * `TOKEN`: the authorization token for this request
     * `PROJECT_ID`: the project for this request
     * `NETWORK_NAME`: the network name for the private cloud

The request returns an operations ID you can use to check the progress of the operation.

  2. Check the status of the operation by making a `GET` request. When the operation returns as `DONE`, check the response to see if the operation was successful:
         
         curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/operations/OPERATION_ID
         

Replace `OPERATION_ID` with the ID from the previous step.

  3. Create a three-node private cloud by making a `POST` request:
         
         curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?privateCloudId=PRIVATE_CLOUD_ID -d "{
         "networkConfig":{
           "vmwareEngineNetwork":"projects/PROJECT_ID/locations/global/vmwareEngineNetworks/NETWORK_NAME",
           "managementCidr":"10.241.0.0/22"
            },
         "managementCluster":{
           "clusterId": "CLUSTER_ID",
           "nodeTypeConfigs": {
           "standard-72": {
             "nodeCount": NODE_COUNT
            }
           }
          }
         }"
         

Replace the following:

     * `TOKEN`: the authorization token for this request.
     * `PROJECT_ID`: the project ID for this request
     * `ZONE`: the zone for the private cloud
     * `PRIVATE_CLOUD_ID`: the ID for the private cloud
     * `NETWORK_NAME`: the network name for the private cloud
     * `CLUSTER_ID`: the ID for the new cluster in this private cloud
     * `NODE_COUNT`: the node count. Specify a value of three or more.

The request returns an operations ID you can use to check the progress of the operation.

  4. Check the status of the operation by making a `GET` request. When the operation returns as `DONE`, check the response to see if the operation was successful:
         
         curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/operations/OPERATION_ID
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request
     * `ZONE`: the zone for the private cloud
     * `OPERATION_ID`: the ID from the previous step
  5. Connect the VMware Engine Network to your VPC by [peering VPC connections](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpc-peering).

  6. Retrieve the vCenter and NSX credentials by making `GET` requests:
         
         curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID:showVcenterCredentials"
         
         
         curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID:showNsxCredentials"
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request
     * `ZONE`: the zone for the private cloud
     * `PRIVATE_CLOUD_ID`: the ID for the private cloud



### Python

  1. Create a legacy network.
         
         from google.cloud import vmwareengine_v1
         
         TIMEOUT = 1200  # 20 minutes
         
         
         def create_legacy_network(
             project_id: str, region: str
         ) -> vmwareengine_v1.VmwareEngineNetwork:
             """
             Creates a new legacy network.
         
             Args:
                 project_id: name of the project you want to use.
                 region: name of the region you want to use. I.e. "us-central1"
         
             Returns:
                 The newly created VmwareEngineNetwork object.
             """
             network = vmwareengine_v1.VmwareEngineNetwork()
             network.description = (
                 "Legacy network created using vmwareengine_v1.VmwareEngineNetwork"
             )
             network.type_ = vmwareengine_v1.VmwareEngineNetwork.Type.LEGACY
         
             request = vmwareengine_v1.CreateVmwareEngineNetworkRequest()
             request.parent = f"projects/{project_id}/locations/{region}"
             request.vmware_engine_network_id = f"{region}-default"
             request.vmware_engine_network = network
         
             client = vmwareengine_v1.VmwareEngineClient()
             result = client.create_vmware_engine_network(request, timeout=TIMEOUT).result()
         
             return result
         
         

  2. Create a three-node private cloud.
         
         from google.api_core import operation
         from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
         
         DEFAULT_MANAGEMENT_CIDR = "192.168.0.0/24"
         DEFAULT_NODE_COUNT = 3
         
         
         def create_private_cloud(
             project_id: str, zone: str, network_name: str, cloud_name: str, cluster_name: str
         ) -> operation.Operation:
             """
             Creates a new Private Cloud using VMware Engine.
         
             Creating a new Private Cloud is a long-running operation and it may take over an hour.
         
             Args:
                 project_id: name of the project you want to use.
                 zone: the zone you want to use, i.e. "us-central1-a"
                 network_name: name of the VMWareNetwork to use for the new Private Cloud
                 cloud_name: name of the new Private Cloud
                 cluster_name: name for the new cluster in this Private Cloud
         
             Returns:
                 An operation object representing the started operation. You can call its .result() method to wait for it to finish.
             """
             request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[CreatePrivateCloudRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.CreatePrivateCloudRequest.html)()
             request.parent = f"projects/{project_id}/locations/{zone}"
             request.private_cloud_id = cloud_name
         
             request.private_cloud = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[PrivateCloud](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.PrivateCloud.html)()
             request.private_cloud.management_cluster = (
                 [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[PrivateCloud](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.PrivateCloud.html).[ManagementCluster](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.PrivateCloud.ManagementCluster.html)()
             )
             request.private_cloud.management_cluster.cluster_id = cluster_name
         
             node_config = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NodeTypeConfig](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NodeTypeConfig.html)()
             node_config.node_count = DEFAULT_NODE_COUNT
         
             # Currently standard-72 is the only supported node type.
             request.private_cloud.management_cluster.node_type_configs = {
                 "standard-72": node_config
             }
         
             request.private_cloud.network_config = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NetworkConfig](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NetworkConfig.html)()
             request.private_cloud.network_config.vmware_engine_network = network_name
             request.private_cloud.network_config.management_cidr = DEFAULT_MANAGEMENT_CIDR
         
             client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
             return client.[create_private_cloud](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_create_private_cloud)(request)
         
         

The `create_private_cloud` function returns an operations object you can use to check the progress of the operation.

  3. Check the status of the operation. Fetch current information about an operation.
         
         from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
         from google.longrunning.operations_pb2 import GetOperationRequest
         
         
         def get_operation_by_name(operation_name: str) -> Operation:
             """
             Retrieve detailed information about an operation.
         
             Args:
                 operation_name: name identifying an operation you want to check.
                     Expected format: projects/{project_id}/locations/{region}/operations/{operation_id}
         
             Returns:
                 Operation object with details.
             """
             client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
             request = GetOperationRequest()
             request.name = operation_name
             return client.[get_operation](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_get_operation)(request)
         
         
         def get_operation(project_id: str, region: str, operation_id: str) -> Operation:
             """
             Retrieve detailed information about an operation.
         
             Args:
                 project_id: name of the project running the operation.
                 region: name of the region in which the operation is running.
                 operation_id: identifier of the operation.
         
             Returns:
                 Operation object with details.
             """
             return get_operation_by_name(
                 f"projects/{project_id}/locations/{region}/operations/{operation_id}"
             )
         
         

You can use `.result()` member method of the operation object to wait for it to complete.

  4. Connect the VMware Engine Network to your VPC by [peering VPC connections](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpc-peering).

  5. Retrieve the vCenter and NSX credentials.
         
         from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
         
         
         def get_vcenter_credentials(
             project_id: str, zone: str, private_cloud_name: str
         ) -> vmwareengine_v1.Credentials:
             """
             Retrieves VCenter credentials for a Private Cloud.
         
             Args:
                 project_id: name of the project hosting the private cloud.
                 zone: name of the zone hosting the private cloud.
                 private_cloud_name: name of the private cloud.
         
             Returns:
                 A Credentials object.
             """
             client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
             credentials = client.[show_vcenter_credentials](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_show_vcenter_credentials)(
                 private_cloud=f"projects/{project_id}/locations/{zone}/privateClouds/{private_cloud_name}"
             )
             return credentials
         
         
         
         from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
         
         
         def get_nsx_credentials(
             project_id: str, zone: str, private_cloud_name: str
         ) -> vmwareengine_v1.Credentials:
             """
             Retrieves NSX credentials for a Private Cloud.
         
             Args:
                 project_id: name of the project hosting the private cloud.
                 zone: name of the zone hosting the private cloud.
                 private_cloud_name: name of the private cloud.
         
             Returns:
                 A Credentials object.
             """
             client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
             credentials = client.[show_nsx_credentials](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_show_nsx_credentials)(
                 private_cloud=f"projects/{project_id}/locations/{zone}/privateClouds/{private_cloud_name}"
             )
             return credentials
         
         




As VMware Engine creates your new private cloud, it deploys a number of [VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) and divides the provided IP address range into subnets. Private cloud creation can take 30 minutes to 2 hours. After the provisioning is complete, you will receive an email.

## What's next

  * [Get sign-in credentials for management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client).
  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
