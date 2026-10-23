---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object-retention/
title: Get object retention \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:43.072834+00:00
---

# Get object retention  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Get object retention Stay organized with collections  Save and categorize content based on your preferences. 

To get an object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) you make a GET request that is scoped to the object, and you use the `retention` query string parameter. If the object has a retention configuration, the configuration is returned in an XML document in the response body. Otherwise, the request fails with a `404 Not Found` response.

You must have `READ` permission to get an object's retention configuration.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[retention](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#retention)` | Return the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). | No  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | Specifies the generation on which to set the retention configuration. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-object#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Object requests that use the `retention` query string parameter.
    
    
    GET /OBJECT_NAME?retention&generation=GENERATION HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Content-Length: 0
    Content-Type: TYPE
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements are applicable only if you use the `retention` query string parameter.

Element | Description  
---|---  
`Retention` | Container for an object's retention configuration.  
`Mode` | Mode of the object retention configuration. `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode.  
`RetainUntilDate` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that indicates the time until which the object is retained as immutable.  
  
## Examples

The following example retrieves the retention configuration for an object named `tokyo.jpg`.

**Request**
    
    
    GET /tokyo.jpg?retention HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 138
    Content-Type: application/xml; charset=UTF-8
    Date: Tue, 01 Nov 2016 17:12:32 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Retention>
      <Mode>
        GOVERNANCE
      </Mode>
      <RetainUntilDate>
        2028-04-12T23:20:00Z
      </RetainUntilDate>
    </Retention>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
