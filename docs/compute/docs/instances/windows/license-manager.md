---
url: https://docs.cloud.google.com/compute/docs/instances/windows/license-manager/
title: About License Manager \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:47.374766+00:00
---

# About License Manager  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/license-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About License Manager Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

License Manager lets you subscribe, manage, and track third-party license usage on Google Cloud. As an administrator, you can use License Manager to assign and monitor per-user licensing products, such as Microsoft Office, on virtual machines (VMs).

## How License Manager works

License Manager uses two main components to authenticate, activate, and monitor per-user licenses on your virtual machines:

  * The license configuration, which stores the licensed application details, region, and number of authorized licenses.

  * The License Manager agent, which activates the software directly with the third-party vendor from your virtual machine (VM) instance. Some third-party licenses depend on user access counts over a given period. The agent also verifies the number of consumed licenses from your license configuration.




In the License Manager dashboard, you can view active licenses across your organization and adjust monthly license counts.

## Supported licensing products

License Manager supports the following products:

  * [Microsoft Office LTSC 2021 Professional Plus](https://docs.cloud.google.com/compute/docs/instances/windows/ms-office)
  * [Microsoft Office LTSC 2024 Professional Plus](https://docs.cloud.google.com/compute/docs/instances/windows/ms-office)



## Limitations

License Manager has the following limitations:

  * License Manager is available on Compute Engine and Google Cloud VMware Engine, but individual licensing products might be available on only one platform. For more information about platform support for each product, refer to its specific documentation.

  * Logging is available only for VMs running on Compute Engine; it isn't supported for Google Cloud VMware Engine instances.

  * License Manager supports a default limit of 5,000 licenses per license configuration. To request a quota increase, contact [license-manager-onboarding@google.com](mailto:license-manager-onboarding@google.com).

  * License Manager supports one license configuration per product per region. You can't create multiple license configurations for the same product in the same region.

  * License Manager is supported in the following regions:

    * `africa-south1`
    * `asia-east1`
    * `asia-east2`
    * `asia-northeast1`
    * `asia-northeast3`
    * `asia-south1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `australia-southeast2`
    * `europe-north1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
    * `me-central1`
    * `me-west1`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `southamerica-west1`
    * `us-central1`
    * `us-east1`
    * `us-east4`
    * `us-south1`
    * `us-west2`

If your target region is not listed, contact [license-manager-onboarding@google.com](mailto:license-manager-onboarding@google.com).




## Get started with License Manager

To use licenses managed by License Manager, do the following:

  1. Enable the License Manager API
  2. Create a license configuration
  3. Install and activate the License Manager agent on a VM



### Before you begin

To get the permissions that you need to get started with License Manager, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [License Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/licensemanager#licensemanager.admin) (`roles/licensemanager.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the License Manager API

To enable the License Manager API, do the following:

  1. In the Google Cloud console, go to the **APIs & Services** page.

[Go to the APIs & Services page](https://console.cloud.google.com/apis)

  2. Click **Enable APIs & Services**.

  3. Search for and select **License Manager API** with the service name `licensemanager.googleapis.com`.

  4. Click **Enable**.




### Create a license configuration

For some licensing products, your billing obligation begins immediately when you create the license configuration. For information about product billing considerations, see Supported licensing products.

To create a license configuration by using the Google Cloud console, do the following:

  1. Open the **License Manager** page in the Google Cloud console.

[Go to the License Manager page](https://console.cloud.google.com/license-manager/configurations)

  2. Click **Create License Configuration**.

  3. Enter a **Name** for your configuration.

  4. Select a **Location** for your configuration.

  5. Choose the **Product** you want to associate with the license. For an up-to-date list of supported products, see Supported licensing products. Note that you can create only one license configuration per product per region.

  6. Enter the total **Number of Licenses** you want to enable.

  7. Select the confirmation checkbox to verify your entered information.

  8. Click **Create** to finalize your license configuration.




### Install and activate the License Manager agent

Each VM using a license managed by License Manager requires the License Manager agent to authenticate and activate software.

To install and activate the License Manager agent, open PowerShell as an administrator on your VM and do the following:

  1. Add the googet repository:
         
         googet addrepo google-cloud-license-manager-agent https://packages.cloud.google.com/yuck/repos/google-cloud-license-manager-agent-windows-x86_64
         

  2. Install the License Manager agent:
         
         googet install google-cloud-license-manager-agent
         

  3. Configure the agent:

Installing the agent creates a directory at `C:\Program Files\Google\google-cloud-license-manager-agent`. To specify the `products` to activate, edit the configuration file located at `conf\configuration.json`.

For VMware Engine, specify the `vcenter_domain` property with your vCenter FQDN (for example, `"vcenter_domain": "vcenter.example.com"`).

The following is an example configuration file for activating Microsoft Office 2024 Professional Plus:
         
         {
           "log_level": "INFO",
           "log_to_cloud": true,
           "products":
             [
               {
                 "name": "Office2024ProfessionalPlus",
                 "source_path": "C:\\Program Files\\Microsoft Office"
               }
             ]
         }
         

The following table describes the properties in the `configuration.json` file:

Property | Type | Description  
---|---|---  
`log_level` | String | Logging verbosity: `DEBUG`, `WARNING`, `ERROR`, or `INFO`. Default is `INFO`.  
`log_to_cloud` | Boolean | Enables export to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). Default is `false`.  
`products[].name` | String | Supported products: `Office2021ProfessionalPlus`, `Office2024ProfessionalPlus`.  
`products[].source_path` | String | Installation directory path (for example, `C:\Program Files\Microsoft Office`).  
  
If you set `"log_to_cloud": true`, ensure you complete the following Cloud Logging prerequisites:

     * Enable the Cloud Logging API (`logging.googleapis.com`) in your project.
     * Grant your virtual machines access to the Cloud Logging API.
     * Grant the VM service account the **Logs Writer** role (`roles/logging.logWriter`).

If your VM uses multiple products managed by License Manager, add an entry for each product to the `products` list.

  4. To verify that the configuration file is formatted correctly, run the `validate_config` command:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' validate_config
         

  5. To apply your changes, restart the agent service:
         
         Restart-Service -Name 'google-cloud-license-manager-agent' -Force
         

  6. To activate your product (for example, `Office2024ProfessionalPlus` or `Office2021ProfessionalPlus`), run the following command:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' activate Office2024ProfessionalPlus
         

Microsoft requires Office LTSC licenses to activate over the internet directly with Microsoft servers. Ensure the VM has outbound internet access during activation.




To verify that activation was successful, open any Microsoft Office application on your VM, click **File** > **Account** , and verify that the status displays **Product Activated**.

### Migrate from Office LTSC 2021 to Office LTSC 2024

To migrate an existing VM from Microsoft Office LTSC 2021 to Office LTSC 2024, do the following:

**Note:** Because Microsoft Office licenses are billed by the calendar month, if you deactivate Office LTSC 2021 and activate Office LTSC 2024 in the same month, you incur billing charges for both products for that calendar month. For more information, see [Calendar month billing](https://docs.cloud.google.com/compute/docs/instances/windows/ms-office#calendar-month-billing).

  1. Create a license configuration for **Microsoft Office LTSC 2024 Professional Plus** in the Google Cloud console in the same region as your VM.

  2. To deactivate Office LTSC 2021, open PowerShell as an administrator on your VM and run the following command:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' deactivate Office2021ProfessionalPlus
         

  3. To deploy Office LTSC 2024, follow [Microsoft's deployment guide for Office LTSC 2024](https://learn.microsoft.com/en-us/office/ltsc/2024/deploy).

  4. To update the License Manager agent, run the following command:
         
         googet update google-cloud-license-manager-agent
         

  5. To replace `Office2021ProfessionalPlus` with `Office2024ProfessionalPlus`, edit the configuration file located at `C:\Program Files\Google\google-cloud-license-manager-agent\conf\configuration.json`:
         
         {
           "log_level": "INFO",
           "log_to_cloud": true,
           "products":
             [
               {
                 "name": "Office2024ProfessionalPlus",
                 "source_path": "C:\\Program Files\\Microsoft Office"
               }
             ]
         }
         

  6. To verify that the configuration file is formatted correctly, run the `validate_config` command:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' validate_config
         

  7. To apply your changes, restart the agent service:
         
         Restart-Service -Name 'google-cloud-license-manager-agent' -Force
         

  8. To activate Office LTSC 2024, run the following command:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' activate Office2024ProfessionalPlus
         




To verify that activation was successful, open any Microsoft Office application on your VM, click **File** > **Account** , and verify that the status displays **Product Activated**.

## Manage your licenses

After creating a license configuration, you can adjust license volume or deactivate the configuration. Deactivated license configurations remain visible for 90 days before permanent deletion. You can reactivate within that period.

### Increase or decrease your license count

Some licenses are billed by the calendar month in which they are active. License volume increases take effect immediately. Decreases or deactivations take effect in the next calendar month. For information about how each license is billed, see Supported licensing products.

To change the total license count for a license configuration, do the following:

  1. Open the **License Manager** page in the Google Cloud console.

[Go to the License Manager page](https://console.cloud.google.com/license-manager/configurations)

  2. On the license configuration that you want to modify, to show additional options, click **Actions**.

  3. Click **Edit License Volume**.

  4. Enter the new license volume amount.

  5. Click **Confirm** to apply the updated volume.




### Deactivate a license configuration

When you no longer require licenses in a particular region, you can deactivate the license configuration. Deactivated configurations display the **Inactive** status and remain visible for 90 days before deletion.

To deactivate a license configuration, do the following:

  1. Open the **License Manager** page in the Google Cloud console.

[Go to the License Manager page](https://console.cloud.google.com/license-manager/configurations)

  2. On the license configuration that you want to deactivate, to show additional options, click **Actions**.

  3. Click **Deactivate License Configuration**.

  4. Click **Confirm** to deactivate the license configuration.




### Reactivate a license configuration

To reactivate a deactivated license configuration, do the following:

  1. Open the **License Manager** page in the Google Cloud console.

[Go to the License Manager page](https://console.cloud.google.com/license-manager/configurations)

  2. On the license configuration that you want to reactivate, to show additional options, click **Actions**.

  3. Click **Reactivate License Configuration**.

  4. Click **Confirm** to reactivate the configuration.




License configurations that were previously active in the current calendar month default to the previous license count. Otherwise, the reactivated license configuration defaults to a license count of 0. To adjust the license count after reactivation, see Increase or decrease your license count.

### Uninstall the License Manager agent

To begin uninstallation, you must first deactivate your licensing products:

  1. In a Powershell terminal with Administrator mode, use the `deactivate`command to deactivate the product:
         
         & 'C:\Program Files\Google\google-cloud-license-manager-agent\google-cloud-license-manager-agent.exe' deactivate Office2021ProfessionalPlus
         

  2. Uninstall the agent with the following command:
         
         googet clean
         googet remove google-cloud-license-manager-agent
         




## Review agent logs

The License Manager agent supports both local logging on the VM and cloud logging with Cloud Logging in the Google Cloud console.

### View local logs

Local logs are stored on the VM in `C:\Program Files\Google\google-cloud-license-manager-agent\logs`.

Each log file has a maximum size of 25 MB before the agent creates a new log file. The agent retains up to three log files and automatically deletes the oldest file when this limit is reached.

### View Cloud Logging logs

If cloud logging is enabled (`"log_to_cloud": true`), you can view agent logs in the Google Cloud console by doing the following:

  1. Open the **Logs Explorer** page in the Google Cloud console.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Click **All Resources**.

  3. In the menu, click **GCP Location** , and then click **Global**.

  4. Click **Apply**.

  5. In the query editor, enter `google-cloud-license-manager-agent`.

  6. Click **Run query**.




Logs generated by agent instances running across your VMs appear in the results list. To filter logs for a specific VM, use the query filters available in the interface.

## Create a service perimeter for License Manager

VPC Service Controls helps mitigate data exfiltration risks from your Google-managed services.

With VPC Service Controls, you can configure service perimeters around the resources of your Google-managed services and control the movement of data across the perimeter boundary.

To create a service perimeter, see the [VPC Service Controls guide to creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

To protect License Manager, add the following APIs to the service perimeter:

  * License Manager API (`licensemanager.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * Agent Communication API (`agentcommunication.googleapis.com`)



Your service perimeter must include all of these services for the License Manager agent to work with VPC Service Controls.

## What's next

  * [Use Microsoft Office with License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/ms-office)
  * [Microsoft Licensing on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)
  * [Microsoft Licensing on Google Cloud FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq)
  * [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
