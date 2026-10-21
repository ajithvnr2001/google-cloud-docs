---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies
title: REST Resource: projects.guestPolicies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:29.758013+00:00
---

# REST Resource: projects.guestPolicies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.guestPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GuestPolicy
    * JSON representation
  * Assignment
    * JSON representation
  * GroupLabel
    * JSON representation
  * OsType
    * JSON representation
  * Package
    * JSON representation
  * DesiredState
  * Manager
  * PackageRepository
    * JSON representation
  * AptRepository
    * JSON representation
  * ArchiveType
  * YumRepository
    * JSON representation
  * ZypperRepository
    * JSON representation
  * GooRepository
    * JSON representation
  * SoftwareRecipe
    * JSON representation
  * Artifact
    * JSON representation
  * Remote
    * JSON representation
  * Gcs
    * JSON representation
  * Step
    * JSON representation
  * CopyFile
    * JSON representation
  * ExtractArchive
    * JSON representation
  * ArchiveType
  * InstallMsi
    * JSON representation
  * InstallDpkg
    * JSON representation
  * InstallRpm
    * JSON representation
  * ExecFile
    * JSON representation
  * RunScript
    * JSON representation
  * Interpreter
  * Methods



## Resource: GuestPolicy

An OS Config resource representing a guest configuration policy. These policies represent the desired state for VM instance guest environments including packages to install or remove, package repository configurations, and software to install.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "assignment": {
        object ([Assignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Assignment))
      },
      "packages": [
        {
          object ([Package](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Package))
        }
      ],
      "packageRepositories": [
        {
          object ([PackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#PackageRepository))
        }
      ],
      "recipes": [
        {
          object ([SoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#SoftwareRecipe))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Required. Unique name of the resource in this project using one of the following forms: `projects/{project_number}/guestPolicies/{guestPolicyId}`.  
`description` |  `string` Description of the guest policy. Length of the description is limited to 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time this guest policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time this guest policy was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assignment` |  `object (`[Assignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Assignment)`)` Required. Specifies the VM instances that are assigned to this policy. This allows you to target sets or groups of VM instances by different parameters such as labels, names, OS, or zones.If left empty, all VM instances underneath this policy are targeted.At the same level in the resource hierarchy (that is within a project), the service prevents the creation of multiple policies that conflict with each other. For more information, see how the service [handles assignment conflicts](https://docs.cloud.google.com/compute/docs/os-config-management/create-guest-policy#handle-conflicts).  
`packages[]` |  `object (`[Package](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Package)`)` The software packages to be managed by this policy.  
`packageRepositories[]` |  `object (`[PackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#PackageRepository)`)` A list of package repositories to configure on the VM instance. This is done before any other configs are applied so they can use these repos. Package repositories are only configured if the corresponding package manager(s) are available.  
`recipes[]` |  `object (`[SoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#SoftwareRecipe)`)` A list of Recipes to install on the VM instance.  
`etag` |  `string` The etag for this guest policy. If this is provided on update, it must match the server's etag.  
  
## Assignment

An assignment represents the group or groups of VM instances that the policy applies to.

If an assignment is empty, it applies to all VM instances. Otherwise, the targeted VM instances must meet all the criteria specified. So if both labels and zones are specified, the policy applies to VM instances with those labels and in those zones.

JSON representation  
---  
      
    
    {
      "groupLabels": [
        {
          object ([GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GroupLabel))
        }
      ],
      "zones": [
        string
      ],
      "instances": [
        string
      ],
      "instanceNamePrefixes": [
        string
      ],
      "osTypes": [
        {
          object ([OsType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#OsType))
        }
      ]
    }  
  
Fields  
---  
`groupLabels[]` |  `object (`[GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GroupLabel)`)` Targets instances matching at least one of these label sets. This allows an assignment to target disparate groups, for example "env=prod or env=staging".  
`zones[]` |  `string` Targets instances in any of these zones. Leave empty to target instances in any zone.Zonal targeting is uncommon and is supported to facilitate the management of changes by zone.  
`instances[]` |  `string` Targets any of the instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`.Instance targeting is uncommon and is supported to facilitate the management of changes by the instance or to target specific VM instances for development and testing.Only supported for project-level policies and must reference instances within this project.  
`instanceNamePrefixes[]` |  `string` Targets VM instances whose name starts with one of these prefixes.Like labels, this is another way to group VM instances when targeting configs, for example prefix="prod-".Only supported for project-level policies.  
`osTypes[]` |  `object (`[OsType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#OsType)`)` Targets VM instances matching at least one of the following OS types.VM instances must match all supplied criteria for a given OsType to be included.  
  
## GroupLabel

Represents a group of VM intances that can be identified as having all these labels, for example "env=prod and app=web".

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Google Compute Engine instance labels that must be present for an instance to be included in this assignment group.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## OsType

Defines the criteria for selecting VM Instances by OS type.

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string,
      "osArchitecture": string
    }  
  
Fields  
---  
`osShortName` |  `string` Targets VM instances with OS Inventory enabled and having the following OS short name, for example "debian" or "windows".  
`osVersion` |  `string` Targets VM instances with OS Inventory enabled and having the following following OS version.  
`osArchitecture` |  `string` Targets VM instances with OS Inventory enabled and having the following OS architecture.  
  
## Package

Package is a reference to the software package to be installed or removed. The agent on the VM instance uses the system package manager to apply the config.

These are the commands that the agent uses to install or remove packages.

Apt install: `apt-get update && apt-get -y install package1 package2 package3` remove: `apt-get -y remove package1 package2 package3`

Yum install: `yum -y install package1 package2 package3` remove: `yum -y remove package1 package2 package3`

Zypper install: `zypper install package1 package2 package3` remove: `zypper rm package1 package2`

Googet install: `googet -noconfirm install package1 package2 package3` remove: `googet -noconfirm remove package1 package2 package3`

JSON representation  
---  
      
    
    {
      "name": string,
      "desiredState": enum ([DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#DesiredState)),
      "manager": enum ([Manager](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Manager))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the package. A package is uniquely identified for conflict validation by checking the package name and the manager(s) that the package targets.  
`desiredState` |  `enum (`[DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#DesiredState)`)` The desiredState the agent should maintain for this package. The default is to ensure the package is installed.  
`manager` |  `enum (`[Manager](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Manager)`)` Type of package manager that can be used to install this package. If a system does not have the package manager, the package is not installed or removed no error message is returned. By default, or if you specify `ANY`, the agent attempts to install and remove this package using the default package manager. This is useful when creating a policy that applies to different types of systems.The default behavior is ANY.  
  
## DesiredState

The desired state that the OS Config agent maintains on the VM instance.

Enums  
---  
`DESIRED_STATE_UNSPECIFIED` | The default is to ensure the package is installed.  
`INSTALLED` | The agent ensures that the package is installed.  
`UPDATED` | The agent ensures that the package is installed and periodically checks for and install any updates.  
`REMOVED` | The agent ensures that the package is not installed and uninstall it if detected.  
  
## Manager

Types of package managers that may be used to manage this package.

Enums  
---  
`MANAGER_UNSPECIFIED` | The default behavior is ANY.  
`ANY` | Apply this package config using the default system package manager.  
`APT` | Apply this package config only if Apt is available on the system.  
`YUM` | Apply this package config only if Yum is available on the system.  
`ZYPPER` | Apply this package config only if Zypper is available on the system.  
`GOO` | Apply this package config only if GooGet is available on the system.  
  
## PackageRepository

A package repository.

JSON representation  
---  
      
    
    {
    
      // Union field repository can be only one of the following:
      "apt": {
        object ([AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#AptRepository))
      },
      "yum": {
        object ([YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#YumRepository))
      },
      "zypper": {
        object ([ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ZypperRepository))
      },
      "goo": {
        object ([GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GooRepository))
      }
      // End of list of possible types for union field repository.
    }  
  
Fields  
---  
Union field `repository`. A specific type of repository. `repository` can be only one of the following:  
`apt` |  `object (`[AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#AptRepository)`)` An Apt Repository.  
`yum` |  `object (`[YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#YumRepository)`)` A Yum Repository.  
`zypper` |  `object (`[ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ZypperRepository)`)` A Zypper Repository.  
`goo` |  `object (`[GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GooRepository)`)` A Goo Repository.  
  
## AptRepository

Represents a single Apt package repository. This repository is added to a repo file that is stored at `/etc/apt/sources.list.d/google_osconfig.list`.

JSON representation  
---  
      
    
    {
      "archiveType": enum ([ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ArchiveType)),
      "uri": string,
      "distribution": string,
      "components": [
        string
      ],
      "gpgKey": string
    }  
  
Fields  
---  
`archiveType` |  `enum (`[ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ArchiveType)`)` Type of archive files in this repository. The default behavior is DEB.  
`uri` |  `string` Required. URI for this repository.  
`distribution` |  `string` Required. Distribution of this repository.  
`components[]` |  `string` Required. List of components for this repository. Must contain at least one item.  
`gpgKey` |  `string` URI of the key file for this repository. The agent maintains a keyring at `/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg` containing all the keys in any applied guest policy.  
  
## ArchiveType

Type of archive.

Enums  
---  
`ARCHIVE_TYPE_UNSPECIFIED` | Unspecified.  
`DEB` | DEB indicates that the archive contains binary files.  
`DEB_SRC` | DEB_SRC indicates that the archive contains source files.  
  
## YumRepository

Represents a single Yum package repository. This repository is added to a repo file that is stored at `/etc/yum.repos.d/google_osconfig.repo`.

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
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the Yum config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for guest policy conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
## ZypperRepository

Represents a single Zypper package repository. This repository is added to a repo file that is stored at `/etc/zypp/repos.d/google_osconfig.repo`.

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
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the zypper config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for guest policy conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
## GooRepository

Represents a Goo package repository. These is added to a repo file that is stored at C:/ProgramData/GooGet/repos/google_osconfig.repo.

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
  
## SoftwareRecipe

A software recipe is a set of instructions for installing and configuring a piece of software. It consists of a set of artifacts that are downloaded, and a set of steps that install, configure, and/or update the software.

Recipes support installing and updating software from artifacts in the following formats: Zip archive, Tar archive, Windows MSI, Debian package, and RPM package.

Additionally, recipes support executing a script (either defined in a file or directly in this api) in bash, sh, cmd, and powershell.

Updating a software recipe

If a recipe is assigned to an instance and there is a recipe with the same name but a lower version already installed and the assigned state of the recipe is `UPDATED`, then the recipe is updated to the new version.

Script Working Directories

Each script or execution step is run in its own temporary directory which is deleted after completing the step.

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "artifacts": [
        {
          object ([Artifact](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Artifact))
        }
      ],
      "installSteps": [
        {
          object ([Step](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Step))
        }
      ],
      "updateSteps": [
        {
          object ([Step](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Step))
        }
      ],
      "desiredState": enum ([DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#DesiredState))
    }  
  
Fields  
---  
`name` |  `string` Required. Unique identifier for the recipe. Only one recipe with a given name is installed on an instance.Names are also used to identify resources which helps to determine whether guest policies have conflicts. This means that requests to create multiple recipes with the same name and version are rejected since they could potentially have conflicting assignments.  
`version` |  `string` The version of this software recipe. Version can be up to 4 period separated numbers (e.g. 12.34.56.78).  
`artifacts[]` |  `object (`[Artifact](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Artifact)`)` Resources available to be used in the steps in the recipe.  
`installSteps[]` |  `object (`[Step](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Step)`)` Actions to be taken for installing this recipe. On failure it stops executing steps and does not attempt another installation. Any steps taken (including partially completed steps) are not rolled back.  
`updateSteps[]` |  `object (`[Step](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Step)`)` Actions to be taken for updating this recipe. On failure it stops executing steps and does not attempt another update for this recipe. Any steps taken (including partially completed steps) are not rolled back.  
`desiredState` |  `enum (`[DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#DesiredState)`)` Default is INSTALLED. The desired state the agent should maintain for this recipe.INSTALLED: The software recipe is installed on the instance but won't be updated to new versions. UPDATED: The software recipe is installed on the instance. The recipe is updated to a higher version, if a higher version of the recipe is assigned to this instance. REMOVE: Remove is unsupported for software recipes and attempts to create or update a recipe to the REMOVE state is rejected.  
  
## Artifact

Specifies a resource to be used in the recipe.

JSON representation  
---  
      
    
    {
      "id": string,
      "allowInsecure": boolean,
    
      // Union field artifact can be only one of the following:
      "remote": {
        object ([Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Remote))
      },
      "gcs": {
        object ([Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Gcs))
      }
      // End of list of possible types for union field artifact.
    }  
  
Fields  
---  
`id` |  `string` Required. Id of the artifact, which the installation and update steps of this recipe can reference. Artifacts in a recipe cannot have the same id.  
`allowInsecure` |  `boolean` Defaults to false. When false, recipes are subject to validations based on the artifact type:Remote: A checksum must be specified, and only protocols with transport-layer security are permitted. GCS: An object generation number must be specified.  
Union field `artifact`. A specific type of artifact. `artifact` can be only one of the following:  
`remote` |  `object (`[Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Remote)`)` A generic remote artifact.  
`gcs` |  `object (`[Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Gcs)`)` A Google Cloud Storage artifact.  
  
## Remote

Specifies an artifact available via some URI.

JSON representation  
---  
      
    
    {
      "uri": string,
      "checksum": string
    }  
  
Fields  
---  
`uri` |  `string` URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}.  
`checksum` |  `string` Must be provided if `allowInsecure` is `false`. SHA256 checksum in hex format, to compare to the checksum of the artifact. If the checksum is not empty and it doesn't match the artifact then the recipe installation fails before running any of the steps.  
  
## Gcs

Specifies an artifact available as a Google Cloud Storage object.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "object": string,
      "generation": string
    }  
  
Fields  
---  
`bucket` |  `string` Bucket of the Google Cloud Storage object. Given an example URL: `https://storage.googleapis.com/my-bucket/foo/bar#1234567` this value would be `my-bucket`.  
`object` |  `string` Name of the Google Cloud Storage object. As specified [here](https://cloud.google.com/storage/docs/naming#objectnames) Given an example URL: `https://storage.googleapis.com/my-bucket/foo/bar#1234567` this value would be `foo/bar`.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Must be provided if allowInsecure is false. Generation number of the Google Cloud Storage object. `https://storage.googleapis.com/my-bucket/foo/bar#1234567` this value would be `1234567`.  
  
## Step

An action that can be taken as part of installing or updating a recipe.

JSON representation  
---  
      
    
    {
    
      // Union field step can be only one of the following:
      "fileCopy": {
        object ([CopyFile](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#CopyFile))
      },
      "archiveExtraction": {
        object ([ExtractArchive](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ExtractArchive))
      },
      "msiInstallation": {
        object ([InstallMsi](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallMsi))
      },
      "dpkgInstallation": {
        object ([InstallDpkg](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallDpkg))
      },
      "rpmInstallation": {
        object ([InstallRpm](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallRpm))
      },
      "fileExec": {
        object ([ExecFile](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ExecFile))
      },
      "scriptRun": {
        object ([RunScript](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#RunScript))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
Union field `step`. A specific type of step. `step` can be only one of the following:  
`fileCopy` |  `object (`[CopyFile](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#CopyFile)`)` Copies a file onto the instance.  
`archiveExtraction` |  `object (`[ExtractArchive](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ExtractArchive)`)` Extracts an archive into the specified directory.  
`msiInstallation` |  `object (`[InstallMsi](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallMsi)`)` Installs an MSI file.  
`dpkgInstallation` |  `object (`[InstallDpkg](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallDpkg)`)` Installs a deb file via dpkg.  
`rpmInstallation` |  `object (`[InstallRpm](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#InstallRpm)`)` Installs an rpm file via the rpm utility.  
`fileExec` |  `object (`[ExecFile](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ExecFile)`)` Executes an artifact or local file.  
`scriptRun` |  `object (`[RunScript](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#RunScript)`)` Runs commands in a shell.  
  
## CopyFile

Copies the artifact to the specified path on the instance.

JSON representation  
---  
      
    
    {
      "artifactId": string,
      "destination": string,
      "overwrite": boolean,
      "permissions": string
    }  
  
Fields  
---  
`artifactId` |  `string` Required. The id of the relevant artifact in the recipe.  
`destination` |  `string` Required. The absolute path on the instance to put the file.  
`overwrite` |  `boolean` Whether to allow this step to overwrite existing files. If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false.  
`permissions` |  `string` Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4  
  
## ExtractArchive

Extracts an archive of the type specified in the specified directory.

JSON representation  
---  
      
    
    {
      "artifactId": string,
      "destination": string,
      "type": enum ([ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ArchiveType_1))
    }  
  
Fields  
---  
`artifactId` |  `string` Required. The id of the relevant artifact in the recipe.  
`destination` |  `string` Directory to extract archive to. Defaults to `/` on Linux or `C:\` on Windows.  
`type` |  `enum (`[ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#ArchiveType_1)`)` Required. The type of the archive to extract.  
  
## ArchiveType

Specifying the type of archive.

Enums  
---  
`ARCHIVE_TYPE_UNSPECIFIED` | Indicates that the archive type isn't specified.  
`TAR` | Indicates that the archive is a tar archive with no encryption.  
`TAR_GZIP` | Indicates that the archive is a tar archive with gzip encryption.  
`TAR_BZIP` | Indicates that the archive is a tar archive with bzip encryption.  
`TAR_LZMA` | Indicates that the archive is a tar archive with lzma encryption.  
`TAR_XZ` | Indicates that the archive is a tar archive with xz encryption.  
`ZIP` | Indicates that the archive is a zip archive.  
  
## InstallMsi

Installs an MSI file.

JSON representation  
---  
      
    
    {
      "artifactId": string,
      "flags": [
        string
      ],
      "allowedExitCodes": [
        integer
      ]
    }  
  
Fields  
---  
`artifactId` |  `string` Required. The id of the relevant artifact in the recipe.  
`flags[]` |  `string` The flags to use when installing the MSI defaults to ["/i"] (i.e. the install flag).  
`allowedExitCodes[]` |  `integer` Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]  
  
## InstallDpkg

Installs a deb via dpkg.

JSON representation  
---  
      
    
    {
      "artifactId": string
    }  
  
Fields  
---  
`artifactId` |  `string` Required. The id of the relevant artifact in the recipe.  
  
## InstallRpm

Installs an rpm file via the rpm utility.

JSON representation  
---  
      
    
    {
      "artifactId": string
    }  
  
Fields  
---  
`artifactId` |  `string` Required. The id of the relevant artifact in the recipe.  
  
## ExecFile

Executes an artifact or local file.

JSON representation  
---  
      
    
    {
      "args": [
        string
      ],
      "allowedExitCodes": [
        integer
      ],
    
      // Union field location_type can be only one of the following:
      "artifactId": string,
      "localPath": string
      // End of list of possible types for union field location_type.
    }  
  
Fields  
---  
`args[]` |  `string` Arguments to be passed to the provided executable.  
`allowedExitCodes[]` |  `integer` Defaults to [0]. A list of possible return values that the program can return to indicate a success.  
Union field `location_type`. Location of the file to execute. `location_type` can be only one of the following:  
`artifactId` |  `string` The id of the relevant artifact in the recipe.  
`localPath` |  `string` The absolute path of the file on the local filesystem.  
  
## RunScript

Runs a script through an interpreter.

JSON representation  
---  
      
    
    {
      "script": string,
      "allowedExitCodes": [
        integer
      ],
      "interpreter": enum ([Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Interpreter))
    }  
  
Fields  
---  
`script` |  `string` Required. The shell script to be executed.  
`allowedExitCodes[]` |  `integer` Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]  
`interpreter` |  `enum (`[Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Interpreter)`)` The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)).  
  
## Interpreter

The interpreter used to execute a script.

Enums  
---  
`INTERPRETER_UNSPECIFIED` | Default value for ScriptType.  
`SHELL` | Indicates that the script is run with `/bin/sh` on Linux and `cmd` on windows.  
`POWERSHELL` | Indicates that the script is run with powershell.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/create)`

|  Create an OS Config guest policy.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/delete)`

|  Delete an OS Config guest policy.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/get)`

|  Get an OS Config guest policy.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/list)`

|  Get a page of OS Config guest policies.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/patch)`

|  Update an OS Config guest policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
