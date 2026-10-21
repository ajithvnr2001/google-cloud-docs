---
url: https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network/
title: Change the MTU setting of a VPC network \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:18.544345+00:00
---

# Change the MTU setting of a VPC network  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change the MTU setting of a VPC network

In Google Cloud, you set the MTU for each VPC network. Compute Engine instances that use that network must be configured to use the same MTU setting for their interfaces.

  * Linux instances based on [public OS images](https://docs.cloud.google.com/compute/docs/images/os-details) receive the VPC network's MTU setting from the DHCP server. DHCP Option 26 contains the MTU setting.

  * Windows instances don't use DHCP to configure the MTU setting. If you change the MTU of a VPC network, you must change the MTU setting of the instance.




For more information, see [Compute instances and MTU settings](https://docs.cloud.google.com/vpc/docs/mtu#vms_and_mtu_settings).

There are two ways to start using a VPC network with a different MTU setting:

  * You can change the MTU setting of an existing VPC network, which requires that you stop all instances in the network at the same time.

  * You can create a new VPC network with a different MTU setting, and migrate the instances to it.




## Before you begin

  * Make sure that you understand the effects of changing a VPC network MTU. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  * Prepare for stopping and restarting all compute instances that are connected to the VPC network, for example, by identifying a maintenance window.



## Change the MTU setting of a VPC network

To update a VPC network MTU, do the following:

  * Stop all compute instances.

To avoid connectivity issues, you must _stop_ the instances. Don't _reboot_ the instances.

  * Change the VPC network MTU.

  * Start all compute instances.

  * Update Windows instances.




### Stop all compute instances

You can stop multiple compute instances simultaneously by using the Google Cloud console. To display all instances in a given network, on the [Compute Engine VM instances page](https://console.cloud.google.com/compute/instances) use the filter bar to filter by the **Network** property, and then select your network.

You can stop multiple instances that are in the same zone simultaneously by using the gcloud CLI.

For more information about stopping instances, including considerations for instances with local SSDs, see [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

### Update the network MTU

Ensure that you have stopped all compute instances before you change the VPC network MTU.

**Caution:** Changing the VPC network MTU without first stopping all connected instances can cause connectivity issues.

###  Console 

Updating network MTU is not supported in the Google Cloud console. See the Google Cloud CLI or API instructions.

###  gcloud 

Update network MTU by using the [`gcloud compute networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update).
    
    
    gcloud compute networks update NETWORK \
        --mtu=MTU
    

Replace the following:

  * `NETWORK`: the name of the VPC network whose MTU you want to change.
  * `MTU`: the network MTU to configure. Can be any value between `1300` and `8896`. Common values are `1460` (default), `1500`, and `8896` (maximum).



###  API 

Change the MTU of an existing VPC network.
    
    
    PATCH https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK
    {
      "mtu": MTU
    }
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the VPC network to modify.
  * NETWORK: the name of the VPC network to modify.
  * `MTU`: the network MTU to configure. Can be any value between `1300` and `8896`. Common values are `1460` (default), `1500`, and `8896` (maximum).



For more information, see the [`networks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/patch).

### Start compute instances

You can start multiple compute instances simultaneously by using the Google Cloud console. To display all instances in a given network, use the filter bar to filter by the **Network** property, and then select your network.

You can start multiple instances that are in the same zone simultaneously by using the gcloud CLI.

For more information about starting instances, see [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

### Change the MTU setting of Windows instances

Windows instances based on [public OS images](https://docs.cloud.google.com/compute/docs/images/os-details) are configured with a fixed MTU of `1460`. Custom Windows instances might have different MTU settings.

To set Windows instances to use a different MTU, do the following on each instance:

###  Command prompt 

  1. Open Command Prompt (cmd.exe) as Administrator.
  2. Run the following command to determine the index of the interface that you want to update:
         
         netsh interface ipv4 show interface 

  3. Update the interface:
         
         netsh interface ipv4 set interface INTERFACE_INDEX mtu=MTU store=persistent 

  4. Update the device driver configuration:

     1. Open the Device Manager with following command: 
            
            devmgmt.msc
            

     2. Expand the **Network adapters** category.
     3. Right-click the **Google VirtIO Ethernet Adapter** /**Google Ethernet Adapter** device.
     4. Select **Properties**.
     5. Click the **Advanced** tab.
     6. In the **Init.MTUSize** field, enter the MTU setting.
     7. Click **OK**.

The instance briefly loses connectivity, because the driver automatically restarts when the registry entries change.




###  PowerShell 

  1. Open PowerShell as Administrator.
  2. Run the following command:
         
         Set-NetIPInterface -InterfaceAlias INTERFACE_NAME -AddressFamily IPv4 -NlMtu MTU 

  3. Run the following command to update device driver settings:
         
         Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword MTU -RegistryValue MTU 

The instance briefly loses connectivity, because the driver automatically restarts when the registry entries change.




## Migrate compute instances to a different MTU network

You might decide to migrate your services to new compute instances in a new network rather than changing the MTU of your existing network. In such a case, you might have a server, such as a database server, that needs to be accessible to all instances during the migration. If so, the following general approach might help you migrate cleanly:

  1. [Create the new network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) with the new MTU.
  2. Create any necessary firewall rules and routes in the new network.
  3. [Create a VM with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#creating_virtual_machine_instances_with_multiple_network_interfaces) in the old network. One interface connects to the new network using the new MTU and the other connects to the old network using the old MTU.
  4. Configure this new instance as a secondary server for the existing one.
  5. Fail the primary server over to the secondary one.
  6. Either [Migrate VMs to the new network](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks) or create new instances in the new network. If you create new instances, you can create them from scratch, from an existing image, or by [creating a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of the existing instances and using that to populate the new persistent disks.
  7. Configure these instances to use the operational server in that network.
  8. Migrate traffic to the new instances.
  9. If you intend to delete the old network, create a new server in the new network, get it in sync with the existing server, and fail over to it.
  10. Delete the old server and old network.



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how VPC performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try VPC free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
