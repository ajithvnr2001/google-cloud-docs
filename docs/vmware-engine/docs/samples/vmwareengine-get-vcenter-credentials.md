---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-get-vcenter-credentials/
title: Get VCenter credentials \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:53.562473+00:00
---

# Get VCenter credentials  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-get-vcenter-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Get VCenter credentials Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves VCenter credentials for a Private Cloud.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
