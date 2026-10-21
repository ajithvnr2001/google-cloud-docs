---
url: https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates/
title: Tags and tag templates \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.355637+00:00
---

# Tags and tag templates  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback 

#  Tags and tag templates Stay organized with collections  Save and categorize content based on your preferences. 

Documenting data entries at scale is difficult, especially when they are used by different groups in an organization with varying needs. Often each group creates their own set of documentation and metadata to describe the same data, resulting in duplicated effort and incomplete information. Data Catalog solves this problem with tags, which enable organizations to create, search, and manage metadata for all their data entries in a unified service.

This document explains two key Data Catalog concepts:

  * **Tags** : custom metadata fields that you can attach to a data entry to provide context

  * **Tag templates** : reusable structures that you can use to rapidly create new tags




## Tags

Tags are a type of business metadata. Adding tags to a data entry helps provide meaningful context to anyone who needs to use the asset. For example, a tag can tell you information such as who is responsible for a particular data entry, whether it contains personally identifiable information (PII), the data retention policy for the asset, and a data quality score.

Tags can be public tags or private tags. Each type of tag has some unique advantages to suit your business requirements.

### Private tags

Private tags provide strict access controls. You can search or view the tags and the data entries associated with the tags only if you are granted the required view permissions on both the private tag template and the data entries.

Searching for private tags in the Data Catalog page requires that you use the `tag:` search syntax or the search filters.

Private tags are suitable for scenarios where you need to store some sensitive information in the tag and you want to apply additional access restrictions beyond checking whether the user has the permissions to view the tagged entry.

### Public tags

Public tags provide less strict access control for searching and viewing the tag as compared to private tags. Any user who has the required view permissions for a data entry can view all the public tags associated with it. View permissions for public tags are only required when you perform a search in Data Catalog using the `tag:` syntax or when you view an unattached tag template.

Public tags support both simple search and search with predicates in the Data Catalog search page. When you create a tag template, the option to create a public tag template is the default and recommended option in the Google Cloud console.

For example, consider a public tag template called `employee data`, which you used to create tags for three data entries called `Name`, `Location`, and `Salary`. Among the three data entries, only members of a specific group called `HR` can view the `Salary` data entry. The other two data entries have view permissions for all employees of the company.

If any employee who isn't a member of the `HR` group uses the Data Catalog search page and searches with the word `employee`, the search result displays only the `Name` and `Location` data entries with the associated public tags.

Public tags are useful for a broad set of scenarios and these tags are intuitive to use. Public tags support simple search and search with predicates while private tags support only search with predicates.

### Sample tags attached to a data entry

The following diagram shows a sample customer table `cust_tbl`, with several business metadata tags attached to the table and its columns.

![The sample uses table tags to describe the data governance, quality, and
  usage, and column tags to flag PII like SSNs and contact info.](https://docs.cloud.google.com/static/data-catalog/images/sample-customer-table.png)**Figure 1.** Data Catalog supports tagging at the table and column levels. 

## Tag templates

To start tagging data, you first need to create one or more tag templates. A tag template can be a public or private tag template. When you create a tag template, the option to create a public tag template is the default and recommended option in the Google Cloud console. A tag template is a group of metadata key-value pairs called **fields**. Having a set of templates is similar to having a database schema for your metadata.

You can structure your tags by topic. For example:

  * **A data governance tag** with fields for data governor, retention date, deletion date, PII (yes or no), and data classification (public, confidential, sensitive, regulatory)
  * **A data quality tag** with fields for quality issues, update frequency, and SLO information
  * **A data usage tag** with fields for top users, top queries, and average daily users



You can then mix and match tags, using only the tags relevant for each data asset and your business needs.

### Fields in a tag

Tags contain one or more **fields** where information can be stored. The fields in a tag are defined by a tag template, and each field can be used to store one or more **values**. Every tag is an instance of a tag template, which can be applied to an entire data entry, or to particular tables or columns. A tag on a column could tell you, for example, if that column contains PII, whether it's been deprecated, or what formula was used to calculate a certain value.

Each field contains an **ID** , a **display name** , and a **type**. The type can be a `string`, `double`, `boolean`, `enum` (enumeration), or `datetime`. When the type is `enum`, the template also stores the allowed values for the field.

**Note:** Each `enum` field can store up to 100 values.

Fields are stored in the template as an ordered set, where the order represents the relative importance of a field relative to the other fields.

Fields are optional unless marked as required. A required field must be given a value when the template is used, while an optional field can be left empty.

You cannot change an optional field to a required after creating your template.

### Sample fields in a tag

Here is an example tag template from the [quickstart](https://docs.cloud.google.com/data-catalog/docs/tag-bigquery-dataset), containing multiple field types:

![The example tag template defines fields for the data source, number of
  rows, presence of PII, and PII type.](https://docs.cloud.google.com/static/data-catalog/images/tag-template-fields.png)**Figure 2.** A Data Catalog tag template. 

Here is a tag created from the template, with **values** provided for each field:

![The example tag indicates its data is from a named table, has hundreds of
  millions of rows, and has no PII.](https://docs.cloud.google.com/static/data-catalog/images/quickstart-tag-example.png)**Figure 3.** A tag created from a tag template. 

### View the tag template gallery

To help you get started, Data Catalog includes a gallery of sample tag templates to illustrate common tagging use cases. Use these examples to learn about the power of tagging, for inspiration, or as a starting point for creating your own tagging infrastructure.

To use a tag template gallery, perform the following steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Tag templates** page.

[Go to Tag templates](https://console.cloud.google.com/dataplex/templates)

  2. Click **Create tag template**.

The template gallery is displayed as part of the **Create template** page.




After you've selected a template from the gallery, you can use it just like any other tag template. You can add and delete attributes, and change anything in the template to suit your business needs. You can then search for the template fields and values using Data Catalog.

## Access control for tags

Tags and their metadata can contain sensitive information, and data governance teams might want certain tags to be visible only to select groups of users. Data Catalog provides access control on tag templates, and these settings extend to all tags created using that template.

You can set up tag templates with many access control configurations, for example:

  * A tag template that only the template creator can use to create tags
  * A tag template that creates tags that are only visible to a select set of users
  * A tag template that a select set of users can use to create tags that are only visible to another (possibly identical) set of users
  * A tag template visible to all the users of an organization or a project (public tag)



Access to a tag template is granted or denied with IAM roles. These provide permissions to create, edit, and use the tag template. The following are some available Data Catalog roles:

  * To let a user create or update a tag template, you must grant them the tag template creator role.

  * To let a user apply tags to a data entry, you must grant them the tag template user role.




For more information, see [Data Catalog Identity and Access Management](https://docs.cloud.google.com/data-catalog/docs/concepts/iam).

## Regional resources

Every tag template and tag is stored in a particular [Google Cloud region](https://docs.cloud.google.com/data-catalog/docs/concepts/regions). You can use a tag template to create a tag in any region, so you don't need to create copies of your template if you have data entries spread across multiple regions.

## What's Next

  * Read about the roles and permissions required to view and attach public and private tags. See [Roles to view public and private tags](https://docs.cloud.google.com/data-catalog/docs/concepts/iam#roles_to_view_public_and_private_tags) and [Roles to attach tags to Google Cloud resources](https://docs.cloud.google.com/data-catalog/docs/concepts/iam#roles_to_attach_tags_to_resources).

  * Read about how to use public and private tags to search data entries. See [Data Catalog search syntax](https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference).

  * Create a sample public tag template and some tags. For more information, [Tag a BigQuery table by using Data Catalog](https://docs.cloud.google.com/data-catalog/docs/tag-bigquery-dataset).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
