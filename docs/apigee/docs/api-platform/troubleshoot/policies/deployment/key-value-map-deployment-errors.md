---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/key-value-map-deployment-errors/
title: Key Value Map Operations policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:53.007691+00:00
---

# Key Value Map Operations policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/key-value-map-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Key Value Map Operations policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/key-value-map-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/key-value-map-deployment-errors/).

## InvalidIndex

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid index index in KeyValueMapStepDefinition policy_name.
    

### Example Error Message
    
    
    Error Saving Revision 2
    Invalid index 0 in KeyValueMapStepDefinition GetKVM.
    

### Example Error Screenshot

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/kvm-deploy-error-3.png)

### Cause

If the `index` attribute specified in the `<Get>` element of a Key Value Map Operations policy is zero or a negative number, then the deployment of the API proxy fails. The index starts from `1`, so an index of zero or negative integer is considered as invalid.

For example, if the `index` specified is `0` in the `<Get>` element of a Key Value Map Operations policy, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the Key Value Map Operations policy where the error occurred and the invalid index. You can find this information from the error message. For example, in the following error, the policy name is `GetKVM` and the invalid index is `0`:

`Invalid index **_0_** in KeyValueMapStepDefinition _GetKVM_.`

  2. Verify that the value of the index specified in the `<Get>` element of the failed Key Value Map Operations policy matches with the value identified in the error message (step #1 above). For example, the following policy specifies the value of the index as `0`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <KeyValueMapOperations mapIdentifier="FooKVM" async="false" continueOnError="false" enabled="true" name="GetKVM">
             <DisplayName>GetKVM</DisplayName>
             <ExpiryTimeInSecs>86400</ExpiryTimeInSecs>
             <Scope>environment</Scope>
             <Get assignTo="foo_variable" index="0">
                 <Key>
                     <Parameter>FooKey_1</Parameter>
                 </Key>
             </Get>
         </KeyValueMapOperations>
         

  3. If the index specified is zero or negative integer, then that's the cause of the error.

In the example Key Value Map Operations policy shown above, the value of the index is `0`, which is invalid. Therefore, the deployment of the API Proxy fails with the error:
         
         Invalid index 0 in KeyValueMapStepDefinition GetKVM.
         




### Resolution

Ensure that index attribute specified in the `<Get>` element of Key Value Map Operations policy is valid (non-zero or negative integer).

To correct the example Key Value Map Operations policy shown above, you could modify the index to `1`.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <KeyValueMapOperations mapIdentifier="FooKVM" async="false" continueOnError="false" enabled="true" name="GetKVM">
        <DisplayName>GetKVM</DisplayName>
        <ExpiryTimeInSecs>86400</ExpiryTimeInSecs>
        <Scope>environment</Scope>
        <Get assignTo="foo_variable" index="1">
            <Key>
                <Parameter>FooKey_1</Parameter>
            </Key>
        </Get>
    </KeyValueMapOperations>
    

## KeyIsMissing

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Error occurred while validation of bean policy_name.xml
    Reason: - Non null value expected for element Parameter in Entry.
    

### Example Error Message
    
    
    Error Saving Revision 3
    Error occurred while validation of bean GetKVM.xml. Reason: - Non null value expected for element Parameter in Entry
    

### Example Error Screenshot

![Error saving revision 3.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/kvm-deploy-error-2.png)

### Cause

This error occurs if the `<Key>` element is completely missing or `<Parameter>` element is missing within `<Key>` element underneath the `<Entry>` of the `<InitialEntries>` element of the Key Value Map Operations policy.

### Diagnosis

  1. Identify the Key Value Map Operations policy where the error occurred. You can find this information from the error message. For example, in the following error the name of the Key Value Map Operations policy is `GetKVM`.
         
         Error occurred while validation of bean GetKVM.xml. Reason: - Non null value expected for element Parameter in Entry
         

  2. In the failed Key Value Map Operations policy, check if there is any `<Entry>` element which has a missing `<Key>` or `<Parameter>` element underneath the `<InitialEntries>`.

Here's a sample Key Value Map Operations policy that has missing `<Parameter>` element within `<Key>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="GetKVM" mapIdentifier="FooKVM">
             <DisplayName>GetKVM</DisplayName>
             <Properties/>
             <ExclusiveCache>false</ExclusiveCache>
             <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
             <InitialEntries>
                 <Entry>
                     <Key/>
                     <Value>v1</Value>
                 </Entry>
                 <Entry>
                     <Key>
                         <Parameter>k2</Parameter>
                     </Key>
                     <Value>v2</Value>
                 </Entry>
             </InitialEntries>
         

In this case the first element is causing the issue.




### Resolution

Ensure that all the `<Entry>` elements underneath the `<InitialEntries>` element in the Key Value Map Operations policy have a `<Key>` element followed by a `<Parameter>` element.

To correct the example Key Value Map Operations policy shown above, adding a `<Parameter>` element solves the problem:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="GetKVM" mapIdentifier="FooKVM">
        <DisplayName>GetKVM</DisplayName>
        <Properties/>
        <ExclusiveCache>false</ExclusiveCache>
        <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
        <InitialEntries>
            <Entry>
                <Key>
                    <Parameter>k1</Parameter>
                </Key>
                <Value>v1</Value>
            </Entry>
            <Entry>
                <Key>
                    <Parameter>k2</Parameter>
                </Key>
                <Value>v2</Value>
            </Entry>
        </InitialEntries>
        ...
    

## ValueIsMissing

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Error occurred while validation of bean policy_name.xml. Reason: - Non null value expected for element Value in Entry.
    

### Example Error Message
    
    
    Error Saving Revision 3
    Error occurred while validation of bean GetKVM.xml.Reason: - Non null value expected for element Value in Entry
    

### Example Error Screenshot

![Error saving revision 3.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/kvm-deploy-error-1.png)

### Cause

This error occurs if the `<Value>` element is missing underneath the `<Entry>` element of the `<InitialEntries>` element of the Key Value Map Operations policy.

### Diagnosis

  1. Identify the Key Value Map Operations policy where the error occurred. You can find this information from the error message. For example, in the following error the name of the Key Value Map Operations policy is `GetKVM`.
         
         Error occurred while validation of bean GetKVM.xml. Reason: - Non null value expected for element Value in Entry
         

  2. In the failed Key Value Map Operations policy, check if there is any `<Entry>` element which has a missing `<Value>` element underneath the `<InitialEntries>`.

Here's a sample Key Value Map Operations policy that has missing `<Value>` element:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="GetKVM" mapIdentifier="testNotEncrypte">
             <DisplayName>GetKVM3</DisplayName>
             <Properties/>
             <ExclusiveCache>false</ExclusiveCache>
             <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
             <InitialEntries>
                 <Entry>
                     <Key>
                         <Parameter>k1</Parameter>
                     </Key>
                 </Entry>
                 <Entry>
                     <Key>
                         <Parameter>k2</Parameter>
                     </Key>
                     <Value>v2</Value>
                 </Entry>
             </InitialEntries>
             ...
         
         




### Resolution

Ensure that all the `<Entry>` elements underneath the `<InitialEntries>` element in the Key Value Map Operations policy have a `<Value>` element.

To correct the example Key Value Map Operations policy shown above, adding a `<Value>` element solves the problem:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <KeyValueMapOperations async="false" continueOnError="false" enabled="true" name="GetKVM" mapIdentifier="testNotEncrypte">
        <DisplayName>GetKVM3</DisplayName>
        <Properties/>
        <ExclusiveCache>false</ExclusiveCache>
        <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
        <InitialEntries>
            <Entry>
                <Key>
                    <Parameter>k1</Parameter>
                </Key>
                <Value>v1</Value>
            </Entry>
            <Entry>
                <Key>
                    <Parameter>k2</Parameter>
                </Key>
                <Value>v2</Value>
            </Entry>
        </InitialEntries>
        ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
