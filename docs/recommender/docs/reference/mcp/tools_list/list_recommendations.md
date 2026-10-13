---
url: https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations/
title: MCP Tools Reference: recommender.googleapis.com \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:23.067578+00:00
---

# MCP Tools Reference: recommender.googleapis.com  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback 

#  MCP Tools Reference: recommender.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_recommendations`

Lists recommendations for a given cloud resource.

The following sample demonstrate how to use `curl` to invoke the `list_recommendations` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://recommender.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_recommendations",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for the `ListRecommendations` method.

### ListRecommendationsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The container resource on which to execute the request. Acceptable formats:

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
  * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> RECOMMENDER_ID refers to supported recommenders: <https://cloud.google.com/recommender/docs/recommenders>.  
`pageSize` |  `integer` Optional. The maximum number of results to return from this request. Non-positive values are ignored. If not specified, the server will determine the number of results to return.  
`pageToken` |  `string` Optional. If present, retrieves the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of other method parameters must be identical to those in the previous call.  
`filter` |  `string` Filter expression to restrict the recommendations returned. Supported filter fields:

  * `state_info.state`
  * `recommenderSubtype`
  * `priority`
  * `targetResources`

Examples:

  * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`
  * `recommenderSubtype = REMOVE_ROLE OR recommenderSubtype = REPLACE_ROLE`
  * `priority = P1 OR priority = P2`
  * `targetResources : //compute.googleapis.com/projects/1234/zones/us-central1-a/instances/instance-1`
  * `stateInfo.state = ACTIVE AND (priority = P1 OR priority = P2)`

