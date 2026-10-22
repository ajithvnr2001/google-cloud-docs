---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/soap-message-validation-deployment-errors/
title: SOAP Message Validation policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:57.617480+00:00
---

# SOAP Message Validation policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/soap-message-validation-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  SOAP Message Validation policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/soap-message-validation-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/soap-message-validation-deployment-errors/).

## InvalidResourceType

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    MessageValidation soap_message_validation_policy: Invalid Resource Type resource_type. It should be xsd or wsdl. Context Revision:revision_number;APIProxy:apiproxy_name;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    MessageValidation SOAP-Message-Validation-1: Invalid Resource Type py.
    It should be xsd or wsdl. Context Revision:1;APIProxy:soapmessagevalidation;
    Organization:gsc-hipaa;Environment:test.
    

### Example Error Screenshot

![Invalid resource error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/invalid-resource-type.png)

### Cause

This error occurs if the `<ResourceURL>` element in the SOAPMessageValidation policy is set to a resource type not supported by the policy. Supported resource types are `xsd` and `wsdl`.

### Diagnosis

  1. Identify the SOAPMessageValidation policy name and the invalid resource type used in the `<ResourceURL>` element of the policy. You can find both of these items in the error message. For example, in the following error the SOAPMessageValidation policy name is `SOAP-Message-Validation-1` and the resource type is `py`.
         
         Error Deploying Revision 1 to test
         MessageValidation SOAP-Message-Validation-1: Invalid Resource Type py. It should
         be xsd or wsdl. Context Revision:1;APIProxy:soapmessagevalidation;Organization:gsc-
         hipaa;Environment:test.
         

  2. Examine the failed SOAPMessageValidation policy XML. If the resource type specified for the `<ResourceURL>` element matches the invalid resource type identified in Step 1 above, then that's the cause of the error.

For example, the following policy specifies the resource type as `py`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true"
             name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <Element namespace="http://sample.com"> sampleObject</Element>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>py://Script-1.py</ResourceURL>
         </MessageValidation>
         

Because the resource type used in `<ResourceURL>` is not `xsd` or `wsdl`, the deployment will fail with the error shown above.




### Resolution

Ensure that the resource type specified in the `<ResourceURL>`element of the SOAPMessageValidation policy is set to either `xsd` or `wsdl`, and that the resource file uses correct formatting.

To correct the example SOAPMessageValidation policy shown above, you could modify the resource type to either `xsd` or `wsdl`:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MessageValidation async="false" continueOnError="false" enabled="true"
    name="SOAP-Message-Validation-1">
        <DisplayName>SOAP Message Validation-1</DisplayName>
        <Properties/>
        <Element namespace="http://sample.com"> sampleObject</Element>
        <SOAPMessage/>
        <Source>request</Source>
    <ResourceURL>wsdl://SOAP-Message-Validation-1.wsdl</ResourceURL>
    </MessageValidation>
    

## ResourceCompileFailed

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    MessageValidation soap_message_validation_policy: Failed to compile resource resource. Context Revision:revision_number;APIProxy:apiproxy_name;Organization:organization;Environment:environment.

### Example Error Message
    
    
    Error Deploying Revision 1 to test
    MessageValidation SOAP-Message-Validation-1: Failed to compile resource SOAP-Message-Validation-1.wsdl. Context Revision:1;APIProxy:soapmessagevalidation;Organization:gsc-hipaa;Environment:test.
    

### Example Error Screenshot

![Failed to compile resource error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/resource-compile-failed.png)

### Cause

This error occurs if the resource script referenced in the `<ResourceURL>` element of the SOAPMessageValidation policy contains an error that prevents it from compiling during deployment.

### Diagnosis

  1. Identify the SOAPMessageValidation policy name and the resource script used in the policy. You can find both of these items in the error message. For example, in the following error the SOAPMessageValidation policy name is `SOAP-Message-Validation-1` and the resource script is `SOAP-Message-Validation-1.wsdl`.
         
         Error Deploying Revision 1 to test
         MessageValidation SOAP-Message-Validation-1: Failed to compile resource
         SOAP-Message-Validation-1.wsdl. Context
         Revision:1;APIProxy:soapmessagevalidation;Organization:gsc-hipaa;
         Environment:test.
         

  2. Examine the failed SOAPMessageValidation policy XML and verify that the resource script specified for the `<ResourceURL>` element matches what's in the error message.

For example, the following policy specifies the `<ResourceURL>` element as `SOAP-Message-Validation-1.wsdl`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true"
         name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <Element namespace="http://sample.com"> sampleObject</Element>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>wsdl://SOAP-Message-Validation-1.wsdl</ResourceURL>
         </MessageValidation>
         

  3. View the resource script file identified in Step 1 and see if there are any potential issues that can result in compilation errors.

Here's an example resource script file:
         
         <?xml version="1.0" encoding="ISO-8859-1"?>
         <wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsd/">
             <wsdl:types>
                 <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                     <xs:element name="request" type="xs:string"/>
                 </xs:schema>
             </wsdl:types>
         </wsdl:definitions>
         

Because `xmlns:wsdl`points to an invalid URL, the deployment will fail with the error shown above.




### Resolution

Ensure that the resource script specified in the `<ResourceURL>` element of the SOAPMessageValidation policy does not have any issues preventing it from compiling.

To correct the `SOAP-Message-Validation-1.wsdl` script shown above, you can modify `xmlns:wsdl` to point to a valid URL:
    
    
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
        <wsdl:types>
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="request" type="xs:string"/>
            </xs:schema>
        </wsdl:types>
    </wsdl:definitions>
    

## RootElementNameUnspecified

### Error Message

Saving the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    MessageValidation soap_message_validation_policy:
    RootElement name is not specified.

