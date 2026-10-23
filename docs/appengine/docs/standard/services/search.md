---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/
title: Search API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:23.238873+00:00
---

# Search API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Search API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The Search API provides a model for indexing documents that contain structured data. You can search an index, and organize and present search results. The API supports full text matching on string fields. Documents and indexes are saved in a separate persistent store optimized for search operations. The Search API can index any number of documents. The App Engine Datastore may be more appropriate for applications that need to retrieve very large result sets.

## Overview

The Search API is based on four main concepts: documents, indexes, queries, and results.

### Documents

A document is an object with a unique ID and a list of fields containing user data. Each field has a name and a type. There are several types of fields, identified by the kinds of values they contain:

  * Atom Field - an indivisible character string.
  * Text Field - a plain text string that can be searched word by word.
  * HTML Field - a string that contains HTML markup tags, only the text outside the markup tags can be searched.
  * Number Field - a floating point number. 
  * Date Field - a date object with year/month/day and optional time.
  * Geopoint Field - a data object with latitude and longitude coordinates.



The maximum size of a document is 1 MB.

### Indexes

An index stores documents for retrieval. You can retrieve a single document by its ID, a range of documents with consecutive IDs, or all the documents in an index. You can also search an index to retrieve documents that satisfy given criteria on fields and their values, specified as a query string. You can manage groups of documents by putting them into separate indexes.

