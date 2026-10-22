---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/query-strings/
title: Query strings \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:45.238261+00:00
---

# Query strings  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/query-strings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Query strings Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

A query string contains Unicode characters. The maximum length of a query string is 2000 characters. All query strings contain at least one field value. It's recommended to write field values in lower case, because searches on atom, text, and HTML fields are case insensitive, and a query string can also contain the boolean operators `AND`, `OR`, and `NOT`, which are recognized by writing them in upper case.

A comma can appear in a query string only if it is used to separate the arguments of a function: `distance(home, geopoint(35.2, 40.5)) > 100` or it's part of a quoted string.

A query string can take many forms. There are two main ways to construct a query: with and without field names. A _global search_ uses a query string that contains only field values:
    
    
    query = "blue"
    query = "NOT white"
    query = "blue OR red"
    query = "blue guitar"
    

A _field search_ uses a query string that contains one or more expressions specifying field names and field values:
    
    
    query = "model:gibson date < 1965-01-01"
    query = "title:\"Harry Potter\" AND pages<500"
    query = "beverage:wine color:(red OR white) NOT country:france"
    

This document describes how to construct query strings for global and field searches, and how the search logic works in each case.

We recommend logging query strings in your application if you wish to keep a record of queries that have been executed.

## Global search

Global search offers the ability to search for documents by specifying values that might appear in _any_ document field. To perform a global search you write a query string that contains one or more field values. The search algorithm recognizes the type of each value and searches all the document fields that could contain that value.

### One-value queries

A search with a query string that contains a single value is handled according to these rules:

If the query string is a word (`red`) or a quoted string (`"red rose"`), search retrieves all documents in an index that have:

  * A text or HTML field that contains that word or quoted string (matching is case insensitive).
  * An atom field with a value that matches the word or quoted string (matching is case insensitive).



If the query string is a number ("3.14159"), search retrieves all documents that have:

  * A text or HTML field that contains a token that matches the number as it appears in the query (the text field "he took 5 minutes" will match the query "5" but not "5.0").
  * An atom field that literally matches the number as it appears in the query.



If the query string is a date in yyyy-mm-dd form, search retrieves all documents that have:

  * A date field whose value equals that date (leading zeros in the query string are optional, "2012-07-04" and "2012-7-4" are the same date).
  * A text or HTML field that contains a token that literally matches the date as it appears in the query.
  * An atom field that literally matches the date as it appears in the query.



You can prepend the NOT boolean operator (upper case) to a one word query. The result is a list of documents that do not have any fields that match the query value, according to the same rules. So the query `NOT red` will retrieve all documents that don't have any text or HTML fields that contain "red", or any atom fields with the value `red`.

You might have noticed that geopoint fields have not been mentioned. At this time, you cannot specify a raw geopoint value as a string, so geopoints cannot appear in global searches.

### Multi-value queries

You can specify multiple values (separated by spaces) in a global search string. The white space between words, quoted strings, numbers, and dates is treated as an implicit AND operator. The two search strings below are _almost_ the same; they differ in how global search treats atom fields, which is explained below:
    
    
    query = "small red"
    query = "small AND red"
    

When performing a global search with multiple values, field matching is done independently on each value in the string, and atom field matching is handled differently, in particular:

  * Query values can appear in any order in a text or HTML field.
  * Different values can appear in different fields.
  * Atom fields are searched only when the query string does not contain any boolean operators (`AND`, `OR`, `NOT`). The entire query string must match an atom field.



