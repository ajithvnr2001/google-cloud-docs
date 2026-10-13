---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec/
title: DataQualitySpec \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:45.532138+00:00
---

# DataQualitySpec  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  DataQualitySpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PostScanActions
    * JSON representation
  * BigQueryExport
    * JSON representation
  * NotificationReport
    * JSON representation
  * Recipients
    * JSON representation
  * ScoreThresholdTrigger
    * JSON representation
  * JobFailureTrigger
  * JobEndTrigger



DataQualityScan related setting.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([DataQualityRule](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityRule))
        }
      ],
      "samplingPercent": number,
      "rowFilter": string,
      "postScanActions": {
        object ([PostScanActions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#PostScanActions))
      },
      "catalogPublishingEnabled": boolean,
      "enableCatalogBasedRules": boolean,
      "filter": string
    }  
  
Fields  
---  
`rules[]` |  `object (`[DataQualityRule](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityRule)`)` Required. The list of rules to evaluate against a data source. At least one rule is required.  
`samplingPercent` |  `number` Optional. The percentage of the records to be selected from the dataset for DataScan.

  * Value can range between 0.0 and 100.0 with up to 3 significant decimal digits.
  * Sampling is not applied if `samplingPercent` is not specified, 0 or 100.

  
`rowFilter` |  `string` Optional. A filter applied to all rows in a single DataScan job. The filter needs to be a valid SQL expression for a [WHERE clause in GoogleSQL syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause).Example: col1 >= 0 AND col2 < 10  
`postScanActions` |  `object (`[PostScanActions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#PostScanActions)`)` Optional. Actions to take upon job completion.  
`catalogPublishingEnabled` |  `boolean` Optional. If set, the latest DataScan job result will be published as Dataplex Universal Catalog metadata.  
`enableCatalogBasedRules` |  `boolean` Optional. If enabled, the data scan will retrieve rules defined in the dataplex-types.global.data-rules aspect on all paths of the catalog entry corresponding to the BigQuery table resource and all attached glossary terms. The path that data-rules aspect is attached on the table entry defines the column that the rule will be evaluated against. For glossary terms, the path that the terms are attached on the table entry defines the column that the rule will be evaluated against. At the start of scan execution, the rules reflect the latest state retrieved from the catalog entry and any updates on the rules thereafter are ignored for that execution. The updates will be reflected from the next execution. Rules defined in the datascan must be empty if this field is enabled.  
`filter` |  `string` Optional. Filter for selectively running a subset of rules. You can filter the request by the name or attribute key-value pairs defined on the rule. If not specified, all rules are run. The filter is applicable to both, the rules retrieved from catalog and explicitly defined rules in the scan. Please see [filter syntax](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) for more details.  
  
## PostScanActions

The configuration of post scan actions of DataQualityScan.

JSON representation  
---  
      
    
    {
      "bigqueryExport": {
        object ([BigQueryExport](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#BigQueryExport))
      },
      "notificationReport": {
        object ([NotificationReport](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#NotificationReport))
      }
    }  
  
Fields  
---  
`bigqueryExport` |  `object (`[BigQueryExport](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#BigQueryExport)`)` Optional. If set, results will be exported to the provided BigQuery table.  
`notificationReport` |  `object (`[NotificationReport](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#NotificationReport)`)` Optional. If set, results will be sent to the provided notification receipts upon triggers.  
  
## BigQueryExport

The configuration of BigQuery export post scan action.

JSON representation  
---  
      
    
    {
      "resultsTable": string
    }  
  
Fields  
---  
`resultsTable` |  `string` Optional. The BigQuery table to export DataQualityScan results to. Format: //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID or projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID  
  
## NotificationReport

The configuration of notification report post scan action.

JSON representation  
---  
      
    
    {
      "recipients": {
        object ([Recipients](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#Recipients))
      },
      "scoreThresholdTrigger": {
        object ([ScoreThresholdTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#ScoreThresholdTrigger))
      },
      "jobFailureTrigger": {
        object ([JobFailureTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#JobFailureTrigger))
      },
      "jobEndTrigger": {
        object ([JobEndTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#JobEndTrigger))
      }
    }  
  
Fields  
---  
`recipients` |  `object (`[Recipients](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#Recipients)`)` Required. The recipients who will receive the notification report.  
`scoreThresholdTrigger` |  `object (`[ScoreThresholdTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#ScoreThresholdTrigger)`)` Optional. If set, report will be sent when score threshold is met.  
`jobFailureTrigger` |  `object (`[JobFailureTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#JobFailureTrigger)`)` Optional. If set, report will be sent when a scan job fails.  
`jobEndTrigger` |  `object (`[JobEndTrigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#JobEndTrigger)`)` Optional. If set, report will be sent when a scan job ends.  
  
## Recipients

The individuals or groups who are designated to receive notifications upon triggers.

JSON representation  
---  
      
    
    {
      "emails": [
        string
      ]
    }  
  
Fields  
---  
`emails[]` |  `string` Optional. The email recipients who will receive the DataQualityScan results report.  
  
## ScoreThresholdTrigger

This trigger is triggered when the DQ score in the job result is less than a specified input score.

JSON representation  
---  
      
    
    {
      "scoreThreshold": number
    }  
  
Fields  
---  
`scoreThreshold` |  `number` Optional. The score range is in [0,100].  
  
## JobFailureTrigger

This type has no fields.

This trigger is triggered when the scan job itself fails, regardless of the result.

## JobEndTrigger

This type has no fields.

This trigger is triggered whenever a scan job run ends, regardless of the result.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
