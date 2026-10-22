---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/verify-JWT-deployment-errors/
title: VerifyJWT policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:42.408192+00:00
---

# VerifyJWT policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/verify-JWT-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  VerifyJWT policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/verify-JWT-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/verify-JWT-deployment-errors/).

## InvalidNameForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid name for additional claim : policy(policy_name) claim(claim_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid name for additional claim : policy(JWT-Verify-RS256) claim(iss).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid name for additional claim error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidNameForAdditionalClaim-VerifyJWT-error.png)

### Cause

This error occurs if the name of the claim used in the child element `<Claim>` of the `<AdditionalClaims>` element is one of the following registered names:

"kid", "iss", "sub", "aud", "iat", "exp", "nbf", "jti"

The registered claims are specified in [RFC 7519](https://tools.ietf.org/html/rfc7519).

For example, using the claim name **`iss`** under the `<AdditionalClaims>` element will result in this error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and claim name from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256` and the claim name is `iss`:
         
         Invalid name for additional claim : policy(JWT-Verify-RS256) claim(iss).
         

  2. Verify that the claim name used under the `<AdditionalClaims>` element in the failed Verify JWT policy XML matches the claim name identified in the error message in Step 1. For example, the following policy specifies the claim as `iss`, which matches what's in the error message:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name="iss"/>
             </AdditionalClaims>
         </VerifyJWT>
         

  3. If the claim name used in the child element `<Claim>` of the `<AdditionalClaims>` element is one of the following registered names:

"kid", "iss", "sub", "aud", "iat", "exp", "nbf", "jti"

then that's the cause of the error.

In the example Verify JWT policy shown above, the `<Claim>` name is specified as `iss` under the `<AdditionalClaims>` element, resulting in the error:
         
         Invalid name for additional claim : policy(JWT-Verify-RS256) claim(iss).
         




### Resolution

Do not use any of the registered names "kid", "iss", "sub", "aud", "iat", "exp", "nbf" or "jti" in the child element `<Claim>` of the `<AdditionalClaims>` element.

To correct the issue with the example Verify JWT policy, change the claim name to `status`:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='status' type='string'>Development</Claim>
        </AdditionalClaims>
    </VerifyJWT>
    

## InvalidTypeForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid type for additional claim : policy(policy_name) claim(claim_name) type(type_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid type for additional claim : policy(JWT-Verify-RS256) claim(claim) type(integer).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid type for additional claim error messsage.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidTypeForAdditionalClaim-VerifyJWT-error.png)

### Cause

The type of the claim used in the child element `<Claim>` of the `<AdditionalClaims>` element of the VerifyJWT policy is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

For example, using the claim type `integer` under the `<AdditionalClaims>` element will result in the error.

### Diagnosis

  1. Identify the name of the Verify JWT policy, the claim name and the type from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256`, the claim name is `claim`, and the type is `integer:`
         
         Invalid type for additional claim : policy(JWT-Verify-RS256) claim(claim) type(integer).
         

  2. Verify that the claim name and the type used under the `<AdditionalClaims>` element in the failed Verify JWT policy XML matches the claim name and type identified in the error message in Step 1. For example, the following policy specifies the claim as `claim` and the type as `integer`, which matches what's in the error message:
         
         <VerifyJWT name="JWT-Verify-RS256">
           <DisplayName>JWT Verify RS256</DisplayName>
           <Algorithm>RS256</Algorithm>
          <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
           <SecretKey>
               <Value ref="private.secretkey"/>
               <Id>1918290</Id>
           </SecretKey>
           <ExpiresIn>1h</ExpiresIn>
           <Subject>monty-pythons-flying-circus</Subject>
           <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
           <Audience>fans</Audience>
           <Id/>
           <AdditionalClaims>
               <Claim name='claim' ref='reqclaim' type='integer'/>
           </AdditionalClaims>
         </VerifyJWT>
         

  3. If the claim type used in the child element `<Claim>` of the `<AdditionalClaims>` element is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

then that's the cause of the error.

In the example Verify JWT policy shown above, the `<Claim>` type is specified as `integer` under the `<AdditionalClaims>` element. Because `integer` is not a supported type, you get the error:
         
         Invalid type for additional claim : policy(JWT-Verify-RS256) claim(claim) type(integer).
         




### Resolution

Ensure that only the supported data types `string` (default), `number`, `boolean`, or `map` are used in the child element `<Claim>` of the `<AdditionalClaims>` element.

To correct the example Verify JWT policy, change the claim type to `boolean`:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalClaims>
    </VerifyJWT>
    

## MissingNameForAdditionalClaim

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Error occurred while validation of bean(policy_name.xml) Reason: - Required attribute name is missing in Claim.

### Example error message
    
    
    Error Saving Revision 2
    Error occurred while validation of bean JWT-Verify-RS256.xml. Reason: - Required attribute name is missing in Claim
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Attribute name is missing in claim error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/MissingNameForAdditionalClaim-VerifyJWT-error.png)