There is no limit to the number of documents in an index or the number of indexes you can use. The total size of all the documents in a single index is limited to 10GB by default. Those with the [App Engine Admin](https://docs.cloud.google.com/appengine/docs/standard/roles#appengine.serviceAdmin) role can submit a request from the Google Cloud console [App Engine Search](https://console.cloud.google.com/appengine/search) page to increase the size up to 200GB.

### Queries

To search an index, you construct a query, which has a query string and possibly some additional options. A query string specifies conditions for the values of one or more document fields. When you search an index you get back only those documents in the index with fields that satisfy the query.

The simplest query, sometimes called a "global search" is a string that contains only field values. This search uses a string that searches for documents that contain the words "rose" and "water":
    
    
    def simple_search(index):
        index.search('rose water')

This one searches for documents with date fields that contain the date July 4, 1776, or text fields that include the string "1776-07-04":
    
    
    def search_date(index):
        index.search('1776-07-04')

A query string can also be more specific. It can contain one or more terms, each naming a field and a constraint on the field's value. The exact form of a term depends on the type of the field. For instance, assuming there is a text field called "product", and a number field called "price", here's a query string with two terms:
    
    
    def search_terms(index):
        # search for documents with pianos that cost less than $5000
        index.search("product = piano AND price < 5000")

Query options, as the name implies, are not required. They enable a variety of features:

  * Control how many documents are returned in the search results.
  * Specify what document fields to include in the results. The default is to include all the fields from the original document. You can specify that the results only include a subset of fields (the original document is not affected).
  * Sort the results.
  * Create "computed fields" for documents using [`FieldExpressions`](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#writing_expressions) and abridged text fields using [snippets](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#snippets).
  * Support paging through the search results by returning only a portion of the matched documents on each query (using offsets and cursors)



We recommend logging query strings in your application if you wish to keep a record of queries that have been executed.

### Search results

A call to `search()` can only return a limited number of matching documents. Your search may find more documents than can be returned in a single call. Each search call returns an instance of the [`SearchResults`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass) class, which contains information about how many documents were found and how many were returned, along with the list of returned documents. You can repeat the same search, using [cursors](https://docs.cloud.google.com/appengine/docs/standard/services/search/results#Using_cursors) or [offsets](https://docs.cloud.google.com/appengine/docs/standard/services/search/results#Using_offsets) to retrieve the complete set of matching documents. 

### Additional training material

In addition to this documentation, you can read the [two-part training class](https://docs.cloud.google.com/appengine/training/fts_intro) on the Search API at the Google Developer's Academy. The class includes a sample Python application.

## Documents and fields

The [`Document`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass) class represents documents. Each document has a _document identifier_ and a list of _fields_. 

### Document identifier

Every document in an index must have a unique document identifier, or ` doc_id `. The identifier can be used to retrieve a document from an index without performing a search. By default, the Search API automatically generates a ` doc_id ` when a document is created. You can also specify the ` doc_id ` yourself when you create a document. A ` doc_id ` must contain only visible, printable ASCII characters (ASCII codes 33 through 126 inclusive) and be no longer than 500 characters. A document identifier cannot begin with an exclamation point ('!'), and it can't begin and end with double underscores ("__").

While it is convenient to create readable, meaningful unique document identifiers, you cannot include the ` doc_id ` in a search. Consider this scenario: You have an index with documents that represent parts, using the part's serial number as the ` doc_id `. It will be very efficient to retrieve the document for any single part, but it will be impossible to search for a range of serial numbers along with other field values, such as purchase date. Storing the serial number in an atom field solves the problem.

### Document fields

A document contains fields that have a _name_ , a _type_ , and a single _value_ of that type. Two or more fields can have the same name, but different types. For instance, you can define two fields with the name "age": one with a text type (the value "twenty-two"), the other with a number type (value 22).

#### Field names

Field names are case sensitive and can only contain ASCII characters. They must start with a letter and can contain letters, digits, or underscore. A field name cannot be longer than 500 characters.

#### Multi-valued fields

A field can contain only one value, which must match the field's type. Field names do not have to be unique. A document can have multiple fields with the same name and same type, which is a way to represent a field with multiple values. (However, date and number fields with the same name can't be repeated.) A document can also contain multiple fields with the same name and _different_ field types.

#### Field types

There are three kinds of fields that store character strings; collectively we refer to them as _string fields_ :

  * Text Field: A string with maximum length 1024**2 characters.
  * HTML Field: An HTML-formatted string with maximum length 1024**2 characters.
  * Atom Field: A string with maximum length 500 characters.



There are also three field types that store non-textual data:

  * Number Field: A double precision floating point value between -2,147,483,647 and 2,147,483,647. 
  * Date Field: A `datetime.date` or `datetime.datetime` . 
  * Geopoint Field: A point on earth described by latitude and longitude coordinates.



The field types are specified by the classes [`TextField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#TextField), [`HtmlField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#HtmlField), [`AtomField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#AtomField), [`NumberField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#NumberField), [`DateField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#DateField), and [`GeoField`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses#GeoField).

### Special treatment of string and date fields

When a document with date , text, or HTML fields is added to an index, some special handling occurs. It's helpful to understand what's going on "under the hood" in order to use the Search API effectively.

#### Tokenizing string fields

When an HTML or text field is indexed, its contents are _tokenized_. The string is split into tokens wherever whitespace or special characters (punctuation marks, hash sign, backslash, etc.) appear. The index will include an entry for each token. This enables you to search for keywords and phrases comprising only part of a field's value. For instance, a search for "dark" will match a document with a text field containing the string "it was a dark and stormy night", and a search for "time" will match a document with a text field containing the string "this is a real-time system".

In HTML fields, text within markup tags is not tokenized, so a document with an HTML field containing `it was a <strong>dark</strong> night` will match a search for "night", but not for "strong". If you want to be able to search markup text, store it in a text field.

Atom fields are not tokenized. A document with an atom field that has the value "bad weather" will only match a search for the entire string "bad weather". It will not match a search for "bad" or "weather" alone.

##### Tokenizing Rules

  * The underscore (_) and ampersand (&) characters do not break words into tokens.

  * These whitespace characters always break words into tokens: space, carriage return, line feed, horizontal tab, vertical tab, form feed, and NULL.

  * These characters are treated as punctuation, and will break words into tokens:

!| "| %| (| )  
---|---|---|---|---  
*| ,| -| || /  
[| ]| ^| `| :  
=| >| ?| @| {  
}| ~| $| |   
  * The characters in the following table _usually_ break words into tokens, but they can be handled differently depending on the context in which they appear:

Character | Rule  
---|---  
`<` | In an HTML field the "less than" sign indicates the start of an HTML tag which is ignored.  
`+` | A string of one or more "plus" signs is treated as a part of the word if it appears at the end of the word (C++).  
`#` | The "hash" sign is treated as a part of the word if it is preceded by a, b, c, d, e, f, g, j, or x (a# - g# are musical notes; j# and x# are programming language, c# is both.) If a term is _preceded_ by '#' (#google), it is treated as a hashtag and the hash becomes part of the word.  
`'` | Apostrophe is a letter if it precedes the letter "s" followed by a word-break, as in "John's hat".  
`.` | If a decimal point appears between digits, this is part of a number (i.e., the decimal-separator). This can also be part of a word if used in an acronym (A.B.C).  
`-` | The dash is part of a word if used in an acronym (I-B-M).  
  * All other 7-bit characters other than letters and digits ('A-Z', 'a-z', '0-9') are handled as punctuation and break words into tokens.

  * Everything else is parsed as a UTF-8 character.


**Note:** Non-western languages, like Japanese and Chinese, use other tokenization rules.

##### Acronyms

Tokenization uses special rules to recognize acronyms (strings like "I.B.M.", "a-b-c", or "C I A"). An acronym is a string of single alphabetic characters, with the same separator character between all of them. The valid separators are the period, dash, or any number of spaces. The separator character is removed from the string when an acronym is tokenized. So the example strings mentioned above become the tokens "ibm", "abc", and "cia". The original text remains in the document field.

When dealing with acronyms, note that:

  * An acronym cannot contain more than 21 letters. A valid acronym string with more than 21 letters will be broken into a series of acronyms, each 21 letters or less.
  * If the letters in an acronym are separated by spaces, all the letters must be the same case. Acronyms constructed with period and dash can use mixed case letters.
  * When searching for an acronym, you can enter the canonical form of the acronym (the string without any separators), or the acronym punctuated with either the dash or the dot (but not both) between its letters. So the text "I.B.M" could be retrieved with any of the search terms "I-B-M", "I.B.M", or "IBM".



#### Date field accuracy

When you create a date field in a document you set its value to a `datetime.date` or `datetime.datetime` . Note that only Python ["naive"](https://docs.python.org/2/library/datetime.html) date and time objects can be used. "Aware" objects are not allowed. For the purpose of indexing and searching the date field, any time component is ignored and the date is converted to the number of days since 1/1/1970 UTC. This means that even though a date field can contain a precise time value a date query can only specify a date field value in the form `yyyy-mm-dd`. This also means the sorted order of date fields with the same date is not well-defined. 

### Other document properties

The _rank_ of a document is a positive integer which determines the default ordering of documents returned from a search. By default, the rank is set at the time the document is created to the number of seconds since January 1, 2011\. You can set the rank explicitly when you create a document. It's a bad idea to assign the same rank to many documents, and you should never give more than 10,000 documents the same rank.

If you specify [sort options](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#SortOptions), you can use the rank as a sort key. Note that when rank is used in a [sort expression](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#sort-multiple-keys) or [field expression](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#FieldExpressions) it is referenced as `_rank`.

The language property specifies the language in which the fields are encoded.

See the [`Document`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass) class reference page for more details about these attributes.

### Linking from a document to other resources

You can use a document's ` doc_id ` and other fields as links to other resources in your application. For example, if you use [Blobstore](https://docs.cloud.google.com/appengine/docs/standard/services/blobstore) you can associate the document with a specific blob by setting the ` doc_id ` or the value of an Atom field to the BlobKey of the data.

## Creating a document

The following code sample shows how to create a document object. The Document constructor is called with the fields argument set to a list of field objects. Each object in the list is created and initialized by using the constructor function of the field's class. Note the use of the [`GeoPoint`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/geopointclass) constructor and the Python `datetime` class to create the appropriate types of field values.
    
    
    def create_document():
        document = search.Document(
            # Setting the doc_id is optional. If omitted, the search service will
            # create an identifier.
            doc_id='PA6-5000',
            fields=[
                search.TextField(name='customer', value='Joe Jackson'),
                search.HtmlField(
                    name='comment', value='this is <em>marked up</em> text'),
                search.NumberField(name='number_of_visits', value=7),
                search.DateField(name='last_visit', value=datetime.now()),
                search.DateField(
                    name='birthday', value=datetime(year=1960, month=6, day=19)),
                search.GeoField(
                    name='home_location', value=search.GeoPoint(37.619, -122.37))
            ])
        return document

Note: When you create a document you must specify all of its attributes using the [`Document constructor`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass#Constructor) class method. You cannot add, remove, or delete fields, nor change the identifier or any other attribute once the document has been created. Date and geopoint fields must be assigned a non-null value. Atom, text, HTML, and number fields can be empty. 

## Working with an index

### Putting documents in an index

When you put a document into an index, the document is copied to persistent storage and each of its fields is indexed according to its name, type, and the ` doc_id `.

The following code example shows how to access an Index and put a document into it.
    
    
    def add_document_to_index(document):
        index = search.Index('products')
        index.put(document)

You can pass up to 200 documents at a time to the `put()` method. Batching puts is more efficient than adding documents one at a time. 

When you put a document into an index and the index already contains a document with the same ` doc_id `, the new document replaces the old one. No warning is given. You can call [`Index.get(id)`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_get) before creating or adding a document to an index to check whether a specific ` doc_id ` already exists.

The `put` method returns a list of [`PutResults`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/PutResult), one for each document passed as an argument. If you did not specify the ` doc_id ` yourself, you can examine the `id` attribute of the result to discover the ` doc_id ` that was generated:
    
    
    def add_document_and_get_doc_id(documents):
        index = search.Index('products')
        results = index.put(documents)
        document_ids = [document.id for document in results]
        return document_ids

Note that creating an instance of the `Index` class does not guarantee that a persistent index actually exists. A persistent index is created the first time you add a document to it with the `put` method. If you want to check whether or not an index actually exists before you start to use it, use the [`search.get_indexes()`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions) function .

#### Updating documents

A document cannot be changed once you've added it to an index. You can't add or remove fields, or change a field's value. However, you can replace the document with a new document that has the same ` doc_id `.

### Retrieving documents by doc_id 

There are two ways to retrieve documents from an index using document identifiers:

  * Use [`Index.get()`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_get) to fetch a single document by its ` doc_id `.
  * Use [`Index.get_range()`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_get_range) to retrieve a group of consecutive documents ordered by ` doc_id `.



Each call is demonstrated in the example below.
    
    
    def get_document_by_id():
        index = search.Index('products')
    
        # Get a single document by ID.
        document = index.get("AZ125")
    
        # Get a range of documents starting with a given ID.
        documents = index.get_range(start_id="AZ125", limit=100)
    
        return document, documents

### Searching for documents by their contents

To retrieve documents from an index, you construct a query string and call `Index.search()`. The query string can be passed directly as the argument, or you can include the string in a [Query](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass) object which is passed as the argument. By default, `search()` returns matching documents sorted in order of decreasing rank. To control how many documents are returned, how they are sorted, or add computed fields to the results, you need to use a `Query` object, which contains a query string and can also specify other search and sorting options.
    
    
    def query_index():
        index = search.Index('products')
        query_string = 'product: piano AND price < 5000'
    
        results = index.search(query_string)
    
        for scored_document in results:
            print(scored_document)

### Deleting an index

Each index consists of its indexed documents and an index schema. To delete an index, delete all the documents in the index and then delete the index schema.

You can delete documents in an index by specifying the ` doc_id ` of one or more documents you wish to delete to the [Index.delete()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_delete) method.
    
    
    def delete_index(index):
        # index.get_range by returns up to 100 documents at a time, so we must
        # loop until we've deleted all items.
        while True:
            # Use ids_only to get the list of document IDs in the index without
            # the overhead of getting the entire document.
            document_ids = [
                document.doc_id
                for document
                in index.get_range(ids_only=True)]
    
            # If no IDs were returned, we've deleted everything.
            if not document_ids:
                break
    
            # Delete the documents for the given IDs
            index.delete(document_ids)
    
        # delete the index schema
        index.delete_schema()

You can pass up to 200 documents at a time to the `delete()` method. Batching deletes is more efficient than handling them one at a time.

To delete all Search API data, iterate over all indexes in all namespaces and use the above instructions for each to delete the documents and index schema.

This approach might take a long time if you need to delete a large number of search index entries. To resolve this issue, try the following:

  1. Delete the project and its dependencies.
  2. Request a [higher quota](https://docs.cloud.google.com/appengine/docs/standard/quotas#search) for faster deletions.



### Eventual consistency

When you put, update, or delete a document in an index, the change propagates across multiple data centers. This usually happens quickly, but the time it takes can vary. The Search API guarantees [eventual consistency](http://en.wikipedia.org/wiki/Eventual_consistency). This means that in some cases, a search or a retrieval of one or more documents might return results that do not reflect the most recent changes.

### Determining the size of an index

An index stores documents for retrieval. You can retrieve a single document by its ID, a range of documents with consecutive IDs, or all the documents in an index. You can also search an index to retrieve documents that satisfy given criteria on fields and their values, specified as a query string. You can manage groups of documents by putting them into separate indexes. There is no limit to the number of documents in an index or the number of indexes you can use. The total size of all the documents in a single index is limited to 10GB by default but can be increased to up to 200GB by submitting a request from the Google Cloud console [App Engine Search](https://console.cloud.google.com/appengine/search) page. The index property [`storage_limit`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_storage_limit) is the maximum allowable size of an index.

The index property [`storage_usage`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_storage_usage) is an estimate of the amount of storage space used by an index. This number is an estimate because the index monitoring system does not run continuously; the actual usage is computed periodically. The `storage_usage` is adjusted between sampling points by accounting for document additions, but not deletions.

### Performing asynchronous operations

You can use asynchronous calls to execute multiple operations without blocking, and then retrieve all the results at the same time, blocking only once. For example, the following code executes multiple searches asynchronously:
    
    
    def async_query(index):
        futures = [index.search_async('foo'), index.search_async('bar')]
        results = [future.get_result() for future in futures]
        return results

## Index schemas

Every index has a schema that shows all the field names and field types that appear in the documents it contains. You cannot define a schema yourself. Schemas are maintained dynamically; they are updated as documents are added to an index. A simple schema might look like this, in JSON-like form:
    
    
    {'comment': ['TEXT'], 'date': ['DATE'], 'author': ['TEXT'], 'count': ['NUMBER']}
    

Each key in the dictionary is the name of a document field. The key's value is a list of the field types used with that field name. If you have used the same field name with different field types the schema will list more than one field type for a field name, like this:
    
    
    {'ambiguous-integer': ['TEXT', 'NUMBER', 'ATOM']}
    

Once a field appears in a schema it can never be removed. There is no way to delete a field, even if the index no longer contains any documents with that particular field name.

You can view the schemas for your indexes like this:
    
    
    from google.appengine.api import search
    ...
    for index in search.get_indexes(fetch_schema=True):
        logging.info("index %s", index.name)
        logging.info("schema: %s", index.schema)
    

By default, only indexes in the current namespace are retrieved. To retrieve indexes from all namespaces, use the `all_namespaces` parameter. 

Note that a call to [`get_indexes`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions) cannot return more than 1000 indexes. To retrieve more indexes, call the function repeatedly using the `start_index_name` argument. 

A schema does not define a "class" in the object-programming sense. As far as the Search API is concerned, every document is unique and indexes can contain different kinds of documents. If you want to treat collections of objects with the same list of fields as instances of a class, that's an abstraction you must enforce in your code. For instance, you could ensure that all documents with the same set of fields are kept in their own index. The index schema could be seen as the class definition, and each document in the index would be an instance of the class.

### Viewing indexes in the Google Cloud console

In the Google Cloud console, you can [view information about your application's indexes and the documents they contain](https://console.cloud.google.com/appengine/search). Clicking an index name displays the documents that index contains. You'll see all the defined schema fields for the index; for each document with a field of that name, you'll see the field's value. You can also issue queries on the index data directly from the console.

### Search API quotas

The Search API has several free quotas:

Resource or API call | Free Quota  
---|---  
Total storage (documents and indexes) | 0.25 GB  
Queries | 1000 queries per day  
Adding documents to indexes | 0.01 GB per day  
  
The Search API imposes these limits to ensure the reliability of the service. These apply to both free and paid apps:

Resource | Safety Quota  
---|---  
Maximum query usage | 100 aggregated minutes of query execution time per minute  
Maximum documents added or deleted  | 15,000 per minute  
Maximum size per index (unlimited number of indexes allowed) | 10 GB  
  
API usage is counted in different ways depending on the type of call:

  * `Index.search()`: Each API call counts as one query; execution time is equivalent to the latency of the call.
  * `Index.put()`: When you add documents to indexes the size of each document and the number of documents counts towards the indexing quota.
  * All other Search API calls are counted based on the number of operations they involve: 
    * `search.get_indexes()`: 1 operation is counted for each index actually returned, or 1 operation if nothing is returned.
    * `Index.get()` and `Index.get_range()`: 1 operation counted for each document actually returned, or 1 operation if nothing is returned.
    * `Index.delete()`: 1 operation counted for each document in the request, or 1 operation if the request is empty.



The quota on query throughput is imposed so that a single user cannot monopolize the search service. Because queries can execute simultaneously, each application is allowed to run queries that consume up to 100 minutes of execution time per one minute of clock time. If you are running many short queries, you probably will not reach this limit. Once you exceed the quota, subsequent queries will fail until the next time slice, when your quota is restored. The quota is not strictly imposed in one minute slices; a variation of the [leaky bucket](https://wikipedia.org/wiki/Leaky_bucket) algorithm is used to control search bandwidth in five second increments.

More information on quotas can be found on the [Quotas](https://docs.cloud.google.com/appengine/docs/quotas) page. When an app tries to exceed these amounts, an insufficient quota error is returned.

Note that although these limits are enforced by the minute, the console displays the daily totals for each. Customers with [Standard, Enhanced, or Premium support](https://docs.cloud.google.com/support) can request higher throughput limits by contacting their support representative.

## Search API pricing

The following charges are applied to usage beyond the free quotas:

Resource | Cost  
---|---  
Total storage (documents and indexes) | $0.18 per GB per month  
Queries | $0.50 per 10K queries  
Indexing searchable documents | $2.00 per GB  
  
Additional information on pricing is on the [Pricing](https://cloud.google.com/appengine/pricing) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
