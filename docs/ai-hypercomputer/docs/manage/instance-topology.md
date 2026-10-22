---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology/
title: View topology of a compute instance \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:19.357663+00:00
---

# View topology of a compute instance  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  View topology of a compute instance Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to view the physical location, also known as _topology_ , of your Compute Engine instances in a zone. To view the topology of a cluster in Cluster Director, see [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology).

After you create A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instances or compute instances that specify a compact placement policy or a workload policy, you can view the physical location of your compute instances in relation to each other. When you know the proximity of your compute instances, you can adjust your application or workload design to run latency-sensitive jobs on the compute instances that are closest to each other. For all other types of compute instances, you can see the ID of the host that they run on after you [expose the host ID](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#expose-host-id).

**Note:** If you created your A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instances in a reservation, then you can view the topology of your reserved resources. For example, when you view the details of a single reserved block, you can view the name and sub-block for all the compute instances that run in the block. For more information about the topology of a reservation, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

## Before you begin

  * Review the [terminology](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology) for compute instance topology.
  * Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to view compute instance topology, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view compute instance topology. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view compute instance topology:

  * To view the details of a compute instance: `compute.instances.get` on the project 
  * To view a list of compute instances: `compute.instances.list` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Understand compute instance topology

To understand the physical location of a compute instance in a cluster, check the **Physical host** field in the Google Cloud console. If you use the gcloud CLI, the Compute Engine API, or a metadata key query, check the `physicalHostTopology` field. These fields contain the following sub-fields:

  * **`cluster`** : the global name of the cluster.

  * **`block`** : the organization-specific ID of the reserved block where the instance is located.

  * **`sub-block`** : the organization-specific ID of the sub-block where the instance is located.

  * **`host`** : the organization-specific ID of the host where the instance runs on.




To understand instance proximity, compare the values of the **Physical host** or `physicalHostTopology` fields between compute instances. The more sub-fields the compute instances share, the closer they are to each other.

You can also view the topology of a reservation in which the compute instances are created. The `physicalHostTopology` fields of a reservation and an instance show the same `block` and `cluster` fields. For example, when you view a specific reserved block, you can view the name and sub-block of all the compute instances that are deployed in the block. For more information about the topology of a reservation, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

## View compute instance topology

To view the physical location of multiple running compute instances at once, use the REST API. Otherwise, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the compute instance that you want to view the details of. A page that gives the details of the compute instance appears and the **Details** tab is selected.

  3. In the **Basic information** section, check the value of the **Physical host** field.




###  gcloud 

To view the physical location of a running compute instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with the `--flatten=resourceStatus.physicalHostTopology` flag:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --flatten=resourceStatus.physicalHostTopology \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `ZONE`: the zone where the compute instance exists.




The output is similar to the following:

  * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
        
        ---
        cluster: europe-west1-cluster-jfhb
        block: 3e3056e23cf91a5cb4a8621b6a52c100
        subBlock: 0fc09525cbd5abd734342893ca1c083f
        host: 1215168a4ecdfb434fd4d28056589059
        

  * If you can only view the ID of the host after you expose it, then the output is similar to the following:
        
        ---
        cluster: null
        block: null
        subBlock: null
        host: 1215168a4ecdfb434fd4d28056589059
        




###  REST 

To view the physical location of your running compute instances, make one of the following `GET` requests. When you make a request, you must include the `fields` query parameter and specify to only show the `name`, `machineType`, and `physicalHostTopology` fields of a compute instance. You must also include the `filter` query parameter and specify to only list running compute instances.

  * To view a list of your instances across all zones: [`instances.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList)
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
        

  * To view a list of your instances in a specific zone: [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list)
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the compute instances exist.

  * `ZONE`: the zone where the compute instances exist.




The output is similar to the following:

  * If you can view the ID of the cluster, block, sub-block, and host of your compute instances, then the output is similar to the following:
        
        {
          "items": [
            {
              "name": "vm-01",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "cluster": "europe-west1-cluster-jfhb",
                  "block": "3e3056e23cf91a5cb4a8621b6a52c100",
                  "subBlock": "0fc09525cbd5abd734342893ca1c083f",
                  "host": "1215168a4ecdfb434fd4d28056589059"
                }
              }
            },
            {
              "name": "vm-02",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "cluster": "europe-west1-cluster-jfhb",
                  "block": "3e3056e23cf91a5cb4a8621b6a52c100",
                  "subBlock": "1fc18636cbd4abd623553784ca2c174e",
                  "host": "2326279b5ecdfc545fd5e39167698168"
                }
              }
            },
            ...
          ]
        }
        

  * If you can only view the ID of your compute instances of the host after you expose it, then the output is similar to the following:
        
        {
          "items": [
            {
              "name": "vm-01",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "cluster": null,
                  "block": null,
                  "subBlock": null,
                  "host": "1215168a4ecdfb434fd4d28056589059"
                }
              }
            },
            {
              "name": "vm-02",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "cluster": null,
                  "block": null,
                  "subBlock": null,
                  "host": "2326279b5ecdfc545fd5e39167698168"
                }
              }
            },
            ...
          ]
        }
        




If you want to refine your list of compute instances, then edit the filter expression in the [`filter` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#body.QUERY_PARAMETERS.filter).

## View compute instance topology with a metadata key query

To view the physical location of a running compute instance with a query to the `physical_host_topology` metadata key, select one of the following options:

###  Linux instances 

  1. Connect to your Linux compute instance.

  2. From your Linux instance, create a query by using the [`curl` tool](https://curl.se/). To query the `physical_host_topology` metadata key on Linux instances, run the following command:
         
         user@myinst:~$ curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology
         

The output is similar to the following:

     * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
           
           {
             "cluster": "europe-west1-cluster-jfhb",
             "block": "3e3056e23cf91a5cb4a8621b6a52c100",
             "subBlock": "0fc09525cbd5abd734342893ca1c083f",
             "host": "1215168a4ecdfb434fd4d28056589059"
           }
           

     * If you can only view the ID of the host after you expose it, then the output is similar to the following:
           
           {
             "cluster": null,
             "block": null,
             "subBlock": null,
             "host": "1215168a4ecdfb434fd4d28056589059"
           }
           




###  Windows instances 

  1. Connect to your Windows compute instance.

  2. From your Windows instance, create a query with the [`Invoke-RestMethod` command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod). To query the `physical_host_topology` metadata key on Windows instances, run the following command:
         
         PS C:\> 
         $value = (Invoke-RestMethod `
                 -Headers @{'Metadata-Flavor' = 'Google'} `
                 -Uri "http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology")
         $value
         

The output is similar to the following:

     * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
           
           {
             "cluster": "europe-west1-cluster-jfhb",
             "block": "3e3056e23cf91a5cb4a8621b6a52c100",
             "subBlock": "0fc09525cbd5abd734342893ca1c083f",
             "host": "1215168a4ecdfb434fd4d28056589059"
           }
           

     * If you can only view the ID of the host after you expose it, then the output is similar to the following:
           
           {
             "cluster": null,
             "block": null,
             "subBlock": null,
             "host": "1215168a4ecdfb434fd4d28056589059"
           }
           




## What's next

  * Learn how to manage host events:

    * [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)

    * [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)

  * [Monitor compute instances and clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
