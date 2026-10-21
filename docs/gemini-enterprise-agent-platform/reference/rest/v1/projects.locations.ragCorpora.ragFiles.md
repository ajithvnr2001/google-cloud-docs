---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles
title: REST Resource: projects.locations.ragCorpora.ragFiles \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:11:56.645256+00:00
---

# REST Resource: projects.locations.ragCorpora.ragFiles  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.ragCorpora.ragFiles Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: RagFile

A RagFile contains user data for chunking, embedding and indexing.

Fields  
  
`name` `string` Output only. The resource name of the RagFile. | `displayName` `string` Required. The display name of the RagFile. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `description` `string` Optional. The description of the RagFile. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this RagFile was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this RagFile was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `fileStatus` `object (`[FileStatus](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#FileStatus)`)` Output only. state of the RagFile. | `userMetadata` `string` Output only. The metadata for metadata search. The userMetadata Needs to be in JSON format. | `rag_file_source` `Union type`  
  
The origin location of the RagFile if it is imported from Google Cloud Storage or Google Drive. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsSource` `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GcsSource)`)` Output only. Google Cloud Storage location of the RagFile. It does not support wildcards in the Cloud Storage uri for now. | `googleDriveSource` `object (`[GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource)`)` Output only. Google Drive location. Supports importing individual files as well as Google Drive folders. | `directUploadSource` `object (`[DirectUploadSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#DirectUploadSource)`)` Output only. The RagFile is encapsulated and uploaded in the UploadRagFile request. | `slackSource` `object (`[SlackSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackSource)`)` The RagFile is imported from a Slack channel. | `jiraSource` `object (`[JiraSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraSource)`)` The RagFile is imported from a Jira query. | `sharePointSources` `object (`[SharePointSources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSources)`)` The RagFile is imported from a SharePoint source. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "fileStatus": {
        object ([FileStatus](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#FileStatus))
      },
      "userMetadata": string,
    
      // rag_file_source
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GcsSource))
      },
      "googleDriveSource": {
        object ([GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource))
      },
      "directUploadSource": {
        object ([DirectUploadSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#DirectUploadSource))
      },
      "slackSource": {
        object ([SlackSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackSource))
      },
      "jiraSource": {
        object ([JiraSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraSource))
      },
      "sharePointSources": {
        object ([SharePointSources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSources))
      }
      // Union type
    }  
  
## GoogleDriveSource

The Google Drive location for the input content.

Fields  
  
`resourceIds[]` `object (`[ResourceId](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#ResourceId)`)` Required. Google Drive resource IDs. | JSON representation  
---  
      
    
    {
      "resourceIds": [
        {
          object ([ResourceId](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#ResourceId))
        }
      ]
    }  
  
## ResourceId

The type and id of the Google Drive resource.

Fields  
  
`resourceType` `enum (`[ResourceType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#ResourceType)`)` Required. The type of the Google Drive resource. | `resourceId` `string` Required. The id of the Google Drive resource. | JSON representation  
---  
      
    
    {
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#ResourceType)),
      "resourceId": string
    }  
  
## ResourceType

The type of the Google Drive resource.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Unspecified resource type.  
`RESOURCE_TYPE_FILE` | File resource type.  
`RESOURCE_TYPE_FOLDER` | Folder resource type.  
  
## DirectUploadSource

This type has no fields.

The input content is encapsulated and uploaded in the request.

## SlackSource

The Slack source for the ImportRagFilesRequest.

Fields  
  
`channels[]` `object (`[SlackChannels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackChannels)`)` Required. The Slack channels. | JSON representation  
---  
      
    
    {
      "channels": [
        {
          object ([SlackChannels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackChannels))
        }
      ]
    }  
  
## SlackChannels

SlackChannels contains the Slack channels and corresponding access token.

Fields  
  
`channels[]` `object (`[SlackChannel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackChannel)`)` Required. The Slack channel IDs. | `apiKeyConfig` `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig)`)` Required. The SecretManager secret version resource name (e.g. projects/{project}/secrets/{secret}/versions/{version}) storing the Slack channel access token that has access to the slack channel IDs. See: <https://api.slack.com/tutorials/tracks/getting-a-token>. | JSON representation  
---  
      
    
    {
      "channels": [
        {
          object ([SlackChannel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackChannel))
        }
      ],
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig))
      }
    }  
  
## SlackChannel

SlackChannel contains the Slack channel id and the time range to import.

Fields  
  
`channelId` `string` Required. The Slack channel id. | `startTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The starting timestamp for messages to import.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `endTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The ending timestamp for messages to import.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "channelId": string,
      "startTime": string,
      "endTime": string
    }  
  
## JiraSource

The Jira source for the ImportRagFilesRequest.

Fields  
  
`jiraQueries[]` `object (`[JiraQueries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraQueries)`)` Required. The Jira queries. | JSON representation  
---  
      
    
    {
      "jiraQueries": [
        {
          object ([JiraQueries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraQueries))
        }
      ]
    }  
  
## JiraQueries

JiraQueries contains the Jira queries and corresponding authentication.

Fields  
  
`projects[]` `string` A list of Jira projects to import in their entirety. | `customQueries[]` `string` A list of custom Jira queries to import. For information about JQL (Jira Query Language), see <https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/> | `email` `string` Required. The Jira email address. | `serverUri` `string` Required. The Jira server URI. | `apiKeyConfig` `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig)`)` Required. The SecretManager secret version resource name (e.g. projects/{project}/secrets/{secret}/versions/{version}) storing the Jira API key. See [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/). | JSON representation  
---  
      
    
    {
      "projects": [
        string
      ],
      "customQueries": [
        string
      ],
      "email": string,
      "serverUri": string,
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig))
      }
    }  
  
