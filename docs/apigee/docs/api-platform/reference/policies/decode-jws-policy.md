---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jws-policy/
title: DecodeJWS policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:32.835910+00:00
---

# DecodeJWS policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jws-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  DecodeJWS policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The DecodeJWS policy decodes the JWS header without verifying the signature on the JWS, and writes each header to a flow variable. This policy is most useful when used in concert with the [VerifyJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jws-policy), when the value of a header from within the JWS must be known before verifying the signature of the JWS.

A JWS can have an _attached_ payload, as in the form:
    
    
    header.payload.signature

Or, the JWS can omit the payload, called a _detached_ payload, and be in the form:
    
    
    header..signature

The DecodeJWS policy works with both forms because it only decodes the header portion of the JWS. The DecodeJWS policy also works regardless of the algorithm that was used to sign the JWS.

See [JWS and JWT policies overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) for a detailed introduction and an overview of the format of a JWS.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

### Sample: Decode a JWS

The policy shown below decodes a JWS found in the flow variable **var.JWS**. This variable must be present and contain a viable (decodable) JWS. The policy can obtain the JWS from any flow variable.
    
    
    <DecodeJWS name="JWS-Decode-HS256">
        <DisplayName>JWS Verify HS256</DisplayName>
        <Source>var.JWS</Source>
    </DecodeJWS>

For each header in the header portion of the JWS, the policy sets a flow variable named:
    
    
    jws.policy-name.header.header-name

If the JWS has an attached payload, then it sets the `jws.policy-name.header.payload` flow variable to the payload. For a detached payload, `payload` is empty. See Flow variables for a complete list of the variables set by this policy. 

## Element reference for Decode JWS

The policy reference describes the elements and attributes of the Decode JWS policy.

### Attributes that apply to the top-level element
    
    
    <DecodeJWS name="JWS" continueOnError="false" enabled="true" async="false">

The following attributes are common to all policy parent elements.

