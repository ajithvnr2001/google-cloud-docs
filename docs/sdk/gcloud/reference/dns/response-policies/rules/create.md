---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create/
title: gcloud dns response-policies rules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:03:07.233558+00:00
---

# gcloud dns response-policies rules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns response-policies rules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns response-policies rules create - creates a new Cloud DNS response policy rule 
SYNOPSIS
    

`gcloud dns response-policies rules create` (`RESPONSE_POLICY_RULE` : `--response-policy`=`RESPONSE_POLICY`) `--dns-name`=`DNS_NAME` [`--behavior`=`BEHAVIOR`] [`--local-data`=[`LOCAL_DATA`,…]] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a new response policy rule with local data rrsets, run: 
    
    
    gcloud dns response-policies rules create myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --local-data=name=www.zone.com.,type=CNAME,ttl=21600,rrdatas=zone.com.

To create a new response policy rule with behavior, run: 
    
    
    gcloud dns response-policies rules create myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --behavior=bypassResponsePolicy

To create a new response policy rule with behavior in a zonal response policy in us-east1-a, run: 
    
    
    gcloud dns response-policies rules create myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --behavior=bypassResponsePolicy --location=us-east1-a

POSITIONAL ARGUMENTS
    

Response policy rule resource - The response policy rule to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `response_policy_rule` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`RESPONSE_POLICY_RULE`
     ID of the response_policy_rule or fully qualified identifier for the response_policy_rule. 

To set the `response-policy-rule` attribute: 

  * provide the argument `response_policy_rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--response-policy`=`RESPONSE_POLICY`
     The Cloud DNS response policy name response_policy_rule. 

To set the `response-policy` attribute: 

  * provide the argument `response_policy_rule` on the command line with a fully specified name; 
  * provide the argument `--response-policy` on the command line. 


REQUIRED FLAGS
    

`--dns-name`=`DNS_NAME`
     DNS name (wildcard or exact) to apply this rule to. 
OPTIONAL FLAGS
    

`--behavior`=`BEHAVIOR`
     The response policy rule query behavior. `BEHAVIOR` must be one of: `behaviorUnspecified`, `bypassResponsePolicy`. 
`--local-data`=[`LOCAL_DATA`,…]
     All resource record sets for this selector, one per resource record type. The name must match the dns_name. 

This is a repeated argument that can be specified multiple times to specify multiple local data rrsets. (e.g. \--local-data=name="zone.com.",type="A",ttl=21600,rrdata="1.2.3.4 " \--local-data=name="www.zone.com.",type="CNAME",ttl=21600,rrdata="1.2.3.4|5.6.7.8") 

`name`
     The DnsName of a resource record set. 
`type`
     Type of all resource records in this set. For example, A, AAAA, SOA, MX, NS, TXT … 
`ttl`
     Number of seconds that this ResourceRecordSet can be cached by resolvers. 
`rrdatas`
     The list of datas for this record, split by "|". 
`--location`=`LOCATION`
     Specifies the desired service location the request is sent to. Defaults to Cloud DNS global service. Use --location=global if you want to target the global service. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns response-policies rules create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/response-policies/rules/create)
    
    
    [gcloud beta dns response-policies rules create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/response-policies/rules/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
