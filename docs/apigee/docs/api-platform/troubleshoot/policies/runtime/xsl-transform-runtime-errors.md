---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xsl-transform-runtime-errors/
title: XSLTransform policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:32.594334+00:00
---

# XSLTransform policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xsl-transform-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  XSLTransform policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/xsl-transform-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xsl-transform-runtime-errors/).

## XSLSourceMessageNotAvailable

### Error code
    
    
    steps.xsl.XSLSourceMessageNotAvailable
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "response message is not available for XSL: policy_name",
            "detail": {
                "errorcode": "steps.xsl.XSLSourceMessageNotAvailable"
            }
        }
    }

### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "response message is not available for XSL: xslt",
            "detail": {
                "errorcode": "steps.xsl.XSLSourceMessageNotAvailable"
            }
        }
    }
    

### Cause

This error occurs if the [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) or string variable specified in the `<Source>` element of the [XSLTransform policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xsl-transform-policy) is either:

  * Out of scope (not available in the specific flow where the policy is being executed)
  * Can't be resolved (is not defined)



For example, this error occurs if the XSLTransform policy is supposed to be executed in the request flow, but the `<Source>` element is set to the response variable, which doesn't exist in the request flow.

### Diagnosis

  1. Identify the XSLTransform policy where the error occurred and the name of the variable that is not available. You can find both of these items in the `faultstring` element of the error response. For example, in the following `faultstring`, the policy name is `xslt` and the variable is `response`:
         
         faultstring": "response message is not available for XSL: xslt
         

  2. In the failed XSLTransform policy XML, verify that the name of the variable set in the `<Source>` element matches the variable name identified in the fault string (step #1 above). For example, the following XSLTransform policy specifies a variable named `response` in the `<Source>` element, which matches what's in the fault string:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <XSL async="false" continueOnError="false" enabled="true" name="xslt">
           <DisplayName>xslt</DisplayName>
               <Properties/>
               <ResourceURL>xsl://XSL-Transform.xsl</ResourceURL>
               <Source>response</Source>
               <Parameters ignoreUnresolvedVariables="false"/>
              <OutputVariable/>
         </XSL>
         

  3. Determine if the variable used in the `<Source>` element is defined and available in the flow in which the XSLTransform policy is being executed.

  4. If the variable is either:

     * Out of scope (not available in the specific flow where the policy is being executed) or
     * Can't be resolved (is not defined)

then that's the cause of the error.

As an example, let's say the XSLTransform policy shown above is supposed to execute in the request flow. Recall that the `response` variable is used in the `<Source>` element of the example policy. The `response` variable is available only in the response flow.

Since the `response` variable does not exist in the request flow, you receive the error code:
    
    steps.xsl.XSLSourceMessageNotAvailable
    




### Resolution

Ensure that the variable set in the `<Source>` element of the failed XSLTransform policy, is defined and exists in the flow where the policy executes.

To correct the example XSLTransform policy shown above, you could modify the `<Source>` element to use the `request` variable, because it exists in the request flow:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
      <XSL async="false" continueOnError="false" enabled="true" name="xslt">
      <DisplayName>xslt</DisplayName>
        <Properties/>
        <ResourceURL>xsl://XSL-Transform.xsl</ResourceURL>
        <Source>request</Source>
        <Parameters ignoreUnresolvedVariables="false"/>
       <OutputVariable/>
    </XSL>
    

## XSLEvaluationFailed

### Error code
    
    
    steps.xsl.XSLEvaluationFailed
    

### Error response body
    
    
    {
      "fault": {
          "faultstring": "Evaluation of XSL <var>XSL_file_name</var> failed with reason: \"<var>reason_for_failure</var>",
          "detail": {
              "errorcode": "steps.xsl.XSLEvaluationFailed"
          }
      }
    }
    

### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Premature end of document while parsing at line 1(possibly  around char 0)\"",
            "detail": {
                "errorcode": "steps.xsl.XSLEvaluationFailed"
            }
        }
    }
    

### Possible causes

