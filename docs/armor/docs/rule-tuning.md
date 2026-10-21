---
url: https://docs.cloud.google.com/armor/docs/rule-tuning/
title: Tune preconfigured WAF rules \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:02.682999+00:00
---

# Tune preconfigured WAF rules  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/rule-tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Tune preconfigured WAF rules Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor helps protect your services against distributed denial-of-service (DDoS) and web attacks by using Google's global infrastructure and security systems. You can tune Cloud Armor [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) to customize how they evaluate incoming requests, refine threat detection, and reduce false positives. This page describes how to choose sensitivity levels, opt in to or opt out of rule signatures, and exclude request fields from inspection.

Preconfigured WAF rules consist of multiple signatures sourced from the [OWASP Core Rule Set](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) . Each signature corresponds to an attack detection rule. By tuning these rules, you can customize how they evaluate incoming requests to better suit your application's specific traffic patterns. You can tune preconfigured WAF rules in [ hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview) that you own. If your service inherits a hierarchical security policy, you cannot tune its rules.

## Choose a sensitivity level

Each signature has a sensitivity level that corresponds to an OWASP [paranoia level](https://coreruleset.org/20211028/working-with-paranoia-levels/). You can select a sensitivity between `0` and `4`, though sensitivity level `0` means that no rules are enabled.

A lower sensitivity level indicates higher confidence signatures, which are less likely to generate a false positive. By default, Cloud Armor is configured to run at sensitivity level 4, and will evaluate all signatures in a rule set once enabled. A higher sensitivity level increases security, but also increases the risk of generating a false positive. When you select a sensitivity level for your preconfigured WAF rule, you opt in signatures at the sensitivity levels less than or equal to the selected sensitivity level. In the following example, you tune a preconfigured WAF rule by selecting the sensitivity level of `1`:

**Note:** A false positive occurs when a preconfigured WAF rule incorrectly identifies a legitimate query as a threat. This leads to a match, and the rule then blocks the query.
    
    
    evaluatePreconfiguredWaf(
      'sqli-v422-stable',
      {
        'sensitivity': 1
      }
    )
    

## Opt out rule signatures

If you decide that a preconfigured WAF rule matches more requests than is necessary, or if the rule is blocking traffic that needs to be allowed, the rule can be tuned to disable noisy or otherwise unnecessary signatures. To disable signatures in a particular preconfigured WAF rule, you provide a list of IDs of the unwanted signatures to the `evaluatePreconfiguredWaf` expression.

The following example excludes two CRS rule IDs from the preconfigured `sqli-v422-stable` (CRS 4.22) WAF rule:
    
    
    evaluatePreconfiguredWaf(
      'sqli-v422-stable',
      {
        'sensitivity': 4,
        'opt_out_rule_ids': ['owasp-crs-v042200-id942350-sqli', 'owasp-crs-v042200-id942360-sqli']
      }
    )
    

When you opt out signature IDs from preconfigured CRS rule sets, you must match the signature ID version with the rule set version (CRS 3.0 or 3.3) to avoid configuration errors.

For more information about preconfigured WAF rule expressions, see the [custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#preconfigured-operator).

## Opt in rule signatures

Instead of opting out rule signatures, you can opt in rule signatures in otherwise disabled sensitivity levels. We recommend that you opt in rule signatures when there are fewer signatures that you want to use in a given sensitivity level than there are rules that you want to opt out. To opt in rule signatures, the sensitivity level must be `0`. The following example opts out all `cve-canary` signatures at all sensitivity levels, and then explicitly opts in `owasp-crs-v042200-id044228-cve` and `owasp-crs-v042200-id144228-cve`:
    
    
    evaluatePreconfiguredWaf(
      'cve-canary',
      {
        'sensitivity': 0,
        'opt_in_rule_ids': ['owasp-crs-v042200-id044228-cve', 'owasp-crs-v042200-id144228-cve']
      }
    )
    

## Exclude request fields from inspection

Custom applications sometimes contain legitimate content in request fields (such as headers, cookies, query parameters, URIs, or request bodies) that matches signatures in preconfigured WAF rules. To reduce false positives, exclude these request fields from inspection by adding a list of exclusions to the security policy rule. Note that when you have a request field exclusion attached to a WAF rule, you can't use the `allow` action.

When you configure a request field exclusion, you associate it with a target. A target can be all rule sets (a global exclusion), an entire preconfigured WAF rule, or a list of signatures under a preconfigured WAF rule. Use a field operator and a field value to specify an exact or partial match. The available field operators are as follows:

  * `EQUALS`: the operator matches if the field value equals the specified value.
  * `STARTS_WITH`: the operator matches if the field value starts with the specified value.
  * `ENDS_WITH`: the operator matches if the field value ends with the specified value.
  * `CONTAINS`: the operator matches if the field value contains the specified value.
  * `EQUALS_ANY`: the operator matches if the field value is any value.



### Tuning exclusion limit

The default tuning exclusion limit is 100 for service-level backend policies (both global and regional). This limit applies per target and controls the maximum number of exclusions you can configure, within a security policy rule. A target is the combination of a rule set and a rule ID. The limit applies to exclusions for the following fields:

  * Request headers
  * Request cookies
  * Request query parameters
  * Request URIs
  * Request bodies



For example, if you have a preconfigured WAF rule (such as `evaluatePreconfiguredWaf('sqli-v422-stable')`), and you want to exclude request fields on a specific target (such as `owasp-crs-v042200-id942100-sqli` under `sqli-v422-stable`), you can configure up to 100 request headers, 100 request cookies, 100 request query parameters, 100 request URIs, and 100 request bodies to be excluded for that target.

The following sections describe global exclusions, the request fields you can exclude from inspection, and examples.

### Global exclusions

To apply an exclusion to all rule sets under a security policy rule, specify a global exclusion by setting the --target-rule-set flag to "*". You can use a global exclusion to exclude any request field type, such as headers, cookies, query parameters, URIs, or request bodies. Don't specify target rule IDs for a global exclusion.

### Request headers

A list of request header names whose value is excluded from inspection during preconfigured WAF rule evaluation.

The exclusion is only applicable for signatures in the target that would inspect the request header value originally. This includes signatures that are associated with the following request flag in the OWASP Core Rule Set:

  * `REQUEST_HEADERS`



Only the value of the specified request headers are excluded from inspection. The name is still inspected.

### Request cookies

A list of request cookie names whose value is excluded from inspection during preconfigured WAF rule evaluation.

The exclusion is only applicable for signatures in the target that would inspect the request cookie value originally. This includes signatures that are associated with the following request flag in the OWASP Core Rule Set:

  * `REQUEST_COOKIES`



Only the value of the specified request cookies are excluded from inspection. The name is still inspected.

### Request query parameters

A list of request query parameter names whose value is excluded from inspection during preconfigured WAF rule evaluation.

The exclusion is only applicable for signatures in the target that would inspect the request parameters originally. This includes signatures that are associated with the following request flags in the OWASP Core Rule Set:

  * `ARGS`
  * `ARGS_GET`
  * `REQUEST_URI`
  * `REQUEST_URI_RAW`
  * `REQUEST_LINE`



Only the value of the specified query parameters are excluded from inspection, which can be in the query string or the request body. The name is still inspected.

Because query parameters are part of the URI and the request line, these fields are re-assembled for inspection after excluding the specified query parameters. However, for signatures that inspect the entire request body (like signatures that are associated with the request flag `REQUEST_BODY`), the exclusion for query parameters isn't applied.

For example, if you exclude a query parameter named "args", you might still see a match on a signature that inspects the entire request body if the request has an "args" parameter in the request body and the value of "args" matches.

### Request URIs

A list of URIs from the request line excluding the query string data to be excluded from inspection during preconfigured WAF rule evaluation.

The exclusion is only applicable for signatures in the target that would inspect the request URI originally. This includes signatures that are associated with the following request flags in the OWASP Core Rule Set:

  * `REQUEST_URI`
  * `REQUEST_URI_RAW`
  * `REQUEST_LINE`
  * `REQUEST_FILENAME`
  * `REQUEST_BASENAME`



When excluding any of the preceding fields, the field is excluded entirely from inspection, and no re-assembling is performed.

### Request bodies

Specifies the request body values to exclude from inspection during preconfigured WAF rule evaluation.

This exclusion applies only to signatures in the target that inspect the request body value, such as signatures associated with the `REQUEST_BODY` request flag in the OWASP Core Rule Set.

Only request bodies that match the specified value are excluded from inspection.

### Field values

You must specify a field value if you use a field operator other than `EQUALS_ANY`.

For request headers, request cookies, and request query parameters, the permitted character set for field values includes the following characters:

  * `!`, `#`, `$`, `%`, `&`, `*`, `+`, `-`, `.`, `^`, `_`, ```, `|`, `~`
  * Alpha characters `A` through `Z` (both uppercase and lowercase)
  * Digit characters `0` through `9`



For request bodies, the permitted character set for field values includes all printable ASCII characters except `'`, `\`,`(`, and`)`:

  * Space (``) and special characters: `!`, `"`, `#`, `$`, `%`, `&`, `*`, `+`, `,`, `-`, `.`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `[`, `]`, `^`, `_`, ```, `{`, `|`, `}`, `~`
  * Alpha characters `A` through `Z` (both uppercase and lowercase)
  * Digit characters `0` through `9`



When applying exclusions for these request fields, the configured field values are compared as they are against the values (case-insensitive, after transformation) from the request. You are not expected to perform additional encoding if you want to exclude a specific character that's not in the permitted character set.

For request URIs, the field value must be given in a URI format as follows:

  * A scheme is allowed, but is restricted to http or https only.
  * A host is allowed, and can be an IP address.
  * A port is allowed.
  * A path is allowed.
  * A query isn't allowed.
  * A fragment isn't allowed.



When applying exclusions for request URIs, the configured field values are compared as they are against the URIs (case-insensitive, after transformation) from the request line, excluding the query string. The URIs from the request line can be relative or absolute. Consider this when configuring exclusions for request URIs.

### Examples

The first example updates the rule in the security policy `POLICY_1` at `PRIORITY` to add a global exclusion configuration for all rule sets. This excludes request bodies that contain `bad-body-value` from inspection:
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_1 \
        --target-rule-set "*" \
        --request-body-to-exclude "op=CONTAINS,val=bad-body-value"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_1`: the name of the security policy



The second example updates the rule in the security policy `POLICY_2` at `PRIORITY` to add an exclusion configuration for all signatures under the `sqli-v422-stable` preconfigured WAF rule, to exclude all request cookies from inspection:
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_2 \
        --target-rule-set "sqli-v422-stable" \
        --request-cookie-to-exclude "op=EQUALS_ANY"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_2`: the name of the security policy



The third example updates the rule in the security policy `POLICY_3` at `PRIORITY` to add an exclusion configuration for signatures `owasp-crs-v042200-id941140-xss` and `owasp-crs-v042200-id941270-xss` under the `xss-v422-stable` preconfigured WAF rule, to exclude request headers that either start with `abc` or end with `xyz` from inspection:
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_3 \
        --target-rule-set "xss-v422-stable" \
        --target-rule-ids "owasp-crs-v042200-id941140-xss,owasp-crs-v042200-id941270-xss" \
        --request-header-to-exclude "op=STARTS_WITH,val=abc" \
        --request-header-to-exclude "op=ENDS_WITH,val=xyz"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_3`: the name of the security policy



The fourth example updates the rule in the security policy `POLICY_4` at `PRIORITY` to add an exclusion configuration for all signatures under the `sqli-v422-stable` preconfigured WAF rule. This excludes request query parameters (parsed from the URI query string or the body payload) that are equal to `bad-param` from inspection:
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_4 \
        --target-rule-set "sqli-v422-stable" \
        --request-query-param-to-exclude "op=EQUALS,val=bad-param"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_4`: the name of the security policy



The fifth example updates the rule in the security policy `POLICY_5` at `PRIORITY` to add an exclusion configuration for signature `owasp-crs-v042200-id930100-lfi` under the `lfi-v422-stable` preconfigured WAF rule. This excludes request URIs that contain `/bad-path` from inspection:
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_5 \
        --target-rule-set "lfi-v422-stable" \
        --target-rule-ids "owasp-crs-v042200-id930100-lfi" \
        --request-uri-to-exclude "op=CONTAINS,val=/bad-path"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_5`: the name of the security policy



The sixth example updates the rule in the security policy `POLICY_6` at `PRIORITY` to remove all the request field exclusions for the rule IDs `owasp-crs-v042200-id942110-sqli` and `owasp-crs-v042200-id942120-sqli` under `sqli-v422-stable`.
    
    
    gcloud compute security-policies rules remove-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_6 \
        --target-rule-set "sqli-v422-stable" \
        --target-rule-ids "owasp-crs-v042200-id942110-sqli,owasp-crs-v042200-id942120-sqli"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_6`: the name of the security policy



## Apply parsing on custom `Content-Type` header values

When Cloud Armor evaluates the request body against preconfigured WAF rules, the `Content-Type` header indicates the format of the data in the request body. By default, Cloud Armor treats the contents of the request body as one string, all of which is eligible for inspection and matching on your preconfigured WAF rules. However, you can configure more precise parsing if your incoming requests have a different encoding. 

Cloud Armor supports the following encoding types:

  * JSON
  * GraphQL



For more information, see [Request body content parsing](https://docs.cloud.google.com/armor/docs/content-parsing).

## What's next

  * Learn more about [tuning rules](https://docs.cloud.google.com/armor/docs/security-policy-rule-tuning).
  * Learn more about [creating and viewing security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies).
  * Learn more about what rule signatures are available for [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules).
  * Learn more about preconfigured WAF rules by using the [custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
