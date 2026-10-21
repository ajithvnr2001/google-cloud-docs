---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-encode-and-decode-rows/
title: Encode and decode rows \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:55:45.392501+00:00
---

# Encode and decode rows  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-encode-and-decode-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Encode and decode rows Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Data Fusion Studio, the Wrangler workspace lets you encode and decode values across your dataset rows. Converting between formats helps you safely handle binary payloads, format URL parameters, and prepare records for downstream processing.

## Encode a row

You can use base encoding of data to store or transfer data in environments that, for legacy reasons, are restricted to US-ASCII data. You might use it in new applications without those legacy restrictions because it allows the manipulation of objects with text editors.

You can apply the following encoding schemes, which are based on [RFC-4648](https://tools.ietf.org/html/rfc4648), to all values in a column:

  * Base32
  * Base64
  * Hex
  * URL



When you encode, Wrangler generates a new column with a name in the following format: `<column>_encode_<type> except for url-encode`.

Cloud Data Fusion uses the following rules for the column values:

  * If the column is `null`, the resulting column is also `null`.
  * If the chosen column isn't found in the row, the row is skipped.
  * If the column value doesn't have a string or byte data type, the transformation fails, and an error displays.



### Supported encoding options

Wrangler supports the following encoding options:

Encode base64
    The **Base64** option adds the `encode64` directive as a transformation step to the recipe and creates a new column with encoded values.
Encode base32
    The **Base32** option adds the `encode32` directive as a transformation step to the recipe and creates a new column with encoded values.
Encode hex
    The **Hex** option adds the `encode_hex` directive as a transformation step to the recipe and creates a new column with encoded values.
Encode URL
    The **URL** option adds the `url-encode` directive as a transformation step to the recipe and encodes the current column.

## Decode a row

You can use base decoding of data to store or transfer data in environments that, for legacy reasons, are restricted to US-ASCII data. You might use it in new applications without those legacy restrictions because it allows the manipulation of objects with text editors.

You can apply the following decoding schemes, which are based on [RFC-4648](https://tools.ietf.org/html/rfc4648), to each value in a column:

  * Base32
  * Base64
  * Hex
  * URL



When you decode, Wrangler generates a new column with a name in the following format: `<column>_encode_<type>`, except for `url-decode`.

Cloud Data Fusion uses the following rules for the column values:

  * If the column is `null`, the resulting column is also `null`.
  * If the chosen column isn't found in the row, the row is skipped.
  * If the column value doesn't contain the string or byte array data types, the operation fails.



### Supported decoding options

Wrangler supports the following encoding options:

Decode base64
    The **base64** option adds the `decode64` directive as a transformation step to the recipe and creates a new column with the decoded values.
Decode base32
    The **base32** option adds the `decode32` directive as a transformation step to the recipe and creates a new column with the decoded values.
Decode hex
    The **Hex** option adds the `decode hex` directive as a transformation step to the recipe and creates a new column with the decoded values.
Decode URL
    The **URL** option adds the `url-decode` directive as a transformation step to the recipe and decodes the current column.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
