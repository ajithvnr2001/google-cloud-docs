---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/domainJoinMachine/
title: Method: domains.domainJoinMachine \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:19.724675+00:00
---

# Method: domains.domainJoinMachine  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/domainJoinMachine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.domainJoinMachine Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.domains.domainJoinMachine

domains.domainJoinMachine API joins a Compute Engine VM to the domain

### HTTP request

`POST https://managedidentities.googleapis.com/v1beta1/{domain=projects/*/locations/global/domains/*}:domainJoinMachine`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`domain` |  `string` Required. The domain resource name using the form: projects/{projectId}/locations/global/domains/{domainName} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `domain`:

  * `managedidentities.domains.domainJoinMachine`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "vmIdToken": string,
      "ouName": string
    }  
  
Fields  
---  
`vmIdToken` |  `string` Required. Full instance id token of compute engine VM to verify instance identity. More about this: <https://cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature>  
`ouName` |  `string` Optional. OU name to which the VM needs to be domain joined. If the field is not provided, the VM is joined to the default OU which is created. The default OU for the domain join api is created as GCE Instances under the Cloud OU. Example - OU=GCE Instances,OU=Cloud,DC=ad,DC=test,DC=com If the field is provided, then the custom OU is searched for under GCE Instances OU. Example - if ouName=test_ou then the VM is domain joined to the following OU: OU=test_ou,OU=GCE Instances,OU=Cloud,DC=ad,DC=test,DC=com if present. If OU is not present under GCE Instances, then error is returned.  
  
### Response body

If successful, the response body contains data with the following structure:

DomainJoinMachineResponse is the response message for domains.domainJoinMachine method

JSON representation  
---  
      
    
    {
      "domainJoinBlob": string
    }  
  
Fields  
---  
`domainJoinBlob` |  `string` The response is the offline domain join blob that is returned after running the djoin command. To correctly use the response of the API, please refer to the sample usage.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
