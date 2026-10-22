---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-saml-assertion-policy/
title: GenerateSAMLAssertion policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:39.647047+00:00
---

# GenerateSAMLAssertion policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-saml-assertion-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  GenerateSAMLAssertion policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The GenerateSAMLAssertion policy enables API proxies to attach SAML assertions to outbound XML requests. Those assertions are then available to backend services to apply further security processing for authentication and authorization. See [SAML policies overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policies-overview) for more information.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Samples
    
    
    <GenerateSAMLAssertion name="SAML" ignoreContentType="false">
      <CanonicalizationAlgorithm />
      <Issuer ref="reference">Issuer name</Issuer>
      <KeyStore>
        <Name ref="reference">keystorename</Name>
        <Alias ref="reference">alias</Alias>
      </KeyStore>
      <OutputVariable>
        <FlowVariable>assertion.content</FlowVariable>
        <Message name="request">
          <Namespaces>
            <Namespace prefix="soap">http://schemas.xmlsoap.org/soap/envelope/</Namespace>
            <Namespace prefix='wsse'>http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd</Namespace>
          </Namespaces>
          <XPath>/soap:Envelope/soap:Header/wsse:Security</XPath>
        </Message>
      </OutputVariable>
      <SignatureAlgorithm />
      <Subject ref="reference">Subject name</Subject>
      <Template ignoreUnresolvedVariables="false">
        <!-- A lot of XML goes here, within CDATA, with {} around
             each variable -->
      </Template>
    </GenerateSAMLAssertion>

## Element reference

This section lists the elements and attributes of the GenerateSAMLAssertion policy.

### Attributes that apply to the top-level element
    
    
    <GenerateSAMLAssertion name="SAML-A1" continueOnError="false" enabled="true" async="false">

The following attributes are common to all policy parent elements.

**Attribute** | **Description** | **Default** | **Presence**  
---|---|---|---  
name |  The internal name of the policy. Characters you can use in the name are restricted to: `A-Z0-9._\-$ %`. However, the Apigee UI enforces additional restrictions, such as automatically removing characters that are not alphanumeric. Optionally, use the `<displayname></displayname>` element to label the policy in the Apigee UI proxy editor with a different, natural-language name. | N/A | Required  
enabled |  Set to `true` to enforce the policy. Set to `false` to "turn off" the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
  
### Elements and attributes for SAML assertion generation

Field Name | Description  
---|---  
`ignoreContentType` attribute | A boolean that can be set to `true` or `false`. By default, the assertion will not be generated if the content type of the message is not an XML Content-Type. If this is set to `true`, then the message will be treated as XML regardless of the Content-type.  
`Issuer` |  The unique identifier of the identity provider. If the optional `ref` attribute is present, then the value of Issuer will be assigned at runtime based on the specified variable. If the optional `ref` attribute is not present, then the value of Issuer will be used.   
`KeyStore` |  The name of the KeyStore that contains the private key and the alias of the private key used to digitally sign SAML assertions.   
`OutputVariable` |  Specifies where the generated SAML assertion will be placed. The assertion can be stored in a flow variable or inserted into an existing message.   
`FlowVariable` |  Specifies the name of the flow variable where the generated SAML assertion content will be stored. This is an alternative to using the `<Message>` element to insert the assertion into an existing XML message.   
`Message` | The target of the policy. Valid values are `message`, `request`, and `response`. When set to `message`, the policy conditionally retrieves the message object based on the attachment point of the policy. When attached to the request Flow, the policy resolves `message` to request, and when attached to the response Flow, the policy resolves `message` to response.   
`XPath` | An XPath expression that indicates the element on the outbound XML document to which the policy will attach the SAML assertion.  
`SignatureAlgorithm` | SHA1 or SHA256  
`Subject` |  The unique identifier of the subject of the SAML assertion. If the optional `ref` attribute is present, then the value of Subject will be assigned at runtime based on the specified variable. If the optional `ref` attribute is not present, then the value of Subject will be used.   
`Template` |  If present, then the assertion will be generated by running this template, replacing everything denoted `{}` with the corresponding variable, and then digitally signing the result. The template is processed following the AssignMessage policy rules. See [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). The `<Template>` element supports the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro). Message templating is only supported when the policy signature is `GenerateSamlAssertion`.  
  
## Usage notes

Policy processing:

  1. If the message is not XML, and `ignoreContentType` is not set to `true`, then raise a fault.
  2. If `Template` is set, then process the template as described for the AssignMessage policy. If any variables are missing and `ignoreUnresolvedVariables` is not set, then raise a fault.
  3. If `Template` is not set, then construct an assertion that includes the values of the Subject and Issuer parameters or their references.
  4. Sign the assertion using the specified key.
  5. Add the assertion to the message at the specified XPath.



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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
