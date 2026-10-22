---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/basic-authentication-deployment-errors/
title: BasicAuthentication policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:00.400317+00:00
---

# BasicAuthentication policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/basic-authentication-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  BasicAuthentication policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/basic-authentication-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/basic-authentication-deployment-errors/).

## UserNameRequired

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to env_name
    BasicAuthenticationPolicy: Username element must be present for operation operation.

**Example error message**
    
    
    Error Deploying Revision 2 to test
    BasicAuthenticationPolicy: Username element must be present for Encode operation.
    

**Example screenshot**

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ba-usernamerequired.png)

### Cause

The deployment of the API Proxy fails if the `<User>` element is not defined in the [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy). The `<User>` element is mandatory for both Encode and Decode operations.

For Encoding operation, the `<User>` element is used to specify the variable containing the username. For the Decoding operation, the `<User>` element is used to specify the variable where the decoded username is written.

### Diagnosis

  1. Examine all the BasicAuthentication policies used in the API proxy. If there is any policy where the `<User>` element is not specified, then that's the cause of the error. The `<User>` element is mandatory in BasicAuthentication policy for Encode or Decode operations.

The sample BasicAuthentication policy shown below is used for Encode operation, but doesn't have the `<User>` element defined:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <BasicAuthentication name="ApplyBasicAuthHeader">
           <DisplayName>ApplyBasicAuthHeader</DisplayName>
           <Operation>Encode</Operation>
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <Password ref="BasicAuth.credentials.password"/>
           <AssignTo createNew="false">request.header.Authorization</AssignTo>
         </BasicAuthentication>
         

The deployment fails with the below error:
         
         BasicAuthenticationPolicy: Username element must be present for Encode operation.
         




### Resolution

Ensure that the `<User>` element is defined within the BasicAuthentication policy for Encode or Decode operation.

To correct the example shown above, include the `<User>` element within the policy as shown below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <BasicAuthentication name="ApplyBasicAuthHeader">
        <DisplayName>ApplyBasicAuthHeader</DisplayName>
        <Operation>Encode</Operation>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <User ref="BasicAuth.credentials.username"/>
        <Password ref="BasicAuth.credentials.password"/>
        <AssignTo createNew="false">request.header.Authorization</AssignTo>
    </BasicAuthentication>
    

## PasswordRequired

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to env_name
    BasicAuthenticationPolicy: Password element must be present for operation operation.

**Example error message**
    
    
    Error Deploying Revision 2 to test
    BasicAuthenticationPolicy: Password element must be present for Encode operation.
    

**Example screenshot**

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ba-passwordrequired.png)

### Cause

The deployment of the API Proxy fails if the `<Password>` element is not defined in the [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy). The `<Password>` element is mandatory for both Encode and Decode operations.

For Encoding operation, the `<Password>` element is used to specify the variable containing the password. For the Decoding operation, the `<Password>` element is used to specify the variable where the decoded password is written.

### Diagnosis

  1. Examine all the BasicAuthentication policies used in the API proxy. If there is any policy where the `<Password>` element is not defined, then that's the cause of the error. The `<Password>` element is mandatory in the BasicAuthentication policy for Encode or Decode operation.

The sample BasicAuthentication policy shown below is used for Encode operation, but doesn't have the `<Password>` element defined:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <BasicAuthentication name="ApplyBasicAuthHeader">
           <DisplayName>ApplyBasicAuthHeader</DisplayName>
           <Operation>Encode</Operation>
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <User ref="BasicAuth.credentials.username"/>
           <AssignTo createNew="false">request.header.Authorization</AssignTo>
         </BasicAuthentication>
         

The deployment fails with the below error:
         
         BasicAuthenticationPolicy: Password element must be present for Encode operation.
         




### Resolution

Ensure that the `<Password>` element is defined within the BasicAuthentication policy for Encode or Decode operation.

To correct the example shown above, include the `<Password>` element within the policy as shown below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <BasicAuthentication name="ApplyBasicAuthHeader">
        <DisplayName>ApplyBasicAuthHeader</DisplayName>
        <Operation>Encode</Operation>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <User ref="BasicAuth.credentials.username"/>
        <Password ref="BasicAuth.credentials.password"/>
        <AssignTo createNew="false">request.header.Authorization</AssignTo>
    </BasicAuthentication>
    

