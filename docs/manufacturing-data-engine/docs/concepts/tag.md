---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/tag/
title: Tag \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:54:04.381089+00:00
---

# Tag  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tag

Tags are data sources emitting a stream of source messages, such as sensors, PLCs, machines, or devices. In Manufacturing Data Engine (MDE), tags are uniquely identified by `tagName`. All records in MDE have a `tagName` attribute, and all records that share the same `tagName` are collectively referred to as the _tag stream_.

In the context of metadata, MDE features a special class of metadata buckets called [tag buckets](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#types_of_buckets). The `tagName` serves as the natural key in tag buckets. That means, you can attach contextual information to tag names, and metadata instances are versioned on the tag name.

You can also change how MDE processes records that share same `tagName` in the context of type versions. That means, you can attach configuration parameters to a `tagName` for type versions. For example, you can override the default type storage specifications for a individual tags in a type version.

### Naming restrictions for Tags

A tag name can contain the following:

  * Letters (uppercase and lowercase), numbers and the special characters `-`, `!`, `*`, `.`,`_`, `(` and `)`.
  * Can be up to 255 characters long.



You can use the following regular expression for validation: `^[A-Za-z0-9\\-_\\$\\.\\!\\*\\(\\)]{1,255}$`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
