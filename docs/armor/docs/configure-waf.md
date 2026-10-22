---
url: https://docs.cloud.google.com/armor/docs/configure-waf/
title: Set up preconfigured WAF rules \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:57.027635+00:00
---

# Set up preconfigured WAF rules  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/configure-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Set up preconfigured WAF rules Stay organized with collections  Save and categorize content based on your preferences. 

Use these instructions to set up and tune Google Cloud Armor preconfigured web application firewall (WAF) rules to help protect your application against attacks. If you aren't familiar with preconfigured WAF rules, see the [overview](https://docs.cloud.google.com/armor/docs/waf-rules).

## Set up a preconfigured WAF rule

This section provides template preconfigured WAF rules that you can copy into the Google Cloud console and customize to fit your use case. In each example Google Cloud CLI command, you configure a security policy with name `POLICY_NAME` and priority `PRIORITY`.

The first example sets up a rule with a rule name `RULE_NAME` and a sensitivity level of `SENSITIVITY`, which enables all signatures with sensitivity less than or equal to `SENSITIVITY`. For more information about rule sensitivity, see [Choose a sensitivity level](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': SENSITIVITY})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': SENSITIVITY})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up
  * `RULE_NAME`: the name of the WAF rule that you want to set up
  * `SENSITIVITY`: the sensitivity level of the WAF rule



The second example is similar to the first, but it opts out rule signatures `SIGNATURE_1` and `SIGNATURE_2`. This means that these two signatures aren't evaluated when the WAF rule is evaluated:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': SENSITIVITY, 'opt_out_rule_ids': ['SIGNATURE_1', 'SIGNATURE_2']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': SENSITIVITY, 'opt_out_rule_ids': ['SIGNATURE_1', 'SIGNATURE_2']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up
  * `RULE_NAME`: the name of the WAF rule that you want to set up
  * `SENSITIVITY`: the sensitivity level of the WAF rule
  * `SIGNATURE_1`: the name of the WAF signature that you want to opt out
  * `SIGNATURE_2`: the name of the WAF signature that you want to opt out



The third example is similar to the second, but instead of opting out two signatures, you opt in two rule signatures. Note that you can only opt in rule signatures when you set the sensitivity level to `0`:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': 0, 'opt_in_rule_ids': ['SIGNATURE_1', 'SIGNATURE_2']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('RULE_NAME', {'sensitivity': 0, 'opt_in_rule_ids': ['SIGNATURE_1', 'SIGNATURE_2']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up
  * `RULE_NAME`: the name of the WAF rule that you want to set up
  * `SIGNATURE_1`: the name of the WAF signature that you want to opt out
  * `SIGNATURE_2`: the name of the WAF signature that you want to opt out



In all of the previous examples, you use only one expression per rule. While you can combine expressions using the logical OR (`||`) logical operator, we recommend that you use only one expression per rule as a best practice to avoid exceeding the maximum expression size.

## Update inspection limit for preconfigured WAF rules

Cloud Armor preconfigured WAF rules can only inspect up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of a request body. You can manually configure a security policy to use one of these inspection limits for your preconfigured WAF rules.

The following command sets the inspection limit of all preconfigured WAF rules available in the `POLICY_NAME` policy to 8 kB using the `--request-body-inspection-size` flag. For more information about the inspection limits of the preconfigured WAF rules, see [Request body inspection limitation](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body).
    
    
    gcloud compute security-policies update POLICY_NAME \
        --request-body-inspection-size=8kB
    

Replace `POLICY_NAME` with the name of the security policy that you want to set up.

Similarly, you can use the `--request-body-inspection-size` flag to set the inspection limit of all preconfigured WAF rules available in the `POLICY_NAME` policy to either 16 kB, 32 kB, 48 kB, or 64 kB.

### Mitigate risk on request body that exceeds configured inspection limit

When a preconfigured WAF rule is evaluated in a Cloud Armor security policy, up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of a request body is inspected for signature matches against the WAF rules.

