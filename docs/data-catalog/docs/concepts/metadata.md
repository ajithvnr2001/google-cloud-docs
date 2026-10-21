---
url: https://docs.cloud.google.com/data-catalog/docs/concepts/metadata/
title: Data Catalog metadata \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:54.506214+00:00
---

# Data Catalog metadata  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/concepts/metadata/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback 

#  Data Catalog metadata Stay organized with collections  Save and categorize content based on your preferences. 

Data Catalog handles two types of metadata: technical metadata and business metadata.

## Types of technical metadata

An example of technical metadata related to a data entry, such as a BigQuery table, can include the following attributes:

  * Project information, such as name and ID
  * Asset name and description
  * Google Cloud resource labels
  * Schema name and description for BigQuery tables and views

**Note:** The "Last modification time" of a BigQuery table resource refers to the modification time of the table's metadata, which might vary from the "Last modified" time listed in the BigQuery UI.

## Types of business metadata

Business metadata for a data entry can be of the following types:

  * **Tags** applied to a data entry.

To know more about tags, see [Tag and tag templates](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates).




**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  * (Preview) **Data stewards** associated with a data entry. A data steward for a data entry can be contacted to request more information about the data entry. A data steward does not require a specific IAM role. You can add a user with a non-Google email account as a data steward for a data entry. A data steward can't perform any project-related activity within the console, unless the user is provided with explicit IAM permissions.

  * (Preview) **Rich text overview** of a data entry that can include images, tables, and links.




### Search for business metadata

Business metadata is always linked to a technical metadata entry. Business metadata is searchable without the use of any syntax. The only exception to this search is tags, which requires the use of [tag syntax](https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference).

The following is a list of important information for the business metadata search for a Data Catalog data entry:

  * You can use email addresses or names of data stewards, and text from the data entry **overview** descriptions to search for relevant Data Catalog data entries.
  * Data Catalog doesn't support image search related to the rich text descriptions.
  * If you delete a data entry and then recreate it within 32 days with the exact same identifier, then the overview and data steward of the data entry are restored.



### Limits for business metadata

For information about the limits for business metadata, see [Quotas and limits](https://docs.cloud.google.com/data-catalog/docs/resources/quotas).

## What's next

  * [Apply](https://docs.cloud.google.com/data-catalog/docs/quickstarts/quickstart-search-tag) a tag, an overview, and a data steward to an entry.

  * Learn more about [tag templates and tags](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates) .




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