### Cause

This error occurs if the name of the claim is not specified in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element.

### Diagnosis

  1. Identify the name of the Verify JWT policy from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256`:
         
         Error occurred while validation of bean JWT-Verify-RS256.xml. Reason: - Required attribute name is missing in Claim
         

  2. Examine the failed Verify JWT policy XML and verify that the claim name is missing in the child element `<Claims>` under the `<AdditionalClaims>` or `<AdditionalHeaders>` element. For example, the following Verify JWT policy does not specify the claim name under the `<AdditionalClaims>` element:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim ref='reqclaim' type='boolean'/>
             </AdditionalClaims>
         </VerifyJWT>
         

Because the `<Claim>` name is not specified under the `<AdditionalClaims>` element you get the error:
         
         Error occurred while validation of bean JWT-Verify-RS256.xml. Reason: - Required attribute name is missing in Claim
         




### Resolution

Ensure that the name of the claim is always specified in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>`element.

To correct the example Verify JWT policy, specify the claim name as shown below:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalClaims>
    </VerifyJWT>
    

## InvalidNameForAdditionalHeader

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid name for additional header : policy(policy_name)header(header_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid name for additional header: policy(JWT-Verify-RS256) header(alg).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid name for additional header error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidNameForAdditionalHeader-VerifyJWT-error.png)

### Cause

This error occurs if the name of the claim used in the child element `<Claim>` of the `<AdditionalHeaders>` element is one of the following standard JWT headers:

`alg` or `typ`

For example, using the claim name `alg` under the `<AdditionalHeaders>` element will cause the error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and header name from the error message. For example, in the following error message, the name of Verify JWT policy is `JWT-Verify-RS256` and header name is `alg`:
         
         Invalid name for additional header: policy(JWT-Verify-RS256) header(alg).
         

  2. Verify that the header name used in the child element `<Claim>` under the `<AdditionalHeaders>` element in the failed Verify JWT policy XML matches the header name identified in the error message in Step 1. For example, the following policy specifies the header as `alg`, which matches what's in the error message:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalHeaders>
                 <Claim name="alg"/>
             </AdditionalHeaders>
         </VerifyJWT>
         

  3. If the header name used in the child element `<Claim>`of the `<AdditionalClaims>` element is one of the following standard JWT headers:

`alg` or `typ`

then that's the cause of the error.

In the example Verify JWT policy shown above, the `<Claim>` name is specified as `alg` under the `<AdditionalClaims>` element, resulting in the error:
         
         Invalid name for additional header: policy(JWT-Verify-RS256) header(alg).
         




### Resolution

Do not use the standard JWT headers `alg` or `typ` in the child element `<Claim>` of the `<AdditionalHeaders>` element.

To correct the example Verify JWT policy, use the name `x5c` in the child element `<Claim>` of the `<AdditionalHeaders>` element:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='x5c'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidTypeForAdditionalHeader

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid type for additional header : policy(policy_name) claim(claim_name) type(type_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid type for additional header : policy(JWT-Verify-RS256) claim(claim1) type(integer).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid type for additional header error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidTypeForAdditionalHeader-VerifyJWT-error.png)

