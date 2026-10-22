---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-retention/
title: Set object retention \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:55.576652+00:00
---

# Set object retention  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Set object retention Stay organized with collections  Save and categorize content based on your preferences. 

To add or modify the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) for an existing object, you make a PUT request that is scoped to the object, and you use the `retention` query string parameter. You must also include an XML document in the request body that contains the retention configuration that you want to apply. A retention configuration cannot be removed or shortened if its mode is set to `COMPLIANCE`.

You can also specify a retention configuration at the time you upload an object.

You must have `FULL_CONTROL` permission to apply a retention configuration to an existing object.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[retention](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#retention)` | Scopes the request to add or modify the retention configuration for an object. You must specify the retention configuration in an XML document in the request body. | No  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | Specifies the generation on which to set the retention configuration. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[x-goog-bypass-governance-retention](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogbypassgovernanceretention)` | Must be set to `true` in order to remove an existing retention configuration, make an existing retention configuration shorter, or set the mode of an existing retention configuration to `COMPLIANCE`. | No  
  
## Request body elements

The following request body elements are applicable only if you use the `retention` query string parameter to add or modify a retention configuration for an existing object. All elements are required.

Element | Description  
---|---  
`Retention` | Container for object's retention configuration.  
`Mode` | Mode of the object retention configuration. `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode.  
`RetainUntilDate` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable.  
  
## Request syntax

The following syntax applies to PUT Object requests that use the `retention` query string parameter and that scope the request to a specific object generation.
    
    
    PUT /OBJECT_NAME?retention&generation=GENERATION_NUMBER HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Authorization: AUTHENTICATION_STRING
    
    XML_DOCUMENT_DEFINING_RETENTION_CONFIGURATION
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample applies a retention configuration to the `london.jpg` object, which is stored in the `travel-maps` bucket. The configuration sets the `Mode` to be `GOVERNANCE` and the `RetainUntilDate` to be `2028-02-15T05:30:00Z`.

**Request**
    
    
    PUT /london.jpg?retention HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Mon, 16 Oct 2023 17:08:44 GMT
    Content-Length: 138
    Content-Type=application/xml; charset=UTF-8
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Retention>
      <Mode>
        GOVERNANCE
      </Mode>
      <RetainUntilDate>
        2028-02-15T05:30:00Z
      </RetainUntilDate>
    </Retention>
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Mon, 16 Oct 2023 17:08:45 GMT
    Content-Length: 0
    Content-Type: text/html
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
