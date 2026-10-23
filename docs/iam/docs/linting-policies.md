---
url: https://docs.cloud.google.com/iam/docs/linting-policies/
title: Linting policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:03.891629+00:00
---

# Linting policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/linting-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Linting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This topic describes how to _lint_ , or validate, your Identity and Access Management (IAM) allow policies.

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Read the [IAM Conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview) to understand the basics of IAM Conditions.


**Note:** This alpha release of [`lintPolicy`](https://docs.cloud.google.com/iam/reference/rest/v1/iamPolicies/lintPolicy) only supports linting operations on the `google.iam.v1.Binding.condition` field.

### Required roles

To lint a resource's allow policy, you need permissions to get the resource, and to get and set the allow policy for the resource. These permissions have the following form, where `SERVICE` is the name of the service that owns the resource and `RESOURCE_TYPE` is the name of the resource type that you want to manage access to:

  * `SERVICE.RESOURCE_TYPE.get`
  * `SERVICE.RESOURCE_TYPE.getIamPolicy`
  * `SERVICE.RESOURCE_TYPE.setIamPolicy`



For example, to lint a project's allow policy, you need the following permissions:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



To gain the required permissions, ask your administrator to grant you a predefined or custom role that includes the permissions. For example, your administrator could grant you the Security Admin role (`roles/iam.securityAdmin`), which includes permissions to get almost all Google Cloud resources and manage their allow policies.

## Understanding linting for allow policies

In the context of allow policies, linting is a method of examining a new or existing allow policy and checking it for specific issues. These issues include the following range of possibilities:

  * Suggestions
  * Warnings
  * Information that can help improve the intent of the allow policy, such as better syntax and semantics
  * Syntax or semantic errors that cause `setIamPolicy` operations to fail



If you try to update an allow policy, and you get an error, linting the allow policy can help you find the cause of the error. You can also use the linter to help ensure that a conditional role binding has the intended effect.

## Linting a condition

Condition expressions can be complex, especially in scenarios that require multiple clauses and logic operators to appropriately manage access. If a condition expression contains invalid logic, or if the syntax violates the restrictions of a condition expression, you cannot add the condition to an allow policy.

Also, even if a condition expression uses the correct syntax, it might contain semantic errors, which can prevent your allow policies and role bindings from working as expected. Common semantic errors include the following:

  * Use of unrecommended functions
  * Use of legacy resource types or legacy service names
  * Ineffective conditions, such as an inapplicable date or time range



When you lint a condition, the linter inspects the condition expression and reports any syntax errors. It also reports possible semantic errors that could cause unexpected results.

Before attempting to set a new conditional role binding, you are encouraged to lint the expression first. This section shows you how to lint a condition expression using the Google Cloud console, Google Cloud CLI, or the REST API.

To lint a condition expression:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Select a project** , choose a project, and click **Open**.

  3. From the list of principals, locate the desired principal and click the edit **Edit** button.

  4. From the **Edit permissions** panel, locate the desired role that you want to lint. Then under **IAM condition (optional)** , click the name of the condition.

  5. In the **Condition editor** , manually add or edit a condition expression.

  6. To validate the CEL syntax, click **Run Linter**.

If the syntax contains errors, an error **Error** icon appears next to the incorrect line. To see details about each error, hold the pointer over the icon.

If the condition uses the correct syntax, but the linter finds a possible issue, a warning **Warning** icon appears next to the line with the issue. To see details about each warning, hold the pointer over the icon.

  7. Make any necessary changes to the condition expression. After you click **Run Linter** , the linter runs automatically in the background while you edit the expression.

You must correct all errors before you save the condition expression. We strongly encourage you to fix all warnings as well.

  8. When there are no errors or warnings, click **Save** to apply the condition.

  9. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.




### gcloud

Execute the [`gcloud alpha iam policies lint-condition`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/policies/lint-condition) command to lint a given condition expression. To execute this command, you can either create a text file that contains the condition, or specify flags for the condition's title, description, and expression.

The following example uses a text file that contains the following condition:

`condition.json`
    
    
    {
      "title": "1_less_than_2",
      "description": "",
      "expression": "1 <"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

The output from the command contains the following:
    
    
    lintResults:
    - debugMessage: |-
        ERROR: Parse expression:1:3: mismatched input '<EOF>' expecting {'[', '{', '(', '.', '-', '!', 'true', 'false', 'null', NUM_FLOAT, NUM_INT, NUM_UINT, STRING, BYTES, IDENTIFIER}
          | 1 >
          | ...^
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 3
      severity: ERROR
      validationUnitName: LintValidationUnits/ConditionCompileCheck
    ...
    

Each of the lint results contain a `debugMessage` that can be used to help locate the problem with the condition expression. If the condition failed to compile, you may see many different `validationUnitName` types with the following `debugMessage` text:
    
    
    The validation unit is skipped due to absence of a required object: CheckedExpr
    

Make changes so that the expression compiles, then lint the condition again.

### REST

The `[iamPolicies.lintPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy)` method lints, or validates, a condition expression in an allow policy. 

Before using any of the request data, make the following replacements: 

  * `condition`: An [`Expr` object](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Expr) representing the condition to lint. For example: 
        
        "title": "1_less_than_2",
        "description": "",
        "expression": "1 <"

To learn about the format of an `Expr` object, see the [`Expr` schema reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Expr#SCHEMA_REPRESENTATION). 




HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/iamPolicies:lintPolicy

Request JSON body: 
    
    
    {
      "condition": {
        condition
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/iamPolicies:lintPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v1/iamPolicies:lintPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response body contains one or more [`LintResult`](https://docs.cloud.google.com/iam/reference/rest/v1/iamPolicies/lintPolicy#LintResult) objects, such as the following: 
    
    
    {
      "lint_results": {
        "level": "CONDITION",
        "validation_unit_name": "LintValidationUnits/ConditionCompileCheck",
        "severity": "ERROR",
        "field_name": "condition.expression",
        "location_offset": "2",
        "debug_message": "ERROR: Parse expression:1:2: mismatched input \'<EOF>\' expecting {\'[\', \'{\', \'(\', \'.\', \'-\', \'!\', \'true\', \'false\', \'null\', NUM_FLOAT, NUM_INT, NUM_UINT, STRING, BYTES, IDENTIFIER}\n  | 1<\n  | ..^"
      },
      "lint_results": {
        "level": "CONDITION",
        "validation_unit_name": "LintValidationUnits/ConditionComplexityCheck",
        "severity": "NOTICE",
        "field_name": "condition.expression",
        "debug_message": "The validation unit is skipped due to absence of a required object: CheckedExpr"
      }
    }
    

Each of the lint results contain a `debug_message` that can be used to help locate the problem with the condition expression. If the condition failed to compile, you may see many different `validation_unit_name` types with the following `debugMessage` text:
    
    
    The validation unit is skipped due to absence of a required object: CheckedExpr
    

Make changes so that the expression compiles, then lint the condition again.

## Supported validation units

As described previously, a validation unit is an individual lint type that evaluates the expression for syntactic issues. The table below summarizes supported validation units, each with intended linting level, linting result severity, and a brief description.

Validation unit | [Lint level](https://docs.cloud.google.com/iam/reference/rest/v1/iamPolicies/lintPolicy#Level) | [Severity](https://docs.cloud.google.com/iam/reference/rest/v1/iamPolicies/lintPolicy#Severity) | Description | `ConditionCompileCheck` | `CONDITION` | `ERROR` |  The condition expression contains a compilation error as a result of invalid CEL syntax.   
---|---|---|---  
`ConditionComplexityCheck` | `CONDITION` | `ERROR` |  The condition expression contains more than the maximum of 12 logic operators.   
`DateTimeCheck` | `CONDITION` | `WARNING` |  The condition expression specifies a timestamp comparison that always evaluates to either true or false, due to one of these issues: 

  * A timestamp does not use the [correct format for timestamps](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time).
  * A timestamp is in the past.

  
`DateTimeRangeCheck` | `CONDITION` | `WARNING` |  Value out of range for the intended advanced timestamp function and the comparison expression. See the [valid values](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#supported_basic_functions_and_operators) for advanced timestamp functions.   
`DrgGetAttributeDefaultValueCheck` | `CONDITION` | `ERROR` |  The condition expression calls `api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', V)`, where `V` is any value other than an empty list, `[]`. For this API attribute, `V` must always be an empty list.   
`EffectiveTimeRangeCheck` | `CONDITION` | `WARNING` |  In a more complex usage of timestamp functions and comparison, the expression results in an empty effective time range, and is therefore effectively false. Alternatively, the time range covers a full range, and is therefore effectively true.   
`HasOnlyListConstCheck` | `CONDITION` | `ERROR` |  The condition expression calls `hasOnly(List<T>)`, where the type `T` is not a constant type, such as a string or integer. The `hasOnly()` function accepts only a list of constants.   
`HasOnlyListLengthCheck` | `CONDITION` | `ERROR` |  The condition expression calls `hasOnly(List<T>)`, and `List<T>` contains more than the maximum of 10 elements.   
`ResourceServiceLiteralCheck` | `CONDITION` | `WARNING` |  The specified `resource.service` value is not supported. The expression using such string literal for equality comparison is effectively false. Use a [supported value](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource_service_values).   
`ResourceTypeLiteralCheck` | `CONDITION` | `WARNING` |  The specified `resource.type` value is not supported. The expression using such string literal for equality comparison is effectively false. Use a [supported value](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource_type_values).   
`RestrictedAttributesCheck` | `CONDITION` | `WARNING` |  The expression uses an attribute that is restricted or not supported. Setting the condition expression might not succeed. See the [list of attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#attribute-summary).   
  
## Linting examples

This section shows examples of conditions that cause each validation unit to report issues. Each example demonstrates linting by using the Google Cloud CLI.

### No validation issues

Example condition:
    
    
    {
      "title": "1_less_than_2",
      "description": "",
      "expression": "1 < 2"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    {}
    

### ConditionCompileCheck

Example condition:
    
    
    {
      "title": "Condition not compiling",
      "description": "",
      "expression": "true=false"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: |-
        ERROR: Parse expression:1:4: token recognition error at: '=f'
          | true=false
          | ....^
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 4
      severity: ERROR
      validationUnitName: LintValidationUnits/ConditionCompileCheck
    

### ConditionComplexityCheck

Example condition:
    
    
    {
      "title": "Condition not compiling",
      "description": "",
      "expression":
        "1<2 || 2<3 || 3<4 || 4<5 || 5<6 || 6<7 || 7<8 || 8<9 || 9<10 || 10<11 || 11<12 || 12<13 || 13<14 || 14<15"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: Logical operators count must not be more than 12
      fieldName: condition.expression
      level: CONDITION
      severity: ERROR
      validationUnitName: LintValidationUnits/ConditionComplexityCheck
    

### DateTimeCheck

Example condition:
    
    
    {
      "title": "Condition not compiling",
      "description": "",
      "expression": "request.time < timestamp('2000-01-01T00:00:00Z')"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: Ineffective date time value 2000-01-01T00:00:00+00:00 parsed
        from "2000-01-01T00:00:00Z"; condition is effectively False. Time expired
        already.
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 25
      severity: WARNING
      validationUnitName: LintValidationUnits/DateTimeCheck
    

### DateTimeRangeCheck

Example condition:
    
    
    {
      "title": "Time function out of range",
      "description": "",
      "expression": "request.time.getMonth() > 13"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: The value being compared to the specified timestamp function
        (getMonth) must be in range [0, 11].
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 26
      severity: WARNING
      validationUnitName: LintValidationUnits/DateTimeRangeCheck
    

### DrgGetAttributeDefaultValueCheck

Example condition:
    
    
    {
      "title": "DRG condition takes non empty list as default value",
      "description": "",
      "expression":
        "api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', ['roles/viewer']).hasOnly(['roles/editor'])"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: api.getAttribute call on
        'iam.googleapis.com/modifiedGrantsByRole' can only
        accept empty list ('[]') as default value.
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 60
      severity: ERROR
      validationUnitName: LintValidationUnits/DrgGetAttributeDefaultValueCheck
    

### EffectiveTimeRangeCheck

Example condition:
    
    
    {
      "title": "Empty time range",
      "description": "",
      "expression": "request.time.getMonth() > 5 && request.time.getMonth() < 4"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: The aggregate of time functions [getMonth] results in empty ranges.
      fieldName: condition.expression
      level: CONDITION
      severity: WARNING
      validationUnitName: LintValidationUnits/EffectiveTimeRangeCheck
    

### HasOnlyListConstCheck

Example condition:
    
    
    {
      "title": "hasOnly contains more than constant value",
      "description": "",
      "expression":
        "api.getAttribute('somekey', []).hasOnly(['somevalue', resource.name])"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: hasOnly() expects an argument of type list containing only const
          values, but a non-const expression was found in the list.
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 59
      severity: ERROR
      validationUnitName: LintValidationUnits/HasOnlyListConstCheck
    

### HasOnlyListLengthCheck

Example condition:
    
    
    {
      "title": "hasOnly contains more than 10 elements",
      "description": "",
      "expression":
        "api.getAttribute('somekey', []).hasOnly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: The list argument to hasOnly() cannot have more than 10 elements
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 39
      severity: ERROR
      validationUnitName: LintValidationUnits/HasOnlyListLengthCheck
    

### ResourceServiceLiteralCheck

Example condition:
    
    
    {
      "title": "Condition with unsupported resource service string",
      "description": "",
      "expression": "resource.service == 'resourcemanager'"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: 'resource.service : resourcemanager is not supported. Using this
        value in condition may lead to unintended consequences. Check user guide at
        https://cloud.google.com/iam/docs/conditions-resource-attributes#resource_service_values
        for supported values for resource.service.'
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 20
      severity: WARNING
      validationUnitName: LintValidationUnits/ResourceServiceLiteralCheck
    

### ResourceTypeLiteralCheck

Example condition:
    
    
    {
      "title": "Condition with legacy resource type",
      "description": "",
      "expression": "resource.type == 'resourcemanager.projects'"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: 'resource.type : resourcemanager.projects is not supported.
        Using this value in condition may lead to unintended consequences. Check
        user guide at https://cloud.google.com/iam/docs/conditions-resource-attributes#resource_type_values
        for supported values for resource.type.'
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 17
      severity: WARNING
      validationUnitName: LintValidationUnits/ResourceTypeLiteralCheck
    

### RestrictedAttributesCheck

Example condition:
    
    
    {
      "title": "Condition with restricted attribute",
      "description": "",
      "expression": "'accessPolicies/123/accesslevels/TRUSTED' in request.auth.access_levels"
    }
    

Run command:
    
    
    gcloud alpha iam policies lint-condition --condition-from-file="condition.json"
    

Lint result:
    
    
    lintResults:
    - debugMessage: Condition attribute `request.auth.access_levels` is restricted
        or unsupported. Please check https://cloud.google.com/iam/docs/conditions-overview
        for the full list of supported attributes
      fieldName: condition.expression
      level: CONDITION
      locationOffset: 57
      severity: WARNING
      validationUnitName: LintValidationUnits/RestrictedAttributesCheck
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