This error occurs if:

  * The input XML payload is unavailable/malformed.
  * The XSLTransform policy fails/is unable to transform the input XML file based on the transformation rules provided in the XSL file. There could be many different causes for the XSLTransform policy to fail. The reason for failure in the error message will provide more information on the cause. The following table lists one such cause for this failure - Invalid Prefix - and is explained with an example.

Cause  | Description   
---|---  
Input XML Payload unavailable | The input XML payload is not passed or empty.   
Malformed Input XML | The input XML payload is malformed or invalid.   
Invalid prefix | The input XML payload has a prefix which is not defined in the XSL file.   
  
### Cause: Input XML payload is unavailable

This error occurs if the input XML payload is not passed or the XML payload passed as part of the API request to the API Proxy having XSLTransform policy is empty.

### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Premature end of document while parsing at line 1(possibly  around char 0)\"",
            "detail": {
                "errorcode": "steps.xsl.XSLEvaluationFailed"
            }
        }
    }
    

### Diagnosis

  1. Identify the XSL file which could not be evaluated by the XML Transform policy and the reason for failure. If the input XML payload is not passed or is empty, the reason for failure would indicate that there's a Premature end of document while parsing. You can find all this information in the `faultstring` element of the error response. For example, in the following `faultstring`, the XSL file is `XSL-Transform.xsl`, and the reason for failure is `Premature end of document while parsing at line 1 (possibly around char 0)`. That error means that the XML payload is either not passed or is empty.
         
         "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Premature end of document while parsing at line 1(possibly  around char 0)\""
         

  2. Determine if the input XML payload that has been passed as part of the request of is empty. If the input payload is not passed or is empty, then that's the cause for the error.

In the example request below, the request payload (that is, the request body) that was sent by the user was empty.

For example:
         
         curl -v "http://your_host_alias/v1/xsltransform" -H "Content-Type: application/xml"
         

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Because the XML input payload is empty, you receive the error:
         
         "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Premature end of document while parsing at line 1(possibly  around char 0)\""
         

**Note:** The HTTP Content-type header of the source message must be set to `application/xml`, otherwise the policy always returns a success.



### Resolution

Ensure that the input passed to XSLTransform policy is a valid XML payload and non-empty.

To fix the issue with the sample XSLTransform policy, pass a valid XML payload. For example:

  1. Create a file named `city.xml` with the following contents:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <root>
            <City>Bengaluru</City>
            <Name>Apigee</Name>
            <Pincode>560016</Pincode>
         </root>
         

  2. Make the API call using a curl command as follows:
         
         curl -v "http://your_host_alias/v1/xsltransform" -H "Content-Type: application/xml" -X POST -d @city.xml
         

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).




### Cause: Malformed Input XML

The input XML payload passed as part of the API request to the XSLTransform policy is malformed or invalid.

### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unexpected char while looking for open tag ('&lt;') character\"",
            "detail": {
                "errorcode": "steps.xsl.XSLEvaluationFailed"
            }
        }
    }
    

### Diagnosis

  1. Identify the XSL file which could not be evaluated by the XML Transform policy and the reason for failure. If the input XML payload is malformed, the reason for failure would indicate that there's an unexpected char. You can find all this information in the `faultstring` element of the error response. For example, in the following `faultstring`, the XSL file is `XSL-Transform.xsl`, and the reason for failure is `Unexpected char while looking for open tag ('&lt;') character`. That is, the "`<`" is missing in the XML payload.
         
         "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unexpected char while looking for open tag ('&lt;') character\""
         

  2. Examine the input XML payload passed to the XSLTransform policy and see if it has valid XML content or not. If the input payload is not valid XML, then that's the cause for the error.

In the example request below, the input payload (that is, the request body) that was sent by the user was invalid.

For example:
         
         curl -v "http://your_host_alias/v1/xsltransform" -H "Content-Type: application/xml" -X POST -d @city.xml
         

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

In this example, `city.xml` is defined as:
         
         {
            "City": "Bengaluru",
            "Name": "Apigee",
            "Pincode": "560016"
         }
         

