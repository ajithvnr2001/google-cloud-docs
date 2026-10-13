---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/update_feed/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:26.431711+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/update_feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_feed`

Update an existing feed in Chronicle.

Modifies the configuration of an existing feed.

**Agent Responsibilities:** \- Provide the `feed` object with the fields to be updated. - Provide the `update_mask` specifying which fields to update (comma-separated).

Args: project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). feed_id (str): The ID of the feed to update. feed (Dict[str, Any]): The feed object with updated values. update_mask (str): Comma-separated list of fields to update (e.g., "display_name,details.http_settings").

Returns: str: Raw JSON response containing the updated feed details.

Example Usage: update_feed( project_id="my-project", customer_id="my-customer", region="us", feed_id="feed_12345", feed={ "display_name": "Updated Feed Name" }, update_mask="display_name" )

The following sample demonstrate how to use `curl` to invoke the `update_feed` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_feed",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for UpdateFeed.

### UpdateFeedRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "feedId": string,
      "feed": {
        object ([Feed](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Feed))
      },
      "updateMask": string
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`feedId` |  `string` The unique ID of the feed.  
`feed` |  `object (`[Feed](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Feed)`)` The feed to update.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The fields to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Feed

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "displayName": string,
      "details": {
        object ([FeedDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedDetails))
      },
      "state": enum (State),
      "failureMsg": string,
      "readOnly": boolean,
      "lastFeedInitiationTime": string,
      "failureDetails": {
        object ([FeedFailureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedFailureDetails))
      },
      "referenceId": string
    }  
  
Fields  
---  
`name` |  `string` The resource name of the feed. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}  
`uid` |  `string` Output only. Unique identifier for the feed.  
`displayName` |  `string` Customer-provided feed name.  
`details` |  `object (`[FeedDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedDetails)`)` Additional details of the feed, these details are dynamic and will be different for each of the feeds.  
`state` |  `enum (`State`)` Output only. State of the feed.  
`failureMsg` |  `string` Output only. Details about the most recent failure when feed state is FAILED.  
`readOnly` |  `boolean` Output only. Whether this feed can be updated or deleted.  
`lastFeedInitiationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Latest timestamp when the transfer was successful for the feed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`failureDetails` |  `object (`[FeedFailureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedFailureDetails)`)` Output only. Failure details for the feed. If the feed is in the failure state, this field will contain the details of the error cause and actions.  
`referenceId` |  `string` Output only. Reference ID, this field will contain the legacy id of the feed.  
  
### FeedDetails

