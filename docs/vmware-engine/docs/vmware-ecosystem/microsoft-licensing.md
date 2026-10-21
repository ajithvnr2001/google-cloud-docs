---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/microsoft-licensing/
title: Microsoft licensing options for Windows Server \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:39.702991+00:00
---

# Microsoft licensing options for Windows Server  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/microsoft-licensing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft licensing options for Windows Server

Google Cloud offers multiple options for using Microsoft licenses on Google Cloud VMware Engine. For details about licensing for SQL Server, see [Microsoft SQL Server licensing options](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/sql-server-licensing). For details about licensing for Microsoft Office, see [Use Microsoft Office with License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/ms-office).

This document describes licensing options for Windows Server. If you want to run [Windows Server VMs](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances) in your VMware Engine private clouds, then you must license the VMs by doing one of the following:

  * Use existing Windows Server licenses purchased before October 1, 2019.

  * Buy on-demand Windows Server licenses directly from Google.

  * Mix Bring Your Own License (BYOL) and on-demand Windows Server licenses.




## Choose your licensing option

By default, the Windows Server VMs in your VMware Engine private clouds aren't licensed. You must license the Windows Server VMs by doing one of the following:

  * Bring your own Windows Server licenses

If you bought Windows Server licenses with dedicated hardware requirements before October 1, 2019, then you can use those licenses within your private clouds. Existing licenses might be more cost-effective than buying on-demand Windows Server licenses from Google because you have more flexibility in licensing the underlying physical CPU cores. However, you're responsible for complying with the terms of your license agreement and reporting license usage to Microsoft.

  * Buy on-demand Windows Server licenses from Google

You can buy on-demand Windows Server licenses from Google for your private clouds. If you buy on-demand licenses from Google, then Google Cloud ensures compliance with the licensing requirements and automatically reports license usage to Microsoft.

  * Use a combination of BYOL and on-demand Windows Server licenses

You can use a combination of BYOL and on-demand Windows Server licenses in a private cloud. For example, you can use BYOL for Windows Server 2019 and earlier, and on-demand licenses from Google for Windows Server 2022 or later VMs. You are responsible for providing your own licenses for all Windows Server versions 2019 and older in your private cloud. **Google supplies on-demand licenses only for vCPUs running Windows Server 2022 or later.**


**Caution:** Google Cloud recommends choosing only one licensing option in a private cloud. If you use your own Windows Server licenses and also buy additional on-demand Windows Server licenses from Google at the same time, then Google Cloud charges you for all Windows Server vCPUs. For more information about pricing for Windows Server licenses in VMware Engine, see Pricing in this document.

### Bring your own Windows Server licenses

If you own Windows Server licenses that require dedicated hardware requirements and were purchased before October 1, 2019, then you can use these existing licenses within your private clouds.

