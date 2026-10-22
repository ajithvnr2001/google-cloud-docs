---
url: https://docs.cloud.google.com/datastream/docs/sources-salesforce/
title: Stream data from Salesforce organizations \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:02.700890+00:00
---

# Stream data from Salesforce organizations  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Salesforce organizations Stay organized with collections  Save and categorize content based on your preferences. 

Datastream supports replicating change events from a Salesforce instance, often referred to as a _Salesforce organization_ , or a _Salesforce org_. Salesforce is a cloud-based CRM platform, and you can replicate data from it just as you would from other sources that Datastream supports.

This page contains information about:

  * The key terms that you need to understand when replicating from Salesforce.
  * The behavior of how Datastream handles data that's being pulled from a source Salesforce org.
  * The versions and editions of Salesforce that Datastream supports.
  * Known limitations for using Salesforce as a source.



## Key terms

Salesforce operates using objects, records and fields:

  * An **object** is a class entity, and is similar to a table in relational databases nomenclature. Objects can be standard or custom. Standard objects are included in Salesforce by default, while custom objects are created by users to store data specific to their use-cases.
  * A **record** is a specific instance of an object, similar to a row in relational databases.
  * A **field** is a specific attribute of an object, similar to a column in relational databases.



## Behavior

The Salesforce source support in Datastream relies upon the REST and Bulk 2.0 APIs. Salesforce polls for source changes based on the interval that you set to allow control over the API usage.

When replicating data from a Salesforce source, the following behavior is observed:

  * Replicateable and queryable standard objects which either have the `SystemModstamp` field or the `LastModifiedDate` can be replicated. For an object to be replicateable, it needs to support the `getUpdated()` and `getDeleted()` API calls. For more information, see [API Calls for Data Replication](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/calls_for_data_replication.htm) in Salesforce documentation.
  * Custom objects can be replicated. 
  * If configured, all historical data is replicated for included objects.
  * All changes, such as inserts, updates, and deletes from the specified objects are replicated.
  * Datastream polls for changes according to the configured polling interval. This is reflected in the stream's data freshness metric. The metric can grow up to the configured polling interval value and reflects the time passed from the most recent poll.



## Versions

Datastream supports the following Salesforce editions:

  * Pro Suite
  * Developer
  * Professional
  * Enterprise
  * Unlimited



Datastream uses the Salesforce API version 61.0.

For more information about available Salesforce editions, see the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=xcloud.overview_edition.htm&type=5).

## Best practices

This section describes recommended best practices for configuring your Salesforce source for use with Datastream.

### Manage API quota usage

Salesforce imposes limits on the number of API requests that can be made in a 24-hour rolling window. Exhausting this quota is a common challenge when replicating data from Salesforce.

You can configure the polling interval in Datastream to reduce the number of API requests made to Salesforce. While a shorter polling interval enhances data freshness, it also increases the API quota usage. We recommend setting a polling interval that balances your chosen data freshness with the constraints of your API quota to ensure sustainable data replication. If needed, you can increase the global API request quota in Salesforce.

## Known limitations

Known limitations for using Salesforce as a source include:

  * Only queryable and replicateable objects are supported.
  * [Compound fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields.htm) are replicated as flattened fields.
  * Up to 600,000 deletes per minute are supported (Salesforce limitation).
  * Streams are limited to 3000 objects.
  * Calculated fields (also known as _formulas_) are only partially supported. Replication of calculated fields is subject to the following constraints:

    * Cross-table references aren't supported.
    * Non-deterministic functions (such as `NOW()` or `TODAY()`) aren't supported, as Datastream can't determine when the values of these fields change.
    * Only a specific set of allowed functions is supported. If a calculated field uses any function outside of this list, the field isn't replicated.

The following list shows the supported functions:

    * **Logical:** `AND`, `OR`, `NOT`, `IF`, `CASE`, `ISNULL`, `ISBLANK`, `BLANKVALUE`, `ISPICKVAL`
    * **Math:** `ABS`, `CEILING`, `MCEILING`, `FLOOR`, `MFLOOR`, `ROUND`, `MOD`, `SQRT`, `EXP`, `LN`, `LOG`, `MAX`, `MIN`
    * **Text:** `BEGINS`, `BR`, `CONTAINS`, `FIND`, `HYPERLINK`, `INCLUDES`, `LEFT`, `LEN`, `LOWER`, `LPAD`, `MID`, `RPAD`, `RIGHT`, `SUBSTITUTE`, `TEXT`, `TRIM`, `UPPER`, `VALUE`
    * **Date and time:** `DATE`, `DATEVALUE`, `DATETIMEVALUE`, `DAY`, `MONTH`, `YEAR`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `WEEKDAY`, `TIMEVALUE`, `ADDMONTHS`
    * **Other:** `REGEX`
  * Stream recovery isn't supported.




## What's next

  * Learn how to [configure a Salesforce source](https://docs.cloud.google.com/datastream/docs/configure-salesforce-org) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
