---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors/
title: SAML Assertion policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:43.008210+00:00
---

# SAML Assertion policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  SAML Assertion policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/samlassertion-deployment-errors/).

## SourceNotConfigured

### Error Message

Deployment of the API proxy through either the [Apigee UI](https://apigee.google.com) or [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    ValidateSAMLAssertion[policy_name]: Source is not correctly configured.

### Example Error Message
    
    
    Error Deploying Revision 2 to test
    ValidateSAMLAssertion[Validate-SAML-Assertion-1]: Source is not correctly configured.
    

### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/saml-assert-error-1.png)

### Cause

The deployment of the API proxy fails with this error if one or more of the following elements of the `ValidateSAMLAssertion` policy is not defined or empty: `<Source>`, `<XPath>`, `<Namespaces>`, `<Namespace>`.

For example, if you miss the `<XPath>` element or leave the `<Source>` element or its entities empty, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the failed `ValidateSAMLAssertion` policy name from the error message. For example, in the following error the `ValidateSAMLAssertion` policy name is `Validate-SAML-Assertion-1`.
         
         ValidateSAMLAssertion[Validate-SAML-Assertion-1]: Source is not correctly configured.
         

  2. Examine the failed `ValidateSAMLAssertion` policy XML. Check if one or more of the following elements of the policy is missing or empty: `<Source>`, `<XPath>`, `<Namespaces>`, `<Namespace>`. If so, that could be the cause of the error.

For example, the following policy has an empty `<Namespaces>` element under the `<Source>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ValidateSAMLAssertion name="SAML" ignoreContentType="false">
           <Source name="request">
             <Namespaces></Namespaces>
            </Source>
            <Description/>
          <TrustStore>ref://TrustStoreName</Truststore>
          <RemoveAssertion>false</RemoveAssertion>
         </ValidateSAMLAssertion>
         

  3. In the above example, the `<Namespaces>` element is empty, therefore you get the error:
         
         ValidateSAMLAssertion[Validate-SAML-Assertion-1]: Source is not correctly configured.
         




### Resolution

Ensure that values of the `<Source>` element are configured correctly with the `<Namespaces>` element and its child element `<Namespace>`. You also need to ensure the `<XPath>` element is defined and non-empty.

To correct the example `ValidateSAMLAssertion` policy shown above, you could add the `<Namespace>` elements as well as `<XPath>`:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ValidateSAMLAssertion name="SAML" ignoreContentType="false">
      <Source name="request">
        <Namespaces>
          <Namespace prefix='soap'>http://schemas.xmlsoap.org/soap/envelope/</Namespace>
          <Namespace prefix='wsse'>http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd</Namespace>
          <Namespace prefix='saml'>urn:oasis:names:tc:SAML:2.0:assertion</Namespace>
        </Namespaces>
        <XPath>/soap:Envelope/soap:Header/wsse:Security/saml:Assertion</XPath>
      </Source>
       <Description/>
    <TrustStore>ref://TrustStoreName</Truststore>
    <RemoveAssertion>false</RemoveAssertion>
    </ValidateSAMLAssertion>
    

## TrustStoreNotConfigured

### Error Message

Deployment of the API proxy through either the [Apigee UI](https://apigee.google.com) or [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    ValidateSAMLAssertion[[Ljava.lang.Object;@object]: Trust store is not correctly configured.

### Example Error Message
    
    
    Error Deploying Revision 2 to test
    ValidateSAMLAssertion[[Ljava.lang.Object;@39537262]: Trust store is not correctly configured.
    

### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/saml-assert-error-2.png)

### Cause

If the `<TrustStore>` element is empty or not specified in the ValidateSAMLAssertion policy, then the deployment of the API proxy fails. A valid Trust Store is required.

### Diagnosis

  1. Examine all the Validate SAML Assertion policies in the specific API Proxy where the failure has occurred. If there is any Validate SAML Assertion policy in which the `<TrustStore>` element is empty or not specified, then that's the cause of the error.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ValidateSAMLAssertion name="SAML" ignoreContentType="false">
          <Source name="request">
             <Namespaces>
               <Namespace prefix='soap'>http://schemas.xmlsoap.org/soap/envelope/</Namespace>
               <Namespace prefix='wsse'>http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd</Namespace>
               <Namespace prefix='saml'>urn:oasis:names:tc:SAML:2.0:assertion</Namespace>
             </Namespaces>
             <XPath>/soap:Envelope/soap:Header/wsse:Security/saml:Assertion</XPath>
           </Source>
             <Description/>
             <TrustStore/>
           <RemoveAssertion>false</RemoveAssertion>
         </ValidateSAMLAssertion>
         




### Resolution

Ensure that the element `<TrustStore>` is always specified and non-empty within the [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy). The `<TrustStore>` name should match the name of a valid TrustStore that exists in all the environments to which you are attempting to deploy a proxy.

To correct the above example, you can specify the `<TrustStore>` element with a valid value.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ValidateSAMLAssertion name="SAML" ignoreContentType="false">
      <Source name="request">
        <Namespaces>
          <Namespace prefix='soap'>http://schemas.xmlsoap.org/soap/envelope/</Namespace>
          <Namespace prefix='wsse'>http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd</Namespace>
          <Namespace prefix='saml'>urn:oasis:names:tc:SAML:2.0:assertion</Namespace>
        </Namespaces>
        <XPath>/soap:Envelope/soap:Header/wsse:Security/saml:Assertion</XPath>
      </Source>
      <TrustStore>TrustStoreName</TrustStore>
      <RemoveAssertion>false</RemoveAssertion>
    </ValidateSAMLAssertion>
    

## NullKeyStore

### Error Message

Deployment of the API proxy through either the [Apigee UI](https://apigee.google.com) or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Assertion KeyStore name cannot be null.

### Example Error Message
    
    
    Error Deploying Revision 4 to test
    Assertion KeyStore name cannot be null.
    

### Example Error Screenshot

![Error deploying revision 4 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/saml-assert-error-3.png)

### Cause

If the child element `<Name>` is empty or not specified in the `<Keystore>` element of `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid Keystore name is required.

### Diagnosis

  1. Examine all the `GenerateSAMLAssertion` policies in the specific API Proxy where the failure has occurred. If there is any `GenerateSAMLAssertion` policy in which the child element `<Name>` is empty or not specified in the `<Keystore>` element, then that's the cause of the error.

The following `GenerateSAMLAssertion` policy has an empty child element `<Name>` in the `<Keystore>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <GenerateSAMLAssertion name="SAML" ignoreContentType="false">`
           <CanonicalizationAlgorithm />
           <Issuer ref="reference">Issuer name</Issuer>
           <KeyStore>
             <Name></Name>
             <Alias ref="reference">alias</Alias>
           </KeyStore>
           <OutputVariable>
             <FlowVariable>assertion.content</FlowVariable>
             <Message name="request">
               <Namespaces>
                 <Namespace prefix="test">http://www.example.com/test</Namespace>
               </Namespaces>
               <XPath>/envelope/header</XPath>
             </Message>
           </OutputVariable>
           <SignatureAlgorithm />
           <Subject ref="reference">Subject name</Subject>
           <Template ignoreUnresolvedVariables="false">
             <!-- A lot of XML goes here, in CDATA, with {} around
                  each variable -->
           </Template>
         </GenerateSAMLAssertion>
         




### Resolution

Ensure that the child element `<Name>` is always specified and non-empty within the `<Keystore>` element of the `GenerateSAMLAssertion` policy.

To correct the above example, you can specify the `<Name>` element correctly as well as ensure that a valid value is specified to the `<Alias>` element.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
            <Namespace prefix="test">http://www.example.com/test</Namespace>
          </Namespaces>
          <XPath>/envelope/header</XPath>
        </Message>
      </OutputVariable>
      <SignatureAlgorithm />
      <Subject ref="reference">Subject name</Subject>
      <Template ignoreUnresolvedVariables="false">
        <!-- A lot of XML goes here, in CDATA, with {} around
             each variable -->
      </Template>
    </GenerateSAMLAssertion>
    

Refer to examples from [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy).

## NullKeyStoreAlias

### Error Message

Deployment of the API proxy through either the [Apigee UI](https://apigee.google.com) or [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Assertion KeyStore alias cannot be null.

### Example Error Message
    
    
    Error Deploying Revision 4 to test
    Assertion KeyStore alias cannot be null.
    

### Example Error Screenshot

![Error deploying revision 4 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/saml-assert-error-4.png)

### Cause

If the child element `<Alias>` is empty or not specified in the `<Keystore>` element of `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid Keystore alias is required.

### Diagnosis

  1. Examine all the `GenerateSAMLAssertion` policies in the specific API Proxy where the failure has occurred. If there is any `GenerateSAMLAssertion` policy in which the child element `<Alias>` is empty or not specified in the `<Keystore>` element, then that's the cause of the error.

The following `GenerateSAMLAssertion` has an empty child element `<Alias>` in the `<Keystore>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <GenerateSAMLAssertion name="SAML" ignoreContentType="false">`
           <CanonicalizationAlgorithm />
           <Issuer ref="reference">Issuer name</Issuer>
           <KeyStore>
             <Name ref="reference">keystorename</Name>
             <Alias></Alias>
           </KeyStore>
           <OutputVariable>
             <FlowVariable>assertion.content</FlowVariable>
             <Message name="request">
               <Namespaces>
                 <Namespace prefix="test">http://www.example.com/test</Namespace>
               </Namespaces>
               <XPath>/envelope/header</XPath>
             </Message>
           </OutputVariable>
           <SignatureAlgorithm />
           <Subject ref="reference">Subject name</Subject>
           <Template ignoreUnresolvedVariables="false">
             <!-- A lot of XML goes here, in CDATA, with {} around
                  each variable -->
           </Template>
         </GenerateSAMLAssertion>
         




### Resolution

Ensure that the child element `<Name>` is always specified and non-empty within the `<Keystore>` element of the `GenerateSAMLAssertion` policy.

To correct the above example, you can specify the `<Alias>` element correctly as well as ensure that a valid value is specified to the `<Name>` element.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
            <Namespace prefix="test">http://www.example.com/test</Namespace>
          </Namespaces>
          <XPath>/envelope/header</XPath>
        </Message>
      </OutputVariable>
      <SignatureAlgorithm />
      <Subject ref="reference">Subject name</Subject>
      <Template ignoreUnresolvedVariables="false">
        <!-- A lot of XML goes here, in CDATA, with {} around
             each variable -->
      </Template>
    </GenerateSAMLAssertion>
    

Refer to examples from [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy).

## NullIssuer

### Error Message

Deployment of the API proxy through either the [Apigee UI](https://apigee.google.com) or [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Assertion Issuer cannot be null.

### Example Error Message
    
    
    Error Deploying Revision 4 to test
    Assertion Issuer cannot be null.
    

### Example Error Screenshot

![Error deploying revision 4 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/saml-assert-error-5.png)

### Cause

If the `<Issuer>` element is empty or not specified in the `GenerateSAMLAssertion` policy, then the deployment of the API proxy fails. A valid `<Issuer>` value is required.

### Diagnosis

  1. Examine all the `GenerateSAMLAssertion` policies in the specific API Proxy where the failure has occurred. If there is any `GenerateSAMLAssertion` policy in which the `<Issuer>` element is empty or not specified, then that's the cause of the error.

The following `GenerateSAMLAssertion` policy has an empty `<Issuer>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <GenerateSAMLAssertion name="SAML" ignoreContentType="false">`
           <CanonicalizationAlgorithm />
           <Issuer></Issuer>
           <KeyStore>
             <Name ref="reference">keystorename</Name>
             <Alias ref="reference">alias</Alias>
           </KeyStore>
           <OutputVariable>
             <FlowVariable>assertion.content</FlowVariable>
             <Message name="request">
               <Namespaces>
                 <Namespace prefix="test">http://www.example.com/test</Namespace>
               </Namespaces>
               <XPath>/envelope/header</XPath>
             </Message>
           </OutputVariable>
           <SignatureAlgorithm />
           <Subject ref="reference">Subject name</Subject>
           <Template ignoreUnresolvedVariables="false">
             <!-- A lot of XML goes here, in CDATA, with {} around
                  each variable -->
           </Template>
         </GenerateSAMLAssertion>
         




### Resolution

Ensure that the `<Issuer>` element is always specified and non-empty in the `GenerateSAMLAssertion` policy.

To correct the above example, specify the `<Issuer>` element correctly:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
            <Namespace prefix="test">http://www.example.com/test</Namespace>
          </Namespaces>
          <XPath>/envelope/header</XPath>
        </Message>
      </OutputVariable>
      <SignatureAlgorithm />
      <Subject ref="reference">Subject name</Subject>
      <Template ignoreUnresolvedVariables="false">
        <!-- A lot of XML goes here, in CDATA, with {} around
             each variable -->
      </Template>
    </GenerateSAMLAssertion>
    

Refer to examples from [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
