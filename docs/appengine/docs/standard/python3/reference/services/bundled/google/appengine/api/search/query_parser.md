---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/
title: Module: google.appengine.api.search.query_parser \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:56:36.068750+00:00
---

# Module: google.appengine.api.search.query_parser  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.search.query_parser Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/query_parser.py) Wrapper for QueryParser.

## Classes

[`class QueryException`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryException): An error occurred while parsing the query input string. [`class QueryLexerWithErrors`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryLexerWithErrors): An overridden Lexer that raises exceptions. [`class QueryParserWithErrors`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryParserWithErrors): An overridden Parser that raises exceptions. [`class QueryTreeException`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryTreeException): An error occurred while analyzing the parse tree.

## Functions

[`ConvertNodes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/ConvertNodes): Converts nodes of type from_type to nodes of type to_type. [`CreateParser(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/CreateParser): Creates a Query Parser. [`CreateQueryNode(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/CreateQueryNode) [`GetPhraseQueryNodeText(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/GetPhraseQueryNodeText): Returns the text from a query node. [`GetQueryNodeText(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/GetQueryNodeText): Returns the text from the node, handling that it could be unicode. [`GetQueryNodeTextUnicode(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/GetQueryNodeTextUnicode): Returns the unicode text from node. [`IsPhrase(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/IsPhrase): Return true if node is the root of a text phrase. [`Parse(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/Parse): Parses a query and returns an ANTLR tree. [`ParseAndSimplify(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/ParseAndSimplify): Parses a query and performs all necessary transformations on the tree. [`RemoveSurroundingQuotes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/RemoveSurroundingQuotes): Removes outer quotation marks, if present. [`SequenceToConjunction(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/SequenceToConjunction): Transform all SEQUENCE nodes into CONJUNCTION nodes. [`Simplify(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/Simplify): Simplifies the output of the parser. [`SimplifyNode(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/SimplifyNode) [`ValidateNode(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/ValidateNode) | 

## Other Members  
  
---  
  
COMPARISON_TYPES |  `[22, 23, 21, 20, 19, 18, 17]`  
QUERY_FUNCTION_NAMES | 
    
    
    {
     'distance',
     'geopoint'
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
