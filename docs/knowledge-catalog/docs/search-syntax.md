---
url: https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax/
title: Search syntax for Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:54.468348+00:00
---

# Search syntax for Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Search syntax for Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Knowledge Catalog search supports both semantic and keyword matching. It also supports keyword-only search mode for backward compatibility. For information about keyword-only search, its filters, and how to use it, see [Keyword-only search](https://docs.cloud.google.com/knowledge-catalog/docs/keyword-search).

Knowledge Catalog lets you discover, centrally catalog, manage, and understand your organization's data. To efficiently find specific data assets within your data catalog, you can use powerful search queries. The syntax for search queries includes:

  * **Simple search** : Finding data assets using a single search term.
  * **Free-text search** : Finding data assets using natural language phrases or keywords.
  * **Qualified predicates** : Refining your search using specific metadata fields like name, location, system, or type.
  * **Aspect search** : Searching for entries based on their attached business and technical metadata.
  * **Logical operators** : Combining multiple search criteria using `AND`, `OR`, or `NOT` operators to create complex queries. By understanding this syntax, you can quickly locate the data you need.



## Qualified predicates

Use a qualified predicate to narrow down the search results by explicitly instructing search to evaluate a specific metadata field, such as an asset name, type, or system.

You can qualify a predicate by prefixing it with a key that restricts the matching to a specific piece of metadata:

  * An equal sign (`=`) to restrict the search to an exact match.
  * A colon (`:`) after the key to match the predicate to either a substring or a token within the value in the search results.



Tokenization splits the stream of text into a series of tokens, with each token usually corresponding to a single word.

For example:

  * `name:foo` selects resources with names that contain the `foo` substring, such as `foo1` and `barfoo`.
  * `description:foo` selects resources with the `foo` token in the description, such as `bar` and `foo`.
  * `location=foo` matches resources in a specified location with `foo` as the location name.



### Supported qualifiers

Knowledge Catalog search supports the following qualifiers:

Qualifier | Description  
---|---  
`name:x` | Matches `x` as a substring of the resource ID or resource display name.  
`displayname:x` | Matches `x` as a substring of the resource display name.  
`column:x` | Matches `x` as a substring of the column name (or nested column name) in the schema of the resource.  
`description:x` | Matches `x` as a token in the resource description. For example: 

  * `description:"products"` shows all the resources that have token `products` in the description. For example, "list of products in inventory".
  * `description:"prod"` doesn't show the resources that have token `products` in the description. Instead, it shows all the resources that have token `prod` in the description. For example, "prod environment".

  