JSON representation  
---  
      
    
    {
      "feedSourceType": enum (FeedSourceType),
      "logType": string,
      "assetNamespace": string,
      "labels": {
        string: string,
        ...
      },
      "stsMigrationReadiness": enum (STSMigrationReadiness),
    
      // Union field details can be only one of the following:
      "anomaliSettings": {
        object ([AnomaliIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AnomaliIocSettings))
      },
      "azureAdContextSettings": {
        object ([AzureADContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADContextSettings))
      },
      "cloudPassageSettings": {
        object ([CloudPassageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CloudPassageSettings))
      },
      "cortexXdrSettings": {
        object ([CortexXDRSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CortexXDRSettings))
      },
      "duoAuthSettings": {
        object ([DuoAuthSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoAuthSettings))
      },
      "duoUserContextSettings": {
        object ([DuoUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoUserContextSettings))
      },
      "microsoftGraphAlertSettings": {
        object ([MicrosoftGraphAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftGraphAlertSettings))
      },
      "microsoftSecurityCenterAlertSettings": {
        object ([MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftSecurityCenterAlertSettings))
      },
      "mimecastMailSettings": {
        object ([MimecastMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailSettings))
      },
      "office365Settings": {
        object ([Office365Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Office365Settings))
      },
      "proofpointMailSettings": {
        object ([ProofpointMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointMailSettings))
      },
      "recordedFutureIocSettings": {
        object ([RecordedFutureIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RecordedFutureIocSettings))
      },
      "workdaySettings": {
        object ([WorkdaySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdaySettings))
      },
      "panIocSettings": {
        object ([PanIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanIocSettings))
      },
      "oktaSettings": {
        object ([OktaSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaSettings))
      },
      "oktaUserContextSettings": {
        object ([OktaUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaUserContextSettings))
      },
      "foxItStixSettings": {
        object ([FoxITStixSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FoxITStixSettings))
      },
      "threatConnectIocSettings": {
        object ([ThreatConnectIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCSettings))
      },
      "serviceNowCmdbSettings": {
        object ([ServiceNowCMDBSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ServiceNowCMDBSettings))
      },
      "impervaWafSettings": {
        object ([ImpervaWAFSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ImpervaWAFSettings))
      },
      "thinkstCanarySettings": {
        object ([ThinkstCanarySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThinkstCanarySettings))
      },
      "rhIsacIocSettings": {
        object ([RHIsacIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RHIsacIocSettings))
      },
      "rapid7InsightSettings": {
        object ([Rapid7InsightSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Rapid7InsightSettings))
      },
      "salesforceSettings": {
        object ([SalesforceSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SalesforceSettings))
      },
      "netskopeAlertSettings": {
        object ([NetskopeAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertSettings))
      },
      "azureMdmIntuneSettings": {
        object ([AzureMDMIntuneSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureMDMIntuneSettings))
      },
      "azureAdSettings": {
        object ([AzureADSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADSettings))
      },
      "proofpointOnDemandSettings": {
        object ([ProofpointOnDemandSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointOnDemandSettings))
      },
      "workspaceUsersSettings": {
        object ([WorkspaceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceUsersSettings))
      },
      "workspaceActivitySettings": {
        object ([WorkspaceActivitySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceActivitySettings))
      },
      "workspaceAlertsSettings": {
        object ([WorkspaceAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceAlertsSettings))
      },
      "workspacePrivilegesSettings": {
        object ([WorkspacePrivilegesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspacePrivilegesSettings))
      },
      "workspaceMobileSettings": {
        object ([WorkspaceMobileSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceMobileSettings))
      },
      "workspaceChromeOsSettings": {
        object ([WorkspaceChromeOSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceChromeOSSettings))
      },
      "workspaceGroupsSettings": {
        object ([WorkspaceGroupsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceGroupsSettings))
      },
      "azureAdAuditSettings": {
        object ([AzureADAuditSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADAuditSettings))
      },
      "symantecEventExportSettings": {
        object ([SymantecEventExportSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SymantecEventExportSettings))
      },
      "qualysVmSettings": {
        object ([QualysVMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysVMSettings))
      },
      "panPrismaCloudSettings": {
        object ([PanPrismaCloudSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaCloudSettings))
      },
      "gcsSettings": {
        object ([GoogleCloudStorageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageSettings))
      },
      "httpSettings": {
        object ([HttpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpSettings))
      },
      "sftpSettings": {
        object ([SftpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpSettings))
      },
      "amazonS3Settings": {
        object ([AmazonS3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3Settings))
      },
      "azureBlobStoreSettings": {
        object ([AzureBlobStoreSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreSettings))
      },
      "amazonSqsSettings": {
        object ([AmazonSQSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSSettings))
      },
      "googleCloudIdentityDevicesSettings": {
        object ([GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDevicesSettings))
      },
      "googleCloudIdentityDeviceUsersSettings": {
        object ([GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDeviceUsersSettings))
      },
      "crowdstrikeDetectsSettings": {
        object ([CrowdStrikeDetectsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeDetectsSettings))
      },
      "mandiantIocSettings": {
        object ([MandiantIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MandiantIoCSettings))
      },
      "sentineloneAlertSettings": {
        object ([SentineloneAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SentineloneAlertSettings))
      },
      "qualysScanSettings": {
        object ([QualysScanSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysScanSettings))
      },
      "pubsubSettings": {
        object ([PubsubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PubsubSettings))
      },
      "amazonKinesisFirehoseSettings": {
        object (AmazonKinesisFirehoseSettings)
      },
      "webhookSettings": {
        object (WebhookSettings)
      },
      "dummyLogTypeSettings": {
        object ([DummyLogTypeSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DummyLogTypeSettings))
      },
      "httpsPushGoogleCloudPubsubSettings": {
        object ([HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushGoogleCloudPubSubSettings))
      },
      "httpsPushAmazonKinesisFirehoseSettings": {
        object ([HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushAmazonKinesisFirehoseSettings))
      },
      "httpsPushWebhookSettings": {
        object ([HttpsPushWebhookSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushWebhookSettings))
      },
      "awsEc2HostsSettings": {
        object ([AWSEC2HostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2HostsSettings))
      },
      "awsEc2InstancesSettings": {
        object ([AWSEC2InstancesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2InstancesSettings))
      },
      "awsEc2VpcsSettings": {
        object ([AWSEC2VpcsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2VpcsSettings))
      },
      "awsIamSettings": {
        object ([AWSIAMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSIAMSettings))
      },
      "netskopeAlertV2Settings": {
        object ([NetskopeAlertV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertV2Settings))
      },
      "gcsV2Settings": {
        object ([GoogleCloudStorageV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageV2Settings))
      },
      "amazonS3V2Settings": {
        object ([AmazonS3V2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3V2Settings))
      },
      "amazonSqsV2Settings": {
        object ([AmazonSQSV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSV2Settings))
      },
      "azureEventHubSettings": {
        object ([AzureEventHubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureEventHubSettings))
      },
      "trellixHxHostsSettings": {
        object ([TrellixHxHostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxHostsSettings))
      },
      "azureBlobStoreV2Settings": {
        object ([AzureBlobStoreV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreV2Settings))
      },
      "trellixHxAlertsSettings": {
        object ([TrellixHxAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxAlertsSettings))
      },
      "googleCloudStorageEventDrivenSettings": {
        object ([GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageEventDrivenSettings))
      },
      "crowdstrikeAlertsSettings": {
        object ([CrowdStrikeAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeAlertsSettings))
      },
      "trellixHxBulkAcqsSettings": {
        object ([TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxBulkAcqsSettings))
      },
      "mimecastMailV2Settings": {
        object ([MimecastMailV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailV2Settings))
      },
      "threatConnectIocV3Settings": {
        object ([ThreatConnectIoCV3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCV3Settings))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`feedSourceType` |  `enum (`FeedSourceType`)` Source Type of the feed.  
`logType` |  `string` LogType. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}  
`assetNamespace` |  `string` The asset namespace to apply to all logs ingested through this feed.  
`labels` |  `map (key: string, value: string)` The ingestion metadata labels to apply to all logs ingested through this feed, and the resulting normalized data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stsMigrationReadiness` |  `enum (`STSMigrationReadiness`)` Optional. The status of the feed's migration to STS.  
Union field `details`. Additional details of the feed. Depends on the feed type. `details` can be only one of the following:  
`anomaliSettings` |  `object (`[AnomaliIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AnomaliIocSettings)`)` Anomali IOC settings.  
`azureAdContextSettings` |  `object (`[AzureADContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADContextSettings)`)` Azure AD Context settings.  
`cloudPassageSettings` |  `object (`[CloudPassageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CloudPassageSettings)`)` Cloud Passage settings.  
`cortexXdrSettings` |  `object (`[CortexXDRSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CortexXDRSettings)`)` Cortex XDR settings.  
`duoAuthSettings` |  `object (`[DuoAuthSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoAuthSettings)`)` Duo Auth settings.  
`duoUserContextSettings` |  `object (`[DuoUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoUserContextSettings)`)` Duo User Context settings.  
`microsoftGraphAlertSettings` |  `object (`[MicrosoftGraphAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftGraphAlertSettings)`)` Microsoft Graph Alert settings.  
`microsoftSecurityCenterAlertSettings` |  `object (`[MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftSecurityCenterAlertSettings)`)` Microsoft Security center alert settings.  
`mimecastMailSettings` |  `object (`[MimecastMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailSettings)`)` Mimecast mail settings.  
`office365Settings` |  `object (`[Office365Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Office365Settings)`)` Office 365 settings.  
`proofpointMailSettings` |  `object (`[ProofpointMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointMailSettings)`)` Proofpoint mail settings.  
`recordedFutureIocSettings` |  `object (`[RecordedFutureIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RecordedFutureIocSettings)`)` Recorded Future IOC settings.  
`workdaySettings` |  `object (`[WorkdaySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdaySettings)`)` Workday settings.  
`panIocSettings` |  `object (`[PanIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanIocSettings)`)` PAN IOC settings.  
`oktaSettings` |  `object (`[OktaSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaSettings)`)` Okta settings.  
`oktaUserContextSettings` |  `object (`[OktaUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaUserContextSettings)`)` Okta user context settings.  
`foxItStixSettings` |  `object (`[FoxITStixSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FoxITStixSettings)`)` Fox-IT STIX settings.  
`threatConnectIocSettings` |  `object (`[ThreatConnectIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCSettings)`)` ThreatConnect IOC settings.  
`serviceNowCmdbSettings` |  `object (`[ServiceNowCMDBSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ServiceNowCMDBSettings)`)` ServiceNow CMDB settings.  
`impervaWafSettings` |  `object (`[ImpervaWAFSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ImpervaWAFSettings)`)` Imperva WAF settings.  
`thinkstCanarySettings` |  `object (`[ThinkstCanarySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThinkstCanarySettings)`)` Thinkst Canary settings.  
`rhIsacIocSettings` |  `object (`[RHIsacIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RHIsacIocSettings)`)` RH-ISAC IOC settings.  
`rapid7InsightSettings` |  `object (`[Rapid7InsightSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Rapid7InsightSettings)`)` Rapid7 Insight settings.  
`salesforceSettings` |  `object (`[SalesforceSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SalesforceSettings)`)` Salesforce settings.  
`netskopeAlertSettings` |  `object (`[NetskopeAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertSettings)`)` Netskope alert settings.  
`azureMdmIntuneSettings` |  `object (`[AzureMDMIntuneSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureMDMIntuneSettings)`)` Azure MDM Intune settings.  
`azureAdSettings` |  `object (`[AzureADSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADSettings)`)` Azure AD settings.  
`proofpointOnDemandSettings` |  `object (`[ProofpointOnDemandSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointOnDemandSettings)`)` Proofpoint On-Demand settings.  
`workspaceUsersSettings` |  `object (`[WorkspaceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceUsersSettings)`)` Workspace users settings.  
`workspaceActivitySettings` |  `object (`[WorkspaceActivitySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceActivitySettings)`)` Workspace activity settings.  
`workspaceAlertsSettings` |  `object (`[WorkspaceAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceAlertsSettings)`)` Workspace alerts settings.  
`workspacePrivilegesSettings` |  `object (`[WorkspacePrivilegesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspacePrivilegesSettings)`)` Workspace privileges settings.  
`workspaceMobileSettings` |  `object (`[WorkspaceMobileSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceMobileSettings)`)` Workspace mobile settings.  
`workspaceChromeOsSettings` |  `object (`[WorkspaceChromeOSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceChromeOSSettings)`)` Workspace ChromeOS settings.  
`workspaceGroupsSettings` |  `object (`[WorkspaceGroupsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceGroupsSettings)`)` Workspace Groups settings.  
`azureAdAuditSettings` |  `object (`[AzureADAuditSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADAuditSettings)`)` Azure AD Audit settings.  
`symantecEventExportSettings` |  `object (`[SymantecEventExportSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SymantecEventExportSettings)`)` Symantec Event Export settings.  
`qualysVmSettings` |  `object (`[QualysVMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysVMSettings)`)` Qualys VM settings  
`panPrismaCloudSettings` |  `object (`[PanPrismaCloudSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaCloudSettings)`)` PAN Prisma Cloud settings.  
`gcsSettings` |  `object (`[GoogleCloudStorageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageSettings)`)` Google Cloud Storage settings.  
`httpSettings` |  `object (`[HttpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpSettings)`)` HTTP settings.  
`sftpSettings` |  `object (`[SftpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpSettings)`)` SFTP settings.  
`amazonS3Settings` |  `object (`[AmazonS3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3Settings)`)` Amazon S3 settings.  
`azureBlobStoreSettings` |  `object (`[AzureBlobStoreSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreSettings)`)` Azure Blob Storage settings.  
`amazonSqsSettings` |  `object (`[AmazonSQSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSSettings)`)` Amazon SQS settings.  
`googleCloudIdentityDevicesSettings` |  `object (`[GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDevicesSettings)`)` Google Cloud Identity Devices settings.  
`googleCloudIdentityDeviceUsersSettings` |  `object (`[GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDeviceUsersSettings)`)` Google Cloud Identity Device Users settings.  
`crowdstrikeDetectsSettings` |  `object (`[CrowdStrikeDetectsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeDetectsSettings)`)` CrowdStrike Detects API settings.  
`mandiantIocSettings` |  `object (`[MandiantIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MandiantIoCSettings)`)` Mandiant IOC settings.  
`sentineloneAlertSettings` |  `object (`[SentineloneAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SentineloneAlertSettings)`)` SentinelOne Alert settings.  
`qualysScanSettings` |  `object (`[QualysScanSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysScanSettings)`)` Qualys Scan Settings  
`pubsubSettings` |  `object (`[PubsubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PubsubSettings)`)` Pub/Sub settings.  
`amazonKinesisFirehoseSettings` |  `object (`AmazonKinesisFirehoseSettings`)` Amazon Kinesis Firehose settings.  
`webhookSettings` |  `object (`WebhookSettings`)` Webhook settings.  
`dummyLogTypeSettings` |  `object (`[DummyLogTypeSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DummyLogTypeSettings)`)` DummyLogType Settings.  
`httpsPushGoogleCloudPubsubSettings` |  `object (`[HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushGoogleCloudPubSubSettings)`)` Https push Google Pub/Sub settings.  
`httpsPushAmazonKinesisFirehoseSettings` |  `object (`[HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushAmazonKinesisFirehoseSettings)`)` Https push Amazon Kinesis Firehose settings.  
`httpsPushWebhookSettings` |  `object (`[HttpsPushWebhookSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushWebhookSettings)`)` Https push Webhook settings.  
`awsEc2HostsSettings` |  `object (`[AWSEC2HostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2HostsSettings)`)` AWS EC2 Hosts settings.  
`awsEc2InstancesSettings` |  `object (`[AWSEC2InstancesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2InstancesSettings)`)` AWS EC2 Instances settings.  
`awsEc2VpcsSettings` |  `object (`[AWSEC2VpcsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2VpcsSettings)`)` AWS EC2 Vpcs settings.  
`awsIamSettings` |  `object (`[AWSIAMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSIAMSettings)`)` AWS IAM settings.  
`netskopeAlertV2Settings` |  `object (`[NetskopeAlertV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertV2Settings)`)` Netskope alert V2 settings.  
`gcsV2Settings` |  `object (`[GoogleCloudStorageV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageV2Settings)`)` Settings for Google Cloud Storage Omniflow feeds.  
`amazonS3V2Settings` |  `object (`[AmazonS3V2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3V2Settings)`)` Settings for S3 Omniflow feeds.  
`amazonSqsV2Settings` |  `object (`[AmazonSQSV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSV2Settings)`)` Settings for SQS Omniflow feeds.  
`azureEventHubSettings` |  `object (`[AzureEventHubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureEventHubSettings)`)` Settings for Omniflow based native ingestion from azure event hub.  
`trellixHxHostsSettings` |  `object (`[TrellixHxHostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxHostsSettings)`)` Settings for Trellix HX Host Metadata.  
`azureBlobStoreV2Settings` |  `object (`[AzureBlobStoreV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreV2Settings)`)` Settings for Azure Blobstore Omniflow feeds.  
`trellixHxAlertsSettings` |  `object (`[TrellixHxAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxAlertsSettings)`)` Settings for Trellix HX Alerts Metadata.  
`googleCloudStorageEventDrivenSettings` |  `object (`[GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageEventDrivenSettings)`)` Settings for Omniflow based Google Cloud Storage event driven feeds.  
`crowdstrikeAlertsSettings` |  `object (`[CrowdStrikeAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeAlertsSettings)`)` CrowdStrike Alerts API settings.  
`trellixHxBulkAcqsSettings` |  `object (`[TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxBulkAcqsSettings)`)` Settings for Trellix HX Bulk Acquisitions Metadata.  
`mimecastMailV2Settings` |  `object (`[MimecastMailV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailV2Settings)`)` Required. Mimecast mail v2 settings.  
`threatConnectIocV3Settings` |  `object (`[ThreatConnectIoCV3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCV3Settings)`)` Threat Connect IOC V3 settings.  
  
### AnomaliIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
  
### UsernameSecretAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "secret": string
    }  
  
Fields  
---  
`user` |  `string` Username of an identity used for authentication.  
`secret` |  `string` Secret of the account identified by user_name.  
  
### AzureADContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "retrieveDevices": boolean,
      "retrieveGroups": boolean,
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`retrieveDevices` |  `boolean` Whether to retrieve device information in user context.  
`retrieveGroups` |  `boolean` Whether to retrieve group information in user context.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MicrosoftOAuthClientCredentials

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
  
### CloudPassageSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "eventTypes": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`eventTypes[]` |  `string` Event types filter for the events API.  
  
### CortexXDRSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`endpoint` |  `string` API Endpoint.  
  
### HttpHeaderAuth

JSON representation  
---  
      
    
    {
      "headerKeyValues": [
        {
          object ([HeaderKeyValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HeaderKeyValue))
        }
      ]
    }  
  
Fields  
---  
`headerKeyValues[]` |  `object (`[HeaderKeyValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HeaderKeyValue)`)` Header key-value pairs.  
  
### HeaderKeyValue

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Key.  
`value` |  `string` Value.  
  
### DuoAuthSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### DuoUserContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API hostname.  
  
### MicrosoftGraphAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MicrosoftSecurityCenterAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "subscriptionId": string,
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`subscriptionId` |  `string` Subscription ID of the Microsoft security center alert settings alert.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MimecastMailSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### Office365Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "contentType": enum (ContentType),
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`contentType` |  `enum (`ContentType`)` Supported office 365 content type.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### ProofpointMailSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
  
### RecordedFutureIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
  
### WorkdaySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([WorkdayAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdayAuth))
      },
      "hostname": string,
      "tenantId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[WorkdayAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdayAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`tenantId` |  `string` Tenant ID.  
  
### WorkdayAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "secret": string,
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "refreshToken": string
    }  
  
Fields  
---  
`user` |  `string` Username. This is unused: Workday feeds were originally configured using a username and secret authentication method, but only the secret field was used, and it was used to supply the OAuth access token.  
`secret` |  `string` The access token used to authenticate against Workday. This field is called "secret" to maintain backwards compatibility. Workday was (only) configured using username (which was unused) and secret (which is used as the access token). Either this field or all of the other OAuth fields below must be specified.  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client Secret.  
`refreshToken` |  `string` Refresh Token.  
  
### PanIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "feedId": string,
      "feed": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`feedId` |  `string` PAN IOC feed ID.  
`feed` |  `string` PAN IOC feed name.  
  
### OktaSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### OktaUserContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "managerIdReferenceField": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`managerIdReferenceField` |  `string` Manager id reference field.  
  
### FoxITStixSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "ssl": {
        object ([SSLClientKeypair](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SSLClientKeypair))
      },
      "pollServiceUri": string,
      "collection": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`ssl` |  `object (`[SSLClientKeypair](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SSLClientKeypair)`)` SSL client key pair.  
`pollServiceUri` |  `string` TAXII poll service URI.  
`collection` |  `string` Collection available at the poll service.  
  
### SSLClientKeypair

JSON representation  
---  
      
    
    {
      "encodedPrivateKey": string,
      "sslCertificate": string
    }  
  
Fields  
---  
`encodedPrivateKey` |  `string` The encoded private key. The string should be a private key in PEM format, and should include the begin header and end footer lines. It may also include newlines.Example: -----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED DEK-Info: DES-EDE3-CBC,F23074E02CF47304 \-----END RSA PRIVATE KEY-----  
`sslCertificate` |  `string` The encoded SSL certificate. The string should be an SSL certificate in PEM format, and should include the begin header and end footer lines. It may also include newlines.Example: -----BEGIN CERTIFICATE-----  \-----END CERTIFICATE-----  
  
### ThreatConnectIoCSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "owners": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`owners[]` |  `string` Owners.  
  
### ServiceNowCMDBSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "feedname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`feedname` |  `string` Feedname.  
  
### ImpervaWAFSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
  
### ThinkstCanarySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### RHIsacIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Input only. Authentication.  
  
### OAuthClientCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
  
### Rapid7InsightSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "endpoint": string,
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`endpoint` |  `string` Rapid7 API endpoint. Should be "vulnerabilities" or "assets".  
`hostname` |  `string` API Hostname.  
  
### SalesforceSettings

JSON representation  
---  
      
    
    {
      "hostname": string,
    
      // Union field authentication can be only one of the following:
      "oauthPasswordGrantAuth": {
        object ([OAuthPasswordGrantCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthPasswordGrantCredentials))
      },
      "oauthJwtCredentials": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      }
      // End of list of possible types for union field authentication.
    }  
  
Fields  
---  
`hostname` |  `string` API hostname.  
Union field `authentication`. Possible types of authentication. `authentication` can be only one of the following:  
`oauthPasswordGrantAuth` |  `object (`[OAuthPasswordGrantCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthPasswordGrantCredentials)`)` Input only. OAuthPasswordGrantCredentials auth.  
`oauthJwtCredentials` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. OAuthJWTCredentials auth.  
  
### OAuthPasswordGrantCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "user": string,
      "password": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
`user` |  `string` Username.  
`password` |  `string` Password.  
  
### OAuthJWTCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "claims": {
        object ([Claims](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Claims))
      },
    
      // Union field credentials can be only one of the following:
      "rsCredentials": {
        object ([RSCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RSCredentials))
      }
      // End of list of possible types for union field credentials.
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`claims` |  `object (`[Claims](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Claims)`)` Claims.  
Union field `credentials`. Credentials. `credentials` can be only one of the following:  
`rsCredentials` |  `object (`[RSCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RSCredentials)`)` RS credentials.  
  
### RSCredentials

JSON representation  
---  
      
    
    {
      "privateKey": string
    }  
  
Fields  
---  
`privateKey` |  `string` Private key in PEM format.  
  
### Claims

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "audience": string
    }  
  
Fields  
---  
`issuer` |  `string` Issuer. Usually the client_id.  
`subject` |  `string` Subject. Usually the email.  
`audience` |  `string` Audience.  
  
### NetskopeAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "feedname": string,
      "contentType": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`feedname` |  `string` Feedname.  
`contentType` |  `string` Content type.  
  
### AzureMDMIntuneSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### AzureADSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### ProofpointOnDemandSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "clusterId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`clusterId` |  `string` Cluster ID.  
  
### WorkspaceUsersSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string,
      "projectionType": enum (ProjectionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
`projectionType` |  `enum (`ProjectionType`)` Optional. Projection Type.  
  
### WorkspaceActivitySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string,
      "applications": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
`applications[]` |  `string` Applications.  
  
### WorkspaceAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspacePrivilegesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceMobileSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceChromeOSSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceGroupsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### AzureADAuditSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### SymantecEventExportSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthRefreshToken](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthRefreshToken))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthRefreshToken](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthRefreshToken)`)` Input only. Authentication.  
  
### OAuthRefreshToken

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "refreshToken": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
`refreshToken` |  `string` Refresh token.  
  
### QualysVMSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### PanPrismaCloudSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([PanPrismaAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[PanPrismaAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### PanPrismaAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "password": string
    }  
  
Fields  
---  
`user` |  `string` Username.  
`password` |  `string` Password.  
  
### GoogleCloudStorageSettings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption),
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`bucketUri` |  `string` Bucket URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
`chronicleServiceAccount` |  `string` Output only. Service Account Chronicle will be using to pull data.  
  
### HttpSettings

JSON representation  
---  
      
    
    {
      "uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`uri` |  `string` HTTP URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SftpSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([SftpAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpAuth))
      },
      "uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[SftpAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpAuth)`)` Input only. Authentication.  
`uri` |  `string` SFTP URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SftpAuth

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string,
      "privateKey": string,
      "privateKeyPassphrase": string
    }  
  
Fields  
---  
`username` |  `string` Username. Used for username and password authentication.  
`password` |  `string` Password. Used for username and password authentication.  
`privateKey` |  `string` Private key. Used for private key authentication.  
`privateKeyPassphrase` |  `string` Private key passphrase. Used for private key authentication.  
  
### AmazonS3Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([S3Auth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3Auth))
      },
      "s3Uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[S3Auth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3Auth)`)` Input only. Authentication.  
`s3Uri` |  `string` S3 URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### S3Auth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string,
      "clientId": string,
      "clientSecret": string,
      "refreshUri": string,
      "region": enum (S3Region)
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID. Used when using access key auth.  
`secretAccessKey` |  `string` Secret access key. Used when using access key auth.  
`clientId` |  `string` Client ID. Used when using OAuth auth.  
`clientSecret` |  `string` Client secret. Used when using OAuth auth.  
`refreshUri` |  `string` Refresh URI. Used when using OAuth auth.  
`region` |  `enum (`S3Region`)` S3 Region.  
  
### AzureBlobStoreSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([AzureAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuth))
      },
      "azureUri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[AzureAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuth)`)` Input only. Authentication.  
`azureUri` |  `string` Azure URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### AzureAuth

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "sharedKey": string,
      "sasToken": string
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. Type of auth used with Azure. `auth_type` can be only one of the following:  
`sharedKey` |  `string` Shared Key.  
`sasToken` |  `string` SAS Token.  
  
### AmazonSQSSettings

JSON representation  
---  
      
    
    {
      "region": enum (S3Region),
      "queue": string,
      "accountNumber": string,
      "authentication": {
        object ([SQSAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuth))
      },
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`region` |  `enum (`S3Region`)` S3 Region.  
`queue` |  `string` Name of the queue.  
`accountNumber` |  `string` Account number of the owner of the queue.  
`authentication` |  `object (`[SQSAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuth)`)` Input only. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SQSAuth

JSON representation  
---  
      
    
    {
      "sqsAccessKeySecretAuth": {
        object ([SQSAccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAccessKeySecretAuth))
      },
      "additionalS3AccessKeySecretAuth": {
        object ([AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AdditionalS3AccessKeySecretAuth))
      }
    }  
  
Fields  
---  
`sqsAccessKeySecretAuth` |  `object (`[SQSAccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAccessKeySecretAuth)`)` SQS access key secret auth.  
`additionalS3AccessKeySecretAuth` |  `object (`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AdditionalS3AccessKeySecretAuth)`)` Authentication for the S3 bucket referred to by the items in the SQS queue. This is only required if it is different from the authentication for the queue.  
  
### SQSAccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID.  
`secretAccessKey` |  `string` Secret access key.  
  
### AdditionalS3AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID.  
`secretAccessKey` |  `string` Secret access key.  
  
### GoogleCloudIdentityDevicesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "apiVersion": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication  
`apiVersion` |  `string` API Version  
  
### GoogleCloudIdentityDeviceUsersSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
  
### CrowdStrikeDetectsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      },
      "hostname": string,
      "ingestionType": enum (IngestionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Input only. OAuthClientCredentials.  
`hostname` |  `string` API Hostname.  
`ingestionType` |  `enum (`IngestionType`)` Optional. Ingestion Type.  
  
### MandiantIoCSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "startTime": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` time since when to start fetching the IOCsUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### SentineloneAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "initialStartTime": string,
      "isAlertApiSubscribed": boolean
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` Hostname of SentinelOne alert settings.  
`initialStartTime` |  `string` initialStartTime from when to fetch the alerts  
`isAlertApiSubscribed` |  `boolean` Is the customer subscribed to Alerts Api  
  
### QualysScanSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "apiType": enum (ApiType)
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication  
`hostname` |  `string` Hostname.  
`apiType` |  `enum (`ApiType`)` Supported Qualys Scan api type.  
  
### PubsubSettings

JSON representation  
---  
      
    
    {
      "googleServiceAccountEmail": string
    }  
  
Fields  
---  
`googleServiceAccountEmail` |  `string` Google Service Account Email.  
  
### DummyLogTypeSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "apiEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`apiEndpoint` |  `string` Full API Endpoint.  
  
### HttpsPushGoogleCloudPubSubSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### HttpsPushAmazonKinesisFirehoseSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### HttpsPushWebhookSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### AWSEC2HostsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSEC2InstancesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSEC2VpcsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSIAMSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "apiType": enum (ApiType)
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication  
`apiType` |  `enum (`ApiType`)` Supported AWS IAM api type.  
  
### NetskopeAlertV2Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "contentCategory": string,
      "contentTypes": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`contentCategory` |  `string` Content Category.  
`contentTypes[]` |  `string` Content type.  
  
### GoogleCloudStorageV2Settings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "chronicleServiceAccount": string,
      "maxLookbackDays": integer
    }  
  
Fields  
---  
`bucketUri` |  `string` Required. Google Cloud Storage Bucket URI for the feed.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
  
### AmazonS3V2Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([S3AuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3AuthV2))
      },
      "s3Uri": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`authentication` |  `object (`[S3AuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3AuthV2)`)` Required. Authentication.  
`s3Uri` |  `string` Required. S3 URI.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### S3AuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "accessKeySecretAuth": {
        object ([S3V2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AccessKeySecretAuth))
      },
      "awsIamRoleAuth": {
        object ([S3V2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AwsIamRoleAuth))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. auth type for S3. `auth_type` can be only one of the following:  
`accessKeySecretAuth` |  `object (`[S3V2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AccessKeySecretAuth)`)` Access Key ID and Secret Access Key for an AWS account.  
`awsIamRoleAuth` |  `object (`[S3V2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AwsIamRoleAuth)`)` AWS IAM Role Auth for Identity Federation.  
  
### S3V2AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Required. Access Key ID for an AWS account (a 20-character, alphanumeric string).  
`secretAccessKey` |  `string` Required. Secret Access Key for an AWS account (a 40-character string).  
  
### S3V2AwsIamRoleAuth

JSON representation  
---  
      
    
    {
      "awsIamRoleArn": string,
      "subjectId": string
    }  
  
Fields  
---  
`awsIamRoleArn` |  `string` AWS IAM Role for Identity Federation.  
`subjectId` |  `string` Subject ID to use for S3.  
  
### AmazonSQSV2Settings

JSON representation  
---  
      
    
    {
      "queue": string,
      "s3Uri": string,
      "authentication": {
        object ([SQSAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuthV2))
      },
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`queue` |  `string` Required. Amazon Resource Name(ARN) of the queue.  
`s3Uri` |  `string` Required. S3 URI.  
`authentication` |  `object (`[SQSAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuthV2)`)` Required. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### SQSAuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "sqsV2AccessKeySecretAuth": {
        object ([SQSV2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AccessKeySecretAuth))
      },
      "awsIamRoleAuth": {
        object ([SQSV2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AwsIamRoleAuth))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. auth tyoe for the SQS queue. `auth_type` can be only one of the following:  
`sqsV2AccessKeySecretAuth` |  `object (`[SQSV2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AccessKeySecretAuth)`)` Required. Auth key and secret for the SQS queue.  
`awsIamRoleAuth` |  `object (`[SQSV2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AwsIamRoleAuth)`)` Required. AWS IAM Role for Identity Federation.  
  
### SQSV2AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID of the S3 bucket. Ex: AKIABCDEFGHIJKL.  
`secretAccessKey` |  `string` Secret access key to access the S3 bucket.  
  
### SQSV2AwsIamRoleAuth

JSON representation  
---  
      
    
    {
      "awsIamRoleArn": string,
      "subjectId": string
    }  
  
Fields  
---  
`awsIamRoleArn` |  `string` AWS IAM Role for Identity Federation.  
`subjectId` |  `string` Subject ID to use for SQS.  
  
### AzureEventHubSettings

JSON representation  
---  
      
    
    {
      "name": string,
      "consumerGroup": string,
      "eventHubConnectionString": string,
      "azureStorageConnectionString": string,
      "azureStorageContainer": string,
      "azureSasToken": string,
      "eventHubNamespace": string
    }  
  
Fields  
---  
`name` |  `string` Required. Event hub to read from.  
`consumerGroup` |  `string` Required. Event hub consumer group to read from.  
`eventHubConnectionString` |  `string` Required. Event hub connection string for authentication.  
`azureStorageConnectionString` |  `string` Optional. Blob store connection string for authentication.  
`azureStorageContainer` |  `string` Optional. Blob storage container name.  
`azureSasToken` |  `string` Optional. SAS token  
`eventHubNamespace` |  `string` Output only. Event hub namespace  
  
### TrellixHxHostsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### TrellixStarXAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "msso": {
        object ([MssoAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MssoAuthentication))
      },
      "trellixIam": {
        object ([TrellixIAMAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixIAMAuthentication))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. One of multiple potential auth types. `auth_type` can be only one of the following:  
`msso` |  `object (`[MssoAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MssoAuthentication)`)` Input only. MssoAuthentication auth type.  
`trellixIam` |  `object (`[TrellixIAMAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixIAMAuthentication)`)` Input only. TrellixIAMAuthentication auth type.  
  
### MssoAuthentication

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string,
      "apiEndpoint": string
    }  
  
Fields  
---  
`username` |  `string` Required. Username for MSSO authentication. There are no restrictions on the format of the username. It has no default, specifically enforced min / max length or character set. The username will have been provided by an MSSO administrator and it is assumed that they have provided a username that is internally consistent with MSSO authentication requirements / validation.  
`password` |  `string` Required. Password of the account identified by username. There are no restrictions on the format of the password. It has no default, specifically enforced min / max length or character set. The password will have been provided by an MSSO administrator and it is assumed that they have provided a password that is internally consistent with MSSO authentication requirements / validation.  
`apiEndpoint` |  `string` Required. The login api endpoint url. This must be a valid URL with an http or https scheme. It has no default.  
  
### TrellixIAMAuthentication

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string,
      "scope": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. Client ID generated in Trellix IAM. This is a unique identifier for the user that is generated in Trellix IAM. It has no default, specifically enforced min / max length or character set. It is assumed that the Client ID generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.  
`clientSecret` |  `string` Required. Secret associated with the Client ID. This is the secret generated in Trellix IAM for the Client ID. It has no default, specifically enforced min / max length or character set. It is assumed that the secret generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.  
`scope` |  `string` Required. OAUTH 2 scope to request for the authentication token. This is the OAUTH 2 scope to request for the authentication token. It has no default, specifically enforced min / max length or character set. It is assumed that the scope provided is internally consistent with Trellix IAM authentication requirements / validation.  
  
### AzureBlobStoreV2Settings

JSON representation  
---  
      
    
    {
      "azureUri": string,
      "authentication": {
        object ([AzureAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuthV2))
      },
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`azureUri` |  `string` Required. Azure URI.  
`authentication` |  `object (`[AzureAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuthV2)`)` Required. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### AzureAuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "accessKey": string,
      "sasToken": string,
      "azureV2WorkloadIdentityFederation": {
        object ([AzureV2WorkloadIdentityFederation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureV2WorkloadIdentityFederation))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. Possible types of authentication. `auth_type` can be only one of the following:  
`accessKey` |  `string` Required. Access Key also known as shared key.  
`sasToken` |  `string` Required. SAS Token.  
`azureV2WorkloadIdentityFederation` |  `object (`[AzureV2WorkloadIdentityFederation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureV2WorkloadIdentityFederation)`)` Required. Azure V2 Workload Identity Federation.  
  
### AzureV2WorkloadIdentityFederation

JSON representation  
---  
      
    
    {
      "clientId": string,
      "tenantId": string,
      "subjectId": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. OAuth client ID.  
`tenantId` |  `string` Required. Tenant ID.  
`subjectId` |  `string` Required. Subject ID of the Azure subscription.  
  
### TrellixHxAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### GoogleCloudStorageEventDrivenSettings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "pubsubSubscription": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "chronicleServiceAccount": string,
      "maxLookbackDays": integer
    }  
  
Fields  
---  
`bucketUri` |  `string` Required. Google Cloud Storage Bucket URI for the feed.  
`pubsubSubscription` |  `string` Required. Subscription name for pubsub topic.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
  
### CrowdStrikeAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      },
      "hostname": string,
      "ingestionType": enum (IngestionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Required. OAuthClientCredentials.  
`hostname` |  `string` Required. API Hostname.  
`ingestionType` |  `enum (`IngestionType`)` Optional. Ingestion Type.  
  
### TrellixHxBulkAcqsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### MimecastMailV2Settings

JSON representation  
---  
      
    
    {
      "authCredentials": {
        object ([MimecastV2OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastV2OAuthClientCredentials))
      }
    }  
  
Fields  
---  
`authCredentials` |  `object (`[MimecastV2OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastV2OAuthClientCredentials)`)` Required. Mimecast OAuthClientCredentials.  
  
### MimecastV2OAuthClientCredentials

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. Client ID.  
`clientSecret` |  `string` Required. Client Secret.  
  
### ThreatConnectIoCV3Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "owners": [
        string
      ],
      "tqlQuery": string,
      "fields": [
        string
      ],
      "schedule": integer
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Required. Input only. UsernameSecretAuth.  
`hostname` |  `string` Required. hostname.  
`owners[]` |  `string` Required. Owners.  
`tqlQuery` |  `string` Optional. ThreatConnect Query Language filter.  
`fields[]` |  `string` Optional. Fields  
`schedule` |  `integer` Optional. Schedule  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FeedFailureDetails

JSON representation  
---  
      
    
    {
      "errorCode": string,
      "httpErrorCode": integer,
      "errorCause": string,
      "errorAction": string
    }  
  
Fields  
---  
`errorCode` |  `string` Output only. error_code contains the error code for the feed. The field is populated for the feeds with failed status.  
`httpErrorCode` |  `integer` Output only. http_error_code contains the HTTP error code for the feed failure. feed transfer failure may or may not result in http error code.  
`errorCause` |  `string` Output only. error_cause contains the information regarding the failure cause.  
`errorAction` |  `string` Output only. error_action contains the user action prescribed for remediation of feed error.  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
## Output Schema

Feed is a resource that contains feed information needed to create a feed.

### Feed

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "displayName": string,
      "details": {
        object ([FeedDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedDetails))
      },
      "state": enum (State),
      "failureMsg": string,
      "readOnly": boolean,
      "lastFeedInitiationTime": string,
      "failureDetails": {
        object ([FeedFailureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedFailureDetails))
      },
      "referenceId": string
    }  
  
Fields  
---  
`name` |  `string` The resource name of the feed. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}  
`uid` |  `string` Output only. Unique identifier for the feed.  
`displayName` |  `string` Customer-provided feed name.  
`details` |  `object (`[FeedDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedDetails)`)` Additional details of the feed, these details are dynamic and will be different for each of the feeds.  
`state` |  `enum (`State`)` Output only. State of the feed.  
`failureMsg` |  `string` Output only. Details about the most recent failure when feed state is FAILED.  
`readOnly` |  `boolean` Output only. Whether this feed can be updated or deleted.  
`lastFeedInitiationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Latest timestamp when the transfer was successful for the feed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`failureDetails` |  `object (`[FeedFailureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FeedFailureDetails)`)` Output only. Failure details for the feed. If the feed is in the failure state, this field will contain the details of the error cause and actions.  
`referenceId` |  `string` Output only. Reference ID, this field will contain the legacy id of the feed.  
  
