---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/soap-message-validation-runtime-errors/
title: SOAP Message Validation policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:27:31.842858+00:00
---

# SOAP Message Validation policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/soap-message-validation-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  SOAP Message Validation policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/soap-message-validation-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/soap-message-validation-runtime-errors/).

## SourceMessageNotAvailable

### Error Code
    
    
    steps.messagevalidation.SourceMessageNotAvailable
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "source_var_name message is not
         available for[policy_name]",
        "detail": {
          "Errorcode":
           "steps.messagevalidation.SourceMessageNotAvailable"
         }
      }
    }

### Example Error response body
    
    
    {
      "fault": {
        "faultstring": "request message is not available for MessageValidation: SOAP-Message-Validation-1",
        "detail": {
          "errorcode": "steps.messagevalidation.SourceMessageNotAvailable"
        }
      }
    }
    

### Cause

This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) variable specified in the `<Source>` element of the SOAPMessageValidation policy is either:

  * Out of scope (not available in the specific flow where the policy is being executed) or
  * can't be resolved (is not defined)



For example, this error occurs if the `<Source>` element in the SOAPMessageValidation policy is set to a variable that doesn't exist in the flow where the policy is executed.

### Diagnosis

  1. Identify the SOAPMessageValidation policy name where the error occurs and the name of the `source` variable from the fault string. For example, in the following fault string, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1`and the `source` variable is `request`:
         
         "faultstring": "request message is not available for MessageValidation: SOAP-Message-Validation-1"
         

  2. In the failed SOAPMessageValidation policy XML, verify that the name of the variable set in the `<Source>` element matches the variable name identified in the fault string (Step 1 above).

For example, the following SOAPMessageValidation policy specifies a variable named `request` in the `<Source>` element, which matches what's in the fault string:
         
         <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <Element namespace="http://schemas.xmlsoap.org/soap/prices">GetPriceResponse</Element>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>xsd://Script-1.xsd</ResourceURL>
         </MessageValidation>
         

  3. Determine if the variable used in the `<Source>` element is defined and available in the flow in which the SOAPMessageValidation policy is being executed.

If the variable is either:

     * out of scope (not available in the specific flow where the policy is being executed) or
     * can't be resolved (is not defined)

then that's the cause of the error.

As an example, let's say the SOAPMessageValidation policy shown above executes in the response flow. However, the `request` variable used in the `<Source>` element example above is only available in the _request_ flow.

Because the `request` variable does not exist in the response flow, you receive the following error:
    
    "faultstring": "request message is not available for MessageValidation: SOAP-Message-Validation-1"
    




### Resolution

Ensure that the variable set in the `<Source>` element of the failed SOAPMessageValidation policy is defined and exists in the flow where the policy executes.

To correct the example shown above, you could modify the `<Source`> element to use the `response` variable, which exists in the response flow:
    
    
    <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
        <DisplayName>SOAP Message Validation-1</DisplayName>
        <Properties/>
        <Element namespace="http://schemas.xmlsoap.org/soap/prices">GetPriceResponse</Element>
        <SOAPMessage/>
        <Source>response</Source>
        <ResourceURL>xsd://Script-1.xsd</ResourceURL>
    </MessageValidation>
    

## NonMessageVariable

### Error Code
    
    
    steps.messagevalidation.NonMessageVariable
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "Variable var_name does not resolve to a Message"
        "detail": {
          "errorcode": "steps.messagevalidation.NonMessageVariable"
        }
      }
    }

### Example Error response body
    
    
    {
      "fault": {
        "faultstring": "Variable message.content does not resolve to a Message",
        "detail": {
          "errorcode": "steps.messagevalidation.NonMessageVariable"
        }
      }
    }
    

### Cause

This error occurs if the `<Source>` element in the SOAPMessageValidation policy is set to a variable which is not of type [Message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message).

Message type variables represent entire HTTP requests and responses. The built-in Apigee flow variables `request`, `response`, and `message` are of type Message. To learn more about message variables, see the [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message).

### Diagnosis

  1. Identify the name of the variable that does not resolve to a Message type from the fault string. For example, in the following fault string the name of variable is `message.content`:
         
         "faultstring": "Variable message.content does not resolve to a Message"
         

  2. Examine all the SOAPMessageValidation policies in the specific API Proxy where the failure has occurred. There could be one or more SOAPMessageValidation policies. Identify the specific SOAPMessageValidation policy or policies in which the variable specified in the `<Source>` element matches the variable name identified in the fault string (Step 1 above).

For example, the following policy sets the `<Source>` element to a variable named `message.content`, which matches what's in the fault string:
         
         <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <Element namespace="http://schemas.xmlsoap.org/soap/prices">GetPriceResponse</Element>
             <SOAPMessage/>
             <Source>message.content</Source>
             <ResourceURL>xsd://Script-1.xsd</ResourceURL>
         </MessageValidation>
         

Because the variable `message.content` is not of type Message, you get the error:
         
         "faultstring": "Variable message.content does not resolve to a Message"
         




### Resolution

Ensure that the `<Source>` element in the failed SOAPMessageValidation policy is set to a [Message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) type variable that exists in the flow where the policy executes.

To correct the policy, you can modify the `<Source>` element to specify a variable that is of type Message. For example, in the failed SOAPMessageValidation policy, you could specify the `<Source>` element as `request`:
    
    
    <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
        <DisplayName>SOAP Message Validation-1</DisplayName>
        <Properties/>
        <Element namespace="http://sample.com"> sampleObject</Element>
        <SOAPMessage/>
        <Source>request</Source>
        <ResourceURL>xsd://Script-1.xsd</ResourceURL>
    </MessageValidation>
    

## Failed

### Error Code
    
    
    steps.messagevalidation.Failed
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "Variable var_name failed with reason: \"reason [Line varline_num
        "detail": {
          "errorcode": "steps.messagevalidation.Failed"
        }
      }
    }

### Example Error response body
    
    
    {
      "fault": {
        "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expecting a child element but found none [Line 9]\"",
        "detail": {
          "errorcode": "steps.messagevalidation.Failed"
        }
      }
    }
    

### Cause

This error occurs if the SOAPMessageValidation policy fails to validate the input message payload against the XSD schema or WSDL definition. It will also occur if there is malformed JSON or XML in the payload message.

Here are some of the possible causes that can lead to this error:

Cause  | Description   
---|---  
Mismatching XML payload | The input XML payload does not adhere to the XSD schema specified in the SoapMessageValidation policy.   
Mismatching SOAP payload | The input SOAP payload does not adhere to the WSDL definition specified in the SoapMessageValidation policy.   
Malformed JSON or XML | The input SOAP payload does not contain well-formed XML or JSON.   
  
### Cause: Mismatching XML payload

This error occurs if the input XML payload does not adhere to the XSD schema specified in the `<ResourceURL>` element of the SoapMessageValidation policy.

#### Example Error Message
    
    
    {
      "fault": {
        "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expecting a child element but found none [Line 9]\"",
        "detail": {
          "errorcode": "steps.messagevalidation.Failed"
        }
      }
    }
    

#### Diagnosis

  1. Identify the SOAPMessageValidation policy name, the reason for the failure and the line number at which the XML payload does not match the XSD schema. All of this information is in the fault string. For example, in the following fault string, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1,`the reason for the failure is `Expecting a child element but found none [Line 9]`: and the line number is `9`.
         
         "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expecting a child element but found none [Line 9]\""
         

  2. Examine the SOAPMessageValidation policy and confirm that it uses an XSD schema definition file to validate messages. For example, the following SOAPMessageValidation policy has an XSD resource file in the`<ResourceURL>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <SOAPMessage/>
             <Source>request</Source>
             <ResourceURL>xsd://Script-1.xsd</ResourceURL>
         </MessageValidation>
         

  3. Examine the input payload on the line number identified in Step 1 above to understand what caused the failure.

**Sample Input XML payload**
         
         <?xml version="1.0"?>
         <soap:Envelope
         xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
         <soap:Body>
             <shipOrder
             xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance">
             <shipTo>
                 <name>Karl Kalckstein</name>
             </shipTo>
             <items>
                 <item>
                     <title>I love APIs</title>
                     <quantity>1</quantity>
                     <price>2.90</price>
                 </item>
             </items>
         </shipOrder>
         </soap:Body>
         </soap:Envelope>
         

In the example shown above, line 9 has the `</shipTo>` end tag.

  4. Examine the XML schema definition file, `Script-1.xsd`, used in the SOAPMessageValidation policy to see how the `<shipTo>` element should look:
         
         ...
         <xsd:element name="shipTo" type="shipAddress"/>
         ...
         <xsd:complexType name="shipAddress">
         <xsd:sequence>
         <xsd:element name="name" type="xsd:string"/>
         <xsd:element name="street" type="xsd:string"/>
         <xsd:element name="address" type="xsd:string"/>
         <xsd:element name="country" type="xsd:string"/>
         </xsd:sequence>
         </xsd:complexType>
         ...
         

According to the sample XSD used for validation, the `<shipTo>` element must have the child elements `<name>`, `<street>`, `<address>` and `<country>`. However, the input XML payload has only one child element, `<name>`. As a result, you get the error:
         
         "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expecting a child element but found none [Line 9]\""
         




#### Resolution

There are two ways to resolve this validation error:

**Solution #1**

If you determine that the XSD schema definition imposes unnecessary limitations and only the `<name>` child element is required under the `<shipTo>` element, you can modify the `Script-1.xsd` used in SOAPMessageValidation policy. To validate the payload example above, you can modify the XSD file as follows:
    
    
    ...
    <xsd:element name="shipTo" type="shipAddress"/>
    ...
    <xsd:complexType name="shipAddress">
    <xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
    </xsd:complexType>
    

**Solution #2**

If the XSD definition file is correct, then the input XML payload can be changed to match the `xsd`. For example, you could modify the payload to comply with the `xsd` as follows:
    
    
    <?xml version="1.0">
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
    <soap:Body>
        <shipOrder xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance">
        <shipTo>
            <name>Karl Kalckstein</name>
            <street>1020 Parkway</street>
            <address>Mountain View, CA 94043</address>
            <country>USA</country>
        </shipTo>
        <items>
            <item>
                <title>I love APIs</title>
                <quantity>1</quantity>
                <price>2.90</price>
            </item>
        </items>
    </shipOrder>
    </soap:Body>
    </soap:Envelope>
    

### Cause: Mismatching SOAP payload

This error occurs if the input SOAP payload does not adhere to the WSDL definition specified in the `<ResourceURL>` element of the SoapMessageValidation policy.

**Note:** This error also occurs when you set the `maxOccurs` attribute on an element to a value greater than 65535 becasue the implementation uses an unsigned 16-bit integer to represent the `maxOccurs` attribute. 

#### Example Error Message
    
    
    {
      "fault": {
        "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Element name mismatch. Wildcard? [Line 11]\"",
        "detail": {
          "errorcode": "steps.messagevalidation.Failed"
        }
      }
    }
    

#### Diagnosis

  1. Identify the SOAPMessageValidation policy name, the reason for the failure and the line number at which the SOAP payload does not match the WSDL definition. You can find all this information from the fault string. For example, in the following fault string, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1`, the reason for the failure is `\"Element name mismatch. Wildcard? [Line 11]\""` and the line number is `11`:
         
         "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Element name mismatch. Wildcard? [Line 11]\""
         

  2. Examine the SOAPMessageValidation policy and confirm that it uses a `wsdl` schema to validate messages. For example, the following SOAPMessageValidation policy has an `wsdl` resource file in the`<ResourceURL>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageValidation async="false" continueOnError="false" enabled="true" name="SOAP-Message-Validation-1">
             <DisplayName>SOAP Message Validation-1</DisplayName>
             <Properties/>
             <SOAPMessage/>
             <Source>request</Source>
          <ResourceURL>wsdl://SOAP-Message-Validation-1.wsdl</ResourceURL>
         </MessageValidation>
         

  3. Examine the input payload on the line number identified in Step 1 to understand what caused the failure.

**Sample Input SOAP Payload**
         
         <?xml version="1.0"?>
         <soap:Envelope
         xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
         soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
         <soap:Body>
         <shipOrder
         xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance">
           <shipTo>
             <name>Karl Kalckstein</name>
             <street>1020 Parkway</street>
             <address>Mountain View, CA 94043</address>
             <country>USA</country>
           </shipTo>
           <items>
             <item>
               <title>I love APIs</title>
               <quantity>1</quantity>
               <price>2.90</price>
             </item>
           </items>
         

In the example shown above, line 11 has the child element `<country>` under the `<shipTo>` element.

  4. Examine the WSDL Definition file, `SOAP-Message-Validation-1.wsdl`, used in the SOAPMessageValidation policy to see what could be wrong with the child element `<country>` under the `<shipTo>` element:
         
         <?xml version="1.0" encoding="ISO-8859-1"?>
         <wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
             <wsdl:types>
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
         </xsd:sequence>
         ...
         

According to the WSDL definition used for validation, the `<shipTo>`element does not have a `<country>` child element. As a result, you get the error:
         
         "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Element name mismatch. Wildcard? [Line 11]\""
         




#### Resolution

There are two ways to resolve this validation error:

**Solution #1**

If you determine that the WSDL definition used is incorrect, you can change the `SOAP-Message-Validation-1.wsdl` used in SOAPMessageValidation policy. To validate the payload example above, you can modify the file as follows:
    
    
    ...
    <xsd:complexType name="shipAddress">`
    ...
    <sequence>
        <element name="name" type="xsd:string"/>
        <element name="street" type="xsd:string"/>
        <element name="address" type="xsd:string"/>
        <element name="country" type="xsd:string"/>
    </sequence>
    

