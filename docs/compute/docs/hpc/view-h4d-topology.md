---
url: https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology/
title: View H4D cluster topology \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:58.041242+00:00
---

# View H4D cluster topology  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View H4D cluster topology Stay organized with collections  Save and categorize content based on your preferences. 

After you [create an H4D cluster on reserved blocks of capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity), you can view the physical arrangement of the VMs that make up the cluster. Understanding the arrangement of your VMs, lets you do the following:

  * Adjust your application or workload design to further minimize network latency, especially for workloads leveraging Cloud RDMA.
  * Troubleshoot network latency or performance issues of VMs that communicate frequently.



## Before you begin

Make sure you have the necessary permissions to view VM topology information.

### Required roles

To get the permissions that you need to view VMs topology, ask your administrator to grant you the [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

This predefined role contains all permissions required to view VMs topology. To see the exact permissions that are required, expand the **Required permissions** section:

The following permissions are required to view VMs topology:

  * To view the details of a VM: `compute.instances.get` on the project
  * To view a list of VMs: `compute.instances.list` on the project



## Understand VMs topology

When you view the details of a running VM, you can retrieve information about its physical location within a cluster by checking the **Physical host** field (for the Google Cloud console), or the `physicalHostTopology` field (for the Google Cloud CLI), Compute Engine API, or by querying the metadata key. These fields contain the following sub-fields:

  * **`cluster`** : the global name of the cluster.
  * **`block`** : the organization-specific ID of the reserved block where the VM is located.
  * **`sub-block`** : the organization-specific ID of the sub-block where the VM is located.
  * **`host`** : the organization-specific ID of the host where the VM runs on.



For definitions of these terms, see [Cluster terminology](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#cluster_terminology).

To understand how close the VMs are to each other, compare the values of the **Physical host** or `physicalHostTopology` fields between VMs. The more sub-fields the VMs share, the closer they are physically located.

You can also view the topology of a reservation in which the VMs are created. The `physicalHostTopology` fields of a reservation and a VM show the same `block` and `cluster` fields. When you view a specific reserved block, you can view the name and sub-block of all the VMs that are deployed in the block. For more information about the topology of a reservation, see [View the topology of a reservation](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-capacity-topology).

## View VMs topology

To view the physical location of multiple running VMs, select any of the following options:

### Console

  * In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  * In the **Name** column, click the name of the VM to view its details. A page that gives the VM details appears. The **Details** tab is selected by default.

  * In the **Basic information** section, check the value of the **Physical host** field.




###  Google Cloud CLI 

To view the physical location of a running VM, use the [`gcloud compute instances describe`](https://cloud.google.com/sdk/gcloud/reference/compute/instances/describe) command with the `flatten=resourceStatus.physicalHostTopology`.

Replace the following:

  * `VM_NAME`: the VM name.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the VM exists.



The output is similar to the following:
    
    
    ---
    cluster: europe-west1-cluster-jfhb
    block: 3e3056e23cf91a5cb4a8621b6a52c100
    subBlock: 0fc09525cbd5abd734342893ca1c083f
    host: 1215168a4ecdfb434fd4d28056589059
    

###  REST 

To view the physical location of your running VMs, make one of the following `GET` requests. When you make a request, you must include the `fields` query parameter and specify to only show the `name`, `machineType`, and `physicalHostTopology` fields of a VM. You must also include the `filter` query parameter and specify to only list running VMs.

  * To view a list of your VMs across all zones: [`instances.aggregatedList`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList) method.


    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
    

  * To view a list of your VMs in a specific zone: [`instances.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list) method.


    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
    

Replace the following: * `PROJECT_ID`: the ID of the project where the VMs exist. * `ZONE`: the zone where the VMs exist.

The output is similar to the following:
    
    
    {
      "items": [
        {
          "name": "vm-01",
          "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/machineTypes/h4d-highmem-192-lssd",
          "resourceStatus": {
            "physicalHostTopology": {
              "cluster": "europe-west4-cluster-jfhb",
              "block": "3e3056e23cf91a5cb4a8621b6a52c100",
              "subBlock": "0fc09525cbd5abd734342893ca1c083f",
              "host": "1215168a4ecdfb434fd4d28056589059"
            }
          }
        },
        {
          "name": "vm-02",
          "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/h4d-highmem-192-lssd",
          "resourceStatus": {
            "physicalHostTopology": {
              "cluster": "europe-west4-cluster-jfhb",
              "block": "3e3056e23cf91a5cb4a8621b6a52c100",
              "subBlock": "1fc18636cbd4abd623553784ca2c174e",
              "host": "2326279b5ecdfc545fd5e39167698168"
            }
          }
        },
        ...
      ]
    }
    

If you want to refine your list of VMs, then edit the filter expression in the [`filter`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#body.QUERY_PARAMETERS.filter) query parameter.

## View VMs topology by querying metadata key

To view the physical location of a running VM by querying the `physical_host_topology` metadata key, select one of the following options:

###  Linux VMs 

  1. [Connect to your Linux VM](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).
  2. From your Linux VM, create a query by using the [curl](https://curl.se/) tool. To query the `physical_host_topology` metadata key on Linux VMs, run the following command:


    
    
    curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology
    

The output is similar to the following:
    
    
    {
      "cluster": "europe-west4-cluster-jfhb",
      "block": "3e3056e23cf91a5cb4a8621b6a52c100",
      "subBlock": "1fc18636cbd4abd623553784ca2c174e",
      "host": "2326279b5ecdfc545fd5e39167698168"
    }
    

###  Windows VMs

  1. [Connect to your Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).
  2. From your Windows VM, create a query by using the [Invoke-RestMethod](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod). To query the `physical_host_topology` metadata key on Windows VMs, run the following command:


    
    
    $value = (Invoke-RestMethod `
      -Headers @{'Metadata-Flavor' = 'Google'} `
      -Uri "http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology")
    $value
    
    

The output is similar to the following:
    
    
    {
      "cluster": "europe-west4-cluster-jfhb",
      "block": "3e3056e23cf91a5cb4a8621b6a52c100",
      "subBlock": "1fc18636cbd4abd623553784ca2c174e",
      "host": "2326279b5ecdfc545fd5e39167698168"
    }
    

## What's next

  * [Manage host events across VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d)
  * [Manage host events across reservations](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
