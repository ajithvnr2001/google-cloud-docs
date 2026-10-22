---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy/
title: GetOAuthV2Info policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:37.093584+00:00
---

# GetOAuthV2Info policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  GetOAuthV2Info policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The GetOAuthV2Info policy gets attributes of access tokens, refresh tokens, authorization codes, and client app attributes and populates variables with the values of those attributes.

This policy is useful when you need to configure dynamic, conditional behavior based on a value in a token or auth code. Whenever token validation occurs, variables are automatically populated with the values of token attributes. However, in cases where token validation has not occurred, you can use this feature to explicitly populate variables with the attribute values of a token. See also [Customizing Tokens and Authorization Codes](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/customizing-access-tokens).

An access token that you pass to this policy must be valid or the policy will throw an `invalid_access_token` error.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** The resource path that is used to call a proxy with this policy must be included in the Product that was used to generate the original token. In other words, if you call the proxy with the path `/tokeninfo`, then the `/tokeninfo` resource path must be included in the Product that was used to generate the token. If not, you will receive an `InvalidAPICallAsNoApiProductMatchFound` error. 

For more information, see [ GetOAuthV2Info fails if token generated using product with resource paths](https://discuss.google.dev/t/getoauthv2info-fails-if-token-generated-using-product-with-resource-paths/14695) in the [Apigee Community](https://discuss.google.dev/).

## Samples

The following samples use the Get OAuth V2 Info policy to retrieve information about various components of the OAuth2 workflow and then then access that information within code.

### Access token

To get a reference to an access token, use the `<AccessToken>` element in your policy.

The following example expects to find the access token in a query parameter named "access_token" (the actual implementation details are up to you):
    
    
    <GetOAuthV2Info name="MyTokenAttrsPolicy">
      <AccessToken ref="request.queryparam.access_token"></AccessToken>
    </GetOAuthV2Info>

Given the access token, the policy looks up the token's profile and populates a set of variables with the profile data.

You can then access the variables using JavaScript or another means. The following example retrieves the scope(s) associated with the access token using JavaScript:
    
    
    var scope = context.getVariable('oauthv2accesstoken.MyTokenAttrsPolicy.scope');

Note that to access those variables in code, you must prefix them with "oauthv2accesstoken". For a complete list of variables available via the access token, see Access token variables.

### Auth code

To get authorization code attributes, use the `<AuthorizationCode>` element in your policy.

The following example expects to find the access token in a form parameter named "code" (the actual implementation details are up to you):
    
    
    <GetOAuthV2Info name="MyAuthCodeAttrsPolicy">
      <AuthorizationCode ref="request.formparam.code"></AuthorizationCode>
    </GetOAuthV2Info>

Given the auth code, the policy looks up the code's information and populates a set of variables with the auth code data.

You can then access the variables using JavaScript or another means. The following example retrieves a custom attribute associated with the authorization code using JavaScript:
    
    
    var attr = context.getVariable('oauthv2authcode.MyAuthCodeAttrsPolicy.custom_attribute_name');

Note that to access those variables in code, you must prefix them with "oauthv2authcode". For a complete list of variables available via the auth code, see Authorization code variables.

### Refresh token

To get refresh token attributes, use the `<RefreshToken>` element in your policy.

The following example expects to find the access token in a query parameter named "refresh_token" (the actual implementation details are up to you):
    
    
    <GetOAuthV2Info name="MyRefreshTokenAttrsPolicy">
      <RefreshToken ref="request.queryparam.refresh_token"/>
    </GetOAuthV2Info>

Given the refresh token, the policy looks up the refresh token's information and populates a set of variables with the refresh token data.

You can then access those variables using JavaScript or another means. The following example retrieves a custom attribute associated with the refresh token using JavaScript:
    
    
    var attr = context.getVariable('oauthv2refreshtoken.MyRefreshTokenAttrsPolicy.accesstoken.custom_attribute_name');

Note that to access the variables in code, you must prefix them with "oauthv2refreshtoken". For a complete list of variables available via the refresh token, see Refresh token variables.

### Static

In some rare cases you may need to get the profile of a statically configured token (one that is not accessible through a variable). You can do this by providing the value of the access token as an element.
    
    
    <GetOAuthV2Info name="GetTokenAttributes">
      <AccessToken>shTUmeI1geSKin0TODcGLXBNe9vp</AccessToken>
    </GetOAuthV2Info>

You can do this with all other token types (client ID, authorization code, and refresh tokens) as well.

### Client ID

This example shows how to retrieve information about the client app using the client ID. Upon execution, the policy populates a set of variables with client information. In this case, the policy expects to find the client ID in a query parameter called `client_id`. Given the client ID, the policy looks up the client's profile and populates a set of variables with the profile data. The variables will be prefixed with `oauthv2client. `
    
    
    <GetOAuthV2Info name="GetClientAttributes">
      <ClientId ref="request.queryparam.client_id"></ClientId>
    </GetOAuthV2Info>

You can then access the variables using JavaScript or another means. For example, to get the developer app name and developer email associated with the client app using JavaScript:
    
    
    context.getVariable("oauthv2client.GetClientAttributes.developer.email");
    context.getVariable("oauthv2client.GetClientAttributes.developer.app.name");

* * *

## Element Reference

The element reference describes the elements and attributes of the GetOAuthV2Info policy.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <GetOAuthV2Info async="false" continueOnError="false" enabled="true" name="GetOAuthV2Info-1"
        <DisplayName>Get OAuth v2.0 Info 1</DisplayName>
        <AccessToken ref="variable"></AccessToken>
        <AuthorizationCode ref="variable"></AuthorizationCode>
        <ClientId ref="variable"></ClientId>
        <RefreshToken ref="variable"></RefreshToken>
    </GetOAuthV2Info>

## <GetOAuthV2Info> attributes
    
    
    <GetOAuthV2Info async="false" continueOnError="false" enabled="true" name="Get-OAuth-v20-Info-1">

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <AccessToken> element

Retrieves the profile for an access token. You pass in a either a variable that contains the access token string or a literal token string (rare case). In this example, the access token is retrieved from a query parameter passed in a request. Use the <IgnoreAccessTokenStatus> element if you want to return information for a revoked or expired token.
    
    
    <AccessToken ref="request.queryparam.access_token"></AccessToken>

**Default:** |  request.formparam.access_token (a x-www-form-urlencoded and specified in the request body)  
---|---  
**Presence:** |  Optional  
**Type:** | String  
**Valid values:** |  Either a flow variable containing an access token string, or a literal string.  
  


## <AuthorizationCode> element

Retrieves the profile for an authorization code. You pass in a either a variable that contains the auth code string or a literal token string (rare case). In this example, the auth code is retrieved from a query parameter passed in a request. For a list of variables populated by this operation, see "Flow variables". 
    
    
    <AuthorizationCode ref="request.queryparam.authorization_code"></AuthorizationCode>

**Default:** |  request.formparam.access_token (a x-www-form-urlencoded and specified in the request body)  
---|---  
**Presence:** |  Optional  
**Type:** | String  
**Valid values:** |  Either a flow variable containing an auth code string, or a literal string.  
  
## <ClientId> element

Retrieves information related to a client ID. In this example, the client ID is retrieved from a query parameter passed in a request. For a list of variables populated by this operation, see "Flow variables". 
    
    
    <ClientId ref="request.queryparam.client_id"></ClientId>

**Default:** |  request.formparam.access_token (a x-www-form-urlencoded and specified in the request body)  
---|---  
**Presence:** |  Optional  
**Type:** | String  
  
**Valid values:** | Either a flow variable containing an auth code string, or a literal string.  
  
## <IgnoreAccessTokenStatus> element

Returns the token information even if the token is expired or revoked. This element can only be used with access tokens. Information for other entities like refresh tokens and authorization codes are returned regardless of their status, by default.
    
    
    <IgnoreAccessTokenStatus>true</IgnoreAccessTokenStatus>

**Default:** |  false  
---|---  
**Presence:** |  Optional  
**Type:** | Boolean  
  
**Valid values:** | true or false  
  
  
## <RefreshToken> element

Retrieves the profile for a refresh token. You pass in a either a variable that contains the refresh token string or a literal token string (rare case). In this example, the refresh token is retrieved from a query parameter passed in a request. For a list of variables populated by this operation, see "Flow variables". 

**Note:** This element works the same whether you use a refresh token issued with a JWT access token or with a traditional opaque access token.
    
    
    <RefreshToken ref="request.queryparam.refresh_token"></RefreshToken>

**Default:** |  request.formparam.access_token (a x-www-form-urlencoded and specified in the request body)  
---|---  
**Presence:** |  Optional  
**Type:** | String  
**Valid values:** |  Either a flow variable containing an refresh token string, or a literal string.  
  
## Flow variables

The GetOAuthV2Info policy populates these variables, and is typically used in cases where you need the profile data, but where a grant or validation has not occurred yet. .

### Client ID variables

These variables are populated when the ClientId element is set:
    
    
    oauthv2client.{policy_name}.client_id
    oauthv2client.{policy_name}.client_secret
    oauthv2client.{policy_name}.redirection_uris // Note the spelling -- 'redirection_uris'
    oauthv2client.{policy_name}.developer.email
    oauthv2client.{policy_name}.developer.app.name
    oauthv2client.{policy_name}.developer.id
    oauthv2client.{policy_name}.{developer_app_custom_attribute_name}

### Access token variables

These variables are populated when the AccessToken element is set:
    
    
    oauthv2accesstoken.{policy_name}.developer.id
    oauthv2accesstoken.{policy_name}.developer.app.name
    oauthv2accesstoken.{policy_name}.developer.app.id
    oauthv2accesstoken.{policy_name}.developer.email
    
    oauthv2accesstoken.{policy_name}.organization_name
    oauthv2accesstoken.{policy_name}.api_product_list
    
    oauthv2accesstoken.{policy_name}.access_token
    oauthv2accesstoken.{policy_name}.scope
    oauthv2accesstoken.{policy_name}.expires_in //in seconds
    oauthv2accesstoken.{policy_name}.status
    oauthv2accesstoken.{policy_name}.client_id
    oauthv2accesstoken.{policy_name}.accesstoken.{custom_attribute_name}
    
    oauthv2accesstoken.{policy_name}.refresh_token
    oauthv2accesstoken.{policy_name}.refresh_token_status
    oauthv2accesstoken.{policy_name}.refresh_token_expires_in //in seconds
    
    oauthv2accesstoken.{policy_name}.refresh_count
    oauthv2accesstoken.{policy_name}.refresh_token_issued_at
    oauthv2accesstoken.{policy_name}.revoke_reason //Apigee hybrid only with value of REVOKED_BY_APP, REVOKED_BY_ENDUSER, REVOKED_BY_APP_ENDUSER, or TOKEN_REVOKED

### Authorization code variables

These variables are populated when the AuthorizationCode element is set:
    
    
    oauthv2authcode.{policy_name}.code
    oauthv2authcode.{policy_name}.scope
    oauthv2authcode.{policy_name}.redirect_uri
    oauthv2authcode.{policy_name}.client_id
    oauthv2authcode.{policy_name}.{auth_code_custom_attribute_name}

### Refresh token variables

These variables are populated when the RefreshToken element is set:
    
    
    oauthv2refreshtoken.{policy_name}.developer.id
    oauthv2refreshtoken.{policy_name}.developer.app.name
    oauthv2refreshtoken.{policy_name}.developer.app.id
    oauthv2refreshtoken.{policy_name}.developer.email
    oauthv2refreshtoken.{policy_name}.organization_name
    oauthv2refreshtoken.{policy_name}.api_product_list
    
    oauthv2refreshtoken.{policy_name}.access_token
    oauthv2refreshtoken.{policy_name}.scope
    oauthv2refreshtoken.{policy_name}.expires_in //in seconds
    
    oauthv2refreshtoken.{policy_name}.status
    oauthv2refreshtoken.{policy_name}.client_id
    oauthv2refreshtoken.{policy_name}.accesstoken.{custom_attribute_name}
    
    oauthv2refreshtoken.{policy_name}.refresh_token
    oauthv2refreshtoken.{policy_name}.refresh_token_status
    oauthv2refreshtoken.{policy_name}.refresh_token_expires_in //in seconds
    
    oauthv2refreshtoken.{policy_name}.refresh_count
    oauthv2refreshtoken.{policy_name}.refresh_token_issued_at
    oauthv2refreshtoken.{policy_name}.revoke_reason //Apigee hybrid only with value of REVOKED_BY_APP, REVOKED_BY_ENDUSER, REVOKED_BY_APP_ENDUSER, or TOKEN_REVOKED

## Schema

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes. The error names shown below are the strings that are assigned to the `fault.name` variable when an error occurs. See the Fault variables section below for more details.

Fault code | HTTP status | Cause  
---|---|---  
`steps.oauth.v2.access_token_expired` | `500` | The access token sent to the policy is expired.  
`steps.oauth.v2.authorization_code_expired` | `500` | The authorization code sent to the policy is expired.  
`steps.oauth.v2.invalid_access_token` | `500` | The access token sent to the policy is invalid.  
`steps.oauth.v2.invalid_client-invalid_client_id` | `500` | The client ID sent to the policy is invalid.  
`steps.oauth.v2.invalid_refresh_token` | `500` | The refresh token sent to the policy is invalid.  
`steps.oauth.v2.invalid_request-authorization_code_invalid` | `500` | The authorization code sent to the policy is invalid.  
`steps.oauth.v2.InvalidAPICallAsNoApiProductMatchFound` | 401 | Please see [ Oauth2.0 Access Token Verification throws "Invalid API call as no apiproduct match found" error](https://discuss.google.dev/t/oauth2-0-access-token-verification-throws-invalid-api-call-as-no-apiproduct-match-found-error/17064) for information about troubleshooting this error.  
`steps.oauth.v2.refresh_token_expired` | `500` | The refresh token sent to the policy is expired.  
  
### Deployment errors

Refer to the message reported in the UI for information about deployment errors.

### Fault variables

These variables are set when this policy triggers an error at runtime.

**Note:** You an use these variables to create Fault Rule conditions. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "IPDeniedAccess"`  
`oauthV2.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `oauthV2.GetTokenInfo.failed = true`  
`oauthV2.policy_name.fault.name` | policy_name is the user-specified name of the policy that threw the fault. | `oauthV2.GetToKenInfo.fault.name = invalid_client-invalid_client_id`  
`oauthV2.policy_name.fault.cause` | policy_name is the user-specified name of the policy that threw the fault. | `oauthV2.GetTokenInfo.cause = ClientID is Invalid`  
  
### Example error response
    
    
    {  
       "fault":{  
          "faultstring":"ClientId is Invalid",
          "detail":{  
             "errorcode":"keymanagement.service.invalid_client-invalid_client_id"
          }
       }
    }

### Example fault rule
    
    
    <FaultRule name="OAuthV2 Faults">
        <Step>
            <Name>AM-InvalidClientIdResponse</Name>
        </Step>
        <Condition>(fault.name = "invalid_client-invalid_client_id")</Condition>
    </FaultRule>

## Related topics

  * [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy)
  * [OAuth home](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home)
  * [Customizing Tokens and Authorization Codes](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/customizing-access-tokens)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
