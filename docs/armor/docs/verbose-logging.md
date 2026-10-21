---
url: https://docs.cloud.google.com/armor/docs/verbose-logging/
title: Verbose logging \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:19.837962+00:00
---

# Verbose logging  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/verbose-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Verbose logging Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about configuring verbose logging, an optional feature that you can use with your Google Cloud Armor security policies.

You can adjust the level of detail recorded in your logs. We recommend that you enable verbose logging only when you first create a policy, make changes to a policy, or troubleshoot a policy. If you enable verbose logging, it is in effect for rules in preview mode as well as enforced rules during standard operations.

Consider an example where you can't tell why a preconfigured web application firewall (WAF) rule is triggered by a particular request. Cloud Armor's default event logs contain the rule that was triggered, as well as the subsignature. However, you might need to identify the details from the incoming request that triggered the rule for troubleshooting, rule validation, or rule tuning purposes. For this example, we recommend that you enable verbose logging.

You can configure the Cloud Armor logging level to enable more detailed logging for each security policy by using the `--log-level` flag in the Google Cloud CLI.

By default, this option is disabled. You can configure the logging level with one of the following options for the `--log-level` flag:

  * `NORMAL`: The default logging level. By default, Cloud Armor returns the priority and, if applicable, the signature ID of the matching rule.
  * `VERBOSE`: Enables verbose logging. When verbose logging is enabled, additional information is logged to Cloud Logging for requests that match a preconfigured WAF rule. This applies to rules in preview mode and enforced rules.



The flag is available only by using the `gcloud compute security-policies update` command. You can't create a new security policy with this option unless you create a security policy in a file and then import that file. For more information, see [Import security policies](https://docs.cloud.google.com/armor/docs/manage-security-policies#importing-policies).

For example, you can update a security policy to enable verbose logging:
    
    
    gcloud compute security-policies update ca-policy-1 \
        --log-level=VERBOSE
    

We recommend that you enable verbose logging when you first create a policy, make changes to a policy, or troubleshoot a policy.

### Values logged when verbose logging is enabled

When verbose logging is enabled, additional information is logged to the load balancing request log that is sent to Cloud Logging. The following additional fields appear in the request log when verbose logging is enabled:

  * `matchedFieldType` (string): this is the type of field causing the match.

    * `ARG_NAMES`
    * `ARG_VALUES`
    * `BODY`
**Note:** When the `BODY` field is in the log, it means that the entire request body matches a rule.
    * `COOKIE_VALUES`
    * `COOKIE_NAMES`
    * `FILENAME`
    * `HEADER_VALUES`
    * `RAW_URI`
    * `REFERER`
    * `REQUEST_LINE`
    * `URI`
    * `USER_AGENT`
    * `HEADER_NAMES`
    * `ARGS_GET`
    * `X_FILENAME`
    * `ARG_NAME_COUNT`
    * `TRANSFER_ENCODING`
    * `REQUEST_METHOD`
    * `request.body`
    * `request.headers`
    * `request.method`
    * `request.params`
    * `request.path`
    * `request.scheme`
  * `matchedFieldName` (string): if this matches the value part of a key-value pair, the key value is stored in this field. Otherwise, it is empty.

  * `matchedFieldValue` (string): a prefix for the part of the field that causes the match. For preconfigured WAF rules, this logs a prefix of up to 16 bytes. For managed rules, this limit increases to 8 KB of the payload to provide improved troubleshooting context.

  * `matchedFieldLength` (integer): the total length of the field.

  * `matchedOffset` (integer): the start offset inside the field that causes the match.

  * `matchedLength` (integer): the length of the match.

  * `inspectedBodySize` (integer): the configured inspection limit (number of bytes) for a request body that you set by using the `--request-body-inspection-size` flag. For more information about this limit, see [Request body inspection limitation](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body).


**Note:** These additional fields are populated in the logs only for requests that or a managed rule.

For example, you might send the following request to a project where SQL injection WAF rules are enabled:
    
    
    curl http://IP_ADDR/?sql_table=abc%20pg_catalog%20xyz
    

The entry in the Logs Explorer is similar to the following:
    
    
    enforcedSecurityPolicy: {
     name: "user-staging-sec-policy"
     priority: 100
     configuredAction: "DENY"
     outcome: "DENY
     inspectedBodySize: 65536
     preconfiguredExprIds: [
       0: "owasp-crs-v042200-id942140-sqli"
      ]
    matchedFieldType: "ARG_VALUES"
    matchedFieldName: "sql_table"
    matchedFieldValue: "pg_catalog"
    matchedFieldLength: 18
    matchedOffset: 4
    matchedLength: 10
    }
    

### Maintaining privacy when verbose logging is turned on

When you use verbose logging, Cloud Armor logs snippets of the elements from the incoming requests that triggered a particular preconfigured WAF rule. These snippets might contain pieces of request headers, request parameters, or elements of the request body. A snippet can contain sensitive data such as an IP address or other sensitive data from the incoming request, depending on what is in the request headers or body and what triggers the WAF rule.

**Note:** Verbose logging applies only to requests matched by preconfigured WAF rules, not to custom rules.

When you enable verbose logging, there is a risk of accumulating potentially sensitive data in your logs in Logging. We recommend that you enable verbose logging only during rule creation and validation or for troubleshooting. During normal operations, we recommend that you leave verbose logging disabled.

## What's next

  * [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies)
  * [Use request logging](https://docs.cloud.google.com/armor/docs/request-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
