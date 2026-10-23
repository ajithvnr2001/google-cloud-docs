---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/options/
title: Query and sorting options \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:05.544378+00:00
---

# Query and sorting options  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Query and sorting options Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

When you call the `search()` method using a query string alone, the results are returned according to the default query options:

  * Documents are returned sorted in order of descending rank
  * Documents are returned in groups of 20 at a time
  * Retrieved documents contain all of their original fields



You can use an instance of the [`Query`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass) class as the argument to `search()` to change these options.

The Query class allows you to specify how many documents to return at a time. It also lets you customize the contents of the retrieved documents. You can ask for document identifiers only, or request that documents contain only a subset of their fields. You can also create custom fields in the retrieved documents : snippets (fragments of text fields showing the text surrounding a matched string), and field expressions (fields with values derived from other fields in the document).

Apart from the query options, the Query class can also include an instance of the `SortOptions` class. Using sort options you can change the sort order, and sort the results on multiple keys.

## Searching with the Query class

When you search with an instance of the Query class, you need to construct an instance of the class in several steps. This is the general order:

  1. Create a query string.
  2. Create `SortOptions` if needed.
  3. Create `QueryOptions`.
  4. Create a Query object that includes the query string and the (optional) `QueryOptions`.
  5. Call the search method on the Query object.



The `QueryOptions` and `SortOptions` constructors use named arguments, as shown in this example:
    
    
    def query_options():
        index = search.Index('products')
        query_string = "product: piano AND price < 5000"
    
        # Create sort options to sort on price and brand.
        sort_price = search.SortExpression(
            expression='price',
            direction=search.SortExpression.DESCENDING,
            default_value=0)
        sort_brand = search.SortExpression(
            expression='brand',
            direction=search.SortExpression.DESCENDING,
            default_value="")
        sort_options = search.SortOptions(expressions=[sort_price, sort_brand])
    
        # Create field expressions to add new fields to the scored documents.
        price_per_note_expression = search.FieldExpression(
            name='price_per_note', expression='price/88')
        ivory_expression = search.FieldExpression(
            name='ivory', expression='snippet("ivory", summary, 120)')
    
        # Create query options using the sort options and expressions created
        # above.
        query_options = search.QueryOptions(
            limit=25,
            returned_fields=['model', 'price', 'description'],
            returned_expressions=[price_per_note_expression, ivory_expression],
            sort_options=sort_options)
    
        # Build the Query and run the search
        query = search.Query(query_string=query_string, options=query_options)
        results = index.search(query)
        for scored_document in results:
            print(scored_document)

## QueryOptions

These properties control how many results are returned and in what order. The offset and cursor options, which are mutually exclusive, support pagination. They specify which selected documents to return in the results.

