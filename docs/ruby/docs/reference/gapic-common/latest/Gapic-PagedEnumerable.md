---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable/
title: gapic-common - Class Gapic::PagedEnumerable (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:11.938438+00:00
---

# gapic-common - Class Gapic::PagedEnumerable (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::PagedEnumerable (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::PagedEnumerable.

A class to provide the Enumerable interface to the response of a paginated method. PagedEnumerable assumes response message holds a list of resources and the token to the next page.

PagedEnumerable provides the enumerations over the resource data, and also provides the enumerations over the pages themselves.

## Inherits

  * Object 



## Includes

  * Enumerable 



## Examples

normal iteration over resources.
    
    
    paged_enumerable.each { |resource| puts resource }

per-page iteration.
    
    
    paged_enumerable.each_page { |page| puts page }

Enumerable over pages.
    
    
    paged_enumerable.each_page do |page|
      page.each { |resource| puts resource }
    end

more exact operations over pages.
    
    
    while some_condition()
      page = paged_enumerable.page
      do_something(page)
      break if paged_enumerable.next_page?
      paged_enumerable.next_page
    end

## Methods 

### #each
    
    
    def each(&block)

Iterate over the resources.

**Yields**

  * (Object) — Gives the resource objects in the stream. 



**Raises**

  * (RuntimeError) — if it's not started yet. 



### #each_page
    
    
    def each_page()

Iterate over the pages.

**Yields**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable-Page)) — Gives the pages in the stream. 



**Raises**

  * — if it's not started yet. 



### #next_page
    
    
    def next_page() -> Page

**Alias Of** : [#next_page!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable#Gapic__PagedEnumerable_next_page!_instance_)

Update the response in the current page.

**Returns**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable-Page)) — the new page object. 



### #next_page!
    
    
    def next_page!() -> Page

**Aliases**

  * [#next_page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable#Gapic__PagedEnumerable_next_page_instance_)



Update the response in the current page.

**Returns**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-PagedEnumerable-Page)) — the new page object. 



### #next_page?
    
    
    def next_page?() -> Boolean

True if it has the next page.

**Returns**

  * (Boolean) 



### #next_page_token
    
    
    def next_page_token() -> String

The page token to be used for the next RPC call.

**Returns**

  * (String) 



### #page
    
    
    def page()

Returns the value of attribute page.

### #response
    
    
    def response() -> Object

The current response object, for the current page.

**Returns**

  * (Object) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
