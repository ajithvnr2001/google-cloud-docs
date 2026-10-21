---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/gql/GQL/
title: google.appengine.ext.gql.GQL \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:36:30.268689+00:00
---

# google.appengine.ext.gql.GQL  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/gql/GQL/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.gql.GQL Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L95-L1441) A GQL interface to the datastore. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.gql.GQL(
        query_string, _app=None, _auth_domain=None, namespace=None
    )
    

GQL is a SQL-like language which supports more object-like semantics in a language that is familiar to SQL users. The language supported by GQL will change over time, but will start off with fairly simple semantics.

  * reserved words are case insensitive
  * names are case sensitive

The syntax for SELECT is fairly straightforward: SELECT [[DISTINCT]  [,  ...] | * | **key** ] [FROM ] [WHERE  [AND  ...]] [ORDER BY  [ASC | DESC] [,  [ASC | DESC] ...]] [LIMIT [,]] [OFFSET ] [HINT (ORDER_FIRST | FILTER_FIRST | ANCESTOR_FIRST)] [;] :=  {< | <= | > | >= | = | != | IN}  :=  {< | <= | > | >= | = | != | IN} CAST()  :=  IN (, ...)  := ANCESTOR IS  Currently the parser is LL(1) because of the simplicity of the grammar (as it is largely predictive with one token lookahead). The class is implemented using some basic regular expression tokenization to pull out reserved tokens and then the recursive descent parser will act as a builder for the pre-compiled query. This pre-compiled query is then bound to arguments before executing the query. Initially, three parameter passing mechanisms are supported when calling Execute():

  * Positional parameters Execute('SELECT * FROM Story WHERE Author = :1 AND Date > :2')
  * Named parameters Execute('SELECT * FROM Story WHERE Author = :author AND Date > :date')
  * Literals (numbers, strings, booleans, and NULL) Execute('SELECT * FROM Story WHERE Author = 'James'')

Users are also given the option of doing type conversions to other datastore types (e.g. db.Email, db.GeoPt). The language provides a conversion function which allows the caller to express conversions of both literals and parameters. The current conversion operators are:

  * GEOPT(float, float)
  * USER(str)
  * KEY(kind, id/name[, kind, id/name...])
  * DATETIME(year, month, day, hour, minute, second)
  * DATETIME('YYYY-MM-DD HH:MM:SS')
  * DATE(year, month, day)
  * DATE('YYYY-MM-DD')
  * TIME(hour, minute, second)
  * TIME('HH:MM:SS')

We will properly serialize and quote all values. It should also be noted that there are some caveats to the queries that can be expressed in the syntax. The parser will attempt to make these clear as much as possible, but some of the caveats include:

  * There is no OR operation. In most cases, you should prefer to use IN to express the idea of wanting data matching one of a set of values.
  * You cannot express inequality operators on multiple different properties
  * You can only have one != operator per query (related to the previous rule).
  * The IN and != operators must be used carefully because they can dramatically raise the amount of work done by the datastore. As such, there is a limit on the number of elements you can use in IN statements. This limit is set fairly low. Currently, a max of 30 datastore queries is allowed in a given GQL query. != translates into 2x the number of datastore queries, and IN multiplies by the number of elements in the clause (so having two IN clauses, one with 5 elements, the other with 6 will cause 30 queries to occur).
  * Literals can take the form of basic types or as type-cast literals. On the other hand, literals within lists can currently only take the form of simple types (strings, integers, floats).

SELECT * will return an iterable set of entities; SELECT **key** will return an iterable set of Keys. | 

## Args  
  
---  
  
`query_string` |  properly formatted GQL query string.   
`namespace` |  the namespace to use for this query.   
  
## Raises  
  
---  
  
`datastore_errors.BadQueryError` |  if the query is not parsable.   
  
## Methods

### `Bind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L302-L382)
    
    
    Bind(
        args, keyword_args, cursor=None, end_cursor=None
    )
    