## SharePointSources

The SharePointSources to pass to ragFiles.import.

Fields  
  
`sharePointSources[]` `object (`[SharePointSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSource)`)` The SharePoint sources. | JSON representation  
---  
      
    
    {
      "sharePointSources": [
        {
          object ([SharePointSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSource))
        }
      ]
    }  
  
## SharePointSource

An individual SharePointSource.

Fields  
  
`clientId` `string` The Application id for the app registered in Microsoft Azure Portal. The application must also be configured with MS Graph permissions "Files.ReadAll", "Sites.ReadAll" and BrowserSiteLists.Read.All. | `clientSecret` `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig)`)` The application secret for the app registered in Azure. | `tenantId` `string` Unique identifier of the Azure Active Directory Instance. | `sharepointSiteName` `string` The name of the SharePoint site to download from. This can be the site name or the site id. | `fileId` `string` Output only. The SharePoint file id. Output only. | `folder_source` `Union type`  
  
The SharePoint folder source. If not provided, uses "root". The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`sharepointFolderPath` `string` The path of the SharePoint folder to download from. | `sharepointFolderId` `string` The id of the SharePoint folder to download from. End of mutually exclusive fields. | `drive_source` `Union type`  
  
The SharePoint drive source. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`driveName` `string` The name of the drive to download from. | `driveId` `string` The id of the drive to download from. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ApiKeyConfig))
      },
      "tenantId": string,
      "sharepointSiteName": string,
      "fileId": string,
    
      // folder_source
      "sharepointFolderPath": string,
      "sharepointFolderId": string
      // Union type
    
      // drive_source
      "driveName": string,
      "driveId": string
      // Union type
    }  
  
## FileStatus

RagFile status.

Fields  
  
`state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#State)`)` Output only. RagFile state. | `errorStatus` `string` Output only. Only when the `state` field is ERROR. | JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#State)),
      "errorStatus": string
    }  
  
## State

RagFile state.

Enums  
---  
`STATE_UNSPECIFIED` | RagFile state is unspecified.  
`ACTIVE` | RagFile resource has been created and indexed successfully.  
`ERROR` | RagFile resource is in a problematic state. See `errorMessage` field for details.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/delete)`

|  Deletes a RagFile.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/get)`

|  Gets a RagFile.  
  
### `[import](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import)`

|  Import files from Google Cloud Storage or Google Drive into a RagCorpus.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/list)`

|  Lists RagFiles in a RagCorpus.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
