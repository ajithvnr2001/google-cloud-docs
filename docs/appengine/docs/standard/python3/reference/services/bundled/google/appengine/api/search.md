---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/
title: Module: google.appengine.api.search \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:06:41.691473+00:00
---

# Module: google.appengine.api.search  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.search Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/__init__.py) Search API module.

## Modules

[`expression_parser`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/expression_parser) module: Wrapper for ExpressionParser. [`query_parser`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser) module: Wrapper for QueryParser. [`search`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search) module: A Python Search API used by app developers. [`search_util`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/search_util) module: Provides utility methods used by modules in the FTS API stub. [`unicode_util`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/unicode_util) module: Utility methods related to Unicode.

## Classes

[`class AtomFacet`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/AtomFacet): A Facet that has content to be treated as a single token for indexing. [`class AtomField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/AtomField): A Field that has content to be treated as a single token for indexing. [`class Cursor`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Cursor): Specifies how to get the next page of results in a search. [`class DateField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/DateField): A Field that has a date or datetime value. [`class DeleteError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/DeleteError): Indicates some error occurred deleting one of the objects requested. [`class DeleteResult`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/DeleteResult): The result of deleting a single document. [`class Document`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Document): Represents a user generated document. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Error): Indicates a call on the search API has failed. [`class ExpressionError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/ExpressionError): An error occurred while parsing an expression input string. [`class Facet`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Facet): An abstract base class which represents a facet of a document. [`class FacetOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetOptions): Options for processing facet reults of a query. [`class FacetRange`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetRange): A facet range with start and end values. [`class FacetRefinement`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetRefinement): A Facet Refinement to filter out search results based on a facet value. [`class FacetResult`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetResult): Represents a facet result returned from a search with faceted search. [`class FacetResultValue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetResultValue): A facet value as part of search result. [`class Field`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field): An abstract base class which represents a field of a document. [`class FieldExpression`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FieldExpression): Represents an expression that will be computed for each result returned. [`class GeoField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/GeoField): A Field that has a GeoPoint value. [`class GeoPoint`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/GeoPoint): Represents a point on the Earth's surface, in lat, long coordinates. [`class HtmlField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/HtmlField): A Field that has HTML content. [`class Index`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Index): Represents an index allowing indexing, deleting and searching documents. [`class InternalError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/InternalError): Indicates a call on the search API has failed on the internal backend. [`class MatchScorer`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/MatchScorer): Assigns a document score based on term frequency. [`class NumberFacet`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/NumberFacet): A Facet that has a numeric value. [`class NumberField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/NumberField): A Field that has a numeric value. [`class OperationResult`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/OperationResult): Represents result of individual operation of a batch index or removal. [`class PutError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/PutError): Indicates some error occurred indexing one of the objects requested. [`class PutResult`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/PutResult): The result of indexing a single object. [`class Query`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Query): Represents a request on the search service to query the index. [`class QueryError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/QueryError): An error occurred while parsing a query input string. [`class QueryOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/QueryOptions): Options for post-processing results for a query. [`class RescoringMatchScorer`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/RescoringMatchScorer): Assigns a document score based on term frequency weighted by doc parts. [`class ScoredDocument`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/ScoredDocument): Represents a scored document returned from a search. [`class SearchResults`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SearchResults): Represents the result of executing a search request. [`class SortExpression`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortExpression): Sort by a user specified scoring expression. [`class SortOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortOptions): Represents a multi-dimensional sort of Documents. [`class TextField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/TextField): A Field that has text content. [`class TokenizedPrefixField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/TokenizedPrefixField): A field that matches searches on prefixes of its individual terms. [`class TransientError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/TransientError): Indicates a call on the search API has failed, but retrying may succeed. [`class UntokenizedPrefixField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/UntokenizedPrefixField): A field that matches searches on prefixes of the whole field. [`class VectorField`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/VectorField): A vector field that can be used in a dot product expression.

## Functions

[`get_indexes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/get_indexes): Returns a list of available indexes. [`get_indexes_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/get_indexes_async): Asynchronously returns a list of available indexes. | 

## Other Members  
  
---  
  
DOCUMENT_ID_FIELD_NAME |  `'_doc_id'`  
LANGUAGE_FIELD_NAME |  `'_lang'`  
MAXIMUM_DEPTH_FOR_FACETED_SEARCH |  `10000`  
MAXIMUM_DOCUMENTS_PER_PUT_REQUEST |  `200`  
MAXIMUM_DOCUMENTS_RETURNED_PER_SEARCH |  `1000`  
MAXIMUM_DOCUMENT_ID_LENGTH |  `500`  
MAXIMUM_EXPRESSION_LENGTH |  `5000`  
MAXIMUM_FACETS_TO_RETURN |  `100`  
MAXIMUM_FACET_VALUES_TO_RETURN |  `100`  
MAXIMUM_FIELDS_RETURNED_PER_SEARCH |  `1000`  
MAXIMUM_FIELD_ATOM_LENGTH |  `500`  
MAXIMUM_FIELD_NAME_LENGTH |  `500`  
MAXIMUM_FIELD_PREFIX_LENGTH |  `500`  
MAXIMUM_FIELD_VALUE_LENGTH |  `1048576`  
MAXIMUM_GET_INDEXES_OFFSET |  `1000`  
MAXIMUM_INDEXES_RETURNED_PER_GET_REQUEST |  `1000`  
MAXIMUM_INDEX_NAME_LENGTH |  `100`  
MAXIMUM_NUMBER_FOUND_ACCURACY |  `25000`  
MAXIMUM_QUERY_LENGTH |  `2000`  
MAXIMUM_SEARCH_OFFSET |  `1000`  
MAXIMUM_SORTED_DOCUMENTS |  `10000`  
RANK_FIELD_NAME |  `'_rank'`  
SCORE_FIELD_NAME |  `'_score'`  
TIMESTAMP_FIELD_NAME |  `'_timestamp'`  
VECTOR_FIELD_MAX_SIZE |  `10000`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
