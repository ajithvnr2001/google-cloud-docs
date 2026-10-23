---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-delete-policy/
title: Delete network policy \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:37.209331+00:00
---

# Delete network policy  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-delete-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  Delete network policy Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a network policy.

## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core import operation
    from google.cloud import vmwareengine_v1
    
    
    def delete_network_policy(project_id: str, region: str) -> operation.Operation:
        """
        Delete a Network Policy.
    
        Args:
            project_id: name of the project hosting the policy.
            region: name of the region hosting the policy. I.e. "us-central1"
    
        Return:
            Operation object. You can use .result() to wait for it to finish.
        """
        client = vmwareengine_v1.VmwareEngineClient()
        return client.delete_network_policy(
            name=f"projects/{project_id}/locations/{region}/networkPolicies/{region}-default"
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
