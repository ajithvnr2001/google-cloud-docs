---
url: https://docs.cloud.google.com/memorystore/docs/redis/ftsearch/
title: FT.SEARCH \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:09.412262+00:00
---

# FT.SEARCH  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/ftsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  FT.SEARCH Stay organized with collections  Save and categorize content based on your preferences. 

`FT.SEARCH` searches the index with the provided query, and returns the specified values.

For details on query syntax, see [Query syntax](https://docs.cloud.google.com/memorystore/docs/redis/query-syntax).

## Syntax
    
    
    FT.SEARCH index query
      [NOCONTENT]
      [TIMEOUT timeout]
      [PARAMS nargs name value [ name value ...]]
      [RETURN num field [AS alias] [ field [AS alias] ... ]]
      [LIMIT offset num]
      DIALECT 2
    

  * `index` (required): This index you want to query.
  * `query` (required): This is your query. For details on query syntax, see [Query syntax](https://docs.cloud.google.com/memorystore/docs/redis/query-syntax).
  * `NOCONTENT` (optional): This returns just the document IDs, and excludes the content.
  * `TIMEOUT` (optional): Lets you set a timeout value for the search command.
  * `PARAMS` (optional): The number of key value pairs times two.
  * `RETURN` (optional): Specifies the fields you want to retrieve from your documents, along with any aliases for the returned values. By default, all fields are returned unless the `NOCONTENT` option is set, in which case no fields are returned. If num is set to 0, it behaves the same as `NOCONTENT`.
  * `LIMIT` (optional): Lets you choose pagination with an offset and a number count. If you don't use this parameter, the default is `LIMIT 0 10`, which returns at most 10 keys.
  * `DIALECT 2` (optional): Specifies your dialect. The only supported dialect is dialect 2.



### Command return

  * This command returns an array or an error message. The elements of the returned array represent the best matched results of the query. Each array element has the following:

  * The entry hash key

  * An array of the following:

    * Key value: [$score_as ] score_value
    * Distance value
    * Attribute name
    * Vector value

If `NOCONTENT` is used, the array elements consist of just the document IDs.




## Example #1: Simple vector search query

For this example, assume we're building a property searching index where customers can search properties based on some features. Assume we have a list of properties with the following attributes:

  * Description - vector embedding for given property.
  * Other fields - each property can have other metadata as well. However, for simplicity, other fields are ignored in this example.



At first, we create an HNSW index with the description as a vector field using the `FT.CREATE` command:
    
    
    FT.CREATE idx SCHEMA description VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC L2
    

Now we can insert a few properties (this can be done prior to index creation as well) using the HSET command:
    
    
    HSET p1 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?"
    HSET p2 description "\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00"
    HSET p3 description "\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00"
    HSET p4 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?"
    HSET p5 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?"
    

Now we can perform queries using the FT.SEARCH command. The following query returns up to five of the most similar properties to the provided query vector:
    
    
    FT.SEARCH idx "*=>[KNN 5 @description $query_vector]" PARAMS 2 query_vector "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00" DIALECT 2
    

Returned result:
    
    
     1) (integer) 5
     2) p5
     3) 1) __description_score
        2) 1.6400001049
        3) description
        4) \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?
     4) p4
     5) 1) __description_score
        2) 1.6400001049
        3) description
        4) \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?
     6) p2
     7) 1) __description_score
        2) 1.6400001049
        3) description
        4) \x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00
     8) p1
     9) 1) __description_score
        2) 1.6400001049
        3) description
        4) \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?
    10) p3
    11) 1) __description_score
        2) 0.0399999953806
        3) description
        4) \x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00
    

### Code Sample

### Python
    
    
    # Before running, ensure you have installed redis-py:
    #    pip install redis
    
    import redis
    client = redis.Redis(host='your_server_host', port=6379)
    result = client.execute_command('FT.SEARCH', 'idx', '*=>[KNN 5 @description $query_vector]', 'PARAMS', '2', 'query_vector', '"\xcd\xccL?\x00\x00\x00\x00"', 'DIALECT', '2')
    print(result)
    