### FeedDetails

JSON representation  
---  
      
    
    {
      "feedSourceType": enum (FeedSourceType),
      "logType": string,
      "assetNamespace": string,
      "labels": {
        string: string,
        ...
      },
      "stsMigrationReadiness": enum (STSMigrationReadiness),
    
      // Union field details can be only one of the following:
      "anomaliSettings": {
        object ([AnomaliIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AnomaliIocSettings))
      },
      "azureAdContextSettings": {
        object ([AzureADContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADContextSettings))
      },
      "cloudPassageSettings": {
        object ([CloudPassageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CloudPassageSettings))
      },
      "cortexXdrSettings": {
        object ([CortexXDRSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CortexXDRSettings))
      },
      "duoAuthSettings": {
        object ([DuoAuthSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoAuthSettings))
      },
      "duoUserContextSettings": {
        object ([DuoUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoUserContextSettings))
      },
      "microsoftGraphAlertSettings": {
        object ([MicrosoftGraphAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftGraphAlertSettings))
      },
      "microsoftSecurityCenterAlertSettings": {
        object ([MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftSecurityCenterAlertSettings))
      },
      "mimecastMailSettings": {
        object ([MimecastMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailSettings))
      },
      "office365Settings": {
        object ([Office365Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Office365Settings))
      },
      "proofpointMailSettings": {
        object ([ProofpointMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointMailSettings))
      },
      "recordedFutureIocSettings": {
        object ([RecordedFutureIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RecordedFutureIocSettings))
      },
      "workdaySettings": {
        object ([WorkdaySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdaySettings))
      },
      "panIocSettings": {
        object ([PanIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanIocSettings))
      },
      "oktaSettings": {
        object ([OktaSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaSettings))
      },
      "oktaUserContextSettings": {
        object ([OktaUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaUserContextSettings))
      },
      "foxItStixSettings": {
        object ([FoxITStixSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FoxITStixSettings))
      },
      "threatConnectIocSettings": {
        object ([ThreatConnectIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCSettings))
      },
      "serviceNowCmdbSettings": {
        object ([ServiceNowCMDBSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ServiceNowCMDBSettings))
      },
      "impervaWafSettings": {
        object ([ImpervaWAFSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ImpervaWAFSettings))
      },
      "thinkstCanarySettings": {
        object ([ThinkstCanarySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThinkstCanarySettings))
      },
      "rhIsacIocSettings": {
        object ([RHIsacIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RHIsacIocSettings))
      },
      "rapid7InsightSettings": {
        object ([Rapid7InsightSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Rapid7InsightSettings))
      },
      "salesforceSettings": {
        object ([SalesforceSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SalesforceSettings))
      },
      "netskopeAlertSettings": {
        object ([NetskopeAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertSettings))
      },
      "azureMdmIntuneSettings": {
        object ([AzureMDMIntuneSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureMDMIntuneSettings))
      },
      "azureAdSettings": {
        object ([AzureADSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADSettings))
      },
      "proofpointOnDemandSettings": {
        object ([ProofpointOnDemandSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointOnDemandSettings))
      },
      "workspaceUsersSettings": {
        object ([WorkspaceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceUsersSettings))
      },
      "workspaceActivitySettings": {
        object ([WorkspaceActivitySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceActivitySettings))
      },
      "workspaceAlertsSettings": {
        object ([WorkspaceAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceAlertsSettings))
      },
      "workspacePrivilegesSettings": {
        object ([WorkspacePrivilegesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspacePrivilegesSettings))
      },
      "workspaceMobileSettings": {
        object ([WorkspaceMobileSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceMobileSettings))
      },
      "workspaceChromeOsSettings": {
        object ([WorkspaceChromeOSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceChromeOSSettings))
      },
      "workspaceGroupsSettings": {
        object ([WorkspaceGroupsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceGroupsSettings))
      },
      "azureAdAuditSettings": {
        object ([AzureADAuditSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADAuditSettings))
      },
      "symantecEventExportSettings": {
        object ([SymantecEventExportSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SymantecEventExportSettings))
      },
      "qualysVmSettings": {
        object ([QualysVMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysVMSettings))
      },
      "panPrismaCloudSettings": {
        object ([PanPrismaCloudSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaCloudSettings))
      },
      "gcsSettings": {
        object ([GoogleCloudStorageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageSettings))
      },
      "httpSettings": {
        object ([HttpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpSettings))
      },
      "sftpSettings": {
        object ([SftpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpSettings))
      },
      "amazonS3Settings": {
        object ([AmazonS3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3Settings))
      },
      "azureBlobStoreSettings": {
        object ([AzureBlobStoreSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreSettings))
      },
      "amazonSqsSettings": {
        object ([AmazonSQSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSSettings))
      },
      "googleCloudIdentityDevicesSettings": {
        object ([GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDevicesSettings))
      },
      "googleCloudIdentityDeviceUsersSettings": {
        object ([GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDeviceUsersSettings))
      },
      "crowdstrikeDetectsSettings": {
        object ([CrowdStrikeDetectsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeDetectsSettings))
      },
      "mandiantIocSettings": {
        object ([MandiantIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MandiantIoCSettings))
      },
      "sentineloneAlertSettings": {
        object ([SentineloneAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SentineloneAlertSettings))
      },
      "qualysScanSettings": {
        object ([QualysScanSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysScanSettings))
      },
      "pubsubSettings": {
        object ([PubsubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PubsubSettings))
      },
      "amazonKinesisFirehoseSettings": {
        object (AmazonKinesisFirehoseSettings)
      },
      "webhookSettings": {
        object (WebhookSettings)
      },
      "dummyLogTypeSettings": {
        object ([DummyLogTypeSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DummyLogTypeSettings))
      },
      "httpsPushGoogleCloudPubsubSettings": {
        object ([HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushGoogleCloudPubSubSettings))
      },
      "httpsPushAmazonKinesisFirehoseSettings": {
        object ([HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushAmazonKinesisFirehoseSettings))
      },
      "httpsPushWebhookSettings": {
        object ([HttpsPushWebhookSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushWebhookSettings))
      },
      "awsEc2HostsSettings": {
        object ([AWSEC2HostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2HostsSettings))
      },
      "awsEc2InstancesSettings": {
        object ([AWSEC2InstancesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2InstancesSettings))
      },
      "awsEc2VpcsSettings": {
        object ([AWSEC2VpcsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2VpcsSettings))
      },
      "awsIamSettings": {
        object ([AWSIAMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSIAMSettings))
      },
      "netskopeAlertV2Settings": {
        object ([NetskopeAlertV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertV2Settings))
      },
      "gcsV2Settings": {
        object ([GoogleCloudStorageV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageV2Settings))
      },
      "amazonS3V2Settings": {
        object ([AmazonS3V2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3V2Settings))
      },
      "amazonSqsV2Settings": {
        object ([AmazonSQSV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSV2Settings))
      },
      "azureEventHubSettings": {
        object ([AzureEventHubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureEventHubSettings))
      },
      "trellixHxHostsSettings": {
        object ([TrellixHxHostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxHostsSettings))
      },
      "azureBlobStoreV2Settings": {
        object ([AzureBlobStoreV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreV2Settings))
      },
      "trellixHxAlertsSettings": {
        object ([TrellixHxAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxAlertsSettings))
      },
      "googleCloudStorageEventDrivenSettings": {
        object ([GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageEventDrivenSettings))
      },
      "crowdstrikeAlertsSettings": {
        object ([CrowdStrikeAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeAlertsSettings))
      },
      "trellixHxBulkAcqsSettings": {
        object ([TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxBulkAcqsSettings))
      },
      "mimecastMailV2Settings": {
        object ([MimecastMailV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailV2Settings))
      },
      "threatConnectIocV3Settings": {
        object ([ThreatConnectIoCV3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCV3Settings))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`feedSourceType` |  `enum (`FeedSourceType`)` Source Type of the feed.  
`logType` |  `string` LogType. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}  
`assetNamespace` |  `string` The asset namespace to apply to all logs ingested through this feed.  
`labels` |  `map (key: string, value: string)` The ingestion metadata labels to apply to all logs ingested through this feed, and the resulting normalized data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stsMigrationReadiness` |  `enum (`STSMigrationReadiness`)` Optional. The status of the feed's migration to STS.  
Union field `details`. Additional details of the feed. Depends on the feed type. `details` can be only one of the following:  
`anomaliSettings` |  `object (`[AnomaliIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AnomaliIocSettings)`)` Anomali IOC settings.  
`azureAdContextSettings` |  `object (`[AzureADContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADContextSettings)`)` Azure AD Context settings.  
`cloudPassageSettings` |  `object (`[CloudPassageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CloudPassageSettings)`)` Cloud Passage settings.  
`cortexXdrSettings` |  `object (`[CortexXDRSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CortexXDRSettings)`)` Cortex XDR settings.  
`duoAuthSettings` |  `object (`[DuoAuthSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoAuthSettings)`)` Duo Auth settings.  
`duoUserContextSettings` |  `object (`[DuoUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DuoUserContextSettings)`)` Duo User Context settings.  
`microsoftGraphAlertSettings` |  `object (`[MicrosoftGraphAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftGraphAlertSettings)`)` Microsoft Graph Alert settings.  
`microsoftSecurityCenterAlertSettings` |  `object (`[MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftSecurityCenterAlertSettings)`)` Microsoft Security center alert settings.  
`mimecastMailSettings` |  `object (`[MimecastMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailSettings)`)` Mimecast mail settings.  
`office365Settings` |  `object (`[Office365Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Office365Settings)`)` Office 365 settings.  
`proofpointMailSettings` |  `object (`[ProofpointMailSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointMailSettings)`)` Proofpoint mail settings.  
`recordedFutureIocSettings` |  `object (`[RecordedFutureIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RecordedFutureIocSettings)`)` Recorded Future IOC settings.  
`workdaySettings` |  `object (`[WorkdaySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdaySettings)`)` Workday settings.  
`panIocSettings` |  `object (`[PanIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanIocSettings)`)` PAN IOC settings.  
`oktaSettings` |  `object (`[OktaSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaSettings)`)` Okta settings.  
`oktaUserContextSettings` |  `object (`[OktaUserContextSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OktaUserContextSettings)`)` Okta user context settings.  
`foxItStixSettings` |  `object (`[FoxITStixSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.FoxITStixSettings)`)` Fox-IT STIX settings.  
`threatConnectIocSettings` |  `object (`[ThreatConnectIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCSettings)`)` ThreatConnect IOC settings.  
`serviceNowCmdbSettings` |  `object (`[ServiceNowCMDBSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ServiceNowCMDBSettings)`)` ServiceNow CMDB settings.  
`impervaWafSettings` |  `object (`[ImpervaWAFSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ImpervaWAFSettings)`)` Imperva WAF settings.  
`thinkstCanarySettings` |  `object (`[ThinkstCanarySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThinkstCanarySettings)`)` Thinkst Canary settings.  
`rhIsacIocSettings` |  `object (`[RHIsacIocSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RHIsacIocSettings)`)` RH-ISAC IOC settings.  
`rapid7InsightSettings` |  `object (`[Rapid7InsightSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Rapid7InsightSettings)`)` Rapid7 Insight settings.  
`salesforceSettings` |  `object (`[SalesforceSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SalesforceSettings)`)` Salesforce settings.  
`netskopeAlertSettings` |  `object (`[NetskopeAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertSettings)`)` Netskope alert settings.  
`azureMdmIntuneSettings` |  `object (`[AzureMDMIntuneSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureMDMIntuneSettings)`)` Azure MDM Intune settings.  
`azureAdSettings` |  `object (`[AzureADSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADSettings)`)` Azure AD settings.  
`proofpointOnDemandSettings` |  `object (`[ProofpointOnDemandSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ProofpointOnDemandSettings)`)` Proofpoint On-Demand settings.  
`workspaceUsersSettings` |  `object (`[WorkspaceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceUsersSettings)`)` Workspace users settings.  
`workspaceActivitySettings` |  `object (`[WorkspaceActivitySettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceActivitySettings)`)` Workspace activity settings.  
`workspaceAlertsSettings` |  `object (`[WorkspaceAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceAlertsSettings)`)` Workspace alerts settings.  
`workspacePrivilegesSettings` |  `object (`[WorkspacePrivilegesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspacePrivilegesSettings)`)` Workspace privileges settings.  
`workspaceMobileSettings` |  `object (`[WorkspaceMobileSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceMobileSettings)`)` Workspace mobile settings.  
`workspaceChromeOsSettings` |  `object (`[WorkspaceChromeOSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceChromeOSSettings)`)` Workspace ChromeOS settings.  
`workspaceGroupsSettings` |  `object (`[WorkspaceGroupsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkspaceGroupsSettings)`)` Workspace Groups settings.  
`azureAdAuditSettings` |  `object (`[AzureADAuditSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureADAuditSettings)`)` Azure AD Audit settings.  
`symantecEventExportSettings` |  `object (`[SymantecEventExportSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SymantecEventExportSettings)`)` Symantec Event Export settings.  
`qualysVmSettings` |  `object (`[QualysVMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysVMSettings)`)` Qualys VM settings  
`panPrismaCloudSettings` |  `object (`[PanPrismaCloudSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaCloudSettings)`)` PAN Prisma Cloud settings.  
`gcsSettings` |  `object (`[GoogleCloudStorageSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageSettings)`)` Google Cloud Storage settings.  
`httpSettings` |  `object (`[HttpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpSettings)`)` HTTP settings.  
`sftpSettings` |  `object (`[SftpSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpSettings)`)` SFTP settings.  
`amazonS3Settings` |  `object (`[AmazonS3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3Settings)`)` Amazon S3 settings.  
`azureBlobStoreSettings` |  `object (`[AzureBlobStoreSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreSettings)`)` Azure Blob Storage settings.  
`amazonSqsSettings` |  `object (`[AmazonSQSSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSSettings)`)` Amazon SQS settings.  
`googleCloudIdentityDevicesSettings` |  `object (`[GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDevicesSettings)`)` Google Cloud Identity Devices settings.  
`googleCloudIdentityDeviceUsersSettings` |  `object (`[GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudIdentityDeviceUsersSettings)`)` Google Cloud Identity Device Users settings.  
`crowdstrikeDetectsSettings` |  `object (`[CrowdStrikeDetectsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeDetectsSettings)`)` CrowdStrike Detects API settings.  
`mandiantIocSettings` |  `object (`[MandiantIoCSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MandiantIoCSettings)`)` Mandiant IOC settings.  
`sentineloneAlertSettings` |  `object (`[SentineloneAlertSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SentineloneAlertSettings)`)` SentinelOne Alert settings.  
`qualysScanSettings` |  `object (`[QualysScanSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.QualysScanSettings)`)` Qualys Scan Settings  
`pubsubSettings` |  `object (`[PubsubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PubsubSettings)`)` Pub/Sub settings.  
`amazonKinesisFirehoseSettings` |  `object (`AmazonKinesisFirehoseSettings`)` Amazon Kinesis Firehose settings.  
`webhookSettings` |  `object (`WebhookSettings`)` Webhook settings.  
`dummyLogTypeSettings` |  `object (`[DummyLogTypeSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.DummyLogTypeSettings)`)` DummyLogType Settings.  
`httpsPushGoogleCloudPubsubSettings` |  `object (`[HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushGoogleCloudPubSubSettings)`)` Https push Google Pub/Sub settings.  
`httpsPushAmazonKinesisFirehoseSettings` |  `object (`[HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushAmazonKinesisFirehoseSettings)`)` Https push Amazon Kinesis Firehose settings.  
`httpsPushWebhookSettings` |  `object (`[HttpsPushWebhookSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpsPushWebhookSettings)`)` Https push Webhook settings.  
`awsEc2HostsSettings` |  `object (`[AWSEC2HostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2HostsSettings)`)` AWS EC2 Hosts settings.  
`awsEc2InstancesSettings` |  `object (`[AWSEC2InstancesSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2InstancesSettings)`)` AWS EC2 Instances settings.  
`awsEc2VpcsSettings` |  `object (`[AWSEC2VpcsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSEC2VpcsSettings)`)` AWS EC2 Vpcs settings.  
`awsIamSettings` |  `object (`[AWSIAMSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AWSIAMSettings)`)` AWS IAM settings.  
`netskopeAlertV2Settings` |  `object (`[NetskopeAlertV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.NetskopeAlertV2Settings)`)` Netskope alert V2 settings.  
`gcsV2Settings` |  `object (`[GoogleCloudStorageV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageV2Settings)`)` Settings for Google Cloud Storage Omniflow feeds.  
`amazonS3V2Settings` |  `object (`[AmazonS3V2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonS3V2Settings)`)` Settings for S3 Omniflow feeds.  
`amazonSqsV2Settings` |  `object (`[AmazonSQSV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AmazonSQSV2Settings)`)` Settings for SQS Omniflow feeds.  
`azureEventHubSettings` |  `object (`[AzureEventHubSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureEventHubSettings)`)` Settings for Omniflow based native ingestion from azure event hub.  
`trellixHxHostsSettings` |  `object (`[TrellixHxHostsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxHostsSettings)`)` Settings for Trellix HX Host Metadata.  
`azureBlobStoreV2Settings` |  `object (`[AzureBlobStoreV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureBlobStoreV2Settings)`)` Settings for Azure Blobstore Omniflow feeds.  
`trellixHxAlertsSettings` |  `object (`[TrellixHxAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxAlertsSettings)`)` Settings for Trellix HX Alerts Metadata.  
`googleCloudStorageEventDrivenSettings` |  `object (`[GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.GoogleCloudStorageEventDrivenSettings)`)` Settings for Omniflow based Google Cloud Storage event driven feeds.  
`crowdstrikeAlertsSettings` |  `object (`[CrowdStrikeAlertsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.CrowdStrikeAlertsSettings)`)` CrowdStrike Alerts API settings.  
`trellixHxBulkAcqsSettings` |  `object (`[TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixHxBulkAcqsSettings)`)` Settings for Trellix HX Bulk Acquisitions Metadata.  
`mimecastMailV2Settings` |  `object (`[MimecastMailV2Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastMailV2Settings)`)` Required. Mimecast mail v2 settings.  
`threatConnectIocV3Settings` |  `object (`[ThreatConnectIoCV3Settings](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.ThreatConnectIoCV3Settings)`)` Threat Connect IOC V3 settings.  
  
### AnomaliIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
  
### UsernameSecretAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "secret": string
    }  
  
Fields  
---  
`user` |  `string` Username of an identity used for authentication.  
`secret` |  `string` Secret of the account identified by user_name.  
  
### AzureADContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "retrieveDevices": boolean,
      "retrieveGroups": boolean,
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`retrieveDevices` |  `boolean` Whether to retrieve device information in user context.  
`retrieveGroups` |  `boolean` Whether to retrieve group information in user context.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MicrosoftOAuthClientCredentials

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
  
### CloudPassageSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "eventTypes": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`eventTypes[]` |  `string` Event types filter for the events API.  
  
### CortexXDRSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`endpoint` |  `string` API Endpoint.  
  
### HttpHeaderAuth

JSON representation  
---  
      
    
    {
      "headerKeyValues": [
        {
          object ([HeaderKeyValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HeaderKeyValue))
        }
      ]
    }  
  
Fields  
---  
`headerKeyValues[]` |  `object (`[HeaderKeyValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HeaderKeyValue)`)` Header key-value pairs.  
  
### HeaderKeyValue

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Key.  
`value` |  `string` Value.  
  
### DuoAuthSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### DuoUserContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API hostname.  
  
### MicrosoftGraphAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MicrosoftSecurityCenterAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "subscriptionId": string,
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`subscriptionId` |  `string` Subscription ID of the Microsoft security center alert settings alert.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### MimecastMailSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### Office365Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "contentType": enum (ContentType),
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`contentType` |  `enum (`ContentType`)` Supported office 365 content type.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### ProofpointMailSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
  
### RecordedFutureIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
  
### WorkdaySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([WorkdayAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdayAuth))
      },
      "hostname": string,
      "tenantId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[WorkdayAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.WorkdayAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`tenantId` |  `string` Tenant ID.  
  
### WorkdayAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "secret": string,
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "refreshToken": string
    }  
  
Fields  
---  
`user` |  `string` Username. This is unused: Workday feeds were originally configured using a username and secret authentication method, but only the secret field was used, and it was used to supply the OAuth access token.  
`secret` |  `string` The access token used to authenticate against Workday. This field is called "secret" to maintain backwards compatibility. Workday was (only) configured using username (which was unused) and secret (which is used as the access token). Either this field or all of the other OAuth fields below must be specified.  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client Secret.  
`refreshToken` |  `string` Refresh Token.  
  
### PanIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "feedId": string,
      "feed": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`feedId` |  `string` PAN IOC feed ID.  
`feed` |  `string` PAN IOC feed name.  
  
### OktaSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### OktaUserContextSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "managerIdReferenceField": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`managerIdReferenceField` |  `string` Manager id reference field.  
  
### FoxITStixSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "ssl": {
        object ([SSLClientKeypair](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SSLClientKeypair))
      },
      "pollServiceUri": string,
      "collection": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`ssl` |  `object (`[SSLClientKeypair](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SSLClientKeypair)`)` SSL client key pair.  
`pollServiceUri` |  `string` TAXII poll service URI.  
`collection` |  `string` Collection available at the poll service.  
  
### SSLClientKeypair

JSON representation  
---  
      
    
    {
      "encodedPrivateKey": string,
      "sslCertificate": string
    }  
  
Fields  
---  
`encodedPrivateKey` |  `string` The encoded private key. The string should be a private key in PEM format, and should include the begin header and end footer lines. It may also include newlines.Example: -----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED DEK-Info: DES-EDE3-CBC,F23074E02CF47304 \-----END RSA PRIVATE KEY-----  
`sslCertificate` |  `string` The encoded SSL certificate. The string should be an SSL certificate in PEM format, and should include the begin header and end footer lines. It may also include newlines.Example: -----BEGIN CERTIFICATE-----  \-----END CERTIFICATE-----  
  
### ThreatConnectIoCSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "owners": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`owners[]` |  `string` Owners.  
  
### ServiceNowCMDBSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "feedname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`feedname` |  `string` Feedname.  
  
### ImpervaWAFSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
  
### ThinkstCanarySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### RHIsacIocSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Input only. Authentication.  
  
### OAuthClientCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
  
### Rapid7InsightSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "endpoint": string,
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`endpoint` |  `string` Rapid7 API endpoint. Should be "vulnerabilities" or "assets".  
`hostname` |  `string` API Hostname.  
  
### SalesforceSettings

JSON representation  
---  
      
    
    {
      "hostname": string,
    
      // Union field authentication can be only one of the following:
      "oauthPasswordGrantAuth": {
        object ([OAuthPasswordGrantCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthPasswordGrantCredentials))
      },
      "oauthJwtCredentials": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      }
      // End of list of possible types for union field authentication.
    }  
  
Fields  
---  
`hostname` |  `string` API hostname.  
Union field `authentication`. Possible types of authentication. `authentication` can be only one of the following:  
`oauthPasswordGrantAuth` |  `object (`[OAuthPasswordGrantCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthPasswordGrantCredentials)`)` Input only. OAuthPasswordGrantCredentials auth.  
`oauthJwtCredentials` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. OAuthJWTCredentials auth.  
  
### OAuthPasswordGrantCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "user": string,
      "password": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
`user` |  `string` Username.  
`password` |  `string` Password.  
  
### OAuthJWTCredentials

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "claims": {
        object ([Claims](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Claims))
      },
    
      // Union field credentials can be only one of the following:
      "rsCredentials": {
        object ([RSCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RSCredentials))
      }
      // End of list of possible types for union field credentials.
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`claims` |  `object (`[Claims](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.Claims)`)` Claims.  
Union field `credentials`. Credentials. `credentials` can be only one of the following:  
`rsCredentials` |  `object (`[RSCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.RSCredentials)`)` RS credentials.  
  
### RSCredentials

JSON representation  
---  
      
    
    {
      "privateKey": string
    }  
  
Fields  
---  
`privateKey` |  `string` Private key in PEM format.  
  
### Claims

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "audience": string
    }  
  
Fields  
---  
`issuer` |  `string` Issuer. Usually the client_id.  
`subject` |  `string` Subject. Usually the email.  
`audience` |  `string` Audience.  
  
### NetskopeAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "feedname": string,
      "contentType": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`feedname` |  `string` Feedname.  
`contentType` |  `string` Content type.  
  
### AzureMDMIntuneSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### AzureADSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### ProofpointOnDemandSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "clusterId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`clusterId` |  `string` Cluster ID.  
  
### WorkspaceUsersSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string,
      "projectionType": enum (ProjectionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
`projectionType` |  `enum (`ProjectionType`)` Optional. Projection Type.  
  
### WorkspaceActivitySettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string,
      "applications": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
`applications[]` |  `string` Applications.  
  
### WorkspaceAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspacePrivilegesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceMobileSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceChromeOSSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### WorkspaceGroupsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "workspaceCustomerId": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
`workspaceCustomerId` |  `string` Customer ID.  
  
### AzureADAuditSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials))
      },
      "tenantId": string,
      "hostname": string,
      "authEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[MicrosoftOAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MicrosoftOAuthClientCredentials)`)` Input only. Authentication.  
`tenantId` |  `string` Tenant ID.  
`hostname` |  `string` API Hostname.  
`authEndpoint` |  `string` API Auth Endpoint.  
  
### SymantecEventExportSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthRefreshToken](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthRefreshToken))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthRefreshToken](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthRefreshToken)`)` Input only. Authentication.  
  
### OAuthRefreshToken

JSON representation  
---  
      
    
    {
      "tokenEndpoint": string,
      "clientId": string,
      "clientSecret": string,
      "refreshToken": string
    }  
  
Fields  
---  
`tokenEndpoint` |  `string` Token endpoint to get the OAuth token from.  
`clientId` |  `string` Client ID.  
`clientSecret` |  `string` Client secret.  
`refreshToken` |  `string` Refresh token.  
  
### QualysVMSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### PanPrismaCloudSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([PanPrismaAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaAuth))
      },
      "hostname": string
    }  
  
Fields  
---  
`authentication` |  `object (`[PanPrismaAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.PanPrismaAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
  
### PanPrismaAuth

JSON representation  
---  
      
    
    {
      "user": string,
      "password": string
    }  
  
Fields  
---  
`user` |  `string` Username.  
`password` |  `string` Password.  
  
### GoogleCloudStorageSettings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption),
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`bucketUri` |  `string` Bucket URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
`chronicleServiceAccount` |  `string` Output only. Service Account Chronicle will be using to pull data.  
  
### HttpSettings

JSON representation  
---  
      
    
    {
      "uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`uri` |  `string` HTTP URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SftpSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([SftpAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpAuth))
      },
      "uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[SftpAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SftpAuth)`)` Input only. Authentication.  
`uri` |  `string` SFTP URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SftpAuth

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string,
      "privateKey": string,
      "privateKeyPassphrase": string
    }  
  
Fields  
---  
`username` |  `string` Username. Used for username and password authentication.  
`password` |  `string` Password. Used for username and password authentication.  
`privateKey` |  `string` Private key. Used for private key authentication.  
`privateKeyPassphrase` |  `string` Private key passphrase. Used for private key authentication.  
  
### AmazonS3Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([S3Auth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3Auth))
      },
      "s3Uri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[S3Auth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3Auth)`)` Input only. Authentication.  
`s3Uri` |  `string` S3 URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### S3Auth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string,
      "clientId": string,
      "clientSecret": string,
      "refreshUri": string,
      "region": enum (S3Region)
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID. Used when using access key auth.  
`secretAccessKey` |  `string` Secret access key. Used when using access key auth.  
`clientId` |  `string` Client ID. Used when using OAuth auth.  
`clientSecret` |  `string` Client secret. Used when using OAuth auth.  
`refreshUri` |  `string` Refresh URI. Used when using OAuth auth.  
`region` |  `enum (`S3Region`)` S3 Region.  
  
### AzureBlobStoreSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([AzureAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuth))
      },
      "azureUri": string,
      "sourceType": enum (URISourceType),
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`authentication` |  `object (`[AzureAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuth)`)` Input only. Authentication.  
`azureUri` |  `string` Azure URI.  
`sourceType` |  `enum (`URISourceType`)` The URI source type.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### AzureAuth

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "sharedKey": string,
      "sasToken": string
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. Type of auth used with Azure. `auth_type` can be only one of the following:  
`sharedKey` |  `string` Shared Key.  
`sasToken` |  `string` SAS Token.  
  
### AmazonSQSSettings

JSON representation  
---  
      
    
    {
      "region": enum (S3Region),
      "queue": string,
      "accountNumber": string,
      "authentication": {
        object ([SQSAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuth))
      },
      "sourceDeletionOption": enum (SourceDeletionOption)
    }  
  
Fields  
---  
`region` |  `enum (`S3Region`)` S3 Region.  
`queue` |  `string` Name of the queue.  
`accountNumber` |  `string` Account number of the owner of the queue.  
`authentication` |  `object (`[SQSAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuth)`)` Input only. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOption`)` Source deletion option.  
  
### SQSAuth

JSON representation  
---  
      
    
    {
      "sqsAccessKeySecretAuth": {
        object ([SQSAccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAccessKeySecretAuth))
      },
      "additionalS3AccessKeySecretAuth": {
        object ([AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AdditionalS3AccessKeySecretAuth))
      }
    }  
  
Fields  
---  
`sqsAccessKeySecretAuth` |  `object (`[SQSAccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAccessKeySecretAuth)`)` SQS access key secret auth.  
`additionalS3AccessKeySecretAuth` |  `object (`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AdditionalS3AccessKeySecretAuth)`)` Authentication for the S3 bucket referred to by the items in the SQS queue. This is only required if it is different from the authentication for the queue.  
  
### SQSAccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID.  
`secretAccessKey` |  `string` Secret access key.  
  
### AdditionalS3AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID.  
`secretAccessKey` |  `string` Secret access key.  
  
### GoogleCloudIdentityDevicesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      },
      "apiVersion": string
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication  
`apiVersion` |  `string` API Version  
  
### GoogleCloudIdentityDeviceUsersSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthJWTCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthJWTCredentials)`)` Input only. Authentication.  
  
### CrowdStrikeDetectsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      },
      "hostname": string,
      "ingestionType": enum (IngestionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Input only. OAuthClientCredentials.  
`hostname` |  `string` API Hostname.  
`ingestionType` |  `enum (`IngestionType`)` Optional. Ingestion Type.  
  
### MandiantIoCSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "startTime": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` time since when to start fetching the IOCsUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### SentineloneAlertSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "initialStartTime": string,
      "isAlertApiSubscribed": boolean
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` Hostname of SentinelOne alert settings.  
`initialStartTime` |  `string` initialStartTime from when to fetch the alerts  
`isAlertApiSubscribed` |  `boolean` Is the customer subscribed to Alerts Api  
  
### QualysScanSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "apiType": enum (ApiType)
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication  
`hostname` |  `string` Hostname.  
`apiType` |  `enum (`ApiType`)` Supported Qualys Scan api type.  
  
### PubsubSettings

JSON representation  
---  
      
    
    {
      "googleServiceAccountEmail": string
    }  
  
Fields  
---  
`googleServiceAccountEmail` |  `string` Google Service Account Email.  
  
### DummyLogTypeSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "apiEndpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`apiEndpoint` |  `string` Full API Endpoint.  
  
### HttpsPushGoogleCloudPubSubSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### HttpsPushAmazonKinesisFirehoseSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### HttpsPushWebhookSettings

JSON representation  
---  
      
    
    {
      "splitDelimiter": string
    }  
  
Fields  
---  
`splitDelimiter` |  `string` Optional. Delimiter to split on for the feed.  
  
### AWSEC2HostsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSEC2InstancesSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSEC2VpcsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      }
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. UsernameSecretAuth.  
  
### AWSIAMSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "apiType": enum (ApiType)
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Input only. Authentication  
`apiType` |  `enum (`ApiType`)` Supported AWS IAM api type.  
  
### NetskopeAlertV2Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth))
      },
      "hostname": string,
      "contentCategory": string,
      "contentTypes": [
        string
      ]
    }  
  
Fields  
---  
`authentication` |  `object (`[HttpHeaderAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.HttpHeaderAuth)`)` Input only. Authentication.  
`hostname` |  `string` API Hostname.  
`contentCategory` |  `string` Content Category.  
`contentTypes[]` |  `string` Content type.  
  
### GoogleCloudStorageV2Settings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "chronicleServiceAccount": string,
      "maxLookbackDays": integer
    }  
  
Fields  
---  
`bucketUri` |  `string` Required. Google Cloud Storage Bucket URI for the feed.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
  
### AmazonS3V2Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([S3AuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3AuthV2))
      },
      "s3Uri": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`authentication` |  `object (`[S3AuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3AuthV2)`)` Required. Authentication.  
`s3Uri` |  `string` Required. S3 URI.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### S3AuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "accessKeySecretAuth": {
        object ([S3V2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AccessKeySecretAuth))
      },
      "awsIamRoleAuth": {
        object ([S3V2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AwsIamRoleAuth))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. auth type for S3. `auth_type` can be only one of the following:  
`accessKeySecretAuth` |  `object (`[S3V2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AccessKeySecretAuth)`)` Access Key ID and Secret Access Key for an AWS account.  
`awsIamRoleAuth` |  `object (`[S3V2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.S3V2AwsIamRoleAuth)`)` AWS IAM Role Auth for Identity Federation.  
  
### S3V2AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Required. Access Key ID for an AWS account (a 20-character, alphanumeric string).  
`secretAccessKey` |  `string` Required. Secret Access Key for an AWS account (a 40-character string).  
  
### S3V2AwsIamRoleAuth

JSON representation  
---  
      
    
    {
      "awsIamRoleArn": string,
      "subjectId": string
    }  
  
Fields  
---  
`awsIamRoleArn` |  `string` AWS IAM Role for Identity Federation.  
`subjectId` |  `string` Subject ID to use for S3.  
  
### AmazonSQSV2Settings

JSON representation  
---  
      
    
    {
      "queue": string,
      "s3Uri": string,
      "authentication": {
        object ([SQSAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuthV2))
      },
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`queue` |  `string` Required. Amazon Resource Name(ARN) of the queue.  
`s3Uri` |  `string` Required. S3 URI.  
`authentication` |  `object (`[SQSAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSAuthV2)`)` Required. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### SQSAuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "sqsV2AccessKeySecretAuth": {
        object ([SQSV2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AccessKeySecretAuth))
      },
      "awsIamRoleAuth": {
        object ([SQSV2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AwsIamRoleAuth))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. auth tyoe for the SQS queue. `auth_type` can be only one of the following:  
`sqsV2AccessKeySecretAuth` |  `object (`[SQSV2AccessKeySecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AccessKeySecretAuth)`)` Required. Auth key and secret for the SQS queue.  
`awsIamRoleAuth` |  `object (`[SQSV2AwsIamRoleAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.SQSV2AwsIamRoleAuth)`)` Required. AWS IAM Role for Identity Federation.  
  
### SQSV2AccessKeySecretAuth

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` Access key ID of the S3 bucket. Ex: AKIABCDEFGHIJKL.  
`secretAccessKey` |  `string` Secret access key to access the S3 bucket.  
  
