---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate/
title: Method: projects.locations.memberships.validateCreate \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:07.169712+00:00
---

# Method: projects.locations.memberships.validateCreate  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.validateCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * ValidationResult
    * JSON representation
  * ValidationResult.ValidatorType
  * Examples
  * Try it!



memberships.validateCreate is a preflight check for memberships.create. It checks the following: 1. Caller has the required `gkehub.memberships.create` permission. 2. The membershipId is still available.

### HTTP request

`POST https://gkehub.googleapis.com/v1alpha/{parent=projects/*/locations/*}/memberships:validateCreate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the Memberships will be created. Specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.memberships.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "membershipId": string,
      "membership": {
        object ([Membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership))
      }
    }  
  
Fields  
---  
`membershipId` |  `string` Required. Client chosen membership id.  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership)`)` Required. Membership resource to be created.  
  
### Response body

Response message for the `GkeHub.ValidateCreateMembership` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "validationResults": [
        {
          object ([ValidationResult](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate#ValidationResult))
        }
      ]
    }  
  
Fields  
---  
`validationResults[]` |  `object (`[ValidationResult](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate#ValidationResult)`)` Wraps all the validator results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ValidationResult

ValidationResults are results set by each validator running during memberships.validateCreate.

JSON representation  
---  
      
    
    {
      "validator": enum ([ValidationResult.ValidatorType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate#ValidationResult.ValidatorType)),
      "success": boolean,
      "result": string
    }  
  
Fields  
---  
`validator` |  `enum (`[ValidationResult.ValidatorType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate#ValidationResult.ValidatorType)`)` Validator type to validate membership with.  
`success` |  `boolean` Whether the validation is passed or not.  
`result` |  `string` Additional information for the validation.  
  
## ValidationResult.ValidatorType

Specifies different types of validation.

Enums  
---  
`VALIDATOR_TYPE_UNSPECIFIED` | UNSPECIFIED validator.  
`MEMBERSHIP_ID` | MEMBERSHIP_ID validator validates that the membershipId is still available.  
`CROSS_PROJECT_PERMISSION` | CROSS_PROJECT_PERMISSION validator validates that the cross-project role binding for the service agent is in place.  
`FLEET_ALLOWED_FOR_PROJECT_GUARDRAIL` | FLEET_ALLOWED_FOR_PROJECT_GUARDRAIL validator validates that the fleet project is allowed for the project guardrail.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
