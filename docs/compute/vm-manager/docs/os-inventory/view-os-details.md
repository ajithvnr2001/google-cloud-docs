---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details/
title: View OS inventory data \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:18.463723+00:00
---

# View OS inventory data  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  View OS inventory data Stay organized with collections  Save and categorize content based on your preferences. 

## Supported operating systems

For the full list of operating systems and versions that support OS inventory management, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

## Required roles and permissions

To get the permissions that you need to list and describe inventory data, ask your administrator to grant you the OS Inventory Viewer(`roles/osconfig.inventoryViewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your VM

Before you can use OS inventory management, you need to configure your VMs to use the feature. To configure your VMs to use OS inventory management, [set up VM Manager](https://docs.cloud.google.com/compute/docs/manage-os).

After setting up VM Manager on your VMs, you can then view OS inventory data and vulnerability reports.

### Configure the OS inventory scan interval

By default, the OS Config agent runs an inventory scan on each VM every 10 minutes. If your VMs experience high CPU or resource usage due to frequent scanning, or if you need a different schedule for operation reasons, you can adjust the scan frequency by setting the `osconfig-poll-interval` metadata key.

You specify the `osconfig-poll-interval` value in minutes. For example, to run an inventory scan once every hour, set `osconfig-poll-interval` to `60`. To run a scan once every 24 hours, set the value to `1440`.

To configure the `osconfig-poll-interval` metadata value, do the following:

###  Console 

You can apply the metadata value to your projects or VMs using one of the following methods:

  * **Set project-wide metadata to apply the setting to all VMs in your project** :

    1. In the Google Cloud console, go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/compute/metadata)

    2. Click **Edit**.

    3. Add the following metadata entry:

Key: `osconfig-poll-interval`  
Value: INTERVAL_IN_MINUTES

    4. Click **Save**.

  * **Set instance-level metadata when creating a VM** :

    1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

    2. Specify the VM details.

    3. Expand the **Advanced options** section, and do the following:

       1. Expand the **Management** section.
       2. In the **Metadata** section, click **Add item** and add the following metadata entry:

Key: `osconfig-poll-interval`  
Value: INTERVAL_IN_MINUTES

    4. To create the VM, click **Create**.

  * **Set metadata on an existing VM** :

    1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

    2. Click the name of the VM for which you want to set the metadata value.

    3. On the **Instance details** page, click **Edit**.

    4. Under **Metadata** , click **Add item** and then add the following metadata entry:

Key: `osconfig-poll-interval`  
Value: INTERVAL_IN_MINUTES

    5. Click **Save**.




Replace `INTERVAL_IN_MINUTES` with the scan interval in minutes. For example, specify `60` for a scan interval of one hour.

###  gcloud 

Use the [`project-info add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) or the [`instances add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) command with the `--metadata=osconfig-poll-interval=INTERVAL_IN_MINUTES` flag.

You can apply the metadata value to your projects or VMs using one of the following methods:

  * **Set project-wide metadata to apply the setting to all VMs in your project** :
        
        gcloud compute project-info add-metadata \
          --project PROJECT_ID \
          --metadata=osconfig-poll-interval=INTERVAL_IN_MINUTES
        

  * **Set instance-level metadata when creating a VM** :
        
        gcloud compute instances create INSTANCE_NAME \
          --project PROJECT_ID \
          --metadata=enable-osconfig=TRUE,osconfig-poll-interval=INTERVAL_IN_MINUTES
        

  * **Set metadata on an existing VM** :
        
        gcloud compute instances add-metadata INSTANCE_NAME \
          --project PROJECT_ID \
          --metadata=osconfig-poll-interval=INTERVAL_IN_MINUTES
        




Replace the following:

  * `PROJECT_ID`: your project ID
  * `INSTANCE_NAME`: the name of your VM instance
  * `INTERVAL_IN_MINUTES`: the scan interval in minutes. For example, specify `60` for a scan interval of one hour.



## View OS inventory data

  * To view OS inventory data, use one of the following methods:

    * Use the Google Cloud console, gcloud CLI, or OS Config API
    * Use Cloud Asset Inventory



### View OS inventory data for a VM

You can use the Google Cloud console, gcloud CLI or OS Config API to view OS information for a specific VM.

###  Console 

To view OS vulnerabilities and information about installed packages on a VM by using the Google Cloud console, perform the following steps:

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance for which you want to view the OS information. The **Instance details** page appears.
  3. Click the **OS info** tab.  
To view OS inventory data, you must enable VM Manager. If Google Cloud console prompts you to enable VM Manager, select one of the following options: 
     * **Enable for current project** : enables VM Manager for all VMs in the selected project
     * **Enable for this VM** : enables VM Manager only for the selected VM
  4. Review the list of OS vulnerabilities and installed packages in the **OS info** tab.
  5. Optional: If updates are available for any of the installed packages, then select the package names and click **Apply updates**.  
The **Patch** page appears. For more information about using the Patch feature in VM Manager, see [Create patch jobs](https://docs.cloud.google.com/compute/docs/os-patch-management/create-patch-job).



###  gcloud 

To view inventory details for a specific VM, run the [`os-config inventories describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe):
    
    
    gcloud compute os-config inventories describe INSTANCE_NAME \
        --location=ZONE \
        --view=VIEW
    

