---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list/
title: Method: projects.groups.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.846932+00:00
---

# Method: projects.groups.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.groups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the existing groups.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/groups`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose groups are to be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` A positive number that is the maximum number of results to return.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
An optional filter consisting of a single group name. The filters limit the groups returned based on their parent-child relationship with the specified group. If no filter is specified, all groups are returned. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`childrenOfGroup` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns groups whose `parentName` field contains the group name. If no groups have this parent, the results are empty.  
`ancestorsOfGroup` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns groups that are ancestors of the specified group. The groups are returned in order, starting with the immediate parent and ending with the most distant ancestor. If the specified group has no immediate parent, the results are empty.  
`descendantsOfGroup` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns the descendants of the specified group. This is a superset of the results returned by the `childrenOfGroup` filter, and includes children-of-children, and so forth.  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

The `groups.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "group": [
        {
          object ([Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`group[]` |  `object (`[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group)`)` The groups that match the specified filters.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