### Cause

The error will occur if the type of claim used in the child element `<Claim>` of the `<AdditionalHeaders>` element of the Verify JWT policy is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

For example, using the claim type `integer` under the `<AdditionalHeaders>` element will cause the error.

### Diagnosis

  1. Identify the name of the Verify JWT policy, claim name and the type from the error message. For example, in the following error message, the name of Verify JWT policy is `JWT-Verify-RS256`, the claim name is `claim` and the type is `integer`:
         
         Invalid type for additional header : policy(JWT-Verify-RS256) claim(claim) type(integer).
         

  2. Verify that the claim name and the type used under the `<AdditionalClaims>` element in the failed Verify JWT policy XML matches the claim name and type identified in the error message in Step 1. For example, the following policy specifies the claim as `claim` and the claim type as `integer,` which matches what's in the error message:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalHeaders>
                 <Claim name='claim' ref='reqclaim' type='integer'/>
             </AdditionalHeaders>
         </VerifyJWT>
         

  3. If the claim type used in the child element `<Claim>` of the `<AdditionalHeaders>` element is not one of the following types:

`string` (default), `number`, `boolean`, or `map`

then that's the cause of the error.

In the example Verify JWT policy shown above, the `<Claim>` type under the `<AdditionalHeaders>` element is specified as `integer`. Because `integer` is not a supported type, you get the error:
         
         Invalid type for additional header : policy(JWT-Verify-RS256) claim(claim) type(integer).
         




### Resolution

Ensure that only the supported data types `string`, `number`, `boolean`, or `map` are used in the child element `<Claim>` of the `<AdditionalHeaders>` element.

To correct the example Verify JWT policy, change the claim type to `boolean`:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='boolean'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidValueOfArrayAttribute

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid value for array attribute: policy(policy_name)claim(claim_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid value for array attribute: policy(JWT-Verify-RS256) claim(claim).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid value for array attribute error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidValueOfArrayAttribute-VerifyJWT-error.png)

### Cause

This error occurs if the value of the array attribute in the in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element is not set to `true` or `false`.