Replace the following:

  * `INSTANCE_NAME`: the name for your VM
  * `ZONE`: the zone where the VM instance is located
  * `VIEW`: the type of output information that is required. The following view types are available:

    * `basic`: displays only OS information
    * `full`: displays information about both OS and packages

If unspecified, the default is `basic`.

**Example (basic view)**
    
    gcloud compute os-config inventories describe vm1-centos \
       --location=us-central1-c
    

#### Example output
    
    architecture: x86_64
    hostname: vm1-centos
    kernelRelease: 3.10.0-1160.92.1.el7.x86_64
    kernelVersion: '#1 SMP Tue Jun 20 11:48:01 UTC 2023'
    longName: CentOS Linux 7 (Core)
    osconfigAgentVersion: 20230504.00-g1.el7
    shortName: centos
    updateTime: '2023-07-26T17:03:50Z'
    version: '7'
    

**Example (full view)**
    
    gcloud compute os-config inventories describe vm1-centos \
       --location=us-central1-c \
       --view=full
    

#### Linux example output
    
    ┌─────────────────────────────────────────────────────────────────────────────────────┐
    │                               Installed Packages (Yum)                              │
    ├─────────────────────────────────────┬──────────────┬────────────────────────────────┤
    │             PACKAGE_NAME            │ ARCHITECTURE │            VERSION             │
    ├─────────────────────────────────────┼──────────────┼────────────────────────────────┤
    │ GeoIP                               │ x86_64       │ 1.5.0-13.el7                   │
    │ NetworkManager                      │ x86_64       │ 1:1.12.0-8.el7_6               │
    │ NetworkManager-libnm                │ x86_64       │ 1:1.12.0-8.el7_6               │
    │ NetworkManager-team                 │ x86_64       │ 1:1.12.0-8.el7_6               │
    │ NetworkManager-tui                  │ x86_64       │ 1:1.12.0-8.el7_6               │
    │ acl                                 │ x86_64       │ 2.2.51-14.el7                  │
    │ yum-cron                            │ all          │ 3.4.3-161.el7.centos           │
    │ yum-metadata-parser                 │ x86_64       │ 1.1.4-10.el7                   │
    │ yum-plugin-fastestmirror            │ all          │ 1.1.31-50.el7                  │
    │ zlib                                │ x86_64       │ 1.2.7-18.el7                   │
    └─────────────────────────────────────┴──────────────┴────────────────────────────────┘
    ┌───────────────────────────────────────────────────────────────────────────────┐
    │                        Package Updates Available (Yum)                        │
    ├───────────────────────────────┬──────────────┬────────────────────────────────┤
    │          PACKAGE_NAME         │ ARCHITECTURE │            VERSION             │
    ├───────────────────────────────┼──────────────┼────────────────────────────────┤
    │ GeoIP                         │ x86_64       │ 1.5.0-14.el7                   │
    │ NetworkManager                │ x86_64       │ 1:1.18.8-2.el7_9               │
    │ NetworkManager-libnm          │ x86_64       │ 1:1.18.8-2.el7_9               │
    │ NetworkManager-team           │ x86_64       │ 1:1.18.8-2.el7_9               │
    │ yum-cron                      │ all          │ 3.4.3-168.el7.centos           │
    │ yum-plugin-fastestmirror      │ all          │ 1.1.31-54.el7_8                │
    │ zlib                          │ x86_64       │ 1.2.7-19.el7_9                 │
    └───────────────────────────────┴──────────────┴────────────────────────────────┘
    architecture: x86_64
    hostname: vm1-centos
    kernelRelease: 3.10.0-957.1.3.el7.x86_64
    kernelVersion: '#1 SMP Thu Nov 29 14:49:43 UTC 2018'
    longName: CentOS Linux 7 (Core)
    osconfigAgentVersion: 20230504.00-g1.el7
    shortName: centos
    updateTime: '2021-05-11T22:21:52.323Z'
    version: '7'
    

