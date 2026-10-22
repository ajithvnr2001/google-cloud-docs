---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass/
title: The Document Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:41.581567+00:00
---

# The Document Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Document Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `Document` represents a document containing searchable content.

`Document` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `Document` is defined as follows:

class Document(doc_id=None, fields=None, language='en', rank=None)
    

Construct an instance of class `Document`.

The following example shows how to create a document consisting of a set of fields, some plain text and one in HTML:
    
    
    from google.appengine.api import search
    
    search.Document(
        doc_id='documentId',
        fields=[search.TextField(name='subject', value='going for dinner'),
                search.HtmlField(name='body', value='<html>I found a place.</html>'),
                search.TextField(name='signature', value='brzydka pogoda', language='pl')],
        language='en')

    

Arguments

doc_id
    

The _document identifier,_ a human-readable ASCII string identifying the document. Must contain no whitespace characters and not start with an exclamation point (`!`). If omitted, the search service will provide an identifier string.

In most cases, you do not need to specify the document identifier explicitly. Specifying your own identifier is useful, however, for implementing search with other storage mechanisms, such as Blobstore or Google Storage. In the case of Blobstore, for example, you can set the document identifier to the `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/BlobKey)` in order to associate that document with a specific blob. 

fields
    

An iterable collection of `Field` objects representing the content of the document.

language
    

A two-letter [ISO 693-1](http://www.sil.org/iso639-3/codes.asp?order=639_1&letter=%25) code for the language in which the document's field values are expressed.

rank
    

The document's _rank,_ an integer specifying the order in which it will be returned in search results. Newer documents are returned first. If not specified the rank will be set to the number of seconds since 1 January 2011 00:00:00 UTC. Note that when rank is used in a FieldExpression or SortExpression it is referenced as `_rank`.

Result value

    

A new instance of class `Document`.

Exceptions

TypeError
    

A parameter has an invalid type or an unknown attribute was passed.

ValueError
    

A parameter has an invalid value.

## Properties

An instance of class `Document` has the following properties:

doc_id
    

The document identifier, a human-readable ASCII string identifying the document.

fields
    

A list of the document's [fields](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses).

language
    

The two-letter [ISO 693-1](http://www.sil.org/iso639-3/codes.asp?order=639_1&letter=%25) code for the language in which the document's field values are expressed.

rank
    

The document's rank, an integer specifying the order in which it will be returned in search results. Note that when rank is used in a FieldExpression or SortExpression it is referenced as `_rank`. Also, if you create a SortExpression that includes rank as one of the sort keys, rank can only be sorted in the DESCENDING direction.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
