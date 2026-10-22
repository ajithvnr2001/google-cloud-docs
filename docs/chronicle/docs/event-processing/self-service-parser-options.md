---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/self-service-parser-options/
title: Manage self-service parser options \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:01.488898+00:00
---

# Manage self-service parser options  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/self-service-parser-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage self-service parser options

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The Google Security Operations platform's Unified Data Model (UDM) provides comprehensive support for threat detection and data normalization. Google SecOps actively develops and updates prebuilt parsers for many commercial products. However, a strict service level governs custom requests: Google Engineering processes requests for new parsers or additional field mapping in existing parsers on a _best-effort basis_. You must review and understand the [Parser support levels](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#levels-parser-support) for complete details.

To achieve the best results—including immediate control over log ingestion, faster time-to-value, and instant deployment of updates—you must take advantage of the following self-service options.

## Recommended self-service options

**Use case** | **Recommended capability** | **Benefits**  
---|---|---  
**New log source (tenant-specific)** | Custom log types | Rapidly onboard unique or highly customized data streams without requiring Google review.  
**Extracting additional fields (JSON/XML)** | Auto Extraction | Automatically identify and extract new fields from structured logs (JSON, XML) with minimal configuration.  
**Custom UDM mapping or non-JSON/XML** | Parser extensions | Achieve granular, precise control over extraction logic and ensure specific fields are correctly mapped to UDM for maximum search and detection efficacy.  
**Creating a full new parser** | Option A: Auto Extraction or Option B: Full custom parser | **A:** Simplest and fastest path for structured logs.  
**B:** Gives you complete ownership and instant update capability for complex logs.  
  
## Detailed use cases for self-service

This section provides scenarios and practical guidance to help you select the most effective self-service tool for your specific parser or data ingestion needs.

### Custom log types for tenant-only sources

If you need to ingest a new log type—even if the commercial product is well-known—but the log format is specific and aimed only for use within your tenant, you should use the self-service capability for **Custom Log Types**.

This approach lets you quickly register your unique log format within your environment, bypassing the need for a global parser that would require extensive review and deployment by Google.

For more information about how to create a custom log type, see [Custom log types](https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type#custom-log-types).

### Enhance existing parsers with Auto Extraction (JSON/XML)

If you're using an existing parser for logs in JSON or XML format and want to extract additional fields that are not currently being parsed, you should use **Auto Extraction**.

Auto Extraction dynamically scans your structured logs to identify unmapped fields, allowing you to instantly enrich your UDM records without requiring code changes to the base parser.

For more information about Auto Extraction capabilities, see [Auto Extraction overview](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction).

### Fine-tune extraction and UDM mapping with parser extensions

If your logs are in a format different from JSON or XML, or if you require precise control over how extracted fields are mapped to specific UDM fields, you should utilize **Parser Extensions**.

Parser extensions provide a powerful mechanism to modify, extend, or override the logic of existing parsers. They're the ideal choice when you need to:

  * Map fields that aren't automatically identified.
  * Apply custom logic to reformat field values.
  * Ensure accurate data normalization to the UDM standard.



For more information on implementing parser extensions, see [Parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions) and [Parser extension examples](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-extension-examples).

### Create a new parser for a new log source

When you're onboarding a completely new log source, use one of these self-service options, ordered by complexity:

  * **Option 1: Auto Extraction (simple):**

Auto extraction is the recommended and most straightforward path for structured logs (JSON/XML). When your new log source is in a structured format, Auto Extraction confirms that all fields are immediately parsed and ready for UDM ingestion with minimal configuration effort.

For more information about using this capability, see [Auto Extraction overview](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction).

  * **Option 2: Full custom parser (advanced):**

This option is best suited for Complex or Unique Log Formats. If the logs are complex, unstructured, or require specific regex patterns for extraction, you can create a full custom parser on your own. This grants you complete ownership of the parser logic and allows for instant updates and iteration.

For more information about how to manage full custom parsers, see [Custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#manage_custom_parser_updates).




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
