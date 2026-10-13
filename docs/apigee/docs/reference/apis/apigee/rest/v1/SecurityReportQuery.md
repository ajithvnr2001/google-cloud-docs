---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportQuery/
title: SecurityReportQuery \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:47.882355+00:00
---

# SecurityReportQuery  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SecurityReportQuery Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Metric
    * JSON representation



Body structure when user makes a request to create a security report.

JSON representation  
---  
      
    
    {
      "metrics": [
        {
          object ([Metric](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportQuery#Metric))
        }
      ],
      "dimensions": [
        string
      ],
      "timeRange": value,
      "filter": string,
      "groupByTimeUnit": string,
      "limit": integer,
      "mimeType": string,
      "csvDelimiter": string,
      "envgroupHostname": string,
      "reportDefinitionId": string,
      "displayName": string
    }  
  
Fields  
---  
`metrics[]` |  `object (`[Metric](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportQuery#Metric)`)` A list of Metrics.  
`dimensions[]` |  `string` A list of dimensions. <https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions>  
`timeRange` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. Time range for the query. Can use the following predefined strings to specify the time range: `last60minutes` `last24hours` `last7days` Or, specify the timeRange as a structure describing start and end timestamps in the ISO format: yyyy-mm-ddThh:mm:ssZ.Example: "timeRange": { "start": "2018-07-29T00:13:00Z", "end": "2018-08-01T00:18:00Z" }  
`filter` |  `string` Boolean expression that can be used to filter data. Filter expressions can be combined using AND/OR terms and should be fully parenthesized to avoid ambiguity. See Analytics metrics, dimensions, and filters reference <https://docs.apigee.com/api-platform/analytics/analytics-reference> for more information on the fields available to filter on. For more information on the tokens that you use to build filter expressions, see Filter expression syntax. <https://docs.apigee.com/api-platform/analytics/asynch-reports-api#filter-expression-syntax>  
`groupByTimeUnit` |  `string` Time unit used to group the result set. Valid values include: second, minute, hour, day, week, or month. If a query includes groupByTimeUnit, then the result is an aggregation based on the specified time unit and the resultant timestamp does not include milliseconds precision. If a query omits groupByTimeUnit, then the resultant timestamp includes milliseconds precision.  
`limit` |  `integer` Maximum number of rows that can be returned in the result.  
`mimeType` |  `string` Valid values include: `csv` or `json`. Defaults to `json`. Note: Configure the delimiter for CSV output using the csvDelimiter property.  
`csvDelimiter` |  `string` Delimiter used in the CSV file, if `outputFormat` is set to `csv`. Defaults to the `,` (comma) character. Supported delimiter characters include comma (`,`), pipe (`|`), and tab (`\t`).  
`envgroupHostname` |  `string` Hostname needs to be specified if query intends to run at host level. This field is only allowed when query is submitted by `[hostSecurityReports.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/create#google.cloud.apigee.v1.SecurityReportService.CreateHostSecurityReport)` where analytics data will be grouped by organization and hostname.  
`reportDefinitionId` |  `string` Report Definition ID.  
`displayName` |  `string` Security Report display name which users can specify.  
  
## Metric

Metric of the Query

JSON representation  
---  
      
    
    {
      "name": string,
      "aggregationFunction": string,
      "alias": string,
      "operator": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Required. Metric name.  
`aggregationFunction` |  `string` Aggregation function: avg, min, max, or sum.  
`alias` |  `string` Alias for the metric. Alias will be used to replace metric name in query results.  
`operator` |  `string` One of `+`, `-`, `/`, `%`, `*`.  
`value` |  `string` Operand value should be provided when operator is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
