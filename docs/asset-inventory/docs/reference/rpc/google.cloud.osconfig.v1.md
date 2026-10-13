---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1
title: Package google.cloud.osconfig.v1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.318785+00:00
---

# Package google.cloud.osconfig.v1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.cloud.osconfig.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory)` (message)
  * `[Inventory.Item](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item)` (message)
  * `[Inventory.Item.OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item.OriginType)` (enum)
  * `[Inventory.Item.Type](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item.Type)` (enum)
  * `[Inventory.OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.OsInfo)` (message)
  * `[Inventory.SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.SoftwarePackage)` (message)
  * `[Inventory.VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` (message)
  * `[Inventory.WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsApplication)` (message)
  * `[Inventory.WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsQuickFixEngineeringPackage)` (message)
  * `[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)` (message)
  * `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)` (message)
  * `[Inventory.ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.ZypperPatch)` (message)



## Inventory

This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time.

You can use this API resource to determine the inventory data of your VM.

For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

Fields  
---  
`name` |  `string` Output only. The `Inventory` API resource name.Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/inventory`  
`os_info` |  `[OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.OsInfo)` Base level operating system information for the VM.  
`items` |  `map<string, `[Item](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item)`>` Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp of the last reported inventory for the VM.  
  
## Item

A single piece of inventory on a VM.

Fields  
---  
`id` |  `string` Identifier for this item, unique across items for this VM.  
`origin_type` |  `[OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item.OriginType)` The origin of this inventory item.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` When this inventory item was first detected.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` When this inventory item was last modified.  
`type` |  `[Type](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.Item.Type)` The specific type of inventory, correlating to its specific details.  
Union field `details`. Specific details of this inventory item based on its type. `details` can be only one of the following:  
`installed_package` |  `[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.SoftwarePackage)` Software package present on the VM instance.  
`available_package` |  `[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.SoftwarePackage)` Software package available to be installed on the VM instance.  
  
## OriginType

The origin of a specific inventory item.

Enums  
---  
`ORIGIN_TYPE_UNSPECIFIED` | Invalid. An origin type must be specified.  
`INVENTORY_REPORT` | This inventory item was discovered as the result of the agent reporting inventory via the reporting API.  
  
## Type

The different types of inventory that are tracked on a VM.

Enums  
---  
`TYPE_UNSPECIFIED` | Invalid. A type must be specified.  
`INSTALLED_PACKAGE` | This represents a package that is installed on the VM.  
`AVAILABLE_PACKAGE` | This represents an update that is available for a package.  
  
## OsInfo

Operating system information for the VM.

Fields  
---  
`hostname` |  `string` The VM hostname.  
`long_name` |  `string` The operating system long name. For example 'Debian GNU/Linux 9' or 'Microsoft Window Server 2019 Datacenter'.  
`short_name` |  `string` The operating system short name. For example, 'windows' or 'debian'.  
`version` |  `string` The version of the operating system.  
`architecture` |  `string` The system architecture of the operating system.  
`kernel_version` |  `string` The kernel version of the operating system.  
`kernel_release` |  `string` The kernel release of the operating system.  
`osconfig_agent_version` |  `string` The current version of the OS Config agent running on the VM.  
  
## SoftwarePackage

Software package information of the operating system.

Fields  
---  
Union field `details`. Information about the different types of software packages. `details` can be only one of the following:  
`yum_package` |  `[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.  
`apt_package` |  `[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.  
`zypper_package` |  `[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`googet_package` |  `[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.  
`zypper_patch` |  `[ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.ZypperPatch)` Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`wua_package` |  `[WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)` Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.  
`qfe_package` |  `[WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsQuickFixEngineeringPackage)` Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.  
`cos_package` |  `[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.VersionedPackage)` Details of a COS package.  
`windows_application` |  `[WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsApplication)` Details of Windows Application.  
  
## VersionedPackage

Information related to the a standard versioned package. This includes package info for APT, Yum, Zypper, and Googet package managers.

Fields  
---  
`package_name` |  `string` The name of the package.  
`architecture` |  `string` The system architecture this package is intended for.  
`version` |  `string` The version of the package.  
  
## WindowsApplication

Contains information about a Windows application that is retrieved from the Windows Registry. For more information about these fields, see: <https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key>

Fields  
---  
`display_name` |  `string` The name of the application or product.  
`display_version` |  `string` The version of the product or application in string format.  
`publisher` |  `string` The name of the manufacturer for the product or application.  
`install_date` |  `[Date](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.type#google.type.Date)` The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product.  
`help_link` |  `string` The internet address for technical support.  
  
## WindowsQuickFixEngineeringPackage

Information related to a Quick Fix Engineering package. Fields are taken from Windows QuickFixEngineering Interface and match the source names: <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering>

Fields  
---  
`caption` |  `string` A short textual description of the QFE update.  
`description` |  `string` A textual description of the QFE update.  
`hot_fix_id` |  `string` Unique identifier associated with a particular QFE update.  
`install_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Date that the QFE update was installed. Mapped from installed_on field.  
  
## WindowsUpdatePackage

Details related to a Windows Update package. Field data and names are taken from Windows Update API IUpdate Interface: <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> Descriptive fields like title, and description are localized based on the locale of the VM being updated.

Fields  
---  
`title` |  `string` The localized title of the update package.  
`description` |  `string` The localized description of the update package.  
`categories[]` |  `[WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)` The categories that are associated with this update package.  
`kb_article_ids[]` |  `string` A collection of Microsoft Knowledge Base article IDs that are associated with the update package.  
`support_url` |  `string` A hyperlink to the language-specific support information for the update.  
`more_info_urls[]` |  `string` A collection of URLs that provide more information about the update package.  
`update_id` |  `string` Gets the identifier of an update package. Stays the same across revisions.  
`revision_number` |  `int32` The revision number of this update package.  
`last_deployment_change_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last published date of the update, in (UTC) date and time.  
  
## WindowsUpdateCategory

Categories specified by the Windows Update.

Fields  
---  
`id` |  `string` The identifier of the windows update category.  
`name` |  `string` The name of the windows update category.  
  
## ZypperPatch

Details related to a Zypper Patch.

Fields  
---  
`patch_name` |  `string` The name of the patch.  
`category` |  `string` The category of the patch.  
`severity` |  `string` The severity specified for this patch  
`summary` |  `string` Any summary information provided about this patch.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
