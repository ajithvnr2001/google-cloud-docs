---
url: https://docs.cloud.google.com/armor/docs/security-policy-rule-tuning/
title: Tune security policy rules \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:15.266421+00:00
---

# Tune security policy rules  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/security-policy-rule-tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Tune security policy rules Stay organized with collections  Save and categorize content based on your preferences. 

You can tune rules by excluding request fields from evaluation to reduce false positives.

When configuring exclusions for a rule, you can exclude the following fields from inspection:

  * Request headers
  * Request cookies
  * Request query parameters
  * Request URIs
  * Request bodies



## Exclude request fields from rules evaluation

To configure a request field exclusion for a rule, associate the configuration with a security policy rule.

These rules don't use rule IDs. Instead, you can configure the `--target-rule-set` flag with one of the following values:

  * `cel` (`--target-rule-set "cel"`): applies exclusions only to custom CEL rules in that security policy rule.
  * `*` (`--target-rule-set "*"`, global exclusion): applies exclusions to all rules attached to that security policy, including both custom CEL rules and those that use `evaluatePreconfiguredWaf()`.



On backend security policies (both global and regional), you can configure up to 100 of each of the following per target (`cel` or `*`):

  * Request headers
  * Request cookies
  * Request query parameters
  * Request URIs
  * Request bodies



The available field operators are:

  * `EQUALS`: matches if the field value equals the specified value.
  * `STARTS_WITH`: matches if the field value starts with the specified value.
  * `ENDS_WITH`: matches if the field value ends with the specified value.
  * `CONTAINS`: matches if the field value contains the specified value.
  * `EQUALS_ANY`: matches if the field value is any value.



### Request headers

You can exclude specific request headers from inspection during rule evaluation by using their header names in the exclusion field.

When a request header matches an exclusion, the entire header entry (both its name and value) is removed from the `request.headers` map before rule evaluation.

**Example**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to exclude request headers that either start with `abc` or end with `xyz` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-header-to-exclude "op=STARTS_WITH,val=abc" \
        --request-header-to-exclude "op=ENDS_WITH,val=xyz"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



### Request cookies

You can exclude specific request cookies from inspection during rule evaluation by using their cookie names in the exclusion field.

When a request cookie matches an exclusion, the entire cookie entry (both its name and value) is excluded from the request attributes before rule evaluation.

**Example**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to exclude request cookies starting with `session_` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-cookie-to-exclude "op=STARTS_WITH,val=session_"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



### Request query parameters

You can exclude specific request parameters from inspection during rule evaluation by using their parameter names in the exclusion field. The `--request-query-param-to-exclude` flag applies to both URL query parameters and [parsed request body parameters](https://docs.cloud.google.com/armor/docs/content-parsing) (JSON, form data, and GraphQL).

When a parameter matches an exclusion, the entire parameter entry (both its key and value) is removed from `request.params` before rule evaluation, so `has(request.params.param_name)` evaluates to `false`.

For parsed request bodies, you can use dot notation to target nested fields and array items:

  * Top-level field: `val=user`
  * Nested field: `val=user.name`
  * Array item: `val=items.0.name`



**Example**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to exclude the URL query parameter `bad-param`, the nested JSON field `user.name`, and the JSON array item field `items.0.name` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-query-param-to-exclude "op=EQUALS,val=bad-param" \
        --request-query-param-to-exclude "op=EQUALS,val=user.name" \
        --request-query-param-to-exclude "op=EQUALS,val=items.0.name"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



### Request URIs

You can exclude URIs from the request line (excluding query string data) from inspection during rule evaluation.

When excluding a URI, the entire URI field is excluded from inspection.

**Example**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to exclude request URIs that contain `/bad-path` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-uri-to-exclude "op=CONTAINS,val=/bad-path"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



### Request bodies

You can exclude specific request body values from inspection during rule evaluation.

When a request body matches an exclusion, the `request.body` attribute is excluded from rule evaluation.

**Example**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to exclude request bodies that contain `bad-body-value` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules add-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-body-to-exclude "op=CONTAINS,val=bad-body-value"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



### Field values

You must specify a field value if you use a field operator other than `EQUALS_ANY`.

For request headers, request cookies, and request query parameters, the permitted character set for field values includes the following characters:

  * `!`, `#`, `$`, `%`, `&`, `*`, `+`, `-`, `.`, `^`, `_`, ```, `|`, `~`
  * Alpha characters `A` through `Z` (both uppercase and lowercase)
  * Digit characters `0` through `9`



For request bodies, the permitted character set for field values includes all printable ASCII characters except `'`, `\`, `(`, and `)`:

  * Space (` `) and special characters: `!`, `"`, `#`, `$`, `%`, `&`, `*`, `+`, `,`, `-`, `.`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `[`, `]`, `^`, `_`, ```, `{`, `|`, `}`, `~`
  * Alpha characters `A` through `Z` (both uppercase and lowercase)
  * Digit characters `0` through `9`



When you apply exclusions for these request fields, the configured field value (`val=`) is compared case-insensitively (after transformation) against the following to determine which entities to exclude from inspection:

  * **Request headers** : matches against the header name (key) to exclude the entire header (both name and value).
  * **Request cookies** : matches against the cookie name to exclude the entire cookie (both name and value).
  * **Request query parameters** : matches against the parameter name or nested JSON path (key) to exclude the entire parameter (both key and value).
  * **Request bodies** : matches against the request body content string to exclude the entire `request.body` attribute.



You don't need to perform additional encoding if you want to exclude a specific character that's not in the permitted character set.

For request URIs, the field value must be given in a URI format with the following component restrictions:

Component | Restriction  
---|---  
Scheme | Allowed, but restricted to `http` or `https`  
Host | Allowed (can be an IP address)  
Port | Allowed  
Path | Allowed  
Query | Not allowed  
Fragment | Not allowed  
  
When you apply exclusions for request URIs, the configured field values are compared case-insensitively (after transformation) against the URIs from the request line, excluding the query string. The URIs from the request line can be relative or absolute. Consider this when configuring exclusions for request URIs.

### Remove exclusions

To remove request field exclusions from a security policy rule, use the `remove-preconfig-waf-exclusion` command. You can remove specific field exclusions by specifying the corresponding field exclusion flags, or omit the field flags to remove all exclusions for that target rule set (`cel` or `*`).

**Examples**

The following example updates the rule in the security policy `POLICY_NAME` at `PRIORITY` to remove the exclusion for request headers starting with `abc` from rules evaluation (`cel`):
    
    
    gcloud compute security-policies rules remove-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel" \
        --request-header-to-exclude "op=STARTS_WITH,val=abc"
    

The following example omits the field flags to remove all request field exclusions configured for rules evaluation (`cel`) on the rule at `PRIORITY`:
    
    
    gcloud compute security-policies rules remove-preconfig-waf-exclusion PRIORITY \
        --security-policy POLICY_NAME \
        --target-rule-set "cel"
    

Replace the following:

  * `PRIORITY`: the priority of the rule
  * `POLICY_NAME`: the name of the security policy



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
