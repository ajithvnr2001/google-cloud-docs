---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/patch/
title: Method: apps.authorizedCertificates.patch \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:59.869904+00:00
---

# Method: apps.authorizedCertificates.patch  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.authorizedCertificates.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update `certificate_data` with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate `displayName` may also be updated.

### HTTP request

`PATCH https://appengine.googleapis.com/v1beta/{name=apps/*/authorizedCertificates/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/authorizedCertificates/12345`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Standard field mask for the set of fields to be updated. Updates are only supported on the `certificateRawData` and `displayName` fields.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates#AuthorizedCertificate)`.

### Response body

If successful, the response body contains an instance of `[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates#AuthorizedCertificate)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
