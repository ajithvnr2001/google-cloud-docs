---
url: https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax/
title: Search query syntax \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:02.792342+00:00
---

# Search query syntax  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Search query syntax Stay organized with collections  Save and categorize content based on your preferences. 

When searching for assets, you can filter the search results by specifying a query made up of an asset metadata field, an operator, and a value.

## Searchable fields and resources

For fields you can use in a `searchAllResources` query, see [ResourceSearchResult Fields](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceSearchResult.FIELDS).

For fields you can use in a `searchAllIamPolicies` query, see [IamPolicySearchResult Fields](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#IamPolicySearchResult.FIELDS).

For resources you can search for, see [Resource types](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource_types).

## Text matching

When searching for a text match, you can match an asset metadata field exactly or partially.

### Exact text matching

For an exact text match, use the `=` (equals) operator with the following syntax:
    
    
    ASSET_METADATA_FIELD**=** QUERY
    

For example:
    
    
    location=us-central1-a
    

Keep the following rules in mind when performing an exact text match:

  * For the query to be true, the query value must exactly match the value of the asset metadata field.

  * For a field with a list value, if the query value matches one of the list's elements, it's considered a match.

  * Query values are case-sensitive.

  * An exact match query value is treated like a phrase, but can't contain wildcards.




### Partial text matching

For a partial text match, use the `:` (has) operator with the following syntax:
    
    
    ASSET_METADATA_FIELD**:** QUERY
    

For example:
    
    
    location:us-central1
    

When performing a search with the `:` operator, the query value and asset metadata field values are [converted to tokens](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax#tokenization_rules) for comparison. Each word of the query value is checked to find out if it exists in consecutive order in the value of the asset metadata field. When using partial matches, the query values are case-insensitive.

Partial match query values can be a phrases or a combination of phrases, and can contain wildcards. Up to 10 comparisons can be made in a query, with a maximum of 2048 characters. If you have a use case for longer queries, contact [gcp-asset-inventory-and-search-feedback@googlegroups.com](mailto:gcp-asset-inventory-and-search-feedback@googlegroups.com). 

#### Tokenization rules

The tokenization rules for partial text matching are as follows:

  * Leading and trailing special characters are removed.

  * Characters that aren't alphanumeric (`[a-zA-Z0-9]`), underscores (`_`), or ampersands (`&`) are treated as delimiters.




Here are some tokenization examples:

  * `us-central1` is tokenized to `[us,central1]`

  * `alex-2020@EXAMPLE.com` is tokenized to `[alex,2020,example,com]`

  * `google.com/cloud` is tokenized to `[google,com,cloud]`

  * `Compute %Instance%` is tokenized to `[compute,instance]`

  * `$%^*-!` is tokenized to `[]`

  * `compute*storage` is tokenized to `[compute,storage]`

  * `compute&storage` is tokenized to `[compute&storage]`

  * `ALEX_test@example.com` is tokenized to `[alex_test,example,com]`

  * `instance/_my_vm_` is tokenized to `[instance,_my_vm_]`




### Exact and partial text matching examples

An asset whose `location` field has the value `us-central1-a` matches the following queries.

Query | Reason for the match  
---|---  
      
    
    location=us-central1-a

| Matches because the phrase `us-central1-a` is exactly the same as the field's value.   
      
    
    location:US-Central1-A

| Matches because punctuation characters are treated as delimiters, and the query value is case-insensitive.   
      
    
    location:"us central1 a"

| Matches because words in the phrase `"us central1 a"` match the field value in consecutive order.   
      
    
    location:(central1 us a)

| Matches because words in the combination `(central1 us a)` match the words in the field value in any order.   
      
    
    location:(a "us central1")

| Matches because the phrases inside the combination, `a` and `"us central1"`, match the words in the field value in any order. Because `"us central1"` is a phrase, these words must be matched in consecutive order.   
      
    
    location:us-central*

| Matches because the wildcard `*` is used to make a prefix match.   
  
An asset whose `location` field has value `us-central1-a` doesn't match the following queries.

Query | Reason for not matching  
---|---  
      
    
    location=US-central1-a

| Doesn't match because the phrase is case-sensitive. Use the `:` operator instead for case-insensitive matches.   
      
    
    location=us-central1

| Doesn't match because the phrase partially matches the field's value. Use the `:` operator instead for partial matches.   
  
## Construct a text match query

A query value can be made up of phrases, combinations, negations, and wildcards.

### Phrases

A phrase is one or more words that are matched in order. To match words without respecting order, use combinations instead.

The following query matches assets whose `policy` field has the word `alex` and the word `2020` in consecutive order:
    
    
    policy:"alex 2020"
    

An asset whose `policy` field value is `"alex.2020@example.com"` matches the query, because the words `alex` and `2020` are in consecutive order. The `.` is ignored as punctuation is treated as a delimiter.

An asset whose `policy` field value is `"2020.alex@example.com"` or `"alex.us.2020@example.com"` doesn't match, because the words `alex` and `2020` aren't in consecutive order.

#### Construct a phrase

Keep the following rules in mind when you construct a phrase:

  * If the phrase only contains ISO basic Latin alphabet characters `[a-zA-Z]`, numbers `[0-9]`, basic email or URL connectors `[_-+.@/&]`, or wildcards `[*]`, it doesn't need to be wrapped in double quotation marks:
        
        policy:alex.2020@example.com
        

However, wrapping in double quotation marks still works, and behaves the same:
        
        policy:"alex.2020@example.com"
        

  * If the phrase has spaces or other special characters it must be wrapped in double quotation marks:
        
        location:"us central1"
        

  * If the phrase is wrapped in double quotation marks and also contains a double quotation mark (`"`) or backslash (`\`), you must escape them as `\"` or `\\`. Alternatively, replace them with a single space as non-alphanumeric characters are treated as delimiters when performing a search. The following queries are treated the same:
        
        description:"One of \"those\" descriptions."
        description:"One of those descriptions."
        

  * When using the gcloud CLI or the REST API, you need to escape the double quotation marks used to indicate a phrase:
        
        --query="location:(a \"us central1\")"
        
        
        "query": "location:(a \"us central1\")"
        




### Combinations

Search phrases can be combined using the uppercase logical operators `AND` or `OR`. Including `AND` is optional when using parentheses. For example, the following queries are treated the same:
    
    
    policy:(alex charlie)
    policy:(alex AND charlie)
    

If an asset contains a metadata field with a list of values, an `AND` combination doesn't guarantee that all words must be in a single element. For example, if a metadata field is `policy=["alex@example.com", "bola@example.com", "charlie@example.com"]`, searching with `policy:(alex charlie)` matches, because `alex@example.com` contains `alex`, and `charlie@example.com` contains `charlie`.

You can use parentheses to group combination types. The following example returns assets that have a policy field that contains `alex` and `charlie` in any order, or assets that have a policy field that contains `bola`.
    
    
    policy:((alex charlie) OR bola)
    

You can use a phrase inside a combination to match multiple words in consecutive order. The following example returns assets that have a policy field that contains `alex` and `2020` in consecutive order, or `bola`:
    
    
    policy:(("alex 2020") OR bola)
    

#### Combination examples

The following queries demonstrate various combinations. Note the placement of parentheses to separate `AND` and `OR` operators. Combining operators within a single set of parentheses is invalid, for example: `policy:(alex charlie OR bola)`.

Query | Description | 
    
    
    policy:(alex charlie)

| Returns assets whose `policy` field contains both `alex` and `charlie`.   
---|---  
      
    
    policy:(alex OR charlie)

| Returns assets whose `policy` field contains either `alex` or `charlie`.   
      
    
    policy:((alex charlie) OR bola)

| Returns assets whose `policy` field contains both `alex` and `charlie`, or has the word `bola`.   
      
    
    policy:(alex charlie) OR name:bola

| Returns assets whose `policy` field contains `alex` and `charlie` or whose `name` field contains `bola`.   
  
### Negation

Search queries can be negated using the uppercase `NOT` operator. Parentheses are supported but not required.

**Note:** Negation is only supported when [searching resources](https://docs.cloud.google.com/asset-inventory/docs/search-resources), not IAM policies.

#### Negation examples

  * Return assets whose `state` field doesn't contain the word `running`.
        
        NOT state:running
        

  * Return assets whose `policy` field contains neither `alex` nor `charlie`.
        
        NOT policy:(alex OR charlie)
        

  * Return assets whose `networkTags` field doesn't contain `internal` or `private`.
        
        NOT (networkTags:internal OR networkTags:private)
        




### Wildcards

Asterisks (`*`) can be used in a phrase as a wildcard character. Depending on position, an asterisk can have different meanings.

  * If `*` is at the end of a phrase, it's treated as a token prefix match. For example, `"al 20*"` is equivalent to `(al* 20*)`. The order of prefixes doesn't matter.

The phrase `"al 20*"` matches a field value with a token starting with `al` (such as `alex`), and a token starting with `20` (such as `2020`).

  * For `labels`, if the whole query value only contains a single `*`—for example, `"labels.env:*"`—it represents an existence check. That is, Cloud Asset Inventory checks whether the label key `env` exist. Only the `labels` field supports existence checks.

  * If `*` is in the middle of a phrase—for example, `"compute*storage"`—it is treated as a tokenization delimiter. This query value is equivalent to `"compute storage"`.

  * If `*` is at both the beginning and the end of a phrase, for example, `"*compute storage*"`, it is treated as a tokenization delimiter. This query value is equivalent to `"compute storage"`.




## Numerical and timestamp comparison

For numerical and timestamp comparison, use comparison operators with the following syntax:
    
    
    ASSET_METADATA_FIELD**> =**QUERY
    

The available comparison operators are as follows:

  * `=`: equal to

  * `>`: greater than

  * `>=`: greater than or equal to

  * `<`: less than

  * `<=`: less than or equal to




To compare against timestamps such as those stored in the `createTime` and `updateTime` asset metadata fields, use a 64-bit signed integer (the epoch timestamp in seconds) or a UTC+0 datetime string in one of following formats:

  * `2021-01-01` (YYYY-MM-DD)

  * `"2021-01-01T00:00:00"` ("YYYY-MM-DDThh:mm:ss")




### Datetime examples

An asset whose `createTime` field has value `1609459200` (epoch timestamp of `2021-01-01T00:00:00`) matches the following queries:
    
    
    createTime=1609459200
    createTime=2021-01-01
    createTime="2021-01-01T00:00:00"
    
    createTime>1500000000
    createTime>2020-01-01
    createTime>"2020-01-01T00:00:00"
    
    createTime>=1609459200
    createTime>=2021-01-01
    createTime>="2021-01-01T00:00:00"
    
    createTime<1700000000
    createTime<2022-01-01
    createTime<"2022-01-01T00:00:00"
    
    createTime<=1609459200
    createTime<=2021-01-01
    createTime<="2021-01-01T00:00:00"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
