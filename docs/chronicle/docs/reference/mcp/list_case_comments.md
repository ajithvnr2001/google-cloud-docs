---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:51.939730+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_case_comments`

Lists all case comments for a given case in Google SecOps.

Retrieves a paginated list of all comments associated with a specific SOAR case, allowing for a comprehensive overview of the investigation history. This tool is essential for understanding the timeline of a case, reviewing actions taken, and gathering context from analyst notes.

**Workflow Integration:** \- Used to build a complete timeline of an investigation in a SOAR UI or report. - Essential for generating audit trails or summaries of case activity for compliance or review. - Enables analysts to programmatically search and filter through all comments to find relevant information, such as notes from a specific user or comments made during a certain time frame. - Provides the necessary context for automated playbooks to make decisions based on the history of a case.

**Use Cases:** \- Generate a complete audit trail of all actions and notes for a specific case to understand the investigation process. - Find a specific comment by filtering based on the user who wrote it, its content, or other metadata. - Display a chronological history of comments on a case detail page in a custom security dashboard. - Automate the process of reviewing cases by searching for keywords in comments.

**Filtering and Ordering:** \- The 'filter' parameter allows for precise searching within comments. You can filter on fields like 'user', 'comment' content, 'create_time', and more. - The 'order_by' parameter controls the sorting of the returned comments. You can sort by fields like 'create_time' or 'update_time' in ascending or descending order.

Args: project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). case_id (str): The numeric Case ID to list comments for (e.g., '12345'). This is a required field. page_size (int, optional): The maximum number of comments to return in a single response. If unspecified, the server will use a default page size. The maximum value is 1000. page_token (str, optional): A token for fetching a specific page of results. This is obtained from a previous call to list_case_comments. filter (str, optional): A filter string to apply to the list of comments. Supported fields include 'CreateTime', 'UpdateTime', 'User', 'Comment', 'DeletedByUser', 'IsFavorite', 'AlertIdentifier', and 'IsDeleted'. Example: filter="User='GUID' AND Comment='suspicious'" order_by (str, optional): A comma-separated list of fields to sort the results by. Add 'desc' for descending order. Supported fields are the same as for filtering. Example: "CreateTime desc"

Returns: ListCaseCommentsResponse: A response object containing a list of CaseComment objects and a next_page_token if more results are available. Each CaseComment object contains the following key fields: - `Name` (str): The full resource name of the comment. - `Id` (int): The unique identifier for the comment. - `Comment` (str): The content of the comment. - `UserOwnerFullName` (str): The full name of the user who created the comment. - `LastEditorFullName` (str): The full name of the user who last edited the comment. - `CreateTime` (int): The creation timestamp of the comment in milliseconds. - `UpdateTime` (int): The last update timestamp of the comment in milliseconds. - `IsFavorite` (bool): Indicates if the comment is marked as a favorite. - `IsDeleted` (bool): Indicates if the comment has been deleted. - `AlertIdentifier` (str): The identifier of the alert associated with the comment, if any. Returns an error message if the parent case is not found or the request is invalid.

Example Usage: # List all comments for a specific case list_case_comments(project_id='123', region='us', customer_id='abc', case_id='456')
    
    
    # List comments from a specific user, sorted by update time
            list_case_comments(project_id='123', region='us', customer_id='abc', case_id='456', filter="user='user@example.com'", order_by="update_time desc")
            

Next Steps (using MCP-enabled tools): - Iterate through the list of comments to extract key information or indicators. - Use 'create_case_comment' to add a new comment to the case based on your findings. - Use 'get_case_comment' with a comment's resource name to fetch its full details if needed.

The following sample demonstrate how to use `curl` to invoke the `list_case_comments` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_case_comments",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for ListCaseComments. Next ID: 9

### ListCaseCommentsRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "caseId": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`caseId` |  `string` Case ID.  
`pageSize` |  `integer` Page size.  
`pageToken` |  `string` Page token.  
`filter` |  `string` Filter.  
`orderBy` |  `string` Order by.  
  
## Output Schema

Response message for ListCaseComments.

### ListCaseCommentsResponse

JSON representation  
---  
      
    
    {
      "caseComments": [
        {
          object ([CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments#Output.Schema.CaseComment))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`caseComments[]` |  `object (`[CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments#Output.Schema.CaseComment)`)` The list of CaseComments.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of CaseComments.  
  
### CaseComment

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "user": string,
      "comment": string,
      "deletionInvoker": string,
      "alertIdentifier": string,
      "caseAttachment": {
        object ([CaseAttachment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments#Output.Schema.CaseAttachment))
      },
      "userOwnerFullName": string,
      "lastEditorFullName": string,
      "deletedByUser": string,
      "case": string,
    
      // Union field _is_favorite can be only one of the following:
      "isFavorite": boolean
      // End of list of possible types for union field _is_favorite.
    
      // Union field _is_deleted can be only one of the following:
      "isDeleted": boolean
      // End of list of possible types for union field _is_deleted.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The unique name(ID) of the CaseComment. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseComments/{case_comment}  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timestamp when the comment was created.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timestamp when the comment was last updated.  
`user` |  `string` Output only. User owner of the comment.  
`comment` |  `string` Required. The content of the comment.  
`deletionInvoker` |  `string` Output only. The user who deleted the comment.  
`alertIdentifier` |  `string` Optional. The alert associated with the comment.  
`caseAttachment` |  `object (`[CaseAttachment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_case_comments#Output.Schema.CaseAttachment)`)` Optional. The attachment associated with the comment.  
`userOwnerFullName` |  `string` Output only. The user who created the comment.  
`lastEditorFullName` |  `string` Output only. The user who last edited the comment.  
`deletedByUser` |  `string` Output only. The user who deleted the comment.  
`case` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The case associated with the comment.  
Union field `_is_favorite`.`_is_favorite` can be only one of the following:  
`isFavorite` |  `boolean` Optional. Whether the comment is marked as a favorite.  
Union field `_is_deleted`.`_is_deleted` can be only one of the following:  
`isDeleted` |  `boolean` Output only. Indicates if the comment has been softly deleted.  
  
### CaseAttachment

JSON representation  
---  
      
    
    {
      "attachmentBase64": string,
      "fileType": string,
      "fileName": string,
      "fileId": string
    }  
  
Fields  
---  
`attachmentBase64` |  `string` Required. Base64 encoded attachment associated with the comment (if exists).  
`fileType` |  `string` Required. The file type of the attachment (if exists).  
`fileName` |  `string` Required. The file name of the attachment (if it exists).  
`fileId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The file id of the attachment.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
