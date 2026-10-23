---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-json/
title: About JSON \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:34.719832+00:00
---

# About JSON  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About JSON Stay organized with collections  Save and categorize content based on your preferences. 

JavaScript Object Notation (JSON) provides an efficient way for you to store and manipulate structured data in Memorystore for Valkey. Using JSON provides you with the following benefits:

  * Having fast search and filtering capabilities
  * Performing in-place updates to JSON data without having to overwrite entire documents
  * Querying, modifying, and managing complex data structures efficiently



If your applications require dynamic and flexible data storage, then JSON is ideal for you. Also, by using JSON, you can encode complex datasets inside of Memorystore for Valkey instances without using schemas. You can store, access, and update data in the instances, and you don't have to manage custom code to serialize and deserialize the data.

A _JSON document_ is a human-readable text format for storing and transporting data. This format consists of key-value pairs and structured data types. The JSON format lets you retrieve and update portions of a JSON document without having to manipulate the entire object. This can improve your performance and reduce your costs. In addition, the JSON format is compliant with [RFC 7159](https://www.ietf.org/rfc/rfc7159.txt), the [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/) JSON data interchange standard, and UTF-8 [Unicode](https://www.unicode.org/standard/WhatIsUnicode.html) in JSON text.

## Availability

If you create a Memorystore for Valkey instance, version 8.0 and later, then version 1.0 of the [JSON data type and associated commands](https://github.com/valkey-io/valkey-json) is available automatically. This data type is API-compatible with version 2 of the JSON module. Also, as of RFC 7159, the root element of a JSON document can be of any JSON data type.

## JSON properties

JSON has the following properties:

  * **Max document size** : to prevent potential out-of-memory issues from malicious or unbounded insertions, you can configure a limit on the size of individual JSON keys.

By default, the value for this property is set to `0`, which means that there's no limit to the size of the JSON document. To set this limit, use the [`CONFIG SET json.max-document-size VALUE`](https://valkey.io/commands/config-set/) command, where VALUE is the maximum size of the document. For example, if you specify `4123456`, then the maximum document size is 4,123,456 bytes (4 MB).

To see how much memory is used by a JSON value that's stored in a specified key, you can use the [`JSON.DEBUG MEMORY KEY`](https://valkey.io/commands/json.debug/) or [`MEMORY USAGE KEY`](https://valkey.io/commands/memory-usage/) commands. For these commands, KEY is the name of the key where the JSON value is stored.

  * **Max depth** : the maximum nesting level for JSON objects and arrays. For more information, see Maximum nesting depth limit.




## JSON document size

Because a JSON document is stored internally in a format that's optimized for rapid access and modification, this type of document can consume a lot of memory. To check how much memory a JSON document consumes, use the [`JSON.DEBUG MEMORY KEY`](https://valkey.io/commands/json.debug/) command, where KEY is the name of the key that contains the document.

## JSON categories

To manage access to JSON commands and data, use the `@json` category. In addition to this category, the following categories use JSON commands: `@read`, `@write`, `@fast`, `@slow`, and `@admin`.

The following table indicates whether you can map JSON commands to the `@read`, `@write`, `@fast`, `@slow`, `@admin`, and `@json` categories.

JSON command | `@json` | `@read` | `@write` | `@fast` | `@slow` | `@admin`  
---|---|---|---|---|---|---  
`JSON.ARRAPPEND` | Y | N | Y | Y | N | N  
`JSON.ARRINDEX` | Y | Y | N | Y | N | N  
`JSON.ARRINSERT` | Y | N | Y | Y | N | N  
`JSON.ARRLEN` | Y | Y | N | Y | N | N  
`JSON.ARRPOP` | Y | N | Y | Y | N | N  
`JSON.ARRTRIM` | Y | N | Y | Y | N | N  
`JSON.CLEAR` | Y | N | Y | Y | N | N  
`JSON.DEBUG` | Y | Y | N | N | Y | Y  
`JSON.DEL` | Y | N | Y | Y | N | N  
`JSON.FORGET` | Y | N | Y | Y | N | N  
`JSON.GET` | Y | Y | N | Y | N | N  
`JSON.MGET` | Y | Y | N | Y | N | N  
`JSON.MSET` | Y | N | Y | N | Y | N  
`JSON.NUMINCRBY` | Y | N | Y | Y | N | N  
`JSON.NUMMULTBY` | Y | N | Y | Y | N | N  
`JSON.OBJKEYS` | Y | Y | N | Y | N | N  
`JSON.OBJLEN` | Y | Y | N | Y | N | N  
`JSON.RESP` | Y | Y | N | Y | N | N  
`JSON.SET` | Y | N | Y | N | Y | N  
`JSON.STRAPPEND` | Y | N | Y | Y | N | N  
`JSON.STRLEN` | Y | Y | N | Y | N | N  
`JSON.TOGGLE` | Y | N | Y | Y | N | N  
`JSON.TYPE` | Y | Y | N | Y | N | N  
  
## JSON metrics

To monitor the usage of JSON documents, the following Cloud Monitoring metrics are available in Memorystore for Valkey:

  * `documents_count`
  * `used_memory`



For more information about these metrics, see [Bloom filter and JSON metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#bloom-filter-json-metrics).

## JSON commands

This section lists and describes the JSON commands that you can use to perform operations on JSON documents.

Command | Description  
---|---  
`[JSON.ARRAPPEND](https://valkey.io/commands/json.arrappend/)` | Append one or more JSON values into the array at the path.  
`[JSON.ARRINDEX](https://valkey.io/commands/json.arrindex/)` | Search for the first occurrence of a scalar JSON value in an array.  
`[JSON.ARRINSERT](https://valkey.io/commands/json.arrinsert/)` | Insert one or more JSON values into an array at a path before the index that you specify.  
`[JSON.ARRLEN](https://valkey.io/commands/json.arrlen/)` | Retrieve the length of the JSON array at the path.  
`[JSON.ARRPOP](https://valkey.io/commands/json.arrpop/)` | Remove and return an element from an index in the array.  
`[JSON.ARRTRIM](https://valkey.io/commands/json.arrtrim/)` | Trim an array at the path so that it contains only the inclusive range of elements that you specify.  
`[JSON.CLEAR](https://valkey.io/commands/json.clear/)` | Clear the arrays or a JSON object at a path that you specify.  
`[JSON.DEBUG](https://valkey.io/commands/json.debug/)` | Retrieve information about a JSON document. Memorystore for Valkey supports the following subcommands:  


  * `MEMORY`: report a value's memory usage in bytes.


  * `DEPTH`: report the maximum path depth of a JSON document. 


  * `FIELDS`: report the number of fields within a JSON element. This element is stored at a key that you specify.


  * `HELP`: return helpful information about the `JSON.DEBUG` command.

  
`[JSON.DEL](https://valkey.io/commands/json.del/)`  
`[JSON.FORGET](https://valkey.io/commands/json.forget/)` | Delete JSON values at a path that you specify.  
`[JSON.GET](https://valkey.io/commands/json.get/)` | Return a value at a path that you specify in JSON serialized form.  
`[JSON.MGET](https://valkey.io/commands/json.mget/)` | Return values at a path that you specify from multiple document keys.  
`[JSON.MSET](https://valkey.io/commands/json.mset/)` | Set multiple JSON values at a path to multiple keys.  
`[JSON.NUMINCRBY](https://valkey.io/commands/json.numincrby/)` | Increment numeric values that are stored at a path by a number that you specify.  
`[JSON.NUMMULTBY](https://valkey.io/commands/json.nummultby/)` | Multiply numeric values that are stored at a path by a number that you specify.  
`[JSON.OBJKEYS](https://valkey.io/commands/json.objkeys/)` | Retrieve key names from JSON objects at a path that you specify.  
`[JSON.OBJLEN](https://valkey.io/commands/json.objlen/)` | Retrieve the number of keys in a JSON object at a path that you specify.  
`[JSON.RESP](https://valkey.io/commands/json.resp/)` | Return the JSON value of a key in the [Redis serialization protocol (RESP)](https://redis.io/docs/latest/develop/reference/protocol-spec/) form.  
`[JSON.SET](https://valkey.io/commands/json.set/)` | Set JSON values at a path that you specify.  
`[JSON.STRAPPEND](https://valkey.io/commands/json.strappend/)` | Append a string to JSON strings at a path that you specify.  
`[JSON.STRLEN](https://valkey.io/commands/json.strlen/)` | Retrieve the length of JSON string values at a path that you specify.  
`[JSON.TOGGLE](https://valkey.io/commands/json.toggle/)` | Toggle a boolean value between `true` and `false`. This value is stored at a path that you specify.  
`[JSON.TYPE](https://valkey.io/commands/json.type/)` | Retrieve the type of a JSON value at a path that you specify.  
  
**Note** : For more information about using these commands, see the [Valkey command reference](https://valkey.io/commands/#json) page. You can check the performance of using these commands. For more information, see [ Performance](https://valkey.io/topics/valkey-json/#performance).

## How Memorystore for Valkey interacts with JSON

This section describes how Memorystore for Valkey interacts with the JSON data type.

### Multiple conditional expressions

If there are multiple conditional expressions for filtering, then Memorystore for Valkey evaluates them in the following order:

  1. Operations inside of parentheses
  2. The logical `AND` expression (`&&`)
  3. The logical `OR` (`||`) expression



### Maximum nesting depth limit

When a JSON object or array has an element that's another JSON object or array, the inner object or array nests within the outer object or array. The maximum nesting depth limit is 128. So, a value like `$.a.b.c.d...` can reach only 128 levels.

If you attempt to create a JSON document that contains a nesting depth greater than 128, then Memorystore for Valkey rejects the document and you receive an error. However, you can adjust this limit by using the [`CONFIG SET json.max-path-limit VALUE`](https://valkey.io/commands/config-set/) command, where VALUE is the depth limit that you want.

### JSON numbers

In JSON, both floating point numbers and integers are called numbers because they have the same data type. When Memorystore for Valkey receives a JSON number, it converts the number into one of the following internal binary representations:

  * A 64-bit IEEE double precision floating point number
  * A 64-bit signed integer



JSON doesn't retain the original string and all of its formatting. When Memorystore for Valkey outputs a number as part of a JSON response, Memorystore for Valkey converts the number from the internal binary representation to a printable string that uses generic formatting rules.

When you use the `JSON.NUMINCRBY` and `JSON.NUMMULTBY` commands with JSON numbers, the following conditions apply:

  * If both numbers are integers and the result is out of the range of `int64`, then the result becomes a 64-bit IEEE double precision floating point number automatically.
  * If at least one of the numbers is a floating point number, then the result is a 64-bit IEEE double precision floating point number.
  * If the result exceeds the range of the 64-bit IEEE double precision floating point number, then you receive an `OVERFLOW` error message.



### Direct arrays

Memorystore for Valkey filters array objects directly. For example, if you have data such as  
[`0`,`1`,`2`,`3`] and a path query such as `$[?(@<3)]`, then Memorystore for Valkey returns [`0,1,2`]. For data such as {`"my_valkey_key":[0,1,2,3]`} and a path query such as  
`$.my_valkey_key[?(@<3)]`, Memorystore for Valkey also returns [`0,1,2`].

### Array indexes

Memorystore for Valkey lets you use positive and negative indexes for arrays. The following conditions apply to these types of indexes:

  * **Positive index** : numbers start at the _beginning_ of the array. For example, if an array has a positive index of three, then 0 queries the first element, 1 queries the second element, and 2 queries the third element.
  * **Negative index** : numbers start at the _end_ of the array. If an array has a negative index of three, then -1 queries the third element, -2 queries the second element, and -3 queries the first element.



Memorystore for Valkey doesn't round indexes up or down. If you have an array with a length of 3, and you call either a positive index that's greater than 3 or a negative index that's less than -3, then Memorystore for Valkey doesn't return a result.

### Syntax for JSON paths

You can't use invalid syntax for your JSON paths. This condition applies, even if a subset of a JSON path with an invalid syntax contains a valid path.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