The max allowed filter length is 500 characters.(These expressions are based on the filter language described at <https://google.aip.dev/160>)  
  
## Output Schema

Response to the `ListRecommendations` method.

### ListRecommendationsResponse

JSON representation  
---  
      
    
    {
      "recommendations": [
        {
          object ([Recommendation](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Recommendation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`recommendations[]` |  `object (`[Recommendation](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Recommendation)`)` The set of recommendations for the `parent` resource.  
`nextPageToken` |  `string` A token that can be used to request the next page of results. This field is empty if there are no additional results.  
  
### Recommendation

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "recommenderSubtype": string,
      "lastRefreshTime": string,
      "primaryImpact": {
        object ([Impact](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Impact))
      },
      "additionalImpact": [
        {
          object ([Impact](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Impact))
        }
      ],
      "priority": enum ([Priority](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Priority)),
      "content": {
        object ([RecommendationContent](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RecommendationContent))
      },
      "stateInfo": {
        object ([RecommendationStateInfo](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RecommendationStateInfo))
      },
      "etag": string,
      "associatedInsights": [
        {
          object ([InsightReference](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.InsightReference))
        }
      ],
      "xorGroupId": string,
      "targetResources": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of recommendation.  
`description` |  `string` Free-form human readable summary in English. The maximum length is 500 characters.  
`recommenderSubtype` |  `string` Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender.Examples: For recommender = "google.iam.policy.Recommender", recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE"  
`lastRefreshTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time this recommendation was refreshed by the system that created it in the first place.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`primaryImpact` |  `object (`[Impact](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Impact)`)` The primary impact that this recommendation can have while trying to optimize for one category.  
`additionalImpact[]` |  `object (`[Impact](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Impact)`)` Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative.  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Priority)`)` Recommendation's priority.  
`content` |  `object (`[RecommendationContent](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RecommendationContent)`)` Content of the recommendation describing recommended changes to resources.  
`stateInfo` |  `object (`[RecommendationStateInfo](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RecommendationStateInfo)`)` Information for state. Contains state and metadata.  
`etag` |  `string` Fingerprint of the Recommendation. Provides optimistic locking when updating states.  
`associatedInsights[]` |  `object (`[InsightReference](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.InsightReference)`)` Insights that led to this recommendation.  
`xorGroupId` |  `string` Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied.  
`targetResources[]` |  `string` Fully qualified resource names that this recommendation is targeting.  
  
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
  
### Impact

JSON representation  
---  
      
    
    {
      "category": enum ([Category](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Category)),
      "service": string,
    
      // Union field projection can be only one of the following:
      "costProjection": {
        object ([CostProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.CostProjection))
      },
      "securityProjection": {
        object ([SecurityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.SecurityProjection))
      },
      "sustainabilityProjection": {
        object ([SustainabilityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.SustainabilityProjection))
      },
      "reliabilityProjection": {
        object ([ReliabilityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ReliabilityProjection))
      }
      // End of list of possible types for union field projection.
    }  
  
Fields  
---  
`category` |  `enum (`[Category](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Category)`)` Category that is being targeted.  
`service` |  `string` The service that this impact is associated with.  
Union field `projection`. Contains projections (if any) for this category. `projection` can be only one of the following:  
`costProjection` |  `object (`[CostProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.CostProjection)`)` Use with CategoryType.COST  
`securityProjection` |  `object (`[SecurityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.SecurityProjection)`)` Use with CategoryType.SECURITY  
`sustainabilityProjection` |  `object (`[SustainabilityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.SustainabilityProjection)`)` Use with CategoryType.SUSTAINABILITY  
`reliabilityProjection` |  `object (`[ReliabilityProjection](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ReliabilityProjection)`)` Use with CategoryType.RELIABILITY  
  
### CostProjection

JSON representation  
---  
      
    
    {
      "cost": {
        object ([Money](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Money))
      },
      "duration": string,
      "costInLocalCurrency": {
        object ([Money](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Money))
      }
    }  
  
Fields  
---  
`cost` |  `object (`[Money](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Money)`)` An approximate projection on amount saved or amount incurred. Negative cost units indicate cost savings and positive cost units indicate increase. See google.type.Money documentation for positive/negative units.A user's permissions may affect whether the cost is computed using list prices or custom contract prices.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration for which this cost applies.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`costInLocalCurrency` |  `object (`[Money](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Money)`)` The approximate cost savings in the billing account's local currency.  
  
### Money

JSON representation  
---  
      
    
    {
      "currencyCode": string,
      "units": string,
      "nanos": integer
    }  
  
Fields  
---  
`currencyCode` |  `string` The three-letter currency code defined in ISO 4217.  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.  
`nanos` |  `integer` Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### SecurityProjection

JSON representation  
---  
      
    
    {
      "details": {
        object
      }
    }  
  
Fields  
---  
`details` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Additional security impact details that is provided by the recommender.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### SustainabilityProjection

JSON representation  
---  
      
    
    {
      "kgCO2e": number,
      "duration": string
    }  
  
Fields  
---  
`kgCO2e` |  `number` Carbon Footprint generated in kg of CO2 equivalent. Chose kg_c_o2e so that the name renders correctly in camelCase (kgCO2e).  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration for which this sustainability applies.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### ReliabilityProjection

JSON representation  
---  
      
    
    {
      "risks": [
        enum ([RiskType](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RiskType))
      ],
      "details": {
        object
      }
    }  
  
Fields  
---  
`risks[]` |  `enum (`[RiskType](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.RiskType)`)` Reliability risks mitigated by this recommendation.  
`details` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Per-recommender projection.  
  
### RecommendationContent

JSON representation  
---  
      
    
    {
      "operationGroups": [
        {
          object ([OperationGroup](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.OperationGroup))
        }
      ],
      "overview": {
        object
      }
    }  
  
Fields  
---  
`operationGroups[]` |  `object (`[OperationGroup](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.OperationGroup)`)` Operations to one or more Google Cloud resources grouped in such a way that, all operations within one group are expected to be performed atomically and in an order.  
`overview` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Condensed overview information about the recommendation.  
  
### OperationGroup

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Operation))
        }
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.Operation)`)` List of operations across one or more resources that belong to this group. Loosely based on RFC6902 and should be performed in the order they appear.  
  
### Operation

JSON representation  
---  
      
    
    {
      "action": string,
      "resourceType": string,
      "resource": string,
      "path": string,
      "sourceResource": string,
      "sourcePath": string,
      "pathFilters": {
        string: value,
        ...
      },
      "pathValueMatchers": {
        string: {
          object ([ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher))
        },
        ...
      },
    
      // Union field path_value can be only one of the following:
      "value": value,
      "valueMatcher": {
        object ([ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher))
      }
      // End of list of possible types for union field path_value.
    }  
  
Fields  
---  
`action` |  `string` Type of this operation. Contains one of 'add', 'remove', 'replace', 'move', 'copy', 'test' and custom operations. This field is case-insensitive and always populated.  
`resourceType` |  `string` Type of GCP resource being modified/tested. This field is always populated. Example: cloudresourcemanager.googleapis.com/Project, compute.googleapis.com/Instance  
`resource` |  `string` Contains the fully qualified resource name. This field is always populated. ex: //cloudresourcemanager.googleapis.com/projects/foo.  
`path` |  `string` Path to the target field being operated on. If the operation is at the resource level, then path should be "/". This field is always populated.  
`sourceResource` |  `string` Can be set with action 'copy' to copy resource configuration across different resources of the same type. Example: A resource clone can be done via action = 'copy', path = "/", from = "/", source_resource =  and resource_name = . This field is empty for all other values of `action`.  
`sourcePath` |  `string` Can be set with action 'copy' or 'move' to indicate the source field within resource or source_resource, ignored if provided for other operation types.  
`pathFilters` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Set of filters to apply if `path` refers to array elements or nested array elements in order to narrow down to a single unique element that is being tested/modified. This is intended to be an exact match per filter. To perform advanced matching, use path_value_matchers.

  * Example:


    
    
    {
      "/versions/*/name" : "it-123"
      "/versions/*/targetSize/percent": 20
    }
    

  * Example:


    
    
    {
      "/bindings/*/role": "roles/owner"
      "/bindings/*/condition" : null
    }
    

  * Example:


    
    
    {
      "/bindings/*/role": "roles/owner"
      "/bindings/*/members/*" : ["x@example.com", "y@example.com"]
    }
    

When both path_filters and path_value_matchers are set, an implicit AND must be performed.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pathValueMatchers` |  `map (key: string, value: object (`[ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher)`))` Similar to path_filters, this contains set of filters to apply if `path` field refers to array elements. This is meant to support value matching beyond exact match. To perform exact match, use path_filters. When both path_filters and path_value_matchers are set, an implicit AND must be performed.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `path_value`. One of the fields in the following block will be set and intend to describe a value for 'path' field. `path_value` can be only one of the following:  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Value for the `path` field. Will be set for actions:'add'/'replace'. Maybe set for action: 'test'. Either this or `value_matcher` will be set for 'test' operation. An exact match must be performed.  
`valueMatcher` |  `object (`[ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher)`)` Can be set for action 'test' for advanced matching for the value of 'path' field. Either this or `value` will be set for 'test' operation.  
  
### ValueMatcher

JSON representation  
---  
      
    
    {
    
      // Union field match_variant can be only one of the following:
      "matchesPattern": string
      // End of list of possible types for union field match_variant.
    }  
  
Fields  
---  
Union field `match_variant`. To be used for full regex matching. `match_variant` can be only one of the following:  
`matchesPattern` |  `string` To be used for full regex matching. The regular expression is using the Google RE2 syntax (<https://github.com/google/re2/wiki/Syntax)>, so to be used with RE2::FullMatch  
  
### PathFiltersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### PathValueMatchersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[ValueMatcher](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.ValueMatcher)`)`  
  
### RecommendationStateInfo

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.State)),
      "stateMetadata": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/recommender/docs/reference/mcp/tools_list/list_recommendations#Output.Schema.State)`)` The state of the recommendation, Eg ACTIVE, SUCCEEDED, FAILED.  
`stateMetadata` |  `map (key: string, value: string)` A map of metadata for the state, provided by user or automations systems.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### StateMetadataEntry

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
  
### InsightReference

JSON representation  
---  
      
    
    {
      "insight": string
    }  
  
Fields  
---  
`insight` |  `string` Insight resource name, e.g. projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/insights/[INSIGHT_ID]  
  
### Category

The category of the impact.

Enums  
---  
`CATEGORY_UNSPECIFIED` | Default unspecified category. Don't use directly.  
`COST` | Indicates a potential increase or decrease in cost.  
`SECURITY` | Indicates a potential increase or decrease in security.  
`PERFORMANCE` | Indicates a potential increase or decrease in performance.  
`MANAGEABILITY` | Indicates a potential increase or decrease in manageability.  
`SUSTAINABILITY` | Indicates a potential increase or decrease in sustainability.  
`RELIABILITY` | Indicates a potential increase or decrease in reliability.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### RiskType

The risk associated with the reliability issue.

Enums  
---  
`RISK_TYPE_UNSPECIFIED` | Default unspecified risk. Don't use directly.  
`SERVICE_DISRUPTION` | Potential service downtime.  
`DATA_LOSS` | Potential data loss.  
`ACCESS_DENY` | Potential access denial. The service is still up but some or all clients can't access it.  
  
### Priority

Recommendation priority levels.

Enums  
---  
`PRIORITY_UNSPECIFIED` | Recommendation has unspecified priority.  
`P4` | Recommendation has P4 priority (lowest priority).  
`P3` | Recommendation has P3 priority (second lowest priority).  
`P2` | Recommendation has P2 priority (second highest priority).  
`P1` | Recommendation has P1 priority (highest priority).  
  
### State

Represents Recommendation State.

Enums  
---  
`STATE_UNSPECIFIED` | Default state. Don't use directly.  
`ACTIVE` | Recommendation is active and can be applied. Recommendations content can be updated by Google.ACTIVE recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.  
`CLAIMED` | Recommendation is in claimed state. Recommendations content is immutable and cannot be updated by Google.CLAIMED recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.  
`SUCCEEDED` | Recommendation is in succeeded state. Recommendations content is immutable and cannot be updated by Google.SUCCEEDED recommendations can be marked as SUCCEEDED, or FAILED.  
`FAILED` | Recommendation is in failed state. Recommendations content is immutable and cannot be updated by Google.FAILED recommendations can be marked as SUCCEEDED, or FAILED.  
`DISMISSED` | Recommendation is in dismissed state. Recommendation content can be updated by Google.DISMISSED recommendations can be marked as ACTIVE.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