You can mitigate the risk from larger requests by creating a rule in your security policies to help ensure that no uninspected content reaches your backends. For example, create a rule to deny traffic that exceeds the configured inspection limit of 8 kB (8192 bytes) in the request body size. The following command shows how to create this rule:
    
    
    gcloud compute security-policies rules create 10 \
        --security-policy my-policy \
        --expression "int(request.headers['content-length']) > 8192" \
        --action deny-403 \
        --description "Block requests greater than 8 kB"
    

Similarly, you can create a rule to deny traffic that exceeds the configured inspection limits of 16 kB, 32 kB, 48 kB, or 64 kB in the request body size. For example, the following command shows how to create this rule for the inspection limit of 64 kB (65536 bytes).
    
    
    gcloud compute security-policies rules create 10 \
        --security-policy my-policy \
        --expression "int(request.headers['content-length']) > 65536" \
        --action deny-403 \
        --description "Block requests greater than 64 kB"
    

## Examples

The examples in this section highlight important aspects of creating and tuning preconfigured WAF rules, including sensitivity level and signature exceptions. In all of the gcloud CLI example commands, you create a security policy with the name `POLICY_NAME` at priority `PRIORITY`.

### Create a rule at a given sensitivity level

In this example, you use all signatures in the `sqli-v422-stable` WAF rule with a sensitivity level less than 4. Therefore, you create the rule at sensitivity level 3, which includes all signatures with a sensitivity level less than or equal to three:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 3})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 3})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up ### Create a rule that opts out one or more signatures



In this example, you use almost all of the signatures at sensitivity level 1 and 2 in the `xss-v422-stable` WAF rule, but you want to exclude the signature `owasp-crs-v042200-id941370-xss`, which checks for JavaScript global variables. Therefore, you create the rule at sensitivity level 2 and use the `opt_out_rule_ids` argument to opt out of the `owasp-crs-v042200-id941370-xss` signature:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 2, 'opt_out_rule_ids': ['owasp-crs-v042200-id941370-xss']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 2, 'opt_out_rule_ids': ['owasp-crs-v042200-id941370-xss']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up To exclude two or more signatures from a rule, provide a comma-separated list of signatures with the `opt_out_rule_ids` argument, as follows:



###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 2, 'opt_out_rule_ids': ['owasp-crs-v042200-id941370-xss', 'owasp-crs-v042200-id941380-xss']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 2, 'opt_out_rule_ids': ['owasp-crs-v042200-id941370-xss', 'owasp-crs-v042200-id941380-xss']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up



### Create a rule that opts in one or more signatures

This example uses only the signature `owasp-crs-v042200-id941150-xss` from the `xss-v422-stable` WAF rule. The signature checks for disallowed HTML attributes, and is at sensitivity level 2. Therefore, you create the rule at sensitivity level 0 and use the `opt_in_rule_ids` argument to opt in the `owasp-crs-v042200-id941150-xss` signature. Note that you can only opt in rule signatures when you set the sensitivity level to `0`:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 0, 'opt_in_rule_ids': ['owasp-crs-v042200-id941150-xss']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 0, 'opt_in_rule_ids': ['owasp-crs-v042200-id941150-xss']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up



If you want to include two or more signatures from a rule, provide a comma-separated list of signatures with the `opt_in_rule_ids` argument, as follows:

###  Console 

Select **Advanced mode** , then use the following example expression in the **Match** field:
    
    
    evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 0, 'opt_in_rule_ids': ['owasp-crs-v042200-id941150-xss', 'owasp-crs-v042200-id941320-xss']})
    

###  gcloud 
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME  \
        --expression "evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 0, 'opt_in_rule_ids': ['owasp-crs-v042200-id941150-xss', 'owasp-crs-v042200-id941320-xss']})" \
        --action deny-403
    

Replace the following:

  * `PRIORITY`: the priority of the security policy
  * `POLICY_NAME`: the name of the security policy that you want to set up



## What's next

  * For more information about WAF rule tuning, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