**Attribute** | **Description** | **Default** | **Presence**  
---|---|---|---  
name |  The internal name of the policy. Characters you can use in the name are restricted to: `A-Z0-9._\-$ %`. However, the Apigee UI enforces additional restrictions, such as automatically removing characters that are not alphanumeric. Optionally, use the `<displayname></displayname>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
continueOnError |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. | false | Optional  
enabled |  Set to `true` to enforce the policy. Set to `false` to "turn off" the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
async | This attribute is deprecated. | false | Deprecated  
  
## <DisplayName>
    
    
    <DisplayName>Policy Display Name</DisplayName>

Use in addition to the name attribute to label the policy in the management UI proxy editor with a different, natural-language name.

**Default** | If you omit this element, the value of the policy's name attribute is used.  
---|---  
**Presence** | Optional  
**Type** | String  
  
## <Source>
    
    
    <Source>JWS-variable</Source>

If present, specifies the flow variable in which the policy expects to find the JWS to decode.

**Note:** By default, the JWS is retrieved from the variable **request.header.authorization**. In this case, Apigee looks for the JWS in the request Authorization header. If you pass the JWS in the Authorization header, you do not need to include the `Source` element in the policy; however, you **must** include **Bearer** in the auth header. For example, you would pass the JWS in the Authorization header like this: 
    
    
    curl -v http://52.200.92.187:9001/doctest-JWS/verify-rs256 -H "Authorization: Bearer <your JWS>"

You can configure to policy to retrieve the JWS from a form or query parameter variable or any other variable. If the variable does not exist or if the policy otherwise can't find the JWS, the policy returns an error.

**Default** | `request.header.authorization` (See the note above for important information about the default).  
---|---  
**Presence** | Optional  
**Type** | String  
**Valid values** | An Apigee flow variable name  
  
## Flow variables

Upon success, the **Verify JWS** and **Decode JWS** policies set context variables according to this pattern:
    
    
    jws.{policy_name}.{variable_name}

For example, if the policy name is `verify-jws`, then the policy will store the algorithm specified in the JWS to this context variable: `jws.verify-jws.header.algorithm`

Variable name | Description  
---|---  
`decoded.header._name_` | The JSON-parsable value of a header in the payload. One variable is set for every header in the payload. While you can also use the `header._name_` flow variables, this is the recommended variable to use to access a header.  
`header.algorithm` | The signing algorithm used on the JWS. For example, RS256, HS384, and so on. See [(Algorithm) Header Parameter](https://tools.ietf.org/html/rfc7515#section-4.1.1) for more.  
`header.kid` | The Key ID, if added when the JWS was generated. See also "Using a JSON Web Key Set (JWKS)" at [JWT and JWS policies overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) to verify a JWS. See [(Key ID) Header Parameter](https://tools.ietf.org/html/rfc7515#section-4.1.4) for more.  
`header.type` | The header type value. See [(Type) Header Parameter](https://tools.ietf.org/html/rfc7515#section-4.1.9) for more.  
`header._name_` | The value of the named header (standard or additional). One of these will be set for every additional header in the header portion of the JWS.  
`header-json` | The header in JSON format.  
`payload` | The JWS payload if the JWS has an attached payload. For a detached paylod, this variable is empty.  
`valid` |  In the case of VerifyJWS, this variable will be true when the signature is verified, and the current time is before the token expiry, and after the token notBefore value, if they are present. Otherwise false. In the case of DecodeJWS, this variable is not set.  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Occurs when  
---|---|---  
`steps.jws.FailedToDecode` | `401` | The policy was unable to decode the JWS. The JWS is possibly corrupted.  
`steps.jws.FailedToResolveVariable` | `401` | Occurs when the flow variable specified in the ` <Source>` element of the policy does not exist.  
`steps.jws.InvalidClaim` | `401` | For a missing claim or claim mismatch, or a missing header or header mismatch.   
`steps.jws.InvalidJsonFormat` | `401` | Invalid JSON found in the JWS header.  
`steps.jws.InvalidJws` | `401` | This error occurs when the JWS signature verification fails.  
`steps.jws.InvalidPayload` | `401` | The JWS payload is invalid.  
`steps.jws.InvalidSignature` | `401` | `<DetachedContent>` is omitted and the JWS has a detached content payload.  
`steps.jws.MissingPayload` | `401` | The JWS payload is missing.  
`steps.jws.NoAlgorithmFoundInHeader` | `401` | Occurs when the JWS omits the algorithm header.  
`steps.jws.UnknownException` | `401` | An unknown exception occurred.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Occurs when  
---|---  
`InvalidAlgorithm` | The only valid values are: `RS256, RS384, RS512, PS256, PS384, PS512, ES256, ES384, ES512, HS256, HS384, HS512`.  
`EmptyElementForKeyConfiguration` `FailedToResolveVariable` `InvalidConfigurationForActionAndAlgorithmFamily` `InvalidConfigurationForVerify` `InvalidEmptyElement` `InvalidFamiliesForAlgorithm` `InvalidKeyConfiguration` `InvalidNameForAdditionalClaim` `InvalidNameForAdditionalHeader` `InvalidPublicKeyId` `InvalidPublicKeyValue` `InvalidSecretInConfig` `InvalidTypeForAdditionalClaim` `InvalidTypeForAdditionalHeader` `InvalidValueForElement` `InvalidValueOfArrayAttribute` `InvalidVariableNameForSecret` `MissingConfigurationElement` `MissingElementForKeyConfiguration` `MissingNameForAdditionalClaim` `MissingNameForAdditionalHeader` | Other possible deployment errors.  
  
### Fault variables

These variables are set when a runtime error occurs. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "TokenExpired"`  
`JWS.failed` | All JWS policies set the same variable in the case of a failure. | `jws.JWS-Policy.failed = true`  
  
### Example error response

For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.

### Example fault rule
    
    
    <FaultRules>
        <FaultRule name="JWS Policy Errors">
            <Step>
                <Name>JavaScript-1</Name>
                <Condition>(fault.name Matches "TokenExpired")</Condition>
            </Step>
            <Condition>JWS.failed=true</Condition>
        </FaultRule>
    </FaultRules>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
