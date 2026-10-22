---
url: https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference/
title: CEL filters reference for storage batch operations \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:21.011542+00:00
---

# CEL filters reference for storage batch operations  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  CEL filters reference for storage batch operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Common Expression Language (CEL) syntax and supported operations when you construct advanced filters for [ storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) job based on [Storage Insights dataset](https://docs.cloud.google.com/storage/docs/insights/datasets) fields.

You can use advanced filters to evaluate conditions and automate management actions across millions of files based on fields in your Storage Insights dataset. Supported filters use [CEL](https://opensource.google/projects/cel) rules directly on object metadata.

Supply filter rules by using the `--bucket-filters` and `--object-filters` flags in the Google Cloud CLI, or the `bucketFilters` and `objectFilters` fields in the JSON API when you [create a job](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters). This option eliminates the need to manually query BigQuery, export object lists to CSV, and upload manifests back to your buckets. When you use dataset filters for object selection, storage batch operations targets objects that are live and current as of the selected dataset snapshot. Consequently, the job only includes objects that have a `NULL` value for both `softDeleteTime` and `timeDeleted` at the time of the snapshot.

## Supported operators and functions

Advanced filters support conditions joined by logical AND (`&&`) statements. Use the following operators to build your criteria strings:

Operator | CEL usage | Equivalent GoogleSQL syntax | Description  
---|---|---|---  
StartsWith | `name.startsWith("prefix")` | `STARTS_WITH(name, "prefix")` | Match objects with a string attribute that begins with a specific prefix.  
EndsWith | `name.endsWith(".pdf")` | `ENDS_WITH(name, ".pdf")` | Match objects with a string attribute that ends with a specific suffix.  
Equals | `==` | `=` | Match objects with an attribute that equals a specific value.  
Not equals | `!=` | `!=` | Exclude objects with an attribute that exactly matches a specific value.  
Greater than | `>` | `>` | Match objects with an integer or timestamp attribute exceeding a threshold.  
Greater than or equal to | `>=` | `>=` | Match objects with an integer or timestamp attribute equal to or exceeding a threshold.  
Less than | `<` | `<` | Match objects with an integer or timestamp attribute below a threshold.  
Less than or equal to | `<=` | `<=` | Match objects with an integer or timestamp attribute equal to or below a threshold.  
Contains | `name.contains("substring")` | `STRPOS(name, "substring") != 0` | Match objects with a string attribute containing the substring.  
In | `name in ['a', 'b']` | `name IN UNNEST(ARRAY<STRING>['a', 'b'])` | Match objects with an attribute that exists in the provided list.  
Logical NOT | `!` | `NOT` | Invert a rule to filter objects that don't match conditions.  
Timestamp | `timestamp("2025-01-01T00:00:00Z")` | `TIMESTAMP "2025-01-01 00:00:00 UTC"` | Cast date strings formatted in RFC 3339 to a timestamp. This function supports microsecond precision to match [BigQuery TIMESTAMP type standards](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type).  
Exists | `contexts.exists(c, c.key == "env")` | `EXISTS(SELECT c FROM UNNEST(contexts) AS c WHERE c.key = "env" LIMIT 1)` | Match objects where at least one item within a repeated record type attribute meets a specific condition.  
**Note:** BigQuery evaluates advanced filter conditions in SQL. To learn about query evaluation, including precision limits and edge cases, see the [GoogleSQL reference documentation for functions and operators](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/operators).

## Supported identifiers

When constructing filter expressions, you can reference both bucket-level fields and object-level fields. The following identifiers map to recognized fields in the [Storage Insights dataset table schemas](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas):

### Bucket attributes

You can use the following bucket-level fields to filter which buckets are included in your storage batch operations jobs.

Field | Type | Description  
---|---|---  
`name` | STRING | The name of the bucket.  
`autoclass` | RECORD | Contains `enabled` and `toggleTime` metadata.  
`autoclass.enabled` | BOOLEAN | Indicates whether Autoclass is enabled for the bucket.  
`autoclass.toggleTime` | TIMESTAMP | The time when Autoclass was last enabled or disabled.  
`labels` | REPEATED RECORD | Contains standard key-value maps.  
`location` | STRING | Bucket location identifier.  
`softDeletePolicy` | RECORD | Contains `retentionDurationSeconds` and `effectiveTime`.  
`softDeletePolicy.retentionDurationSeconds` | INTEGER | The soft delete retention period, in seconds.  
`softDeletePolicy.effectiveTime` | TIMESTAMP | The time when the soft delete policy became effective.  
  
### Object attributes

You can use the following attributes to filter storage batch operations jobs by object-level fields:

Field | Type | Description  
---|---|---  
`name` | STRING | The name of the object.  
`contexts` | REPEATED RECORD | Contexts attached to an object.  
`contexts.key` | STRING | The custom context key.  
`contexts.value` | STRING | The value of the custom context key.  
`contexts.type` | STRING | The custom context type.  
`contexts.createTime` | TIMESTAMP | The time when the custom context key was created.  
`contexts.updateTime` | TIMESTAMP | The time when the custom context key was updated.  
`contentType` | STRING | MIME type content categorization.  
`customTime` | TIMESTAMP | User-defined timestamp.  
`generation` | INTEGER | Object generation identifier.  
`metadata` | REPEATED RECORD | Custom metadata.  
`metadata.key` | STRING | The custom metadata key.  
`metadata.value` | STRING | The custom metadata value.  
`metageneration` | INTEGER | Metadata generation identifier.  
`retentionExpirationTime` | TIMESTAMP | Time when object retention expires.  
`securityInsights` | RECORD | Contains public access insights for the object.  
`securityInsights.publicAccessInsight` | RECORD | Provides the public accessibility status of the object.  
`securityInsights.publicAccessInsight.readPublicAccess` | STRING | The public readability status of the object. Supported values are `PUBLIC`, `NOT_PUBLIC`, `UNSUPPORTED`, and `ERROR`.  
`securityInsights.publicAccessInsight.readPublicAccessSource` | STRING | If `readPublicAccess` is `PUBLIC`, returns the source of the public read permission. Supported values are `Object`, `Bucket`, and `ERROR`.  
`securityInsights.publicAccessInsight.writePublicAccess` | STRING | The public writability status of the object. Supported values are `PUBLIC`, `NOT_PUBLIC`, `UNSUPPORTED`, and `ERROR`.  
`size` | INTEGER | Object size in bytes.  
`storageClass` | STRING | The assigned storage class.  
`temporaryHold` | BOOLEAN | Active block status preventing release.  
`timeCreated` | TIMESTAMP | Initial generation registration clock.  
`timeStorageClassUpdated` | TIMESTAMP | Time when storage class was last updated.  
`updated` | TIMESTAMP | Time when object was last updated.  
  
## Expression format rules

To help your jobs run at a large scale, the query engine applies the following formatting rules:

  1. **Filter conditions** : You can join filter conditions only by using the logical AND (`&&`) operator. The query engine doesn't support the logical OR (`||`) operator.
  2. **Argument positioning** : You must place the target metadata field on the left side of functions. For example, use `name.startsWith("live-")` instead of `"live-".startsWith(name)`.
  3. **Array methods** : You can call the `exists` macro directly on repeated fields, such as `contexts.exists(...)` or `metadata.exists(...)`.
  4. **Bucket limit** : A single storage batch operations job can operate on up to 1,000 buckets. If your filter expressions dynamically match more than 1,000 buckets in your dataset, job creation fails. Use specific bucket-level fields (for example, location filtering such as `location == "us-central1"` or name matching such as `name.startsWith("prod-")`) to narrow your query scope and satisfy this limit.
  5. **Character limit** : Bucket filters and object filters are each limited to a maximum of 150 characters.



## Examples

The following examples show common combined filters that you can use to target resources project-wide. Specify the filter snippets directly as flags in the `gcloud storage batch-operations jobs create` command:

  * **Target specific buckets** : Apply actions to objects in specific buckets: 
        
        --bucket-filters="name in ['bucket-1', 'bucket-2']"

  * **Check storage class and bucket location** : Apply actions to objects in the Standard storage storage class in `US` locations: 
        
        --bucket-filters="location.startsWith('us')"   
        
        --object-filters="storageClass == 'STANDARD'"

  * **Filter by soft delete retention** : Apply actions to objects in buckets that have soft delete enabled for at least 7 days: 
        
        --bucket-filters="softDeletePolicy.retentionDurationSeconds >= 604800"

  * **Filter by object size and extensions** : Find PDF objects greater than 5 KiB: 
        
        --object-filters="size >= 5120 && name.endsWith('.pdf')"

  * **Check custom context keys** : Apply actions to objects that have a custom context key `env`: 
        
        --object-filters="contexts.exists(context, context.key == 'env')"

  * **Match custom context key-value pairs** : Apply actions to objects that have a custom context key `env` with a value of `prod`: 
        
        --object-filters="contexts.exists(context, context.key == 'env' && context.value == 'prod')"

  * **Match custom context values by prefix and suffix** : Apply actions to objects with a custom context value that begins with the prefix `prod` and ends with the suffix `.txt`: 
        
        --object-filters="contexts.exists(context, context.value.startsWith('prod') && context.value.endsWith('.txt'))"

  * **Identify missing context keys** : Apply actions to objects that don't have a custom context key `env`: 
        
        --object-filters="!contexts.exists(context, context.key == 'env')"




## What's next

  * Learn how to [create a job using advanced filters](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters).
  * Learn how to [create and manage storage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