For example, setting the value of the array attribute as `yes` in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` element causes the error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and claim name from the error message. For example, in the following error message, the name of Verify JWT policy is `JWT-Verify-RS256` and claim name is `claim`:
         
         Invalid value for array attribute: policy(JWT-Verify-RS256) claim(claim).
         

  2. Verify that the claim name used in the child element `<Claim>` under the `<AdditionalHeaders>` element in the failed Verify JWT policy XML matches the claim name identified in the error message in Step 1. For example, the following policy specifies the claim name as `claim`, which matches what's in the error message:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='yes'/>
             </AdditionalClaims>
         </VerifyJWT>
         

  3. If the value of the `array` attribute in the child element `<Claim>` of the `<AdditionalClaims>` element is not set to `true` or `false`, then that's the cause of the error.

Because the `array` attribute in the child element `<Claim>` of the `<AdditionalClaims>` element is set to `yes` in the example above, you get the error:
         
         Invalid value for array attribute: policy(JWT-Verify-RS256) claim(claim).
         




### Resolution

Ensure that the value of the array attribute in the child element `<Claim>` of the `<AdditionalClaims>` or `<AdditionalHeaders>` elements is set to `true` or `false`.

To correct the example Verify JWT policy shown above, change the value of array attribute to `true`:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidValueForElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision
    Invalid Value for element : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision
    Invalid Value for element : policy(JWT-Verify-RS256) element(Algorithm).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid value for element error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidValueForElement-VerifyJWT-error.png)

### Cause

This error occurs if the value specified in the `<Algorithm>` element is not one of the following values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

For example, specifying the algorithm value as `RS128` in the `<Algorithm>` element leads to this error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and element name from the error message. For example, in the following error message, the name of Verify JWT policy is `JWT-Verify-RS256` and the element name is `Algorithm`:
         
         Invalid Value for element : policy(JWT-Verify-RS256) element(Algorithm).
         

  2. Examine the failed Verify JWT policy XML and check the value specified for the `<Algorithm>` element.

Here's a sample Verify JWT policy:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS128</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id>1918290</Id>
             </SecretKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='status' type='string'>Development</Claim>
             </AdditionalClaims>
         </VerifyJWT>
         

  3. Examine the value specified in the `<Algorithm>` element. If it is not one of the following values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

then that's the cause of the error.

In the example Verify JWT policy shown above, the `<Algorithm>` name is specified as `HS128`. Because this is not a supported algorithm, you get the error:
         
         Invalid Value for element : policy(JWT-Verify-RS256) element(Algorithm).
         




### Resolution

Ensure that the value specified in the `<Algorithm>` element is one of the supported values:

`HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`

To correct the example Verify JWT policy shown above, which uses the `<SecretKey>` element, change the value of the `<Algorithm>` to `HS25`. Note, when the `<SecretKey>` element is used, you can only use HS Family algorithms.
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref="private.secretkey"/>
            <Id>1918290</Id>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalClaims>
            <Claim name='status' type='string'>Development</Claim>
        </AdditionalClaims>
    </VerifyJWT>
    

## MissingConfigurationElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision
    Missing configuration element : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision
    Missing configuration element : policy(JWT-Verify-RS256) element(PublicKey).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Missing configuration element error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/MissingConfigurationElement-VerifyJWT-error.png)

### Cause

This error occurs when the `<PublicKey>` element is **not** used with RSA Family algorithms in the Verify JWT policy. Likewise, the error can occur if the `<SecretKey>` element is **not** used with HS Family algorithms in the Verify JWT policy.

For example, not using the `<PublicKey>` element with RSA Family algorithms leads to this error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and missing element name from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256` and the missing element name is `PublicKey`:
         
         Missing configuration element : policy(JWT-Verify-RS256) element(PublicKey).
         

  2. Examine the failed Verify JWT policy XML and verify that the element indicated in the error message is missing. If it is missing, then that's the cause of the error.

For example, the following policy shows that the `PublicKey` is missing and the `Algorithm` used is `RS256`:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </VerifyJWT>
         

The example Verify JWT policy uses HS Family algorithms, but the mandatory element `PublicKey` is missing, resulting in the error:
         
         Missing configuration element : policy(JWT-Verify-RS256) element(PublicKey).
         




### Resolution

Ensure that the mandatory `<PublicKey>` element is used with RSA Family algorithms and the mandatory `<SecretKey>` element is used with HS Family algorithms.

To correct the example Verify JWT policy shown above, which uses the RS256 algorithm, add the `<PublicKey>` element to the VerifyJWT policy:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Algorithm>RS256</Algorithm>
        <PublicKey>
          <Value ref="public.publickey"/>
        </PublicKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidKeyConfiguration

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 
    Invalid Key configuration : policy(policy_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid Key configuration : policy(JWT-Verify-RS256).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid key configuration error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidKeyConfiguration-VerifyJWT-error.png)

### Cause

This error occurs if the child element `<Value>` or the mandatory child element `<JWKS>` is not defined in the `<PublicKey>` or `<SecretKey>` elements of the Verify JWT policy.

