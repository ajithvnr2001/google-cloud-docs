---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups.members/list/
title: Method: projects.groups.members.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:12.337009+00:00
---

# Method: projects.groups.members.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups.members/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.groups.members.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the monitored resources that are members of a group.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/members`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The group whose members are listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
      
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` A positive number that is the maximum number of results to return.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`filter` |  `string` An optional [list filter](https://cloud.google.com/monitoring/api/learn_more#filtering) describing the members to be returned. The filter may reference the type, labels, and metadata of monitored resources that comprise the group. For example, to return only resources representing Compute Engine VM instances, use this filter:
    
    
    `resource.type = "gce_instance"`
      
  
`interval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval)`)` An optional time interval for which results should be returned. Only members that were part of the group during the specified interval are included in the response. If no interval is provided then the group membership over the last minute is returned.  
  
### Request body

The request body must be empty.

### Response body

The `members.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "members": [
        {
          object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`members[]` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` A set of monitored resources in the group.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
`totalSize` |  `integer` The total number of elements matching this request.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
