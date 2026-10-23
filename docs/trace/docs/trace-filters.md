---
url: https://docs.cloud.google.com/trace/docs/trace-filters/
title: Cloud Trace filters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:22.573233+00:00
---

# Cloud Trace filters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  Cloud Trace filters Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Trace filters let you query the Trace API [`list`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) method to retrieve traces that match specific criteria, such as span names, minimum latency, HTTP attributes, or labels.

These filter expressions don't apply to the **Trace Explorer** page in the Google Cloud console. In **Trace Explorer** , you can filter traces by using the predefined filters in the **Span filters** pane or by using the **Filter** bar. For more information, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## Filter overview

Trace filters consist of a sequence of comparisons called **terms**. Traces must match all the terms in the filter to be selected. For example, the following filter matches traces that have a latency of one second or more and that contain a span named `/modules.GetNumInstances`:
    
    
    +span:/modules.GetNumInstances latency:1s
    

All string comparisons are case-sensitive.

### Boolean attributes

To specify values for Boolean attributes, use `false` for false and `true` for true:
    
    
    Client:true
    

### Special characters

Simple values, that is, those that match the regular expression `[a-zA-Z0-9./_][a-zA-Z0-9./_-]*`, can be provided without quotation:
    
    
    environment:production
    path:/index.html
    error_code:200
    

Values that include other characters, including whitespace, must be enclosed in double-quote (`"`) characters:
    
    
    my-label:"Notice: This value contains spaces and a colon"
    

To search for the double-quote character or the backslash (`\`) character within a quoted string, escape the character with a backslash:
    
    
    my-label:"Notice: This value contains spaces, a colon, a \"quote\", and a backslash (\\)"
    

## Filter syntax

On this page, `NAME` refers to the name of a field, and `VALUE` refers to the value of a key-value pair. The strings `_PREFIX` and `_EXACT` are visual indications of whether a test is a prefix test or an exact match. For example, `root:[NAME_PREFIX]` means that the name of the root span must begin with `[NAME_PREFIX]`.

**Note:** Don't use the following keywords as label keys: `root`, `span`, `label`, `method`, `latency`, and `url`. Traces with these label keys can't be queried.

The remainder of this page describes the filter syntax for the Trace API.

### Request filter examples

The following list shows describes the filter terms:

`root:[NAME_PREFIX]`
    

The trace's root-span name must begin with [NAME_PREFIX]. For example, the following filter matches a trace named `"/_ah/background"`, but not one named `"/_ahx/background"`:
    
    
    root:/_ah/
    

`+root:[NAME]`
    

The trace's root-span name must be [NAME], exactly. For example:
    
    
    +root:/_ah/background
    

`[NAME_PREFIX]`
    

This syntax is a shortcut for `root:[NAME_PREFIX]`.

`+[NAME]`
    

This syntax is a shortcut for `+root:[NAME]`.

`span:[NAME_PREFIX]`
    

The trace must have at least one span whose name begins with [NAME_PREFIX]. For example:
    
    
    span:/modules.
    

`+span:[NAME]`
    

The trace must have at least one span whose name is [NAME], exactly. For example:
    
    
    +span:/modules.GetNumInstances
    

`latency:[DURATION]`
    

The trace must have an overall latency that is greater than or equal to [DURATION]. The duration is expressed as an integer followed by a unit specifier: `s` for seconds, `ms` for milliseconds, or `ns` for nanoseconds. If there is no unit specifier, then the units are milliseconds. For example, the following four durations are the same:
    
    
    12s 12000ms 12000000ns 12000
    

`label:[LABEL_KEY]`
    

The trace must contain the specified label key, exactly. The value of the label (if any) doesn't matter. For example:
    
    
    label:/http/url
    

`[LABEL_KEY]:[VALUE_PREFIX]`
    

The trace must contain the specified label key, exactly, and the value of the label must start with [VALUE_PREFIX]. For example, the following term matches traces whose App Engine version begins with `"2017"`:
    
    
    g.co/gae/app/module_version:2017
    

`+[LABEL_KEY]:[VALUE_EXACT]`
    

The trace must contain the specified label key _and_ value, exactly. For example:
    
    
    +g.co/gae/app/module_version:201750925t173233.387410594824284458
    

`method:[VALUE_PREFIX]`
    

This syntax is a shortcut for the label test `/http/method:[VALUE_PREFIX]`.

`+method:[VALUE_EXACT]`
    

This syntax is a shortcut for the label test `+/http/method:[VALUE_EXACT]`.

`url:[VALUE_PREFIX]`
    

This syntax is a shortcut for the label test `/http/url:[VALUE_PREFIX]`.

`+url:[VALUE_EXACT]`
    

This syntax is a shortcut for the label test `+/http/url:[VALUE_EXACT]`.

### Root-span search examples

To restrict the search term to only the root span, add a caret (`^`) before a search term and after the optional plus sign (`+`).

The following list shows some root-span-only search terms and their equivalences:

`^label:[LABEL_KEY]`
    This is a root-span search for `label:[LABEL_KEY]`.
`^[LABEL_KEY]:[VALUE_PREFIX]`
    This is a root-span search for `[LABEL_KEY]:[VALUE_PREFIX]`.
`+^[LABEL_KEY]:[VALUE]`
    This is a root-span search for `+[LABEL_KEY]:[VALUE]`.
`^method:[VALUE_PREFIX]`
    This is a root-span search for `method:[VALUE_PREFIX]`.
`+^method:[VALUE]`
    This is a root-span search for `+method:[VALUE]`.
`^url:[VALUE_PREFIX]`
    This is a root-span search for `url:[VALUE_PREFIX]`.
`+^url:[VALUE]`
    This is a root-span search for `+url:[VALUE]`.
`^span:[NAME_PREFIX]`
    This is equivalent to `root:[NAME_PREFIX]`.
`+^span:[NAME]`
    This is equivalent to `+root:[NAME]`.

You can further customize your search by creating a query with mixed terms. For example,
    
    
    +^url:/main /images method:200
    

matches traces when the root span label `/http/url` is exactly "/main", the root span's name is prefixed by `/images`, and any span has the label `/http/method` with a value of 200.

## Troubleshooting

The following sections describe how to resolve common issues with Trace filters.

### Slow performance

If your trace filter is complicated, then it takes longer to run and could time out. To improve performance, simplify the filter.

### No results

If your filter does not return any traces, then check the following:

  * Be sure there are no spaces in the filter except the ones that separate the comparisons.

  * Be sure the letter case and spelling of all the words in the filter are correct. For example, if you misspell a keyword such as `method:GET`, then the filter is interpreted as `label:method:GET`, which does not match any traces.

  * To test the filter terms one at a time, go to the [`list`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) API method and then use the APIs Explorer. If one of the terms returns no results, then that term might be the reason why no data is being returned.

The APIs Explorer is open when the page displays a pane titled **Try this method**. If necessary, click **Try it** , which opens the APIs Explorer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
