---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers/
title: Configure custom parsers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:19.902422+00:00
---

# Configure custom parsers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure custom parsers

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides guidance on how to create custom parsers for cases where a prebuilt parser isn't available or when you want more control. Custom parsers appear in the parsers list, alongside prebuilt parsers.

Common use cases include:

  * Ingesting log data for a log type that doesn't have a prebuilt parser. 

Use one of the following methods:

    * Create a custom parser based on mapping instructions to raw logs.
    * Create a custom parser based on an existing parser.
  * Create a custom parser to [skip prebuilt parser updates](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#opt_out_of_parser_updates).




## Limitations and unsupported operations

When you create and manage custom parsers, consider the following operational boundaries:

  * **Parser syntax versus YARA-L detection rules** : Ingestion parsers and parser extensions use Logstash Grok and configuration syntax with filters (for example, `grok`, `mutate`, `json`, `date`, and `base64`) at ingestion time to parse raw logs into the Unified Data Model (UDM). Parsers can't use YARA-L syntax, outcome blocks, or generator functions (such as `yield`). YARA-L 2.0 is strictly a detection engine query language evaluated downstream on normalized UDM events for threat alerting and can't parse raw logs, mutate UDM fields, or drop incoming log traffic.
  * **1:1 ingestion model** : Google SecOps custom parsers operate strictly on a 1:1 relationship. Custom parsers can't de-batch, loop, or split a single log entry containing multiple embedded events (such as JSON arrays or concatenated strings) into separate UDM events. You must split multi-event payloads before ingestion by using log collection pipelines such as BindPlane OP, OpenTelemetry Collector, Fluent Bit, or a pre-ingestion Cloud Run function.
  * **`drop {}` filter behavior**: The `drop {}` filter in a parser suppresses UDM event generation only. When a parser drops a log, Google SecOps doesn't create a UDM record, and detection rules can't evaluate the event. However, Google SecOps retains the original raw log in the immutable raw repository for compliance and audit retention. The raw log remains searchable through Raw Log Search. To drop logs before storage, configure filtering upstream in your forwarder or collector.
  * **Forward-only parsing by default** : When you activate a custom parser, it applies to newly ingested logs only from the time of activation. If there is a critical business need to apply custom parser mappings to existing historical logs, you can request a backend Log Replay task. For more information, see [Re-parse historical data (Log Replay)](https://docs.cloud.google.com/chronicle/docs/event-processing/reparse-historical-data).



## Create a custom parser based on mapping instructions

You can create a custom parser by writing code that converts the original raw log to a UDM record. 

Additional reading:

  * For more information about the structure of a parser, see [Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview).
  * For more information about parser syntax, see [Parser syntax reference](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax).



When creating a parser, aim to populate as many [important UDM fields](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields) as possible.

  1. Go to **Settings**.

  2. Go to **SIEM Settings**.

  3. Click **Create Parser**.

  4. Select an appropriate log source from the **Log Source** list.

  5. Select **Start with Raw Logs Only** to create a new parser according to your requirements.

  6. Click **Create**.

  7. Enter your code in the **Parser Code Terminal**. For more information, see [Create a code snippet mapping instruction](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions#code_snippet).

**Note:** Make sure that your custom parser logic correctly maps and produces valid, current timestamps. If a custom parser incorrectly maps timestamps to a date outside of your standard retention window, the data is successfully ingested but will remain unsearchable in the user interface. Since search features rely on event timestamps for filtering, data mapped to an incorrect date is effectively invisible despite successful ingestion.

  8. Optional: Click edit **Edit** to edit the existing raw log or copy.

  9. Optional: Click refresh **Load** to load the latest raw log.

  10. Click **Preview** to view the UDM output. An error message is displayed if the code is incorrect.

In the preview, you can use the statedump filter plugin to validate a parser's internal state. For more information, see [Validate data using statedump plugin](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax#validate_data_using_statedump_plugin).

  11. Click **Validate** to validate the custom parser.

The validation process may take a few minutes, so we recommend that you preview the custom parser first, make changes if required, and then validate the custom parser.

  12. Click **Submit**.

The parser is activated for the normalization process after 20 minutes.




## Create a custom parser based on an existing parser

Use an existing parser as a template to create a new custom parser. This method supports only the code-based approach. To get started, follow these steps:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click **Create Parser**.

  3. Select an appropriate log source from the **Log Source** list.

  4. Select **Start with an Existing Prebuilt Parser** to use an existing parser as a base to create a new custom parser.

**Note:** If the selected log source does not have a prebuilt parser then this option is not displayed.
  5. Click **Create**.

  6. Edit your code in the **Parser Code Terminal**. For more information, see [Create a code snippet mapping instruction](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions#code_snippet).

  7. Optional: Click edit **Edit** to edit the raw log.

  8. Optional: Click refresh **Refresh** to refresh the raw log.

  9. As you add code to build the parser, click **Preview** to view the UDM output. An error message is displayed if the code is incorrect.

In the preview, you can use the statedump filter plugin to validate the internal state of a parser. For more information, see [Validate data using statedump plugin](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax#validate_data_using_statedump_plugin).

  10. Click **Validate** to validate the custom parser.

The validation process may take a few minutes, so we recommend that you preview the custom parser first, make changes if required, and then validate the custom parser.

  11. Click **Submit**.

The parser is activated for the normalization process after 20 minutes.




## Make a custom parser inactive

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert **Menu** against the parser that you want to make inactive and select **Make inactive** from the list.

The **Make parser inactive** dialog appears.

  3. Click **Make inactive**.




The custom parser is deactivated and the current prebuilt parser version is activated after 20 minutes. The prebuilt parser now becomes the default parser.

## Delete a custom parser

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert **Menu** against the custom parser that you want to delete and select **Delete** from the list. Note: You cannot delete a prebuilt parser.

The **Delete custom parser** dialog appears.

  3. Click **Delete**.




The custom parser is deleted and the current prebuilt parser version is activated after 20 minutes.

## Create an extension

Parser extensions provide a flexible way to extend the capabilities of existing custom parsers. They don't replace custom parsers. Instead, they enable the seamless extraction of additional fields from the original raw log into the UDM record. A parser extension is different from a custom parser.

To create a parser extension, see [Using parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions).

## Validation status

The Validation column displays the status of the validation test for either the custom parser or for the parser extension.

  * Parser failed: Custom parser validation failed
  * Parser Validation passed: Custom parser validation successful
  * Skipped: Custom parser is not validated
  * Skipped for Extension: Parser extension is not validated



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
