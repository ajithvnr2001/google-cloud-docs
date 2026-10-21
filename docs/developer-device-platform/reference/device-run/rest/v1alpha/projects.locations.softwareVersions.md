---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions
title: REST Resource: projects.locations.softwareVersions \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:56.721025+00:00
---

# REST Resource: projects.locations.softwareVersions  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  REST Resource: projects.locations.softwareVersions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SoftwareVersion
    * JSON representation
  * AndroidxTestOrchestratorDetails
  * XcodeDetails
    * JSON representation
  * SoftwareType
  * Methods



## Resource: SoftwareVersion

A single software version in the catalog.

JSON representation  
---  
      
    
    {
      "name": string,
      "softwareType": enum ([SoftwareType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#SoftwareType)),
      "displayName": string,
      "version": string,
      "lifecycle": {
        object ([Lifecycle](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle))
      },
      "isDefault": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "androidxTestOrchestratorDetails": {
        object ([AndroidxTestOrchestratorDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#AndroidxTestOrchestratorDetails))
      },
      "xcodeDetails": {
        object ([XcodeDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#XcodeDetails))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Identifies the software version resource. Format: `projects/{project}/locations/{location}/softwareVersions/{software_version}`. The {software_version} segment is an opaque, stable string. Clients must not parse it to derive or assume the version.  
`softwareType` |  `enum (`[SoftwareType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#SoftwareType)`)` Output only. Specifies which software this is a version of.Filter on this field to narrow the collection to a single kind of software, for example `softwareType = "ANDROIDX_TEST_ORCHESTRATOR"`.  
`displayName` |  `string` Output only. Provides a human-readable name for this version, ex. "Android Test Orchestrator 1.4.1".  
`version` |  `string` Output only. Specifies the version identifier, ex. "1.4.1". Unique within a `softwareType`.  
`lifecycle` |  `object (`[Lifecycle](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle)`)` Output only. The version lifecycle (maturity stage and removal date).  
`isDefault` |  `boolean` Output only. Indicates whether the system uses this version when a request does not select one explicitly. Exactly one version per `softwareType` is the default, and it may change over time.  
Contains software-specific attributes. The field that is set matches `software_type`. It is type-safe, so one kind of software can never carry another's fields.Filterable by dot-path, for example `androidx_test_orchestrator_details.some_field = "value"`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`androidxTestOrchestratorDetails` |  `object (`[AndroidxTestOrchestratorDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#AndroidxTestOrchestratorDetails)`)` Output only. Contains Android Test Orchestrator-specific attributes (set when softwareType == ANDROIDX_TEST_ORCHESTRATOR).  
`xcodeDetails` |  `object (`[XcodeDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions#XcodeDetails)`)` Output only. Contains Xcode-specific attributes (set when softwareType == XCODE).  
End of mutually exclusive fields.  
  
## AndroidxTestOrchestratorDetails

This type has no fields.

Android Test Orchestrator-specific attributes. Reserved for future orchestrator-only fields.

## XcodeDetails

Xcode-specific attributes.

JSON representation  
---  
      
    
    {
      "supportedIosVersions": [
        string
      ]
    }  
  
Fields  
---  
`supportedIosVersions[]` |  `string` Output only. Lists the iOS versions this Xcode can run tests against, ex. "16.6". This is a property of the toolchain, so it says nothing about whether a device on that iOS version is available; list the `Device` collection to find out.  
  
## SoftwareType

The kind of software a version belongs to.

New values may be added in the future.

Enums  
---  
`SOFTWARE_TYPE_UNSPECIFIED` | Software type not specified.  
`ANDROIDX_TEST_ORCHESTRATOR` | Android Test Orchestrator, which runs each Android instrumentation test case in its own process.  
`XCODE` | Apple Xcode, the toolchain that builds and runs iOS XCTests.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions/get)`

|  Returns information about a specific software version.  
  
### `[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions/list)`

|  Lists all software packages in lab and their versions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
