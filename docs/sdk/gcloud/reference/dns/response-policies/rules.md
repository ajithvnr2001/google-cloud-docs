---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/
title: gcloud dns response-policies rules \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:50.521945+00:00
---

# gcloud dns response-policies rules  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns response-policies rules Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns response-policies rules - manage your Cloud DNS response policy rules 
SYNOPSIS
    

`gcloud dns response-policies rules` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a new response policy rule with local data rrsets, run: 
    
    
    gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --local-data=name=www.zone.com.,type=CNAME,ttl=21600,rrdatas=zone.com.

To create a new response policy rule with behavior, run: 
    
    
    gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --behavior=bypassResponsePolicy

To update a new response policy rule with local data rrsets, run: 
    
    
    gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --local-data=name=www.zone.com.,type=A,ttl=21600,rrdatas=1.2.3.4

To update a new response policy rule with behavior, run: 
    
    
    gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --behavior=bypassResponsePolicy

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create)`
     Creates a new Cloud DNS response policy rule. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete)`
     Deletes a Cloud DNS response policy rule. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/describe)`
     Shows details about a Cloud DNS response policy rule. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/list)`
     Displays the list of all a Cloud DNS response policy rules. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update)`
     Updates a new Cloud DNS response policy rule. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns response-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/response-policies/rules)
    
    
    [gcloud beta dns response-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/response-policies/rules)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
