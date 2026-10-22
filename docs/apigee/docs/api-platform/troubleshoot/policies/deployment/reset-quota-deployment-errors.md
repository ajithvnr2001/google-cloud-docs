---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/reset-quota-deployment-errors/
title: Reset Quota policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:49.049342+00:00
---

# Reset Quota policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/reset-quota-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Reset Quota policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/reset-quota-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/reset-quota-deployment-errors/).

## InvalidCount

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid count value interval for identifier identifier_name in policy_name.

### Example error message
    
    
    Error Saving Revision 1
    Invalid count value 10.0 for identifier identifierName in Reset_Quota_Demo.
    

### Example screenshot

![Error saving revision 1.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/resetquota-deploy-error-1.png)

### Cause

If the count value specified in the `<Allow>` element of the Reset Quota Policy is not an integer, then the deployment of the API proxy fails.

For example, if the quota interval specified is `10.0` in the `<Allow>` element, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the Reset Quota policy where the error occurred and the invalid allow count. You can find this information from the error message. For example, in the following error, the policy name is `Reset_Quota_Demo` and the invalid allow count is `10.0`:
         
         Error Saving Revision 1
         Invalid count value 10.0 for identifier identifierName in Reset_Quota_Demo.
         

  2. Verify that the value of the allow count specified in the failed policy matches with the value identified in the error message (step 1 above). For example, the following policy specifies the value of the allow count as `10.0`, which matches with what's in the error message:
         
         <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset_Quota_Demo">
             <DisplayName>Reset_Quota_Demo</DisplayName>
             <Properties/>
             <Quota>
                 <Identifier name="identifierName" ref="request.header.identifier">
                     <Allow>10.0</Allow>
                 </Identifier>
             </Quota>
         </ResetQuota>
         

In the example Reset Quota Policy shown above, the value of the allow count is `10.0`, which is not an integer. Therefore, the deployment of the API Proxy fails with the error:
         
         Invalid count value 10.0 for identifier identifierName in Reset_Quota_Demo.
         




### Resolution

Ensure that the value of the allow count specified in the `<Allow>` element of the Reset Quota Policy is an integer. To correct the example ResetQuota policy shown above, you could modify the `<Allow>` element to have a value of **10**.
    
    
    <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset_Quota_Demo">
        <DisplayName>Reset_Quota_Demo</DisplayName>
        <Properties/>
        <Quota>
            <Identifier name="identifierName" ref="request.header.identifier">
                <Allow>10</Allow>
            </Identifier>
        </Quota>
    </ResetQuota>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
