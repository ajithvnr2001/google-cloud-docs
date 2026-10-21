---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/generate-JWT-deployment-errors/
title: GenerateJWT policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:27:32.488068+00:00
---

# GenerateJWT policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/generate-JWT-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  GenerateJWT policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/generate-JWT-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/generate-JWT-deployment-errors/).

## InvalidNameForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid name for additional claim : policy(policy_name) claim(claim_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid name for additional claim : policy(JWT-Generate-HS256) claim(iss).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidNameForAdditionalClaim-error.png)

### Cause

This error occurs if the name of the claim used in the child element `<Claim>` of the `<AdditionalClaims>` element is one of the following registered names:

"kid", "iss", "sub", "aud", "iat", "exp", "nbf", "jti"

The registered claims are specified in [RFC 7519](https://tools.ietf.org/html/rfc7519).

For example, using the claim name `iss` under the `<AdditionalClaims>` element will lead to this error.

### Diagnosis

  1. Identify the name of the Generate JWT policy and the claim name from the error message. For example, in the following error message, the name of Generate JWT policy is `JWT-Generate-HS256` and claim name is `iss`:
         
         Invalid name for additional claim : policy(JWT-Generate-HS256) claim(iss).
         

  2. Verify that the claim name used under the `<AdditionalClaims>` element in the failed Generate JWT policy XML matches the claim name identified in the error message (Step 1 above). For example, the following policy specifies the claim as `iss`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name="iss"/>
             </AdditionalClaims>
         </GenerateJWT>
         

  3. If the claim name used in the child element `<Claim>`of the`<AdditionalClaims>` element is one of the following registered names:

"kid", "iss", "sub", "aud", "iat", "exp", "nbf", "jti"

then that's the cause of the error.

In the example Generate JWT policy shown above, the `<Claim>` name is specified as `iss` under the `<AdditionalClaims>` element, resulting in the error:
         
         Invalid name for additional claim : policy(JWT-Generate-HS256) claim(iss).
         




### Resolution

Do not use any of the registered names "kid", "iss", "sub", "aud", "iat", "exp", "nbf" or "jti" in the child element `<Claim>`of the`<AdditionalClaims>` element.

To correct the example Generate JWT policy shown above, change the claim name to `status`:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='status' type='string'>Development</Claim>
        </AdditionalClaims>
    </GenerateJWT>
    

## InvalidTypeForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid type for additional claim : policy(policy_name) claim(claim_name) type(type_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid type for additional claim : policy(JWT-Generate-HS256) claim(claim) type(integer).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidTypeForAdditionalClaim-error.png)

### Cause

This error occurs if the type of claim used in the child element `<Claim>` of the `<AdditionalClaims>` element of the GenerateJWT policy is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

For example, using the claim type `integer` under the `<AdditionalClaims>` element will result in the error.

### Diagnosis

  1. Identify the name of the Generate JWT policy, the claim name, and the claim type from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256`, the claim name is `claim` and the claim type is `integer`:
         
         Invalid type for additional claim : policy(JWT-Generate-HS256) claim(claim) type(integer).
         

  2. Verify that the claim name and the type used under the `<AdditionalClaims>` element in the failed Generate JWT policy XML matches the claim name and type identified in the error message in Step 1. For example, the following policy specifies the claim as `claim` and the type as `integer`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='integer'/>
             </AdditionalClaims>
         </GenerateJWT>
         

  3. If the claim type used in the child element `<Claim>` of the `<AdditionalClaims>` element is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

then that's the cause of the error.

In the example Generate JWT policy shown above, the `<Claim>` type under the `<AdditionalClaims>` element is specified as `integer`. Because `integer` is not a supported type, you get the error:
         
         Invalid type for additional claim : policy(JWT-Generate-HS256) claim(claim) type(integer).
         




### Resolution

Ensure that only supported data types such as `string`, `number`, `boolean`, or `map` are used in the child element `<Claim>` of the `<AdditionalClaims>` element.

To correct the example Generate JWT policy shown above, change the claim type to `boolean`.
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalClaims>
    </GenerateJWT>
    

## MissingNameForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Error occurred while validation of bean(policy_name.xml) Reason: - Required attribute name is missing in Claim.

### Example error message
    
    
    Error Saving Revision 2
    Error occurred while validation of bean JWT-Generate-HS256.xml. Reason: - Required attribute name is missing in Claim
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/MissingNameForAdditionalClaim-error.png)

### Cause

This error occurs if the name of the claim is not specified in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element.

### Diagnosis

  1. Identify the name of the Generate JWT policy from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256`:
         
         Error occurred while validation of bean JWT-Generate-HS256.xml. Reason: - Required attribute name is missing in Claim
         

  2. Examine the failed Generate JWT policy XML and verify if the claim name is missing in the child element `<Claims>` under the `<AdditionalClaims>` or `<AdditionalHeaders>` element. For example, the following Generate JWT policy does not specify the claim name under the `<AdditionalClaims>` element:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim ref='reqclaim' type='boolean'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the `<Claim>` name is not specified under the `<AdditionalClaims>` element you get the error:
         
         Error occurred while validation of bean JWT-Generate-HS256.xml. Reason: - Required attribute name is missing in Claim
         




### Resolution

Ensure that the name of the claim is always specified in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element.

To correct the example Generate JWT policy shown above, specify the claim name as shown below:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalClaims>
    </GenerateJWT>
    

## InvalidNameForAdditionalHeader

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid name for additional header : policy(policy_name)header(header_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid name for additional header: policy(JWT-Generate-HS256) header(alg).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidNameForAdditionalHeader-error.png)

### Cause

This error occurs if the name of the claim used in the child element `<Claim>` of the `<AdditionalHeaders>` element is one of the following standard JWT headers:

`alg` or `typ`

For example, using the claim name `alg` under the `<AdditionalHeaders>` element will cause the error.

### Diagnosis

  1. Identify the name of the Generate JWT policy and header name from the error message. For example, in the following error message, the name of Generate JWT policy is `JWT-Generate-HS256` and header name is `alg`:
         
         Invalid name for additional header: policy(JWT-Generate-HS256) header(alg).
         

  2. Verify that the header name used in the child element `<Claim>` under the `<AdditionalHeaders>` element in the failed Generate JWT policy XML matches the header name identified in the error message in Step 1. For example, the following policy specifies the header as `alg`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalHeaders>
                 <Claim name="alg"/>
             </AdditionalHeaders>
         </GenerateJWT>
         

  3. If the header name used in the child element `<Claim>` of the `<AdditionalClaims>` element is one of the following standard JWT headers:

`alg` or `typ`

then that's the cause of the error.

In the example Generate JWT policy shown above, the `<Claim>` name is specified as `alg` under the `<AdditionalClaims>` element, resulting in the error:
         
         Invalid name for additional header: policy(JWT-Generate-HS256) header(alg).
         




### Resolution

Do not use the standard JWT headers `alg` or `typ` in the child element `<Claim>` of the `<AdditionalHeaders>` element.

To correct the example Generate JWT policy shown above, use the name `x5c` in the child element `<Claim>` of the `<AdditionalHeaders>` element:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='x5c'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidTypeForAdditionalHeader

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid type for additional header : policy(policy_name) claim(claim_name) type(type_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid type for additional header : policy(JWT-Generate-HS256) claim(claim1) type(integer).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidTypeForAdditionalHeader-error.png)

### Cause

The error will occur if the type of claim used in the child element `<Claim>` of the `<AdditionalHeaders>` element of the GenerateJWT policy is not one of the following types:

`string` (default), `number`, `boolean`, or `map`.

For example, using the claim type `integer` under the `<AdditionalHeaders>` element will cause the error.

### Diagnosis

  1. Identify the name of the Generate JWT policy, the claim name, and the claim type from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256`, the claim name is `claim,` and the claim type is `integer:`
         
         Invalid type for additional header : policy(JWT-Generate-HS256) claim(claim) type(integer).
         

  2. Verify that the claim name and the claim type used under the `<AdditionalClaims>` element in the failed Generate JWT policy XML matches the claim name and claim type identified in the error message in Step 1. For example, the following policy specifies the claim as `claim` and the claim type as `integer`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalHeaders>
                 <Claim name='claim' ref='reqclaim' type='integer'/>
             </AdditionalHeaders>
         </GenerateJWT>
         

  3. If the claim type used in the child element `<Claim>` of the `<AdditionalHeaders>` element is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

then that's the cause of the error.

In the example Generate JWT policy shown above, the `<Claim>` type under the `<AdditionalHeaders>` element is specified as `integer`. Because `integer` is not a supported type, you get the error:
         
         Invalid type for additional header : policy(JWT-Generate-HS256) claim(claim) type(integer).
         




### Resolution

Ensure that only the supported data types `string`, `number`, `boolean`, or `map` are used in the child element `<Claim>` of the `<AdditionalHeaders>` element.

To correct the example Generate JWT policy shown above, change the claim type to `boolean`:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidValueOfArrayAttribute

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid value for array attribute: policy(policy_name)claim(claim_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid value for array attribute: policy(JWT-Generate-HS256) claim(claim).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidValueOfArrayAttribute-error.png)

### Cause

This error occurs if the value of the array attribute in the in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element is not set to `true` or `false`.

For example, setting the value of the array attribute as `yes` in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` causes the error.

### Diagnosis

  1. Identify the name of the Generate JWT policy and the claim name from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the claim name is `claim:`
         
         Invalid value for array attribute: policy(JWT-Generate-HS256) claim(claim).
         

  2. Verify that the claim name used in the child element `<Claim>` under the `<AdditionalHeaders>` element in the failed Generate JWT policy XML matches the claim name identified in the error message in Step 1. For example, the following policy specifies the claim name as `claim`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='yes'/>
             </AdditionalClaims>
         </GenerateJWT>
         

  3. If the value of the `array` attribute in the child element `<Claim>` of the `<AdditionalClaims>` element is not set to `true` or `false`, then that's the cause of the error.

Because the `array` attribute in the child element `<Claim>` of the `<AdditionalClaims>` element is set to `yes` in the example above, you get the error:
         
         Invalid value for array attribute: policy(JWT-Generate-HS256) claim(claim).
         




### Resolution

Ensure that the value of the array attribute in the in the child element `<Claim>`of the `<AdditionalClaims>` or `<AdditionalHeaders>` is set to `true` or `false`.

To correct the example Generate JWT policy shown above, change the value of array attribute to `true`:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidConfigurationForActionAndAlgorithm

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid configuration element for this action and algorithm Family: policy(<var>policy_name</var>) element(<var>element_name</var>) action(<var>action_name</var>) family(<var>family_name</var>).
    

### Example error message
    
    
    Error Saving Revision 2
    Invalid configuration element for this action and algorithm Family: policy(JWT-Generate-HS256) element(PrivateKey) action(Generate) family(HMAC).

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidConfigurationForActionAndAlgorithm-error.png)

