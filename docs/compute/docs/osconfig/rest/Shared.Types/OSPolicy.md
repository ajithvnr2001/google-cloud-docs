---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy/
title: OSPolicy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:11.249841+00:00
---

# OSPolicy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  OSPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResourceGroup
    * JSON representation
  * InventoryFilter
    * JSON representation
  * Resource
    * JSON representation
  * PackageResource
    * JSON representation
  * APT
    * JSON representation
  * Deb
    * JSON representation
  * File
    * JSON representation
  * Remote
    * JSON representation
  * Gcs
    * JSON representation
  * YUM
    * JSON representation
  * Zypper
    * JSON representation
  * RPM
    * JSON representation
  * GooGet
    * JSON representation
  * MSI
    * JSON representation
  * RepositoryResource
    * JSON representation
  * AptRepository
    * JSON representation
  * YumRepository
    * JSON representation
  * ZypperRepository
    * JSON representation
  * GooRepository
    * JSON representation
  * ExecResource
    * JSON representation
  * Exec
    * JSON representation
  * FileResource
    * JSON representation



An OS policy defines the desired state configuration for a VM.

JSON representation  
---  
      
    
    {
      "id": string,
      "description": string,
      "mode": enum ([Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Mode)),
      "resourceGroups": [
        {
          object ([ResourceGroup](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ResourceGroup))
        }
      ],
      "allowNoResourceGroupMatch": boolean
    }  
  
Fields  
---  
`id` |  `string` Required. The id of the OS policy with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the assignment.

  
`description` |  `string` Policy description. Length of the description is limited to 1024 characters.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Mode)`)` Required. Policy mode  
`resourceGroups[]` |  `object (`[ResourceGroup](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ResourceGroup)`)` Required. List of resource groups for the policy. For a particular VM, resource groups are evaluated in the order specified and the first resource group that is applicable is selected and the rest are ignored.If none of the resource groups are applicable for a VM, the VM is considered to be non-compliant w.r.t this policy. This behavior can be toggled by the flag `allowNoResourceGroupMatch`  
`allowNoResourceGroupMatch` |  `boolean` This flag determines the OS policy compliance status when none of the resource groups within the policy are applicable for a VM. Set this value to `true` if the policy needs to be reported as compliant even if the policy has nothing to validate or enforce.  
  
## ResourceGroup

Resource groups provide a mechanism to group OS policy resources.

Resource groups enable OS policy authors to create a single OS policy to be applied to VMs running different operating Systems.

When the OS policy is applied to a target VM, the appropriate resource group within the OS policy is selected based on the `OSFilter` specified within the resource group.