Property | Description | Default | Maximum  
---|---|---|---  
` limit ` | The maximum number of documents to return in the results. | 20 | 1000 `number_found_accuracy`  
`offset` | The offset of the first document in the results to return. | 0\. Results will contain all matching documents (up to limit). | 1,000  
`cursor` | A cursor can be used in lieu of an offset to retrieve groups of documents in sorted order. A cursor is updated as it is passed into and out of consecutive queries, allowing each new search to be continued from the end of the previous one. Cursor and offset are discussed on the [Handling Results](https://docs.cloud.google.com/appengine/docs/standard/services/search/results) page. | Null. Results will contain all matching documents (up to limit). | -  
`sort_options` | Set a `SortOptions` object to control the ordering of the search results. An instance of `SortOptions` has its own set of properties which are described below. | Null. Sort by decreasing document rank. | -  
  
These properties control what document fields appear in the results.

Property | Description | Default  
---|---|---  
`ids_only` | Set to ` True ` or ` False `. When ` True `, the documents returned in the results will contain IDs only, no fields. | ` False ` (return all fields).  
`returned_fields` | Specifies which document fields to include in the results. No more than 100 fields can be specified. | Return all document fields (up to 100 fields).  
`returned_expressions` | Field expressions describing computed fields that are added to each document returned in the search results. These fields are added to the expressions property of the document. The field value is specified by writing an expression which may include one or more document fields. | None  
`snippeted_fields` | A list of text field names. A snippet is generated for each field. This is a computed field that is added to the expressions property of the documents in the search results. The snippet field has the same name as its source field.  
  
This option implicitly uses the snippet function with only two arguments, creating a snippet with at most one matching string, based on the same query string that the search used to retrieve the results: `snippet("query-string", field-name)`.  
  
You can also create customized snippets with the `returned_expressions` option by adding a field expression that explicitly calls the snippet function. | None  
  
## SortOptions

The properties of `SortOptions` control the ordering and scoring of the search results.

Property | Description | Default  
---|---|---  
`expressions` | A list of `SortExpressions` representing a multi-dimensional sort of Documents. | None  
`match_scorer` | An optional [`MatchScorer`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/matchscorerclass) object . When present this will cause the documents to be scored according to search term frequency. The score will be available as the `_score` field. Scoring documents can be expensive (in both billable operations and execution time) and can slow down your searches. Use scoring sparingly. | None  
limit  | Maximum number of objects to score and/or sort. Cannot be more than 10,000. | 1,000  
  
### Sorting on multiple keys

You can order the search results on multiple sort keys. Each key can be a simple field name, or a value that is computed from several fields.Note that the term 'expression' is used with multiple meanings when speaking about sort options: The `SortOption` itself has an _expressions attribute_. This attribute is a list of `SortExpression` objects which correspond to sort keys. Finally, each `SortExpression` object contains an _expression attribute_ which specifies how to calculate the value of the sort key. This expression is constructed according to the rules in the next section.

A `SortExpression` also defines the direction of the sort and a default key value to use if the expression cannot be calculated for a document. Here is the complete list of properties:

Property | Description | Default  
---|---|---  
`expression` | An expression to be evaluated when sorting results for each matching document. | None  
`direction` | The direction to sort the search results, either `ASCENDING` or `DESCENDING`. | `DESCENDING` |   
`default_value` | The default value of the expression, if no field is present and cannot be calculated for a document. A text value must be specified for text sorts. A numeric value must be specified for numeric sorts. | None  
  
### Sorting on multi-valued fields

When you sort on a multi-valued field of a particular type, only the first value assigned to the field is used. For example, consider two documents, DocA and DocB that both have a text field named "color". Two values are assigned to the DocA "color" field in the order (red, blue), and two values to DocB in the order (green, red). When you perform a sort specifying the text field "color", DocA is sorted on the value "red" and DocB on the value "green". The other field values are not used in the sort.

### To sort or not to sort

If you do not specify any sort options, your search results are automatically returned sorted by descending rank. There is no limit to the number of documents that are returned in this case. If you specify any sorting options, the sort is performed after all the matching documents have been selected. There is an explicit property, `SortOptions.limit` , that controls the size of the sort. You can never sort more than 10,000 docs, the default is 1,000. If there are more matching documents than the number specified by `SortOptions.limit` , search only retrieves, sorts, and returns that limited number. It selects the documents to sort from the list of all matching documents, which is in descending rank order. It is possible that a query might select more matching documents than you can sort. If you are using sort options and it is important to retrieve every matching document, you should try to ensure that your query will return no more documents than you can sort.

## Writing expressions

Expressions are used to define field expressions (which are set in the `QueryOptions` ) and sort expressions, which are set in the `SortOptions`. They are written as strings:
    
    
    "price * quantity"
    "(men + women)/2"
    "min(daily_use, 10) * rate"
    "snippet('rose', flower, 120)"
    

Expressions involving Number fields can use the arithmetical operators (+, -, *, /) and the built-in numeric functions listed below. Expressions involving geopoint fields can use the geopoint and distance functions. Expressions for Text and HTML fields can use the snippet function.

Expressions can also include these special terms:

Term | Description  
---|---  
`_rank` | A document's [rank](https://docs.cloud.google.com/appengine/docs/standard/services/search#other_document_properties) property. It can be used in field expressions and sort expressions.  
`_score` | The score assigned to a document when you include a [`MatchScorer`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/matchscorerclass) object in the `SortOptions`. This term can only appear in sort expressions; it cannot be used in field expressions.  
  
### Numeric functions

The expressions to define numeric values for `FieldExpressions` and `SortExpressions` can use these built-in functions. The arguments must be numbers, field names, or expressions using numbers and field names.

Function | Description | Example  
---|---|---  
`max` | Returns the largest of its arguments. | `max(recommended_retail_price, discount_price, wholesale_price)`  
`min` | Returns the smallest of its arguments. | `min(height, width, length)`  
`log` | Returns the natural logarithm. | `log(x)`  
`abs` | Returns the absolute value. | `abs(x)`  
`pow` | Takes two numeric arguments. The call pow(x, y) computes the value of x raised to the y power. | `pow(x, 2)`  
`count` | Takes a field name as its argument. Returns the number of fields in the document with that name. Remember that a document can contain multiple fields of different types with the same name. Note: `count` can only be used in `FieldExpressions`. It cannot appear in `SortExpressions`. | `count(user)`  
  
### Geopoint functions

These functions can be used for expressions involving geopoint fields.

Function | Description | Example  
---|---|---  
`geopoint` | Defines a geopoint given a latitude and longitude. | `geopoint(-31.3, 151.4)`  
`distance` | Computes the distance in meters between two geopoints. Note that either of the two arguments can be the name of a geopoint field or an invocation of the geopoint function. However, only one argument can be a field name. | `distance(geopoint(23, 134), store_location)`  
  
### Snippets

A snippet is a fragment of a text field that matches a query string and includes the surrounding text. Snippets are created by calling the `snippet` function:

`snippet(query, body, [max_chars])`

`query`
    A quoted query string specifying the text to find in the field.
`body`
    The name of a text, HTML, or atom field.
`max_chars`
    The maximum number of characters to return in the snippet. This argument is optional; it defaults to 160 characters.

The function returns an HTML string. The string contains a snippet of the body field's value, with the text that matched the query in boldface.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
