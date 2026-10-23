---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-update-policy/
title: Update network policy \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:34.641996+00:00
---

# Update network policy  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-update-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Update network policy Stay organized with collections  Save and categorize content based on your preferences. 

Updates a network policy in a given network.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure internet access for workload VMs](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core import operation
    from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
    
    
    def update_network_policy(
        project_id: str, region: str, internet_access: bool, external_ip: bool
    ) -> operation.Operation:
        """
        Updates a network policy in a given network.
    
        Args:
            project_id: name of the project you want to use.
            region: name of the region you want to use. I.e. "us-central1".
            internet_access: should internet access be allowed.
            external_ip: should external IP addresses be assigned.
    
        Returns:
            An operation object representing the started operation. You can call its .result() method to wait for
            it to finish.
        """
    
        client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
        request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.UpdateNetworkPolicyRequest.html)()
        request.update_mask = "internetAccess.enabled,externalIp.enabled"
        network_policy = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NetworkPolicy.html)()
        network_policy.name = (
            f"projects/{project_id}/locations/{region}/networkPolicies/{region}-default"
        )
        network_policy.vmware_engine_network = f"projects/{project_id}/locations/{region}/vmwareEngineNetworks/{region}-default"
        network_policy.internet_access.enabled = internet_access
        network_policy.external_ip.enabled = external_ip
    
        request.network_policy = network_policy
    
        return client.[update_network_policy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_update_network_policy)(request)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
