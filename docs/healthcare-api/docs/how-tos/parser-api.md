---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/parser-api/
title: Configure a schema to parse HL7v2 messages \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:28.004566+00:00
---

# Configure a schema to parse HL7v2 messages  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/parser-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Configure a schema to parse HL7v2 messages Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview on how and when to configure a schema on an HL7v2 store to parse HL7v2 messages.

## Default schema

The Cloud Healthcare API uses a default schema to parse HL7v2 messages that conform to the HL7v2 standard. If your HL7v2 messages conform to the standard, and do not contain custom segments, fields, or any other data that deviates from the standard, see [Enable schematized parsing for HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-default-parser).

## Custom schema

If you have HL7v2 messages that don't conform to the HL7v2 standard, see [Use a custom schema to parse HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-custom-parser).

## Select a parser version

You can specify options for the parser in the [`ParserConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig) object, regardless of whether you're using the default schema or a custom schema. The `ParserConfig` contains a [`ParserVersion`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserVersion) object that lets you specify a version for the parser. See the [reference documentation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserVersion.ENUM_VALUES) for details on each version.

We recommend that, for all use cases, you specify the [`V3`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserVersion.ENUM_VALUES.V3) version of the parser. The `V3` version has the following advantages:

  * It contains the existing functionality in the `V2` version.
  * When used with the default parser, it unescapes the following default escaped HL7v2 control characters:

    * Field separator: `|`
    * Component separator: `^`
    * Sub-component separator: `&`
    * Repetition separator: `~`
    * Escape character: `\`
    * Truncation character: `#`
  * When used with a custom parser, the `V3` parser uses improved matching techniques over the other parser versions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
