---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/calculated-fields/
title: Configure calculated fields \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:08.183590+00:00
---

# Configure calculated fields  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/calculated-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure calculated fields

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This guide is for security analysts and SOC managers who want to automate data enrichment within their security operations. It explains how to create and manage Calculated Fields using logical formulas to derive new values from existing case and alert data. By following this method, you can eliminate manual data entry and ensure critical metrics are updated in real time. Successful completion improves platform analytical capabilities and accelerates incident triage through automated field population.

With Calculated Fields, you can dynamically derive new data points within Google Security Operations cases and alerts. By defining logical formulas, you can compute values based on existing system or custom fields. The calculated value is automatically evaluated and stored in a user-selected, pre-existing custom field (labeled **Target Field**) in real time.

## Common use cases

The following scenarios represent the most frequent ways organizations leverage calculated fields to improve operational efficiency and data clarity.

### Automated risk scoring

  * **Objective** : Categorize cases based on event volume or priority levels. 
  * **Value** : Standardizes triage and ensures high-risk incidents are visible to the team immediately.



### Data normalization

  * **Objective** : Flag alerts as **Test** or **Production** based on naming conventions. 
  * **Value** : Reduces noise by letting analysts filter out non-critical testing data from their primary view.



## Key terminology

  * **Formula** : A text-based logical expression you define, using functions, operators, and field references, to compute a value.
  * **Target Field** : An existing **Custom Field** (**Free Text** type) where the formula result calculation is stored.
  * **Dependencies** : The fields referenced within your formula. When the value of a dependency field changes, the **Calculated Field** is re-evaluated synchronously.



## Before you begin

Before you create a calculation, make sure your environment meets the following technical requirements:

  * **Permissions** : You must have administrative access to the **Settings** menu and permissions to manage Case Data.
  * **Environment check** : Make sure you have existing, active **Custom Fields** (**Free Text** type) to act as target fields.



Make sure you have existing custom fields to use as target fields in your system. If not, perform the following steps:

  1. Go to **Settings** > **Case Data** > **Custom Fields**.
  2. Create a new Custom Field and set the type to **Free Text**.