`labels:bar` | Matches resources that have a label (with some value) and the label key has `bar` as a substring.  
`labels=bar` | Matches resources that have a label (with some value) and the label key equals `bar` as a string.  
`labels.bar:x` | Matches `x` as a substring in the value of a label with key `bar` attached to a resource.  
`labels.foo=bar` | Matches resources where the key equals `foo` and the key value equals `bar`.  
`type=TYPE` | Matches resources of a specific entry type or its type alias. Requires the `=` qualifier.  
`projectid:bar` | Matches resources within Google Cloud projects that match `bar` as a substring in the ID.  
`parent:x` | Matches `x` as a substring of the hierarchical path of a resource.  
`system=SYSTEM` | Matches resources from a specified system. Requires the `=` qualifier.  
`location=LOCATION` |  Matches resources in a specified location with an exact name. Requires the `=` qualifier. For example, `location=us-central1` matches assets hosted in Iowa. BigQuery Omni assets support this qualifier by using the [BigQuery Omni location name](https://docs.cloud.google.com/bigquery/docs/omni-introduction#locations). For example, `location=aws-us-east-1` matches BigQuery Omni assets in Northern Virginia.   
`createtime` |  Finds resources that were created within, before, or after a given date, timestamp, or relative time in days. For supported formats and operators, see Time filters.  
`updatetime` |  Finds resources that were updated within, before, or after a given date, timestamp, or relative time in days. For supported formats and operators, see Time filters.  
  
### Exact match qualifiers

The predicate keys `type`, `system`, `location`, and aspect search (excluding `has`) support only the exact match (`=`) qualifier, not the substring qualifier (`:`).

Use the following exact match syntax for these predicates:

Predicate key | Correct syntax | Incorrect syntax  
---|---|---  
`type` | `type=table` (or `type=view`, `type=dataset`) | `type:table` or `type:tab`  
`system` | `system=bigquery` (or `system=spanner`) | `system:bigquery` or `system:big`  
`location` | `location=us-central1` (or `location=europe-west1`) | `location:us-central1` or `location:us`  
  
### Substring qualifiers

Predicates such as `name`, `displayname`, `column`, `projectid`, and `parent`, support substring matching with the colon (`:`) qualifier:

  * `name:transactions` matches resources whose ID or display name contains `transactions`. For example, `daily_transactions_raw` and `transactions_v2`.
  * `column:customer_id` matches resources with a column name containing `customer_id`.
  * `projectid:prod` matches resources in projects whose ID contains `prod`. For example, `finance-prod-2026`.



## Time filters

You can filter resources by creation time (`createtime`) or last update time (`updatetime`).

### Supported operators and formats

  * **Supported operators** : `:`, `=`, `<`, `>`, `<=`, `>=`, `=>`, `=<`
  * **Relative days (`-Nd`)**: Filter by a relative number of days in the past (for example, `-30d`, `-7d`, `-1d`).
  * **Calendar dates (`YYYY-MM-DD` or `YYYY/MM/DD`)**: Filter by a specific date in GMT/UTC.
  * **Full timestamps (`YYYY-MM-DDTHH:MM:SS` or `YYYY-MM-DDTHH:MM:SSZ`)**: Filter by a precise timestamp in GMT/UTC. Partial timestamps, such as `YYYY-MM-DDTHH:MM` or `YYYY-MM-DDTHH`, are also supported.



### Time filter syntax

The following table explains the time filter syntax:

Format category | Valid syntax | Invalid syntax | Description  
---|---|---|---  
**Relative time units** | 

  * `createtime>-30d` (last 30 days)
  * `createtime<=-7d` (7 days ago or earlier)
  * `updatetime=-1d` (previous day)
  * `updatetime>=-90d`

| 

  * `createtime>-24h`
  * `createtime>-60m`
  * `createtime>-2w`
  * `createtime>30d`

| 

  * Only negative day units (`-Nd`) are supported for relative time.
  * Shorter units (hours `h`, minutes `m`) and longer units (weeks `w`, months `m`) are not supported.
  * Positive offsets without a leading minus sign (`-`) are invalid.

  
**Calendar dates** | 

  * `createtime:2025-01-15`
  * `createtime>2025-01-01`
  * `createtime<=2025-06-30`
  * `createtime:2025/01/15`
  * `createtime:2025-01`
  * `createtime:2025`

| 

  * `createtime:15-01-2025`
  * `createtime:Jan-15-2025`
  * `createtime:01/15/2025`

| 

  * Dates must follow `YYYY-MM-DD` or `YYYY/MM/DD` format. 
  * Formats with non-standard component order (such as `DD-MM-YYYY` or `MM/DD/YYYY`) or month names are invalid.

  
**Timestamps and time zones** | 

  * `createtime:2025-01-15T05:30:00`
  * `createtime>2025-01-15T05:30:00Z`
  * `createtime:2025-01-15T05:30`

| 

  * `createtime:2025-01-15T05:30:00-08:00`
  * `createtime:2025-01-15T05:30:00 EST`
  * `createtime:2025-01-15T05:30:00+05:30`

| 

  * All timestamps are evaluated in GMT/UTC. 
  * Non-GMT time zone offsets (such as `-08:00` or `+05:30`) and time zone abbreviations (such as `EST` or `PST`) are not supported.

  
**Time-of-day ranges** | 

  * `createtime>=2025-01-15T09:00:00 createtime<=2025-01-15T17:00:00`

| 

  * `createtime:09:00:00..17:00:00`
  * `createtime:09:00-17:00`

| 

  * Time-of-day range syntax is not supported.
  * Use separate lower and upper bound comparisons with full date-time strings instead.

  
**Natural language dates** | 

  * `createtime=-1d`
  * `createtime>-30d`

| 

  * `createtime:yesterday`
  * `createtime:"last week"`
  * `createtime:today`

| 

  * Natural language date phrases are not supported within `createtime` or `updatetime` qualifiers.
  * Use relative day syntax (`-1d`, `-7d`) or explicit dates.

  
  
## Label filters

Use the `labels` predicate to filter resources by attached labels. You can filter by label key, label value, or both:

Query pattern | Example | Description  
---|---|---  
`labels=KEY` | `labels=environment` | Matches resources that have a label with the exact key `environment`, regardless of its value.  
`labels:KEY_SUBSTRING` | `labels:tier` | Matches resources with a label key containing `tier` as a substring (such as `service_tier` or `storage_tier`).  
`labels.KEY=VALUE` | `labels.env=prod` | Matches resources where the label key is `env` and its value is exactly `prod`.  
`labels.KEY:VALUE_SUBSTRING` | `labels.owner:analytics` | Matches resources with label key `owner` where the value contains `analytics` as a substring (such as `analytics-team` or `data-analytics`).  
Multiple labels (AND) | `labels.env=prod labels.data_tier=tier1` | Matches resources that have both the `env=prod` and `data_tier=tier1` labels attached.  
Combined with system and type | `system=bigquery type=table labels.env=prod labels.confidentiality=high` | Matches BigQuery tables labeled with `env=prod` and `confidentiality=high`.  
  
## Aspect search

You can use query syntax to search for entries based on their attached aspects.

The substring match tries to match against a limited number of aspects. If you can't find the entry by using a fragment of the path, then use the full path to narrow the search and increase recall.

Qualifier | Description  
---|---  
`aspect:x`  
or  
`has:x` | Matches `x` as a substring of the full path to the aspect type of an aspect that is attached to the entry, in the format `projectid.location.ASPECT_TYPE_ID`  
`aspect=x`  
or  
`has=x` | Matches `x` as the full path to the aspect type of an aspect that is attached to the entry, in the format `projectid.location.ASPECT_TYPE_ID`  
`x  
OPERATOR  
value` |  Searches for aspect field values. Matches `x` as a substring of the full path to the aspect type and field name of an aspect that is attached to the entry, in the following formats:

  * Syntax for system aspect types:
    * `ASPECT_TYPE_ID.FIELD_NAME`
    * `dataplex-types.ASPECT_TYPE_ID.FIELD_NAME`
    * `dataplex-types.LOCATION.ASPECT_TYPE_ID.FIELD_NAME`
For example, the following queries match entries where the value of the `type` field in the `bigquery-dataset` aspect is `default`:
    * `bigquery-dataset.type=default`
    * `dataplex-types.bigquery-dataset.type=default`
    * `dataplex-types.global.bigquery-dataset.type=default`
  * Syntax for custom aspect types:
    * If the aspect is created in the global region: `PROJECT_ID.ASPECT_TYPE_ID.FIELD_NAME`
    * If the aspect is created in a specific region: `PROJECT_ID.REGION.ASPECT_TYPE_ID.FIELD_NAME `
For example, the following queries match entries where the value of the `is-enrolled` field in the `employee-info` aspect is `true`.
    * `example-project.us-central1.employee-info.is-enrolled=true`
    * `example-project.employee-info.is-enrolled=true`
The list of supported operators depends on the type of field in the aspect, as follows:
    * **String** : `=` (exact match)
    * **All number types** : `=`, `:`, `<`, `>`, `<=`, `>=`, `=>`, `=<`
    * **Enum** : `=`
    * **Datetime** : same as for numbers, but the values to compare are treated as datetimes instead of numbers
    * **Boolean** : `=`

Only top-level fields of the aspect are searchable.  
  
## Logical operators

A query can combine multiple predicates using logical operators. Note: Logical operators `AND`, `OR`, and `NOT` are case-sensitive and must be in uppercase letters.

### `AND` operator

If you separate multiple search terms or predicates with a space, logical AND is implied, which means you don't have to write it explicitly.

The following examples show how to construct queries with the `AND` operator.

  * Search for BigQuery tables
        
        system=bigquery type=table
        

  * Search for resources in project `banking-prod` with a column named `customer_id`
        
        projectid:banking-prod column:customer_id
        

  * If required, you can use explicit `AND` operator:
        
        system=bigquery AND type=table AND location=us-central1
        




### `OR` operator

Use the `OR` operator to match any of multiple conditions. When combining `OR` with other criteria, use parentheses `( )` to group the expressions and define precedence.

The following examples show how to construct queries with the `OR` operator.

  * Search for BigQuery tables and views
        
        system=bigquery (type=table OR type=view)
        

  * Search for tables across multiple systems
        
        (system=bigquery OR system=spanner) type=table
        

  * Search for entries in either marketing or finance datasets
        
        system=bigquery (parent:marketing_analytics OR parent:finance_analytics)
        




### `NOT` operator

You can negate a predicate by prefixing it with uppercase `NOT` or a `-` (hyphen).

The following examples show how to construct queries with the `NOT` operator.

  * Find all tables except those in a sandbox project

    * Use the `NOT` operator
    
    type=table NOT projectid:sandbox-project
    

    * Use hyphen
    
    type=table -projectid:sandbox-project
    

  * Find all BigQuery resources that don't contain `test` in their name
        
        system=bigquery -name:test
        




### Abbreviated syntax

If you want to use the abbreviated syntax, use `|` (vertical bar) for `OR` operators and `,` (comma) for `AND` operators within parentheses. This abbreviated syntax works for the qualified predicates.

  * Search across multiple project IDs

    * Use the `OR` operator:
    
    projectid:(finance-prod|sales-prod|analytics-prod)
    

    * Use parentheses:
    
    projectid:finance-prod OR projectid:sales-prod OR projectid:analytics-prod
    

  * Search for entries matching multiple column names (`AND`)
        
        column:(customer_id,transaction_date,amount)
        

  * Search for entries matching any of multiple column names (`OR`)
        
        column:(customer_id|user_id|client_id)
        




## Wildcard policy

Knowledge Catalog search syntax doesn't support wildcards, such as `*` or `?`, in query strings or predicates.

If you include an asterisk (`*`) or question mark (`?`) in a query, it is treated as a literal character rather than a pattern-matching wildcard.

For example, to search for tables whose names end with `_masked`:

  * **Supported** : `name:_masked` : uses the substring match `:` qualifier to find all resources whose name contains `_masked`, such as `customer_records_masked` or `transactions_masked`.
  * **Not supported** : `name:*_masked`: the `*` is treated as a literal character, not a pattern wildcard.



## Parentheses

Parentheses in search queries have specific technical functions. If you overuse parentheses or apply them to natural language queries, you can confuse the search parser and degrade result quality.

### Plain natural language

When asking a business question, pass the query in plain text. Don't wrap it in parentheses. For example, write:
    
    
    Find customer orders containing email addresses
    

### Abbreviated predicate syntax

Parentheses are highly effective when used with predicate keys to list multiple `OR` and`AND` conditions in a compact format.

  * Group predicate keys with `OR` (`|`)

    * Search for entries residing in any of the listed projects using (`|`)
          
          projectid:(finance-prod|finance-test|analytics-raw)
          

    * Search for entries residing in any of the listed projects using (`OR`)
    
    projectid:finance-prod OR projectid:finance-test OR projectid:finance-raw
    

  * Group predicate keys with `AND` (`,`)

    * Search for entries that contain all of the specified columns using (`,`)
    
    column:(customer_id, order_date, total_amount)
    

    * Search for entries that contain all of the specified columns using (`AND`)
    
    column:customer_id AND column:order_date AND column:total_amount
    




### Hybrid search

You can combine a natural language query with compact filters.

For example, to find tables specifying monthly active users, but restrict the search to the specified projects, use the following query:
    
    
    monthly active users type=table projectid:(data-warehouse|analytical-tier)
    

### Best practices for using parentheses

  * Don't wrap the entire question in parentheses, because the semantic engine might treat the parentheses as literal characters, leading to low-relevance results.

    * **Incorrect** : `(Show me datasets about US population by state)`
    * **Correct** : `Show me datasets about US population by state`
  * Avoid mixing complex, nested boolean trees with parentheses inside the natural language field. Search is optimized for natural language intent. Overcomplicating the query with parentheses and explicit logic blocks confuses the parser. 

    * **Incorrect** : `(revenue data) AND system=BIGQUERY AND projectid:(data-warehouse | analytical-tier)`
    * **Correct** : `revenue data system=bigquery projectid:(data-warehouse|analytical-tier)`
  * Don't add spaces arbitrarily unless they are part of the value.

    * **Incorrect** : `column:( email | id )`
    * **Correct** : `column:(email|id)`.



## What's next

  * Learn how to [search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) in Knowledge Catalog
  * Learn more [about metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn how to [enrich entries and entry links with metadata by using aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Learn how to [manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
