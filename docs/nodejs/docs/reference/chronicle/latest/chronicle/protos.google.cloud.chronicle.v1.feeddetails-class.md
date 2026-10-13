---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class
title: Class protos.google.cloud.chronicle.v1.FeedDetails (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:35.556750+00:00
---

# Class protos.google.cloud.chronicle.v1.FeedDetails (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.FeedDetails (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a FeedDetails.

## Implements

[protos.google.cloud.chronicle.v1.IFeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifeeddetails)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IFeedDetails);

Constructs a new FeedDetails.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifeeddetails)`   
Properties to set  
  
## Properties 

### amazonKinesisFirehoseSettings
    
    
    public amazonKinesisFirehoseSettings?: (google.cloud.chronicle.v1.IAmazonKinesisFirehoseSettings|null);

FeedDetails amazonKinesisFirehoseSettings.

### amazonS3Settings
    
    
    public amazonS3Settings?: (google.cloud.chronicle.v1.IAmazonS3Settings|null);

FeedDetails amazonS3Settings.

### amazonS3V2Settings
    
    
    public amazonS3V2Settings?: (google.cloud.chronicle.v1.IAmazonS3V2Settings|null);

FeedDetails amazonS3V2Settings.

### amazonSqsSettings
    
    
    public amazonSqsSettings?: (google.cloud.chronicle.v1.IAmazonSQSSettings|null);

FeedDetails amazonSqsSettings.

### amazonSqsV2Settings
    
    
    public amazonSqsV2Settings?: (google.cloud.chronicle.v1.IAmazonSQSV2Settings|null);

FeedDetails amazonSqsV2Settings.

### anomaliSettings
    
    
    public anomaliSettings?: (google.cloud.chronicle.v1.IAnomaliIocSettings|null);

FeedDetails anomaliSettings.

### assetNamespace
    
    
    public assetNamespace: string;

FeedDetails assetNamespace.

### awsEc2HostsSettings
    
    
    public awsEc2HostsSettings?: (google.cloud.chronicle.v1.IAWSEC2HostsSettings|null);

FeedDetails awsEc2HostsSettings.

### awsEc2InstancesSettings
    
    
    public awsEc2InstancesSettings?: (google.cloud.chronicle.v1.IAWSEC2InstancesSettings|null);

FeedDetails awsEc2InstancesSettings.

### awsEc2VpcsSettings
    
    
    public awsEc2VpcsSettings?: (google.cloud.chronicle.v1.IAWSEC2VpcsSettings|null);

FeedDetails awsEc2VpcsSettings.

### awsIamSettings
    
    
    public awsIamSettings?: (google.cloud.chronicle.v1.IAWSIAMSettings|null);

FeedDetails awsIamSettings.

### azureAdAuditSettings
    
    
    public azureAdAuditSettings?: (google.cloud.chronicle.v1.IAzureADAuditSettings|null);

FeedDetails azureAdAuditSettings.

### azureAdContextSettings
    
    
    public azureAdContextSettings?: (google.cloud.chronicle.v1.IAzureADContextSettings|null);

FeedDetails azureAdContextSettings.

### azureAdSettings
    
    
    public azureAdSettings?: (google.cloud.chronicle.v1.IAzureADSettings|null);

FeedDetails azureAdSettings.

### azureBlobStoreSettings
    
    
    public azureBlobStoreSettings?: (google.cloud.chronicle.v1.IAzureBlobStoreSettings|null);

FeedDetails azureBlobStoreSettings.

### azureBlobStoreV2Settings
    
    
    public azureBlobStoreV2Settings?: (google.cloud.chronicle.v1.IAzureBlobStoreV2Settings|null);

FeedDetails azureBlobStoreV2Settings.

### azureEventHubSettings
    
    
    public azureEventHubSettings?: (google.cloud.chronicle.v1.IAzureEventHubSettings|null);

FeedDetails azureEventHubSettings.

### azureMdmIntuneSettings
    
    
    public azureMdmIntuneSettings?: (google.cloud.chronicle.v1.IAzureMDMIntuneSettings|null);

FeedDetails azureMdmIntuneSettings.

### cloudPassageSettings
    
    
    public cloudPassageSettings?: (google.cloud.chronicle.v1.ICloudPassageSettings|null);

FeedDetails cloudPassageSettings.

### cortexXdrSettings
    
    
    public cortexXdrSettings?: (google.cloud.chronicle.v1.ICortexXDRSettings|null);

FeedDetails cortexXdrSettings.

### crowdstrikeAlertsSettings
    
    
    public crowdstrikeAlertsSettings?: (google.cloud.chronicle.v1.ICrowdStrikeAlertsSettings|null);

FeedDetails crowdstrikeAlertsSettings.

### crowdstrikeDetectsSettings
    
    
    public crowdstrikeDetectsSettings?: (google.cloud.chronicle.v1.ICrowdStrikeDetectsSettings|null);

FeedDetails crowdstrikeDetectsSettings.

### customApiSettings
    
    
    public customApiSettings?: (google.cloud.chronicle.v1.ICustomAPISettings|null);

FeedDetails customApiSettings.

### details
    
    
    public details?: ("anomaliSettings"|"azureAdContextSettings"|"cloudPassageSettings"|"cortexXdrSettings"|"duoAuthSettings"|"duoUserContextSettings"|"microsoftGraphAlertSettings"|"microsoftSecurityCenterAlertSettings"|"mimecastMailSettings"|"office365Settings"|"proofpointMailSettings"|"recordedFutureIocSettings"|"workdaySettings"|"panIocSettings"|"oktaSettings"|"oktaUserContextSettings"|"foxItStixSettings"|"threatConnectIocSettings"|"serviceNowCmdbSettings"|"impervaWafSettings"|"thinkstCanarySettings"|"rhIsacIocSettings"|"rapid7InsightSettings"|"salesforceSettings"|"netskopeAlertSettings"|"azureMdmIntuneSettings"|"azureAdSettings"|"proofpointOnDemandSettings"|"workspaceUsersSettings"|"workspaceActivitySettings"|"workspaceAlertsSettings"|"workspacePrivilegesSettings"|"workspaceMobileSettings"|"workspaceChromeOsSettings"|"workspaceGroupsSettings"|"azureAdAuditSettings"|"symantecEventExportSettings"|"qualysVmSettings"|"panPrismaCloudSettings"|"gcsSettings"|"httpSettings"|"sftpSettings"|"amazonS3Settings"|"azureBlobStoreSettings"|"amazonSqsSettings"|"googleCloudIdentityDevicesSettings"|"googleCloudIdentityDeviceUsersSettings"|"crowdstrikeDetectsSettings"|"mandiantIocSettings"|"sentineloneAlertSettings"|"qualysScanSettings"|"pubsubSettings"|"amazonKinesisFirehoseSettings"|"webhookSettings"|"dummyLogTypeSettings"|"httpsPushGoogleCloudPubsubSettings"|"httpsPushAmazonKinesisFirehoseSettings"|"httpsPushWebhookSettings"|"awsEc2HostsSettings"|"awsEc2InstancesSettings"|"awsEc2VpcsSettings"|"awsIamSettings"|"netskopeAlertV2Settings"|"gcsV2Settings"|"amazonS3V2Settings"|"amazonSqsV2Settings"|"azureEventHubSettings"|"trellixHxHostsSettings"|"azureBlobStoreV2Settings"|"trellixHxAlertsSettings"|"googleCloudStorageEventDrivenSettings"|"crowdstrikeAlertsSettings"|"trellixHxBulkAcqsSettings"|"mimecastMailV2Settings"|"threatConnectIocV3Settings"|"customApiSettings");

FeedDetails details.

### dummyLogTypeSettings
    
    
    public dummyLogTypeSettings?: (google.cloud.chronicle.v1.IDummyLogTypeSettings|null);

FeedDetails dummyLogTypeSettings.

### duoAuthSettings
    
    
    public duoAuthSettings?: (google.cloud.chronicle.v1.IDuoAuthSettings|null);

FeedDetails duoAuthSettings.

### duoUserContextSettings
    
    
    public duoUserContextSettings?: (google.cloud.chronicle.v1.IDuoUserContextSettings|null);

FeedDetails duoUserContextSettings.

### feedSourceType
    
    
    public feedSourceType: (google.cloud.chronicle.v1.FeedDetails.FeedSourceType|keyof typeof google.cloud.chronicle.v1.FeedDetails.FeedSourceType);

FeedDetails feedSourceType.

### foxItStixSettings
    
    
    public foxItStixSettings?: (google.cloud.chronicle.v1.IFoxITStixSettings|null);

FeedDetails foxItStixSettings.

### gcsSettings
    
    
    public gcsSettings?: (google.cloud.chronicle.v1.IGoogleCloudStorageSettings|null);

FeedDetails gcsSettings.

### gcsV2Settings
    
    
    public gcsV2Settings?: (google.cloud.chronicle.v1.IGoogleCloudStorageV2Settings|null);

FeedDetails gcsV2Settings.

### googleCloudIdentityDevicesSettings
    
    
    public googleCloudIdentityDevicesSettings?: (google.cloud.chronicle.v1.IGoogleCloudIdentityDevicesSettings|null);

FeedDetails googleCloudIdentityDevicesSettings.

### googleCloudIdentityDeviceUsersSettings
    
    
    public googleCloudIdentityDeviceUsersSettings?: (google.cloud.chronicle.v1.IGoogleCloudIdentityDeviceUsersSettings|null);

FeedDetails googleCloudIdentityDeviceUsersSettings.

### googleCloudStorageEventDrivenSettings
    
    
    public googleCloudStorageEventDrivenSettings?: (google.cloud.chronicle.v1.IGoogleCloudStorageEventDrivenSettings|null);

FeedDetails googleCloudStorageEventDrivenSettings.

### httpSettings
    
    
    public httpSettings?: (google.cloud.chronicle.v1.IHttpSettings|null);

FeedDetails httpSettings.

### httpsPushAmazonKinesisFirehoseSettings
    
    
    public httpsPushAmazonKinesisFirehoseSettings?: (google.cloud.chronicle.v1.IHttpsPushAmazonKinesisFirehoseSettings|null);

FeedDetails httpsPushAmazonKinesisFirehoseSettings.

### httpsPushGoogleCloudPubsubSettings
    
    
    public httpsPushGoogleCloudPubsubSettings?: (google.cloud.chronicle.v1.IHttpsPushGoogleCloudPubSubSettings|null);

FeedDetails httpsPushGoogleCloudPubsubSettings.

### httpsPushWebhookSettings
    
    
    public httpsPushWebhookSettings?: (google.cloud.chronicle.v1.IHttpsPushWebhookSettings|null);

FeedDetails httpsPushWebhookSettings.

### impervaWafSettings
    
    
    public impervaWafSettings?: (google.cloud.chronicle.v1.IImpervaWAFSettings|null);

FeedDetails impervaWafSettings.

### labels
    
    
    public labels: { [k: string]: string };

FeedDetails labels.

### lastV2MigrationAttemptTime
    
    
    public lastV2MigrationAttemptTime?: (google.protobuf.ITimestamp|null);

FeedDetails lastV2MigrationAttemptTime.

### logType
    
    
    public logType: string;

FeedDetails logType.

### mandiantIocSettings
    
    
    public mandiantIocSettings?: (google.cloud.chronicle.v1.IMandiantIoCSettings|null);

FeedDetails mandiantIocSettings.

### microsoftGraphAlertSettings
    
    
    public microsoftGraphAlertSettings?: (google.cloud.chronicle.v1.IMicrosoftGraphAlertSettings|null);

FeedDetails microsoftGraphAlertSettings.

### microsoftSecurityCenterAlertSettings
    
    
    public microsoftSecurityCenterAlertSettings?: (google.cloud.chronicle.v1.IMicrosoftSecurityCenterAlertSettings|null);

FeedDetails microsoftSecurityCenterAlertSettings.

### mimecastMailSettings
    
    
    public mimecastMailSettings?: (google.cloud.chronicle.v1.IMimecastMailSettings|null);

FeedDetails mimecastMailSettings.

### mimecastMailV2Settings
    
    
    public mimecastMailV2Settings?: (google.cloud.chronicle.v1.IMimecastMailV2Settings|null);

FeedDetails mimecastMailV2Settings.

### netskopeAlertSettings
    
    
    public netskopeAlertSettings?: (google.cloud.chronicle.v1.INetskopeAlertSettings|null);

FeedDetails netskopeAlertSettings.

### netskopeAlertV2Settings
    
    
    public netskopeAlertV2Settings?: (google.cloud.chronicle.v1.INetskopeAlertV2Settings|null);

FeedDetails netskopeAlertV2Settings.

### office365Settings
    
    
    public office365Settings?: (google.cloud.chronicle.v1.IOffice365Settings|null);

FeedDetails office365Settings.

### oktaSettings
    
    
    public oktaSettings?: (google.cloud.chronicle.v1.IOktaSettings|null);

FeedDetails oktaSettings.

### oktaUserContextSettings
    
    
    public oktaUserContextSettings?: (google.cloud.chronicle.v1.IOktaUserContextSettings|null);

FeedDetails oktaUserContextSettings.

### panIocSettings
    
    
    public panIocSettings?: (google.cloud.chronicle.v1.IPanIocSettings|null);

FeedDetails panIocSettings.

### panPrismaCloudSettings
    
    
    public panPrismaCloudSettings?: (google.cloud.chronicle.v1.IPanPrismaCloudSettings|null);

FeedDetails panPrismaCloudSettings.

### proofpointMailSettings
    
    
    public proofpointMailSettings?: (google.cloud.chronicle.v1.IProofpointMailSettings|null);

FeedDetails proofpointMailSettings.

### proofpointOnDemandSettings
    
    
    public proofpointOnDemandSettings?: (google.cloud.chronicle.v1.IProofpointOnDemandSettings|null);

FeedDetails proofpointOnDemandSettings.

### pubsubSettings
    
    
    public pubsubSettings?: (google.cloud.chronicle.v1.IPubsubSettings|null);

FeedDetails pubsubSettings.

### qualysScanSettings
    
    
    public qualysScanSettings?: (google.cloud.chronicle.v1.IQualysScanSettings|null);

FeedDetails qualysScanSettings.

### qualysVmSettings
    
    
    public qualysVmSettings?: (google.cloud.chronicle.v1.IQualysVMSettings|null);

FeedDetails qualysVmSettings.

### rapid7InsightSettings
    
    
    public rapid7InsightSettings?: (google.cloud.chronicle.v1.IRapid7InsightSettings|null);

FeedDetails rapid7InsightSettings.

### recordedFutureIocSettings
    
    
    public recordedFutureIocSettings?: (google.cloud.chronicle.v1.IRecordedFutureIocSettings|null);

FeedDetails recordedFutureIocSettings.

### rhIsacIocSettings
    
    
    public rhIsacIocSettings?: (google.cloud.chronicle.v1.IRHIsacIocSettings|null);

FeedDetails rhIsacIocSettings.

### salesforceSettings
    
    
    public salesforceSettings?: (google.cloud.chronicle.v1.ISalesforceSettings|null);

FeedDetails salesforceSettings.

### sentineloneAlertSettings
    
    
    public sentineloneAlertSettings?: (google.cloud.chronicle.v1.ISentineloneAlertSettings|null);

FeedDetails sentineloneAlertSettings.

### serviceNowCmdbSettings
    
    
    public serviceNowCmdbSettings?: (google.cloud.chronicle.v1.IServiceNowCMDBSettings|null);

FeedDetails serviceNowCmdbSettings.

### sftpSettings
    
    
    public sftpSettings?: (google.cloud.chronicle.v1.ISftpSettings|null);

FeedDetails sftpSettings.

### stsMigrationReadiness
    
    
    public stsMigrationReadiness: (google.cloud.chronicle.v1.FeedDetails.STSMigrationReadiness|keyof typeof google.cloud.chronicle.v1.FeedDetails.STSMigrationReadiness);

FeedDetails stsMigrationReadiness.

### symantecEventExportSettings
    
    
    public symantecEventExportSettings?: (google.cloud.chronicle.v1.ISymantecEventExportSettings|null);

FeedDetails symantecEventExportSettings.

### thinkstCanarySettings
    
    
    public thinkstCanarySettings?: (google.cloud.chronicle.v1.IThinkstCanarySettings|null);

FeedDetails thinkstCanarySettings.

### threatConnectIocSettings
    
    
    public threatConnectIocSettings?: (google.cloud.chronicle.v1.IThreatConnectIoCSettings|null);

FeedDetails threatConnectIocSettings.

### threatConnectIocV3Settings
    
    
    public threatConnectIocV3Settings?: (google.cloud.chronicle.v1.IThreatConnectIoCV3Settings|null);

FeedDetails threatConnectIocV3Settings.

### trellixHxAlertsSettings
    
    
    public trellixHxAlertsSettings?: (google.cloud.chronicle.v1.ITrellixHxAlertsSettings|null);

FeedDetails trellixHxAlertsSettings.

### trellixHxBulkAcqsSettings
    
    
    public trellixHxBulkAcqsSettings?: (google.cloud.chronicle.v1.ITrellixHxBulkAcqsSettings|null);

FeedDetails trellixHxBulkAcqsSettings.

### trellixHxHostsSettings
    
    
    public trellixHxHostsSettings?: (google.cloud.chronicle.v1.ITrellixHxHostsSettings|null);

FeedDetails trellixHxHostsSettings.

### webhookSettings
    
    
    public webhookSettings?: (google.cloud.chronicle.v1.IWebhookSettings|null);

FeedDetails webhookSettings.

### workdaySettings
    
    
    public workdaySettings?: (google.cloud.chronicle.v1.IWorkdaySettings|null);

FeedDetails workdaySettings.

### workspaceActivitySettings
    
    
    public workspaceActivitySettings?: (google.cloud.chronicle.v1.IWorkspaceActivitySettings|null);

FeedDetails workspaceActivitySettings.

### workspaceAlertsSettings
    
    
    public workspaceAlertsSettings?: (google.cloud.chronicle.v1.IWorkspaceAlertsSettings|null);

FeedDetails workspaceAlertsSettings.

### workspaceChromeOsSettings
    
    
    public workspaceChromeOsSettings?: (google.cloud.chronicle.v1.IWorkspaceChromeOSSettings|null);

FeedDetails workspaceChromeOsSettings.

### workspaceGroupsSettings
    
    
    public workspaceGroupsSettings?: (google.cloud.chronicle.v1.IWorkspaceGroupsSettings|null);

FeedDetails workspaceGroupsSettings.

### workspaceMobileSettings
    
    
    public workspaceMobileSettings?: (google.cloud.chronicle.v1.IWorkspaceMobileSettings|null);

FeedDetails workspaceMobileSettings.

### workspacePrivilegesSettings
    
    
    public workspacePrivilegesSettings?: (google.cloud.chronicle.v1.IWorkspacePrivilegesSettings|null);

FeedDetails workspacePrivilegesSettings.

### workspaceUsersSettings
    
    
    public workspaceUsersSettings?: (google.cloud.chronicle.v1.IWorkspaceUsersSettings|null);

FeedDetails workspaceUsersSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IFeedDetails): google.cloud.chronicle.v1.FeedDetails;

Creates a new FeedDetails instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifeeddetails)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class)` | FeedDetails instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.FeedDetails;

Decodes a FeedDetails message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[FeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class)` | FeedDetails  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.FeedDetails;

Decodes a FeedDetails message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class)` | FeedDetails  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IFeedDetails, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeedDetails message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifeeddetails)`   
FeedDetails message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IFeedDetails, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeedDetails message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifeeddetails)`   
FeedDetails message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.FeedDetails;

Creates a FeedDetails message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class)` | FeedDetails  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeedDetails

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this FeedDetails to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.FeedDetails, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeedDetails message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeedDetails](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feeddetails-class)`   
FeedDetails  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeedDetails message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
