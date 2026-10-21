---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/
title: Module: google.appengine.api.search.search_util \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:01:40.812548+00:00
---

# Module: google.appengine.api.search.search_util  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.search.search_util Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search_util.py) Provides utility methods used by modules in the FTS API stub.

## Classes

[`class UnsupportedOnDevError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/UnsupportedOnDevError): Indicates attempt to perform an action unsupported on the dev server.

## Functions

[`AddFieldsToDocumentPb(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/AddFieldsToDocumentPb): Add the id and fields to document. [`ConvertToNfkd(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/ConvertToNfkd) [`DeserializeDate(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/DeserializeDate) [`EpochTime(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/EpochTime): Returns millisecond epoch time for a date or datetime. [`GetAllFieldInDocument(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/GetAllFieldInDocument): Find and return all fields with the provided name in the document. [`GetFieldCountInDocument(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/GetFieldCountInDocument) [`GetFieldInDocument(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/GetFieldInDocument): Find and return the field with the provided name and type. [`RemoveAccents(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/RemoveAccents) [`RemoveAccentsNfkd(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/RemoveAccentsNfkd) [`Repr(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/Repr): Generates an unambiguous representation for instance and ordered dict. [`SerializeDate(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/SerializeDate) [`TreeRepr(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util/TreeRepr): Generate a string representation of an ANTLR parse tree for debugging. | 

## Other Members  
  
---  
  
BASE_DATE |  Instance of [`google.appengine.ext.db.DateTimeProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type)  
DEFAULT_MAX_SNIPPET_LENGTH |  `160`  
EXPRESSION_RETURN_TYPE_NUMERIC |  `2`  
EXPRESSION_RETURN_TYPE_TEXT |  `1`  
NUMBER_DOCUMENT_FIELD_TYPES |  `[4]`  
TEXT_DOCUMENT_FIELD_TYPES |  `[2, 0, 1, 6, 7]`  
TEXT_QUERY_TYPES |  `[13, 32]`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
