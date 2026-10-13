---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v3/latest/Google-Cloud-Translate-V3-InputConfig/
title: Cloud Translation V3 API - Class Google::Cloud::Translate::V3::InputConfig (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:39.145945+00:00
---

# Cloud Translation V3 API - Class Google::Cloud::Translate::V3::InputConfig (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v3/latest/Google-Cloud-Translate-V3-InputConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Translation V3 API - Class Google::Cloud::Translate::V3::InputConfig (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.2  0.10.0  0.9.0  0.8.0  0.7.3  0.6.0  0.5.2  0.4.2 

Reference documentation and code samples for the Cloud Translation V3 API class Google::Cloud::Translate::V3::InputConfig.

Input configuration for BatchTranslateText request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #gcs_source
    
    
    def gcs_source() -> ::Google::Cloud::Translate::V3::GcsSource

**Returns**

  * ([::Google::Cloud::Translate::V3::GcsSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v3/latest/Google-Cloud-Translate-V3-GcsSource)) — Required. Google Cloud Storage location for the source input. This can be a single file (for example, `gs://translation-test/input.tsv`) or a wildcard (for example, `gs://translation-test/*`). If a file extension is `.tsv`, it can contain either one or two columns. The first column (optional) is the id of the text request. If the first column is missing, we use the row number (0-based) from the input file as the ID in the output file. The second column is the actual text to be translated. We recommend each row be <= 10K Unicode codepoints, otherwise an error might be returned. Note that the input tsv must be RFC 4180 compliant.

You could use https://github.com/Clever/csvlint to check potential formatting errors in your tsv file. csvlint --delimiter='\t' your_input_file.tsv

The other supported file extensions are `.txt` or `.html`, which is treated as a single large chunk of text. 




### #gcs_source=
    
    
    def gcs_source=(value) -> ::Google::Cloud::Translate::V3::GcsSource

**Parameter**

  * **value** ([::Google::Cloud::Translate::V3::GcsSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v3/latest/Google-Cloud-Translate-V3-GcsSource)) — Required. Google Cloud Storage location for the source input. This can be a single file (for example, `gs://translation-test/input.tsv`) or a wildcard (for example, `gs://translation-test/*`). If a file extension is `.tsv`, it can contain either one or two columns. The first column (optional) is the id of the text request. If the first column is missing, we use the row number (0-based) from the input file as the ID in the output file. The second column is the actual text to be translated. We recommend each row be <= 10K Unicode codepoints, otherwise an error might be returned. Note that the input tsv must be RFC 4180 compliant.

You could use https://github.com/Clever/csvlint to check potential formatting errors in your tsv file. csvlint --delimiter='\t' your_input_file.tsv

The other supported file extensions are `.txt` or `.html`, which is treated as a single large chunk of text. 




**Returns**

  * ([::Google::Cloud::Translate::V3::GcsSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v3/latest/Google-Cloud-Translate-V3-GcsSource)) — Required. Google Cloud Storage location for the source input. This can be a single file (for example, `gs://translation-test/input.tsv`) or a wildcard (for example, `gs://translation-test/*`). If a file extension is `.tsv`, it can contain either one or two columns. The first column (optional) is the id of the text request. If the first column is missing, we use the row number (0-based) from the input file as the ID in the output file. The second column is the actual text to be translated. We recommend each row be <= 10K Unicode codepoints, otherwise an error might be returned. Note that the input tsv must be RFC 4180 compliant.

You could use https://github.com/Clever/csvlint to check potential formatting errors in your tsv file. csvlint --delimiter='\t' your_input_file.tsv

The other supported file extensions are `.txt` or `.html`, which is treated as a single large chunk of text. 




### #mime_type
    
    
    def mime_type() -> ::String

**Returns**

  * (::String) — Optional. Can be "text/plain" or "text/html". For `.tsv`, "text/html" is used if mime_type is missing. For `.html`, this field must be "text/html" or empty. For `.txt`, this field must be "text/plain" or empty. 



### #mime_type=
    
    
    def mime_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Can be "text/plain" or "text/html". For `.tsv`, "text/html" is used if mime_type is missing. For `.html`, this field must be "text/html" or empty. For `.txt`, this field must be "text/plain" or empty. 



**Returns**

  * (::String) — Optional. Can be "text/plain" or "text/html". For `.tsv`, "text/html" is used if mime_type is missing. For `.html`, this field must be "text/html" or empty. For `.txt`, this field must be "text/plain" or empty. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
