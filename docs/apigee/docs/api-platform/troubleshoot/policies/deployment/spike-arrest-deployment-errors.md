---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/spike-arrest-deployment-errors/
title: Spike Arrest policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:42.906883+00:00
---

# Spike Arrest policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/spike-arrest-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Spike Arrest policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/spike-arrest-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/spike-arrest-deployment-errors/).

## InvalidAllowedRate

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [revision_number]
    Invalid spike arrest rate [invalid_rate].

**Example error messages**
    
    
    Error Saving Revision 1
    Invalid spike arrest rate 30s.
    
    Error Saving Revision 1
    Invalid spike arrest rate 30.1ps.
    

**Example screenshots**

![Invalid spike arrest rate 30s error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/spike-arrest-deploy-error-1.png)

![Invalid spike arrest rate 30.1ps error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/spike-arrest-deploy-error-2.png)

### Cause

If the spike arrest rate specified in the `<Rate>` element of the Spike Arrest Policy is not an integer or if the rate does not have `ps` or `pm` as a suffix, then the deployment of the API proxy fails.

The valid values are `[**_int_**]ps` and `[**_int_**]pm`.

For example, if the spike arrest rate specified is `30.1ps` in the `<Rate>` element of a Spike Arrest Policy, then the deployment of the API proxy fails. This is because 30.1 is not an integer.

### Diagnosis

  1. Identify the invalid spike arrest rate specified in the Spike Arrest policy. You can find this information from the error message. For example, in the following error, the invalid spike arrest is `30.1`:
         
         Error Saving Revision 1
         Invalid spike arrest rate 30.1ps.
         

  2. Examine all the Spike Arrest policies in the specific API proxy where the failure has occurred. If there is any Spike Arrest policy in which the spike arrest specified in the `<Rate>` element matches the invalid spike arrest rate identified in Step #1 above, then that's the cause of the error.

For example, the following policy specifies the value of `<Rate>` as 30.1ps, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <SpikeArrest async="false" continueOnError="false" enabled="true" name="CheckRate">
             <DisplayName>CheckRate</DisplayName>
             <Properties/>
             <Identifier ref="request.header.some-header-name"/>
             <MessageWeight ref="request.header.weight"/>
             <Rate>30.1ps</Rate>
         </SpikeArrest>
         

Since the spike arrest rate specified in the `<Rate>` element is not an integer, the deployment of the API Proxy fails with the error:
         
         Invalid spike arrest rate 30.1ps.
         




### Resolution

Ensure that the value of the spike arrest rate specified in the `<Rate>` element of the Spike Arrest Policy is an integer and has `ps` or `pm` as a suffix. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <SpikeArrest async="false" continueOnError="false" enabled="true" name="CheckRate">
        <DisplayName>CheckRate</DisplayName>
        <Properties/>
        <Identifier ref="request.header.some-header-name"/>
        <MessageWeight ref="request.header.weight"/>
        <Rate>30ps</Rate>
    </SpikeArrest>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
