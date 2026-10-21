---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-create/
title: Create an HMAC key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:07.770539+00:00
---

# Create an HMAC key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Create an HMAC key Stay organized with collections  Save and categorize content based on your preferences. 

To create a new HMAC key for the specified service account, make a `POST` request that is scoped to a project. The authenticated user must have `storage.hmacKeys.create` permission for the project in which the key will be created.

For general information about HMAC keys in Cloud Storage, see [HMAC Keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

## HTTP Request
    
    
    POST https://storage.googleapis.com/?Action=CreateAccessKey&UserName=ServiceAccountEmail

### Query string parameters

Parameter | Description | Required  
---|---|---  
`Action` | The HMAC key operation to be performed. | Yes  
`UserName` | The email address of the service account. | Yes  
  
## Request headers

Use the [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-key#request-headers).

## Response

If successful, this method returns a response body with the following structure:
    
    
    <CreateAccessKeyResponse>
      <CreateAccessKeyResult>
        <AccessKey>
          <UserName>serviceAccount@proj.iam.gserviceaccount.com</UserName>
          <AccessKeyId>GOOG1EXAMPLEAEU</AccessKeyId>
          <Status>Active</Status>
          <SecretAccessKey>EXAMPLE/KEY/aserafd</SecretAccessKey>
        </AccessKey>
      </CreateAccessKeyResult>
    </CreateAccessKeyResponse>
    

Parameter name | Value | Description  
---|---|---  
`UserName` | `string` |  The email address of the service account.   
`AccessKeyId` | `string` |  The access key ID for this HMAC key.   
`Status` | `string` | The status of this HMAC key. Valid values are: 

  * `Active`: This key can be used to sign requests.
  * `Inactive`: Requests signed with this key will be denied.

  
`SecretAccessKey` | `string` | A 40 character Base-64 encoded string that is used to sign requests as part of the authentication process. This secret is only ever returned in the `create` request.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