### NodeJS
    
    
    # Before running, ensure you have installed ioredis:
    #   npm install ioredis
    
    const Redis = require("ioredis");
    const redis = new Redis(6379, "your_server_host")
    redis.call("FT.SEARCH", "idx", "*=>[KNN 5 @description $query_vector]", "PARAMS", "2", "query_vector", "\xcd\xccL?\x00\x00\x00\x00\x00\x00", "DIALECT", "2").then(result => {
    console.log(result);
    redis.disconnect();
    });
    

### CLI
    
    
    # Before running, ensure you have install redis-cli
    
    redis-cli -h your_server_host -p 6379 FT.SEARCH idx "(*)=>[KNN 5 @description $query_vector]" PARAMS 2 query_vector "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00" DIALECT 2
    

## Example #2: Vector search with [hybrid queries](https://docs.cloud.google.com/memorystore/docs/redis/query-syntax#hybrid-queries)

For this example we will do a [hybrid query](https://docs.cloud.google.com/memorystore/docs/redis/query-syntax#hybrid-queries) by using an additional two attributes named city and price:

  * Description - vector embedding for given property.
  * City - name of the city.
  * Price - cost of the property.



At first, we create an index with the description as a vector field, city as a tag field, price as a numeric field:
    
    
    FT.CREATE idx SCHEMA description VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC L2 city TAG price NUMERIC
    

Now, we can insert a few properties (this can be done prior to index creation as well):
    
    
    HSET p1 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?" city "NEW YORK" price 500000
    HSET p2 description "\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00" city "NEW JERSEY" price 400000
    HSET p3 description "\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00" city "BANGALORE" price 60000
    HSET p4 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?" city "NEW YORK" price 600000
    HSET p5 description "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?" city "BANGALORE" price 75000
    

Now, we can perform queries. The following query returns up to five of the most similar properties to the provided query vector, filtering only to those in BANGALORE priced less than 100000:
    
    
    FT.SEARCH idx "(@city:{BANGALORE} @price:[-inf 100000])=>[KNN 5 @description $query_vector]" PARAMS 2 query_vector "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00" DIALECT 2
    

Returned result:
    
    
    1) (integer) 2
    2) p5
    3) 1) __description_score
       2) 1.6400001049
       3) city
       4) BANGALORE
       5) price
       6) 75000
       7) description
       8) \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?
    4) p3
    5) 1) __description_score
       2) 0.0399999953806
       3) city
       4) BANGALORE
       5) price
       6) 60000
       7) description
       8) \x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00
    

Refer to [Query syntax](https://docs.cloud.google.com/memorystore/docs/redis/query-syntax) for details on the filter query format.

### Code Sample

### Python
    
    
    # Before running, ensure you have installed redis-py:
    #   pip install redis
    
    import redis
    client = redis.Redis(host='your_server_host', port=6379)
    result = client.execute_command('FT.SEARCH', 'idx', '(@city:{BANGALORE} @price:[-inf 100000])=>[KNN 5 @description $query_vector]', 'PARAMS', '2', 'query_vector', '"\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00"', 'DIALECT', '2')
    print(result)
    

### NodeJS
    
    
    # Before running, ensure you have installed ioredis:
    #   npm install ioredis
    
    const Redis = require("ioredis");
    const redis = new Redis(6379, "your_server_host")
    redis.call("FT.SEARCH", "idx", "(@city:{BANGALORE} @price:[-inf 100000])=>[KNN 5 @description $query_vector]", "PARAMS", "2", "query_vector", "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00", "DIALECT", "2").then(result => {
    console.log(result);
    redis.disconnect();
    });
    

### CLI
    
    
    # Before running, ensure you have install redis-cli
    
    redis-cli -h your_server_host -p 6379 FT.SEARCH idx "(@city:{BANGALORE} @price:[-inf 100000])=>[KNN 5 @description $query_vector]" PARAMS 2 query_vector "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00" DIALECT 2
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