Because the input payload is JSON and not valid XML, you receive the error:
         
         "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unexpected char while looking for open tag ('&lt;') character\""
         

**Note:** The HTTP`Content-type` header of the source message must be set to `application/xml`, otherwise the policy always returns success.



### Resolution

Ensure that the input passed to the XSLTransform policy is a valid XML payload and non-empty.

To fix the issue with the sample XSLTransform policy, pass a valid XML payload. For example:

  1. Modify the file `city.xml` to have the content in XML as shown below:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <root>
            <City>Bengaluru</City>
            <Name>Apigee</Name>
            <Pincode>560016</Pincode>
         </root>
         

  2. Make the API call using the curl command as follows:
         
         curl -v "http://your_host_alias/v1/xsltransform" -H "Content-Type: application/xml" -X POST -d @city.xml
         

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).




### Cause: Invalid prefix

The input XML payload passed to the XSLTransform policy has an element that is not defined as a prefix in the XSL file specified in the policy.

### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unresolved Prefix at line 1(possibly  around char 270)\"",
            "detail": {
                "errorcode": "steps.xsl.XSLEvaluationFailed"
            }
        }
    }
    

### Diagnosis

  1. Identify the XSL file that could not be evaluated by the XML Transform policy and the reason for failure. In this case, the reason for failure would indicate that there is an unresolved prefix at a specific line number in the input XML payload. You can find all this information in the `faultstring` element of the error response. For example, in the following `faultstring`, the XSL file is `XSL-Transform.xsl`, and the reason for failure is `Unresolved Prefix` and line number is `1`.
         
         "faultstring":"Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unresolved Prefix at line 1(possibly  around char 270)\""
         

  2. Examine the content of the XSL file (identified in step #1 above) and the input XML payload. If the prefix used in the line number (identified in step #1 above) of input XML payload does not exist in the XSL file, then that's the cause of the error.

Here are the sample XSL and the corresponding XML payload that lead to the error:
         
         XSL-Transform.xsl
         
         <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
           <xsl:output method="text"/>
           <xsl:variable name="newline">
            <xsl:text>
            </xsl:text>
           </xsl:variable>
           <xsl:template match="/">
           <xsl:text>&lt;Life&gt;</xsl:text>
             <xsl:value-of select="$newline"/>
             <xsl:text>Here are the odd-numbered items from the list:</xsl:text>
             <xsl:value-of select="$newline"/>
             <xsl:for-each select="list/listitem">
               <xsl:if test="(position() mod 2) = 1">
                 <xsl:number format="1. "/>
                 <xsl:value-of select="."/>
                 <xsl:value-of select="$newline"/>
               </xsl:if>
             </xsl:for-each>
           <xsl:text>&lt;/Life&gt;</xsl:text>
         </xsl:template>
         </xsl:stylesheet>
         

Input XML Payload
         
         <?xml version="1.0"?>
         <Life:Books>
           <title>A few of my favorite albums</title>
           <listitem>Beat Crazy</listitem>
           <listitem>Here Come the Warm Jets</listitem>
           <listitem>Kind of Blue</listitem>
           <listitem>London Calling</listitem>
         </Life:Books>
         

The example XML payload shown above contains an element `<Life:Books>`. Notice that the XSL does not have this prefix. Instead it has the prefix as `<xsl:text>&lt;Life&gt;</xsl:text>`. Hence you get the error:
         
         "faultstring":"Evaluation of XSL XSL-Transform.xsl failed with reason: \"Unresolved Prefix at line 1(possibly  around char 270)\""
         




### Resolution

Ensure that the input XML payload passed to the XSLTransform policy has all the element formats defined as prefixes in the XSL file used in the policy.

To fix the example XML file shown above, you can modify the file as shown below:

Updated Input XML Payload
    
    
    <?xml version="1.0"?>
    <Life>
      <title>A few of my favorite albums</title>
      <listitem>Beat Crazy</listitem>
      <listitem>Here Come the Warm Jets</listitem>
      <listitem>Kind of Blue</listitem>
      <listitem>London Calling</listitem>
    </Life>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
