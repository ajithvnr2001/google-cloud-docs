---
url: https://docs.cloud.google.com/php/docs/reference/auth/latest/CredentialSource.AwsNativeSource
title: Google Auth Library Client - Class AwsNativeSource (1.55.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:29.334719+00:00
---

# Google Auth Library Client - Class AwsNativeSource (1.55.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/auth/latest/CredentialSource.AwsNativeSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Auth Library Client - Class AwsNativeSource (1.55.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.55.1 (latest)  1.52.0  1.50.1  1.49.0  1.48.1  1.47.1  1.46.0  1.45.2 

Reference documentation and code samples for the Google Auth Library Client class AwsNativeSource.

Authenticates requests using AWS credentials.

## Namespace

Google \ Auth \ CredentialSource

## Implements

[ExternalAccountCredentialSourceInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/ExternalAccountCredentialSourceInterface)

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`audience` |  `string`   
The audience for the credential.  
`regionalCredVerificationUrl` |  `string`   
The regional AWS GetCallerIdentity action URL used to determine the AWS account ID and its roles. This is not called by this library, but is sent in the subject token to be called by the STS token server.  
`regionUrl` |  `string|null`   
This URL should be used to determine the current AWS region needed for the signed request construction.  
`securityCredentialsUrl` |  `string|null`   
The AWS metadata server URL used to retrieve the access key, secret key and security token needed to sign the GetCallerIdentity request.  
`imdsv2SessionTokenUrl` |  `string|null`   
Presence of this URL enforces the auth libraries to fetch a Session Token from AWS. This field is required for EC2 instances using IMDSv2.  
  
### fetchSubjectToken

**Parameter**  
---  
**Name** | **Description**  
`httpHandler` |  `?callable`   
  
  
### getCacheKey

Gets the unique key for caching For AwsNativeSource the values are: Imdsv2SessionTokenUrl.SecurityCredentialsUrl.RegionUrl.RegionalCredVerificationUrl

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### static::getImdsV2SessionToken

**Parameters**  
---  
**Name** | **Description**  
`imdsV2Url` |  `string`   
  
`httpHandler` |  `callable`   
  
  
### static::getSignedRequestHeaders

See also:

  * <http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html>



**Parameters**  
---  
**Name** | **Description**  
`region` |  `string`   
  
`host` |  `string`   
  
`accessKeyId` |  `string`   
  
`secretAccessKey` |  `string`   
  
`securityToken` |  `?string`   
  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### static::getRegionFromEnv

### static::getRegionFromUrl

**Parameters**  
---  
**Name** | **Description**  
`httpHandler` |  `callable`   
  
`regionUrl` |  `string`   
  
`headers` |  `array`   
Request headers to send in with the request.  
  
### static::getRoleName

**Parameters**  
---  
**Name** | **Description**  
`httpHandler` |  `callable`   
  
`securityCredentialsUrl` |  `string`   
  
`headers` |  `array`   
Request headers to send in with the request.  
  
### static::getSigningVarsFromUrl

**Parameters**  
---  
**Name** | **Description**  
`httpHandler` |  `callable`   
  
`securityCredentialsUrl` |  `string`   
  
`roleName` |  `string`   
  
`headers` |  `array`   
Request headers to send in with the request.  
**Returns**  
---  
**Type** | **Description**  
`array{: string, : string, : ?string}` |   
  
### static::getSigningVarsFromEcs

**Parameter**  
---  
**Name** | **Description**  
`httpHandler` |  `callable`   
  
**Returns**  
---  
**Type** | **Description**  
`array{: string, : string, : ?string}|null` |   
  
### static::getSigningVarsFromEnv

**Returns**  
---  
**Type** | **Description**  
`array{: string, : string, : ?string}` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
