---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/escaping/
title: gcloud alpha topic escaping \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:04.530162+00:00
---

# gcloud alpha topic escaping  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/escaping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha topic escaping Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha topic escaping - list/dictionary-type argument escaping supplementary help 
DESCRIPTION
     `(ALPHA)` List/dictionary-type argument escaping supplementary help. 

`gcloud` supports list-type and dictionary-type flags that take one argument which is a list of one or more comma-separated items: 
    
    
    --list-flag=value1,value2,value3
    
    
    --dict-flag=key1=value1,key2=value2

In the case of a dict-type flag, each item is a key-value pair separated by '='. If more than one '=' is present, the first is used. 

In order to include commas in your arguments, specify an alternate delimiter using the following syntax: 
    
    
    ^DELIM^flag value, with comma

where `DELIM` is a sequence of one or more characters that may not appear in any value in the list. 

NOTE: In cmd.exe and PowerShell on Windows, `^` is a special character and you must escape it by repeating it. In the following examples, every time you see `^`, replace it with `^^^^`. 

EXAMPLES
     In these examples, a list-type or dictionary-type flag is given, along with a shell comment explaining how it is parsed. The parsed flags are shown here using Python-style list or dict formats (in other languages, what Python calls "dicts" are often called "associative arrays," "maps," or "hashes"). 

Basic example: 
    
    
    --list-flag=^:^a,b:c,d # => ['a,b', 'c,d']

Multi-character delimiters are allowed: 
    
    
    --list-flag=^--^a-,b--c # => ['a-,b', 'c']

Just one '^' has no special meaning: 
    
    
    --list-flag=^a,b,c # => ['^a', 'b', 'c']

This is an alternative way of starting with '^': 
    
    
    --list-flag=^,^^a,b,c # => ['^a', 'b', 'c']

A '^' anywhere but the start has no special meaning: 
    
    
    --list-flag=a^:^,b,c # => ['a^:^', 'b', 'c']

Dictionary-type arguments work exactly the same as list-type arguments: 
    
    
    --dict-flag=^:^a=b,c:d=f,g # => {'a': 'b,c', 'd': 'f,g'}

To reserve ephemeral IP addresses, passed in as a list, which are being used by virtual machine instances in the us-central1 region, run: 
    
    
    [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) --addresses ^:^123.456.789.198:22.333.146.189:789.312.645 --region us-central1

To create a Google Compute Engine virtual machine instance with metadata as a list ({'key1': '"value1"', 'key2': 'value2', 'key3': 'value3Index1,value3Index2', 'key4': 'value4'), run: 
    
    
    [gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) example-instance1 --metadata ^:^key1="value1":key2=value2:key3=value3Index1,value3Index2,valueIndex3:key4=value4

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping)
    
    
    [gcloud beta topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/escaping)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