### SQSV2AwsIamRoleAuth

JSON representation  
---  
      
    
    {
      "awsIamRoleArn": string,
      "subjectId": string
    }  
  
Fields  
---  
`awsIamRoleArn` |  `string` AWS IAM Role for Identity Federation.  
`subjectId` |  `string` Subject ID to use for SQS.  
  
### AzureEventHubSettings

JSON representation  
---  
      
    
    {
      "name": string,
      "consumerGroup": string,
      "eventHubConnectionString": string,
      "azureStorageConnectionString": string,
      "azureStorageContainer": string,
      "azureSasToken": string,
      "eventHubNamespace": string
    }  
  
Fields  
---  
`name` |  `string` Required. Event hub to read from.  
`consumerGroup` |  `string` Required. Event hub consumer group to read from.  
`eventHubConnectionString` |  `string` Required. Event hub connection string for authentication.  
`azureStorageConnectionString` |  `string` Optional. Blob store connection string for authentication.  
`azureStorageContainer` |  `string` Optional. Blob storage container name.  
`azureSasToken` |  `string` Optional. SAS token  
`eventHubNamespace` |  `string` Output only. Event hub namespace  
  
### TrellixHxHostsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### TrellixStarXAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "msso": {
        object ([MssoAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MssoAuthentication))
      },
      "trellixIam": {
        object ([TrellixIAMAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixIAMAuthentication))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. One of multiple potential auth types. `auth_type` can be only one of the following:  
`msso` |  `object (`[MssoAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MssoAuthentication)`)` Input only. MssoAuthentication auth type.  
`trellixIam` |  `object (`[TrellixIAMAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixIAMAuthentication)`)` Input only. TrellixIAMAuthentication auth type.  
  
### MssoAuthentication

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string,
      "apiEndpoint": string
    }  
  
