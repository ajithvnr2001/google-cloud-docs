---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-iam-policy/
title: VerifyIAM policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:09.986745+00:00
---

# VerifyIAM policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  VerifyIAM policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Use the VerifyIAM policy to enforce authorization checks on API access, based on Google Cloud IAM. This is an alternative to the [OAuthv2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy), and the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy). For information on how to include VerifyIAM in an IAM-based access control solution, see [IAM-based API authentication overview](https://docs.cloud.google.com/apigee/docs/api-platform/security/iam/iam-overview).

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Important:** Use of VerifyIAM is subject to the [ Characteristics and limitations of IAM-based access control](https://docs.cloud.google.com/apigee/docs/api-platform/security/iam/iam-overview#characteristics-and-limitations-of-iam-based-access-control).**Note:** This policy is not available with Apigee hybrid at this time.

## Element reference

This reference shows the elements and attributes of the VerifyIAM policy.
    
    
    <VerifyIAM async="false" continueOnError="false" enabled="true" name="MyVerifyIAMPolicy">
        <DisplayName>Custom label used in UI</DisplayName>
        <CredentialSource>flow_variable_name_containing_credential_value</CredentialSource>
    </VerifyIAM>

## <VerifyIAM> attributes
    
    
    <VerifyIAM async="false" continueOnError="false" enabled="true" name="MyVerifyIAMPolicy">

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <CredentialSource> element
    
    
    <CredentialSource>flow_variable_name_containing_credential_value</CredentialSource>

This element specifies the flow variable containing the credential value, and has these characteristics:

  * Typically, the client sends the value in a query parameter, HTTP header, or a form parameter. The string must specify the corresponding flow variable in the form `request.queryparam.token`.
  * When read from the reference, a direct value is expected. For example, 'Bearer' should not be present as the prefix.
  * If omitted, policy execution assumes the value is in the authorization header and in the standard format "Bearer xyz".

Default | N/A  
---|---  
Presence | Optional  
Type | Flow variable  
  
Example:
    
    
    <VerifyIAM async="false" continueOnError="false" enabled="true" name="Verify-IAM-Permissions-1">
        <DisplayName>VerifyIAM policy for flow 1</DisplayName>
        <CredentialSource>request.queryparam.token</CredentialSource>
    </VerifyIAM>

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.verifyiam.CredentialSourceRefUnresolved` | `400` | Flow variable provided inside credential source could not be resolved.  
`steps.verifyiam.CredentialValueNotProvided` | `400` | Credential not found. If the credential source reference is not provided, we look at the default place like authorization header.  
`steps.verifyiam.Forbidden` | `403` | Request could not be forwarded due to lack of sufficient permissions or missing access scopes or any other related issues.  
`steps.verifyiam.MiscellaneousAuthorizationConfigurationError` | `500` | An issue with the authentication request to IAM. The API producer needs to fix this error based on details in the error response.  
`steps.verifyiam.Unauthorized` | `401` | Problem with the credential, such as the value being invalid or expired.  
`steps.verifyiam.UnexpectedAuthorizationInfrastructureError` | `500` | Internal error.  
  
### Deployment errors

This policy does not return any policy-specific deployment errors.

### Fault variables

These variables are set when this policy triggers an error at runtime.

**Note:** You can use these variables to create Fault Rule conditions. Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name="Unauthorized"`  
`verifyiam.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `verifyiam.Verify-IAMToken.failed = true`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
