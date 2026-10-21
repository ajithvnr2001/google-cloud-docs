---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list/
title: Method: uptimeCheckIps.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:17.569241+00:00
---

# Method: uptimeCheckIps.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: uptimeCheckIps.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * UptimeCheckIp
    * JSON representation
  * Try it!



Returns the list of IP addresses that checkers run from.

### HTTP request

`GET https://monitoring.googleapis.com/v3/uptimeCheckIps`

### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of results to return in a single response. The server may further constrain the maximum number of results returned in a single page. If the pageSize is <=0, the server will decide the number of results to be returned. NOTE: this field is not yet implemented  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call. NOTE: this field is not yet implemented  
  
### Request body

The request body must be empty.

### Response body

The protocol for the `uptimeCheckIps.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "uptimeCheckIps": [
        {
          object ([UptimeCheckIp](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list#UptimeCheckIp))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`uptimeCheckIps[]` |  `object (`[UptimeCheckIp](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list#UptimeCheckIp)`)` The returned list of IP addresses (including region and location) that the checkers run from.  
`nextPageToken` |  `string` This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the nextPageToken is passed to the subsequent List method call (in the request message's pageToken field). NOTE: this field is not yet implemented  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## UptimeCheckIp

Contains the region, location, and list of IP addresses where checkers in the location run from.

JSON representation  
---  
      
    
    {
      "region": enum ([UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckRegion)),
      "location": string,
      "ipAddress": string
    }  
  
Fields  
---  
`region` |  `enum (`[UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckRegion)`)` A broad region category in which the IP address is located.  
`location` |  `string` A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category.  
`ipAddress` |  `string` The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