### Cause

This error occurs if the `<PrivateKey>` element is used with HS Family algorithms and the `<SecretKey>` element is used with RSA Family algorithms. The error will also occur if _either_ of these conditions are true.

For example, using the `<PrivateKey>` element with HS Family algorithms leads to this error.

### Diagnosis

  1. Identify the name of the Generate JWT policy, the element name, and the algorithm family name from the error message. For example, in the following error message the name of the Generate JWT policy is `JWT-Generate-HS256`, the element name is `PrivateKey` and the algorithm family is `HMAC`:
         
         Invalid configuration element for this action and algorithm Family: policy(JWT-Generate-HS256) element(PrivateKey) action(Generate) family(HMAC).
         

  2. Verify that the element and the algorithm family used in the failed Generate JWT policy XML matches the element and the algorithm family identified in the error message in Step 1. For example, the following policy specifies the element as `PrivateKey` and the algorithm family as `HMAC`, which matches what's in the error message:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <PrivateKey>
                 <Password ref="private.privatekey-password"/>
         
             </PrivateKey>
                 <ExpiresIn>1h</ExpiresIn>
                 <Subject>monty-pythons-flying-circus</Subject>
                 <Issuer>urn://apigee-JWT-policy-test</Issuer>
                 <Audience>fans</Audience>
                 <Id/>
                 <AdditionalClaims>
                     <Claim name='claim' ref='reqclaim' type='string' array=tuu
             =/>
                 </AdditionalClaims>
             </GenerateJWT>
         

  3. If the value of the `<Algorithm>` element is `HS256`, but you have used `<PrivateKey>`, then that's the cause of the error.