### Example Error Message
    
    
    Error Saving Revision 2
    MessageValidation SOAP-Message-Validation-1: RootElement name is not specified.
    

### Example Error Screenshot

![RootElement name not specified error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/root-element-name-unspecified.png)

### Cause

This error occurs if the `<Element>` element in the SOAPMessageValidation policy does not contain the root element's name.

### Diagnosis

  1. Identify the SOAPMessageValidation policy name where the error occurred. For example, in the following error, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1`:
         
         Error Saving Revision 2
         MessageValidation SOAP-Message-Validation-1: RootElement name is not specified.
         

  2. Examine the failed SOAPMessageValidation policy XML. If the root element name used for validation is not specified in the `<Element>` element, then that's the cause of the error.

For example, the following policy does not specify the root element name:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true"
         name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <Element namespace="http://schemas.xmlsoap.org/soap/prices"/>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>xsd://Script-1.xsd</ResourceURL>
         </MessageValidation>
         

Because the root element name is not specified, the deployment will fail with the error shown above.




### Resolution

Ensure that the `<Element>` element of the SOAPMessageValidation policy contains the correct root element.

To correct the SOAPMessageValidation policy shown above, you can modify the `<Element>` and add a valid root element as below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MessageValidation async="false" continueOnError="false" enabled="true"
    name="SOAP-Message-Validation-1">
        <DisplayName>SOAP Message Validation-1</DisplayName>
        <Properties/>
        <Element namespace="http://schemas.xmlsoap.org/soap/prices">GetPriceResponse</Element>
        <SOAPMessage/>
        <Source>request</Source>
        <ResourceURL>xsd://Script-1.xsd</ResourceURL>
    </MessageValidation>
    

## InvalidRootElementName

### Error Message

Saving the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    MessageValidation soap_message_validation_policy: RootElement name root_element_name is invalid.

### Example Error Message
    
    
    Error Saving Revision 2
    MessageValidation SOAP-Message-Validation-1: RootElement name 1GetPriceResponse
    is invalid.
    

### Example Error Screenshot

![RootElement name 1GetPriceResponse is invalid error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/invalid-root-element-name.png)

### Cause

This error occurs if the `<Element>` element in the SOAPMessageValidation policy contains a root element name that does not adhere to XML rules for valid element naming.

### Diagnosis

  1. Identify the SOAPMessageValidation policy name where the error occurred. For example, in the following error, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1`:
         
         Error Saving Revision 2
         MessageValidation SOAP-Message-Validation-1: RootElement name 1GetPriceResponse
         is invalid.
         

  2. Examine the failed SOAPMessageValidation policy XML. If the root element name specified in the `<Element>` element does not match the criteria for a valid XML element name, then that's the cause of the error.

For example, the following policy has a root element name that starts with a number, which is invalid. An element name containing spaces would also be invalid.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true"
         name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
              <Element namespace="http://schemas.xmlsoap.org/soap/prices">1GetPriceResponse</Element>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>xsd://Script-1.xsd</ResourceURL>
         </MessageValidation>
         




### Resolution

Ensure that the `<Element>` element of the SOAPMessageValidation policy contains a valid root element name.

To correct the SOAPMessageValidation policy shown above, you can modify the `<Element>` element to contain a valid root element name, as shown below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
        <DisplayName>SOAP Message Validation-1</DisplayName>
        <Properties/>
        <Element namespace="http://schemas.xmlsoap.org/soap/prices">GetPriceResponse</Element>
        <SOAPMessage/>
        <Source>request</Source>
        <ResourceURL>xsd://Script-1.xsd</ResourceURL>
    </MessageValidation>
    

## NoElements

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number
    Resource "resource_url" has no element definitions.

### Example Error Message
    
    
    Error Deploying Revision 2 to test
    Resource "xsd://Script-1.xsd" has no element definitions.
    

### Example Error Screenshot

![Resource has no element definitions error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/no-elements.png)

### Cause

This error occurs if the resource file specified in the `<Resource>` element of the SOAPMessageValidation policy does not contain any elements that can be used for validation.

### Diagnosis

  1. Identify the resource file missing element definitions from the error message. For example, in the following error, the resource file used in the is `xsd://Script-1.xsd`:
         
         Error Deploying Revision 2 to test
         Resource "xsd://Script-1.xsd" has no element definitions.
         

  2. Examine the resource file identified in Step 1. If there are no elements defined, then that's the cause of the error.

For example, the following resource file `Script-1.xsd` doesn't contain any elements:
         
         <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
         </xsd:schema>
         

Because the resource file does not have any elements, the deployment will fail with the error shown above.




### Resolution

Ensure that the resource file used in the SOAPMessageValidation policy contains the relevant element definitions.

To correct the example resource file shown above, you can modify the `xsd` file to add the following content:
    
    
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="shipOrder" type="order"/>
    <xsd:complexType name="order">
    <xsd:sequence>
    <xsd:element name="shipTo" type="shipAddress"/>
    <xsd:element name="items" type="cdItems"/>
    </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="shipAddress">
    <xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
    <xsd:element name="street" type="xsd:string"/>
    <xsd:element name="address" type="xsd:string"/>
    <xsd:element name="country" type="xsd:string"/>
    </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="cdItems">
    <xsd:sequence>
    <xsd:element name="item" type="cdItem" maxOccurs="unbounded"/>
    </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="cdItem">
    <xsd:sequence>
    <xsd:element name="title" type="xsd:string"/>
    <xsd:element name="quantity" type="xsd:integer"/>
    <xsd:element name="price" type="xsd:decimal"/>
    </xsd:sequence>
    </xsd:complexType>
    </xsd:schema>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