Bind the existing query to the argument list.

Assumes that the input args are first positional, then a dictionary. So, if the query contains references to :1, :2 and :name, it is assumed that arguments are passed as (:1, :2, dict) where dict contains a mapping [name] -> value.

Args  
---  
  
`args` |  the arguments to bind to the object's unbound references.   
`keyword_args` |  dictionary-based arguments (for named parameters).   
  
Raises  
---  
  
`datastore_errors.BadArgumentError` |  when arguments are left unbound (missing from the inputs arguments) or when arguments do not match the expected type.   
  
Returns  
---  
The bound datastore.Query object. This may take the form of a MultiQuery object if the GQL query will require multiple backend queries to statisfy.   
  
### `EnumerateQueries`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L384-L412)
    
    
    EnumerateQueries(
        used_args, args, keyword_args
    )
    

Create a list of all multi-query filter combinations required.

To satisfy multi-query requests ("IN" and "!=" filters), multiple queries may be required. This code will enumerate the power-set of all multi-query filters.

Args  
---  
  
`used_args` |  set of used positional parameters (output only variable used in reporting for unused positional args)   
`args` |  positional arguments referenced by the proto-query in self. This assumes the input is a tuple (and can also be called with a varargs param).   
`keyword_args` |  dict of keyword arguments referenced by the proto-query in self.   
  
Returns  
---  
A list of maps [(identifier, condition) -> value] of all queries needed to satisfy the GQL query with the given input arguments.   
  
### `Run`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L789-L827)
    
    
    Run(
        *args, **keyword_args
    )
    

Runs this query.

Similar to datastore.Query.Run. Assumes that limit == -1 or > 0

Args  
---  
  
`args` |  arguments used to bind to references in the compiled query object.   
`keyword_args` |  dictionary-based arguments (for named parameters).   
  
Returns  
---  
A list of results if a query count limit was passed. A result iterator if no limit was given.   
  
### `filters`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L829-L831)
    
    
    filters()
    

Return the compiled list of filters.

### `hint`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L833-L835)
    
    
    hint()
    

Return the datastore hint.

### `is_distinct`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L860-L862)
    
    
    is_distinct()
    

Returns True if this query is marked as distinct.

### `is_keys_only`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L852-L854)
    
    
    is_keys_only()
    

Returns True if this query returns Keys, False if it returns Entities.

### `kind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L864-L865)
    
    
    kind()
    

### `limit`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L837-L839)
    
    
    limit()
    

Return numerical result count limit.

### `offset`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L841-L846)
    
    
    offset()
    

Return numerical result offset.

### `orderings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L848-L850)
    
    
    orderings()
    

Return the result ordering list.

### `projection`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L856-L858)
    
    
    projection()
    

Returns the tuple of properties in the projection, or None.

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/gql/__init__.py#L789-L827)
    
    
    __iter__(
        *args, **keyword_args
    )
    

Runs this query.

Similar to datastore.Query.Run. Assumes that limit == -1 or > 0

Args  
---  
  
`args` |  arguments used to bind to references in the compiled query object.   
`keyword_args` |  dictionary-based arguments (for named parameters).   
  
Returns  
---  
A list of results if a query count limit was passed. A result iterator if no limit was given.   
  
## Class Variables  
  
---  
  
MAX_ALLOWABLE_QUERIES |  `30`  
RESERVED_KEYWORDS |  `(frozenset({'ANCESTOR', 'ANCESTOR_FIRST', 'AND', 'ASC', 'BY', 'DESC', 'DISTINCT', 'FILTER_FIRST', 'FROM', 'GROUP', 'HINT', 'IN', 'IS', 'LIMIT', 'NOT', 'OFFSET', 'OR', 'ORDER', 'ORDER_FIRST', 'SELECT', 'WHERE'}), frozenset())`  
TOKENIZE_REGEX |  Instance of `re.Pattern`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
