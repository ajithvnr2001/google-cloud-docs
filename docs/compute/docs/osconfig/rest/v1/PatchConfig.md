---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig/
title: PatchConfig \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:55.681059+00:00
---

# PatchConfig  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  PatchConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * RebootConfig
  * AptSettings
    * JSON representation
  * Type
  * YumSettings
    * JSON representation
  * GooSettings
  * ZypperSettings
    * JSON representation
  * WindowsUpdateSettings
    * JSON representation
  * Classification
  * ExecStep
    * JSON representation
  * ExecStepConfig
    * JSON representation
  * GcsObject
    * JSON representation
  * Interpreter



Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance.

JSON representation  
---  
      
    
    {
      "rebootConfig": enum ([RebootConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#RebootConfig)),
      "apt": {
        object ([AptSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#AptSettings))
      },
      "yum": {
        object ([YumSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#YumSettings))
      },
      "goo": {
        object ([GooSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#GooSettings))
      },
      "zypper": {
        object ([ZypperSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ZypperSettings))
      },
      "windowsUpdate": {
        object ([WindowsUpdateSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#WindowsUpdateSettings))
      },
      "preStep": {
        object ([ExecStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStep))
      },
      "postStep": {
        object ([ExecStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStep))
      },
      "migInstancesAllowed": boolean,
      "skipUnpatchableVms": boolean
    }  
  
Fields  
---  
`rebootConfig` |  `enum (`[RebootConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#RebootConfig)`)` Post-patch reboot settings.  
`apt` |  `object (`[AptSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#AptSettings)`)` Apt update settings. Use this setting to override the default `apt` patch rules.  
`yum` |  `object (`[YumSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#YumSettings)`)` Yum update settings. Use this setting to override the default `yum` patch rules.  
`goo` |  `object (`[GooSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#GooSettings)`)` Goo update settings. Use this setting to override the default `goo` patch rules.  
`zypper` |  `object (`[ZypperSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ZypperSettings)`)` Zypper update settings. Use this setting to override the default `zypper` patch rules.  
`windowsUpdate` |  `object (`[WindowsUpdateSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#WindowsUpdateSettings)`)` Windows update settings. Use this override the default windows patch rules.  
`preStep` |  `object (`[ExecStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStep)`)` The `ExecStep` to run before the patch update.  
`postStep` |  `object (`[ExecStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStep)`)` The `ExecStep` to run after the patch update.  
`migInstancesAllowed` |  `boolean` Allows the patch job to run on Managed instance groups (MIGs).  
`skipUnpatchableVms` |  `boolean` Optional. Enables enhanced reporting for the patch job:

  1. The patch job skips instances that cannot be patched and reports them as `SKIPPED`. An instance cannot be patched for two reasons:
     1. The instance runs Container-Optimized OS (COS), which cannot be patched.
     2. The instance is part of a managed instance group (MIG), and patching MIG instances is disabled in the patch job's configuration (`[PatchConfig.migInstancesAllowed](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#FIELDS.mig_instances_allowed)` is `false`).
  2. The patch job is reported as `SUCCEEDED` if it completes without errors, even if some instances are `SKIPPED`.
  3. The patch job is reported as `COMPLETED_WITH_INACTIVE_VMS` if it completes without errors, but does not patch instances that are `INACTIVE`.

  
  
## RebootConfig

Post-patch reboot settings.

Enums  
---  
`REBOOT_CONFIG_UNSPECIFIED` | The default behavior is DEFAULT.  
`DEFAULT` | The agent decides if a reboot is necessary by checking signals such as registry keys on Windows or `/var/run/reboot-required` on APT based systems. On RPM based systems, a set of core system package install times are compared with system boot time.  
`ALWAYS` | Always reboot the machine after the update completes.  
`NEVER` | Never reboot the machine after the update completes.  
  
## AptSettings

Apt patching is completed by executing `apt-get update && apt-get upgrade`. Additional options can be set to control how this is executed.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Type)),
      "excludes": [
        string
      ],
      "exclusivePackages": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Type)`)` By changing the type to DIST, the patching is performed using `apt-get dist-upgrade` instead.  
`excludes[]` |  `string` List of packages to exclude from update. These packages will be excluded  
`exclusivePackages[]` |  `string` An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields.  
  
## Type

Apt patch type.

Enums  
---  
`TYPE_UNSPECIFIED` | By default, upgrade will be performed.  
`DIST` | Runs `apt-get dist-upgrade`.  
`UPGRADE` | Runs `apt-get upgrade`.  
  
## YumSettings

Yum patching is performed by executing `yum update`. Additional options can be set to control how this is executed.

Note that not all settings are supported on all platforms.

JSON representation  
---  
      
    
    {
      "security": boolean,
      "minimal": boolean,
      "excludes": [
        string
      ],
      "exclusivePackages": [
        string
      ]
    }  
  
Fields  
---  
`security` |  `boolean` Adds the `--security` flag to `yum update`. Not supported on all platforms.  
`minimal` |  `boolean` Will cause patch to run `yum update-minimal` instead.  
`excludes[]` |  `string` List of packages to exclude from update. These packages are excluded by using the yum `--exclude` flag.  
`exclusivePackages[]` |  `string` An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field must not be specified with any other patch configuration fields.  
  
## GooSettings

This type has no fields.

Googet patching is performed by running `googet update`.

## ZypperSettings

Zypper patching is performed by running `zypper patch`. See also <https://en.opensuse.org/SDB:Zypper_manual>.

JSON representation  
---  
      
    
    {
      "withOptional": boolean,
      "withUpdate": boolean,
      "categories": [
        string
      ],
      "severities": [
        string
      ],
      "excludes": [
        string
      ],
      "exclusivePatches": [
        string
      ]
    }  
  
Fields  
---  
`withOptional` |  `boolean` Adds the `--with-optional` flag to `zypper patch`.  
`withUpdate` |  `boolean` Adds the `--with-update` flag, to `zypper patch`.  
`categories[]` |  `string` Install only patches with these categories. Common categories include security, recommended, and feature.  
`severities[]` |  `string` Install only patches with these severities. Common severities include critical, important, moderate, and low.  
`excludes[]` |  `string` List of patches to exclude from update.  
`exclusivePatches[]` |  `string` An exclusive list of patches to be updated. These are the only patches that will be installed using 'zypper patch patch:' command. This field must not be used with any other patch configuration fields.  
  
## WindowsUpdateSettings

Windows patching is performed using the Windows Update Agent.

JSON representation  
---  
      
    
    {
      "classifications": [
        enum ([Classification](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Classification))
      ],
      "excludes": [
        string
      ],
      "exclusivePatches": [
        string
      ]
    }  
  
Fields  
---  
`classifications[]` |  `enum (`[Classification](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Classification)`)` Only apply updates of these windows update classifications. If empty, all updates are applied.  
`excludes[]` |  `string` List of KBs to exclude from update.  
`exclusivePatches[]` |  `string` An exclusive list of kbs to be updated. These are the only patches that will be updated. This field must not be used with other patch configurations.  
  
## Classification

Microsoft Windows update classifications as defined in [1] <https://support.microsoft.com/en-us/help/824684/description-of-the-standard-terminology-that-is-used-to-describe-micro>

Enums  
---  
`CLASSIFICATION_UNSPECIFIED` | Invalid. If classifications are included, they must be specified.  
`CRITICAL` | "A widely released fix for a specific problem that addresses a critical, non-security-related bug." [1]  
`SECURITY` | "A widely released fix for a product-specific, security-related vulnerability. Security vulnerabilities are rated by their severity. The severity rating is indicated in the Microsoft security bulletin as critical, important, moderate, or low." [1]  
`DEFINITION` | "A widely released and frequent software update that contains additions to a product's definition database. Definition databases are often used to detect objects that have specific attributes, such as malicious code, phishing websites, or junk mail." [1]  
`DRIVER` | "Software that controls the input and output of a device." [1]  
`FEATURE_PACK` | "New product functionality that is first distributed outside the context of a product release and that is typically included in the next full product release." [1]  
`SERVICE_PACK` | "A tested, cumulative set of all hotfixes, security updates, critical updates, and updates. Additionally, service packs may contain additional fixes for problems that are found internally since the release of the product. Service packs my also contain a limited number of customer-requested design changes or features." [1]  
`TOOL` | "A utility or feature that helps complete a task or set of tasks." [1]  
`UPDATE_ROLLUP` | "A tested, cumulative set of hotfixes, security updates, critical updates, and updates that are packaged together for easy deployment. A rollup generally targets a specific area, such as security, or a component of a product, such as Internet Information Services (IIS)." [1]  
`UPDATE` | "A widely released fix for a specific problem. An update addresses a noncritical, non-security-related bug." [1]  
  
## ExecStep

A step that runs an executable for a PatchJob.

JSON representation  
---  
      
    
    {
      "linuxExecStepConfig": {
        object ([ExecStepConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStepConfig))
      },
      "windowsExecStepConfig": {
        object ([ExecStepConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStepConfig))
      }
    }  
  
Fields  
---  
`linuxExecStepConfig` |  `object (`[ExecStepConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStepConfig)`)` The ExecStepConfig for all Linux VMs targeted by the PatchJob.  
`windowsExecStepConfig` |  `object (`[ExecStepConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#ExecStepConfig)`)` The ExecStepConfig for all Windows VMs targeted by the PatchJob.  
  
## ExecStepConfig

Common configurations for an ExecStep.

JSON representation  
---  
      
    
    {
      "allowedSuccessCodes": [
        integer
      ],
      "interpreter": enum ([Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Interpreter)),
    
      // Union field executable can be only one of the following:
      "localPath": string,
      "gcsObject": {
        object ([GcsObject](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#GcsObject))
      }
      // End of list of possible types for union field executable.
    }  
  
Fields  
---  
`allowedSuccessCodes[]` |  `integer` Defaults to [0]. A list of possible return values that the execution can return to indicate a success.  
`interpreter` |  `enum (`[Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#Interpreter)`)` The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)).  
Union field `executable`. Location of the executable. `executable` can be only one of the following:  
`localPath` |  `string` An absolute path to the executable on the VM.  
`gcsObject` |  `object (`[GcsObject](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#GcsObject)`)` A Cloud Storage object containing the executable.  
  
## GcsObject

Cloud Storage object representation.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "object": string,
      "generationNumber": string
    }  
  
Fields  
---  
`bucket` |  `string` Required. Bucket of the Cloud Storage object.  
`object` |  `string` Required. Name of the Cloud Storage object.  
`generationNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Generation number of the Cloud Storage object. This is used to ensure that the ExecStep specified by this PatchJob does not change.  
  
## Interpreter

The interpreter used to run the file.

Enums  
---  
`INTERPRETER_UNSPECIFIED` | If the interpreter is not specified, the value defaults to `NONE`.  
`NONE` | Indicates that the file is run as follows on each operating system: + For Linux VMs, the file is ran as an executable and the interpreter might be parsed from the [shebang line](<https://wikipedia.org/wiki/Shebang_(Unix)>) of the file. + For Windows VM, this value is not supported.  
`SHELL` | Indicates that the file is run with `/bin/sh` on Linux and `cmd` on Windows.  
`POWERSHELL` | Indicates that the file is run with PowerShell.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