Fields  
---  
`username` |  `string` Required. Username for MSSO authentication. There are no restrictions on the format of the username. It has no default, specifically enforced min / max length or character set. The username will have been provided by an MSSO administrator and it is assumed that they have provided a username that is internally consistent with MSSO authentication requirements / validation.  
`password` |  `string` Required. Password of the account identified by username. There are no restrictions on the format of the password. It has no default, specifically enforced min / max length or character set. The password will have been provided by an MSSO administrator and it is assumed that they have provided a password that is internally consistent with MSSO authentication requirements / validation.  
`apiEndpoint` |  `string` Required. The login api endpoint url. This must be a valid URL with an http or https scheme. It has no default.  
  
### TrellixIAMAuthentication

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string,
      "scope": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. Client ID generated in Trellix IAM. This is a unique identifier for the user that is generated in Trellix IAM. It has no default, specifically enforced min / max length or character set. It is assumed that the Client ID generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.  
`clientSecret` |  `string` Required. Secret associated with the Client ID. This is the secret generated in Trellix IAM for the Client ID. It has no default, specifically enforced min / max length or character set. It is assumed that the secret generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.  
`scope` |  `string` Required. OAUTH 2 scope to request for the authentication token. This is the OAUTH 2 scope to request for the authentication token. It has no default, specifically enforced min / max length or character set. It is assumed that the scope provided is internally consistent with Trellix IAM authentication requirements / validation.  
  
