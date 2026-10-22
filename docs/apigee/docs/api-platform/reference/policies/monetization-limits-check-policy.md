---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy/
title: MonetizationLimitsCheck policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:06.296899+00:00
---

# MonetizationLimitsCheck policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  MonetizationLimitsCheck policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note** : The MonetizationLimitsCheck policy is valid only if you have [enabled Apigee monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable) in your organization.

The MonetizationLimitsCheck policy enables you to enforce monetization limits.

Specifically, the policy is triggered if the app developer accessing the monetized API has not purchased a subscription to the associated API product or if the developer has insufficient balance. In this case, The MonetizationLimitsCheck policy will raise a fault and block an API call. For more information, see [Enforcing developer subscriptions to API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#subscriptions).

When you attach the MonetizationLimitsCheck policy to an API proxy, the `mint.limitscheck.*` and `mint.subscription_*` flow variables are populated, as described in the [mint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) flow variable reference. 

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** In spite of using the MonetizationLimitsCheck policy, it is possible that a prepaid developer will be allowed to make excess API calls and the developer might end up with a negative wallet balance. To understand the conditions under which a developer's balance will become negative, see [Negative developer balance](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-prepaid-balances#negative-bal).

## `<MonetizationLimitsCheck>`

Defines the MonetizationLimitsCheck policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#displayname)  
[`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#ignoreunresolvedvariables)  
  
  
The following table provides a high-level description of the child elements of [`<MonetizationLimitsCheck>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#monetizationlimitscheck): 

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#displayname) | Optional | A custom name for the policy.  
[`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse) | Optional | Defines the response message returned to the requesting client.  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#ignoreunresolvedvariables) | Optional | Ignores any unresolved variable error in the flow.  
  
The `<MonetizationLimitsCheck>` element uses the following syntax:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="no"?><MonetizationLimitsCheck continueOnError="[true|false]" enabled="[true|false]" name="policy_name">
       <DisplayName>POLICY_DISPLAY_NAME</DisplayName>
       <FaultResponse>
            <AssignVariable>
              <Name/>
              <Value/>
            </AssignVariable>
            <Add>
                <Headers/>
            </Add>
            <Copy source="request">
                <Headers/>
                <StatusCode/>
           </Copy>
            <Remove>
                <Headers/>
            </Remove>
            <Set>
                <Headers/>
                <Payload/>
                <StatusCode/>
            </Set>
        </FaultResponse>
        <IgnoreUnresolvedVariables>VALUE</IgnoreUnresolvedVariables>
    </MonetizationLimitsCheck>

### Example

In the following example, if a developer has not purchased subscription to the associated API product, access to the monetized API is blocked, and a `403` status is returned with a custom message.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MonetizationLimitsCheck continueOnError="false" enabled="true" name="MonetizationLimitsCheck-1">
      <DisplayName>Monetization-Limits-Check-1</DisplayName>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <FaultResponse>
        <Set>
          <Payload contentType="text/xml">
            <error>
              <messages>
                <message>Usage has been exceeded ({mint.limitscheck.isRequestBlocked}) or app developer has been suspended</message>
              </messages>
            </error>
          </Payload>
          <StatusCode>403</StatusCode>
        </Set>
      </FaultResponse>
    </MonetizationLimitsCheck>

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
## Child element reference

This section describes the child elements of [`<MonetizationLimitsCheck>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#monetizationlimitscheck). 

### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<FaultResponse>`

Defines the response message returned to the requesting client. FaultResponse uses the same settings as the [`<FaultResponse`>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy#faultresponseelement) element in the RaiseFault policy.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<MonetizationLimitsCheck>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#monetizationlimitscheck)  
  
**Child Elements** |  [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#assignvariable)  
[`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#add)  
[`<Copy>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#copy)  
[`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#remove)  
[`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#set)  
  
  
#### `<AssignVariable>`

Assigns a value to a destination flow variable. If the flow variable does not exist, then `AssignVariable` creates it.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
  
**Child Elements** |  [`<Name>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#name)  
[`<Value>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#value)  
  
  
For example, use the following code to set the variable named `myFaultVar` in the MonetizationLimitsCheck policy:
    
    
    <FaultResponse>
    <AssignVariable>
      <Name>myFaultVar</Name>
      <Value>42</Value>
    </AssignVariable>
    </FaultResponse>

A policy in a fault rule can then access the variable. For example, the following AssignMessage policy uses the variable to set a Header in the fault response:
    
    
    <AssignMessage enabled="true" name="Assign-Message-1">
    <Add>
      <Headers>
        <Header name="newvar">{myFaultVar}</Header>
      </Headers>
    </Add>
    <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    <AssignTo createNew="false" transport="http" type="response"/>
    </AssignMessage>

`<AssignVariable>` in the MonetizationLimitsCheck policy uses the same syntax as the [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable) element in the AssignMessage policy.

##### `<Name>`

Variable name. For more information, see the [Name](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable-name) element in the AssignMessage policy.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#assignvariable)  
  
**Child Elements** |  None   
  
##### `<Value>`

Variable value. For more information, see the [Value](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable-value) element in the AssignMessage policy.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#assignvariable)  
  
**Child Elements** |  None   
  
#### `<Add>`

Adds HTTP headers to the error message. 

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
  
**Child Elements** |  [`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#headers)  
  
  
##### `<Headers>`

Specifies the HTTP header to add, set, copy, or remove.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#add)  
[`<Copy>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#copy)  
[`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#remove)  
[`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#set)  
  
**Child Elements** |  None   
  
  * An empty header (`<Add><Headers/></Add>`) does not add any header.
  * The `<Header>` element supports the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).



Examples:

###### Add header

The following example copies the value of the `request.user.agent` flow variable into the header:
    
    
    <Add>
        <Headers>
            <Header name="user-agent">{request.user.agent}</Header>
        </Headers>
    </Add>

###### Set header

The following example sets the `user-agent` header to the message variable specified with the `<AssignTo>` element.
    
    
    <Set>
        <Headers>
            <Header name="user-agent">{request.header.user-agent}</Header>
        </Headers>
    </Set>

###### Copy header - 1

The following example copies the `headerA` from the request:
    
    
    <Copy source='request'>
        <Headers>
            <Header name="headerA"/>
        </Headers>
    </Copy>

###### Copy header - 2

The following example copies multiple headers:
    
    
    <Copy source='request'>
        <Headers>
          <Header name="h1"/>
          <Header name="h2"/>
          <Header name="h3.2"/>
        </Headers>
    </Copy>

This example copies "h1", "h2", and the second value of "h3". If "h3" has only one value, then "h3" is not copied.

###### Remove header - 1

The following example removes a header:
    
    
    <Remove>
        <Headers>
            <Header name="user-agent"/>
        </Headers>
    </Remove>

###### Remove header - 2

The following example removes multiple headers:
    
    
    <Remove>
        <Headers>
          <Header name="h1"/>
          <Header name="h2"/>
          <Header name="h3.2"/>
        </Headers>
    </Remove>

This example removes "h1", "h2", and the second value of "h3". If "h3" has only one value, then "h3" is not removed.

#### `<Copy>`

Copies information _**from**_ the message specified by the `source` attribute **_to_** the error message.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
  
**Child Elements** |  [`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#headers)  
[`<StatusCode>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#statuscode)  
  
  
The following table describes the attributes of `<Copy>`:

Attribute | Required? | Type | Description  
---|---|---|---  
source | Optional | String |  Specifies the source object of the copy.

  * If source is not specified, it is treated as a simple message. For example, if the policy is in the request flow, then the source defaults to the request object. If the policy is in the response flow, it defaults to the response object. If you omit source, you can use an absolute reference to a flow variable as the source of the copy. For example, specify the value as {request.header.user-agent}.
  * If the source variable cannot be resolved, or resolves to a non-message type, <Copy> fails to respond.

  
  
##### `<StatusCode>`

Specifies the HTTP status code in the error message. You can copy or set the value from for the object specified by the `source` attribute.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<Copy>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#copy)  
[`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#set)  
  
**Child Elements** |  None   
  
Example:

###### Copy status code
    
    
    <Copy source='response'>
        <StatusCode>404</StatusCode>
    </Copy>

###### Set status code
    
    
    <Set source='request'>
        <StatusCode>404</StatusCode>
    </Set>

#### `<Remove>`

Removes specified HTTP headers from the error message. To remove all the headers, specify `<Remove><Headers/></Remove>`.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
  
**Child Elements** |  [`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#headers)  
  
  
#### `<Set>`

Sets information in the error message.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<FaultResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#faultresponse)  
  
**Child Elements** |  [`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#headers)  
[`<Payload>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#payload)  
[`<StatusCode>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#statuscode)  
  
  
##### `<Payload>`

Sets the payload of the error message.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#set)  
  
**Child Elements** |  None   
  
Examples:

###### Set text payload
    
    
    <Set>
        <Payload contentType="text/plain">test1234</Payload>
    </Set>

###### Set JSON payload - 1
    
    
    <Set>
        <Payload contentType="application/json">
            {"name":"foo", "type":"bar"}
        </Payload>
    </Set>

###### Set JSON payload - 2
    
    
    <Set>
        <Payload contentType="application/json" variablePrefix="@" variableSuffix="#">
            {"name":"foo", "type":"@variable_name#"}
        </Payload>
    </Set>

This example inserts variables using the `variablePrefix` and `variableSuffix` attributes with delimiter characters.

###### Set JSON payload - 3
    
    
    <Set>
        <Payload contentType="application/json">
            {"name":"foo", "type":"{variable_name}"}
        </Payload>
    </Set>

This example inserts variables using curly braces. You can use curly braces starting with the 16.08.17 release.

###### Set XML payload
    
    
    <Set>
        <Payload contentType="text/xml">
            <root>
              <e1>sunday</e1>
              <e2>funday</e2>
              <e3>{var1}</e3>
        </Payload>
    </Set>

This example inserts variables using curly braces. You can use curly braces starting with the 16.08.17 release.

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when an unresolved variable is encountered.

Set to `true` to ignore unresolved variables and continue processing; otherwise `false`. The default value is `true`.

Setting `<IgnoreUnresolvedVariables>` to `true` is different from setting the [`<MonetizationLimitsCheck>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy#monetizationlimitscheck)'s `continueOnError` to `true`. If you set `continueOnError` to `true`, Apigee ignores all errors, not only errors in variables.

The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
    <IgnoreUnresolvedVariables>[true|false]</IgnoreUnresolvedVariables>

### Example

The following example sets `<IgnoreUnresolvedVariables>` to `false`:
    
    
    <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`mint.service.subscription_not_found_for_developer` | `500` | This error occurs when a developer does not have a subscription to the API Product.  
`mint.service.wallet_not_found_for_developer` | `500` | This error occurs when a prepaid developer attempts to consume a monetized API without maintaining a wallet for the currency specified in rate plan.  
`mint.service.developer_usage_exceeds_balance` | `500` | This error occurs when a prepaid developer's usage exceeds the wallet balance.  
`mint.service.wallet_blocked_due_to_inactivity` | `500` | This error occurs when a prepaid developer's wallet is not topped up in over 1.5 years and the developer attempts to consume an API.  
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful.

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

Variables | Where | Example  
---|---|---  
`fault.name` | The `fault.name` can match to any of the faults listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`MonetizationLimitsCheck.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `MonetizationLimitsCheck.monetization-limits-check-1.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors)

## Flow variables

The following predefined flow variables automatically populate when the MonetizationLimitsCheck policy executes. For more information, see the [mint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) flow variables. 

Flow variable | Description | `mint.limitscheck.is_request_blocked` | `true` for blocked requests.  
---|---  
`mint.limitscheck.is_subscription_found` | `true` if an API subscription is found.  
`mint.limitscheck.purchased_product_name` | Name of the purchased API product. For example: `MyProduct`.  
`mint.limitscheck.status_message` | Status message. These values can be returned:  


  * `limits_check_success` \- Successful limits check.
  * `apiproduct_name_and_developer_email_not_available` \- Unable to determine the API developer or the API product name in order to perform limits check.
  * `apiproduct_name_not_available` \- Unable to determine the API product name in order to perform limits check.
  * `developer_email_not_available` \- Unable to determine the API developer email in order to perform limits check.
  * `developer_usage_exceeds_balance` \- Prepaid developer balance is too low.
  * `rateplan_not_available` \- API product with no rate plan, no fault.
  * `subscription_not_available` \- API developer that owns the app does not have a subscription.
  * `wallet_disabled_due_to_inactivity` \- The developer has not used their wallet for over a year. A top-up of at least one unit (in dollars, this would be $0.01) will reactivate it.
  * `wallet_not_found` \- The developer does not have a wallet. This may happen when no top-up has been executed for that developer.

  
`mint.subscription_end_time_ms` | End time of the API product subscription.  
`mint.subscription_start_time_ms` | Start time of the API product subscription. For example: `1618433956209`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
