---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/greedy-quantifiers/
title: Antipattern: Use greedy quantifiers in the RegularExpressionProtection policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:18.237282+00:00
---

# Antipattern: Use greedy quantifiers in the RegularExpressionProtection policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/greedy-quantifiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Use greedy quantifiers in the RegularExpressionProtection policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/greedy-quantifiers) documentation._

The [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) defines regular expressions that are evaluated at runtime on input parameters or flow variables. You typically use this policy to protect against content threats like SQL orJavaScript injection, or to check against malformed request parameters like email addresses or URLs.

The regular expressions can be defined for request paths, query parameters, form parameters, headers, XML elements (in an XML payload defined using XPath), JSON object attributes (in a JSON payload defined using JSONPath).

The following example RegularExpressionProtection policy protects the backend from SQL injection attacks:
    
    
    <!-- /antipatterns/examples/greedy-1.xml -->
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true"
      name="RegexProtection">
        <DisplayName>RegexProtection</DisplayName>
        <Properties/>
        <Source>request</Source>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <QueryParam name="query">
          <Pattern>[\s]*(?i)((delete)|(exec)|(drop\s*table)|
            (insert)|(shutdown)|(update)|(\bor\b))</Pattern>
        </QueryParam>
    </RegularExpressionProtection>

## Antipattern

The default quantifiers (`*`, `+`, and `?`) are greedy in nature: they start to match with the longest possible sequence. When no match is found, they backtrack gradually to try to match the pattern. If the resultant string matching the pattern is very short, then using greedy quantifiers can take more time than necessary. This is especially true if the payload is large (in the tens or hundreds of KBs).

The following example expression uses multiple instances of `.*`, which are greedy operators:
    
    
    <Pattern>.*Exception in thread.*</Pattern>

In this example, the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) first tries to match the longest possible sequence—the entire string. If no match is found, the policy then backtracks gradually. If the matching string is close to the start or middle of the payload, then using a greedy quantifier like `.*` can take a lot more time and processing power than reluctant qualifiers like `.*?` or (less commonly) possessive quantifiers like `.*+`. 

Reluctant quantifiers (like `X*?`, `X+?`, `X??`) start by trying to match a single character from the beginning of the payload and gradually add characters. Possessive quantifiers (like `X?+`, `X*+`, `X++`) try to match the entire payload only once.

Given the following sample text for the above pattern:
    
    
    Hello this is a sample text with Exception in thread
    with lot of text after the Exception text.

Using the greedy `.*` is non-performant in this case. The pattern `.*Exception in thread.*` takes 141 steps to match. If you used the pattern `.*?Exception in thread.*` (which uses a reluctant quantifier) instead, the result would be only 55 steps.

## Impact

Using greedy quantifiers like wildcards (`*`) with the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) can lead to:

  * An increase in overall latency for API requests for a moderate payload size (up to 1MB)
  * Longer time to complete the execution of the RegularExpressionProtection policy
  * API requests with large payloads (>1MB) failing with 504 Gateway Timeout Errors if the predefined timeout period elapses on the Apigee Router
  * High CPU utilization on Message Processors due to large amount of processing which can further impact other API requests



## Best practice

  * Avoid using greedy quantifiers like `.*` in regular expressions with the [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection). Instead, use reluctant quantifiers like `.*?` or possessive quantifiers like `.*+` (less commonly) wherever possible.



## Further reading

  * [ Regular Expression Quantifiers](https://docs.oracle.com/javase/tutorial/essential/regex/quant.html)
  * [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