### AzureBlobStoreV2Settings

JSON representation  
---  
      
    
    {
      "azureUri": string,
      "authentication": {
        object ([AzureAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuthV2))
      },
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "maxLookbackDays": integer,
      "chronicleServiceAccount": string
    }  
  
Fields  
---  
`azureUri` |  `string` Required. Azure URI.  
`authentication` |  `object (`[AzureAuthV2](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureAuthV2)`)` Required. Authentication.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
  
### AzureAuthV2

JSON representation  
---  
      
    
    {
    
      // Union field auth_type can be only one of the following:
      "accessKey": string,
      "sasToken": string,
      "azureV2WorkloadIdentityFederation": {
        object ([AzureV2WorkloadIdentityFederation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureV2WorkloadIdentityFederation))
      }
      // End of list of possible types for union field auth_type.
    }  
  
Fields  
---  
Union field `auth_type`. Possible types of authentication. `auth_type` can be only one of the following:  
`accessKey` |  `string` Required. Access Key also known as shared key.  
`sasToken` |  `string` Required. SAS Token.  
`azureV2WorkloadIdentityFederation` |  `object (`[AzureV2WorkloadIdentityFederation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.AzureV2WorkloadIdentityFederation)`)` Required. Azure V2 Workload Identity Federation.  
  