In the example Generate JWT policy shown above, the `<PrivateKey>` is used even though the `<PrivateKey>` is set to a family algorithm, `HS256`, resulting in the error:
         
         Invalid configuration element for this action and algorithm Family: policy(JWT-Generate-HS256) element(PrivateKey) action(Generate) family(HMAC).
         




### Resolution

Ensure the `<PrivateKey>` element is used only with RSA Family algorithms and the `<SecretKey>` element is used only with HS Family algorithms.

To correct the example Generate JWT policy shown above, use the `<SecretKey>` from the GenerateJWT policy that uses the HS256 algorithm:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidValueForElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid Value for element : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid Value for element : policy(JWT-Generate-HS256) element(Algorithm).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidValueForElement-error.png)

### Cause

This error occurs if the value specified in the `<Algorithm>` element is not one of the following values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

For example, specifying the algorithm value as `RS128` in the `<Algorithm>` element leads to this error.

### Diagnosis

  1. Identify the name of the Generate JWT policy and the element name from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the element name is `Algorithm.`
         
         Invalid Value for element : policy(JWT-Generate-HS256) element(Algorithm).
         

  2. Examine the failed Generate JWT policy XML and check the value specified for the `<Algorithm>` element.

Here's a sample Generate JWT policy:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS128</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='status' type='string'>Development</Claim>
             </AdditionalClaims>
         </GenerateJWT>
         

  3. Examine the value specified in the `<Algorithm>` element. If it is not one of the following values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

