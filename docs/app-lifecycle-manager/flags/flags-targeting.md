---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-targeting/
title: Target flags with CEL \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:00.695607+00:00
---

# Target flags with CEL  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-targeting/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Target flags with CEL Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Common Expression Language (CEL) provides the logic for sophisticated, rule-based flag evaluations. It lets you create precise targeting rules by combining multiple user or request attributes using logical operators.

This guide shows you how to define flags with CEL rules and update evaluation specs.

## Prerequisites

Before you begin, ensure you have:

  1. Completed the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart).
  2. A `gcloud` environment configured to manage App Lifecycle Manager resources.



## Logical operators and syntax

CEL supports standard logical operators to build complex conditions:

  * `&&` logical AND
  * `||` logical OR
  * `!` logical NOT
  * `in` check if a value exists in a list



## Define attributes

CEL attributes are specific data points, such as `source.ip`, request headers, or paths, used within boolean expressions to define security or routing policies. 

Any attribute used in a CEL condition must be explicitly defined and listed in the attributes array of the `EvaluationSpec`. If an attribute is used in a condition but missing from the list, the API will reject the request.

### Create an attribute

You can use App Lifecycle Manager to create CEL attributes.

To create a plan attribute, run the command:
    
    
    gcloud beta app-lifecycle-manager flags attributes create "plan-attr" \
        --key="plan" \
        --attribute-value-type="STRING" \
        --location=global
    

To create a country attribute, run the command:
    
    
    gcloud beta app-lifecycle-manager flags attributes create "country-attr" \
        --key="country" \
        --attribute-value-type="STRING" \
        --location=global
    

To create a platform attribute, run the command:
    
    
    gcloud beta app-lifecycle-manager flags attributes create "platform-attr" \
        --key="platform" \
        --attribute-value-type="STRING" \
        --location=global
    

## Configure a flag with CEL rules

When creating or updating a flag, define the evaluation logic in the `evaluation-spec`.

For example, this snippet enables a feature for premium customers in Germany using their mobile app.
    
    
    gcloud beta app-lifecycle-manager flags create "advanced-reporting-flag" \
        --key="advanced-reporting-flag" \
        --flag-value-type=BOOL \
        --unit-kind="UNIT_KIND_NAME" \
        --location=global \
        --evaluation-spec='{
          "rules": [{
            "id": "premium_mobile_users_in_germany",
            "condition": "plan == \"premium\" && country == \"DE\" && platform == \"mobile\"",
            "target": "enabled"
          }],
          "defaultTarget": "disabled",
          "attributes": [
            "projects/PROJECT_ID/locations/global/flagAttributes/plan-attr",
            "projects/PROJECT_ID/locations/global/flagAttributes/country-attr",
            "projects/PROJECT_ID/locations/global/flagAttributes/platform-attr"
          ]
        }'
    

Replace `PROJECT_ID`, and `UNIT_KIND_NAME` with your values.

## Application integration

Your application must inject the attributes into the evaluation context at runtime.

### Python example:
    
    
    from openfeature.evaluation_context import EvaluationContext
    
    eval_ctx = EvaluationContext(
        targeting_key=user_id,
        attributes={
            "plan": "premium",
            "country": "DE",
            "platform": "mobile"
        }
    )
    
    is_enabled = client.get_boolean_value("advanced-reporting-flag", False, eval_ctx)
    

## Best practices

  * **Order of Evaluation:** Rules are evaluated sequentially. The first rule that evaluates to true determines the flag's value.
  * **Safe Defaults:** If a user context is missing a required attribute for a condition, the evaluation engine will skip that specific rule.
  * **Character Limits:** CEL expressions can be up to 4,096 bytes (4kB) in size.



## What's next

  * Learn about [Multi-Tenant Architecture](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant).
  * Learn about [Experimentation and A/B Testing](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-experimentation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