#### Windows example output
    
    ┌───────────────────────────────────────────────────────────┐
    │                Installed Packages (GooGet)                │
    ├───────────────────────┬──────────────┬────────────────────┤
    │      PACKAGE_NAME     │ ARCHITECTURE │      VERSION       │
    ├───────────────────────┼──────────────┼────────────────────┤
    │ google-osconfig-agent │ x86_64       │ 20210415.4.0+win@1 │
    └───────────────────────┴──────────────┴────────────────────┘
    ┌───────────────────────────────────────────────────┐
    │     Installed Packages (Windows Update Agent)     │
    ├───────┬────────────┬────────────────┬─────────────┤
    │ TITLE │ CATEGORIES │ KB_ARTICLE_IDS │ SUPPORT_URL │
    ├───────┼────────────┼────────────────┼─────────────┤
    │ title │ C1, C2     │ 4589208        │ url.com     │
    └───────┴────────────┴────────────────┴─────────────┘
    ┌───────────────────────────────────────────────────────────────┐
    │           Installed Packages (Quick Fix Engineering)          │
    ├─────────┬─────────────────┬────────────┬──────────────────────┤
    │ CAPTION │   DESCRIPTION   │ HOT_FIX_ID │     INSTALL_TIME     │
    ├─────────┼─────────────────┼────────────┼──────────────────────┤
    │ caption │ Security Update │ KB4470788  │ 2019-03-12T00:00:00Z │
    └─────────┴─────────────────┴────────────┴──────────────────────┘
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                  Installed Packages (Windows Application)                 │
    ├──────────────────┬─────────────────┬───────────────────────┬──────────────┤
    │   DISPLAY_NAME   │ DISPLAY_VERSION │       PUBLISHER       │ INSTALL_DATE │
    ├──────────────────┼─────────────────┼───────────────────────┼──────────────┤
    │ PowerShell 7-x64 │ 7.0.2.0         │ Microsoft Corporation │ 2021-06-08   │
    └──────────────────┴─────────────────┴───────────────────────┴──────────────┘
    ┌───────────────────────────────────────────────────────────┐
    │             Package Updates Available (GooGet)            │
    ├───────────────────────┬──────────────┬────────────────────┤
    │      PACKAGE_NAME     │ ARCHITECTURE │      VERSION       │
    ├───────────────────────┼──────────────┼────────────────────┤
    │ google-osconfig-agent │ x86_64       │ 20210415.4.0+win@1 │
    └───────────────────────┴──────────────┴────────────────────┘
    ┌───────────────────────────────────────────────────┐
    │  Package Updates Available (Windows Update Agent) │
    ├───────┬────────────┬────────────────┬─────────────┤
    │ TITLE │ CATEGORIES │ KB_ARTICLE_IDS │ SUPPORT_URL │
    ├───────┼────────────┼────────────────┼─────────────┤
    │ title │ C1, C2     │ 4589208        │ url.com     │
    └───────┴────────────┴────────────────┴─────────────┘
    ┌───────────────────────────────────────────────────────────────┐
    │       Package Updates Available (Quick Fix Engineering)       │
    ├─────────┬─────────────────┬────────────┬──────────────────────┤
    │ CAPTION │   DESCRIPTION   │ HOT_FIX_ID │     INSTALL_TIME     │
    ├─────────┼─────────────────┼────────────┼──────────────────────┤
    │ caption │ Security Update │ KB4470788  │ 2019-03-12T00:00:00Z │
    └─────────┴─────────────────┴────────────┴──────────────────────┘
    architecture: x86_64
    hostname: vm3-windows
    kernelRelease: 10.0.17763.1817
    kernelVersion: 10.0.17763.1817 (WinBuild.160101.0800)
    longName: Microsoft Windows Server 2019 Datacenter
    osconfigAgentVersion: 20210901.00.0+win@1
    shortName: windows
    updateTime: '2021-09-12T22:14:35Z'
    version: 10.0.17763
    




###  REST 

To view inventory details for a specific VM, create a `GET` request to the [`projects.locations.instances.inventories.get` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.inventories/get).
    
    
       GET https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE/inventory
       

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where the VM instance is located
  * `INSTANCE`: specify either the instance ID or the name for your VM



### View OS inventory data for VMs in a specific zone

You can use gcloud CLI or OS Config API to view the OS information for VMs in a specific zone.

###  gcloud 

