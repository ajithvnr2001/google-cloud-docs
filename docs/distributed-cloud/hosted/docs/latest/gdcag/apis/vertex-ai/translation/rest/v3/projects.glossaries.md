---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries
title: REST Resource: projects.glossaries \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:48.324383+00:00
---

# REST Resource: projects.glossaries  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  REST Resource: projects.glossaries Stay organized with collections  Save and categorize content based on your preferences. 

Important: To access the URL listed within parentheses, you must connect to the internet. The URL is provided to access outside of your air-gapped environment. 

## Resource: Glossary

Represents a glossary built from user provided data.

JSON representation  
---  
      
    
    {
      "name": string,
      "input_config": {
        object ([GlossaryInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#GlossaryInputConfig))
      },
      "entry_count": integer,
      "submit_time": string,
      "end_time": string,
      "display_name": string,
    
      // Union field languages can be only one of the following:
      "language_pair": {
        object ([LanguageCodePair](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#LanguageCodePair))
      },
      "language_codes_set": {
        object ([LanguageCodesSet](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#LanguageCodesSet))
      }
      // End of list of possible types for union field languages.
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the glossary. Glossary names have the form `projects/{project-id}/glossaries/{glossary-id}`.  
`input_config` |  `object (`[GlossaryInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#GlossaryInputConfig)`)` Required. Provides examples to build the glossary from. Total glossary must not exceed 10M Unicode codepoints.  
`entry_count` |  `integer` Output only. The number of entries defined in the glossary.  
`submit_time` |  `string (`Timestamp (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. When glossaries.create was called.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`end_time` |  `string (`Timestamp (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. When the glossary creation was finished.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`display_name` |  `string` Optional. The display name of the glossary.  
Union field `languages`. Languages supported by the glossary. `languages` can be only one of the following:  
`language_pair` |  `object (`[LanguageCodePair](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#LanguageCodePair)`)` Used with unidirectional glossaries.  
`language_codes_set` |  `object (`[LanguageCodesSet](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#LanguageCodesSet)`)` Used with equivalent term set glossaries.  
  
## LanguageCodePair

Used with unidirectional glossaries.

JSON representation  
---  
      
    
    {
      "source_language_code": string,
      "target_language_code": string
    }  
  
Fields  
---  
`source_language_code` |  `string` Required. The BCP-47 language code of the input text, for example, "en-US". Expected to be an exact match for GlossaryTerm.language_code.  
`target_language_code` |  `string` Required. The BCP-47 language code for translation output, for example, "zh-CN". Expected to be an exact match for GlossaryTerm.language_code.  
  
## LanguageCodesSet

Used with equivalent term set glossaries.

JSON representation  
---  
      
    
    {
      "language_codes": [
        string
      ]
    }  
  
Fields  
---  
`language_codes[]` |  `string` The BCP-47 language code(s) for terms defined in the glossary. All entries are unique. The list contains at least two entries. Expected to be an exact match for GlossaryTerm.language_code.  
  
## GlossaryInputConfig

Input configuration for glossaries.

JSON representation  
---  
      
    
    {
      "s3_source": {
        object ([S3Source](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#GcsSource))
      }
    }  
  
Fields  
---  
`s3_source` |  `object (`[S3Source](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries#GcsSource)`)` Required. Storage location of glossary data. File format is determined based on the filename extension. API returns `google.rpc.Code.INVALID_ARGUMENT` for unsupported URI-s and file formats. Wildcards aren't allowed. This must be a single file in one of the following formats:For unidirectional glossaries:

  * TSV/CSV (`.tsv`/`.csv`): 2 column file, tab- or comma-separated. The first column is source text. The second column is target text. The file must not contain headers. That is, the first row is data, not column names.
  * TMX (`.tmx`): TMX file with parallel data defining source/target term pairs.

For equivalent term sets glossaries:

  * CSV (`.csv`): Multi-column CSV file defining equivalent glossary terms in multiple languages. See documentation for more information - glossaries (https://cloud.google.com/translate/docs/advanced/glossary).

  
  
## S3Source

The storage location for the input content.

JSON representation  
---  
      
    
    {
      "input_uri": string
    }  
  
Fields  
---  
`input_uri` |  `string` Required. Source data URI. For example, `s3://my_bucket/my_object`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/create)`

|  Creates a glossary and returns the long-running operation.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/delete)`

|  Deletes a glossary if the glossary hasn't been created.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/get)`

|  Gets a glossary.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/list)`

|  Lists glossaries in a project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
