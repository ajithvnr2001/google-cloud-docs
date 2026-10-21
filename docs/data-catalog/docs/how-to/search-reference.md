---
url: https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference/
title: Data Catalog search syntax \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.201113+00:00
---

# Data Catalog search syntax  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback 

#  Data Catalog search syntax Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the syntax for Data Catalog search queries. Before you read this document, it is important that you understand the concepts of Data Catalog such as data entry, tags and tag templates, and other kinds of metadata. See [What is Data Catalog?](https://docs.cloud.google.com/data-catalog/docs/concepts/overview).

To launch a Data Catalog search query in the Google Cloud console, go to the Data Catalog **Search** page and select **Data Catalog** as the search mode.

[Go to Search](https://console.cloud.google.com/dataplex/search)

## Simple search

In its simplest form, a Data Catalog search query comprises a single predicate. Such a predicate can match several pieces of metadata:

  * A substring of a name, display name, or description of a data asset
  * Exact type of a data asset
  * A substring of a column name (or [nested column](https://docs.cloud.google.com/bigquery/docs/nested-repeated) name) in the schema of a data asset
  * A substring of a project ID
  * The value of a public tag, the name of a public tag template, or a field name in a public tag template attached to a data entry.
  * (Preview) A string for an email address or name for a data steward
  * (Preview) A string from an overview description



The simple search does not support tag template fields of type `datetime`.

For example, the predicate `foo` matches the following entities:

  * Data asset with the `foo.bar` name
  * Data asset with the `Foo Bar` display name
  * Data asset with the description `This is the foo script.`
  * Data asset with the exact `foo` type
  * Column `foo_bar` in the schema of a data asset
  * Nested column `foo_bar` in the schema of a data asset
  * Project `prod-foo-bar`
  * Public tag template named `foo`, data entries tagged with the `foo` tag template, tag template display name of `foo`, tag template field name of `foo`, and tag field value of `foo` in a string, enum, or rich text.
  * (Preview) Data asset with a data steward called `foo`.
  * (Preview) Data asset with an overview containing the word `foo`.



To know more about the roles and permissions to view public and private tags, see [Roles to view public and private tags](https://docs.cloud.google.com/data-catalog/docs/concepts/iam#roles_to_view_public_and_private_tags).

## Qualified predicates

You can qualify a predicate by prefixing it with a key that restricts the matching to a specific piece of metadata.

An equal sign (`=`) restricts the search to an exact match.

A colon (`:`) after the key matches the predicate to either a substring or token within the value in search results.

Tokenization breaks the stream of text up into a series of tokens, with each token usually corresponding to a single word.

For example:

  * `name:foo` selects entities with names that contain the `foo` substring: `foo1` and `barfoo`.
  * `description:foo` selects entities with the `foo` token in the description: `bar and foo`.
  * `location=foo` matches all data assets in a specified location with `foo` as the location name.

**Note:** You can only search for an exact `type=foo`, `system=foo`, `location=foo`, or `orgid=number`. The corresponding predicate keys can't be followed by a colon.

Data Catalog supports the following qualifiers:

Qualifier | Description  
---|---  
`name:x` | Matches `x` as a substring of the data asset ID.  
`displayname:x` | Match `x` as a substring of the data asset display name.  
`column:x` | Matches `x` as a substring of the column name (or nested column name) in the schema of the data asset.  
You can search for a nested column by its path using the AND logical operator.  
For example, `column:(foo bar)` matches a nested column with the `foo.bar` path.  
`description:x` | Matches `x` as a token in the data asset description.  
`label:bar` | Matches BigQuery data assets that have a label (with some value) and the label key has `bar` as a substring.  
`label=bar` | Matches BigQuery data assets that have a label (with some value) and the label key equals `bar` as a string.  
`label:bar:x` | Matches `x` as a substring in the value of a label with key `bar` attached to a BigQuery data asset.  
`label=foo:bar` | Matches BigQuery data assets where the key equals `foo` and the key value equals `bar`.  
`label.foo=bar` | Matches BigQuery data assets where the key equals `foo` and the key value equals `bar`.  
`label.foo` | Matches BigQuery data assets that have a label whose key equals `foo` as a string.  
`type=<type>` | Matches data assets of a specific object type or subtype. Subtypes can be added with the format `<type>.<sub-type>.`  
Types and subtypes include:

  * `type=table` matches all tables, views, and materialized views.
  * `type=dataset` matches all datasets.
  * `type=table.view` or `type=view` matches all views but not materialized views.
  * `type=materialized_view` matches all materialized views.
  * `type=lake` matches all lakes.
  * `type=zone` matches all zones.
  * `type=tag_template` matches all tag templates.
  * `type=entry_group` matches all entry groups.
  * `type=data_stream` matches all Pub/Sub topics.
  * (Preview) `type=dataset.linked` matches all BigQuery sharing (formerly Analytics Hub) linked datasets.

  
`projectid:bar` | Matches data assets within Cloud projects that match `bar` as a substring in the ID.  
`parent:x` | Matches `x` as a substring of the hierarchical path of a BigQuery data asset. The path has the format `<project_id>.<dataset_name>`.  
For example, `parent:foo.bar` matches all tables and views of a dataset with the path `project-foo.bar-dataset`.  
`orgid=number` | Matches data assets within a Cloud organization with the exact ID value of `number`.  
`system=<system>` | Matches all data assets from a specified system.  
Systems include:

  * `system=bigquery` matches all data assets from BigQuery.
  * `system=cloud_bigtable` matches all data assets from Bigtable.
  * `system=cloud_pubsub` matches all data assets from Pub/Sub.
  * `system=cloud_spanner` matches all data assets from Spanner.
  * `system=dataproc_metastore` matches all data assets from Dataproc Metastore.
  * `system=data_catalog` matches all data assets created in Data Catalog.
  * `system=dataplex` matches all data assets created in Knowledge Catalog.

  
`location=<location>` | Matches all data assets in a specified location with an exact name. For example, `location=us-central1` matches all assets hosted in Iowa.  
For a full list of supported locations, see [Data Catalog regions](https://docs.cloud.google.com/data-catalog/docs/concepts/regions).  
`cluster_location=<location>` | Matches all Bigtable data assets in a specified location with an exact name.  
For example, `cluster_location=us-central1` matches all assets hosted in Iowa.  
For a full list of supported locations, see [Bigtable regions](https://docs.cloud.google.com/bigtable/docs/locations).  
`tag:x` | Matches data assets where `x` matches any substring in <`tag_template_project_id`>.<`tag_template_id`>.<`tag_field_id`> of a private or public tag.  
Examples:

  * `tag:data_owner` matches data assets that have the `data_owner` tag.
  * `tag:data_gov_template` matches data assets that have been tagged with the `data_gov_template` tag template.
  * `tag:mycloudproject.data_gov_template` matches data assets tagged with the `data_gov_template` template in the `mycloudproject` project.

  
`tag:key<operator>val` | First, matches the `key` to any substring of the tag field ID, tag template ID, or Google Cloud project ID of a tag template. Then, matches `val` to the tag value of the `key` depending on the tag field type.  
The type-dependent `<operator>` sets permitted for tag values are:

  * _string/richtext_ : ":"  
Note: The colon in this string search denotes an exact token match, not a substring.
  * _boolean_ and _enum_ : "="
  * _double_ : "=", "<", ">", "<=", ">="
  * _timestamp_ : ":", "=", "<", ">", "<=", ">="

Examples:
  * _string_ : `tag:data_owner:@mail.com` matches data assets that have `@mail.com` values.
  * _boolean_ : `tag:data_gov_template.hasPII=true` matches `hasPII` boolean tags in the `data_gov_template` that are `true`.
  * _enum_ : `tag:certification_level_1=HIGHEST`.
  * _double_ : `tag:datascore=9` matches data assets with `datascore` double tags that have value `9`.
  * _timestamp_ : `tag:expiredDate:2019-01-01` matches data assets that have an `expiredDate` tag of `2019-01-01`.
  * _timestamp_ : `tag:expiredDate<2019-02` matches data assets that have an `expiredDate` tag prior to `2019-02-01T00:00:00`.

Timestamp format:`YYYY-MM-DDThh:mm:ss`. All timestamps must be in GMT (time zones are not supported). Partial timestamps and "-" and "/" date separators are supported, for example:

  * 2010-10-22T05:36:24
  * 2010-10-22T05:36
  * 2010-10-22T05
  * 2010-10-22
  * 2010-10
  * 2010
  * 2010/10/22

  
`createtime` | Finds data assets that were created within, prior to, or after a given date or time.  
Examples:

  * `createtime:2019-01-01` matches data assets created on `2019-01-01`.
  * `createtime<2019-02` matches data assets created prior to `2019-02-01T00:00:00`.
  * `createtime>2019-02` matches data assets created after `2019-02-01T00:00:00`.

Timestamp format:`YYYY-MM-DDThh:mm:ss`. All timestamps must be in GMT (time zones are not supported). Partial timestamps and "-" and "/" date separators are supported, for example:

  * 2010-10-22T05:36:24
  * 2010-10-22T05:36
  * 2010-10-22T05
  * 2010-10-22
  * 2010-10
  * 2010
  * 2010/10/22

  
`updatetime` | Finds data assets that were updated within, prior to, or after a given date or time.  
Examples:

  * `updatetime:2019-01-01` matches data assets updated on `2019-01-01`.
  * `updatetime<2019-02` matches data assets updated prior to `2019-02-01T00:00:00`.
  * `updatetime>2019-02` matches data assets updated after `2019-02-01T00:00:00`.

Timestamp format:`YYYY-MM-DDThh:mm:ss`. All timestamps must be in GMT (time zones are not supported). Partial timestamps and "-" and "/" date separators are supported, for example:

  * 2010-10-22T05:36:24
  * 2010-10-22T05:36
  * 2010-10-22T05
  * 2010-10-22
  * 2010-10
  * 2010
  * 2010/10/22

  
`policytag:x` | Match `x` as a substring of the [policy tag](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) display name. Finds all assets using matching policy tag or its descendants.  
`policytagid=x` | Matches `x` as a [policy tag or taxonomy](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) ID. Finds all assets using matching policy tag or its descendants.  
`term:x` | Matches data assets connected to a business glossary term where a substring of name, description, or data steward matches `x`.  
`fully_qualified_name:x` | Matches `x` as a substring of `fully_qualified_name`.  
`fully_qualified_name=x` | Matches `x` as `fully_qualified_name`.  
  
## Logical operators

A query can be comprised of several predicates with logical operators. If you don't specify an operator, logical `AND` is implied. For example, `foo bar` returns entities that match both predicate `foo` and predicate `bar`.

Logical AND and logical OR are supported, for example, `foo OR bar`.

You can negate a predicate with a `-` or `NOT` prefix. For example, `-name:foo` returns all entities with names that don't match the predicate `foo`.

Logical operators are not case-sensitive (for example, "or" and "OR" are acceptable).

### Abbreviated syntax

An abbreviated search syntax is also available, using `|` for `OR` operators and `,` for `AND` operators.

For example, to search for entries inside one of many projects using the `OR` operator, you can use:

`projectid:(pid1|pid2|pid3|pid4)`

Instead of:

`projectid:pid1 OR projectid:pid2 OR projectid:pid3 OR projectid:pid4`

To search for entries with matching column names:

  * AND: `column:(name1, name2, name3)`
  * OR: `column:(name1|name2|name3)`



This abbreviated syntax works for the qualified predicates listed earlier, except for `tag`, `term`, `policytag`, `policytagid` and `label`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