For more information about custom fields, see [Create a custom field](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#create_a_custom_field).

## Technical constraints and validation rules

Before you define a calculation, make sure your target fields and logic follow these system constraints. These rules govern how the Google SecOps engine validates and persists formula results.

### Field validation criteria

The calculation engine strictly enforces the following requirements for any field designated as a **Target Field** :

  * **Data type** : The field must be a **Free Text** type.
  * **Operational status** : The field must be **Active** ; the system can't write to deleted or invalidated fields.
  * **Dependency mapping** : To prevent circular logic, a field can't be a target if it's already a dependency for another calculated field.



### Field scoping

When you create a **Custom Field** with a `Both` scope, the system generates unique entries for each context. This lets you maintain separate logic for cases and alerts within the same logical category.

In the **Target Field** menu, you must select the specific scope relevant to your formula:

  * **Case scope** : Labeled as `CaseCustom.YourField` (for example, `CaseCustom.RiskLevel`)
  * **Alert scope** : Labeled as `AlertCustom.YourField` (for example, `AlertCustom.RiskLevel`)



## Create and manage Calculated Fields

This section outlines how to define a new calculation and address common issues during the setup process.

### Create a new calculation

To create a new calculation, do the following:

  1. Go to **Settings** > **Case Data** > **Calculated Fields**.
  2. Click  add  **Add**.
  3. In the **Calculated Field Name** field, enter a unique name and description for your calculation.
  4. In the **Target Field** area, select the existing **Custom Field** to store the result.

     1. **Anticipated failure** : The selected field doesn't appear in the menu.
     2. **Corrective step** : Verify the **Custom Field** is active, set to **Free Text** , and isn't already a dependency for another calculation.
  5. In the text editor, build your formula using the supported functions, operators, and syntax. Create a logical expression (for example, `IF ([case.priority] == "High") THEN "Urgent" ELSE "Standard"`). For more details, see Formula language and syntax.

  6. Click **Save**.

     1. **Anticipated failure** : The system rejects the save and shows a red error highlight.
     2. **Corrective step** : Check for syntax errors, such as missing parentheses around `IF` conditions or lowercase keywords.



## Access advanced assets and references

Formulas must follow strict grammar and case-sensitivity rules for all built-in operators and functions. Use the following technical specifications to make sure your calculations are valid.

### Formula examples

The following templates demonstrate how to combine functions and operators to automate data enrichment. You can copy and adapt these snippets to match your specific field names and organizational requirements.

#### Example 1: Setting a risk level

Use this formula to categorize cases based on specific keywords found within the case title.

  * **Target Field** : `CaseCustom.risk_level` (Text)
  * **Goal** : Automatically assign a "High" status to urgent incidents
  * **Formula** :

`IF (CONTAINS([case.name], "urgent")) THEN "High" ELSE "Medium"`




#### Example 2: Flagging test alerts

This logic identifies and labels testing data to help analysts filter their primary views and maintain focus on production incidents.

  * **Target Field** : `AlertCustom.is_test` (Text)
  * **Goal** : Detect the `-TEST` suffix or `TEST` string in an alert name
  * **Formula** :
        
        IF (CONTAINS([alert.name], "TEST") OR ENDS_WITH([alert.name], "-TEST"))
        THEN "TRUE"
        ELSE "FALSE"
        




#### Example 3: Combining conditions

This example demonstrates nested logic to prioritize reviews based on both event volume and existing priority levels.

  * **Target Field** : `CaseCustom.review_status` (Text)
  * **Goal** : Trigger a manual review only when log length is significant and the priority is not `Low`.
  * **Formula** : 
        
        IF (LENGTH(\[AlertCustom.event\_details\]) \> 100 AND NOT IS(\[case.priority\], "Low"))
        THEN "Needs Review"
        ELSE "Auto-Closed"
        




### Formula language and syntax

The calculation engine is case-sensitive for all built-in operators, keywords, and functions. You must write keywords (for example, `IF, THEN, ELSE, AND, OR, NOT`) and function names (for example, `CONTAINS, LENGTH, STARTS_WITH, ENDS_WITH, IS, IS_NOT, DOES_NOT_CONTAIN`) in uppercase. However, testing of text strings within functions and equality operators is case-insensitive. For example, searching for "phishing" will successfully match "PHISHING" or "Phishing".

### Data types and literals

A literal is a fixed value used in expressions. We recommend that you make sure your operations and function arguments use compatible types.

Type | Syntax and rules | Example  
---|---|---  
**STRING** | Text enclosed in double quotes. | "critical", "N/A"  
**NUMBER** | Integer or decimal numbers. | 100, 3.14  
**BOOLEAN** | Must be uppercase. | TRUE, FALSE  
**NULL** | Represents an empty value. | NULL  
  
### Field references

To use the value of another field, enclose the field name in square brackets, such as `[object.field_name]`.

  * **Syntax rule:** You must use a prefix with field references. You must use a prefix (for example, `case.` or `AlertCustom.`) followed by a dot and the field name. The field name itself can contain **letters** , **numbers** , **underscores** , and **spaces**. For example: `[case.name]`, `[alert.priority]`, `[AlertCustom.my_custom_field]`.
  * You can use these system fields: `case.name`, `case.stage`, `case.priority`, `alert.name`, `alert.priority`, `alert.rule_generator`.
  * You can reference all user-defined Custom Fields.
  * A **Calculated Field** formula can't reference another **Calculated Field**.



### Operators

Use operators for comparisons and logical operations. Use parentheses `()` to override default precedence and group expressions

  * **Comparison operators** : `==`, `!=`, `>`, `>=`, `<`, `<=`
  * **Logical operators** : `AND`, `OR`, `NOT`
  * **Operator precedence** : `NOT`, `>`, `>=`, `<`, `<=`, `AND`, `OR`,



### Conditional expressions

The system supports conditional logic using the `IF (condition) THEN expression1 ELSE expression2` syntax. The `ELSE` part is optional; if you omit it and the condition is `FALSE`, the result defaults to `NULL`.

The condition must be an expression that evaluates to `TRUE` or `FALSE`.

For example, `IF ( [CaseCustom.score] > 75 ) THEN "High Risk" ELSE "Low Risk"`.

### Functions

Functions are predefined operations that must be entirely uppercase. The following table lists the supported functions for data manipulation and evaluation.

Function | Description | Syntax | Return Type  
---|---|---|---  
`CONTAINS(field, substring)` | Checks if a text field contains substring (case-insensitive) | `CONTAINS([case.name], "phishing")` | `BOOLEAN`  
`DOES_NOT_CONTAIN(field, substring)` | Checks if a text field doesn't contain a substring (case-insensitive) | `DOES_NOT_CONTAIN([case.name], "test")` | `BOOLEAN`  
`LENGTH(field)` | Returns the number of characters in a field | `LENGTH([case.name])` | `NUMBER`  
`STARTS_WITH(field, prefix)` | Checks if the field begins with a prefix (case-insensitive) | `STARTS_WITH([CaseCustom.hostname], "srv-")` | `BOOLEAN`  
`ENDS_WITH(field, suffix)` | Checks if the field ends with a suffix (case-insensitive) | `ENDS_WITH([AlertCustom.filename], ".exe")` | `BOOLEAN`  
`IS(field, literal)` | Checks if the field value is equal to literal (case-insensitive) | `IS([alert.priority], "High")` | `BOOLEAN`  
`IS_NOT(field, literal)` | Checks if the field value is NOT equal to literal (case-insensitive) | `IS_NOT([alert.priority], "Low")` | `BOOLEAN`  
  
### Reserved keywords and identifiers

The calculation engine reserves specific words for logical operations and functions. You cannot use these terms as custom field names or other identifiers within a formula:

  * **Logical** : `AND, OR, NOT, IF, THEN, ELSE`
  * **Values** : `NULL, TRUE, FALSE`
  * **Functions** : `CONTAINS, LENGTH, STARTS_WITH, ENDS_WITH, IS, IS_NOT, DOES_NOT_CONTAIN`



### Data type compatibility

To ensure successful evaluation, verify that all operations and function arguments use compatible types. Supported types include `STRING`, `NUMBER`, `BOOLEAN`, and `NULL`.

The formula's final output must match the **Target Field** 's expected type. Because **Target Fields** are restricted to "Free Text," your formula must ultimately resolve to a string or a value that can be implicitly cast to the target's format.

### Formatting and whitespace

While spaces, tabs, and newlines are generally ignored between tokens, they are strictly required to separate keywords from identifiers. Use whitespace strategically to structure complex, multi-line formulas for better maintainability and peer review.

### Write effective formulas

While the calculation engine is flexible with whitespace, follow these formatting standards to help prevent logic errors and simplify troubleshooting.

  * **Explicit grouping** : Use parentheses to define the order of operations clearly, even when relying on standard precedence. This helps prevent logical ambiguity.
  * **Visual structure** : Apply spaces around operators (`==, AND, OR`) and insert newlines for nested `IF/THEN` statements to make the logic scannable.
  * **Type validation** : Always verify that your formula's final output matches the Target Field's expected type to prevent evaluation errors.
        
        IF (
            (IS([CaseCustom.event_count], "100") AND NOT IS([case.priority], "Low"))
            OR CONTAINS([case.name], "Critical")
        )
        THEN "Needs Immediate Review"
        ELSE "Standard Review"
        




## Troubleshooting

This section outlines performance expectations and provides self-service fixes for common deployment issues encountered when building or managing formulas.

### Latency and limits

**Calculated Fields** evaluate synchronously whenever a dependency field changes. To maintain system performance, a **Calculated Field** cannot reference another **Calculated Field** ; the system blocks these chained dependencies to prevent recursion and processing delays.

### Error remediation

When you write formulas manually, errors can occur due to syntax or data type mismatches. Use the following table to map specific, journey-related error codes to their exact, actionable fixes.

Error type | Issue | Fix  
---|---|---  
Syntax | The formula violates grammar rules, such as mismatched parentheses or lowercase keywords. | Wrap all IF conditions in () and verify all keywords are UPPERCASE.  
Validation | The formula references an unknown field (for example, [\case.typo]) or results in a type mismatch. | Verify the field names in square brackets and confirm the output matches the Target Field type.  
Evaluation | The formula is valid but fails during execution, often displaying #ERROR!. | Check for runtime issues, such as passing a non-string value to a function like LENGTH().  
  
### Modify or delete target fields

The system actively protects the fields your formulas rely on to maintain data integrity. If you attempt to delete or modify a **Custom Field** used as a target field, the system blocks the action and displays a warning indicating its active use in a **Calculated Field**.

### Validation and testing

After saving a new calculation, verify the results by navigating to a case or alert and updating a dependency field. Confirm that the Target Field populates with the expected value in real time.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
