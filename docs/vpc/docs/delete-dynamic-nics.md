---
url: https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics/
title: Delete Dynamic Network Interfaces from an instance \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:12.598051+00:00
---

# Delete Dynamic Network Interfaces from an instance  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete Dynamic Network Interfaces from an instance

This page describes how to delete a Dynamic Network Interface (NIC) from an existing Compute Engine instance.

For an overview of multiple network interfaces, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

To view an instance's existing network interfaces, see [View network interfaces for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties#view_network_interfaces_for_an_instance).

## Delete a Dynamic NIC from an instance

This section describes how to delete a Dynamic NIC from an instance.

To prevent a possible [error when deleting a Dynamic NIC by instance update](https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces#instance-update-dynamic-nic), don't delete Dynamic NICs from individual instances by updating instance properties.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance for which you want to delete a Dynamic NIC.

  3. On the instance details page, click **Edit**.

  4. In the **Dynamic Network Interfaces** section, locate the Dynamic NIC that you want to delete.

  5. To delete the Dynamic NIC, click delete**Delete**.

  6. To save your configuration, click **Save**.




###  gcloud 

To delete a Dynamic NIC from an existing instance, use the [`instances network-interfaces delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/delete).
    
    
    gcloud compute instances network-interfaces delete INSTANCE_NAME \
        --zone=ZONE \
        --network-interface=DYNAMIC_NIC_NAME
    
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to create
  * `ZONE`: the zone of the instance
  * `DYNAMIC_NIC_NAME`: the name of the Dynamic NIC to delete, such as `nic0.2`



###  API 

To delete a Dynamic NIC from an existing instance, use the [`instances.deleteNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/deleteNetworkInterface).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/deleteNetworkInterface?networkInterfaceName=DYNAMIC_NIC_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance
  * `ZONE`: the zone that contains the instance
  * `INSTANCE_NAME`: the name of the instance to delete the Dynamic NIC from
  * `DYNAMIC_NIC_NAME`: the name of the Dynamic NIC to delete, such as `nic0.2`



## Delete a Dynamic NIC from instances in a MIG

This section describes how to delete a Dynamic NIC from instances in a MIG by creating a new instance template and applying the configuration to the MIG. Updating an existing instance template is not supported.

For more information about creating instance templates, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). To view an existing instance template, see [Get, list, and delete instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates).

###  Console 

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click the instance template that you want to copy and update.

  3. Click **Create similar**.

  4. Expand the **Advanced options** section, and then expand the **Networking** section.

  5. In the **Dynamic Network Interfaces** section, locate the Dynamic NIC that you want to delete.

  6. To delete the Dynamic NIC, click delete**Delete**.

  7. To create the instance template, click **Create**.

  8. To update or recreate your instances with the new instance template, see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).




###  gcloud 

  1. To create a new instance template that deletes a Dynamic NIC, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

Include the `--network-interface` flag for each network interface from your existing instance template, except for the Dynamic NIC that you want to delete.

Adjust the following example to specify network interfaces and other properties as needed. For more examples of how to create instances with multiple network interfaces, see [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
            --network-interface=network=NETWORK_A,subnet=SUBNET_A \
            [--network-interface=network=NETWORK_B,subnet=SUBNET_B[,vlan=VLAN_ID]]
         

Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: a name for the new instance template.
     * `NETWORK_A`, `NETWORK_B`: the network where the interface attaches.
     * `SUBNET_A`, `SUBNET_B`: the subnet where the interface attaches.
     * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC in the command.
  2. To update or recreate your instances with the new instance template, see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).




###  API 

  1. To create a new instance template that deletes a Dynamic NIC, use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) to create a global instance template or the [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert) to create a regional instance template.

In the `networkInterfaces` field, include each network interface from your existing instance template, except for the Dynamic NIC that you want to delete.

Adjust the following example to specify network interfaces and other properties as needed. For more examples of how to create instances with multiple network interfaces, see [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
         {
            ....
         
            "networkInterfaces": [
              {
                "subnetwork": "regions/REGION/subnetworks/SUBNET_A"
              },
              {
                "subnetwork": "regions/REGION/subnetworks/SUBNET_B",
                "vlan": "VLAN_ID"
              },
              additional network interfaces...
            ],
            other instance settings...
          }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the instance template.
     * `REGION`: the region that contains the instances.
     * `SUBNET_A,SUBNET_B`: the subnet where each network interface is located.
     * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC the request.
  2. To update or recreate your instances with the new instance template, see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
