---
url: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-list-clusters/
title: List VMWare Engine clusters \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:14:23.486088+00:00
---

# List VMWare Engine clusters  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/samples/vmwareengine-list-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/vmware-engine/docs/samples)



#  List VMWare Engine clusters Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of clusters in private cloud.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud)



## Code sample

### Python

To authenticate to VMware Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Iterable
    
    from google.cloud import vmwareengine_v1
    
    
    def list_clusters(
        project_id: str, zone: str, private_cloud_name: str
    ) -> Iterable[vmwareengine_v1.Cluster]:
        """
        Retrieves a list of clusters in private cloud.
    
        Args:
            project_id: name of the project hosting the private cloud.
            zone: zone in which the private cloud is located.
            private_cloud_name: name of the cloud of which you want to list cluster.
    
        Returns:
            An iterable collection of Cluster objects.
        """
        client = vmwareengine_v1.VmwareEngineClient()
        return client.list_clusters(
            parent=f"projects/{project_id}/locations/{zone}/privateClouds/{private_cloud_name}"
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlecloudvmwareengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