## AssignToRequired

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to env_name
    BasicAuthenticationPolicy: AssignTo element must be present for operation operation.

**Example error message**
    
    
    Error Deploying Revision 2 to test
    BasicAuthenticationPolicy: AssignTo element must be present for Encode operation.
    

**Example screenshot**

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ba-assigntorequired.png)

### Cause

The deployment of the API Proxy fails if the `<AssignTo>` element is not defined in the [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy). The `<AssignTo>` element is mandatory for both Encode and Decode operations.

The `<AssignTo>` element specifies the target variable to set with the encoded or decoded value generated by the BasicAuthentication policy.

### Diagnosis

  1. Examine all the BasicAuthentication policies used in the API proxy. If there is any policy where the element `<AssignTo>` is not defined, then that's the cause of the error. The `<AssignTo>` element is mandatory to be defined in BasicAuthentication policy for both Encode and Decode operations.

The sample BasicAuthentication policy shown below is used for Encode operation, but doesn't have the `<AssignTo>` element defined:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <BasicAuthentication name="ApplyBasicAuthHeader">
           <DisplayName>ApplyBasicAuthHeader</DisplayName>
           <Operation>Encode</Operation>
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <User ref="BasicAuth.credentials.username"/>
           <Password ref="BasicAuth.credentials.password"/>
         </BasicAuthentication>
         

The deployment fails with the below error:
         
         BasicAuthenticationPolicy: AssignTo element must be present for Encode operation.
         




### Resolution

Ensure that the `<AssignTo>` element is defined within the BasicAuthentication policy for Encode or Decode operation.

To correct the example shown above, include the `<AssignTo>` element within the policy as shown below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <BasicAuthentication name="ApplyBasicAuthHeader">
        <DisplayName>ApplyBasicAuthHeader</DisplayName>
        <Operation>Encode</Operation>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <User ref="BasicAuth.credentials.username"/>
        <Password ref="BasicAuth.credentials.password"/>
        <AssignTo createNew="false">request.header.Authorization</AssignTo>
    </BasicAuthentication>
    

## SourceRequired

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to env_name
    BasicAuthenticationPolicy: Source element must be present for Decode operation.

**Example error message**
    
    
    Error Deploying Revision 2 to test
    BasicAuthenticationPolicy: Source element must be present for Decode operation.
    

**Example screenshot**

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ba-sourcerequired.png)

### Cause

The deployment of the API Proxy fails if the `<Source>` element is not defined in the BasicAuthentication policy that is used for decoding operation. The `<Source>` element is mandatory if the `<Operation>` is specified as `Decode` in the BasicAuthentication policy.

The `<Source>` element specifies the Base64 encoded string that needs to be decoded.

### Diagnosis

  1. Examine all the BasicAuthentication policies used in the API proxy. If there is any policy where the element `<Source>` is not defined and the `<Operation>` element is defined as `Decode`, then that's the cause of the error. The `<Source>` element is mandatory if the `<Operation>` is specified as `Decode` in the BasicAuthentication policy.

The sample BasicAuthentication policy shown below is used for `Decode` operation, but doesn't have the `<Source>` element defined:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <BasicAuthentication name="ApplyBasicAuthHeader">
           <DisplayName>ApplyBasicAuthHeader</DisplayName>
           <Operation>Decode</Operation>
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <User ref="BasicAuth.credentials.username"/>
           <Password ref="BasicAuth.credentials.password"/>
           <AssignTo createNew="false">request.header.Authorization</AssignTo>
         </BasicAuthentication>
         

The deployment fails with the below error:
         
         BasicAuthenticationPolicy: Source element must be present for Decode operation.
         




### Resolution

Ensure that the `<Source>` element is defined in BasicAuthentication policy when it is used for `Decode` operation.

To correct the example shown above, include the <`Source>`element within the policy as shown below:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <BasicAuthentication name="ApplyBasicAuthHeader">
        <DisplayName>ApplyBasicAuthHeader</DisplayName>
        <Operation>Decode</Operation>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <User ref="BasicAuth.credentials.username"/>
        <Password ref="BasicAuth.credentials.password"/>
        <AssignTo createNew="false">request.header.Authorization</AssignTo>
        <Source>request.header.Authorization</Source>
    </BasicAuthentication>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