### AzureV2WorkloadIdentityFederation

JSON representation  
---  
      
    
    {
      "clientId": string,
      "tenantId": string,
      "subjectId": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. OAuth client ID.  
`tenantId` |  `string` Required. Tenant ID.  
`subjectId` |  `string` Required. Subject ID of the Azure subscription.  
  
### TrellixHxAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### GoogleCloudStorageEventDrivenSettings

JSON representation  
---  
      
    
    {
      "bucketUri": string,
      "pubsubSubscription": string,
      "sourceDeletionOption": enum (SourceDeletionOptionV2),
      "chronicleServiceAccount": string,
      "maxLookbackDays": integer
    }  
  
Fields  
---  
`bucketUri` |  `string` Required. Google Cloud Storage Bucket URI for the feed.  
`pubsubSubscription` |  `string` Required. Subscription name for pubsub topic.  
`sourceDeletionOption` |  `enum (`SourceDeletionOptionV2`)` Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.  
`chronicleServiceAccount` |  `string` Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.  
`maxLookbackDays` |  `integer` Optional. Maximum File Age to ingest in days.  
  
### CrowdStrikeAlertsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials))
      },
      "hostname": string,
      "ingestionType": enum (IngestionType)
    }  
  
Fields  
---  
`authentication` |  `object (`[OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.OAuthClientCredentials)`)` Required. OAuthClientCredentials.  
`hostname` |  `string` Required. API Hostname.  
`ingestionType` |  `enum (`IngestionType`)` Optional. Ingestion Type.  
  