then that's the cause of the error.

In the example Generate JWT policy shown above, the `<Algorithm>` name is specified as `HS128`. Because this is not a supported algorithm, you get the error:
         
         Invalid Value for element : policy(JWT-Generate-HS256) element(Algorithm).
         




### Resolution

Ensure that the value specified in the `<Algorithm>` element is one of the supported values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

To correct the example Generate JWT policy shown above, which uses the `<SecretKey>` element, change the value of the `<Algorithm>` to `HS25`. Note, when the `<SecretKey>` element is used, you can only use HS Family algorithms.
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='status' type='string'>Development</Claim>
        </AdditionalClaims>
    </GenerateJWT>
    

## MissingConfigurationElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Missing configuration element : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Missing configuration element : policy(JWT-Generate-HS256) element(SecretKey).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/MissingConfigElem-error.png)

### Cause

This error occurs when the `<PrivateKey>` element is **not** used with RSA Family algorithms in the Generate JWT policy. Likewise, the error can occur if the `<SecretKey>` element is **not** used with HS Family algorithms in the Generate JWT policy.

For example, not using the `<PrivateKey>` element with RSA Family algorithms leads to this error.

### Diagnosis

  1. Identify the name of the Generate JWT policy and missing element name from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the missing element name is `SecretKey`.
         
         Missing configuration element : policy(JWT-Generate-HS256) element(SecretKey).
         

  2. Examine the failed Generate JWT policy XML and verify that the element indicated in the error message is missing. If it is missing, then that's the cause of the error.

For example, in the following policy the `SecretKey` is missing and the `Algorithm` used is `HS256`:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

The example Generate JWT policy uses HS Family algorithms, but the mandatory element `SecretKey` is missing, resulting in the error:
         
         Missing configuration element : policy(JWT-Generate-HS256) element(SecretKey).
         




### Resolution

Ensure that the mandatory `<PrivateKey>` element is used with RSA Family algorithms and the mandatory `<SecretKey>` element is used with HS Family algorithms.

To correct the example Generate JWT policy shown above, which uses the `HS256` algorithm, add the `<SecretKey>` element to the Generate JWT policy:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidKeyConfiguration

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 
    Invalid Key configuration : policy(policy_name).

### Example error message
    
    
    Error Saving Revision 3
    Invalid Key configuration : policy(JWT-Generate-HS256).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 3.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidKeyConfiguration-error.png)

### Cause

This error occurs if the mandatory child element `<Value>` is not defined in the `<PrivateKey>` or `<SecretKey>` elements in the Generate JWT policy.

