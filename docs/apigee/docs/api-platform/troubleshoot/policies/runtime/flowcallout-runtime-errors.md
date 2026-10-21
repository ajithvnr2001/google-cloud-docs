---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/flowcallout-runtime-errors/
title: FlowCallout policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:30.520947+00:00
---

# FlowCallout policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/flowcallout-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  FlowCallout policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/flowcallout-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/flowcallout-runtime-errors/).

## SharedFlowNotFound

### Error code
    
    
    flow.SharedFlowNotFound
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Shared Flow shared_flow_name Not Found",
            "detail": {
                "errorcode": "flow.SharedFlowNotFound"
            }
        }
    }
    

### Possible Causes

The possible causes for this error are:

**Cause** | **Description**  
---|---  
Shared flow not available | The shared flow does not exist.   
Shared flow not deployed | The shared flow exists but is not deployed.   
  
### Cause: Shared flow not available

In the Flow Callout policy, if the shared flow defined within the `<SharedFlowBundle>` element does not exist in the environment, then this error occurs.

For example, If the `<SharedFlowBundle>` element in the Flow Callout policy contains a shared flow called `SharedFlow_Sample` and if this shared flow does not exist in the environment, then the error occurs.

#### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Shared Flow SharedFlow_Sample Not Found",
            "detail": {
                "errorcode": "flow.SharedFlowNotFound"
            }
        }
    }
    

#### Diagnosis

  1. Identify the shared flow which does not exist. You can find this in the `faultstring` element of the error response. For example, in the following `faultstring`, the shared flow name is `SharedFlow_Sample`:

`"faultstring": "Shared Flow SharedFlow_Sample Not Found"`

  2. Examine all the Flow Callout policies in the specific API Proxy where the failure has occurred. Check if there is any Flow Callout policy in which `<SharedFlowBundle>` element is specified with the flow name identified in step #1 above.

For example, the following policy specifies the `<SharedFlowBundle>` as `SharedFlow_Sample`, which matches with what's in the fault string.
         
         <FlowCallout async="false" continueOnError="false" enabled="true" name="Auth-Flow-Callout">
            <DisplayName>Auth Flow Callout</DisplayName>
            <SharedFlowBundle>SharedFlow_Sample</SharedFlowBundle>
         </FlowCallout>
         

  3. In the UI, check if this shared flow exists under **Develop > Shared Flows**. If it does not exist, then that's the cause of the error. (Note that in the New UI, you can find Shared Flows under the Develop tab.)

For example, in the screenshot shown below, the shared flow `SharedFlow_Sample` does not exist.

![The shared flow SharedFlow_Sample is not listed in the Shared Flow column.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/flowcallout-runtime-error-3.png)

Because this shared flow does not exist, you receive the error code:
         
         flow.SharedFlowNotFound
         




#### Resolution

Ensure that the shared flow specified in the `<SharedFlowBundle>` element in the Flow Callout policy, exists and deployed in the specific environment in which the API request is executed.

You could choose one of the following ways to address the issue:

  1. Create a shared flow called `SharedFlow_Sample` and deploy it the test environment as shown below:

![The shared flow SharedFlow_Sample is listed in the Shared Flow column.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/flowcallout-runtime-error-2.png)

  2. Use an already existing Shared Flow that is deployed in the test environment in the Flow Callout policy. For example, you could specify **SharedFlow_demo** in the Flow Callout policy.
         
         <FlowCallout async="false" continueOnError="false" enabled="true" name="Auth-Flow-Callout">
           <DisplayName>Auth Flow Callout</DisplayName>
           <SharedFlowBundle>SharedFlow_demo</SharedFlowBundle>
         </FlowCallout>
         

If you make an API call to the test environment, you will no longer see the error, because the Flow Callout is deployed to the test environment as well.




### Cause: Shared flow not deployed

If the shared flow specified in the `<SharedFlowBundle>` element of the Flow Callout policy, is not deployed, then this error occurs.

For example, If the `<SharedFlowBundle>` element in the Flow Callout policy contains a shared flow called `Shared-Flow_example` which is not deployed in the specific environment in which the API request is made, then the error occurs.

#### Example Error Message
    
    
    {
        "fault": {
            "faultstring": "Shared Flow Shared-Flow_example Not Found",
            "detail": {
                "errorcode": "flow.SharedFlowNotFound"
            }
        }
    }
    

#### Diagnosis

  1. Identify the shared flow which is not deployed. You can find this in the `faultstring` element of the error response. For example, in the following `faultstring`, the shared flow name is `Shared-Flow_example`:

`"faultstring": "Shared Flow Shared-Flow_example Not Found"`

  2. In the UI, check if this shared flow is deployed.

For example, you will notice in the below screenshot that the shared flow `Shared-Flow_example` exists but is not deployed.

![The shared flow Shared-Flow_example exists and has no deployments.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/flowcallout-runtime-error-1.png)

Since this shared flow is not deployed, you receive the error code:
         
         flow.SharedFlowNotFound
         




#### Resolution

Ensure that the shared flow specified in the `<SharedFlowBundle>` element in the Flow Callout policy, exists and deployed in the specific environment in which the API request is executed.

To correct the above example, deploy the shared flow called `Shared-Flow_example` in the test environment. The following screenshot shows that the shared flow `SharedFlow_Sample` is deployed:

![The shared flow SharedFlow_Sample is deployed in the test environment.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/flowcallout-runtime-error-4.png)

If you make an API call to the test environment, you will no longer see the error, because the Flow Callout is deployed to the test environment as well.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
