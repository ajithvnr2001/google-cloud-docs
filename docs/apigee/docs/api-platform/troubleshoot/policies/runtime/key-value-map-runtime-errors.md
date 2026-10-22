---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/key-value-map-runtime-errors/
title: Key Value Map Operations runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:06.247160+00:00
---

# Key Value Map Operations runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/key-value-map-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Key Value Map Operations runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/key-value-map-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/key-value-map-runtime-errors/).

## UnsupportedOperationException

### Error code
    
    
    java.lang.UnsupportedOperationException
    

### Error response body
    
    
    {
       "fault":{
          "faultstring":"java.lang.UnsupportedOperationException",
          "detail":{
             "errorcode":"Internal Server Error"
          }
       }
    }
    

### Cause

This error occurs if the `mapIdentifier` attribute is set to an empty string in the Key Value Map Operations policy.

### Diagnosis

  1. Examine all the Key Value Map Operations policies in the specific API Proxy where the failure has occurred. If there is any Key Value Map Operations policy in which the `mapIdentifier` attribute is set as an empty string, then that's the cause of the error.

For example, the following Key Value Map Operations policy has an empty `mapIdentifier`:
         
         <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="StoreKvm" mapIdentifier="">
             <DisplayName>StoreKvm</DisplayName>
             <Properties/>
             <ExclusiveCache>false</ExclusiveCache>
             <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
             <Put override="true">
                 <Key>
                     <Parameter ref="request.queryparam.key"/>
                 </Key>
                 <Value ref="request.queryparam.value"/>
             </Put>
             <Scope>environment</Scope>
         </KeyValueMapOperations>
         




### Resolution

Ensure the attribute `mapIdentifier` is set to a valid key value map in the Key Value Map Operations policy.

To correct the example policy shown above, you can specify the `mapIdentifier` to an existing key value map `UserLocationMap`.
    
    
    <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="StoreKvm" mapIdentifier="UserLocationMap">
        <DisplayName>StoreKvm</DisplayName>
        <Properties/>
        <ExclusiveCache>false</ExclusiveCache>
        <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
        <Put override="true">
            <Key>
                <Parameter ref="request.queryparam.key"/>
            </Key>
            <Value ref="request.queryparam.value"/>
        </Put>
        <Scope>environment</Scope>
    </KeyValueMapOperations>
    

## SetVariableFailed

### Error code
    
    
    steps.keyvaluemapoperations.SetVariableFailed
    

### Error response body
    
    
    {
       "fault":{
          "faultstring":"Failed to set variable variable_name in KeyValueMapStepDefinition policy_name",
          "detail":{
             "errorcode":"steps.keyvaluemapoperations.SetVariableFailed"
          }
       }
    }
    

### Example Error Message
    
    
    {
       "fault":{
          "faultstring":"Failed to set variable myvar in KeyValueMapStepDefinition EncryptedKVM",
          "detail":{
             "errorcode":"steps.keyvaluemapoperations.SetVariableFailed"
          }
       }
    }
    

### Cause

This error occurs if you try to retrieve a value from an encrypted key value map and set the value to a variable whose name does not have the prefix `private.`. The prefix, which is required for basic security purposes during debugging, hides the encrypted values from API proxy Trace and debug sessions.

### Diagnosis

1\. Identify the Key Value Map Operations policy where the error occurred and the name of the variable to which the value cannot be set. You can find both of these items in the `faultstring` element of the error response. For example, in the following `faultstring`, the policy name is `EncryptedKVM` and the variable is `myvar`:
    
    
      "faultstring":"Failed to set variable myvar in KeyValueMapStepDefinition EncryptedKVM"
    

1\. In the failed Key Value Map Operations policy XML, verify that the name of the variable specified in the **`assignTo`** attribute of the `<Get>` element matches the variable name identified in the fault string (step #1 above). For example, the following Key Value Map Operations policy specifies a variable named `myvar` in the `<Get>` element, which matches what's in the `faultstring`:
    
    
      <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="Key-Value-Map-Operations-1" mapIdentifier="testEncrypted">
          <DisplayName>KeyValueMapOperations-1</DisplayName>
          <Properties/>
          <ExclusiveCache>false</ExclusiveCache>
          <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
          <Get assignTo="myvar" index="1">
              <Key>
                  <Parameter>foo</Parameter>
              </Key>
          </Get>
          <Scope>environment</Scope>
      </KeyValueMapOperations>
    

  1. Check if the key value map specified in the `mapIdentifier` attribute is an encrypted KVM.

To check if a KVM is encrypted in the Apigee UI:

     1. In the Apigee UI, click **Admin** in the left navigation menu.
     2. Click **Environments**.
     3. Click **Key Value Maps**.
     4. Find the Key Value Map you want to use.
     5. Click the arrow to the left of the name to expand the list of values.
     6. Encrypted Key Value Maps display values masked with asterisks in the UI (*****) as shown in [About encrypted KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps#aboutencrypted).
  2. If the key value map is an encrypted KVM and the variable name used in the `assignTo` attribute of the `<Get>` element does not have the prefix `private`. Then that's the cause for the error.

In the example Key Value Map Operations policy shown above, the key value map `testEncrypted` is encrypted and the variable name `myvar` does not have the prefix `private`. Hence you receive the error code:
         
         steps.keyvaluemapoperations.SetVariableFailed
         




### Resolution

Ensure that the variable name has the prefix `private.` in the `assignTo` attribute of the `<Get>` element in Key Value Map Operations policy if the key value map used is encrypted.

To correct the example Key Value Map Operations policy shown above, you can modify the value of the attribute `assignTo` to `private.myvar`:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="Key-Value-Map-Operations-1" mapIdentifier="testEncrypted">
        <DisplayName>KeyValueMapOperations-1</DisplayName>
        <Properties/>
        <ExclusiveCache>false</ExclusiveCache>
        <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
        <Get assignTo="private.myvar" index="1">
            <Key>
                <Parameter>foo</Parameter>
            </Key>
        </Get>
        <Scope>environment</Scope>
    </KeyValueMapOperations>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
