---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/add-preconfig-waf-exclusion/
title: gcloud compute security-policies rules add-preconfig-waf-exclusion \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:57:24.082394+00:00
---

# gcloud compute security-policies rules add-preconfig-waf-exclusion  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/add-preconfig-waf-exclusion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute security-policies rules add-preconfig-waf-exclusion Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute security-policies rules add-preconfig-waf-exclusion - add an exclusion configuration for preconfigured WAF evaluation into a security policy rule 
SYNOPSIS
    

`gcloud compute security-policies rules add-preconfig-waf-exclusion` `PRIORITY` `--target-rule-set`=`TARGET_RULE_SET` [`--region`=`REGION`] [`--request-body-to-exclude`=[`op`=`OP`],[`val`=`VAL`]] [`--request-cookie-to-exclude`=[`op`=`OP`],[`val`=`VAL`]] [`--request-header-to-exclude`=[`op`=`OP`],[`val`=`VAL`]] [`--request-query-param-to-exclude`=[`op`=`OP`],[`val`=`VAL`]] [`--request-uri-to-exclude`=[`op`=`OP`],[`val`=`VAL`]] [`--security-policy`=`SECURITY_POLICY`] [`--target-rule-ids`=[`RULE_ID`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute security-policies rules add-preconfig-waf-exclusion` is used to add an exclusion configuration for preconfigured WAF evaluation into a security policy rule. 

Note that request field exclusions are associated with a target, which can be a single rule set, or a rule set plus a list of rule IDs under the rule set. 

EXAMPLES
     To add specific request field exclusions that are associated with the target of 'sqli-stable': ['owasp-crs-v030001-id942110-sqli', 'owasp-crs-v030001-id942120-sqli'], run: 
    
    
    [gcloud compute security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules) add-preconfig-waf-exclusion 1000 --security-policy=my-policy --target-rule-set=sqli-stable --target-rule-ids=owasp-crs-v030001-id942110-sqli,owasp-crs-v030001-id942120-sqli --request-header-to-exclude=op=EQUALS,val=abc --request-header-to-exclude=op=STARTS_WITH,val=xyz --request-uri-to-exclude=op=EQUALS_ANY --request-body-to-exclude=op=CONTAINS,val=bad_data

To add specific request field exclusions that are associated with the target of 'sqli-stable': [], run: 
    
    
    [gcloud compute security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules) add-preconfig-waf-exclusion 1000 --security-policy=my-policy --target-rule-set=sqli-stable --request-cookie-to-exclude=op=EQUALS_ANY

POSITIONAL ARGUMENTS
    

`PRIORITY`
     The priority of the rule to add the exclusion configuration for preconfigured WAF evaluation. Rules are evaluated in order from highest priority to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. 
REQUIRED FLAGS
    

`--target-rule-set`=`TARGET_RULE_SET`
     Target WAF rule set where the request field exclusions being added would apply. 

This, together with the target rule IDs (if given), determines the target for associating request field exclusions. See `--target-rule-ids`. 

OPTIONAL FLAGS
    

`--region`=`REGION`
     Region of the security policy to add the exclusion configuration for preconfigured WAF evaluation. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--request-body-to-exclude`=[`op`=`OP`],[`val`=`VAL`]
     Adds a request body to the request field exclusions associated with the rule set and rule IDs (if provided). This flag specifies a request body to exclude from inspection during preconfigured WAF evaluation. 

For syntax, see `--request-cookie-to-exclude`. 

You can repeat this flag to specify multiple request bodies. 

`--request-cookie-to-exclude`=[`op`=`OP`],[`val`=`VAL`]
     Adds a request cookie to the request field exclusions associated with the rule set and rule IDs (if given). This specifies a request cookie whose value will be excluded from inspection during preconfigured WAF evaluation. 

You can specify an exact match or a partial match by using a field operator and a field value. Available field operators are: 

  * ``EQUALS``: the operator matches if the field value equals the specified value. 
  * ``STARTS_WITH``: the operator matches if the field value starts with the specified value. 
  * ``ENDS_WITH``: the operator matches if the field value ends with the specified value. 
  * ``CONTAINS``: the operator matches if the field value contains the specified value. 
  * ``EQUALS_ANY``: the operator matches if the field value is any value. 



A field value must be given if the field operator is not ``EQUALS_ANY``, and cannot be given if the field operator is ``EQUALS_ANY``. For example, `--request-header-to-exclude op=EQUALS,val=abc` or `--request-header-to-exclude op=EQUALS_ANY`. 

This flag can be repeated to specify multiple request headers to exclude. For example, `--request-header-to-exclude op=EQUALS,val=abc --request-header-to-exclude op=STARTS_WITH,val=xyz`. 

`--request-header-to-exclude`=[`op`=`OP`],[`val`=`VAL`]
     Adds a request header to the request field exclusions associated with the rule set and rule IDs (if given). This specifies a request header whose value will be excluded from inspection during preconfigured WAF evaluation. 

Refer to the syntax under `--request-cookie-to-exclude`. 

This flag can be repeated to specify multiple request headers. 

`--request-query-param-to-exclude`=[`op`=`OP`],[`val`=`VAL`]
     Adds a request query parameter to the request field exclusions associated with the rule set and rule IDs (if given). This specifies a request query parameter in the query string or in the POST body whose value will be excluded from inspection during preconfigured WAF evaluation. 

Refer to the syntax under `--request-cookie-to-exclude`. 

This flag can be repeated to specify multiple request query parameters. 

`--request-uri-to-exclude`=[`op`=`OP`],[`val`=`VAL`]
     Adds a request URI to the request field exclusions associated with the rule set and rule IDs (if given). This specifies a request URI from the request line to be excluded from inspection during preconfigured WAF evaluation. 

Refer to the syntax under `--request-cookie-to-exclude`. 

This flag can be repeated to specify multiple request URIs. 

`--security-policy`=`SECURITY_POLICY`
     The security policy that this rule belongs to. 
`--target-rule-ids`=[`RULE_ID`,…]
     A comma-separated list of target rule IDs under the WAF rule set where the request field exclusions being added would apply. If omitted, the added request field exclusions will be associated with the rule set only, which would apply to all the rule IDs under the rule set. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies/rules) add-preconfig-waf-exclusion
    
    
    [gcloud beta compute security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies/rules) add-preconfig-waf-exclusion
    
    
    [gcloud preview compute security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/rules) add-preconfig-waf-exclusion

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
