---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xsl-transform-deployment-errors/
title: XSL Transform policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:07.283442+00:00
---

# XSL Transform policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xsl-transform-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  XSL Transform policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/xsl-transform-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xsl-transform-deployment-errors/).

## XSLEmptyResourceUrl

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Error occurred while validation of bean policy_name.xml. Reason:- Non null
    value expected for element ResourceURL in XSL

### Example error message

In the following example error message, the name of the XSL Transform policy causing the error is `xslt`:
    
    
    Error Saving Revision 1
    Error occurred while validation of bean xslt.xml. Reason: - Non null value
    expected for element ResourceURL in XSL
    

### Example screenshot

In the Apigee UI, you will see an error similar to the following:

![Non null value expected for element ResourceURL in XSL.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/xsl-transform-error-1.png)

### Cause

If the `<ResourceURL>` element in the XSL Transform policy is empty, then the deployment of the API proxy fails.

### Diagnosis

Examine the `<ResourceURL>` element in the XSL Transform policy named in the error message. If there is no Resource URL specified in the `<ResourceURL>` element, then that is the cause of the error. For example, the following XSL Transform policy has an empty `<ResourceURL>` element:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XSL async="false" continueOnError="false" enabled="true" name="xslt">
        <DisplayName>xslt</DisplayName>
        <Properties/>
        <ResourceURL></ResourceURL>
        <Parameters ignoreUnresolvedVariables="true"/>
        <OutputVariable/>
    </XSL>
    

Because the `<ResourceURL>` element is empty, the deployment of the API proxy fails.

### Resolution

Ensure that the `<ResourceURL>` element in the XSL Transform policy has a valid URL pointing to an XSLT file.

For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XSL async="false" continueOnError="false" enabled="true" name="xslt">
        <DisplayName>xslt</DisplayName>
        <Properties/>
        <ResourceURL>xsl://my_transform.xsl</ResourceURL>
        <Parameters ignoreUnresolvedVariables="true"/>
        <OutputVariable/>
    </XSL>
    

## XSLInvalidResourceType

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to env_name
    XSL policy_name: Resource type must be xsl. Context Revision:revision_number;
    APIProxy:api_proxy_name;Organization:org_name;Environment:env_name.

### Example error message

In the following example error message, the name of the XSL Transform policy causing the error is `xslt`:
    
    
    Error Deploying Revision 1 to test
    XSL xslt: Resource type must be xsl. Context Revision:1;APIProxy:XSLTransform;
    Organization:jdoe-test;Environment:test.
    

### Example screenshot

In the Apigee UI, you will see an error similar to the following:

![Resource type must be xsl.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/xsl-transform-error-2.png)

### Cause

If the resource type specified in the `<ResourceURL>` element of the XSL Transform policy is not of type `xsl`, then the deployment of the API proxy fails.

The correct format to specify this is as shown below:
    
    
    <ResourceURL>xsl://<file_name>.xsl</ResourceURL>
    

For example, if the resource type is specified as `jsc` in the `<ResourceURL>` element of the XSL Transform policy as shown below, then the deployment of the API proxy fails:
    
    
    <ResourceURL>jsc://my_transform.xsl</ResourceURL>
    

### Diagnosis

  1. Identify the name of the XSL Transform policy where the error has occurred. You can find this information from the error message. For example, in the following error, the policy name is `xslt`.
         
         XSL xslt: Resource type must be xsl. Context Revision:1;APIProxy:XSLTransform;
         Organization:jdoe-test;Environment:test.
         

  2. In the failed XSL Transform policy XML, verify if the type of the resource specified in the `<ResourceURL>` element is not of type `xsl`. If it is not of `xsl` type, then that's the cause of the error.

For example, the following policy specifies a non `xsl` type in the `<ResourceURL>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <XSL async="false" continueOnError="false" enabled="true" name="xslt">
             <DisplayName>xslt</DisplayName>
             <Properties/>
             <ResourceURL>jsc://my_transform.xsl</ResourceURL>
             <Parameters ignoreUnresolvedVariables="true"/>
             <OutputVariable/>
         </XSL>
         

Because the resource URL is specified as `jsc://my_transform.xsl`, which is notof `xsl` type, the deployment of the API Proxy fails with the error:
         
         XSL xslt: Resource type must be xsl. Context Revision:1;APIProxy:XSLTransform;
         Organization:jdoe-test;Environment:test.
         




### Resolution

Ensure that the resource type specified in the `<ResourceURL>` element of the XSL Transform policy is always of `xsl` type. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XSL async="false" continueOnError="false" enabled="true" name="xslt">
        <DisplayName>xslt</DisplayName>
        <Properties/>
        <ResourceURL>xsl://my_transform.xsl</ResourceURL>
        <Parameters ignoreUnresolvedVariables="true"/>
        <OutputVariable/>
    </XSL>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