### TrellixHxBulkAcqsSettings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication))
      },
      "endpoint": string
    }  
  
Fields  
---  
`authentication` |  `object (`[TrellixStarXAuthentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.TrellixStarXAuthentication)`)` Required. Authentication.  
`endpoint` |  `string` Required. Trellix HX Device URL. This must be a valid URL with an http or https scheme. It has no default. Usually a device URL is in the form of either: <https://xxx.trellix.com/hx/id/>/ - or - <https://htapdeviceproxy.md.mandiant.net/dphb/hx/>/  
  
### MimecastMailV2Settings

JSON representation  
---  
      
    
    {
      "authCredentials": {
        object ([MimecastV2OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastV2OAuthClientCredentials))
      }
    }  
  
Fields  
---  
`authCredentials` |  `object (`[MimecastV2OAuthClientCredentials](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.MimecastV2OAuthClientCredentials)`)` Required. Mimecast OAuthClientCredentials.  
  
### MimecastV2OAuthClientCredentials

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. Client ID.  
`clientSecret` |  `string` Required. Client Secret.  
  
### ThreatConnectIoCV3Settings

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth))
      },
      "hostname": string,
      "owners": [
        string
      ],
      "tqlQuery": string,
      "fields": [
        string
      ],
      "schedule": integer
    }  
  
Fields  
---  
`authentication` |  `object (`[UsernameSecretAuth](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_feeds#Output.Schema.UsernameSecretAuth)`)` Required. Input only. UsernameSecretAuth.  
`hostname` |  `string` Required. hostname.  
`owners[]` |  `string` Required. Owners.  
`tqlQuery` |  `string` Optional. ThreatConnect Query Language filter.  
`fields[]` |  `string` Optional. Fields  
`schedule` |  `integer` Optional. Schedule  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FeedFailureDetails

JSON representation  
---  
      
    
    {
      "errorCode": string,
      "httpErrorCode": integer,
      "errorCause": string,
      "errorAction": string
    }  
  
Fields  
---  
`errorCode` |  `string` Output only. error_code contains the error code for the feed. The field is populated for the feeds with failed status.  
`httpErrorCode` |  `integer` Output only. http_error_code contains the HTTP error code for the feed failure. feed transfer failure may or may not result in http error code.  
`errorCause` |  `string` Output only. error_cause contains the information regarding the failure cause.  
`errorAction` |  `string` Output only. error_action contains the user action prescribed for remediation of feed error.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
