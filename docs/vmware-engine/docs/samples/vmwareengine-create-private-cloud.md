---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-private-cloud/
title: Create VMWare Engine Private Cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:54.267362+00:00
---

# Create VMWare Engine Private Cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Create VMWare Engine Private Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new Private Cloud using VMWare Engine. Creating a new Private Cloud is a long-running operation and it may take over an hour.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
