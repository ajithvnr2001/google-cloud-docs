---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/validate-saml-assertion-policy/
title: ValidateSAMLAssertion policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:32:40.120882+00:00
---

# ValidateSAMLAssertion policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/validate-saml-assertion-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ValidateSAMLAssertion policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The ValidateSAMLAssertion policy enables API proxies to validate SAML assertions that are attached to inbound SOAP requests. The SAML policy validates incoming messages that contain a digitally-signed SAML assertion, rejects them if they are invalid, and sets variables that allow additional policies, or the backend services itself, to further validate the information in the assertion. See [SAML policies overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policies-overview) for more information.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Samples
    
    
    <ValidateSAMLAssertion name="SAML" ignoreContentType="false">
      <Source name="request">
        <Namespaces>
          <Namespace prefix='soap'>http://schemas.xmlsoap.org/soap/envelope/</Namespace>
          <Namespace prefix='wsse'>http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd</Namespace>
          <Namespace prefix='saml'>urn:oasis:names:tc:SAML:2.0:assertion</Namespace>
        </Namespaces>
        <AssertionXPath>/soap:Envelope/soap:Header/wsse:Security/saml:Assertion</AssertionXPath>
        <SignedElementXPath>/soap:Envelope/soap:Header/wsse:Security/saml:Assertion</SignedElementXPath>
      </Source>
      <TrustStore>TrustStoreName</TrustStore>
      <RemoveAssertion>false</RemoveAssertion>
    </ValidateSAMLAssertion>

## Element reference

### Validate SAML Assertion

Field Name | Description  
---|---  
`name` attribute |  The name of the policy instance. The name must be unique in the organization. Characters you can use in the name are restricted to: `A-Z0-9._\-$ %`. However, the Apigee UI enforces additional restrictions, such as automatically removing characters that are not alphanumeric.   
`ignoreContentType` attribute | A boolean that can be set to `true` or `false`. By default, the assertion will not be validated if the content type of the message is not an XML Content-Type. If this is set to `true` then the message will be treated as XML regardless of the Content-type.  
`Source` | The target of the policy. Valid values are `message`, `request`, and `response`. When set to `message`, the policy conditionally retrieves the message object based on the attachment point of the policy. When attached to the request Flow, the policy resolves `message` to `request`, and when attached to the response Flow, the policy resolves `message` to `response`.   
`XPath` |  **Deprecated.** Child of `Source`. Use `AssertionXPath` and `SignedElementXPath`.   
`AssertionXPath` |  Child of `Source`. An XPath expression that indicates the element on the inbound XML document from which the policy can extract the SAML assertion.   
`SignedElementXPath` |  Child of `Source`. An XPath expression that indicates the element on the inbound XML document from which the policy can extract the signed element. This may be different or the same as the XPath for the `AssertionXPath`.   
`TrustStore` |  The name of the TrustStore that contains trusted X.509 certificates used to validate digital signatures on SAML assertions.   
`RemoveAssertion` |  A boolean that can be set to `true` or `false`. When `true`, the SAML assertion will be stripped from the request message before the message is forwarded to the backend service.   
  
## Usage notes

Policy processing:

  1. The policy checks the inbound message to verify that the request's media type is XML, by checking if the content type matches the formats `text/(.*+)?xml` or `application/(.*+)?xml`. If the media type is not XML and the `ignoreContentType` attribute is not set to `true`, then the policy will raise a fault.
  2. The policy will parse the XML. If parsing fails then it will raise a fault.
  3. The policy will extract the signed element and the assertion, using the respective XPaths specified (`<SignedElementXPath>` and `<AssertionXPath>`). If either of these paths do not return an element, then the policy will raise a fault.
  4. The policy will verify that the Assertion is the same as the signed element, or is a child of the signed element. If this is not true, then the policy will raise a fault.
  5. If either of the `<NotBefore>` or `<NotOnOrAfter>` elements are present in the assertion, the policy will check the current timestamp against these values, as described in SAML Core section 2.5.1.
  6. The policy will apply any additional rules for processing the "Conditions" as described in SAML Core section 2.5.1.1.
  7. The policy validates the XML digital signature using the trust store value (`<TrustStore>`) described above. If validation fails, the policy raises a fault.



Once the policy has completed without raising a fault, the developer of the proxy can be sure of the following:

  * The digital signature on the assertion is valid and was signed by a trusted CA
  * The assertion is valid for the current time period
  * The subject and issuer of the assertion will be extracted and set in flow variables. It is the responsibility of other policies to use these values for additional authentication, such as checking that the subject name is valid, or passing it to a target system for validation.



Other policies, such as ExtractVariables, may be used to parse the raw XML of the assertion for more complex validation.

## Flow variables

There are many pieces of information that may be specified in a SAML assertion. The SAML assertion itself is XML that can be parsed using the [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) and other mechanisms in order to implement more complex validations.

Variable | Description  
---|---  
`saml.id` | The SAML assertion ID  
`saml.issuer` | The "Issuer" of the assertion, converted from its native XML type to a string  
`saml.subject` | The "Subject" of the assertion, converted from its native XML type to a string  
`saml.valid` | Returns true or false based on the result of the validity check  
`saml.issueInstant` | IssueInstant  
`saml.subjectFormat` | Subject format  
`saml.scmethod` | Subject confirmation method  
`saml.scdaddress` | Subject confirmation data address  
`saml.scdinresponse` | Subject confirmation data in response  
`saml.scdrcpt` | Subject confirmation data recipient  
`saml.authnSnooa` | AuthnStatement SessionNotOnOrAfter  
`saml.authnContextClassRef` | AuthnStatement AuthnContextClassRef  
`saml.authnInstant` | AuthnStatement AuthInstant  
`saml.authnSessionIndex` | AuthnStatement Session Index  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information. Error name | Cause | Fix  
---|---|---  
`SourceNotConfigured` |  One or more of the following elements of the `ValidateSAMLAssertion` policy is not defined or empty: `<Source>`, `<XPath>`, `<Namespaces>`, `<Namespace>`.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors#sourcenotconfigured)  
`TrustStoreNotConfigured` |  If the `<TrustStore>` element is empty or not specified in the `ValidateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid truststore is required.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors#truststorenotconfigured)  
`NullKeyStoreAlias` |  If the child element `<Alias>` is empty or not specified in the `<Keystore>` element of `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid keystore alias is required.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors#nullkeystorealias)  
`NullKeyStore` |  If the child element `<Name>` is empty or not specified in the `<Keystore>` element of `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid keystore name is required.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors#nullkeystore)  
`NullIssuer` |  If the `<Issuer>` element is empty or not specified in the `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid `<Issuer>` value is required.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors#nullissuer)  
  
### Fault variables

These variables are set when a runtime error occurs. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault. The fault name is the last part of the fault code. | `fault.name = "InvalidMediaTpe"`  
`GenerateSAMLAssertion.failed` | For a validate SAML assertion policy configuration, the error prefix is `ValidateSAMLAssertion`. | `GenerateSAMLAssertion.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "GenerateSAMLAssertion[GenSAMLAssert]: Invalid media type",
        "detail": {
          "errorcode": "steps.saml.generate.InvalidMediaTpe"
        }
      }
    }

### Example fault rule
    
    
    <FaultRules>
        <FaultRule name="invalid_saml_rule">
            <Step>
                <Name>invalid-saml</Name>
            </Step>
            <Condition>(GenerateSAMLAssertion.failed = "true")</Condition>
        </FaultRule>
    </FaultRules>

## Related topics

Extracting variables: [Extract Variables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
