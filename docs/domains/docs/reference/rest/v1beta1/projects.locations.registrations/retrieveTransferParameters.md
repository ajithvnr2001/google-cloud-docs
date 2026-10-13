---
url: https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveTransferParameters/
title: Method: projects.locations.registrations.retrieveTransferParameters \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:59.131788+00:00
---

# Method: projects.locations.registrations.retrieveTransferParameters  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveTransferParameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Reference ](https://docs.cloud.google.com/domains/docs/apis)



Send feedback 

#  Method: projects.locations.registrations.retrieveTransferParameters Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * TransferParameters
    * JSON representation
  * Try it!



This item is deprecated!

Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains already managed by [Google Domains](https://domains.google/), use `registrations.import` instead.

Use the returned values to call `registrations.transfer`.

### HTTP request

`GET https://domains.googleapis.com/v1beta1/{location=projects/*/locations/*}/registrations:retrieveTransferParameters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. The location. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `location`:

  * `domains.registrations.list`

  
  
### Query parameters

Parameters  
---  
`domainName` |  `string` Required. The domain name. Unicode domain names must be expressed in Punycode format.  
  
### Request body

The request body must be empty.

### Response body

This item is deprecated!

Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations). Response for the `registrations.retrieveTransferParameters` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transferParameters": {
        object ([TransferParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveTransferParameters#TransferParameters))
      }
    }  
  
Fields  
---  
`transferParameters` |  `object (`[TransferParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveTransferParameters#TransferParameters)`)` Parameters to use when calling the `registrations.transfer` method.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## TransferParameters

This item is deprecated!

Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations). Parameters required to transfer a domain from another registrar.

JSON representation  
---  
      
    
    {
      "domainName": string,
      "currentRegistrar": string,
      "currentRegistrarUri": string,
      "nameServers": [
        string
      ],
      "transferLockState": enum ([TransferLockState](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations#TransferLockState)),
      "supportedPrivacy": [
        enum ([ContactPrivacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations#ContactPrivacy))
      ],
      "yearlyPrice": {
        object ([Money](https://docs.cloud.google.com/domains/docs/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`domainName` |  `string` The domain name. Unicode domain names are expressed in Punycode format.  
`currentRegistrar` |  `string` The registrar that currently manages the domain.  
`currentRegistrarUri` |  `string` The URL of the registrar that currently manages the domain.  
`nameServers[]` |  `string` The name servers that currently store the configuration of the domain.  
`transferLockState` |  `enum (`[TransferLockState](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations#TransferLockState)`)` Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar.  
`supportedPrivacy[]` |  `enum (`[ContactPrivacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations#ContactPrivacy)`)` Contact privacy options that the domain supports.  
`yearlyPrice` |  `object (`[Money](https://docs.cloud.google.com/domains/docs/reference/rest/Shared.Types/Money)`)` Price to transfer or renew the domain for one year.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
