---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-custom-cluster/
title: Create custom VMWare Engine cluster \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:18.761976+00:00
---

# Create custom VMWare Engine cluster  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-custom-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Create custom VMWare Engine cluster Stay organized with collections  Save and categorize content based on your preferences. 

Create a new cluster with custom number of cores in its nodes in a private cloud. Creation of a new cluster is a long-running operation and it may take over an hour.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core import operation
    from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
    
    
    def create_custom_cluster(
        project_id: str,
        zone: str,
        private_cloud_name: str,
        cluster_name: str,
        node_count: int = 4,
        core_count: int = 28,
    ) -> operation.Operation:
        """
        Create a new cluster with custom number of cores in its nodes
        in a private cloud.
    
        Creation of a new cluster is a long-running operation and it may take over an hour.
    
        Args:
            project_id: name of the project you want to use.
            zone: region in which your private cloud is located.
            private_cloud_name: name of the private cloud hosting the new cluster.
            cluster_name: name of the new cluster.
            node_count: number of nodes in the new cluster.
            core_count: number of CPU cores in the new cluster nodes.
    
        Returns:
            An Operation object related to started cluster creation operation.
    
        Raises:
            ValueError in case an incorrect number of nodes is provided.
        """
        if node_count < 3:
            raise ValueError("Cluster needs to have at least 3 nodes")
    
        request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.CreateClusterRequest.html)()
        request.parent = (
            f"projects/{project_id}/locations/{zone}/privateClouds/{private_cloud_name}"
        )
    
        request.cluster = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[Cluster](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.Cluster.html)()
        request.cluster.name = cluster_name
    
        # Currently standard-72 is the only supported node type.
        request.cluster.node_type_configs = {
            "standard-72": [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NodeTypeConfig](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NodeTypeConfig.html)()
        }
        request.cluster.node_type_configs["standard-72"].node_count = node_count
        request.cluster.node_type_configs["standard-72"].custom_core_count = core_count
    
        client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
        return client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_create_cluster)(request)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