Note the third rule dealing with atom fields. The query string "red small" does not contain the boolean `AND` (even though it's implied), so search will attempt to find matching atom fields. The string "red AND small" does contain a boolean operator, so search will not try to match the query string against atom fields.

The following example shows four documents that were retrieved using the query string "rose bud." Each document has two text fields and one atom field. The comment column explains why each document satisfies the query.

Doc ID | Text Field 1 | Text Field 2 | Atom Field | Comment  
---|---|---|---|---  
1 | mighty like a **rose** | one **bud** to bind them all | thorn bush | Matching values can appear in different fields  
2 | wide like a river | like a **bud** on a **rose** | tumble weed | Matching values can appear in any order in the same text or HTML field, with intervening text  
3 | deep like the ocean | the **rose bud** boys | blue bonnet | Matching values can appear in any order in the same text or HTML field  
4 | tall like a mountain | the beautiful garden | **rose bud** | Atom field matches because its value is the same as the entire query string  
  
Note that if you reversed the values in the query and searched for "bud rose" instead, documents 1, 2, and 3 would still be returned, but document 4 would not. To search for an exact character string in atom, text, and HTML fields, quote the string in the query string. A search for `"rose bud"` would return only documents 3 and 4 in the example.

### Boolean operators

You can specify a more complex global search by using the boolean operator `NOT` before a value, and the operators AND and OR between values. Note that these operators must be written in upper case. If they appear within a quoted string they are treated as part of the field value, not as operators. You can use parentheses in a query string make the logic clear.

The boolean operator precedence, from highest to lowest, is: `NOT`, `OR`, `AND`:
    
    
    NOT cat AND dogs OR horses --> (NOT cat) AND (dogs OR horses)
    NOT cat OR dogs AND horses --> ((NOT cat) OR dogs) AND horses
    

### Stemming

To search for common variations of a word, like plural forms and verb endings, use the `~` stem operator (the tilde character). This is a prefix operator which must precede a value with no intervening space. The value `~cat` will match "cat" or "cats," and likewise `~dog` matches "dog" or "dogs." The stemming algorithm is not fool-proof. The value `~care` will match "care" and "caring," but not "cares" or "cared." Stemming is only used when searching text and HTML fields.

### Tokenization

When a document is indexed, its fields are [tokenized](https://docs.cloud.google.com/appengine/docs/standard/services/search#tokenizing_string_fields). Similarly, the values in a query string are also tokenized. This means that what might appear to be a one-value query is actually treated as a multi-value query. For example:
    
    
    "real-time" --> "real time"
    "2001-12-15" --> "2001 12 15"
    "1.5" --> "1 5"
    

## Field search

A field search looks for values in specific document fields, by field name. A field search query string is composed of one or more expressions that specify a _field name_ , a _relational operator_ , and a _field value_. The available relational operators depend on the type of the field. The equality operator, represented by either a colon or the equals sign, can be used for all field types. Here are some field query strings for different types of fields:
    
    
    query = "pet = dog"
    query = "author = \"Ray Bradbury\""
    query = "color:red"
    query = "NOT color:red"
    query = "price < 500"
    query = "birthday>=2011-05-10"
    

Note that the use of whitespace on either side of the relational operator is optional. As with global search query strings, the value of a text, HTML, or atom field can be enclosed in quotes to specify a string, and an expression for a field value can be negated by prepending an uppercase `NOT`.

### Queries on atom fields

The value of an atom field is a character string. Queries on atom fields are case insensitive. If your query specifies a field value with whitespace or punctuation, be sure to quote the value within the query string. The only valid relational operator for atom fields is the equality operator. The complete contents of an atom field must match the query value; this includes any Unicode combining characters or accented characters in the field. Stemming is not supported for atom fields.

Query String | Comments  
---|---  
`"weather=stormy"  
"weather: stormy"` |  Either form of the equality operator is valid. Retrieves documents with a weather field that equals "stormy."   
`"Title: \"Tom&Jerry\""  
"Couple: \"Fred and Ethel\""  
"Version = \"1HCP(21.3)\""  
` |  If you are searching for an atom field that contains whitespace or special characters, enclose the value in quotes.   
`"Color = (red OR blue)"  
"Color = (\"dark red\" OR \"bright blue\")" ` |  You can use parentheses and the logical operator OR to specify a list of alternate field values.   
  
### Queries on text and HTML fields

The only valid relational operator for text and HTML fields is equality. In this case the operator means "field includes value" not "field equals value." You can use the stemming operator to search for variants on a word. You can also use the OR and AND operators to specify complex boolean expressions for the field value. If a boolean operator appears within a quoted string, it is not treated specially, it's just another piece of the character string to be matched. Remember that when searching HTML fields, the text within HTML markup tags is ignored. Queries on text and HTML fields are case insensitive. When these fields are indexed, any Unicode combining characters and accented characters in them are "normalized" to their unaccented equivalents. Combining characters and accents are also normalized in query strings on these fields, so a query can include the accented forms or not, and will match the fields in either case.

Query String| Comments  
---|---  
`"Comment = great"  
"Comment: great"` | Either form of the equality operator is valid. Retrieves documents with a comment field that contains at least one occurrence of the word "great" in the Comment field.  
` "Comment = (great big ball)"  
"Comment = (great AND big AND ball)" ` | To search for two or more words in a field, in any order, enclose the words in parentheses. This query string retrieves documents with a Comment field that includes all three words in any order with any number of other words between them. The space between words implies a logical AND; the second form makes this explicit.   
`"Comment = \"insanely great\""` | To search for a specific string of text, enclose the string in quotes. This query will retrieve documents whose Comment field contains the phrase "insanely great" (and also "insanely-great" which is tokenized to the same thing).  
`"pet = ~dog"` | The stemming operator will match variants of the word "dog" in the pet field.   
`"Color = (red OR blue)"` | To search for a match from a list of alternatives, enclose the list in parentheses with the keyword OR between alternatives. This query retrieves documents whose Color field includes either "red" or "blue" or both.  
`"weather = ((rain OR snow) AND cold)"` |  You can use the logical operators OR and AND, along with parentheses, to specify a more complex field value.   
`"weather = \"rain OR shine\""` |  Because the logical OR is embedded in a quoted string, it is not treated as a relational operator. This query string retrieves documents with a weather field that contains the string "rain or shine"   
  
### Queries on number fields

A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operators, along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. Here are some example query strings for number fields:
    
    
    "quantity = 10000"
    "size: 4"
    "price < 9.99"
    "theta > 1.5E-2"
    

### Queries on date fields

A date field value must be written in `yyyy-mm-dd form`. Leading zeros are optional for one-digit months and days. The valid relational operators for date fields are the equality operators, along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality operator. You can prepend the `NOT` operator to an expression to negate it. Here are some example query strings for date fields:
    
    
    "start_date: 2012-05-20"
    "end_date: 2013-5-1"
    "birthday >= 2000-12-31"
    "NOT birthday = 2000-12-25"
    

### Queries on geopoint fields

There are no relational operators that work with geopoint fields, so geopoint fields cannot be named directly in a query string. The Search API provides two special functions that can be used for queries involving geopoint fields:

`geopoint(lat,long)`
    Defines a geopoint given a latitude and longitude.
`distance(point1, point2)`
    Computes the distance in meters between two geopoints. Each point can be specified by using the name of a geopoint field or an invocation of the geopoint function. Note that you cannot provide two field names as arguments to this function. At least one argument must be a constant.

These functions can be used to construct queries that retrieve locations relative to a constant position. The following examples assume that the index contains documents with geopoint fields named "survey_marker" and "home."

Query String | Comments  
---|---  
`"distance(survey_marker, geopoint(35.2, 40.5)) < 100"` | Search for markers less than 100 meters from a given geopoint.  
`"distance(home, geopoint(35.2, 40.5)) > 100"` | Search for homes more than 100 meters from a given geopoint.  
  
Applications that use geolocation typically receive information from the browser. If the user allows, location can be inferred from their IP address, or they can enter a postal code. Location can also come from other APIs like the [Google Maps Geolocation API](https://developers.google.com/maps/documentation/business/geolocation).

### Queries on multiple fields

You can combine multiple field query expressions in one query by listing them in sequence separated by whitespace. This puts an implied `AND` between each expression, so all of them must be satisfied to retrieve a document. You can explicitly add AND and OR operators between expressions, and use parentheses to make the logic clear.

Query String | Comments  
---|---  
`"product=piano manufacturer=steinway"`  
`"product=piano AND manufacturer=steinway"` |  These queries retrieve all Steinway pianos. The space between the terms implies a logical AND; the second form makes this explicit.   
`"product=piano AND NOT manufacturer=steinway"` | Retrieves all non-Steinway pianos.  
`"product=piano AND price<2000"` | This query retrieves inexpensive pianos.  
  
## Mixing global and field searches

A query string can contain any number of global search expressions and field search expressions. Spaces between expressions are treated as `AND`. You can also use `OR` and `AND` explicitly, along with parentheses. Each expression will be handled according to the rules associated with that kind of term.

Query String| Comments  
---|---  
`"keyboard great price<5000"  
"keyboard AND great AND price<5000"` |  Retrieves documents where the words "great" and "keyboard" appear in any text, HTML, or atom fields, and there is a price field less than 5000. The `AND` is implied, the second form is equivalent.   
`"keyboard OR product=piano"` |  Retrieves documents with a product field that contains piano, or documents with any text, HTML, or atom field that contains keyboard.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
