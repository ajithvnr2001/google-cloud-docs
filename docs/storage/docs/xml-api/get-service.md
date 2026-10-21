---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-service/
title: GET Service \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:08.221428+00:00
---

# GET Service  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  GET Service Stay organized with collections  Save and categorize content based on your preferences. 

Lists all buckets in a specified project, ordered in the list lexicographically by name.

The GET Service method is a simple GET request without a bucket or object scope. The request returns the list of buckets in an XML document in the response body. The request must be authenticated (anonymous requests will fail). By default, only the project owners group can list buckets because they are the owner of all buckets within the project. The project team and project editors groups have only view or write access to buckets, respectively.

If the GET Service request fails, it returns a [403 Forbidden](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code. The body of the error response will also contain a message describing the reason why the request failed.

The XML API does not return lists longer than 1000 buckets.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). * Not required for requests that use chunked transfer encoding. | Yes*  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-project-id](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogprojectid)` | The project ID of a project. Required unless you have set the default project for interoperable access. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax
    
    
    GET / HTTP/1.1
    Host: storage.googleapis.com
    Date: DATE
    Authorization: AUTHENTICATION_STRING
    Content-Length: 0
    x-goog-project-id: PROJECT_ID
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

Element | Description  
---|---  
ListAllMyBucketsResult | Container for bucket information.  
Buckets | Container for information about the owner's buckets.  
Bucket | Container for information about a specific bucket.  
Name | Name of the bucket.  
CreationDate | Creation date for the bucket.  
  
## Example

The following sample lists the buckets in the specified project.

**Request**
    
    
    GET / HTTP/1.1
    Host: storage.googleapis.com
    Date: Mon, 15 Feb  2010 11:00:00 GMT
    Content-Length: 0
    x-goog-project-id: 123456789123
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 648
    Content-Type: application/xml
    Date: Mon, 15 Feb  2010 11:00:01 GMT
    
    <?xml version='1.0' encoding='utf-8'?>
    <ListAllMyBucketsResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
      <Buckets>
        <Bucket>
          <Name>city-maps</Name>
          <CreationDate>2009-12-16T18:36:25.369Z</CreationDate>
        </Bucket>
        <Bucket>
          <Name>state-maps</Name>
          <CreationDate>2009-12-16T18:42:37.408Z</CreationDate>
        </Bucket>
        <Bucket>
          <Name>country-maps</Name>
          <CreationDate>2010-01-22T01:27:03.633Z</CreationDate>
        </Bucket>
      </Buckets>
    </ListAllMyBucketsResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