### Diagnosis

  1. Identify the name of the Verify JWT policy from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256`:
         
         Invalid Key configuration : policy(JWT-Verify-RS256).
         
         

  2. Examine the failed Verify JWT policy XML and verify if the child element `<Value>` or the child element `<JWKS>` is not defined in the `<PublicKey>` or `<SecretKey>` elements. If the child element is not defined, then that's the cause of the error.

For example, the following policy shows that the child element `<Value>` or `<JWKS>` is not defined in the `<PublicKey>` element:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <PublicKey>
             </PublicKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </VerifyJWT>
         

Because the child element `<Value>` or `<JWKS>`is not defined in the `<PublicKey>`element of the Verify JWT policy, you get the error:
         
         Invalid Key configuration : policy(JWT-Verify-RS256).
         




### Resolution

Ensure that the child element `<Value>` or `<JWKS>` is always defined in the `<PublicKey>` element of the Verify JWT policy.

To correct the example Verify JWT policy, define the child element `<Value>` or `<JWKS>` under the `<PublicKey>` element as shown below:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <PublicKey>
            <Value ref="public.publickey"/>
        </PublicKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </PublicJWT>
    

## EmptyElementForKeyConfiguration

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Empty Element for Key Configuration : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Empty Element for Key Configuration : policy(JWT-Verify-RS256) element(PublicKey/Value).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Empty element for key configuration error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/EmptyElementForKeyConfiguration-VerifyJWT-error.png)

### Cause

This error occurs if the ref attribute in the child element `<Value>` or `<JWKS>` of the `<PublicKey>` element is not specified or empty.

For example, if the child element `<Value>` of the `<PublicKey>` element is empty, then the error occurs.

### Diagnosis

  1. Identify the name of the Verify JWT policy and element name which is empty from the error message. For example, in the following error message, the name of Verify JWT policy is `JWT-Verify-RS256` and the element name is `PublicKey/Value`:
         
         Empty Element for Key Configuration : policy(JWT-Verify-RS256) element(PublicKey/Value).
         

  2. Examine the failed Verify JWT policy XML and verify that the element identified in Step 1 is empty. If it is empty, then that's the cause of the error.

For example, the following policy shows that the child element `<Value>` of the `<PublicKey>` element is empty:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <PublicKey>
                 <Value/>
             </PublicKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </VerifyJWT>
         

Because the child element `<Value>` of the `<PublicKey>` element of the Verify JWT policy is empty, you get the error:
         
         Empty Element for Key Configuration : policy(JWT-Verify-RS256) element(PublicKey/Value).
         
         




### Resolution

Ensure that the ref attribute in the child element `<Value>` or `<JWKS>` of the `<PublicKey>` element is always specified.

To correct the example Verify JWT policy, use the flow variable `public.publickey` in the child element `<Value>` of the `<PublicKey>` element:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <PublicKey>
            <Value ref="public.publickey"/>
        </PublicKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidConfigurationForVerify

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid configuration element for verify : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 3
    Invalid configuration element for verify : policy(JWT-Verify-HS256) element(SecretKey/Id).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid configuration element for verify error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidConfigurationForVerify-VerifyJWT-error.png)

### Cause

This error occurs if the element `<Id>` is defined within the `<SecretKey>` element of a VerifyJWT policy.

For example, if the element `<Id>` is defined in the `<SecretKey>` element, this error occurs.

### Diagnosis

  1. Identify the name of the Verify JWT policy and the invalid element name from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256` and the element name is `SecretKey/Id`:
         
         Invalid configuration element for verify : policy(JWT-Verify-HS256) element(SecretKey/Id)
         

  2. Examine the failed Verify JWT policy XML and verify that the invalid element identified in Step 1 is defined. If it is defined, then that's the cause of the error.

For example, the following policy shows that the child element `<Id>` of the `<SecretKey>` element is defined:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <SecretKey>
                 <Value ref="private.secretkey"/>
                 <Id/>
             </SecretKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </VerifyJWT>
         

Because the element `<Id>` is defined within the `<SecretKey>` element of the Verify JWT policy, you get the error:
         
         Invalid configuration element for verify : policy(JWT-Verify-HS256) element(SecretKey/Id)
         




### Resolution

Ensure that the element `<Id>` is never defined within the `<SecretKey>` element of a Verify JWT policy.

To correct the example Verify JWT policy, remove the child element `<Id>` from the `<SecretKey>` element:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <SecretKey>
            <Value ref='private.secretkey'/>
        </SecretKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidEmptyElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision 
    Invalid empty element : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 3
    Invalid empty element : policy(JWT-Verify-HS256) element(Source).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid empty element error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidEmptyElement-VerifyJWT-error.png)

### Cause

This error occurs if the `<Source>` element of the Verify JWT policy is empty. If present, it must be defined with a flow variable name.

