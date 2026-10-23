---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vmware-aria-automation/
title: Configure VMware Aria Automation \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:17.703576+00:00
---

# Configure VMware Aria Automation  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vmware-aria-automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VMware Aria Automation

**Note:** The instructions on this page are for VMware Aria Automation 7.x. If you're using VMware Aria Automation 8.x or later, the configuration process is different and involves deploying a cloud proxy.

You can set up VMware vCenter Server on your Google Cloud VMware Engine private cloud as an endpoint for VMware Aria Automation 7.x.

## Before you begin

Complete the following tasks before configuring vCenter Server:

  * Set up [private services access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access) for connectivity between your on-premises environment and your private cloud.
  * [Configure DNS forwarding of on-premises DNS requests](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises) to the DNS servers for your private cloud.
  * [Elevate your vCenter privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) from VMware Engine portal. 
    * Create a group named `VMware Aria Automation IaaS administrator group`.
    * Create a user named `VMware Aria Automation IaaS administrator user` and add the user to the group created in the previous step. If you [set up vCenter to use Active Directory](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources) and want to use a user from your identity source, add the user to the group.
    * Create a role named `VMware Aria Automation IaaS administrator role` with the set of permissions that are listed in the following table.
    * Apply the `VMware Aria Automation IaaS administrator role` to the `VMware Aria Automation IaaS administrator group` at the vCenter level.

**Attribute value** | **Permission**  
---|---  
Datastore |  Allocate space Browse datastore  
Datastore cluster | Configure a datastore cluster  
Folder |  Create folder Delete folder  
Global |  Manage custom attributes Set custom attribute  
Network | Assign network  
Permissions | Modify permissions  
Resource |  Assign VM to resource pool Migrate powered off VM Migrate powered on VM  
VM inventory |  Create from existing Create new Move Remove  
Virtual machine interaction |  Configure CD media Console interaction Device connection Power off Power on Reset Suspend Tools install  
Virtual machine configuration |  Add existing disk Add new disk Add or remove Remove disk Advanced Change CPU count Change resource Extend virtual disk Disk change tracking Memory Modify device settings Rename Set annotation (version 5.0 and later) Settings Swapfile placement  
Provisioning |  Customize Clone template Clone VM Deploy template Read customization specs  
Virtual machine state |  Create snapshot Remove snapshot Revert to snapshot  
  
## Install VMware Aria Automation in your on-premises environment

Deploy a vSphere Agent for the VMware Aria Automation endpoint.

  1. Sign in to the VMware Aria Automation IaaS server appliance as `VMware Aria Automation IaaS administrator user`.
  2. Go to `https://vra-url:5480/installer`, where `vra-url` is the URL that you use to access the VMware Aria Automation administration UI.
  3. Click **IaaS Installer** to download the installer. The naming convention for the installer file is `setup_vra-url@5480.exe`.
  4. Run the installer. On the **Welcome** screen, click **Next**.
  5. Accept the EULA and click **Next**.
  6. Provide the sign-in information, click **Accept Certificate** , and then click **Next**.
  7. Select **Custom Install** and **Proxy Agents** , and click **Next**.
  8. Enter the IaaS server sign-in information and click **Next**. If you are using Active Directory, enter the username in **domain\user** format. Otherwise, use **user@domain** format.
  9. For the proxy settings, enter **vSphere** for **Agent type**. Enter a name for the agent.
  10. Enter the IaaS server FQDN in the **Manager Service Host** and the **Model Manager Web Service Host** fields.
  11. Click **Test** to test the connection for each of the FQDN values. If the test fails, modify your DNS settings so that the IaaS server hostname is resolved.
  12. Enter a name for the vCenter server endpoint for the private cloud. Record the name for use later in the configuration process.
  13. Click **Next**.
  14. Click **Install**.



## Configure the vSphere agent

  1. Go to `https://vra-url/vcac` and sign in as **ConfigurationAdmin**.
  2. Select **Infrastructure > Endpoints > Endpoints**.
  3. Select **New > Virtual > vSphere**.
  4. Enter the vSphere endpoint name that you specified in the previous procedure.
  5. For **Address** , enter the private cloud vCenter Server URL in the format `https://vcenter-fqdn/sdk`, where `vcenter-fqdn` is the name of the vCenter server.
  6. Enter the credentials for the VMware Aria Automation IaaS administrator user that Cloud Customer Care created for you.
  7. Click **Test Connection** to validate the user credentials. If the test fails, verify the URL, account information, and endpoint name and test again.
  8. After a successful test, click **OK** to create the vSphere endpoint.



### Verify the endpoint name

To identify the correct vCenter server endpoint name, do the following:

  1. Open a command prompt on the IaaS appliance.
  2. Change the directory to `C:\Program Files (x86)\VMware\vCAC\Agents<var>AGENT_NAME`, replacing `AGENT_NAME` with the name you assigned to the vCenter server endpoint.
  3. Run the following command.
         
         ..\..\Server\DynamicOps.Vrm.VRMencrypt.exe VRMAgent.exe.config get
         




The output is similar to the following. The value of the `managementEndpointName` field is the endpoint name.

`managementEndpointName: cslab1pc3-vc`   
`doDeletes: true`

## What's next

  * Learn about [elevating privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) on your private cloud.
  * [Contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/support) to create a VMware Aria Automation IaaS administrator user.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
