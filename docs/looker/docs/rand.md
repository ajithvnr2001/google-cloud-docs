---
url: https://docs.cloud.google.com/looker/docs/rand/
title: rand \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:24.351932+00:00
---

# rand  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/rand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  rand Stay organized with collections  Save and categorize content based on your preferences. 

The `rand` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to return a random number between 0 and 1.

## Syntax

**`rand()`**

The `rand` function returns a random number between 0 and 1.

## Examples

The `rand` function is often used to generate random integers, sometimes to select a random sampling of data. For example, to generate an integer between 1 and 100 (inclusive) you could use:
    
    
    (floor(rand()*100)+1)
    

This expression works as follows:

  1. Uses the `rand()` function to generate a random number between 0 and 1.
  2. Multiplies by 100 to turn it into a random number between 1 and 100.
  3. Uses the [`floor`](https://docs.cloud.google.com/looker/docs/functions-and-operators#function-floor) function to round down the random number to the nearest integer, producing a random number between 0 and 99 (inclusive).
  4. Adds 1 to bring the random integer up to 1 to 100 (inclusive).



You could then filter your query to only include data below a certain random number.

## Things to know

The `rand` function produces a number with 16 decimal places, such as 0.04277424614631747.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