**Solution #2**

If the WSDL definition is correct, then the input SOAP payload can be changed to match the WSDL definition.

For example, you can modify the input SOAP payload as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <soap:Envelope
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
    <soap:Body>
    <shipOrder xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance">
        <shipTo>
            <name>Karl Kalckstein</name>
            <street>1020 Parkway</street>
            <address>Mountain View, CA 94043</address>
        </shipTo>
        <items>
            <item>
                <title>I love APIs</title>
                <quantity>1</quantity>
                <price>2.90</price>
            </item>
        </items>
    

### Cause: Malformed JSON or XML

This error occurs if the input SOAP payload does not adhere to the WSDL definition specified in the `<ResourceURL>` element of the SoapMessageValidation policy.

#### Example Error Message
    
    
    {
      "fault": {
        "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expected <\/title> at line 15(possibly  around char 420)\"",
        "detail": {
          "errorcode": "steps.messagevalidation.Failed"
        }
      }
    }
    

#### Diagnosis

  1. Identify the SOAPMessageValidation policy name, the reason for the failure and the line number of the XML payload that does not match the WSDL definition. You can find all this information in the fault string. For example, in the following fault string, the SOAPMessageValidation policy name is `SOAP-Message-Validation-1`, the reason for the failure is `Expected </title> at line 15(possibly around char 420):` and the line number is`15.`
         
         "faultstring": "SOAP-Message-Validation-1 failed with reason: \"Expected </title> at line 15(possibly  around char 420)\""
         

  2. Examine the input payload on the line number identified in Step 1 above to understand what caused the failure.

**Sample Input SOAP Payload**
         
         <?xml version="1.0"?>
         <soap:Envelope
         xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
         soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
         <soap:Body>
         <shipOrder xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance">
           <shipTo>
             <name>Karl Kalckstein</name>
             <street>1020 Parkway</street>
             <address>Mountain View, CA 94043</address>
             <country>USA</country>
           </shipTo>
           <items>
             <item>
               <title>I love APIs</titles>
               <quantity>1</quantity>
               <price>2.90</price>
             </item>
           </items>
         </shipOrder>
         </soap:Body>
         </soap:Envelope>
         

In the example shown above, line 15 of the input XML has the element `<title>` but is not closed with a `</title>` end tag.




#### Resolution

To resolve the error, ensure that the input payload is valid and formed correctly.

For example, you could modify the input XML payload as follows:
    
    
    ...
    </shipTo>
    <items>
      <item>
        <title>I love APIs</title>
        <quantity>1</quantity>
        <price>2.90</price>
      </item>
    </items>
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