JSON representation  
---  
      
    
    {
      "inventoryFilters": [
        {
          object ([InventoryFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#InventoryFilter))
        }
      ],
      "resources": [
        {
          object ([Resource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Resource))
        }
      ]
    }  
  
Fields  
---  
`inventoryFilters[]` |  `object (`[InventoryFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#InventoryFilter)`)` List of inventory filters for the resource group.The resources in this resource group are applied to the target VM if it satisfies at least one of the following inventory filters.For example, to apply this resource group to VMs running either `RHEL` or `CentOS` operating systems, specify 2 items for the list with following values: inventoryFilters[0].os_short_name='rhel' and inventoryFilters[1].os_short_name='centos'If the list is empty, this resource group will be applied to the target VM unconditionally.  
`resources[]` |  `object (`[Resource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Resource)`)` Required. List of resources configured for this resource group. The resources are executed in the exact order specified here.  
  
## InventoryFilter

Filtering criteria to select VMs based on inventory details.

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string
    }  
  
Fields  
---  
`osShortName` |  `string` Required. The OS short name  
`osVersion` |  `string` The OS versionPrefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*`An empty string matches all OS versions.  
  
## Resource

An OS policy resource is used to define the desired state configuration and provides a specific functionality like installing/removing packages, executing a script etc.

The system ensures that resources are always in their desired state by taking necessary actions if they have drifted from their desired state.

JSON representation  
---  
      
    
    {
      "id": string,
    
      // Union field resource_type can be only one of the following:
      "pkg": {
        object ([PackageResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#PackageResource))
      },
      "repository": {
        object ([RepositoryResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#RepositoryResource))
      },
      "exec": {
        object ([ExecResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ExecResource))
      },
      "file": {
        object ([FileResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#FileResource))
      }
      // End of list of possible types for union field resource_type.
    }  
  
Fields  
---  
`id` |  `string` Required. The id of the resource with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the OS policy.

  
Union field `resource_type`. Resource type. `resource_type` can be only one of the following:  
`pkg` |  `object (`[PackageResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#PackageResource)`)` Package resource  
`repository` |  `object (`[RepositoryResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#RepositoryResource)`)` Package repository resource  
`exec` |  `object (`[ExecResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ExecResource)`)` Exec resource  
`file` |  `object (`[FileResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#FileResource)`)` File resource  
  
## PackageResource

A resource that manages a system package.

JSON representation  
---  
      
    
    {
      "desiredState": enum (DesiredState),
    
      // Union field system_package can be only one of the following:
      "apt": {
        object ([APT](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#APT))
      },
      "deb": {
        object ([Deb](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Deb))
      },
      "yum": {
        object ([YUM](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#YUM))
      },
      "zypper": {
        object ([Zypper](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Zypper))
      },
      "rpm": {
        object ([RPM](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#RPM))
      },
      "googet": {
        object ([GooGet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#GooGet))
      },
      "msi": {
        object ([MSI](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#MSI))
      }
      // End of list of possible types for union field system_package.
    }  
  
Fields  
---  
`desiredState` |  `enum (`DesiredState`)` Required. The desired state the agent should maintain for this package.  
Union field `system_package`. A system package. `system_package` can be only one of the following:  
`apt` |  `object (`[APT](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#APT)`)` A package managed by Apt.  
`deb` |  `object (`[Deb](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Deb)`)` A deb package file.  
`yum` |  `object (`[YUM](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#YUM)`)` A package managed by YUM.  
`zypper` |  `object (`[Zypper](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Zypper)`)` A package managed by Zypper.  
`rpm` |  `object (`[RPM](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#RPM)`)` An rpm package file.  
`googet` |  `object (`[GooGet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#GooGet)`)` A package managed by GooGet.  
`msi` |  `object (`[MSI](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#MSI)`)` An MSI package.  
  
## APT

A package managed by APT. - install: `apt-get update && apt-get -y install [name]` \- remove: `apt-get -y remove [name]`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
## Deb

A deb package file. dpkg packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File))
      },
      "pullDeps": boolean
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File)`)` Required. A deb package.  
`pullDeps` |  `boolean` Whether dependencies should also be installed. - install when false: `dpkg -i package` \- install when true: `apt-get update && apt-get -y install package.deb`  
  
## File

A remote or local file.

JSON representation  
---  
      
    
    {
      "allowInsecure": boolean,
    
      // Union field type can be only one of the following:
      "remote": {
        object ([Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Remote))
      },
      "gcs": {
        object ([Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Gcs))
      },
      "localPath": string
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`allowInsecure` |  `boolean` Defaults to false. When false, files are subject to validations based on the file type:Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
Union field `type`. A specific type of file. `type` can be only one of the following:  
`remote` |  `object (`[Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Remote)`)` A generic remote file.  
`gcs` |  `object (`[Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Gcs)`)` A Cloud Storage object.  
`localPath` |  `string` A local path within the VM to use.  
  
## Remote

Specifies a file available via some URI.

JSON representation  
---  
      
    
    {
      "uri": string,
      "sha256Checksum": string
    }  
  
Fields  
---  
`uri` |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`sha256Checksum` |  `string` SHA256 checksum of the remote file.  
  
## Gcs

Specifies a file available as a Cloud Storage Object.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "object": string,
      "generation": string
    }  
  
Fields  
---  
`bucket` |  `string` Required. Bucket of the Cloud Storage object.  
`object` |  `string` Required. Name of the Cloud Storage object.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Generation number of the Cloud Storage object.  
  
## YUM

A package managed by YUM. - install: `yum -y install package` \- remove: `yum -y remove package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
## Zypper

A package managed by Zypper. - install: `zypper -y install package` \- remove: `zypper -y rm package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
## RPM

An RPM package file. RPM packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File))
      },
      "pullDeps": boolean
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File)`)` Required. An rpm package.  
`pullDeps` |  `boolean` Whether dependencies should also be installed. - install when false: `rpm --upgrade --replacepkgs package.rpm` \- install when true: `yum -y install package.rpm` or `zypper -y install package.rpm`  
  
## GooGet

A package managed by GooGet. - install: `googet -noconfirm install package` \- remove: `googet -noconfirm remove package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
## MSI

An MSI package. MSI packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File))
      },
      "properties": [
        string
      ]
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File)`)` Required. The MSI package.  
`properties[]` |  `string` Additional properties to use during installation. This should be in the format of Property=Setting. Appended to the defaults of `ACTION=INSTALL REBOOT=ReallySuppress`.  
  
## RepositoryResource

A resource that manages a package repository.

