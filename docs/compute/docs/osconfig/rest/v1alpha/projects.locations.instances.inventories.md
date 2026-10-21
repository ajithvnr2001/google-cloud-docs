---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories
title: REST Resource: projects.locations.instances.inventories \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:22.602146+00:00
---

# REST Resource: projects.locations.instances.inventories  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instances.inventories Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Inventory
    * JSON representation
  * OsInfo
    * JSON representation
  * Item
    * JSON representation
  * OriginType
  * Type
  * SoftwarePackage
    * JSON representation
  * VersionedPackage
    * JSON representation
  * ZypperPatch
    * JSON representation
  * WindowsUpdatePackage
    * JSON representation
  * WindowsUpdateCategory
    * JSON representation
  * WindowsQuickFixEngineeringPackage
    * JSON representation
  * WindowsApplication
    * JSON representation
  * Methods



## Resource: Inventory

This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time.

You can use this API resource to determine the inventory data of your VM.

For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

JSON representation  
---  
      
    
    {
      "name": string,
      "osInfo": {
        object ([OsInfo](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#OsInfo))
      },
      "items": {
        string: {
          object ([Item](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Item))
        },
        ...
      },
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The `Inventory` API resource name.Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/inventory`  
`osInfo` |  `object (`[OsInfo](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#OsInfo)`)` Output only. Base level operating system information for the VM.  
`items` |  `map (key: string, value: object (`[Item](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Item)`))` Output only. Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last reported inventory for the VM.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## OsInfo

Operating system information for the VM.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "longName": string,
      "shortName": string,
      "version": string,
      "architecture": string,
      "kernelVersion": string,
      "kernelRelease": string,
      "osconfigAgentVersion": string
    }  
  
Fields  
---  
`hostname` |  `string` The VM hostname.  
`longName` |  `string` The operating system long name. For example 'Debian GNU/Linux 9' or 'Microsoft Window Server 2019 Datacenter'.  
`shortName` |  `string` The operating system short name. For example, 'windows' or 'debian'.  
`version` |  `string` The version of the operating system.  
`architecture` |  `string` The system architecture of the operating system.  
`kernelVersion` |  `string` The kernel version of the operating system.  
`kernelRelease` |  `string` The kernel release of the operating system.  
`osconfigAgentVersion` |  `string` The current version of the OS Config agent running on the VM.  
  
## Item

A single piece of inventory on a VM.

JSON representation  
---  
      
    
    {
      "id": string,
      "originType": enum ([OriginType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#OriginType)),
      "createTime": string,
      "updateTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Type)),
    
      // Union field details can be only one of the following:
      "installedPackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#SoftwarePackage))
      },
      "availablePackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#SoftwarePackage))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`id` |  `string` Identifier for this item, unique across items for this VM.  
`originType` |  `enum (`[OriginType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#OriginType)`)` The origin of this inventory item.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was first detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Type)`)` The specific type of inventory, correlating to its specific details.  
Union field `details`. Specific details of this inventory item based on its type. `details` can be only one of the following:  
`installedPackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#SoftwarePackage)`)` Software package present on the VM instance.  
`availablePackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#SoftwarePackage)`)` Software package available to be installed on the VM instance.  
  
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
  
## SoftwarePackage

Software package information of the operating system.

JSON representation  
---  
      
    
    {
    
      // Union field details can be only one of the following:
      "yumPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage))
      },
      "aptPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage))
      },
      "zypperPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage))
      },
      "googetPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage))
      },
      "zypperPatch": {
        object ([ZypperPatch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#ZypperPatch))
      },
      "wuaPackage": {
        object ([WindowsUpdatePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsUpdatePackage))
      },
      "qfePackage": {
        object ([WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsQuickFixEngineeringPackage))
      },
      "cosPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage))
      },
      "windowsApplication": {
        object ([WindowsApplication](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsApplication))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
Union field `details`. Information about the different types of software packages. `details` can be only one of the following:  
`yumPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage)`)` Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.  
`aptPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage)`)` Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.  
`zypperPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage)`)` Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`googetPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage)`)` Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.  
`zypperPatch` |  `object (`[ZypperPatch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#ZypperPatch)`)` Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`wuaPackage` |  `object (`[WindowsUpdatePackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsUpdatePackage)`)` Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.  
`qfePackage` |  `object (`[WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsQuickFixEngineeringPackage)`)` Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.  
`cosPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#VersionedPackage)`)` Details of a COS package.  
`windowsApplication` |  `object (`[WindowsApplication](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsApplication)`)` Details of Windows Application.  
  
