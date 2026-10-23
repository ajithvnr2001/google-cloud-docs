---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-get-operation/
title: Get operation details \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:18.798938+00:00
---

# Get operation details  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-get-operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Get operation details Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve detailed information about an operation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
