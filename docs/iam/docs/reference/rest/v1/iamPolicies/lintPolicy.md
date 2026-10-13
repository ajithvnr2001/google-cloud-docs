---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy/
title: Method: iamPolicies.lintPolicy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:43.059098+00:00
---

# Method: iamPolicies.lintPolicy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: iamPolicies.lintPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * LintResult
    * JSON representation
  * Level
  * Severity
  * Examples
  * Try it!



Lints, or validates, an IAM policy. Currently checks the `[google.iam.v1.Binding.condition](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding.FIELDS.condition)` field, which contains a condition expression for a role binding.

Successful calls to this method always return an HTTP `200 OK` status code, even if the linter detects an issue in the IAM policy.

### HTTP request

`POST https://iam.googleapis.com/v1/iamPolicies:lintPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
    
      // Union field lint_object can be only one of the following:
      "condition": {
        object ([Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr))
      }
      // End of list of possible types for union field lint_object.
    }  
  
Fields  
---  
`fullResourceName` |  `string` The full resource name of the policy this lint request is about.The name follows the Google Cloud format for full resource names. For example, a Google Cloud project with ID `my-project` will be named `//cloudresourcemanager.googleapis.com/projects/my-project`.The resource name is not used to read a policy from IAM. Only the data in the request object is linted.  
Union field `lint_object`. Required. The IAM object to be linted. `lint_object` can be only one of the following:  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr)`)` `[google.iam.v1.Binding.condition](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding.FIELDS.condition)` object to be linted.  
  
### Response body

The response of a lint operation. An empty response indicates the operation was able to fully execute and no lint issue was found.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "lintResults": [
        {
          object ([LintResult](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#LintResult))
        }
      ]
    }  
  
Fields  
---  
`lintResults[]` |  `object (`[LintResult](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#LintResult)`)` List of lint results sorted by `severity` in descending order.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## LintResult

Structured response of a single validation unit.

JSON representation  
---  
      
    
    {
      "level": enum ([Level](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#Level)),
      "validationUnitName": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#Severity)),
      "fieldName": string,
      "locationOffset": integer,
      "debugMessage": string
    }  
  
Fields  
---  
`level` |  `enum (`[Level](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#Level)`)` The validation unit level.  
`validationUnitName` |  `string` The validation unit name, for instance "lintValidationUnits/ConditionComplexityCheck".  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy#Severity)`)` The validation unit severity.  
`fieldName` |  `string` The name of the field for which this lint result is about.For nested messages `fieldName` consists of names of the embedded fields separated by period character. The top-level qualifier is the input object to lint in the request. For example, the `fieldName` value `condition.expression` identifies a lint result for the `expression` field of the provided condition.  
`locationOffset` |  `integer` 0-based character position of problematic construct within the object identified by `fieldName`. Currently, this is populated only for condition expression.  
`debugMessage` |  `string` Human readable debug message associated with the issue.  
  
## Level

Possible Level values of a validation unit corresponding to its domain of discourse.

Enums  
---  
`LEVEL_UNSPECIFIED` | Level is unspecified.  
`CONDITION` | A validation unit which operates on an individual condition within a binding.  
  
## Severity

Possible Severity values of an issued result.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Severity is unspecified.  
`ERROR` | A validation unit returns an error only for critical issues. If an attempt is made to set the problematic policy without rectifying the critical issue, it causes the `setPolicy` operation to fail.  
`WARNING` | Any issue which is severe enough but does not cause an error. For example, suspicious constructs in the input object will not necessarily fail `setPolicy`, but there is a high likelihood that they won't behave as expected during policy evaluation in `checkPolicy`. This includes the following common scenarios:

  * Unsatisfiable condition: Expired timestamp in date/time condition.
  * Ineffective condition: Condition on a <principal, role> pair which is granted unconditionally in another binding of the same policy.

  
`NOTICE` | Reserved for the issues that are not severe as `ERROR`/`WARNING`, but need special handling. For instance, messages about skipped validation units are issued as `NOTICE`.  
`INFO` | Any informative statement which is not severe enough to raise `ERROR`/`WARNING`/`NOTICE`, like auto-correction recommendations on the input content. Note that current version of the linter does not utilize `INFO`.  
`DEPRECATED` | Deprecated severity level.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
