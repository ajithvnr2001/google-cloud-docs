---
url: https://docs.cloud.google.com/recaptcha/docs/challenge-policies/
title: Configure challenge policies \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:11.755679+00:00
---

# Configure challenge policies  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/challenge-policies/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Configure challenge policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to configure challenge policies with an existing Google Cloud Fraud Defense integration.

Challenge policies let you selectively trigger CAPTCHA challenges based on custom rules. These rules decide when to show a Fraud Defense challenge based on risk scores, IP addresses, user agents, ASNs, geographic regions, or verified bot (AI agent) identities.

You can use challenge policies with the following recommended features:

  * [**AutoExecute configuration**](https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages#autoexecute-configuration): Simplifies JavaScript integration for client applications.
  * [**Challenges**](https://docs.cloud.google.com/recaptcha/docs/select-challenge-types): Triggers user verification when required by your challenge rules. Fraud Defense supports the following challenge types: 
    * **Visual challenges** : Ask users to select images based on a prompt. By default, a visual challenge gets selected when a rule is configured with the challenge option selected.
    * **Audio challenges** : Ask users to identify spoken audio cues as an accessibility alternative.
    * **QR code challenges** : Ask users to scan a QR code with their mobile device to solve a challenge. Your Universal key must be on an allowlist to use this feature. To add your Universal key to the allowlist, contact the Fraud Defense team at [fraud-defense@google.com](mailto:fraud-defense@google.com) and provide your Universal key.



## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). You can enable billing by using either a credit card or an existing Google Cloud project billing ID. If you require assistance with billing, contact [Cloud Billing support](https://docs.cloud.google.com/support/billing).
  3. Create or identify a Universal key for your project. To create a key, see [Create a Universal key](https://docs.cloud.google.com/recaptcha/docs/policy-engine#create-key). Alternatively, you can copy the ID of an existing Universal key by completing one of the following steps:

     * To copy the ID of an existing key from the Google Cloud console, do the following:

       1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. In the **Keys** list, find the key that you want to copy and click content_copy **Copy to clipboard**.

     * To copy the ID of an existing key using the REST API, call the [`projects.keys.list`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method.

     * To copy the ID of an existing key using the gcloud CLI, run the [`gcloud recaptcha keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command.

  4. Plan your Fraud Defense integration by identifying the user actions that you want to protect (such as `login`, `signup`, or `password_reset`) and which pages on your website trigger these actions. If you use the [AutoExecute configuration](https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages), ensure that these actions are consistent with the action names specified in the `protected_endpoint_group`.

  5. Integrate Fraud Defense into your web page. We recommend that you use the Fraud Defense AutoExecute configuration. For general setup instructions, see [Install Universal keys on websites](https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages).




## Fraud Defense policy configuration overview

The Fraud Defense policy configuration lets you customize the behavior of your Fraud Defense protection. You can configure challenge policies using the `challenge_rule_groups` section.

You can view and update the policy configuration using the Google Cloud console, the gcloud CLI, or the reCAPTCHA Enterprise REST API.

### Console

To view or update your policy configuration in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Make sure that your project is selected in the resource selector.

  3. In the **reCAPTCHA keys** table, click the name of the key for which you want to configure challenge policies.

  4. On the **Key details** page, go to the **Policy** tab.

  5. In the **Rule groups** section, you can view, add, or edit your challenge rules and condition expressions.

  6. Click **Save**.




### gcloud

To update the policy configuration for a key, run the [`gcloud alpha recaptcha policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/policies/update) command:
    
    
    gcloud alpha recaptcha policies update --key=KEY_ID --policy=POLICY.yaml
    

To view the current policy configuration for a key, run the [`gcloud alpha recaptcha policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/policies/describe) command:
    
    
    gcloud alpha recaptcha policies describe --key=KEY_ID
    

### REST API

To update the policy configuration for a key, call the [`projects.keys.updatePolicy`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/updatePolicy) method:
    
    
    PATCH https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy
    
    {
      "clientSettings": {
        "allowedDomains": [
          "example.com"
        ]
      },
      "challengeRuleGroups": [
        {
          "actions": ["login"],
          "challengeRules": [
            {
              "condition": "score < 0.7",
              "challenge": {}
            }
          ]
        }
      ]
    }
    

To view the current policy configuration for a key, call the [`projects.keys.getPolicy`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/getPolicy) method:
    
    
    GET https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy
    

The policy configuration uses YAML format for the Google Cloud CLI and JSON format for the REST API. For the complete schema of the `challenge_rule_groups` section, see Configure challenge policies.

For examples of different use cases, see Example challenge rule configurations.

## Configure challenge policies

You configure challenge policies within the `challenge_rule_groups` section of the Fraud Defense policy configuration. If you already have a policy with `client_settings`, including the domains information, you can update the policy to include your challenge policy rules.

The `challenge_rule_groups` section has the following structure:
    
    
    challenge_rule_groups:
      - actions: [string, ...]
        challenge_rules:
          - condition: string
            challenge:
              # difficulty is optional: USABILITY | BALANCE (default) | SECURITY
              difficulty: BALANCE
            # OR no_challenge: {}
          - condition: string
            challenge:
              difficulty: BALANCE
            # OR no_challenge: {}
    

In every challenge rule, the `condition` field is optional. If `condition` is unspecified or empty, the rule applies unconditionally. Furthermore, the `challenge` and `no_challenge` fields are mutually exclusive, and exactly one of them must be present in each rule.

### Rule evaluation order

Rule groups and their internal rules are evaluated sequentially from top to bottom. The first matching rule is applied. When no group and no rule matches the interaction, evaluation defaults to standard assessment with no challenge shown but a risk score is generated for the request.

### Challenge difficulty levels

You can specify the difficulty level when triggering a challenge. For a complete list of valid difficulty values, see the [`ChallengeSecurityPreference`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#ChallengeSecurityPreference) API reference.

## Condition syntax

The `condition` field is an optional string formatted as a [Common Expression Language (CEL)](https://cel.dev/) expression. If `condition` is unspecified or empty, the rule applies unconditionally. CEL provides standard C-like operators, including relational (`<`, `<=`, `>`, `>=`, `==`, `!=`), arithmetic (`+`, `-`, `/`, `*`, `%`), logical (`!`, `&&`, `||`), and container (`[]`, `in`) operators. CEL supports common primitive data types (`bool`, `int`, `uint`, `double`, `string`), basic container types (`lists`, `messages`), and constants (such as `true`, `1`, `0.5`, `"hello"`, and `[1, 2, 3]`).

Within the runtime, the following Fraud Defense variables are accessible:

Variable | Type | Description  
---|---|---  
`score` | `double` | The Fraud Defense bot score.  
`user_ip_address` | `string` | The IP address (IPv4 or IPv6) of the user making the request.  
`user_agent` | `string` | The user agent of the user making the request.  
`user_asn` | `int` | The Autonomous System Number (ASN) of the user making the request. Omit the `AS` prefix (for example, use `12345` instead of `AS12345`).  
`region_code` | `string` | The Unicode CLDR region code (based on ISO 3166-1 alpha-2) associated with the request location (for example, `"US"`, `"CA"`, or `"FR"`).  
`verified_bots` | `list(Bot)` | A list of verified automated crawlers or agents (such as search engine indexers, AI search assistants, and partner content scrapers) that Fraud Defense has identified.  
  
The following additional non-primitive types are defined. For the complete list of values, see [Bot](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#Bot).
    
    
    message Bot {
      name [string] - the name of the bot
      bot_type [BotType] - the type of automated agent
    }
    

For more information about possible `name` values, see the [`Bot`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#Bot) API reference. For more information about valid `bot_type` enum values, see the [`BotType`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#BotType) API reference.

In Fraud Defense challenge policies, you can use any of these variables to produce a boolean expression. For example, `score > 0.5`, `user_ip_address == "192.0.2.1"`, `region_code == "US"`, and `user_asn == 12345` are valid condition expressions that evaluate to a boolean. Note that because `user_asn` is an integer type, you must omit the `AS` prefix when checking ASNs.

The following functions are available for use in Fraud Defense challenge policy conditions:

Name | Signature | Description  
---|---|---  
`contains` | `string.contains(string) -> bool` | Checks whether the string operand contains the substring.  
`startsWith` | `string.startsWith(string) -> bool` | Checks whether the string operand starts with the specified prefix.  
`endsWith` | `string.endsWith(string) -> bool` | Checks whether the string operand ends with the specified suffix.  
`size` | `size(string) -> int`  
`size(list) -> int`  
`string.size() -> int`  
`list.size() -> int` | Returns the size of a string (number of codepoints) or list (number of elements).  
  
Comprehension functions are a style of macro built into CEL. The following comprehensions are available:

Name | Signature | Description | Example  
---|---|---|---  
`has` | `has(message.field) -> bool` | Checks whether a field is available. | `has(verified_bots[0].name)`  
`all` | `list(A).all(A, predicate(A) -> bool) -> bool` | Checks whether all elements `x` in a list `e` match predicate `p`. | `[1, 2, 3].all(x, x > 0)`  
`exists` | `list(A).exists(A, predicate(A) -> bool) -> bool` | Checks whether any element `x` in a list `e` matches predicate `p`. | `[1, 2, 3].exists(i, i % 2 != 0)`  
`exists_one` | `list(A).exists_one(A, predicate(A)) -> bool` | Checks whether exactly one element `x` in a list `e` matches predicate `p`. | `[1, 2, 2].exists_one(i, i < 2)`  
  
## Example challenge rule configurations

This section contains valid challenge rule configuration examples.

### Challenge all requests that have a low score
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: 'score < 0.5'
            challenge: {}
    

### Select a high-friction challenge for all requests with a low score
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: 'score < 0.5'
            challenge:
              difficulty: 'SECURITY'
    

### Challenge specific actions that have a low score
    
    
    challenge_rule_groups:
      - actions: ['login', 'signup']
        challenge_rules:
          - condition: 'score < 0.5'
            challenge: {}
    

### Configure different rule thresholds for different actions
    
    
    challenge_rule_groups:
      - actions: ['login']
        challenge_rules:
          - condition: 'score < 0.5'
            challenge: {}
      - actions: ['signup']
        challenge_rules:
          - condition: 'score < 0.7'
            challenge: {}
    

### Don't show challenge to IP addresses on allowlist
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: 'user_ip_address in ["123.255.255.001", "123.255.255.002"]'
            no_challenge: {}
    

**Note:** This rule is distinct from the [Fraud Defense IP allowlists](https://docs.cloud.google.com/recaptcha/docs/allowlist-ip) feature.

### Don't show challenge to subnet of IP addresses
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: 'user_ip_address.startsWith("123.255.255")'
            no_challenge: {}
    

### Don't show challenge to requests from specific ASNs
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          # Note that ASNs must be specified as integers without the AS prefix (e.g., 12345 instead of AS12345)
          - condition: 'user_asn in [12345, 67890]'
            no_challenge: {}
    

### Don't show challenge to a Google agent
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: 'verified_bots.exists(e, e.name == "google-agent")'
            no_challenge: {}
    

### Show challenge based on complex conditions
    
    
    challenge_rule_groups:
      - actions: ['*']
        challenge_rules:
          - condition: '(user_agent.contains("Chrome/143") && score < 0.5) || (user_agent.contains("Chrome/149") && score < 0.7)'
            challenge: {}
    

## What's next

  * To assess the reCAPTCHA response token, see [Create assessments for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