To view a list of inventory data for VMs in a specific zone, run the [`os-config inventories list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/list).
    
    
    gcloud compute os-config inventories list \
        --location=ZONE \
        --view=VIEW
    

Replace the following:

  * `ZONE`: the zone where the VM is located
  * `VIEW`: the type of output information that is required. The following view types are available:

    * `basic`: displays only OS information
    * `full`: displays information about both OS and packages

If unspecified, the default is `basic`.

**Example (basic view)**
    
    gcloud compute os-config inventories list \
       --location=us-central1-c
    

The output is similar to the following:
    
    INSTANCE_ID          INSTANCE_NAME     OS                                         OSCONFIG_AGENT_VERSION       UPDATE_TIME
    29255009728795105    vm1-centos        CentOS Linux 7 (Core)                      20230504.00-g1.el7           2023-07-26T16:53:49Z
    5138980234596718741  vm2-rhel8         Red Hat Enterprise Linux 8.8 (Ootpa)       20230504.00-g1.el8           2023-07-26T16:55:33Z
    7127836223366142250  vm3-windows       Microsoft Windows Server 2022 Datacenter   20230403.00.0+win@1          2023-07-26T16:49:16Z
    

**Example (full view)**
    
    gcloud compute os-config inventories list \
       --location=us-central1-c \
       --view=full
    

The output is similar to the following:
    
    INSTANCE_ID          INSTANCE_NAME     OS                                       INSTALLED_PACKAGES   AVAILABLE_PACKAGES  OSCONFIG_AGENT_VERSION       UPDATE_TIME
    29255009728795105    vm1-centos        CentOS Linux 7 (Core)                    334                    2                 20230504.00-g1.el7           2023-07-26T16:53:49Z
    5932621394110773366  vm2-rhel8         Red Hat Enterprise Linux 8.8 (Ootpa)     410                  138                 20230504.00-g1.el8           2023-07-26T16:55:33Z
    7127836223366142250  vm3-windows       Microsoft Windows Server 2022 Datacenter  36                    6                 20230403.00.0+win@1          2023-07-26T16:49:16Z
    




###  REST 

To view a list of inventory data for VMs in a specific zone, create a `GET` request to the [`projects.locations.instances.inventories.list` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.inventories/list).
    
    
       GET https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/-/inventories
       

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where the VMs are located



### View OS inventory data from Cloud Asset Inventory

OS inventory management stores and forwards inventory and vulnerability report data to [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). Cloud Asset Inventory is a metadata inventory service that allows you to view, monitor, and analyze assets across Google Cloud. From Cloud Asset Inventory, you can poll the information and view changes in the data.

To access OS inventory and vulnerability report data from Cloud Asset Inventory, you need to complete the following setup:

  * Set up [VM Manager](https://docs.cloud.google.com/compute/docs/manage-os#overview).
  * On your Google Cloud project, enable the [Cloud Asset Inventory API, the Google Cloud CLI, and assign permissions](https://docs.cloud.google.com/asset-inventory/docs/export-asset-metadata).



For more information, see [Viewing VM Manager data](https://docs.cloud.google.com/asset-inventory/docs/vm-runtime-info).

## OS inventory management (earlier version)

If you are still using the earlier version of OS inventory management, expand the following section to review the instructions for the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).

#### OS inventory management (earlier version)

**List VMs**

To view the list of VMs that have OS inventory management set up, run the [`instances os-inventory list-instances`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances) command.

For example, to list all the VMs that have inventory data, run the following command:
    
    
    gcloud compute instances os-inventory list-instances

The output is similar to the following:
    
    
      NAME                 ZONE          MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP STATUS
      inventory-instance   us-east1-b    e2-standard-2               192.0.2.1    RUNNING
      instance-inventory1  us-west1-b    e2-standard-2               192.0.2.2    RUNNING
      instance-inventory2  asia-east2-b  e2-standard-2               192.0.2.3    RUNNING
      

You can also use filters to narrow down your results. For example, you can list all VMs that have OS inventory management set up and whose hostname matches the regular expression `instance-*` by running the following command:
    
    
    gcloud compute instances os-inventory list-instances
          --inventory-filter="Hostname~instance-*"

The output is similar to the following:
    
    
      NAME                 ZONE         MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP STATUS
      inventory-instance   us-east1-b   e2-standard-2               192.0.2.1    RUNNING
      instance-inventory1  us-west1-b   e2-standard-2               192.0.2.2    RUNNING
      instance-inventory2  asia-east2-b e2-standard-2               192.0.2.3    RUNNING
      

**View inventory data**

To view the inventory data for your VM, use the [`instances os-inventory describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/describe) command.

To view the inventory data collected for a VM, run the following command:
    
    
    gcloud compute instances os-inventory describe INSTANCE_NAME \
          --zone=ZONE

Replace the following:

  * `INSTANCE_NAME`: the name of your VM
  * `ZONE`: the zone where the VM is located



To view the types of output details that are returned, review [Information provided by OS inventory management](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected).

## What's next

  * [View vulnerability reports for your operating systems](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/vulnerability-reports).
  * Learn more about [OS inventory management](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