To bring a Windows Server license to your private clouds, ensure the following conditions are met:

  * The license purchase date must be earlier than October 1, 2019.

  * The release date of the licensed product must be earlier than October 1, 2019.

  * You must bring images. If you have questions during the import or migration process, then contact [Google Support](https://docs.cloud.google.com/support).

  * You are responsible for activating your licenses and complying with your licensing agreements.

  * You are responsible for reporting the usage of your licenses.

  * You must license all physical CPU cores in the underlying servers within your VMware Engine nodes regardless of the [number of custom CPU cores](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count). The following table shows the number of CPU cores to license based on the [stock keeping unit (SKU)](https://cloud.google.com/skus/sku-groups/compute-solutions):

SKU | Number of physical CPU cores to license  
---|---  
GCVE Storage Only Node | 0  
VMware Engine Gen 2 Mega Storage Only VCPU Node  | 0  
VMware Engine Gen 2 Standard Storage Only VCPU Node  | 0  
Standard 72 VCPU Node | 36  
VMware Engine Gen 2 Mega 80 VCPU Node | 64  
VMware Engine Gen 2 Mega 96 VCPU Node | 64  
VMware Engine Gen 2 Mega 112 VCPU Node | 64  
VMware Engine Gen 2 Mega 128 VCPU Node | 64  
VMware Engine Gen 2 Standard 96 VCPU Node | 64  
VMware Engine Gen 2 Standard 128 VCPU Node | 64  



### Buy on-demand Windows Server licenses from Google

You can purchase on-demand Windows Server licenses directly from Google and use them within your VMware Engine nodes. After you purchase and enable the on-demand licenses in your private clouds, as described in this section, Google licenses any Windows Server vCPUs running in those private clouds.

To purchase on-demand Windows Server licenses directly from Google and enable them in your private clouds, do the following:

  1. Install the VMware tools on all running Windows Server VMs in your private clouds. For more information, see [How to install VMware Tools](https://knowledge.broadcom.com/external/article/315363/how-to-install-vmware-tools.html) in the Broadcom documentation.

  2. On vCenter, ensure **Guest OS Family** and **Guest OS Version** are set correctly for every VM. For example, identify the **Guest OS Family** as "Windows" and **Guest OS Version** as "Windows Server 2022" for VMs running Windows Server 2022. You must set these values correctly.

  3. To receive a startup script for the Windows Server VMs in each private cloud where you want to enable on-demand licenses, do one of the following:

     * Contact your [Technical Account Manager (TAM)](https://docs.cloud.google.com/support/docs/premium).

     * [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). For each private cloud where you want to enable on-demand licenses, include the following in the support case:

       * The number of the project where the private cloud is located.

       * The name of the private cloud.

       * The region where the private cloud is located.

       * Specify **All SPLA** as the licensing mode.

  4. Add the startup script to all running Windows Server VMs in your private clouds.




After you enable the on-demand licenses, you must provide your own Windows Server OS images. Google Cloud verifies that the on-demand licenses comply with the licensing requirements, and it automatically reports license consumption to Microsoft.

**Important:** If you [delete a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud) after enabling on-demand Windows Server licenses in it, then on-demand licensing support for that private cloud ends and you must enable it again. You might experience a delay of up to 30 minutes for first-time activations for Windows Server licenses, especially for newly created Windows Server VMs.

### Use a combination of BYOL and on-demand Windows Server licenses from Google

On VMware Engine, if you upgrade your VMs to a new version of Windows Server released on or after October 1, 2019 (such as Windows Server 2022 and 2025), you must use on-demand licenses from Google. BYOL is not permitted for these newer versions.

If your private clouds run Windows Server images using BYOL, you can switch to this on-demand licensing mode to upgrade to Windows Server 2022 or later. When you use this mode, you remain responsible for providing your own licenses for all instances running Windows Server versions 2019 and older in your private cloud. Google provides on-demand licenses only for vCPUs running Windows Server 2022 or later. All vCPUs running Windows Server 2022 or later incur charges, and Google reports the consumed on-demand licenses to Microsoft to verify compliance with licensing requirements. To get started, do the following:

  1. Install the VMware tools on all running Windows Server VMs in your private clouds. For more information, see [Install VMware Tools in VMware products](https://knowledge.broadcom.com/external/article/315363/how-to-install-vmware-tools.html).
  2. On vCenter, ensure **Guest OS Family** and **Guest OS Version** are set correctly for every VM. For example, identify the **Guest OS Family** as "Windows" and **Guest OS Version** as "Windows Server 2022" for VMs running Windows Server 2022. You must set these values correctly.
  3. To receive a startup script for the Windows Server VMs in each private cloud where you want to switch to on-demand licenses, do one of the following: 
     * Contact your [Technical Account Manager (TAM)](https://docs.cloud.google.com/support/docs/premium).
     * [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). For each private cloud where you want to enable on-demand licenses, include the following in the support case: 
       * The number of the project where the private cloud is located.
       * The name of the private cloud.
       * The region where the private cloud is located.
       * Specify **Mixed mode / Windows Server 2022/2025 support** as the licensing mode.
  4. Add the startup script to all Windows Server VMs running Windows Server 2022 or newer version in your private clouds.

**Important:** If you [delete a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud) after enabling on-demand Windows Server licenses in it, then on-demand licensing support for that private cloud ends and you must enable it again. You might experience a delay of up to 30 minutes for first-time activations for Windows Server licenses, especially for newly created Windows Server VMs.

## Supported transitions

The following table lists the supported transitions for licensing options:

From | To | Allowed? | Impact or Action  
---|---|---|---  
BYOL | On-demand Licenses from Google | Yes | You start paying for licenses for all Windows Server vCPUs in the private cloud  
BYOL | On-demand licenses from Google only for Windows Server 2022 or later | Yes | You start paying for licenses for all vCPUs running Windows Server 2022 or later in the private cloud  
On-demand licenses from Google | BYOL | Not recommended | Delete the private cloud and start as BYOL  
On-demand licenses from Google only for Windows Server 2022 or later | On-demand licenses from Google | Yes | You start paying for licenses for all vCPUs running Windows Server in the private cloud  
On-demand licenses from Google only for Windows Server 2022 or later | BYOL | Not recommended | Delete the private cloud and start as BYOL  
  
## Pricing

Pricing for Windows Server licenses varies based on your chosen licensing option as follows:

  * If you bring your own Windows Server licenses, then you incur charges according to your agreements with Microsoft.

  * If you purchase on-demand Windows Server licenses from Google, then Google Cloud charges you for each running Windows Server vCPU in your private clouds per the [pricing for Windows Server OS images](https://docs.cloud.google.com/compute/all-pricing#windows_server_pricing).




## What's next

  * Learn more about [Microsoft SQL Server licensing options](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/sql-server-licensing).

  * Learn how to [use License Mobility with Microsoft server applications](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#license-mobility).

  * Learn how to [migrate VMware VMs to your private cloud](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
