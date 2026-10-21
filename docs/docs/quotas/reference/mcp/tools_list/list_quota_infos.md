---
url: https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos/
title: MCP Tools Reference: cloudquotas.googleapis.com \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:16.754174+00:00
---

# MCP Tools Reference: cloudquotas.googleapis.com  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  MCP Tools Reference: cloudquotas.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_quota_infos`

Lists QuotaInfos of all quotas for a given project, folder, or organization. Expected request structure: 'parent' (string, format: projects/{project}/locations/global/services/{service}, folders/{folder}/locations/global/services/{service}, or organizations/{organization}/locations/global/services/{service}), 'page_size' is automatically fixed to 100.

The following sample demonstrate how to use `curl` to invoke the `list_quota_infos` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://cloudquotas.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_quota_infos",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Message for requesting list of QuotaInfos

### ListQuotaInfosRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed.Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
  
## Output Schema

Message for response to listing QuotaInfos

### ListQuotaInfosResponse

JSON representation  
---  
      
    
    {
      "quotaInfos": [
        {
          object ([QuotaInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaInfo))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`quotaInfos[]` |  `object (`[QuotaInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaInfo)`)` The list of QuotaInfo  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### QuotaInfo

JSON representation  
---  
      
    
    {
      "name": string,
      "quotaId": string,
      "metric": string,
      "service": string,
      "isPrecise": boolean,
      "refreshInterval": string,
      "containerType": enum ([ContainerType](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.ContainerType)),
      "dimensions": [
        string
      ],
      "metricDisplayName": string,
      "quotaDisplayName": string,
      "metricUnit": string,
      "quotaIncreaseEligibility": {
        object ([QuotaIncreaseEligibility](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaIncreaseEligibility))
      },
      "isFixed": boolean,
      "dimensionsInfos": [
        {
          object ([DimensionsInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.DimensionsInfo))
        }
      ],
      "isConcurrent": boolean,
      "serviceRequestQuotaUri": string
    }  
  
Fields  
---  
`name` |  `string` Resource name of this QuotaInfo. The ID component following "locations/" must be "global". For example, `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`quotaId` |  `string` The id of the quota, which is unique within the service. For example, `CpusPerProjectPerRegion`  
`metric` |  `string` The metric of the quota. It specifies the resources consumption the quota is defined for. For example, `compute.googleapis.com/cpus`  
`service` |  `string` The name of the service in which the quota is defined. For example, `compute.googleapis.com`  
`isPrecise` |  `boolean` Whether this is a precise quota. A precise quota is tracked with absolute precision. In contrast, an imprecise quota is not tracked with precision.  
`refreshInterval` |  `string` The reset time interval for the quota. Refresh interval applies to rate quota only. For example, "minute" for per minute, "day" for per day, or "10 seconds" for every 10 seconds.  
`containerType` |  `enum (`[ContainerType](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.ContainerType)`)` The container type of the QuotaInfo.  
`dimensions[]` |  `string` The dimensions the quota is defined on.  
`metricDisplayName` |  `string` The display name of the quota metric  
`quotaDisplayName` |  `string` The display name of the quota.  
`metricUnit` |  `string` The unit in which the metric value is reported, e.g., "MByte".  
`quotaIncreaseEligibility` |  `object (`[QuotaIncreaseEligibility](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaIncreaseEligibility)`)` Whether it is eligible to request a higher quota value for this quota.  
`isFixed` |  `boolean` Whether the quota value is fixed or adjustable  
`dimensionsInfos[]` |  `object (`[DimensionsInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.DimensionsInfo)`)` The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.  
`isConcurrent` |  `boolean` Whether the quota is a concurrent quota. Concurrent quotas are enforced on the total number of concurrent operations in flight at any given time.  
`serviceRequestQuotaUri` |  `string` URI to the page where users can request more quota for the cloud service—for example, <https://console.cloud.google.com/iam-admin/quotas>.  
  
### QuotaIncreaseEligibility

JSON representation  
---  
      
    
    {
      "isEligible": boolean,
      "ineligibilityReason": enum ([IneligibilityReason](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.IneligibilityReason))
    }  
  
Fields  
---  
`isEligible` |  `boolean` Whether a higher quota value can be requested for the quota.  
`ineligibilityReason` |  `enum (`[IneligibilityReason](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.IneligibilityReason)`)` The reason of why it is ineligible to request increased value of the quota. If the is_eligible field is true, it defaults to INELIGIBILITY_REASON_UNSPECIFIED.  
  
### DimensionsInfo

JSON representation  
---  
      
    
    {
      "dimensions": {
        string: string,
        ...
      },
      "details": {
        object ([QuotaDetails](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaDetails))
      },
      "applicableLocations": [
        string
      ]
    }  
  
Fields  
---  
`dimensions` |  `map (key: string, value: string)` The map of dimensions in key-value pairs. The key of a map entry is "region", "zone", or the name of a service-specific dimension, and the value of a map entry is the value of the dimension. If a dimension does not appear in the map of dimensions, the dimensions info applies to all the dimension values except for those that have another DimensionInfo instance configured for the specific value. For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`details` |  `object (`[QuotaDetails](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.QuotaDetails)`)` Quota details for the specified dimensions.  
`applicableLocations[]` |  `string` The applicable regions or zones of this dimension. The field is set to ['global'] for quotas that are not per region or per zone. Otherwise, it will be set to the list of locations this dimension info is applicable to.  
  
### DimensionsEntry

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
  
### QuotaDetails

JSON representation  
---  
      
    
    {
      "value": string,
      "rolloutInfo": {
        object ([RolloutInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.RolloutInfo))
      }
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The value currently in effect and being enforced.  
`rolloutInfo` |  `object (`[RolloutInfo](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos#Output.Schema.RolloutInfo)`)` Rollout information of this quota. This field is present only if the effective limit will change due to the ongoing rollout of the service config.  
  
### RolloutInfo

JSON representation  
---  
      
    
    {
      "ongoingRollout": boolean
    }  
  
Fields  
---  
`ongoingRollout` |  `boolean` Whether there is an ongoing rollout for a quota or not.  
  
### ContainerType

The enumeration of the types of a cloud resource container.

Enums  
---  
`CONTAINER_TYPE_UNSPECIFIED` | Unspecified container type.  
`PROJECT` | consumer project  
`FOLDER` | folder  
`ORGANIZATION` | organization  
  
### IneligibilityReason

The enumeration of reasons when it is ineligible to request increase adjustment.

Enums  
---  
`INELIGIBILITY_REASON_UNSPECIFIED` | Default value when is_eligible is true.  
`NO_VALID_BILLING_ACCOUNT` | The container is not linked with a valid billing account.  
`NOT_SUPPORTED` | Quota increase is not supported for the quota.  
`NOT_ENOUGH_USAGE_HISTORY` | There is not enough usage history to determine the eligibility.  
`OTHER` | Other reasons.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