## VersionedPackage

Information related to the a standard versioned package. This includes package info for APT, Yum, Zypper, and Googet package managers.

JSON representation  
---  
      
    
    {
      "packageName": string,
      "architecture": string,
      "version": string
    }  
  
Fields  
---  
`packageName` |  `string` The name of the package.  
`architecture` |  `string` The system architecture this package is intended for.  
`version` |  `string` The version of the package.  
  
## ZypperPatch

Details related to a Zypper Patch.

JSON representation  
---  
      
    
    {
      "patchName": string,
      "category": string,
      "severity": string,
      "summary": string
    }  
  
Fields  
---  
`patchName` |  `string` The name of the patch.  
`category` |  `string` The category of the patch.  
`severity` |  `string` The severity specified for this patch  
`summary` |  `string` Any summary information provided about this patch.  
  
## WindowsUpdatePackage

Details related to a Windows Update package. Field data and names are taken from Windows Update API IUpdate Interface: <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> Descriptive fields like title, and description are localized based on the locale of the VM being updated.

JSON representation  
---  
      
    
    {
      "title": string,
      "description": string,
      "categories": [
        {
          object ([WindowsUpdateCategory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsUpdateCategory))
        }
      ],
      "kbArticleIds": [
        string
      ],
      "supportUrl": string,
      "moreInfoUrls": [
        string
      ],
      "updateId": string,
      "revisionNumber": integer,
      "lastDeploymentChangeTime": string
    }  
  
Fields  
---  
`title` |  `string` The localized title of the update package.  
`description` |  `string` The localized description of the update package.  
`categories[]` |  `object (`[WindowsUpdateCategory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#WindowsUpdateCategory)`)` The categories that are associated with this update package.  
`kbArticleIds[]` |  `string` A collection of Microsoft Knowledge Base article IDs that are associated with the update package.  
`supportUrl` |  `string` A hyperlink to the language-specific support information for the update.  
`moreInfoUrls[]` |  `string` A collection of URLs that provide more information about the update package.  
`updateId` |  `string` Gets the identifier of an update package. Stays the same across revisions.  
`revisionNumber` |  `integer` The revision number of this update package.  
`lastDeploymentChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last published date of the update, in (UTC) date and time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## WindowsUpdateCategory

Categories specified by the Windows Update.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string
    }  
  
Fields  
---  
`id` |  `string` The identifier of the windows update category.  
`name` |  `string` The name of the windows update category.  
  
## WindowsQuickFixEngineeringPackage

Information related to a Quick Fix Engineering package. Fields are taken from Windows QuickFixEngineering Interface and match the source names: <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering>

JSON representation  
---  
      
    
    {
      "caption": string,
      "description": string,
      "hotFixId": string,
      "installTime": string
    }  
  
Fields  
---  
`caption` |  `string` A short textual description of the QFE update.  
`description` |  `string` A textual description of the QFE update.  
`hotFixId` |  `string` Unique identifier associated with a particular QFE update.  
`installTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date that the QFE update was installed. Mapped from installed_on field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## WindowsApplication

Contains information about a Windows application that is retrieved from the Windows Registry. For more information about these fields, see: <https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key>

JSON representation  
---  
      
    
    {
      "displayName": string,
      "displayVersion": string,
      "publisher": string,
      "installDate": {
        object ([Date](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Date))
      },
      "helpLink": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the application or product.  
`displayVersion` |  `string` The version of the product or application in string format.  
`publisher` |  `string` The name of the manufacturer for the product or application.  
`installDate` |  `object (`[Date](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Date)`)` The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product.  
`helpLink` |  `string` The internet address for technical support.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/get)`

|  Get inventory data for the specified VM instance.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/list)`

|  List inventory data for all VM instances in the specified zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