### Diagnosis

  1. Identify the name of the Verify JWT policy and the empty element name from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256` and the element name is `PublicKey/Value`:
         
         Invalid empty element : policy(JWT-Verify-HS256) element(Source).
         

  2. Examine the failed Verify JWT policy XML and verify that the element identified in Step 1 is empty. If it is empty, then that's the cause of the error.

For example, the following policy shows that the element `<Source>` is empty:
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <ExpiresIn>1h</ExpiresIn>
             <Source></Source>
             <PublicKey>
                 <Value ref="public.publickey"/>
             </PublicKey>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
             <AdditionalClaims>
                 <Claim name='claim' ref='reqclaim' type='string' array='true'/>
             </AdditionalClaims>
         </VerifyJWT>
         

Because the `<Source>` element of the Verify JWT policy is empty, you get the error:
         
         Invalid empty element : policy(JWT-Verify-HS256) element(Source).
         




### Resolution

If the `<Source>` element of a Verify JWT policy is present, ensure that it specifies a flow variable.

To correct the example Verify JWT policy, use a valid flow variable in the `<Source>` element:
    
    
    <VerifyJWT name="JWT-Verify-RS256">
        <DisplayName>JWT Verify RS256</DisplayName>
        <Algorithm>RS256</Algorithm>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <Source>jwt-variable</Source>
        <PublicKey>
            <Value ref="public.publickey"/>
        </PublicKey>
        <ExpiresIn>1h</ExpiresIn>
        <Subject>monty-pythons-flying-circus</Subject>
        <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
        <Audience>fans</Audience>
        <Id/>
        <AdditionalHeaders>
            <Claim name='claim' ref='reqclaim' type='string' array='true'/>
        </AdditionalHeaders>
    </VerifyJWT>
    

## InvalidPublicKeyValue

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid Public Key Value in Configuration : policy(policy_name) element(element_name).

### Example error message
    
    
    Error Saving Revision 2
    Invalid Public Key Value in Configuration : policy(JWT-Verify-RS256) element(PublicKey/JWKS).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid public key value in configuration error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidPublicKeyValue-VerifyJWT-error.png)

### Cause

This error occurs if the value used in the child element `<JWKS>` of the `<PublicKey>` element is not in a valid format as specified in [RFC 7517](https://tools.ietf.org/html/rfc7517).

For example, using `abc` as the value of the child element `<JWKS>` under the `<PublicKey>` element will lead to this error.

### Diagnosis

  1. Identify the name of the Verify JWT policy and element name containing an invalid value from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-RS256` and the element is `PublicKey/JWKS`:
         
         Invalid Public Key Value in Configuration : policy(JWT-Verify-RS256) element(PublicKey/JWKS).
         

  2. Examine the failed Verify JWT policy XML and verify that the element identified in Step 1 contains a value in a valid format as per [RFC 7517](https://tools.ietf.org/html/rfc7517). If the value of the element is not in valid format, then that's the cause of the error.
         
         <VerifyJWT name="JWT-Verify-RS256">
             <DisplayName>JWT Verify RS256</DisplayName>
             <Algorithm>RS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <PublicKey>
                 <JWKS>abc<JWKS>
             </PublicKey>
             <ExpiresIn>1h</ExpiresIn>
             <Subject>monty-pythons-flying-circus</Subject>
             <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
             <Audience>fans</Audience>
             <Id/>
         </VerifyJWT>
         

Because the value in the child element `<JWKS>` of the `<PublicKey>` element is not in a valid format per [RFC 7517](https://tools.ietf.org/html/rfc7517), you get the error:
         
         Invalid Public Key Value in Configuration : policy(JWT-Verify-RS256) element(PublicKey/JWKS).
         




### Resolution

Ensure that the value specified in the child element `<JWKS>` of the `<PublicKey>` element is a valid string or flow variable in a valid JWKS format ([RFC 7517](https://tools.ietf.org/html/rfc7517)).

To correct the example Verify JWT policy, change the value of `<JWKS>` as shown below:
    
    
        <VerifyJWT name="JWT-Verify-RS256">
            <DisplayName>JWT Verify RS256</DisplayName>
            <Algorithm>RS256</Algorithm>
            <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
            <PublicKey>
            <JWKS>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM</JWKS>
            </PublicKey>
            <ExpiresIn>1h</ExpiresIn>
            <Subject>monty-pythons-flying-circus</Subject>
            <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
            <Audience>fans</Audience>
            <Id/>
        </VerifyJWT>
    

## InvalidConfigurationForActionAndAlgorithm

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision <var>revision_number</var>
    Invalid configuration element for this action and algorithm Family: policy(<var>policy_name</var>) element(<var>element_name</var>) action(<var>action_name</var>) family(<var>family_name</var>).
    

### Example error message
    
    
    Error Saving Revision
    Invalid configuration element for this action and algorithm Family: policy(JWT-Verify-HS256) element(PublicKey) action(Verify) family(RSA).
    

### Example screenshot

In the Apigee UI, you will see a dialog with an error:

![Invalid configuration element for this action and algorithm error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/InvalidConfigurationForActionAndAlgorithm-VerifyJWT-error.png)

### Cause

This error occurs if the `<PublicKey>` element is used with HS Family algorithms and the `<SecretKey>` element is used with RSA Family algorithms. The error will also occur if _either_ of these conditions are true.

For example, using the `<PublicKey>` element with HS Family algorithms leads to this error.

### Diagnosis

  1. Identify the name of the Verify JWT policy, the element name and the algorithm family name from the error message. For example, in the following error message, the name of the Verify JWT policy is `JWT-Verify-HS256`, the element name is `PublicKey` and the algorithm family is `RSA`:
         
         Invalid configuration element for this action and algorithm Family: policy(JWT-Verify-HS256) element(PublicKey) action(Verify) family(RSA).
         

  2. Verify that the element and the algorithm family used in the failed Verify JWT policy XML matches the element and the algorithm family identified in the error message in Step 1. For example, the following policy specifies the element as `PublicKey` and the algorithm family as `HMAC`, which matches what's in the error message
         
         <VerifyJWT name="JWT-Verify-HS256">
             <DisplayName>JWT Verify HS256</DisplayName>
             <Algorithm>HS256</Algorithm>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
             <Source>request.formparam.jwt</Source>
             <PublicKey>
                 <Value ref="var-value"/>
             </PublicKey>
             <SecretKey>
                 <Value ref="private.secretkey"/>
             </SecretKey>
                 <ExpiresIn>1h</ExpiresIn>
                 <Subject>monty-pythons-flying-circus</Subject>
                 <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
                 <Audience>fans</Audience>
             </VerifyJWT>
         

  3. If the value of the `<Algorithm>` element is `HS256`, but you have used `<PublicKey>` then that's the cause of the error.

In the example Verify JWT policy shown above, the `<PublicKey>` element is used even though the `<Algorithm>` is set to a family algorithm HS256, resulting in the error:
         
         Invalid configuration element for this action and algorithm Family: policy(JWT-Verify-HS256) element(PublicKey) action(Verify) family(RSA).
         




### Resolution

Ensure that the `<PublicKey>` element is used only with RSA Family algorithms and the `<SecretKey>` element is used only with HS Family algorithms.

To correct the example Verify JWT policy, use the `<SecretKey>` from the VerifyJWT policy that uses the HS256 algorithm:
    
    
        <VerifyJWT name="JWT-Verify-HS256">
            <DisplayName>JWT Verify HS256</DisplayName>
            <Algorithm>HS256</Algorithm>
            <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
            <Source>request.formparam.jwt</Source>
            <SecretKey>
            <Value ref="private.secretkey"/>
        </SecretKey>
            <ExpiresIn>1h</ExpiresIn>
            <Subject>monty-pythons-flying-circus</Subject>
            <Issuer>urn://apigee-edge-JWT-policy-test</Issuer>
            <Audience>fans</Audience>
        </VerifyJWT>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
