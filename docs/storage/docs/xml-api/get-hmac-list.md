---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-hmac-list/
title: List HMAC keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:09.599451+00:00
---

# List HMAC keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-hmac-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  List HMAC keys Stay organized with collections  Save and categorize content based on your preferences. 

To retrieve a list of HMAC keys for the specified service account, make a `GET` request that is scoped to a project. The authenticated user must have `storage.hmacKeys.list` permission for the project in which the key exists.

For general information about HMAC keys in Cloud Storage, see [HMAC Keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

## HTTP Request
    
    
    GET https://storage.googleapis.com/?Action=ListAccessKeys&UserName=ServiceAccountEmail

### Query string parameters

Parameter | Description | Required  
---|---|---  
`Action` | The HMAC key operation to be performed. | Yes  
`MaxItems` | Maximum number of keys to return in a single response. The service may return fewer results than `MaxItems`. Check for a `Marker` in the result and paginate if necessary. | No  
`Marker` | A previously-returned page token representing part of the larger set of results to view. This is meant to be an opaque token and the format may change at any time. Attempting to build your own instead of using one returned by a previous `list` request is not supported.  
  
If you start a listing and then create a new HMAC key before using a `Marker` to continue listing, you will not see the new HMAC key in subsequent listing results if it is in part of the HMAC key namespace already listed. | No  
`UserName` | The email address of a service account in the project. Specifying this parameter will filter the list results to only return keys for this service account. | No  
  
## Request headers

The following are request headers for GET HMAC Key.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Response

If successful, this method returns a response body with the following structure:
    
    
    <ListAccessKeysResponse>
      <ListAccessKeysResult>
        <UserName>serviceAccount@proj.iam.gserviceaccount.com</UserName>
        <AccessKeyMetadata>
           <member>
              <UserName>serviceAccount@proj.iam.gserviceaccount.com</UserName>
              <AccessKeyId>GOOG1EXAMPLE12345</AccessKeyId>
              <Status>Active</Status>
            <CreateDate>2019-09-03T18:53:41Z</CreateDate>
           </member>
           <member>
              <UserName>serviceAccount@proj.iam.gserviceaccount.com</UserName>
              <AccessKeyId>GOOG1EXAMPLE54321</AccessKeyId>
              <Status>Inactive</Status>
            <CreateDate>2019-03-25T20:38:14Z</CreateDate>
           </member>
        </AccessKeyMetadata>
        <IsTruncated>true</IsTruncated>
        <Marker>AERPALERN/NEXT/TOKEN</Marker>
      </ListAccessKeysResult>
    </ListAccessKeysResponse>
    

Parameter name | Value | Description  
---|---|---  
`UserName` | `string` |  The email address of the service account.   
`AccessKeyId` | `string` |  The access key ID for this HMAC key.   
`Status` | `string` | The status of this HMAC key. Valid values are: 

  * `Active`: This key can be used to sign requests.
  * `Inactive`: Requests signed with this key will be denied.
  * `Deleted`: Requests signed with this key will be denied.

  
`CreateDate` | `datetime` | The creation time of the HMAC key in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.   
`IsTruncated` | `boolean` | `true` if there are additional pages of keys. `false` otherwise. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results.  
`Marker` | `string` | The continuation token, used to page through large result sets. Only included in the response if `IsTruncated` is `true`. Provide this value in subsequent `list` requests until `IsTruncated` is `false`. Note that the next page may be empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
