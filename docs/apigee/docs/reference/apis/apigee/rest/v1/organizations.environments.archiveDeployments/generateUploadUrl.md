---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateUploadUrl/
title: Method: organizations.environments.archiveDeployments.generateUploadUrl \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:51.598369+00:00
---

# Method: organizations.environments.archiveDeployments.generateUploadUrl  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateUploadUrl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.archiveDeployments.generateUploadUrl Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Generates a signed URL for uploading an Archive zip file to Google Cloud Storage. Once the upload is complete, the signed URL should be passed to archiveDeployments.create.

When uploading to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * Source file size should not exceed 1GB limit.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, these two headers need to be specified:

  * `content-type: application/zip`
  * `x-goog-content-length-range: 0,1073741824`



And this header SHOULD NOT be specified:

  * `Authorization: Bearer YOUR_TOKEN`



### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/archiveDeployments:generateUploadUrl`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The organization and environment to upload to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.archivedeployments.upload`

  
  
### Request body

The request body must be empty.

### Response body

Response for archiveDeployments.generateUploadUrl method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "uploadUri": string
    }  
  
Fields  
---  
`uploadUri` |  `string` The Google Cloud Storage signed URL that can be used to upload a new Archive zip file.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