### Diagnosis

  1. Identify the name of the Generate JWT policy from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256`.
         
         Invalid Key configuration : policy(JWT-Generate-HS256).
         

  2. Examine the failed Generate JWT policy XML and verify if the child element `<Value>` is not defined in the `<PrivateKey>` or `<SecretKey>` elements. If `<Value>` is not defined, then that's the cause of the error.

For example, in the following policy the child element `<Value>` is not defined in the `<SecretKey>`element:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <SecretKey>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the child element `<Value>` is not defined in the `<SecretKey>` element of the Generate JWT policy, you get the error:
         
         Invalid Key configuration : policy(JWT-Generate-HS256).
         




### Resolution

Ensure that the child element `<Value>` is always defined in the `<PrivateKey>` or `<SecretKey>` elements of the Generate JWT policy.

To correct the example Generate JWT policy shown above, define the child element `<Value>` under the `<SecretKey>` element as shown below:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## EmptyElementForKeyConfiguration

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Empty Element for Key Configuration : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Empty Element for Key Configuration : policy(JWT-Generate-HS256) element(SecretKey/Value).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/EmptyElementForKeyConfiguration-error.png)

### Cause

This error occurs if the ref attribute in the child element `<Value>` of the `<PrivateKey>` or `<SecretKey>` elements is not specified or empty.

For example, if the child element `<Value>` of the `<SecretKey>` element is empty, then the error occurs.

### Diagnosis

  1. Identify the name of the Generate JWT policy and the empty element name from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the empty element name is `SecretKey/Value`.
         
         Empty Element for Key Configuration : policy(JWT-Generate-HS256) element(SecretKey/Value).
         

  2. Examine the failed Generate JWT policy XML and verify if the element identified in Step 1 is empty. If it is empty, then that's the cause of the error.

For example, the following policy shows that the child element `<Value>` of the `<SecretKey>` element is empty:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <SecretKey>
                 <Value/>
                 <Id>1918290</Id>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the child element `<Value>` of the `<SecretKey>` element in the Generate JWT policy is empty, you get the error:
         
         Empty Element for Key Configuration : policy(JWT-Generate-HS256) element(SecretKey/Value).
         




### Resolution

Ensure that the ref attribute in the child element `<Value>` of the `<PrivateKey>` or `<SecretKey>` elements is always specified and has the prefix "`private.`".

To correct the example Generate JWT policy shown above, use the flow variable `private.privatekey` in the child element `<Value>` of the `<SecretKey>` element.
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidVariableNameForSecret

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid variable name for secret : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid variable name for secret : policy(JWT-Generate-HS256) element(SecretKey/Value).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidVariableNameForSecret-error.png)

### Cause

This error occurs if the flow variable name specified in the ref attribute in the child element `<Value>` of the `<PrivateKey>` or `<SecretKey>` elements does not include the private prefix (**`private.`**).

For example :

If the flow variable name is specified as **`mykey`** in the ref attribute of the child element `<Value>` of the `<PrivateKey>` element, then this error occurs.

### Diagnosis

  1. Identify the name of the Generate JWT policy and the name of the element with an invalid variable name from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the element name is `SecretKey/Value`.
         
         Invalid variable name for secret : policy(JWT-Generate-HS256) element(SecretKey/Value).
         

  2. Examine the failed Generate JWT policy XML and verify the variable name used in the element, identified in Step 1. If the variable name does not have the prefix **`private.`** , then that's the cause of the error.

For example, the following policy shows that the child element `<Value>` of the `<SecretKey>` element has the invalid variable name `mykey`:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <SecretKey>
                 <Value ref="mykey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the variable name specified in the child element `<Value>` of the `<SecretKey>` element of the Generate JWT policy does not have the prefix **`private.`** , you get the error:
         
         Invalid variable name for secret : policy(JWT-Generate-HS256) element(SecretKey/Value).
         




### Resolution

Ensure that the ref attribute in the child element `<Value>` of the `<PrivateKey>` or `<SecretKey>` elements is always specified and has the prefix **`private.`**.

To correct the example Generate JWT policy shown above, use the flow variable `private.privatekey` in the child element `<Value>` of the `<SecretKey>` element:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidSecretInConfig

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Specifying a secret in the configuration is invalid : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Specifying a secret in the configuration is invalid : policy(JWT-Generate-HS256) element(SecretKey/Value).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidSecretInConfig-error.png)

### Cause

This error occurs if the value (secret) is specified explicitly in:

  * The child elements `<Value>` or `<Password>` of the `<PrivateKey>` element or
  * The child element `<Value>` of the `<SecretKey>` element



in the Generate JWT policy.

For example, if the secret is specified explicitly as **`abc`** in the child element `<Value>` of the `<SecretKey>` element, then this error occurs.

### Diagnosis

  1. Identify the name of the Generate JWT policy and element name in which the secret is explicitly specified from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the element name is `SecretKey/Value`.
         
         Specifying a secret in the configuration is invalid : policy(JWT-Generate-HS256) element(SecretKey/Value).
         

  2. Examine the failed Generate JWT policy XML and verify if the secret is explicitly specified in the element identified in Step 1. If it is specified explicitly, then that's the cause of the error.

For example, the following policy shows that the secret has been specified explicitly in the child element `<Value>` of the `<SecretKey>`element:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <SecretKey>
                 <Value>abc</Value>
                 <Id>1918290</Id>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the secret is specified explicitly in the child element `<Value>` of the `<SecretKey>` element of the Generate JWT policy, you get the error:
         
         Specifying a secret in the configuration is invalid : policy(JWT-Generate-HS256) element(SecretKey/Value).
         




### Resolution

Ensure that the value is always specified as a flow variable in the child element `<Value>` of the `<PrivateKey>` or `<SecretKey>` elements.

To correct the example Generate JWT policy shown above, use the flow variable `private.secretkey` in the ref attribute of the child element `<Value>` of the `<SecretKey>`:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <ExpiresIn>1h</ExpiresIn>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

## InvalidTimeFormat

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 2
    Invalid Time format: policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 3
    Invalid Time format: policy(JWT-Generate-HS256) element(NotBefore).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision 3.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidTimeFormat-error.png)

### Cause

This error occurs if the value specified in the `<NotBefore>` element is not among one of the supported formats:

`sortable`, `RFC 1123`, `RFC 850`, `ANCI-C`

For example, if the value specified in `<NotBefore>` is `20-JUN-1990 08:03`, which is not a supported format, then this error occurs.
    
    
    <NotBefore>20-JUN-1990 08:03:00:21-07:00</NotBefore>
    

### Diagnosis

  1. Identify the name of the Generate JWT policy and the element name which has an invalid time format from the error message. For example, in the following error message, the name of the Generate JWT policy is `JWT-Generate-HS256` and the element name is `NotBefore`.
         
         Invalid Time format: policy(JWT-Generate-HS256) element(NotBefore).
         

  2. Examine the failed Generate JWT policy XML and verify the time format used in the element identified in Step 1. If the element does not use any of the supported formats:

`sortable`, `RFC 1123`, `RFC 850`, `ANCI-C`

then that's the cause of the error.

For example, the following policy shows that the child element `<NotBefore>` uses an unsupported time format:
         
         <GenerateJWT name="JWT-Generate-HS256">
             <DisplayName>JWT Generate HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <NotBefore>20-JUN-1990 08:03:00:21-07:00</NotBefore>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </GenerateJWT>
         

Because the element `<NotBefore>` of the Generate JWT policy does not use any of the supported time formats, you get the error:
         
         Invalid variable name for secret : policy(JWT-Generate-HS256) element(SecretKey/Value).
         




### Resolution

Ensure the value specified in the `<NotBefore>` element uses one of the supported formats:

`sortable`, `RFC 1123`, `RFC 850`, `ANCI-C`

To correct the example Generate JWT policy, modify the date in the `<NotBefore>` element to use the `sortable` format as shown below:
    
    
    <GenerateJWT name="JWT-Generate-HS256">
        <DisplayName>JWT Generate HS256</DisplayName>
        <Algorithm>HS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <ExpiresIn>1h</ExpiresIn>
        <NotBefore>2018-08-14T11:00:21-07:00</NotBefore>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </GenerateJWT>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