JSON representation  
---  
      
    
    {
    
      // Union field repository can be only one of the following:
      "apt": {
        object ([AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#AptRepository))
      },
      "yum": {
        object ([YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#YumRepository))
      },
      "zypper": {
        object ([ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ZypperRepository))
      },
      "goo": {
        object ([GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#GooRepository))
      }
      // End of list of possible types for union field repository.
    }  
  
Fields  
---  
Union field `repository`. A specific type of repository. `repository` can be only one of the following:  
`apt` |  `object (`[AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#AptRepository)`)` An Apt Repository.  
`yum` |  `object (`[YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#YumRepository)`)` A Yum Repository.  
`zypper` |  `object (`[ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#ZypperRepository)`)` A Zypper Repository.  
`goo` |  `object (`[GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#GooRepository)`)` A Goo Repository.  
  
## AptRepository

Represents a single apt package repository. These will be added to a repo file that will be managed at `/etc/apt/sources.list.d/google_osconfig.list`.

JSON representation  
---  
      
    
    {
      "archiveType": enum ([ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/ArchiveType)),
      "uri": string,
      "distribution": string,
      "components": [
        string
      ],
      "gpgKey": string
    }  
  
Fields  
---  
`archiveType` |  `enum (`[ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/ArchiveType)`)` Required. Type of archive files in this repository.  
`uri` |  `string` Required. URI for this repository.  
`distribution` |  `string` Required. Distribution of this repository.  
`components[]` |  `string` Required. List of components for this repository. Must contain at least one item.  
`gpgKey` |  `string` URI of the key file for this repository. The agent maintains a keyring at `/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg`.  
  
## YumRepository

Represents a single yum package repository. These are added to a repo file that is managed at `/etc/yum.repos.d/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "baseUrl": string,
      "gpgKeys": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the yum config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for resource conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
## ZypperRepository

Represents a single zypper package repository. These are added to a repo file that is managed at `/etc/zypp/repos.d/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "baseUrl": string,
      "gpgKeys": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the zypper config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for GuestPolicy conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
## GooRepository

Represents a Goo package repository. These are added to a repo file that is managed at `C:/ProgramData/GooGet/repos/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "name": string,
      "url": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the repository.  
`url` |  `string` Required. The url of the repository.  
  
## ExecResource

A resource that allows executing scripts on the VM.

The `ExecResource` has 2 stages: `validate` and `enforce` and both stages accept a script as an argument to execute.

When the `ExecResource` is applied by the agent, it first executes the script in the `validate` stage. The `validate` stage can signal that the `ExecResource` is already in the desired state by returning an exit code of `100`. If the `ExecResource` is not in the desired state, it should return an exit code of `101`. Any other exit code returned by this stage is considered an error.

If the `ExecResource` is not in the desired state based on the exit code from the `validate` stage, the agent proceeds to execute the script from the `enforce` stage. If the `ExecResource` is already in the desired state, the `enforce` stage will not be run. Similar to `validate` stage, the `enforce` stage should return an exit code of `100` to indicate that the resource in now in its desired state. Any other exit code is considered an error.

NOTE: An exit code of `100` was chosen over `0` (and `101` vs `1`) to have an explicit indicator of `in desired state`, `not in desired state` and errors. Because, for example, Powershell will always return an exit code of `0` unless an `exit` statement is provided in the script. So, for reasons of consistency and being explicit, exit codes `100` and `101` were chosen.

JSON representation  
---  
      
    
    {
      "validate": {
        object ([Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Exec))
      },
      "enforce": {
        object ([Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Exec))
      }
    }  
  
Fields  
---  
`validate` |  `object (`[Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Exec)`)` Required. What to run to validate this resource is in the desired state. An exit code of 100 indicates "in desired state", and exit code of 101 indicates "not in desired state". Any other exit code indicates a failure running validate.  
`enforce` |  `object (`[Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#Exec)`)` What to run to bring this resource into the desired state. An exit code of 100 indicates "success", any other exit code indicates a failure running enforce.  
  
## Exec

A file or script to execute.

JSON representation  
---  
      
    
    {
      "args": [
        string
      ],
      "interpreter": enum ([Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Interpreter)),
      "outputFilePath": string,
    
      // Union field source can be only one of the following:
      "file": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File))
      },
      "script": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`args[]` |  `string` Optional arguments to pass to the source during execution.  
`interpreter` |  `enum (`[Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/Interpreter)`)` Required. The script interpreter to use.  
`outputFilePath` |  `string` Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 500K bytes.  
Union field `source`. What to execute. `source` can be only one of the following:  
`file` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File)`)` A remote or local file.  
`script` |  `string` An inline script. The size of the script is limited to 32KiB.  
  
## FileResource

A resource that manages the state of a file.

JSON representation  
---  
      
    
    {
      "path": string,
      "state": enum ([DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DesiredState)),
      "permissions": string,
    
      // Union field source can be only one of the following:
      "file": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File))
      },
      "content": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`path` |  `string` Required. The absolute path of the file within the VM.  
`state` |  `enum (`[DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DesiredState)`)` Required. Desired state of the file.  
`permissions` |  `string` Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4  
Union field `source`. The source for the contents of the file. `source` can be only one of the following:  
`file` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#File)`)` A remote or local source.  
`content` |  `string` A file with this content. The size of the content is limited to 32KiB.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
