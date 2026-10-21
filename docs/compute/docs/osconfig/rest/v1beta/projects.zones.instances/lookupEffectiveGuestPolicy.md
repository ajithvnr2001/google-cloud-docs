---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy/
title: Method: projects.zones.instances.lookupEffectiveGuestPolicy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:47.691348+00:00
---

# Method: projects.zones.instances.lookupEffectiveGuestPolicy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.zones.instances.lookupEffectiveGuestPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * SourcedPackage
    * JSON representation
  * SourcedPackageRepository
    * JSON representation
  * SourcedSoftwareRecipe
    * JSON representation
  * Try it!



Lookup the effective guest policy that applies to a VM instance. This lookup merges all policies that are assigned to the instance ancestry.

### HTTP request

`POST https://osconfig.googleapis.com/v1beta/{instance=projects/*/zones/*/instances/*}:lookupEffectiveGuestPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The VM instance whose policies are being looked up.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string,
      "osArchitecture": string
    }  
  
Fields  
---  
`osShortName` |  `string` Short name of the OS running on the instance. The OS Config agent only provides this field for targeting if OS Inventory is enabled for that instance.  
`osVersion` |  `string` Version of the OS running on the instance. The OS Config agent only provides this field for targeting if OS Inventory is enabled for that VM instance.  
`osArchitecture` |  `string` Architecture of OS running on the instance. The OS Config agent only provides this field for targeting if OS Inventory is enabled for that instance.  
  
### Response body

The effective guest policy that applies to a VM instance.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "packages": [
        {
          object ([SourcedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedPackage))
        }
      ],
      "packageRepositories": [
        {
          object ([SourcedPackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedPackageRepository))
        }
      ],
      "softwareRecipes": [
        {
          object ([SourcedSoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedSoftwareRecipe))
        }
      ]
    }  
  
Fields  
---  
`packages[]` |  `object (`[SourcedPackage](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedPackage)`)` List of package configurations assigned to the VM instance.  
`packageRepositories[]` |  `object (`[SourcedPackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedPackageRepository)`)` List of package repository configurations assigned to the VM instance.  
`softwareRecipes[]` |  `object (`[SourcedSoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy#SourcedSoftwareRecipe)`)` List of recipes assigned to the VM instance.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## SourcedPackage

A guest policy package including its source.

JSON representation  
---  
      
    
    {
      "source": string,
      "package": {
        object ([Package](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Package))
      }
    }  
  
Fields  
---  
`source` |  `string` Name of the guest policy providing this config.  
`package` |  `object (`[Package](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#Package)`)` A software package to configure on the VM instance.  
  
## SourcedPackageRepository

A guest policy package repository including its source.

JSON representation  
---  
      
    
    {
      "source": string,
      "packageRepository": {
        object ([PackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#PackageRepository))
      }
    }  
  
Fields  
---  
`source` |  `string` Name of the guest policy providing this config.  
`packageRepository` |  `object (`[PackageRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#PackageRepository)`)` A software package repository to configure on the VM instance.  
  
## SourcedSoftwareRecipe

A guest policy recipe including its source.

JSON representation  
---  
      
    
    {
      "source": string,
      "softwareRecipe": {
        object ([SoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#SoftwareRecipe))
      }
    }  
  
Fields  
---  
`source` |  `string` Name of the guest policy providing this config.  
`softwareRecipe` |  `object (`[SoftwareRecipe](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#SoftwareRecipe)`)` A software recipe to configure on the VM instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
