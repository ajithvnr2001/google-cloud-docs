---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-legacy-network/
title: Create a new legacy network \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:54.832613+00:00
---

# Create a new legacy network  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-create-legacy-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Create a new legacy network Stay organized with collections  Save and categorize content based on your preferences. 

Create a new legacy network in your project to be used as connection to your VMWare Engine resources.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
