---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable/
title: gapic-common - Class Gapic::Rest::PagedEnumerable (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:13.003061+00:00
---

# gapic-common - Class Gapic::Rest::PagedEnumerable (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::PagedEnumerable (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::PagedEnumerable.

A class to provide the Enumerable interface to the response of a REST paginated method. PagedEnumerable assumes response message holds a list of resources and the token to the next page.

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
    
    
    def each(&block) -> Enumerator

Iterate over the individual resources, automatically requesting new pages as needed.

**Yields**

  * (Object) — Gives the resource objects in the stream. 



**Returns**

  * (Enumerator) — if no block is provided 



### #each_page
    
    
    def each_page() -> Enumerator

Iterate over the pages.

**Yields**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable-Page)) — Gives the pages in the stream. 



**Returns**

  * (Enumerator) — if no block is provided 



### #next_page
    
    
    def next_page() -> Page, nil

**Alias Of** : [#next_page!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable#Gapic__Rest__PagedEnumerable_next_page!_instance_)

Load the next page and set it as the current page. If there is no next page, sets nil as a current page.

**Returns**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable-Page), nil) — the new page object. 



### #next_page!
    
    
    def next_page!() -> Page, nil

**Aliases**

  * [#next_page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable#Gapic__Rest__PagedEnumerable_next_page_instance_)



Load the next page and set it as the current page. If there is no next page, sets nil as a current page.

**Returns**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable-Page), nil) — the new page object. 



### #next_page?
    
    
    def next_page?() -> Boolean

True if there is at least one more page of results.

**Returns**

  * (Boolean) 



### #next_page_token
    
    
    def next_page_token() -> String, nil

The page token to be used for the next RPC call, or the empty string if there is no next page. nil if the iteration is complete.

**Returns**

  * (String, nil) 



### #page
    
    
    def page() -> Page

**Returns**

  * ([Page](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-PagedEnumerable-Page)) — The current page object. 



### #response
    
    
    def response() -> Object, nil

The current response object, for the current page. nil if the iteration is complete.

**Returns**

  * (Object, nil) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
